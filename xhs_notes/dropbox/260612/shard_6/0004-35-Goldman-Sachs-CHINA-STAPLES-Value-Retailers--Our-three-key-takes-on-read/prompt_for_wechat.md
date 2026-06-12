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
## CHINA STAPLES

# Value Retailers: Our three key takes on read-across from new booming Fresh Snacks retail chains

We have received numerous questions on the rise of fresh snacks retailers and read-across to our F&B value retailer coverage (Busy Ming/Wanchen). First and foremost, we believe the thriving of fresh snacks retailers since 2025 suggests that snack consumption in China remains strong with new growth drivers emerging. Following the fast scaling of F&B value retailers since 2022, the rapid store rollout (200+ stores/10+ brands emerging in 2025, Exhibit 3)/strong traffic (daily sales up to Rmb100k+)/robust margin (30%+ GPM/teens% EBITDA margin, Exhibit 4/Exhibit 6) of fresh snacks retailers reinforces that consumer demand for snacks and beverages remains robust driven by new formats and category expansion. In our view, the rise of fresh snacks retailers posts an opportunity for category expansion, store-format upgrade, and assessment of competition for F&B value retailers. Our key takes:

1) Category: We think fresh snacks provide a positive read-across for F&B value retailers by introducing new levers for growth on top of F&B value retailers' traditional strength in assortment/pricing/turnover by: a) increasing reasons for frequent store visits as they are inherently more conducive to repeat, high-frequency purchases than packaged snacks; b) raising the sales ceiling per store as they serve more occasions including breakfast/late-night snacking/food pairing, and household stock-up missions. Busy Ming has mentioned the trial of baked egg tarts/hot sausage is bearing fruit on increasing per store GMV since 2H25. That said, strengthening differentiation and competitive barriers on supply chain/turnover will be the key to success given the shorter shelf life.

2) Store format diversification: We believe the next source of alpha for F&B value retailer leaders may evolve from store-opening beta to store-format-upgrade/diversification alpha with large existing network, supply chain strength/consumer data insights. Leading players are already making trials on products selection of cold-chain products, as well as trial of different store format (CVS/discounter supermarket, etc.). Our UE comparison (Exhibit 6) suggests fresh-snack retailers' high margin/attractive payback period are typically built around: a) broad but tightly curated assortment of fresh-food offerings that increases purchase frequency and impulse top-up demand, while also contains spoilage; b) high GPM on higher short-shelf-life share (c.30\~50% of SKU) and predominantly private-label mix supported by partial in-house production. c)

## Leaf Liu

+852-3966-4169 | leaf.liu@gs.com GS (Asia) L.L.C.

## Christina Liu

+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

## Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

strong operating leverage on larger-format model (200\~400 sqm) /high energy catchment locations (e.g. shopping mall B1 level) that enable high traffic/ticket size/sales per sqm (leading flagship stores reaching Rmb20\~50mn annualized GMV/Rmb40\~60 AOV vs. Rmb4\~6mn/c.Rmb30 for F&B value retailers, similar to the early-stage of Busy Ming/Wanchen when some flagship stores reached Rmb10mn+ annualized sales). In our view, Fresh-snacks stores may provide a good experiment for the next stage of store-format evolution in F&B value retail where leading chains could potentially evolve from packaged snacks value retailers toward broader community food retail platforms if executed well.

3) Competition: We do not see fresh-snack retailers as a near-term strong competition threat to F&B value retailers, as the model will likely become materially more complex and location/cost-sensitive when scaled. Specifically, fresh snacks retailers hold fewer SKUs (hundreds to 1k+) and are more labor-intensive, more exposed to rent and location quality given reliance on high sell-through, and are harder to replicate nationally due to logistics/cold-chain/self-production requirements, vs. F&B value retailers, in our view. Therefore, the store UE appears less favorable to penetrate into lower-tier markets because of the dependence on high traffic/turnover (now mostly located in tier 1-2 cities) and the difficulty on franchising given the greater complexity of spoilage control. For F&B value retailer leaders like Busy Ming and Wanchen, however, we believe short-shelf-life expansion should amplify the advantages of scale leaders given: 1) Unmatched scale/density of store network lowers procurement costs and dilutes the logistic costs; 2) Professional store-management experience/systems to control spoilage; 3) Membership assets lowers customer acquisition cost and enhances repeat-purchase. By contrast, smaller players trying to scale fresh formats across regions are much more likely to be dragged down by operational complexity and elevated loss rates.

