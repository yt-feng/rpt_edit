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
# JPM

## Hong Kong Property

Implications of China's taxation on offshore trusts

China's latest taxation on offshore trusts (20% tax rate) is not a major surprise, given Bloomberg's late-March report (link). However, the new framework appears stricter than expected, featuring retroactive provisions (e.g., income from 2023 must be declared within 90 days) and enhanced anti-avoidance measures (e.g., obtaining foreign citizenship alone may not eliminate tax obligations). While the move is not specifically aimed at Mainland Chinese purchases of HK property, it still reduces the financial attractiveness of holding Hong Kong real estate—and, more broadly, offshore assets—thereby we consider it directionally negative for HK property. That said, we believe the impact is manageable, as we estimate $< 2\%$ of property sales are purchased via entities under Mainland Chinese-controlled offshore trusts, so this change alone is unlikely to derail the current upcycle in home prices (although we believe the growth momentum will still slow down in 2H26, regardless of this taxation – more in our earlier report). Arguably, this may also mildly slow down the sales momentum among en-bloc commercial properties and thus drag the pace of property companies' capital recycling. In the near term, the concerns on capital outflow control and rate hike remain two overhangs for the HK residential market, and thus we generally prefer landlords over developers. Our top picks are Link REIT, Swire Properties and Hongkong Land.

\- What's new? On 24 July, China's Ministry of Finance published a notice on individual income tax on offshore trusts (关于离岸信托个人所得税有关事项的公告; original policy in Chinese). Effective immediately, assets placed in offshore trusts held by Mainland Chinese tax residents will be subject to a $20\%$ tax rate, including: (1) the appreciation in value at the time of transfer of shares, property or other assets into offshore trusts; and (2) income from such trusts/offshore entities. Such offshore trusts have long been a gray zone in Chinese tax enforcement, and the move is Beijing's latest effort to capture revenue from the wealth its citizens hold overseas. The rules feature sweeping anti-avoidance provisions. Those who become foreign citizens or overseas permanent residents but retain their main economic interests in China may still be treated as Chinese tax residents (and thus the rules still apply to them). Notably, the new rule also has a retroactive clause, stating that unpaid taxes on assets placed in trusts since January 2023, and on trust income received before 2026, must be settled within 90 days to avoid penalties for late payment (Reuters). A detailed English translation of the full policy can be found in the Appendix – Full policy details.

\- A recap on offshore trusts: Offshore trusts have long been a vehicle for wealthy Mainland Chinese families to hold offshore assets (including listed companies, investments & real estate). However, apart from taxation (which was a gray area), families establish trusts also for many other reasons, including succession planning, asset protection and cross-generation wealth management. According to the Hong Kong Trustees' Association, the total asset size held under HK trusts amounted to HK\$5.1trn as of 2023, of which 55% are assets in Mainland China and Hong Kong, 18% in North America and 13% in Europe. Note that the latest rule does not just apply to trusts established in Hong Kong, but also any other offshore jurisdiction outside of Mainland China (e.g. Singapore).

See page 10 for analyst certification and important disclosures, including non-US analyst disclosures.

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

\- The new rules may make holding HK real estate assets less financially attractive, but at least they are not the only target: First of all, the new framework aims to tax ultra-rich Mainland Chinese individuals' offshore assets, but is not designed to specifically crack down on Mainland Chinese buying real estate properties in Hong Kong (note that the current forex rules do not allow Mainland Chinese to remit money offshore for the purpose of property buying; however, if the source of funding is offshore, e.g. dividend income or salaries generated in HK, Mainland Chinese are allowed to buy properties in HK – for more details, please see our takeaways from legal expert call). Since the new taxation applies to all offshore assets (such as listed equity investments and real estate assets in Singapore), while the new rule does make holding HK real estate assets less financially attractive than before, theoretically speaking this at least does not make holding HK real estate assets less favorable vs. other offshore asset types. That said, for Mainland Chinese individuals deciding between buying residential properties in Mainland China vs. HK, the gap has now narrowed, as although capital gain from property resale is also subject to a 20% tax rate (individual income tax) in Mainland China, if the residential asset is held for >5 years and is the family's only home for self-use (满五唯一), the 20% tax rate is exempt (but exemption may not necessarily apply to HK residential properties). Arguably, the move is marginally positive for the Mainland Chinese housing market.

