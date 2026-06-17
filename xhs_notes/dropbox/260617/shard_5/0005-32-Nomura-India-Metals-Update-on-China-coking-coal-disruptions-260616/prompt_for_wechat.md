你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
EQUITY: METALS & MINING

# Update on China coking coal disruptions

China coking coal supply resumes, but recovery remains uneven; seaborne prices stable for now

## Mine restarts underway, but supply normalization remains gradual, reinforcing our regulatory-risk thesis

Following the fatal Shanxi mine accident in late May-26 (link), several suspended coking coal mines have gradually resumed operations. According to a Mysteel survey (link), 77 mines had restarted by 11 June 2026, representing around $56\%$ of the suspended 137 mines in Shanxi since 23 May 2026 (Fig. 9). However, the recovery remains uneven, with some mines reportedly suspending operations again after only a few days of resumption amid intensified safety inspections. Notably, authorities have expanded inspections across major mining regions, particularly targeting illegal and hidden mining tunnels (link).

## China domestic coking coal prices continue to reflect supply concerns

Despite resumption of some mining activity, domestic prices reflect uncertainties around coal availability. China's spot domestic coking coal price has climbed to USD270/t, up more than $10\%$ since the incident (Fig. 8), suggesting the market is pricing in a broader tightening in domestic steelmaking raw material availability rather than an isolated operational event.

## Australian exports to China rise as buyers seek seaborne supply

Recent developments strengthen our view that prolonged safety-led disruptions in China could gradually shift demand towards seaborne coking coal markets. Australia's coking coal exports to China surged 114% m-m (+77% y-y) to 1.48MT in May-26, with Australia's share of exports to China rising to \~11% in May-26 from \~7% in both May-25 and Apr-26, although it remains a relatively small contributor to China's overall coking coal requirements (link).

While we believe China can offset part of the disrupted supply via inland imports, primarily Mongolia/Russia (Fig. 4), logistics constraints and quality differences might limit full substitution. Consequently, if inspections persist, mine resumptions are delayed and domestic supply recovery remains uneven, China may increasingly rely on Australia's seaborne supplies potentially pressuring global coking coal prices, in our view. However, Australian spot premium hard coking coal prices have largely remained stable and increased marginally by around $1.5\%$ to USD244/t so far since the incident.

## Indian steelmakers' margins largely shielded as China's coal supply recovers

For Indian steelmakers, the primary transmission mechanism is imported coking coal costs. As a directional sensitivity, we calculate that every USD10/t increase in coking coal can create \~USD7-9/t EBITDA impact for integrated steelmakers, depending on inventory cover and coal blend assumptions. Within our coverage, we believe JSW Steel and Tata Steel India would be the most exposed (Fig. 5), with partial impact on Jindal Steel depending on the procurement mix. However, the gradual resumption of coking coal supply in China is likely to keep seaborne coking coal prices relatively stable and therefore, may not be incrementally negative for near-term margin expectations of Indian steel players, in our view (Fig. 11).

We maintain our Buy recommendations on Tata Steel (TATA IN), JSW Steel (JSTL IN), Jindal Steel (JINDALST IN) and Lloyds Metals (LLOYDSME IN).

## Research Analysts

India Metals & Mining

Jashandeep Singh Chadha - NFASL

jashandeep.singhchadha@NOM.com

+91 22 40374124

Fig. 1: China's coal production run-rate suggests \~500MT of coal production in CY26F  
China Met coal production (MT)  
![](images/f75f8f8c508f78a5370216e7d86294db3d89ed5b04795f86df94d1c402e294e0.jpg)

<details>
<summary>bar chart</summary>

