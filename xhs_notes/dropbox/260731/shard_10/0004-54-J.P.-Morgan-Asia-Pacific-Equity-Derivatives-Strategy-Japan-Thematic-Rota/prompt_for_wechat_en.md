You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Asia Pacific Equity Derivatives Strategy

Japan Thematic Rotation Trades Amid Yen Reversal Risk; Diversify into Korea Buybacks Amid AI/Momentum Unwind

\- Japan Equity Hedges for a Potential USDJPY Reversal: With USDJPY approaching our house 4Q26 target of 164, August looks like a key window for episodic yen-strength risk. Rising JGB yields, fuelled by BoJ rate hike expectations and fiscal uncertainty, have brought renewed focus to GPIF's end-June holdings release on 7 August, which could reinforce speculation that policymakers are encouraging greater domestic demand for JGBs as part of a broader effort to stabilize the rates market. Against a backdrop of elevated foreign ownership and crowded exposure to exporters and AI-related sectors, a USDJPY reversal could drive meaningful equity rotation. Historically, Strong Yen (JPJBSYEN) and Importers (JPJBIMPO) have been the most effective baskets in orderly yen-appreciation episodes, with both gaining as investors rotate toward more domestic and defensive exposures; in faster de-risking episodes such as the August 2024 carry unwind or April 2025 "Liberation Day," equity beta tends to dominate. We therefore prefer zero-cost call spread collars on Strong Yen and Importers to express an orderly USDJPY decline through thematic basket upside. We also reiterate our prior diversification idea of using a TOPIX-over-Nikkei outperformance call contingent on lower USDJPY to capture yen-led sector rotation away from AI/exporter leadership. For an August 2024-style tail-risk unwind, a best-of put on Nikkei/TOPIX contingent on lower USDJPY is the cleaner hedge.

\- Diversify into Korea Buyback Basket during Market Volatility: We reiterate our preference for the Korea buyback basket (JPKRBUBK) as a more defensive way to diversify in a volatile environment while staying aligned with Korea Value Up efforts, with policy support building through the dividend tax cut and rising Value Up disclosures. Value Up is moving from signaling to execution, with shareholder return improvement through buybacks and treasury share cancellations. Investors can consider long Korea buyback basket or buying a call spread collar on the basket to take advantage of elevated volatility.

