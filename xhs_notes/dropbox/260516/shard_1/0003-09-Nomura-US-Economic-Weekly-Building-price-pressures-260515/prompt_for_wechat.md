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
# US Economic Weekly

Economics - North America

# Building price pressures

- Inflation data released this week were broadly hawkish, pointing to signs of building price pressures. We have revised up our core PCE tracking estimate to 0.300% m-o-m, which translates to 3.3% y-o-y, significantly above the Fed's target.   
- Fedspeak this week continued to show waning support for an easing bias. We expect the April FOMC minutes will show “many” participants either directly advocating a shift to more neutral guidance or at least indicating they could have supported an adjustment.   
- Retail sales were strong in April despite headwinds from the Iran war. We believe steady consumption and strong business investment will to lead to an acceleration in real GDP growth in Q2.

# April inflation data boosted by technical factors

Core CPI inflation surprised to the upside, rising by $0.376\%$ m-o-m in April (NOM: $0.287\%$ , Consensus: $0.3\%$ ). Our forecast miss was primarily attributable to stronger rent-related components, as well as to airline fares. As we had expected, regular rent and owners' equivalent rent (OER) inflation were boosted by the positive payback of the BLS's carry-forward imputation last fall, but there was also some unexpected incremental strength as well. Stripping out those components, the underlying inflation trend does not appear to have changed materially.

PPI's portfolio management and investment advice prices, a key input into core PCE inflation, declined more than we had expected. Taking CPI, PPI, and import prices into account, our forecast for April core PCE inflation was revised to $0.300\%$ m-o-m (or $3.3\%$ y-o-y) (Fig. 1 & Fig. 2), slightly up from our forecast of $0.284\%$ m-o-m at the beginning of this week.

Fig. 1: Core PCE inflation likely remained elevated at 0.300% m-o-m in April   
Decomposition of m-o-m core PCE inflation by data source   
![](images/52552f26e3969844c65e28c5d54e6e3b41111deacba2106365361c444ac2302d.jpg)

<details>
<summary>bar_line</summary>

| Date    | Other components | Contributions from components that are covered by PPI | Contributions from components that are covered by CPI | Core PCE inflation |
|---------|------------------|--------------------------------------------------------|--------------------------------------------------------|--------------------|
| Jan-23  | 0.0              | 0.0                                                    | 0.3                                                    | 0.4                |
| Jul-23  | 0.0              | 0.0                                                    | 0.2                                                    | 0.3                |
| Jan-24  | 0.0              | 0.1                                                    | 0.2                                                    | 0.5                |
| Jul-24  | 0.0              | 0.1                                                    | 0.1                                                    | 0.2                |
| Jan-25  | 0.0              | 0.1                                                    | 0.2                                                    | 0.4                |
| Jul-25  | 0.0              | 0.1                                                    | 0.1                                                    | 0.3                |
| Jan-26  | 0.0              | 0.1                                                    | 0.2                                                    | 0.4                |
</details>

Source: BLS, BEA, Haver, NOM

# Research Analysts

# North America Economics

Aichi Amemiya - NSI

aichi.amemiya@NOM.com

+1 212 667 9347

Jeremy Schwartz - NSI

jeremy.schwartz@NOM.com

+1 212 667 9637

Ruchir Sharma - NSI

ruchir.sharma@NOM.com

+1 212 667 9186

Jacklyn Goloborodsky - NSI

jacklyn.goloborodsky@NOM.com

+1 212 298 4739

# Global Economics

David Seif - NSI

david.seif@NOM.com

+1 212 667 9180

Fig. 2: Y-o-y core PCE inflation likely rose by 3.3% in April   
![](images/2626758e214a9b6b9c6fa247ffa00f9646b5f99dbd136f5f9957097dd9c6cc79.jpg)

<details>
<summary>line</summary>

