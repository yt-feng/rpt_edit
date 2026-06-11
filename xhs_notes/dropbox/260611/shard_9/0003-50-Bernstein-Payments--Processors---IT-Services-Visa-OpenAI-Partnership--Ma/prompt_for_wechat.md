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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Payments, Processors & IT Services

# Visa-OpenAI Partnership, Mastercard Agent Pay for Machines: Cards firmly enter the agentic era

![](images/f14a66977126eb0da5f5dc8ea73cb4d34f6e34c24202db6901387b749214ec60.jpg)

Harshita Rawat, CFA

+1 917 344 8485

harshita.rawat@bernsteinsg.com

![](images/f72ecaa4f6d2c619216e01af02f6e0afe2042b62504a2022d9f75255b87848cc.jpg)

Viola Chen

+1 917 344 8614

viola.chen@bernsteinsg.com

![](images/3a0e48cf35f80753684c1898376cd533242afa7f04d6622e6a470c8f5f831256.jpg)

Simran Ratani

+1 917 344 8329

simran.ratani@bernsteinsg.com

Visa today announced a partnership with OpenAI (link) to essentially enable agentic commerce, conversational agentic workflows and developer experiences through Visa Intelligent Commerce (including Visa agent tokens) and services. Visa and OpenAI are solving for two key focus areas 1) seamless agentic commerce experiences, 2) exploring future agentic economy use cases including developer-focused autonomous agent experiences powered by Codex, and conversational automated workflows. For anyone who has doubted Visa's (and cards') positioning in agentic commerce and machine-to-machine payments - we believe this partnership is a strong proof point that cards have firmly entered the agentic era of commerce. To be clear, we believe this is a 5yr opportunity (not a 2yr one) but it is critical to the multiple.

V (and MA) are networks of trust (and often misunderstood as backend money movement which settlement layers handle). Agents will (eventually) bring a paradigm shift in how we engage in commerce experiences, and simultaneously bring new economic models/payments (e.g., automated agent workflows). A massive trust infrastructure will be required to facilitate these commerce experiences - and cards are extremely well positioned.

OpenAI's comment in the release was quite noteworthy: “Commerce is going to happen in many more places and in many more ways than it does today, and agents will play an increasingly important role in helping people complete tasks that involve money—from purchases and payments to more complex transactions,” “By integrating with Visa Intelligent Commerce, we're building the infrastructure for secure, transparent, and user-controlled agentic transactions, helping people do more with AI agents while maintaining confidence that payments are being handled securely.”

The announcements today not only provide a big stamp of approval for agentic card tokens but also a proof point that value-added services' (VAS) growth opportunity will be enhanced with agentic (e.g., around authentication tokenization, risk, fraud). For example, Visa announced new services today — Agent Score (allows merchants to evaluate their websites for agentic commerce readiness), Agentic Directory (whether the merchant or agents are verified), and Large Transaction Model (for fraud detection).

Concurrently, with this announcement, Visa also announced enhancements to its tokens — bringing more data (e.g., on transaction type, where token is being used and who is making the payment), assurance (using token history to generate a signal of trust behind each transaction) and context — to enable agent-initiated transactions. Note that all these create monetization opportunities in the future.

It is likely that OpenAI announces a partnership around Mastercard AgentPay for agentic commerce, but unclear if it will include the future enterprise machine payment use-case. Separately, we note that Mastercard also introduced Agent Pay for Machines (AP4M) today, a new credentialed multi-rail service to enable permissioned machine payments. Partners include Adyen, Ant, Checkout, Coinbase, Lovable, Stripe, etc.

## Taking a step back, Agentic Commerce is often discussed as a potential risk for Visa/Mastercard. It's very much the opposite (more digitization, transactions, & VAS).

In the agentic world (where trust will be scarce), cards (with an array of services, 7B+ credentials, 100m+ merchants) will quite likely be the payment method of choice. Cards can also easily adjust their commercial models to accommodate autonomous agent transactions (including very small ticket transactions for compute, tokens, images). V/MA have done this historically to make transit and vending machine small-ticket transactions addressable. There is then the optionality with B2B where agentic commerce has the strongest product market fit.

