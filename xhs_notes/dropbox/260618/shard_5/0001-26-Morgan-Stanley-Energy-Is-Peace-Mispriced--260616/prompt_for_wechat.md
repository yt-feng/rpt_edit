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
## Energy | North America

# Is Peace Mispriced?

With a MoU between the US and Iran set to be formally signed on Friday, we refresh sensitivities for our E&P & Integrated coverage and revisit what's priced in. Oil E&Ps currently trade at a 13% median '27 FCF yield near strip (\$72 WTI). Intrinsically, valuations reflect \$66 WTI.

## Key Takeaways

Including today's move, WTI has now fallen by 29% since the US and Iran first announced a cease fire in early April, a \~\$30/bbl decline.  
Fully restoring production & inventories will take time. MS oil strategist expects Brent to be supported around \$90 in 3Q and at or above \$80 into next year.  
At strip (\~\$72 WTI), we estimate median 2027 FCF yield of 11% for our oil coverage (13% for US oil E&Ps, 8% for US Majors, and 9% for Canada).  
Intrinsically, we estimate oil producer valuations reflect an average WTI price of \~\$66/bbl, or \~13% below 12-month strip of \~\$75/bbl.  
With strong FCF & attractive valuations, the pull-back creates an opportunity to add exposure to Majors and high-quality E&Ps

Peace deal, pending release. Over the weekend, President Trump announced that the United States and Iran have reached a MoU (memorandum of understanding) to end the conflict with a formal signing ceremony taking place in Switzerland this Friday (see here and here for more). The full text of the agreement has yet to be released, but reports indicate it calls for an end to hostilities and re-opening of the Strait of Hormuz. Both sides have indicated that discussions surrounding Iran's nuclear capabilities will take place over the next 60 days.

Restoring production and replenishing inventories will take time. Including today's 5% move, WTI has now fallen by 29% since the US and Iran first announced a cease fire in early April, a \~\$30/bbl decline. Assuming a near-term re-opening of the Strait, MS Oil Strategist Martijn Rats expects it to take several weeks for tanker flow to be restored (more here); with 50% of production back by Sept, and 80% by December. On these assumptions, the summer still appears tight, with a \~3.4 mb/d average deficit in 3Q (1.1 mb/d looking at just OECD). The market screens closer to balance by 4Q, assuming no further disruptions to global supply, but at this point the world will still need to replenish the substantial inventory draws that have occurred since the start of the conflict. Martijn expects Brent to be supported around \$90 in 3Q and at or above \$80/bbl into next year.

Sensitizing commodity prices. Broadly speaking, FCF yields and intrinsic valuations screen attractive across much of our producer coverage. The pull-back creates an opportunity to add exposure to Majors and high-quality E&Ps.

\- Oil Producers: At strip (\~\$72 WTI), we estimate median 2027 FCF yield of

MS & CO. LLC

## Devin McDermott

Equity Analyst and Commodities Strategist

Devin.McDermott@morganstanley.com +1 212 761-1125

## Joe Laetsch, CFA

Equity Analyst

Joe.Laetsch@morganstanley.com +1 212 761-8804

## Svetlana Do

Research Associate

Svetlana.DO@morganstanley.com +1 212 761-2409

## Helen Lin

Research Associate

Helen.Lin@morganstanley.com +1 212 761-0766

## Justin W Latran, CFA

Research Associate

Justin.Latran@morganstanley.com +1 212 761-2869

## Jacqueline M Kenny

Research Associate

Jacqueline.Kenny@morganstanley.com +1 212 761-2253

EXPLORATION & PRODUCTION

<table><tr><td colspan="2">North America</td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

INTEGRATED OIL

<table><tr><td>North AmericaIndustry View</td><td>Attractive</td></tr></table>

DIVERSIFIED NATURAL GAS

<table><tr><td colspan="2">North America</td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

11% for our oil coverage (13% for oil E&Ps, 8% for US majors, and 9% for Canada). This would fall to 5% at \$55 and rise to 19% at \$105, implying a \~3 percentage points change for every \$10/bbl move in WTI. Intrinsically, we estimate oil producer valuations reflect an average WTI price of \~\$66/bbl, or \~13% below 12-month strip of \~\$75/bbl.

