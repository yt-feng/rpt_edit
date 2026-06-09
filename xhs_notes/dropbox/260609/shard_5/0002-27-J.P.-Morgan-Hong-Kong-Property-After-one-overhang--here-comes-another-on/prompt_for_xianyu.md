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
# Hong Kong Property

After one overhang, here comes another one

Over the past 2 weeks, the sector has underperformed the HSI by 7% due to concerns over tighter capital outflow controls in Mainland China (more discussion in our reports on 29 May and 3 Jun). Then, over the weekend, a new overhang emerged: the reignited concerns about rate hikes (driven by strong US labor data). While we do not think these two overhangs alone will derail the housing market recovery (home prices have jumped 9.6% YTD (Figure 4), and we maintain our full-year forecast of 10-15% for FY26), the uncertainties will likely weigh on sentiment for a while, and thus we expect the sector to face some near-term pressure. However, we remain constructive on the HK housing market as we believe it is more driven by the strength in the financial industry & inventory (report), though only continually solid data (e.g. prices/sales volume/sell-through rates) will abate investors' concerns. In the near term, we believe Sino & CKA may relatively outperform due to net cash, while Henderson may underperform as it is more affected by the two overhangs (Henderson is more exposed to Kai Tak (Figure 3) and more sensitive to rates (Figure 6)). Meanwhile, SHKP may also be prone to profit-taking due to its still-strong YTD outperformance (30% over the HSI) (Figure 13). However, on dips, we suggest long-term investors accumulate SHKP, Sino, Swire Prop & HLP.

- Existing overhang - Potential tighter capital outflow controls: For this concern, we already discussed our thoughts in Will tightened controls on capital outflows, if true, derail the upcycle? published on 29 May and Implications of State Council's Regulations on Outbound Investment published on 3 Jun. As a recap: (1) So far there is no official ban on Mainland Chinese buying properties in HK; (2) capital outflow control is not new; (3) even in the worst scenario where all “Mainland China-based Mainland Chinese” cease to be homebuyers in HK, we estimate they account for 5-10% of volume (10-15% by value), but we believe “HK-based Mainland Chinese” should see limited impact; the majority of buyers remain locals; (4) if the concern materializes, high-end properties in Kai Tak will be the most affected as “Mainland China-based Mainland Chinese” buyers are the majority in this segment (Table 2).  
- New overhang - Reignited fear of a rate hike: Over the weekend, strong labor data in the US has driven concerns of a rate hike scenario again. JPM currently maintains the forecast of a rate pause till 1Q27 (report). However, if the US Fed Funds Rate is raised, Hong Kong prime rate may follow and thus mortgage rates may turn higher (Figure 5). That said, if the rates pause at current levels, HK homebuyers would still be enjoying a marginally positive carry (Figure 5) (headline mortgage rate $3.25\%$ , but effective mortgage rate $2.9 - 3.0\%$ if including cash rebates, vs. net rental yield $3.0\%$ ). Meanwhile, a US rate hike may also cause some upward pressure on HIBOR, although for now we believe if HIBOR stays between $2 - 3\%$ , this should be largely within investors' expectations ( $>3\%$ would be a negative surprise). For homebuyers, higher mortgage rates are directionally negative, but do not necessarily cause a downcycle (as seen in 2004-06; 16-18, during which both HK property stocks

## Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

& home prices went up despite rate hikes). For property companies, a higher HIBOR would hurt earnings, and based on our sensitivity analysis, within our coverage, NWD & Henderson will be more impacted, while Sino & CKA will be the least impacted (Figure 6). For more discussion, please see our earlier report HK Property: What if there is a rate hike?.

- The two overhangs have not yet materialized, but concerns may only abate with continually solid data: For the concern about capital outflow control, while there might be more clarity when the State Council publishes more detailed guidelines for individual investors, we doubt whether there will be explicit mentions of home buying in HK (as the recent crackdown seems to target illegal cross-border investment activities only, at least for now). Therefore, we think there is a chance there will not be any official clarification. If not, then investors' concerns may only abate upon the resiliency of key housing data, such as home prices, sell-through rates of primary launches (only for those with market prices, not those with aggressive premiums or discounts), and secondary sales volume.  
- Sector valuation: The sector is trading at a 47% NAV discount, which is close to 1 s.d. below the historical mean (48%) (Figure 14). Alternatively, the sector is trading at a 4.4% dividend yield, which is 0.5 s.d. above the historical average (Figure 16). Arguably, the sector's valuations are not stretched, and a significant derating is unlikely as long as home prices remain at least stable. However, HK Property remains one of the better-performing sectors YTD (+12% vs. the HSI -3%) (Figure 12), on the back of a solid recovery in the housing market (home prices have rebounded almost 10% year-to-date), retail sales bottoming out, and office seeing a K-shaped stabilization. Assuming no further additional overhangs, we expect <10% downside from here. On dips, we suggest long-term investors accumulate: (1) SHKP: likely continual MSD% growth in EPS & DPS over the next 2-3 years; (2) Sino Land: 5% yield with high dividend certainty; (3) Swire Prop: Mainland China retail continues to improve, with HK office bottoming out; 5.6% yield with 5% p.a. DPS growth; (4) HLP: Mainland China tenant sales likely to outperform; 6.6% yield with high certainty.

