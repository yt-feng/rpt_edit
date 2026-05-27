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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Mining Strategy

# On the Road: China trip feedback -> Better...

# What was the takeaway from our latest China trip? Better.

Our latest China trip in the week of 11 $^{th}$ May featured meetings with >25 contacts across industry, government and experts, across two days in Beijing and 2½ days in Shanghai. The one-liner from the trip was incrementally better / bullish vs our last trip in Nov-25. We came away from the tour incrementally positive aluminium & copper 6-12mths forward, our positive lithium price views reinforced, and perhaps a little more sanguine steel and iron ore. We summarise key debates below and read through for key commodities / industries.

# Key Themes

- The one-liner: was it better / same / worse sequentially (vs last trip in November)? Better.   
- Sentiment appeared sequentially better, with house prices in parts of some Tier 1 cities tracking a little better, attitudes toward second hand property purchases and residential rental incomes improving (despite inventory months still above mid-cycle), the share market at/near record highs, deflation moderating / very muted inflation emerging (PPI +2.8% y/y in Apr albeit energy related), corporate profits +15-20% Mar-Q, and exports strengthening. Balance of risks is seen if exports slow, then government can step in with consumer oriented stimulus.   
- Exports: The positive export story was noteworthy, with contacts reflecting increased export orders partly reflecting lower energy costs in China, and partly reflecting ongoing cost / quality improvements.   
- Government policy and stimulus has been relatively muted, which is being interpreted as government being comfortable with the broader economy and pace of growth relative to 4.5-5% GDP targets.   
- The 15th Five Year Plan features a significant focus on grid spend, where announced 15FYP target spend by State Grid Corp + China Southern Power Grid Corp of up to RMB 5trn is estimated at some 40-60% above 14FYP targets/actuals. Focus is on: UHV transmission, renewables integration, storage (BESS), distribution (last mile + urban grid) upgrades, AI/DC load growth, and; rural / micro grid resilience.   
- Anti-involution is lower priority at the moment, and while it remains a key item on the reform agenda, industry capacity utilization is the best guide as to likelihood of more/less interventionist anti-involution agenda.

# Key Commodity/Industry Debates

# Lithium: Moving toward deficit pricing thanks to a BESS tipping point.

- EV Demand: Removal of EV purchase subsidies and imposition of the 5% purchase tax on Jan 1st 2026 has resulted in lower y/y YTD domestic sales, but a \~25% lift in average PV battery size in Mar-Q ytd is significantly offsetting, as is surging e-Truck penetration and the much larger batteries (\~200-500KWh) in medium to large size trucks. The surge in EV exports (+84% y/y YTD Jan-Apr) is put down in part to energy price related bring forward, and in part structural growth uplift.   
- BESS Demand: 15th Five Year Plan features a strong focus on power grid broadening and deepening, with a focus on transmission, distribution and BESS build out to support 3,600GW solar+wind by 2035 (\~1,900GW in 2025). BESS

# Equities

Global

Basic Materials

Lachlan Shaw

Analyst

lachlan.shaw@ubs.com

+61-3-9242 6387

Sharon Ding

Analyst

sharon.ding@ubs.com

+852-2971 6284

Sky Han

Analyst

sky.han@ubs.com

+852-3712 4548

Levi Spry

Analyst

levi.spry@ubs.com

+61-3-9242 6709

Dim Ariyasinghe

Analyst

dim.ariyasinghe@ubs.com

+61-3-9242 6385

Fintan Collins

Associate Analyst

fintan.collins@ubs.com

+61-3-9242 6179

Ben Wood

Analyst

ben.wood@ubs.com

+61-39-242 6709

Thomas Nightingale

Associate Analyst

thomas.nightingale@ubs.com

+61-3-9242 6176

Daniel Major

Analyst

daniel.major@ubs.com

+44-20-7568 3472

Myles Allsop

Analyst

myles.allsop@ubs.com

+44-20-7568 1693

battery demand could lift from \~25% share of LCE demand in 2025 to \~40% share in 2027/28, or approx. 300kt to 900kt LCE in 2-3yrs.

\- IRRs need to be >6% for project sanction, and while battery cell costs could lift \~30% with full pass through of RMB 200k/t Li2CO3 price, this results in a \~20% lift in module costs and \~10% lift in overall BESS unit costs. ASP of BESS is +5-6% implying less than full pass through of higher prices. New capacity payments introduced in June 2025 offset and add 3-4% to IRRs, helping to explain recent resilience of BESS orders. Increasing intermittent share of generation (= intraday spreads) also help to support IRRs.