\- Gas E&Ps: Our median 2027 FCF yield for gas E&Ps sits at \~9% at prices near strip (\$3.50 Henry Hub), rising to 14% at \$4.50 and falling to 4% at \$2.50. Each \$0.50 move in Henry Hub changes the average FCF yield across our gas coverage by \~3 percentage points in '27. Intrinsically, we estimate gas E&Ps reflect a median Henry Hub price of \~\$3.38/mmbtu, in-line with the forward strip.

Exhibit 1: We estimate that oil E&Ps currently discount an average WTI price of \~\$65/bbl, well below the current 12-month strip of \~\$75.  
![](images/2d53c37bbc67672db5e3a3f37b7d827dc9905fd2b9953ced1b02e2128a4ea461.jpg)

<details>
<summary>line chart</summary>

| Quarter | Median NAV Implied Oil Price | FY1 Strip Price | FY2 Strip Price |
|---------|------------------------------|-----------------|-----------------|
| 1Q19    | ~$55                         | ~$55            | ~$55            |
| 2Q19    | ~$53                         | ~$53            | ~$53            |
| 3Q19    | ~$52                         | ~$52            | ~$52            |
| 4Q19    | ~$50                         | ~$50            | ~$50            |
| 1Q20    | ~$48                         | ~$48            | ~$48            |
| 2Q20    | ~$45                         | ~$45            | ~$45            |
| 3Q20    | ~$43                         | ~$43            | ~$43            |
| 4Q20    | ~$45                         | ~$45            | ~$45            |
| 1Q21    | ~$48                         | ~$48            | ~$48            |
| 2Q21    | ~$50                         | ~$50            | ~$50            |
| 3Q21    | ~$55                         | ~$55            | ~$55            |
| 4Q21    | ~$60                         | ~$60            | ~$60            |
| 1Q22    | ~$65                         | ~$70            | ~$70            |
| 2Q22    | ~$68                         | ~$75            | ~$75            |
| 3Q22    | ~$65                         | ~$70            | ~$70            |
| 4Q22    | ~$68                         | ~$75            | ~$75            |
| 1Q23    | ~$65                         | ~$70            | ~$70            |
| 2Q23    | ~$68                         | ~$75            | ~$75            |
| 3Q23    | ~$65                         | ~$70            | ~$70            |
| 4Q23    | ~$68                         | ~$75            | ~$75            |
| 1Q24    | ~$70                         | ~$78            | ~$78            |
| 2Q24    | ~$68                         | ~$75            | ~$75            |
| 3Q24    | ~$65                         | ~$70            | ~$70            |
| 4Q24    | ~$68                         | ~$75            | ~$75            |
| 1Q25    | ~$65                         | ~$70            | ~$70            |
| 2Q25    | ~$68                         | ~$75            | ~$75            |
| 3Q25    | ~$65                         | ~$70            | ~$70            |
| 4Q25    | ~$68                         | ~$75            | ~$75            |
| 1Q26    | ~$70                         | ~$80            | ~$80            |
| 2Q26    | ~$68                         | ~$78            | ~$78            |
| Current | ~$65                         | ~$75            | ~$75            |
</details>

Source: Company data, Bloomberg, FactSet, MS estimates

## Key Charts

Exhibit 2: Seaborne net exports from the US sit \~4 mb/d higher than last year...  
United States  
Seaborne net exports (crude + products, 30-day avg, mb/d)  
![](images/4edbad681fb6027015669d2b3b4142b9f5a7a8a9b2986f5930bbb8128e589734.jpg)

<details>
<summary>line chart</summary>

| Month | 2021-2024 | 2025 | 2026 |
|-------|-----------|------|------|
| Jan   | ~4.5      | ~5.5 | ~5.8 |
| Apr   | ~3.0      | ~5.0 | ~7.0 |
| Jul   | ~3.5      | ~5.5 | ~9.0 |
| Oct   | ~1.5      | ~6.0 | ~8.5 |
| Jan   | ~4.0      | ~5.8 | ~5.5 |
</details>

Source: Vortexa, MS  
Source: Vortexa, MS

Exhibit 4: Based on known tanker movements, it appears net seaborne oil imports into China will be down even further in June vs May.  
China seaborne total-petroleum net imports: firming fan  
![](images/112f956c1c3eb374a23a26319c840fc1b0ffd8ed30dbcf66dc4aedb24126f640.jpg)

<details>
<summary>line chart</summary>

