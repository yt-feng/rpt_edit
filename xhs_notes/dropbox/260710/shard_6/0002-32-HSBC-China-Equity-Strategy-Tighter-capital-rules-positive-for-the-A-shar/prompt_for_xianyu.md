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
Tighter controls, clearer direction. The Regulation on Outbound Investment (link) and enhanced regulation of cross-border securities and insurance companies suggest that regulators intend to channel capital back to authorised markets like the A-share market and the Southbound Connect. We see this as the third round of capital outflow restrictions since 2016 (Exhibit 1): 1) 2016-17: Regulating unlawful selling of overseas insurance products and restricting overseas investment in sectors like real estate; 2) 2021-22: Prohibited overseas institutions (e.g., Futu and UP Fintech) from opening new accounts for onshore residents; and 3) a two-year initiative to prevent unlawful cross-border operations conducted by overseas financial institutions.

Impact for financial institutions. The impact could be limited for banks; however, for insurers, more regulatory guidance, especially for cross-border sales, distribution and enforcement, is expected. For brokers, we estimate the suspension of cross-border equity total return swaps (TRS) could suggest a 0.8-1.2% impact on the top 10 listed brokers' total revenue. Cross-border asset management is also facing more compliance requirements, but onshore wealth managers might benefit from some offshore investment activities going back to onshore channels (see Hong Kong Financials: Top ten Q&A on cross-border wealth flows, Gary Lam, 29 June 2026).

Impact for China stocks. We believe the regulation is positive for the A-share market as both onshore institutions and personal investments face greater difficulty in investing in overseas markets. Onshore growth stocks offering going global opportunities (e.g., ChiNext) and tech self-sufficiency (e.g., STAR50) should benefit the most. For H-shares, this could be a short-term negative as onshore funds will have to sell stakes from their original broker accounts but should be neutral when these funds are channelled back and re-invested through the Southbound channel. As such, we expect to see continued southbound inflows (Exhibit 2).

Impact of the correction on mutual funds' style shift. Our analysis suggests that the impact could be limited as it involves market cap of only RMB11.6bn – 0.3% of the total AUM of active mutual funds of RMB4.0trn (Exhibit 9), much less than investors anticipated. This is because: 1) most active mutual funds are flexible enough to avoid concentration in one industry or one theme and the total AUM of consumer, healthcare and dividend-mandate active mutual funds is only RMB333.4bn; and 2) among special mandate funds, only a small fraction of AUM is involved in style drift, especially for healthcare-mandate funds (1.4% AUM). We find the stocks benefitting most from style drift are CATL, TFC and Eoptolink (Exhibit 10). In our view, the AI-centric rally will broaden, driven by fundamentals (industrials and materials), valuations and positions (consumer-related), and dividend appeal (high-yield stocks).

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

No country for bears

The $24^{\text{th}}$ edition of the EM Sentiment Survey Click to view

Issuer of report: HSBC Qianhai Securities Limited

View HSBC Qianhai Securities at: https://www.research.hsbc.com

Exhibit 1. China's policy measures on outbound investment since 2016