- BESS medium term demand: One contact outlined \~40% CAGR in BESS installations / shipments, with global installations lifting from 507GWh in 2026 to 1,976GWh in 2030, and shipments (= production) lifting from 1,101GWh in 2026 to 3,034GWh in 2030.   
- LCE Demand: Bringing EV and BESS demand together, contacts thought LCE demand would lift by 20-29% in 2026 (\~25% midpoint), vs UBSe 16%, with top of the range implying \~2.1Mt LCE demand in 2026; while growth to 2029 was estimated at another 60% to \~3Mt.   
- Supply: China is seen as mixed, with growth in Tibet salt lake projects and Sichuan spodumene offsetting ongoing delays in CATL's mine restart (questions on tailings) and other lepidolite producers in Yichun set to go offline for licensing/permitting/expansion outages lasting \~3-15mths.

\- Zimbabwe is returning, with Huayou, Sinomine, Yahua and Chengxin all thought to have secured permits for concentrate export resumption while lithium sulphate plants are built.

\- DRC: Zijin's Manono project in the DRC aims for mine/concentrator completion mid-26, sulphate plant end-26, and full ramp up through 2027 (although the sulphate plant timing is understood to potentially be slipping). Manono East delivers \~70ktpa LCE in spod, and 60ktpa LCE in sulphate, with spod con landing CFR China at US\$400/t. Shipments will be shipped via a Zijin-built road in DRC to Tanzania, then to the Darussalam port for export. From mine gate to refinery in China is 2-3mths. We model 70ktpa LCE from 2027 vs company targets of 130ktpa.

- Lithium prices: All contacts were bullish either calling for prices to range at a high level, to remain in deficit and volatile for some time. Some contacts see a supply response in 2027 and potentially slower demand growth, but others see sustained deficits.   
- Anti-involution is still a theme in parts of the battery chain with significant excess capacity, but has been de-emphasised somewhat.

# Copper: Sulphur squeeze looms, while structural electrification demand is strong.

- Sulphuric acid: Cost and disrupted supply is being seen as a real risk into 2H. Some 80-90% of DRC production (>2Mtpa) imports acid from the Middle East, a portion has 2-3mths inventory, but potentially 0.8-1.0Mtpa could be impacted if SoH remains choked. Chile has about 20% of production (\~1Mtpa) requiring acid, with about 20% (\~200ktpa) potentially impacted. Middle East needs 2-3mths to normalise should SoH open.   
- In short, risk to physical copper production is rising.   
- Demand: Mixed perspectives. Many cited near term demand risks from energy prices / inflation, but equally boosting electrification related demand (eg: solar, wind, EV, BESS). Accelerating grid spend (15th FYP +40-60% vs 14th FYP), solar, wind, EVs and BESS points to robust medium term demand. AI/DC is a significant tailwind.   
- Supply: Refined output has accelerated and scrap usage lifted on higher benchmark pricing and tight concentrate supply. Inventory drawdown of blister/anode inventory has also contributed. This may result in deficits in concentrate, in part due to more conventional outages (eg: Grasberg, Cobre Panama, others), but potential balanced or surplus conditions in refined supply.   
- Pricing: No-one reported a copper buyers strike at recent price levels \$5.50-\$6.00/lb, but several mentioned caution in terms of i) demand risks and ii) positioning. Looking a bit further afield, the combination of disrupted supply and mixed

demand, as Middle East crisis has lifted electrification (eg: solar, wind, EV, BESS) interest but may weigh on traditional demand, was seen as supportive of copper prices trading towards \$6.30-6.80/lb in 2027/28. Tariffs will be a critical factor; positioning into the US importing cathode and storing ahead of potential S.232 tariffs has been a strong tailwind for US copper demand.

- Strategic / critical minerals: Increasingly participants view copper of growing strategic importance beyond its more traditional "Dr Copper" role as a gauge of overall economic conditions. Geopolitics, localisation and onshoring were seen to support strategic stockpiles, but estimation of a "strategic premium" to the copper price was seen as elusive for now.   
- Capex/opex: costs continue to rise, with more stable jurisdictions seeing 3-5% inflation per annum, and more dynamic jurisdictions 5-8%, with both sustaining and new project capex seen with upside risk.   
- Substitution: Limited clear-cut views on substitution risks from here, with contacts pointing to relatively stable Cu:Al price ratio (both metals used in electrical applications). Some discussion around potential to reduce silver loadings in solar PV manufacture and replace with increased copper loadings

