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
## Korea Chemicals

## May NBL/SBR margins surge to five-year highs as naphtha/LPG shortage triggers rubber tightness

According to Korea Customs data, Korea NBL prices increased by 3.4% m/m to \$1,633/t in May, and the Apr-May average price of \$1,606/t is the highest in five years. This is attributable to: 1) naphtha supply shortage post the Middle East war – we forecast a >20% q/q decline in 2Q26 NBL volumes for Kumho, and 2) improved demand for Malaysian medical gloves due to US restocking. We estimate that NBL margins have expanded to \$916/t – exceeding SBR for the first time since 2022 and the highest since 2021. Key beneficiaries include Kumho Petchem and LG Chem, for which we forecast 2Q chems OP to increase q/q despite lower volumes. Our APAC top pick remains Nan Ya Plastics.

- Rubber feedstock costs fall alongside oil: Asia Butadiene prices have fallen by -27% in May, versus 4-year highs of \$1945/t in April. This mainly reflects a decline in oil prices, the restart of naphtha crackers following scheduled maintenance and lower ABS/SBR utilizations amid weaker demand/margins. The fall in butadiene contrasts with continued strength in NBL prices (+3% m/m) and SBR (-13% m/m), which, in our view, indicates continued supply tightness.  
- Malaysian glove makers struggling with feedstock shortage: Malaysian glove makers import 64% of their NBL requirements, the majority of which is from Korea. As shown in Figure 3, Korea NBL exports averaged only 44kt in Apr-May, 33% lower vs the average monthly volume in 1Q26. According to Bloomberg, WRP Asia Pacific announced a winddown of its operations with effect from 15 April, citing a liquidity crunch caused by raw material shortages.  
- NBL price forecast: As shown in Figure 1, we forecast a gradual decline in NBL prices to \$1281/t in 3Q26 and \$1083/t in 4Q26, reflecting 2H26 oil prices of around \$90/bbl. We expect robust NBL S-D through 2028, given negligible capacity addition globally. We forecast a Korea NBL price of \$940/t in 2027 and \$890/t in 2028, well above the 2023-25 average of \$786/t despite similar oil prices.

## Head of Asia Energy & Chemicals | Asia EV Battery

Parsley Ong AC

(65) 6882-8578

parsley.rh.ong@JPM.com

JPM Securities Singapore Private Limited/

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Michelle Wong

(852) 2800 8556

michelle.wong@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Vicky Hsia

(852) 2800 3752

vicky.hsia@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Figure 1: JPM NBL price forecast (\$/t)

<table><tr><td></td><td>1Q26</td><td>2Q26e</td><td>3Q26e</td><td>4Q26e</td><td>1Q27e</td><td>2Q27e</td><td>3Q27e</td><td>4Q27e</td><td>1Q28e</td><td>2Q28e</td><td>3Q28e</td><td>4Q28e</td></tr><tr><td>Korea NBL price ($/t)</td><td>736</td><td>1,572</td><td>1,281</td><td>1,083</td><td>974</td><td>946</td><td>927</td><td>913</td><td>903</td><td>894</td><td>886</td><td>878</td></tr></table>

Source: Korea Customs, JPM estimates.

