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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## China Insurance

## Summer Series: Market polarization risk rising as smaller players face capital pressure

In this note, we analyze 163 insurers, comprising 75 life and 88 non-life companies, with a focus on solvency capital, risk management and shareholder returns. Since 2005, the number of insurance legal entities has more than doubled, from 97 in Dec-05 to 238 in Jun-25, including 13 insurance groups, 75 life insurers, 88 non-life insurers, 7 reinsurers, 9 pension insurers, 7 health insurers, and 39 policy insurers and asset management arms. However, total insurance premium, across life and non-life combined, has grown only modestly, while insurance penetration improved to 4.4% in 2025 from 3.5% in 2015. Our initial view is that market polarization across both life and non-life insurance is likely to accelerate, particularly among small insurers that require repeated capital injections. This should widen the investment distinction between scale leaders and capital-constrained smaller players. Within our SMid insurance coverage, we see China Taiping and China Re as potential beneficiaries of industry restructuring. In the regional banking sector, we see a similar debate emerging, and Bank of Ningbo is our preferred name with better growth potential.

\- Market structure. China's insurance is an oligopolistic market at the top but fragmented below, with top 5 insurers holding $45\% / 68\%$ of life/non-life premiums. While GDP per capita above US\$10,000 supports the long-term penetration story, insurance remains highly capital intensive, requiring upfront spending on distribution, customer acquisition, claims infrastructure and risk management. Ongoing bancassurance channel reforms disproportionately favor large-cap insurers with better client access, hindering SMid insurers from generating organic earnings. Scale, therefore, becomes the key differentiator, raising the question of how many players may survive in the foreseeable future.

\- Life insurers. The overview of 75 life insurers shows a widening gap between large caps and SMids in capital efficiency, core solvency buffers and regulatory risk ratings. Listed insurers continue to maintain core solvency $>100\%$ , while 17 unlisted insurers are below $100\%$ , including 4 insurers $<70\%$ (vs. min.: $50\%$ ), the threshold that might potentially trigger capital calls. Many SMid life insurers face weaker brand recognition, sluggish new sales growth and rising capital risks. For most, market capital appears reluctant to flow into small players on a sustainable basis, exerting further pressure for business model retrenchment, as weak returns fail to cover long-term capital costs. We expect them to gradually cede market share amid intensifying structural competition.

\- Non-life insurers. Our review of 88 non-life insurers points to intensifying competition, particularly in auto insurance, where pricing pressure continues to weigh on underwriting profitability. Roughly 55% of non-life insurers reported underwriting losses in 2025. Only seven non-life insurers sustained their Mar-26 core solvency below 150%, vs. 180% across the top 5 non-life insurers. We believe large non-life insurers benefit from claims scale, data, reinsurance access and diversified risk pools, while SMid players remain exposed to narrow regional lines, single-product segments, catastrophe losses and cyclical pricing pressure.

\- Regional banks. A similar split is unfolding in the regional banking sector, as consolidation thins out SMid players with weak capital, asset quality and operating efficiencies, while quality franchises with credit growth compound.

Insurance

MW Kim AC
(852) 2800-8517
mw.kim@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Dan Wang
(86-21) 6106-6349
dan.wang@JPM.com
SAC Registration Number: S1730524080001
JPM Securities (China) Company Limited

Haomin Chen
(86-21) 6106 6347
haomin.chen@JPM.com
SAC Registration Number: S1730524080002
JPM Securities (China) Company Limited

Katherine Lei
(852) 2800-8552
katherine.lei@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 13 for analyst certification and important disclosures, including non-US analyst disclosures.

## Investment thesis

China's insurance sector has benefited from structurally supportive regulatory policies. The central government rolled out a suite of supportive measures lowering entry barriers for insurance participants. After 2005, the number of licensed insurance legal entities rose materially, from 97 (Dec-2005), peaking at 240 (Dec-2019), and then edging down slightly to 238 (Jun-2025). The sector comprises 13 insurance groups, 75 life insurers, 88 non-life insurers, 7 reinsurers, 9 pension insurers, 7 health insurers and 39 policy-focused insurers and asset management arms.

