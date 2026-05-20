你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Global Equity Volatility Insights

# Underestimate FOMO at your own risk

# In bubble-builds, FOMO can trump macro

Renewed inflation concerns and rising long-end yields have slowed the breakneck US equity rally, but numerous signs point to equity resilience and concerns over further upside. As one example, a striking disconnect has emerged between steep put skew in rates vol and historically flat call skew across equity indices & sectors. We note that in bubble-like markets, FOMO can overwhelm rising yields & macro headwinds, as seen in the Dotcom bubble when Nasdaq surged with 30y yields. Near term, the clash between macro risks and a bubble-prone market is pushing risk into both tails, making options' asymmetry valuable. TLT put spreads offer historic \~8x max payouts to hedge a further yield rise, while QQQ call spreads and NDX-USDGBP hybrids offer cheap, limited-risk upside participation. Upcoming mega-cap tech IPOs will likely be another driver of tech enthusiasm, and we reiterate NDX over SPX in delta and vol to hedge growing concentration risk and rising bubble-era boom/bust dynamics (see 6-May-26 GEVI for more details).

# UK-specific risk creates opportunities in banks & hybrids

UK political risk is reasserting itself as a meaningful macro driver, with Labour leadership uncertainty and associated fiscal divergence feeding into Gilt yields, macro volatility and renewed Sterling weakness. This uncertainty creates attractive trading opportunities for UK vs other regional assets. For instance, as UK banks remain sensitive to domestic political and fiscal risk, a historically low SX7E/SX7P vol ratio combined with persistently high correlation cheapens SX7E calls contingent on limited SX7P upside. More broadly, Sterling-equity correlations are counter to scenarios in which equities continue to rally even as idiosyncratic UK risk weighs on GBP. Specifically, we like SX5E up, EURGBP up dual-digitals offering 13:1 max payouts and Al-upside geared NDX calls contingent on weaker GBPUSD at a 60% discount vs vanilla.

# China AI hardware: 7.1x payout call spreads on FTSE A50

AI hardware is starting to dominate the FTSE China A50 index (XIN9I) and the index doesn't include Hong Kong-listed "AI software" (e.g. Tencent and Alibaba). At 25%, IT is on track to overtake Financials as the largest sector in the A50 index, more than tripling its weight from a year ago. Indeed, recent performance is more in line with semiconductor stocks in the US than with common China Tech instruments such as the KWEB ETF and the Hang Seng Tech index. We like XIN9I 3m call spreads for a 7.1x max payout ratio as they leverage the most inverted call skew globally and offer good upside participation while limiting losses at 1.4%. With most AI-linked assets in Asia trading well above 50% vol, A50 vols remain in the low 20s.

# Also in the GEVI

Global cross-asset stress finished higher after Friday's moves reversed earlier easing

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 27 to 30. Analyst Certification on page 27

# 19 May 2026

Equity Derivatives

Global

BofA

Data

Analytics

![](images/23eb2697dd15f9b21a9beeec796bf237f4d330d72818e88205a9da4006615917.jpg)

Global Equity Derivatives Rsch
BofAS

Lars Naeckter >>

Equity-Linked Analyst

BofA (DIFC)

Riddhi Prasad >>

Equity-Linked Analyst

MLI (UK)

Arjun Goyal

Equity-Linked Analyst

BofAS

Benjamin Bowler

Equity-Linked Analyst

BofAS

benjamin.bowler@bofa.com

Abhinandan Deb >>

Equity-Linked Analyst

MLI (UK)

Meriem Hafid >>

Research Analyst

BofASE (France)

Nitin Saksena

Equity-Linked Analyst

BofAS

Nicholas Dunne

Equity-Linked Analyst

BofAS

Vittoria Volta >>

Equity-Linked Analyst

BofASE (France)

See Team Page for List of Analysts

Exhibit 1: 3M volatility (weekly chg)

Level & changes (in parentheses) in vol pts

