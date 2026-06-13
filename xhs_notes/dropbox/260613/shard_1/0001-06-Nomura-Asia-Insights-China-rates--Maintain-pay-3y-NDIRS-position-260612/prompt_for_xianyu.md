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
## China rates: Maintain pay 3y NDIRS position

Tighter liquidity and higher bond supply are key drivers.

• We stay paid 3y NDIRS, targeting a move to 1.60% by end-July.  
- Liquidity has finally tightened, with the 7d repo fixing back above $1.4\%$ . The PBoC's net liquidity drain via medium- to long-term monetary policy tools since March is finally starting to filter through.  
- Government bond supply will likely pick up in Q3 after CGB and LGB issuance only reached 35% of the annual target at end-May (compared to 39% in 2025). Also, there are signs that funds have started to take profit on long bond positions.

## The long-awaited liquidity normalization has finally happened

In the last week of May, China rates rallied by 4-6bp across tenors, owing to flush liquidity (the PBoC net injected RMB100bn via 1y MLF and conducted a relatively large amount of OMOs), the 5bp decline in the 1y MLF rate to $1.45\%$ (source: Bloomberg) and media reports that local governments guided rural banks to invest more in bonds than NCDs (source: Wind; our preliminary data has not yet shown such a pattern).

Then, in June MTD, China rates rebounded by \~4-5bp from the low. In our view, liquidity continues to be the key driver of China rates, as has been the case since April. Considering the slow pace of government bond issuance (especially LGBs) in the first five months of the year, bond supply should start to garner more attention in coming months, as large/concentrated bond issuance could mean tighter liquidity and some improvement in the economic growth outlook (with fiscal expenditure speeding up). On the demand side, after accumulating a large amount of (ultra) long-end CGBs/PFBs in April and May, onshore funds reduced their bond holdings in June. It remains to be seen whether such outflows can sustain, or if there will be buy-on-dip flows once 10y and 30y CGB yields reach key levels of 1.75% and 2.25%, respectively.

In this report, we present our view on liquidity and bond supply/demand outlook and provide an update on our China Rates Trading Model (CHaRT).

## Liquidity

## 1. OMOs:

The PBoC skipped OMOs on 3 and 4 June but resumed operations on 5 June. Looking at the moves in money market rates, both DR007 and 1y NCD yields started to rebound on 5 June. Thus, we interpret the PBoC's OMO pattern as an effort to net inject short-term liquidity via 7d OMOs when there is real demand in the market (i.e., on the dates when money market rates are likely to move higher), and skip OMOs as needed to avoid injecting too much liquidity and bringing already-cheap funding costs even lower.

Note that prior to 3 June, the last time the PBoC skipped an OMO was on 7 August 2024. At that time, the DR007 dropped to \~1.69% on 2-6 August, below the 7d OMO rate of 1.70%. While we do not think there is any material difference between the OMO gross injections of RMB0.5bn (which happened on a few days in April and May), RMB0.2bn (2 June) and RMB0bn (3 and 4 June), the PBoC might still send a signal to the market that it could skip OMOs if there is no demand and it does not want money market rates to decline further.

Figure 1 shows the outstanding OMO amount. In previous years, the PBoC usually became more proactive in liquidity injection via OMOs in the last 1-2 weeks of June, to smooth the funding tightness amid higher government bond supply, tax payment and

## Research Analysts

## Asia Rates Strategy

Clair Gao, CFA - NIHK

clair.gao@NOM.com

+852 2252 1081

Albert Leung - NIHK

albert.leung1@NOM.com

+852 2252 1401

quarter-end funding needs. In this year, however, the short-term OMO liquidity injection started earlier.

## 2. Medium- to long-term monetary policy tools (ORR, MLF, net CGB purchases):

