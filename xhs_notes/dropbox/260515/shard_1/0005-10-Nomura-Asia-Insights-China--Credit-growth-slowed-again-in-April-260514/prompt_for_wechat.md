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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China: Credit growth slowed again in April

New aggregate financing (AF) came in significantly below market expectations in April, with outstanding AF growth declining to 7.8% y-o-y from 7.9% in March. Within AF, the primary drags were new RMB loans and government bond issuance, which more than offset the relatively sanguine corporate bond issuance. Outstanding RMB loan growth fell to a fresh historical low of 5.6% in April from 5.7% in March, weighed down by both the household and corporate sectors, with the former particularly weak compared with year earlier levels. New loans in the corporate sector may appear adequate on the surface, as they exceeded year earlier levels, but this was primarily attributable to a sUBStantial volume of bill financing, which is not a genuine indicator of corporate credit demand, in our view. Stripping out this distortion, the headline new RMB loan figure would look even weaker. In addition, new household loans remain particularly concerning, having been persistently soft since the beginning of the year. Government bond issuance was modestly weaker than year earlier levels in April, which was slightly surprising. Looking ahead, we still expect government bond issuance to accelerate in coming months, owing to Beijing's need to support still-weak fixed asset investment, which in turn should help to steady credit expansion.

# We expect no policy rate or RRR cuts in 2026

Following the latest Politburo meeting held at the end of April, we have completely removed our forecast for any RRR cut or policy rate cut in 2026. Previously, we had expected one 50bp RRR cut in Q2 and a 10bp policy rate cut in Q4. The Politburo's assessment of the current state of the economy and its wording on monetary policy, which is consistent with all recent PBoC communications, showed no signs of near-term urgency for monetary easing. Moreover, amid the ongoing double blockade of the Strait of Hormuz and the associated global energy shock, domestic inflation began to show a notable pickup in April. The inflationary pressure has been further compounded by pronounced price increases in certain imported products (most notably memory chips). Import growth remained highly elevated at $25.3\%$ y-o-y in April, to which the price impact of semiconductor imports made a notable contribution. In the Q1 Monetary Policy Report released earlier this week, the PBoC explicitly warned of the importance of monitoring imported inflationary pressures caused by the ongoing energy shock. As such, we believe the PBoC is likely to keep its RRR and policy rate tools steady this year.

# A review of April's credit data

- New aggregate financing totalled RMB621bn in April, far below market expectations (Consensus: RMB1,251bn; NOM: RMB1,019bn; April 2025: RMB1,160bn), with growth in outstanding AF slowing to 7.8% y-o-y in April, from 7.9% in March, the weakest monthly reading on record.   
- New RMB loans in April totalled -RMB10bn, notably below market expectations (Consensus: RMB300bn; NOM: RMB384bn; April 2025: RMB280bn), the first negative monthly reading since July 2025, with growth in outstanding RMB loans declining to $5.6\%$ y-o-y in April from $5.7\%$ in March, reaching another historical low.   
- M2 growth was 8.6% y-o-y in April, up marginally from 8.5% in March, while M1 growth edged down to 5.0% from 5.1%.

# New RMB loans posted lowest April reading on record

New RMB loans tumbled to -RMB10bn in April, the lowest April reading on record, weighed on by weakness in both corporate and household sectors. New bill financing surged to a record high, pointing to even weaker loan demand in the corporate sector.

# A breakdown of bank loans

New RMB loans to the corporate sector fell markedly to RMB390bn in April from RMB610bn a year earlier, as both new medium- to long-term loans slumped to -RMB410bn from

# Research Analysts

# Asia Economics

Harrington Zhang - NIHK

harrington.zhang@NOM.com

+852 2252 2057

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Hannah Liu - NIHK

hannah.liu@NOM.com

+852 2252 1082

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

RMB250bn, while the new short-term component was at -RMB460bn, largely unchanged from -RMB480bn a year earlier. However, new bill financing surged to a record high of RMB1,243bn in April from RMB834bn a year earlier, suggesting actual corporate loan demand could have been even weaker. Meanwhile, new corporate bond financing under the AF rose to RMB454bn in April from RMB234bn a year earlier, underscoring the possibility of a shift in corporate funding to bonds from loans.

New RMB loans to the household sector fell sharply to -RMB787bn in April from -RMB522bn a year earlier, as both the new short-term and medium- to long-term components turned more negative in April, falling to -RMB446bn and -RMB341bn, respectively, from -RMB402bn and -RMB123bn a year earlier. The persistent weakness in household loan data suggest households are still generally cautious about their borrowing.

