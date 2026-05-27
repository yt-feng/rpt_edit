你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Utilities & Renewables

# Global China Summit panel - ESS and Power Infrastructure's Role in the AI Race

Key Summary: We hosted a panel discussion on “ESS and Power Infrastructure’s Role in the AI Race” at the JPM Global China Summit over the last week. Panelists saw strong ESS growth momentum in China, while AIDCs were identified as a major growth engine for ESS. Power grid infrastructure may see meaningful investment opportunities, on the back of surging power demand and aging existing grid infrastructure. Meanwhile, nuclear power is gaining renewed attention in APAC for energy security. Overlaying key macro developments: 1) DC deployment opportunity in the DM; 2) energy transition and security development with bottom-up industry cycle factors, we have Sungrow, Orient Cable, Deye, Goldwind-H, TGOOD, and Wasion as our key OWs.

For the full highlights from the 2026 JPM Global China Summit by Feng Zhu, Erin Zhang and team, please see here (link). This is part of the report.

ESS installations see strong growth momentum in China: China's ESS is transitioning rapidly from policy driven to market-oriented/value-driven development. Following policies on power price liberalization (i.e. allowing peak-to-trough pricing throughout the day) and ESS capacity fees, the return profile (IRR) of independent ESS projects may improve from $4 - 5\%$ to $>10\%$ (some may reach $20\%$ in well-located sites). China's cumulative ESS installations have reached 144GW by 2025 and are expected to reach 450GW by 2030, representing a $25\%$ CAGR.

Emerging use-cases for AIDC: The higher power density of AIDC (60-200+kw per rack vs 5-8kw per rack for traditional data centers) creates massive peak loads and grid connection challenges. ESS has become an essential requirement for peak shaving, load smoothing, and power cost improvements (potentially up to $30\%$ ). In part due to low base (such use cases have just emerged), expects to see the TAM for this area may grow by 15-20x into 2030.

Power grid infrastructure may see meaningful investment opportunities: Surging power demand from AIDC & electrification and accelerating renewable deployment is placing significant pressure on aging power grids globally. Trillions of dollars (Usd) in grid upgrades are required, with China remaining the largest single market and Southeast Asia representing opportunity in the magnitude of hundreds of billions (Usd). Key investment themes include intelligent grid technologies, better integration of intermittent renewables, enhanced demand-side mgmt, and efficiency improvements.

Nuclear energy may be an emerging option for energy security: The Middle East conflict has renewed focus on energy security and resilience across the APAC region. Nuclear power is receiving renewed attention as countries seek greater self-sufficiency amid low oil and gas reserves. China and South Korea have emerged as the two leading players, with Korea strong in international certifications and project delivery, and China excelling in cost competitiveness and supply chain scale. However, decisions remain heavily influenced by geopolitics, safety

# APAC Utilities & Renewables | Sustainable Investing

Alan Hon AC

(852) 2800-8573

alan.hon@JPM.com

Stephen Tsui, CFA AC

(852) 2800-8592

stephen.tsui@JPM.com

Daqi Jiao

(852) 2800-8595

daqi.jiao@JPM.com

Vento Suen

(852) 2800-8546

vento.suen@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

protocols, long-term fuel supply relationships, and technology choices, with large-scale reactors currently favored over small modular reactors (SMR) at this stage, due to technology maturity.

Some renewable trends observed from meetings during the Global China Summit: 1) DG ESS is seeing a surge in demand in the SEA region; 2) Utility-Scale ESS is taking time to pass-through higher cost due to long order-to-delivery timeline; 3) Improving policy clarity on China off-shore wind development; 4) power market liberalization hurts wind farm operator; 5) poly maker reflects anti-involution policy on industry consolidation is still taking time to develop

