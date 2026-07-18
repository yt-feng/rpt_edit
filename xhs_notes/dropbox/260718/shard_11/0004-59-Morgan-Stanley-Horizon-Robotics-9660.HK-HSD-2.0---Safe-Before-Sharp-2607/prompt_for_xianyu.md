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
China Autos & Shared Mobility | China

Horizon Robotics | Asia Pacific

# HSD 2.0 – Safe Before Sharp

We attended Horizon's HSD 2.0 test ride and mgmt meeting. HSD 2.0 was assured in most scenarios but hesitant in complex ones that should benefit from data training. With order concerns largely discounted, we think the stock needs a trigger rather than a floor. Stay OW.

Stock priced for doubt, awaiting a trigger: The stock setup is range-bound in the near term in our view, as the anemic 1H print and lack of a near-term catalyst or valuation anchor should constrain the shares until there is greater clarity on the per-vehicle content impact of the shift from hardware to licensing and design-win upside at anchor customers, like BYD. We think the negatives are largely discounted, but a catalyst is still missing. We will monitor J6/Starry 6P cadence, iCAR-to-mainstream progress, and project win quantification.

Our test-ride in Shenzhen suggests the system performs smoothly on highways and wide urban roads without being overly aggressive or conservative. However, it tends to hesitate for extended periods in complex scenarios, such as navigating around parked vehicles amid merging traffic or turning across oncoming traffic. HSD 2.0 also currently lacks reversing capability due to the absence of rearview camera data. However, the team expects the system's overall performance to improve rapidly as more driving data (including rearview) are incorporated into training, with further enhancements delivered through subsequent software updates.

Horizon acknowledged that HSD 2.0 is still at an early stage and is being improved through rapid iteration. The system currently errs on the side of caution and can be hesitant in certain scenarios, but records almost no safety-critical takeovers. Mgmt views this as the right trade-off, arguing that unsafe behavior reflects a more fundamental issue.

Strategically, Horizon aims to become the “Wintel” of autos by providing the compute and software stack rather than competing as an OEM. Mgmt expects rising industry specialization to create opportunities for third-party autonomy providers and believes Horizon can gain share alongside OEMs' in-house solutions.

Mgmt emphasized its competitive advantage lies in execution rather than proprietary technology. While world models, VLA and reinforcement learning are widely known, Horizon's strength lies in commercializing them at scale.

On customers, Horizon is deploying its integrated smart-driving and cockpit solution on Chery's iCAR, which it sees as a reference case for broader adoption. Longer term, the company aims to build a recurring, subscription-like per-vehicle revenue model.

On overseas expansion, mgmt believes solution providers may face fewer barriers than Chinese automakers by positioning as partners rather than competitors. Horizon also noted a potential opportunity from VW's reported shift away from Bosch, though any overseas contribution is likely to be gradual and long term.

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td>Tim Hsiao</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Tim.Hsiao@morganstanley.com</td><td>+852 2848-1982</td></tr><tr><td>Peggy Wang</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Peggy.Pc.Wang@morganstanley.com</td><td>+852 3963-3934</td></tr><tr><td>Shelley Wang, CFA</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Shelley.Wang@morganstanley.com</td><td>+852 3963-0047</td></tr><tr><td>Joey Xu, CFA</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Joey.Xu@morganstanley.com</td><td>+852 3963-0337</td></tr></table>

![](images/8385b07e4c942d5f11dd15230ed3196a25e0230e241b51ef4011e3f4c29336df.jpg)

## Horizon Robotics (9660.HK, 9660 HK)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>HK$8.70</td></tr><tr><td>Up/downside to price target (%)</td><td>97</td></tr><tr><td>Shr price, close (Jul 14, 2026)</td><td>HK$4.42</td></tr><tr><td>52-Week Range</td><td>HK$11.32-3.60</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>14,652</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb56,004.1</td></tr><tr><td>EV, curr (mn)</td><td>Rmb32,730.0</td></tr><tr><td>Avg daily trading value (mn)</td><td>HK$1,419</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>(0.81)</td><td>(0.19)</td><td>(0.08)</td><td>0.08</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Revenue, net (Rmb mn)</td><td>3,758</td><td>6,092</td><td>9,381</td><td>13,300</td></tr><tr><td>EBITDA (Rmb mn)</td><td>(3,750)</td><td>(2,696)</td><td>(733)</td><td>1,893</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>(10,469)</td><td>(2,793)</td><td>(1,143)</td><td>1,244</td></tr><tr><td>P/E</td><td>NM</td><td>NM</td><td>NM</td><td>45.0</td></tr><tr><td>ROE (%)</td><td>(87.9)</td><td>(22.1)</td><td>(10.6)</td><td>11.6</td></tr><tr><td>EV/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>17.8</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Risk Reward – Horizon Robotics (9660.HK)

