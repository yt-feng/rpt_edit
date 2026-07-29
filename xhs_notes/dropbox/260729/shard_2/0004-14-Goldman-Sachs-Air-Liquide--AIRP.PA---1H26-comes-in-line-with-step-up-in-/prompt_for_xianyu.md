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
# Air Liquide (AIRP.PA): 1H26 comes in line with step up in EL growth and IM pricing; 2H commentary light vs. Street

Air Liquide reported 1H26 results this morning (July 28), with 2Q26 G&S comp. growth above Vara Consensus (3.3% vs. 2.9%) and 1H26 OIR 1% above Vara Consensus. We highlight our key takeaways below:

Comparable growth in 2Q26: G&S comp. growth of $3.3\%$ came in above Vara Consensus, driven by slightly better Industrial Merchant and materially better Electronics growth. Comp. growth in Large Industries was in line with Visible Alpha Consensus $(-0.3\%)$ comp. growth vs. Cons $-0.2\%$ and $-0.2\%$ in 1Q26). Industrial Merchant comp. growth of $3.8\%$ was above Visible Alpha Consensus $3.3\%$ and vs. $2.7\%$ in 1Q26. Industrial Merchant pricing was $5.0\%$ in 2Q26, up from $3.4\%$ in Q126. Healthcare comp. growth was $4.4\%$ , vs. Visible Alpha Consensus at $4.4\%$ , and Electronics comp. growth accelerated to $9.5\%$ vs. Visible Alpha Consensus at $4.6\%$ .

Earnings in 1H: Group OIR of €2,845mn was 1% above Vara Consensus for a 20.9% margin (vs. 21.1% Vara Consensus and 21.5% in 2H25).

Cash performance: Operating cash flow in 1H26 came in at €3,372mn, a 13% increase y/y, and cash conversion (OCF/EBITDA) was 84% in 1H26 vs. 96% in 2H25 and 74% in 1H25.

Efficiency gains: Structural efficiencies reached €157mn in 2Q26 (€299mn for 1H26), up 11% from the €142mn in 1Q26.

Investment opportunities: The NTM investment opportunities increased to €4.8bn (vs. €4.5bn in 1Q26 and €4.1bn at in 2Q25), of which more than 50% represents opportunities in electronics (from 40%). Air Liquide reported an all-time high industrial decisions and >€1bn of EL successes in Carrier Gases.

FY26 Outlook: Air Liquide confirmed its FY26 guidance for further increased operating margin +100bps OIR margin improvement in FY26/27 and +560bps over 2022-27 as well as recurring net profit growth in 2026 at constant exchange rates.

## GS View

An in-line print. The guidance for comp growth in 2H26 to be “similar to, or slightly higher than, that of H1” (2.6%) is softer than the 5%+ that consensus/GS are looking for. Some strong positives to take from the print today are the notable step up in EL comp growth to close to 10%, as well as the step up in IM pricing sequentially. OIR margins are already tracking up 110 bps y/y vs. the 100bps improvement guided to

Georgina Fraser, Ph.D.
+44(20)7552-5984 |
georgina.fraser@gs.com
GS International

Marcus von Scheele
+44(20)7774-7676 |
marcus.vonscheele@gs.com
GS International

Thomas Ward  
+44(20)7051-2527 | thomas.ward@gs.com GS International

Gabriel Simoes  
+44(20)7051-6922 | gabriel.simoes@gs.com GS International

for 2026. Cash came in line on OCF and a beat at FCF (due to lower capex). We expect investors to take well the strength of the backlog and NTM of opportunities, especially the clear momentum in Electronics/Carrier Gases projects. As we have seen for quality growth names reporting already this quarter, in-line might not be enough to support the shares today given the c.9% outperformance vs the SX4P YTD, even if there is a lot to like from a mid-term perspective.

## The conference call will be held at 10am UK time.

Exhibit 1: Air Liquide 2Q26 results vs. GSe and Consensus Gas & Services sub-segments on Visible Alpha; remainder on Vara Consensus

