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
# International Business Machines Corp. (IBM): Ticks down guidance on mainframe pushouts; execution needs to improve for the stock to work

Key stock takeaways: We expect the stock to be range bound following IBM's lowered 2026 guidance, as the magnitude of the guidance cut is likely somewhat less severe than expected, in light of the stock's steep underperformance (down $29\%$ after the negative pre-announcement on July 14). We believe IBM's reduced outlook reflects the ongoing client demand re-prioritization toward near-term server and hardware purchases amid rising memory and component prices, which is weighing on both mainframe hardware and Transaction Processing demand. We were somewhat encouraged by management's commentary on the partial recovery in deal signings which pushed out of 2Q, and IBM's efficiency actions should mitigate near-term downside to EPS and cash flow estimates. However, we believe the company's lower-quality business mix in 2026 (stronger hardware and weaker software) and weak near-term sales execution is likely to weigh on the stock's multiple until management can restore investor confidence in IBM's software growth trajectory and overall financial execution. We are Buy rated on IBM based on our view that the company remains on track to deliver improving software revenue growth and consulting market share gains over time.

Read-through to our coverage: We see IBM's results as a modestly negative read-across for our IT Services coverage, as consulting results in the quarter were slightly weaker against a challenging macro backdrop and tepid reports from peers.

## 2Q revenue results are below the Street, in line with IBM's negative

pre-announcement on July 14: In line with its negative pre-announcement on July 14, IBM reported 2Q26 revenue of \$17.2 bn. Total revenue from continuing operations was up 1% in nominal terms. Software revenue growth of 5% was well below the Street at 11%, Consulting revenue was flat and was below the Street at 2.0%. Infrastructure revenue decreased by 7% and was well below the Street estimate of down 3%. Non-GAAP gross margin of 59.4% came in below the Street at 59.8% and our estimate of 60.1%. Pre-tax margin of 19.2% was above the Street at 18.8% and in line with our estimate of 19.2%. EPS from continuing operations of \$2.93 was below the Street at \$2.98 and our estimate of \$3.06. Free cash flow as of 2Q26 of \$4.8 bn was below the Street at \$5.51 bn, and compares to \$4.81 bn in 1H25.

■ Software: Software revenue was \$7.76 bn (up 4.6% yoy in CC, including an estimated 400-500bps impact from M&A). In line with its pre-announcement, IBM posted better growth in Hybrid Cloud (up 11% in CC), but a contraction in

James Schneider, Ph.D.  
+1(212)357-2929 | jim.schneider@gs.com GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

Transaction Processing (down 9% in CC) given the shortfall in mainframe. Automation (which includes HashiCorp) grew 3% in CC and Data was up 18% (driven mainly by Confluent). IBM now expects Software revenue growth of 6% - 8% (down from over 10% previously) for 2026 given the shortfall in Transaction Processing and Data.

Consulting: Consulting revenue was \$5.33 bn (up 1% in CC). Total consulting signings were \$5.0 bn (up 6% in CC); consulting book-to-bill now stands at 1.05X on a trailing 12-month basis. Within the segment, Strategy and Technology (previously Business Transformation and Technology Consulting) and Intelligent Operations (previously Application Operations and BPO services) both grew 1%. Management still expects low- to mid-single digit growth in Consulting in 2026.

Infrastructure: Infrastructure revenue was \$3.84 bn (down 7.4% yoy in constant currency). Hybrid Infrastructure was down 10% (with IBM Z-series down 42% given the pushout in z17 mainframe purchases and Distributed Infrastructure up 37%), while Infrastructure Support was down 1%. Management now expects Infrastructure to be up low-single digits (up from down low-single digits prior) in 2026, given stronger Power and storage demand offsetting mainframe weakness.

