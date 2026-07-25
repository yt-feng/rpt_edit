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
## Holding Up

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>$230.00</td><td>$255.00</td></tr></table>

Source: Company data, MS

TI reported a strong quarter and seasonal outlook, basically meeting elevated expectations; comments about automotive positive sustainability were notable. It's a positive cycle but relative valuation keeps us UW.

## Key Takeaways

■ Consensus beat and raise driven by strength across all end markets.

GM% upside (61.4% JunQ vs 60%) driven by increasing loadings; guided up q/q in SepQ.

CY26 capex guide biased above midpoint ( $2bn-$ 3bn); MSe moves from $2.6bn$ to $2.8bn$ .

TI reported a solid quarter, but was up against heightened expectations going into the print. We had expected TI to have a strong quarter, and raised our JunQ/SepQ estimates to above-seasonality earlier this week, primarily based on positive read-throughs from our Distributor Survey. While the company reported above seasonal q/q growth for both qtrs and above cons GM% – prior to the quarter we believe investors were looking for DD+ sequential revenue growth or confidence in meaningful GM% expansion. We view the quarter as broadly in line with elevated expectations given the GM% print and modest guide-up, but with the bar already high, the slight stock pullback was not surprising.

That said, we acknowledge the recent strength for TI, and our CY26/27 ests come up by 9%/11% primarily on the stronger JunQ print, as we had already given above-seasonal credit to SepQ. Our view is that this time appears to be proving different – recall last JunQ the recovery was narrow and expectations missed after a false start. This quarter, automotive inflected hard (mid-teens YoY, +HSD (q/q) and mgmt characterized demand as "everywhere." The broadening seems to be holding up, but durability post-restocking (particularly in auto) and the GM% ceiling given the depreciation overhang remain the key debates heading into SepQ.

We remain UW. The core bull case still rests on a post-build FCF inflection in 2027, with FCF moving above reported earnings, but comments on the call appear to point to another year of capex at or above depreciation in 2027, unless revenues slow. We

<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Nicole Kozhukhov</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Nicole.Kozhukhov@morganstanley.com</td><td>+1 212 761-1636</td></tr><tr><td colspan="2">Shane Brett</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shane.Brett@morganstanley.com</td><td>+1 212 761-1022</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr></table>

<table><tr><td>Stock Rating</td><td>Underweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>$255.00</td></tr><tr><td>Shr price, close (Jul 22, 2026)</td><td>$294.19</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$273,029</td></tr><tr><td>52-Week Range</td><td>$334.03-152.73</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>5.45</td><td>8.57</td><td>9.80</td><td>10.73</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>7.90</td><td>8.86</td><td>9.79</td></tr><tr><td>P/E</td><td>31.5</td><td>34.4</td><td>29.4</td><td>26.7</td></tr><tr><td>EPS ($)§</td><td>5.48</td><td>7.77</td><td>9.25</td><td>10.72</td></tr><tr><td>Div yld (%)</td><td>3.2</td><td>1.9</td><td>2.1</td><td>2.2</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
§ = Consensus data is provided by Refinitiv Estimates
e = MS estimates

<table><tr><td colspan="6">QUARTERLY EPS ($)</td></tr><tr><td>Quarter</td><td>2025</td><td>2026e Prior</td><td>2026e Current</td><td>2027e Prior</td><td>2027e Current</td></tr><tr><td>Q1</td><td>1.28</td><td>-</td><td>1.68a</td><td>2.09</td><td>2.31</td></tr><tr><td>Q2</td><td>1.41</td><td>-</td><td>2.14a</td><td>2.11</td><td>2.36</td></tr><tr><td>Q3</td><td>1.48</td><td>2.18</td><td>2.43</td><td>2.40</td><td>2.66</td></tr><tr><td>Q4</td><td>1.27</td><td>2.10</td><td>2.31</td><td>2.26</td><td>2.48</td></tr></table>

e = MS estimates, a = Actual Company reported data

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

also continue to think the SLAB acquisition could weigh on the multiple, given how central cash return is to the story. We continue to respect TI mgmt, but against that backdrop still view Analog Devices as the stronger long-term compounder, with TI's much more capital-intensive business model giving it much lower ROIC. That said, we are starting to see higher capacity utilization across the industry, which could mean we have underestimated some of the merits of TI's strategy in a more robust environment.

## What we learned from the call/callback/release:

1.) (+) Cyclical broadening seems durable, with bright spots appearing in Auto. The cycle has been relatively uneven, but last quarter we saw Industrial accelerate meaningfully and demand broaden across end markets. This print showed that strength holding up, with Auto joining the recovery in both units and mix - +mid-teens y/y, +HSD q/q, led by China EVs/hybrids and replenishment from unsustainably low customer inventory levels. Industrial also remained strong at \~30% y/y and \~10% q/q, still 5-6 points below the 2022 peak, with customers "early and not yet building inventory" – a setup that is positive for the broader analog group if demand holds. PE was flat y/y and +HSD q/q, while Comms grew both y/y and q/q despite some supply pressure on PE customers; DC doubled y/y and grew \~20% q/q, with demand remaining strong.

