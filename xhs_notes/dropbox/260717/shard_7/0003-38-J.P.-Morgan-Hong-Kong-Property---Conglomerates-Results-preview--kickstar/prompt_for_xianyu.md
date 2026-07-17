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
# Hong Kong Property & Conglomerates

Results preview: kickstarting the earnings upcycle

After a 2-3 year earnings downcycle, we believe the upcoming results (to be released from July to November; most are interim, but some are annual results) will kickstart a multi-year earnings upcycle (we forecast a 9% Y/Y earnings growth (Figure 3) and 2-3% Y/Y DPS growth), driven by improving HK DP margins (Table 10), partial stabilization in rental income (Figure 12) & lowering financing costs. In the near term, we expect the sector may continue to be heavily influenced by the interest rate narrative, which is rapidly shifting. In our stock-picking, we prefer companies with (1) lower sensitivity to rates; (2) earnings revival over the next 2-3 years; (3) proactive capital recycling; and (4) improvement in operating data of key sub-sector exposure (e.g. spot rent rebound in Central office; spot rent stabilization in HK retail). Since the overhang of capital outflow control may not be totally removed any time soon, we see higher certainty in landlords over developers in the near term. Top picks: Link REIT, HKL & Swire Prop among landlords; SHKP among developers; CK Hutchison & Jardine Matheson among conglomerates.

## Results preview

\- Most companies will see earnings growth (Figure 1): Both CKH & CKA will likely see $>100\%$ Y/Y earnings growth due to the disposal gains of UKPN (which benefited both companies). Excluding disposal gains, we expect CKH to see $11\%$ Y/Y earnings growth (benefiting from elevated oil prices through Cenovus) while CKA will see a $6\%$ Y/Y decline due to the booking of low-margin DP projects in HK. We expect Henderson to see a strong $42\%$ Y/Y growth due to the booking of The Legacy ( $>50\%$ margin), while the $13\%$ Y/Y jump in Swire Prop's is also due to the booking of HK DP. We expect SHKP to register a $5\%$ Y/Y growth with upside risk if DP margin is better than expected, while JM should see a $3\%$ Y/Y growth despite a drag from Astra. For HKL ( $+10\%$ ), Wharf REIC ( $+2\%$ ) and Link REIT ( $+0\%$ ), the earnings improvement is mostly due to cost savings. For Hang Lung, while we expect core net profit to drop $2\%$ , this is mostly due to a drop in interest capitalization (non-cash); operating profit (which we expect a mild $2\%$ growth) is a better way to assess the company's well-being. We expect an $8\%$ Y/Y drop in Sino's earnings due to smaller DP booking and lower interest income. NWD will likely remain in a net loss, but the loss may narrow due to profit booking of high-margin HK DP projects (The Legacy & Pavilia Farm).

\- Assessing dividend certainty (Figure 2): Apart from NWD (no dividend), we expect all companies to at least maintain a flat DPS. We forecast SHKP, HKL & CKH to deliver \~5% DPS growth, while JM, Swire Prop & Wharf REIC should see 2-3% growth. We see upside risk in CKH (as we expect EPS to grow >10% Y/Y, but historically DPS growth has not necessarily tracked the same as EPS growth) and SHKP (if earnings growth is >5%). We see downside risk to Wharf REIC if the increase in turnover rent is unable to offset the decline in base rent. CKA is another one with higher uncertainty, especially as a special dividend has been anticipated by some investors, but we don’t have 100%

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

conviction that CKA will declare one (based on track record). That said, in our base case, we pencil in a small special DPS to offset the decline in core DPS (thus we expect interim DPS to be flat Y/Y). The following companies should see high certainty in meeting our DPS forecast (likely at least flat): HKL, JM, Swire Prop, Hang Lung, Sino & Henderson. Finally, we expect Link REIT to see a flattish DPS due to cost savings (to be reported in November).