2026 guidance ticked down: For 2026, IBM lowered guidance for constant currency revenue growth to 4% - 5%, down from more than 5% prior (we now model 4.4% CC growth or \$70.46 bn vs. the Street at \$70.49 bn), along with a neutral FX impact of (previously a tailwind of 0.5%-1.0%). IBM maintained its FCF guidance for a \$1.0 bn increase in FCF, which translates to approximately \$15.7 bn in free cash flow (vs. GS at \$15.9 bn and the Street at \$15.3 bn). IBM also guided for PTI margin expansion of 100bps, essentially unchanged relative to prior guidance. By segment, IBM now expects Software to grow revenue by 6% - 8% in CC (down from \~10% CC prior), with Red Hat growth in the double digits and Transaction Processing down low-to-mid single digits. For Consulting, IBM still expects low-to-mid single digit growth. Infrastructure is now expected to grow low-single digits (up from a decline of low-single digits previously given stronger Power and storage demand offsetting mainframe weakness).

Estimate changes: We tick down our EPS estimates to \$12.40/\$13.35/\$14.95 from \$12.50/\$13.50/\$15.20 prior, given lower revenue growth assumptions and FX tailwinds in 2026 and beyond.

Price target update: We lower our 12-month price target to \$270 from \$335 prior, which is based on 20X (down from 25X previously given lower visibility and lower peer multiples) our one-year forward earnings estimates. Downside risks: 1) increased macro headwinds, 2) slowdown in consulting, 3) AI bookings deceleration, 4) dilutive M&A.

We maintain our Buy rating on IBM, as we believe the company is on track to complete its pivot to long-term growth driven by long-term improvements in software growth and consulting market share gains.

Exhibit 1: IBM - Variance summary

<table><tr><td rowspan="2">Financials ($ mn)</td><td colspan="6">2Q26</td></tr><tr><td>Actual</td><td>GS</td><td>Street</td><td>Actual/GS</td><td>Y/Y</td><td>FY26 Guidance</td></tr><tr><td>Software</td><td>7,761</td><td>8,156</td><td>7,938</td><td>-4.8%</td><td>+5.1%</td><td></td></tr><tr><td>Consulting</td><td>5,327</td><td>5,451</td><td>5,379</td><td>-2.3%</td><td>+0.2%</td><td></td></tr><tr><td>Infrastructure</td><td>3,835</td><td>4,047</td><td>3,908</td><td>-5.2%</td><td>-7.4%</td><td></td></tr><tr><td>Financing</td><td>186</td><td>158</td><td>173</td><td>+17.8%</td><td>+12.0%</td><td></td></tr><tr><td>Other</td><td>52</td><td>48</td><td>23</td><td>+8.3%</td><td>-267.7%</td><td></td></tr><tr><td>Total Revenue</td><td>17,162</td><td>17,860</td><td>17,431</td><td>-3.9%</td><td>+1.1%</td><td></td></tr><tr><td>Y/Y (as reported)</td><td>1.0%</td><td>5.2%</td><td></td><td></td><td></td><td></td></tr><tr><td>Y/Y (cc)</td><td>1.0%</td><td>5.1%</td><td></td><td></td><td></td><td>4% - 5%</td></tr><tr><td>Gross Margin (non-GAAP)</td><td>59.4%</td><td>60.1%</td><td>59.1%</td><td>-70 bps</td><td>-69 bps</td><td></td></tr><tr><td>Pre-tax Income Margin (non-GAAP)</td><td>19.2%</td><td>19.2%</td><td>18.8%</td><td>-4 bps</td><td>+37 bps</td><td>~100 bps expansion</td></tr><tr><td>Net Income (non-GAAP)</td><td>2,792</td><td>2,920</td><td>2,774</td><td>-4.4%</td><td>+5.3%</td><td></td></tr><tr><td>EPS (non-GAAP diluted)</td><td>$2.93</td><td>$3.06</td><td>$2.91</td><td>-4.3%</td><td>+4.8%</td><td></td></tr><tr><td>FCF (adjusted)</td><td>2,540</td><td>3,175</td><td>2,795</td><td>-20.0%</td><td>-10.7%</td><td>FY26: &gt;$15.7 bn</td></tr></table>

