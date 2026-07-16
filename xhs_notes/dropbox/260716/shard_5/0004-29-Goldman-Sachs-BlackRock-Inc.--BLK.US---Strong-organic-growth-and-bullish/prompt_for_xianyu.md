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
# BlackRock Inc. (BLK): Strong organic growth and bullish margin outlook paves the way for P/E re-rating; Reiterate Buy

Following 2Q26 results, we raise our 2026E-28E EPS to \$55.54/\$64.37/\$75.05 from \$53.97/\$62.70/\$72.45 on the back of a higher organic growth outlook and constructive margin commentary, which should be supportive of a positive EPS revision cycle for the stock with ample runway for the multiple to mean-revert to historical \~20X. Specifically, BLK continues to deliver above-target organic base fee growth — 8% in 2Q26 / 10% LTM, with management noting recent trends are likely to be sustainable, supported by: 1) broadening growth in the ETF business, including momentum in Active and Precision ETFs, 2) runway for >10% FPAUM growth in private markets (driven by demand and activity across Private Credit and Infrastructure, with tailwinds from Insurance and financing the AI boom), and 3) continued growth in higher-fee systematic and tax aware products. Importantly, management also struck a constructive tone on margins (an issue for investors since GIP/HPS deals), pointing to a structurally higher margin trajectory from a mix shift into higher-margin private markets, systematic, and technology. Moreover, BLK reiterated that current \~46% margins are not a ceiling relative to the \~47% achieved in 2021 when BLK was less scaled in its higher margin businesses. We see a path to >48% margins in 2028E (Visible Alpha Consensus Data is <47%). All in, we believe BLK will generate mid-teens EPS growth over the coming years assuming a normal markets backdrop and expect positive EPS revisions for 2026/2027 to clear the path for the stock to re-rate closer to its historical averages. With the stock currently trading at \~19X NTM P/E (\~9% discount to SPX, relative to slightly below historically) and the organic revenue growth momentum sustaining over the coming year, we believe that current valuation leaves an attractive risk/reward - our PT goes to \$1,389 from \$1,353 based on a 20X Q5-Q8 P/E, implying 27% upside. More details within.

Key notables from earnings include:

Organic base fee growth: BLK generated 8% organic base fee growth during 2Q26 with \~\$200bn of net inflows (and 10% over the LTM), driven by a breadth of net inflows across ETFs, systematic/tax aware products, and private markets. Management sees above target organic base fee growth as sustainable moving forward as it leans into higher fee products with structural growth and whole portfolio relationships. On structural growers, management sees strength across its ETF franchise, model portfolios, tax aware, and systematic strategies as the main drivers of organic fee growth. BLK also spoke to taking share in whole portfolio relationships as investors consolidate business with fewer providers, a

Alexander Blostein, CFA
+1(212)357-9976 |
alexander.blostein@gs.com
GS & Co. LLC

Anthony Corbin  
+1(212)357-7512 | anthony.corbin@gs.com GS & Co. LLC

Aditya Sharma, CFA
+1(212)934-9869 |
aditya.x.sharma@gs.com
GS India SPL

Michael Vinci
+1(212)357-8239 |
michael.vinci@gs.com
GS & Co. LLC

Vaasu Gupta
+1(332)245-7522 |
vaasu.x.gupta@gs.com
GS India SPL

trend we have seen over the last several years. Overall, we expect organic base fee growth to be in the 7%-8% range over the next few years.

iShares: iShares remained the standout this quarter, generating \$178bn of inflows. Flows were led by Core Equity (\$85bn) and Index bond ETFs (\$61bn), but is increasingly seeing strong flows towards higher fee categories - Active ETFs saw \$20bn of inflows in the quarter, while precision exposure ETF contributed \$15bn of inflows. The franchise is also increasingly expanding globally with European iShares at \$80bn of YTD inflows (\$1.5tn of AUM) aided by a structural shift of European retail investors moving away from bank savings towards capital markets via ETFs. Management also framed tokenization as a further organic growth opportunity, granting iShares a new distribution channel into the >\$2tn of assets in digital wallets. Overall, we see strength in iShares underpinning BLK's 7%-8% organic base fee growth over the next few years.

