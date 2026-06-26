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
# China Internet & New Media

EQUITY: INTERNET & NEW MEDIA

# Takeaways from ByteDance FORCE AI Cloud Conference

Video generation and coding emerging as key competitive arenas

Key takeaways

ByteDance's (unlisted) cloud business segment, Volcano Engine (VE), held a two-day conference for its industry partners on June 23 and June 24 to showcase its latest AI products. Among the offerings, the upcoming early-July release of Seedance 2.5, its video-generating tool, attracted the most attention. Meanwhile, the newly released foundation model series, Doubao Seed 2.1, represents ByteDance's solution for agentic tasks. VE management indicated that the Doubao Seed 2.1 series should provide ByteDance with an entry ticket into the AI coding arena.

Recent industry events hosted by major AI platforms including ByteDance and Alibaba (BABA US, Buy) highlight a strategic pivot toward AI coding and video generation. These two areas appear closer to scalable commercialization, whereas most other segments in the broader large language model (LLM) space still require continued incubation.

In the video-generation segment, ByteDance has maintained a strong position since the release of Seedance 2.0 earlier this year, according to ByteDance, adding that the upcoming launch of Seedance 2.5 would further solidify ByteDance's standing in this important vertical. According to VE management, Seedance 2.5 addresses key pain points in this field, such as extending the video output length from the existing 15 seconds per take to 30 seconds and upgrading the video quality to 4K resolution (Fig.1). With these significant advancements, Seedance 2.5 not only raises the bar for peers but also has the potential to reshape operational models for businesses in short dramas, advertising, and short-video ecommerce, according to VE management.

Comparatively, ByteDance's other business-oriented AI products have faced a more challenging adoption curve. In the AI coding field, while the latest Doubao Seed 2.1 Pro demonstrates stronger agentic abilities than its previous versions, our industry contacts suggest that ByteDance currently trails the tier-1 camp, which consists of GLM-5.2, Deepseek (unlisted), and Alibaba. However, our contacts also noted that an established leader has yet to emerge in the coding market, making it too early to declare a definitive winner. It is widely expected in the market that competition in the AI coding field will intensify significantly, potentially compressing the product upgrade cycle to 1-2 months from the previous 5-6 months.

Bytedance management cited a significant market share of nearly 50% in China's public cloud Model-as-a-Service (MaaS) market. According to our industry contacts, over half of this MaaS revenue is likely driven by its video-generating tool Seedance 2.0, while the remainder of the MaaS portfolio—particularly the foundation model, Doubao Seed—has thus far struggled to gain strong traction with business users, likely due to softer model performance. We will monitor whether the latest Doubao Seed 2.1 series can help the company gain ground.

Overall, we continue to view Alibaba as a more comprehensive AI cloud player, possessing a solid footing across all critical fields of the AI value chain. This encompasses AI chips (T-Head), robust CPU/GPU cloud infrastructure, the Bailian LLM marketplace, and the Qwen LLM, which remains one of the state-of-the-art models in China's LLM market.

We believe Alibaba's year-to-date weakness, currently trading at 13x CY27F PE (i.e., also FY28F), offers an attractive entry point for long-term investors, although we caution that the June quarter e-commerce Customer Management Revenue (CMR) may surprise on the downside (please see our preview report).

## Research Analysts

China Internet & New Media

Jialong Shi - NIHK
Jialong.shi@NOM.com
+852 2252 1409

Rachel Guo - NIHK

rachel.guo@NOM.com

+852 2252 1400

Finally, we believe the industry-wide shift toward business-oriented solutions (video generation and coding) may lead to a temporary easing of competition in consumer-facing AI chatbots. Ongoing chip supply constraints may force AI platforms to concentrate their resources on a single battlefront at a time. This context helps explain ByteDance's decision to launch the subscription-based Doubao AI chatbot, arriving at a time when its free version has already garnered over 150mn daily active users (DAUs), according to QuestMobile.

## Seedance 2.5: A leap forward in performance

Seedance 2.5 represents the most distinct commercial product highlight from the conference. Management positioned Seedance 2.0 as the first ByteDance video model to cross the “production threshold,” marking a shift in AI video from 5 to 10 seconds experimental user-generated content (UGC) to longer, more realistic, and more controllable commercial videos. Seedance 2.5 is designed to push these capabilities further into enterprise-grade video production.

The first major upgrade is video duration. According to management at the conference, comparable video models in the market generally support up to 15 – 20 seconds of direct output, while Seedance 2.5 supports up to 30 seconds of native single-video generation.

The second upgrade is multi-reference capability. Seedance 2.5 can utilize up to 50 multimodal reference assets in a single generation workflow. This is critical for professional users, as commercial content production typically requires consistency across characters, products, scenes, and style. Enhanced reference control makes the model significantly more practical for real-world production, reducing the likelihood of generating visually impressive but inconsistent clips.

The third upgrade is controllable editing. Seedance 2.5 allows creators to modify specific parts of a video while keeping the broader scene stable. Examples include changing the background, replacing the displayed merchandise, adjusting the model, or localizing the creative for different markets. This functionality is particularly relevant for advertising and e-commerce, where the same base creative often requires multiple iterations based on product, price point, country, language, user segment, or campaign theme.

