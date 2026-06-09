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
07 Jun 2026 17:56:14 ET | 13 pages

# Taiwan PCB & Laminates

What's New at Citi Taiwan Tech Conference 2026 – strong demand and shortage

## CITI'S TAKE

Overall, EMC, TUC and Gold Circuit (GCE) are all positive about AI demand and mentioned their capacity expansion pace could not catch up with end-customers' demand. EMC and TUC mentioned new CCL capacity ramp would be lower than new PCB capacity ramp, resulting in CCL shortage and potential price hikes going forward. EMC and TUC would continuously raise the price reflecting either inflation or premium based on customers' demand. GCE mentioned currently customers all agreed with the PCB price hike as well. GCE now sees m/s gain in its existing ASIC customer and sees good chance to support another new ASIC customer from 4Q26 onward. GCE's sales contribution from Thailand plant is guided to grow QoQ from 1Q26 onward, supporting its Thailand plant's profitability. Below are the key takeaways at Citi Taiwan Conference.

## GCE

- GCE plans to add one greenfield plant each year in 2027, 2028, and 2029. However, management indicated that the planned capacity expansion may still be insufficient to fully meet customers' demand.  
- In addition to expanding MLB capacity, GCE also intends to invest in HDI production capacity to support future growth opportunities.  
- For its existing ASIC customer, GCE is seeing market share gain in 2026 vs 2025. Meanwhile, management believes the company has a high probability of securing ASIC mainboard for additional ASIC customer.  
- Thailand operations are expected to increase monthly revenue contribution from approximately NT\$600mn in 2Q26 to NT\$1.3bn in 3Q26. The facility is currently focused on general-purpose server products, with AI server production scheduled to commence in 2H26. Management expects profitability at the Thailand plant to improve gradually as utilization ramps.  
- Regarding CCL supply, management believes supply can still be secured through previously negotiated long-term procurement forecasts. However, rush orders placed outside of committed volumes are unlikely to be fulfilled given tight industry supply conditions.

## EMC and TUC

- Both EMC and TUC observed that CCL industry capacity additions remain below the pace of PCB industry expansion. As a result, both companies expect CCL supply tightness to persist, supporting further pricing hikes in CCL sector.  
- EMC's future capacity expansion will primarily be concentrated in China, where management believes capacity deployment is more efficient and customer

## Jack Chen $^{AC}$

+886-2-8726-9091

jack1.chen@citi.com

Laura (Chia Yi) Chen

+886-2-8726-9090

laura.cy.chen@citi.com

Nicholas Lai

+886-2-8726-9093

nicholas.lai@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

demand is more abundant. Nevertheless, the company does not rule out additional investments in Malaysia.

- On glass fiber supply, EMC believes it is unlikely to be affected by potential Low-Dk2 shortages, whereas TUC expects Low-Dk2 materials to remain tight. Both companies noted that E-glass supply conditions appear to be improving and may no longer represent a major bottleneck in 2027.  
- For copper foil, EMC expects supply tightness could emerge in 2H26/2027. In contrast, TUC sees no meaningful shortage risk and believes copper foil pricing remains stable.  
- Regarding pricing strategy, EMC intends to continue passing through higher raw material costs. At the same time, management emphasized the importance of maintaining long-term strategic relationships with key AI customers when implementing price adjustments.  
- EMC believes customers' adoption of PTFE material remains at a very early evaluation stage and does not view PTFE adoption as a done deal at this point.  
- EMC is currently qualifying its ABF CCL for an ASIC project. Management indicated that the qualification results are unlikely to be available until end-2026.  
- TUC plans to adopt a more aggressive pricing strategy for M7 and below CCL. For M8 CCL, management expects pricing actions to remain aligned with EMC's strategy.  
- TUC remains constructive on its Thailand expansion and continues to observe OOC demand from US-based customers.  
- TUC's Thailand facility is now expected to begin contributing revenue by end-3Q26, later than previously anticipated, primarily due to delays in equipment deliveries.

## Elite Material

(2383.TW; NT\$4885.0; 1; 05 Jun 26; 13:30)

## Valuation