# Bauxite / Alumina / Aluminium: "Largest aluminium deficit in decades looms"....

- Guinea bauxite export quotas: Export quotas \~150Mt in 2026, vs 183Mt of actual exports in 2025, but the quotas are seen not to have taken effect yet. Equally, large participants are seen as relatively immune, reflecting size and commitment to construct refining capacity.   
- Alumina refinery build out: Chalco are near completion on their 1.2Mtpa refinery which has taken 7yrs to design/engineer/construct. Bx to Alumina ratio is 2.6-2.7x. [Post trip, Guinea and Chalco agreed a new framework for Chalco's alumina refinery project in Guinea].   
- Alumina balance/outlook: Market is in surplus, and price outlook muted, and expected to remain that way on i) muted aluminium production growth (Middle East, delays in Indonesia) and ii) ongoing growth in new refinery supply in China, India, Indonesia, and stubborn legacy/high cost capacity.   
- Alumina demand: Middle East outages of \~2.5Mt smelting capacity is seen taking at least until 2H-2027 to return, while new smelter projects especially in Indonesia (see below) are observed taking more time to build and power.   
- Alumina supply: Global capacity is estimated \~200Mt that ran \~80% utilisation in 2025 for \~160Mt production. Contacts highlight significant growth in new refining capacity, due in part to project sanction 2023-24 when Russia-Ukraine saw prices spike higher.   
- In China there are >13Mt of new refineries set to open in 2026, and ex-China, almost 17Mt new capacity to open 2026-28. New Chinese capacity is close to the coast for imported bauxite. Cost spreads are meaningful, with breakeven costs typically RMB 2,700-3,000/t inland, vs RMB 2,500-2,600/t on the coast. Inland supply is significantly loss-making, but 60-70% vertically integrated with profitable smelters, so is unlikely to close.   
- The supply dynamic is bearish, with the market expected to remain in a surplus 2026-27.   
- Alumina price outlook: Contacts saw alumina prices trading into cost curves, but the necessary rebalancing potentially taking longer to materialise. RMB 2,600-2,700/t was seen as a reasonable price expectation in China this year and next, with upside if loss making refiners close in China more rapidly than currently observed / expected.   
- Aluminium demand: Contacts see underlying demand growth 3-4% p.a. globally, with China towards top of that range and ex-China lower end. Contacts see risk of slower demand from Middle East energy price headwinds to consumption, but equally highlight increased interest in aluminium-intensive solar, BESS and EVs following Middle East conflict, and longer term bullish demand from China's 15th FYP grid spend.   
- BESS: Contacts assessed BESS demand (module fabricated framing) could be \~1Mt of Al demand in the near term, growing in line with the rapid expected

lift in BESS production.

\- Aluminium supply: The outages in Middle East of \~2.5Mt, including EGA's 1.2Mt cold start, could be complicated / take time to bring back on line.

\- For some contacts, this results in the largest aluminium market deficits in decades, and clearly supportive to price.

\- Indonesia has 10-14Mt of new aluminium smelter projects in the pipeline, but slow power build out (3-4yrs), fragmented locations/islanded grids, and equipment delays, result in contacts observing a more measured pace of capacity expansion.

\- China 45Mtpa primary capacity cap is very firm, but advanced technology higher productivity (eg: AP60, 30-40% China capacity) and debottlenecking creep result in selected smelters able to produce between 103-110% of nameplate. Other jurisdictions are now tabling new smelter projects, but longer build/commission times for ex-China capacity mean supply growth may be more rational and not overwhelm strong underlying demand growth.

\- Aluminium substitution: With the Cu:Al price ratio relatively stable / benign vs historical averages, contacts did not highlight significant substitution pressures in electrical applications in the near term. Contacts did offer potential for Al to steel substitution in select applications in manufacturing and construction for which weight is less of a concern.

\- Aluminium prices: Current domestic Al prices of RMB24-25k/t are seen as high but reasonable, given where Cu is trading, and robust underlying demand. Pace and direction of inventory movement is important for price, a steady draw was expected by contacts to potentially underpin higher metal prices eg: RMB 26-28k/t on a 6-12mth view. Longer term eg: 2-3yrs, contacts expect supply to catch up to demand and potentially weigh on prices.