As we have flagged in previous reports, large net liquidity injections by the PBoC in January-February were one of the main drivers of super flush liquidity in recent months. The total net liquidity injection of RMB2.05trn in January-February 2026 was clearly well above the average levels over the past few years (Figure 2). From March to May, the PBoC net withdrew RMB200bn, RMB560bn and RMB850bn of liquidity, respectively (mainly via ORRs, Figure 3). In June so far, the PBoC further net drained RMB300bn via 3m ORRs on 5 June. Accordingly, the cumulative medium- to long-term net liquidity injections from the PBoC since start of the year (via ORRs, MLFs, the PBoC's net CGB purchases and RRR cuts; excluding OMOs) dropped significantly to RMB140bn latest, well below 2020-25 average of \~RMB1.1trn. This is consistent with our view in the mid-May update, and money market rates did eventually react to the low absolute level of liquidity in the market in May, albeit at a gradual pace.

## 3. NCD:

Monthly net NCD issuance has been in negative territory most of the time since June 2025 (except October 2025), as the PBoC was proactive in injecting medium- to long-term liquidity to the market over that period (including the 50bp RRR cut in May 2025). Banks were equipped with enough funding and it was not necessary to expand their liabilities through the NCD market. However, in May, net NCD supply turned positive for the first time since October last year. If we look at weekly data (Figure 4), net supply was positive during the weeks of 18 May and 1 June, and this is why NCDs have garnered more attention lately; when net supply turns positive, large NCD maturities matter more (RMB940-960bn this week and next week; RMB730bn in the week of 22 June) and NCD yields should face more upside pressure as well.

## 4. Our view on liquidity in coming weeks:

We continue to expect the PBoC to be more flexible with 7d OMOs to inject short-term liquidity amid higher government bond supply, as well as tax payment and month-end funding needs. As for medium- to long-term liquidity (ORRs, MLFs and net CGB purchase combined), the PBoC might continue to drain in June, but we expect the pace to slow from April and May, as the current YTD cumulative injection is already below that of previous years (except 2021).

Figure 5 shows that, while DR001 already started to grind higher around mid-May, DR007 and 1y NCD yields only began to rebound more significantly since 5 June. This is worth noting, as if only the overnight rate climbs higher but 7d and 1y money market rates remain stable, it would be difficult to conclude there was an increase in broader funding costs. In the past week, with DR007 and 1y NCD yields rising, market expectation for tighter liquidity have been growing as well. Considering large NCD maturities in the next two weeks, tax payment effects (due on 15 June) and a potential pickup in LGB supply in the last week of June, we see further upside in money market rates. We expect the 7d repo fixing to continue moving higher towards $1.50\%$ (or slightly above that) through the rest of June. The monthly average spread may widen to 5-10bp in June from -3bp in May, which is also consistent with seasonality (Figure 6).

Fig. 1: Outstanding OMOs  
![](images/ed3d11ed98cd650d25de3b20008badc0a788d9e42304abffe2ae008102e4f638.jpg)

<details>
<summary>line chart</summary>

| Date | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
| --- | --- | --- | --- | --- | --- | --- |
| 01-Mar | 1800 | 1000 | 1800 | 1800 | 1800 | 1800 |
| 08-Mar | 100 | 400 | 100 | 100 | 700 | 100 |
| 15-Mar | 100 | 100 | 100 | 100 | 1500 | 200 |
| 22-Mar | 100 | 100 | 100 | 100 | 1300 | 300 |
| 29-Mar | 100 | 100 | 1200 | 100 | 1300 | 700 |
| 05-Apr | 100 | 100 | 100 | 100 | 1200 | 700 |
| 12-Apr | 100 | 100 | 100 | 100 | 400 | 100 |
| 19-Apr | 100 | 100 | 100 | 100 | 800 | 100 |
| 26-Apr | 100 | 100 | 750 | 450 | 1650 | 450 |
| 03-May | 100 | 100 | 750 | 450 | 650 | 450 |
| 10-May | 100 | 100 | 750 | 450 | 850 | 450 |
| 17-May | 100 | 100 | 750 | 450 | 450 | 450 |
| 24-May | 100 | 100 | 750 | 950 | 950 | 950 |
| 31-May | 100 | 100 | 750 | 650 | 1650 | 950 |
| 07-Jun | 100 | 100 | 750 | - | - | - |
| 14-Jun | - | - | - | - | - | - |
| 21-Jun | - | - | - | - | - | - |
| 28-Jun | - | - | - | - | - | - |
| - | - | - | - | - | - | - |
| - | - | - | - | - | - | - |
| - | - | - | - | - | - | - |
| - | - | - | - | - | - | - |
</details>

Source: Wind, NOM

Fig. 2: The PBoC's medium- to long-term net liquidity injections (cumulative from the start of the year)  
![](images/8d1647cc04606016616208a5e8a97cfe17e589be3a5846bb6412735f9a751607.jpg)

<details>
<summary>line chart</summary>

| Month | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|------|------|
| Jan   | 100  | 100  | 100  | 100  | 100  | 100  | 100  |
| Feb   | 500  | 500  | 500  | 500  | 500  | 500  | 2000 |
| Mar   | 1000 | 1000 | 1000 | 1000 | 1000 | 1000 | 1800 |
| Apr   | 1200 | 1200 | 1200 | 1200 | 1200 | 1200 | 1400 |
| May   | 1000 | 1000 | 1000 | 1000 | 1000 | 1000 | 500  |
| Jun   | 500  | 500  | 500  | 500  | 500  | 500  | 100  |
| Jul   | 300  | 300  | 300  | 300  | 300  | 300  | -    |
| Aug   | 500  | 500  | 500  | 500  | 500  | 500  | -    |
| Sep   | 750  | 750  | 750  | 750  | 750  | 750  | -    |
| Oct   | 1,250| 1,250| 1,250| 1,250| 1,250| 1,250| -    |
| Nov   | 1,750| 1,750| 1,750| 1,750| 1,750| 1,750| -    |
| Dec   | 2,250| 2,250| 2,250| 2,250| 2,250| 2,250| -    |
</details>

Source: Wind, the PBoC, NOM

Fig. 3: The PBoC's medium- to long-term net liquidity injections  
![](images/17426b7eaf24906509e4baa09db550656eaa12e92d770a1ccad6fec05fc27cad.jpg)

<details>
<summary>bar chart</summary>

| Month   | MLF    | PBoC's net CGB purchase | Outright reverse repo | RRR cut |
|---------|--------|--------------------------|------------------------|---------|
| Jul-24  | 200    | 100                      | 0                      | 0       |
| Sep-24  | -300   | 100                      | 0                      | 700     |
| Nov-24  | -500   | 100                      | 0                      | 1000    |
| Jan-25  | -1200  | 0                        | 1700                   | 0       |
| Mar-25  | -200   | 0                        | 600                    | 0       |
| May-25  | 500    | -500                     | -200                   | 800     |
| Jul-25  | 100    | 0                        | 300                    | 0       |
| Sep-25  | 300    | 0                        | 600                    | 0       |
| Nov-25  | 200    | 0                        | 600                    | 0       |
| Jan-26  | 700    | 100                      | 1100                   | 0       |
| Mar-26  | 300    | 100                      | 900                    | 0       |
| May-26  | 100    | 100                      | -1100                  | 100     |
</details>

Source: Wind, the PBoC, NOM

Fig. 4: Weekly net NCD issuance  
![](images/4631901f3bf9d2a3ca8b90f958807da1b2cf713973c28907ed4d7be0a2499558.jpg)

<details>
<summary>bar chart</summary>

| Month | Net issuance (RMB bn) |
|---|---|
| Jun-25 | -100 |
| Jul-25 | 150 |
| Aug-25 | -150 |
| Sep-25 | 250 |
| Oct-25 | 350 |
| Nov-25 | -400 |
| Dec-25 | -100 |
| Jan-26 | -300 |
| Feb-26 | 350 |
| Mar-26 | -400 |
| Apr-26 | -100 |
| May-26 | 450 |
| Jun-26 | 250 |
| Jul-26 | -600 |
The chart displays the net issuance values for each month from June 2025 to May 2026. The data is presented in a single column format with red bars representing net issuance amounts in RMB billions. There are no additional categories or trends visible in the image. The title of the chart is 'Net issuance'.
</details>

Source: Wind, NOM

Fig. 5: DR001, DR007 and 1y NCD yield  
![](images/86441f22a28b06c8d31269578f44a530d9a612de32bd445f837c2b11fbe9c10e.jpg)

<details>
<summary>line chart</summary>

| Date   | DR001 | DR007 | 7d OMO rate | 1y NCD yield |
|--------|-------|-------|-------------|--------------|
| Jul-25 | 1.35  | 1.45  | 1.4         | 1.6          |
| Aug-25 | 1.55  | 1.55  | 1.4         | 1.65         |
| Sep-25 | 1.35  | 1.45  | 1.4         | 1.65         |
| Oct-25 | 1.45  | 1.55  | 1.4         | 1.68         |
| Nov-25 | 1.35  | 1.45  | 1.4         | 1.65         |
| Dec-25 | 1.45  | 1.55  | 1.4         | 1.68         |
| Jan-26 | 1.25  | 1.45  | 1.4         | 1.65         |
| Feb-26 | 1.35  | 1.45  | 1.4         | 1.6          |
| Mar-26 | 1.35  | 1.45  | 1.4         | 1.55         |
| Apr-26 | 1.3   | 1.4   | 1.4         | 1.5          |
| May-26 | 1.25  | 1.35  | 1.4         | 1.45         |
| Jun-26 | 1.35  | 1.4   | 1.4         | 1.4          |
</details>

Source: Bloomberg, NOM

Fig. 6: Monthly average spread between 7d repo fixing and 7d OMO rate  
![](images/019e51b4200c69bc83dede8f81789931e56353fe8df1e1f28ee59a91a66cf30d.jpg)

<details>
<summary>line chart</summary>

| Month | 2026 | 2025 | 2024 | 2023 |
|-------|------|------|------|------|
| Jan   | 15   | 63   | 43   | 15   |
| Feb   | 17   | 60   | 20   | 30   |
| Mar   | 11   | 48   | 30   | 37   |
| Apr   | 1    | 28   | 15   | 25   |
| May   | -3   | 24   | 8    | -3   |
| Jun   | 0    | 25   | 19   | 17   |
| Jul   |      | 15   | 12   | 5    |
| Aug   |      | 10   | 18   | 10   |
| Sep   |      | 15   | 25   | 20   |
| Oct   |      | 12   | 40   | 48   |
| Nov   |      | 11   | 33   | 58   |
| Dec   |      | 18   | 43   | 64   |
</details>

Source: Wind, Bloomberg, NOM

## Bond supply

As of end-May, 35% of annual net bond financing quota has been completed for both CGBs and LGBs. The CGB issuance pace was slower than in 2025 but still faster than in 2021-2024 (Figure 7). For LGBs, however, issuance over the first five months on 2026 looks slower than in previous years (2021-25 average: 38%; Figure 8). In May 2026, net government bond supply was particularly low (due mainly to LGBs). On one hand, this (together with the super flush liquidity) might explain the large bond buying flows from onshore funds in May, as there was a lack of high-quality assets in the market. On the other hand, it also means bond issuance pressure in coming months can be higher. We expect monthly net CGB and LGB supply to rise to \~RMB1.0trn in June (May: RMB890bn) and further to RMB1.3trn in Q3, before declining to an average of RMB900bn in Q4 (Figure 9).

## Bond demand

As shown in Figure 10, after accumulating massive (ultra) long-end CGBs/policy bank bonds in April and May, onshore funds reduced bond holdings in June. In the first week of June, funds were still adding 10y and above tenors while net selling the front-end and belly parts of the curve. Then this week, the selling extended to the back end as well, and funds sold large amount of 10y policy bank bonds.

On 30y CGBs, while we saw outflows from funds and securities firms starting from 9 June, the size was small relative to inflows seen in previous weeks. While liquidity tightness (or expectations on that) may trigger larger selling flows in 30y CGBs, the currently wide 10s30s spread at \~49bp provides a buffer and would generally support 30y CGB outperformance, in our view. Also, insurance firms' demand for 30y CGBs has clearly picked up this week. This is consistent with their historical buy/sell patterns, as insurance firms tend to add 30y bonds amid selloffs and reduce holdings during rallies. Such flows can gain further momentum if 30y CGB yields climb to 2.25%, which means the upside in yields is also somewhat capped.

We do not expect a significant steepening in the CGB space until we see a meaningful improvement in economic data (especially credit demand and retail sales etc.), or unless liquidity tightens at a much faster pace/by a much larger amount (for example, DR001 to \~1.50%, DR007 to \~1.60%). Thus, we continue to prefer to pay 3y NDIRS over 5y tenors. Also, we believe positioning favors payers, since NDIRS are trading \~3bp below the onshore IRS level, which is slightly wider than the 12-month average.

Fig. 7: Net CGB issuance as percentage of annual quota  
![](image

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
