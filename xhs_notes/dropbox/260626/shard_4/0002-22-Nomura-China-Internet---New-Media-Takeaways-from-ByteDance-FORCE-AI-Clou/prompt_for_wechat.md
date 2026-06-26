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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`NOM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

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
