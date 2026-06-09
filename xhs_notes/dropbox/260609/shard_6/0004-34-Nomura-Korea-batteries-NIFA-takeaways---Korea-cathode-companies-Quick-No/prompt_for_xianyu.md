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
# NIFA takeaways – Korea cathode companies Quick Note

LG Chem (051910 KS, Buy), L&F (066970 KS, Buy), and EcoproBM (247540 KS, Buy) attended the NOM Investment Forum Asia (NIFA) 2026 in Singapore, held over 2-5 June. We note these three cathode companies are taking varying strategic paths to achieve growth and profitability. The following are the key takeaways from the meetings.

## Ecopro BM (EBM) – Hungary cathode plant as a growth driver

Of 244k tpa cathode capacity of EBM, 54ktpa is based in Hungary, with the first line scheduled to commence operations in June, while the second line is expected to start in 2H26E, according to the company. Meanwhile, EBM is working to convert the third line into NCM (nickel cobalt manganese) production with an aim to supply to non-Korea battery plants in Europe. With a concentrated product mix on high-nickel (rather than mid-nickel or LFP) cathode for EV applications, EBM looks well positioned to benefit from the European EV/battery industry, which is witnessing a revival of consumer subsides in the UK/Germany, and a regulatory environment that requires on-shore supply-chain installations (link). Europe's electric vehicle (EV) subsidies are making a comeback. EBM is strengthening upstream/metal integration through Ecopro Group's \~10% stake in Indonesia nickel smelters whose combined capacity is 150k tpa. The Ecopro Group is evaluating Phase 2 investments. In our view, EBM's near-term priorities are the successful ramp-up of the Hungary plant, solid-state cathode from 2027, and the expansion of its Indonesian nickel smelting operations, rather than LFP investments.

## L&F – commercializing first Korean LFP cathode in 3Q26

We project L&F's shipment volumes to rise by 19% y-y to 80k tonne in 2026F, as we expect \~85% of revenue to stem from LG Energy Solution ([373220 KS, Buy] with Tesla [TSLA US, Not rated] being the end-customer. Management noted that L&F would be taking its LFP cathode capacity of 60k tpa in Korea with 30ktpa likely to be commercialized in 3Q26E, and the remaining 30ktpa in 1H27E. Initial production will be supplied to Samsung SDI's (006400 KS, Buy) US ESS battery business under the long-term supply agreement signed in March 2026 (link). L&F sounded optimistic about the LFP cathode profitability outlook, assuming ASP of USD11/kg, although overall profitability likely favors high-nickel cathodes. We believe L&F is well positioned to capture the rapid growth of the US ESS market, which is a large consumer of cost-competitive LFP batteries. As Samsung SDI expands its US ESS footprint, L&F's LFP business could emerge as a meaningful growth contributor; longer out, we see a likelihood of its LFP applications extending to EVs. L&F is working to diversify its LFP customer base, in our view, which may require additional capex if contracts are signed. On the technology front, it is pursuing precursor-free LFP. Cathode production consists of: (1) making NCM precursor, (2) mix precursor with lithium, and (3) high-temperature calcination. Precursor-free LFP means skipping the mixing ingredient part and finalizing much of production in the calcination process. However, technologically, it is challenging as one has to mix metals uniformly, add lithium and also form crystal structure all at once. However, L&F and other industry peers are working to eliminate the calcination process with a goal of lowering cost and reducing dependency in imported Chinese precursor. The company is also working to produce sodium batteries, which can be swing produced from the LFP line.

## LG Chem – Cathode volume improvement, chem restructuring, better TSR

LGC expects cathode shipment recovery to accelerate in 2H26E, supported by the ramp-up of North American battery production and the start of mass production for 2170 cell supplies in 3Q26E. While current utilization is low, improving volumes should drive a gradual recovery in profitability. Management – the new CEO Dong-chun Kim – regards cathode and

## Research Analysts

Asia Energy

Cindy Park - NFIK

cindy.park@NOM.com

+822 3783 2324

Dongmin Lee - NFIK

dongmin.lee@NOM.com

+822 3783 2338

electronics materials as a key growth driver. In addition to existing nickel-based cathode, LGC is preparing to commercialize LFP cathode, possibly by 2027-28E. In battery materials, management acknowledged that its competing peer company gained an early advantage in a leading electric vehicle (EV) OEM customer, but expects LGC's position to improve, targeting a roughly 50:50 share over time (i.e. LGC and competitors share to be roughly 50:50). In ensuring better shareholder returns, LGC: (1) has linked management compensation metrics to ratios such as $>10\%$ ROE, (2) is monitoring its NAV discount at the board level, (3) has reiterated plans to reduce its LG Energy Solution (LGES) stake to $70\%$ over the next five years. On the chemical business, management outlined a restructuring plan centered on forming a JV and rationalizing naphtha cracker (NCC) capacity. The objective is to consolidate roughly 4.0mn tonne of NCC capacity and shut down about 1.0mn tonne, addressing industry oversupply and weak ethylene economics. Management believes significant cost reductions can be achieved through restructuring.

