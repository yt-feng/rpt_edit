You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# China Oil Product Monthly

# China's crude oil imports fell sharply in April; focus on refined oil export policies

# Crude oil imports -20% YoY; domestic oil product demand still weak

Affected by geopolitical tension in the Middle East, China's crude oil imports fell 20% YoY to 38.47m tonnes in April, the lowest level since July 2022. The utilization rate of major domestic refineries fell to 70.8% (vs. a 2025 average of 80%). That said, China's crude inventory has remained relatively stable since March (\~1.3bn bbl, equivalent to 76 days of crude oil demand and >100 days of crude oil imports). Gasoline and diesel inventory remains high. We believe this is mainly due to: 1) high oil prices significantly dampening domestic gasoline and diesel demand; and 2) restrictions on refined oil exports. In the near term, with a sharp rise in crude import official selling prices (OSP) and freight/insurance premiums, coupled with weak domestic product demand, domestic refiners face significant pressure. Thus, we remain cautious on the domestic refining sector. Moreover, we advise monitoring adjustments to oil product export policies.

# Major refineries' utilization down to 70.8%; May oil product exports to rise a bit

Oil product prices: In April, the domestic retail price ceilings for gasoline/diesel had one increase and one decrease, with cumulative cuts of Rmb135/t and Rmb130/t. Due to persistently weak demand, market average prices fell nearly Rmb1000/t and Rmb300/t.

Utilisation: Affected by the disruption to Middle East crude supply, major refineries' utilization fell 5.9ppt MoM to 70.8% in April. Shandong independent refinery utilization was relatively stable, up 0.8ppt MoM to 55.2%. Oil product exports: To ensure domestic energy supply, China suspended oil product exports in March. However, according to a Reuters report, China approved 0.5m tonnes of exports to non-Hong Kong regions in May (doubling from April and c30% of pre-Iran conflict level). We believe that is mainly due to still-weak domestic oil product demand and high inventory pressure for gasoline and diesel.

# Middle East refining exports/capacity impact

UBS estimates that, even assuming SPR releases at the maximum pace, the outright shortfall of product exports from the Middle East would be \~3.5Mb/d. According to a recent expert call (see note), the actual SPR releases on the crude and product sides may turn out slower and more challenging; thus, the actual shortfall could be higher than theoretically. Additionally, the crude shortfall is likely to translate into similar cuts to throughput, so \~9Mb/d of the shortfall could become visible on the product side. UBS estimates that due to strikes/attacks, >3.5Mb/d of refining capacity in the Gulf Cooperation Council (GCC) has halted operations, >2Mb/d of which could be damaged and require some sort of repairs. For context, at the peak of the drone attacks at Russian refineries in fall 2025, UBS estimates <1Mb/d of refining capacity was affected, significantly below the current scale of the impact in the Middle East. UBS estimates GCC refineries are likely to run at \~50% capacity, on average. Beyond the Middle East disruption, March-April are typically the peak of scheduled maintenance for global refineries. Coupled with intensified drone attacks at Russian assets, a fire at the 120kb/d Geelong refinery in Australia, as well as a workers' strike at the Whiting refinery, based on Kpler data and UBS estimates, offline capacity globally may have exceeded \~12Mb/d in April (see note).

# Equities

China

Energy

Amily Guo

Analyst

amily.guo@UBS.com

+86-105-832 8845

Cheryl Wen

Analyst

S1460525030002

cheryl.wen@UBS.com

+86-21-3866 8916

Jay LIN

Analyst

S1460525070001

jay.lin@UBS.com

+86-105-832 8044

Henri Patricot, CFA

Analyst

henri.patricot@UBS.com

+33-14-888 3033

Anna Kishmariya

Analyst

anna.kishmariya@UBS.com

+44-20-7568 7999

Nayoung Kim

Analyst

nayoung.kim@UBS.com

+44-20-7568 4010

Figure 1: China's crude oil inventory (Mb)   
![](images/387f4838c606f368ae6f762aa645ff7a33e7424f7825c783e731dfaf95b9df6b.jpg)

<details>
<summary>bar_stacked</summary>