\- Other non-results catalysts: For developers, we believe the following data may be stronger share price drivers: (1) home price momentum; (2) sell-through rates of primary launches; (3) overall sales volumes. For landlords, we believe monthly retail sales data & quarterly office rental data may also be important. Generally, capital recycling is also a key rerating factor. Within our coverage, companies active in recycling include HKL, Swire Prop, Link REIT, JM &CKH. To a lesser extent, CKA might also be considered one, although its asset disposals are relatively passive. Meanwhile, Wharf REIC's potential disposal of its Singapore assets might also be a positive catalyst if executed. Finally, Link REIT, HKL & JM have been active in buyback.

## Sub-sector outlook

Sub-sector preference: In 2H26, in terms of momentum (measured by growth in home prices/rents), our pecking order is HK office (Central only) > HK residential = Mainland China retail = HK discretionary retail > HK staples retail > HK office (ex-Central) > Mainland China office.

## In an upcycle:

\- HK Office (Central only): Since the bottom in 3Q25, spot rents in Central have risen 9%, and due to improvement in vacancy rates (now down to 8.8%) & solid demand from the financial services sector (Figure 6), we expect spot office rents in Central to see another MSD% growth in 2H26 (after a 7-8% jump in 1H26). If the trajectory continues, rental reversion should turn stable in FY27. More discussion can be found in our earlier report on HK commercial property.

\- HK Residential: Year-to-date, HK home prices have surged 11% (stronger than expected) (Figure 4), already reaching our target range of 10-15% for FY26. While we maintain our full-year forecast, this implies home price growth will slow to <5% in 2H26 as the housing market faces 3 major uncertainties (capital outflow control, rate hike concerns, and a bleak stock market), although the last two have recently been eased. We believe the upcycle will continue but the momentum will slow after the strong FOMO sentiment in 1H26 fades. Structurally supportive factors (population inflows, optimal inventory) remain in place (more in our in-depth report). Recent secondary sales volume has slowed (Figure 5), but if the interest rate narrative turns less hawkish & the stock market recovery continues in HK, we see upside risk to the housing market. Sell-through rates of upcoming launches are key to watch, and the next one will be Garden Regency by SHKP this weekend (with >40x over-subscriptions, we expect a 95-100% sell-through rate).

\- Mainland China Retail: Note that for this sub-segment, we only refer to mid/high-end retail in top-tier cities which most HK landlords are exposed to. We estimate HK landlords have achieved a 5-10% Y/Y tenant sales growth in 1H26, outperforming the broader market (+1% Y/Y)(Figure 10). We expect HK landlords to see low-single-digit % positive rental reversion among their malls in Mainland China in FY26.

\- HK Discretionary Retail: Year-to-date, HK discretionary retail sales have risen 17% Y/Y, but are still 20-30% below 2015-18 levels (Figure 7). While negative rental reversion may continue for the next 1-2 years, we expect spot rents to see stable/low-single-digit % growth in FY26. That said, we note that the Y/Y growth in tourist arrivals has been moderating from $>10\%$ in 1Q to $<10\%$ over the past 2 months, and this may drag down the growth momentum.

## Bottoming out:

\- HK Staples Retail: Staples retail sales have risen 5% Y/Y year-to-date, and have already recovered to surpass the average 2015-18 level (Figure 8). Since last year, the sector has faced challenges from cross-border e-commerce like Pinduoduo, but the trend, albeit becoming structural, has stabilized. We believe spot rents should stabilize in 2026, and negative rental reversion may narrow to a MSD% in 2027.

## In a downcycle:

\- HK Office (ex-Central): The HK office market is seeing a K-shaped recovery. While Central has been outperforming, districts outside of Central remain lackluster (particularly Kowloon East) due to high vacancy rates (mid-to-high teens %) (Figure 6). Spot rents (ex-Central) have mildly dropped 1% in 1H26, and we expect a continual low-single-digit % drop in 2H26, mostly dragged by Kowloon East.

