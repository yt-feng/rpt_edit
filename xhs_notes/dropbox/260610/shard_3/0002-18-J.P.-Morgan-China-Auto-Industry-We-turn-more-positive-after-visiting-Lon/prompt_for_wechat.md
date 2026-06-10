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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Auto Industry

We turn more positive after visiting London and Paris

We turn more optimistic on Chinese OEMs' overseas expansion, particularly in Europe, following our annual European Auto Conference last week (here), where we took the opportunity to visit BYD stores in London and Paris. To reflect our positive stance, we raise our 2026 overseas sales forecasts for BYD/Geely by \~15%/30%. Key strategic highlights below:

- Europe: Mixed-propulsion transition market: Chinese OEMs are shifting from single-powertrain exports to balanced portfolios (BEV+PHEV/HEV) plus brand ladders (e.g., BYD to Denza) and tech stories. Our store checks show robust PHEV demand alongside “value-for-money” BEV wins.  
- Retail execution moat: Channels + after-sales + residual value: BYD emphasizes dense dealership/store coverage and high test-drive conversion (\~50%); Chinese OEMs stress after-sales depth to build trust, residual value and monthly payment competitiveness, aiming to avoid pure price competition. Foreign brands face pressure as Chinese cars bundle high feature content as standard vs. options-heavy incumbents. Chinese OEMs reached an 18% share in Europe's NEV segment in Apr-26, tripled from the same time last year.  
- Charging/ecosystem as differentiator (not just the car): BYD is using flash/ultra-fast charging rollout as part of the value proposition, targeting 3,000 flash-charging posts in Europe by end-2026. We believe execution will be key to boosting conversion and reducing buyer friction, helping defend residuals and compete on total ownership experience, rather than sticker price.  
- Export tailwinds are structural: China's export mix is shifting rapidly toward NEVs (NEVs $>50\%$ of PV exports; PHEV share rising within NEVs), supporting overseas revenue/margin upside. BYD focuses on vertical integration, while Geely is more partnership/KD "asset-light." We see localization as critical to mitigating tariff/regulatory risk. Meanwhile, European OEMs will aim to compete via an "in China, for global" strategy, including exporting select models from China and leveraging the cost-competitive Chinese supply chain to the global supply network.  
- Our BYD store visits at Canary Wharf and the Champs-Élysées: Staff at both stores reported strong demand for PHEVs. We learned about: (1) the launch of the Denza flash charging model in the EU/UK; and (2) wait times of about two to three months for most BYD models in France.

Equity Ratings and Price Targets

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>BYD Company Limited - H</td><td>1211 HK</td><td>91,987</td><td>HKD</td><td>88.05</td><td>OW</td><td>n/c</td><td>124.00</td><td>Dec-26</td><td>120.00</td><td>n/c</td></tr><tr><td>BYD Company Limited - A</td><td>002594 CH</td><td>109,946</td><td>CNY</td><td>91.19</td><td>OW</td><td>n/c</td><td>124.00</td><td>Dec-26</td><td>120.00</td><td>n/c</td></tr><tr><td>Geely Automobile Holdings Ltd. (0175)</td><td>175 HK</td><td>21,235</td><td>HKD</td><td>18.17</td><td>OW</td><td>n/c</td><td>29.00</td><td>Dec-26</td><td>28.00</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 08 Jun 26.

## China

## Head of APAC Auto Research

Nick Lai AC

(65) 6801-3176

nick.yc.lai@JPM.com

JPM Securities Singapore Private

Limited/ JPM Securities (Asia Pacific)

Limited/ JPM Broking (Hong Kong)

Limited

## Jiajie Shen, CFA

(86-21) 6106 6352

jiajie.shen@jpmchase.com

SAC Registration Number: S1730520030006

JPM Securities (China) Company

Limited

## Cathy Liu

(852) 2800-8629

cathy.xiao.liu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Four strategic highlights from our store visits, Asia auto tour and European Auto Conference

We visited BYD stores in London and Paris along with our annual European Auto Conference in London last week (note). Our recent annual Asia auto tour along with JPM's China summit yielded similar observations (note). We highlight collective strategic takeaways below. Further, to reflect our positive view on Chinese OEMs' expansion in overseas markets, we lift our 2026 overseas sales estimates for BYD and Geely by \~15% and \~30%, respectively.

Chinese OEMs' market share gains are noticeable not only in Europe (note), but also in other parts of the world, such as Southeast Asia (note) and Latin America. For example, the latest data from Europe (including Eastern and Western Europe) suggest that Chinese OEMs' market share in the NEV space (where Chinese brands are very competitive vs. foreign brands) topped $18\%$ in April, more than tripling from $5\%$ during the same time last year.

