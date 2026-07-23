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
Marketing takeaways: The best non-AI play

\- China A/H healthcare index rebounded 16%/11% from its low on 26 June

\- Stronger position backed by solid growth and industry globalisation momentum

◆ Prefer: Wuxi Bio, Pharmaron, Keymed, and Innovent; all Buys

We had over 30 offline client meetings in Singapore, Hong Kong, and Shanghai over the past two weeks. The major investors are changing from specialists to generalists and tech-PMs vs one month ago (Marketing takeaways, 18 June 2026). Key topics:

How to play China healthcare when the AI narrative changes? Innovative drugs, CDMO, AIDD (AI drug discovery), and surgery robotics are among the most discussed topics. Since 26 June, the H/A-share healthcare index has risen $16\% / 11\%$ , outperforming the HSI by 7ppt, and the CSI300 by 19ppt over the same period. The market believes this is due to: (1) the unwinding of AI funds; (2) the inflow of AI/tech/ consumer funds with promising 1H26 results; and (3) rotation to non-AI sectors and positioning healthcare as an aggressive sector with a global story driven by innovation. Global investors are most interested in CDMO and biotech/pharma sectors. Wuxi Apptec is heavily owned given its high expectations for 1H26, while Wuxi Bio/ Pharmaron are preferred for accelerating their growth rate outlook and margin expansion in FY26-28. For biotech/pharmaceuticals, Innovent/Kelun Bio are preferred by both generalists and specialists, given their strong domestic growth and visible global story. Among pharmaceuticals, CSPC and Hansoh are widely discussed for their business development (BD) momentum and valuation breakdown. As such, companies with a global growth story in China's healthcare system are becoming consensus plays when the AI theme is volatile.

What is the key debate for China healthcare – how long will the rally last, and what is next? According to feedback from clients, China healthcare is still largely underweight. Key debates include: (1) uncertainty surrounding domestic policies including biosimilar VBP, medical device VBP, and the repricing of healthcare service fees in public hospitals; (2) AI is back in focus, which could drive capital rotation away from healthcare; and (3) the impact of US Biosecure Act list and bill restricting cross-border biotech BD transactions. Investors think this time the rally relates to value discovery, which is lagging strong 1H26 BD momentum. As a result, the market expects it to last until 31 July or 1 September, until mid-year results. However, because of the impact of the anti-corruption drive, the market lowered its expectations in pharmaceuticals, medical devices, and hospital growth. We believe the next catalysts for China biotech will relate to commercialisation in the US market, ESMO data, and Harmoni 3 data.

Maintain Buy on Wuxi Biologics, Pharmaron, Keymed, and Innovent. We expect robust growth in China's CDMO and biotech industries, supported by an expanding global footprint and strong data readouts from clinical programmes. Moreover, we believe the healthcare innovation industry is in a strong position both in terms of near-term catalysts and long-term potential.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

China

Linda Shu\*, PhD (Reg. No. S1700522120001)
Head of China Healthcare Research
HSBC Qianhai Securities Limited
linda.y.l.shu@hsbcqh.com.cn
+86 755 88983246

Oliver Wang\* (Reg. No. S1700523100003)
Analyst, China Healthcare Research
HSBC Qianhai Securities Limited
oliver.h.y.wang@hsbcqh.com.cn
+86 21 5066 2058

## Cindy Chai\* (Reg. No. S1700523040001)

Analyst, China Healthcare Research

HSBC Qianhai Securities Limited

cindy.x.r.chai@hsbcqh.com.cn

+86 21 5066 2005

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations.

No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: HSBC Qianhai Securities Limited

View HSBC Qianhai Securities at: https://www.research.hsbc.com

## Industry update

Exhibit 1. Y-t-d performance of China Healthcare index  
![](images/25f0dfe856df7fe154e9130068e941011bb54de87340836ca49c88b8a9f53b55.jpg)  
Source: Wind, HSBC Qianhai Securities

Exhibit 2. North Bound Holding and changes

<table><tr><td>North Bound Holding</td><td>2Q26 (%)</td><td>1Q26 (%)</td><td>q-o-q</td><td>y-o-y</td></tr><tr><td>Pharma</td><td>4.68</td><td>5.46</td><td>-0.78</td><td>-1.92</td></tr><tr><td>Device</td><td>5.27</td><td>5.72</td><td>-0.45</td><td>-2.94</td></tr><tr><td>CXO</td><td>9.93</td><td>7.03</td><td>2.90</td><td>-0.60</td></tr><tr><td>Pharmacies</td><td>2.73</td><td>2.78</td><td>-0.05</td><td>-0.26</td></tr><tr><td>Distributors</td><td>2.04</td><td>1.43</td><td>0.61</td><td>-0.78</td></tr><tr><td>Services</td><td>1.33</td><td>1.50</td><td>-0.18</td><td>-0.70</td></tr><tr><td>ICL</td><td>5.84</td><td>5.75</td><td>0.09</td><td>-2.49</td></tr></table>

Source: Wind, HSBC Qianhai Securities

Exhibit 3. South Bound Holding and changes

