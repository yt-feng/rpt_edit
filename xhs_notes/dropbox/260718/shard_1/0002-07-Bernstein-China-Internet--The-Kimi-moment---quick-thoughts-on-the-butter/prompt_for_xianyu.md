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
China Internet

# China Internet: The Kimi moment - quick thoughts on the butterfly effects

![](images/da993742bb55b4123674f43098b09997a34214a5ffd830bedf324c6996b527d1.jpg)

Robin Zhu

+852 2123 2659

robin.zhu@bernsteinsg.com

![](images/247b61460fc0ef82811897bec6ba08f733a1b504a53f28189f06f4e5d4482f3d.jpg)

Charles Gou

+852 2123 2618

charles.gou@bernsteinsg.com

![](images/180e84db997d72852f819907f6972a617b6fac2e68d826ae8c0fdabb17948a60.jpg)

Min-Joo Kang

+852 2123 2644

![](images/0db5d152d0c547595eb916ad2b11c2cb05969810b3d583841aa8208b131a7a44.jpg)

minjoo.kang@bernsteinsg.com

Hyrum Caesar

+81 3 6777 6979

hyrum.caesar@bernsteinsg.com

Kimi K3 a home run. On Thursday Asia time, Kimi released K3 with 2.8tn total parameters, and 16 active out of 896 total experts per token. The K3 model card claims performance close to Claude Fable 5 and GPT-5.6, while the early public benchmark results have pointed to performance beating one or both in specific tasks (e.g. front-end code). Both online reactions and our own initial use of the model have pointed to impressive reasoning and asset generation capabilities. In-line with our many discussions with Kimi over time, K3 demonstrated a clear emphasis on the aesthetics of deliverables.

Scale is all you need? After DeepSeek V3, and GLM-5.2 earlier this year, K3 represented another instance where the ability of China's top AI labs to keep pace with the US frontier has surprised global investors. Priced at \$3 and \$15 per million input and output tokens (and the customary 90% discount on cache hits), K3 is 40% cheaper than Opus 4.8, and 70% cheaper than Fable. At a high level, K3 feels confirmatory of our views that (1) AI SOTA continues to evolve rapidly; and (2) China AI can continue to keep pace with global SOTA, and take some share over time. But the immediate market reactions to K3 (e.g. China AI labs down, semis down) generally feel sensible.

China open source vs. Anthropic. Mythos was announced in early April, which means the K3 launch (together with GLM-5.2, which came out four months after Opus 4.6) adds weight to the idea of a 3-4 month gap between US and China AI SOTA. Convergence of reasoning capabilities at the frontier is directionally negative for AI model lab terminal margins, and it feels notable that OpenAI and Anthropic have started to engage in a price (rate limit) war of sorts in the last couple of weeks. Looking ahead, it wouldn't surprise us if K3 kicks Anthropic's regulatory-capture-as-a-strategy campaign into overdrive. Online comparisons with the US ban against BYD operating Stateside strike us as... plausible.

Competition among the China labs. We've long considered Kimi and Z.ai (along with Alibaba's Qwen) frontier in China. But Kimi is, at least for now, the clear leader on pre-train scale. The onus will now be on Z.ai to bring its own trillion-parameter model to market. We doubt Dr. Tang at Z.ai meant Kimi when he argued on Twitter/X (in response to Elon Musk) that a Chinese Mythos-class model will come sooner than Q1 2027. Note too the fact K3 is priced at double GLM-5.2 levels means both can remain at the Pareto frontier for model performance by price point (arena.ai currently confirms this for WebDev). "The world is a big place" should continue to apply for both, as far as ARR growth is concerned.

The (mostly indirect) implications for our large cap coverage. Alibaba acquired 36% of Kimi during a Feb 2024 funding round, while Tencent is also a known investor. Beyond equity investment value, which markets have a habit of looking past, greater model layer fragmentation and competition helps give more influence and bargaining power to the large distribution platforms... and users of Al. On the margin, Kimi success is probably a positive for Alicloud revenue growth. The fact Tencent's Workbuddy reportedly now has 8-9mn monthly visits - as the leading desktop agentic harness application in China - feels notable to us as something investors have mostly ignored.