| Date   | Core PCE Inflation (y-o-y) | 3m annualized | 6m annualized |
|--------|-----------------------------|---------------|---------------|
| Jan-21 | ~1.8%                       | ~3.0%         | ~2.5%         |
| Jan-22 | ~5.5%                       | ~6.5%         | ~6.0%         |
| Jan-23 | ~4.5%                       | ~5.5%         | ~5.0%         |
| Jan-24 | ~3.0%                       | ~1.8%         | ~2.0%         |
| Jan-25 | ~2.8%                       | ~3.0%         | ~2.8%         |
| Jan-26 | ~3.2%                       | ~4.5%         | ~4.0%         |
</details>

Note: All NOM forecasts are modal.   
Source: BEA, Haver, NOM

While the drivers of elevated inflation in April are likely to prove temporary, details of CPI, PPI, and import prices confirmed growing upside risks to the medium-term inflation outlook.

Tech-related components are emerging as a new source of inflation, offsetting some slowdown in tariff-sensitive consumer goods. CPI's information technology commodities, including computers and computer software, continued to rise in April. A further rise in semiconductor prices measured by PPI indicates a growing pipeline of inflationary pressures on consumers' electronics (Fig. 3).

Spillovers from energy shocks caused by the Iran war appear to be materializing. PPI's price index for rubber and plastic products jumped in April. PPI's truck transportation prices rose at their fastest pace in the series' two-decade history, driven by higher fuel costs as well as limited capacity in the truck industry.

On an aggregate basis, PPI data show cost pressures on domestic manufacturers kept intensifying (Fig. 4) as prices for processed materials and components prices for manufacturing registered a 2.0% m-o-m increase in April, following 1.0% and 1.1% advances in the two price months. These price increases are consistent with the recent strengthening of prices paid indices in regional and nationwide factory surveys. PPI's prices for finished consumer goods suggest these cost increases are beginning to be passed on to customers after several months of margin pressure.

Fig. 3: Prices for tech-related components have risen sharply across various measures   
![](images/6189483a26e234ecc35a64851ad14e70ff30f3787cc695288893669f795a6ed6.jpg)

<details>
<summary>line</summary>

| Year | CPI: Computers, Peripherals, and Smart Home Assistant Devices (LHS) | Import prices: semiconductors (LHS) | PPI: Semiconductor & Oth Electronic Component Mfg (RHS) |
|------|------------------------------------------------------------------------|--------------------------------------|-----------------------------------------------------|
| 16   | -8.0%                                                                  | -3.0%                                | -1.0                                                |
| 17   | -5.0%                                                                  | -2.0%                                | -0.5                                                |
| 18   | -4.0%                                                                  | 1.0%                                 | 0.0                                                 |
| 19   | -3.0%                                                                  | -1.0%                                | -1.5                                                |
| 20   | -2.0%                                                                  | -5.0%                                | -2.0                                                |
| 21   | 0.0%                                                                   | 0.0%                                 | 0.0                                                 |
| 22   | 8.0%                                                                   | 8.0%                                 | 5.0                                                 |
| 23   | -5.0%                                                                  | 5.0%                                 | 0.0                                                 |
| 24   | -6.0%                                                                  | -3.0%                                | -1.0                                                |
| 25   | -7.0%                                                                  | -5.0%                                | -2.0                                                |
| 26   | 2.0%                                                                   | 10.0%                                | 25.0                                                |
</details>

Source: BLS, Haver, NOM

Fig. 4: Certain materials and components for manufacturers continued to rise strongly on a y-o-y basis   
![](images/a54834cc237133a963cf2fceab710cdef94293995398753ba98edc4963c24193.jpg)

<details>
<summary>line</summary>

| Date   | PPI: Electronic Components & Accessories | PPI: Electrical Machinery & Equipment | PPI: Nonferrous Metals | PPI: Rubber & Plastic Products | PPI: Truck Transportation |
|--------|------------------------------------------|--------------------------------------|------------------------|-------------------------------|---------------------------|
| Jan-18 | -5                                       | 0                                    | 12                     | 3                             | 5                         |
| Jan-20 | -2                                       | 0                                    | 0                      | 0                             | 0                         |
| Jan-22 | 5                                        | 8                                    | 35                     | 20                            | 25                        |
| Jan-24 | 0                                        | 0                                    | -5                     | -5                            | -5                        |
| Jan-26 | 28                                       | 10                                   | 40                     | 0                             | 15                        |
</details>