New RMB loans to non-bank financial institutions increased slightly to RMB175bn in April from RMB163bn in a year earlier.

# New household deposits continued to decelerate

Amid weak household loans, new household deposits fell markedly to -RMB1.9trn in April from -RMB1.4trn a year earlier. Nevertheless, overall new RMB deposits increased to RMB270bn in April from -RMB440bn a year earlier, driven by the government sector and non-bank financial institutions (NBFI). In detail, with elevated government bond issuance, new fiscal deposits increased to RMB739bn in April from RMB371bn a year earlier. For NBFIs, their new deposits increased to RMB2.5trn in April from RMB1.6trn a year earlier. We reckon the deposit breakdown pattern may reveal a potential modest shift from household deposits to NBFIs, as trillions of households' time deposits are set to mature this year, while lower bank deposit rates are prompting households to seek better returns from investment products offered by NBFIs.

# Details of the new AF data

New aggregate financing totalled RMB621bn in April, far below market expectations (Consensus: RMB1,251bn; NOM: RMB1,019bn; April 2025: RMB1,160bn), with growth in outstanding AF slowing to $7.8\%$ y-o-y in April, from $7.9\%$ in March, the weakest monthly reading on record. The drag came from weak new RMB loans.

# A breakdown of new AF

New RMB loans included in AF (excluding loans to financial institutions) dipped to -RMB400bn from RMB88bn a year earlier. Net government bond issuance fell to RMB906bn in April from RMB973bn a year earlier. For other key components, net corporate bond financing totalled RMB454bn in April, above the RMB234bn recorded a year earlier. Net financing from undiscounted bankers' bills totalled -RMB528bn in April, below the -RMB279bn a year earlier. Shadow financing including new trust loans and entrusted loans declined to -RMB41bn in April from -RMB8bn a year earlier.

# M2 growth edged up in April

M2 growth edged up to 8.6% y-o-y in April from 8.5% in March, despite a higher base and an increase in fiscal deposits. Fiscal deposits rose by RMB739bn in April, above the RMB371bn increase recorded a year earlier. By contrast, M1 growth edged down to 5.0% y-o-y in April from 5.1% in March.

Liquidity conditions eased notably in April, with the daily average DR007 (interbank repo rates between banks only) declining to 1.35% from 1.44% in March, dropping below the PBoC's 7-day reverse repo rate of 1.40%. This is the first time monthly DR007 has been below the policy rate since August 2023. The monthly average yield on the 10-year CGB dropped to 1.78% in April from 1.81% in March. For long-term liquidity management, the PBoC net withdrew RMB800bn from the banking system in April (ORR: -RMB400bn; MLF: -RMB200bn; PSL: -RMB200bn).

Fig. 1: Major money and credit indicators 

<table><tr><td>Major money and credit indicators</td><td>Apr 26</td><td>Mar 26</td><td>Apr 25</td><td>2025</td><td>2024</td></tr><tr><td>New RMB loans (RMBbn)</td><td>-10</td><td>2,990</td><td>280</td><td>16,270</td><td>18,090</td></tr><tr><td>to the corporate sector</td><td>390</td><td>2,660</td><td>610</td><td>15,470</td><td>14,330</td></tr><tr><td>short-term loans</td><td>-460</td><td>1,480</td><td>-480</td><td>4,810</td><td>2,610</td></tr><tr><td>medium- to long-term loans</td><td>-410</td><td>1,350</td><td>250</td><td>8,820</td><td>10,080</td></tr><tr><td>bill financing</td><td>1,243</td><td>-191</td><td>834</td><td>1,660</td><td>1,570</td></tr><tr><td>to the household sector</td><td>-787</td><td>491</td><td>-522</td><td>442</td><td>2,720</td></tr><tr><td>short-term loans</td><td>-446</td><td>196</td><td>-402</td><td>-835</td><td>473</td></tr><tr><td>medium- to long-term loans</td><td>-341</td><td>295</td><td>-123</td><td>1,280</td><td>2,250</td></tr><tr><td>to the non-bank financial institutions</td><td>175</td><td>-169</td><td>163</td><td>-110</td><td>286</td></tr><tr><td>Aggregate financing (AF; RMBbn)</td><td>621</td><td>5,227</td><td>1,160</td><td>35,603</td><td>32,256</td></tr><tr><td>New RMB loans</td><td>-400</td><td>3,152</td><td>88</td><td>15,915</td><td>17,050</td></tr><tr><td>Entrusted loans</td><td>-28</td><td>-28</td><td>0</td><td>120</td><td>-58</td></tr><tr><td>Trust loans</td><td>-13</td><td>-17</td><td>-8</td><td>368</td><td>398</td></tr><tr><td>Undiscounted bankers&#x27; acceptance</td><td>-528</td><td>126</td><td>-279</td><td>11</td><td>-330</td></tr><tr><td>Corporate bond</td><td>454</td><td>391</td><td>234</td><td>2,392</td><td>1,909</td></tr><tr><td>Government bond</td><td>906</td><td>1,166</td><td>973</td><td>13,837</td><td>11,296</td></tr><tr><td>M1 growth (% y-o-y)</td><td>5.0</td><td>5.1</td><td>1.5</td><td>3.8</td><td>1.2</td></tr><tr><td>M2 growth (% y-o-y)</td><td>8.6</td><td>8.5</td><td>8.0</td><td>8.5</td><td>7.3</td></tr><tr><td>Outstanding RMB loan growth (% y-o-y)</td><td>5.6</td><td>5.7</td><td>7.2</td><td>6.4</td><td>7.6</td></tr><tr><td>Outstanding AF growth (% y-o-y)</td><td>7.8</td><td>7.9</td><td>8.7</td><td>8.3</td><td>8.0</td></tr></table>