Rearranging our ranking of China SOTA. K3 helps Kimi leapfrog Z.ai as (at least for now) the leading AI lab in China, by virtue of having the model with both the largest pre-training scale, and highest scores on a range of benchmarks we think are instructive (e.g. DeepSWE v1.1, Terminal-Bench v2.1). Alibaba's Qwen rounds out the top three for us, followed by DeepSeek (largely on account of six months lost to helping domestic chip suppliers on hardware compatibility. Z.ai's next pre-train and Alibaba's Apsara cloud conference are probably now the upcoming catalysts to watch in China AI.

One for the distillation debate. Anthropic recently added Z.ai to its list of China AI labs it's accused of illicit distillation attempts. Our base case remains that everyone distills everyone in the industry. Distillation mainly helps to bootstrap post-training (e.g. supervised fine-tuning) rather than determine pre-training scale which Kimi argues - and we agree - is the far greater challenge. Entertainingly, Thinking Machines' debut model Inkling was a rather lukewarm effort where the model documentation indicated use of data generated by Kimi K2.5. Maybe it's only distillation when Anthropic is the purported victim, otherwise it's just sparkling post-training bootstrap.

## INVESTMENT IMPLICATIONS

The Kimi K3 launch is directionally additive to our view that the top China AI labs can continue to keep pace with US peers, and become a force globally. The implications for our large cap stock coverage is mostly indirect in nature, but note Alibaba has a large ownership stake in Kimi.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="2">16 Jul 2026</td><td rowspan="2">Price Target</td><td rowspan="2">TTM Rel. Perf.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>700.HK (Tencent)</td><td>O</td><td>HKD</td><td>484.00</td><td>780.00</td><td>(38.5)%</td><td>CNY</td><td>28.09</td><td>30.00</td><td>34.91</td><td>14.9</td><td>13.9</td><td>12.0</td></tr><tr><td>BABA (Alibaba )</td><td>O</td><td>USD</td><td>117.49</td><td>180.00</td><td>(18.8)%</td><td>CNY</td><td>65.41</td><td>26.82</td><td>46.57</td><td>12.2</td><td>29.7</td><td>17.1</td></tr><tr><td>9988.HK (Alibaba)</td><td>O</td><td>HKD</td><td>116.90</td><td>176.00</td><td>(28.2)%</td><td>HKD</td><td>8.82</td><td>3.69</td><td>6.68</td><td>11.4</td><td>27.4</td><td>15.1</td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,921.27</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,533.77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

## Tencent Holdings Ltd

We value Tencent at HK\$780 per share, on a 20x FY+1 (i.e. Quarters 5-8) PE multiple.

## Alibaba Group Holding Ltd

We value Alibaba at US\$180/HK\$176 per share, based on our SOTP valuation for FY+1 revenues and profits in its core e-commerce and Cloud businesses.

## RISKS

## Tencent Holdings Ltd

The main downside risks associated with Tencent include macroeconomic risks (e.g. credit, retail consumption), fluctuations in user engagement with its platforms, gaming and advertising demand competition with rival internet platforms, and regulatory risks – for example related to China's anti-monopoly regulations.

## Alibaba Group Holding Ltd

The main downside risks associated with our price target for Alibaba include macroeconomic risks (e.g. credit, retail consumption), fluctuations in user engagement with Taobao, Tmall, and other platforms, competition with rival internet platforms, regulatory risks – for example related to China's anti-monopoly regulations, and losses in the company's innovation initiatives & others segment.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

\- Outperform: Stock will outpace the market index by more than 15 pp

• Market-Perform: Stock will perform in line with the market index to within +/-15 pp

• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 600 Financials Price Return Index (E600BK) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 600 Insurance Price Return Index (E600IN) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

\- Outperform (OP): Stock will outpace the relevant index by more than 10 pp

\- Neutral (N): Stock will perform in line with the market index to within +/-10 pp

\- Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

\- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

\- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

\- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.2%</td><td>15.3%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>35.8%</td><td>16.2%

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