Figure 1: Chinese OEMs' annual market share in the NEV space in Europe  
![](images/55ce606e13a75f2db5f167df7a60a4a9fcc83a3ce5b19f479c5458060e1ffe8a.jpg)

<details>
<summary>line chart</summary>

| Year | Value (%) |
|---|---|
| 2014 | 0 |
| 2015 | 0 |
| 2016 | 0 |
| 2017 | 0 |
| 2018 | 0 |
| 2019 | 0.3 |
| 2020 | 1.5 |
| 2021 | 2.1 |
| 2022 | 4.2 |
| 2023 | 5.8 |
| 2024 | 5.5 |
| YTD26 | 16.5 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

Figure 3: BYD market share in Europe's NEV market (8% in Apr-26)  
![](images/b9381ceca2c401a9a142c31e11aa160a5029358afa494b95b824d1d2e5a2022c.jpg)

<details>
<summary>line chart</summary>

| Date | Value (%) |
|---|---|
| 5/1/2024 | 1.2 |
| 6/1/2024 | 1.4 |
| 7/1/2024 | 1.9 |
| 8/1/2024 | 1.9 |
| 9/1/2024 | 1.6 |
| 10/1/2024 | 2.3 |
| 11/1/2024 | 2.6 |
| 12/1/2024 | 2.8 |
| 1/1/2025 | 2.8 |
| 2/1/2025 | 3.0 |
| 3/1/2025 | 4.3 |
| 4/1/2025 | 4.5 |
| 5/1/2025 | 4.5 |
| 6/1/2025 | 4.4 |
| 7/1/2025 | 4.5 |
| 8/1/2025 | 4.7 |
| 9/1/2025 | 6.3 |
| 10/1/2025 | 5.1 |
| 11/1/2025 | 5.8 |
| 12/1/2025 | 6.6 |
| 1/1/2026 | 6.3 |
| 2/1/2026 | 6.3 |
| 3/1/2026 | 7.5 |
| 4/1/2026 | 7.6 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

Figure 2: Chinese OEMs' monthly market share in the NEV space in Europe  
![](images/f63460185b350ca25f397f7b63780fedb06eddf79dcf7a4a576ff8dacebd45d2.jpg)

<details>
<summary>line chart</summary>

| Date | Value (%) |
|---|---|
| 5/1/2024 | 5.3 |
| 6/1/2024 | 7.1 |
| 7/1/2024 | 5.8 |
| 8/1/2024 | 4.9 |
| 9/1/2024 | 5.0 |
| 10/1/2024 | 5.5 |
| 11/1/2024 | 5.8 |
| 12/1/2024 | 6.2 |
| 1/1/2025 | 6.1 |
| 2/1/2025 | 6.1 |
| 3/1/2025 | 8.0 |
| 4/1/2025 | 9.0 |
| 5/1/2025 | 9.8 |
| 6/1/2025 | 10.3 |
| 7/1/2025 | 10.7 |
| 8/1/2025 | 10.8 |
| 9/1/2025 | 13.6 |
| 10/1/2025 | 11.8 |
| 11/1/2025 | 13.3 |
| 12/1/2025 | 14.9 |
| 1/1/2026 | 13.8 |
| 2/1/2026 | 15.6 |
| 3/1/2026 | 17.8 |
| 4/1/2026 | 18.3 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

Figure 4: MG (under SAIC) market share in Europe's NEV market (2% by Apr-26)  
![](images/d9de080623a3b17ba1bfaffdd591a667d61a0a86e537286307eccd59385043ac.jpg)

<details>
<summary>line chart</summary>

| Date | Value (%) |
|---|---|
| 5/1/2024 | 3.2 |
| 6/1/2024 | 4.9 |
| 7/1/2024 | 2.8 |
| 8/1/2024 | 1.8 |
| 9/1/2024 | 2.4 |
| 10/1/2024 | 1.9 |
| 11/1/2024 | 1.8 |
| 12/1/2024 | 2.1 |
| 1/1/2025 | 1.7 |
| 2/1/2025 | 1.4 |
| 3/1/2025 | 2.0 |
| 4/1/2025 | 1.6 |
| 5/1/2025 | 1.8 |
| 6/1/2025 | 2.4 |
| 7/1/2025 | 2.5 |
| 8/1/2025 | 2.0 |
| 9/1/2025 | 2.5 |
| 10/1/2025 | 1.9 |
| 11/1/2025 | 2.2 |
| 12/1/2025 | 2.4 |
| 1/1/2026 | 1.3 |
| 2/1/2026 | 1.5 |
| 3/1/2026 | 1.7 |
| 4/1/2026 | 2.3 |
</details>