Fig. 1: Korea cathode players: capacity expansion  
![](images/90c9b3a3bec5ed73adef92eb0d73c0f0df87253b87fabf14770b8bcbf518d0c8.jpg)

<details>
<summary>bar chart</summary>

| Company | 2025 (k tpa) | 2030F (k tpa) |
| :--- | :--- | :--- |
| Ecopro BM | 190 | 355 |
| POSCO Future M | 175 | 396 |
| LG Chem | 150 | 300 |
| L&F | 190 | 342 |
</details>

Source: Company data, NOM estimates

Fig. 2: Korea cathode players: shipment forecasts  
![](images/3daec6d6425d4d4643f953698f914c328511e41553fc06cbe8e40e30d536ba0f.jpg)

<details>
<summary>bar chart</summary>

| Company | 2025 (k ton) | 2030F (k ton) |
| :--- | :--- | :--- |
| Ecopro BM | 72 | 214 |
| POSCO Future M | 45 | 239 |
| LG Chem | 38 | 193 |
| L&F | 66 | 188 |
</details>

Source: Company data, NOM estimates

## Appendix A-1

This report has been produced by NOM Financial Investment (Korea) Co., Ltd. (NFIK), Korea.

See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Cindy Park and Dongmin Lee, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>POSCO Future M</td><td>003670 KS</td><td>KRW 187,700</td><td>08-Jun-2026</td><td>Neutral</td><td>N/A</td><td></td></tr><tr><td>LG Chem</td><td>051910 KS</td><td>KRW 321,000</td><td>08-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>L&amp;F</td><td>066970 KS</td><td>KRW 124,600</td><td>08-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>EcoproBM</td><td>247540 KS</td><td>KRW 159,700</td><td>08-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>LG Energy Solution</td><td>373220 KS</td><td>KRW 388,500</td><td>08-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

POSCO Future M (003670 KS)  
Rating and target price chart (three year history)  
![](images/3d83448b8a6de90d86f7aca62132c409e9c32ce6090cd5c3c4504083aae98cb0.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2023/07/01 | ~580000.00    | ~470000.00         | Yes                    |
| 2024/01/01 | ~350000.00    | ~340000.00         | No                     |
| 2024/07/01 | ~250000.00    | ~310000.00         | No                     |
| 2025/01/01 | ~150000.00    | ~240000.00         | No                     |
| 2025/07/01 | ~110000.00    | ~120000.00         | No                     |
| 2026/01/01 | ~280000.00    | ~240000.00         | No                     |
</details>

KRW 187,700 (08-Jun-2026) Neutral (Sector rating: N/A)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>19-Mar-26</td><td></td><td>200,000.00</td><td>198,000.00</td></tr><tr><td>27-Oct-25</td><td></td><td>240,000.00</td><td>245,500.00</td></tr><tr><td>09-Apr-25</td><td></td><td>120,000.00</td><td>117,772.00</td></tr><tr><td>30-Oct-24</td><td></td><td>240,000.00</td><td>221,490.00</td></tr><tr><td>02-Apr-24</td><td></td><td>300,000.00</td><td>278,195.00</td></tr><tr><td>24-Oct-23</td><td></td><td>340,000.00</td><td>295,643.00</td></tr><tr><td>26-Sep-23</td><td></td><td>420,000.00</td><td>356,710.00</td></tr><tr><td>24-Jul-23</td><td>Neutral</td><td></td><td>525,371.00</td></tr><tr><td>24-Jul-23</td><td></td><td>520,000.00</td><td>525,371.00</td></tr><tr><td>23-Jun-23</td><td></td><td>470,000.00</td><td>363,495.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our target price of KRW200,000 is based on DCF methodology. EV valuation currently stands at KRW20.7tn, based on our cathode/anode capacity estimates of 620k/180k tpa for 2035F, EBIT margin of 5.1% (average of 2025-2035F) and a WACC of 6.1%. Our benchmark index is KOSPI 200.

Risks that may impede the achievement of the target price Downside risk — weak 1H26 earnings, lack of meaningful cathode contract win; upside – further order win from global EV OEMs to supply anode or LFP cathode.

## LG Chem (051910 KS)

## KRW 321,000 (08-Jun-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/b507636c1a53410e399632d7f3b00c69b0c5000101067f03c11f310f39faccf0.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2024/07/01 | ~750000.00    | ~580000.00         | Yes                    |
| 2024/01/01 | ~500000.00    | ~560000.00         | Yes                    |
| 2024/07/01 | ~400000.00    | ~420000.00         | Yes                    |
| 2025/01/01 | ~350000.00    | ~420000.00         | Yes                    |
| 2025/07/01 | ~300000.00    | ~360000.00         | Yes                    |
| 2026/01/01 | ~450000.00    | ~540000.00         | Yes                    |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>13-Apr-26</td><td></td><td>440,000.00</td><td>340,000.00</td></tr><tr><td>03-Nov-25</td><td></td><td>540,000.00</td><td>393,000.00</td></tr><tr><td>07-Aug-25</td><td></td><td>360,000.00</td><td>292,500.00</td></tr><tr><td>12-Jun-25</td><td></td><td>300,000.00</td><td>210,500.00</td></tr><tr><td>04-Feb-25</td><td></td><td>280,000.00</td><td>213,000.00</td></tr><tr><td>20-Nov-24</td><td></td><td>420,000.00</td><td>291,500.00</td></tr><tr><td>18-Apr-24</td><td></td><td>550,000.00</td><td>378,500.00</td></tr><tr><td>02-Apr-24</td><td>Buy</td><td></td><td>424,000.00</td></tr><tr><td>02-Apr-24</td><td></td><td>570,000.00</td><td>424,000.00</td></tr><tr><td>30-Oct-23</td><td></td><td>500,000.00</td><td>445,000.00</td></tr><tr><td>26-Sep-23</td><td>Neutral</td><td></td><td>505,000.00</td></tr><tr><td>26-Sep-23</td><td></td><td>580,000.00</td><td>505,000.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our SOTP-based target price of KRW440,000 is based on: 1) chemicals business target enterprise value (EV) of KRW2.9tn; 2) battery valuation of KRW46.9tn, applying 40% discount to LGES market cap (79.4% stake); 3) advanced materials KRW5.4tn; 4) agro chem/pharma KRW0.9tn. Our benchmark index is KOSPI 200.

