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
# Global Equity Volatility Insights

# Lookbackmaxxing for a smarter AI hedge

# Lookback puts look like ideal hedge for rising bubble risks

Historic upside momentum in US tech stocks has powered the Nasdaq to 12 fresh all-time highs over the past month, generated near record up vs down realized vol, and pushed our Bubble Risk Indicator on US tech closer to the 0.8 threshold – further evidence we are living in “The Bubble Era”. In a runaway market exposed to persistent threats, protecting downside with fixed-strike hedges can be difficult given strike & timing risk. Vol-based hedges are compelling in this environment, as long equity + long vol have worked well recently, and 15x payout VIX call spreads offer limited risk, long vol exposure. Alternatively, structures like QQQ expanding put spreads automatically re-strike protection higher as markets rally (at prior max) just like a lookback put and are better-suited for high-trend markets (like today or the ‘90s dotcom bubble). They are better than vanilla hedges for mitigating strike & timing risk (requires only \~8% QQQ draw-up by Dec to beat vanilla puts, which is in bottom decile of draw-ups since 2023).

# Onward to resolution? EU upside & VSTOXX downside

Financial markets continue to look through episodic setbacks in US-Iran negotiations, with muted Brent (vs crisis highs), resilient European equities and a normalized VIX all pointing to a fading of geopolitical risk. We highlight opportunities for a further reduction of EU risk premium via SX7E/FTSEMIB and V2X. (i) Eurozone banks remain a high-beta beneficiary of improving sentiment, with SX7E “grinding lower, spiking higher” and FTSEMIB offering cyclicality at low vol levels; funding FTSEMIB calls with short SX7E puts allows us to efficiently position for 'war resolution' upside that benefits from cross-index vol dislocations. (ii) The V2X curve continues to embed war risk, reflecting Europe’s greater conflict sensitivity. As confidence in a durable ceasefire builds, V2X has scope to 'catch down' to pre-war levels with a typical upward-sloping curve, making Jun-26 put ratios (4x max payout ratio) attractive to position for limited vol normalization.

# Asia & Korean AI: Up to 13.5x payouts via worst of calls

Asian AI stocks keep climbing, with SK Hynix and Samsung Electronics up 193% and 137%. YTD, respectively. We still favour upside trades but with many of these stocks scoring very high on our BofA Bubble Risk Indicator, we note the benefits of options exposure vs holding cash equities outright. Worst-of call options (WoC) offer investors potential upside but with limited loss. At 59% and 66% discounts to the cheapest vanilla call option, respectively, we like 3-month worst of calls on 1) top AI stocks in Korea, Taiwan and Japan and 2) the top 3 IT stocks in Korea. At current cost, these could have paid out 8.0x and 13.5x the cost in the recent past.

# Also in the GEVI

Global x-asset stress falls as all asset classes except for commodities see stress decline

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 26 to 29. Analyst Certification on page 26. 12972283

# 12 May 2026

Equity Derivatives
Global

BofA

# Data Analytics

![](images/f42af9d6209375b09415a4e4e0b57ca365fb6863ee05da3dda11bcd36af22911.jpg)

Global Equity Derivatives Rsch
BofAS

Arjun Goyal

Equity-Linked Analyst
BofAS

Lars Naeckter >>

Equity-Linked Analyst
BofA (DIFC)

Riddhi Prasad >>

Equity-Linked Analyst
MLI (UK)

Nitin Saksena

Equity-Linked Analyst
BofAS

Vittoria Volta >>

Equity-Linked Analyst
BofASE (France)

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

Nicholas Dunne

Equity-Linked Analyst
BofAS

See Team Page for List of Analysts

Exhibit 1: 3M volatility (weekly chg)

Level & changes (in parentheses) in vol pts