# Overhang #1) Tighter capital outflow control in Mainland China

## Mainland Chinese buyers in HK residential market

Table 1: HK private residential market - % of buyers who are NOT holders of Hong Kong Identity Card (HKID)

<table><tr><td rowspan="2"></td><td colspan="4">Individual buyers who are not HKID holders</td></tr><tr><td colspan="2">Volume(units) as % of total</td><td colspan="2">Value(HK$ bn) as % of total</td></tr><tr><td>FY20/21</td><td>110</td><td>0.1%</td><td>1.1</td><td>0.2%</td></tr><tr><td>FY21/22</td><td>153</td><td>0.2%</td><td>1.6</td><td>0.2%</td></tr><tr><td>FY22/23</td><td>168</td><td>0.3%</td><td>1.6</td><td>0.4%</td></tr><tr><td>FY23/24</td><td>700</td><td>1.6%</td><td>6.8</td><td>2.0%</td></tr><tr><td>FY24/25</td><td>2,997</td><td>5.5%</td><td>31.3</td><td>7.2%</td></tr></table>

Source: HK Inland Revenue Department  
Note: FY denotes HK government's fiscal year (year ending 31 March). For example, FY24/25 refers to the period from 2Q24 to 1Q25.

Figure 1: HK private residential market - % of Mainland Chinese buyers, defined by last name with Mandarin pinyin (by volume)  
![](images/53a8caeb92adceca18df5003c988ec1bc8779ad98050b897f96bfd63c77ae629.jpg)

<details>
<summary>line chart</summary>

| Quarter | Primary | Secondary | Overall |
| ------- | ------- | --------- | ------- |
| 26Q1    | 36%     | 17%       | 23%     |
</details>

Source: Centraline.  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

Figure 2: HK private residential market - % of Mainland Chinese buyers, defined by last name with Mandarin pinyin (by volume)  
![](images/8de75f827da55925b415487cb1399087ebc836042cb5b291cc82acaeb60f5075.jpg)

<details>
<summary>line chart</summary>

| Quarter | Primary | Secondary | Overall |
| ------- | ------- | --------- | ------- |
| 261Q    | 49%     | 21%       | 32%     |
</details>

Source: Centraline.  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

## Districts with the most “Mainland Chinese” buyers in Hong Kong

Table 2: Top 5 districts ranked by no. of Mainland Chinese buyers (primary units) since the lifting of the additional stamp duties (Mar 2024 to Feb 2026)

<table><tr><td>District</td><td></td><td>Total</td><td>Primary</td><td>Secondary</td></tr><tr><td>Kai Tak</td><td>啟德</td><td>3,050</td><td>2,786</td><td>264</td></tr><tr><td>Wong Chuk Hang</td><td>黃竹坑</td><td>1,162</td><td>1,131</td><td>31</td></tr><tr><td>Cheung Sha Wan / Sham Shui Po</td><td>長沙灣/深水埗</td><td>1,376</td><td>838</td><td>538</td></tr><tr><td>Tseung Kwan O</td><td>將軍澳</td><td>1,544</td><td>777</td><td>767</td></tr><tr><td>Central &amp; Western</td><td>中西區</td><td>1,971</td><td>731</td><td>1,240</td></tr></table>

Source: Midland  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

Figure 3: Developers' exposure in Kai Tak Runway Area based on attributable number of unsold units  
![](images/d5d918b5584b295222a92e3a8e44701c4dbd97db280422ffd04286d25291c39e.jpg)

<details>
<summary>bar chart</summary>

| Company | Percentage (%) |
| :--- | :--- |
| COLI | 21 |
| Henderson | 13 |
| Wheelock | 13 |
| CKA | 12 |
| K Wah | 11 |
| NWD | 10 |
| Wharf | 6 |
| SHKP | 4 |
| Empire | 4 |
| Far East | 2 |
| CR Land | 1 |
| Poly Property | 1 |
| Chinachem | 1 |
</details>

Source: Centraline, JPM  
Note: For projects involving a consortium, we assume an equal split among the developers.

# Overhang #2) Concern on interest rate hike

## Hong Kong interest rates vs. US Fed funds rate

Figure 4: HK mortgage rate / 1M HIBOR / prime rate vs. U.S. Fed funds rate (long-dated)  
![](images/74ab7fa7bcfb0cff3f4e8043bfa1c2cb4e899e75fac1f0cb02ebcdccff06626c.jpg)

<details>
<summary>line chart</summary>