\- Mainland China Office: Year-to-date, office rents in tier-1 cities have dropped 4% (Figure 11). With no improvement in vacancy rates (15-20%), we expect another mid-single-digit % drop in 2H26. Fortunately, HK landlords are not heavily exposed to this sub-segment (\~5% of NAV), but with >10% negative rental reversion, this segment will continue to be a drag to HK landlords' rental income.

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td colspan="2">Cur End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>CK Asset Holdings Ltd (1113)</td><td>1113 HK</td><td>21,049</td><td>HKD</td><td>47.14</td><td>OW</td><td>n/c</td><td>52.00</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>Henderson Land Development (0012)</td><td>12 HK</td><td>16,616</td><td>HKD</td><td>26.90</td><td>N</td><td>n/c</td><td>27.00</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>New World Development (0017)</td><td>17 HK</td><td>2,129</td><td>HKD</td><td>6.63</td><td>N</td><td>n/c</td><td>6.80</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>Sino Land (0083)</td><td>83 HK</td><td>13,026</td><td>HKD</td><td>10.65</td><td>OW</td><td>n/c</td><td>12.50</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>Sun Hung Kai Properties (0016)</td><td>16 HK</td><td>45,217</td><td>HKD</td><td>122.30</td><td>OW</td><td>n/c</td><td>140.00</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>Hang Lung Properties (0101)</td><td>101 HK</td><td>4,899</td><td>HKD</td><td>7.38</td><td>OW</td><td>n/c</td><td>12.00</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>Hongkong Land</td><td>HKL SP</td><td>15,802</td><td>USD</td><td>7.40</td><td>OW</td><td>n/c</td><td>10.70</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>Swire Properties (1972)</td><td>1972 HK</td><td>15,955</td><td>HKD</td><td>21.72</td><td>OW</td><td>n/c</td><td>30.00</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr><tr><td>CK Hutchison Holdings (0001)</td><td>1 HK</td><td>35,013</td><td>HKD</td><td>71.65</td><td>OW</td><td>n/c</td><td>79.00</td><td>Jun-27</td><td>n/c</td><td>n/c</td></tr><tr><td>Jardine Matheson</td><td>JM SP</td><td>18,117</td><td>USD</td><td>61.59</td><td>OW</td><td>n/c</td><td>94.00</td><td>Jun-27</td><td>n/c</td><td>Dec-26</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 15 Jul 26.

## 1HFY26 / FY26 / 1HFY27 results preview

## Figure 1: 1H26E / FY26E / 1HFY27E core net profit Y/Y growth

<table><tr><td></td><td>net loss</td></tr><tr><td>CK Hutchison (1H26E) (incl. disposal gain)</td><td>139%</td></tr><tr><td>CK Asset (1H26E) (incl. disposal gain)</td><td>117%</td></tr><tr><td>Henderson Land (1H26E)</td><td>42%</td></tr><tr><td>Swire Prop (1H26E)</td><td>13%</td></tr><tr><td>CK Hutchison (1H26E)</td><td>11%</td></tr><tr><td>HK Land (1H26E)</td><td>10%</td></tr><tr><td>SHKP (FY26E)</td><td>5%</td></tr><tr><td>Jardine Matheson (1H26E)</td><td>3%</td></tr><tr><td>Hang Lung Prop (1H26E) (operating profit)</td><td>2%</td></tr><tr><td>Wharf REIC (1H26E)</td><td>2%</td></tr><tr><td>Link REIT (1HFY27E)</td><td>0%</td></tr><tr><td>Hang Lung Prop (1H26E)</td><td>-2%</td></tr><tr><td>CK Asset (1H26E)</td><td>-6%</td></tr><tr><td>Sino Land (FY26E)</td><td>-8%</td></tr><tr><td>Swire Prop (1H26E) (incl. disposal gain)</td><td>-13%</td></tr><tr><td>NWD (FY26E)</td><td></td></tr></table>