A leading independent autonomous driving solutions provider

## PRICE TARGET HK\$8.70

Probability-weighted DCF, with probability weightings of 25% bull case, 50% base case, 25% bear case. The balanced probabilities in our bull case vs. bear case reflect our constructive view on Horizon gaining volume market share among ADAS+AD players in China, but we are also aware of rising competition and potential geopolitical headwinds in the smart driving business. Key DCF assumptions: 12.2% WACC (1.9 beta, 3% long-term growth rate).

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/cac43cb17540333304c1fc7e9dfabae6a0c680699bcbb0061c60342bebd94fed.jpg)

## RISK REWARD CHART

![](images/a1d6b9e838bf4551ae1d33cc9613aa82678c7fde5eb65a430f1147c9d9405a55.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target  
Source: Refinitiv, MS

## OVERWEIGHT THESIS

■ Horizon Robotics is a leading independent autonomous driving solutions provider with scarcity value.

\- We believe it is a key beneficiary of China's deepening autonomous driving trend.
- The autonomous driving industry's high barriers to entry favor leading players such as Horizon Robotics, thanks to its technology know-how in both software and hardware.

■ Horizon Robotics is also an early mover in the industry with extensive cooperation formed with global OEMs and Tier-1 suppliers.

■ We are OW relative to our coverage because we believe Horizon Robotics' solid project pipeline bodes well for its volume share gains among China ADAS and autonomous driving players.

![](images/98fddb5721e1bab94efae9d1ecc5f57c231a759dd44baaf3f82681f29cfe8e22.jpg)

## Risk Reward Themes

Electric Vehicles: Positive
Secular Growth: Positive

View descriptions of Risk Rewards Themes here

## BULL CASE

HK\$15.00

## 30x bull case 2026E revenue

We assume (1) J6P reaches mass delivery in 2026, (2) total ADAS+AD volume to exceed 5.5mn units in 2026 and 8mn units in 2027, and (3) Horizon Robotics reaches profit breakeven in 2027.

## BASE CASE

## HK\$8.20

## 18x base case 2026E revenue

We expect (1) J6P ramps up gradually, (2) total ADAS+AD volume to reach 5.1mn units in 2026 and 7.1mn units in 2027, and (3) Horizon Robotics reaches profit breakeven by 2028.

## BEAR CASE

HK\$3.50

## 9x bear case 2026E revenue

We assume (1) J6P ramps up slower than expected, (2) total ADAS+AD volume to be less than 5mn units in 2026 and 6mn units in 2027 due to order loss amid OEMs' switch to in-house solutions, and (3) Horizon Robotics remains loss-making in 2028.

0-10% Europe ex UK

0-10% APAC, ex Japan, Mainland China and India

◆ Mean ◆ MS Estimates
Source: Refinitiv, MS

## Risk Reward – Horizon Robotics (9660.HK)

## KEY EARNINGS INPUTS

<table><tr><td>Drivers</td><td>Dec 2025</td><td>Dec 2026e</td><td>Dec 2027e</td><td>Dec 2028e</td></tr><tr><td>Product solutions Revenue (Rmb, mn)</td><td>1,622</td><td>3,948</td><td>7,107</td><td>10,885</td></tr><tr><td>License and Services Revenue (Rmb, mn)</td><td>1,935</td><td>2,032</td><td>2,133</td><td>2,240</td></tr><tr><td>Total Gross Profit (Rmb, mn)</td><td>2,426</td><td>3,323</td><td>5,241</td><td>7,592</td></tr></table>

## INVESTMENT DRIVERS

• ADAS/AD adoption rate in China

\- Design-win by Horizon Robotics' next-generation products - J6 series

\- Sales ramp-up of mass produced products equipped with the company's solution

## GLOBAL REVENUE EXPOSURE

![](images/4befc47482212750f836e1c0c1af79547c243110a4ebb7c1fa53a55af76b3b1d.jpg)

0-10% India

0-10% Japan

0-10% Latin America

10-20% MEA

10-20% Mainland China

10-20% UK

20-30% North America

Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

## 5/5 MOST 3 Month Horizon

Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

\- Faster-than-expected ADAS/AD adoption growth in China

\- Delays/failure in OEMs' in-house hardware design

\- Narrowing access to other solutions providers in China

\- Expanding customer base with additional key customers

## RISKS TO DOWNSIDE

\- Slower-than-expected ADAS/AD adoption in China

• Supply chain disruption - OEMs' successful in-house hardware design initiatives

\- Vehicle sales pressure from key customers in China

## OWNERSHIP POSITIONING

<table><tr><td>Inst. Owners, % Active</td><td>47.8%</td></tr></table>

Source: Refinitiv, MS

MS ESTIMATES VS. CONSENSUS

<table><tr><td colspan="3">FY Dec 2026e</td></tr><tr><td rowspan="2">Sales / Revenue (Rmb, mn)</td><td rowspan="2">5,292.0</td><td>6,091.8 6,944.6</td></tr><tr><td>6,020.3</td></tr><tr><td rowspan="2">EBIT (Rmb, mn)</td><td rowspan="2">(5,164.0)</td><td>(3,183) (2,100.0)</td></tr><tr><td>(3,336.1)</td></tr><tr><td rowspan="2">Net income (Rmb, mn)</td><td rowspan="2">(4,512.2)</td><td>(2,793) (758.8)</td></tr><tr><td>(2,699.5)</td></tr><tr><td rowspan="2">EPS (Rmb)</td><td rowspan="2">(0.3)</td><td>(0.2) (0.1)</td></tr><tr><td>(0.2)</td></tr></table>

## Risk Reward Reference links

1. View explanation of Options Probabilities methodology -

Options\_Probabilities\_Exhibit\_Link.pdf

2. View descriptions of Risk Rewards Themes - RR\_Themes\_Exhibit\_Link.pdf

3. View explanation of regional hierarchies - GEG\_Exhibit\_Link.pdf

4. View explanation of Theme/Exposure methodology -

ESG\_Sustainable\_Solutions\_External\_Link.pdf

5. View explanation of HERS methodology - ESG\_HERS\_External\_Link.pdf

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Tim Hsiao; Shelley Wang, CFA; Joey Xu, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Brilliance China Automotive, BYD Company Limited, Changzhou Xingyu Automotive Lighting Sys, EHang Holdings Ltd, Great Wall Motor Company Limited, Hesai Group, Li Auto Inc., NIO Inc., Suzhou Recodeal Interconnect System, Voyah Automotive Technology Co. Ltd., WeRide Inc, XPeng Inc., Zhejiang Sanhua Intelligent Controls, Zhengzhou Yutong Bus Co.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Hori

[中间内容因长度限制已省略]

fully before investing.

INDUSTRY COVERAGE: China Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/14/2026)</td></tr><tr><td colspan="3">Joey Xu, CFA</td></tr><tr><td>Anhui Jianghuai Automobile (600418.SS)</td><td>E (08/19/2023)</td><td>Rmb22.50</td></tr><tr><td>BAIC Motor (1958.HK)</td><td>E (10/02/2025)</td><td>HK$0.80</td></tr><tr><td>Brilliance China Automotive (1114.HK)</td><td>E (03/31/2025)</td><td>HK$1.94</td></tr><tr><td>Chongqing Changan Automobile (000625.SZ)</td><td>E (03/03/2026)</td><td>Rmb6.94</td></tr><tr><td>Guangzhou Automobile Group (601238.SS)</td><td>U (10/23/2019)</td><td>Rmb4.94</td></tr><tr><td>Guangzhou Automobile Group (2238.HK)</td><td>O (05/05/2020)</td><td>HK$2.10</td></tr><tr><td>Huayu Automotive (600741.SS)</td><td>O (09/08/2020)</td><td>Rmb16.15</td></tr><tr><td>Jiangsu Changshu Automotive Trim Group (603035.SS)</td><td>E (08/14/2023)</td><td>Rmb10.70</td></tr><tr><td>Ningbo Huaxiang Electronic Co., Ltd. (002048.SZ)</td><td>E (05/05/2026)</td><td>Rmb21.37</td></tr><tr><td>SAIC Motor Corp. Ltd. (600104.SS)</td><td>O (11/25/2021)</td><td>Rmb10.05</td></tr><tr><td>Voyah Automotive Technology Co. Ltd, (7489.HK)</td><td>O (03/31/2026)</td><td>HK$2.96</td></tr><tr><td>Zhengzhou Yutong Bus Co (600066.SS)</td><td>E (09/22/2023)</td><td>Rmb28.65</td></tr><tr><td colspan="3">Shelley Wang, CFA</td></tr><tr><td>Beijing Jingwei Hirain Technologies (688326.SS)</td><td>U (09/27/2024)</td><td>Rmb63.69</td></tr><tr><td>Bethel Automotive Safety Systems Co Ltd (603596.SS)</td><td>O (12/11/2023)</td><td>Rmb22.61</td></tr><tr><td>Changzhou Xingyu Automotive Lighting Sys (601799.SS)</td><td>O (09/27/2024)</td><td>Rmb90.48</td></tr><tr><td>China MeiDong Auto Holdings Ltd (1268.HK)</td><td>U (07/10/2026)</td><td>HK$0.51</td></tr><tr><td>China Yongda Automobiles Services (3669.HK)</td><td>U (07/10/2026)</td><td>HK$0.83</td></tr><tr><td>Foryou Corporation (002906.SZ)</td><td>O (03/06/2024)</td><td>Rmb23.26</td></tr><tr><td>Fuyao Glass Industry Group (600660.SS)</td><td>E (12/01/2016)</td><td>Rmb50.70</td></tr><tr><td>Fuyao Glass Industry Group (3606.HK)</td><td>E (12/01/2016)</td><td>HK$50.15</td></tr><tr><td>Huizhou Desay SV Automotive Co Ltd (002920.SZ)</td><td>O (02/28/2025)</td><td>Rmb80.80</td></tr><tr><td>Keboda (603786.SS)</td><td>O (01/17/2024)</td><td>Rmb39.60</td></tr><tr><td>Minth Group Limited (0425.HK)</td><td>O (08/24/2015)</td><td>HK$26.92</td></tr><tr><td>NavInfo Co Ltd (002405.SZ)</td><td>U (03/06/2024)</td><td>Rmb6.22</td></tr><tr><td>Nexteer Automotive Group (1316.HK)</td><td>E (02/28/2025)</td><td>HK$3.83</td></tr><tr><td>Ningbo Joyson Electronic Corp (600699.SS)</td><td>E (03/11/2026)</td><td>Rmb20.29</td></tr><tr><td>Ningbo Tuopu Group Co Ltd (601689.SS)</td><td>E (11/12/2025)</td><td>Rmb54.36</td></tr><tr><td>Ningbo Xusheng Group Co Ltd (603305.SS)</td><td>E (06/18/2025)</td><td>Rmb11.23</td></tr><tr><td>Suzhou Recodeal Interconnect System (688800.SS)</td><td>O (07/02/2026)</td><td>Rmb72.88</td></tr><tr><td>TUHU Car Inc (9690.HK)</td><td>O (07/29/2024)</td><td>HK$13.31</td></tr><tr><td>Zhejiang Sanhua Intelligent Controls (002050.SZ)</td><td>E (11/12/2025)</td><td>Rmb41.94</td></tr><tr><td>Zhongsheng Group Holdings (0881.HK)</td><td>E (07/10/2026)</td><td>HK$4.65</td></tr><tr><td colspan="3">Tim Hsiao</td></tr><tr><td>BAIC BluePark New Energy (600733.SS)</td><td>U (08/07/2024)</td><td>Rmb4.57</td></tr><tr><td>BYD Company Limited (002594.SZ)</td><td>O (04/14/2025)</td><td>Rmb90.18</td></tr><tr><td>BYD Company Limited (1211.HK)</td><td>O (04/14/2025)</td><td>HK$86.15</td></tr><tr><td>EHang Holdings Ltd (EH.O)</td><td>O (03/13/2025)</td><td>US$5.45</td></tr><tr><td>Geely Automobile Holdings (0175.HK)</td><td>O (06/26/2024)</td><td>HK$18.31</td></tr><tr><td>Great Wall Motor Company Limited (601633.SS)</td><td>U (03/16/2022)</td><td>Rmb15.03</td></tr><tr><td>Great Wall Motor Company Limited (2333.HK)</td><td>E (01/08/2024)</td><td>HK$8.70</td></tr><tr><td>Hesai Group (HSAI.O)</td><td>O (07/28/2025)</td><td>US$15.61</td></tr><tr><td>Horizon Robotics (9660.HK)</td><td>O (12/02/2024)</td><td>HK$4.42</td></tr><tr><td>Li Auto Inc. (LI.O)</td><td>O (08/24/2020)</td><td>US$12.47</td></tr><tr><td>Li Auto Inc. (2015.HK)</td><td>O (11/16/2021)</td><td>HK$48.56</td></tr><tr><td>NIO Inc. (9866.HK)</td><td>O (10/03/2022)</td><td>HK$40.64</td></tr><tr><td>NIO Inc. (NIO.N)</td><td>O (08/26/2020)</td><td>US$5.01</td></tr><tr><td>WeRide Inc (WRD.O)</td><td>O (11/19/2024)</td><td>US$6.12</td></tr><tr><td>XPeng Inc. (9868.HK)</td><td>O (11/16/2021)</td><td>HK$52.35</td></tr><tr><td>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$13.36</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