Our target price for EMC is set at NT\$5,100, based on a target PE multiple of 30x on our 2027E EPS average. We believe our target PE multiple, at the peak of its forward PE average in the past 5 years, is justified by a strong earnings outlook supported by its leading position in CCL supply for AI GPU and ASIC (high m/s) from 2026E onwards. We also believe the continued spec upgrade for CCL and price hikes should help support its margin expansion going forward. At our target price, the shares would trade at 22.9x/13.0x 2026E/27E PB.

## Risks

Citi's quant system rates EMC high-risk given high share price volatility, which we largely attribute to frequent debates over the spec upgrade for next-gen AI servers. In general, we believe some investors initially tend to have high hope for aggressive spec upgrade without sufficiently considering the scalability and cost structure of CCL products, which then leads to a shortfall in the end. However, from a longer-term perspective, we see a decent and clear spec upgrade trend with meaningful ASP growth potential among AI servers of different generations. As such, we do not assign a high-risk rating.

Key downside risks that could prevent the shares from reaching our target price include: 1) a slower-than-expected CCL upgrade trend; 2) weaker-than-expected AI server demand; 3) production bottlenecks in AI supply chain (eg, glass, copper foil, foundry or OSAT); 4) unexpected share loss in key AI server projects; and 5) stricter practice of OOC policy by end customers.

## Gold Circuit Electronics

(2368.TW; NT\$1315.0; 1; 05 Jun 26; 13:30)

## Valuation

Our TP of NT\$1,650 for GCE is based on 26x our 2027E EPS estimate, which is higher than 22x or +2std level of its 1-year-forward PE over the past three years. We believe the 25x multiple is justified by GCE's high AI server/networking sales exposure, market share gain in existing ASIC customer and new AI ASIC customer wins from 4Q26, which drives its AI ASIC sales growth and margin profile. Recall that TSMC expects close to a 50%+ CAGR in the next five years for its AI-related demand, which is stronger than any other applications. Thus, we believe investors would be willing to pay for high-growth AI names (especially ASIC) with high PE multiples. Our target price is equivalent to 44x/26x our 2026/27E EPS estimates and 16.1x/10.0x our 2026/27E BVPS.

## Risks

Key downside risks that could prevent the shares from reaching our target price include: 1) weaker-than-expected server recovery; 2) slower ramp-up pace of new server platform; 3) less-than-expected AI demand; 4) more PCB peers added into AI supply chain; and 5) stricter practice of China+1 by customers due to geopolitical concerns.

## TUC

(6274.TWO; NT\$1610.0; 1; 05 Jun 26; 15:00)

## Valuation

Our target price for TUC is set at NT\$1,600, based on a target PE multiple of 25x on our 2027E EPS. We believe our target PE multiple, at the peak of TUC's PE average in the last upcycle, is justified by its strong margin expansion potential on a higher sales mix from AI ASIC server/800G products and price hikes on supply tightness. We believe TUC's growth outlook is well supported by AI ASIC and 800G with its capacity ramp in Thailand from 2Q26 onward. At our target price, the shares would trade at 2026E/27E PB of 16.6x/10.0x.

## Risks

Citi's quant system rates TUC high-risk given high share price volatility, which we largely attribute to frequent debates over the spec upgrade for next-gen AI servers. In general, we believe some investors initially tend to have high hope for aggressive spec upgrade without sufficiently considering the scalability and cost structure of CCL products, which then leads to a shortfall in the end. However, from a longer-term perspective, we see a decent and clear spec upgrade trend with meaningful ASP growth potential among AI servers of different generations. As such, we do not assign a high-risk rating.

Key downside risks that could prevent the shares from reaching our target price include: 1) a slower-than-expected CCL upgrade trend; 2) weaker-than-expected AI server/800G demand; 3) production bottlenecks in AI supply chain (eg, glass, copper foil, foundry or OSAT); 4) unexpected share loss in key AI server projects; 5) flexible practice of OOC policy by end customers; and 6) slow development of the PCB industry in Southeast Asia.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Elite Material (2383.TW)

Ratings and Target Price History Fundamental Research

Analyst: Jack Chen

![](images/972a5c5bae5027711798f085fca17420e4276a7d3f52f51f9ac915031bfacd8d.jpg)

<details>
<summary>line chart</summary>

