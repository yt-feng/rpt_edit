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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## HK/China

## Capital Flow Policy: Mixed impacts, clearer framework - gauging implications for CNY and Banks

China's policymakers have introduced multiple regulatory updates affecting capital flows in recent months, including tighter outbound investment rules. Taken together, these measures reflect a mix of relaxation and tightening with differing implications for cross-border flows, and we view them as part of a broader effort to complete a comprehensive capital-flow regulatory framework rather than a move to restrict capital outflows. From an FX perspective, we expect the latest changes to provide a modest near-term tailwind for the CNY, although the medium-term implications are less clear. For the banking sector, we see BOC benefiting from a NIM tailwind as FX deposit spreads widen, while for Hong Kong banks, the potential headwind to wealth management tied to Mainland Chinese Visitor (MCV) business is well-flagged (link), but the tailwind from CIB activity appears underappreciated. In particular, we expect STAN and HSBC to benefit from the relaxation of multi-national company's cash management rules, greater flexibility around onshore corporates' overseas lending, expanded regulated channels for inbound/outbound financial investments, and continued progress in RMB internationalization.

## A holistic view on regulatory changes regarding capital flows

\- It is not a one-way street: The recently announced update to outbound investment regulations has raised concerns about tighter capital controls. However, over the past 12 months, Chinese policymakers have introduced multiple regulatory updates affecting capital flows. Reviewing these measures (Table 2-Table 3), we see a mix of relaxation and tightening, with differing policy directions and implications for cross-border flows. This reinforces our view that the latest developments are less about cracking down on capital outflows and more about building a comprehensive governance framework for managing capital flows.

\- What's been relaxed? Key points include the following: 1) On cash management for multi-national companies operating in China, they have more flexibility in currency conversion and fund management for their RMB and FX liquidity onshore and offshore. 2) On onshore corporates extending loans overseas, regulators increased the quota, and require lender companies to make filing instead of getting approval from SAFE. 3) The PBOC and HKMA expanded the list of eligible institutions to participate in southbound Bond Connect and the PBOC resumed QDII quota approvals. 4) There is relaxation regarding onshore banks' indirect offshore lending. Previously, there were strict criteria regarding onshore banks making indirect lending to offshore corporates via offshore banks. Under the new regulation (Doc 72), the criteria have been removed. In our view, at times when asset returns offshore are higher than onshore, the above-mentioned regulatory changes may be accommodative towards outbound flows.

\- What's been tightened? The following regulatory updates may be relatively more accommodative towards inflows and more restrictive towards outflows.

## Banks & Financial Services

## Katherine Lei AC

(852) 2800-8552

katherine.lei@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

## Tiffany Wang AC

(852) 2800-1726

tiffany.r.wang@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

## Tingting Ge

(852) 2800-0143

tingting.ge@JPM.com

JPM Chase Bank, N.A., Hong Kong Branch

## Peter Zhang

(852) 2800-8557

peter.zhang@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

## Lincoln Yu

(852) 2800 8523

lincoln.yu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

## Haomin Chen

(86-21) 6106 6347

haomin.chen@JPM.com

SAC Registration Number: S1730524080002

JPM Securities (China) Company Limited

1) Outbound investment rule announced on June 1 tightened corporate outbound investments and brought individual investors' outbound investments into regulatory scope, though details are yet to be released (link, link). 2) CSRC and seven other agencies jointly announced tightening enforcement regarding cross-border securities trading regulation (link). 3) Doc 252 requires China companies to timely repatriate their offshore IPO proceeds back to China, unless they obtain approval for eligible use of proceeds overseas. We do not expect this to have a material impact on existing business practices, following "Capital Account Foreign Exchange Business Guidelines (2024 Edition)" released by SAFE in 2024.

## Macro & FX views