<table><tr><td></td><td>Implied</td><td>Realized</td></tr><tr><td>S&amp;P500</td><td>16.4 (0.5)</td><td>14.7 (0.0)</td></tr><tr><td>ESTX50</td><td>18.8 (0.5)</td><td>22.5 (0.6)</td></tr><tr><td>FTSE</td><td>14.5 (0.2)</td><td>16.6 (0.2)</td></tr><tr><td>DAX</td><td>19.1 (0.4)</td><td>22.7 (0.6)</td></tr><tr><td>NKY</td><td>28.1 (0.6)</td><td>33.2 (-0.7)</td></tr><tr><td>HSCEI</td><td>21.1 (0.1)</td><td>20.4 (-0.4)</td></tr><tr><td>KOSPI</td><td>58.6 (8.1)</td><td>63.3 (-0.1)</td></tr><tr><td>EEM US</td><td>27.2 (2.3)</td><td>30.4 (1.5)</td></tr><tr><td>XIN9I</td><td>19.5 (0.4)</td><td>14.0 (0.5)</td></tr></table>

Source: BofA Global Research

BofA GLOBAL RESEARCH

See list of acronyms at the end of the report

# BofA GFSI™ X-Asset Risk Landscape

# GFSI slightly increases after Friday's market moves

The GFSI mildly increased last week as it moved from -0.13 on 8-May-26 to -0.11 on 15-May-26. Stress actually decreased through Thursday, as equities moved higher and the index reached -0.18, its lowest level since 27-Jan. However, Friday's move higher in rates and oil, coupled with equity weakness, erased earlier stress easing, leaving the GFSI in its $33^{\text{rd}}$ percentile since 2000.

Commodities led stress higher with copper and crude implied vols among the top eight stress-gainers of the week (Exhibit 3 & Exhibit 4). In fact, copper implied vol recorded a $95^{\text{th}}$ percentile gain in stress while crude implied vol stress increased for the fourth consecutive week (Exhibit 6). Crude implied vol remained the most stressed GFSI subcomponent and is joined in bearish territory by gold implied vol, with stress in both more than half a standard deviation above median levels (Exhibit 2).

Although all three commodity implied vol subcomponents saw stress increase last week, rates vol was the largest stress gainer versus all cross-asset vols and spreads (Exhibit 7). Interest rate implied vol EUR and USD were the first and third largest stress-gainers, respectively, as they each posted stress gains in their top deciles versus history (Exhibit 3 & Exhibit 6). Meanwhile, FX and equity stress also increased while credit stress slightly declined. Commodities remain the GFSI's most stressed asset class while FX is the least stressed (Exhibit 4).

• The US was the only region to record a decline in stress last week   
(Exhibit 5). Stress decreased for the third consecutive week, as volume flow, the subcomponent that tracks bullish or bearish US stock volume, posted the largest decline in stress (Exhibit 3).   
- GBP/USD implied vol posted a 90 $^{th}$ percentile stress gain (Exhibit 6) as GBP was under pressure from risks of a change in UK leadership (see UK Watch: 15-May-26 for perspective from our UK econ, rates, and FX teams).

Exhibit 2: Latest\* stress across GFSI sub-components   
Crude implied vol is the most stressed while Govt-OIS EUR is the least stressed   
![](images/e6245b1c8691670f1c337619248ddd22b273d56e7f975f3a390a961e77260575.jpg)

<details>
<summary>bar</summary>

