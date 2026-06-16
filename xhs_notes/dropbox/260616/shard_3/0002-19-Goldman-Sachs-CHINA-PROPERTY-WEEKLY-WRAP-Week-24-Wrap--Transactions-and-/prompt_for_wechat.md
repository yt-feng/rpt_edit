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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## CHINA PROPERTY WEEKLY WRAP

# Week 24 Wrap - Transactions and sentiment broadly plateaued; more details on N-T urban renewal funding support outlined

## Key highlights for the week:

Urban renewal funding supports: Following the release of the urban renewal framework for the 15th Five-Year Plan, central ministries provided further clarifications regarding N-T funding allocations, with NDRC outlining: 1) Rmb97bn in central budgetary investment dedicated to the renovations of old urban communities and dilapidated housing, benefiting c.8mn households according to the ministry; 2) Rmb160bn in ultra-long-term treasury bonds (up Rmb25bn yoy) dedicated to underground pipeline upgrades. Meanwhile, the MOF reaffirmed its commitment to subsidy programs in key cities (15 selected for 2026, bringing cumulative beneficiaries to c.50 key cities), and to leverage multi-pronged financing tool kits including direct fiscal subsidies, local government special bonds, and tax incentives to strengthen the capital base for broader urban renewal initiatives. These details align with the framework's focused areas of acceleration, and we continue to view front-loaded implementation as key in buffering economic downside risks and supporting a recovery in housing demand.

Market performance: Transaction volumes plateaued in both primary and secondary markets (both recording flattish yoy), with the latter mirrored by sequentially stable subscription/visitations. Overall sentiment remained steady, with the new listing pace largely unchanged from the May level (MTD 14% below Jun-25 averages) resulting in flattish wow transaction prices in monitored cities, echoed by stable price expectations for home-sellers despite agent sentiment edging lower.

## Key data points:

■ New homes sales volume was +1% wow and flat yoy, while new home search activities were -0.9% wow.  
Secondary transactions were flat wow and +1% yoy, with price appreciation expectations staying stable for home-sellers while edging lower for agents.  
MTD June: Primary GFA sold on median was -17% mom and was -25% yoy; Secondary GFA sold on median was -2% mom and +14% yoy.  
YTD: Primary GFA sold on average was -13% yoy and was -11%/-43% vs. the 2024/2023 level; secondary GFA sold on average was +1% yoy and was +22%/+8%

## Yi Wang, CFA

+86(21)2401-8930

yi.wang@goldmansachs.cn

GS (China) Securities

Company Limited

## Shi Xu

+86(21)2401-8929

shi.x.xu@goldmansachs.cn

GS (China) Securities

Company Limited

## Kaiyan Jing

+86(21)2411-8092

kaiyan.jing@goldmansachs.cn

GS (China) Securities

Company Limited

vs. the 2024/2023 level.

- Inventory balance was -0.2% wow, with inventory months at 27.8 (vs. average 28.5 in May-26).  
Valuation: Our covered stronger SOE developers saw share price -1% wow on average, with CRL (1109.HK, Buy) outperforming at +2% wow; meanwhile, POE developers and other SOE developers saw share price on average +2%/flat wow, respectively. Our offshore/onshore coverage now trades at an average 27%/28% discount to end-2026E NAV and at 0.5X/0.4X 2026E P/Bs.

## Implications:

Property sales in c.75 cities suggest top-100 developers' contract sales are likely to decline 7% yoy in June, vs. -2% in May.  
■ Completions: GSPC tracker indicates high-teens % yoy decline in May (vs. -19% yoy/c.10% yoy decline in Apr by NBS/GSe) and -1% yoy in FY26E per GSe.  
New starts: New starts to record a low-twenties % yoy decline in May (vs. -27%/mid-teens % yoy decline in Apr by NBS/GSe), based on the land sales trends in 300 cities and nationwide cement shipment ratio.  
■ GTV for BEKE (new and existing) likely rose 3% yoy in Apr-MTD June (-23%/+14% for new/existing).

## Primary market Week 24: GFA +1% wow and was flat yoy, sending YTD to -13% yoy