Risks that may impede the achievement of the target price Downside risks: further chemical margin weakness

## L&F (066970 KS)

## KRW 124,600 (08-Jun-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/f22a33d8b5b84bbb868f9774185f92477fa7a6cea42a835c83007c71a3e8507c.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2023/07/01 | ~280000.00    | -                   | -                      |
| 2024/01/01 | ~210000.00    | ~240000.00         | -                      |
| 2025/01/01 | ~95000.00     | ~110000.00         | ~95000.00              |
| 2025/07/01 | ~75000.00     | ~80000.00          | -                      |
| 2026/01/01 | ~150000.00    | ~200000.00         | ~145000.00             |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>01-Apr-26</td><td>Buy</td><td></td><td>147,400.00</td></tr><tr><td>01-Apr-26</td><td></td><td>200,000.00</td><td>147,400.00</td></tr><tr><td>30-Jul-25</td><td></td><td>80,000.00</td><td>72,000.00</td></tr><tr><td>09-Apr-25</td><td></td><td>65,000.00</td><td>54,000.00</td></tr><tr><td>20-Oct-24</td><td>Neutral</td><td></td><td>98,700.00</td></tr><tr><td>20-Oct-24</td><td></td><td>110,000.00</td><td>98,700.00</td></tr><tr><td>01-Feb-24</td><td></td><td>240,000.00</td><td>152,900.00</td></tr><tr><td>26-Sep-23</td><td></td><td>290,000.00</td><td>170,800.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of KRW200,000 is based on discounted cashflow valuation, where we assume: 1) cathode capacity of 220k/410k tpa in 2026F/35F (2025: 190k tpa); 2) cathode shipments increasing $16\%$ p.a. and ASP decline of $3\%$ p.a. in 2026-35F; 3) average EBIT margin of $5.3\%$ for 2026-35F; and 4) WACC of $5.8\%$

Risks that may impede the achievement of the target price Downside risks: contract cancellation with battery or OEM customers.

## EcoproBM (247540 KS)

## KRW 159,700 (08-Jun-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/ec39e3c4bf89bcc5350f287d3f6853963ac34a7738834e3a1d6e48e499f70b98.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2023/07/01 | ~450000.00    | ~350000.00         | -                      |
| 2024/01/01 | ~280000.00    | ~290000.00         | ●                      |
| 2025/01/01 | ~160000.00    | ~240000.00         | ●                      |
| 2025/07/01 | ~120000.00    | ~150000.00         | ●                      |
| 2026/01/01 | ~220000.00    | ~280000.00         | -                      |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>29-Apr-26</td><td></td><td>280,000.00</td><td>212,500.00</td></tr><tr><td>09-Apr-26</td><td></td><td>270,000.00</td><td>206,000.00</td></tr><tr><td>04-Nov-25</td><td></td><td>200,000.00</td><td>161,800.00</td></tr><tr><td>05-Aug-25</td><td>Buy</td><td></td><td>124,500.00</td></tr><tr><td>05-Aug-25</td><td></td><td>150,000.00</td><td

[中间内容因长度限制已省略]

Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved.
"""