| Days to month-end (dashed = month closes) | May 2026 (mb/d) | Jun 2026 (mb/d) | Jul 2026 (mb/d) |
| ----------------------------------------- | ---------------- | ---------------- | ---------------- |
| 75                                        | ~3               | ~3               | ~3               |
| 50                                        | ~7               | ~7               | ~7               |
| 25                                        | ~11              | ~9               | ~17              |
| 0                                         | ~8               | ~8               | ~14              |
| -25                                       | ~8               | ~8               | ~14              |
| -50                                       | ~8               | ~8               | ~14              |
</details>

Source: Vortexa, MS

Exhibit 3: While net seaborne imports into China have maintained their downward trend.  
China  
![](images/77fe3a6142aa99fc1c0adfcad3422519e95fe01d99a77fc656406b587ead1064.jpg)

<details>
<summary>line chart</summary>

| Month | 2021-2024 | 2025 | 2026 |
|-------|-----------|------|------|
| Jan   | ~13.5     | ~13.0 | ~15.0 |
| Apr   | ~12.0     | ~13.5 | ~10.0 |
| Jul   | ~11.0     | ~13.0 | ~7.0  |
| Oct   | ~11.5     | ~13.5 | -    |
| Jan   | ~12.5     | ~15.0 | -    |
</details>

Source: Vortexa, MS  
Source: Vortexa, MS

Exhibit 5: Global SPR releases are running at 2.5 mb/d during Apr-Jun, but are set to fall sharply to 0.7 mb/d in July and August.  
![](images/117fe53eb302919448ab10913b4cc85d506f5b08f5e5421fa685be4089ee4206.jpg)

<details>
<summary>stacked bar chart</summary>

Global strategic stock draws by source, Mar-Aug 2026 (mb/month)
| Month | US SPR (mb/month) | Japan (mb/month) | South Korea (mb/month) | UK (mb/month) | Spain (mb/month) | Hungary (mb/month) | India (mb/month) | Baltic States (mb/month) | Austria (mb/month) |
|---|---|---|---|---|---|---|---|---|---|
| Mar | 36 | 15 | 10 | 2 | 1 | 4 | 1 | 0 | 0 |
| Apr | 79 | 48 | 25 | 3 | 1 | 3 | 1 | 0 | 0 |
| May | 74 | 30 | 5 | 2 | 1 | 2 | 1 | 0 | 0 |
| Jun | 76 | 35 | 5 | 3 | 1 | 2 | 1 | 0 | 0 |
| Jul | 22 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| Aug | 20 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
Forecast
</details>

Additional IEA contributors also excluded: Canada 23.6, Turkiye 11.7, Poland 7.5, Netherlands 5.4, Mexico 3.9 (\~52 mb; Canada and Mexico are production-increase commitments, not stock releases).  
Source: US DOE Weekly Petroleum Status Report, Japan METI, Agrus, Platts, MS

Exhibit 6: Global oil and refined product inventories have been drawing rapidly since the start of the conflict.

Observable crude oil and oil products inventories  
![](images/12d8c31b2244be245232bf1d9a75f7f737ba41879de69c9424c005b3150035ca.jpg)

<details>
<summary>line chart</summary>

| Month | 2022  | 2023  | 2024  | 2025  | 2026  |
|-------|-------|-------|-------|-------|-------|
| Jan   | ~8150 | ~8180 | ~8170 | ~8160 | ~8550 |
| Apr   | ~8180 | ~8200 | ~8190 | ~8170 | ~8400 |
| Jul   | ~8150 | ~8190 | ~8180 | ~8250 | ~8250 |
| Oct   | ~8170 | ~8180 | ~8160 | ~8450 | ~8350 |
| Jan   | ~8160 | ~8170 | ~8150 | ~8500 | ~8300 |
</details>

Note: Inventories include SPR  
Source: IEA, EIA/DOE, PJK, IE, Genscape, PAJ, Platts, Vortexa, MS  
Source: IEA, EIA/DOE, PJK, IE, Genscape, PAJ, Platts, Vortexa, MS

