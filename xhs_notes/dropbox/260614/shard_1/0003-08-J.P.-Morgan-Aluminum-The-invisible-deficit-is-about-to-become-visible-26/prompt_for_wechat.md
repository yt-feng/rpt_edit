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
## Aluminum

The invisible deficit is about to become visible

- Even with higher Chinese supply forecasts and a base case that Middle East smelters begin the process of ramping up idled production next quarter, we still forecast a more than 2 mmt aluminum deficit over 2Q26-4Q26.  
- For now, this supply gap is being bridged first by a draw in “invisible” inventories (producer/trader/consumer stocks).  
- Yet these hidden stocks are also now depleting, with industry feedback suggesting only \~2 more months of drawdown coverage.  
- With our balances showing a primary aluminum deficit of nearly 1 mmt that still needs to be covered in 2H26, the deficit should increasingly transmit into draws in visible inventory, which are heavily concentrated (75%) in China.  
- A sustained, material drawing trend in Chinese inventory should support higher SHFE prices. To keep needed Chinese product exports flowing, LME prices must stay high enough to keep the export arb open. This arb chase is the next core fundamental driver for higher LME prices.  
- While aluminum could come under initial knee-jerk pressure following a sustained re-opening of the Strait of Hormuz, we don't think it will be sustained as Middle East production will still likely take multiple quarters to approach normalcy, keeping deficits in place.  
- In short, the sharp deficit in aluminum is taking time to transmit through the supply chain, a process that will continue even after the Strait reopens. We are in the middle innings and still think aluminum prices are biased higher in the coming quarters.  
- We still expect an ultimate push towards \$4,000/mt and now see aluminum prices averaging \$3,750/mt over 2H26.  
- Chinese aluminum export controls, motivated by ensuring domestic supply security, remain a significant bullish risk in our view.  
- Accelerating Chinese-funded supply outside China (Indonesia, Angola, Saudi, etc.) does little to change the supply gap in the near term, but longer term it is a momentous shift, essentially ending a period of global supply discipline in aluminum.  
- Even as overall supply and demand remains relatively balanced in 2027, we think prices will begin to roll over next year, falling back below \$3,000/mt in 2H27 as the spectre of looming 2028 oversupply, which is now approaching 1 mmt, comes into sharper focus.

## Global Commodities Research

## Gregory C. Shearer

(44-20) 7134-8161

gregory.c.shearer@JPM.com

JPM Securities plc

## Ali A. Ibrahim

(44-20) 3493-6438

ali.ibrahim@JPM.com

JPM Securities plc

## Ananyashree Gupta

(91-22) 6157 3627

ananyashree.gupta@jpmchase.com

JPM India Private Limited

The invisible to become visible. Despite boosting estimates for Chinese supply even further and continuing to assume a more imminent opening of the Strait of Hormuz that allows Middle East smelters to begin the process of ramping up idled production next quarter, in our latest aluminum balance update we still forecast a monumental supply hole that needs to be filled. Overall, we now forecast a 1.7 mmt primary aluminum deficit in 2026 with 2Q26-4Q26 amounting to an implied 2.3 mmt draw on inventory over three quarters (Figure 1). With our assumption that Middle East smelter restarts begin in 3Q26 and accelerate over 4Q26 and 1Q27, this current quarter marks the peak deficit in our forecast with a 1.3 mmt implied draw in 2Q26 (Figure 2). However, while the push higher in global premiums reflects this tightness, global visible aluminum inventory, after drawing in the last few weeks, is basically still only roughly on par with end-February levels (Figure 3 & Figure 4).

