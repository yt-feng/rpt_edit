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

Importers also helped, but primarily on a relative basis. While Importers were not immune to the broader selloff, they outperformed Exporters du

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
