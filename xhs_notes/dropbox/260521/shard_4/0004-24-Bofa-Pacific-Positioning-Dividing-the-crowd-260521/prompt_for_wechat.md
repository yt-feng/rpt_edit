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
# Pacific Positioning

# Dividing the crowd

# Large performance spread within “Crowded” stocks

Contrary to popular opinion, some crowded stocks can continue outperforming despite being well held by investors. In the last 12 months, “Crowded Positives” (well-owned stocks + Positive Triple Momentum) outperformed “Crowded Negatives” (well-owned stocks + Negative Triple Momentum) by 36.0%. The latest screen of Crowded Positives includes TSMC, MediaTek, BeOne Medicine-ADR, WinWay Tech, and Taiwan Union. “Crowded Negatives” include Bharti (Airtel), Infosys, Hub24, NextDC, and Faraday Tech.

# Active funds sold China and Korea in April

As the MSCI Asia Pac ex-Japan Index rallied 15% in April, long-only funds globally bought shares in Australia (+\$3.8bn) and India (+\$2.9bn) but sold shares in China (-\$39.7bn) and Korea (-\$13.6bn). By sector in Asia, long-only funds bought the most shares in Energy (+\$1.4bn) and Materials (+\$0.9bn), while selling Semis (-\$26.2bn). By stock, funds bought shares in Suzhou Dongshan, Bharti (Airtel), Zhongji Innolight, and China CSSC. In contrast, funds sold shares in SK Hynix, TSMC, Samsung Electronics, and CATL.

# Funds remain most overweight Taiwan and Korea

Funds remain most overweight Taiwan and Korea, and underweight India and Australia. By sector, funds are most overweight Semis, Tech Hardware, and Consumer Discretionary, and most underweight Banks, Energy, and Diversified Financials.

Chart 1: Asia Positioning + Triple Momentum relative performance: Last 12-months   
In the last year, Crowded Positives outperformed, Under-owned Negatives underperformed   
![](images/0ad3b650c979fdfaf3fff243ea5b46e55c2a1e5b5ef26e215c1f063e3efffd41.jpg)

<details>
<summary>line</summary>

| Month   | Crowded Positives | Crowded Negatives | Under-owned Positives | Under-owned Negatives |
|---------|-------------------|-------------------|----------------------|-----------------------|
| Apr-26  | 21.2%             | -14.8%            | 20.7%                | -15.6%                |
</details>

Source : BofA Asia Pac Quantitative Strategy, MSCI, FTSE, FactSet, Bloomberg, 13F Filings, Benchmark Indices, Country Stock Exchanges Performance is shown relative to the average performance of stocks in the analysis with Ownership, Active Exposure, and Triple Momentum Ranks.

BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 75 to 77.

12976301

# 21 May 2026

Quant Strategy

Asia Pacific

BofA

Data

Analytics

![](images/a62242c9f993bad27220fa30a2833e2bc35ff9ae2fae617472a19177679e12f3.jpg)

Nigel Tupper >>

Quant Strategist

BofA (Australia)

+61 2 9226 5735

nigel.tupper@bofa.com

Amar Vashi >>

Quant Strategist

BofA (Australia)

amar.vashi@bofa.com

Sumuhan Shanmugalingam >>

Quant Strategist

BofA (Australia)

sumuhan.shanmugalingam@bofa.com

Unless otherwise noted all links on the front page of this report refer to sections in this research report.

# Executive Summary

Crowded Positives Screen

Crowded Negatives Screen

Under-owned Negatives Screen

Under-owned Positives Screen

Equity Flow

■ Active Exposures (over/underweights)

■ Stock Charts (Australia, China, India, Korea, Singapore, Taiwan)

Performance Overview

# Contents

Executive Summary 5

Active Exposure – Positioning versus Benchmark 5

Equity Flow – Long-only Funds 6

Fund Ownership 7

Combining Fund Ownership & Active Exposure 7

Four Stock Screens 8

Stock Positioning Charts 9

Methodology changes versus previous version of this analysis 9

Methodology 10

Funds included in this Analysis 10

Stocks included in this Analysis 12

