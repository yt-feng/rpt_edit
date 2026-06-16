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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 15, 2026 10:13 PM GMT

# The Oil Manual

# 'Let the Oil Flow'

We adjust our forecast following the US/Iran MOU. We still see a tight summer ahead, and suspect Dated Brent can rebound from current levels into 3Q. However, with prospects of SoH recovery improved, our previous forecasts now appear too high. From 4Q onwards, we see Brent anchored around \$80/b.

## Key Takeaways

Our previous modelling assumptions reflected a political agreement by late July; with the MOU announced over the weekend, this has come \~2 weeks earlier  
From here, it likely takes several weeks for tanker flow to be restored; we see 50% of production back by Sept, and 80% by Dec, slightly faster than before  
Despite the disruption, a broad range of indicators has signaled weakness in physical oil markets in recent weeks; notably, unsold cargos are above-average  
The 'twin solvers' of high US exports and low China imports are the key drivers; in the short term (i.e. next weeks) they do not seem to come to an end just yet  
In the end, we still see a tight summer that can support a modest rebound, but that period now appears too short to support our previous Brent forecast

Exhibit 1: For any given month, information on tanker movements firms up over time. Based on known voyages, it appears that net seaborne oil imports into China will decline even further in June vs May, and even July is tracking below May as well.  
![](images/b662edb5deac74d22734a10e72801ed324a6d7a43a329d66e03a32523ef91a71.jpg)

<details>
<summary>line chart</summary>

| Days to month-end | May 2026 | Jun 2026 | Jul 2026 |
| ----------------- | -------- | -------- | -------- |
| 75                | ~3       | ~3       | ~3       |
| 50                | ~8       | ~7       | ~7       |
| 25                | ~11      | ~9       | ~17      |
| 0                 | ~8       | ~8       | ~14      |
| -50               | ~8       | ~8       | ~14      |
</details>

Source: Vortexa /pit/cargo-movements vintages, MS

MS & CO. INTERNATIONAL PLC+

## Martijn Rats, CFA

Equity Analyst and Commodities Strategist

Martijn.Rats@morganstanley.com +44 20 7425-6618

## Charlotte Firkins

Commodities Strategist

Charlotte.Firkins@morganstanley.com +44 20 7425-3866

## Amy Gower (Amy Sergeant), CFA

Commodities Strategist

Amy.Gower1@morganstanley.com +44 20 7677-6937

Exhibit 2: We revise our near-term Brent price lower; our long-term forecast remains anchored around \$80/b

Dated Brent price forecasts

<table><tr><td>($/bbl)</td><td>3Q26</td><td>4Q26</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td></tr><tr><td>New</td><td>90.0</td><td>80.0</td><td>80.0</td><td>80.0</td><td>80.0</td><td>80.0</td></tr><tr><td>Previous</td><td>100.0</td><td>95.0</td><td>85.0</td><td>80.0</td><td>80.0</td><td>80.0</td></tr><tr><td>Change</td><td>-10.0</td><td>-15.0</td><td>-5.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Source: MS

## Previous research:

- The Oil Manual: How Fast Can Middle East Production Return? (1 June 2026)  
• The Oil Manual: SPR Tracker: How Much Has Been Released? What's Next? (28 May 2026)  
- The Oil Manual: Why is the Price of Oil Not Higher? (11 May 2026)  
- The Oil Manual: US Gasoline: Tight Balance; Fair Value For Now (4 May 2026)  
• The Oil Manual: Schrodinger's Strait (27 Apr 2026)  
- The Oil Manual: Hormuz Closure – Six Weeks In: Where Do We Stand? (13 Apr 2026)  
- The Oil Manual: 'Paper' vs 'Physical' Oil - A Short Primer (7 Apr 2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## 'Let the Oil Flow'

## Re-opening of the Strait agreed

106 days after the start of the conflict, President Trump announced yesterday that the United States and Iran have reached an intermediate agreement. Although the precise content of this MoU has not been released, both sides have indicated that it calls for 1) an end to hostilities on all fronts, 2) the opening of the Strait of Hormuz from both sides, and 3) a negotiation over Iran's nuclear programme and highly enriched uranium over a 60-day period.

In the end, this announcement came even slightly earlier than our modelling assumptions had implied. In our note How Fast Can Middle East Production Return? (1 Jun 2026), we had updated our estimate for the timing of a political break-through to 'late June'; it turned out to be 'mid-June' instead.

Much is still to be negotiated and key risks remain, but for now, this is a key step towards a de-escalation of the conflict and higher oil exports via the Strait of Hormuz.