<table><tr><td>Date</td><td>Authorities</td><td>Key policy measures</td></tr><tr><td>2 Jun 2026</td><td>State Council</td><td>State Council Regulations on Outbound Investment◆ For the purposes of this provision, &quot;investors&quot; refer to companies, other organisations, and individual residents in China;◆ Investors enjoy the right to autonomy in outbound investment in accordance with the law, making their own decisions, bearing their own risks, and assuming responsibility for their own profits and losses;◆ Improve the comprehensive overseas service system, coordinate service resources covering foreign affairs, legal affairs, finance and taxation, banking, trade, and logistics to deliver service guarantees for investors;◆ Strengthen the outbound investment management system, refine regulatory and control measures, conduct full-process supervision by category and tier, and reinforce risk prevention and control.</td></tr><tr><td>22 May 2026</td><td>China Securities Regulatory Commission (CSRC)</td><td>Implementation Plan for the Comprehensive Remediation of Illegal Cross-Border Securities, Futures, and Fund Business Activities◆ Establish a two-year intensive rectification period to clear out existing illegal business operations and fully outlaw illegal cross-border operations conducted by overseas securities, futures and fund operating institutions;◆ During the period of intensive rectification, overseas institutions are prohibited from illegally providing services, such as facilitating buy orders or fund inflows, to existing domestic investors; only one-way sell transactions and fund withdrawals are permitted;◆ Upon the conclusion of the intensive rectification period, overseas institutions must fully shut down their onshore websites, trading software, and associated servers.</td></tr><tr><td>30 Dec 2022</td><td>China Securities Regulatory Commission (CSRC)</td><td>Futu Holdings and UP FinTech are required to rectify their illegal and non-compliant activities:◆ Soliciting domestic investors, acquiring new domestic clients and opening new accounts are prohibited for illegal activities;◆ Existing domestic investors are allowed to continue conducting transactions through the original overseas institutions; however, overseas institutions are prohibited from accepting incremental funds that violate China&#x27;s foreign exchange administration rules into the accounts of such investors.</td></tr><tr><td>11 Nov 2021</td><td>China Securities Regulatory Commission (CSRC)</td><td>Regulatory meeting with senior management of Futu Holdings and UP FinTech, requiring them to standardise their cross-border securities businesses targeting onshore investors in accordance with laws and regulations.</td></tr><tr><td>26 Dec 2017</td><td>National Development and Reform Commission (NDRC)</td><td>Administrative Measures for Outbound Investment by Enterprises◆ Outbound investment includes: 1) establishing new overseas companies or increasing capital contributions to existing overseas companies; 2) initiating or subscribing to overseas equity investment funds; and 3) controlling overseas companies or assets through means, such as agreements and trusts.</td></tr><tr><td>4 Aug 2017</td><td>General Office of the State Council</td><td>Guidance on Further Directing and Regulating Overseas Investment Direction◆ Prioritise the advancement of overseas infrastructure investments that facilitate the Belt and Road Initiative and the interconnection of infrastructure with neighbouring regions;◆ Strengthen investment cooperation with overseas high-tech and advanced manufacturing companies, and encourage the establishment of overseas R&amp;D centres;◆ Restrict overseas investment in sectors, such as real estate, hotels, cinemas, entertainment industries, and sports clubs.</td></tr><tr><td>23 May 2016</td><td>China Insurance Regulatory Commission (CIRC)</td><td>Notice on Strengthening the Regulation of the Illegal Sale of Overseas Insurance Products◆ Closely supervise the practice of illegally selling insurance products in a disguised manner, specifically through a process of domestic introduction, offshore contract signing, and offshore underwriting.</td></tr></table>

Source: Wind, NDRC, State Council, Cailianshe, Guardian, Reuters, HSBC Qianhai Securities

Exhibit 2. Continued southbound inflows during capital outflow restriction periods  
![](images/e6ad9595c3f2dd5689d553a0975519acd7bda18ac7f0cfeb4c7ef325b4384743.jpg)  
Note: Shaded region indicates periods of capital outflow restrictions. Source: Wind, HSBC Qianhai Securities

Exhibit 3. Impact on financial institutions from the Regulation and recent regulatory policies