<table><tr><td>South Bound Holding</td><td>2Q26 (%)</td><td>1Q26 (%)</td><td>q-o-q</td><td>y-o-y</td></tr><tr><td>Pharma</td><td>19.74</td><td>19.50</td><td>0.24</td><td>0.04</td></tr><tr><td>Biotech</td><td>32.91</td><td>33.57</td><td>-0.66</td><td>-5.47</td></tr><tr><td>CXO</td><td>16.81</td><td>20.39</td><td>-3.58</td><td>-5.38</td></tr><tr><td>Distributors</td><td>27.32</td><td>31.55</td><td>-4.23</td><td>-2.45</td></tr><tr><td>Services</td><td>33.58</td><td>37.70</td><td>-4.12</td><td>0.75</td></tr><tr><td>ICL</td><td>2.94</td><td>3.13</td><td>-0.19</td><td>0.98</td></tr></table>

Source: Wind, HSBC Qianhai Securities

Exhibit 4. Expected commercialisation impact

<table><tr><td>Timeline</td><td></td><td>Key products</td><td></td></tr><tr><td>2026 NDA</td><td>Kelun Bio Trop 2 ADC</td><td>Keymed Claudin 18.2 ADC</td><td>Akeso AK112</td></tr><tr><td>2027 Ph3</td><td>Hansoh B7H3, B7H4</td><td>Beone CDK4</td><td>Innovent PD1/IL2</td></tr></table>

Source: PharmCube, HSBC Qianhai Securities

Valuation and risks

<table><tr><td colspan="2"></td><td>Valuation</td><td>Risks</td></tr><tr><td>WuXi Biologics2269 HKBuy</td><td>Current price:HKD38.26Target price:HKD46.80Upside:+22%</td><td>We continue to use a DCF model to value WuXi Bio. Our key assumptions include a WACC of 9.0% (based on a risk-free rate of 4.25% and a market risk premium of 4.25%), a terminal growth rate of 3.5% and an end-2026e RMB-HKD exchange rate assumption of 1.17 (all unchanged). Our target price of HKD46.80 implies c22% upside from current levels; accordingly, we maintain our Buy rating on the stock.Linda Shu*, PhD (Reg. No. S1700522120001) | linda.y.l.shu@hsbcqh.com.cn | +86 755 88983246</td><td>Key downside risksProgress of potential US legislation to restrict US pharmaceutical companies to have contracts with Wuxi Biologics.A larger-than-expected impact from US tariffs.A longer-than-expected high US interest rate period that constrains the financing capability and project outsourcing demand of biotechnology companies.Overbuilt capacity for Wuxi Bio with demand shrinking among US and European customers.Regulatory tightening.</td></tr><tr><td>Pharmaron300759 CH /3759 HKBuy/Buy</td><td>Current price:RMB37.28HKD23.48Target price:RMB42.80HKD30.80Upside:+15%/+31%</td><td>We use a DCF model to value the A-share. The key assumptions in our valuation model include a WACC of 8.7% (based on a risk-free rate of 4.25%, a China A-share market risk premium of 4.75%, and a 2-year weekly beta coefficient of 1.26), and a terminal growth rate of 3.0%. We derive our target price of RMB42.80 for the A-shares (unchanged), which implies c15% upside from current levels. We maintain our Buy rating on the stock as we see high growth visibility in demand rebound driven by funding recovery. All our assumptions are unchanged.For the H-share, we apply a H/A-share discount of 0.72x, based on its five-year average, and an RMB-HKD FX rate of 1.17, to derive our H-shares target price of HKD30.80, which implies c31% upside from current levels; accordingly, we maintain our Buy rating on the stock.Linda Shu* PhD (Reg. No. S1700522120001) | linda.y.l.shu@hsbcqh.com.cn | +86 755 88983246</td><td>Key downside risksWorsening geopolitical tensions and global supply chain relocation.Margin pressure from worsening competition.Failure to meet regulatory standards, more stringent compliance, and regulatory delays.Failure of project delivery and loss of significant clientsFX fluctuations.</td></tr><tr><td rowspan="2">Keymed2162 HKBuy</td><td rowspan="2">Current price:HKD87.20Target price:HKD105.00Upside:+20%</td><td rowspan="2">We continue to use a DCF model to value Keymed. Our valuation is based on a risk-free rate of 4.25%, a market risk premium of 4.75% for a mainland China company listed in Hong Kong, a 1-year historical mean beta of 1.1, and a terminal growth rate of 4%, in line with our other covered biotech companies. Our target price implies 20.4% upside from current levels; accordingly, we maintain our Buy rating on the stock.</td><td>Key downside risksCMG901&#x27;s failure to file an NDA in US/EU for treating 2L+ CLDN18.2 ADC due to a phase III study failure.CM310&#x27;s domestic sales growth misses market expectations due to intense market competition from Sanofi&#x27;s Dupi and/or domestic IL4R launched by peers.Worse-than-expected efficacy and safety performance of CM512 (IL13/TSLP) could impact BD potential.Lower-than-expected efficacy results in overseas phase III could impact CM336 and CMG901&#x27;s sales growth in both China and the overseas market.Delay or failure to launch other late-stage assets could hurt sales in the short term.Slower-than-expected breakeven timeline or faster-than-expected increase in expenses could impact cash flow.Worse-than-expected domestic competitive landscape for ADC assets could hurt sales.Worse-than-expected domestic anti-corruption campaign could impact new drug sales growth.</td></tr><tr><td>Linda Shu* PhD (Reg. No. S1700522120001) | linda.y.l.shu@hsbcqh.com.cn | +86 755 88983246</td></tr><tr><td>Innovent1801 HKBuy</td><td>Current price:HKD92.50Target price:HKD120.00Upside:+30%</td><td>We continue to use DCF model to value the stock. We derive our target price of HKD120.00 (unchanged), based on a WACC of 9.0% (unchanged), derived from a risk-free rate of 4.25%, an equity risk premium of 4.75% (unchanged), a terminal growth rate of 3.6% (unchanged), and HSBC Global Investment Research FX team&#x27;s end-2026 RMB-HKD FX rate forecast of 1.17 (unchanged). Our target price implies c30% upside from current levels; accordingly, we maintain our Buy rating on the stock.Linda Shu*, PhD (Reg. No. S1700522120001) | linda.y.l.shu@hsbcqh.com.cn | +86 755 88983246</td><td>Key downside risksSlower-than-expected R&amp;D progress for Innovent&#x27;s key pipeline candidates.Faster-than-expected nationwide volume-based procurement (VBP) for biosimilars, which could hurt top-line growth potential.Lower-than-expected domestic sales due to intense competition.Failure in late-stage clinical trials could affect new drugs&#x27; launch and its potential to go global.</td></tr></table>