Source: BLS, Haver, NOM

Services inflation also appear to be picking up. PCE price components that are derived from PPI data will likely accelerate in the months following April. We expect portfolio management and investment advice prices to rebound in May given the recent strong performance of stock prices (Fig. 5). Airline fares in both CPI and PPI are likely to continue to rise in the next few months on the back of higher jet fuel prices (Fig. 6).

Fig. 5: We expect portfolio management and investment advice prices to rebound in May given the recent strong performance of stock prices   
Stock prices and PPI'a portfolio management and investment advice prices   
![](images/e6b2691c246ba6ba94381dfb95de242cc6119732dc22ac95dab4f59f5bc124fb.jpg)

<details>
<summary>line</summary>

| Date   | PPI: Portfolio Management and Investment Advice | S&P500 stock price index (1-mon lead) |
|--------|--------------------------------------------------|--------------------------------------|
| Jan-23 | ~2.5                                             | ~0.0                                 |
| Aug-23 | ~4.0                                             | ~4.5                                 |
| Mar-24 | ~6.0                                             | ~4.0                                 |
| Oct-24 | ~2.0                                             | ~3.0                                 |
| May-25 | ~7.0                                             | ~8.0                                 |
| Dec-25 | ~1.0                                             | ~4.5                                 |
</details>

Source: BLS, Haver, NOM

Fig. 6: Jet fuel prices have risen lately, and this could push airline fares higher in the coming months   
![](images/665e444b05d2dea745ee7765f273f9d00021c380d877238059fff2dd928c67c8.jpg)

<details>
<summary>line</summary>

| Year | CPI airline fares (LHS) | Kerosene-Type Jet Fuel prices (RHS) |
|------|--------------------------|-------------------------------------|
| 11   | ~5                       | ~15                                 |
| 14   | ~0                       | ~-10                                |
| 17   | ~5                       | ~20                                 |
| 20   | ~-30                     | ~-60                                |
| 23   | ~45                      | ~80                                 |
| 26   | ~10                      | ~90                                 |
</details>

Source: BLS, EIA, Haver, NOM

# Developments on the FOMC

Kevin Warsh was confirmed as the next Fed chair in a 54-45 Senate vote, representing the slimmest Senate support for a Fed chair in history (Fig. 7).

Fedspeak this week was consistently hawkish. Boston Fed President Collins leaned hawkish, emphasizing the persistence of inflation and stating that more than five years of above-target inflation had reduced her patience for looking through another supply shock. She stressed the importance of returning inflation to target in a reasonable amount of time. KC Fed president Schmid also cited inflation as the "most pressing risk to the economy." Governor Barr also echoed the hawkish sentiment in his remarks, stating that inflation is an "overwhelming risk." NY Fed President Williams referred to supply chain disruptions as the New York Fed's Global Supply Chain Pressure Index started to rise.

This hawkish lean may be reflected in the April FOMC meeting minutes scheduled for release next week. We expect the minutes will show “many” participants either directly advocating a shift to more neutral guidance or at least indicating they could have supported an adjustment. Three voters dissented against the easing bias (presidents Hammack, Logan, and Kashkari), and two additional non-voting officials (Collins and Musalem) have sUBSequently indicated they would have preferred to change the guidance. The minutes first showed this discussion in January, with “several” participants advocating for a change. This sUBSequently increased to “some” in the March minutes.

The NY Fed released its T-bill purchase schedule for May and June. The pace of reserve management purchases (RMP) will slow to \$10bn per month, from \$25bn previously. This was well below both our forecast and the primary dealer survey median of \$20bn (Fig. 8). Note, the Fed initially announced RMPs last year at a pace of \$40bn per month, before slowing to \$25bn in April and May.

We continue to expect trend balance sheet growth of \$20bn per month in the medium term. However, this reduction suggests the NY Fed may allow purchases to undershoot temporarily during periods of softer seasonal demand.

Fig. 7: Warsh's confirmation represents the Senate's slimmest support for a Fed chair   
US Senate confirmation for Fed Chair 

