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
![](images/61cc581fc50364ff93a6f3900e8c651f523263b8356bf6fba7f8a5b82712a784.jpg)

<details>
<summary>line chart</summary>

| Month | 2021 (%) | 2022 (%) | 2023 (%) | 2024 (%) | 2025 (%) | 2026 (%) |
|---|---|---|---|---|---|---|
| Jan | -5 | 0 | 0 | 0 | 6 | 6 |
| Feb | -10 | -5 | 5 | 10 | 12 | 12 |
| Mar | 5 | 0 | 10 | 12 | 17 | 17 |
| Apr | 10 | 5 | 15 | 10 | 25 | 25 |
| May | 15 | 15 | 20 | 25 | 35 | 35 |
| Jun | 20 | 25 | 25 | 30 | 50 | - |
| Jul | 18 | 40 | 25 | 45 | 60 | - |
| Aug | - | 45 | 35 | 65 | 70 | - |
| Sep | - | 65 | 55 | 75 | 80 | - |
| Oct | - | 70 | 65 | 85 | 85 | - |
| Nov | - | 90 | 80 | 95 | 95 | - |
| Dec | - | 100 | 100 | 100 | 100 | - |
</details>

Source: Wind, NOM

Fig. 8: Net LGB issuance as percentage of annual quota  
![](images/07ee3cf561cdc68b620c059535c03078414e1db6a472d34cf2b671fe7b46e96e.jpg)

<details>
<summary>line chart</summary>

| Month | 2021 (%) | 2022 (%) | 2023 (%) | 2024 (%) | 2025 (%) | 2026 (%) |
|---|---|---|---|---|---|---|
| Jan | 0 | 8 | 10 | 5 | 8 | 9 |
| Feb | 0 | 15 | 18 | 12 | 15 | 20 |
| Mar | 0 | 25 | 27 | 18 | 25 | 28 |
| Apr | 10 | 35 | 32 | 22 | 30 | 33 |
| May | 20 | 50 | 45 | 35 | 40 | 35 |
| Jun | 30 | 85 | 60 | 45 | 55 | - |
| Jul | 40 | 88 | 65 | 45 | 60 | - |
| Aug | 50 | 90 | 75 | 60 | 70 | - |
| Sep | 60 | 90 | 85 | 75 | 75 | - |
| Oct | 70 | 98 | 95 | 90 | 85 | - |
| Nov | 80 | 100 | 98 | 95 | 95 | - |
| Dec | 90 | 100 | 100 | 100 | 100 | - |
The chart displays a single data series for each year from January to December. The values are labeled on the lines, and the numerical labels inside the lines are explicitly provided in the table. The title is 'Yearly Percentage Change'. The legend indicates the years: 2021 (gray), 2022 (black), 2023 (orange), 2024 (blue), and 2025 (red). The data points are annotated with numbers such as '8', '20', '32', '35', and '37' above the lines.
</details>

Source: Wind, NOM

Fig. 9: Monthly net CGB and LGB supply  
![](images/34df9e3742df916fda5101b2398c2a5d6334c52fc252afe4b26ac98728f0c2d3.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month | 2026 (RMB bn) | 2025 (RMB bn) | 2020-2024 avg (RMB bn) |
|---|---|---|---|
| Jan | 850 | 760 | 410 |
| Feb | 1000 | 920 | 415 |
| Mar | 680 | 1030 | 490 |
| Apr | 760 | 520 | 260 |
| May | 950 | 1430 | 950 |
| Jun | 980 | 1340 | 990 |
| Jul | 1360 | 1150 | 480 |
| Aug | 1250 | 1420 | 1170 |
| Sep | 1360 | 1210 | 1080 |
| Oct | 1190 | 540 | 620 |
| Nov | 900 | 1150 | 710 |
| Dec | 620 | 510 | 550 |
F
</details>

Source: Wind, NOM

Fig. 10: Onshore funds' net CGB/PFB buying  
![](images/04b7b629e4427a5be4da137b25e49c2777c231db185878100a93fc55f1fe9096.jpg)

<details>
<summary>stacked bar chart</summary>

| Date | <=1y (RMB bn) | 1-3y (RMB bn) | 3-5y (RMB bn) | 5-7y (RMB bn) | 7-10y (RMB bn) | >10y (RMB bn) |
|---|---|---|---|---|---|---|
| 12/29/2025 | - | - 

[中间内容因长度限制已省略]

 SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
