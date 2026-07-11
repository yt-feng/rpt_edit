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
## Economics China Macro

## Inflation monitor: Reflation taking a break

China's reflation is taking a break. Both CPI and PPI recorded declines on a month-on-month basis, with most components decelerating from May. The decline is broader than lower oil prices; it reflects that softening domestic demand is starting to negatively impact China's reflation momentum.

Headline CPI fell to 1.0% YoY and -0.3% MoM due to sharp declines in energy and subdued food inflation, while core inflation also decreased, though services and AI-related product prices remained relatively resilient.

\- Energy prices fell sharply by 4.5% MoM, reducing the contribution to CPI by 0.2ppt. Food inflation also remained subdued at -1.6% YoY.

\- Core inflation edged down 0.1ppt to 1.0% YoY, the lowest reading since September last year (after Lunar New Year adjustment). On a sequential basis, it fell 0.1% MoM, marking a second consecutive monthly decline.

\- Consumer goods prices showed weakness, dropping by 0.5ppt to $1.1\%$ YoY. Prices of home appliances and autos saw moderation, likely resulting from diminished impact from trade-in subsidies.

\- Prices of services and AI-related products remained relatively resilient. Services inflation held steady at 0.8% YoY, with inflation in education, tourism and recreation edging up by 0.1ppt on YoY horizon. Meanwhile, communication device prices accelerated by a further 1.0ppt to 7.6% YoY.

PPI rose to 4.1% YoY due to base effect; however, it declined by 0.3% MoM as the oil-price shock on upstream and midstream faded, while only limited pass-through to downstream industries emerged amid weak domestic demand.

\- Oil-price shock in upstream and midstream sectors is fading. PPI inflation in fossil-fuel-related industries turned sharply negative on a MoM basis, weighing on prices for chemicals, plastics and rubber products.

\- There are signs that previous price hikes are being passed through to some downstream sectors, such as equipment, furniture, automobiles and communication devices. However, the pass-through remains modest, constrained by soft domestic demand.

We reiterate our full-year CPI inflation forecast at 1.3% and PPI inflation forecast to 3.0%, both of which have been revised down in our H2 outlook. The latest June data confirms that softening domestic demand has increasingly transmitted into price dynamics, preventing price transmission from upstream to downstream products. Looking forward, we expect more supportive domestic policy in the second half, fiscal spending in particular, will help revert the recent slip in consumer prices. Absent such policy support, we see risk of CPI inflation weakening further.

Figure 1: Momentum slowed across upstream and midstream  
![](images/75cf3a628b24432e682b7e51ca47c019d52b039dc9f6fbc9f56e9d32e25fe6d4.jpg)  
Source: DB, Wind

Figure 2: Limited pass-through to downstream industries emerged  
![](images/bec5716dd22ed9e482b94c82bb1f036f0228434c3fc0602f55ad7b5ae268d385.jpg)

Figure 3: Energy prices' contribution to CPI dropped by 0.2ppt  
![](images/2d0e771beca6f6bb2e13d15e975ecd1035ca1ef89a022379023056a4403a6018.jpg)  
Jan-24 Apr-24 Jul-24 Oct-24 Jan-25 Apr-25 Jul-25 Oct-25 Jan-26 Apr-26

Figure 4: Headline CPI and core CPI slowed in June  
![](images/f0af7dadaa3462a5781e3ac5f1ba306aabb257e2b932dd8d23376602c8f98329.jpg)

Figure 5: Core inflation underperformed seasonality  
![](images/08a45f4151a3c5a6439d7fdd2c8417255543821f570fac9ef04b322229ccb9fc.jpg)  
Source: DB, Wind

Figure 6: Food inflation remained in negative territory  
![](images/5e83c86ac07ad24e1709b4b3240209676c718750487b26e25eb3a5fb28fa5dbb.jpg)  
Source: DB, Wind

Figure 7: Consumer goods prices showed weakness  
![](images/ad8049d9902d4b3832f904d6254e1097adec421344ca349860119329a467b572.jpg)  
Source: DB, Wind