We divide China's insurance sector development into two phases. The expansion phase spanned 2005–2019, underpinned by liberalized licensing rules designed to expand insurance supply to meet rising consumption demand. This trend was reflected in industry premiums, where combined life and non-life premiums recorded a 17% CAGR over this period. The subsequent phase (2020–2025) prioritized high-quality development over scale expansion. Regulators pushed insurers to strengthen underwriting discipline and build capacity to manage macro and micro risks, supporting sustainable competitiveness against global peers. Authorities also relaxed FDI restrictions in phases, starting with life insurers in 2020, lifting foreign ownership caps gradually to 100% from the previous 51% (link). To compete in an open landscape, domestic insurers need to upgrade risk management frameworks. Policymakers now permit greater foreign participation via wholly-owned subsidiaries or joint ventures. Even so, total insurance premiums (life + non-life), a proxy for market size, have delivered just a 6% CAGR over the past five years, pushing up the insurance penetration (= premium over GDP) to 4.4% of GDP in 2025, versus 3.5% in 2015.

China's insurance market operates under an oligopolistic structure: the top five players have captured $45\%$ and $68\%$ market share within life and non-life segments, respectively. Our analysis covers 163 insurers (75 life and 88 non-life), focusing on solvency capital, risk management practices and shareholder return potential. While all large non-life insurers maintain core solvency ratios above $100\%$ , $28\%$ of life insurers reported core solvency below $100\%$ as of Mar-26, signaling weaker capital adequacy to absorb risks. From an equity investor standpoint, this weighs on expectations for sustainable excess capital distributions to shareholders. By contrast, large-cap insurers consistently maintain solvency above $120\%$ with a track record of steady dividend distribution.

In short, we expect market polarization to widen between large-cap and small-medium cap insurers over the medium term. Key drivers include capital constraints, uneven channel access and asymmetric macro risk resilience. Our initial view is that polarization across life and non-life segments will intensify, as market capital appears reluctant to flow into small players on a sustainable basis, given weak returns fail to cover long-term capital costs, especially amid risks of recurring capital calls. As a result, we expect SMid insurers to gradually cede market share amid intensifying structural competition.

Positioning (Insurance): Within our SMid Insurance coverage, China Taiping and China Re look well positioned to emerge as winners amid rising market concentration. Hampered by thin capital buffers, limited distribution reach and sluggish internal earnings, many SMid insurers face a sustained risk of losing market share. Distribution reforms channel high-quality resources toward established industry players. Supported by mature participating insurance operations and balanced capital allocation, Taiping stands to capture organically migrating business flows, independent of M&A activity.

For China Re, capital pressure pushes SMid insurers to explore capital supplementation avenues. Given limited internal capital generation and higher costs for external capital raising, financial reinsurance emerges as a viable tool to ease solvency strains. Even as regulators tighten the rules that govern financial reinsurance, such instruments will gradually lift reinsurance coverage demand for primary insurers with thin solvency buffers, driving market share gains amid broader industry polarization.

We see a similar debate and set of observations in the China's regional banking sector. Following a decade of license-driven expansion, regulators have pivoted decisively from scale growth towards risk resolution and ‘reduce quantity, improve quality’ since 2020, catalyzed by Baoshang Bank’s failure. The consolidation has been most pronounced among village banks. According to a media report (link), in 2025, 310 village banks completed merger-driven restructuring or dissolution, and 134 village banks have exited, as of 9 July 2026.

NFRA data suggest there are 124 city commercial banks and 3,381 rural financial institutions as of 1H25. In aggregate, they represent 27% of banking system assets as of 1H26, which we believe are the weaker link in the banking system, as they carry higher NPL ratios, lower provision coverage, weaker ROA and capital ratios relative to larger peers (Table 2).

Positioning (Banks): Although our coverage is concentrated in leading regional banks that carry lower risks and higher operating efficiencies, investors remain cautious about the vulnerabilities that characterize the SMid players across the sector – less stable EPS growth, thinner capital buffer and consequently lower dividend visibility. As a result, among regional banks, the market ascribes a dividend-reliability discount to high-yield SMid banks, favoring those whose valuations are underpinned by credible growth stories. We prefer Bank of Ningbo among our regional banks on the back of its fee growth potential in FY26 and stable asset quality.

Figure 1: China – time series data for licensed insurers
Number of legal entities  
![](images/d3968cf14f9b5c28fc23e3a5c8b64943eade26648d94aff9e3e6ccfeabf84334.jpg)

Source: National Financial Regulatory Administration (NFRA), Statistics Bureau of China. The number of licensed insurers from 2005 to 2018 is based on each year's China statistics book published by the Statistics Bureau of China, while data from 2019 to 2025 are based on the full list of financial institution legal entities disclosed by NFRA for each year. These data are as of each fiscal year end. The total number of insurer legal entities includes insurance groups, P&C insurers, life insurers, health insurers, pension insurers, reinsurers, asset management companies, policy insurers, and mutual insurance corporations.

Table 1: China – license insurers tracked over the past six years
Number of legal entities

