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
# The Road to ROI: Patience Required

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Tesla Inc (TSLA.O)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>$417.00</td><td>$400.00</td></tr></table>

We view Tesla's accelerating capex cycle as a necessary investment to secure leadership in autonomy & robotics. However, these investments push FCF further into negative territory, increasing focus on tangible Robotaxi & Optimus milestones. We lower our PT to \$400 reflecting elevated cash burn.

## Key Takeaways

■ TSLA remains positioned to lead in Physical AI, but the ROI on a heavy capex cycle requires patience and consistent execution.

FSD adoption was an upside surprise, with North America attach rates reaching 55% in the quarter, far surpassing our 25-30% estimate.

■ Robotaxi commentary was upbeat; we need density + larger sample of safety data within existing cities, not just geographic expansion.

■ Cybercab production is scaling, but software recalibration limits near-term fleet entry.

\- Optimus SOP is expected soon. Supply chain complexities elongate the initial ramp.

Nothing this quarter changes our thesis in a meaningful way. The capex step-up is a known trend, now confirmed and extended for the next 2-3 years, prolonging cash burn through the end of the decade on our estimates. We view this as a necessary investment to establish and defend a leadership position in autonomy and robotics. The open question remains the timing of when we actually see the ROI – specifically, a scaled robotaxi network that demonstrates increasing density and improving safety within existing cities, plus tangible progress commercializing Optimus. Absent consistent, transparent proof points, we'd expect the market's tolerance for incremental capex to narrow. We are lowering our price target to \$400 (from \$417) reflecting increasing capex and worsening cash burn through the end of the decade. Our long-term estimates are broadly unchanged.

<table><tr><td colspan="2">Andrew S Percoco</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Andrew.Percoco@morganstanley.com</td><td>+1 212 296-4322</td></tr><tr><td colspan="2">Daniela M Haigian</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daniela.Haigian@morganstanley.com</td><td>+1 212 761-6071</td></tr><tr><td colspan="2">Jahvonte G Bain</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Jahvonte.Bain@morganstanley.com</td><td>+1 212 761-9231</td></tr><tr><td colspan="2">Katherine A Bennorth</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Katie.A.Bennorth@morganstanley.com</td><td>+1 212 761-3753</td></tr></table>

<table><tr><td>Stock Rating</td><td>Equal-weight</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>$400.00</td></tr><tr><td>Shr price, close (Jul 22, 2026)</td><td>$374.01</td></tr><tr><td>Mkt cap, curr (mm)</td><td>$1,323,247</td></tr><tr><td>52-Week Range</td><td>$498.83-297.82</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS ($)**</td><td>1.67</td><td>1.70</td><td>2.07</td><td>2.69</td></tr><tr><td>Prior EPS ($)**</td><td>-</td><td>2.20</td><td>2.50</td><td>3.11</td></tr><tr><td>ModelWare EPS ($)</td><td>1.07</td><td>0.71</td><td>0.76</td><td>1.39</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework
\*\* = Based on consensus methodology
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

![](images/ff15f1281561dfdaccf1bfbfa379f8b66886a5502746e21aa1a61f1050df602f.jpg)  
Source: MS estimates

## What did we learn from the quarter?

\- Robotaxi: new unsupervised miles driven disclosure and growth target (DD% w/w growth through YE). Tesla disclosed a total of 380k cumulative unsupervised robotaxi miles driven to date (in TX/FL), vs. the company's disclosed cumulative 2.5mn paid robotaxi miles driven (across Texas, Florida, and the Bay Area). According to the company, no notable incidents were reported over those unsupervised miles, which is broadly consistent with the NHTSA data we track monthly. Weekly unsupervised miles have grown DD% w/w and are expected to continue at that pace through year-end. Notably, the robotaxi fleet is already operating early versions of v15 FSD software.

