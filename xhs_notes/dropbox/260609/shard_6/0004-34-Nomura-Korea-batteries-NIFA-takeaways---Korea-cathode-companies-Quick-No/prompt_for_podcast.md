你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>29-Apr-26</td><td></td><td>280,000.00</td><td>212,500.00</td></tr><tr><td>09-Apr-26</td><td></td><td>270,000.00</td><td>206,000.00</td></tr><tr><td>04-Nov-25</td><td></td><td>200,000.00</td><td>161,800.00</td></tr><tr><td>05-Aug-25</td><td>Buy</td><td></td><td>124,500.00</td></tr><tr><td>05-Aug-25</td><td></td><td>150,000.00</td><td>124,500.00</td></tr><tr><td>09-Apr-25</td><td>Neutral</td><td></td><td>94,700.00</td></tr><tr><td>09-Apr-25</td><td></td><td>100,000.00</td><td>94,700.00</td></tr><tr><td>01-Nov-24</td><td>Buy</td><td></td><td>169,700.00</td></tr><tr><td>01-Nov-24</td><td></td><td>240,000.00</td><td>169,700.00</td></tr><tr><td>07-Nov-23</td><td>Neutral</td><td></td><td>284,500.00</td></tr><tr><td>07-Nov-23</td><td></td><td>290,000.00</td><td>284,500.00</td></tr><tr><td>23-Jun-23</td><td></td><td>350,000.00</td><td>263,000.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our target price of KRW280,000 is based on DCF method where we assume cathode valuation (EV) at KRW29.2tn, EBIT margin of 6.1% (average 2026F-35F) and WACC of 6.1%. Our benchmark index is KOSPI 200.

Risks that may impede the achievement of the target price Downside risks: the company's strategic focus/priority of high nickel and solid state batteries may come at the expense of capturing LFP demand.

## LG Energy Solution (373220 KS)

## KRW 388,500 (08-Jun-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/33c7e4dc648018442ab34330e108d05602785acf7909764c244ddc8396edce07.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2023/07/01 | ~600000.00    | -                   | -                      |
| 2024/01/01 | ~450000.00    | ~600000.00         | -                      |
| 2024/07/01 | ~350000.00    | ~550000.00         | -                      |
| 2025/01/01 | ~350000.00    | ~500000.00         | -                      |
| 2025/07/01 | ~280000.00    | -                   | -                      |
| 2026/01/01 | ~480000.00    | ~600000.00         | -                      |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>30-Oct-25</td><td></td><td>600,000.00</td><td>486,500.00</td></tr><tr><td>27-Jan-25</td><td></td><td>500,000.00</td><td>353,500.00</td></tr><tr><td>28-Oct-24</td><td></td><td>600,000.00</td><td>416,500.00</td></tr><tr><td>25-Jul-24</td><td></td><td>500,000.00</td><td>332,500.00</td></tr><tr><td>25-Apr-24</td><td></td><td>560,000.00</td><td>372,500.00</td></tr><tr><td>02-Apr-24</td><td></td><td>570,000.00</td><td>393,000.00</td></tr><tr><td>28-Jan-24</td><td></td><td>610,000.00</td><td>381,000.00</td></tr><tr><td>25-Oct-23</td><td></td><td>620,000.00</td><td>409,500.00</td></tr><tr><td>26-Sep-23</td><td></td><td>700,000.00</td><td>475,500.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology Our TP of KRW600,000 is based on

[中间内容因长度限制已省略]

TABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved.
"""