2.) (+) Pricing and supply tightness create \~incremental upside, but the current growth remains primarily demand-driven. TI's pricing increases should phase in through SepQ, DecQ and potentially flow into 2027, and while this is certainly a positive development, the company had already been guiding to stronger 2H pricing since last quarter. At the same time, pricing has been firmer across the analog group more broadly, and TI's pricing actions have been known since last year, limiting how differentiated the upside is for TI over the NT-MT. Mgmt described the pricing contribution to the \~8% q/q SepQ guide as almost insignificant, with the vast majority coming from units. That leaves supply availability as the more tangible NT share opportunity, though it does not come without trade-offs: TI highlighted its competitive lead times, but that availability is supported by \$4.6bn of inventory/196 DOI and therefore comes with a meaningful balance sheet/capital-intensity trade-off. So while we agree TI is positioned to gain some share, the company lost share for several years before stabilizing in 2025, and we expect further gains to remain competitive.

3.) (=) The capacity advantage is increasingly visible, but capex/FCF remains the central LT debate. Loadings increased from MarQ into JunQ and continued to rise throughout the quarter, while inventory allowed TI to respond to demand that developed faster than customer forecasts. TI does not appear close to a structural capacity ceiling: the company has several years of clean room availability and can add tools incrementally across Richardson, Sherman and Lehi. That said, the offset is that stronger demand requires additional equipment and backend capacity, with CY26 capex biased above the midpoint of current guidance (\$2-\$3bn CY26) and a greater proportion of spending moving toward assembly/test, where there are no ITC benefits. We acknowledge that higher revenue, improving loadings and 300mm production support strong incremental fall-through and FCF growth, but the current setup also suggests that capital intensity may remain higher for longer than the

cleanest version of the bull case assumes – and we raise our CY26 capex from \$2.6bn to \$2.8bn for CY26.

## Result Details:

\- JunQ (strong beat MSe & cons). \$5,463mn (up 13.2% q/q and 22.8% y/y) was above MSe and consensus at \$5,264mn/\$5,258mn. Analog sales were up 11.2% q/q and 26.4% y/y, while Embedded Processing was up 9.0% q/q and 16.1% y/y. Gross margin was 61.4%, above MSe and consensus at 60.0%/59.4%. EPS of \$2.14 was above MSe and consensus, both at \$1.94.

\- SepQ (strong beat MSe & cons). Revenue guide of \$5,900mn at the midpoint was above MSe at \$5,706mn and consensus at \$5,626mn. EPS was guided to \$2.40, above MSe and consensus, both at \$2.18.

