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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## CHINA BROKERS & ASSET MANAGERS

# Positioned for Structural Growth Amid Shifting Sector Dynamics

China brokers' shares have performed strongly since June 9, +7%/+5% vs. +1%/+3% of banks for A/H shares within our coverage. This aligns with our key takeaways from the recent China Financials trip: we prefer brokers over banks. Incorporating incremental insights from GS strategists' latest views on the HK IPO market, we reiterate a constructive stance on China brokers relative to banks, reflecting a meaningful shift in the sector's fundamental drivers. As loan growth decelerates across the banking system, earnings growth is no longer the primary determinant of bank valuations; instead, investor focus has shifted toward balance sheet resilience and capital strength. In this context, brokers offer a more compelling combination of cyclical earnings recovery and structural return improvement, supported by capital markets activity and international business expansion.

Exhibit 1: Brokers are demonstrating strong performance, +7%/+5% vs. +1%/+3% of banks for A/H share since June 9.  
As of June 15  
![](images/f9af3571ca776844471ba75d21da682103db83ab6963133a3628eff56f50c873.jpg)

<details>
<summary>bar chart</summary>

Price performance since June 9
| Category | Price Performance (%) |
|---|---|
| Brokers (A) | 7 |
| Banks (A) | 1 |
| Brokers (H) | 5 |
| Banks (H) | 3 |
</details>

Price performance is based on the average of our covered companies  
Source: Wind

Central to our positive view is the role of Hong Kong business as a key engine of ROE expansion for Chinese brokers. Management teams across leading brokers have articulated a clear strategic pivot toward scaling their international businesses, particularly in Hong Kong, where returns are structurally higher than in the onshore market. This shift is being enabled by active capital raising, such as equity placements and refinancing, which are designed to fund balance sheet expansion in

## Shuo Yang, Ph.D.

+852-2978-0701 | shuo.yang@gs.com

GS (Asia) L.L.C.

## Claire Ouyang

+852-2978-6686

claire.x.ouyang@gs.com

GS (Asia) L.L.C.

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

offshore operations. As a result, offshore subsidiaries are already delivering meaningfully higher leverage and ROE compared to group averages, providing a clear pathway for consolidated ROE improvement over the medium term. For example, CICC management mentioned during a CEO meeting it has raised its medium-term ROE target to 13–15%, explicitly citing capital deployment into Hong Kong as the primary driver.

Exhibit 2: The average leverage for the offshore subsidiaries of the three brokers in our coverage is 11x, compared to the group average leverage of 6x As of 2025  
![](images/334cc23289c2ff21957c8ddc63d0728d3ac1caba8701ea4251dcff8e52af622b.jpg)

<details>
<summary>bar chart</summary>

| Category | Offshore | Onshore | Group |
|---|---|---|---|
| CICC | 7.6 | 6.0 | 6.4 |
| CITICS | 16.6 | 5.5 | 6.5 |
| GFS | 9.9 | 6.0 | 6.2 |
</details>

Source: Company data, GS Global Investment Research

Exhibit 3: The average ROE for the offshore subsidiaries of the three brokers in our coverage is 16%, compared to the group average leverage of 9%
As of 2025  
![](images/c881c5fd45c17fc86de7220df0791d4eb67cc9d16773d447bd5224708af89219.jpg)

<details>
<summary>bar chart</summary>

| Category | Offshore (%) | Onshore (%) | Group (%) |
| :--- | :--- | :--- | :--- |
| CICC | 15 | 5 | 8 |
| CITICS | 22 | 8 | 10 |
| GFS | 11 | 10 | 10 |
</details>

Source: Company data, GS Global Investment Research

The strength of the Hong Kong IPO cycle further reinforces this thesis. GS strategists believe the IPO market has experienced a notable resurgence, with strong issuance volumes and robust post-listing performance, with newly listed companies since 2025 having generated average returns of approximately $40\%$ in the first month, albeit with significant dispersion. This backdrop supports a favorable operating environment for brokers' core businesses, including underwriting, advisory, and trading. In particular, leading brokers have cited a current pipeline of over 180 IPO deals, highlighting both the depth and sustainability of the current cycle.

Exhibit 4: GS strategists note the IPO market experienced a notable resurgence in 2025 and expect it to further normalize to historical averages in 2026  
![](images/1c9cb280b7631d2f178613936804dc0afa660adee9a559eb4b505e4a34128117.jpg)

<details>
<summary>bar-line hybrid</summary>