<table><tr><td></td><td>Implied</td><td>Realized</td></tr><tr><td>S&amp;P500</td><td>15.9 (0.0)</td><td>14.7 (-0.4)</td></tr><tr><td>ESTX50</td><td>18.2 (0.2)</td><td>21.9 (1.2)</td></tr><tr><td>FTSE</td><td>14.3 (-0.4)</td><td>16.5 (0.8)</td></tr><tr><td>DAX</td><td>18.6 (-0.1)</td><td>22.1 (0.8)</td></tr><tr><td>NKY</td><td>27.4 (0.8)</td><td>33.9 (1.8)</td></tr><tr><td>HSCEI</td><td>21.0 (0.3)</td><td>20.8 (-1.1)</td></tr><tr><td>KOSPI</td><td>50.5 (2.0)</td><td>63.4 (1.6)</td></tr><tr><td>EEM US</td><td>24.9 (0.2)</td><td>28.9 (0.7)</td></tr><tr><td>XIN9I</td><td>19.1 (1.5)</td><td>13.4 (-0.2)</td></tr></table>

Source: BofA Global Research

BofA GLOBAL RESEARCH

See list of acronyms at the end of the report

# BofA GFSI™ X-Asset Risk Landscape

# GFSI continues to ease as equity stress declines

Global stress declined for the fifth time in the last six weeks as the GFSI fell from -0.01 on 1-May-26 to -0.13 on 8-May-26. The index is now in its 31 $^{st}$ percentile since 2000 and at its lowest level since 10-Feb.

Equities led stress lower as they posted the largest absolute change in stress for the fourth straight week (Exhibit 4). This came as the S&P 500 recorded its sixth consecutive week of gains and notched another all-time high. Like the prior week, volume flow, the subcomponent that measures bullish and bearish US stock volume, and S&P 500 skew recorded the top two declines in stress. This contributed to making the US the top regional stress-decliner (Exhibit 5). Nikkei and ESTX50 skews were also among the top eight stress-decliners of the week (Exhibit 3). Notably, equity vol stress slightly increased with Nikkei implied vol recording the second largest stress increase (Exhibit 3 & Exhibit 7).

Rates, FX, and credit stress also declined while commodity stress increased (Exhibit 4). Interest rate implied vol EUR posted a $95^{\text{th}}$ percentile decline in stress as it led rates stress lower (Exhibit 3 & Exhibit 6). In fact, it helped rates vol record the largest decline in stress versus all cross-asset vols and spreads (Exhibit 7). AUDJPY skew was the only subcomponent outside of equities or rates among the top ten stress-decliners (Exhibit 3). Commodities remain the GFSI's most stressed asset class while FX is the least stressed (Exhibit 4).

\- Crude implied vol is now the GFSI's most stressed subcomponent (Exhibit 2). Stress increased for the third consecutive week, though, unlike the prior two weeks, the rise in stress occurred alongside declining crude futures prices (Exhibit 3).

Exhibit 2: Latest\* stress across GFSI sub-components   
Crude implied vol is the most stressed while sub-IG foreign sovereign bond spreads are the least stressed   
![](images/1f6a243055ca6dc8fc2c57cd99255a2d6f4378227904defff54e8213102514d1.jpg)

<details>
<summary>bar</summary>

| Category | GFSI Stress |
| --- | --- |
| Comdty Imp Vol Crude | 2.36 |
| Tibor-OIS | 2.26 |
| Nikkei Imp Vol | 1.12 |
| Comdty Imp Vol Gold | 1.05 |
| Equity Fund Flow EM | 0.30 |
| SP500 Skew | |
| Int Rate Imp Vol EUR | |
| HSI Imp Vol | |
| ESTX50 Skew | |
| ESTX50 Imp Vol | |
| CDS Index Skew USD | |
| Comdty Imp Vol Copper | |
| HY Bond Flow | |
| FTSE Imp Vol | |
| Euribor-OIS | |
| Bond Basis EUR | |
| Nikkei Skew | |
| SP500 Imp Vol | |
| Bond Basis USD | |
| USDJPY Skew | |
| HY Corp CDS EUR | |
| HY Corp CDS USD | |
| Money Mkt Flow | |
| EURJPY Skew | |
| CDS Index Skew EUR | |
| AUDJPY Skew | |
| IG Corp CDS EUR | |
| Euro member Bond Spread | |
| 3Y/5Y Credit Curve EUR | |
| Int Rate Imp Vol USD | |
| Volume Flow | |
| IG Corp CDS USD | |
| Govt-OIS USD | |
| GBPUSD Imp Vol | |
| IG Foreign Sovrn Bond Spread | |
| USDJPY Imp Vol | |
| Basis Swap EURUSD | -0.78 |
| Basis Swap USDJPY | -1.02 |
| EURUSD Imp Vol | -1.07 |
| Govt-OIS EUR | -1.14 |
| Sub IG Foreign Sovrn Bond Spread | -1.18 |
</details>