\- Changes to our estimates: We revise our FY26 revenue/gross margin/EPS estimates to \$22.018bn/60.9%/\$8.57, from \$21.035bn/60.1%/\$7.82 prior, and our FY27 estimates to \$23.832bn/62.7%/\$9.80, from \$22.310bn/62.2%/\$8.50 prior.

\- We leave our multiple unchanged at 26x a slight discount to ADI (28x) and reflects mid-cycle positioning. Based on our new CY27 EPS of \$9.80, our PT moves up from \$230 to \$255.

## Risk Reward – Texas Instruments (TXN.O)

Underweight on limited upside given premium valuation & margin contraction

## PRICE TARGET \$255.00

Represents 26x our CY27e EPS of \$9.80, reflecting mid-cycle positioning, a slight premium to its long-term average of 24x and \~in-line with large-cap analog peers.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/f0f9b3fa090b54a27ef76e3ab9bd79f5dc8e9621d9f2c7c53a06c2d0f183eeb9.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/7c31a37577414fa5f218b6831d7cc405e7a375bfdeb069babb1d6eacfd12d04e.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 22 Jul 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario price in either three-months' or one-years' time. View explanation of Options Probabilities methodology here

## UNDERWEIGHT THESIS

\- TI is looking to ramp capex over the next few years to help bring more manufacturing in-house, but this will act as a near-term headwind to earnings and FCF growth. The company has also seen pricing and market share pressure in personal electronics and enterprise, as customers move to multisource components, and face competition with local Chinese supply.
- The company trades at a premium valuation for its solid governance track record, and we admire the company's long-term direction, but we see this dynamic as limiting upside in the near-term as margin should come under pressure from the capex ramp.

![](images/43c5484be0ccc055b81214b716a7a8a35bf24c5335de22a8db295bd83d07db68.jpg)

## Risk Reward Themes

Pricing Power: Negative View descriptions of Risk Rewards Themes here

## BULL CASE

## \$302.00

## 28x Bull Case 2027e EPS of \$10.78

Rebound in macroeconomic environment drives analog and embedded snapback, and end markets grow more than expected in 2026 & 2027.

\- Revenue growth 14.7% in 2027

-Gross margin expands to $64.2\%$ in 2027

\- EPS of \$10.78 in 2027

## BASE CASE

## \$255.00 BEAR CASE

## 26x Base case 2027e EPS of \$9.80

Assumes a moderate analog and embedded recovery through 2026 & 2027.

\- 24.5% revenue growth in 2026 and 8.2% revenue growth in 2027

\- TXN achieves 60.9% GMs in 2026 and 62.7% in 2027

\- EPS of \$8.57 in CY26 and \$9.80 in CY27

\$213.00

## 24x Bear Case 2027e EPS of \$8.86

Global macroeconomic weakness slows down the recovery in analog and embedded, and end markets remain weak.

\- 1.7% revenue growth in 2027

\- Gross margin of $61.2\%$ in 2027

\- EPS of \$8.86 in 2027

◆ Mean ◆ MS Estimates

## Risk Reward – Texas Instruments (TXN.O)

## KEY EARNINGS INPUTS

<table><tr><td>Drivers</td><td>Dec 2025</td><td>Dec 2026e</td><td>Dec 2027e</td><td>Dec 2028e</td></tr><tr><td>GAAP Revenue ($, mm)</td><td>17,682</td><td>22,018</td><td>23,832</td><td>25,137</td></tr><tr><td>MW Gross Margin (%)</td><td>57.0</td><td>60.9</td><td>62.7</td><td>63.6</td></tr><tr><td>GAAP EPS ($)</td><td>5.45</td><td>8.57</td><td>9.80</td><td>10.73</td></tr><tr><td>Inventory ($, mm)</td><td>4,804</td><td>4,499</td><td>4,222</td><td>3,983</td></tr><tr><td>DOI</td><td>227.6</td><td>188.3</td><td>171.1</td><td>156.8</td></tr></table>

## INVESTMENT DRIVERS

STM/Infineon/Renesas/NXP/MCHP for embedded).