Source: Bloomberg Finance L.P., JATO Dynamics.

## (1) Europe as a mixed-propulsion transition market: Chinese OEMs are winning by offering a portfolio (BEV + PHEV/HEV) plus a clear brand ladder (mainstream → premium), not a single “cheap BEV export” play

Chinese OEMs (e.g., BYD, Geely) are shifting their overseas strategies toward multi-powertrain portfolios and brand/tech storytelling, with Europe explicitly treated as a transition market, where PHEV demand matters alongside BEV.

Examples (store checks): BYD's Paris and London stores show strong PHEV traction (e.g., Seal U DMi highlighted by sales staff we met as a bestselling PHEV; a meaningful share of store orders are PHEV), while certain BEV models (e.g., Sealion 7) are positioned as “value for money” leaders with long wait times, especially at the Paris store, suggesting that demand exceeds supply in inventory.

Implications for overseas markets: We expect share gains to be driven less by “BEV-only price disruption” and more by a menu that matches local charging readiness and consumer needs, with PHEV acting as a commercialization bridge.

Foreign brands' strategy signal: Incumbents face a tougher value equation because Chinese models often bundle high-feature content as standard, e.g., Level 2 ADAS (vs. options-heavy German pricing), shifting competition toward content-per-euro and monthly payments (as opposed to MSRPs or sticker prices).

JPM view: We are surprised at the speed of overseas volume growth among Chinese brands, driven by competitive product offerings, multi-powertrain options and superior interior/content vs. foreign brands at similar price points. To reflect this positive moment, we raise our overseas volume estimates for BYD and Geely in our earnings models.

## (2) Go-to-market is becoming a retail execution game: Dense channels + after-sales credibility + residual value discipline (i.e., monthly payment competitiveness)

One key observation throughout our visits and meetings is that Chinese OEMs are emphasizing rapid channel buildout (stores/dealers), measurable conversion and deepening after-sales to build trust and residual value, explicitly linking this to monthly payment competitiveness, rather than sticker price warfare.

Examples: BYD's Europe expansion plan targets large physical scale (dealers/stores), and management messaging highlights rapid conversion ( $\sim 45 - 50\%$ ) into orders after test drives and solid demand (especially considering supply tightness in Europe, such as at the Paris store we visited).

Overseas market implications: The winning playbook looks closer to “fast retail rollout + service credibility” than to traditional export-only distribution, raising the bar for incumbents that may be slower to reconfigure dealer economics and inventory strategy.

Foreign brands' strategy response: Foreign OEMs are already adjusting, e.g., German premium OEMs have been consolidating dealer networks in China and rightsizing production capacity in China, signaling a broader shift toward

profitability protection and structural resizing, rather than pure volume defense. Outside China, we notice select global OEMs' strategic shift from “in China, for China” previously to “in China, for global” now, meaning that global OEMs are bringing select China-made products to overseas markets and exploring leveraging cost-competitive Chinese suppliers to their global supply chain networks.

JPM view: Based on our store visits and discussions with management, we believe BYD's focus on residual value discipline (and avoiding price competition) is central to sustaining brand health and monthly-payment positioning as volumes scale.

## (3) The next moat is ecosystem + charging (flash/ultra-fast) paired with premium products – used to lift value propositions and reduce price pressure

We learned at our store visits and European auto conference that BYD is positioning charging infrastructure (including flash charging) as an ownership proposition and commercialization lever; management has stated a target of 3,000 flash-charging posts in Europe by end-2026, including 300 in the UK, and a premium-brand Denza launch in 2H26, which will be the first BYD offering with a “flash charging solution.”

What also surprised us was the Paris store sales staff's comment that there are meaningful orders for the newly launched Denza model and that wait times are now about six months, even though Denza has not been formally launched in Europe and buyers know only an initial indicative price of \~€115,000.

Overseas market implications: If executed, OEM-tied charging could reduce buyer friction (range/charging anxiety), support fleets and shift competition from price to total ownership experience, which is particularly important in Europe, where charging availability varies widely across geographies.

Foreign brands' strategy response: This development pressures incumbents to compete not just on vehicle specs, but also on ecosystem partnerships (charging access, software stacks, service plans), and to rethink what is bundled vs. optioned.

JPM view: We believe the charging rollout, if delivered at scale, could support conversion/acceptance and help BYD avoid pure price competition by strengthening the overall value proposition beyond sticker price.

## (4) The “overseas story” is structurally supported by export mix shifts (NEV/PHEV) and a push toward localization, but execution + policy risk is rising

We expect China PV exports to be increasingly NEV-led (NEVs reaching a majority share), with PHEV becoming a larger component of NEV exports, a pattern that may surprise overseas investors and aligns with Europe's transition-market reality.

