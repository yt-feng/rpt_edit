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
# China rates: Turn outright pay Jun-3y NDIRS

We now remove the long 30y CGB leg

Since our last update on 6 May, China rates have been trading in a very tight range. The 7d repo fixing moved lower though, against our expectation of a small rebound. That said, swap rates did not rally either, meaning flush liquidity had been expected by the market. With the PBoC having net drained RMB1trn of medium-to-long term liquidity via 3m and 6m ORRs in May so far, we think the risk-reward still favours positioning for small liquidity tightening and higher front-end rates. On the 30y CGB yield, we now see some upside risk owing to the marked selloff in global rates. Thus, we now exit our long 30y CGB leg (current level of 260002: 2.2875%) and turn net paid in Jun-3y NDIRS (indicative USD2k DV01).

# Liquidity – Still flush but PBoC has sped up withdrawal in May

Figure 1 shows that the latest outstanding OMOs dropped to close to zero again. This means that the PBoC has been unable to withdraw further short-term liquidity from the system (as there is not much left any way). Thus, the key focus is how much medium- to long-term liquidity the PBoC has drained.

As we flagged in our previous reports, large net liquidity injections by the PBoC in January-February were one of the main drivers of super flush liquidity in recent months. In Figure 2, we show the cumulative medium- to long-term net liquidity injections from the PBoC since start of the year (via ORRs, MLFs, the PBoC's net CGB purchases, RRR cuts; excluding OMOs), and compare them with those in previous years.

The total net liquidity injection of RMB2.05trn in January-February 2026 was obviously well above the levels of the past few years (2020-25 average as of end-February: RMB631bn). In March and April, liquidity proved to be excessively loose (thanks to very weak domestic demand, the moderate pace of bond issuance, underperformance of onshore equities versus other Asia/DM markets). Accordingly, the PBoC net withdrew RMB200bn and RMB560bn of medium and long-term liquidity, respectively. However, even after the RMB760bn net liquidity withdrawal, YTD injections have still totalled RMB1.29trn as of end-April, which is still higher than the 2020-25 average of RMB963bn.

In May, however, the PBoC sped up the pace of its net liquidity drain by withdrawing RMB1trn of liquidity via 3m and 6m ORRs. As a result, the YTD cumulative liquidity injection has dropped sharply to RMB290bn, well below the average of RMB1.18trn in May 2020-25. We believe money market rates will eventually react to the low absolute level of liquidity in the market (after the RMB1trn net drain in May so far), though we note progress will only likely be gradual and slow.

# Lower 7d repo fixing is unlikely to preclude policy rate cuts

The monthly average spread between the 7d repo fixing and 7d OMO rate fell to -3bp in May (April: +1bp), the first negative print since May 2023. In 2026 so far, the loose liquidity / narrower spread 7d repo fixing and 7d OMO rate have been in line with historical patterns (Figure 3). In 2022-25, six out of seven OMO rate cuts were delivered in Q2 and Q3, and prior to rate cuts, the PBoC would guide/allow the 7d repo fixing to drift lower. Also, the May to September period usually marks the peak of government bond supply (CGBs and LGBs), and is when the PBoC tends to ensure there is sufficient liquidity in the banking system. These might partly explain the seasonality in previous years. Our economics team does not expect any rate or RRR cuts in 2026, and we estimate net government bond supply will rise in June-September (actual/planned issuance in May was below our earlier expectation, due mainly to slow LGB supply). Thus, we see very limited downside in the 7d repo fixing/ broad money market rates.

If we assume seasonality holds well for coming months, then liquidity is likely to tighten

Research Analysts

Asia Rates Strategy

Clair Gao, CFA - NIHK

clair.gao@NOM.com

+852 2252 1081

Albert Leung - NIHK

albert.leung1@NOM.com

+852 2252 1401

from June onwards. In fact, DR001 already started to move higher in May (May MTD average: 1.27%; April average: 1.23%), but DR007 and the 1y NCD yield are yet to rebound from the previous month (Figure 4).

Fig. 1: Outstanding OMOs   
![](images/9a6a5dfc14edeb5f4fbc67cee04fd45b35e0af489c6a1b3bb80bad52f615e6d4.jpg)  
Source: Wind, NOM

Fig. 2: The PBoC's medium- to long-term net liquidity injections (cumulative from the start of the year)   
![](images/9d5fe79faa326a6f7b77cd9844e2dbcf40fba2123f9f15e32296d12668e6a9df.jpg)

<details>
<summary>line</summary>

| Month | 2020 (RMB bn) | 2021 (RMB bn) | 2022 (RMB bn) | 2023 (RMB bn) | 2024 (RMB bn) | 2025 (RMB bn) | 2026 (RMB bn) |
|---|---|---|---|---|---|---|---|
| Jan | 200 | 100 | 150 | 800 | 900 | 1100 | 1100 |
| Feb | 500 | 150 | 300 | 1200 | 1300 | 1400 | 2100 |
| Mar | 1100 | 200 | 400 | 1300 | 1400 | 1500 | 1900 |
| Apr | 1000 | 300 | 900 | 1300 | 1400 | 1400 | 1300 |
| May | 1100 | 350 | 950 | 1350 | 1450 | 2700 | 300 |
| Jun | 800 | 450 | 950 | 1350 | 1450 | 3150 | - |
| Jul | 300 | 950 | 950 | 1350 | 1450 | 3450 | - |
| Aug | 600 | 950 | 950 | 1350 | 1450 | 4150 | - |
| Sep | 950 | 950 | 950 | 1950 | 2350 | 4750 | - |
| Oct | 1250 | 950 | 950 | 2350 | 3150 | 5450 | - |
| Nov | 1650 | 950 | 950 | 2850 | 3750 | 6150 | - |
| Dec | 1950 | 1650 | 1150 | 3650 | - | - | - |
</details>

Source: Wind, the PBoC, NOM

Fig. 3: Monthly average spread between 7d repo fixing and 7d OMO rate   
![](images/5e6fd01df083fc012cb917315aecfbc7ec53cfe7aee7f7c07bdf154af51153a7.jpg)

<details>
<summary>line</summary>

| Month | 2026 (bp) | 2025 (bp) | 2024 (bp) | 2023 (bp) |
|---|---|---|---|---|
| Jan | 15 | 63 | 43 | 8 |
| Feb | 17 | 60 | 20 | 30 |
| Mar | 11 | 48 | 30 | 37 |
| Apr | 1 | 28 | 16 | 24 |
| May | -3 | 24 | 8 | -1 |
| Jun | | 25 | 19 | 17 |
| Jul | | 16 | 12 | 5 |
| Aug | | 11 | 18 | 10 |
| Sep | | 15 | 26 | 20 |
| Oct | | 11 | 40 | 48 |
| Nov | | 11 | 33 | 58 |
| Dec | | 19 | 43 | 64 |
</details>

Source: Bloomberg, Wind, NOM

Fig. 4: DR001, DR007 and 7d OMO rate   
![](images/27f2105a01ab9c45cc6a09337217436844b3ef84d255fd1e988620a5639b8d0b.jpg)

<details>
<summary>line</summary>

| Date   | DR001 | DR007 (1m avg) | 7d OMO | 7d OMO-20bp | 7d OMO+50bp |
|--------|-------|----------------|--------|-------------|-------------|
| Jan-24 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Mar-24 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| May-24 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Jul-24 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Sep-24 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Nov-24 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Jan-25 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Mar-25 | ~1.8  | ~2.0           | ~1.8   | ~1.6        | ~2.3        |
| May-25 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Jul-25 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Sep-25 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Nov-25 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Jan-26 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| Mar-26 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
| May-26 | ~1.8  | ~1.9           | ~1.8   | ~1.6        | ~2.3        |
</details>

Source: Bloomberg, NOM

# 30y CGB yield (260002) – Fails to stay below 2.25% despite flush liquidity

In recent weeks, there has been a marked selloff in global yields, owing to rising oil prices and inflation, strong growth data and concerns over central banks' faster/earlier rate hikes or fiscal expansion etc (Figure 5). The selloff in developed markets tends to affect price action in other markets as well. However, China is the only market where we have seen real independence in yield movements. There are some underlying reasons behind this, including: 1) unlike other DMs or Asia central banks, we believe the likelihood of a PBoC rate hike is very small; 2) economic growth headwinds remain, especially from weak domestic demand, which is once again consistent with the broad-based disappointment in today's April activity data. That said, there have been positive developments owing to the warm truce from the Trump-Xi Summit, and property market data, with positive gains in average existing home prices reported across all tier-1 cities in April. Thus, fundamental-related factors supporting lower and higher rates are more balanced at this

stage, in our view.

On positioning, although onshore funds (key drivers of CGB yields) are yet to reduce their 30y CGB holdings in large size, buying flows have slowed over the past two weeks (Figure 6). Insurance firms have started to add back 30y CGBs but only in small amount, while large banks and securities firms remain the main sellers. Looking ahead, we see a risk from the external backdrop, and the 30y CGB may start to have a higher beta to global rates (especially after its outperformance in April). Thus, we remove the long 30y CGB leg from our previous recommendation and now turn to pay Jun-3y NDIRS with a conviction level of 3/5.

Fig. 5: Monthly change in 30y government bond yield   
![](images/a6fcc09df7035c1c64f648a77db2fda579a4c4b733a01ddffb602e8587ec8c71.jpg)

<details>
<summary>bar</summary>

| Region | Mar-26 | Apr-26 | May-26 |
|---|---|---|---|
| US | 30 | 5 | 19 |
| Europe | 14 | 9 | 13 |
| UK | 48 | 17 | 16 |
| Japan | 37 | 3 | 36 |
| Korea | 36 | 2 | 39 |
| China | 6 | -10 | 3 |
</details>

Source: Bloomberg, NOM

Fig. 6: Onshore funds' net weekly buying in CGBs and PFBs   
![](images/1cf3708aa5aaa82c131b425b9694fd89d91f22f0279e04caa8f8d74ff34a47ad.jpg)

<details>
<summary>bar_stacked</summary>

| Date | <=1y (RMB bn) | 1-3y (RMB bn) | 3-5y (RMB bn) | 5-7y (RMB bn) | 7-10y (RMB bn) | >10y (RMB bn) |
|---|---|---|---|---|---|---|
| 7/7/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 7/28/2025 | -5 | -5 | -5 | -5 | -5 | -40 |
| 8/18/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 9/8/2025 | -5 | -5 | -5 | -5 | -5 | -20 |
| 9/29/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 10/20/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 11/10/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 12/11/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 12/22/2025 | -5 | -5 | -5 | -5 | -5 | -10 |
| 1/12/2026 | -5 | -5 | -5 | -5 | -5 | -40 |
| 2/2/2026 | -5 | -5 | -5 | -5 | -5 | -10 |
| 3/2/2026 | -5 | -5 | -5 | -5 | -5 | -10 |
| 3/23/2026 | -5 | -5 | -5 | -5 | -5 | -10 |
| 4/13/2026 | -5 | -5 | -5 | -5 | -5 | 30 |
| 5/4/2026 | -5 | -5 | -5 | -5 | -5 | 10 |
</details>

Source: iData, NOM

Please see Strategy portfolio update (7 May 2026) for our full portfolio.

# Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong.

See Disclaimers for NOM Group entity details.

# Analyst Certification

We, Clair Gao and Albert Leung, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# ADDITIONAL DISCLOSURES REQUIRED IN THE U.S.

Principal Trading: NOM Securities International, Inc and its affiliates will usually trade as principal in the fixed income securities (or in related derivatives) that are the subject of this research report. Analyst Interactions with other NOM Securities International, Inc. Personnel: The fixed income research analysts of NOM Securities International, Inc and its affiliates regularly interact with sales and trading desk personnel in connection with obtaining liquidity and pricing information for their respective coverage universe.

# Valuation methodology - Fixed Income

NOM's Fixed Income Strategists express views on the price of securities and financial markets by providing trade recommendations. These can be relative value recommendations, directional trade recommendations, asset allocation recommendations, or a mixture of all three.

The analysis which is embedded in a trade recommendation would include, but not be limited to:

\- Fundamental analysis regarding whether a security's price deviates from its underlying macro- or micro-economic fundamentals.

• Quantitative analysis of price variations.

\- Technical factors such as regulatory changes, changes to risk appetite in the market, unexpected rating actions, primary market activity and supply/ demand considerations.

The timeframe for a trade recommendation is variable. Tactical ideas have a short timeframe, typically less than three months. Strategic trade ideas have a longer timeframe of typically more than three months.

For the purposes of the EU Market Abuse Regulation, the distribution of ratings published by NOM Global Fixed Income Research is as follows:

52% have been assigned a Buy (or equivalent) rating; 50% of issuers with this rating were supplied material services\* by the NOM Group\*\*.
0% have been assigned a Neutral (or equivalent) rating.

48% have been assigned a Sell (or equivalent) rating; 50% of issuers with this rating were supplied material services by the NOM Group. As at 31 Mar 2026.

\*As defined by the EU Market Abuse Regulation

\*\*The NOM Group as defined in the Disclaimer section at the end of this report

# Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd.

('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other members of the NOM Group; in particular, NOI's interests in PRC securities are not disclosed to, or aggregated with the holdings of, any other NOM Group entities and the interests in PRC securities of other NOM Group entities are not disclosed to, or aggregated with the holdings of, NOI. An individual name printed next to NOI on the front page of a research report indicates that individual is employed by NOI to provide research assistance to NIHK under a research part

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