Relative Weight versus Benchmark 12

Data Sources 12

Construction Methodology 13

Performance Calculation Methodology 15

Limitations 15

Four Stock Screens 17

Crowded Positives - Stock Screen 18

Under-owned Positives - Stock Screen 18

Crowded Negatives - Stock Screen 19

Under-owned Negatives - Stock Screen 19

Equity Flow - Long-Only 20

Countries – Equity Flow 20

Asia Pac ex-Japan Sectors – Equity Flow 23

Country-Sectors – Equity Flow 25

Asia Pac ex-Japan Stocks – Equity Flow 27

Positioning versus Benchmark - Active Long-Only 28

Countries - Positioning versus benchmark 28

Asia Pac ex-Japan Sectors - Positioning versus benchmark 31

Asia Pac ex-Japan Stocks – Positioning versus Benchmark 35

Stock Positioning Charts 37

Australia 37

China 41

India 45

South Korea 49

Singapore 53

Taiwan 57

Performance Overview 61

Positioning and Triple Momentum Performance 61

Back-testing Results 65

Appendix A: Positioning and Triple Momentum Performance Summary 67

Global Quant Publications 73

# Notice to Readers:

The various screens identified in this report are intended to be indicative metrics only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. These screens were not created to act as a benchmark.

The screens in this report are not a recommended list either individually or as a group of stocks. Investors should consider the fundamentals of the companies and their own individual circumstances/objectives before making any investment decisions.

Triple Momentum is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. Triple Momentum was not created to act as a benchmark.

Some of the analysis as described in this report is back-tested and does not represent the actual performance of any account or fund. Back-tested performance depicts the hypothetical back-tested performance of a particular strategy over the time period indicated. In future periods, market and economic conditions will differ and the same strategy will not necessarily produce the same results. No representation is being made that any actual portfolio is likely to have achieved returns similar to those shown herein. In fact, there are frequently sharp differences between back-tested returns and the actual results realized in the actual management of a portfolio. Back-tested performance results are created by applying an investment strategy or methodology to historical data and attempts to give an indication as to how a strategy might have performed during a certain period in the past if the product had been in existence during such time. Back-tested results have inherent limitations including the fact that they are calculated with the full benefit of hindsight, which allows the security selection methodology to be adjusted to maximize the returns. Further, the results shown do not reflect actual trading or the impact that material economic and market factors might have had on a portfolio manager's decision-making under actual circumstances. Back-tested returns do not reflect advisory fees, trading costs, or other fees or expenses.

This report includes factors for informational or descriptive purposes, and inclusion here is not equivalent to a recommendation of the factor or portfolio.

All data in the report is as of 30-Apr-2026 unless stated otherwise.

# Executive Summary

This report includes analysis on the following topics:

• Active Exposure - Positioning versus Benchmark   
• Equity Flow - Long-only funds   
• Fund Ownership – Proportion of funds owning a stock   
• Combining Fund Ownership & Active Exposure   
• Four Stock Screens   
• Stock Positioning Charts   
- Back-testing   
• Methodology changes versus previous version of this analysis

# Active Exposure – Positioning versus Benchmark

# Long-only funds' declared portfolio holdings versus benchmark

Each month we analyze the declared portfolio holdings of large active long-only funds globally that invest in Asia equities or Asia stocks are in their benchmark. Funds are included in the analysis if (i) they manage more than US\$500m in equities, (ii) declare portfolio holdings on a regular basis, (iii) we can identify the benchmark of these funds, and (iv) we have access to the constituents of the benchmark. We review the funds included in the analysis annually. This analysis currently includes more than 4581 active long-only funds managing more than US\$2.8 trillion in equities. We identify the benchmark of each fund, and there are more than 637 unique benchmarks across the funds in this analysis.

To find the active exposure for each fund, we compare the stock holdings versus the specific benchmark disclosed by the relevant fund to establish relative overweight and underweight stock positions (“Relative Weight”). The relative positions are weighted by the dollar value of the relative positions to calculate AUM-weighted relative weight. We aggregate the US dollar-weighted overweight and underweight positions by stock, sector, country, and region in order to monitor how funds’ active exposures against the benchmarks change through time.