\- What is the potential impact on the HK residential market? Based on our understanding, specifically for HK real estate assets, the new taxation framework would require Mainland Chinese tax residents to: (1) pay a 20% tax on rental income, although double taxation is unlikely, and thus the extra payment would be calculated after settling local Hong Kong taxes (i.e., for rental income from residential properties, HK levies a 15% tax rate, or 12% effective, and thus the extra nominal tax rate difference is 5%); and (2) pay a 20% tax on capital gains on resale (note: there is no capital gains tax in HK, and thus the 20% tax is fully extra). While there is no official data on the percentage of HK residential transactions that are made through entities under an offshore trust, we can gauge it by the percentage of company buyers, which is 4.5% as of 4M26 (Figure 1). However, since many local homebuyers also hold residential assets through a company (especially for wealthy families/celebrities), we estimate that company buyers that are controlled by a Mainland Chinese tax resident should be <50%, and thus we roughly estimate that, in the extreme scenario where no more non-local Mainland Chinese buy HK properties through offshore trusts (which is unrealistic, in our view), the impact on property sales is likely to be <2%. Among all districts in HK, we believe Kai Tak will be relatively more impacted as the district has seen the highest percentage of Mainland Chinese buyers.

\- There could be a broader impact if this applies to all individuals: The latest taxation only applies to offshore trusts, which mostly target ultra-rich families from Mainland China. However, if the Chinese government scrutinizes taxation for individual “Mainland Chinese tax residents” too, then there could be a broader impact. As a recap, “Mainland Chinese” homebuyers (defined by Mandarin pinyin of last name) account for 32%/23% of HK property sales (primary & secondary combined) by value/volume (Figure 2). We believe the majority of those reside in Hong Kong or have a HK identity card and thus may not necessarily be regarded as “Mainland China tax resident” (note: we estimate that non-local-based Mainland Chinese homebuyers account for 5-10% of total by volume, or 10-15% by value, Table 1). The biggest question lies in whether such homebuyers are defined as “Mainland Chinese tax residents”, which are defined by either: (1) having a “residence” in Mainland China (based on hukou/economic interest/family); or (2) residing in Mainland China for >183 days within a year. As such, if there is higher scrutiny on the definition, it is possible for Mainland Chinese who live/work in Hong Kong (even if they have no homeownership in Mainland China or have not lived/worked in Mainland China for a long time) to be taxed by Mainland Chinese tax authorities for their rental income/capital gains on HK properties, as long as they still hold a local hukou of a Mainland Chinese city. Execution is a question mark, because as of now real estate is not yet classified in CRS (common reporting standard), but this remains a risk.

\- There could be some implications on commercial properties too: In recent years, there have been more “Mainland Chinese buyers” in HK commercial assets (especially office), such as Li Ning (Harbour East) and Alibaba (One Causeway Bay). The new rules would likely apply to offshore trusts (controlled by Mainland Chinese) that hold commercial assets too, and thus this may potentially reduce the momentum in sale transactions (and thus the pace of property companies’ capital recycling). That said, there should be limited impact on leasing (which is our area of focus).

## "Company buyers" in HK residential market

Figure 1: HK residential property transactions – % of company buyers  
![](images/4adfca00d78fbb8afa4f5b800fd2cbaba03f4e7b0cfb018cc05abcb3fbaa15ad.jpg)  
Source: Midland.

## "Mainland Chinese buyers" in HK residential market

Table 1: HK private residential market – % of buyers who are not holders of Hong Kong Identity Card (HKID)

<table><tr><td rowspan="2"></td><td colspan="4">Individual buyers who are not HKID holders</td></tr><tr><td colspan="2">Volume(units) as % of total</td><td colspan="2">Value(HK$ bn) as % of total</td></tr><tr><td>FY20/21</td><td>110</td><td>0.1%</td><td>1.1</td><td>0.2%</td></tr><tr><td>FY21/22</td><td>153</td><td>0.2%</td><td>1.6</td><td>0.2%</td></tr><tr><td>FY22/23</td><td>168</td><td>0.3%</td><td>1.6</td><td>0.4%</td></tr><tr><td>FY23/24</td><td>700</td><td>1.6%</td><td>6.8</td><td>2.0%</td></tr><tr><td>FY24/25</td><td>2,997</td><td>5.5%</td><td>31.3</td><td>7.2%</td></tr></table>