| Component | GFSI Stress |
| --- | --- |
| Comdty Imp Vol Crude | 2.48 |
| Tibor-OIS | 2.04 |
| Nikkei Imp Vol | 1.22 |
| Comdty Imp Vol Gold | 1.12 |
| Equity Fund Flow EM | 0.51 |
| Int Rate Imp Vol EUR | 0.51 |
| Comdty Imp Vol Copper | 0.25 |
| SP500 Skew | 0.25 |
| Nikkei Skew | 0.15 |
| ESTX50 Imp Vol | 0.15 |
| HSI Imp Vol | 0.15 |
| ESTX50 Skew | 0.15 |
| FTSE Imp Vol | 0.15 |
| SP500 Imp Vol | 0.15 |
| USDJPY Skew | 0.15 |
| CDS Index Skew USD | 0.15 |
| HY Bond Flow | 0.15 |
| Int Rate Imp Vol USD | 0.15 |
| Euribor-OIS | 0.15 |
| Bond Basis USD | 0.15 |
| HY Corp CDS EUR | 0.15 |
| Bond Basis EUR | 0.15 |
| CDS Index Skew EUR | 0.15 |
| Money Mkt Flow | 0.15 |
| 3Y/5Y Credit Curve EUR | 0.15 |
| HY Corp CDS USD | 0.15 |
| IG Corp CDS EUR | 0.15 |
| EURJPY Skew | 0.15 |
| Euro member Bond Spread | 0.15 |
| AUDJPY Skew | 0.15 |
| GBPUSD Imp Vol | 0.15 |
| IG Corp CDS USD | 0.15 |
| Govt-OIS USD | 0.15 |
| USDJPY Imp Vol | -0.88 |
| Basis Swap EURUSD | -1.00 |
| IG Foreign Sovm Bond Spread | -1.01 |
| Volume Flow | -1.17 |
| EURUSD Imp Vol | -1.22 |
| Basis Swap USDJPY | -1.22 |
| Sub IG Foreign Sovm Bond Spread | -1.22 |
| Govt-OIS EUR | -1.22 |
</details>

Source: BofA Global Research. \*Latest as of 15-May-26. Disclaimer: The indicator identified above as BofA GFSI is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Exhibit 3: Change\*\* in stress across GFSI sub-components   
Interest rate implied vol EUR was the largest stress riser over the last week while volume flow stress fell the most   
![](images/82a99066c5709247a34a307ebf474c7a21454206b9ecc558df6a1d0876900311.jpg)

<details>
<summary>bar</summary>

| Entity | Change in GFSI Stress |
| :--- | :--- |
| Int Rate Imp Vol EUR | 0.36 |
| GBPUSD Imp Vol | 0.33 |
| Int Rate Imp Vol USD | 0.33 |
| Comdty Imp Vol Copper | 0.28 |
| Nikkei Skew | 0.21 |
| SP500 Skew | |
| Equity Fund Flow EM | |
| Comdty Imp Vol Crude | |
| Nikkei Imp Vol | |
| Govt-OIS USD | |
| CDS Index Skew EUR | |
| 3Y/5Y Credit Curve EUR | |
| ESTX50 Imp Vol | |
| Comdty Imp Vol Gold | |
| SP500 Imp Vol | |
| EURUSD Imp Vol | |
| IG Corp CDS EUR | |
| Basis Swap EURUSD | |
| IG Corp CDS USD | |
| FTSE Imp Vol | |
| HY Corp CDS EUR | |
| Euro member Bond Spread | |
| Sub IG Foreign Sovm Bond Spread | |
| Basis Swap USDJPY | |
| Money Mkt Flow | |
| USDJPY Imp Vol | |
| USDJPY Skew | |
| AUDJPY Skew | |
| EURJPY Skew | |
| ESTX50 Skew | |
| HSI Imp Vol | |
| IG Foreign Sovrn Bond Spread | |
| HY Corp CDS USD | |
| Govt-OIS EUR | |
| Bond Basis USD | |
| HY Bond Flow | -0.15 |
| CDS Index Skew USD | -0.17 |
| Euribor-OIS | -0.22 |
| Tibor-OIS | -0.24 |
| Bond Basis EUR | -0.42 |
| Volume Flow | |
</details>

Source: BofA Global Research. \*\*Latest as of 15-May-26. Change from 8-May-26 to 15-May-26.

BofA GLOBAL RESEARCH