Potential business use cases are broad, spanning advertising, movies, short dramas, and e-commerce. In our view, Seedance 2.5 may serve as a particularly useful tool for TikTok Shop merchants selling merchandise to various international markets. The model can create product showcase videos in multiple languages and localized styles more efficiently. This could improve the content supply for cross-border merchants, lower creative production costs, and potentially lift conversion rates. For TikTok Shop, we believe the strategic value lies not only in improved AI video technology but also in establishing a more scalable content production engine for global merchants.

Fig. 1: Seedance 2.5 vs its previous version

<table><tr><td>Feature / Dimension</td><td>Seedance 2.0</td><td>Seedance 2.5(Latest Breakthroughs)</td></tr><tr><td>Max Duration per Generation</td><td>15 seconds</td><td>30 seconds (Doubled)</td></tr><tr><td>Max Reference Inputs</td><td>Up to 12 reference materials per prompt</td><td>Up to 50 reference materials per prompt (images, video, audio)</td></tr><tr><td>Resolution &amp; Quality</td><td>720p / 1080p HD output</td><td>Upgraded quality, expected to support up to 4K resolution</td></tr><tr><td>Consistency &amp; Control</td><td>Director-level control, multi-shot character consistency, native audio sync</td><td>Significantly enhanced creative control, accurately parsing intent from massive reference data</td></tr></table>

Source: Company website, NOM

## Appendix A-1

This report has been produced by NOM International (Hong Kong) Ltd. (NIHK), Hong Kong. See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Rachel Guo and Jialong Shi, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Issuer Specific Regulatory Disclosures

The terms "NOM" and "NOM Group" used herein refer to NOM Holdings, Inc. and its affiliates and subsidiaries, including NOM Securities International, Inc. ('NSI') and Instinet, LLC ('ILLC'), U. S. registered broker dealers and members of SIPC.

## Materially mentioned issuers

<table><tr><td>Issuer</td><td>Ticker</td><td>Price</td><td>Price date</td><td>Stock rating</td><td>Sector rating</td><td>Disclosures</td></tr><tr><td>Alibaba Group Holding</td><td>BABA US</td><td>USD 99.80</td><td>24-Jun-2026</td><td>Buy</td><td>N/A</td><td>A10</td></tr></table>

A10 The NOM Group is a registered market maker in the securities / related derivatives of the issuer.

![](images/c52090e30c73767af0fe2308cf47a4c410f9ae2c47bd5889c7d6b43251c10f2a.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Target price</td><td>Closing price</td></tr><tr><td>24-Jun-26</td><td></td><td>178.00</td><td>99.80</td></tr><tr><td>14-May-26</td><td></td><td>207.00</td><td>141.12</td></tr><tr><td>20-Mar-26</td><td></td><td>200.00</td><td>122.41</td></tr><tr><td>23-Jan-26</td><td></td><td>237.00</td><td>173.23</td></tr><tr><td>09-Jan-26</td><td></td><td>193.00</td><td>150.96</td></tr><tr><td>08-Oct-25</td><td></td><td>215.00</td><td>181.12</td></tr><tr><td>01-Sep-25</td><td></td><td>170.00</td><td>135.00</td></tr><tr><td>09-Jul-25</td><td></td><td>152.00</td><td>103.83</td></tr><tr><td>21-Feb-25</td><td></td><td>172.00</td><td>142.62</td></tr><tr><td>18-Nov-24</td><td></td><td>130.00</td><td>88.65</td></tr><tr><td>10-Oct-24</td><td></td><td>135.00</td><td>108.42</td></tr><tr><td>16-Aug-24</td><td></td><td>106.00</td><td>82.52</td></tr><tr><td>09-Apr-24</td><td></td><td>101.00</td><td>71.80</td></tr><tr><td>08-Feb-24</td><td></td><td>103.00</td><td>69.63</td></tr><tr><td>10-Jan-24</td><td></td><td>117.00</td><td>70.25</td></tr><tr><td>17-Nov-23</td><td></td><td>134.00</td><td>76.34</td></tr><tr><td>11-Aug-23</td><td></td><td>142.00</td><td>94.16</td></tr></table>

For explanation of ratings refer to the stock rating keys located after chart(s)

Valuation Methodology We value Alibaba's China Ecommerce Group at USD89bn, based on 5x FY27F P/E; its AliCloud business at USD270bn, based on 7x FY28F P/S; and its net valuation of non-core assets (including international ecommerce business) at USD40bn. The resulting TP is USD178. The benchmark index for this stock is Nasdaq Composite. Risks that may impede the achievement of the target price Downside risks include: margin downside due to ramp-up in investments; regulatory risks related to the payment and internet finance industry, which could hurt Alibaba's main business and its value in Ant Group.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

57% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 34% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

41% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

2% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 0% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 31 March 2026.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

## Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the

Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ00025563

[中间内容因长度限制已省略]

M AN INDEPENDENT FINANCIAL ADVISER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
