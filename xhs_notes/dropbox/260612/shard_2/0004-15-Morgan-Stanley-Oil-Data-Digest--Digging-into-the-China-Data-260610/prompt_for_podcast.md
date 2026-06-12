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
## Oil Data Digest | Europe

# Digging into the China Data

China has played a significant role in balancing the global oil market over the last few months. In this note we go through the latest data on China's oil trade, refining and demand sectors to understand how Chinese refiners were able to curtail imports by \~5 mb/d over March-May.

China has been a key balancing market in helping the world absorb the supply shock resulting from the closure of the Strait of Hormuz. Chinese refiners have cut crude imports dramatically over March-May, with total May crude imports at \~7.8 mb/d, down 3.2 mb/d YoY and almost \~5 mb/d lower than pre-conflict levels in February. However, observable crude inventory data shows China's crude stocks rising over the course of March and April before eventually drawing in May, which feels inconsistent with the large import cuts.

However, it must be recalled that prior to this conflict China was over-importing on crude for the majority of 2025 and early 2026, aggressively building both commercial and strategic oil inventories. This was true in February 2026, where China's crude balance appeared to be in a \~2.7 mb/d surplus, as crude imports outpaced refinery demand.

Cuts to crude imports therefore came against a backdrop of a strong supply surplus in China and does not mean oil demand has fallen one-for-one with imports. Focusing specifically on April, for which we have the full government dataset, domestic production and net crude imports of 4.4 mb/d and 9.3 mb/d respectively still marginally outpaced refinery demand at 13.4 mb/d. Observable crude inventories showing small builds in April now makes sense. Neither of these datasets are perfect, but directionally they tell the same story.

The drop in crude imports has been partly offset by lower refinery runs and likely depressed end user demand, particularly in petchems. Refinery runs in April were 1.8 mb/d lower than February and down 0.8 mb/d YoY. State-owned refiners have cut runs aggressively to minimise losses as high crude prices, refined product export restrictions and limited ability to pass through cost increases to domestic product prices had combined to turn refining margins negative across China by April. Independent refiners have instead shouldered more of the burden of supplying the domestic market, after being mandated by the government not to cut runs.

Our apparent demand calculation estimates China's underlying end-user oil demand to be running down 1.2 mb/d YoY. Demand declines YoY have been driven by LPG and fuel oil, as petchem facilities have cut run rates and independent refiners have shifted away from fuel oil as a feedstock. Diesel and gasoline demand appears marginally more resilient, as strong mobility data is offset by accelerating NEV sales. However, weak domestic prices do point at an overall soft transport fuel market.

MS & CO. INTERNATIONAL PLC+

## Charlotte Firkins

Commodities Strategist

Charlotte.Firkins@morganstanley.com +44 20 7425-3866

## Martijn Rats, CFA

Equity Analyst and Commodities Strategist

Martijn.Rats@morganstanley.com +44 20 7425-6618

