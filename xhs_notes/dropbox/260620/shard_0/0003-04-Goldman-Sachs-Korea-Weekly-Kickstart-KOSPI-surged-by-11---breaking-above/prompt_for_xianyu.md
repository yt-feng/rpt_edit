你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
## KOREA WEEKLY KICKSTART

# KOSPI surged by 11%, breaking above the KOSPI 9,000 as tech continues to lead the rally amid US-Iran deal and hawkish FOMC

KOSPI surged by 11%, breaking above the KOSPI 9,000 as tech continues to lead the rally amid US-Iran deal and hawkish June FOMC. The Insurance, Tech and Retail sectors outperformed this week, while Construction, Telecom and Leisure sectors underperformed the most (Exhibit 6).  
■ Foreign investors turned to buy the KOSPI market, driven by inflows for KOSPI Tech and Auto (Exhibit 33).  
KOSPI 12m-forward EPS was revised up by +1.5%. The Tech sector saw the strongest upward earnings revisions, while the Chemicals sector was revised down the most this week (Exhibit 20).  
The KRW weakened 0.8% vs. USD this week. It also weakened by 0.1% vs. JPY but strengthened 0.2% vs. EUR.  
The latest Korea Equity Risk Barometer (GSSRKERB Index) is at 0.2, rebounding back into a risk-neutral territory.

Charts of the Week: Preliminary Mutual Fund Positioning (May 2026), MSCI Market Accessibility Review

■ Preliminary Mutual Fund Positioning (May 2026) :

Based on preliminary EPFR data (\~46% of total AUM reported), Asian and EM funds have trimmed exposure in Korea (vs. benchmark) as they are UW with the market. By sector, among EM & Asian focused funds, Insurance and Tech H/W are the most OW while Internet and Health Care are the most UW for Korea. Over the past 3 months, EM & Asian funds have raised their exposure to Industrials the most while trimmed down Tech H/W exposure by sector.

MSCI Market Accessibility Review : MSCI upgraded Availability of Investment Instruments from “−” to “+”, reflecting Korean index derivatives listed on international exchanges. Five “−” criteria remain: FX Liberalization (no fully deliverable offshore KRW), Investor Registration (IRC/LEI coexistence constraining omnibus adoption), Information Flow (English disclosure effectiveness still pending full 2027 rollout), Clearing & Settlement (settlement remains per investor ID; funding amount calculation remains unclear), and Transferability. MSCI acknowledged ongoing reform progress, including Phase 2 English disclosure, the planned 24-hour FX market (July 2026), and the offshore KRW pilot (2H26), but noted these have yet to deliver a “meaningful improvement in the experience of

## Timothy Moe, CFA

+65-6889-1199 | timothy.moe@gs.com

GS (Singapore) Pte

## John Kwon

+65-6654-6337

jongmin.kwon@gs.com

GS (Singapore) Pte

## Table of Contents

Charts of the week: Preliminary Mutual Fund Positioning (May 2026) 4  
Charts of the week: MSCI Market Accessibility Review 5  
Summary 6  
Investment flows 7  
Macro Indicators 8  
Performance 9  
Valuations 11  
Valuation discount relative to Global and Asia regional peers 13  
Flows 14  
Currency, rates and commodities 16  
Korea ERB, Credit and Market Technicals 17  
Disclosure Appendix 18

international institutional investors". Post-ban short-selling frictions were also flagged. MSCI continues to focus on realized improvements in investor experience rather than announced reforms. Our base case remains no DM watchlist inclusion at the Annual Market Classification Review on June 23 (after US market close)

## Charts of the week: Preliminary Mutual Fund Positioning (May 2026)

Exhibit 1: Based on preliminary EPFR data (\~46% of total AUM reported), Asian funds are most OW China, Hong Kong, Singapore, and most UW Taiwan and India. In May, Asian funds raised exposure in China and Taiwan, while trimmed exposure in Korea (vs. benchmark)

AEJ funds (US\$100 bn - Active Fund Only)

<table><tr><td>Market</td><td>OW/UW allocation (in bp)</td><td>Market</td><td>1-mth chg</td><td>3-mth chg</td></tr><tr><td>China</td><td>290</td><td>China</td><td>100</td><td>185</td></tr><tr><td>Hong Kong</td><td>185</td><td>Taiwan</td><td>70</td><td>115</td></tr><tr><td>Singapore</td><td>170</td><td>India</td><td>45</td><td>20</td></tr><tr><td>Indonesia</td><td>80</td><td>Malaysia</td><td>10</td><td>15</td></tr><tr><td>Thailand</td><td>55</td><td>Philippines</td><td>(2)</td><td>(25)</td></tr><tr><td>Philippines</td><td>5</td><td>Indonesia</td><td>(10)</td><td>(35)</td></tr><tr><td>Malaysia</td><td>-55</td><td>Thailand</td><td>(15)</td><td>(25)</td></tr><tr><td>Korea</td><td>-195</td><td>Hong Kong</td><td>(15)</td><td>(45)</td></tr><tr><td>India</td><td>-310</td><td>Singapore</td><td>(30)</td><td>(55)</td></tr><tr><td>Taiwan</td><td>-360</td><td>Korea</td><td>(105)</td><td>(140)</td></tr></table>