Source: Company data, Visible Alpha Consensus Data, GS Global Investment Research

Exhibit 2: IBM - Estimate Changes

<table><tr><td rowspan="2">Financials ($ mn)</td><td colspan="4">2026E</td><td colspan="4">2027E</td><td colspan="4">2028E</td></tr><tr><td>GS</td><td>Old</td><td>Y/Y</td><td>Δ</td><td>GS</td><td>Old</td><td>Y/Y</td><td>Δ</td><td>GS</td><td>Old</td><td>Y/Y</td><td>Δ</td></tr><tr><td>Software</td><td>32,046</td><td>33,219</td><td>+7.0%</td><td>-3.5%</td><td>34,757</td><td>35,702</td><td>+8.5%</td><td>-2.6%</td><td>37,029</td><td>38,021</td><td>+6.5%</td><td>-2.6%</td></tr><tr><td>Consulting</td><td>21,493</td><td>21,617</td><td>+2.1%</td><td>-0.6%</td><td>22,434</td><td>22,787</td><td>+4.4%</td><td>-1.5%</td><td>23,556</td><td>24,154</td><td>+5.0%</td><td>-2.5%</td></tr><tr><td>Infrastructure</td><td>16,004</td><td>15,598</td><td>+1.8%</td><td>+2.6%</td><td>15,321</td><td>14,755</td><td>-4.3%</td><td>+3.8%</td><td>17,133</td><td>16,469</td><td>+11.8%</td><td>+4.0%</td></tr><tr><td>Financing</td><td>761</td><td>736</td><td>+3.4%</td><td>+3.5%</td><td>769</td><td>743</td><td>+1.0%</td><td>+3.5%</td><td>826</td><td>797</td><td>+7.4%</td><td>+3.6%</td></tr><tr><td>Other</td><td>160</td><td>156</td><td>+154.0%</td><td>+2.6%</td><td>240</td><td>240</td><td>+50.0%</td><td>+0.0%</td><td>240</td><td>240</td><td>+0.0%</td><td>+0.0%</td></tr><tr><td>Total Revenue</td><td>70,464</td><td>71,325</td><td>+4.3%</td><td>-1.2%</td><td>73,521</td><td>74,227</td><td>+4.3%</td><td>-1.0%</td><td>78,784</td><td>79,682</td><td>+7.2%</td><td>-1.1%</td></tr><tr><td>Y/Y (as reported)</td><td>4.3%</td><td>5.6%</td><td></td><td></td><td>4.3%</td><td>4.1%</td><td></td><td></td><td>7.2%</td><td>7.3%</td><td></td><td></td></tr><tr><td>Y/Y (cc)</td><td>4.4%</td><td>5.2%</td><td></td><td></td><td>4.3%</td><td>4.1%</td><td></td><td></td><td>7.2%</td><td>7.3%</td><td></td><td></td></tr><tr><td>Gross Margin (non-GAAP)</td><td>59.7%</td><td>59.8%</td><td>+16 bps</td><td>-17 bps</td><td>60.1%</td><td>60.1%</td><td>+45 bps</td><td>+0 bps</td><td>60.4%</td><td>60.4%</td><td>+27 bps</td><td>+1 bps</td></tr><tr><td>Pre-tax Income Margin (non-GAAP)</td><td>19.7%</td><td>19.5%</td><td>+90 bps</td><td>+21 bps</td><td>20.5%</td><td>20.4%</td><td>+77 bps</td><td>+6 bps</td><td>21.4%</td><td>21.5%</td><td>+94 bps</td><td>-2 bps</td></tr><tr><td>Net Income (non-GAAP)</td><td>11,841</td><td>11,908</td><td>+7.7%</td><td>-0.6%</td><td>12,805</td><td>12,887</td><td>+8.1%</td><td>-0.6%</td><td>14,439</td><td>14,620</td><td>+12.8%</td><td>-1.2%</td></tr><tr><td>EPS (non-GAAP diluted)</td><td>$12.40</td><td>$12.50</td><td>+7.0%</td><td>-0.7%</td><td>$13.35</td><td>$13.50</td><td>+7.7%</td><td>-1.1%</td><td>$14.95</td><td>$15.20</td><td>+11.9%</td><td>-1.7%</td></tr><tr><td>FCF (adjusted)</td><td>15,969</td><td>15,964</td><td>+8.4%</td><td>+0.0%</td><td>17,166</td><td>17,316</td><td>+7.5%</td><td>-0.9%</td><td>18,075</td><td>18,143</td><td>+5.3%</td><td>-0.4%</td></tr></table>

