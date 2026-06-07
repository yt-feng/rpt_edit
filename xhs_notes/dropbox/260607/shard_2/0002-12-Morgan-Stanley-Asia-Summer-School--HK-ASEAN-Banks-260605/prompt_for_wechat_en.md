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
# Investor Presentation | Asia Pacific

# Asia Summer School: HK/ASEAN Banks

The session will cover industry structure, individual banks under our coverage and stock price drivers. We also focus on key thematics including capital returns, wealth management, Singapore's EQDP and the emergence of digital assets.

MS ASIA (SINGAPORE) PTE.+

# Nick Lord

Equity Analyst

Nick.Lord@morganstanley.com +65 6834-6746

# Selvie Jusman, CFA

Equity Analyst

Selvie.Jusman@morganstanley.com +65 6834-6517

# Aitong Li

Research Associate

Aitong.Li@morganstanley.com +65 6834-6295

![](images/3d534f916c08967c49bb675e6bcebe5abed495066bce9c1abfbb97b060362e3f.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

# ASEAN FINANCIALS

Asia Pacific

Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Asia Summer School 2026

# I. MAPPING HK/ASEAN BANKS

Banking Markets in Context   
![](images/f9613f4426ac8b4c2c2d6ca75e006acea51ef9dd764872a23c7f1e9d975ebc0c.jpg)

<details>
<summary>other</summary>

| Category               | Value |
| ---------------------- | ----- |
| Emerging Markets       | 1     |
| Low Credit Penetration | 2     |
| Developed Markets      | 0     |
| Low Sensitivity to US Interest Rates | 3   |
</details>

Source: MS

# ASEAN in a Glimpse

Credit Penetration   
![](images/db91b9ea7c92b8faba007d8f72b82db47c45cccf0182fb182c94b54ea5b1fa3e.jpg)

<details>
<summary>bar</summary>

Non financial corporate and household debt as % GDP
| Country | Non-financial corporate and household debt as % GDP (%) |
| :--- | :--- |
| Indonesia | 47 |
| Philippines | 59 |
| Malaysia | 146 |
| Singapore | 183 |
| Thailand | 185 |
</details>

Source: CEIC, Haver, MS. Data as of end of 2025.

Return Level   
![](images/04dbb10da4c0c5acdc12f3fddf30e29d81a0177f8010e9cab4d5f5ab62a9c77c.jpg)

<details>
<summary>bar</summary>

RoE (2025)
| Country | RoE (%) |
| :--- | :--- |
| Thailand | 9.2 |
| Malaysia | 11.1 |
| Singapore | 13.4 |
| Philippines | 14.7 |
| Indonesia | 18.4 |
</details>

Source: Company Reports, MS

Capital Position   
![](images/179dbbfb62a958e53a8351ab451c3a64922608f6a34b79f67e9d8b56dbbf15cc.jpg)

<details>
<summary>bar_line</summary>

| Country | Regulatory Requirement (%) | Avg. CET1 |
| :--- | :--- | :--- |
| Singapore | 9 | 15 |
| Indonesia | 12 | 22 |
| Thailand | 8 | 18 |
| Philippines | 11 | 14 |
| Malaysia | 8 | 15 |
</details>

Source: Company Reports, MS

# Themes

Capital Return   
![](images/927d46db29b725c35c04f2b15c9b3759024d79534489a455a8b8dc26c21f7757.jpg)

<details>
<summary>scatter</summary>

| Label | Dividend payout (2026e) | Dividend yield (2026e) |
|-------|--------------------------|-------------------------|
| BRI   | 90.0%                    | 13.5%                   |
| BNI   | 75.0%                    | 7.5%                    |
| Mandiri| 85.0%                    | 5.0%                    |
| SCBX  | 80.0%                    | 7.5%                    |
| KTB   | 75.0%                    | 6.5%                    |
| MBBM  | 70.0%                    | 6.0%                    |
| BCA   | 70.0%                    | 6.0%                    |
| CMB   | 65.0%                    | 6.5%                    |
| KBANK | 65.0%                    | 6.0%                    |
| OCBC  | 60.0%                    | 4.5%                    |
| PUBM  | 55.0%                    | 4.5%                    |
| UOB   | 50.0%                    | 4.5%                    |
| BPI   | 45.0%                    | 5.5%                    |
| TCB   | 35.0%                    | 4.0%                    |
| BDO   | 30.0%                    | 3.5%                    |
</details>

Source: MS estimates

# ASEN Banks Evolving Industry Landscape

# Indonesia

- Rebuilt in the wake of the 1998 Asia Financial Crisis, Indonesia's banks have grown loans at an $8\%$ CAGR (2014-25) This has been driven by the country's private debt to GDP ratio of less than $50\%$ , the lowest in the region, and strong economic growth in the recent past.   
- The industry's loan/deposit ratio (LDR), climbed from 44% in 2002 to 96% in May-19 as deposits lagged loan growth. In the past two years, softer loan growth and rising liquidity has driven a fall in LDR to 80% (Dec 2022), but has recovered to \~90% now.   
- Sector is dominated by four large banks, there is also a long tail of mid and small sized banks, potentially leading to more consolidation.

# Thailand

- A developing market with structural issues due to highly indebted economy, (household debt of GDP of \~87%) and ageing demographics.   
- Loan growth has slowed significantly since 2014 to 2-5%. Asset quality has been an issue since 2012 when the banks faced consumer/ auto credit quality issue, followed by SME credit issues in 2014 and more recently credit quality issues from Covid-19. After several years of loan book consolidation, the question is whether credit quality is now on a sounder footing.   
- Returns have been under pressure from lower fees and higher credit charges. Banks looking to develop higher margin businesses outside of traditional competencies e.g., digital unsecured lending, wealth   
- Relatively concentrated banking system leaving little room for further consolidation

# Philippines

• Banking sector predominantly caters to corporate customers; this is one of the drivers of low historic RoA. Loan growth slowed materially in 2019-21, before recovering to 8% loan growth in 2023 and 12% in 2024 and 10% in 2025.   
- Financial inclusion is on the central bank's agenda and there is a strong push towards cashless transactions, but banks have lagged in their digital transformation.   
- Cost to income ratio is one of the highest in the region driven by investment and the Philippines archipelagic geography. Asset quality has not been an issue since the GFC and the banks have managed credit risks from Covid-19 well, helped by low system leverage.   
- Historically, capital ratios tend to be at the lower end, and capital raising is common in each credit cycle but low loan growth over the past years has changed the dynamics.

# Evolving Industry Landscape

# Singapore

• A mature economy with a relatively low loan growth of 3-5%. Interest rate has been one of the largest drivers of returns. Market is relatively consolidated.   
- Most of the banks have regional presence with DBS and OCBC having a Greater China focus and UOB has more of a focus in ASEAN.   
- Singapore banks have built a respectable fee franchise, particularly wealth management. In recent years there has been a greater focus on capital returns. The banks are seen as global leaders in digitization, especially DBS. Singapore is a leader in the digital assets space.

# Malaysia

- A relatively mature market and loan growth has slowed to 5-6%, with mortgages as one of the largest drivers of loan growth. Asset quality in Malaysia has been relatively stable.   
• Some of the banks have regional ASEAN presence. CIMB has significant exposure to Indonesia and Maybank has significant exposure to Singapore.   
- There is a renewed focus on managing returns with rising shareholder payouts. In the past there has been discussions on banks' consolidation, even though the sector is already relatively consolidated.   
- Since Malaysia has a large Muslim population, the country has a dual banking system, conventional and Islamic.

# HK Banks Snapshot

Loan Book Split   
![](images/1f9d4bdbb2bd14f0dbb44a97a33b28bd9208fcb051bb7547406e6a3bfa49f7ce.jpg)

<details>
<summary>bar_stacked</summary>

| Category | HK Mortgage (%) | HK Personal (%) | HK Commercial (%) | Mainland China (%) | Other Asia (%) | UK (%) | Rest of Europe (%) | N.America (%) | Latin America (%) | Mid. East and Africa (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Stan C. | 10 | 5 | 10 | 5 | 45 | 20 | 0 | 0 | 0 | 5 |
| HSBC | 10 | 5 | 15 | 5 | 20 | 30 | 0 | 0 | 0 | 5 |
| BOCH-K | 30 | 10 | 40 | 5 | 15 | 0 | 0 | 0 | 0 | 0 |
</details>

Source: Company Reports, MS. Data as of FY25. Data based on legal location of guarantor; economic allocation of loans maybe different

Return Level   
![](images/84becab59a22a71a35eaf5fc45b6586bfbec7b4280e8a1e48636c62debc75bd6.jpg)

<details>
<summary>bar</summary>

RoTE 2025 vs. 2024
| Company | 2025 (%) | 2024 (%) |
| :--- | :--- | :--- |
| STAN.C | 11.8 | 9.7 |
| HSBC | 13.3 | 14.5 |
| BOCHK | 11.4 | 11.6 |
</details>

Source: Company Reports, MS

# Themes

Capital Position   
![](images/47c38de9c18ce839c74c55ce23b31c5e808c53e3247c4398608b6d3eb843d8c5.jpg)

<details>
<summary>bar</summary>

CET1 (2025)
| Category | Value (%) |
| :--- | :--- |
| BOCHK | 10.0 |
| CET1 | 24.0 |
| STANC | 13.5 |
| CET1 | 14.0 |
| HSBC | 14.5 |
| Reg. Req | 10.0 |
</details>

Source: Company Reports, MS. Reg. req refers to   
Pillar 1. HK banks also have an undisclosed Pillar 2 requirement

Dividend Payout and Yield   
![](images/a66e1041276bdbf9f3d8d90f3ae1dd21fccb8b2c72ad5f40f2e85ca21fbdd3ff.jpg)

<details>
<summary>scatter</summary>

| Company | Dividend Payout 2026e | Dividend Yield 2026e |
|---------|------------------------|----------------------|
| STANC   | 30.0%                  | 2.5%                 |
| HSBC    | 50.0%                  | 4.5%                 |
| BOCHK  | 58.0%                  | 4.5%                 |
</details>

Source: Company data, MS

# Who are the HK Banks?

# HSBC (5.HK)

- A London-headquartered bank with a dominant market share in HK (33% group revenues) and a large presence in UK (20% group revenues). The rest of the group spread across the rest of Asia and Europe, the Middle East and the Americas.   
• A deposit-driven franchise with a strong CASA ratio, especially in HK. HSBC is rate sensitive.   
- The key differentiating factor is its global network, with a strong focus on leveraging that network to support trade and capital flows and to grow its wealth businesses.   
• RoE improving and the group targets 17% or better RoTE in each year from 2026 to 2028.   
• We expect increased IT investment as HSBC looks to transform its business.

# Standard Chartered (2888.HK)

• A London-headquartered, emerging markets-focused bank, with 60% of income from Asia, 6% from UAE and 14% from the UK and US. It has 81k employees across 54 markets.   
- It survived GFC well but was hit by credit problems in 2015-17. The turnaround and transformation are now complete. Management is focused on achieving leadership in four key areas, EM wholesale banking, mass retail, affluent client business (wealth) and sustainability.   
- RoTE is improving (11.9% in 2025), the key driver of share prices will be the extent to which RoTE can be lifted towards the >15% target by 2028e.

# BOCHK (2388.HK)

• 65.65% owned by Bank Of China (BOC).   
- HK-focused business, with 15%/20% deposit/loan market share in HK and a CASA ratio of 53.4%. Historically, it has grown loans and deposits ahead of the market.   
• CNY clearing bank, dominant market share in China-linked IPOs.   
- Mainland China presence is lower than other local HK banks (5% total loans). In 2016/17, it acquired most of BOC's ASEAN businesses.   
- Operates with a low cost/income ratio (\~24%), low credit costs (<50bps), and high capital ratios. \~50% dividend payout.

# II. THE FUNDAMENTALS

Returns Profile 

<table><tr><td>2025</td><td>Indonesia</td><td>Malaysia</td><td>Philippines</td><td>Singapore</td><td>Thailand</td><td>BOCHK</td><td>HSBC</td><td>Stan.C</td></tr><tr><td>Net int income</td><td>5.1%</td><td>2.1%</td><td>4.1%</td><td>1.6%</td><td>2.9%</td><td>1.2%</td><td>1.1%</td><td>1.3%</td></tr><tr><td>Interest income</td><td>7.3%</td><td>3.7%</td><td>5.9%</td><td>3.3%</td><td>4.0%</td><td>2.8%</td><td>3.1%</td><td>2.9%</td></tr><tr><td>Interest expense</td><td>-2.1%</td><td>-1.7%</td><td>-1.8%</td><td>-1.7%</td><td>-1.1%</td><td>1.6%</td><td>2.0%</td><td>1.6%</td></tr><tr><td>Non-int income</td><td>2.0%</td><td>0.8%</td><td>1.5%</td><td>0.9%</td><td>1.3%</td><td>0.6%</td><td>1.2%</td><td>1.1%</td></tr><tr><td>Net fee income</td><td>1.1%</td><td>0.3%</td><td>0.9%</td><td>0.1%</td><td>0.7%</td><td>0.3%</td><td>0.4%</td><td>0.5%</td></tr><tr><td>Non interest income</td><td>0.9%</td><td>0.5%</td><td>0.7%</td><td>0.9%</td><td>0.6%</td><td>0.3%</td><td>0.7%</td><td>0.6%</td></tr><tr><td>Operating income</td><td>7.1%</td><td>2.8%</td><td>5.6%</td><td>2.5%</td><td>4.1%</td><td>1.8%</td><td>2.3%</td><td>2.4%</td></tr><tr><td>Operating expense</td><td>-3.0%</td><td>-1.3%</td><td>-3.0%</td><td>-1.1%</td><td>-1.8%</td><td>0.4%</td><td>1.1%</td><td>1.5%</td></tr><tr><td>Pre-provision profit</td><td>4.1%</td><td>1.6%</td><td>2.6%</td><td>1.4%</td><td>2.3%</td><td>1.4%</td><td>1.2%</td><td>0.9%</td></tr><tr><td>Provision</td><td>-0.8%</td><td>-0.1%</td><td>-0.4%</td><td>-0.2%</td><td>-0.8%</td><td>0.2%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>Loan Loss Provision</td><td>-0.9%</td><td>-0.1%</td><td>-0.4%</td><td>-0.2%</td><td>-0.8%</td><td>0.2%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>Other provisions</td><td>0.2%</td><td>0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Operating profits</td><td>3.3%</td><td>1.4%</td><td>2.2%</td><td>1.3%</td><td>1.4%</td><td>1.2%</td><td>1.2%</td><td>0.8%</td></tr><tr><td>Others</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>PBT</td><td>3.3%</td><td>1.4%</td><td>2.2%</td><td>1.3%</td><td>1.5%</td><td>1.1%</td><td>1.2%</td><td>0.8%</td></tr><tr><td>Tax</td><td>-0.7%</td><td>-0.3%</td><td>-0.4%</td><td>-0.2%</td><td>-0.3%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>PAT</td><td>2.6%</td><td>1.1%</td><td>1.8%</td><td>1.1%</td><td>1.2%</td><td>0.9%</td><td>0.7%</td><td>0.6%</td></tr><tr><td>Minorities</td><td>-0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>-0.1%</td><td>0.0%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>ROA</td><td>2.6%</td><td>1.1%</td><td>1.8%</td><td>1.1%</td><td>1.1%</td><td>0.9%</td><td>0.7%</td><td>0.5%</td></tr><tr><td>Leverage (x)</td><td>7.2</td><td>10.4</td><td>8.2</td><td>11.9</td><td>8.1</td><td>12.3</td><td>19.7</td><td>23.3</td></tr><tr><td>ROE</td><td>18.4%</td><td>11.2%</td><td>14.5%</td><td>13.2%</td><td>9.1%</td><td>11.4%</td><td>13.3%</td><td>12.0%</td></tr></table>

Source: Company Reports, MS

# Market Structure in ASEAN

Singapore   
![](images/4c4ac664ac5cb97bf24733114d41ecaa3903cdde15e3273679b6ee2d16822027.jpg)

<details>
<summary>bar_stacked</summary>

| Category | DBS (%) | UOB (%) | OCBC (%) | CIMB (%) | MBBM (%) | RHB (%) | HSBC (%) | Stan.C (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Loan | 20 | 15 | 10 | 5 | 5 | 5 | 10 | 10 |
| Deposit | 23 | 24 | 18 | 0 | 0 | 0 | 15 | 15 |
Total: ~90%. The chart displays stacked bars representing the proportional allocation for each institution within a loan and deposit categories.
</details>

Malaysia   
![](images/c690be761f74537d560bae4d04613c68d8d0ba35f1ffb584e575c7a73a353787.jpg)

<details>
<summary>bar_stacked</summary>

| Category | HSBC (%) | UOB (%) | OCBC (%) | RHB (%) | AMMB (%) | CIMB (%) | Public Bank (%) | Maybank (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Loan | 20 | 5 | 10 | 10 | 5 | 10 | 15 | 5 |
| Deposit | 20 | 5 | 10 | 5 | 5 | 10 | 15 | 5 |
</details>

Philippines   
![](images/c7b532a8bf349594ce1b06f4b44e1babdde7f7aeeb18bd85a35a8c2296e85fd2.jpg)

<details>
<summary>bar_stacked</summary>

| Category | SECB (%) | Metro (%) | BPI (%) | BDO (%) |
| :--- | :--- | :--- | :--- | :--- |
| Loan | 5 | 10 | 12 | 28 |
| Deposit | 3 | 10 | 10 | 22 |
</details>

Thailand   
![](images/2b4a4b451d55630347063f4744e1cfc770a5ed2899321e19662331310578e34f.jpg)

<details>
<summary>bar_stacked</summary>

| Category | MBBM (%) | CIMB (%) | UOB (%) | TMB (%) | KTB (%) | Kbank (%) | BBL (%) | SCBx (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Loan | 2 | 1 | 0 | 5 | 13 | 17 | 14 | 13 |
| Deposit | 0 | 0 | 0 | 0 | 12 | 14 | 20 | 14 |
</details>

Indonesia   
![](images/4fe61efaf18b360e6d2ad7f62d035f60ab120a71acee0355e43b52a8c7684f15.jpg)

<details>
<summary>bar_stacked</summary>

| Category | HSBC (%) | MBBM (%) | CIMB (%) | UOB (%) | OCBC (%) | BBNI (%) | BBCA (%) | BBRI (%) | BMRI (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Loan | 2 | 1 | 0 | 5 | 3 | 10 | 10 | 15 | 2 |
| Deposit | 0 | 0 | 0 | 0 | 0 | 8 | 12 | 15 | 14 |
</details>

Source: Company Reports, Central Banks data, MS

# Market Shares in Hong Kong

Loan for use in HK market share   
![](images/48c044692fbb827e6caf8853d46ead0e39699a8edf699a31a2f9738f7c9e2b21.jpg)

<details>
<summary>pie</summary>

| Entity | Percentage (%) |
| :--- | :--- |
| HSBC | 29 |
| BOCHK | 20 |
| STANC | 7 |
| BEA | 4 |
| DBS (HK) | 3 |
| Others | 37 |
</details>

Deposit market share   
![](images/0f2449ca1c74da3205ff0e94ccd3e30f490388e7a570908e1ff4078cc9e589ab.jpg)

<details>
<summary>pie</summary>

| Entity | Percentage (%) |
| :--- | :--- |
| HSBC | 25 |
| BOCHK | 15 |
| STANC | 11 |
| BEA | 4 |
| DBS (HK) | 2 |
| Others | 44 |
</details>

Mortgage market share   
![](images/98e537a64f424e6838db74a550a7d067651333750af32c4e94c98d26c266aa45.jpg)

<details>
<summary>pie</summary>

| Category | Value (%) |
|---|---|
| HSBC | 40 |
| BOCHK | 23 |
| STANC | 11 |
| BEA | 5 |
| DBS (HK) | 1 |
| Others | 20 |
</details>

Credit card market share   
![](images/9165c32ae17a18b4526f86f7a2c233209b4cc629cb94da32144fb1c6f6166065.jpg)

<details>
<summary>pie</summary>

| Entity | Percentage (%) |
| :--- | :--- |
| HSBC | 48 |
| STANC | 22 |
| BOCHK | 8 |
| BEA | 2 |
| DBS (HK) | 6 |
| Others | 13 |
</details>

Source: HKMA, Compa

[中间内容因长度限制已省略]

gan Stanley Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: ASEAN Financials 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/04/2026)</td></tr><tr><td colspan="3">Nick Lord</td></tr><tr><td>CIMB Group (CIMB.KL)</td><td>E (03/23/2020)</td><td>RM7.35</td></tr><tr><td>DBS Group Holdings (DBSM.SI)</td><td>E (10/17/2022)</td><td>S$64.14</td></tr><tr><td>Maybank (MBBM.KL)</td><td>E (01/08/2021)</td><td>RM10.60</td></tr><tr><td>Oversea-Chinese Banking Corp (OCBC.SI)</td><td>E (12/12/2023)</td><td>S$24.00</td></tr><tr><td>Public Bank (PUBM.KL)</td><td>E (02/05/2026)</td><td>RM4.78</td></tr><tr><td>Singapore Exchange Ltd (SGXL.SI)</td><td>O (11/18/2024)</td><td>S$21.88</td></tr><tr><td>United Overseas Bank (UOBH.SI)</td><td>O (12/12/2023)</td><td>S$38.31</td></tr><tr><td>Vietnam Technological and Commercial JSB (TCB.HM)</td><td>E (10/06/2023)</td><td>VND31,700.00</td></tr><tr><td colspan="3">Selvie Jusman, CFA</td></tr><tr><td>Bangkok Bank Public Company Limited (BBL.BK)</td><td>O (02/08/2024)</td><td>Bt174.50</td></tr><tr><td>Bank Central Asia (BBCA.JK)</td><td>O (12/05/2023)</td><td>Rp5,425</td></tr><tr><td>Bank Jago Tbk PT (ARTO.JK)</td><td>O (05/10/2023)</td><td>Rp1,035</td></tr><tr><td>Bank Mandiri (BMRI.JK)</td><td>U (05/07/2025)</td><td>Rp3,970</td></tr><tr><td>Bank Negara Indonesia (BBNI.JK)</td><td>E (03/12/2025)</td><td>Rp3,420</td></tr><tr><td>Bank of the Philippine Islands (BPI.PS)</td><td>E (05/14/2026)</td><td>PP94.75</td></tr><tr><td>Bank Rakyat Indonesia (BBRI.JK)</td><td>E (12/11/2025)</td><td>Rp2,810</td></tr><tr><td>BDO Unibank (BDO.PS)</td><td>E (05/14/2026)</td><td>PP118.00</td></tr><tr><td>Kasikorn Bank Public Company (KBANK.BK)</td><td>E (09/11/2025)</td><td>Bt203.00</td></tr><tr><td>Krung Thai Bank Public Company (KTB.BK)</td><td>E (04/04/2024)</td><td>Bt35.50</td></tr><tr><td>SCB X PCL (SCB.BK)</td><td>E (02/08/2024)</td><td>Bt141.00</td></tr><tr><td>Security Bank Corporation (SECB.PS)</td><td>E (01/08/2021)</td><td>PP62.70</td></tr><tr><td>TMBThanachart Bank PCL (TTB.BK)</td><td>U (12/21/2023)</td><td>Bt2.28</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.

© 2026 MS
"""