We wonder if the news including the ones from today help the narrative around the networks transition from an ‘AI trade funding source trade’ to ‘AI winners’. We also note that several key overhangs are now somewhat behind us including CCCA (likelihood quite low vs. beginning of the year), the MDL settlement and Illinois card fee lawsuit. Also, good to remember that networks are excellent inflation hedges (and get paid on bps on gas spend).

## INVESTMENT IMPLICATIONS

We rate V, MA, TOST, Adyen, XYZ OP. We rate FISV, FIS, GPN, KLAR and PYPL MP.

## PLEASE SEE LINKS TO OUR PREVIOUS RELATED NOTES:

• Payments: Visa/Mastercard merchant settlement preliminary approval; A closure, finally? (June 2026)  
• The Long View: Payments - Does Cash Digitization Runway Still Exist? (June 2026)  
- Weekend Tech Byte: The 'cost' of cards — the often misleading comparisons; our perspectives in key charts (June 2026)  
• Visa: Reflections on our Fireside Chat with CEO Ryan McInerney (May 2026)  
- Payments: Stablecoins – What we learned from our dozens of industry conversations; Slide deck (May 2026)  
• The Age of Agents: Insights from our Inaugural Agentic Commerce Day (April 2026)  
• Visa, Mastercard: Payments-ocalypse, will Al doom the networks? (March 2026)  
• The Age of Agents: How does it change commerce and how we pay? (December 2025)

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">10 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>ADYEY (Adyen)</td><td>O</td><td>USD</td><td>9.14</td><td>18.63</td><td>(77.0)%</td><td>USD</td><td>0.39</td><td>0.50</td><td>0.60</td><td>23.3</td><td>18.2</td><td>15.3</td></tr><tr><td>ADYEN.NA (Adyen)</td><td>O</td><td>EUR</td><td>803.10</td><td>1,600.00</td><td>(65.9)%</td><td>EUR</td><td>33.62</td><td>42.83</td><td>51.05</td><td>23.9</td><td>18.8</td><td>15.7</td></tr><tr><td>XYZ (Block Inc)</td><td>O</td><td>USD</td><td>66.63</td><td>85.00</td><td>(19.7)%</td><td>USD</td><td>2,084</td><td>3,347</td><td>4,700</td><td>19.0</td><td>11.8</td><td>8.4</td></tr><tr><td>FIS (FIS)</td><td>M</td><td>USD</td><td>38.97</td><td>73.00</td><td>(74.9)%</td><td>USD</td><td>5.76</td><td>6.30</td><td>6.91</td><td>6.8</td><td>6.2</td><td>5.6</td></tr><tr><td>FISV(Fiserv)</td><td>M</td><td>USD</td><td>53.28</td><td>76.00</td><td>(91.4)%</td><td>USD</td><td>8.64</td><td>8.06</td><td>8.76</td><td>6.2</td><td>6.6</td><td>6.1</td></tr><tr><td>GPN (Global Payments)</td><td>M</td><td>USD</td><td>62.47</td><td>86.00</td><td>(45.6)%</td><td>USD</td><td>12.22</td><td>13.89</td><td>16.13</td><td>5.1</td><td>4.5</td><td>3.9</td></tr><tr><td>KLAR (Klarna)</td><td>M</td><td>USD</td><td>15.78</td><td>20.00</td><td>NA</td><td>USD</td><td>65.1</td><td>305.3</td><td>461.7</td><td>40.1</td><td>8.5</td><td>5.7</td></tr><tr><td>MA (Mastercard)</td><td>O</td><td>USD</td><td>489.08</td><td>710.00</td><td>(40.0)%</td><td>USD</td><td>17.01</td><td>19.82</td><td>22.82</td><td>28.8</td><td>24.7</td><td>21.4</td></tr><tr><td>PYPL (PayPal)</td><td>M</td><td>USD</td><td>40.70</td><td>45.00</td><td>(68.5)%</td><td>USD</td><td>5.31</td><td>5.23</td><td>5.30</td><td>7.7</td><td>7.8</td><td>7.7</td></tr><tr><td>TOST (Toast)</td><td>O</td><td>USD</td><td>24.30</td><td>39.00</td><td>(66.9)%</td><td>USD</td><td>633.00</td><td>802.78</td><td>990.80</td><td>19.5</td><td>15.4</td><td>12.5</td></tr><tr><td>V (Visa)</td><td>O</td><td>USD</td><td>322.96</td><td>450.00</td><td>(35.9)%</td><td>USD</td><td>11.47</td><td>13.17</td><td>15.16</td><td>28.2</td><td>24.5</td><td>21.3</td></tr><tr><td>SPX</td><td></td><td></td><td>7,386.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,533.88</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
XYZ estimate is EBIT (M); KLAR estimate is Adjusted EBIT; TOST estimate is EBITDA (M); XYZ valuation is EV/EBIT (x); KLAR valuation is EV/Adj EBIT (x);  
TOST valuation is EV/EBITDA (x);  
Source: Bloomberg, Bernstein estimates and analysis.