Figure 8: We have revised down our full-year CPI forecast to 1.3%  
![](images/4da2b7a113e62f9d144ab4dad3bcd1f9758027e2c6b3f49807e01ee53834e4fb.jpg)  
Source: DB, Wind

Figure 9: June inflation momentum

<table><tr><td>%, YoY</td><td>Weight</td><td>21 avg</td><td>22 avg</td><td>23 avg</td><td>24 avg</td><td>25 avg</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td>Headline CPI</td><td></td><td>0.9</td><td>2.0</td><td>0.2</td><td>0.2</td><td>0.0</td><td>0.2</td><td>1.3</td><td>1.0</td><td>1.2</td><td>1.2</td><td>1.0</td></tr><tr><td>Core CPI</td><td></td><td>0.8</td><td>0.9</td><td>0.7</td><td>0.5</td><td>0.8</td><td>0.8</td><td>1.8</td><td>1.1</td><td>1.2</td><td>1.1</td><td>1.0</td></tr><tr><td>Food, Tobacco, Alcohol &amp; Dining Out</td><td>30%</td><td>-0.3</td><td>2.5</td><td>0.3</td><td>-0.1</td><td>-0.6</td><td>-0.2</td><td>1.4</td><td>0.4</td><td>-0.8</td><td>-0.9</td><td>-0.8</td></tr><tr><td>Clothing</td><td>5%</td><td>0.3</td><td>0.5</td><td>1.0</td><td>1.4</td><td>1.5</td><td>1.9</td><td>1.9</td><td>1.6</td><td>1.5</td><td>1.4</td><td>1.4</td></tr><tr><td>Housing</td><td>22%</td><td>0.8</td><td>0.7</td><td>0.0</td><td>0.1</td><td>0.1</td><td>-0.1</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.2</td><td>-0.3</td></tr><tr><td>Household Articles &amp; Services</td><td>6%</td><td>0.4</td><td>1.2</td><td>0.1</td><td>0.5</td><td>0.9</td><td>2.6</td><td>2.8</td><td>1.5</td><td>1.4</td><td>1.8</td><td>1.3</td></tr><tr><td>Transportation &amp; Communication</td><td>14%</td><td>4.2</td><td>5.2</td><td>-2.3</td><td>-1.9</td><td>-2.6</td><td>-3.4</td><td>-0.7</td><td>0.9</td><td>4.6</td><td>5.4</td><td>4.1</td></tr><tr><td>Recreation Education &amp; Cultural Services</td><td>11%</td><td>1.9</td><td>1.8</td><td>2.0</td><td>1.5</td><td>0.8</td><td>0.0</td><td>2.0</td><td>1.1</td><td>1.3</td><td>1.3</td><td>1.4</td></tr><tr><td>Medicine &amp; Healthcare</td><td>9%</td><td>0.4</td><td>0.6</td><td>1.1</td><td>1.3</td><td>0.8</td><td>1.7</td><td>1.9</td><td>1.9</td><td>2.2</td><td>2.1</td><td>2.3</td></tr><tr><td>Others</td><td>3%</td><td>-1.3</td><td>1.6</td><td>3.2</td><td>3.8</td><td>9.2</td><td>13.2</td><td>15.4</td><td>13.5</td><td>11.0</td><td>9.9</td><td>6.6</td></tr><tr><td>Headline PPI</td><td></td><td>8.1</td><td>4.2</td><td>-3.0</td><td>-2.1</td><td>-2.6</td><td>-1.4</td><td>-0.9</td><td>0.5</td><td>2.8</td><td>3.9</td><td>4.1</td></tr><tr><td>Mining &amp; Quarrying</td><td></td><td>34.8</td><td>18.7</td><td>-7.6</td><td>-2.8</td><td>-8.9</td><td>-8.1</td><td>-5.3</td><td>2.0</td><td>10.6</td><td>15.8</td><td>16.5</td></tr><tr><td>Raw Materials</td><td></td><td>15.9</td><td>10.7</td><td>-4.3</td><td>-1.6</td><td>-3.4</td><td>-2.0</td><td>-1.9</td><td>1.1</td><td>7.1</td><td>9.2</td><td>8.6</td></tr><tr><td>Manufacturing</td><td></td><td>6.6</td><td>1.6</td><td>-3.3</td><td>-2.9</td><td>-2.4</td><td>-0.4</td><td>0.3</td><td>0.9</td><td>1.5</td><td>2.3</td><td>3.0</td></tr></table>