Figure 1: China Utilities and Renewables Top Stock Ideas 

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Investment thesis/ Key Catalysts</td></tr><tr><td colspan="4">Top Long</td></tr><tr><td>Sungrow</td><td>300274 CH</td><td>OW</td><td>Riding on rising global ESS demand, while AIDC ESS development could be an emerging catalyst.</td></tr><tr><td>Deye</td><td>605117 CH</td><td>OW</td><td>(1) Riding the strong DG ESS growth in EM; (2) Beneficiary of disruption and tailwinds from energy resilience; (3) First mover in EM + cost leadership</td></tr><tr><td>Orient Cables</td><td>603606 CH</td><td>OW</td><td>Benefitting from China&#x27;s offshore wind demand pickup, as well as submarine cable&#x27;s (1) high entry barriers, (2) stable competitive landscape, (3) strong profitability</td></tr><tr><td>Goldwind-H</td><td>2208 HK</td><td>OW</td><td>WTG business may continue to improve, on the back of rising export sales and stronger-than-expected GPM</td></tr><tr><td>TGOOD</td><td>300001 CH</td><td>OW</td><td>Tailwinds from improving outlook on electrical equipment and EV charging platform</td></tr><tr><td>Wasion</td><td>3393 HK</td><td>OW</td><td>China smart meter leader with strong earnings growth driven by overseas expansion, new productsd, grid tender recovery, and AIDC orders</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates. All prices as of 25 May 2026 market close.

Companies Discussed in This Report (all prices in this report as of market close on 25 May 2026, unless otherwise indicated) Deye - A(605117.SS/Rmb118.36/OW), Goldwind - H(2208.HK/HK\$14.59[22 May 2026]/OW), Orient Cables - A(603606.SS/Rmb56.98/OW), Qingdao TGOOD Electric(300001.SZ/Rmb37.61/OW), Sungrow - A(300274.SZ/Rmb167.24/OW), Wasion Holdings Ltd - H(3393.HK/HK\$23.72[22 May 2026]/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

Research excerpts: This material may include excerpts from previously published reports. For access to the full reports, including analyst certification and important disclosures, please contact your sales representative or the covering analyst's team, or visit https://www.JPMmarkets.com.

# Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

# Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Hon, Alan : Arctech - A (688408.SS), CGN Power (1816) (1816.HK), Daqo (DQ), Datang Renewable (1798) (1798.HK), Deye - A (605117.SS), Envicool - A (002837.SZ), Flat Glass (6865.HK), GCL Tech (3800.HK), Goldwind - A (002202.SZ), Goldwind - H (2208.HK), Hangzhou First - A (603806.SS), Huaneng Hydropower - A (600025.SS), LONGi Green - A (601012.SS), Longyuan (0916) (0916.HK), Maxwell - A (300751.SZ), Mingyang - A (601615.SS), Orient Cables - A (603606.SS), SDIC Power - A (600886.SS), Shenzhen SC - A (300724.SZ), Sichuan Chuantou - A (600674.SS), Sungrow - A (300274.SZ), Tongwei - A (600438.SS), Xinyi Solar (0968) (0968.HK), Yangtze Power - A (600900.SS)Tsui, Stephen T: CK Infrastructure (1038.HK), CLP Holdings (0002) (0002.HK), China Gas Holdings (0384.HK), China Resources Gas (1193.HK), China Resources Power (0836.HK), ENN Energy (2688.HK), ENN Natural Gas – A (600803.SS), HD Hyundai Electric (267260.KS), Hangzhou Oxygen (002430.SZ), Hong Kong & China Gas (0003.HK), Huaming Equipment - A (002270.SZ), Huaneng Power - H (0902.HK), Hyosung Heavy Industries (298040.KS), Kunlun Energy (0135.HK), LS Electric (010120.KS), Nari Technology - A (600406.SS), Power Assets (0006.HK), Qingdao TGOOD Electric (300001.SZ), Sieyuan Electric - A (002028.SZ), Wasion Holdings Ltd - H (3393.HK), Xuji Electric - A (000400.SZ)

JPM Equity Research Ratings Distribution, as of April 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>79%</td><td>74%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>49%</td><td>39%</td><td>13%</td></tr><tr><td>IB clients**</td><td>94%</td><td>93%</td><td>85%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.

\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

# History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

# Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

All research material made available to clients are simultaneously available on our client website, JPM Markets, unless specifically permitted by relevant laws. Not all research content is redistributed, e-mailed or made available to third-party aggregators. For all research material available on a particular stock, please contact your sales representative.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities)

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase &

Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 25 May 2026 10:40 PM HKT

Disseminated 25 May 2026 10:40 PM HKT
"""