## Trajectory for production recovery brought forward by 1-2 weeks

Full restoration of tanker flow through the Strait will first require a period for the clearing of sea mines. There are alternative routes that avoid the traditional shipping lanes, but the capacity of these routes is likely only a fraction of pre-conflict transits.

Then, some time is likely needed to rebuild commercial confidence amongst ship owners and insurance companies, and allow tankers - many of which have relocated elsewhere - to come back to the region.

Also, for production to be restored, export tanks need to be cleared first, which means that the pace at which empty tankers enter the Gulf is arguably even more important than laden tankers leaving.

For these reasons, we estimated that the ramp-up in production would start from late-July, which we now bring forward to mid-July. After that, we assume that 50% of lost production will be back by September, 80% by December, with the rest to follow in early 2027.

Exhibit 3: Outbound tanker transit are still sharply below pre-conflict levels but notably improved since early May  
![](images/7bb9591732f46cb385576efa1786c6809a32d495629e8897b27279a0d1140bb2.jpg)

<details>
<summary>bar chart</summary>

| Date       | Oil  | LPG  | LNG  |
| ---------- | ---- | ---- | ---- |
| Feb        | 25   | 10   | 15   |
| Mar        | 10   | 5    | 10   |
| Apr        | 5    | 5    | 5    |
| May        | 5    | 5    | 5    |
| Jun        | 5    | 5    | 5    |
</details>

Exhibit 4: With that, also oil exports from the region have seen a small but notable bounce from the low  
![](images/7d31dbb0eb5122426511328dc709ad2d8ac4f14611322e927e33337a76d12d86.jpg)

<details>
<summary>line chart</summary>

| Year | Vortexa | Petro-Logistics |
|------|---------|-----------------|
| 2024 | ~15     | ~15             |
| 2025 | ~15     | ~15             |
| 2026 | ~10     | ~10             |
</details>

## Despite ongoing supply loss, physical market has softened

By now, the cumulative supply loss from the Middle East since 1 March has reached $\sim 1.4$ billion barrels across both crude oil and refined products, relative to the same period in 2025. Nevertheless, the Brent market has softened visibly in recent weeks.

This has not only been a story of Brent futures anticipating the Strait to re-open. Dated Brent has come under pressure too, both the DFL and CFD curves have weakened in both level and structure, physical diffs have softened, the cash Dubai premium has been on a steady decline, and refined product cracks have mostly been on a downward slope too. The stand-out here is the naphtha crack spread in Asia relative to Dubai crude; this has fallen \$13/b in the last four weeks to \$(11)/b, close to its 1-year low - quite a counter-intuitive weakening for a production for which 33% of seaborne supply has been cut off by the Strait of Hormuz.

This weakening can also be seen in the overview of unsold cargoes. The table below summarises indications of unsold cargoes over the last two weeks. To be clear, the oil industry always has some cargoes that struggle to sell - it's part of the friction of buying and selling. However, we would characterise the current level as higher-than-normal and broadening. And that would be compared against 'normal' times. Considering that 11 mb/d of crude oil production is currently shut-in across the Middle East, this is quite unusual and highlights the physical weakness in the market.

Exhibit 5: We'd characterise the current number of unsold cargoes as above-normal and broadening in recent weeks  
Unsold crude cargoes - latest estimate by region/grade  
As of 15 June 2026. Trader anecdotes, not a continuous series.