## I. REQUIRED DISCLOSURES

References to "Bernstein" or the "Firm" in these disclosures relate to the following entities: Bernstein Institutional Services LLC (April 1, 2024 onwards), Bernstein & Co., LLC (pre April 1, 2024), Bernstein Autonomous LLP, BSG France S.A. (April 1, 2024 onwards), Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited, Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社) and analysts employed by SG Africa Technologies & Services to produce Bernstein under a Global Services Agreement in place between Bernstein and SG.

Bernstein is part of a joint venture between SG (SG) and AllianceBernstein, L.P. (AB). Unless specifically noted otherwise, for purposes of these disclosures, references to Bernstein's “affiliates” relate to both SG and AB and their respective affiliates.

## VALUATION METHODOLOGY

This research publication covers six or more companies. For valuation methodology and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RISKS

This research publication covers six or more companies. For risks and other company disclosures:

Please visit: https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

Or, you can also write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

## RATINGS DEFINITIONS, BENCHMARKS AND DISTRIBUTION

## EQUITY RATINGS DEFINITIONS

## Bernstein brand

The Bernstein brand rates stocks based on forecasts of relative performance for the next 12 months versus the S&P 500 for stocks listed on the U.S. and Canadian exchanges, versus the Bloomberg Europe Developed Markets Large and Mid Cap Price Return Index EUR (EDME) for stocks listed on the European exchanges and emerging markets exchanges outside of the Asia Pacific region, versus the Bloomberg Japan Large and Mid Cap Price Return Index USD (JPL) for stocks listed on the Japanese exchanges, and versus the Bloomberg Asia ex-Japan Large and Mid Cap Price Return Index (ASIAX) for stocks listed on the Asian (ex-Japan) exchanges -unless otherwise specified.

The Bernstein brand has three categories of ratings:

- Outperform: Stock will outpace the market index by more than 15 pp  
• Market-Perform: Stock will perform in line with the market index to within +/-15 pp  
• Underperform: Stock will trail the performance of the market index by more than 15 pp

Coverage Suspended: Coverage of a company under the Bernstein brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Not Covered (NC) denotes companies that are not under coverage.

Bernstein brand stock ratings are based on a 12-month time horizon.

## Autonomous brand – common stocks

The Autonomous brand rates common stocks as indicated below. As our benchmarks we use the Bloomberg Europe 500 Banks And Financial Services Index (BEBANKS) and Bloomberg Europe Dev Mkt Financials Large and Mid Cap Price Ret Index EUR (EDMFI) index for developed European banks and Payments, the Bloomberg Europe 500 Insurance Index (BEINSUR) for European insurers, the S&P 500 and S&P Financials for US banks and Payments coverage, S5LIFE for US Insurance, the S&P Insurance Select Industry (SPSIINS) for US Non-Life Insurers coverage, and the Bloomberg Emerging Markets Financials Large, Mid and Small Cap Price Return Index (EMLSF) for emerging market banks and insurers and Payments. Ratings are stated relative to the sector (not the market).

The Autonomous brand has three categories of common stock ratings:

- Outperform (OP): Stock will outpace the relevant index by more than 10 pp  
- Neutral (N): Stock will perform in line with the market index to within +/-10 pp  
• Underperform (UP): Stock will trail the performance of the relevant index by more than 10 pp

Coverage Suspended: Coverage of a company under the Autonomous research brand has been suspended. Ratings and price targets are suspended temporarily, are no longer current, and should therefore not be relied upon.