<table><tr><td>Industry</td><td>Relevant mentions in the Regulation and recent regulatory policies</td><td>Impact on related industry</td></tr><tr><td>Insurance</td><td>The SFC and the HKMA issued circulars on tightened cross-border compliance and financial institutions should obtain a written declaration from mainland China investors confirming that all funds used for investment activities are from lawful sources outside mainland China.Policy-oriented insurance institutions are encouraged to offer services, such as overseas investment insurance, to support investors in their cross-border investment activities.</td><td>General insurers face greater uncertainty and potential volatility, and more guidance, especially for cross-border insurance sales, distribution, and enforcement, are expected.Policy-oriented insurers are encouraged to offer services to cross-border investment.</td></tr><tr><td>Brokers</td><td>The Regulation applies to activities involving direct or indirect acquisition of ownership, control, management rights, or other related interests regarding enterprises, assets, etc., in other countries (regions).Regulators require a suspension of the expansion of cross-border equity TRS.</td><td>0.8-1.2% of total top 10 listed brokers&#x27; revenue (RMB362bn in 2025, according to Wind), assuming RMB200-300bn cross-border equity TRS outstanding and a 1.5% fee per annum (as per cls).</td></tr><tr><td>Asset Management</td><td>Management of investors&#x27; overseas investments in foreign financial markets using their own funds, raised funds, or other entrusted funds shall be conducted in accordance with the Regulation and other relevant national provisions. The Regulation covers aspects, including approval and filing, information reporting, cross-border capital registration, and security reviews.</td><td>Onshore wealth managers might benefit from some offshore investment activities going back to onshore channels.</td></tr><tr><td>Banking</td><td>Banking financial institutions should, based on their functional positioning, adhere to the principles of market orientation, rule of law, commercial sustainability, and risk controllability. Within their scope of business, they shall provide financing and other financial services to support investors in their overseas investments.</td><td>Limited impact on HK banks.Beware of indirect effects rising from equity and property market sentiment fluctuations.</td></tr><tr><td>Professional Services</td><td>The Regulation supports professional service institutions, including those specialising in consulting and valuation, legal services, accounting and auditing, credit rating, mediation and arbitration, and intellectual property, to expand their overseas services networks. This aims to enhance their international services capabilities and standards, thereby delivering high-quality professional services to investors and their overseas investment projects.</td><td>Expanding overseas services networks is encouraged but with stricter compliance requirements.</td></tr></table>

Note: See Hong Kong Financials: Top ten Q&A on cross-border wealth flows, Gary Lam, 29 June 2026.  
Source: State Council, cls, HSBC, HSBC Qianhai Securities

Exhibit 4. Both QDII quota and NAV of QDII mutual funds are increasing. Crucially, regulators have signalled their intention to allocate further quotas, suggesting a supportive stance towards cross-border investments via compliant channels  
![](images/75bc46f71d6bd526a05f5a3846cc017102c42723662f8e9a4334be00387cb73f.jpg)  
Source: Wind, stcn, HSBC Qianhai Securities

Exhibit 5. Consensus 2026e earnings for materials and energy have seen upward revisions of 28.9% and 13.3%, respectively, YTD  
![](images/33f4e5450fcb16b0d3cf000c3f0a314ff99ec839aa676eb5d5c52f6727d3b0ea.jpg)  
Note: Data updated to 3 July 2026; the real estate sector, which registered a $244.7\%$ downward revision, is excluded from the chart. Source: Wind consensus, HSBC Qianhai Securities

Exhibit 6. Consensus 2026e earnings for ChiNext Index have seen upward revisions of $5.7\%$ YTD; consensus 2026e earnings for HSTECH have seen downward revisions of $14.0\%$ YTD  
![](images/b474e753775571716c5c3e69a5a7df9ff082b299d35af8ea0617dd02a5046874.jpg)  
Note: Data updated to 3 July 2026.  
Source: Wind consensus, HSBC Qianhai Securities

Exhibit 7. Sharp divergence between A-share tech indices (ChiNext Index and STAR50) and offshore tech indices (HSTECH and Nasdaq Golden Dragon China) so far this year  
![](images/03ead9fd79d649efa8ca9f78e27bba822ce1e723b450353b6e221fb46d02ffd3.jpg)  
Source: Wind, HSBC Qianhai Securities

Exhibit 8. A comparison of major tech indices suggests that STAR50 offers the highest earnings growth, while the ChiNext Index offers growth at a reasonable price (GARP)