Source: DB, Wind

## Appendix 1

## Analyst Certification

The views expressed in this report accurately reflect the personal views of the undersigned lead analyst(s). In addition, the undersigned lead analyst(s) has not and will not receive any compensation for providing a specific recommendation or view in this report. Deyun Ou, Yi Xiong, Ph.D..

## Important Disclosures

Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For further information regarding disclosures relevant to DB, please visit our global disclosure look-up page on our website at

https://research.db.com/Research/Disclosures/FICCDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

## Additional Information

The information and opinions in this report were prepared by DB AG or one of its affiliates (collectively 'DB'). Though the information herein is believed to be reliable and has been obtained from public sources believed to be reliable, DB makes no representation as to its accuracy or completeness. Hyperlinks to third-party websites in this report are provided for reader convenience only. DB neither endorses the content nor is responsible for the accuracy or security controls of those websites.

If you use the services of DB in connection with a purchase or sale of a security that is discussed in this report, or is included or discussed in another communication (oral or written) from a DB analyst, DB may act as principal for its own account or as agent for another person.

DB may consider this report in deciding to trade as principal. It may also engage in transactions, for its own account or with customers, in a manner inconsistent with the views taken in this research report. Others within DB, including strategists, sales staff and other analysts, may take views that are inconsistent with those taken in this research report. DB issues a variety of research products, including fundamental analysis, equity-linked analysis, quantitative analysis and trade ideas. Recommendations contained in one type of communication may differ from recommendations contained in others, whether as a result of differing time horizons, methodologies, perspectives or otherwise. DB and/or its affiliates may also be holding debt or equity securities of the issuers it writes on. Analysts are paid in part based on the profitability of DB AG and its affiliates, which includes investment banking, trading and principal trading revenues.

Opinions, estimates and projections constitute the current judgment of the author as of the date of this report. They do not necessarily reflect the opinions of DB and are subject to change without notice. DB provides liquidity for buyers and sellers of securities issued by the companies it covers. DB analysts sometimes have shorter-term trade ideas that may be inconsistent with DB's existing longer-term ratings. Some trade ideas for equities are listed as Catalyst Calls on the Research Website (https://research.db.com/Research/), and can be found on the general coverage list and also on the covered company's page. A Catalyst Call represents a high-conviction belief by an analyst that a stock will outperform or underperform the market and/or a specified sector over a time frame of no less than two weeks and no more than three months. In addition to Catalyst Calls, analysts may occasionally discuss with our clients, and with DB salespersons and traders, trading strategies or ideas that reference catalysts or events that may have a near-term or medium-term impact on the market price of the securities discussed in this report, which impact may be directionally counter to the analysts' current 12-month view of total return or investment return as described herein. DB has no obligation to update, modify or amend this report or to otherwise notify a recipient thereof if an opinion, forecast or estimate changes or becomes inaccurate. Coverage and the frequency of changes in market conditions and in both general and company-specific economic prospects make it difficult to update research at defined intervals. Updates are at the sole discretion of the coverage analyst or of the Research Department Management, and the majority of reports are published at irregular intervals. This report is provided for informational purposes only and does not take into account the particular investment objectives, financial situations, or needs of individual clients. It is not an offer or a solicitation of an offer to buy or sell any financial instruments or to participate in any particular trading strategy. Target prices are inherently imprecise and a product of the analyst's judgment. The financial instruments discussed in this report may not be suitable for all investors, and investors must make their own informed investment decisions. Prices and availability of financial instruments are subject to change without notice, and investment transactions can lead to losses as a result of price fluctuations and other factors. If a financial instrument is denominated in a currency other than an investor's currency, a change in exchange rates may adversely affect the investment. Past performance is not necessarily indicative of future results. Performance calculations exclude transaction costs, unless otherwise indicated. Unless otherwise indicated, prices are current as of the end of the previous trading session and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Data is also sourced from DB, subject companies, and other parties. Artificial intelligence tools may be used in the preparation of this material, including but not limited to assist in fact-finding, data analysis, pattern recognition, content drafting and editorial corrections pertaining to research material.