| Year | IPO amount - HK (US$bn) | IPO amount - A shares (US$bn) | A+H IPOs as % of all China mkt cap (%) |
|---|---|---|---|
| 2009 | 51 | 21 | 1.0 |
| 2010 | 124 | 70 | 2.5 |
| 2011 | 60 | 40 | 1.5 |
| 2012 | 23 | 15 | 0.5 |
| 2013 | 16 | 8 | 0.3 |
| 2014 | 25 | 10 | 0.4 |
| 2015 | 54 | 22 | 0.5 |
| 2016 | 46 | 21 | 0.4 |
| 2017 | 50 | 33 | 0.4 |
| 2018 | 55 | 19 | 0.5 |
| 2019 | 73 | 43 | 0.6 |
| 2020 | 123 | 71 | 0.7 |
| 2021 | 128 | 84 | 0.7 |
| 2022 | 98 | 83 | 0.6 |
| 2023 | 55 | 49 | 0.5 |
| 2024 | 20 | 8 | 0.3 |
| 2025 | 56 | 18 | 0.4 |
| Ytd | 18 | 6 | 0.5 |
| 2026E | 18 | 100 | 0.6 |
As of March 31, 2026
Ytd: YTD: YTD
2026E: 
*Year-over-Year change: YTD
</details>

Source: Wind, Bloomberg, GS Global Investment Research

Exhibit 5: Investors participating in IPOs over the past two years could have achieved approximately 40% returns on average in the first month  
![](images/3fb3de361eee7e3afe48f437e23ec6e7eeaad9cbfaccbbb245673da99bdee8f8.jpg)

<details>
<summary>bar chart</summary>

Average post-IPO returns (in absolute terms for all HK Main Board IPOs)
| Period | 2019-23 (%) | 2024 (%) | 2025 (%) | 2026ytd (%) | 2025 (median) (%) | 2026ytd (median) (%) |
|---|---|---|---|---|---|---|
| T+1D | 10 | 10 | 34 | 34 | 10 | 13 |
| T+1W | 9 | 17 | 38 | 41 | 9 | 23 |
| T+1M | 11 | 19 | 45 | 34 | 9 | 20 |
| T+3M | 10 | 41 | 64 | - | - | 19 |
| T+6M | 3 | - | 72 | - | - | 13 |
As of March 31, 2026
</details>

Source: Wind, FactSet, GS Global Investment Research

The AI theme represents another pillar supporting the sector's outlook. Elevated market interest in AI and related industries has contributed to strong trading activity, with sector-wide ADTV forecast to increase meaningfully. Brokers benefit from this trend

through higher brokerage commissions, increased derivatives activity, and stronger demand for capital markets services. CICC management have indicated that as long as compelling investment themes such as AI persist, accompanied by a supportive interest rate environment, trading volumes are unlikely to see a material decline. This suggests that AI is not merely a short-term catalyst but should be an important driver of sustained market engagement.

However, it is important to distinguish between different sources of broker earnings growth. While participation in IPOs and STAR Board principal investments can boost reported earnings, these activities are inherently volatile and subject to valuation fluctuations and lock-up constraints. Historical experience indicates that such investments tend to increase earnings volatility without delivering a commensurate uplift in valuation multiples. As a result, we believe the market will place greater emphasis on structural drivers of ROE improvement—namely, leverage expansion and capital deployment into higher-return international businesses—rather than on episodic investment gains.