We reiterate Buy on Busy Ming/Wanchen given attractive risk/reward considering that the stocks are trading at 17x/14x 2026E P/E vs. $22\% / 15\%$ NP CAGR in 2026-28E, respectively. Key catalysts include: 1) improving per-store GMV trends, supported by category expansion; 2) Further revising up store open targets in full-year 2026 and outer years; 3) Wanchen's update on HK dual listing schedule.

The authors would like to thank Lily Qi for her contribution to this report.

## Related Read:

China Consumer Staples: Value Retailers: Addressing key investor questions on recent competition; Reiterate Buy on Busy Ming/Wanchen

China Consumer Staples: Value Retailers: Busy Ming/Wanchen officially reiterated commitment to healthy competitive environment; Store open acceleration in May; Buy

China Consumer Staples: Value retailers initiation feedback: Key investor questions on UE/cost impact/category expansion

## OP comp table/store open trajectory/category margin

Exhibit 1: Tier-1 players mainly have 20-100 stores each and concentrated in tier1-2 cities

<table><tr><td colspan="6">Tier 1 players</td></tr><tr><td>Brand name</td><td>Founding year</td><td>store count</td><td>Avg. GMV per order</td><td>Sales area (sqm)</td><td>Regions</td></tr><tr><td>Kinglomo</td><td>2015</td><td>20+</td><td>Rmb40-60</td><td>100-400</td><td>Changsha/Wuhan/Shenzhen/Nanjing/Chanqde etc..</td></tr><tr><td>Jido Plus</td><td>2025</td><td>c.100</td><td>Rmb30-50</td><td>150-200</td><td>20 cities in China</td></tr><tr><td>Nutco</td><td>2015</td><td>100+</td><td>Rmb40-60</td><td>100-150</td><td>North China/Beijing/Tianjin/Nanjing</td></tr><tr><td>Pu Mama</td><td>2024</td><td>52+</td><td>Rmb40-60</td><td>250-300</td><td>Zhejiang/Fujian/Shaanxi/Guangdong</td></tr></table>

As of June 2026  
Source: Food Boards

Exhibit 2: Tier-2 players have lower store count and are also concentrated in tier-12 cities, mainly launched in 2025/2026

<table><tr><td colspan="4">Tier 2 players</td></tr><tr><td>Brand name</td><td>Founding year</td><td>store count</td><td>Regions</td></tr><tr><td>WoW Fresh (有点推荐)</td><td>2025</td><td>1 self-operated store</td><td>Wuhan</td></tr><tr><td>Juewei (newproject)</td><td>2025</td><td>6 self-operated trial stores</td><td>Changsha etc.</td></tr><tr><td>Xueji Chaohuo (renovated fresh stores)</td><td>2024</td><td>200 existing stores to be renovated</td><td>Tier 1-2 cities and counties</td></tr><tr><td>ChaYan YueSe (new project)</td><td>launch in 2026</td><td>1 self-operated trial store</td><td>Changsha</td></tr><tr><td>You You - Wanweizu</td><td>launch in 2026</td><td>1 self-operated trial store</td><td>Chongqing</td></tr><tr><td>Lemon Right(柠檬向右)</td><td>launch in 2026</td><td>1 self-operated trial store</td><td>Shanghai</td></tr><tr><td>Qaqaco (恰小可)</td><td>2025</td><td>c.13</td><td>Chengdu/Chongqing/Shenzhen</td></tr><tr><td>Joy Season (久食山)</td><td>2025</td><td>c.22</td><td>Shenzhen/Guangdong/Dongquan</td></tr><tr><td>Freshouse (鲜博士)</td><td>2025</td><td>c.5</td><td>Shenyang/Fuxin/Liaoning province</td></tr><tr><td>Superman snacks (超人零拾)</td><td>2025</td><td>c.6</td><td>Chongqing</td></tr><tr><td>Tata Ling (零团团)</td><td>2025</td><td>c.6</td><td>Guangzhou/Shenzhen/Foshan</td></tr><tr><td>W small sea (五小海)</td><td>2025</td><td>c.8</td><td>Xiamen/Quanzhou/Fuzhou</td></tr><tr><td>Chill HFF (轻禾丰)</td><td>2025</td><td>c.3</td><td>Ganzhou/Jiangxi province</td></tr><tr><td>Top Sold (大口兽)</td><td>2025</td><td>c.12</td><td>Changsha/Shenzhen</td></tr><tr><td>Qing Sense (清山森)</td><td>2026</td><td>1 self-operated store</td><td>Zhengzhou</td></tr></table>