| Date  | Covered | Not covered |
|-------|---------|-------------|
| Dec 2024 |         |             |
| Dec 2025 |         |             |
| Dec 2026 |         |             |
| Mar 2027 |         |             |
| Jun 2027 |         |             |
</details>

![](images/ed6702ce833dc912dacab5e897da652bed46730cd04da03227277bffc39cfaaa.jpg)  
\*Indicates Change

![](images/9e611ee249a64f753058a12a42cbd0c12436f8213bf617e1c97495f82701de07.jpg)

![](images/294a72470bfa77804eebb5b64e0621b2fed85b393cd097114b5a7ce1cdc113cc.jpg)  
Rating/target price changes above reflect Eastern Time

TUC (6274.TWO)

Ratings and Target Price History
Fundamental Research

Analyst: Jack Chen

![](images/7facbb6efa12af27286067bbc7813e2131b02be2dbc3829c8cec64e6fa0be6cb.jpg)

<details>
<summary>line chart</summary>

| Month | Covered | Not covered |
|-------|---------|-------------|
| Jun   | 1       | 3           |
</details>

![](images/d8a656fb61a11a938e418437fcb499e14dc2d5472d1d21200aae4cf13978f2d5.jpg)  
\*Indicates Change

![](images/281e3f928af2c9c0eb5283df0a54ff631a1ee58cf5a87a2347567636c8085a84.jpg)

![](images/23299f19c86200b909ad78646d0d17df7712403051896333f839a55a7a9acaa7.jpg)  
Rating/target price changes above reflect Eastern Time

## Gold Circuit Electronics (2368.TW)

Ratings and Target Price History
Fundamental Research

Analyst: Jack Chen

![](images/e00c83f06477679e6c668c9ab6a410e0fff49e11b790838b88303ec6e38f2f1b.jpg)

<details>
<summary>line chart</summary>

