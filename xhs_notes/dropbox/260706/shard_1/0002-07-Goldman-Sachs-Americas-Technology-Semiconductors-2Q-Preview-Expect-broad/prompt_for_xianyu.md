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
# Americas Technology: Semiconductors: 2Q Preview: Expect broad upside but run in stocks raises the bar; tactical ideas for earnings

Most estimate upside for SemiCap/Compute/Storage, but risk/reward less positive We see upside to estimates across most sub-sectors of the semiconductor ecosystem heading into 2Q earnings. But following dramatic outperformance for the sector in 2Q (SOX up 88% vs. SPX up 14%), we see a more challenging trading setup ahead of earnings. In compute, given an upward bias to hyperscaler CapEx, we see upside for both server CPUs (increasing AI attach) and key ASIC programs. We see also fundamental upside for the entire memory/storage complex, but prefer HDDs and NAND given a lack of incremental near-term supply additions. We also expect positive estimate revisions for SemiCap companies given pull-ins to WFE spending, and long-term visibility into 2028. Finally, we see upside to analog estimates – and we prefer stocks with the greatest industrial, aero/defense and datacenter exposure.

Tactical Ideas: We see upside for AMAT, AMD, ON; downside for KLAC, ARM, Q AMAT (Buy) – We expect DRAM strength to drive best-in-class growth in 2026, and see visibility into 2028 and potential pricing tailwinds driving the stock higher.

AMD (Buy) - We see upside in the quarter driven mainly by server CPUs, with some level of potential offset in terms of PC downside; we see a favorable setup for the stock driven by strength in Server CPUs.

ON (Neutral) - We expect some upside to the Street for the quarter set against somewhat lowered investor expectations following a proposed acquisition; we thus see a favorable risk/reward for the stock heading into earnings.

KLAC (Neutral) - Despite modest upside to the quarter/guidance, we expect results to lag peers, as WFE spending is skewed toward DRAM, where inspection/metrology intensity is lower.

ARM (Sell) – We expect ARM to report a modestly below 3Q guide, driven by persistent weakness in smartphone market and higher than expected OpEx.

Q (Buy) - We are constructive on the prospects for ongoing growth at Qnity, but believe risk/reward is less skewed to the downside given the run in the stock.

James Schneider, Ph.D.
+1(212)357-2929 |
jim.schneider@gs.com
GS & Co. LLC

Anmol Makkar
+1(212)357-1366 |
anmol.makkar@gs.com
GS & Co. LLC

Luya You
+1(212)902-5297 | luya.you@gs.com
GS & Co. LLC

Khalil Fenina
+1(212)357-6392 |
khalil.fenina@gs.com
GS & Co. LLC

## Table of Contents

<table><tr><td>Digital Semiconductors &amp; EDA Software</td><td>3</td></tr><tr><td>AMD (AMD, Buy): Expect strong server CPU demand, with Advancing AI event a positive catalyst</td><td>4</td></tr><tr><td>Arm Holdings (ARM, Sell): Focus on AGI CPU supply, FY27 royalty growth, and OpEx outlook</td><td>5</td></tr><tr><td>Cadence (CDNS, Buy): Expect increased 2026 guidance as agentic tools drive monetization</td><td>6</td></tr><tr><td>Intel (INTC, Neutral): Focus on Foundry progress and upside to Server CPUs</td><td>7</td></tr><tr><td>Qualcomm Inc. (QCOM, Neutral): Focus on FY27 datacenter outlook and smartphone trends</td><td>8</td></tr><tr><td>Analog Semiconductors</td><td>9</td></tr><tr><td>Microchip (MCHP, Buy): Expect another beat-and-raise quarter, with focus on margin trajectory</td><td>10</td></tr><tr><td>NXP Semiconductors (NXPI, Buy): Expect a robust quarter to boost investor confidence</td><td>11</td></tr><tr><td>onsemi (ON, Neutral): Expect a positive quarter, with focus on datacenter and latest acquisition</td><td>12</td></tr><tr><td>SiTime Corp. (SITM, Buy): Expect upside to estimates, driven by strength in datacenter and aerospace</td><td>13</td></tr><tr><td>Texas Instruments (TXN, Sell): Expect a strong quarter, with a focus on end markets and factory loading</td><td>14</td></tr><tr><td>Semiconductor Capital Equipment &amp; Foundry</td><td>15</td></tr><tr><td>Applied Materials (AMAT, Buy): Expect strong numbers, with upside in 2027 and pricing key swing factors</td><td>16</td></tr><tr><td>Amkor (AMKR, Neutral): We expect investors to focus on 2.5D momentum and Arizona facility progress</td><td>17</td></tr><tr><td>Camtek (CAMT, Neutral): Expect investor focus on HBM4 ramp, packaging share, and 2027 visibility</td><td>18</td></tr><tr><td>Entegris (ENTG, Sell): Expect investors to focus on unit-driven recovery, content gains and deleveraging</td><td>19</td></tr><tr><td>GlobalFoundries (GFS, Neutral): Expect focus on SiPh/CPO trajectory, mature node recovery and pricing</td><td>20</td></tr><tr><td>KLA (KLAC, Neutral): Expect focus on process control intensity given leading-edge dollar content</td><td>21</td></tr><tr><td>Lam Research (LRCX, Buy): Expect focus on potential WFE upside into 2027 &amp; timing of NAND cycle</td><td>22</td></tr><tr><td>MKS (MKSI, Sell): We expect investor focus on WFE outgrowth, packaging momentum, deleveraging</td><td>23</td></tr><tr><td>Qnity (Q, Buy): We expect investors to focus on wafer starts upside and operational execution</td><td>24</td></tr><tr><td>Teradyne (TER, Buy): Expect focus on 2H revenue, memory test recovery and merchant GPU share</td><td>25</td></tr><tr><td>Memory and Storage</td><td>26</td></tr><tr><td>SanDisk (SNDK, Buy): Expect a very strong quarter, with focus on customer agreements</td><td>27</td></tr><tr><td>Seagate (STX, Buy): Positive HDD pricing and margin upside remain key swing factors</td><td>28</td></tr><tr><td>Western Digital (WDC, Neutral): Expect focus on HDD tightness and long-term gross margin upside</td><td>29</td></tr><tr><td>Disclosure Appendix</td><td>30</td></tr></table>