Not Rated: A rating assigned when the stock cannot be accurately valued, or the performance of the company accurately predicted, at the present time. The covering analyst may continue to publish research reports on the company to update investors on events and developments.

Those denoted as ‘Feature’ (e.g., Feature Outperform FOP, Feature Under Outperform FUP) are our core ideas.

Not Covered (NC) denotes companies that are not under coverage.

Autonomous brand common stock ratings are based on a 12-month time horizon.

## Autonomous brand – preferred stocks

The Autonomous brand has three categories of preferred stock ratings:

- Outperform (OP): The total return of the preferred instrument is expected to outperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.  
- Neutral (N): The total return of the preferred instrument is expected to perform in line with preferred securities of other issuers operating in similar sectors or rating categories over the next six months.  
- Underperform (UP): The total return of the preferred instrument is expected to underperform preferred securities of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous preferred stock ratings are based on a 6-month time horizon.

## AUTONOMOUS CREDIT RESEARCH

Where this report contains investment recommendations for credit instruments, as defined in article 3(1)(35) of the Market Abuse Regulation, the information below is presented to comply with its disclosure requirements.

The report may also include reference(s) to published opinions by other Autonomous or Bernstein analysts covering the equity securities of the issuer(s) referenced herein. Please note an investment recommendation for credit instruments published by the author(s) of this report may differ from the published view of the analyst covering equity securities for the issuer(s) contained in this report and vice versa.

## CREDIT RATINGS DEFINITIONS

The Autonomous brand has three categories of credit ratings:

\- Credit Outperform (C-OP): The total return of the Reference Credit Instrument is expected to outperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

- Credit Neutral (C-N): The total return of the Reference Credit Instrument is expected to perform in line with the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.  
- Credit Underperform (C-UP): The total return of the Reference Credit Instrument is expected to underperform the credit spread of bonds of other issuers operating in similar sectors or rating categories over the next six months.

Autonomous credit ratings are based on a 6-month time horizon.

A list of all investment recommendations produced by the author(s) of this report alongside credit ratings history are available upon request.

It is at the sole discretion of the Firm as to when to initiate, update and cease research coverage. The Firm has established, maintains and relies on information barriers to control the flow of information contained in one or more areas (i.e. the private side) within the Firm, and into other areas, units, groups or affiliates (i.e. public side) of the Firm

DISTRIBUTION OF EQUITY RATINGS/INVESTMENT BANKING SERVICES

<table><tr><td>Equity Rating</td><td>Market Abuse Regulation (MAR) and FINRA Rating Category</td><td>Global Rating Distribution</td><td>Investment Banking Relationships*</td></tr><tr><td>Outperform</td><td>BUY</td><td>51.1%</td><td>16.5%</td></tr><tr><td>Market-Perform (Bernstein Brand) Neutral (Autonomous Brand)</td><td>HOLD</td><td>36.3%</td><td>17.8%</td></tr><tr><td>Underperform</td><td>SELL</td><td>12.6%</td><td>14.9%</td></tr></table>

\* These figures represent the percentage of companies within each equity rating category for which affiliates of Bernstein have provided investment banking services within the previous 12 months.  
As of March 31, 2026. All figures are updated quarterly.

Prior to April 1, 2024, Bernstein & Co., LLC. issued the ratings and price target information in the graph(s) below for the following companies: Adyen NV, FIS, Global Payments Inc, Mastercard Inc, PayPal Holdings Inc, Toast Inc and Visa Inc.

## PRICE CHARTS/ RATINGS AND PRICE TARGET HISTORY

This research publication covers six or more companies. For price chart and other company disclosures, please visit https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action or you can write to the Director of Compliance, Bernstein Institutional Services LLC, 245 Park Avenue, New York, NY 10167.

Adyen NV, Block Inc, FIS, Fiserv, Global Payments Inc, Klarna Group plc, Mastercard Inc, PayPal Holdings Inc, Toast Inc and Visa Inc are covered by both the Autonomous and Bernstein brands. For the research ratings and price target history please go to https://bernstein-autonomous.bluematrix.com/sellside/Disclosures.action.

## CONFLICTS OF INTEREST

SG and/or its affiliate

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