Source: HK Inland Revenue Department.  
Note: FY denotes HK government's fiscal year (year ending 31 March). For example, FY24/25 refers to the period from 2Q24 to 1Q25.

Figure 2: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by volume)  
![](images/470208ddebe2a0a5016c9c34b344b761b7eeb7d3e29008729b6892244e9a15b6.jpg)  
Source: Centraline.  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

Figure 3: HK private residential market – % of “Mainland Chinese” buyers with a last name in Mandarin pinyin (by value)  
![](images/8e702e4fe64cc57d1c888c0a67f333b215315425409329879ac1e65006f36cdf.jpg)  
Source: Centraline.  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

# Appendix – Full policy details

Ministry of Finance and the State Taxation Administration – Announcement on Matters Concerning Individual Income Tax on Offshore Trusts (English Translation)

Ministry of Finance, 24 July 2026

Original article

Note: The below is our own translation and is only for illustrative purposes. Please refer to and rely on the original Chinese version at the link above for the full release.

## Article 1

Where an individual transfers property into an offshore trust and/or derives income through an offshore trust, such income shall be declared and individual income tax shall be paid in accordance with this Announcement.

## Article 2

An individual's transfer of asset into an offshore trust includes (1) direct transfer to an offshore trust; (2) transfers to an overseas entity that is held, controlled, or managed by an offshore trust or its trustee.

## Article 3

Where a resident individual transfers asset into an offshore trust, the taxable income shall be the balance of the market value of the asset at the time of transfer minus the asset's original cost and reasonable expenses. Such income shall be declared and individual income tax paid under "income from transfer of asset."

## Article 4

Any income generated during the trust term, whether or not actually distributed, shall be taxed with the resident individual as the taxpayer, and shall be declared and paid annually under “Income from transfer of asset” (balance of total proceeds minus original value and reasonable expenses), or “Interest, dividends, and bonus income”. Where trust income has already been declared and taxed, it shall not be declared again upon actual distribution.

## Article 5

Upon termination of the offshore trust, the liquidation gains on all offshore trust asset shall be taxable income, to be declared and taxed under “income from interest, dividends and bonuses”.

## Article 6

When the resident individual becomes a non-resident individual, the individual shall pay the income tax of the balance of the market value of the asset minus the original value.

## Article 7

After the resident individual's death, taxable income shall be the balance of the market value of trust asset on the date of death minus the original value. Any unpaid individual income tax payable shall be filed and paid by the trustee or its designated domestic institution.

## Article 8

When a non-resident individual transfers asset into an offshore trust but the trust is actually controlled by a resident individual, it shall be deemed that the resident individual has transferred the asset into an offshore trust, and individual income tax shall be declared and paid.

## Article 9

Where two or more resident individuals transfer assets into the same offshore trust, the trust asset and income attributable to each individual shall be allocated in proportion to the asset's market value transferred by the individual as a percentage of the total market value. Each individual shall separately declare and pay individual income tax. Where both resident and non-resident individuals transfer assets into the same offshore trust, it shall be treated as though all the assets were transferred by the resident individuals.

## Article 10

When a resident individual declares and pays individual income tax, any foreign taxes paid overseas for the offshore trust in accordance with local law may be credited against the current-period tax payable in accordance with law.

## Article 11

Individuals who have obtained foreign nationality or long-term/permanent overseas residence, but whose main economic interests are sourced from within China, may be determined to be resident individuals with domicile.

## Article 12

Where an offshore trust into which a non-resident individual has transferred asset has any of the following circumstances, it shall be deemed to have distributed income to a resident individual and shall declare and pay individual income tax:

\- Trust asset is used to provide a guarantee for a resident individual's debt, or a loan is provided to a resident individual, and such mortgage/guarantee is not released or such loan is not repaid by December 31 of the year;

\- Expenses are paid or reimbursed on behalf of a resident individual, or the resident individual is allowed to use trust asset free of charge or at an obvious

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