\- How increased capex will impact revenue growth and market share as well as depreciation burden on gross margin.

## GLOBAL REVENUE EXPOSURE

![](images/88729289a3baf4a7fe72bc54c72cb045b8a5ca4689a106a49c65b3fd0af36884.jpg)  
Source: MS Estimate View explanation of regional hierarchies here

## MS ALPHA MODELS

<table><tr><td>5/5BEST</td><td>24 MonthHorizon</td><td>5/5MOST</td><td>3 MonthHorizon</td></tr></table>

Source: Refinitiv, FactSet, MS; 1 is the highest favored Quintile and 5 is the least favored Quintile

## RISKS TO PT/RATING

## RISKS TO UPSIDE

\- Increasing domestic capacity leads to outsized market share gains.

\- Recovery in consumer markets (personal electronics and embedded).

\- Continued content gains in Auto and Industrial end-markets.

## RISKS TO DOWNSIDE

\- Continued market share loss in the embedded business.

\- Pricing and market share pressure from China local capacity.

• Market share loss to ADI in the analog business.

## OWNERSHIP POSITIONING

<table><tr><td>Inst. Owners, % Active</td><td>49.7%</td><td></td></tr><tr><td>HF Sector Long/Short Ratio</td><td>2.1x</td><td></td></tr><tr><td>HF Sector Net Exposure</td><td>29.5%</td><td></td></tr></table>

Refinitiv; MSPB Content. Includes certain hedge fund exposures held with MSPB. Information may be inconsistent with or may not reflect broader market trends. Long/Short Ratio = Long Exposure / Short exposure. Sector % of Total Net Exposure = (For a particular sector: Long Exposure - Short Exposure) / (Across all sectors: Long Exposure – Short Exposure).

MS ESTIMATES VS. CONSENSUS
FY Dec 2026e  
![](images/bf3896568642cc2d334a052d2682cdc4a945bddbd35f1b4653a07c0b4d7ace14.jpg)  
Source: Refinitiv, MS

## Financial Summary

Exhibit 1: Income Statement Summary  
TXN-US: Snapshot for the quarter ended June 2026

<table><tr><td colspan="10">Income Statement</td></tr><tr><td>Qtr Results:</td><td colspan="3">Actual</td><td>Lst Qtr</td><td>QoQ</td><td>Lst Yr</td><td>YoY</td><td>Cons.</td><td>MSe</td></tr><tr><td>Revenue</td><td colspan="3">$5,463.0</td><td>$4,825.0</td><td>13.2%</td><td>$4,448.0</td><td>22.8%</td><td>$5,258.0</td><td>$5,263.8</td></tr><tr><td>Gross Margin</td><td colspan="3">61.4%</td><td>58.0%</td><td>335 bps</td><td>57.9%</td><td>347 bps</td><td>59.4%</td><td>60.0%</td></tr><tr><td>EPS</td><td colspan="3">$2.14</td><td>$1.68</td><td>$0.46</td><td>$1.41</td><td>$0.73</td><td>$1.94</td><td>$1.94</td></tr><tr><td>Nxt Qtr Outlook:</td><td>Low</td><td>High</td><td>Midpoint</td><td rowspan="4"></td><td></td><td></td><td></td

[中间内容因长度限制已省略]

ively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/22/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$552.33</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$16.75</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$49.87</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$69.01</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$66.97</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$386.73</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$330.90</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$396.81</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$209.80</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$58.49</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$102.62</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$34.68</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$210.99</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$85.02</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$959.48</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$12.67</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$212.06</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$278.80</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>++</td><td>$92.33</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$89.48</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>E (06/24/2026)</td><td>$175.63</td></tr><tr><td>Quantinuum (QNT.O)</td><td>E (06/29/2026)</td><td>$54.88</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,599.27</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$136.93</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$217.17</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$63.16</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$294.19</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$29.27</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$283.40</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$337.01</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$377.61</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