<table><tr><td colspan="2"></td><td>ChiNext Index</td><td>STAR50</td><td>HSTECH</td></tr><tr><td rowspan="3">Valuation level</td><td>PE (2026e)</td><td>33.4x</td><td>104.3x</td><td>18.3x</td></tr><tr><td>Earnings growth(2026-28e three-year CAGR)</td><td>40.5%</td><td>76.5%</td><td>16.6%</td></tr><tr><td>PEG</td><td>0.83</td><td>1.36</td><td>1.10</td></tr><tr><td rowspan="7">Weight distribution</td><td>Domestic compute</td><td>13.5%</td><td>75.3%</td><td>13.0%</td></tr><tr><td>Overseas compute</td><td>37.5%</td><td>10.7%</td><td>0.0%</td></tr><tr><td>AI enabler</td><td>4.6%</td><td>1.7%</td><td>2.5%</td></tr><tr><td>AI adopter</td><td>9.8%</td><td>5.7%</td><td>82.6%</td></tr><tr><td>Electric equipment</td><td>24.0%</td><td>2.2%</td><td>0.0%</td></tr><tr><td>Healthcare</td><td>3.7%</td><td>3.6%</td><td>1.8%</td></tr><tr><td>Others</td><td>6.9%</td><td>0.8%</td><td>0.0%</td></tr><tr><td rowspan="5">Key constituents</td><td>#1</td><td>Innolight (14.5%)</td><td>Cambricon (9.2%)</td><td>NetEase (9.6%)</td></tr><tr><td>#2</td><td>CATL-A (13.6%)</td><td>Montage (8.2%)</td><td>SMIC-H (8.8%)</td></tr><tr><td>#3</td><td>Eoptolink (10.0%)</td><td>AMEC (8.1%)</td><td>Tencent (8.3%)</td></tr><tr><td>#4</td><td>East Money (3.5%)</td><td>Hygon (7.9%)</td><td>BYD-H (8.0%)</td></tr><tr><td>#5</td><td>Sungrow Power (3.1%)</td><td>SMIC-A (7.4%)</td><td>Meituan (7.7%)</td></tr><tr><td rowspan="2">Earnings growth</td><td>FY25</td><td>+17.3%</td><td>-20.3%</td><td>+4.1%</td></tr><tr><td>1QFY26</td><td>+25.6%</td><td>+261.3%</td><td>-6.6%</td></tr><tr><td>Earnings revision</td><td>YTD</td><td>+5.7%(+8.7% by excluding Wens)</td><td>-6.5%(-1.8% by excluding solar names)</td><td>-14.0%</td></tr></table>

Note: Data updated until 3 July 2026.  
Source: Wind, Wind consensus estimates, HSBC Qianhai Securities

Exhibit 9. The AUM involving style drift, as a percentage of total AUM of active mutual funds, is only c0.3%

<table><tr><td></td><td>AUM (RMBbn)</td><td>AUM involving style drift (RMBbn)</td><td>Percentage of style drift</td></tr><tr><td>Consumer-mandate active mutual funds</td><td>84.6</td><td>4.1</td><td>4.8%</td></tr><tr><td>Healthcare-mandate active mutual funds</td><td>168.5</td><td>2.4</td><td>1.4%</td></tr><tr><td>Dividend-mandate active mutual funds</td><td>80.3</td><td>5.1</td><td>6.4%</td></tr><tr><td>Sub Total</td><td>333.4</td><td>11.6</td><td>3.5%</td></tr><tr><td>Other active mutual funds</td><td>3,618.1</td><td></td><td></td></tr><tr><td>Total</td><td>3,951.5</td><td>11.6</td><td>0.3%</td></tr></table>

Source: Wind, HSBC Qianhai Securities

Exhibit 10. Funds involving style drift like to buy CATL (mainly consumer-mandate and dividend-mandate), TFC (mainly healthcare-mandate and dividend-mandate), and Eoptolink (same as TFC) the most  
![](images/ddc04871af3716f8e812c799b38b4078d939481176bbc11cc9f8aa123bd3f9ef.jpg)  
■ Healthcare-mandate active mutual funds  
Source: Wind, HSBC Qianhai Securities

Exhibi

[中间内容因长度限制已省略]

ssion and the Financial Supervisory Service of Korea. In Singapore, this publication is distributed by The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch for the general information of institutional investors or other persons specified in Sections 274 and 304 of the Securities and Futures Act 2001 of Singapore ("SFA") and accredited investors and other persons in accordance with the conditions specified in Sections 275 and 305 of the SFA. Only Economics or Currencies reports are intended for distribution to a person who is not an Accredited Investor, Expert Investor or Institutional Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc., a US-registered broker-dealer and member of FINRA, accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Qianhai Securities Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.
"""