The chart below is an example of Active long-only funds' relative weight for a stock.

Chart 2: Stock A - Long-only Funds Active Exposure (Relative Weight %) vs identified Benchmarks   
Active Long-only funds have been persistently overweight   
![](images/79746cfb6ce58f0c1edf482bfeaf7419e128936fa6ceff41744eb580dcd8415b.jpg)

<details>
<summary>line</summary>

| Date    | Stock A-Relative Weight (%) |
|---------|----------------------------|
| Jan-15  | 0.30%                      |
| Jul-15  | 0.32%                      |
| Jan-16  | 0.34%                      |
| Jul-16  | 0.36%                      |
| Jan-17  | 0.38%                      |
| Jul-17  | 0.40%                      |
| Jan-18  | 0.42%                      |
| Jul-18  | 0.44%                      |
| Jan-19  | 0.46%                      |
| Jul-19  | 0.58%                      |
| Jan-20  | 0.40%                      |
| Jul-20  | 0.35%                      |
| Jan-21  | 0.20%                      |
| Jul-21  | 0.15%                      |
| Jan-22  | 0.10%                      |
| Jul-22  | 0.25%                      |
| Jan-23  | 0.30%                      |
| Jul-23  | 0.35%                      |
| Jan-24  | 0.40%                      |
| Jul-24  | 0.42%                      |
| Jan-25  | 0.35%                      |
| Jul-25  | 0.30%                      |
</details>

Source: BofA Global Quantitative Strategy, MSCI, FTSE, Factset, Bloomberg, 13F Filings, Benchmark Indices, Country Stock Exchanges
BofA GLOBAL RESEARCH

# Equity Flow -Long-only Funds

# Value of shares bought and sold by long-only funds

In addition to monitoring Active Exposure versus benchmark, we also calculate the value of the shares that long-only funds (active and passive) have bought and sold each month. Each month, we calculate the change in the number of every share held in each portfolio and disclosed by the relevant long-only fund, and multiple this by the respective Volume Weighted Average Price (VWAP) for the month. We believe VWAP is a reasonable approximation of the price at which funds may have bought and sold stocks during the month. It’s worth noting the Active Exposure versus benchmark can be impacted by 1) changes to stock holdings, but also 2) changes to benchmark weights, and 3) the performance of stocks (e.g. an underweight position increases in magnitude if a stock outperforms even if no shares were sold).

Client have consistently asked for information on what funds are buying and selling. To address this question we introduce the Equity Flow analysis. We believe Equity Flow effectively determines the contribution to the change in the active exposure from funds buying and selling shares. We aggregate the US dollar value of the change in the declared portfolio holdings by stock, sector, country, and region. The chart below is an example of the value of Active long-only funds' cumulative buying and selling in aggregate for all listed China stocks.

Chart 3: Aggregate Cumulative Long-only Equity Flow   
China Cumulative Long-only Equity Flow   
![](images/6880080c5da611eea42dc9817ca036d81dbcb902dd207dc4d7775e6c10028d13.jpg)

<details>
<summary>line</summary>

| Date    | Cumulative Long-only Equity Flow ($bn) |
|---------|----------------------------------------|
| Sep-25  | 193.0                                  |
</details>

Source: BofA Global Quantitative Strategy, MSCI, FTSE, FactSet, Bloomberg, 13F Filings, Benchmark Indices, Country Stock Exchanges
BofA GLOBAL RESEARCH

Chart 4: APxJ Long-only Active and Passive Funds Cumulative Equity Flow (\$bn)   
Long-only funds have been consistently buying Passive Funds and selling shares in Active Funds   
![](images/badf9172cac23966626a2f0329c54c6261a87e97da1d63c8be6cb7ee35590bc6.jpg)

<details>
<summary>line</summary>