## Digital Semiconductors & EDA Software

## AMD (AMD, Buy): Expect strong server CPU demand, with Advancing AI event a positive catalyst

Key stock takeaways: We expect a strong quarter and guidance, with investors focusing on potential upside to Server CPU demand and the MI450 ramp in 2H. We believe upside to server CPU demand, quantification of the MI450 ramp in 2H, and comments on new customer engagements should drive 2027 datacenter estimates and the stock higher. Our 2027 EPS estimate of \$14.50 is 13% above Street.

Setup heading into the print: We see a constructive setup heading into the quarter driven by CPU demand for agentic AI and AI infrastructure spending.

Our view on key metrics and our estimates: We expect upside to 2Q results and 3Q guidance, driven by Datacenter strength, partly offset by tepid PC trends. Our 2Q and 3Q EPS estimates are 1% above Street (3Q Datacenter revenue estimate 2% is above).

Items on the call that could move the stock: (1) Potential server CPU upside: AMD guided for 70% YoY growth in server CPU revenues for 2Q, and we believe commentary on agentic AI driving server CPU demand could drive upside to datacenter estimates; (2) Updates on Meta / OpenAI deployment and overall MI450 contribution: Incremental detail on Meta and OpenAI partnerships and any quantification of MI450 contribution in 2H could improve confidence in Datacenter GPU revenue in 2027; (3) Margin progression: Commentary on gross margins and OpEx leverage could be impactful.

Coming out of the print: We expect (1) quantification of MI450 ramp in 2H, datapoints on new customer engagements and upside to 2027 Datacenter GPU estimates; (2) potential upside to server CPU revenues driven by agentic AI to be key stock drivers.

Advancing AI day on July 23 should be a positive catalyst: We expect AMD's Advancing AI day on July 23 to be a positive catalyst. We expect AMD to share constructive outlook for the strength and sustainability in server CPU demand, along with incremental details on Datacenter GPU customer engagements.

Estimate changes: We increase our EPS estimates by \~7% on average driven by higher Server CPU revenues and higher margins.