Exhibit 6: During the 2020-23 period, the investment income growth of our covered brokers ranged from a peak of $265\%$ to a trough of $-72\%$ YoY, with the valuation of H-shares for the brokers declining from a peak of 12x to a trough of 7x  
![](images/bf939f4f2f3f3df0e3644b5b8c9c76258d6a0329867549978d2556037c6a27ef.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Year | Investment Income Yoy(RHS) | Forward P/E(H) |
|------|-----------------------------|----------------|
| 2020 | 4                           | 100%           |
| 2021 | 6                           | 80%            |
| 2022 | 9                           | 130%           |
| 2023 | 5                           | 120%           |
| 2024 | 6                           | 50%            |
| 2025 | 18                          | 150%           |
</details>

Investment income growth and forward P/E both use the average of CICC, CITICS, GFS in our coverage

Exhibit 7: We therefore believe principal investment tends to exacerbate the volatility of brokers' earnings and not drive an uplift in their valuation multiples  
![](images/76cc58fad903dceee27eb44c8c42270862d9aeb36718cfcbf1d3bf2bbddae393.jpg)

<details>
<summary>line chart</summary>

| Quarter | CITICS | CICC | GFS |
|---------|--------|------|-----|
| 4Q19    | 0%     | 5%   | 0%  |
| 1Q20    | 0%     | 10%  | 0%  |
| 2Q20    | 0%     | 15%  | 0%  |
| 3Q20    | 0%     | 10%  | 0%  |
| 4Q20    | 0%     | 5%   | 0%  |
| 1Q21    | 0%     | -5%  | 0%  |
| 2Q21    | 5%     | 10%  | 0%  |
| 3Q21    | 0%     | -5%  | 0%  |
| 4Q21    | 0%     | -5%  | 0%  |
| 1Q22    | -5%    | -25% | 0%  |
| 2Q22    | -5%    | 0%   | 0%  |
| 3Q22    | 0%     | -5%  | 0%  |
| 4Q22    | 0%     | 5%   | 0%  |
| 1Q23    | 5%     | 15%  | 0%  |
| 2Q23    | 0%     | -5%  | 0%  |
| 3Q23    | -5%    | -10% | 0%  |
| 4Q23    | -5%    | -5%  | 0%  |
| 1Q24    | -5%    | -25% | 0%  |
| 2Q24    | -5%    | -5%  | 0%  |
| 3Q24    | 5%     | 30%  | 0%  |
| 4Q24    | 0%     | 20%  | 0%  |
</details>

Source: Company data, GS Global Investment Research, Wind

Source: Company data, Wind

Against this backdrop, we reiterate our preference for CICC-H and CITICS-A as our top broker picks. Both companies offer clear exposure to the key themes outlined above. CICC stands out for its leading position in the Hong Kong IPO market, its significant contribution from international operations, and a well-articulated strategy to drive ROE expansion through capital reallocation and potential M&A. CITICS, meanwhile, is actively raising capital to expand its international footprint, with a clear plan to increase the contribution of offshore business to overall equity and earnings while creating additional headroom for leverage optimization. These characteristics make both names well positioned to benefit from the confluence of IPO cycle strength and structural ROE improvement.

Exhibit 8: CICC's offshore business contributes the most to both revenue and profit, at over $40\%$ , the highest among Chinese brokers As of 2025  
![](images/e384da21af21fc093c84ea48169edd182a702517c356373190229084aac19530.jpg)

<details>
<summary>bar chart</summary>

International business contribution (2025)
| Category | CICC (%) | CITICS (%) | GFS (%) |
| :--- | :--- | :--- | :--- |
| Total asset | 30 | 23 | 11 |
| Total equity | 26 | 9 | 7 |
| Revenue | 48 | 31 | 6 |
| Net income | 47 | 21 | 8 |
</details>

Source: Company data

Exhibit 9: Following CITICS' Rmb 16bn refinancing, we calculate the leverage of its international business will decrease from 16.6x to 10.6x, creating greater room for expansion  
![](images/9f64b94b9e3bebd8311397d3958d55098e6cbfeb890a84f9e52aa1c1f918dc6f.jpg)

<details>
<summary>bar chart</summary>

| Category | 2025 (x) | Post refinancing (x) |
| :--- | :--- | :--- |
| CITICS leverage | 6.4 | 6.1 |
| CITICS International leverage | 16.6 | 10.6 |
</details>

Source: Company data, GS Global Investment Research

Lastly, we note that online brokers such as FUTU also stand to benefit from the current capital market environment, particularly through increased retail participation and AUM growth. However, regulatory developments related to cross-border capital flows and the normalization of mainland client activity introduce near-term uncertainty. While regulatory clarity is improving and the long-term wealth management opportunity remains intact, we believe these headwinds limit the stock's risk-reward relative to traditional brokers with stronger institutional franchises and are Neutral on FUTU.

Exhibit 10: Valuation Summary  
price as of June 15

<table><tr><td rowspan="2">Name</td><td rowspan="2">Ticker</td><td rowspan="2">Price (Local currency)</td><td rowspan="2">Rating</td><td rowspan="2">Valuation method</td><td rowspan="2">Target multiple</td><td rowspan="2">Target price (Local currency)</td><td rowspan="2">Upside (%)</td><td colspan="2">Net profit growth</td><td colspan="2">Trading PE</td><td colspan="2">Trading PB</td><td colspan="2">Implied PE</td><td colspan="2">Implied PB</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="18">Covered companies</td></tr><tr><td colspan="18">Brokers (A)</td></tr><tr><td>CICC-A</td><td>601995.SS</td><td>33.68</td><td>Neutral</td><td>12m PE</td><td>18.0x</td><td>45.72</td><td>36%</td><td>24%</td><td>1%</td><td>13.4x</td><td>13.3x</td><td>1.1x</td><td>1.1x</td><td>18.2x</td><td>18.0x</td><td>1.6x</td><td>1.4x</td></tr><tr><td>CITICS-A</td><td>600030.SS</td><td>26.86</td><td>Buy</td><td>12m PE</td><td>16.0x</td><td>39.96</td><td>49%</td><td>23%</td><td>0%</td><td>10.8x</td><td>10.8x</td><td>1.1x</td><td>1.0x</td><td>16.0x</td><td>16.0x</td><td>1.7x</td><td>1.5x</td></tr><tr><td>GFS-A</td><td>000776.SZ</td><td>20.83</td><td>Buy</td><td>12m PE</td><td>14.0x</td><td>32.09</td><td>54%</td><td>37%</td><td>-5%</td><td>8.7x</td><td>9.1x</td><td>0.9x</td><td>0.8x</td><td>13.4x</td><td>14.0x</td><td>1.3x</td><td>1.2x</td></tr><tr><td colspan="18">Brokers (H)</td></tr><tr><td>CICC-H</td><td>3908.HK</td><td>20.80</td><td>Buy</td><td>12m PE</td><td>11.0x</td><td>30.45</td><td>46%</td><td>24%</td><td>1%</td><td>7.6x</td><td>7.5x</td><td>0.6x</td><td>0.6x</td><td>11.1x</td><td>11.0x</td><td>0.9x</td><td>0.9x</td></tr><tr><td>CITICS-H</td><td>6030.HK</td><td>27.18</td><td>Neutral</td><td>12m PE</td><td>11.0x</td><td>29.95</td><td>10%</td><td>23%</td><td>0%</td><td>10.0x</td><td>10.0x</td><td>1.0x</td><td>1.0x</td><td>11.0x</td><td>11.0x</td><td>1.1x</td><td>1.1x</td></tr><tr><td>GFS-H</td><td>1776.HK</td><td>16.91</td><td>Neutral</td><td>12m PE</td><td>8.0x</td><td>19.99</td><td>18%</td><td>37%</td><td>-5%</td><td>6.5x</td><td>6.8x</td><td>0.6x</td><td>0.6x</td><td>7.6x</td><td>8.0x</td><td>0.8x</td><td>0.7x</td></tr><tr><td colspan="18">Fintech</td></tr><tr><td>Futu</td><td>FUTU</td><td>97.54</td><td>Neutral</td><td>12m PE</td><td>11.0x</td><td>118.19</td><td>21%</td><td>-18%</td><td>25%</td><td>11.4x</td><td>9.1x</td><td>2.1x</td><td>1.7x</td><td>13.9x</td><td>11.1x</td><td>2.6x</td><td>2.1x</td></tr></table>

Source: FactSet, Company data, GS Global Investment Research

The authors would like to thank Zihan Wang for her contribution to this report.

## Price Target Risks and Methodology - China International Capital Corp.

We are Buy/Neutral on CICC-H/CICC-A. Our 12-month target prices of HK\$ 30.45/Rmb 45.72 are based on 11x/18x 2027E P/Es.

Downside risks: 1) weaker-than-expected China capital market, 2) OTC derivative losses, 3) decreased AUM and fee rate, 4) higher cost income ratio.