<table><tr><td colspan="10">Air Liquide Q2-26</td></tr><tr><td>Euro mn</td><td>2Q 2025 act</td><td>1Q 2026 act</td><td>2Q 2026 est</td><td>2Q 2026 act</td><td>% chg yoy</td><td>% chg qoq</td><td>Consensus</td><td>Actuals vs. GSe</td><td>Actuals vs. Consensus</td></tr><tr><td colspan="10">Sales</td></tr><tr><td>Gas &amp; Services</td><td>6,479</td><td>6,596</td><td>6,764</td><td>6,812</td><td>5.1%</td><td>3.3%</td><td>6,801</td><td>0.7%</td><td>0.2%</td></tr><tr><td>Comp growth (%)</td><td>1.8%</td><td>1.9%</td><td>3.3%</td><td>3.3%</td><td></td><td></td><td>2.9%</td><td>5 bps</td><td>40 bps</td></tr><tr><td>Large Industries</td><td>1,741</td><td>1,834</td><td>1,771</td><td>1,869</td><td>7.4%</td><td>1.9%</td><td>1,867</td><td>5.5%</td><td>0.1%</td></tr><tr><td>Comp growth (%)</td><td>1.0%</td><td>-0.9%</td><td>-1.0%</td><td>-0.3%</td><td></td><td></td><td>-0.2%</td><td>70 bps</td><td>-7 bps</td></tr><tr><td>Industrial Merchant</td><td>3,050</td><td>3,022</td><td>3,190</td><td>3,123</td><td>2.4%</td><td>3.3%</td><td>3,199</td><td>-2.1%</td><td>-2.4%</td></tr><tr><td>Comp growth (%)</td><td>1.8%</td><td>2.7%</td><td>4.5%</td><td>3.8%</td><td></td><td></td><td>3.3%</td><td>-70 bps</td><td>48 bps</td></tr><tr><td>Healthcare</td><td>1,088</td><td>1,112</td><td>1,132</td><td>1,132</td><td>4.0%</td><td>1.8%</td><td>1,147</td><td>0.0%</td><td>-1.3%</td></tr><tr><td>Comp growth (%)</td><td>4.8%</td><td>4.0%</td><td>4.5%</td><td>4.4%</td><td></td><td></td><td>4.4%</td><td>-10 bps</td><td>-5 bps</td></tr><tr><td>Electronics</td><td>600</td><td>628</td><td>672</td><td>688</td><td>14.7%</td><td>9.6%</td><td>652</td><td>2.4%</td><td>5.5%</td></tr><tr><td>Comp growth (%)</td><td>-1.6%</td><td>2.9%</td><td>7.0%</td><td>9.5%</td><td></td><td></td><td>4.6%</td><td>250 bps</td><td>493 bps</td></tr><tr><td>Total Group sales</td><td>6,694</td><td>6,786</td><td>6,986</td><td>7,042</td><td>5.2%</td><td>3.8%</td><td>7,030</td><td>0.8%</td><td>0.2%</td></tr><tr><td>Comp growth (%)</td><td>1.9%</td><td>1.8%</td><td>3.2%</td><td>3.5%</td><td>87.7%</td><td>90.0%</td><td>2.8%</td><td>25 bps</td><td>70 bps</td></tr></table>

Source: Vara Research, Visible Alpha Consensus Data, GS Global Investment Research

Exhibit 2: Air Liquide 1H26 results vs. GSe and Consensus Gas & Services sub-segments on Visible Alpha; remainder on Vara Consensus

<table><tr><td colspan="9">Air Liquide 1H 2026</td></tr><tr><td>Euro mn Sales</td><td>1H 25 Act.</td><td>2H 25 Act.</td><td>1H 2026 Est.</td><td>1H 2026 Act.</td><td>% chg yoy</td><td>% chg hoh</td><td>Consensus</td><td>Actuals vs. Consensus</td></tr><tr><td>Gas &amp; Services</td><td>13,309</td><td>12,776</td><td>13,360</td><td>13,408</td><td>0.7%</td><td>4.9%</td><td>13,396</td><td>0.1%</td></tr><tr><td>Comp growth (%)</td><td>1.8%</td><td>2.2%</td><td>2.6%</td><td>2.6%</td><td></td><td></td><td>2.4%</td><td>20 bps</td></tr><tr><td>Large industries</td><td>3,701</td><td>3,410</td><td>3,605</td><td>3,703</td><td>0.1%</td><td>8.6%</td><td>3,707</td><td>-0.1%</td></tr><tr><td>Comp growth (%)</td><td>0.3%</td><td>0.0%</td><td>-0.9%</td><td>-0.6%</td><td></td><td></td><td>-0.6%</td><td>-3 bps</td></tr><tr><td>Industrial Merchant</td><td>6,193</td><td>5,938</td><td>6,212</td><td>6,144</td><td>-0.8%</td><td>3.5%</td><td>6,216</td><td>-1.2%</td></tr><tr><td>Comp growth (%)</td><td>1.6%</td><td>2.7%</td><td>3.6%</td><td>3.2%</td><td></td><td></td><td>3.1%</td><td>15 bps</td></tr><tr><td>Healthcare</td><td>2,191</td><td>2,186</td><td>2,244</td><td>2,244</td><td>2.4%</td><td>2.7%</td><td>2,265</td><td>-0.9%</td></tr><tr><td>Comp growth (%)</td><td>5.0%</td><td>5.0%</td><td>4.2%</td><td>4.2%</td><td></td><td></td><td>4.4%</td><td>-19 bps</td></tr><tr><td>Electronics</td><td>1,224</td><td>1,242</td><td>1,300</td><td>1,317</td><td>7.6%</td><td>6.0%</td><td>1,280</td><td>2.9%</td></tr><tr><td>Comp growth (%)</td><td>0.9%</td><td>1.5%</td><td>4.9%</td><td>6.2%</td><td></td><td></td><td>3.0%</td><td>316 bps</td></tr><tr><td>Total Group sales</td><td>13,722</td><td>13,218</td><td>13,772</td><td>13,828</td><td>0.8%</td><td>4.6%</td><td>13,815</td><td>0.1%</td></tr><tr><td>Comp growth (%)</td><td>2.0%</td><td>2.1%</td><td>2.5%</td><td>2.6%</td><td></td><td></td><td>2.3%</td><td>30 bps</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBIT (recurring)</td><td>2,737</td><td>2,845</td><td>3,002</td><td>2,893</td><td>5.7%</td><td>1.7%</td><td>2,908</td><td>-0.5%</td></tr><tr><td>Group margin</td><td>19.9%</td><td>21.5%</td><td>21.8%</td><td>20.9%</td><td></td><td></td><td>21.1%</td><td>-13 bps</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating cashflow</td><td>2,977</td><td>3,878</td><td>n/a</td><td>3,372</td><td>13.3%</td><td>-13.1%</td><td>3318</td><td>1.6%</td></tr><tr><td>Capital Expenditure</td><td>(1,836)</td><td>(2,007)</td><td>n/a</td><td>(1,828)</td><td>-0.4%</td><td>-8.9%</td><td>(1,970)</td><td>-7.2%</td></tr><tr><td>FCF</td><td>1,141</td><td>1,871</td><td>n/a</td><td>1,544</td><td>35.3%</td><td>-17.5%</td><td>1,348</td><td>14.5%</td></tr></table>