As of June 2026  
Source: Food Boards

Exhibit 3: Store open trajectory of leading tier-1 players vs Busy Ming/Wanchen at early stage  
![](images/e84a55b03f3fe972c613262f9fc4abfdf3ab4834b988921698c29aef5ac510f0.jpg)

<details>
<summary>line chart</summary>

Store open trajectory
| Year | Kinglomo | Jido Plus | Nutco | Pu Mama | Busy Ming | Wanchen |
|---|---|---|---|---|---|---|
| 2024 | c.20 | c.10 | c.60-70 | c.40 | c.500 | c.500 |
| 2025 | c.20 | c.60-70 | c.60-70 | c.40 | >1,000 | 100 |
| 2026 YTD | 20+ | c.100 | 100+ | 52+ | 250 | 4,726 |
| 2023 | - | - | - | - | 6,585 | - |
The chart displays a line graph with two separate subplots: the left shows a horizontal bar chart (c.10 to c.20) and the right shows a line chart (c.500 to c.585) with a vertical line at c.585.
</details>

Wanchen Store count in 2017-2021 was mainly from Haoxianglai  
Source: Food Boards, Company data

Exhibit 4: Key SKUs are nuts/braised meats/crispy snacks/freshly-made beverages with short duration, and also at relatively affordable prices

<table><tr><td colspan="5">Key SKUs margin profile</td></tr><tr><td>Category name</td><td>ASP range (Rmb/unit)</td><td>ASP range (Rmb/g)</td><td>GPM</td><td>Duration (days)</td></tr><tr><td>Nuts/dried fruits</td><td>10-30</td><td>0.05-0.15</td><td>25%-35%</td><td>3-5</td></tr><tr><td>Braised meats</td><td>10-60</td><td>0.1-0.2</td><td>35%-50%</td><td>4-5</td></tr><tr><td>Crispy snacks</td><td>10-15</td><td>0.03-0.06</td><td>30%-40%</td><td>60-90</td></tr><tr><td>Pastries</td><td>10-40</td><td>0.06-0.1</td><td>20%-35%</td><td>1-3</td></tr><tr><td>Freshly-made Milk tea</td><td>9-12</td><td>/</td><td>30%-40%</td><td>1</td></tr><tr><td>Juice</td><td>10-15</td><td>/</td><td>30%-35%</td><td>1</td></tr></table>

Source: New Retail, Zhaibo

Exhibit 5: Leading fresh snacks players comp table