| Year | HSBC Prime Rate | HIBOR 1M | US Federal Funds Target Rate | HK Mortgage Rate |
|------|-----------------|----------|------------------------------|------------------|
| 1993 | ~6.5            | ~4.0     | ~3.0                         | ~8.0             |
| 1994 | ~7.0            | ~5.5     | ~3.5                         | ~8.5             |
| 1995 | ~7.5            | ~6.0     | ~4.0                         | ~9.0             |
| 1996 | ~8.0            | ~6.5     | ~4.5                         | ~10.0            |
| 1997 | ~8.5            | ~7.0     | ~5.0                         | ~11.0            |
| 1998 | ~9.0            | ~7.5     | ~5.5                         | ~11.5            |
| 1999 | ~9.5            | ~8.0     | ~6.0                         | ~11.0            |
| 2000 | ~10.0           | ~8.5     | ~6.5                         | ~10.5            |
| 2001 | ~9.5            | ~8.0     | ~6.0                         | ~10.0            |
| 2002 | ~8.5            | ~7.5     | ~5.5                         | ~9.5             |
| 2003 | ~7.5            | ~7.0     | ~5.0                         | ~9.0             |
| 2004 | ~7.0            | ~6.5     | ~4.5                         | ~8.5             |
| 2005 | ~6.5            | ~6.0     | ~4.0                         | ~8.0             |
| 2006 | ~7.0            | ~6.5     | ~4.5                         | ~7.5             |
| 2007 | ~7.5            | ~7.0     | ~5.0                         | ~7.0             |
| 2008 | ~7.0            | ~6.5     | ~4.5                         | ~6.5             |
| 2009 | ~6.5            | ~6.0     | ~4.0                         | ~6.0             |
| 2010 | ~6.0            | ~5.5     | ~3.5                         | ~5.5             |
| 2011 | ~5.5            | ~5.0     | ~3.0                         | ~5.0             |
| 2012 | ~5.0            | ~4.5     | ~2.5                         | ~4.5             |
| 2013 | ~4.5            | ~4.0     | ~2.0                         | ~4.0             |
| 2014 | ~4.0            | ~3.5     | ~1.5                         | ~3.5             |
| 2015 | ~3.5            | ~3.0     | ~1.0                         | ~3.0             |
| 2016 | ~3.0            | ~2.5     | ~0.5                         | ~2.5             |
| 2017 | ~2.5            | ~2.0     | ~0.0                         | ~2.0             |
| 2018 | ~2.0            | ~1.5     | -                            | ~1.5             |
| 2019 | ~1.5            | ~1.0     | -                            | ~1.0             |
| 2020 | ~1.0            | ~0.5     | -                            | ~0.5             |
| 2021 | ~0.5            | ~0.0     | -                            | -                |
| 2022 | ~0.0            | -        | -                            | -                |
| 2023 | -               | -        | -                            | -                |
| 2024e| -              | -        | -                            | -                |
| 2025e| -              | -        | -                            | -                |
| 2026e| -              | -        | -                            | -                |
</details>

Source: Bloomberg Finance L.P., HKET, Mingpao, HSBC, JPM.

## Mortgage rate vs. rental yield

Figure 5: HK rental yield over mortgage rate vs. secondary home price  
![](images/dc0709f977a58a747dd70a7c1184351f63de1c58e633e6595b572b6fa9242ae2.jpg)

<details>
<summary>line chart</summary>

| Year | Gross yield spread | Net yield spread | HK Secondary Home Price Index (CCL) |
|------|---------------------|------------------|-------------------------------------|
| 1997 | -8%                 | -8%              | -2%                                 |
| 1998 | -6%                 | -6%              | -4%                                 |
| 1999 | -4%                 | -4%              | -6%                                 |
| 2000 | -2%                 | -2%              | -8%                                 |
| 2001 | 0%                  | 0%               | -8%                                 |
| 2002 | 2%                  | 2%               | -6%                                 |
| 2003 | 4%                  | 4%               | -4%                                 |
| 2004 | 2%                  | 2%               | -2%                                 |
| 2005 | 0%                  | 0%               | 0%                                  |
| 2006 | -2%                 | -2%              | 2%                                  |
| 2007 | 0%                  | 0%               | 4%                                  |
| 2008 | 2%                  | 2%               | 6%                                  |
| 2009 | 4%                  | 4%               | 8%                                  |
| 2010 | 2%                  | 2%               | 10%                                 |
| 2011 | 0%                  | 0%               | 12%                                 |
| 2012 | -2%                 | -2%              | 14%                                 |
| 2013 | 0%                  | 0%               | 16%                                 |
| 2014 | 2%                  | 2%               | 18%                                 |
| 2015 | 4%                  | 4%               | 20%                                 |
| 2016 | 2%             

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jun 2026 08:25 AM HKT

Disseminated 08 Jun 2026 08:26 AM HKT
"""