\- Aluminium inventory: In China is not low/tight, indeed it has been a tad elevated in recent months, due to i) rapid price increase, and ii) reduced metal collateralised borrowing. But a recent acceleration in aluminium rod inventory drawdown is supportive, as usually leads broader metal inventory drawdowns by 1-2mths.

# Steel / Iron ore: "China's steel bear market is over" & "US\$110/t iron ore is OK"

\- Steel margins: Some contacts offered that China's steel industry bear market is ending in 2026. The logic flows that current mill margins of RMB 30-90/t, +RMB 300/t from 3mths, ago, are symbolic of an improved cycle.

\- Mill margins are better due to i) lower / normalised met coke prices, in part due to higher Mongolian met coal supply, ii) supply discipline eg: maintenance, CO2 emissions pressure, and iii) closing domestic / export price arbitrage.

\- While anti-involution has been somewhat de-emphasized, capacity reduction requirements remain (1.25:1 for new capacity, 1.5:1 for M&A).

\- Steel demand/production: Most contacts see production of crude steel flat this year, but manufactured exports (indirect steel exports) are likely to be a bright spot.

\- Manufacturing demand has grown significantly and including autos & shipping, some saw manufacturing now up to half of overall Chinese domestic steel demand (including amounts exported in manufactured goods).

\- Property construction steel demand is muted, perhaps one-fifth or less of the \~1Bt annual crude steel output rate. Housing construction is \~10% or less, with the remainder government, commercial, industrial real estate.

\- Infrastructure construction steel demand is seen growing \~GDP less a little, as while overall infrastructure FAI growth remains healthy, the steel intensity of infrastructure FAI is trending lower.

\- Exports are mixed. Direct steel exports (125Mt in 2025, of billet, etc) were seen as down or perhaps flat, with anti-dumping and narrowing export arbitrage weighing on shipments (eg: 110-120Mt net exports CY26). But indirect exports (\~130-150Mt in 2025) of steel embedded in manufactured goods were seen likely higher by 10-15% y/y, reflecting i) China's lower energy costs, ii) China's relentless lift in quality.

\- Steel scrap: Availability is OK, but with iron ore prices at US\$110/t, scrap economics struggle against virgin hot metal. On EAFs, contacts highlighted that EAFs can't compete with BF/BOF at peak power prices, and that some former EAF projects have been delayed/cancelled. Scrap rates into BOFs currently run \~8-15%.

\- Iron ore port stocks: We asked contacts how to rationalise record iron ore port stocks \~160-165Mt vs iron ore prices \~US\$100-110/t? Most steel mills now hold inventories of iron ore at ports or in trader stocks on their behalf, while traders and producers continue to hold stocks at ports in support of blending operations. In other words, a growing share of iron ore port stocks are effectively steel mill working capital and therefore not indicative of true quantities available to a pure "spot" physical market. Some traders estimate 60%+ of port stocks support blending and mill inventories.

\- Iron ore cost support: Contacts see cost support at US\$100/t (US\$80/t prior), with higher cost Indian, Chinese domestic and other smaller seaborne supply seen as having left or being in and out of the trade recently. Energy was seen impacting suppliers further from China and those needing energy intensive processing.

\- Iron ore prices: Some steel mills noted that US\$110/t is "OK", although we suspect subject to mill margins which have been supported by lower met coal prices and normalised average (eg: domestic + export) mill margins.

\- Low grade discounts / high grade premiums. Mill and producer contacts agreed that if steel mill margins firmed further towards and above RMB 200/t, further pressure would mount on low grade discounts, and potential further expansion of high grade premiums, although the latter is less certain given Middle East DRI/EAF has curtailed.

\- Middle East / Iran impact: 15-20Mt of exported steel eg: billet, is out of the market, while 10-15Mt of iron ore exports are also out. The result is degree of tightness in steel exports but also the iron ore market.

\- Simandou: Ramp up is going more slowly, with lack of slots / production of US-manufactured locomotives the key bottleneck. The wet season (Apr-Oct, average rainfall 4.5m at port, 2.5m at mines) is now also impacting. Works continue at both mines, while safety / worker injury increasing focus for the government. Expectations for shipments have been trimmed, with some reducing expected shipments in 2026 from 40-50Mt to 20-30Mt.

\- CMRG: Contacts expect that other iron ore suppliers eg: RIO, FM

[中间内容因长度限制已省略]

d Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/04d5bf71fde73d64123d5b42a11cb1a68883d2cc81f6f655beeb807f1e88c5bb.jpg)
"""