<table><tr><td>Region / grade</td><td>Unsold estimate</td><td>As of</td><td>Source</td></tr><tr><td>Nigeria</td><td>July programme &quot;largely unsold&quot;; Bonny Light &amp; Forcados &quot;numerous unsold cargoes&quot;; ~15mn bl June unplaced earlier in cycle</td><td>Jun 12 / Jun 5</td><td>Platts / Argus</td></tr><tr><td>Angola</td><td>~a dozen stems (10-12 cargoes) July; ~10mn bl July explicitly unsold</td><td>Jun 12 / Jun 10</td><td>Platts / Argus</td></tr><tr><td>Congo (Djeno)</td><td>Some July cargoes unsold at ~$4/bl under Dated - &quot;not attractive enough for Chinese refiners&quot;</td><td>Jun 10</td><td>Argus</td></tr><tr><td>CPC Blend</td><td>June 2-3 cargoes; rebounded off Jan-2023 low (Jun 11) but July &quot;plenty unsold first decade&quot;, Asia arb unviable; 11-Suezmax injection lingering</td><td>Jun 9-11</td><td>Platts</td></tr><tr><td>Libya / Es Sider</td><td>7-10 June cargoes (incl. 4-5 Es Sider); unplaced Libyan barrels persist into July trade</td><td>Jun 5 / Jun 12</td><td>Platts / Argus</td></tr><tr><td>Azeri BTC / Kirkuk</td><td>Kirkuk unsold in June; Socar/Eni CPC offers went unplaced; first Basrah offers reaching Europe</td><td>Jun 3-5</td><td>Platts / Argus</td></tr><tr><td>North Sea</td><td>Forties ~1/3 of 9 June cargoes (May 26) - since cleared; Atlantic overhang still capping diffs &amp; US exports</td><td>May 26 - Jun 2</td><td>Platts</td></tr><tr><td>Mideast Gulf</td><td>Spot thin but placing July cargoes - cleared</td><td>May 26</td><td>Platts</td></tr><tr><td>Russian ESPO</td><td>&gt;50% of July programme unsold; June cargoes still unsold</td><td>Jun 12 / Jun 8</td><td>Argus / Platts</td></tr><tr><td>Brazil</td><td>Unsold July-delivery to China (late May); Aug cycle ~18mn bl taken - lower than prior</td><td>May 25-29</td><td>Argus</td></tr><tr><td>Guyana</td><td>July cycle &quot;quiet&quot;, buying limited into third week; June stragglers still offered</td><td>Jun 11</td><td>Argus</td></tr><tr><td>Canada / TMX</td><td>August injection cargoes &quot;still to be sold&quot;, count unclear</td><td>Jun 12</td><td>Argus</td></tr><tr><td>Asia-Pac condensate</td><td>July NWS unsold, pressuring August values &amp; cracks</td><td>Jun 3-5</td><td>Argus</td></tr><tr><td colspan="4">Source: Platts, Argus, MS</td></tr></table>

## High US exports, low Chinese imports...but little change expected in June

The reasons for this are the same as those discussed in prior research: unusually large exports from the United States, unusually low imports into China, and weak apparent demand.

The charts below show the first two. In rounded numbers, net exports of crude oil and refined products have increased from \~5 mb/d last year to nearly \~9 mb/d recently. At the same time, China's net imports of crude and products have declined from \~13 mb/d last year to \~7 mb/d recently. With \~4 mb/d more from the US, and \~6 mb/d less going into China, these two countries have shielded the rest of the world - including the Brent market - of 10 mb/d of tightness.

Exhibit 6: US seaborne net exports are nearly 4 mb/d higher than last year...  
![](images/5f7c2b03bb1e75f61ee8737355d7490d9600b5f3587b6b050ae56b77dfeabd5c.jpg)

<details>
<summary>line chart</summary>

| Month | 2021-2024 | 2025 | 2026 |
|-------|-----------|------|------|
| Jan   | ~5.5      | ~5.8 | ~5.7 |
| Apr   | ~6.5      | ~5.5 | ~5.3 |
| Jul   | ~8.5      | ~5.8 | ~5.6 |
| Oct   | ~5.0      | ~5.5 | ~5.4 |
| Jan   | ~5.5      | ~5.8 | ~5.7 |
</details>

Exhibit 7: ...whilst China's seaborne net imports are down \~ 6mb/d  
![](images/203fefb67108135658d833f6e174bc6fa6771bfd1660acab7ba681050f076309.jpg)

<details>
<summary>line chart</summary>

| Month | 2021-2024 | 2025 | 2026 |
|-------|-----------|------|------|
| Jan   | 15.0      | 13.0 | 12.0 |
| Apr   | 9.0       | 14.0 | 13.0 |
| Jul   | 7.0       | 13.0 | 14.0 |
| Oct   | 11.0      | 14.0 | 13.0 |
| Jan   | 13.0      | 15.0 | 14.0 |
</details>

It is unlikely, however, that both countries can sustain this. The key question is, of course, when will this come to an end? We previously mentioned that if US exports were to fall and/or China's imports were to increase before the Strait of Hormuz was open, the Brent market could have a period of strength again. That may still happen, but it has become less likely.

We can estimate US exports and China imports based on known future tanker movements. Naturally, fewer tanker movements are known further in advance, but they 'firm up' as time goes by. The two exhibits below show the 'firming fans' for both time series - they show how known tanker movements related to US exports and China imports have developed over time.

US net exports for June 2026 are currently tracking the path of April, so is still likely to end up in the 8.5-9 mb/d range, broadly where the May level ended as well. It is still early to judge July exports on this basis, which are still tracking below both the May and June trajectories so far, but are still above any of the previous 12 months.