<table><tr><td></td><td>Dec-19</td><td>Dec-20</td><td>Dec-21</td><td>Dec-22</td><td>Dec-23</td><td>Dec-24</td><td>Jun-25</td></tr><tr><td>Insurance Group/Holding co.</td><td>14</td><td>14</td><td>13</td><td>13</td><td>13</td><td>13</td><td>13</td></tr><tr><td>P&amp;C insurers</td><td>88</td><td>87</td><td>87</td><td>88</td><td>88</td><td>89</td><td>88</td></tr><tr><td>Life Insurers</td><td>81</td><td>75</td><td>75</td><td>75</td><td>75</td><td>75</td><td>75</td></tr><tr><td>Pension insurers</td><td>8</td><td>9</td><td>9</td><td>10</td><td>9</td><td>9</td><td>9</td></tr><tr><td>Health Insurers</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td></tr><tr><td>Reinsurers</td><td>12</td><td>14</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td></tr><tr><td>Insurance asset management</td><td>26</td><td>28</td><td>33</td><td>33</td><td>35</td><td>35</td><td>35</td></tr><tr><td>Policy insurers</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Mutual insurance corporation</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Total</td><td>240</td><td>238</td><td>235</td><td>237</td><td>238</td><td>239</td><td>238</td></tr></table>

Source: NFRA. Data from 2019 to 2025 is based on the full list of financial institution legal entities disclosed by NFRA for each year.

Table 2: Overview and key ratios of China banking system by institutional type

<table><tr><td rowspan="2"></td><td rowspan="2">Number of institutions in 1H25</td><td colspan="3">as % of banking system in 1H26</td><td colspan="5">Key ratios in 1Q26</td></tr><tr><td>Assets</td><td>Liabilities</td><td>Equities</td><td>CAR</td><td>NPL ratio</td><td>NPL coverage</td><td>ROA</td><td>NIM</td></tr><tr><td>SOE banks</td><td>6</td><td>44%</td><td>44%</td><td>41%</td><td>17.54%</td><td>1.22%</td><td>240.70%</td><td>0.60%</td><td>1.29%</td></tr><tr><td>Joint-stock banks</td><td>12</td><td>16%</td><td>16%</td><td>17%</td><td>13.14%</td><td>1.22%</td><td>204.60%</td><td>0.74%</td><td>1.54%</td></tr><tr><td>City commercial banks</td><td>124</td><td>14%</td><td>14%</td><td>12%</td><td>12.09%</td><td>1.85%</td><td>171.20%</td><td>0.57%</td><td>1.38%</td></tr><tr><td>Rural Fis</td><td>3,381</td><td>13%</td><td>13%</td><td>11%</td><td>12.85%</td><td>2.79%</td><td>156.90%</td><td>0.45%</td><td>1.58%</td></tr><tr><td>Others*</td><td>547</td><td>13%</td><td>13%</td><td>19%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total banking system</td><td>4,070</td><td>100%</td><td>100%</td><td>100%</td><td>15.00%</td><td>1.51%</td><td>203.10%</td><td>0.60%</td><td>1.40%</td></tr></table>

Source: NFRA [1H25's list of legal persons of financial institutions in the banking industry (link); Table of Main Indicators of Commercial Banks (link)], People's Bank of China (PBOC), CEIC [banking asset/liability data accessed from the CEIC web site on 27 July 2026; the CEIC shows the original source as being the PBOC]. \*Others includes policy banks, China Development Bank, private banks, foreign banks, non-bank financial institutions, financial asset investment corps, and wealth management companies; the number of institutions data is as of end-1H25.

# Oligopolistic market at the top but fragmented below

China's aggregate insurance premium reached Rmb6.1T, or US\$870B, in 2025, representing more than threefold growth since 2005. The market is characterized by an oligopolistic structure among leading players, alongside significant fragmentation among smaller participants. As of 2025, the top five insurers accounted for $45\%$ of life insurance premiums and $68\%$ of non-life premiums.

Market share trends have diverged sharply across segments. In life insurance, the combined share of the top five insurers gradually declined from 51.7% in 2021 to 45.3% in 2025, while the top five non-life insurers maintained a stable share of around 68% over the same period. Notably, the number of licensed life insurers has stabilized at 75 over the past five years. This suggests that the gradual erosion of large life insurers' market share is more likely attributable to intensified competition from existing small and mid-sized participants. Supported by the industry shift towards participating products, many small and mid-sized life insurers achieved short-term premium expansion, although this growth carries material capital consumption risks.

Data from the National Financial Regulatory Administration (NFRA) show that the total 

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