Exhibit 2: TSLA Robotaxi Fleet Size ('000)  
![](images/8f571b219fd01154a8a38d871762f7899c97400cbac86a6ca274492329fafa29.jpg)  
Exhibit 3: TSLA Robotaxi Passenger Miles (bn)  
Source: MS estimates

![](images/fe60a83ba7c10edaf730d78a6265c382aa2352121fea9890a15ce6d36db97c04.jpg)  
Source: MS estimates

\- Cybercab: Testing and validating v15 FSD on new chassis. Cybercab manufacturing targets are now aligned to the projected growth rate of unsupervised miles. Before Cybercabs can be deployed in the fleet, the company needs to accumulate driving data specific to the Cybercab's new vehicle chassis to calibrate the software.

\- FSD: 12.6bn miles traveled, 1.5mn active subs, 55% attach rate on NA deliveries in 2Q. TSLA disclosed a 55% attach rate of FSD on incremental volume in North America, well above our prior assumption of \~25-30%. This is a strong indicator that consumers are buying TSLA vehicles for FSD, which we've long written is a growing competitive moat. This updated disclosure and commentary supports our view that global attach rates will reach 40% by 2030 and 80% by 2040 (still subject to international regulatory approval). No update on unsupervised FSD, though the company discussed unsupervised robotaxi progress on v15, which is supportive of future rollout to passenger vehicles.

Exhibit 4: FSD Penetration  
![](images/3eac4ae1c9e87609d1dc2356c08429f3d13757d798ac1725d392250ec1e56c9a.jpg)  
Source: MS estimates

\- Optimus: SOP expected to start soon. Complexity of supply chain likely to weigh on pace of initial ramp. Management provided limited new commentary on production readiness during the call, and Musk again reiterated the challenge of building new supply chains that do not yet exist, designing a sufficiently dexterous robot ('human, and then superhuman dexterity'), and developing the tech that enables a humanoid robot to be able to perform generalized tasks (vs. pre-programmed or remote controlled). While we remain bullish on the Humanoid TAM longer term, we maintain our conservative adoption estimates through the end of the decade (see Exhibit 5).

Exhibit 5: Optimus Deployments  
![](images/ca06ac106690851bac9724361330efe92452e4b02464d3df0d9ba8a910890ab6.jpg)  
Source: MS estimates

\- TeraFab: details imminent. Management flagged an upcoming TeraFab event. Recall, TeraFab is a collaboration between Tesla and SpaceX (covered by Adam Jonas). Based on prior commentary, the expectation is that the bulk of the associated capex will sit with SpaceX, though we await a more comprehensive update.

\- Energy. Normalizing for 1Q tariff benefits (\$200mn) and 2Q warranty charges (\$240mn), Energy gross margin fell \~300 bps q/q to 28% due to lower ASPs amid growing competition. Management expects robust growth to continue due to a healthy backlog and demand tied to the data center buildout and broader electrification. However, long-term gross margins are expected to compress to the low-to-mid 20% range. As such, we have lowered our 2030+ gross margin assumption by 150 bps to 23.5%. The company also reiterated its commitment to establishing fully vertically integrated solar manufacturing in the US (silicon refining through to the panel). Separately, management detailed a “megapod” design, pairing Tesla AI4 and x86 compute in a shippable enclosure that can be placed anywhere power is available — including at Tesla's Supercharger network (\~7 GW and growing). The concept effectively pairs distributed power with distributed inference and could add a further demand vector for Megapack over time.

Exhibit 6: ESS Deployments  
![](images/6c353eb3ad7104ffa2fabaa8208a88b2b20733d3b59bfcb711eb98da9570ec8b.jpg)  
Source: MS estimates

\- CapEx. Management reiterated the 2026 CapEx guide of more than \$25bn and, notably, expects CapEx to increase over the next 2-3 years as Tesla expands the Robotaxi fleet, Optimus capacity, the semiconductor fab, solar manufacturing and AI compute - a step-up versus our prior assumption of a moderating CapEx profile. Beyond cash generated from operations and cash on hand, management noted it is opportunistically securing debt facilities that would provide capacity to borrow up to \$30bn to accelerate these investments.

Exhibit 7: Capital Expenditures and FCF  
![](images/f786b83e5b75ab44be6a120c3d9d52bb6698f05362903a7b5a685fef194d1140.jpg)  
Source: MS estimates

How our estimates are changing. We assume lower gross margins in auto and energy carry through the remainder of the year, while continued R&D growth adds further margin pressure. In total, our 2026 adj. EBITDA estimates decline by 7% with these changes. This also carries forward to 2027 where we expect Energy margins to remain under pressure and R&D to continue to grow as Tesla further invests in Optimus, semi manufacturing, etc. As a result, our 2027 adj. EBITDA estimate declines by 12%. The biggest change in our 2027 estimates is capex, where we now assume the company spends nearly \$30bn (vs. \$20bn previously). Our higher capex and lower EBITDA estimates drives a FCF burn of \~\$14bn in 2027 (vs. \$5bn previously).

## Changes to Valuation

\- Our Base Case PT of \$400. Our \$400 PT is comprised of 5 DCF-driven components: (1) \$45/share for core Tesla Auto business on \~8.5mm units in 2040, 8.4% exit EBIT margin (ex-FSD), 10.9% WACC, and 10x 2040 exit EBITDA multiple. (2) Network Services at \$144/share, 80% attach rate at \$240/month ARPU by 2040 (3) Tesla Mobility at \$120/share on DCF with \~5mn cars at \~\$1.33/mile by 2040. (4) Energy at \$35/share (16% 15yr rev CAGR and 17% terminal EBIT margin), and (5) Humanoids at \$56/share (50% probability discount).

\- Our Bull Case PT of \$821. For core auto, we assume TSLA is able to deliver \~12.5mm units by 2040 with \~13.5% EBIT margin (ex-FSD), implying \~\$82/share. TSLA Network Services valued at \$257/share, on 90% attach rate at \~\$250 Monthly ARPU by 2040. We value TSLA Mobility at \$201/share with 8.5mn fleet and 30% EBITDA margin in 2040. For Energy, \$82/share (21% 15yr rev CAGR and 21% terminal EBIT margin). Tesla Humanoids at \$199/share (0% probability discount).

\- Our Bear Case PT of \$130. Our \$130 bear case ascribes \$24/share for automotive which assumes \~6.0mn units by 2040 at a 3.4% EBIT margin (ex-FSD). Tesla Network Services at \$51/share (60% attach rate at \$200

Monthly ARPU by 2040). Other value is ascribed to Tesla Mobility at \$39/share on a 2mn car fleet and \~40% EBITDA margin by 2040, and Tesla Energy at \$16/share (\~15% 15 yr rev CAGR and 13% terminal EBIT margin). Humanoids at \$0/share.

For our Tesla deep-dive, see: Beyond the Wheel – Mapping Tesla's Journey into Physical AI.

Exhibit 8: SOTP Bridge: Changes to PT  
![](images/14ceeba602ff0259dd6f6620b3d52aba0ec51f1415df9281400066f0d0b98acd.jpg)  
Source: MS estimates

Exhibit 9: Changes to Estimates

<table><tr><td rowspan="2">Income Statement ($MM)</td><td colspan="3">2026e</td><td colspan="3">2027e</td></tr><tr><td>New</td><td>Old</td><td>Δ</td><td>New</td><td>Old</td><td>Δ</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Auto</td><td>72,149</td><td>72,158</td><td>0.0%</td><td>78,496</td><td>77,732</td><td>1.0%</td></tr><tr><td>Energy + Services and Other</td><td>30,621</td><td>30,254</td><td>1.2%</td><td>40,572</td><td>39,854</td><td>1.8%</td></tr><tr><td>ZEV Credit</td><td>1,192</td><td>1,430</td><td>-16.7%</td><td>1,113</td><td>1,113</td><td>0.0%</td></tr><tr><td>Total Revenue</td><td>102,770</td><td>102,412</td><td>0.3%</td><td>119,068</td><td>117,586</td><td>1.3%</td></tr><tr><td>COGS</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Auto</td><td>58,645</td><td>58,066</td><td>1.0%</td><td>63,847</td><td>62,941</td><td>1.4%</td></tr><tr><td>Energy + Services and Other</td><td>24,970</td><td>24,516</td><td>1.9%</td><td>33,740</td><td>32,695</td><td>3.2%</td></tr><tr><td>Gross Profit</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Auto Gross Profit</td><td>13,504</td><td>14,092</td><td>-4.2%</td><td>14,650</td><td>14,791</td><td>-1.0%</td></tr><tr><td>% Gross Margin</td><td>18.7%</td><td>19.5%</td><td>-0.8%</td><td>18.7%</td><td>19.0%</td><td>-0.4%</td></tr><tr><td>% Gross Margin (ex. ZEV)</td><td>17.4%</td><td>17.9%</td><td>-0.6%</td><td>17.5%</td><td>17.9%</td><td>-0.4%</td></tr><tr><td>Energy + Services and Other Gross Profit</td><td>5,651</td><td>5,738</td><td>-1.5%</td><td>6,832</td><td>7,159</td><td>-4.6%</td></tr><tr><td>% Gross Margin</td><td>18.5%</td><td>19.0%</td><td>-0.5%</td><td>16.8%</td><td>18.0%</td><td>-1.1%</td></tr><tr><td>Total Gross Profit</td><td>19,155</td><td>19,830</td><td>-3.4%</td><td>21,481</td><td>21,950</td><td>-2.1%</td></tr><tr><td>% Gross Margin</td><td>18.6%</td><td>19.4%</td><td>-0.7%</td><td>18.0%</td><td>18.7%</td><td>-0.6%</td></tr><tr><td>R&amp;D</td><td>9,344</td><td>7,889</td><td>18.4%</td><td>10,278</td><td>8,442</td><td>21.8%</td></tr><tr><td>% of Sales</td><td>9.1%</td><td>7.7%</td><td>1.4%</td><td>8.6%</td><td>7.2%</td><td>1.5%</td></tr><tr><td>SG&amp;A</td><td>7,852</td><td>7,750</td><td>1.3%</td><td>8,335</td><td>7,937</td><td>5.0%</td></tr><tr><td>% of Sales</td><td>7.6%</td><td>7.6%</td><td>0.1%</td><td>7.0%</td><td>6.8%</td><td>0.2%</td></tr><tr><td>RX</td><td>0</td><td>0</td><td>0.0%</td><td>0</td><td>0</td><td>0.0%</td></tr><tr><td>Operating Income</td><td>1,960</td><td>4,191</td><td>-53.2%</td><td>2,869</td><td>5,572</td><td>-48.5%</td></tr><tr><td>% Margin</td><td>1.9%</td><td>4.1%</td><td>-2.2%</td><td>2.4%</td><td>4.7%</td><td>-2.3%</td></tr><tr><td>Adjusted EBITDA</td><td>15,084</td><td>16,181</td><td>-6.8%</td><td>15,717</td><td>17,784</td><td>-11.6%</td></tr><tr><td>% Margin</td><td>14.7%</td><td>15.8%</td><td>-1.1%</td><td>13.2%</td><td>15.1%</td><td>-1.9%</td></tr><tr><td>SBC</td><td>4,673</td><td>4,292</td><td>8.9%</td><td>4,653</td><td>4,095</td><td>13.6%</td></tr><tr><td>Interest Expense</td><td>(1,304)</td><td>(1,248)</td><td>4.5%</td><td>(826)</td><td>(991)</td><td>-16.7%</td></tr><tr><td>Other expense / (income), net</td><td>55</td><td>(535)</td><td>-110.3%</td><td>0</td><td>0</td><td>NA</td></tr><tr><td>Pre-Tax Earnings</td><td>3,319</td><td>4,904</td><td>-32.3%</td><td>3,694</td><td>6,563</td><td>-43.7%</td></tr><tr><td>Income Tax</td><td>772</td><td>1,316</td><td>-41.4%</td><td>948</td><td>1,694</td><td>-44.0%</td></tr><tr><td>% Tax Rate</td><td>23.2%</td><td>26.8%</td><td>-3.6%</td><td>25.7%</td><td>25.8%</td><td>-0.1%</td></tr><tr><td>Net loss contributable to NCI</td><td>(52)</td><td>(50)</td><td>4.0%</td><td>(55)</td><td>(53)</td><td>4.0%</td></tr><tr><td>Net Income</td><td>2,496</td><td>3,538</td><td>-29.5%</td><td>2,692</td><td>4,816</td><td>-44.1%</td></tr><tr><td>GAAP Diluted EPS</td><td>$0.71</td><td>$1.00</td><td>-29.4%</td><td>$0.76</td><td>$1.35</td><td>-44.1%</td></tr><tr><td>Non-GAAP Diluted EPS</td><td>$1.70</td><td>$2.20</td><td>-22.7%</td><td>$2.07</td><td>$2.50</td><td>-17.5%</td></tr><tr><td>Diluted Common Shares Outstanding</td><td>3,531</td><td>3,532</td><td>0.0%</td><td>3,556</td><td>3,558</t

[中间内容因长度限制已省略]

s directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/22/2026)</td></tr><tr><td colspan="3">Andrew S Percoco</td></tr><tr><td>Adient PLC (ADNT.N)</td><td>E (12/07/2025)</td><td>$20.65</td></tr><tr><td>Aptiv Plc (APTV.N)</td><td>O (05/07/2026)</td><td>$58.22</td></tr><tr><td>Avis Budget Group Inc (CAR.O)</td><td>E (12/07/2025)</td><td>$164.36</td></tr><tr><td>BorgWarner Inc. (BWA.N)</td><td>E (12/07/2025)</td><td>$64.25</td></tr><tr><td>Dauch Corporation (DCH.N)</td><td>E (12/07/2025)</td><td>$5.70</td></tr><tr><td>Ford Motor Company (F.N)</td><td>E (09/25/2024)</td><td>$14.42</td></tr><tr><td>General Motors Company (GM.N)</td><td>O (12/07/2025)</td><td>$82.13</td></tr><tr><td>Hertz Global Holdings Inc (HTZ.O)</td><td>E (02/08/2024)</td><td>$1.93</td></tr><tr><td>Lear Corporation (LEA.N)</td><td>E (12/07/2025)</td><td>$143.69</td></tr><tr><td>Lucid Group Inc (LCID.O)</td><td>U (12/07/2025)</td><td>$6.78</td></tr><tr><td>Magna International Inc. (MGA.N)</td><td>E (09/25/2024)</td><td>$67.58</td></tr><tr><td>Mobileye Global Inc (MBLY.O)</td><td>E (08/02/2024)</td><td>$8.78</td></tr><tr><td>Quantumscape Corp (QS.O)</td><td>E (12/07/2025)</td><td>$5.87</td></tr><tr><td>Rivian Automotive, Inc. (RIVN.O)</td><td>U (12/07/2025)</td><td>$17.18</td></tr><tr><td>Tesla Inc (TSLA.O)</td><td>E (12/07/2025)</td><td>$374.01</td></tr><tr><td>Versigent Plc (VGNT.N)</td><td>O (05/07/2026)</td><td>$41.16</td></tr><tr><td>Visteon Corporation (VC.O)</td><td>E (06/01/2022)</td><td>$103.16</td></tr><tr><td colspan="3">Daniela M Haigian</td></tr><tr><td>Asbury Automotive Group Inc (ABG.N)</td><td>E (09/25/2024)</td><td>$223.36</td></tr><tr><td>AutoNation Inc. (AN.N)</td><td>O (09/25/2024)</td><td>$205.97</td></tr><tr><td>Carmax Inc (KMX.N)</td><td>E (11/10/2025)</td><td>$57.45</td></tr><tr><td>Carvana Co (CVNA.N)</td><td>O (08/07/2025)</td><td>$62.75</td></tr><tr><td>Group 1 Automotive, Inc (GPI.N)</td><td>O (09/25/2024)</td><td>$327.93</td></tr><tr><td>Lithia Motors Inc. (LAD.N)</td><td>E (09/25/2024)</td><td>$339.95</td></tr><tr><td>Penske Automotive Group, Inc (PAG.N)</td><td>O (09/25/2024)</td><td>$214.57</td></tr><tr><td>Sonic Automotive Inc (SAH.N)</td><td>E (09/25/2024)</td><td>$100.88</td></tr><tr><td colspan="3">Javier Martinez de Olcoz Cerdan</td></tr><tr><td>Goodyear Tire &amp; Rubber Company (GT.O)</td><td>U (09/28/2025)</td><td>$7.45</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.
\* Historical prices are not split adjusted.

© 2026 MS
"""
