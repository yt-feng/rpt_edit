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
<table><tr><td colspan="2">MS &amp; CO. LLC</td></tr><tr><td colspan="2">Joseph Moore</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Joseph.Moore@morganstanley.com</td><td>+1 212 761-7516</td></tr><tr><td colspan="2">Ella Tulchinsky</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ella.Tulchinsky@morganstanley.com</td><td>+1 212 761-2222</td></tr><tr><td colspan="2">Nicole Kozhukhov</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Nicole.Kozhukhov@morganstanley.com</td><td>+1 212 761-1636</td></tr><tr><td colspan="2">Mason Wayne</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Mason.Wayne@morganstanley.com</td><td>+1 212 761-6012</td></tr><tr><td colspan="2">Shane Brett</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Shane.Brett@morganstanley.com</td><td>+1 212 761-1022</td></tr></table>

# Weekly: Earnings Week 8 MU & CBRS Preview

Raising Micron numbers again as shortages continue to intensify; higher capex and limited LTA disclosure shouldn't hold the story back. Separately we see CBRS posting in line #s for its first public qtr, with visibility into the coming ramp.

CBRS (OW, reporting after the market close on Tuesday, June 23rd): CBRS will report its first quarter as a public company, and while we are not expecting a major surprise, we remain constructive on what we view as a differentiated architecture with significant upside. With large take or pay agreements already in place, the near term story remains centered on execution rather than demand. We continue to view the pace of capacity deployment as the key driver of revenue and gross margin upside, and remain focused on management's progress toward bringing the initial 250MW tranche online, which we currently expect by mid 2027. Longer term, the more important question is whether the Wafer Scale Engine proves to be a durable competitive advantage. The company will need to demonstrate that the technology delivers meaningful value to customers and can scale economically. For now, however, we believe the investment debate is primarily about execution, and we remain constructive.

We model core revenue of \$180 million and core gross margin of 44% for the March quarter, in line with consensus expectations. Looking ahead, we expect core revenue to remain roughly flat in the June quarter while core gross margin declines to 24%, driven by G42 rent back arrangements that support the initial capacity ramp. We expect these arrangements to remain a drag on cloud margins until roughly mid 2027. On a GAAP basis, we forecast revenue of \$182 million in March and \$153 million in June, with the difference between GAAP versus core revenue reflecting mostly warrant related contra revenue. While we think the compute ramp may be somewhat messy near term, with pressure on margins and warrant related costs, we believe these headwinds are well understood by investors. Ultimately, what we are playing for is a differentiated architecture with leadership in one of the fastest growing segments of AI infrastructure, where successful execution could unlock significant upside beyond current expectations.

MU (OW, reporting after market closes on Wednesday, June 24th): Raising numbers again as demand continues to outstrip supply in memory and especially in DRAM, incremental commentary on SCAs (strategic customer agreements) a key focus. Micron's initial guidance for May was revenue growth of 40% q/q, implying ASP increases in both DRAM/NAND of 30-35% or so q/q. Micron has since said conditions are trending better but has not provided a numerical update for investors. We model DRAM ASP's up 45% vs 40% prior, and NAND up 50% vs 35% prior, with third party forecasts calling for \~60% increases in C2Q for DRAM and \~75% for NAND; we don't expect that to come as a surprise to investors. Our

## SEMICONDUCTORS

North America
Industry View
Attractive

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

resulting EPS of \$21.31 compares to consensus at \$20.57. For August we expect pricing up in the 20% range for both DRAM and NAND, with an upward bias to that number as our checks continue to point to very strong market conditions, although negotiations have not yet concluded and but we would expect Micron to remain conservative at the outset.

More important than strong results will be proofpoints on the durability of the current cycle, especially in light of downward LPDDR content adjustments for Rubin. To us that comes back to what are always the two key memory variables, demand and supply. On the demand side the company is unlikely to comment specifically on Rubin, but will likely emphasize that customers in all markets are being forced to make difficult decisions with regards to their volumes and content; to us that's a sign of an enduring shortage and think management at MU will make a similar case. As far as supply, the Tongluo acquisition from PSMC (covered by Daniel Yen) may start to see WFE deliveries quicker than initial expectations, putting an upward bias on current FY capex vs guidance for "above \$25bn" - we raise Aug quarter from \$8bn to \$10bn (FY from \$25bn to \$27bn). Supply growth in DRAM overall continues to come in above out expectations, and will accelerate next year given capital spending this year. But the levels are still much lower than headline WFE would suggest, with construction timelines, HBM trade ratio inputs, and lower node migration efficiency continuing to limit the speed of the supply response and we continue to see q/q bit shipment increases still in the mid single digits vs demand that seems to grow much faster.