Figure 2: Korea NBL price (\$/t)  
![](images/33f4cb08bd5441c426b4c8409634f00ea80b78e1154fa33e93f761e0ac7f4df4.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jan-20 | 900   |
| May-20 | 800   |
| Sep-20 | 1,000 |
| Jan-21 | 1,900 |
| May-21 | 2,100 |
| Sep-21 | 1,800 |
| Jan-22 | 1,000 |
| May-22 | 1,050 |
| Sep-22 | 900   |
| Jan-23 | 700   |
| May-23 | 850   |
| Sep-23 | 650   |
| Jan-24 | 750   |
| May-24 | 850   |
| Sep-24 | 850   |
| Jan-25 | 800   |
| May-25 | 750   |
| Sep-25 | 700   |
| Jan-26 | 650   |
| May-26 | 1,600 |
</details>

Source: Korea Customs, JPM Asia Energy Research.

Figure 3: Korea NBL export volume (kt)  
![](images/c5f4316305cfdf0a22b8dc99c700957da6e6d046ce84362aa2757575a7163e9d.jpg)

<details>
<summary>bar chart</summary>

| Month | Value |
|---|---|
| Jan-22 | 52 |
| Feb-22 | 51 |
| Mar-22 | 54 |
| Apr-22 | 57 |
| May-22 | 45 |
| Jun-22 | 30 |
| Jul-22 | 30 |
| Aug-22 | 34 |
| Sep-22 | 35 |
| Oct-22 | 38 |
| Nov-22 | 33 |
| Dec-22 | 43 |
| Jan-23 | 50 |
| Feb-23 | 56 |
| Mar-23 | 37 |
| Apr-23 | 40 |
| May-23 | 44 |
| Jun-23 | 51 |
| Jul-23 | 54 |
| Aug-23 | 53 |
| Sep-23 | 53 |
| Oct-23 | 52 |
| Nov-23 | 43 |
| Dec-23 | 51 |
| Jan-24 | 57 |
| Feb-24 | 50 |
| Mar-24 | 65 |
| Apr-24 | 55 |
| May-24 | 67 |
| Jun-24 | 70 |
| Jul-24 | 79 |
| Aug-24 | 71 |
| Sep-24 | 69 |
| Oct-24 | 52 |
| Nov-24 | 64 |
| Dec-24 | 73 |
| Jan-25 | 57 |
| Feb-25 | 58 |
| Mar-25 | 63 |
| Apr-25 | 64 |
| May-25 | 69 |
| Jun-25 | 64 |
| Jul-25 | 66 |
| Aug-25 | 74 |
| Sep-25 | 58 |
| Oct-25 | 67 |
| Nov-25 | 75 |
| Dec-25 | 67 |
| Jan-26 | 66 |
| Feb-26 | 65 |
| Mar-26 | 45 |
| Apr-26 | 42 |
</details>

Source: Korea Customs, J.P., Morgan Asia Energy Research.

Figure 4: Key chemical spreads for Kumho Petchem  
Monthly spread data (\$/tonne)  
BPA vs Phenol  
![](images/2d7e36c7c56233dadaed5800128322c9f831331f8feffc9c33ad16f15405d382.jpg)

<details>
<summary>line chart</summary>

| Date    | Value |
|---------|-------|
| Jun-14  | ~500  |
| Feb-15  | ~600  |
| Oct-15  | ~300  |
| Jun-16  | ~400  |
| Feb-17  | ~500  |
| Oct-17  | ~600  |
| Jun-18  | ~700  |
| Feb-19  | ~400  |
| Oct-19  | ~300  |
| Jun-20  | ~500  |
| Feb-21  | ~1,500|
| Oct-21  | ~2,500|
| Jun-22  | ~500  |
| Feb-23  | ~400  |
| Oct-23  | ~500  |
| Jun-24  | ~400  |
| Feb-25  | ~500  |
| Oct-25  | ~700  |
</details>

Phenol vs Benzene  
![](images/8c7b9b5909c69e30538af5d6c4708b4c49a3e33b562443a33a6c032f72e5b90f.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun-14 | 200   |
| Feb-15 | 400   |
| Oct-15 | 250   |
| Jun-16 | 200   |
| Feb-17 | 50    |
| Oct-17 | 150   |
| Jun-18 | 700   |
| Feb-19 | 600   |
| Oct-19 | 300   |
| Jun-20 | 250   |
| Feb-21 | 350   |
| Oct-21 | 450   |
| Jun-22 | 350   |
| Feb-23 | 50    |
| Oct-23 | -100  |
| Jun-24 | 100   |
| Feb-25 | 50    |
| Oct-25 | 0     |
</details>

China polycarbonate price (\$/t)  
![](images/d2666cb2840c328375ac2349f96e1a8f9cdfa507c46214171f9f3cbd80d54511.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jan-14 | 3000  |
| Jan-15 | 2900  |
| Jan-16 | 2800  |
| Jan-17 | 3200  |
| Jan-18 | 4500  |
| Jan-19 | 3500  |
| Jan-20 | 1800  |
| Jan-21 | 3500  |
| Jan-22 | 4500  |
| Jan-23 | 2500  |
| Jan-24 | 2300  |
| Jan-25 | 2200  |
| Jan-26 | 2400  |
</details>

SBR & NBL spread (\$/t)  
![](images/61d3a0b556456cdd540f5c6800061dfec52bc2e186a162ef11e0d27adcf3baf2.jpg)

<details>
<summary>line chart</summary>

| Date   | NBL spread | SBR spread |
|--------|------------|------------|
| Jan-20 | 400        | 350        |
| Jun-20 | 500        | 400        |
| Nov-20 | 700        | 500        |
| Apr-21 | 1,400      | 900        |
| Sep-21 | 1,100      | 800        |
| Feb-22 | 500        | 600        |
| Jul-22 | 300        | 400        |
| Dec-22 | 250        | 350        |
| May-23 | 300        | 450        |
| Oct-23 | 250        | 500        |
| Mar-24 | 300        | 600        |
| Aug-24 | 350        | 700        |
| Jan-25 | 300        | 650        |
| Jun-25 | 250        | 600        |
| Nov-25 | 200        | 550        |
| Apr-26 | 150        | 900        |
</details>

MDI spread (\$/tonne)  
![](images/e019306b0fc9cbd291155c7d62bc9002bbc344a851c5d4c2792688df74ea2419.jpg)

<details>
<summary>line chart</summary>

| Date    | Value |
|---------|-------|
| May-14  | 800   |
| Jan-15  | 1300  |
| Sep-15  | 600   |
| May-16  | 700   |
| Jan-17  | 1000  |
| Sep-17  | 2000  |
| May-18  | 3700  |
| Jan-19  | 1500  |
| Sep-19  | 800   |
| May-20  | 1000  |
| Jan-21  | 3500  |
| Sep-21  | 1800  |
| May-22  | 1400  |
| Jan-23  | 2200  |
| Sep-23  | 1400  |
| May-24  | 1300  |
| Jan-25  | 1200  |
| Sep-25  | 1100  |
| May-26  | 1700  |
</details>

ABS spread  
![](images/581fb2304621126c4fbd25f279868cf3407e8471a9ac274248487e4487568d10.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jun-14 | 200   |
| Feb-15 | 400   |
| Oct-15 | 200   |
| Jun-16 | 200   |
| Feb-17 | 500   |
| Oct-17 | 400   |
| Jun-18 | 0     |
| Feb-19 | 200   |
| Oct-19 | 400   |
| Jun-20 | 800   |
| Feb-21 | 1,100 |
| Oct-21 | 800   |
| Jun-22 | 400   |
| Feb-23 | 200   |
| Oct-23 | 200   |
| Jun-24 | 300   |
| Feb-25 | 300   |
| Oct-25 | 400   |
</details>

Monthly data, priced as of 8-Jun-26. Source: IHS, JPM Asia Energy Research  
Source: Chemical Market Analytic, Korea Customs, Bloomberg Finance L.P., JPM Asia Energy Research.

Companies Discussed in This Report (all prices in this report as of market close on 08 June 2026, unless otherwise indicated) Kumho Petrochemical(011780.KS/W118,600/OW), LG Chem Ltd(051910.KS/W319,500/OW), Nan Ya Plastics Corp(1303.TW/NT\$97.50/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Kumho Petrochemical, LG Chem Ltd, Nan Ya Plastics Corp or related entities.  
- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of LG Chem Ltd or related entities.  
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Kumho Petrochemical, LG Chem Ltd, Nan Ya Plastics Corp or related entities.  
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Kumho Petrochemical, LG Chem Ltd, Nan Ya Plastics Corp or related entities.  
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: LG Chem Ltd or related entities.  
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from LG Chem Ltd or related entities.  
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Kumho Petrochemical, LG Chem Ltd, Nan Ya Plastics Corp or related entities.  
- Debt Position: JPM may hold a position in the debt securities of Kumho Petrochemical, LG Chem Ltd, Nan Ya Plastics Corp or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Kumho Petrochemical (011780.KS, 011780 KS) Price Chart  
![](images/f8d387598abe88da9ba1c3ffd516afe70bc8a2df4306914ada79772149b7d8e3.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(W) |
| ---------- | -------- |
| Sep 23     | 110,000  |
| May 24     | 170,000  |
| Sep 25     | 145,000  |
| Jan 26     | 135,000  |
| May 26     | 150,000  |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>04-Aug-23</td><td>UW</td><td>126000</td><td>110,000</td></tr><tr><td>05-Aug-24</td><td>OW</td><td>141500</td><td>170,000</td></tr><tr><td>01-Aug-25</td><td>OW</td><td>122300</td><td>145,000</td></tr><tr><td>09-Nov-25</td><td>OW</td><td>111100</td><td>135,000</td></tr><tr><td>07-May-26</td><td>OW</td><td>141400</td><td>150,000</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Oct 30, 2017. All share prices are as of market close on the previous business day.

LG Chem Ltd (051910.KS, 051910 KS) Price Chart  
![](images/3cb81458e44c06b766ea3ae6208fe99f266dce0722134e646c057cd252a03641.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(W) |
| ---------- | -------- |
| Sep 23     | 750k     |
| Jan 24     | 500k     |
| May 24     | 400k     |
| Sep 24     | 350k     |
| Jan 25     | 250k     |
| May 25     | 200k     |
| Sep 25     | 300k     |
| Jan 26     | 400k     |
| May 26     | 350k     |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (W)</td><td>Price Target (W)</td></tr><tr><td>31-Oct-23</td><td>OW</td><td>445000</td><td>560,000</td></tr><tr><td>25-Jan-24</td><td>OW</td><td>400500</td><td>520,000</td></tr><tr><td>23-Apr-24</td><td>OW</td><td>378000</td><td>460,000</td></tr><tr><td>01-May-24</td><td>OW</td><td>402500</td><td>470,000</td></tr><tr><td>26-Jul-24</td><td>OW</td><td>313000</td><td>410,000</td></tr><tr><td>08-Oct-24</td><td>OW</td><td>359000</td><td>450,000</td></tr><tr><td>09-Nov-24</td><td>OW</td><td>303000</td><td>380,000</td></tr><tr><td>04-Feb-25</td><td>OW</td><td>222000</td><td>325,000</td></tr><tr><td>01-May-25</td><td>OW</td><td>216000</td><td>280,000</td></tr><tr><td>01-Jul-25</td><td>OW</td><td>211500</td><td>290,000</td></tr><tr><td>09-Jul-25</td><td>OW</td><td>254500</td><td>305,000</td></tr><tr><td>27-Jul-25</td><td>OW</td><td>307000</td><td>360,000</td></tr><tr><td>27-Oct-25</td><td>OW</td><td>400000</td><td>480,000</td></tr><tr><td>30-Jan-26</td><td>OW</td><td>345500</td><td>400,000</td></tr><tr><td>01-May-26</td><td>OW</td><td>398000</td><td>460,000</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Oct 08, 2002. All share prices are as of market close on the previous business day.

Nan Ya Plastics Corp (1303.TW, 1303 TT) Price Chart  
![](images/a15795723d90708fa83981e7d8a1468ff1cfff1e9b98d584838be46cbcc08b9a.jpg)

<details>
<summary>line chart</summary>

| Date       | Price(NT$) |
| ---------- | ---------- |
| Sep 23     | 65         |
| May 24     | 52.5       |
| Jan 25     | 24         |
| Sep 25     | 50         |
| Jan 26     | 70         |
| May 26     | 120        |
| Jan 27     | 80         |
| May 27     | 125        |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (NT$)</td><td>Price Target(NT$)</td></tr><tr><td>28-Jun-23</td>

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jun 2026 10:15 PM HKT

Disseminated 08 Jun 2026 10:15 PM HKT
"""