The GFSI Risk Allocator (using Bull, Bear & Neutral weights of 2, 0, 1) suggested a 7.3% overweight position as of 15-May-26 (vs a 14.6% overweight position as of 8-May-26). The percentages of Bullish, Bearish, and Neutral GFSI components (as used in the Risk Allocator) as of 15-May-26 were 22.0%, 14.6%, and 63.4%, respectively.

Exhibit 4: Commodity stress increased the most last week   
On the other hand, credit stress decreased   
![](images/744dcea2a7854945058534c09d37166729d0e9b6cbf045639c004a9326d6d6d1.jpg)

<details>
<summary>bar</summary>

| Category | Latest stress (15-May-26) | Change in stress |
| :--- | :--- | :--- |
| Commodities | 1.3 | 0.16 |
| FX | -0.45 | 0.07 |
| Rates | -0.15 | 0.04 |
| Equities | 0.2 | 0.03 |
| Credit | -0.35 | -0.03 |
</details>

Source: BofA Global Research. Change from 8-May-26 to 15-May-26.   
BofA GLOBAL RESEARCH

Exhibit 6: Top 10 biggest stress movers (vs history)   
Copper implied vol saw a historically large stress increase   
![](images/1b8b319abda7d1de3ec7fe2dbb95da7e88794d07ffffdc3eef3ee3100e0fc3f7.jpg)

<details>
<summary>bar</summary>

%-ile of abschg in stress vs history*
| Category | Stress fall (%) | Stress rise (%) |
| :--- | :--- | :--- |
| Tibor-OIS | 96 | |
| Comdty Imp Vol Copper | 95 | |
| Int Rate Imp Vol EUR | 93 | |
| Int Rate Imp Vol USD | 91 | |
| GBPUSD Imp Vol | 90 | |
| Euribor-OIS | 90 | |
| Bond Basis USD | 83 | |
| Bond Basis EUR | 73 | |
| HY Bond Flow | 72 | |
| Volume Flow | 68 | |
</details>

Source: BofA Global Research. \* %-ile of 5-day moves in stress vs all historical 5-day moves (earliest 3-Jan-00). Bar colors represent rise (red) or fall (green) in stress. 5-day change (8-May-26 to 15-May-26).   
BofA GLOBAL RESEARCH

Exhibit 5: EM led regional stress higher last week   
In contrast, US stress declined   
![](images/f53b77abeac2c5e47cd45118a52970b691ea0f963d1a58a073aca259c8497c67.jpg)

<details>
<summary>bar</summary>

| Region | Latest stress (15-May-26) | Change in stress |
| :--- | :--- | :--- |
| EM | -0.2 | 0.04 |
| Europe | -0.2 | 0.04 |
| Japan | 1.2 | 0.03 |
| US | -0.3 | -0.02 |
</details>

Source: BofA Global Research. Change from 8-May-26 to 15-May-26.   
BofA GLOBAL RESEARCH

Exhibit 7: Biggest stress movers in cross-asset vols and spreads   
Rates vol experienced the largest increase in stress last week   
![](images/9aaadafbd4524bf2b5e5632832c8e70b78e1d3a5cd7b6118b946856724697bc0.jpg)

<details>
<summary>bar</summary>

| Category | Latest stress (15-May-26) | Change in stress |
| :--- | :--- | :--- |
| Rates Vol | 0.25 | 0.34 |
| Commodity Vol | 1.3 | 0.16 |
| FX Vol | -0.7 | 0.13 |
| Equity Vol | 0.3 | 0.05 |
| IG CDS | -0.35 | 0.04 |
| Sovm risk | -0.8 | 0.00 |
| HY CDS | -0.25 | -0.01 |
</details>

Source: BofA Global Research. Change from 8-May-26 to 15-May-26.   
BofA GLOBAL RESEARCH

# BofA Bubble Risk Indicator Landscape

# Global equity BRI rising, led by Kospi, Nikkei, US tech