Figure 1: Strong Yen and Importers have worked best in orderly USDJPY declines, while in fast de-risking episodes their value has been mainly relative  
![](images/e0def3480bb9d23022b521a63731232ad6f44572f376588fcda33d5fc4095a42.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

Figure 2: The Korea buyback basket has shown resilience during the recent momentum unwind - hypothetical performance since July 2025  
![](images/044e7634b5b39f834c138182b88402c48b899106fc4f4ab144c535163c209e9e.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P. Basket was introduced on June 25, 2026. Past performance is not indicative of future returns.

## Global Equity Derivatives Strategy

Tony SK Lee AC
(852) 2800-8857
tony.sk.lee@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Haoshun Liu AC
(852) 2800-7736
haoshun.liu@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Xipu Han AC
(852) 2800-1029
xipu.han@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Twinkle Mehta, CFA AC
(852) 2800-7109
twinkle.mehta@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Davide Silvestrini
(44-20) 7134-4082
davide.silvestrini@JPM.com
JPM Securities plc

Bram Kaplan, CFA
(1-212) 272-1215
bram.kaplan@JPM.com
JPM Securities LLC

Yangyang Hou
(1-212) 834-6734
yangyang.hou@JPM.com
JPM Securities LLC

See page 22 for analyst certification and important disclosures.

# Japan Thematic Rotation Trades Amid Yen Reversal Risk

## Why Consider Stronger Yen Risks?

With USD/JPY approaching our house 4Q26 target of 164, we believe August represents an important risk window where the distribution of outcomes is skewed towards episodic yen strength rather than a continuation of recent depreciation.

The shift in focus is being driven more by developments in Japan's domestic rates market. Japanese government bond yields have continued to move higher as expectations for further Bank of Japan policy normalization have increased, while uncertainty surrounding the government's fiscal agenda (see here), including the potential cost of new growth initiatives and discussion around consumption tax reductions, has added further upward pressure on long-end yields. Against this backdrop, market attention has increasingly shifted from the authorities' ability to stabilize the currency towards policies aimed at containing the rise in government bond yields.

Figure 3: With USDJPY approaching our house 4Q26 target of 164, August looks like a key window for episodic yen-strength risk  
![](images/16a0433db40c1f7c955728ed5df7aa38649736f17215a996d3cecbd8181079c7.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

Figure 4: With JGB yields rising, market focus has shifted from currency stabilization to policies aimed at containing bond yields  
![](images/611ac2435f9ec799dea8406f19a8945e24a90bb918b96e9210995735a13542f5.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

This changing policy backdrop has also brought renewed focus to GPIF (see here and here). While the release of its end-June holdings on 7 August is not a strategic asset allocation review, investors are likely to scrutinize the data for evidence of continued increases in domestic bond holdings. Such an outcome would reinforce speculation that policymakers are encouraging greater domestic demand for JGBs as part of a broader effort to stabilize the rates market. In the most extreme scenario, our FX strategists estimate that a sustained reallocation towards domestic assets could strengthen the yen by as much as 15 yen against the US dollar (see here), although this represents a tail-risk scenario rather than our central expectation.

Figure 5: BoJ rate hike expectations have continued to fuel the rise in Japanese government bond yields  
![](images/c871f13c861551b8ae50aff84edcb6d2e4efdb124bf125bd712ee227111fd30c.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

Figure 6: Foreign net buying of Japanese equities this year leaves the market more vulnerable to seasonal profit-taking  
![](images/240c6cd766c1b004efbb4efcfafc9e471a92d077663ce115ed4a6bebdd52ea49.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

These macro developments come against a backdrop of elevated foreign ownership of Japanese equities and continued concentration in exporters and AI-related sectors. Although much of the seasonal momentum unwind occurred earlier than usual during the June and July correction, foreign investors remain meaningfully exposed to the Japanese market. A stronger yen would therefore likely coincide with further rotation within equities, particularly away from globally exposed exporters and towards domestically oriented companies.

The combination of renewed macro uncertainty and concentrated positioning naturally invites comparisons with the August 2024 carry unwind. We are not forecasting a repeat of that episode. Nevertheless, the combination of prolonged yen weakness, higher domestic yields and renewed policy speculation suggests that stronger-yen risks warrant closer attention over the coming weeks.

## FX-sensitive Thematic Baskets

To evaluate potential equity implementations around changes in USDJPY, we focus on four JPM thematic baskets together with index-level expressions. These baskets provide differentiated exposures to companies with varying degrees of sensitivity to exchange-rate movements and domestic versus overseas demand. Depending on market conditions, they can be used to express either stronger- or weaker-yen views. $^{1}$

Figure 7: Performance of JPM Japan FX-sensitive thematic baskets  
![](images/f58189651672f03f86d4d5c1004f5875621c90c08bd32fcd69c704314f1b8348.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P. Past performance is not indicative of future returns.

Table 1: Comparing Japan FX-Sensitive Thematic Baskets

<table><tr><td>Name Ticker</td><td>TOPIX TPX</td><td>Nikkei 225 NKY</td><td>Strong Yen JPJBSYEN</td><td>Weaker Yen JPJBWYEN</td><td>Importers JPJBIMPO</td><td>Exporters JPJBEXPO</td></tr><tr><td>Number of stocks</td><td>1636</td><td>225</td><td>27</td><td>32</td><td>15</td><td>57</td></tr><tr><td>Japan Revenue Exposure</td><td>58%</td><td>51%</td><td>94%</td><td>60%</td><td>78%</td><td>33%</td></tr><tr><td>Overseas Revenue Exposure</td><td>42%</td><td>49%</td><td>6%</td><td>40%</td><td>22%</td><td>67%</td></tr><tr><td>Correlation vs USDJPY</td><td>13%</td><td>5%</td><td>-14%</td><td>15%</td><td>1%</td><td>14%</td></tr><tr><td>Beta vs USDJPY</td><td>0.25</td><td>0.13</td><td>-0.21</td><td>0.41</td><td>0.02</td><td>0.45</td></tr><tr><td>YTD Return</td><td>16.7%</td><td>23.3%</td><td>5.8%</td><td>20.6%</td><td>5.9%</td><td>19.4%</td></tr><tr><td>3M Realized Volatility</td><td>20.8%</td><td>35.5%</td><td>18.5%</td><td>20.8%</td><td>15.7%</td><td>36.4%</td></tr><tr><td colspan="7">Largest Industry Group (Weight)</td></tr><tr><td>1</td><td>Elec Appl (20%)</td><td>Elec Appl (37%)</td><td>Rtl Trade (31%)</td><td>Machinery (18%)</td><td>Foods (37%)</td><td>Elec Appl (32%)</td></tr><tr><td>2</td><td>Banks (12%)</td><td>Rtl Trade (12%)</td><td>Foods (19%)</td><td>Elec Appl (17%)</td><td>Iron&amp;Steel (37%)</td><td>Trans Equip (14%)</td></tr><tr><td>3</td><td>Whsle Trd (8%)</td><td>Info &amp; Comm (11%)</td><td>Services (17%)</td><td>Whsle Trd (13%)</td><td>Pulp&amp;Paper (16%)</td><td>Machinery (13%)</td></tr><tr><td>4</td><td>Info &amp; Comm (6%)</td><td>Chemicals (4%)</td><td>Info &amp; Comm (15%)</td><td>Trans Equip (12%)</td><td>Rtl Trade (8%)</td><td>Chemicals (7%)</td></tr><tr><td>5</td><td>Machinery (6%)</td><td>Machinery (4%)</td><td>Whsle Trd (6%)</td><td>Insurance (12%)</td><td>Glass&amp;Ceram (3%)</td><td>Pharma (6%)</td></tr></table>

Data as of July 28, 2026.  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

## Strong Yen and Weak Yen

The Strong Yen (JPJBSYEN) and Weak Yen (JPJBWYEN) baskets are designed to capture companies whose earnings are expected to benefit from opposite currency regimes.

The Strong Yen basket consists of 27 stocks and has historically exhibited a negative correlation (-14%) and negative beta (-0.21) to USDJPY, making it the basket with the strongest inverse relationship to yen weakness among our thematic universes. The basket generated a 5.8% YTD return with 18.5% realised volatility over the past three months. Constituents are predominantly domestically oriented, with approximately 94% of revenues generated within Japan, and are concentrated in Retail Trade (31%), Foods (19%) and Services (17%).

By comparison, the Weak Yen basket contains 32 stocks and exhibits a positive correlation (15%) and beta (0.41) versus USDJPY, reflecting greater sensitivity to yen depreciation. The basket returned 20.6% YTD with 20.8% realised volatility. Its industry composition is tilted towards internationally exposed sectors, with Machinery (18%), Electrical Appliances (17%) and Wholesale Trade (13%) representing the

largest industry groups. The basket derives 60% of its revenue from Japan.

Relative-value strategies between Weak Yen vs Strong Yen also exhibit diversified industry exposures, with net overweight positions in Machinery (+17.5%) and Electrical Appliances (+16%), offset by a net underweight in Retail Trade (-24%).

Figure 8: Sector Net Weights: Weak Yen vs Strong Yen  
![](images/2ea396f2e0c38648ebce208e717a49b939e3aedd9d022a993a41bf3c24819269.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

Figure 9: Sector Net Weights: Exporters vs Importers  
![](images/9013e084cfb593bffb1aa4410905db58b11561659661fbd80e56c7f754ad6939.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

## Exporters and Importers

The Exporters (JPJBEXPO) and Importers (JPJBIMPO) baskets provide a more direct representation of companies that benefit from changes in Japan's external trade environment and are linked to shifts in market leadership during periods of currency appreciation or depreciation.

The Importers basket contains 15 stocks and is considerably more domestically oriented, with approximately 78% of revenues generated within Japan. The basket exhibits near-zero correlation and beta versus USDJPY. It has returned 5.9% YTD with 15.7% realised volatility, with the largest industry exposures in Foods (37%), Iron & Steel (37%) and Pulp & Paper (16%).

The Exporters basket comprises 57 stocks and exhibits a positive correlation (14%) and beta (0.45) versus USDJPY. It has returned 19.4% YTD with 36.4% realised volatility, reflecting its concentration in higher-beta manufacturing sectors. Only around 33% of revenues are generated domestically, with the basket heavily weighted towards Electrical Appliances (32%), Transportation Equipment (14%) and Machinery (13%), making it closely aligned with Japan's exporter and AI manufacturing complex.

Compared with the Weak Yen/Strong Yen framework, the Exporters/Importers baskets provide a stronger expression of equity rotation. Relative-value strategies between the two baskets carry a sizeable net overweight in Electrical Appliances (+35%) and net underweights in Foods (-34%) and Iron & Steel (-36%), making them particularly relevant when changes in USDJPY coincide with broader rotation away from exporter and AI leadership.

## Performance During Previous Yen Strength Episodes

Across prior episodes, Strong Yen and Importers have been the most useful equity baskets for hedging a more orderly decline in USDJPY. In those periods, both baskets gained, consistent with their defensive domestic orientation and lower reliance on yen weakness as an earnings tailwind. By contrast, when USDJPY declines coincided with fast de-risking, such as the August 2024 carry unwind or the April 2025 “Liberation Day” episode, absolute performance weakened across these equity baskets. In those environments, the main benefit came through relative resilience: Strong Yen outperformed Weak Yen, and Importers outperformed Exporters, even when absolute returns were negative.

Figure 10: We focus on major USDJPY drawdowns since 2024, as they capture the fast reversal and de-risking dynamics investors want to hedge  
![](images/aab3ad25bbf4ccb22a6152058353e5d610e55903c36406b2601822247c1ae3fd.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

Figure 11: During the August 2024 yen-strength episode, Importers and Strong Yen significantly outperformed Exporters, Weak Yen, and the broader market  
![](images/a445b5324ce62f4256e9fa925c1818390fcb2d6e650cdd6e45f6444958d1b37f.jpg)  
Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

## Fast de-risking episodes

Fast de-risking episodes are the most difficult environment for equity-based FX hedges. In these periods, yen appreciation typically reflects or reinforces broader risk reduction, deleveraging and position unwinds. As a result, equity market beta can dominate basket-level FX sensitivity.

The August 2024 carry unwind and April 2025 “Liberation Day” episode illustrate this dynamic. During these episodes, most baskets declined as yen strength coincided with broad equity weakness. Strong Yen was the key exception, and showing the most resilient absolute performance, providing the clearest equity hedge among the baskets. Strong Yen outperformed Weak Yen during these periods.

Importers also helped, but primarily on a relative basis. While Importers were not immune to the broader selloff, they outperformed Exporters during fast de-risking episodes. This relative resilience reflects the weaker yen sensitivity and more domestic cost/earnings profile of Importers, while Exporters were more exposed to the combined pressure of yen appreciation, global cyclicality and crowded positioning in manufacturing and AI-related sectors.

Table 2: Strong Yen and Importers would have worked best in orderly USDJPY declines, while in fast de-risking episodes their value would have been mainly relative—Strong Yen outperforming Weak Yen and Importers outperforming Exporters

<table><tr><td>Period</td><td colspan="2">Fast de-risking</td><td colspan="3">Orderly yen appreciation</td></tr><tr><td>Start</td><td>7/10/2024</td><td>3/27/2025</td><td>8/15/2024</td><td>11/14/2024</td><td>1/8/2025</td></tr><tr><td>End</td><td>8/5/2024</td><td>4/21/2025</td><td>9/16/2024</td><td>12/3/2024</td><td>3/10/2025</td></tr><tr><td>USDJPY</td><td>-10.8%</td><td>-6.7%</td><td>-5.8%</td><td>-4.3%</td><td>-7.0%</td></tr><tr><td>NKY</td><td>-24.8%</td><td>-9.3%</td><td>-0.4%</td><td>1.9%</td><td>-7.4%</td></tr><tr><td>TPX</td><td>-23.4%</td><td>-10.2%</td><td>-1.1%</td><td>1.9%</td><td>-2.5%</td></tr><tr><td>Strong Yen</td><td>-11.4%</td><td>6.8%</td><td>5.9%</td><td>6.4%</td><td>6.1%</td></tr><tr><td>Weak Yen</td><td>-33.1%</td><td>-12.8%</td><td>-2.2%</td><td>-1.6%</td><td>4.4%</td></tr><tr><td>Importers</td><td>-12.7%</td><td>-1.8%</td><td>1.9%</td><td>1.8%</td><td>2.2%</td></tr><tr><td>Exporters</td><td>-28.4%</td><td>-15.4%</td><td>-5.4%</td><td>1.1%</td><td>-9.4%</td></tr><tr><td>TPX vs NKY</td><td>1.4%</td><td>-0.9%</td><td>-0.7%</td><td>0.1%</td><td>4.9%</td></tr><tr><td>Strong Yen vs Weak Yen</td><td>21.8%</td><td>19.6%</td><td>8.2%</td><td>8.0%</td><td>1.6%</td></tr><tr><td>Importers vs Exporters</td><td>15.7%</td><td>13.6%</td><td>7.3%</td><td>0.7%</td><td>11.6%</td></tr></table>

Source: JPM Equity Derivatives Strategy, Bloomberg Finance L.P.

## Orderly yen appreciation

The performance profile was more constructive during orderly USDJPY declines, where yen appreciation occurred without a broad deleveraging shock.

This is the environment where Strong Yen and Importers have been most effective as outright hedges. Both baskets gained during orderly yen-strength episodes, making them useful tools for investors looking to protect against a controlled USDJPY decline rather than an abrupt risk-off unwind.

Strong Yen offers the cleaner FX hedge, in our view. Its negative sensitivity to USDJPY and concentration in more domestically oriented sectors make it well suited to a scenario where yen appreciation leads investors to rotate away from ex

[中间内容因长度限制已省略]

erial only and are therefore subject to change without

notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