Overseas market implications: As the mix shifts to higher-ASP electrified products, overseas could become disproportionately important to revenue/profit (vs. volume), which supports more aggressive investment in channels, charging and local footprints.

Localization divergence (BYD vs. Geely): We see strategic differences between OEMs, with BYD pursuing a more vertically integrated overseas footprint (plants outside China), while Geely leans more toward partnership/KD and “asset-light” pathways.

Foreign brands' strategy response (“in China, for global”): Global OEMs are trying to export China-made models and leverage China’s cost-competitive supply chain globally, an explicit attempt to turn China capabilities into an international countermeasure.

JPM view: Longer-term, we view Chinese OEMs' exports/share gains as structural, rather than cyclical. At the same time, Chinese OEMs' localization will be a decisive strategic variable to mitigate tariff/regulatory risk; examples include BYD's plants in Brazil and Hungary, Geely's partnerships with Porton in Malaysia and with Ford in Spain, Leapmotor's JV with Stellantis, and XPeng's alliance with Magna in Austria. Localized solutions should help potential geopolitical headwinds and tariff/non-tariff barriers facing Chinese brands in their overseas endeavors.

## Summary of our BYD store visits in Paris and London

## Paris store

- Bestselling BEV: Sealion 7 with an MSRP of \~€48,000 and a wait time of three  
to four months; monthly installment around €800 if buyers choose the leasing finance option.  
- Bestselling PHEV: Seal U DMI with a starting MSRP of €40,600 and monthly installments around €600-700. Wait time is around one month, where most buyers also consider Tesla Model Y.  
- Most buyers choose BYD for its value-for-money position: BYD offers many features as standard, e.g., 360 view, seat heating, ADAS level 2 vs. German models, where these features are mostly optional and customers need to pay.  
- What surprises us is BYD's introduction of premium-brand Denza Z9 GT, which will be equipped with the company's latest flash-charging solution (i.e., state of charge (SOC) only 9 minutes from $10\%$ to $97\%$ ). The initial indicative price is €115,000, according to sales staff at the store, with formal debut in 2H26.

Despite this, BYD has already received meaningful orders, so wait times are about six months. Most buyers compare the Z9 GT with the Porsche Taycan (starting MSRP \~€103,000). The store manager told us that BYD is starting to building ultra-fast charging stations in Southern France first.

- All in all, BYD sales staff told us that the company currently has 10 models available in the market, and its average order flow is split between around 50-60% PHEVs and the rest BEVs.  
- In terms of promotion, BYD offers around a 5-7% discount for most models. When asked why BYD needs to offer discounts, considering robust demand, sales staff told us it is a marketing practice, as customers like to receive some incentive before making a purchase decision.

## London store

- Similar to Paris, BYD recently introduced the highest-end Denza Z9 GT in the UK, with formal debut scheduled for 2H26. Sales staff told us that estimated starting MSRP would be £80k-85k, more expensive than the BMW i5 (starting at £68k) and the Benz EQE (from £69k). Denza will be equipped with BYD's latest flash-charging battery and solution.  
- BYD indicates that it plans to build 3,000 ultra-fast charging stations or posts in Europe by end-2026, of which 300 will be in the UK.  
- PHEV Seal U DMi is the bestselling model, with a starting MSRP of \~£40k or monthly installments around £420 if buyers choose the leasing finance option.  
- The Sealion 7 BEV SUV is BYD's top-selling BEV in the UK because of its value-for-money strategy. Starting MSRP is \~£60k, and the monthly installment is \~£610.

Figure 3: BYD store in Paris (the bestselling BEV, Sealion 7, at an MSRP of \~€48k or a monthly installment of \~€800 and three months' wait time  
![](images/77d996ddc705aa2f6b7b183997a1b4d6f693d1a68256d9cc0a6d4357d6f458fc.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a modern white BYD electric vehicle on display at an auto show, with no visible text or symbols on the vehicle itself.
</details>

Source: Photo taken by JPM at the BYD store.

Figure 4: BYD store in London  
![](images/8663528929653dcc67a9c0997ef690504399e305e61985d1722d2ffaf71a66cb.jpg)

<details>
<summary>text_image</summary>

BYD
BYD
</details>

Source: Photo taken by JPM at the BYD store.

## Overweight

1211.HK,1211 HK

Price (08 Jun 26): HK\$88.05

▲ Price Target (Dec-26): HK\$124.00

Prior (Dec-26): HK\$120.00

China

Head of APAC Auto Research

Nick Lai AC

(65) 6801-3176

nick.yc.lai@JPM.com

JPM Securities Singapore Private Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Key Changes (FYE Dec)

<

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own

independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