\- We do not view the latest regulatory development as a broad-based move to restrict capital outflows. First, from a policy consistency perspective, China still needs to align implementation with its longer-term RMB internationalization agenda, which requires deeper and more accessible offshore RMB liquidity. Second, the current FX backdrop does not suggest an urgent macro need to tighten outflow controls, as the CNY is facing appreciation rather than depreciation pressure. Third, we noted easing outflow pressures. We estimate cumulative resident outflows over 2023-25 at around \$1.3tn, including roughly \$507bn (0.4% of GDP) via unofficial channels (Figure 1). Note that the cumulative resident outflow via unofficial channels has stabilized at \~\$500bn since mid-2025, implying easing outflow pressure. On an FX-adjusted basis, returns on Chinese equities now compare more favorably with US markets, marking a shift from the structural discount seen in prior years, which partly contributed to the easing outflow pressure.

\- Macro implications: Recent cross-border tightening looks less like a crackdown on capital outflows and more like a comprehensive governance framework for managing cross-border flows across capital, technology, data and talent; key watchpoints are the follow-up implementation rules that define practical boundaries, and whether Beijing expands compliant channels, via more approved routes, higher quotas, or both, to keep the framework consistent with RMB internationalization initiatives.

\- FX implications - tightening in outbound investment rules may provide a near-term tailwind for CNY strength, by reducing outflow pressure and supporting repatriation. However, Chinese investors remain structurally underexposed to global assets relative to regional peers, suggesting that underlying diversification demand will persist. Over the medium term, the bias likely remains toward continued outbound flows from residents. Against this backdrop, and with currency stability no longer a binding constraint, the policy makers in fact selectively eased formal outbound channels since last year, including relaxed investment rules for southbound Bond Connect and the resumption of QDII quota approvals by the PBOC (Figure 4). Therefore, the recent tightening should be viewed less as a shift towards broad capital control tightening, but more as an effort to improve the composition and transparency of flows. We expect policymakers to keep opening “front-door” channels for controlled overseas allocation, while maintaining pressure on informal or unregulated routes.

## Banking sector and stock implications