\- ETF platform/distribution fees: Management addressed recent industry news (BofA revenue-sharing increases and SCHW platform fees on ETFs), noting BLK will not pay platform fees on its Index ETFs and that they haven’t been approached by any major US distribution platform on this topic. That said, BLK did acknowledge that Active ETFs could see platform fees implemented though noted the economics are not meaningfully different for mutual funds.

☐ Systematic/Tax Aware: BLK spoke to robust demand for its systematic and tax-aware strategies which together generated \$27bn of net inflows in the quarter. Management sees demand accelerating for these strategies as investors look for strategies that allocate across factor and signals to generate alpha. Majority of BLK’s systematic products sit within Active Equities which has turned organic growth positive in recent quarters, while newer areas like systematic active ETFs and its global equity market neutral fund are further supporting organic growth in its iShares and Liquid Alts franchises. BLK has also seen robust growth for its tax-aware strategies at Aperio and SpiderRock with AUM at \~\$210bn, up 4X over the last 5 years. At Aperio, while historically focused around its direct indexing strategy, BLK has seen accelerating flows into its long-short product with 2Q Aperio flows of \$7bn evenly split between its direct indexing and long/short products. Overall, management sees the usage of tax-optimized strategies in early stages and expects to see continued structural growth as clients focus on after-tax returns.

☐ Private Markets: BLK is seeing continued strength in Private Markets with \$15bn of inflows in the quarter, driven by \$6bn of private credit deployment, \$5bn of infrastructure activity (a mix of fundraising and deployment in infra debt), and a \$3bn partial funding of a PE outsourcing solution mandate. BLK reiterated its Investor Day target of \$400bn in gross fundraising through 2030 (currently at \$22bn). Management spoke to the robust opportunity it has in the insurance channel as insurance clients increasingly look to access private markets to achieve higher yields (\~150bps-350bps over treasuries) in exchange for illiquidity. With \~\$800bn of Insurance AUM, BLK sees an

opportunity to rotate 5%-10% of that capital to private markets, providing a meaningful lift to fees. To capture some this rotation, management noted its deepening the integration of GIP and HPS on the origination side,

collaborating on large-scale financings (particularly in digital infrastructure) it can originate and pass on to insurance clients (though not limited to insurance clients). Management noted private credit demand remains robust given wider spreads while infrastructure demand is in the early stages of a multi-year cycle driven by the hyperscalers transition from balance sheet light to balance sheet heavy models which require a substantial amount of debt (and to a lesser equity) to build out data center and digital infrastructure. On fundraising, BLK is in the market with its legacy infra flagship (prior vintage \$7bn) and its EM infra flagship (prior vintage \$2bn), with the next vintage of the GIP flagship (prior vintage \$20bn) expected to have a first close by late 2026/early 2027.

\- Fee Rate: Private Markets fees were down 3% driven by a \~4bps q/q decline in the fee rate. BLK noted the decline in the fee rate was driven by realizations within Infra equity early in the quarter and timing of flows toward the back half of the quarter. Looking ahead, BLK sees 80-81bps as the right jumping off point for 3Q. We expect a Private Markets fee rate of 80.9bps in 3Q, before gradually building as the Infra flagships hold closes (which will also come with catch up fees) and HPS Wealth vehicles return flow positive.

\- Margin outlook: BLK delivered a strong quarter on profitability, posting an operating margin of 45.9% (46.5% ex. performance fees), its highest level since 2021 driven by solid comp leverage. On the forward, management struck a constructive tone on margins highlighting a structurally higher margin profile given the mix of business toward higher-margin, structural growth business like Private markets, Active and Precision ETFs, Systematic strategies, SMAs/models, and technology. BLK also noted that its 2030 target of >30% of revenue coming from Private Markets and Tech should mitigate market sensitivity and led to sustainable double-digit EPS growth. Management was explicit that this quarter’s \~46% margin is not a ceiling, noting BLK ran at a \~47% margin back in 2021 without the current scale of its Private Markets, systematic, and SMA capabilities. Overall, management sees the biggest components of margin expansion are 1) driving FRE margins (margins excluding performance fees) toward Alt managers’ levels (Public Alts avg. FRE margins are \~55%), and 2) higher fee rates on flows combined with strong organic growth and tech-driven operating leverage. We see a path for BLK to deliver \~48% operating margins by 2028 (and \~50% margin ex. performance fees), implying \~150bps of margin expansion annually on average.

