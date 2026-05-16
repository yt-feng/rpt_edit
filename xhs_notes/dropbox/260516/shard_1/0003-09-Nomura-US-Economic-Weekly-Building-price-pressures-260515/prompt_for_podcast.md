你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

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