| Date    | Cumulative Long-only Equity Flow ($bn) |
|---------|----------------------------------------|
| Jan-15  | 0                                      |
| Jun-15  | 0                                      |
| Nov-15  | 0                                      |
| Apr-16  | 0                                      |
| Sep-16  | 0                                      |
| Feb-17  | 0                                      |
| Jul-17  | 0                                      |
| Dec-17  | 0                                      |
| May-18  | 0                                      |
| Oct-18  | 0                                      |
| Mar-19  | 0                                      |
| Aug-19  | 0                                      |
| Jan-20  | 0                                      |
| Jun-20  | 0                                      |
| Nov-20  | 0                                      |
| Apr-21  | 0                                      |
| Sep-21  | 0                                      |
| Feb-22  | 0                                      |
| Jul-22  | 0                                      |
| Dec-22  | 0                                      |
| May-23  | 0                                      |
| Oct-23  | 0                                      |
| Mar-24  | 0                                      |
| Aug-24  | 0                                      |
| Jan-25  | 0                                      |
| Jun-25  | 0                                      |
| Nov-25  | 0                                      |
| Apr-26  | 0                                      |
| Sep-26  | 0                                      |
</details>

Source : BofA Asia Pac Quantitative Strategy, MSCI, FTSE, FactSet, Bloomberg, 13F Filings, Benchmark Indices, Country Stock Exchanges   
BofA GLOBAL RESEARCH

# Fund Ownership

For each stock in the analysis, every month we calculate “Fund Ownership” as the proportion of relevant Active Long-only funds that own a stock (e.g. 73% of relevant funds own Stock B) at the end of each month. A relevant fund is one for which the stock is included in the fund’s benchmark, or the fund owns the stock even if it is not in the benchmark. For example, if the total number of funds in the analysis is 1000, but a certain stock is only in the benchmark of 180 funds, and 150 funds in total own the stock, of which 20 funds own the stock even though it is not in the benchmark of that fund, then Fund Ownership is 75% (150 / (180 +20)).

The example chart below shows the proportion of Active long-only funds in the analysis that own Stock A.

Chart 5: Stock B: Fund Ownership = Proportion of Active Long-only Funds holding the stock   
Fund Ownership of Stock B has increased through time and is now at all-time high   
![](images/1dc5d249e5a73f8c07bd9aafc4220b0d8c83c15c04f584aa16b8590098543bde.jpg)

<details>
<summary>line</summary>

| Date   | Funds Ownership (%) |
|--------|---------------------|
| Aug-25 | 73%                 |
</details>

Source: BofA Global Quantitative Strategy, MSCI, FTSE, FactSet, 13F Filings, Benchmark Indices, Country Stock Exchanges   
BofA GLOBAL RESEARCH

# Combining Fund Ownership & Active Exposure

# Combining fund ownership levels and relative weight

We illustrate in quadrant charts (Chart 5) which stocks have various combinations of 1)

Above/Below-median Fund Ownership, and 2) Active Exposure

(Overweight/Underweight):

- Above-median Fund Ownership ("High Fund Ownership") + Overweight   
- Above-median Fund Ownership ("High Fund Ownership") + Underweight   
Below-median Fund Ownership ("Low Fund Ownership") + Overweight   
• Below-median Fund Ownership ("Low Fund Ownership") + Underweight

# Four Stock Screens

# Positioning (Fund Ownership + Active Exposure) + Catalyst (Triple Momentum)

While many investors often aim to do the opposite of what everyone else is doing, it is not necessarily a successful strategy to always be contrarian. Our analysis shows that stocks that have high ownership and are overweight can outperform for years if a stock's fundamentals remain relatively attractive. Therefore, we believe the challenge for investors is to differentiate between crowded trades with a positive catalyst and crowded trades with a negative catalyst. Similarly, there is an opportunity to identify under-owned stocks which have a positive catalyst and under-owned stocks with a negative catalyst.

Our Triple Momentum analysis combines earnings, price, and news momentum to determine when a stock is in vogue or not in vogue, and is useful for identifying stocks with catalysts for a potential change (positive or negative) in subsequent performance. Methodology for Triple Momentum is detailed in “Triple Momentum Allocator” report.

We therefore combined the analysis we introduced above with our Triple Momentum Strategy to create the Four Stock Screens. These are:

• Crowded Positives (Consensus)   
Hig

[中间内容因长度限制已省略]

ch information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