Note: The allocation of AEJ mandate only includes active funds, as of May '26  
Source: EPFR, GS Global Investment Research

Exhibit 3: Among EM & Asian focused funds, Insurance and Tech H/W are the most OW while Internet and Health Care are the most UW  
![](images/5762488b4b050d33dfc57ba1068c11fd7db6216080dedd717cb2aa9c792d4cc5.jpg)

<details>
<summary>bar chart</summary>

Korea allocation in EM & Asian focused funds (OW/UW vs. benchmark, bp)
| Sector | Allocation (bp) |
|---|---|
| Insur./Other Fins | 30 |
| Tech H/w & Semis | 15 |
| Banks | 7 |
| Telcos | 6 |
| Consumer Staples | 5 |
| Consumer Retail | 4 |
| Chem. & Other Mat. | 2 |
| Autos | -1 |
| Industrial | -1 |
| Real Estate | -1 |
| Transportation | -3 |
| Software & Services | -2 |
| Utilities | -3 |
| Energy | -8 |
| Metals & Mining | -12 |
| Internet/Media/Ent. | -14 |
| Health Care | -22 |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 2: EM funds are most OW Brazil/Mexico, and most UW Taiwan. Over the past month, EM funds have raised exposure the most in China, and trimmed exposure in Korea

EM funds (US\$210 bn - Active Fund Only)

<table><tr><td>Market</td><td>OW/UW allocation (in bp)</td><td>Market</td><td>1-mth chg</td><td>3-mth chg</td></tr><tr><td>Brazil</td><td>300</td><td>China</td><td>100</td><td>165</td></tr><tr><td>Mexico</td><td>70</td><td>India</td><td>45</td><td>40</td></tr><tr><td>Hungary</td><td>35</td><td>Saudi Arabia</td><td>10</td><td>20</td></tr><tr><td>Turkey</td><td>30</td><td>Malaysia</td><td>10</td><td>5</td></tr><tr><td>Indonesia</td><td>25</td><td>South Africa</td><td>5</td><td>20</td></tr><tr><td>Malaysia</td><td>-55</td><td>Hungary</td><td>(1)</td><td>1</td></tr><tr><td>Saudi Arabia</td><td>-120</td><td>Taiwan</td><td>(2)</td><td>(5)</td></tr><tr><td>India</td><td>-190</td><td>Turkey</td><td>(5)</td><td>(2)</td></tr><tr><td>Korea</td><td>-285</td><td>Brazil</td><td>(5)</td><td>10</td></tr><tr><td>Taiwan</td><td>-345</td><td>Korea</td><td>(165)</td><td>(195)</td></tr></table>

Note: The allocation of GEM mandates only include active funds, as of May '26  
Source: EPFR, GS Global Investment Research

Exhibit 4: Over the past 3 months, EM & Asian funds have raised their exposure to Industrials the most while trimmed down Tech H/W exposure by sector  
![](images/1b7a4551877fea10ff629c6d4e128fd1b33f077d09e84d5bc7ef2ecaa472b74c.jpg)

<details>
<summary>bar chart</summary>

Change in Korea allocation in EM & Asian focused funds (past 3M, bp)
| Sector | Change (bp) |
|---|---|
| Industrial | 40 |
| Health Care | 5 |
| Banks | 3 |
| Insur./Other Fins | 2 |
| Consumer Staples | 1 |
| Internet/Media/Ent. | 1 |
| Energy | -1 |
| Metals & Mining | -1 |
| Consumer Retail | -1 |
| Utilities | -1 |
| Transportation | -1 |
| Real Estate | -1 |
| Chem. & Other Mat. | -1 |
| Software & Services | -1 |
| Telcos | -1 |
| Autos | -5 |
| Tech H/w & Semis | -60 |
Note: Latest data as of May '26
</details>

Source: FactSet, GS Global Investment Research

## Charts of the week: MSCI Market Accessibility Review

Exhibit 5: While MSCI acknowledged the implemented regulatory frameworks, their comments remained conservative to continue monitoring