Exhibit 8: Based on the pace at which known tanker movements firm up, seaborne net exports from the US are tracking similar to April, which is also where May levels ended up  
US seaborne total-petroleum net exports: firming fan  
![](images/e970a68bd85cf522c29fc71f90827ce45492b2f510897962ccbb4c36655461f7.jpg)

<details>
<summary>line chart</summary>

| Days to month-end | May 2026 | Jun 2026 | Jul 2026 |
| ----------------- | -------- | -------- | -------- |
| 75                | 0.0      | 0.0      | 0.0      |
| 50                | 1.0      | 1.0      | 1.0      |
| 25                | 3.0      | 3.0      | 3.0      |
| 0                 | 5.0      | 5.0      | 5.0      |
| -25               | 8.0      | 8.0      | 8.0      |
| -50               | 8.0      | 8.0      | 8.0      |
</details>

Source: Vortexa /pit/cargo-movements vintages, MS

Known tanker movements for June imply even lower net imports into China than for May, and data for July is also still tracking below the May path so far:

Exhibit 9: Along similar lines, known tanker movements in/out of China suggest that June net imports will likely be even lower than May, and July is also tracking below the May level as well  
China seaborne total-petroleum net imports: firming fan  
![](images/28373b130028fde53a60830f88deca0db36e48c9a559882d48a34bc046e0dd1b.jpg)

<details>
<summary>line chart</summary>

| Days to month-end | May 2026 | Jun 2026 | Jul 2026 |
| ----------------- | -------- | -------- | -------- |
| 75                | ~3       | ~3       | ~3       |
| 50                | ~7       | ~7       | ~7       |
| 25                | ~11      | ~9       | ~18      |
| 0                 | ~8       | ~8       | ~14      |
| -50               | ~8       | ~8       | ~14      |
</details>

Source: Vortexa /pit/cargo-movements vintages, MS

In addition to this, we can track China's buying activity by aggregating individual spot crude deals entered into by Chinese refiners, trading houses and other companies. Spot deals usually only cover \~6 mb/d out of \~11 mb/d of crude oil imports; the remainder comes from deliveries under longer-term contracts.

Spot deals supplied an unusually low $\sim 4.5$ mb/d in April, and an even lower $\sim 4.1$ mb/d in

May. So far, known-deals for June are tracking even lower than the paths for April and May, and data for July and August shows little to no improvement either:

Exhibit 10: Known spot crude deals entered into by Chinese players do not signal a pickup in buying interest yet

China crude deals tracking  
Known crude supply agreements, relative to last day of delivery month (mb/d)  
![](images/d0f14a9ea1a2a4e3bbc65be87f93982462b91819cfaabd309f8e1f6d2495e2d4.jpg)

<details>
<summary>line chart</summary>

| Days to the end of the delivery month | Sep 26 | Aug 26 | Jul 26 | Jun 26 | May 26 | Apr 26 | Mar 26 | Feb 26 | Jan 26 | Dec 25 | Nov 25 | Oct 25 |
| -------------------------------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| -100                                   | 0.5    | 0.3    | 0.4    | 0.6    | 0.7    | 0.8    | 0.9    | 1.0    | 1.1    | 1.2    | 1.3    | 1.4    |
| -50                                    | 1.5    | 1.3    | 1.4    | 1.6    | 1.7    | 1.8    | 1.9    | 2.0    | 2.1    | 2.2    | 2.3    | 2.4    |
| 0                                      | 2.5    | 2.3    | 2.4    | 2.6    | 2.7    | 2.8    | 2.9    | 3.0    | 3.1    | 3.2    | 3.3    | 3.4    |
| 50                                     | 3.5    | 3.3    | 3.4    | 3.6    | 3.7    | 3.8    | 3.9    | 4.0    | 4.1    | 4.2    | 4.3    | 4.4    |
| 100                                    | 4.5    | 4.3    | 4.4    | 4.6    | 4.7    | 4.8    | 4.9    | 5.0    | 5.1    | 5.2    | 5.3    | 5.4    |
</details>

Source: Argus, MS

Finally, on demand. We estimate that global refinery crude runs were down \~5.8 mb/d year-on-year in May, and with this, global crude demand was down by the same. This too has had a significant impact on crude oil prices.

However, our strong suspicion is that this sharply overstates the underlying demand decline. Instead, this decline in crude demand - and the associated decline in refined products production - is largely driven by delayed purchasing, not necessarily lower consumption. We have limited data to describe this effect fully on a global basis, but Exhibit 11 provides an example:

Exhibit 11: Expecting the Strait of Hormuz to open soon, German households have not been filling their heating oil tanks - consumption has continued but buying is delayed

[中间内容因长度限制已省略]

tional Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital

Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