The BofA Bubble Risk Indicator (BRI) is a price-based measure designed to detect bubble-like asset dynamics. Inspired by the way the first four moments describe a statistical distribution, the BRI distils an asset's returns, volatility, momentum, and fragility into a single bubble-risk reading on a 0 to 1 scale; 1 represents extreme bubble-like price action while 0 represents none. Historic asset bubbles have exhibited high BRI levels as they formed and peaked (see our 2026 Year Ahead for more details).

Exhibit 8: Bubble-like instability in global equities (MSCI World) broadly continues to rise, led by the BRIs of Kospi, Nikkei and US tech (though Mag7 still appears subdued); persistent geopolitical stress understandably keeps the energy-complex's BRIs high   
BofA Bubble Risk indicator (as of 15-May-26) across global equity indices, US equity sectors, commodities and crypto (bars: range of short- to long-term sub-indicators)   
![](images/ce7f544a9c2ea78557ac23d8bb3deab36fdd591b01fee913c131c441d4ed10e9.jpg)

<details>
<summary>bar</summary>

| Company   | Eq. index | US sector eq. | Commodity | Crypto |
|-----------|-----------|---------------|-----------|--------|
| Kospi     | 0.98      | 0.98          | 0.98      | 0.98   |
| Brent     | 0.75      | 0.72          | 0.92      | 0.92   |
| BCOM      | 0.75      | 0.68          | 0.90      | 0.90   |
| Nikkei    | 0.75      | 0.62          | 0.88      | 0.88   |
| Tech      | 0.75      | 0.70          | 0.85      | 0.85   |
| MSCI World| 0.75      | 0.75          | 0.85      | 0.85   |
| Energy    | 0.75      | 0.82          | 0.85      | 0.85   |
| Copper    | 0.75      | 0.68          | 0.65      | 0.65   |
| Silver    | 0.75      | 0.85          | 0.92      | 0.92   |
| Nasdaq    | 0.75      | 0.78          | 0.65      | 0.65   |
| S&P       | 0.75      | 0.70          | 0.65      | 0.65   |
| Russell   | 0.75      | 0.45          | 0.45      | 0.45   |
| Gold      | 0.75      | 0.45          | 0.45      | 0.45   |
| Mtrls     | 0.75      | 0.72          | 0.45      | 

[中间内容因长度限制已省略]

ng a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

# Research Analysts

# Benjamin Bowler

Equity-Linked Analyst

BofAS

+1 415 676 3595

benjamin.bowler@bofa.com

# Abhinandan Deb >>

Equity-Linked Analyst

MLI (UK)

+44 20 7995 7148

abhinandan.deb@bofa.com

# Nitin Saksena

Equity-Linked Analyst

BofAS

+1 646 855 5480

nitin.saksena@bofa.com

# Lars Naeckter >>

Equity-Linked Analyst

BofA (DIFC)

+971 4425

lars.naeckter@bofa.com

# Chintan Kotecha

Equity-Linked Analyst

BofAS

+1 646 855 5478

chintan.kotecha@bofa.com

# Riddhi Prasad >>

Equity-Linked Analyst

MLI (UK)

+44 20 7995-7852

riddhi.prasad@bofa.com

# Michael Youngworth, CFA

CBs, Pfds & Derivs Strategist

BofAS

+1 646 855 6493

michael.youngworth@bofa.com

# Vittoria Volta >>

Equity-Linked Analyst

BofASE (France)

+33 1 8770 0703

vittoria.volta@bofa.com

# Nicholas Dunne

Equity-Linked Analyst

BofAS

+1 646 855 2631

nicholas.dunne@bofa.com

# Arjun Goyal

Equity-Linked Analyst

BofAS

+1 646 743 4273

arjun.goyal@bofa.com

# Meriem Hafid >>

Research Analyst

BofASE (France)

+33 1 5365 5664

meriem.hafid@bofa.com

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules. Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.
"""