<table><tr><td>Year</td><td>Nominee</td><td>Yes</td><td>No</td></tr><tr><td>1979</td><td>Paul Volcker</td><td>98</td><td>0</td></tr><tr><td>1983</td><td>Paul Volcker</td><td>84</td><td>16</td></tr><tr><td>1987</td><td>Alan Greenspan</td><td>91</td><td>2</td></tr><tr><td>1992</td><td>Alan Greenspan</td><td colspan="2">Unanimous</td></tr><tr><td>1996</td><td>Alan Greenspan</td><td>91</td><td>7</td></tr><tr><td>2000</td><td>Alan Greenspan</td><td>89</td><td>4</td></tr><tr><td>2006</td><td>Ben Bernanke</td><td colspan="2">Unanimous</td></tr><tr><td>2010</td><td>Ben Bernanke</td><td>70</td><td>30</td></tr><tr><td>2014</td><td>Janet Yellen</td><td>56</td><td>26</td></tr><tr><td>2018</td><td>Jerome Powell</td><td>84</td><td>3</td></tr><tr><td>2022</td><td>Jerome Powell</td><td>80</td><td>19</td></tr><tr><td>2026</td><td>Kevin Warsh</td><td>54</td><td>45</td></tr></table>

Source: FRB, NOM

Fig. 8: The pace of RMPs will slow to \$10bn/month, from \$25bn previously below our and consensus forecast of \$20bn   
![](images/5c8f8d8678fd937191e7b05831bf0bde53c212e6fb931318e72b1ff78073ec14.jpg)

<details>
<summary>bar</summary>

| Month | Reserve Management purchases ($bn) | Reinvestment purchases ($bn) |
| :--- | :--- | :--- |
| Dec-Jan | 40 | 14.5 |
| Jan-Feb | 40 | 15.3 |
| Feb-Mar | 40 | 13.5 |
| Mar-April | 40 | 13.8 |
| Apr-May | 25 | 15.6 |
| May-June | 10 | 16.4 |
</details>

Source: NY Fed, NOM

# Data suggest resilience in domestic demand

Retail sales remained strong in April, with upward revisions to the control group in prior months. Strength was broad-based, suggesting that higher gasoline spending has not weighed on demand for other components thus far. It appears that higher-than-usual tax refunds, coupled with strong income growth, have more than offset headwinds from the Iran war.

We initiated our Q2 GDP tracking this week, and we expect growth accelerated in Q2 (Fig. 9). Our tracking estimate stands at 2.7% q-o-q ar. We expect real final sales to private domestic purchasers accelerated to 2.9% in Q2, driven by resilient personal consumption and continued strength in business capex.

Fig. 9: We expect real GDP growth to accelerate in Q2 due to robust fixed investment and steady personal consumption   
![](images/00c439c7e4de49ce37d11bc578508e02fc3987464c7ca2c1bf151149be748074.jpg)  
Source: BEA, Haver, NOM

Fig. 10: The administration has started to process tariff-refunds and issue payments to importers   
![](images/435235cea73dac3a8bbf8c5ce8107cdb9e1034bd1cb6e61583e40ba756690865.jpg)

<details>
<summary>line</summary>

| Date   | Daily cash withdrawals from Tsy: CBP ($bn) |
|--------|------------------------------------------|
| Jan-26 | 0.3                                      |
| Feb-26 | 0.1                                      |
| Mar-26 | 0.8                                      |
| Apr-26 | 0.5                                      |
| May-26 | 1.8                                      |
</details>

Source: US Treasury, Haver, NOM

# Tariff refunds

Media reports indicate the administration has processed \$35.5bn in tariff refunds for several importers, clearing the way for Treasury to issue payments. CBP-related withdrawals from the Treasury have picked up recently (Fig. 10), suggesting the process is moving swiftly.

Tariff refunds will provide an additional fiscal boost to businesses on top of the stimulus already in place from the OBBBA. The cash flow support could lift investment and hiring, or help firms absorb tariff- and energy-related cost pressures. On the other hand, faster refund issuance would likely widen the deficit in the current fisc

[中间内容因长度限制已省略]

ct of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

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

Copyright © 2026 NOM Securities International, Inc., US. All rights reserved.
"""