| Month | spr | refinery | commercial | Oil in Transit on Ships | Floating Storage |
|---|---|---|---|---|---|
| Jan-20 | 300 | 300 | 400 | 100 | 100 |
| Aug-20 | 300 | 300 | 400 | 100 | 150 |
| Mar-21 | 300 | 300 | 400 | 100 | 150 |
| Oct-21 | 300 | 300 | 400 | 100 | 150 |
| May-22 | 300 | 300 | 400 | 100 | 150 |
| Dec-22 | 300 | 300 | 400 | 100 | 150 |
| Jul-23 | 300 | 300 | 400 | 100 | 150 |
| Feb-24 | 300 | 300 | 400 | 100 | 150 |
| Sep-24 | 300 | 300 | 400 | 100 | 150 |
| Apr-25 | 300 | 300 | 400 | 100 | 150 |
| Nov-25 | 300 | 300 | 400 | 100 | 150 |
</details>

Source: Kpler, UBS

Figure 2: Monthly changes in China's crude oil inventory, vs. quarterly global crude oil market balance (Mb/d)   
![](images/2efab8c311cca987a5f68afbc7c8c1405ccc00a3c862fdf9e56c745eafc27f97.jpg)

<details>
<summary>bar_line</summary>

| Month    | Kpler (Mbbl/d) | IEA (Mbbl/d) | Global oil market balance (Mbbl/d) |
|----------|----------------|--------------|-----------------------------------|
| Jan-23   | -0.1           | 1.1          | -                                 |
| Apr-23   | 0.9            | 0.4          | -                                 |
| Jul-23   | 0.6            | 0.0          | -                                 |
| Oct-23   | -1.0           | 0.8          | -                                 |
| Jan-24   | 0.3            | 1.0          | -                                 |
| Apr-24   | 1.2            | 0.7          | -                                 |
| Jul-24   | 0.1            | 0.1          | -                                 |
| Oct-24   | -0.1           | 0.3          | -                                 |
| Jan-25   | -0.5           | 1.0          | -                                 |
| Apr-25   | 1.5            | 2.0          | -                                 |
| Jul-25   | 0.5            | 2.8          | -                                 |
| Oct-25   | -0.5           | 1.8          | -                                 |
| Jan-26   | 1.4            | 0.3          | -                                 |
| Apr-26   | 0.3            | -3.0         | -                                 |
</details>

Source: IEA (2026) Oil Market Report - February 2026, Kpler, UBS. Note: IEA's China crude oil inventory data available from January 2025.

Figure 3: Refined product flow affected by the Middle East (Mb/d)   
![](images/f0203a86549c04a876e730d8f41d53db15c1cc8b5de4f509ff218c938d882c1d.jpg)

<details>
<summary>bar</summary>

| Category | Value |
|---|---|
| Flows via Sol pre-conflict of Hormuz | 15.0 |
| Flows via Sol pre-conflict products | 5.0 |
| Lost products exports from China | 0.3 |
| Redirected/continued crude flows | -7.5 |
| Redirected products | -1.0 |
| Shortfall pre-spr | 11.8 |
| At max SPR crude | -2.2 |
| At max SPR products | -0.8 |
| Remaining shortfall crude | 5.3 |
| Remaining shortfall products | 3.5 |
</details>

Source: Kpler, IEA, UBS

Figure 4: Capacity in GCC affected by attacks   
![](images/66f47fe8d236a2985488d4f40623178c5276353b9378020d1d25ec04ea09d4df.jpg)

<details>
<summary>bar_stacked</summary>