What about LTAs? A quarter ago Micron disclosed signing a five year SCA (strategic customer agreement), but with limited information on the terms and sizing of relevant financial commitments. We think Micron may announce the closing of additional deals, but wouldn't necessarily expect more clarity on the terms - as they are likely in conversations with multiple customers and don't want to tip their hand. We think these deals are important for market sentiment around the case for further multiple expansion, and the stock may go down if there's limited new information. But in that we would be looking to add to positions as new disclosures don't change what we know - which is that customers see DRAM as increasingly tight over a multiyear time horizon – something not priced in at 9.3x our new FY27 EPS, in our view.

## Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Cerebras Systems CBRS.O</td></tr><tr><td>Core Revenue</td><td>— In-line</td><td>— Largely unchanged</td></tr></table>

\- While we are not expecting significant upside, we remain constructive on what we view as a differentiated architecture with significant upside.

\*Likely impact to consensus EPS is for the next 12 months

Source: Company data, MS

## Cerebras Earnings Preview

The company is scheduled to report after the market close on Tuesday, June 23rd.

CBRS will report its first quarter as a public company, and while we are not expecting a major surprise, we remain constructive on what we view as a differentiated architecture with significant upside. With large take or pay agreements already in place, the near term story remains centered on execution rather than demand. We continue to view the pace of capacity deployment as the key driver of revenue and gross margin upside, and remain focused on management's progress toward bringing the initial 250MW tranche online, which we currently expect by mid 2027. Longer term, the more important question is whether the Wafer Scale Engine proves to be a durable competitive advantage. The company will need to demonstrate that the technology delivers meaningful value to customers and can scale economically. For now, however, we believe the investment debate is primarily about execution, and we remain constructive.

We model core revenue of \$180 million and core gross margin of 44% for the March quarter, in line with consensus expectations. Looking ahead, we expect core revenue to remain roughly flat in the June quarter while core gross margin declines to 24%, driven by G42 rent back arrangements that support the initial capacity ramp. We expect these arrangements to remain a drag on cloud margins until roughly mid 2027. On a GAAP basis, we forecast revenue of \$182 million in March and \$153 million in June, with the difference between GAAP versus core revenue reflecting mostly warrant related contra revenue. While we think the compute ramp may be somewhat messy near term, with pressure on margins and warrant related costs, we believe these headwinds are well understood by investors. Ultimately, what we are playing for is a differentiated architecture with leadership in one of the fastest growing segments of AI infrastructure, where successful execution could unlock significant upside beyond current expectations.

Exhibit 1: CBRS: MS estimates  
MS Estimates

<table><tr><td colspan="5">Figures in $ MMs</td></tr><tr><td></td><td>F1Q26E</td><td>F2Q26E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Core Rev</td><td>180.4</td><td>180.2</td><td>831.4</td><td>2,694.8</td></tr><tr><td>Q/Q Change</td><td>5.2%</td><td>-0.2%</td><td></td><td></td></tr><tr><td>GAAP Rev</td><td>182.8</td><td>153.0</td><td>792.4</td><td>3,174.3</td></tr><tr><td>Q/Q Change</td><td>6.6%</td><td>-16.3%</td><td></td><td></td></tr><tr><td>Core GM</td><td>43.8%</td><td>24.2%</td><td>29.5%</td><td>51.1%</td></tr><tr><td>Non-GAAP EPS</td><td>$ (0.21)</td><td>$ (0.40)</td><td>$ (1.22)</td><td>$ 0.88</td></tr></table>

Source: MS

## Micron Earnings Preview

The company is scheduled to report after the market close on Wednesday, June 24th.

Raising numbers again as demand continues to outstrip supply in memory and especially in DRAM, incremental commentary on SCAs (strategic customer agreements) a key focus. Micron's initial guidance for May was revenue growth of 40% q/q, implying ASP increases in both DRAM/NAND of 30-35% or so q/q. Micron has since said conditions are trending better but has not provided a numerical update for investors. We model DRAM ASP's up 45% vs 40% prior, and NAND up 50% vs 35% prior, with third party forecasts calling for \~60% increases in C2Q for DRAM and \~75% for NAND for we don't expect that to come as a surprise for investors. Our resulting EPS of \$21.31 compares to consensus at \$20.57. For August we expect pricing up in the 20% range for both DRAM and NAND, with an upward bias to that number as our checks continue to point to very strong market conditions, although negotiations have not yet concluded and but we would expect Micron to remain conservative at the outset.

More important than strong results will be proofpoints on the durability of the current cycle, especially in light of downward LPDDR content adjustments for Rubin. To us that comes back to what are always the two key memory variables, demand and supply. On the demand side, the company is unlikely to comment specifically on Rubin, but will likely emphasize that customers in all markets are being forced to make difficult decisions with regards to their volumes and content; to us that's a sign of an enduring shortage and think management at MU will make a similar case. As far as supply, the Tongluo acquisition from PSMC (covered by Daniel Yen) may start to see WFE deliveries quicker than initial expectations, putting an upward bias on current FY capex vs guidance for "above \$25bn" - we raise Aug quarter from \$8bn to \$10bn (FY from \$25bn to \$27bn). Supply growth in DRAM overall continues to come in above our expectations, and will accelerate next year given capital spending this year. But the levels are still much lower than headline WFE would suggest, with construction timelines, HBM trade ratio inputs, and lower node migration efficiency continuing to limit the speed of the supply response and we continue to see q/q bit shipment increases still in the mid single digits vs demand that seems to grow much faster.