- Implications for the banking sector – on track for opening of financial markets: China’s top policy makers have reiterated their commitment to open up China’s financial market (link) and RMB internationalization (link). We view the recent regulatory changes as part of a broader effort to complete a comprehensive capital-flow regulatory framework, which involves enhancing information flows and government oversight, and minimizing potential friction as China accelerates financial-sector opening and RMB internationalization. While these changes may cause temporary disruption in offshore wealth management - particularly in Hong Kong SAR for Mainland Chinese Visitor (MCV) business (as highlighted here), the longer-term trajectory should be an expansion of CIB business opportunities for selected financial institutions. Overall, we expect the net impact to be positive for HK/China banks over the medium to long term.  
- Improvement in FX deposits spread – BOC benefits the most: The removal of loan proceeds use restriction for onshore banks' overseas corporate loans, according to Doc 72, will improve related loan demand, in our view. This benefits banks with strong domestic FX deposits franchise, as banks can allocate the FX deposits to fund overseas corporate lending to improve deposits spread. Among China banks we cover, BOC's FX deposits account for 16% of Group liabilities, the highest among peers (peers' average 4%). This should become a tailwind for its NIM, all else equal.  
- Rise in corporate & investment banking (CIB) business for selected banks – STAN and HSBC stand to benefit: The relaxation on cash management for multi-national companies operating in China will benefit banks with strong onshore and offshore cash management capacity in RMB and foreign currencies. Relaxation on onshore corporate's overseas lending will benefit banks with ability to advise and provide currency hedging services. And the acceleration in RMB internationalization, as evidenced by rise in Dim Sum bonds and expansion of southbound Bond Connect program, etc., may benefit banks with strong onshore and offshore CIB franchise. Among banks in our coverage, STAN and HSBC will benefit the most via their CIB business, followed by BOC.

Figure 1: Resident outflows from China have picked up in recent years, with unrecorded flows accounting for a major share  
![](images/0bbab823a5f309bf4eca0baab00de0d16ff9555a1d6346f9b800f9bda5f8427b.jpg)

<details>
<summary>area chart</summary>

| Month    | Outflows via unofficial channels | outflows via regulated channels |
| -------- | ------------------------------- | ------------------------------- |
| Mar-23   | 0                               | 0                               |
| Jun-23   | -100                            | -100                            |
| Sep-23   | -200                            | -200                            |
| Dec-23   | -300                            | -300                            |
| Mar-24   | -400                            | -400                            |
| Jun-24   | -500                            | -500                            |
| Sep-24   | -600                            | -600                            |
| Dec-24   | -700                            | -700                            |
| Mar-25   | -800                            | -800                            |
| Jun-25   | -900                            | -900                            |
| Sep-25   | -1000                           | -1000                           |
| Dec-25   | -1100                           | -1100                           |
</details>

Source: SAFE, JPM (see our FX team note here). Note: In \$bn, cumulative since 1Q23.

Figure 2: The synchronized strength in CNY FX and Chinese equities has created return synergies for domestic investors  
![](images/5938f6950edcd687669ea434ea966b2a77b813e0b9f4d36f55f74005bb956ccb.jpg)

<details>
<summary>line chart</summary>

| Date   | ChiNext vs SPX returns in CNY | CSI300 vs SPX returns in CNY |
|--------|-------------------------------|------------------------------|
| Jan-15 | ~50%                          | ~50%                         |
| Jan-16 | ~-30%                         | ~-30%                        |
| Jan-17 | ~-10%                         | ~-10%                        |
| Jan-18 | ~-20%                         | ~-20%                        |
| Jan-19 | ~-50%                         | ~-50%                        |
| Jan-20 | ~30%                          | ~30%                         |
| Jan-21 | ~20%                          | ~20%                         |
| Jan-22 | ~-10%                         | ~-10%                        |
| Jan-23 | ~-20%                         | ~-20%                        |
| Jan-24 | ~-30%                         | ~-30%                        |
| Jan-25 | ~-10%                         | ~-10%                        |
| Jan-26 | ~50%                          | ~50%                         |
</details>

Source: Bloomberg Finance L.P., JPM (see our FX team note here). Note: Relative return of Chinese stocks vs SPX returns in CNY terms, 6m rolling.

Figure 3: Resident outflows through southbound Bond Connect have picked up since last year's policy relaxation  
![](images/22f26fee84d6c3afddac83cb165efff6dc1c3f9a4bb0fd0c067225e2cee81f9e.jpg)

<details>
<summary>line chart</summary>

| Date    | monthly southbound Bondconnect outflows ($bn) | cumulative since Sep 21 (rhs) |
|---------|-----------------------------------------------|-------------------------------|
| Sep-21  | 6.00                                          | 0                             |
| Mar-22  | -12.00                                        | -40                           |
| Sep-22  | -8.00                                         | -60                           |
| Mar-23  | -4.00                                         | -80                           |
| Sep-23  | 4.00                                          | -100                          |
| Mar-24  | -2.00                                         | -120                          |
| Sep-24  | -6.00                                         | -140                          |
| Mar-25  | -8.00                                         | -140                          |
| Sep-25  | -10.00                                        | -140                          |
| Mar-26  | -12.00                                        | -140                          |
</details>

Source: SHCH, JPM (see our FX team note here).

Figure 4: The PBOC has resumed the expansion of the QDII quota  
![](images/bc4c534aba0328bcf27119c8a4606460fa1e3a62e806cab9809903eb81986e45.jpg)

<details>
<summary>line chart</summary>

| Date | Value |
|---|---|
| May-10 | 15 |
| May-12 | 18 |
| May-14 | 20 |
| May-16 | 90 |
| May-18 | 90 |
| May-20 | 105 |
| May-22 | 155 |
| May-24 | 165 |
| May-26 | 175 |
</details>

Source: PBOC, JPM (see our FX team note here).

Figure 5: Dim Sum and Panda bond issuance is growing  
![](images/073657e7c17b84ede8c424886a07f349a605beee5a09828fbe7bb92a33e3d941.jpg)

<details>
<summary>bar chart</summary>

| Year | Panda bond new issuance (Rmb bn) | Dim Sum bond new issuance (Rmb bn) |
|---|---|---|
| 2015 | 10 | 340 |
| 2016 | 130 | 230 |
| 2017 | 60 | 100 |
| 2018 | 80 | 130 |
| 2019 | 40 | 250 |
| 2020 | 50 | 290 |
| 2021 | 110 | 340 |
| 2022 | 80 | 730 |
| 2023 | 150 | 940 |
| 2024 | 190 | 1250 |
| 2025 | 170 | 1360 |
| 5M26 | 130 | 710 |
</details>

Source: Wind, JPM. Note: Panda bonds are RMB-denominated bonds issued by foreign entities inside mainland China, while Dim Sum bonds are RMB-denominated bonds issued outside mainland China for international investors.

Figure 6: FX deposits as % of total liabilities by bank  
![](images/a653eed5c39094024b87328c6fed6cf24b891494569a436df32cc67a57e757ca.jpg)

<details>
<summary>bar chart</summary>

| Company | FX deposits as % of total liabilities - 2025 |
|---|---|
| BOC | 15.8 |
| CMB | 7.3 |
| Citic | 6.9 |
| BoComm | 5.6 |
| Pingan | 4.2 |
| ICBC | 3.9 |
| Minsheng | 3.8 |
| SPDB | 3.7 |
| Industrial | 3.5 |
| Huaxia | 3.2 |
| CCB | 3.0 |
| Everbright | 3.0 |
| ABC | 2.9 |
| PSBC | 0.1 |
</details>

Source: Company data.

Table 1: Summary of key regulated outbound investment channels

<table><tr><td>Name</td><td>Qualified assets</td><td>Qualified investors</td><td>Cap/flow limits</td></tr><tr><td>Stock Connect (southbound)</td><td>HK equities</td><td>Individual and institutional investors</td><td>Daily flow cap of CNY42bn</td></tr><tr><td>SH-LN Stock Connect (eastbound)</td><td>Equity (CDR)</td><td>Individual and institutional investors</td><td>CNY250bn</td></tr><tr><td>QDII/RQDII</td><td>Overseas securities including bonds and equities</td><td>Institutional investors</td><td>HK$176bn</td></tr><tr><td>Mutual Recognition of Funds (southbound)</td><td>Public funds in HK</td><td>Individual and institutional investors</td><td>CNY300bn</td></tr><tr><td>WMP connect (southbound)</td><td>Wealth management products in HK</td><td>Qualified retail investors in the Greater Bay Area</td><td>CNY150bn</td></tr><tr><td>Payment connect (southbound)</td><td>Cash</td><td>NA</td><td>Subject to the $50k/year quota for cash service</td></tr><tr><td>Bond Connect (southbound)</td><td>Bonds in HK</td><td>Institutional investors</td><td>CNY500bn</td></tr><tr><td>QDLP (Qualified Domestic Limited Partner)/QDIE (Qualified Domestic Investment Enterprise)</td><td>Overseas securities in secondary and primary markets, HF, PE, REIT etc.</td><td>Institutional investors</td><td>Case by case on pilot</td></tr><tr><td>Cash</td><td>Cash</td><td>Individual investors</td><td>Annual limit of $50k/person</td></tr></table>

Source: PBOC, HKEX, J.P Morgan (see our FX team note here).

Table 2: Summary of recent regulatory changes on cross-border capital management

<table><tr><td>Document</td><td>Target audience and topic</td><td>What's changed?</td><td>Notes</td></tr><tr><td>Relaxation</td><td></td><td></td><td></td></tr><tr><td>"Notice of PBOC and SAFE on Matters Related to Multinational Corporations' Integrated RMB and Foreign-currency Cash Pooling Business"(Doc 251) issued in Dec 2025"中国人民银行 国家外汇管理局关于跨国公司本外币一体化资金池业务有关事宜的通知"</td><td>Targeting multinational corporations on cash management</td><td>Advance from the pilot program first released in 2021 in 10 trial cities and provinces, and establish a country-level framework allowing multinational companies to centrally operate and manage onshore and offshore RMB and foreign currency funds. Some key points include:1) Set uniform standard for RMB and foreign currency cash management business. Companies can set up one cross-border cash pool to manage onshore and offshore RMB and FX, with SAFE being the direct regulator; while under previous practice, companies need to maintain two separate cross-border cash pools, with RMB cash pool regulated by the PBOC and FX ca

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