<table><tr><td>MSCI Assessments</td><td>2026 Result</td><td>MSCI Comments</td></tr><tr><td colspan="2">Openness to foreign ownership</td><td></td></tr><tr><td>Investor qualification requirement</td><td>++</td><td>++</td></tr><tr><td>Foreign ownership limit (FOL) level</td><td>++</td><td>++</td></tr><tr><td>Foreign room level</td><td>+</td><td>+</td></tr><tr><td>Equal rights to foreign investors</td><td>+</td><td>+</td></tr><tr><td colspan="2">Ease of capital inflows/outflows</td><td></td></tr><tr><td>Capital flows restriction level</td><td>++</td><td>++</td></tr><tr><td>Foreign exchange market liberalization level</td><td>-</td><td>-A fully deliverable offshore currency market is still not available, and constraints persist on the onshore FX market. Building on the MOEF&#x27;s FX reform announced in 2023 and subsequent measures implemented through 2024–2025, the authorities have outlined further initiatives to align the FX framework with global practices, including plans for 24-hour onshore trading in July 2026 and offshore KRW settlement targeted for 2027.</td></tr><tr><td colspan="2">Efficiency of the operational framework</td><td></td></tr><tr><td colspan="2">Market entry</td><td></td></tr><tr><td>Investor registration &amp; account set up</td><td>-</td><td>- Registration is mandatory. Since December 2023, foreign investors must obtain a Legal Entity Identifier (LEI), which superseded the previous Investor Registration Certificate (IRC) system. The transition between both frameworks remains ongoing, and their coexistence continues to create operational friction, with implications for the use of omnibus account structures.</td></tr><tr><td colspan="2">Market organization</td><td></td></tr><tr><td>Market regulations</td><td>++</td><td>++</td></tr><tr><td>Information flow</td><td>-</td><td>-Detailed stock market information is not always disclosed in English. A phased mandatory English disclosure framework introduced in 2023 has progressively improved disclosure practices. The first phase has concluded. The second phase expands coverage in 2026, with a further phase expected in 2027. Additionally, adoption of the revised dividend distribution procedure remains partial but is progressing.</td></tr><tr><td colspan="2">Market Infrastructure</td><td></td></tr><tr><td>Clearing and Settlement</td><td>-</td><td>- Despite recent regulatory measures, settlement is still predominantly conducted on a per-investor-ID basis. Overdraft and omnibus mechanisms are permitted but practical adoption remains limited. The Korea Securities Depository (KSD) recently advanced its settlement start time and reduced the settlement progress payment amounts, partially easing broker pre-settlement funding requirements. However, there is a lack of clarity around the calculation of funding amounts, creating inefficiency in the settlement process.</td></tr><tr><td>Custody</td><td>++</td><td>++</td></tr><tr><td>Registry/Depository</td><td>++</td><td>++</td></tr><tr><td>Trading</td><td>++</td><td>++</td></tr><tr><td>Transferability</td><td>-</td><td>- Following regulatory reforms of 2023, in-kind transfers and off-exchange transactions are allowed with restrictions. However, they are not yet common practice.</td></tr><tr><td>Stock lending</td><td>++</td><td>++</td></tr><tr><td>Short selling</td><td>+</td><td>+</td></tr><tr><td>Availability of Investment instrument</td><td>+</td><td>+</td></tr><tr><td>Stability of institutional framework</td><td>+</td><td>+</td></tr></table>

++: no issues; +: no major issues, improvements possible; -: improvements needed / extent to be assessed

## Summary

Exhibit 6: Summary of the past week's performance