What about LTAs? A quarter ago Micron disclosed signing a five year SCA (strategic customer agreement), but with limited information on the terms and sizing of relevant financial commitments. We think Micron may announce the closing of additional deals, but wouldn't necessarily expect more clarity on the terms - as they are likely in conversations with multiple customers and don't want to tip their hand. We think these deals are important for market sentiment around the case for further multiple expansion, and the stock may go down if there's limited new information. But in that we would be looking to add to positions as new disclosures don't change what we know – which is that customers see DRAM as increasingly tight over a multiyear time horizon – something not priced in at 9.3x our new FY27 EPS, in our view.

Details on the May quarter: We model revenue of \$36.454bn (up 52.8% q/q and 291.9% y/y), above the Street at \$35.555bn. By segment, we model DRAM sequential bit shipments to increase 5.0% q/q and average selling prices to increase 45.0%; and NAND sequential bit shipments to rise 4.0%, with prices up 50.0%. Our gross margin estimate of

83.1% is above the Street at 81.7%, and our EPS estimate of \$21.31 is above the Street at \$20.57.

Outlook on August quarter: We model revenue of \$43.328bn (up 18.9% q/q and 282.9% y/y), ahead of the Street at \$42.688bn. By segment, we forecast DRAM sequential bit shipments to increase by 2.0%, and prices up 15.0%; and NAND bit shipments to increase 4.0%, with prices increasing by 20.0%. We forecast gross margin to come in at 85.1%, ahead of the street at 82.3%, and our EPS estimate of \$26.01 is also ahead of the Street at \$25.00.

Exhibit 2: MU: MS vs. Cons  
MS vs. Consensus

<table><tr><td colspan="9">Figures in $ MMs</td></tr><tr><td rowspan="2"></td><td colspan="2">F3Q26E</td><td colspan="2">F4Q26E</td><td colspan="2">CY2026E</td><td colspan="2">CY2027E</td></tr><tr><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td><td>MS</td><td>Cons.</td></tr><tr><td>Revenues</td><td>36,454</td><td>35,555</td><td>43,328</td><td>42,688</td><td>151,954</td><td>141,640</td><td>220,827</td><td>202,654</td></tr><tr><td>Q/Q Change</td><td>52.8%</td><td>49.0%</td><td>18.9%</td><td>20.1%</td><td></td><td></td><td></td><td></td></tr><tr><td>GMs</td><td>83.1%</td><td>81.7%</td><td>85.1%</td><td>82.3%</td><td>83.3%</td><td>79.5%</td><td>86.4%</td><td>78.3%</td></tr><tr><td>EPS</td><td>$ 21.31</td><td>$ 20.57</td><td>$ 26.01</td><td>$ 25.00</td><td>$ 86.99</td><td>$ 80.46</td><td>$ 128.04</td><td>$ 116.57</td></tr></table>

Source: FactSet, MS estimates

## Risk Reward – Micron Technology Inc. (MU.O)

See multiple quarters of upward revisions, with AI driving a higher multiple

## PRICE TARGET \$1,050.00

\~29.5x through-cycle earnings of US \$35.00, a premium to history reflecting new opportunities in AI, in-line with broader semis.

Consensus Price Target Distribution

Source: Refinitiv, MS

![](images/d5e5ada9df81ab6e5bb44bdaad7a8acaa54a11c4f25d7eca7c01701c5dff42ae.jpg)

## RISK REWARD CHART AND OPTIONS IMPLIED PROBABILITIES (12M)

![](images/23ddd70a2f3c6574ab39d2b052685e332e337b57f1918dca571a496df0fb6198.jpg)  
Key: — Historical Stock Performance ● Current Stock Price ◆ Price Target

Source: Refinitiv, MS, MS Institutional Equities Division. The probabilities of our Bull, Base, and Bear case scenarios playing out were estimated with implied volatility data from the options market as of 18 Jun 2026. All figures are approximate risk-neutral probabilities of the stock reaching beyond the scenario pri

[中间内容因长度限制已省略]

ivity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Semiconductors

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/18/2026)</td></tr><tr><td>Joseph Moore</td><td></td><td></td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$537.37</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$24.39</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$59.00</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$69.97</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$90.46</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$434.46</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$417.07</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$411.35</td></tr><tr><td>Cerebras Systems (CBRS.O)</td><td>O (06/08/2026)</td><td>$234.71</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$85.83</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$133.99</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$56.55</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$310.58</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$99.77</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$1,133.99</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$24.02</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$210.69</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$313.27</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>E (05/11/2025)</td><td>$121.62</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$98.42</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>U (02/10/2026)</td><td>$226.11</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$2,184.75</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$158.23</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$219.75</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$72.45</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$322.86</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$57.41</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$439.46</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$387.39</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$455.51</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