The DB Department is independent of other business divisions of the Bank. Details regarding our organizational arrangements and information barriers we have to prevent and avoid conflicts of interest with respect to our research are available on our website (https://research.db.com/Research/) under Disclaimer.

Macroeconomic fluctuations often account for most of the risks associated with exposures to instruments that promise to pay fixed or variable interest rates. For an investor who is long fixed-rate instruments (thus receiving these cash flows), increases in interest rates naturally lift the discount factors applied to the expected cash flows and thus cause a loss. The longer the maturity of a certain cash flow and the higher the move in the discount factor, the higher will be the loss. Upside surprises in inflation, fiscal funding needs, and FX depreciation rates are among the most common adverse macroeconomic shocks to receivers. But counterparty exposure, issuer creditworthiness, client segmentation, regulation (including changes in assets holding limits for different types of investors), changes in tax policies, currency convertibility (which may constrain currency conversion, repatriation of profits and/or liquidation of positions), and settlement issues related to local clearing houses are also important risk factors. The sensitivity of fixed-income instruments to macroeconomic shocks may be mitigated by indexing the contracted cash flows to inflation, to FX depreciation, or to specified interest rates - these are common in emerging markets. The index fixings may - by construction - lag or mis-measure the actual move in the underlying variables they are intended to track. The choice of the proper fixing (or metric) is particularly important in swaps markets, where floating coupon rates (i.e., coupons indexed to a typically short-dated interest rate reference index) are exchanged for fixed coupons. Funding in a currency that differs from the currency in which coupons are denominated carries FX risk. Options on swaps (swaptions) the risks typical to options in addition to the risks related to rates movements.

Derivative transactions involve numerous risks including market, counterparty default and illiquidity risk. The appropriateness of these products for use by investors depends on the investors' own circumstances, including their tax position, their regulatory environment and the nature of their other assets and liabilities; as such, investors should take expert legal and financial advice before entering into any transaction similar to or inspired by the contents of this publication. The risk of loss in futures trading and options, foreign or domestic, can be substantial. As a result of the high degree of leverage obtainable in futures and options trading, losses may be incurred that are greater than the amount of funds initially 

[中间内容因长度限制已省略]

inancial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau  
Group Chief Economist and Global Head of Research

<table><tr><td>Pam Finelli
COO and Head of Fixed Income Research</td><td>Steve Pollard
Global Head of Company Research and Sales</td><td>Jim Reid
Global Head of Macro and Thematic Research</td><td>Tim Rokossa
Head of European Company Research</td></tr><tr><td>Matthew Barnard
Head of Americas
Company Research</td><td>Debbie Jones
Global Head of Sustainability and Data Innovation, Research</td><td>Robin Winkler
Head of German Macro Research</td><td>Sameer Goel
Global Head of EM &amp; APAC Research</td></tr><tr><td>Francis Yared
Global Head of Rates Research</td><td>George Saravelos
Global Head of FX Research</td><td>Peter Hooper
Vice-Chair of Research</td><td>Nilendra de-Mel
Head of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG  
21 Moorfields  
London EC2Y 9DB  
United Kingdom  
Tel: (44) 20 7545 8000

DB AG  
Filiale Singapur  
One Raffles Quay, South Tower  
Singapore 048583  
Tel: (65) 6423 8001
"""