<table><tr><td colspan="5">Equity Market Performance</td></tr><tr><td></td><td>P/E 2026E</td><td></td><td></td><td>1-wk chg</td></tr><tr><td>KOSPI</td><td>8.0</td><td>9,052.42</td><td>↑</td><td>11.4</td></tr><tr><td>KOSDAQ</td><td>29.1</td><td>966.59</td><td>↓</td><td>(6.1)</td></tr><tr><td>MSCI Korea</td><td>7.1</td><td>3,431.52</td><td>↑</td><td>13.7</td></tr><tr><td colspan="5">KOSPI Performance by sector</td></tr><tr><td>Top 3</td><td>wk chg (%)</td><td>Bottom 3</td><td></td><td>1wk chg (%)</td></tr><tr><td>Insurance</td><td>18.4</td><td>Construction</td><td></td><td>(9.9)</td></tr><tr><td>Tech</td><td>16.6</td><td>Telecom</td><td></td><td>(6.2)</td></tr><tr><td>Retail</td><td>5.4</td><td>Leisure</td><td></td><td>(5.1)</td></tr><tr><td colspan="5">Market Flows</td></tr><tr><td colspan="2">Equities (KRW bn)</td><td>1-wk flow</td><td></td><td>in std dev*</td></tr><tr><td colspan="2">KOSPI Flows: Foreigners</td><td>2,539</td><td>↑</td><td>0.5</td></tr><tr><td></td><td>Institutions</td><td>(246)</td><td>↓</td><td>-0.1</td></tr><tr><td></td><td>Individuals</td><td>(1,917)</td><td>↓</td><td>-0.3</td></tr><tr><td></td><td>Pensions</td><td>(1,095)</td><td>↓</td><td>-3.7</td></tr><tr><td colspan="2">KOSDAQ Flows: Foreigners</td><td>(717)</td><td>↓</td><td>-1.2</td></tr><tr><td></td><td>Institutions</td><td>(1,106)</td><td>↓</td><td>-0.7</td></tr><tr><td></td><td>Individuals</td><td>1,834</td><td>↑</td><td>1.1</td></tr><tr><td></td><td>Pensions</td><td>(20)</td><td>↓</td><td>-0.2</td></tr><tr><td colspan="5">FX/Interest Rate</td></tr><tr><td></td><td></td><td>Current</td><td></td><td>1-wk chg</td></tr><tr><td colspan="2">USDKRW</td><td>1,530</td><td>↑</td><td>0.8</td></tr><tr><td colspan="2">JPYKRW</td><td>9.48</td><td>↑</td><td>0.1</td></tr><tr><td colspan="2">USDKRW 1M Risk Reversal/ATM vc</td><td>0.08</td><td>-</td><td>0bp</td></tr><tr><td colspan="2">USDKRW 1yr swap basis</td><td>(85)</td><td>↑</td><td>4bp</td></tr><tr><td colspan="2">3-year KTB</td><td>3.78</td><td>↓</td><td>-2bp</td></tr><tr><td colspan="2">10-year KTB</td><td>4.17</td><td>↓</td><td>-2bp</td></tr></table>

Up (↑) = Up wow vs. the previous week  
Asterisk (\*) = Expressed in standard deviation of 1-wk change in 1-year  
Source: Bloomberg

Exhibit 7: Summary of year-to-date flows  
Year-to-date Foreign Inflows to Korea  
![](images/f3a7f1430bd35f74e86dd926ef6a89b4496b5d6ba8fb83a6e831366fa2f1c37a.jpg)

<details>
<summary>line chart</summary>

| Year | Korea Equities (LHS) | Korea Bonds |
|------|----------------------|-------------|
| 17   | -5                   | 5           |
| 18   | -5                   | 30          |
| 19   | -5                   | 45          |
| 20   | -5                   | 40          |
| 21   | -25                  | 60          |
| 22   | -30                  | 90          |
| 23   | -10                  | 50          |
| 24   | 10                   | 60          |
| 25   | -10                  | 40          |
| 26   | -30                  | 90          |
</details>

![](images/f804abe081cf4f69803c21ca1cde238fae1c9bf62f1df396f04f4039b22c192b.jpg)

<details>
<summary>line chart</summary>

| Year | *AEJ Equities (LHS) | **AEJ Bonds |
|------|---------------------|-------------|
| 17   | ~0                  | ~0          |
| 18   | ~-40                | ~80         |
| 19   | ~-60                | ~40         |
| 20   | ~-40                | ~60         |
| 21   | ~-60                | ~40         |
| 22   | ~-60                | ~100        |
| 23   | ~-60                | ~50         |
| 24   | ~-40                | ~70         |
| 25   | ~-60                | ~60         |
| 26   | ~-60                | ~100        |
</details>

Source: Bloomberg

## Investment flows

Exhibit 8: Equity inflows to 5 AEJ markets  
4-week rolling sum  
![](images/50454409c8f1f2b481f34c812a0970de1f84320731d935ea008330ad515c0f3b.jpg)

<details>
<summary>line chart</summary>

| Date    | Korea | Indonesia | India | Taiwan | Thailand |
|---------|-------|-----------|-------|--------|----------|
| Jan-18  | -2.0  | -1.5      | -1.0  | -3.0   | -2.5     |
| Jul-18  | -1.5  | -1.0      | -0.5  | -2.5   | -2.0     |
| Jan-19  | -1.0  | -0.5      | 0.0   | -2.0   | -1.5     |
| Jul-19  | -0.5  | 0.0       | 0.5   | -1.5   | -1.0     |
| Jan-20  | 0.0   | 0.5       | 1.0   | -1.0   | -0.5     |
| Jul-20  | 0.5   | 1.0       | 1.5   | -0.5   | 0.0      |
| Jan-21  | 1.0   | 1.5       | 2.0   | 0.0    | 0.5      |
| Jul-21 

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