Source: BofA Global Research. \*Latest as of 8-May-26. Disclaimer: The indicator identified above as BofA GFSI is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Exhibit 3: Change\*\* in stress across GFSI sub-components   
Copper implied vol was the largest stress riser over the last week while volume flow stress fell the most   
![](images/9ba1c9a5379e56db5f597b2d06d7ebca96d11e753a7adddc143d5108fe8b00b7.jpg)

<details>
<summary>bar</summary>

| Entity | Change in GFSI Stress |
| :--- | :--- |
| Comdty Imp Vol Copper | 0.13 |
| Nikkei Imp Vol | 0.12 |
| Bond Basis EUR | 0.11 |
| Euribor-OIS | 0.10 |
| Comdty Imp Vol Crude | 0.10 |
| CDS Index Skew EUR | 0.01 |
| ESTX50 Imp Vol | 0.01 |
| Equity Fund Flow EM | 0.00 |
| CDS Index Skew USD | 0.00 |
| SP500 Imp Vol | 0.00 |
| HSI Imp Vol | 0.00 |
| Money Mkt Flow | 0.00 |
| HY Corp CDS USD | 0.00 |
| 3Y/5Y Credit Curve EUR | 0.00 |
| IG Corp CDS USD | 0.00 |
| EURJPY Skew | -0.01 |
| HY Bond Flow | 0.00 |
| HY Corp CDS EUR | 0.00 |
| IG Corp CDS EUR | 0.00 |
| Sub IG Foreign Sovm Bond Spread | 0.00 |
| Basis Swap USDJPY | 0.00 |
| IG Foreign Sovrn Bond Spread | 0.00 |
| FTSE Imp Vol | 0.00 |
| Comdty Imp Vol Gold | 0.00 |
| Bond Basis USD | 0.00 |
| Basis Swap EURUSD | 0.00 |
| Euro member Bond Spread | 0.00 |
| GBPUSD Imp Vol | -0.01 |
| EURUSD Imp Vol | -0.01 |
| USDJPY Skew | -0.14 |
| USDJPY Imp Vol | -0.14 |
| Govt-OIS USD | -0.28 |
| Int Rate Imp Vol USD | -0.32 |
| ESTX50 Skew | -0.32 |
| AUDJPY Skew | -0.32 |
| Nikkei Skew | -0.32 |
| Tibor-OIS | -0.21 |
| Govt-OIS EUR | -0.25 |
| Int Rate Imp Vol EUR | -0.44 |
| SP500 Skew | -0.54 |
| Volume Flow | -0.79 |
</details>

Source: BofA Global Research. \*\*Latest as of 1-May-26. Change from 1-May-26 to 8-May-26.

BofA GLOBAL RESEARCH

The GFSI Risk Allocator (using Bull, Bear & Neutral weights of 2, 0, 1) suggested a 14.6% overweight position as of 8-May-26 (vs a 4.9% overweight position as of 1-May-26). The percentages of Bullish, Bearish, and Neutral GFSI components (as used in the Risk Allocator) as of 8-May-26 were 24.4%, 9.8%, and 65.9%, respectively.

Exhibit 4: Equity stress decreased the most last week   
On the other hand, commodity stress increased   
![](images/82a4eae5ffbee1d1f5b1a6030bf1dbd7853565675944534c7dc0ff4b346809ef.jpg)

<details>
<summary>bar</summary>

| Category | Latest stress (08-May-26) | Change in stress |
| :--- | :--- | :--- |
| Commodities | 1.18 | 0.06 |
| Credit | -0.35 | -0.02 |
| FX | -0.55 | -0.12 |
| Rates | -0.25 | -0.14 |
| Equities | 0.10 | -0.16 |
</details>