| Month-Year | Covered | Not covered |
| --- | --- | --- |
| Jan 2024 |  |  |
| Feb 2024 |  |  |
| Mar 2024 |  |  |
| Apr 2024 |  |  |
| May 2024 |  |  |
| Jun 2024 |  |  |
| Jul 2024 |  |  |
| Aug 2024 |  |  |
| Sep 2024 |  |  |
| Oct 2024 |  |  |
| Nov 2024 |  |  |
| Dec 2024 |  |  |
| Jan 2025 |  |  |
| Feb 2025 |  |  |
| Mar 2025 |  |  |
| Apr 2025 |  |  |
| May 2025 |  |  |
| Jun 2025 |  |  |
| Jul 2025 |  |  |
| Aug 2025 |  |  |
| Sep 2025 |  |  |
| Oct 2025 |  |  |
| Nov 2025 |  |  |
| Dec 2025 |  |  |
| Jan 2026 |  |  |
| Feb 2026 |  |  |
| Mar 2026 |  |  |
| Apr 2026 |  |  |
| May 2026 |  |  |
| Jun 2026 |  |  |
| Jul 2026 |  |  |
| Aug 2026 |  |  |
| Sep 2026 |  |  |
| Oct 2026 |  |  |
| Nov 2026 |  |  |
| Dec 2026 |  |  |
| Jan 2027 |  |  |
| Feb 2027 |  |  |
| Mar 2027 |  |  |
| Apr 2027 |  |  |
| May 2027 |  |  |
| Jun 2027 |  |  |
| Jul 2027 |  |  |
| Aug 2027 |  |  |
| Sep 2027 |  |  |
| Oct 2027 |  |  |
| Nov 2027 |  |  |
| Dec 2027 |  |  |
| Jan 2028 |  |  |
| Feb 2028 |  |  |
| Mar 2028 |  |  |
| Apr 2028 |  |  |
| May 2028 |  |  |
| Jun 2028 |  |  |
| Jul 2028 |  |  |
| Aug 2028 |  |  |
| Sep 2028 |  |  |
| Oct 2028 |  |  |
| Nov 2028 |  |  |
| Dec 2028 |  |  |
| Jan 2029 |  |  |
| Feb 2029 |  |  |
| Mar 2029 |  |  |
| Apr 2029 |  |  |
| May 2029 |  |  |
| Jun 2029 |  |  |
| Jul 2029 |  |  |
| Aug 2029 |  |  |
| Sep 2029 |  |  |
| Oct 2029 |  |  |
| Nov 2029 |  |  |
| Dec 2029 |  |  |
| Jan 2030 |  |  |
| Feb 2030 |  |  |
| Mar 2030 |  |  |
| Apr 2030 |  |  |
| May 2030 |  |  |
| Jun 2030 |  |  |
| Jul 2030 |  |  |
| Aug 2030 |  |  |
| Sep 2030 |  |  |
| Oct 2030 |  |  |
| Nov 2030 |  |  |
| Dec 2030 |  |  |
| Jan 2031 |  |  |
| Feb 2031 |  |  |
| Mar 2031 |  |  |
| Apr 2031 |  |  |
| May 2031 |  |  |
| Jun 2031 |  |  |
| Jul 2031 |  |  |
| Aug 2031 |  |  |
| Sep 2031 |  |  |
| Oct 2031 |  |  |
| Nov 2031 |  |  |
| Dec 2031 |  |  |
| Jan 2032 |  |  |
| Feb 2032 |  |  |
| Mar 2032 |  |  |
| Apr 2033 |  |  |
| May 2033 |  |  |
| Jun 2033 |  |  |
| Jul 2033 |  |  |
| Aug 2033 |  |  |
| Sep 2033 |  |  |
| Oct 2033 |  |  |
| Nov 2033 |  |  |
| Dec 2033 |  |  |
| Jan 2034 |  |  |
| Feb 2034 |  |  |
| Mar 2034 |  |  |
| Apr 2034 |  |  |
| May 2034 |  |  |
| Jun 2034 |  |  |
| Jul 2034 |  |  |
| Aug 2034 |  |  |
| Sep 2034 |  |  |
| Oct 2034 |  |  |
| Nov 2034 |  |  |
| Dec 2034 |  |  |
| Jan 2035 |  |  |
| Feb 2035 |  |  |
| Mar 2035 |  |  |
| Apr 2035 |  |  |
| May 2035 |  |  |
| Jun 2035 |  |  |
| Jul 2035 |  |  |
| Aug 2035 |  |  |
| Sep 2035 |  |  |
| Oct 2035 |  |  |
| Nov 2035 |  |  |
| Dec 2035 |  |  |
| Jan 2036 |  |  |
| Feb 2036 |  |  |
| Mar 2036 |  |  |
| Apr 2036 |  |  |
| May 2036 |  |  |
| Jun 2036 |  |  |
| Jul 2036 |  |  |
| Aug 2036 |  |  |
| Sep 2036 |  |  |
| Oct 2036 |  |  |
| Nov 2036 |  |  |
| Dec 2036 |  |  |
| Jan 2037 |  |  |
| Feb 2037 |  |  |
| Mar 2037 |  |  |
| Apr 2037 |  |  |
| May 2037 |  |  |
| Jun 2037 |  |  |
| Jul 2037 |  |  |
| Aug 2037 |  |  |
| Sep 2037 |  |  |
| Oct 2037 |  |  |
| Nov 2037 |  |  |
| Dec 2037 |  |  |
| Jan 2038 |  |  |
| Feb 2038 |  |  |
| Mar 2038 |  |  |
| Apr 2038 |  |  |
| May 2038 |  |  |
| Jun 2038 |  |  |
| Jul 2038 |  |  |
| Aug 2038 |  |  |
| Sep 2038 |  |  |
| Oct 2038 |  |  |
| Nov 2038 |  |  |
| Dec 2038 |  |  |
</details>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>28-Sep-23 03:46:01</td><td>*1</td><td>*270.00</td><td>219.50</td></tr><tr><td>2</td><td>09-Nov-23 13:43:33</td><td>1</td><td>*275.00</td><td>215.00</td></tr><tr><td>3</td><td>12-Mar-24 09:50:59</td><td>1</td><td>*280.00</td><td>242.50</td></tr><tr><td>4</td><td>09-May-24 19:40:33</td><td>1</td><td>*270.00</td><td>198.50</td></tr><tr><td>5</td

[中间内容因长度限制已省略]

ceipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
