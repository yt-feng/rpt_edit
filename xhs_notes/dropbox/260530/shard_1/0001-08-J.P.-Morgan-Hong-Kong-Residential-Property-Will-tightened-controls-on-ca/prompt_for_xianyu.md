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
# Hong Kong Residential Property

Will tightened controls on capital outflows, if true, derail the upcycle?

Since last Friday, the sector has underperformed the HSI by 3%, likely due to rising concerns on potential tightening of capital outflow controls in Mainland China (as a read-through from the recent regulators' crackdown on illegal cross-border securities trading through brokers like Futu) (more). First of all, the sell-off looks precautionary, as so far there is no evidence of imminent tightening. However, if true, this may indeed impact some demand, with primary luxury units in Kai Tak likely to be most affected. We estimate 10-15% of all homebuyers are Mainland China-based (note that many other “Mainland Chinese” buyers are those who reside in Hong Kong and thus may not be affected by capital outflow controls). That said, even if true, this does not change our upcycle thesis as the various tailwinds remain in place (e.g. population growth, solid demand from HK-based Mainland Chinese, optimal inventory levels, <5% vacancy rates, and a strong financial services industry), and this may at best mildly drag down the home price uptrend momentum (but we still forecast both FY26 and FY27 to see positive growth). Year-to-date, HK home prices have already risen 9% (Figure 11) (faster than expected), while our full-year forecast is 10-15%, implying another 1-6% growth for the rest of the year. On the positive side, a milder home price growth (a slow bull) lowers the risk of policy tightening (e.g. further stamp duty hikes). Our top picks (with defensive biases as the rate direction remains unclear) are SHKP, Sino & CKA among developers; Swire Prop & HKL among landlords.

\- A read-through from the Futu incident? On 22 May, CSRC issued the Implementation Plan for the Comprehensive Rectification of Illegal Cross-border Securities, Futures and Fund Business Activities. The Plan focuses on shutting down illegal cross-border operations and guides investors to invest overseas through lawful channels (more from our China financials analysts Katherine Lei & Peter Zhang). Accordingly, brokers like Futu have been fined. Although this alone has no direct impact on the Hong Kong housing market, nor has the Chinese government explicitly banned Mainland Chinese from buying properties in Hong Kong, some investors have started to worry about (as a read-across) whether this implies capital outflow control in Mainland China may be tightened (see Table 1 for the current regulations), thus potentially impacting home demand in Hong Kong.

\- Be aware of the definition of “Mainland Chinese” in the data: According to Centraline, by value/transaction, “Mainland Chinese” buyers account for 32%/23% in the housing market (primary & secondary combined) as of 1Q26 (Figure 2). The ratio would be higher in the primary market (49%/36% by value/transaction). However, the statistics from Centraline are based on buyers’ last names with Mandarin pinyin, not by actual residence address. Therefore, the “Mainland Chinese” buyers in the statistics include those who reside in Hong Kong or have a Hong Kong identity, who may not be affected by capital outflow control, if any. In fact, the data would also have included some local Hong Kong people who happen to keep a Mandarin pinyin last name (e.g. “Wang”). We estimate that “Mainland China-based Mainland

# Mainland China/Hong Kong Property & Conglomerates

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

Chinese" accounts for $\sim 15\%$ of transaction value (or $\sim 10\%$ by number of transactions). We currently forecast total transaction value in FY26E (primary & secondary) to grow $32\%$ Y/Y to HK\$687 billion, but in a bearish (and unlikely) scenario where all demand from "Mainland China-based Mainland Chinese" is eliminated, the full-year transaction value would still grow $12\%$ Y/Y. Note, however, that HK property stocks have historically traded more on home prices, rather than volume. Therefore, this is just for illustrative purposes.

\- If true, luxury primary homes will be more affected: Assuming all “Mainland China-based Mainland Chinese” will no longer find ways to channel their money to Hong Kong to buy homes, we believe luxury primary homes will be more impacted. By district, we believe Kai Tak will be the most impacted (Table 2), as we roughly estimate that 40-50% of the buyers in that district are “Mainland China-based Mainland Chinese”. The next most impacted district would be Wong Chuk Hang.

\- Demand from HK-based Mainland Chinese should still be solid: We estimate that Mainland Chinese households who have resided in Hong Kong for <7 years total \~200-300K. This group of buyers was previously subject to additional stamp duties until 1Q24. We believe this group of buyers have been the majority of “Mainland Chinese buyers” as they live in Hong Kong with genuine home demand. Since 2Q24, there have been 30K transactions from “Mainland Chinese buyers” (Figure 1). Stripping out Mainland China-based Mainland Chinese and those who have resided in HK for >7 years, we roughly estimate that \~15K transactions are from HK-based Mainland Chinese who have resided in HK for <7 years (or 5-8% of this group have already purchased a flat). This suggests further upside in home demand from these “new Hong Kongers”.

\- Other supportive factors remain in place: Our upcycle thesis on the housing market does not just rely on demand from “Mainland China-based Mainland Chinese”. Rather, it is based on various supportive factors, including (1) population growth driven by incoming talent from Mainland China and return of Hong Kong people who migrated from Western countries (Figure 5); (2) a low vacancy rate of 4.3% which supports further uptrend in rents (Figure 6), pushing renters to become buyers (31% of private households are renters) (Figure 8); (3) a strong financial services industry; (4) optimal inventory levels (<10 months in primary market) (Figure 9); (5) genuine demand from HK-based Mainland Chinese; (6) a marginally positive carry (3.0% net rental yield vs. 3.25% mortgage rate, although effective mortgage rate is likely <3% if considering cash rebates and mortgage rate-linked interest income) (Figure 10).

\- Home price growth has been faster than expected; a “slow bull” would lower policy tightening risk: The pace of home price growth year to date (up 9%) has been stronger than expected (Figure 11). If potentially lower demand from Mainland China-based Mainland Chinese drags down home price growth, this actually reduces the risk of additional policy tightening. As a recap, in 2010-16, the HK government introduced various additional stamp duties (e.g. special stamp duties / buyer’s stamp duties) which raise the buying costs for non-local buyers, with the goal of curbing speculative activities. In February 2026, HK policymakers raised the stamp duty rate for properties valued at >HK\$100 million from 4.25% to 6.5% (report). If home price growth continues to be too fast, we would not be surprised if the government extends the higher 6.5% stamp duty rate to properties of a lower value (say HK\$50 million).

\- Key risks: Rather than capital outflow control, we believe the bigger risk that may derail the housing market recovery is a collapse of the stock market (which may lead to a very weak financial services industry) as the Hang Seng Index has historically shown a strong correlation to Hong Kong home prices. Another downside risk is an unexpected call for curbing quotas for talent schemes, as this may affect our home demand forecast. Finally, a near-term overhang is the concern on rate hikes (which also partially explains the recent share price weakness). JPM's base-case scenario is still a rate pause, but if the US raises the interest rate, Hong Kong may follow and thus mortgage rates may go up. However, we believe interest rates are only one of the many factors, but not the dominating factor, for HK home prices (more in HK Property: What if there is rate hike?).

# Mainland Chinese buyers in HK residential market

Figure 1: 12m rolling no. of Mainland Chinese buyers for private residential units in HK   
![](images/ba86a5cb0521d7c96ae3ad6b6ce8896f64df9eb72af039d4af5c31f3dc46d0b9.jpg)

<details>
<summary>bar</summary>

| Quarter | Value |
|---|---|
| 091Q | 3800 |
| 093Q | 4800 |
| 101Q | 7500 |
| 103Q | 8500 |
| 111Q | 10200 |
| 113Q | 10500 |
| 121Q | 9200 |
| 123Q | 8800 |
| 131Q | 7200 |
| 133Q | 6100 |
| 141Q | 3200 |
| 143Q | 3400 |
| 151Q | 3800 |
| 153Q | 3700 |
| 161Q | 3400 |
| 163Q | 4000 |
| 171Q | 5200 |
| 173Q | 6200 |
| 181Q | 5900 |
| 183Q | 5600 |
| 191Q | 4800 |
| 193Q | 5100 |
| 201Q | 4900 |
| 203Q | 3900 |
| 211Q | 4200 |
| 213Q | 5400 |
| 221Q | 6100 |
| 223Q | 5700 |
| 231Q | 4800 |
| 233Q | 5400 |
| 241Q | 5900 |
| 243Q | 9400 |
| 251Q | 13200 |
| 253Q | 14500 |
| 261Q | 16500 |
</details>

Source: Centraline. Note: "Mainland Chinese" is defined here using the Mandarin pinyin of the buyer's last name and does not distinguish the buyer's current residence or identity. As a result, "Mainland Chinese" who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as "Mainland Chinese" in this dataset.

Figure 2: Percentage of Mainland Chinese buyers in private residential sales (by value)   
![](images/13eda116e9e8f1614752e146fed249a914140c8050b7c90d0fc4d07fc8d0c0b3.jpg)

<details>
<summary>line</summary>

| Quarter | Primary | Secondary | Overall |
| ------- | ------- | --------- | ------- |
| 261Q    | 49%     | 21%       | 32%     |
</details>

Source: Centraline. Note: "Mainland Chinese" is defined here using the Mandarin pinyin of the buyer's last name and does not distinguish the buyer's current residence or identity. As a result, "Mainland Chinese" who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as "Mainland Chinese" in this dataset.

Figure 3: Percentage of Mainland Chinese buyers in private residential sales (by volume)   
![](images/fc4bb5061b7b38c969dca35d49e4757fd3ec829cfc451f597d8bad86e71049b6.jpg)

<details>
<summary>line</summary>

| Quarter | Primary | Secondary | Overall |
| ------- | ------- | --------- | ------- |
| 26Q1    | 36%     | 17%       | 23%     |
</details>

Source: Centraline.   
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

Figure 4: No. of visas granted under various schemes   
![](images/4be3619ea58b7d79990a06a52d5bc8fec09ff7ada835ec6d2a70db8d466e8234.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Admission Scheme for Mainland Talents and Professionals | Quality Migrant Admission Scheme | Immigration Arrangements for Non-local Graduates (IANG) | General Employment Policy | Top Talent Pass Scheme |
|---|---|---|---|---|---|
| 2008 | 14,000 | 0 | 0 | 26,460 | 0 |
| 2009 | 14,500 | 0 | 0 | 26,988 | 0 |
| 2010 | 15,500 | 0 | 0 | 26,884 | 0 |
| 2011 | 16,500 | 0 | 0 | 27,552 | 0 |
| 2012 | 17,628 | 0 | 0 | 28,628 | 0 |
| 2013 | 18,380 | 0 | 0 | 29,380 | 0 |
| 2014 | 19,678 | 0 | 0 | 31,678 | 0 |
| 2015 | 20,438 | 0 | 0 | 33,438 | 0 |
| 2016 | 21,997 | 0 | 0 | 35,997 | 0 |
| 2017 | 23,952 | 0 | 0 | 39,952 | 0 |
| 2018 | 24,592 | 0 | 0 | 41,592 | 0 |
| 2019 | 21,289 | 0 | 0 | 42,289 | 0 |
| 2020 | 14,618 | 14,618 | 14,618 | 41,592 | 0 |
| 2021 | 15,824 | 15,824 | 15,824 | 43,824 | 0 |
| 2022 | 13,495 | 13,495 | 13,495 | 44,952 | 0 |
| 2023 | 26,270 | 26,270 | 26,270 | 49,737 | 49,737 |
| 2024 | 35,058 | 35,058 | 35,058 | 41,057 | 41,057 |
| 2025 | 31,278 | 31,278 | 31,278 | 31,508 | 31,508 |
| 3M26 | 6,974 | 6,974 | -6,974 | -7,035 | -7,035 |
</details>

Source: HK Immigration Department.

Table 1: Personal cross-boundary remittance regulations from Mainland China to Hong Kong SAR 

<table><tr><td>Category</td><td>Quota</td><td>Details</td></tr><tr><td>Facilitative foreign exchange arrangement</td><td>US$50,000 per person per year</td><td>Directly conduct currency conversion at Mainland banks with identity document and remit outside the Mainland.</td></tr><tr><td>購匯便利化額度</td><td></td><td>If a remitter prefers not to use the quota / the conversion quota is reached, remitter shall provide the bank with supporting documents for verification of the use of funds (e.g. travel, study abroad, daily life, and medical care.)</td></tr><tr><td>Payment Connect 跨境支付通</td><td>Follow the facilitative foreign exchange arrangement (US$50,000 per year)</td><td>Real-time and small-value cross-boundary remittances at participating institutions in the Mainland</td></tr><tr><td>Withdraw cash using debt/credit cards issued in Mainland</td><td>Annual limit of RMB100,000, and a daily limit of RMB10,000</td><td></td></tr><tr><td>Cross-border cash carrying</td><td>Rmb 20,000 per person per trip; or USD 5,000 for foreign currency</td><td></td></tr></table>

Source: HKMA

Table 2: Top 5 districts ranked by no. of Mainland Chinese buyers (primary units) since the lifting of the additional stamp duties (Mar 2024 to Feb 2026) 

<table><tr><td>District</td><td></td><td>Total</td><td>Primary</td><td>Secondary</td></tr><tr><td>Kai Tak</td><td>啟德</td><td>3,050</td><td>2,786</td><td>264</td></tr><tr><td>Wong Chuk Hang</td><td>黃竹坑</td><td>1,162</td><td>1,131</td><td>31</td></tr><tr><td>Cheung Sha Wan / Sham Shui Po</td><td>長沙灣/深水埗</td><td>1,376</td><td>838</td><td>538</td></tr><tr><td>Tseung Kwan O</td><td>將軍澳</td><td>1,544</td><td>777</td><td>767</td></tr><tr><td>Central &amp; Western</td><td>中西區</td><td>1,971</td><td>731</td><td>1,240</td></tr></table>

Source: Midland

# Other supportive factors for the HK housing market

Figure 5: Hong Kong population   
![](images/3bb94b28201107476c0efe2d7aaecd6e6972710d3a1aec085e38250ecc68fd56.jpg)

<details>
<summary>bar_stacked</summary>

HK population (in million)
| Period | Usual resident (million) | Mobile resident (million) |
|---|---|---|
| Dec-10 | 6.75 | 0.18 |
| Jun-11 | 6.78 | 0.19 |
| Dec-11 | 6.80 | 0.19 |
| Jun-12 | 6.83 | 0.19 |
| Dec-12 | 6.85 | 0.19 |
| Jun-13 | 6.87 | 0.19 |
| Dec-13 | 6.89 | 0.19 |
| Jun-14 | 6.91 | 0.19 |
| Dec-14 | 6.93 | 0.19 |
| Jun-15 | 6.95 | 0.19 |
| Dec-15 | 6.97 | 0.19 |
| Jun-16 | 6.99 | 0.19 |
| Dec-16 | 7.01 | 0.19 |
| Jun-17 | 7.03 | 0.19 |
| Dec-17 | 7.05 | 0.19 |
| Jun-18 | 7.07 | 0.19 |
| Dec-18 | 7.09 | 0.19 |
| Jun-19 | 7.11 | 0.19 |
| Dec-19 | 7.13 | 0.19 |
| Jun-20 | 7.15 | 0.19 |
| Dec-20 | 7.17 | 0.19 |
| Jun-21 | 7.19 | 0.19 |
| Dec-21 | 7.21 | 0.19 |
| Jun-22 | 7.23 | 0.19 |
| Dec-22 | 7.25 | 0.19 |
| Jun-23 | 7.27 | 0.19 |
| Dec-23 | 7.29 | 0.19 |
| Jun-24 | 7.31 | 0.19 |
| Dec-24 | 7.33 | 0.19 |
| Jun-25 | 7.35 | 0.19 |
| Dec-25 | 7.37 | 0.19 |
| 2026E | - | - |
| 2031E | - | - |
| 2036E | - | - |
| 2041E | - | - |
| 2046E | - | - |
</details>

Source: Hong Kong Census & Statistics Department.

Figure 6: Vacancy rates in HK private residential units   
![](images/d53adf91ff55e71d426db94cffac6594b61c626df483858c5a192228c2deb388.jpg)

<details>
<summary>line</summary>

| Year | Value (%) |
|---|---|
| 1985 | 3.7 |
| 1986 | 3.9 |
| 1987 | 3.4 |
| 1988 | 2.9 |
| 1989 | 4.2 |
| 1990 | 3.5 |
| 1991 | 4.2 |
| 1992 | 4.2 |
| 1993 | 3.9 |
| 1994 | 4.7 |
| 1995 | 4.1 |
| 1996 | 3.7 |
| 1997 | 3.8 |
| 1998 | 4.5 |
| 1999 | 5.9 |
| 2000 | 5.4 |
| 2001 | 5.7 |
| 2002 | 6.8 |
| 2003 | 6.8 |
| 2004 | 6.2 |
| 2005 | 5.9 |
| 

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 May 2026 02:36 AM HKT

Disseminated 29 May 2026 02:36 AM HKT
"""