Source: BofA Global Research. Change from 1-May-26 to 8-May-26.

BofA GLOBAL RESEARCH

Exhibit 6: Top 10 biggest stress movers (vs history)   
Tibor-OIS saw a historically large stress decrease   
![](images/9a0a7c902f2a0351467d3bb6d1fb8338199fff73ef6cfcc6695632216c3c71c1.jpg)

<details>
<summary>bar</summary>

%-ile of abschg in stress vs history*
| Category | Stress fall (%) | Stress rise (%) |
| :--- | :--- | :--- |
| Tibor-OIS | 96 | |
| Int Rate Imp Vol EUR | 95 | |
| Volume Flow | 93 | |
| AUDJPY Skew | 81 | |
| SP500 Skew | 81 | |
| Euribor-OIS | 81 | |
| Govt-OIS USD | 78 | |
| Euro member Bond Spread | 78 | |
| Int Rate Imp Vol USD | 77 | |
| Comdty Imp Vol Copper | 77 | |
</details>

Source: BofA Global Research. \* %-ile of 5-day moves in stress vs all historical 5-day moves (earliest 3-Jan-00). Bar colors represent rise (red) or fall (green) in stress. 5-day change (1-May-26 to 8-May-26).

BofA GLOBAL RESEARCH

Exhibit 5: The US led regional stress lower last week   
Meanwhile, EM stress declined the least   
![](images/f96eb2146cab73772d273b041f7599f46837e3cbc07dc56cdc2add1a3a968836.jpg)

<details>
<summary>bar</summary>

| Region | Latest stress (08-May-26) | Change in stress |
| :--- | :--- | :--- |
| EM | -0.01 | |
| Japan | 1.15 | -0.10 |
| Europe | -0.18 | -0.10 |
| US | -0.23 | -0.15 |
</details>

Source: BofA Global Research. Change from 1-May-26 to 8-May-26.

BofA GLOBAL RESEARCH

Exhibit 7: Biggest stress movers in cross-asset vols and spreads   
Rates vol experienced the largest decrease in stress last week   
![](images/5e3a77416c92b8b25f711bfd997c5c6a57bd672a1dd049e4fa76641f4b611b9b.jpg)

<details>
<summary>bar</summary>

| Category | Latest stress (08-May-26) | Change in stress |
| :--- | :--- | :--- |
| Commodity Vol | 1.2 | 0.06 |
| Equity Vol | 0.3 | 0.02 |
| HY CDS | -0.3 | -0.03 |
| IG CDS | -0.4 | -0.04 |
| Sovrn risk | -0.7 | -0.06 |
| FX Vol | -0.8 | -0.12 |
| Rates Vol | -0.1 | -0.31 |
</details>

Source: BofA Global Research. Change from 1-May-26 to 8-May-26.

BofA GLOBAL RESEARCH

# BofA Bubble Risk Indicator Landscape

# Price action in US tech stocks appears increasingly frothy

The BofA Bubble Risk Indicator (BRI) is a price-based measure designed to detect bubble-like asset dynamics. Inspired by the way the first four moments describe a statistical distribution, the BRI distils an asset's returns, volatility, momentum, and fragility into a single bubble-risk reading on a 0 to 1 scale; 1 represents extreme bubble-like price action while 0 represents none. Historic asset bubbles have exhibited high BRI levels as they formed and peaked (see our 2026 Year Ahead for more details).

Exhibit 8: The Kospi, Nikkei and US tech continue to exhibit bubble-like instability, with Nasdaq's BRI also moving higher (though still not at extremes); persistent geopolitical stress understandably keeps the energy-complex's BRIs high   
BofA Bubble Risk indicator (as of 8-May-26) across global equity indices, US equity sectors, commodities and crypto (bars: range of short- to long-term sub-indicators)   
![](images/73d8befd6e5a4bc36e022d1afa2dc7674a7752416e58705d4daa1e2533e0c807.jpg)

<details>
<summary>bar</summary>