Figure 1: Global primary aluminum balance, quarterly  
![](images/e48bb863614e795c97bed0467409fb932175bb035076a9bb2aeca21f9454f4d0.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Value (Thousand mt) | Annual (RHS) |
|---|---|---|
| 1Q21 | 300 | -900 |
| 2Q21 | -850 | -900 |
| 3Q21 | -400 | -900 |
| 4Q21 | -600 | -900 |
| 1Q22 | -300 | -300 |
| 2Q22 | -250 | -300 |
| 3Q22 | 250 | -300 |
| 4Q22 | 750 | 300 |
| 1Q23 | -600 | 300 |
| 2Q23 | 50 | 300 |
| 3Q23 | 250 | 300 |
| 4Q23 | 600 | 300 |
| 1Q24 | -350 | -100 |
| 2Q24 | -150 | -100 |
| 3Q24 | -150 | -100 |
| 4Q24 | 350 | -100 |
| 1Q25 | -600 | -150 |
| 2Q25 | 150 | -150 |
| 3Q25 | 650 | -150 |
| 4Q25 | -1,250 | -1,500 |
| 1Q26 | -750 | -1,500 |
| 2Q26 | -350 | -1,500 |
| 3Q26 | 300 | -1,500 |
| 4Q26 | -550 | -1,500 |
| 1Q27 | 250 | -1,500 |
| 2Q27 | 150 | -1,500 |
| 3Q27 | 150 | -1,500 |
</details>

Source: Company Reports, Government and Industry data, IAI, CRU, JPM Commodities Research

Figure 2: JPM estimates for Middle East primary aluminum production, quarterly  
![](images/0c09f3b7208db02c13d70521d5f6b77b00afa1a4ff6471164e1992d52f17fb4b.jpg)

<details>
<summary>stacked bar chart</summary>

| Quarter | Bahrain (Thousand mt) | Iran (Thousand mt) | Oman (Thousand mt) | Qatar (Thousand mt) | Saudi Arabia (Thousand mt) | UAE (Thousand mt) |
|---|---|---|---|---|---|---|
| 1Q25 | 1600 | 700 | 300 | 900 | 1100 | 2200 |
| 2Q25 | 1600 | 700 | 300 | 900 | 1100 | 2200 |
| 3Q25 | 1600 | 700 | 300 | 900 | 1100 | 2200 |
| 4Q25 | 1600 | 700 | 300 | 900 | 1100 | 2200 |
| 1Q26 | 1400 | 600 | 200 | 800 | 1000 | 2400 |
| 2Q26 | 600 | 300 | 100 | 500 | 800 | 1300 |
| 3Q26 | 600 | 300 | 100 | 500 | 800 | 1300 |
| 4Q26 | 800 | 400 | 200 | 600 | 900 | 1400 |
| 1Q27 | 1200 | 500 | 300 | 700 | 1100 | 1500 |
| 2Q27 | 1400 | 600 | 300 | 800 | 1200 | 1600 |
| 3Q27 | 1400 | 600 | 300 | 800 | 1200 | 1600 |
| 4Q27 | 1400 | 600 | 300 | 800 | 1200 | 1600 |
| 1Q28 | 1600 | 700 | 400 | 900 | 1300 | 1700 |
| 2Q28 | 1600 | 700 | 400 | 900 | 1300 | 1700 |
| 3Q28 | 1600 | 700 | 400 | 900 | 1300 | 1700 |
| 4Q28 | 1600 | 700 | 400 | 900 | 1300 | 1700 |
</details>

Source: Company reports, CRU, JPM Commodities Research

In our view this mismatch points to a significant, industry-wide destock of more “invisible” inventory, stocks of aluminum not captured in exchange and social inventory tallies, being the first mechanism called upon to backfill the chasm in supply this quarter. This includes stocks of metal held by Middle East producers in consumer regions (Asia, Europe, US) which have helped buffer the blow from disrupted production and logistics so far. Moreover, this also includes trader and merchant stocks not held at the exchange to avoid the higher LME rent. Given the backwardated forward curve for most of this quarter, which penalizes stock holders who need to finance and carry this metal, there has been strong incentive to sell off this inventory too and for consumers themselves to draw down their carrying inventory buffer as well to avoid the backwardation penalty as much as possible.

Gregory C. Shearer AC (44-20) 7134-8161 Ananyashree Gupta (91-22) 6157 3627  
gregory.c.shearer@JPM.com ananyashree.gupta@jpmchase.com  
JPM Securities plc JPM India Private Limited  
Ali A. Ibrahim (44-20) 3493-6438  
ali.ibrahim@JPM.com  
JPM Securities plc

Global Markets Strategy

12 June 2026

Figure 3: Regional aluminum ingot premiums  
![](images/e8da4b995ef58cb07a233159fa1edfd2aedf96c67fb97b97f789d49d3ccb0843.jpg)

<details>
<summary>line chart</summary>

| Date    | Rotterdam (duty paid) | US MW (RHS) | Japan (spot) |
|---------|------------------------|-------------|--------------|
| Jun-20  | ~100                   | ~100        | ~100         |
| Nov-20  | ~150                   | ~150        | ~150         |
| Apr-21  | ~250                   | ~250        | ~200         |
| Sep-21  | ~350                   | ~350        | ~250         |
| Feb-22  | ~550                   | ~250        | ~300         |
| Jul-22  | ~400                   | ~200        | ~350         |
| Dec-22  | ~300                   | ~150        | ~400         |
| May-23  | ~350                   | ~150        | ~450         |
| Oct-23  | ~300                   | ~150        | ~500         |
| Mar-24  | ~350                   | ~150        | ~550         |
| Aug-24  | ~350                   | ~150        | ~600         |
| Jan-25  | ~350                   | ~150        | ~650         |
| Jun-25  | ~350                   | ~150        | ~700         |
| Nov-25  | ~400                   | ~150        | ~750         |
| Apr-26  | ~650                   | ~126        | ~867         |
</details>

Source: CRU

Figure 4: Global visible aluminum inventories  
![](images/ebdd979ff835d9fa66fa482b412e2b83c148306b51224cacc8d97f12cbd6fef4.jpg)

<details>
<summary>stacked bar chart</summary>

| Date | LME (On Warrant) (Thousand mt) | LME (Off Warrant) (Thousand mt) | COMEX (Thousand mt) | SHFE (Thousand mt) | Unregistered China (Ex-SHFE) (Thousand mt) |
|---|---|---|---|---|---|
| Feb-20 | 1000 | 500 | 300 | 200 | 1000 |
| Jun-20 | 1500 | 800 | 400 | 250 | 1200 |
| Oct-20 | 1400 | 900 | 450 | 300 | 1300 |
| Feb-21 | 1600 | 1000 | 500 | 350 | 1400 |
| Jun-21 | 1800 | 1100 | 550 | 400 | 1500 |
| Oct-21 | 1200 | 600 | 350 | 250 | 1100 |
| Feb-22 | 800 | 400 | 250 | 150 | 900 |
| Jun-22 | 600 | 300 | 200 | 120 | 750 |
| Oct-22 | 700 | 350 | 220 | 130 | 850 |
| Feb-23 | 900 | 450 | 300 | 160 | 1150 |
| Jun-23 | 850 | 420 | 280 | 155 | 1125 |
| Oct-23 | 950 | 480 | 320 | 175 | 1250 |
| Feb-24 | 1100 | 550 | 380 | 215 | 1450 |
| Jun-24 | 1250 | 650 | 450 | 265 | 1650 |
| Oct-24 | 1150 | 620 | 430 | 255 | 1625 |
| Feb-25 | 950 | 480 | 350 | 215 | 1350 |
| Jun-25 | 850 | 450 | 320 | 215 | 1325 |
| Oct-25 | 980 | 490 | 360 | 235 | 1450 |
| Feb-26 | 880 | 470 | 340 | 225 | 1475 |
| Jun-26 | 780 | 430 | 315 | 215 | 1475 |
</details>

Source: CRU, LME, SHFE, COMEX, SMM. Regional includes stocks in Shanghai, Jiangsu, Nanhai, Zhejiang, Tianjin, Henan, Shandong, Chongqing.

Feedback from our discussions around recent industry conferences, including the Harbor Aluminum Summit last week, indicate that these hidden pools of inventory are now also running lean, with general expectations that there is now around 2 more months of drawdown coverage of this more “invisible” inventory. However, our balance still shows a primary aluminum deficit of nearly 1 mmt that still needs to be covered in 2H26 (with a 700 kmt deficit in 3Q26) as, even when the Strait of Hormuz more fully reopens (our base case is this month), smelter ramp ups take time, even 1-2 quarters following a controlled shutdown. As invisible industry stockpiles begin to exhaust in the coming months, we think the ongoing aluminum deficit will begin to become much more “visible”, necessitating draws from global surveyed stocks where China holds about 75% of the global \~1.7 mmt of visible inventory.

In short, the sharp deficit in aluminum is taking time to transmit through the supply chain, a process that will continue even after the Strait reopens. We are in the middle innings and still think aluminum prices are biased higher in the coming quarters as the next stretch involves a transition towards sharper draws in visible inventory concentrated in China. Given the magnitude of the supply shortage facing the market, the ex-China market needs China to continue to backfill for lost Middle East tonnes via boosted levels of aluminum product exports (Figure 5). While a jump higher in Chinese production to push above the 45 mmt capacity cap amid expanded producer margins combined with softer domestic ingot demand for now have both helped so far to insulate China's inventory level from significant draws, we don't think this can sustain. Indeed, this week brought a \~63 kt wow draw in Chinese social inventory, the largest weekly draw since December 2023 (Figure 6). Moreover, while we see Chinese supply pushing above 45 mmt on maximized efficiency gains at some smelters, we do think ongoing inspections and greater scrutiny of key industrial energy use and emissions will likely act as a brake, preventing supply from significantly blowing past the capacity cap (Figure 7).

Gregory C. Shearer AC (44-20) 7134-8161 Ananyashree Gupta (91-22) 6157 3627  
gregory.c.shearer@JPM.com ananyashree.gupta@jpmchase.com  
JPM Securities plc JPM India Private Limited  
Ali A. Ibrahim (44-20) 3493-6438  
ali.ibrahim@JPM.com  
JPM Securities plc

Figure 5: Chinese unwrought aluminum and aluminum product exports  
LHS: Thousand mt; RHS: Percent change, yoy  
![](images/f54b6e6a3a6669f936362a02cadab65d0b6d381864c0238c3c9c2fcdb78a03cf.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month    | Monthly Exports | YoY Growth (RHS) |
| -------- | --------------- | ---------------- |
| Jun-21   | 450             | 20%              |
| Oct-21   | 500             | 15%              |
| Feb-22   | 600             | 30%              |
| Jun-22   | 680             | 45%              |
| Oct-22   | 550             | 25%              |
| Feb-23   | 450             | -10%             |
| Jun-23   | 480             | -30%             |
| Oct-23   | 500             | -15%             |
| Feb-24   | 550             | 0%               |
| Jun-24   | 600             | 15%              |
| Oct-24   | 680             | 30%              |
| Feb-25   | 500             | -10%             |
| Jun-25   | 550             | -20%             |
| Oct-25   | 580             | -15%             |
| Feb-26   | 600             | 10%              |
</details>

Source: China Customs, JPM Commodities Research

## Global Markets Strategy

Aluminum

12 June 2026

Figure 6: Weekly change in China visible aluminum inventory (SHFE + regional warehouses).  
X-axis = weeks post Chinese New Year (week 0 = week closest to start of CNY), Y-axis = kt of aluminum increase / (decrease)  
![](images/b8313ea76b12298e76020dc76d1e7f35cd51045eb4cf6da9284a28c4e6cc825f.jpg)

<details>
<summary>bar chart</summary>

| X-Axis | 2026 | 5-yr avg |
|---|---|---|
| -3 | 10 | -10 |
| -1 | 40 | 5 |
| 2 | 270 | 250 |
| 4 | 90 | 50 |
| 6 | 30 | 10 |
| 8 | 35 | -20 |
| 10 | 40 | -30 |
| 12 | 10 | -20 |
| 14 | -10 | -30 |
| 16 | -20 | -40 |
| 18 | -70 | -30 |
| 20 | -10 | -20 |
| 22 | -5 | -10 |
| 24 | -5 | -5 |
| 26 | -5 | 5 |
| 28 | -5 | 5 |
| 30 | -5 | 0 |
| 32 | -5 | 0 |
| 34 | -5 | 0 |
| 36 | -5 | 10 |
| 38 | -5 | 30 |
| 40 | -5 | -5 |
| 42 | -5 | -10 |
| 44 | -5 | -10 |
</details>

Source: SHFE, CRU, SMM, JPM Commodities, \*First and second weeks grouped together due to lagged inventory reporting.

Eventually, given we still see $1.6\%$ yoy domestic demand growth in China this year (2.5% yoy growth inclusive of boosted exports), the continued excess export pull on Chinese supply from the rest of the world is expected to drive a more pronounced and prolonged visible destocking in Chinese inventory over the coming months (Figure 8). Amid this sharper destocking and relative tightening in China's inventory coverage, we see Chinese SHFE aluminum prices pushing higher. With transaction prices in the rest of the world needing to keep China's product export arb open to receive sufficient Chinese metal, we see this arb friction being the fundamental catalyst for LME aluminum prices to continue to push higher (Figure 10).

Figure 7: Annualized Chinese quarterly primary aluminum production estimates  
![](images/bdb78b274404a13fc98d413c02598aaf2617596df9aec9ee1f6949af12c1f5ae.jpg)

<details>
<summary>bar chart</summary>

| Quarter | Value (Thousand mt) |
|---|---|
| 1Q21 | 39,000 |
| 2Q21 | 38,800 |
| 3Q21 | 38,500 |
| 4Q21 | 37,500 |
| 1Q22 | 38,800 |
| 2Q22 | 40,500 |
| 3Q22 | 40,800 |
| 4Q22 | 40,800 |
| 1Q23 | 40,800 |
| 2Q23 | 40,800 |
| 3Q23 | 42,500 |
| 4Q23 | 42,500 |
| 1Q24 | 42,300 |
| 2Q24 | 42,800 |
| 3Q24 | 43,500 |
| 4Q24 | 43,500 |
| 1Q25 | 43,500 |
| 2Q25 | 43,800 |
| 3Q25 | 44,500 |
| 4Q25 | 44,500 |
| 1Q26 | 45,000 |
| 2Q26 | 45,000 |
| 3Q26 | 45,500 |
| 4Q26 | 45,500 |
| 1Q27 | 45,500 |
| 2Q27 | 45,500 |
| 3Q27 | 45,500 |
| 4Q27 | 45,500 |
| 1Q28 | 45,500 |
| 2Q28 | 45,500 |
| 3Q28 | 45,500 |
</details>

Source: CRU, JPM Commodities Research

Figure 8: Total visible China aluminum inventory (SHFE + regional warehouses)  
Y-axis: Thousand mt; X-axis: Weeks around Chinese New Year (0 = week closest to start of CNY)  
![](images/5fece18294fbcf57cebd505706518d273a8333b44c1c7e316a52a4f680336c55.jpg)

<details>
<summary>line chart</summary>

| Year | 5-yr range | 5-yr avg | 2025 | 2026 |
|------|------------|----------|------|------|
| -4   | 750        | 600      | 500  | 750  |
| -2   | 800        | 650      | 450  | 800  |
| 0    | 900        | 700      | 400  | 900  |
| 2    | 1000       | 800      | 500  | 1100 |
| 4    | 1100       | 900      | 600  | 1200 |
| 6    | 1200       | 1000     | 700  | 1300 |
| 8    | 1250       | 1050     | 800  | 1400 |
| 10   | 1200       | 1000     | 750  | 1450 |
| 12   | 1150       | 950      | 700  | 1400 |
| 14   | 1100       | 900      | 650  | 1350 |
| 16   | 1050       | 850      | 600  | 1300 |
| 18   | 1000       | 800      | 550  | 1250 |
| 20   | 950        | 750      | 500  | 1200 |
| 22   | 900        | 700      | 450  | 1150 |
| 24   | 850        | 650      | 450  | 1100 |
| 26   | 800        | 650      | 450  | 1100 |
| 28   | 750        | 650      | 450  | 1100 |
| 30   | 750        | 650      | 450  | 1100 |
| 32   | 750        | 650      | 450  | 1100 |
| 34   | 750        | 650      | 450  | 1100 |
| 36   | 750        | 650      | 450  | 1100 |
| 38   | 750        | 650      | 450  | 1100 |
| 40   | 750        | 650      | 450  | 1100 |
| 42   | 750        | 650      | 450  | 1100 |
| 44   | 750        | 650      | 450  | 1100 |
| 46   | 750        | 650      | 450  | 1100 |
</details>

Source: SHFE, CRU, SMM, JPM Commodities Research

The journey is taking longer but the destination remains the same. With our updated balance views, we remain bullish on aluminum over 2H26 and still see LME prices pushing towards \$4,000/mt on a spot basis in the near term. So far this week, aluminum has come under pressure amid a broader risk-off move, falling back towards \$3,500/mt and consumer buying support as the backwardation at the front of the curve eased significantly. We don’t think this bearish bout of volatility is a sea change, rather, we

view it as another breather in aluminum's eventual push higher as the underlying fundamentals in the coming quarters remain broadly the same... very tight. Moreover, while aluminum could come under initial knee-jerk pressure with energy prices following a sustained re-opening of the Strait of Hormuz, we don't think it will be sustained. With supply loss still solidified for months amid slow Middle East restarts (a reopening by mid-year is indeed our base case) and risks to overall demand and the macroeconomy actually diminishe

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 Jun 2026 01:50 AM BST

Disseminated 12 Jun 2026 08:30 AM BST
"""