| Date | Possibly damaged, kb/d | Reported as a precautionary closure, kb/d |
|---|---|---|
| 02-Mar | 500 | 700 |
| 03-Mar | 500 | 1200 |
| 04-Mar | 700 | 1300 |
| 05-Mar | 1100 | 1900 |
| 06-Mar | 1200 | 2300 |
| 07-Mar | 1200 | 2800 |
| 08-Mar | 1200 | 2800 |
| 09-Mar | 1200 | 2800 |
| 10-Mar | 1200 | 2300 |
| 11-Mar | 1200 | 2300 |
| 12-Mar | 1800 | 2300 |
| 13-Mar | 1800 | 2300 |
| 14-Mar | 1800 | 2300 |
| 15-Mar | 1800 | 2300 |
| 16-Mar | 1800 | 2300 |
| 17-Mar | 1800 | 2300 |
| 18-Mar | 1800 | 2300 |
| 19-Mar | 1800 | 2300 |
| 20-Mar | 1800 | 2300 |
| 21-Mar | 1800 | 2300 |
| 22-Mar | 1800 | 2300 |
| 23-Mar | 1800 | 2300 |
| 24-Mar | 1800 | 2300 |
| 25-Mar | 1800 | 2300 |
| 26-Mar | 1800 | 2300 |
| 27-Mar | 1800 | 2300 |
| 28-Mar | 1800 | 2300 |
| 29-Mar | 1800 | 2300 |
| 30-Mar | 1800 | 2300 |
| 31-Mar | 1800 | 2300 |
| 32-Mar | 1800 | 2300 |
| 33-Mar | 1800 | 2300 |
| 34-Mar | 1800 | 2300 |
| 35-Mar | 1800 | 2300 |
| 36-Mar | 1800 | 2300 |
| 37-Mar | 1800 | 2300 |
| 38-Mar | 1800 | 2300 |
| 39-Mar | 1800 | 2300 |
| 40-Mar | 1800 | 2300 |
| 41-Mar | 1800 | 2300 |
| 42-Mar | 1800 | 2300 |
| 43-Mar | 1800 | 2300 |
| 44-Mar | 1800 | 2300 |
| 45-Mar | 1800 | 2300 |
| 46-Mar | 1800 | 2300 |
| 47-Mar | 1800 | 2300 |
| 48-Mar | 1800 | 2300 |
| 49-Mar | 1800 | 2300 |
| 50-Mar | 1800 | 2300 |
| 51-Mar | 1800 | 2300 |
| 52-Mar | 1800 | 2300 |
| 53-Mar | 1800 | 2300 |
| 54-Mar | 1800 | 2300 |
| 55-Mar | 1800 | 2300 |
| 56-Mar | 1800 | 2300 |
| 57-Mar | 1800 | 2300 |
| 58-Mar | 1800 | 2300 |
| 59-Mar | 1800 | 2300 |
| 6 Oct-May | - | - |
The chart displays the total number of possible damaged cases and those reported as a precautionary closure. The data is presented in a stacked bar format for each bar. The x-axis represents the date (from March to May), and the y-axis represents the count of possible damaged cases. There are two categories: 'Possibly damaged, kb/d' and 'Reported as a precautionary closure, kb/d'. The bars are stacked to show the proportion of possible damaged cases relative to the total. The labels above the bars indicate the date and the corresponding value.
</details>

Source: Media reports, UBS estimates. Note: GCC refers to the Gulf Cooperation Council.

Figure 5: China weighted average realised retail price discounts to NDRC ceiling – gasoline (92)   
![](images/d661d509f9b19c23a730115860cb00e8881486edf91592442f5ffb3a9dffcc36.jpg)

<details>
<summary>line</summary>

| Date    | Sinopec | PetroChina | Independents |
|---------|---------|------------|--------------|
| May-20  | -5%     | -5%        | -15%         |
| Nov-20  | -5%     | -5%        | -15%         |
| May-21  | -5%     | -5%        | -10%         |
| Nov-21  | -5%     | -5%        | -5%          |
| May-22  | -5%     | -5%        | -10%         |
| Nov-22  | -5%     | -5%        | -10%         |
| May-23  | -5%     | -5%        | -5%          |
| Nov-23  | -5%     | -5%        | -5%          |
| May-24  | -5%     | -5%        | -5%          |
| Nov-24  | -5%     | -5%        | -5%          |
| May-25  | -5%     | -5%        | -5%          |
| Nov-25  | -5%     | -5%        | -5%          |
| May-26  | -5%     | -5%        | -5%          |
</details>

Source: UBS Evidence Lab (> Access dataset), 315i, NBS, Reuters

Figure 6: China weighted average realised retail price discounts to NDRC ceiling – diesel   
![](images/aa9757721bac85a14da77a1daae510bf3c7361ad4135248e489816deef7b513c.jpg)

<details>
<summary>line</summary>