Source: Wind, NOM Global Economics.

Fig. 2: Outstanding AF growth vs nominal GDP growth   
![](images/d9a84e8c714f2f24595b909b19bdc5034b02d0a8ede40b32675dd82aa555cfd2.jpg)

<details>
<summary>line</summary>

| Date   | Outstanding AF growth | Nominal GDP growth |
|--------|------------------------|--------------------|
| Jan-13 | 20                     | 10                 |
| Jan-14 | 18                     | 9                  |
| Jan-15 | 16                     | 8                  |
| Jan-16 | 14                     | 7                  |
| Jan-17 | 16                     | 10                 |
| Jan-18 | 14                     | 11                 |
| Jan-19 | 12                     | 9                  |
| Jan-20 | 10                     | -5                 |
| Jan-21 | 13                     | 22                 |
| Jan-22 | 10                     | 10                 |
| Jan-23 | 9                      | 5                  |
| Jan-24 | 8                      | 4                  |
| Jan-25 | 7                      | 4                  |
| Jan-26 | 8                      | 5                  |
</details>

Source: Wind, NOM Global Economics.

Fig. 3: M2 growth and outstanding RMB loan growth   
![](images/cc6437d73f879bfe3dcda1afe30782c3c731fb60833f79a7b3b08279a5933e03.jpg)

<details>
<summary>line</summary>

| Date   | M2 growth | Outstanding RMB loan growth |
|--------|-----------|-----------------------------|
| Jan-13 | 16.0      | 14.5                        |
| Jan-14 | 14.0      | 14.0                        |
| Jan-15 | 12.0      | 13.5                        |
| Jan-16 | 10.0      | 15.5                        |
| Jan-17 | 8.0       | 13.0                        |
| Jan-18 | 8.5       | 13.0                        |
| Jan-19 | 8.0       | 13.5                        |
| Jan-20 | 8.5       | 13.0                        |
| Jan-21 | 10.0      | 12.5                        |
| Jan-22 | 8.0       | 12.0                        |
| Jan-23 | 12.0      | 11.5                        |
| Jan-24 | 10.0      | 10.0                        |
| Jan-25 | 7.0       | 8.0                         |
| Jan-26 | 6.0       | 5.5                         |
</details>

Source: Wind, NOM Global Economics.

# Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong.

See Disclaimers for NOM Group entity details.

# Analyst Certification

We, Harrington Zhang, Jing Wang, Hannah Liu and Ting Lu, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and sUBSidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other members of the NOM Group; in particular, NOI's interests in PRC securities are not disclosed to, or aggregated with the holdings of, any other NOM Group entities and the interests in PRC securities of other NOM Group entities are not disclosed to, or aggregated with the holdings of, NOI. An individual name printed next to NOI on the front page of a research report indicates that individual is employed by NOI to provide research assistance to NIHK under a research partnership agreement. 'NSFSPL' next to an employee's name on the front page of a research report indicates that the individual is employed by NOM Structured Finance Services Private Limited to provide assistance to certain NOM entities under inter-company agreements. 'Verdhana' next to an individual's name on the front page of a research report indicates that the individual is employed by PT Verdhana Sekuritas Indonesia ('Verdhana') to provide research assistance to NIHK under a research partnership agreement and neither Verdhana nor such individual is licensed outside of Indonesia.

THIS MATERIAL IS: (I) FOR YOUR PRIVAT

[中间内容因长度限制已省略]

934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian Citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are Citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its sUBSidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

# NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
