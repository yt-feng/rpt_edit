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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`BARC`。标题格式建议：`# BARC：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份BARC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Energy Sigma

# Staying put on \$100/b for 2026 and initiating 2027 Brent at \$88/b

Our 2026 and 2027 price forecasts for Brent at \$100/b and \$88/b, respectively, are \$9/b and \$7/b ahead of the forwards curve at the time of writing.

- We update our baseline balances forecast assuming freedom of navigation through the Strait of Hormuz is restored by the end of this month. We stay put on our \$100/b forecast for Brent in 2026 and initiate 2027 at \$88/b on average.  
- If the timeline of the Strait normalization gets pushed out to the end of July, we would expect Brent to average \$105/b in 2026 and \$95/b in 2027. On the other hand, if it gets pushed out to the end of August, we would expect Brent to average \$110/b in 2026 and \$105/b in 2027.

In late March, we thought that if the Strait remained closed through the end of May, 2026 Brent would reprice to

\$110/b. May is behind us but the forwards-implied 2026

Brent stood at \$91/b at the time of writing. We maintain

our forecast for Brent to average \$100/b in 2026 and expect it to average \$88/b in 2027, assuming the freedom of navigation through the Strait is restored by the end of this month.

The Strait remains largely closed but managed money positioning has retreated back to pre-war levels (Figure 1), and so has implied volatility (Figure 2). We interpret this as fundamentals having grown into the initial hype over time, albeit at a slower pace than we initially expected, and the lack of conviction among market participants about how long the current situation could persist.

## Commodities Research

## Amarpreet Singh

+1 212 526 1672

amarpreet.x.singh@BARC.com

BCI, US

FIGURE 1. Managed money positioning in oil is back to pre-war levels...  
![](images/db7323e4fd5fb2d2257237316e46e3f4708f8947e1c7fc3889cb8e65ed1c8888.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| May-22 | 45    |
| May-23 | 55    |
| May-24 | 70    |
| May-25 | 50    |
| May-26 | 75    |
</details>

Note: Net speculative positioning in Brent and WTI futures and options combined, percentile rank based on data since 2014.
Source: Bloomberg, BARC

FIGURE 2. ...so is excess implied vol in oil markets  
![](images/da2ede8505d7057a07de00d7a088dbffbea5a51fc5eb8fca18b24e3ed7e45258.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jan-21 | -1.5  |
| Jan-22 | 2.5   |
| Jan-23 | 0.5   |
| Jan-24 | 0.0   |
| Jan-25 | -2.0  |
| Jan-26 | 7.0   |
</details>

Note: OVX minus VIX in standard deviation from mean since 2020  
Source: Bloomberg, BARC

We reiterate that this is not a new equilibrium. The Strait cannot remain closed in perpetuity with oil prices at \$100/b. Oil inventories continue to draw down, although the pace has not accelerated to the extent we expected. Our global total oil inventory indicator suggests that adjusted for seasonality, observed inventories have been declining at 4.5 mb/d over the past eight weeks (Figure 3).

FIGURE 3. Observed inventories continue to decline at \~4.5 mb/d...  
![](images/7b09215ef92bd4e57affbdc7139d660962801e1d6501ca97e87555599253d8b8.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jan-21 | 400   |
| Jan-22 | 0     |
| Jan-23 | -100  |
| Jan-24 | -200  |
| Jan-25 | -150  |
| Jan-26 | 200   |
</details>

Note: Our weekly global total oil inventory indicator excluding the Middle East Gulf region minus the pre-pandemic seasonal average (2017-19), mb  
Source: Kpler, BARC

FIGURE 4. ...but the pace has not accelerated because of the pull back in Chinese demand  
![](images/8ee26d46910624ff8e0843a5f218f8fa2cbc9402a89b9ecd6a5de94bb568b0a0.jpg)

<details>
<summary>line chart</summary>

| Date   | Value |
|--------|-------|
| Jan-17 | 13.0  |
| Jan-18 | 13.5  |
| Jan-19 | 14.0  |
| Jan-20 | 15.0  |
| Jan-21 | 18.0  |
| Jan-22 | 16.0  |
| Jan-23 | 17.0  |
| Jan-24 | 18.0  |
| Jan-25 | 19.0  |
</details>

Note: Chinese oil demand and the long-term trend, mb/d  
Source: GACC, NBS, Kpler, BARC

Adjusted for the historical beta between observed inventory draws and estimated imbalance, recent inventory trends imply that the market is currently running a 7 mb/d deficit, which is largely in line with our latest bottom-up supply-demand estimates (see attached). If the timeline for the freedom of navigation through the Strait being restored shifts to July-end, we would expect Brent to average \$105/b and \$95/b in 2026 and 2027, respectively. In a more

extended scenario in which the Strait does not normalize until the end of August, we would expect Brent to average \$110/b and \$105/b in 2026 and 2027, respectively.

The biggest surprise relative to the scenarios we laid out in late-March has been a sharp decline in Chinese oil demand (Figure 4). In April, China's oil demand was down 12% y/y but was still up 2% y/y for the first four months of 2026. Most market participants have interpreted this as the price elasticity of demand in China being much higher than anticipated, but these are extraordinary times and therefore the divergence between steady-state and observed demand elasticity should be studied with caution and in conjunction with the lagged activity indicators.

Visible inventories in China are largely unchanged since the Iran war began (Figure 5), while they have been declining at a rapid pace everywhere else. Could the country be conserving supplies for a scenario in which this impasse continues for much longer than most expect? It is hard to prove but probably easier than attributing the recent weakness in demand to an abrupt increase in energy efficiency given the country's oil demand has been growing at a steady pace over the past several years despite growing electrification of the vehicle fleet.

The obvious question would be why such caution? Oil prices have done nothing for years and there will certainly be a glut after the Strait reopens. Our own balances show a large surplus for 2027 based on the assumption that the freedom of navigation through the Strait is restored by the end of this month.

FIGURE 5. China's crude oil inventories are largely unchanged so far this year  
![](images/24fa67581699fbfc8fcba15a0c06e852317314286cc2fce30c5f66099507e3c7.jpg)

<details>
<summary>line chart</summary>

| Month | 2025  | 2026  | 5-year Avg. |
|-------|-------|-------|-------------|
| Jan   | 1.12  | 1.24  | 1.08        |
| Feb   | 1.08  | 1.25  | 1.07        |
| Mar   | 1.09  | 1.26  | 1.07        |
| Apr   | 1.11  | 1.27  | 1.08        |
| May   | 1.15  | 1.27  | 1.09        |
| Jun   | 1.17  | 1.26  | 1.10        |
| Jul   | 1.18  | 1.25  | 1.10        |
| Aug   | 1.19  | 1.24  | 1.10        |
| Sep   | 1.18  | 1.23  | 1.09        |
| Oct   | 1.17  | 1.22  | 1.08        |
| Nov   | 1.18  | 1.23  | 1.09        |
| Dec   | 1.23  | 1.24  | 1.10        |
</details>

Note: China's crude oil inventories, bb  
Source: Kpler, BARC

FIGURE 6. US commercial crude oil inventories have been tightening under the surface  
![](images/c9e69f4f4eef9b6563651aac4934e52edcf0480555ae438895940fbb34a7fbaa.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| End 2008 | 300 |
| SPR release | 700 |
| Pipeline fills | 750 |
| Organic supply/demand factors | 450 |
| Last week | 450 |
</details>

Note: Change in US commercial crude oil inventories since 2008, mb  
Source: EIA, BARC

The flip side is that in the US, which has driven a large majority of all supply growth for the past several years, commercial crude oil inventories, adjusted for the decline in SPR and the increase in pipeline fills, have declined by 323 mb since 2008. For perspective, commercial crude oil inventories stood at 301 mb at the end of 2008 (Figure 6).

At the recent pace, commercial crude oil inventories in the US in days of refining demand (Figure 7), adjusted for the increase in pipeline fills to accommodate growth in production, would breach the 20-year minimum in eight to ten weeks, and storage capacity utilization at Cushing, OK, the pricing hub for WTI, is within sight of the lowest level since 2010 (Figure 8). Last, even with the UAE fully utilizing its spare capacity, we still see demand growth outpacing non-OPEC supply growth in 2027.

FIGURE 7. US crude oil inventories are tighter than they appear  
![](images/8b8b11489cfaeffe7dc4b83991dc0baa4c8e399dc939610c625865bfa7bee158.jpg)

<details>
<summary>line chart</summary>

| Month | 20-yr. range | 2025 | 2026 | 20-yr. avg. |
|-------|--------------|------|------|-------------|
| Jan   | ~33          | ~25  | ~25  | ~24         |
| Feb   | ~34          | ~28  | ~27  | ~25         |
| Mar   | ~35          | ~29  | ~28  | ~26         |
| Apr   | ~36          | ~29  | ~29  | ~27         |
| May   | ~37          | ~28  | ~28  | ~27         |
| Jun   | ~36          | ~25  | ~26  | ~26         |
| Jul   | ~35          | ~25  | ~25  | ~25         |
| Aug   | ~34          | ~25  | ~25  | ~24         |
| Sep   | ~33          | ~25  | ~25  | ~24         |
| Oct   | ~34          | ~26  | ~26  | ~25         |
| Nov   | ~35          | ~27  | ~27  | ~26         |
| Dec   | ~34          | ~25  | ~25  | ~24         |
</details>

NOte: US commercial crude oil inventories in days of refining demand  
Source: EIA, BARC

FIGURE 8. Cushing storage utilization has been declining fast  
![](images/b6e1e211dbc6925cbc3c88b36dc73050e87cfa2bb01ef0ef333356f96649f045.jpg)

<details>
<summary>line chart</summary>

| Date   | Cushing available tank capacity utilization |
|--------|---------------------------------------------|
| Jan-11 | 85%                                         |
| Jul-13 | 75%                                         |
| Jan-16 | 90%                                         |
| Jul-18 | 60%                                         |
| Jan-21 | 80%                                         |
| Jul-23 | 50%                                         |
| Jan-26 | 35%                                         |
</details>

Source: EIA, BARC

FIGURE 9. Our \$100/b forecast for Brent this year is significantly ahead of the forward curve

<table><tr><td>BARC oil price forecast ($/b)</td><td>2025</td><td>2026 Q1</td><td>2026 Q2</td><td>2026 Q3</td><td>2026 Q4</td><td>2026</td><td>2027 Q1</td><td>2027 Q2</td><td>2027 Q3</td><td>2027 Q4</td><td>2027</td></tr><tr><td>Brent</td><td>68</td><td>79</td><td>115</td><td>105</td><td>100</td><td>100</td><td>95</td><td>90</td><td>85</td><td>80</td><td>88</td></tr><tr><td>WTI</td><td>65</td><td>73</td><td>102</td><td>98</td><td>95</td><td>92</td><td>92</td><td>87</td><td>83</td><td>77</td><td>85</td></tr><tr><td>WTI-Brent (S:ENCO 1-1)</td><td>-3.4</td><td>-6.1</td><td>-13.0</td><td>-7.0</td><td>-5.0</td><td>-7.8</td><td>-3.0</td><td>-3.0</td><td>-2.0</td><td>-3.0</td><td>-2.8</td></tr><tr><td>Brent (vs curve)</td><td></td><td></td><td>15</td><td>15</td><td>14</td><td>8</td><td></td><td>9</td><td>5</td><td>1</td><td>7</td></tr><tr><td>Brent (vs consensus)</td><td></td><td></td><td>15</td><td>14</td><td>15</td><td>14</td><td></td><td>n/a</td><td>n/a</td><td>n/a</td><td>13</td></tr><tr><td>WTI (vs curve)</td><td></td><td></td><td>5</td><td>12</td><td>14</td><td>6</td><td></td><td>11</td><td>8</td><td>3</td><td>9</td></tr><tr><td>WTI (vs consensus)</td><td></td><td></td><td>7</td><td>17</td><td>17</td><td>11</td><td></td><td>n/a</td><td>n/a</td><td>n/a</td><td>13</td></tr></table>

Note: Curve and consensus estimates as of 9 June 2026.
Source: Bloomberg, BARC

## Analyst(s) Certification(s):

I, Amarpreet Singh, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may have either a long and / or short position in such securities, other financial instruments and / or derivatives, which may pose a conflict with the interests of investing customers. Where permitted and subject to appropriate information barrier restrictions, BARC fixed income research analysts regularly interact with its trading desk personnel regarding current market conditions and prices. BARC fixed income research analysts receive compensation based on various factors including, but not limited to, the quality of their work, the overall performance of the firm (including the profitability of the Investment Banking Department), the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst. To the extent that any historical pricing information was obtained from BARC trading desks, the firm makes no representation that it is accurate or complete. All levels, prices and spreads are historical and do not necessarily represent current market levels, prices or spreads, some or all of which may have changed since the publication of this document. BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations and trade ideas contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Disclosure(s) regarding Information Sources

Bloomberg® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

All pricing information is indicative only. Unless otherwise indicated, prices are sourced from LSEG Data & Analytics and reflect the closing price in the relevant trading market, which may not be the last available price at the time of publication.

## Types of investment recommendations produced by BARC FICC Research:

In addition to any ratings assigned under BARC' formal rating systems, this publication may contain investment recommendations in the form of trade ideas, thematic screens, scorecards or portfolio recommendations that have been produced by analysts in FICC Research. Any such investment recommendations produced by non-Credit Research teams shall remain open until they are subsequently amended, rebalanced or closed in a future research report. Any such investment recommendations produced by the Credit Research teams are valid at current market conditions and may not be otherwise relied upon.

## Disclosure of other investment recommendations produced by BARC FICC Research:

BARC FICC Research may have published other investment recommendations in respect of the same securities/instruments recommended in this research report during the preceding 12 months. To view all investment recommendations published by BARC FICC Research in the preceding 12 months please refer to https://live.barcap.com/go/research/Recommendations.

BARC does not assign ratings to asset backed securities. BARC Capital Inc. and/or one of its affiliates may have acted as an underwriter for public offerings of any asset backed securities that are otherwise recommended in trade ideas contained within its securitised research reports.

## Legal entities involved in producing BARC:

BARC Bank PLC (BARC, UK)

BARC Capital Inc. (BCI, US)

BARC Bank Ireland PLC, Frankfurt Branch (BBI, Frankfurt)

BARC Bank Ireland PLC, Paris Branch (BBI, Paris)

BARC Bank Ireland PLC, Milan Branch (BBI, Milan)

BARC Securities Japan Limited (BSJL, Japan)

BARC Bank PLC, Hong Kong Branch (BARC Bank, Hong Kong)

BARC Bank Mexico, S.A. (BBMX, Mexico)

BARC Capital Casa de Bolsa, S.A. de C.V. (BCCB, Mexico)

BARC Securities (India) Private Limited (BSIPL, India)

BARC Bank PLC, Singapore Branch (BARC Bank, Singapore)

BARC Bank PLC, DIFC Branch (BARC Bank, DIFC)

## Disclaimer:

This publication has been produced by BARC Department in the Investment Bank of BARC Bank PLC and/or one or more of its affiliates (collectively and each individually, "BARC").

It has been prepared for institutional investors and not for retail investors. It has been distributed by one or more BARC affiliated legal entities listed below or by an independent and non-affiliated third-party entity (as may be 

[中间内容因长度限制已省略]

 scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