Exhibit 8: OECD oil stocks have fallen further below 5-year averages, driven by a large draw in the US...  
Total Crude Oil Inventories (mln bbls)  
![](images/3b01c0f3bc925a6966f3a7d008ed563cabe348e2d0021bec472657a111f0ca68.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 | 5Y Avg | 5Y Range |
|-------|------|------|--------|----------|
| 1     | 950  | 970  | 1050   | 1280     |
| 4     | 960  | 975  | 1045   | 1275     |
| 7     | 970  | 980  | 1040   | 1270     |
| 10    | 980  | 990  | 1035   | 1265     |
| 13    | 990  | 1000 | 1030   | 1260     |
| 16    | 1000 | 1005 | 1025   | 1255     |
| 19    | 995  | 1000 | 1020   | 1250     |
| 22    | 990  | 995  | 1015   | 1245     |
| 25    | 985  | 990  | 1010   | 1240     |
| 28    | 980  | 985  | 1005   | 1235     |
| 31    | 975  | 980  | 1000   | 1230     |
| 34    | 970  | 975  | 995    | 1225     |
| 37    | 965  | 970  | 990    | 1220     |
| 40    | 960  | 965  | 985    | 1215     |
| 43    | 955  | 960  | 980    | 1210     |
| 46    | 950  | 955  | 975    | 1205     |
| 49    | 945  | 950  | 970    | 1200     |
| 52    | 940  | 945  | 965    | 1195     |
</details>

Source:  
EIA, PJK International, IE Singapore, PAJ, Genscape, FEDCom/Platts. Includes US SPR.

Exhibit 10: Implied US product demand has held up well so far...  
![](images/7f54632c359de4fef3baf8a9b535b3eda60924a4d115943a99b0bb2a11ed03c4.jpg)

<details>
<summary>line chart</summary>

| Month | 5Y Min-Max | 5Y Avg | 2025 | 2026 |
|-------|------------|--------|------|------|
| J     | ~19        | ~19    | ~19  | ~19  |
| F     | ~22        | ~20    | ~20  | ~21  |
| M     | ~21        | ~19    | ~19  | ~21  |
| A     | ~20        | ~19    | ~19  | ~20  |
| M     | ~18        | ~19    | ~19  | ~21  |
| J     | ~20        | ~19    | ~19  | ~20  |
| J     | ~21        | ~20    | ~20  | ~21  |
| A     | ~21        | ~20    | ~20  | ~21  |
| S     | ~23        | ~21    | ~21  | ~22  |
| O     | ~21        | ~20    | ~20  | ~21  |
| N     | ~20        | ~19    | ~19  | ~20  |
| D     | ~23        | ~21    | ~20  | ~21  |
</details>

Source:  
US EIA, MS.

Exhibit 7: ...including large draws in commercial storage.  
Observable crude oil and oil products inventories  
![](images/aae8d92d109ac68b917f9579611457fcc5aed148c3d96957b152f9387efea3ac.jpg)

<details>
<summary>line chart</summary>

| Month | 2022  | 2023  | 2024  | 2025  | 2026  |
|-------|-------|-------|-------|-------|-------|
| Jan   | ~6850 | ~7050 | ~6950 | ~6880 | ~7350 |
| Apr   | ~6750 | ~7000 | ~6980 | ~6950 | ~7150 |
| Jul   | ~6850 | ~6950 | ~6900 | ~7050 | ~7100 |
| Oct   | ~6950 | ~6900 | ~6850 | ~7250 | ~7150 |
| Jan   | ~6850 | ~6850 | ~6800 | ~7300 | ~7150 |
</details>

Note: inventories on land, at sea and in-transit, not including SPR in OECD countries  
Source: IEA, EIA/DOE, PJK, IE, Genscape, PAJ, Platts, Vortexa, MS  
Source: IEA, EIA/DOE, PJK, IE, Genscape, PAJ, Platts, Vortexa, MS

Exhibit 9: ...While refined product stocks have continued to grind lower as well  
Total Refined Products Inventories (mln bbls)  
![](images/71a0abcc63af97735337a3f311b20ac0e5535beef8569484827131d34938573c.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 | 5Y Avg | 5Y Range |
|-------|------|------|--------|----------|
| 1     | 630  | 640  | 630    | 630-710  |
| 4     | 640  | 650  | 640    | 640-720  |
| 7     | 630  | 640  | 630    | 630-710  |
| 10    | 610  | 620  | 610    | 610-680  |
| 13    | 600  | 610  | 600    | 600-670  |
| 16    | 590  | 580  | 590    | 590-660  |
| 19    | 580  | 570  | 580    | 580-650  |
| 22    | 570  | 560  | 570    | 570-640  |
| 25    | 580  | 570  | 580    | 580-650  |
| 28    | 590  | 580  | 590    | 590-660  |
| 31    | 600  | 590  | 600    | 600-670  |
| 34    | 610  | 600  | 610    | 610-680  |
| 37    | 620  | 610  | 620    | 620-690  |
| 40    | 630  | 620  | 630    | 630-700  |
| 43    | 640  | 630  | 640    | 640-710  |
| 46    | 650  | 640  | 650    | 650-720  |
| 49    | 660  | 650  | 660    | 660-730  |
| 52    | 670  | 660  | 670    | 670-740  |
</details>

Source:  
EIA, PJK International, IE Singapore, PAJ, Genscape, FEDCom/Platts

Exhibit 11: ...with gasoline consumption still within normal  
![](images/525711fccacd0550e8a1736926e55a9d573a82f2732b696adb3af8ad1e52840c.jpg)

<details>
<summary>line chart</summary>

| Month | 5Y Min-Max | 5Y Avg | 2025 | 2026 |
| --- | --- | --- | --- | --- |
| J | 7.5 | 8.0 | 8.5 | 8.0 |
| F | 8.0 | 8.5 | 8.0 | 8.5 |
| M | 8.5 | 9.0 | 8.5 | 9.0 |
| A | 9.0 | 9.5 | 9.0 | 9.5 |
| M | 9.5 | 10.0 | 9.5 | 10.0 |
| J | 10.0 | 10.5 | 10.0 | 10.5 |
| J | 10.5 | 11.0 | 10.5 | 11.0 |
| A | 11.0 | 11.5 | 11.0 | 11.5 |
| S | 11.5 | 12.0 | 11.5 | 12.0 |
| O | 12.0 | 12.5 | 12.0 | 12.5 |
| N | 12.5 | 13.0 | 12.5 | 13.0 |
| D | 13.0 | 13.5 | 13.0 | 13.5 |
| D | 13.5 | 14.0 | 13.5 | 14.0 |
| D | 14.0 | 14.5 | 14.0 | 14.5 |
| D | 14.5 | 15.0 | 14.5 | 15.0 |
| D | 15.0 | 15.5 | 15.0 | 15.5 |
| D | 15.5 | 16.0 | 15.5 | 16.0 |
| D | 16.0 | 16.5 | 16.0 | 16.5 |
| D | 16.5 | 17.0 | 16.5 | 17.0 |
| D | 17.0 | 17.5 | 17.0 | 17.5 |
| D | 17.5 | 18.0 | 17.5 | 18.0 |
| D | 18.0 | 18.5 | 18.0 | 18.5 |
| D | 18.5 | 19.0 | 18.5 | 19.0 |
| D | 19.0 | 19.5 | 19.0 | 19.5 |
| D | 19.5 | 20.0 | 19.5 | 20.0 |
| D | 20.0 | 20.5 | 20.0 | 20.5 |
| D | 20.5 | 21.0 | 20.5 | 21.0 |
| D | 21.0 | 21.5 | 21.0 | 21.5 |
| D | 21.5 | 22.0 | 21.5 | 22.0 |
| D | 22.0 | 22.5 | 22.0 | 22.5 |
| D | 22.5 | 23.0 | 22.5 | 23.0 |
| D | 23.0 | 23.5 | 23.0 | 23.5 |
| D | 23.5 | 24.0 | 23.5 | 24.0 |
| D | 24.0 | 24.5 | 24.0 | 24.5 |
| D | 24.5 | 25.0 | 24.5 | 25.0 |
| D | 25.0 | 25.5 | 25.0 | 25.5 |
| D | 25.5 | 26.0 | 25.5 | 26.0 |
| D | 26.0 | 26.5 | 26.0 | 26.5 |
| D | 26.5 | 27.0 | 26.5 | 27.0 |
| D | 27.0 | 27.5 | 27.0 | 27.5 |
| D | 27.5 | 28.0 | 27.5 | 28.0 |
| D | 28.0 | 28.5 | 28.0 | 28.5 |
| D | 28.5 | 29.0 | 28.5 | 29.0 |
| D | 29.0 | 29.5 | 29.0 | 29.5 |
| D | 29.5 | 30.0 | 29.5 | 30.0 |
| D | 30.0 | 30.5 | 30.0 | 30.5 |
| D | 30.5 | 31.0 | 30.5 | 31.0 |
| D | 31.0 | 31.5 | 31.0 | 31.5 |
| D | 31.5 | 32.0 | 31.5 | 32.0 |
| D | 32.0 | 32.5 | 32.0 | 32.5 |
| D | 32.5 | 33.0 | 32.5 | 33.0 |
| D | 33.0 | 33.5 | 33.0 | 33.5 |
| D | 33.5 | 34.0 | 33.5 | 34.0 |
| D | 34.0 | 34.5 | 34.0 | 34.5 |
| D | 34.5 | 35.0 | 34.5 | 35.

[中间内容因长度限制已省略]

ents and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Exploration & Production

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Antero Resources Corp (AR.N)</td><td>O (04/17/2024)</td><td>$34.03</td></tr><tr><td>APA Corp (APA.O)</td><td>U (04/15/2024)</td><td>$34.77</td></tr><tr><td>Chord Energy Corporation (CHRD.O)</td><td>O (03/27/2026)</td><td>$127.60</td></tr><tr><td>CNX Resources Corp (CNX.N)</td><td>U (01/10/2025)</td><td>$32.96</td></tr><tr><td>Comstock Resources Inc. (CRK.N)</td><td>E (01/10/2025)</td><td>$13.05</td></tr><tr><td>ConocoPhillips (COP.N)</td><td>O (12/16/2024)</td><td>$112.26</td></tr><tr><td>Devon Energy Corp (DVN.N)</td><td>O (12/11/2023)</td><td>$43.53</td></tr><tr><td>Diamondback Energy Inc (FANG.O)</td><td>O (12/11/2020)</td><td>$189.96</td></tr><tr><td>EOG Resources Inc (EOG.N)</td><td>E (12/11/2023)</td><td>$131.98</td></tr><tr><td>EQT Corp. (EQT.N)</td><td>O (11/18/2021)</td><td>$50.75</td></tr><tr><td>Expand Energy Corp (EXE.O)</td><td>O (01/10/2025)</td><td>$87.90</td></tr><tr><td>Matador Resources Co (MTDR.N)</td><td>E (01/10/2025)</td><td>$51.38</td></tr><tr><td>Murphy Oil Corporation (MUR.N)</td><td>U (01/22/2025)</td><td>$36.45</td></tr><tr><td>Northern Oil &amp; Gas Inc. (NOG.N)</td><td>U (08/18/2025)</td><td>$19.96</td></tr><tr><td>Occidental Petroleum Corp (OXY.N)</td><td>E (08/18/2025)</td><td>$54.46</td></tr><tr><td>Ovintiv Inc (OVV.N)</td><td>E (03/27/2026)</td><td>$54.31</td></tr><tr><td>Permian Resources Corp (PR.N)</td><td>O (01/10/2025)</td><td>$18.90</td></tr><tr><td>Range Resources Corp. (RRC.N)</td><td>E (03/26/2025)</td><td>$37.46</td></tr><tr><td>Tourmaline Oil Corp. (TOU.TO)</td><td>E (01/10/2025)</td><td>C$61.26</td></tr><tr><td>Viper Energy Inc (VNOM.O)</td><td>O (08/18/2025)</td><td>$43.69</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Integrated Energy

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Devin McDermott</td></tr><tr><td>Canadian Natural Resources Ltd (CNQ.TO)</td><td>E (10/07/2021)</td><td>C$61.69</td></tr><tr><td>Cenovus Energy (CVE.TO)</td><td>O (10/07/2021)</td><td>C$37.96</td></tr><tr><td>Chevron Corporation (CVX.N)</td><td>O (08/04/2025)</td><td>$180.40</td></tr><tr><td>Exxon Mobil Corporation (XOM.N)</td><td>O (05/14/2024)</td><td>$140.92</td></tr><tr><td>Imperial Oil Ltd (IMO.TO)</td><td>E (10/07/2021)</td><td>C$168.35</td></tr><tr><td>Suncor Energy Inc (SU.TO)</td><td>E (12/16/2024)</td><td>C$83.39</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Diversified Natural Gas

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td>Devin McDermott</td><td></td><td></td></tr><tr><td>Cheniere Energy Inc (LNG.N)</td><td>O (03/23/2026)</td><td>$235.25</td></tr><tr><td>Cheniere Energy Partners LP (CQP.N)</td><td>E (09/20/2019)</td><td>$60.34</td></tr><tr><td>Excelerate Energy Inc (EE.N)</td><td>E (11/06/2025)</td><td>$35.04</td></tr><tr><td>NextDecade Corporation (NEXT.O)</td><td>E (09/12/2025)</td><td>$7.73</td></tr><tr><td>Venture Global Inc (VG.N)</td><td>O (03/23/2026)</td><td>$11.70</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