| Date    | Sinopec | PetroChina | Independents |
|---------|---------|------------|--------------|
| Nov-19  | -5%     | -5%        | -10%         |
| May-20  | -5%     | -5%        | -10%         |
| Nov-20  | -5%     | -5%        | -10%         |
| May-21  | -5%     | -5%        | -10%         |
| Nov-21  | -5%     | -5%        | -10%         |
| May-22  | -5%     | -5%        | -10%         |
| Nov-22  | -5%     | -5%        | -10%         |
| May-23  | -5%     | -5%        | -10%         |
| Nov-23  | -5%     | -5%        | -10%         |
| May-24  | -5%     | -5%        | -10%         |
| Nov-24  | -5%     | -5%        | -10%         |
| May-25  | -5%     | -5%        | -10%         |
| Nov-25  | -5%     | -5%        | -10%         |
| May-26  | -5%     | -5%        | -10%         |
</details>

Source: UBS Evidence Lab (> Access dataset), 315i, NBS, Reuters

Figure 7: Heat map of realised retail diesel price discounts to NDRC benchmark prices (by retailer and province)   
![](images/6de4a994f01f4308455cba3badc556306caf69a9b9bb5c6d8efd5da180992514.jpg)  
Source: UBS Evidence Lab (> Access dataset), 315i

Figure 8: Heat map of realised gasoline price discounts to NDRC benchmark prices (by retailer and province)   
![](images/e7c080accd70fd48f7ff67013e038c02678b9e6738a9d712101f21ea4a0c74b1.jpg)  
Source: UBS Evidence Lab (> Access dataset), 315i

Figure 9: Estimated spread of SNP (Sinopec) realised retail oil product price to wholesale price (Rmb/litre, quarterly, Shandong)   
![](images/96d37987c3a452132b01fd7ac2978c8ed256f56cc71df3aa1fc754aaae464f02.jpg)

<details>
<summary>bar</summary>

| Quarter | Diesel (SNP-SNP) | Gasoline (SNP-SNP) | Diesel (SNP-IND) | Gasoline (SNP-IND) |
|---------|------------------|--------------------|------------------|--------------------|
| Q1 22   | 0.5              | 0.7                | 0.6              | 0.6                |
| Q2 22   | 0.9              | 1.7                | 1.0              | 1.7                |
| Q3 22   | 0.7              | 1.2                | 0.8              | 1.6                |
| Q4 22   | 0.5              | 1.5                | 0.7              | 1.9                |
| Q1 23   | 0.6              | 0.8                | 0.8              | 1.1                |
| Q2 23   | 0.6              | 0.5                | 0.8              | 0.9                |
| Q3 23   | 0.6              | 0.7                | 0.8              | 0.9                |
| Q4 23   | 0.8              | 0.8                | 1.0              | 1.3                |
| Q1 24   | 0.7              | 0.4                | 0.9              | 0.7                |
| Q2 24   | 0.9              | 0.5                | 1.1              | 1.1                |
| Q3 24   | 0.8              | 0.6                | 1.1              | 1.1                |
| Q4 24   | 0.7              | 0.8                | 0.9              | 1.3                |
| Q1 25   | 0.7              | 0.3                | 1.0              | 0.8                |
| Q2 25   | 0.5              | 0.3                | 0.8              | 0.8                |
| Q3 25   | 0.8              | 0.6                | 1.0              | 1.1                |
| Q4 25   | 0.7              | 0.6                | 0.9              | 1.2                |
| Q1 26   | 0.8              | 0.3                | 1.1              | 1.1                |
| Q2 26   | 1.1              | 1.6                | 1.6              | 1.9                |
</details>

Source: UBS Evidence Lab (> Access dataset), 315i, Wind

Figure 10: Shandong independent wholesale oil product price discount to Sinopec (Rmb/t)   
![](images/97490a847c502e83e9b63dae32f73eb5da765e6ab2a909ff6203a31e9f928bc8.jpg)

<details>
<summary>line</summary>

| Date    | Diesel | Gasoline |
|---------|--------|----------|
| May-20  | -500   | -1000    |
| Feb-21  | 0      | 0        |
| Nov-21  | 0      | 0        |
| Aug-22  | 0      | 0        |
| May-23  | 0      | 0        |
| Feb-24  | 0      | 0        |
| Nov-24  | 0      | 0        |
| Aug-25  | 0      | 0        |
| May-26  | -500   | -2500    |
</details>