Source: Vara Research, Visible Alpha Consensus Data, GS Global Investment Research

## Valuation & Risks

## Valuation

We are Buy rated on Air Liquide, with a 12-month price target of €179. Our price target is derived using a two-stage DCF, assuming a WACC of 7.8% and 3.0% terminal growth

rate.

## Risks

Downside risks to our view and price target include:

\- Prolonged economic downturn on the back of global tariff regime impacting Air Liquide's end markets.

■ Continued weakening of the USD against the EUR.

■ Material delays in project start-ups.

■ Pricing pressure in the European/US healthcare markets.

■ Pricing pressure in Industrial Merchant.

■ New entrants to the Industrial Merchant competitive landscape.

■ Slower-than-expected US IP.

\- Slower-than-expected build-out of decarbonization infrastructure/semiconductor fabs.

■ Value-destructive M&A.

<table><tr><td>AIRP.PA</td><td>12m Price Target: €179.00</td><td colspan="2">Price: €177.18</td><td colspan="2">Upside: 1.0%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: €112.4bn / $127.8bn</td><td>Revenue (€ mn)</td><td>26,940.0</td><td>28,006.9</td><td>29,700.9</td><td>31,422.6</td></tr><tr><td>Enterprise value:</td><td>EBIT (€ mn)</td><td>5,581.4</td><td>6,233.6</td><td>6,979.7</td><td>7,572.8</td></tr><tr><td>€122.5bn / $139.4bn</td><td>EPS (€)</td><td>5.90</td><td>6.60</td><td>7.49</td><td>8.18</td></tr><tr><td>3m ADTV: €159.4mn / $184.1mn</td><td>P/E (X)</td><td>26.7</td><td>26.8</td><td>23.7</td><td>21.7</td></tr><tr><td>France</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Europe Chemicals</td><td>EV/EBITDA (ex lease,X)</td><td>13.6</td><td>14.1</td><td>12.9</td><td>12.0</td></tr><tr><td>M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>2.1</td><td>2.0</td><td>2.1</td><td>2.2</td></tr><tr><td>Leases incl. in net debt &amp; EV?:</td><td>FCF yield (%)</td><td>2.5</td><td>3.1</td><td>2.6</td><td>2.9</td></tr><tr><td>Yes</td><td>CROCI (%)</td><td>8.9</td><td>9.0</td><td>9.4</td><td>9.6</td></tr><tr><td></td><td>N debt/EBITDA (ex lease,X)</td><td>1.1</td><td>0.9</td><td>0.8</td><td>0.7</td></tr><tr><td></td><td></td><td>12/25</td><td>6/26E</td><td>12/26E</td><td>6/27E</td></tr><tr><td></td><td>EPS (€)</td><td>3.01</td><td>3.17</td><td>3.43</td><td>3.65</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 27 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Georgina Fraser, Ph.D., Marcus von Scheele, Thomas Ward and Gabriel Simoes, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Georgina Fraser, Ph.D. GS International, Marcus von Scheele GS International, Thomas Ward GS International, Gabriel Simoes GS International.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclosures

The rating(s) for Air Liquide is/are relative to the other companies in its/their coverage universe: Air Liquide, Akzo Nobel, Arkema, BASF SE, Clariant, Croda, DSM-Firmenich, Evonik, Givaudan, Kerry, Lanxess AG, Novonesis, Syensqo, Symrise, Umicore

## Company-specific regulatory disclosures

The following disclosures relate to relationships between The GS Group, Inc. (with its affiliates, “GS”) and companies covered by GS Global Investment Research and referred to in this research.

GS has received compensation for investment banking services in the past 12 months: Air Liquide (€177.18)

GS expects to receive or intends to seek compensation for investment banking services in the next 3 months: Air Liquide (€177.18)

GS has received compensation for non-investment banking services during the past 12 months: Air Liquide (€177.18)

GS had an investment banking services client relationship during the past 12 m

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