Exhibit 1: Crude net imports fell 2.4 mb/d MoM in April to 9.3 mb/d. Net imports then declined to 7.8 mb/d in May, down 3.2 mb/d YoY.  
![](images/54158a897067124bd18287380c952ed1541950b6f47481c883db332185007195.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 | 5Y Avg | 5Y Range |
|-------|------|------|--------|----------|
| Mar   | 11.5 | 12.5 | 10.5   | 10.5     |
| Jun   | 11.0 | 9.0  | 11.0   | 12.0     |
| Sep   | 11.5 | 8.0  | 10.5   | 11.0     |
| Dec   | 13.0 | 13.0 | 11.0   | 13.0     |
</details>

Source: China General Administration of Customs, MS

Exhibit 2 : Observable Chinese crude inventories continued to build over March and April, based on Vortexa data. Average build rate was \~1.1 mb/d. However, inventories switched to draws in May, with an average draw rate of 750 kb/d.  
![](images/c99116273a95b545a9306fde7896a2d3959613ecb7b6efa519bf3bea8578a17a.jpg)

<details>
<summary>line chart</summary>

China crude inventories (mln bbls)
| Month | 2021 (mbls) | 2022 (mbls) | 2023 (mbls) | 2024 (mbls) | 2025 (mbls) | 2026 (mbls) |
|---|---|---|---|---|---|---|
| Jan | 1200 | 1100 | 1150 | 1080 | 1150 | 1250 |
| Apr | 1180 | 1050 | 1080 | 1070 | 1100 | 1300 |
| Jul | 1150 | 1080 | 1120 | 1100 | 1180 | 1303 |
| Oct | 1100 | 1050 | 1150 | 1120 | 1220 | - |
| Jan | 1080 | 1030 | 1250 | 1140 | 1250 | - |
</details>

Source: Vortexa, MS

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## China Oil Demand Data

China's total apparent oil demand was 1.2 mb/d lower YoY in April, down 8%. Our apparent demand assessment is based on a combination of domestic crude production, refinery runs and net refined product trade data. This gives us an estimate for total refined product supply into the market. Actual consumption is difficult to measure and the lack of comprehensive refined product inventory data means we cannot easily split out final consumption from inventory draws/builds. Consequently, we refer to this assessment as 'apparent demand' rather than a definitive measure of actual consumption.

The drop in apparent demand in April was largely driven by a decline in refinery runs in China, with net refined product exports broadly flat YoY, given both exports and imports were \~500 kb/d lower YoY. Taking the individual calculations for apparent demand by product, a sharp decline in fuel oil and LPG demand appears to explain \~70% of the decline in total apparent oil demand YoY.

Exhibit 3: China's apparent oil demand fell 1.4 mb/d MoM and was 1.2 mb/d lower YoY (-8%) in April  
China Apparent Oil Demand (mb/d)  
![](images/e963529e066e98baccc406c47bb3192a97b1e3b208287617c96ddbe1827d8bef.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 | 5Y Avg | 5Y Range |
|-------|------|------|--------|----------|
| Mar   | 15.9 | 16.2 | 15.2   | 14.8–16.5 |
| Jun   | 15.4 | 14.3 | 15.7   | 13.8–16.5 |
| Sep   | 16.1 |      | 15.6   | 13.5–16.5 |
| Dec   | 15.9 |      | 15.2   | 13.4–16.0 |
</details>

China Apparent Oil Demand YoY (mb/d)

![](images/9a95eafb628b3d95e0616f3d96dc135396557472f41ce105987e3cd31f7cbac9.jpg)

<details>
<summary>bar chart</summary>

| Year | Value |
| ---- | ----- |
| 2021 | 3.00 |
| 2022 | -1.00 |
| 2023 | -1.50 |
| 2024 | 2.80 |
| 2025 | -1.00 |
| 2026 | -1.20 |
</details>

Source: China General Administration of Customs, MS

Apparent diesel demand in China fell to 3.7 mb/d in April, down 2% YoY. Apparent diesel demand in April averaged 210 kb/d lower than pre-conflict demand in February, although on a YoY basis diesel demand is only down 70 kb/d, indicating soft demand but not widespread demand destruction. Manufacturing activity declined over March to May, however still remained higher than a year ago. This firm industrial demand for diesel helped offset declines in the transport sector. In general, road fuel consumers in China have been partly protected from price increases. The government has limited pass through of higher refined product prices from refiners to consumers in China, only raising retail prices but half of what would usually have been passed through under the pricing mechanism. This may help explain the relatively small decline in apparent demand YoY.

Accelerated deployment of LNG and NEV heavy trucks is eroding diesel demand in China, driven by rising oil prices and expectations of firm trucking demand at the start of 2026. Although retail diesel price rises have been capped, high fuel price volatility and expectations of future price hikes is still incentivising switching to NEVs or LNG trucks at the margin. Argus estimates that diesel displacement by new energy and LNG heavy trucks increased by 230 kb/d on the year in January-March, based on mileage data. LNG trucks remain an attractive prospect, as LNG is still the cheaper fuel on a energy equivalent basis, with LNG heavy truck penetration in sales reaching 26% in April. China's domestic electric heavy truck sales grew by over 90% YoY in May, taking estimates of domestic penetration to \~40% in May, up from \~30% sales penetration in January (CVWorld, June 2nd). Expectations of a stronger manufacturing sector in 2026, as the uncertainty from US tariffs faded, boosted expectations of trucking demand and prompted heavy truck fleet build out into 2026.

China's manufacturing PMI peaked in March but then saw two months of consecutive decline over April and May, indicating weakening manufacturing activity. Slowing new orders was a driver of the declining PMI prints, partly reflecting business uncertainty around impacts from events in the Middle East. A slowdown in fiscal spending has also weighed on new orders, with construction business activity a noticeable laggard. However, despite the weakening trend, PMIs remained in expansion territory (>50) over March and April before dropping back to 49.9 in May. PMIs were also higher than April and May 2025 levels, when the US-China trade war weighed on business activity, indicating improved industrial activity YoY. New orders for export specifically remained strong in Mar-Apr, likely reflecting strength in key energy-transition related exports, such as EVs, batteries and solar products amid the energy shock (see here).

Exhibit 4: Apparent diesel demand fell 100 kb/d MoM and was down 70 kb/d YoY (-2%) in April  
![](images/3afaf13e634f7bf7e51d8e983574c910a8a6fb6deca7ac14c1d2e757411506a9.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 | 5Y Avg | 5Y Range |
|-------|------|------|--------|----------|
| Mar   | 3.9  | 3.9  | 3.7    | 3.8      |
| Jun   | 4.0  | 3.7  | 3.6    | 4.0      |
| Sep   | 4.1  | 4.0  | 4.0    | 4.1      |
| Dec   | 4.1  | 4.1  | 4.1    | 4.1      |
</details>

![](images/08107a78da69beb64cd0014f9a6c020a7a9ab448aca9b5d0ed24a40befaafb1a.jpg)

<details>
<summary>bar chart</summary>

| Year | Demand (mb/d) |
| --- | --- |
| 2022 | 0.83 |
| 2022 | 1.09 |
| 2022 | 0.99 |
| 2022 | 0.84 |
| 2022 | 0.91 |
| 2023 | -0.05 |
| 2023 | 0.04 |
| 2023 | 1.31 |
| 2023 | 0.91 |
| 2023 | 0.29 |
| 2023 | 0.01 |
| 2024 | 0.27 |
| 2024 | 0.51 |
| 2024 | 1.03 |
| 2024 | 0.81 |
| 2024 | 1.33 |
| 2024 | 1.01 |
| 2025 | -0.07 |
| 2025 | -0.11 |
| 2025 | 0.28 |
| 2025 | 0.04 |
| 2025 | -0.34 |
| 2025 | -0.47 |
| 2026 | -0.38 |
| 2026 | -0.39 |
| 2026 | -0.19 |
| 2026 | -0.11 |
| 2026 | -0.17 |
| 2026 | -0.19 |
| 2027 | -0.19 |
| 2027 | -0.19 |
| 2027 | -0.19 |
| 2027 | -0.19 |
| 2027 | -0.19 |
| 2028 | -0.19 |
| 2028 | -0.19 |
| 2028 | -0.19 |
| 2028 | -0.19 |
| 2028 | -0.19 |
| 2029 | -0.19 |
| 2029 | -0.19 |
| 2030 | -0.19 |
| 2030 | -0.19 |
| 2031 | -0.19 |
| 2031 | -0.19 |
| 2032 | -0.19 |
| 2032 | -0.19 |
| 2033 | -0.19 |
| 2033 | -0.19 |
| 2034 | -0.19 |
| 2034 | -0.19 |
| 2035 | -0.19 |
| 2035 | -0.19 |
| 2036 | -0.19 |
| 2036 | -0.19 |
| 2037 | -0.19 |
| 2037 | -0.19 |
| 2038 | -0.19 |
| 2038 | -0.19 |
| 2039 | -0.19 |
| 2039 | -0.19 |
| 2040 | -0.19 |
| 2040 | -0.19 |
| 2041 | -0.19 |
| 2041 | -0.19 |
| 2042 | -0.19 |
| 2042 | -0.19 |
| 2043 | -0.19 |
| 2043 | -0.19 |
| 2044 | -0.19 |
| 2044 | -0.19 |
| 2045 | -0.19 |
| 2045 | -0.19 |
| 2046 | -0.19 |
| 2046 | -0.19 |
| 2047 | -0.19 |
| 2047 | -0.19 |
| 2048 | -0.19 |
| 2048 | -0.19 |
| 2049 | -0.19 |
| 2049 | -0.19 |
| 2050 | -0.19 |
| 2050 | -0.19 |
| 2051 | -0.19 |
| 2051 | -0.19 |
| 2052 | -0.19 |
| 2052 | -0.19 |
| 2053 | -0.19 |
| 2053 | -0.19 |
| 2054 | -0.19 |
| 2054 | -0.19 |
| 2055 | -0.19 |
| 2055 | -0.19 |
| 2056 | -0.19 |
| 2056 | -0.19 |
| 2057 | -0.19 |
| 2057 | -0.19 |
| 2058 | -0.19 |
| 2058 | -0.19 |
| 2059 | -0.19 |
| 2059 | -0.19 |
| 2060 | -0.19 |
| 2060 | -0.19 |
| 2061 | -0.19 |
| 2061 | -0.19 |
| 2062 | -0.19 |
| 2062 | -0.19 |
| 2063 | -0.19 |
| 2063 | -0.19 |
| 2064 | -0.19 |
| 2064 | -0.19 |
| 2065 | -0.19 |
| 2065 | -0.19 |
| 2066 | -0.19 |
| 2066 | -0.19 |
| 2067 | -0.19 |
| 2067 | -0.19 |
</details>

Source: China State Statistical Bureau/General Administration of Customs, Oilchem, MS

Apparent gasoline demand fell 290 kb/d MoM in April to 3.2 mb/d. Although gasoline demand appeared 2% higher YoY, April 2025 represented a very weak base. Meanwhile, the strong growth YoY in apparent gasoline demand observed over Jan-Feb has largely been eroded. NEV deployment continues at pace in the passenger sector in China, with data from the China Passenger Car Association showing sales penetration reaching 51% in March and 61% in April, up from 39% in January. ICE vehicle sales meanwhile have shrunk 37% YoY, dragging down overall numbers of passenger vehicle sales in April.

Argus estimates that Chinese gasoline demand is relatively insensitive to small prices rises up to the +\$5-7/bbl threshold, at which point demand destruction accelerates. By the end of April, retail prices for gasoline had risen by \$30/bbl, passing through the sensitivity level of Chinese consumer. One independent refiner in Shandong with an integrated retail arm says its pump sales were around 20% lower in March-April compared with February (Argus 30th).

Into May, record EV use likely capped upside to gasoline demand despite record travel numbers for the Labor Day May holiday in China. Cross-regional passenger trips during the 1-5 May holiday rose by 3.5% YoY to a record 1.52 bln, Ministry of Transport data show. However, this appears to have not translated into higher retail gasoline sales, as rising EV and high-speed train use is weakening the link between public holidays and gasoline consumption. National Energy Administration data shows highway charging volumes for NEVs rose by 53% YoY during the 1-5 of May, with the transport ministry estimating that NEVs would account for around 24% of vehicles on highways during the holiday. Meanwhile, some gasoline retailers reported holiday sales were down by around 10-30% from a year earlier, with declines reaching as much as 50% in some of the more developed eastern and southern regions (Argus May 7th). This is despite independent refiners in Shandong cutting wholesale gasoline prices ahead of the holiday, in order to spur de-stocking.

Exhibit 5: Apparent gasoline demand fell 290 kb/d MoM but was up 60 kb/d YoY (+2%) in April  
![](images/dcd8dafc74907a1fabc8476dda5bfb1a998f7ec6ae7b3b1037f70b4e2f4529ff.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 | 5Y Avg | 5Y Range |
|-------|------|------|--------|----------|
| Mar   | 3.6  | 3.7  | 3.5    | 3.7      |
| Jun   | 3.2  | 3.2  | 3.3    | 3.5      |
| Sep   | 3.5  | 3.4  | 3.4    | 3.7      |
| Dec   | 3.3  | 3.2  | 3.2    | 3.4      |
</details>

Source: China State Statistical Bureau/General Administration of Customs, MS

![](images/1500bef94f0eaaea94b137ece434ad41d42f8c29767446f4c1c2abecded7814b.jpg)

<details>
<summary>bar chart</summary>

China apparent gasoline demand YoY (mb/d)
| Year | Gas demand (mb/d) |
| :--- | :--- |
| 2022 | 0.41 |
| 2023 | -0.75 |
| 2024 | 0.63 |
| 2025 | -0.18 |
| 2026 | 0.23 |
</details>

Exhibit 6: Traffic levels in China have tracked broadly flat YoY over May  
![](images/6a43fcb9b91227ac7dbc863465a0d619b33120e4aa1f79dc0214c424ac6c7db0.jpg)

<details>
<summary>line chart</summary>

| Month | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|------|
| Jan   | ~130 | ~135 | ~135 | ~135 | ~135 | ~135 |
| Apr   | ~140 | ~145 | ~145 | ~145 | ~145 | ~145 |
| Jul   | ~130 | ~135 | ~135 | ~135 | ~135 | ~135 |
| Oct   | ~160 | ~165 | ~165 | ~165 | ~165 | ~165 |
| Jan   | ~140 | ~145 | ~145 | ~145 | ~145 | ~145 |
</details>

Source: BNEF, Baidu, MS

Exhibit 7: China flight numbers were down 1% YoY in April, driven by a decline in domestic flight numbers.  
![](images/79bb0753adeccfe9037a572dbd2b63aba01c60ce6224ebda2604baf700ab13ab.jpg)

<details>
<summary>bar chart</summary>

China Domestic and International Flight numbers (thousands)
| Date | Domestic Flight Number (thousands) |
| :--- | :--- |
| Sep 2025 | 102 |
| Oct 2025 | 104 |
| Nov 2025 | 108 |
| Dec 2025 | 118 |
| Jan 2026 | 117 |
| Feb 2026 | 119 |
| Mar 2026 | 119 |
| Apr 2026 | 120 |
| May 2026 | 119 |
| Jun 2026 | 113 |
| Jul 2026 | 106 |
| Aug 2026 | 107 |
| Sep 2026 | 107 |
| Oct 2026 | 111 |
| Nov 2026 | 116 |
| Dec 2026 | 109 |
| Jan 2027 | 106 |
| Feb 2027 | 105 |
| Mar 2027 | 103 |
| Apr 2027 | 101 |
| May 2027 | 101 |
| Jun 2027 | 103 |
| Jul 2027 | 103 |
| Aug 2027 | 103 |
| Sep 2027 | 103 |
| Oct 2027 | 103 |
| Nov 2027 | 103 |
| Dec 2027 | 103 |
| Jan 2028 | 103 |
| Feb 2028 | 103 |
| Mar 2028 | 103 |
| Apr 2028 | 103 |
| May 2028 | 103 |
| Jun 2028 | 103 |
| Jul 2028 | 103 |
| Aug 2028 | 103 |
| Sep 2028 | 103 |
| Oct 2028 | 103 |
| Nov 2028 | 103 |
| Dec 2028 | 103 |
| Jan 2029 | 103 |
| Feb 2029 | 103 |
| Mar 2029 | 103 |
| Apr 2029 | 103 |
| May 2029 | 103 |
| Jun 2029 | 103 |
| Jul 2029 | 103 |
| Aug 2029 | 103 |
| Sep 2029 | 103 |
| Oct 2029 | 103 |
| Nov 2029 | 103 |
| Dec 2029 | 103 |
| Jan 21, 2030 | 103 |
| Feb 21, 2030 | 103 |
| Mar 21, 2030 | 103 |
| Apr 21, 2030 | 103 |
| May 21, 2030 | 103 |
| Jun 21, 2030 | 103 |
| Jul 21, 2030 | 103 |
| Aug 21, 2030 | 103 |
| Sep 21, 2030 | 103 |
| Oct 21, 2030 | 103 |
| Nov 21, 2030 | 103 |
| Dec 21, 2030 | 103 |
| Jan 22, 2031 | 103 |
| Feb 22, 2031 | 103 |
| Mar 22, 2031 | 103 |
| Apr 22, 2031 | 103 |
| May 22, 2031 | 103 |
| Jun 22, 2031 | 103 |
| Jul 22, 2031 | 103 |
| Aug 22, 2031 | 103 |
| Sep 22, 2031 | 103 |
| Oct 22, 2031 | 103 |
| Nov 22, 2031 | 103 |
| Dec 22, 2031 |
</details>

Source: BNEF, MS

Apparent jet fuel demand fell 200 kb/d MoM in April, falling broadly flat YoY. Jet fuel demand is down 410 kb/d vs February levels vs a usual seasonal Feb-Apr decline of 210 kb/d. However, on a YoY basis jet fuel demand appears broadly flat, indicating flight growth has been curtailed but there has

[中间内容因长度限制已省略]

ational Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