Exhibit 1: AMD - Summary of GS vs. Street estimates
Note: Our 2028E EPS moves from \$18.00 to \$19.40.

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="5">2Q26E</td><td colspan="5">3Q26E</td><td colspan="4">2026E</td><td colspan="4">2027E</td></tr><tr><td>New</td><td>Old</td><td>Change (%)</td><td>Street</td><td>GS / Street</td><td>New</td><td>Old</td><td>Change (%)</td><td>Street</td><td>GS / Street</td><td>New</td><td>Old</td><td>Street</td><td>GS / Street</td><td>New</td><td>Old</td><td>Street</td><td>GS / Street</td></tr><tr><td>Total Revenue</td><td>11,258</td><td>11,223</td><td>0%</td><td>11,277</td><td>0%</td><td>12,348</td><td>11,994</td><td>3%</td><td>12,441</td><td>-1%</td><td>50,573</td><td>49,661</td><td>50,070</td><td>1%</td><td>86,013</td><td>83,301</td><td>75,899</td><td>13%</td></tr><tr><td>Gross Margin (excl. SBC)</td><td>56.3%</td><td>56.1%</td><td>+16 bps</td><td>56.1%</td><td>+19 bps</td><td>56.7%</td><td>56.2%</td><td>+45 bps</td><td>55.8%</td><td>+94 bps</td><td>55.7%</td><td>55.4%</td><td>55.0%</td><td>+67 bps</td><td>54.2%</td><td>53.7%</td><td>54.8%</td><td>-58 bps</td></tr><tr><td>Operating Income (excl. SBC)</td><td>3,020</td><td>2,982</td><td>1%</td><td>3,001.6</td><td>1%</td><td>3,441</td><td>3,186</td><td>8%</td><td>3,456.4</td><td>0%</td><td>14,352</td><td>13,680</td><td>13,921</td><td>3%</td><td>27,846</td><td>25,902</td><td>24,800</td><td>12%</td></tr><tr><td>Operating Margin (%)</td><td>26.8%</td><td>26.6%</td><td>+26 bps</td><td>26.6%</td><td>+21 bps</td><td>27.9%</td><td>26.6%</td><td>+130 bps</td><td>27.8%</td><td>+8 bps</td><td>28.4%</td><td>27.5%</td><td>27.8%</td><td>+58 bps</td><td>32.4%</td><td>31.1%</td><td>32.7%</td><td>-30 bps</td></tr><tr><td>EPS (excl. SBC)</td><td>$1.61</td><td>$1.59</td><td>1%</td><td>$1.60</td><td>1%</td><td>$1.83</td><td>$1.70</td><td>8%</td><td>$1.81</td><td>1%</td><td>$7.65</td><td>$7.30</td><td>$7.44</td><td>3%</td><td>$14.50</td><td>$13.50</td><td>$12.87</td><td>13%</td></tr><tr><td>Segments</td><td>New</td><td>Old</td><td>Change (%)</td><td>Street</td><td>GS / Street</td><td>New</td><td>Old</td><td>Change (%)</td><td>Street</td><td>GS / Street</td><td>New</td><td>Old</td><td>Street</td><td>GS / Street</td><td>New</td><td>Old</td><td>Street</td><td>GS / Street</td></tr><tr><td>Client</td><td>2,861</td><td>2,934</td><td>-2%</td><td>2,970</td><td>-4%</td><td>2,859</td><td>2,853</td><td>0%</td><td>3,008</td><td>-5%</td><td>11,503</td><td>11,507</td><td>11,922</td><td>-4%</td><td>11,906</td><td>12,005</td><td>12,218</td><td>-3%</td></tr><tr><td>Data Center</td><td>6,688</td><td>6,586</td><td>2%</td><td>6,553</td><td>2%</td><td>7,784</td><td>7,431</td><td>5%</td><td>7,656</td><td>2%</td><td>32,381</td><td>31,457</td><td>31,348</td><td>3%</td><td>66,682</td><td>63,948</td><td>56,590</td><td>18%</td></tr><tr><td>Gaming</td><td>748</td><td>742</td><td>1%</td><td>791</td><td>-5%</td><td>669</td><td>672</td><td>0%</td><td>747</td><td>-11%</td><td>2,739</td><td>2,748</td><td>2,942</td><td>-7%</td><td>3,137</td><td>3,059</td><td>3,025</td><td>4%</td></tr><tr><td>Embedded</td><td>960</td><td>960</td><td>0%</td><td>966</td><td>-1%</td><td>1,037</td><td>1,037</td><td>0%</td><td>1,013</td><td>2%</td><td>3,949</td><td>3,949</td><td>3,931</td><td>0%</td><td>4,289</td><td>4,289</td><td>4,393</td><td>-2%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

## Price Target Methodology and Risks

We are Buy rated on AMD. Our 12-month target price of \$640 (up from \$450) is based on a 32X P/E multiple (up from 30X on faster DC growth) applied to our normalized EPS estimate of \$20 (up from \$15 on higher estimates and better visibility). Key downside risks include: (1) slower than expected adoption of agentic AI; (2) slower than anticipated deployment of AMD GPUs related to the Meta deal; (3) share erosion of x86 architecture in enterprise AI and (4) lack of operating leverage.

## Arm Holdings (ARM, Sell): Focus on AGI CPU supply, FY27 royalty growth, and OpEx outlook