Note: JM's figure has excluded the non-trading items (HKL's DP segment, disposals of businesses at DFI Retail and JC&C, and shift in accounting treatment of Zhongsheng).
Source: Company data, JPM estimates.  
Figure 2: 1H26E / FY26E / 1HFY27E DPS Y/Y growth

![](images/021e636fe1e2f1a124785173bf54348778d6cdcdcae418972d14223b2edb20ad.jpg)  
Source: Company data, JPM estimates.

Core net profit Y/Y

Figure 3: Semi-annual core net profit Y/Y growth  
![](images/d26b55c2c6c744310ee744a3ca6438c3597b74c805fb4a7ee2ee3d5366ffa580.jpg)  
Source: JPM estimates, Company data.
Note: including companies reporting 1H26 results only

# Results preview / what to watch out for

## 1H26 results

## CK Asset (1113.HK) - Overweight

\- Strong headline earnings growth due to disposals: Including disposal gains from UKPN (HK\$8.4bn) and UK Rail (HK\$0.8bn), we forecast a 117% Y/Y growth in headline net profit (HK\$14.8bn).

\- Core net profit growth may, however, remain soft: Excluding disposal gains from UKPN (but including UK Rail), we forecast a 6% Y/Y decline in core net profit to HK\$6.4bn, due to (1) lower profit contribution from HK DP booking (Blue Coast will be booked in 1H26, but we estimate a very low profit contribution due to low margin); (2) smaller DP delivery in Mainland China; (3) decline in rental income (-2%); (4) lower contribution from infrastructure projects due to disposals.

\- Special dividend, if any, will be small: While we forecast interim DPS (excluding special DPS, if any) to drop 6% Y/Y due to lower core net profit, we believe it is possible for CKA to declare a special dividend (due to the earlier disposal gains), which may be distributed in either 1H26 or FY26. However, since we believe CKA's priority is to recoup cash in the near term, we expect the special dividend to be minimal, and may be used as a “balancing figure” to keep interim DPS flat by offsetting the decline in core DPS.

\- Watch out for: (1) any potential special dividend from disposal gains; (2) pricing strategy for upcoming HK residential launches (e.g. Victoria Blossom); (3) capital allocation priorities (especially CKA has likely turned net cash as of end-June 2026 due to disposal proceeds); (4) leasing updates for CKC II; (5) asset disposals.

## Henderson Land (12.HK) - Neutral

\- Strong earnings growth from a low base: We expect core net profit to surge 46% Y/Y to HK\$4.3bn, due to (1) a low base in 1H25 (core net profit fell 44% Y/Y in 1H25 due to a lack of one-off items); (2) higher DP profit contribution from the booking of The Legacy (we estimate a >50% margin & EBIT contribution of HK\$1-2 billion in 1H26), partly offset by projects with lower margin (e.g. Eight Southpark). We expect rental income to remain broadly stable, as the incremental contribution from The Henderson should offset the negative rental reversions in existing properties. We expect a flat interim DPS of HK\$0.5.

\- Farmland resumption may accelerate in 2H26: Based on the latest progress, we do not expect any profit contribution from farmland resumption in 1H26. That said, as the government is scheduled to resume farmland in San Tin and Hung Shui Kiu in September, we expect Henderson to benefit from this, and there could be profit contribution from farmland resumption in 2H26.

\- Watch out for: (1) guidance on progress of farmland resumption; (2) latest DP sales and pricing strategy; (3) latest status of shareholders' loans & progress in deleveraging; (4) leasing updates of Central Yards; (5) appetite for fund raising (e.g. CB).

## Swire Properties (1972.HK) - Overweight

\- Higher DP profit contribution to offset the mild decline in IP profit: We forecast a 13% Y/Y growth in core net profit to HK\$3.9bn (but -13% Y/Y if considering the disposal gains from Miami assets in 1H25). For DP EBIT, we estimate a 68% Y/Y jump to HK\$860mn from the booking of two ultra-luxury houses at 6 Deep Water Bay Road. For 

[中间内容因长度限制已省略]

 date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not
"""