☐ 2026: While G&A came above expectations, BLK re-affirmed its MSD % growth target (after annualizing 2H25) which implies \~\$2.8bn of G&A for FY26. Within this, BLK expects G&A to be roughly flat for the next two quarters. On the comp rate ex. performance fees, BLK expects it to be in the \~32% range for 2026 (though we could see room for upside if markets remain supportive).

Exhibit 1: BLK is trading \~18.5X NTM P/E, 5% below its historical average...

![](images/c9c00262fd7b6ca505d5778a4fb48e320a8fc282d061e0e9058e875b622acc96.jpg)  
Source: Company data, GS Global Investment Research, FactSet  
Exhibit 2: ...though it's trading at a \~9% discount to SPX which has historically traded slightly below SPX levels

![](images/edbd3d40db194c8ac965a5edcb78b1d30d64c1e5e1c79f010ecdee1e2d1d5e64.jpg)  
Source: Company data, FactSet, GS Global Investment Research  
Exhibit 3: Based on historical levels, BLK implied multiple should be \~20X

<table><tr><td colspan="5">BLK Current Multiple vs. Historical Levels</td></tr><tr><td></td><td>Current</td><td>Historical</td><td>Discount vs. Hist.</td><td>Implied</td></tr><tr><td>NTM</td><td>18.5X</td><td>19.5X</td><td>-5%</td><td>19.5X</td></tr><tr><td>Discount to SPX</td><td>-9%</td><td>-2%</td><td>-8%</td><td>20.0X</td></tr><tr><td>Discount to SPX EW</td><td>14%</td><td>21%</td><td>-7%</td><td>19.7X</td></tr></table>

Source: Company data, FactSet, GS Global Investment Research

EPS Revisions: Following 2Q26 results, we raise our 2026E-28E EPS to \$55.54/\$64.37/\$75.05 from \$53.97/\$62.70/\$72.45 on the back of a stronger organic growth and margin outlook.

Price Target and Valuation: We remain Buy rated on BLK and revise our 12-month PT to \$1,389 from \$1,353 based on a 20X Q5-Q8 P/E (unchanged). This implies 27% upside from current levels.

Risks: Downside: Higher Expenses, weaker equity markets.

<table><tr><td>BLK</td><td colspan="2">12m Price Target: $1,389.00</td><td colspan="2">Price: $1,093.40</td><td colspan="2">Upside: 27.0%</td></tr><tr><td rowspan="13">Buy</td><td rowspan="2"></td><td rowspan="2">GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $179.1bn</td><td>Revenue ($ mn) New</td><td>24,216.0</td><td>29,439.3</td><td>33,756.5</td><td>37,897.7</td></tr><tr><td>Enterprise value: $161.2bn</td><td>Revenue ($ mn) Old</td><td>24,216.0</td><td>29,212.8</td><td>33,214.7</td><td>37,093.0</td></tr><tr><td>3m ADTV: $757.4mn</td><td>EBIT ($ mn)</td><td>9,600.0</td><td>12,104.0</td><td>14,313.1</td><td>16,611.1</td></tr><tr><td>United States</td><td>EPS ($) New</td><td>48.05</td><td>55.54</td><td>64.37</td><td>75.05</td></tr><tr><td rowspan="7">Americas Asset Managers &amp; Capital Markets M&amp;A Rank: 3</td><td>EPS ($) Old</td><td>48.05</td><td>53.97</td><td>62.70</td><td>72.45</td></tr><tr><td>P/E (X)</td><td>21.6</td><td>19.7</td><td>17.0</td><td>14.6</td></tr><tr><td>Dividend yield (%)</td><td>2.0</td><td>2.1</td><td>2.3</td><td>2.5</td></tr><tr><td>ROE (%)</td><td>14.9</td><td>15.5</td><td>16.5</td><td>16.6</td></tr><tr><td>AuM ($ mn)</td><td>13,463,648.0</td><td>13,896,067.0</td><td>18,097,806.4</td><td>18,097,806.4</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS ($)</td><td>12.53</td><td>13.91</td><td>14.02</td><td>15.08</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 15 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Alexander Blostein, CFA, Anthony Corbin, Aditya Sharma, CFA, Michael Vinci and Vaasu Gupta, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Alexander Blostein, CFA GS & Co. LLC, Anthony Corbin GS & Co. LLC, Aditya Sharma, CFA GS India SPL, Michael Vinci GS & Co. LLC, Vaasu Gupta GS India SPL.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