Key stock takeaways: We expect investors to focus on supply availability for incremental AGI CPU demand. We also expect investors to focus on FY27 royalty revenue commentary as they weigh the near-term strength in server CPUs against smartphone unit weakness. We believe expectations are elevated given the significant run-up in the stock.

Setup heading into the print: We believe expectations are elevated as (1) investors look for details on supply procurement and quantitative upside to AGI CPU revenue guidance; and (2) AI related spending remains strong, which should benefit ARM's datacenter royalty business.

Our view on key metrics and our estimates: We expect an in-line quarter with EPS guidance modestly below consensus, driven by elevated OpEx. We also note near-term risk to the royalty business driven by persistent smartphone weakness.

Items on the call that could move the stock: (1) Supply availability and potential upside to FY27 AGI CPU revenue: Recall that management had noted \$2bn in demand for its AGI CPU in FY27-28, but cited supply constraints tied to an incremental \$1bn of demand. Any progress on supply procurement and margins for this business could move the stock; (2) Smartphone demand and impact on royalty revenues: Thoughts on persistent smartphone market weakness and its impact on ARM's royalty business could be impactful; (3) Margin progression: Any incremental thoughts on direction of travel for gross and operating margin as ARM ramps its gross margin-dilutive AGI CPU business could move the stock in either direction.

Coming out of the print: We expect (1) procurement of additional supply to satisfy demand for AGI CPU, (2) new customer engagements for the AGI CPU, and (3) sustainability of AI related spending and its impact on the royalty business to be key drivers of the stock.

Exhibit 2: ARM - Summary of GS vs Street estimates

<table><tr><td rowspan="2">Financials ($ mn, except EPS)</td><td colspan="3">CY2Q26E</td><td colspan="3">CY3Q26E</td><td colspan="3">CY2026E</td><td colspan="3">CY2027E</td></tr><tr><td>GS</td><td>Street</td><td>GS / Street</td><td>GS</td><td>Street</td><td>GS / Street</td><td>GS</td><td>Street</td><td>GS / Street</td><td>GS</td><td>Street</td><td>GS / Street</td></tr><tr><td>Total Revenue</td><td>1,262</td><td>1,266</td><td>0%</td><td>1,300</td><td>1,338</td><td>-3%</td><td>5,585</td><td>5,731</td><td>-3%</td><td>7,400</td><td>7,526</td><td>-2%</td></tr><tr><td>Gross Margin (excl. SBC)</td><td>98.6%</td><td>98.2%</td><td>+40 bps</td><td>98.7%</td><td>98.7%</td><td>+4 bps</td><td>98.6%</td><td>97.6%</td><td>+98 bps</td><td>91.9%</td><td>93.2%</td><td>-124 bps</td></tr><tr><td>Operating Income (excl. SBC)</td><td>484</td><td>481</td><td>1%</td><td>486</td><td>525</td><td>-7%</td><td>2,385</td><td>2,477</td><td>-4%</td><td>3,181</td><td>3,371</td><td>-6%</td></tr><tr><td>Operating Margin (%)</td><td>38.4%</td><td>38.0%</td><td>+38 bps</td><td>37.4%</td><td>39.2%</td><td>-180 bps</td><td>42.7%</td><td>43.2%</td><td>-52 bps</td><td>43.0%</td><td>44.8%</td><td>-182 bps</td></tr><tr><td>EPS (excl. SBC)</td><td>$0.41</td><td>0.41</td><td>1%</td><td>$0.41</td><td>0.44</td><td>-7%</td><td>$1.98</td><td>2.05</td><td>-3%</td><td>$2.62</td><td>2.81</td><td>-7%</td></tr><tr><td>Segments</td><td>GS</td><td>Street</td><td>GS / Street</td><td>GS</td><td>Street</td><td>GS / Street</td><td>GS</td><td>Street</td><td>GS / Street</td><td>GS</td><td>Street</td><td>GS / Street</td></tr><tr><td>Licensing</td><td>561</td><td>568</td><td>-1%</td><td>550</td><td>588</td><td>-7%</td><td>2,623</td><td>2,634</td><td>0%</td><td>3,006</td><td>3,045</td><td>-1%</td></tr><tr><td>Royalty</td><td>701</td><td>696</td><td>1%</td><td>750</td><td>749</td><td>0%</td><td>2,962</td><td>3,021</td><td>-2%</td><td>3,643</td><td>3,678</td><td>-1%</td></tr></table>

Source: Company data, GS Global Investment Research, Visible Alpha Consensus Data

We are Sell rated on ARM. Our 12-month price target of \$150 is based on 50X our norm

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