Note: Priced as of 20 July 2026. \*Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/qualified pursuant to FINRA regulations. Source: Wind, HSBC Qianhai Securities estimates

# Disclosure appendix

## Analyst Certification

The following analyst(s), economist(s), or strategist(s) who is(are) primarily responsible for this report, including any analyst(s) whose name(s) appear(s) as author of an individual section or sections of the report and any analyst(s) named as the covering analyst(s) of a subsidiary company in a sum-of-the-parts valuation certifies(y) that the opinion(s) on the subject security(ies) or issuer(s), any views or forecasts expressed in the section(s) of which such individual(s) is(are) named as author(s), and any other views or forecasts expressed herein, including any views expressed on the back page of the research report, accurately reflect their personal view(s) and that no part of their compensation was, is or will be directly or indirectly related to the specific recommendation(s) or views contained in this research report: Linda Shu, PhD, Oliver Wang and Cindy Chai

## Important disclosures

## Equities: Stock ratings and basis for financial analysis

HSBC and its affiliates, including the issuer of this report (“HSBC”) believes an investor's decision to buy or sell a stock should depend on individual circumstances such as the investor's existing holdings, risk tolerance and other considerations and that investors utilise various disciplines and investment horizons when making investment decisions. Ratings should not be used or relied on in isolation as investment advice. Different securities firms use a variety of ratings terms as well as different rating systems to describe their recommendations and therefore investors should carefully read the definitions of the ratings used in each research report. Further, investors should carefully read the entire research report and not infer its contents from the rating because research reports contain more complete information concerning the analysts' views and the basis for the rating.

## From 23rd March 2015 HSBC has assigned ratings on the following basis:

The target price is based on the analyst's assessment of the stock's actual current value, although we expect it to take six to 12 months for the market price to reflect this. When the target price is more than $20\%$ above the current share price, the stock will be classified as a Buy; when it is between $5\%$ and $20\%$ above the current share price, the stock may be classified as a Buy or a Hold; when it is between $5\%$ below and $5\%$ above the current share price, the stock will be classified as a Hold; when it is between $5\%$ and $20\%$ below the current share price, the stock may be classified as a Hold or a Reduce; and when it is more than $20\%$ below the current share price, the stock will be classified as a Reduce.

Our ratings are re-calibrated against these bands at the time of any 'material change' (initiation or resumption of coverage, change in target price or estimates).

Upside/Downside is the percentage difference between the target price and the share price.

## Prior to this date, HSBC's rating structure was applied on the following basis:

For each stock we set a required rate of return calculated from the cost of equity for that stock's domestic or, as appropriate, regional market established by our strategy team. The target price for a stock represented the value the analyst expected the stock to reach over our performance horizon. The performance horizon was 12 months. For a stock to be classified as Overweight, the potential return, which equals the percentage difference between the current share price and the target price, including the forecast dividend yield when indicated, had to exceed the required return by at least 5 percentage points over the succeeding 12 months (or 10 percentage points for a stock classified as Volatile\*). For a stock to be classified as Underweight, the stock was expected to underperform its required return by at least 5 percentage points over the succeeding 12 months (or 10 percentage points for a stock classified as Volatile\*). Stocks between these bands were classified as Neutral.

\*A stock was classified as volatile if its historical volatility had exceeded 40%, if the stock had been listed for less than 12 months (unless it was in an industry or sector where volatility is low) or if the analyst expected significant volatility.

[中间内容因长度限制已省略]

ssion and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc., a US-registered broker-dealer and member of FINRA, accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Qianhai Securities Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.
"""