<table><tr><td colspan="3"></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="2">2025 if not stated</td><td>Kinglomo (金粉门)</td><td>Jido Plus (几多全)</td><td>Nutco (一梁)</td><td>Pu mama (鸿阳妈)</td><td>Joy Season (久食山)</td><td>WoW Fresh (有点推荐)</td></tr><tr><td rowspan="9">Operation</td><td>Store format</td><td>Fresh food &amp; snacks</td><td>Fresh food &amp; snacks</td><td>Fresh food &amp; snacks</td><td>Fresh food &amp; snacks</td><td>Fresh food &amp; snacks</td><td>Fresh food &amp; snacks</td></tr><tr><td>Business model</td><td>Self-operated</td><td>Self-operated + Franchise</td><td>Self-operated</td><td>Self-operated + Supermarket shop-in-shop</td><td>Self-operated</td><td>Self-operated</td></tr><tr><td>Founding year</td><td>2015</td><td>2025</td><td>2015</td><td>2024</td><td>2025</td><td>2025</td></tr><tr><td>Headquarter</td><td>Changsha</td><td>Changsha</td><td>Shenyang</td><td>Ningbo</td><td>Shenzhen</td><td></td></tr><tr><td>Regions</td><td>South China/East China/Hubei province</td><td>20 cities in China</td><td>Beijing/Jiangsu/North China</td><td>Jiangsu/Zhejiang/Fujian etc.</td><td>Guangzhou/Shenzhen</td><td>Wuhan</td></tr><tr><td>Key strategy</td><td>First mover in the industryShort-shelf-life products and independent product innovation</td><td>Short-shelf-life products and open-kitchen in store</td><td>Freshly-made baked goods/milk tea/slice to increase retention rate; nuts gift box for better margin mix, high turnover due to high order concentration</td><td>Freshly-made and healthy foods mainly attracting young women &amp; mothers (18-35 years-old)</td><td>Diversified and value-for-money product portfolio (Rmb9.9 products) targeting young group Location selection: at high-traffic ports of entry/super markets</td><td>Open in super markets/health and clean concepts</td></tr><tr><td># of stores</td><td>20+</td><td>60+ self-operated stores, c.100 stores in total</td><td>100+</td><td>52+</td><td>c.22</td><td>1</td></tr><tr><td>Store (count) target</td><td>Plan to expand to South/Central China tier 1-3 cities</td><td>2026: 600-1000 in tier 1-3 cities</td><td>Plan to expand to tier 1-2 cities; mid-term target 30-50 stores in Beijing</td><td>2026: 200 (50 self-operated, 150 supermarket shop-in-shop) in tier 1-3 cities</td><td>Plan to expand to tier 1 cities</td><td>800 stores nationwide</td></tr><tr><td>Average GMV per order</td><td>Rmb40-60</td><td>Rmb30-50</td><td>Rmb40-60</td><td>Rmb40-60</td><td>Rm30-40</td><td></td></tr><tr><td rowspan="4">Products</td><td># of SKUs</td><td>c.130-160</td><td>600-1000</td><td>3-10 SKUs for each category</td><td>c.340</td><td></td><td>100+</td></tr><tr><td>Product coverage</td><td>Spicy &amp; braised snacks/Baked goods/Beverage/Ice cream etc.</td><td>Nuts/Braised snacks/Baked goods/Beverage etc.</td><td>Nuts/Braised snacks/Baked goods/Beverage/Ice cream etc.</td><td>Freshly made: Baked goods/Nuts/Milk Tea/Braised snacksCustomized: Fresh-locked snacks/Frozen food/Seasonal products</td><td>Nuts/Braised snacks/Baked goods/Crispy snacks/Beverage etc.</td><td>Nuts/Braised snacks/Baked goods/Beverage/traditional pastries/dried fruits</td></tr><tr><td>Pricing range</td><td>Rmb5-50</td><td>Rmb10-100</td><td>Rmb9 9-220</td><td></td><td>Rmb9 9 - 40</td><td></td></tr><tr><td>Private label %</td><td>99%</td><td></td><td></td><td>100%</td><td></td><td>100%</td></tr><tr><td rowspan="5">Store</td><td>Area/store (sqm)</td><td>100-400</td><td>150-200</td><td>100-150</td><td>250-300</td><td>70-80</td><td>300</td></tr><tr><td>Monthly GMV per store (Rmb mn)</td><td>Rmb4mn for benchmark stores</td><td></td><td>Rmb million level in general</td><td>Core 8 products contributing to 15% of total store GMV</td><td></td><td>c.Rmb4-4.5mn</td></tr><tr><td>GPM</td><td>35%-40%</td><td></td><td></td><td>30-35%</td><td></td><td></td></tr><tr><td>Logistics</td><td>New factories in Changzhou and Shenzhen were put into production in May</td><td>New factories put into production in Nanjing, 20 production sites nationwide in plan</td><td>Self-built supply chain: pollution-free planting base + self-owned processing factories + temperature-zoned warehouses spanning nearly 5k sqm</td><td>Self-built braised snacks/bakery/nuts factories</td><td></td><td>100k sqm central kitchen for beverages and braised food/600sqm warehouse with stores, 10+ bakery SKUs share the same production line with Sam&#x27;s Club</td></tr><tr><td>Sourcing strategy</td><td>Direct-sourcing + central kitchen + full-chain supply chain</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Food Boards and other sources, Data compiled by GS Gloabl Invetsment Research

## Store UE: Fresh Snack Retailers - still in early stage of growth curve with small store numbers

Exhibit 6: Illustrative Store UE comparison (2025, annualized)