Upside risks for A shares: 1) improving brokerage fee and IBD income, 2) increasing OTC derivative business and income growth, 3) more cost savings to support ROE.

## Price Target Risks and Methodology - CITIC Co.

We are Buy/Neutral on CITICS A/H. Our 12-month target prices of Rmb 39.96/HK\$ 29.95 are based on 16x/11x 2027E P/Es.

Downside Risks: 1) further slower revenue growth on weaker capital market, 2) decreasing AUM and take rate of asset management business, 3) slower growth of investment income, 4) more operating expense to keep cost income ratio high.

Upside risks for H share: 1) improving capital market and higher ADTV to drive core business growth, 2) further greater than expected cost savings.

## Price Target Risks and Methodology - GFS Co.

We are Buy/Neutral on GFS-A/H. Our 12-month target prices of Rmb 32.09/HK\$ 19.99 are based on 14x/8x 2027E P/Es.

Upside risks: 1) improving brokerage fees and IBD income, 2) increasing asset management AUM, 3) more cost savings to support ROE.

Downside risks: 1) weaker-than-expected China capital market, 2) a decrease in AUM and fee rate, 3) higher cost-to-income ratio.

## Price Target Risks and Methodology - FUTU Holdings

We are Neutral-rated on FUTU with a 12-month TP of US\$ 118.19, based on a 12m forward 2027E P/E of 11x.

Upside/Downside risks: 1) Lower-/greater-than-expected regulatory impact, 2) Stronger-/weaker-than-expected capital market performance, 3) an optimized cost structure in new markets, 4) challenges in new market expansion.

## Disclosure Appendix

## Reg AC

We, Shuo Yang, Ph.D. and Claire Ouyang, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shuo Yang, Ph.D. GS (Asia) L.L.C., Claire Ouyang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal ye

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