Source: GS Global Investment Research

Exhibit 3: IBM - Price Target Methodology

<table><tr><td colspan="5">VALUATION METHODOLOGY</td></tr><tr><td>Method</td><td>Metric</td><td>Base</td><td>Bull</td><td>Bear</td></tr><tr><td rowspan="4">P/E Method</td><td>One-Year Forward EPS Estimate</td><td>$13.40</td><td>$14.07</td><td>$12.86</td></tr><tr><td>Multiple</td><td>20.0x</td><td>30.0x</td><td>18.0x</td></tr><tr><td>Valuation</td><td>$270.00</td><td>$422.00</td><td>$231.00</td></tr><tr><td>Upside/Downside</td><td>31.7%</td><td>105.9%</td><td>12.7%</td></tr><tr><td rowspan="4">Price Target</td><td>12-Month Price Target</td><td>$270.00</td><td></td><td></td></tr><tr><td>Potential Upside/Downside</td><td>31.7%</td><td colspan="2">100% P/E</td></tr><tr><td>Dividend Yield at Current Price</td><td>3.3%</td><td></td><td></td></tr><tr><td>Potential Total Return</td><td>35.0%</td><td></td><td></td></tr></table>

Source: GS Global Investment Research

<table><tr><td colspan="2">IBM 12m Price Target: $270.00</td><td colspan="2">Price: $205.77</td><td colspan="2">Upside: 31.2%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: $196.2bn</td><td>Revenue ($ mn) New</td><td>67,535.0</td><td>70,464.2</td><td>73,521.2</td><td>78,783.6</td></tr><tr><td>Enterprise value: $241.3bn</td><td>Revenue ($ mn) Old</td><td>67,535.0</td><td>71,325.0</td><td>74,226.8</td><td>79,681.7</td></tr><tr><td>3m ADTV: $2.8bn</td><td>EBITDA ($ mn)</td><td>19,151.0</td><td>20,855.3</td><td>23,349.1</td><td>24,214.1</td></tr><tr><td>United States</td><td>EBIT ($ mn)</td><td>14,130.0</td><td>15,133.3</td><td>16,549.1</td><td>18,614.1</td></tr><tr><td rowspan="5">Americas Semiconductors &amp; IT Services</td><td>EPS ($) New</td><td>11.59</td><td>12.40</td><td>13.35</td><td>14.95</td></tr><tr><td>EPS ($) Old</td><td>11.59</td><td>12.50</td><td>13.50</td><td>15.20</td></tr><tr><td>P/E (X)</td><td>23.0</td><td>16.6</td><td>15.4</td><td>13.8</td></tr><tr><td>Dividend yield (%)</td><td>2.5</td><td>3.3</td><td>3.3</td><td>3.3</td></tr><tr><td>Net debt/EBITDA (X)</td><td>2.3</td><td>2.2</td><td>1.5</td><td>0.9</td></tr><tr><td></td><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td></td><td>EPS ($)</td><td>2.93</td><td>2.85</td><td>4.70</td><td>2.00</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 22 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, James Schneider, Ph.D., Luya You, Anmol Makkar and Khalil Fenina, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: James Schneider, Ph.D. GS & Co. LLC, Luya You GS & Co. LLC, Anmol Makkar GS & Co. LLC, Khalil Fenina GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a mor

[中间内容因长度限制已省略]

including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY

10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