<table><tr><td>Snack discounter store UE (annualized)</td><td colspan="2">Fresh Snacks Retailers</td><td colspan="2">F&amp;B Value Retailers</td></tr><tr><td>K Rmb</td><td>Kinglomo Flagship (avg.)</td><td>Kinglomo Flagship (top)</td><td>Busy Ming</td><td>Wanchen</td></tr><tr><td>Initial Investment</td><td>2,500</td><td>3,500</td><td>550</td><td>463</td></tr><tr><td>Deposit</td><td></td><td></td><td>30</td><td>20</td></tr><tr><td>Furnishment</td><td>500</td><td>600</td><td>130</td><td>125</td></tr><tr><td>Equipment</td><td>1,000</td><td>1,500</td><td>160</td><td>138</td></tr><tr><td>First stock</td><td>1,000</td><td>1,400</td><td>230</td><td>180</td></tr><tr><td>Training and others</td><td></td><td></td><td></td><td></td></tr><tr><td>CAPEX (excl. first stock and deposit)</td><td>1,500</td><td>2,100</td><td>290</td><td>263</td></tr><tr><td>Subsidies</td><td></td><td></td><td>36</td><td>70</td></tr><tr><td>CAPEX per sqm</td><td>5</td><td>5</td><td>2</td><td>2</td></tr><tr><td>CAPEX with first stock</td><td>2,500</td><td>3,500</td><td>520</td><td>443</td></tr><tr><td>GMV</td><td>24,000</td><td>48,000</td><td>5,397</td><td>4,691</td></tr><tr><td>Assumed avg. store size (sqm)</td><td>300</td><td>400</td><td>150</td><td>140</td></tr><tr><td>Sales per sqm</td><td>80</td><td>120</td><td>36</td><td>34</td></tr><tr><td>Daily sales</td><td>65.8</td><td>131.5</td><td>14.8</td><td>12.9</td></tr><tr><td>Ticket size (Rmb)</td><td>50</td><td>50</td><td>31</td><td>31</td></tr><tr><td>Daily order #</td><td>1,315</td><td>2,630</td><td>479</td><td>419</td></tr><tr><td>Sales</td><td>21,239</td><td>42,478</td><td>4,776</td><td>4,152</td></tr><tr><td>VAT rate</td><td>13%</td><td>13%</td><td>13%</td><td>13%</td></tr><tr><td>Cost of good sold</td><td>14,867</td><td>29,735</td><td>3,821</td><td>3,321</td></tr><tr><td>% of sales</td><td>70%</td><td>70%</td><td>80%</td><td>80%</td></tr><tr><td>Gross profits</td><td>6,372</td><td>12,743</td><td>955</td><td>830</td></tr><tr><td>Gross Margin ex. Spoilage</td><td>30%</td><td>30%</td><td>20%</td><td>20%</td></tr><tr><td>Gross Margin</td><td>35%</td><td>35%</td><td></td><td></td></tr><tr><td>Staff costs</td><td>1,800</td><td>2,400</td><td>240</td><td>216</td></tr><tr><td>% of sales</td><td>8.5%</td><td>5.7%</td><td>5.0%</td><td>5.2%</td></tr><tr><td># of staff</td><td>30</td><td>40</td><td>4</td><td>4</td></tr><tr><td>Monthly salary</td><td>5.0</td><td>5.0</td><td>5.0</td><td>4.5</td></tr><tr><td>Rental costs</td><td>960</td><td>2,400</td><td>192</td><td>168</td></tr><tr><td>% of sales</td><td>4.5%</td><td>5.7%</td><td>4.0%</td><td>4.0%</td></tr><tr><td>Monthly rental fee</td><td>80.0</td><td>200.0</td><td>16.0</td><td>14.0</td></tr><tr><td>Utility expenses</td><td>288.0</td><td>384.0</td><td>72.0</td><td>67.2</td></tr><tr><td>% of sales</td><td>1.4%</td><td>0.9%</td><td>1.5%</td><td>1.6%</td></tr><tr><td>D&amp;A expense</td><td>300</td><td>420</td><td>58</td><td>53</td></tr><tr><td>% of sales</td><td>1.3%</td><td>0.9%</td><td>1.1%</td><td>1.1%</td></tr><tr><td>Years of depreciation</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>Total capex</td><td>1,500</td><td>2,100</td><td>290</td><td>263</td></tr><tr><td>Other expenses (Logistics, markting, etc.)</td><td>637</td><td>1,062</td><td>40</td><td>38</td></tr><tr><td>% of sales</td><td>3.0%</td><td>2.5%</td><td>0.7%</td><td>0.8%</td></tr><tr><td>Store level operating profit</td><td>2,387</td><td>6,077</td><td>353</td><td>289</td></tr><tr><td>Store level OPM</td><td>11.2%</td><td>14

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