Source: UBS Evidence Lab (> Access dataset), 315i, Wind

Figure 11: China's gasoline net exports (kbpd)   
![](images/76f0f39ebe4340502de22cff76dda57e4da78828cce9bcdf4e7dbd2f96a6bf14.jpg)

<details>
<summary>bar_line</summary>

| Date    | Gasoline | Gasoline (3m avg) |
|---------|----------|-------------------|
| Mar-18  | 450      | 300               |
| Sep-18  | 350      | 400               |
| Mar-19  | 400      | 350               |
| Sep-19  | 450      | 450               |
| Mar-20  | 500      | 500               |
| Sep-20  | 550      | 450               |
| Mar-21  | 450      | 400               |
| Sep-21  | 400      | 350               |
| Mar-22  | 350      | 300               |
| Sep-22  | 400      | 350               |
| Mar-23  | 550      | 450               |
| Sep-23  | 350      | 350               |
| Mar-24  | 300      | 300               |
| Sep-24  | 250      | 250               |
| Mar-25  | 350      | 250               |
| Sep-25  | 250      | 250               |
| Mar-26  | 100      | 100               |
</details>

Source: General Administration of Customs of China (GACC)

Figure 12: China's diesel net exports (kbpd)   
![](images/dd036f573eafa2e01e39c1ab1bd03ee0c6af249e2d33c5402d462fd5a6f0e019.jpg)

<details>
<summary>bar_line</summary>

| Date    | Diesel | Diesel (3m avg) |
|---------|--------|-----------------|
| Mar-18  | 550    | 450             |
| Sep-18  | 400    | 500             |
| Mar-19  | 650    | 550             |
| Sep-19  | 500    | 450             |
| Mar-20  | 680    | 550             |
| Sep-20  | 500    | 400             |
| Mar-21  | 680    | 580             |
| Sep-21  | 400    | 450             |
| Mar-22  | 150    | 100             |
| Sep-22  | 450    | 150             |
| Mar-23  | 680    | 600             |
| Sep-23  | 350    | 300             |
| Mar-24  | 350    | 250             |
| Sep-24  | 200    | 150             |
| Mar-25  | 150    | 100             |
| Sep-25  | 250    | 150             |
| Mar-26  | 200    | 100             |
</details>

Source: General Administration of Customs of China (GACC)

Figure 13: Domestic refining margin   
![](images/9db0eae3aba54ed1492e5e674198fdd43603a195fbd87ce08e029e9512d09734.jpg)

<details>
<summary>line</summary>

| Year | Domestic refining margin (Rmb/t) | Teapot refining margin (Rmb/t) |
|------|----------------------------------|-------------------------------|
| 2015 | ~1,000                           | ~-1,000                       |
| 2016 | ~800                             | ~-500                         |
| 2017 | ~1,200                           | ~-200                         |
| 2018 | ~1,400                           | ~-100                         |
| 2019 | ~1,300                           | ~-50                          |
| 2020 | ~800                             | ~-1,000                       |
| 2021 | ~1,400                           | ~-50                          |
| 2022 | ~1,800                           | ~2,500                        |
| 2023 | ~1,500                           | ~-1,500                       |
| 2024 | ~1,300                           | ~-50                          |
| 2025 | ~1,400                           | ~-1,00                         |
| 2026 | ~3,200                           | ~2,500                        |
</details>

Source: Baiinfo. Note: Refining margin calculated using weighted average of output proportion, ex. VAT/consumption tax and including freight; oil prices on a 45-day lag.

Figure 14: European refining margin   
![](images/47f9676f57778b09cbc48bd12c9466c3b62ed77b7cf3c3b1c9e4268103697b94.jpg)

<details>
<summary>line</summary>

| Month | 5-year range | 5-year average | 2025 | 2026 |
|-------|--------------|----------------|------|------|
| Jan   | ~18          | ~7             | ~4   | ~9   |
| Feb   | ~17          | ~6             | ~5   | ~8   |
| Mar   | ~16          | ~5         

[中间内容因长度限制已省略]

 authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, sUBSidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.UBS.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its sUBSidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/883c993c3e72ccfc0fce1bcd66a13756cce48dbb5996c51d01f88c97822216f3.jpg)
"""