Exhibit 1: Primary GFA sold last week was $+1\%$ wow and flat yoy in c.75 cities  
![](images/8c5950ddb12e65b814d602d944ace71296299bb52fbb902be173113459371776.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|------|
| W1   | 60   | 80   | 50   | 40   | 40   |
| W4   | 70   | 80   | 50   | 40   | 30   |
| W7   | 60   | 100  | 50   | 40   | 30   |
| W10  | 70   | 120  | 50   | 40   | 20   |
| W13  | 80   | 120  | 50   | 40   | 40   |
| W16  | 70   | 80   | 50   | 40   | 30   |
| W19  | 60   | 70   | 50   | 40   | 40   |
| W22  | 70   | 70   | 50   | 40   | 40   |
| W25  | 80   | 90   | 50   | 40   | 40   |
| W28  | 70   | 80   | 50   | 40   | 40   |
| W31  | 60   | 70   | 50   | 40   | 40   |
| W34  | 70   | 70   | 50   | 40   | 40   |
| W37  | 80   | 70   | 50   | 40   | 40   |
| W40  | 70   | 60   | 50   | 40   | 40   |
| W43  | 60   | 50   | 50   | 40   | 40   |
| W46  | 70   | 60   | 50   | 40   | 40   |
| W49  | 60   | 70   | 50   | 40   | 40   |
| W52  | 70   | 70   | 50   | 40   | 40   |
</details>

Source: CREIS, GS Global Investment Research

Exhibit 2: Primary GFA sold YTD on average was -13% yoy in c.75 cities, and -11%/-43% vs. 2024/2023 level  
![](images/c3019b121c36401aee0a82667a673cd973b40906ee57c2974707a18db14a9b00.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|------|
| W1   | 0    | 0    | 0    | 0    | 0    |
| W4   | 500  | 500  | 500  | 500  | 500  |
| W7   | 1000 | 1000 | 1000 | 1000 | 1000 |
| W10  | 1500 | 1500 | 1500 | 1500 | 1500 |
| W13  | 2000 | 2000 | 2000 | 2000 | 2000 |
| W16  | 2500 | 2500 | 2500 | 2500 | 2500 |
| W19  | 3000 | 3000 | 3000 | 3000 | 3000 |
| W22  | 3500 | 3500 | 3500 | 3500 | 3500 |
| W25  | 4000 | 4000 | 4000 | 4000 | 4000 |
| W28  | 4500 | 4500 | 4500 | 4500 | 4500 |
| W31  | 5000 | 5000 | 5000 | 5000 | 5000 |
| W34  | 5500 | 5500 | 5500 | 5500 | 5500 |
| W37  | 6000 | 6000 | 6000 | 6000 | 6000 |
| W40  | 6500 | 6500 | 6500 | 6500 | 6500 |
| W43  | 7000 | 7000 | 7000 | 7000 | 7000 |
| W46  | 7500 | 7500 | 7500 | 7500 | 7500 |
| W49  | 8000 | 8000 | 8000 | 8000 | 8000 |
| W52  | 8500 | 8500 | 8500 | 8500 | 8500 |
c.75 cities
</details>

Source: CREIS, GS Global Investment Research

Secondary market: Week 24/YTD volumes were $+1\% / +1\%$ yoy, with price appreciation expectations stable for home-sellers but edging lower for agents

Exhibit 3: Secondary GFA sold last week was flat wow and +1% yoy in c.20 cities  
Average weekly volume of secondary property sales  
![](images/431c16d4d0a5e85f7ecb5e34c93e7d695b7289620b6c294abc49cf009f2cc6a8.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|------|
| W1   | 100  | 110  | 105  | 190  | 85   |
| W4   | 140  | 130  | 120  | 150  | 155  |
| W7   | 80   | 70   | 60   | 10   | 0    |
| W10  | 100  | 110  | 105  | 130  | 80   |
| W13  | 120  | 130  | 125  | 160  | 140  |
| W16  | 140  | 150  | 145  | 180  | 160  |
| W19  | 160  | 170  | 165  | 200  | 180  |
| W22  | 180  | 190  | 185  | 195  | 175  |
| W25  | 160  | 170  | 165  | 180  | 165  |
| W28  | 140  | 150  | 145  | 160  | 155  |
| W31  | 120  | 130  | 125  | 140  | 145  |
| W36  | 100  | 110  | 105  | 120  | 135  |
| W39  | 80   | 90   | 85   | 100  | 95   |
| W42  | 60   | 70   | 65   | 80   | 75   |
| W45  | 80   | 90   | 85   | 100  | 95   |
| W48  | 100  | 110  | 105  | 120  | 115  |
| W51  | 60   | 70   | 65   | 80   | 75   |
</details>

Source: Wind, GS Global Investment Research

Exhibit 4: Secondary GFA sold YTD was $+1\%$ yoy in c.20 cities, while $+22\% / +8\%$ vs. 2024/2023  
2026 secondary volume sold vs. 2022-25  
![](images/286aa2199f99dd6d94df2cf05a37b3764eddd8e263303e73a495c67943666baf.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|------|
| W1   | 0    | 0    | 0    | 0    | 0    |
| W4   | 500  | 500  | 500  | 500  | 500  |
| W7   | 1000 | 1000 | 1000 | 1000 | 1000 |
| W10  | 1500 | 1500 | 1500 | 1500 | 1500 |
| W13  | 2000 | 2000 | 2000 | 2000 | 2000 |
| W16  | 2500 | 2500 | 2500 | 2500 | 2500 |
| W19  | 3000 | 3000 | 3000 | 3000 | 3000 |
| W22  | 3500 | 3500 | 3500 | 3500 | 3500 |
| W25  | 4000 | 4000 | 4000 | 4000 | 4000 |
| W28  | 4500 | 4500 | 4500 | 4500 | 4500 |
| W31  | 5000 | 5000 | 5000 | 5000 | 5000 |
| W34  | 5500 | 5500 | 5500 | 5500 | 5500 |
| W37  | 6000 | 6000 | 6000 | 6000 | 6000 |
| W40  | 6500 | 6500 | 6500 | 6500 | 6500 |
| W43  | 7000 | 7000 | 7000 | 7000 | 7000 |
| W46  | 7500 | 7500 | 7500 | 7500 | 7500 |
| W49  | 8000 | 8000 | 8000 | 8000 | 8000 |
| W52  | 8500 | 8500 | 8500 | 8500 | 8500 |
</details>

Source: Wind, GS Global Investment Research

Exhibit 5: Average CSI was -0.9pp wow and +6.3pp yoy  
Weekly Centraline Salesman Index (CSI) tracker in 4 cities  
![](images/35fec94c598b970479c8267582b81bd64421c4a40657f3f365a4cad9aaf9b03f.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|------|
| W1   | 49   | 52   | 48   | 47   | 45   |
| W4   | 50   | 58   | 49   | 61   | 47   |
| W7   | 54   | 65   | 50   | 55   | 50   |
| W10  | 53   | 63   | 51   | 54   | 51   |
| W13  | 52   | 60   | 50   | 53   | 52   |
| W16  | 51   | 57   | 49   | 52   | 51   |
| W19  | 50   | 55   | 48   | 51   | 50   |
| W22  | 49   | 53   | 47   | 50   | 49   |
| W25  | 48   | 51   | 46   | 49   | 48   |
| W28  | 47   | 49   | 45   | 48   | 47   |
| W31  | 46   | 47   | 44   | 47   | 46   |
| W34  | 45   | 45   | 43   | 46   | 45   |
| W37  | 44   | 43   | 42   | 45   | 44   |
| W40  | 43   | 41   | 41   | 44   | 43   |
| W43  | 42   | 39   | 40   | 43   | 42   |
| W46  | 41   | 37   | 39   | 42   | 41   |
| W49  | 40   | 35   | 38   | 41   | 40   |
| W52  | 39   | 33   | 37   | 40   | 39   |
</details>

CSI refers to agents' view on property price, $>50$ means positive views on price increases, and vice versa.

Source: Centraline

Exhibit 6: Average CAI was +0.1pp wow and -4.3pp yoy  
Weekly Centraline Seller Asking Index (CAI) tracker in 6 cities  
![](images/a87097d9fbdcc84d7cbaa26e83ed06d4c91c6edf0e28ec15c35d07df6867180d.jpg)

<details>
<summary>line chart</summary>

| Week | 2022 | 2023 | 2024 | 2025 | 2026 |
|------|------|------|------|------|------|
| W1   | 33   | 35   | 20   | 26   | 19   |
| W4   | 34   | 55   | 21   | 27   | 20   |
| W7   | 38   | 45   | 23   | 30   | 21   |
| W10  | 36   | 40   | 25   | 25   | 19   |
| W13  | 37   | 35   | 18   | 24   | 19   |
| W16  | 36   | 30   | 17   | 23   | 19   |
| W19  | 35   | 28   | 18   | 22   | 19   |
| W22  | 36   | 26   | 19   | 21   | 18   |
| W25  | 34   | 25   | 20   | 20   | 18   |
| W28  | 33   | 24   | 21   | 19   | 18   |
| W31  | 32   | 23   | 20   | 19   | 18   |
| W34  | 31   | 22   | 19   | 19   | 18   |
| W37  | 30   | 21   | 19   | 19   | 18   |
| W40  | 28   | 20   | 30   | 18   | 18   |
| W43  | 26   | 19   | 31   | 18   | 18   |
| W46  | 25   | 18   | 30   | 18   | 18   |
| W49  | 24   | 17   | 29   | 17   | 18   |
| W52  | 23   | 16   | 28   | 17   | 18   |
</details>

CAI refers to sellers' quoted price.

Source: Centraline

Inventory Week 24: Inventory -0.2% wow and -4.7% from end-25 level, with inventory months at 27.8 (vs. average 28.5 in May-26)

Exhibit 7: Inventory balance was -0.2% wow, -4.7% from end-25 levels  
c.20 cities' total inventory breakdown by city tier  
![](images/d36a0332a52e9fdda402b7faee405f06555707d867a8830961e4b62fba6fc206.jpg)

<details>
<summary>stacked area chart</summary>

(Indexed to Jan 2013)
| Date | Weekly inventory in tier-1 cities | Weekly inventory in tier-2 cities | Weekly inventory in tier-3 cities |
|---|---|---|---|
| Jun-16 | 125 | 80 | 100 |
| Dec-16 | 110 | 75 | 95 |
| Jun-17 | 100 | 70 | 90 |
| Dec-17 | 95 | 65 | 85 |
| Jun-18 | 90 | 60 | 80 |
| Dec-18 | 95 | 65 | 85 |
| Jun-19 | 100 | 70 | 90 |
| Dec-19 | 105 | 75 | 95 |
| Jun-20 | 110 | 80 | 100 |
| Dec-20 | 115 | 85 | 105 |
| Jun-21 | 120 | 90 | 110 |
| Dec-21 | 125 | 95 | 115 |
| Jun-22 | 130 | 100 | 120 |
| Dec-22 | 135 | 105 | 125 |
| Jun-23 | 140 | 110 | 130 |
| Dec-23 | 145 | 115 | 135 |
| Jun-24 | 150 | 120 | 140 |
| Dec-24 | 145 | 115 | 135 |
| Jun-25 | 140 | 110 | 130 |
| Dec-25 | 135 | 105 | 125 |
| Jun-26 | 130 | 100 | 120 |
</details>

Source: CREIS, GS Global Investment Research

Exhibit 8: Inventory month was -0.2% wow, representing -0.4% from end-25 levels  
c.20 cities' inventory months (12mth rolling) breakdown by city tier  
![](images/d352e9282ecbc7eb588d45ac0054970eb0793c13ac941dc232d11d4243cfad45.jpg)

<details>
<summary>line chart</summary>

| Date    | Inventory month in tier-1 cities | Inventory month in tier-2 cities | Inventory month in tier-3 cities |
|---------|----------------------------------|----------------------------------|----------------------------------|
| Jun-17  | 10                               | 8                                | 7                                |
| Dec-17  | 15                               | 9                                | 8                                |
| Jun-18  | 14                               | 8                                | 7                                |
| Dec-18  | 16                               | 9                                | 10                               |
| Jun-19  | 15                               | 10                               | 12                               |
| Dec-19  | 14                               | 11                               | 13                               |
| Jun-20  | 15                               | 12                               | 14                               |
| Dec-20  | 14                               | 13                               | 15                               |
| Jun-21  | 10                               | 9                                | 10                               |
| Dec-21  | 12                               | 11                               | 13                               |
| Jun-22  | 15                               | 14                               | 17                               |
| Dec-22  | 18                               | 16                               | 20                               |
| Jun-23  | 20                               | 18                               | 23                               |
| Dec-23  | 22                               | 20                               | 25                               |
| Jun-24  | 24                               | 22                               | 28                               |
| Dec-24  | 25                               | 23                               | 30                               |
| Jun-25  | 23                               | 21                               | 27                               |
| Dec-25  | 24                               | 22                               | 29                               |
| Jun-26  | 23                               | 21                               | 28                               |
</details>

Source: CREIS, GS Global Investment Research

## GSPC implies high-teens % yoy decline/-1% yoy in completions for May-26/FY26E per GSe

GS Property Completion (GSPC) tracker indicates a high-teens % yoy decline in May-26 (vs. -19% yoy/c.10% yoy decline in Apr by NBS/GSe) and -1% yoy for FY26E per GSe, based on downstream supply/demand implied from our China float glass industry outlook and proprietary weekly float glass demand model.

Exhibit 9: GSPC tracker implied monthly completions...  
GSPC tracker implied monthly GFA completion - based on GS float glass S-D model  
![](images/244d2d57e9c750145686fcfeeded43e6acac1257e893eae7f8e0125eb23c3705.jpg)

<details>
<summary>line chart</summary>

| Month | 2023 (mn sqm) | 2024 (mn sqm) | 2025 (mn sqm) | 2026 (mn sqm) |
|---|---|---|---|---|
| Jan-Feb | 80 | 80 | 70 | 70 |
| Mar | 105 | 105 | 80 | 90 |
| Apr | 115 | 105 | 105 | 80 |
| May | 110 | 95 | 85 | 70 |
| Jun | 98 | 85 | 80 | - |
| Jul | 105 | 90 | 100 | - |
| Aug | 125 | 100 | 95 | - |
| Sep | 105 | 85 | 90 | - |
| Oct | 120 | 100 | 88 | - |
| Nov | 120 | 90 | 85 | - |
| Dec | 125 | 105 | 98 | - |
</details>

Jan-Feb refers to average level in Jan and Feb.

Exhibit 10: ...suggesting completions at a high-teens % yoy decline for May-26  
% yoy change of GSPC - based on GS float glass S-D model  
![](images/01f477f0d26dfe81d1c73ad4089956ffbc946135beb73e80d4abd85dc52e81b1.jpg)

<details>
<summary>line chart</summary>

| Date | % yoy of GS property completion (GSPC) (%) yoy |
|---|---|
| Aug-20 | -30 |
| Nov-20 | -10 |
| Feb-21 | -15 |
| May-21 | 60 |
| Aug-21 | 60 |
| Nov-21 | 40 |
| Feb-22 | -30 |
| May-22 | -15 |
| Aug-22 | -20 |
| Nov-22 | -25 |
| Feb-23 | 35 |
| May-23 | 60 |
| Aug-23 | 40 |
| Nov-23 | 35 |
| Feb-24 | 0 |
| May-24 | -15 |
| Aug-24 | -20 |
| Nov-24 | -25 |
| Feb-25 | -20 |
| May-25 | -10 |
| Aug-25 | 0 |
| Nov-25 | 5 |
| Feb-26 | 0 |
| May-26 | -5 |
</details>

Source: Sublime China Information, Wind, NBS, GS Global Investment Research  
Source: Sublime China Information, Wind, NBS, GS Global Investment Research

## Valuations: P/B valuation at downturn trough

Over week 24, our covered stronger SOE developers saw share price -1% wow on average, with CRL (1109.HK, Buy) outperforming at +2% wow; meanwhile, POE developers and other SOE developers saw share price on average +2%/flat wow, respectively.  
- Our offshore coverage developers on average saw share prices +1% wow (vs. +1% for MSCI China); our onshore coverage developers averaged -2% wow (vs. +4% for CSI 300).  
Our offshore coverage now trades at an average 27% discount to end-2026E NAV and 0.5X 2026E P/B vs. 2H2008, 2H2011 and 1H2014 troughs of 39%, 0.7X; 73%, 0.9X; 58%, 0.9X.  
Our onshore coverage trades at an average $28\%$ discount to end-2026E NAV and 0.4X 2026E P/B vs. 2H2008, 2H2011 and 1H2014 troughs of $67\%$ , 1.6X; $64\%$ , 1.5X; $61\%$ , 1.2X.

Exhibit 11: Over week 24, our covered stronger SOE developers saw share price -1% wow on average, with CRL (1109.HK, Buy) outperforming at +2% wow; meanwhile, POE developers and other SOE developers saw share price on average -2%/flat wow, respectively. Our offshore coverage developers on average saw share prices +1% wow (vs. +1% for MSCI China); our onshore coverage developers averaged -2% wow (vs. +4% for CSI 300).

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Type</td><td rowspan="2">Price as of 6/15/2026</td><td colspan="3">Share price performance</td></tr><tr><td>Past week</td><td>MTD</td><td>YTD</td></tr><tr><td>Stronger SOE developers</td><td></td><td></td><td>(LCY)</td><td></

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