| Year | Value |
| :--- | :--- |
| 2021 | 458 |
| 2022 | 471 |
| 2023 | 490 |
| 2024 | 486 |
| 2025 | 502 |
| 2026* | 167 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 2: Shanxi is the biggest coal producing province in China; it accounts for \~25% of total coal and >20% of met coal  
China top 5 coal producing states (ex-Inner Mongolia)  
![](images/f1515e25b4372e7f55006fc925e29fbce84731b32481b8bb15a079867d09a9f8.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | Shanxi (%) | Hebei (%) | Xinjiang (%) | Shaanxi (%) | Shandong (%) |
|---|---|---|---|---|---|
| 2021 | 24 | 10 | 6 | 10 | 7 |
| 2022 | 23 | 10 | 6 | 11 | 7 |
| 2023 | 22 | 10 | 8 | 10 | 7 |
| 2024 | 21 | 10 | 9 | 10 | 7 |
| 2025 | 23 | 10 | 9 | 10 | 7 |
| 2026* | 22 | 10 | 9 | 9 | 7 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 3: China accounts for \~20-25% of global seaborne coking coal trade, in our view  
![](images/4d3268552fe4b571e9cdc8f1ef7df0cc2942cd2916a153fbfe81d5528d986745.jpg)

<details>
<summary>bar chart</summary>

China coking coal imports (MT)
| Year | Value (MT) |
| :--- | :--- |
| 2021 | 55 |
| 2022 | 64 |
| 2023 | 103 |
| 2024 | 122 |
| 2025 | 119 |
| 2026* | 44 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 4: Mongolia should be China's first mitigation lever in case of supply shortfall  
![](images/8fef97bdd8d910650daa43f56038e903d01990104b5cab3b3b3456ce04e4cbb8.jpg)

<details>
<summary>stacked bar chart</summary>

China coking coal importing countries (%)
| Year | Mongolia (%) | Russia (%) | Canada (%) | United States (%) | Australia (%) | Indonesia (%) | Others (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2021 | 26 | 20 | 18 | 19 | 13 | 4 | 3 |
| 2022 | 40 | 33 | 15 | 7 | 4 | 3 | 3 |
| 2023 | 53 | 26 | 7 | 6 | 3 | 4 | 2 |
| 2024 | 46 | 25 | 8 | 10 | 8 | 3 | 2 |
| 2025 | 51 | 28 | 9 | 5 | 8 | 3 | 1 |
| 2026* | 61 | 27 | 6 | 3 | 6 | 1 | 1 |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 5: JSW Steel has the highest exposure to imported coking coal among our coverage, followed by Tata Steel; Jindal Steel appears better placed  
![](images/843f46f700008340b0b0660dfa5548b32fa4bf4b685127d80e194e310f292951.jpg)

<details>
<summary>stacked bar chart</summary>

| Year   | SAIL  | JSW Steel | Tata Steel | RINL  | Jindal Steel | Bhushan Power & Steel | NMDC  | Others |
|--------|-------|-----------|------------|-------|--------------|------------------------|-------|--------|
| 2020   | 25%   | 18%       | 17%        | 5%    | 7%           | 3%                     | 4%    | 15%    |
| 2021   | 24%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 17%    |
| 2022   | 29%   | 18%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 15%    |
| 2023   | 26%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 16%    |
| 2024   | 25%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 17%    |
| 2025   | 22%   | 19%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 19%    |
| 2026*  | 19%   | 20%       | 16%        | 5%    | 7%           | 3%                     | 4%    | 20%    |
</details>

Note: \*till April 2026  
Source: Bigmint, NOM

Fig. 6: China's coking coal imports have increased significantly as a % of consumption; any domestic supply gap can lead to increased global prices  
![](images/b3d3d7c805ddd272fcc7244072fdaee4c305c83a20f0b37824a803a3569b9d33.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | China Coking Coal Imports/Consumption Ratio | Median (last 9 years, in INR) |
|--------|---------------------------------------------|-------------------------------|
| Apr-17 | 10%                                         | 13%                           |
| Apr-18 | 15%                                         | 13%                           |
| Apr-19 | 17%                                         | 13%                           |
| Apr-20 | 19%                                         | 13%                           |
| Apr-21 | 14%                                         | 13%                           |
| Apr-22 | 18%                                         | 13%                           |
| Apr-23 | 28%                                         | 13%                           |
| Apr-24 | 26%                                         | 13%                           |
| Apr-25 | 34%                                         | 13%                           |
| Apr-26 | 24%                                         | 13%                           |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 7: Gap between Australian and Chinese coking coal has narrowed due to the pick up in the latter's prices  
![](images/7ca56c968f202f5ca891e229af9260a974a12c2406fba3dce606df351fa3aa3f.jpg)

<details>
<summary>line chart</summary>

| Date   | China domestic coking coal premium/(discount) over Australia (USD/t) |
|--------|---------------------------------------------------------------------|
| May-17 | ~0                                                                  |
| May-18 | ~-50                                                                |
| May-19 | ~0                                                                  |
| May-20 | ~50                                                                 |
| May-21 | ~100                                                                |
| May-22 | ~200                                                                |
| May-23 | ~50                                                                 |
| May-24 | ~0                                                                  |
| May-25 | ~-50                                                                |
| May-26 | ~0                                                                  |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 8: China's domestic coking coal spot prices are trading over $10\%$ higher since the incident  
![](images/d972493eeee365589166b463e888b3af406f0bd83b06b400abe20e2b5cdf00fe.jpg)

<details>
<summary>line chart</summary>

| Date   | Price (USD/t) |
|--------|---------------|
| Jun-20 | 170           |
| Jun-21 | 300           |
| Jun-22 | 480           |
| Jun-23 | 230           |
| Jun-24 | 280           |
| Jun-25 | 180           |
| Jun-26 | 270           |
</details>

Source: Bloomberg Finance L.P., NOM

Fig. 9: Number of coking coal mines halted and resumed at Shanxi  
![](images/3bf367fc345e928eceddc6c663100f75a03affbc8a86ae742856fad5559f8b45.jpg)

<details>
<summary>stacked bar chart</summary>

| Date | Halted | Resumed |
|---|---|---|
| 25 May'26 | 109 | 0 |
| 27 May'26 | 113 | 16 |
| 29 May'26 | 112 | 18 |
| 1 Jun'26 | 87 | 43 |
| 3 Jun'26 | 75 | 59 |
| 5 Jun'26 | 74 | 61 |
| 8 Jun'26 | 65 | 70 |
| 10 Jun'26 | 56 | 81 |
| 11 Jun'26 | 60 | 77 |
</details>

Source: BigMint, Mysteel Global, NOM

Fig. 10: China's export HRC margins levels have recovered recently due to higher realization but remain below median levels  
![](images/f54a539827c6cffc410fac87787ba818844a2466e01be5b4e659c7f1ed20fad9.jpg)

<details>
<summary>line chart</summary>

| Date   | China Export HRC Margins (USD/Ton) |
|--------|------------------------------------|
| Jun-19 | 150                                |
| Jun-20 | 250                                |
| Jun-21 | 550                                |
| Jun-22 | 350                                |
| Jun-23 | 250                                |
| Jun-24 | 200                                |
| Jun-25 | 180                                |
| Jun-26 | 170                                |
</details>

Note: Margins calculated using Australia iron ore and China domestic coking coal prices  
Source: Bloomberg Finance L.P., NOM

Fig. 11: India steelmakers' margins have moderated recently as HRC prices ease, but remain at healthy levels  
![](images/a03795cbc70954d2e6d25ee899fc93e900f336130617d7fb9f5764fe63c3dc10.jpg)

<details>
<summary>line chart</summary>

| Date   | India HRC Margin (INR/t) |
|--------|--------------------------|
| Jun-19 | 27,000                   |
| Jun-20 | 28,000                   |
| Jun-21 | 49,000                   |
| Jun-22 | 47,000                   |
| Jun-23 | 39,000                   |
| Jun-24 | 32,000                   |
| Jun-25 | 34,000                   |
| Jun-26 | 36,000                   |
</details>

Note: Margins calculated using domestic iron ore and Australia coking coal prices  
Source: Bloomberg Finance L.P., NOM

## Appendix A-1

This report has been produced by NOM Financial Advisory and Securities (India) Private Limited (NFASL), India.

See Disclaimers for NOM Group entity details.

## Analyst Certification

I, Jashandeep Singh Chadha, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Jindal Steel</td><td>JINDALST IN</td><td>INR 1,140</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>JSW Steel</td><td>JSTL IN</td><td>INR 1,274</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Lloyds Metals and Energy</td><td>LLOYDSME IN</td><td>INR 1,765</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr><tr><td>Tata Steel</td><td>TATA IN</td><td>INR 196</td><td>16-Jun-2026</td><td>Buy</td><td>N/A</td><td></td></tr></table>

Jindal Steel (JINDALST IN)  
Rating and target price chart (three year history)  
![](images/51c6e371dfc5023940238e2d1b8394a17abab91a181ede049f2243c560696a3f.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2024/07/01 | ~1000.00      | -                   | -                      |
| 2025/01/01 | ~950.00       | -                   | -                      |
| 2026/01/01 | ~1300.00      | -                   | -                      |
| As of 16-Jun-2026 | -           | -                   | INR                    |
</details>

INR 1,140 (16-Jun-2026) Buy (Sector rating: N/A)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>04-May-26</td><td></td><td>1,350.00</td><td>1,261.00</td></tr><tr><td>01-Feb-26</td><td></td><td>1,280.00</td><td>1,131.00</td></tr><tr><td>22-Sep-25</td><td></td><td>1,150.00</td><td>1,033.00</td></tr><tr><td>31-Jan-25</td><td></td><td>1,080.00</td><td>792.00</td></tr><tr><td>07-Nov-24</td><td></td><td>1,180.00</td><td>947.00</td></tr><tr><td>02-Oct-24</td><td>Buy</td><td></td><td>1,036.00</td></tr><tr><td>02-Oct-24</td><td></td><td>1,200.00</td><td>1,036.00</td></tr></table>

Source: LSEG, NOM  
For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at TP of Rs1,350 by applying slightly higher than mid-cycle one-year-forward EV/EBITDA of 8.0x on new steady-state EBITDA in June-28F. The benchmark for this stock is NIFTY50

Risks that may impede the achievement of the target price 1. Lower spreads - If Chinese HRC margins fail to recover or if the net exports from China increase, it would result in continued pressure on export HRC prices. In such a case, domestic HRC prices will remain under pressure due to lower import parity prices leading to lower spreads/margins. 2. Delays in expansion & cost overruns - This would result in lower than expected volume from FY26F onwards. Delay in commissioning might also result in capex cost overrun resulting in lower than earlier expected ROCE 3. Domestic demand disruptions - If the domestic demand grows lower than expected or lower than the capacity addition, it would result in lower domestic HRC margins and higher dependence on exports. In such a case, the margins will be lower than expected

## JSW Steel (JSTL IN)

## INR 1,274 (16-Jun-2026) Buy (Sector rating: N/A)

Rating and target price chart (three year history)

![](images/e591b30e88412b94041d53d14501c26c8fff749017c57756081af5f891d56915.jpg)

<details>
<summary>line chart</summary>

| Date       | Closing Price | Target Price Change | Recommendation Changes |
| ---------- | ------------- | ------------------- | ---------------------- |
| 2024/07/01 | ~950.00       | ~1200.00            | Yes                    |
| 2025/01/01 | ~1050.00      | -                   | Yes                    |
| 2026/01/01 | ~1350.00      | ~1350.00            | -                      |
| As of 16-Jun-2026 | -         | -                   | -                      |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>21-May-26</td><td></td><td>1,400.00</td><td>1,281.00</td></tr><tr><td>26-Jan-26</td><td></td><td>1,340.00</td><td>1,170.00</td></tr><tr><td>22-Sep-25</td><td></td><td>1,300.00</td><td>1,117.00</td></tr><tr><td>02-Oct-24</td><td>Buy</td><td></td><td>1,027.00</td></tr><tr><td>02-Oct-24</td><td></td><td>1,220.00</td><td>1,027.00</td></tr><tr><td>20-Sep-24</td><td>Not Rated</td><td></td><td>982.00</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We arrive at TP of INR1,400 by applying slightly higher than mid-cycle one-year forward EV/EBITDA of 8.1x on new steady-state EBITDA in Jun'28. The benchmark for this stock is NIFTY50

Risks that may impede the achievement of the target price 1. Lower spreads - If Chinese HRC margins fail to recover or if the net exports from China increase, it would result in continued pressure on export HRC prices. In such a case, domestic HRC prices will remain under pressure due to lower import parity prices leading to lower spreads/margins. 2. Delays in Dolvi commissioning - This would result in lower than expected volume from FY28F onwar

[中间内容因长度限制已省略]

STMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public

offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Financial Advisory and Securities (India) Private Limited, India. All rights reserved.
"""