| Index     | Eq. index | US sector eq. | Commodity | Crypto |
|-----------|-----------|---------------|-----------|--------|
| Kospi     | 1.0       | -             | -         | -      |
| Brent     | -         | -             | 0.9       | -      |
| BCOM      | -         | -             | 0.9       | -      |
| Nikkei    | 0.85      | -             | -         | -      |
| Tech      | -         | 0.7           | -         | -      |
| MSCI World| 0.7       | -             | -         | -      |
| Silver    | -         | -             | 0.65      | -      |
| Nasdaq    | 0.65      | -             | -         | -      |
| Copper    | -         | -             | 0.65      | -      |
| S&P       | 0.6       | -             | -         | -      |
| Russell   | 0.55      | -             | -         | -      |
| Mtrls     | -         | 0.85          | -         | -      |
| Energy    | -         | 0.75          | -         | -      |
| Indus     | -         | 0.7           | -         | -      |
| Gold      | -         | 0.9           | 0.5       | -      |
| R'estate  | -         | 0.7           | -         | -      |
| Staples   | -         | 0.8           | -         | -      |
| FTSE      | 0.4       | -             | -         | -      |
| Mag7      | -         | 0.6           | -         | -      |
| Disc      | -         | 0.4           | -         | -      |
| SX7E      | 0.35      | -             | -         | -      |
| SX5E      | 0.35      | -             | -         | -      |
| Utils     | 0.35      | 0.3           | -         | -      |
| Bitcoin   | -         | 0.3           | -         | 0.25   |
| CAC       | 0.25      | -             | -         | -      |
| DAX       | 0.25      | -             | -         | -      |
| Comms     | 0.3       | 0.2           | -         | -      |
| H'care    | 0.4       | 0.2           | -         | -      |
| Ethereum  | 0.3       | 0.2           | -         | 0.15   |
| HSCEI     | 0.2       | 0.15          | -         | -      |
| Nifty     | 0.15      | 0.1           | -         | -      |
| Fins      | 0.1       | 0.1           | -         | -      |
</details>

Source: BofA Global Research. Data as of 8-May-26. Underlying tickers: SPX, NDX, RTY, SX5E, SX7E, CAC, DAX, UKX, NKY, HSCEI, KOSPI2, NIFTY, MXWD, IXB, IXCPR, IXE, IXM, IXI, IXT, IXR, IXRE, IXU, IXV, IXY, BM7P, BCOM, CO1, XAU, XAG, HG1, XBTUSD, XETUSD. Disclaimer: The indicator identified as the BofA Bubble Risk Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark.

BofA GLOBAL RESEARCH

Exhibit 9: Semiconductor stocks still show relatively high bubble-like dynamics among popular equity themes   
Highest BRI readings across popular equity themes (as of 8-May-26)   
![](images/dcd91f2121a244d8ca0e007032e6868867ecc5cf347ca526a18217fe90a5166a.jpg)

<details>
<summary>bar</summary>

| Category       | Value |
| -------------- | ----- |
| Semis          | 0.85  |
| Momentum       | 0.78  |
| Clean Ener     | 0.68  |
| EM             | 0.67  |
| Oil Explor     | 0.63  |
| Infra          | 0.58  |
| Transport      | 0.55  |
| Biotech        | 0.54  |
| Growth         | 0.52  |
| Metals Mining  | 0.25  |
</details>

Source: BofA Global Research. Data as of 8-May-26. Underlying tickers: DZETR, GU731834, SPGTCLNT, FQEACR, SPSIOPTR, IPAVE, SPTSCUT, SPSIBITR, CRSPLCGT, SPSIMMTR. See Disclaimer in Exhibit 8.

Exhibit 10: Cybersecurity stocks have seen the biggest jump in their Bubble Risk Indicator over the past week among popular equity themes   
Largest 1w changes in BRI across popular equity themes (as of 8-May-26)   
![](images/654eed030f6162ed0d70a953a553ba123de16e9017b14f7046ee518d9ea09d5e.jpg)

<details>
<summary>bar</summary>

| Category   

[中间内容因长度限制已省略]

ed on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

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
