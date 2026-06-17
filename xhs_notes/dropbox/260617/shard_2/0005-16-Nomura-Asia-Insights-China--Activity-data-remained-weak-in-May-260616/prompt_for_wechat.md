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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Economics - Asia ex-Japan

## China: Activity data remained weak in May

China's NBS just released May activity data, with another month of deteriorating domestic demand and a soft rebound in industrial production (IP). Retail sales growth turned negative for the first time since the abrupt Covid reopening in late 2022, worsening to -0.6% y-o-y in May from 0.2% in April, which is below the market consensus of -0.2% but close to our forecast of -1.0%. Fixed asset investment (FAI) growth plunged to -10.7% y-o-y in May from -8.0% in April, far worse than market expectations (Consensus: -4.2%; NOM: -4.9%). IP growth rebounded marginally to 4.5% y-o-y in May from 4.1% in April, largely in line with market expectations (Consensus: 4.4%; NOM: 4.1%) but well below the readings of 6.1% in Q1 2026 and 5.9% in 2025.

The worsening of domestic demand increases our conviction in our view that both markets and policymakers should not simply assume an AI boom and a rise in stock indices will cure China's property bust-driven economic woes. The sustained weakness in IP growth reflects a limited boost from the price-driven export boom and lingering supply disruptions across energy raw materials. Despite the US-Iran deal, the shipment of energy supplies from Persian Gulf nations may take time to fully resume. The weak data in April-May lend support to our view that the growth rebound in Q1 was short-lived and Beijing should maintain a heightened level of fiscal spending to address exceptionally weak domestic demand. We maintain our below-consensus Q2 GDP growth forecast at 4.1% (Consensus: 4.7%). The weak economy should also prevent Beijing from allowing RMB to appreciate too quickly. Indeed, Bloomberg recently reported that banks have been allowed to offer higher interest rates on corporate USD deposits to slow FX conversions.

## A soft rebound in industrial production growth

Headline IP growth increased to 4.5% y-o-y in May from 4.1% in April, largely in line with market expectations (Consensus: 4.4%; NOM: 4.1%). Average IP growth in April-May was 4.3% y-o-y, well below the readings of 6.1% in Q1 2026 and 5.9% in 2025, partly due to disruptions in energy supplies from the Middle East and the limited drawdown of oil reserves. In sequential, seasonally adjusted terms, month-over-month IP growth increased to 0.40% in May from 0.05% in April (May 2025: 0.41%).

By major sector, output growth of the manufacturing and utilities sectors increased to 4.4% y-o-y and 7.6%, respectively, in May from 4.0% and 5.3% in April, while output growth of the mining sector slowed to 2.3% y-o-y in May from 3.8% in April. In line with higher growth in the utilities sector, growth of electricity production rose to 4.2% y-o-y in May from 2.6% in April. In line with lower growth in mining sector, raw coal output growth fell to -1.7% y-o-y in May from -1.0% y-o-y in April.

On major construction raw materials, output growth of crude steel and cement remained negative in May, at -2.7% y-o-y and -8.1%, respectively, little changed from -2.8% and -10.8% in April.

On electronic products, output volume growth of PCs and smartphones fell sharply to -19.4% y-o-y and -8.8%, respectively, in May from -9.3% and 4.7% in April, despite rising chip prices. In volume terms, export growth of smartphones remained negative in May, albeit rising to -3.5% y-o-y from -5.2% in April.

Due to AI-driven demand, output growth of integrated circuits (IC) increased to 22.9% y-o-y in May from 22.1% in April. The solid output growth appears inconsistent with weaker exports, as IC export growth fell further to 2.1% y-o-y in May from 3.6% in April, in volume terms.

Amid the anti-involution campaign to constrain supply, output growth of solar panels

## Research Analysts

Asia Economics

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Harrington Zhang - NIHK

harrington.zhang@NOM.com

+852 2252 2057

Hannah Liu - NIHK

hannah.liu@NOM.com

+852 2252 1082

remained deeply negative at -20.4% y-o-y in May, improving little from -25.6% in April.

Auto output growth fell to -3.2% y-o-y in May from -2.6% in April, while according to CPCA, volume growth of passenger car output fell to -3.1% y-o-y in May from -1.8% in April. As domestic markets still contribute about 70% of overall auto sales, the deep contraction in domestic auto sales will likely continue to weigh on auto output, despite the export strength.

Due to the price effect, growth of export-delivered value remained elevated at 10.1% y-o-y in May, little changed from 10.6% in April.

## The impact of the oil-linked supply shock extended into May

With oil import volume slumping to 7.8mbpd in May, the lowest in nine years and 30% below pre-war levels, we see continued disruptions to industrial production activity, especially in oil- and chemical-related sectors.

- Output growth of crude oil processing volume dropped further to -9.1% y-o-y in May from -5.8% in April and -2.2% in March.  
- Due to the acute shortage of sulfur, a by-product of petroleum refining and natural gas purification (desulfurization), output growth of sulfuric acid, hailed as the “mother of the chemical industry”, remained negative in May, albeit rising to -1.6% y-o-y from -2.2% in April (March: 6.2%).  
- Due to the shortage of oil-linked raw materials, output growth of ethylene fell further to 2.1% y-o-y in May from 4.1% in April and 6.8% in March.  
- Output growth of chemical fiber remained negative in May, despite rising to -3.3% y-o-y in May from -3.9% in April (March: 2.2%).  
- At the sectoral level, output growth of raw chemical materials and chemical products dropped further to 0.3% y-o-y in May from 5.3% in April and 9.0% in March. IP growth in extraction of petroleum and natural gas dropped further to 1.5% y-o-y in May from 4.6% in April and 9.4% in March.

## FAI growth plunged further into negative territory in May

FAI growth fell sharply further into negative territory to -10.7% y-o-y in May from -8.0% in April, marking two consecutive months of contraction and the deepest single-month decline so far this year. The result significantly undershot both market expectations and our own more pessimistic forecast (Consensus: -4.2%; NOM: -4.9%). By sector, the plunge was broad-based, with contractions recorded in manufacturing FAI, infrastructure FAI and property FAI. The property sector slumped further and remained in deeply negative territory, remaining the primary drag.

Manufacturing investment growth was essentially flat at -4.2% y-o-y in May (April: -4.3%), which suggests the sector may have stabilised at a moderately contractionary level rather than recovering. The April Politburo meeting pointedly placed renewed focus on the ongoing "anti-involution" campaign, which has intensified significantly since July 2025 and likely continued to weigh on manufacturing FAI in May. Notably, the persistent weakness occurred despite highly robust export growth in the same month, reinforcing our view that policy-driven capacity constraints may be overriding external demand signals.

Based on our calculations, FAI growth in the motor vehicle sector – now predominantly EVs – improved slightly to -7.9% y-o-y in May from -10.4% in April, though it remained firmly in contraction. FAI growth in the electrical machinery and equipment sector, which includes both lithium-ion batteries and solar modules, fell back into negative territory, dropping to -2.3% y-o-y in May from 7.6% in April and exhibiting the sectoral reach of the anti-involution drive.

On the other hand, FAI growth in the railways, ships, aerospace and other transport equipment category – which has been one of the most notable drivers of manufacturing growth over the past two years – rebounded to 21.4% y-o-y in May from 17.8% in April. We recently highlighted the V-shaped rebound of China's shipbuilding orders in global markets, which should backstop China's ship production in coming years (Shipbuilding one year on: China's lead endures as Washington turns to allies, 8 June 2026).

Infrastructure investment growth plunged to -10.8% y-o-y in May from -3.7% in April, a sharp deterioration that appears difficult to reconcile with available policy signals and funding conditions. First, China is in the midst of a major nationwide push for data centre construction amid the ongoing AI super-cycle and intensifying US-China AI competition, which should in principle be supporting infrastructure outlays. Second, the issuance in May of special LGBs – a key funding source for infrastructure – was broadly on par with the same period last year, which suggests funding availability per se is not the binding constraint. The most plausible explanation, in our view, is sluggish fiscal deposit drawdown; that is, bond proceeds are being raised but not deployed in a timely manner. This may point to the slowness of project approval at the central government level or execution bottlenecks at the local government level rather than a shortage of financing, and suggests infrastructure FAI weakness may persist until disbursement mechanisms improve.

By ownership type, FAI growth across state-controlled entities slumped to -8.9% y-o-y in May from -6.3% in April, while private enterprise FAI growth deteriorated further to -11.8% from -11.2%. The breadth of the weakness across both ownership categories underscores the severity of the May slowdown and suggests that neither fiscal-led nor market-driven investment is providing a meaningful offset at present.

## Details of the retail sales data

Retail sales growth fell short of expectations (Consensus: -0.2%; NOM: -1.0%) by turning negative to -0.6% y-o-y in May from 0.2% in April. Using May CPI inflation of 1.2% y-o-y as a proxy deflator, real retail sales growth became more negative, falling to -1.8% y-o-y in May from -1.0% in April. The drop in retail sales growth was broad-based across categories, reflecting weak consumer sentiment, payback effects from the scaled-back trade-in program and negative price effects on petroleum and consumer electronic products, as households curtailed purchases amid surging energy and chip prices.

Auto sales growth in value terms worsened to -16.1% y-o-y in May from -15.3% in April. The deterioration in value terms was consistent with the volume growth reported by the China Passenger Car Association (CPCA). According to the CPCA, passenger car sales growth in volume terms worsened to -22.1% y-o-y in May from -20.0% in April. We also observed renewed price cuts among automakers and dealers amid mounting domestic demand pressures, following some temporary price improvements in early 2026.

Merchandise sales growth excluding autos improved to 3.3% y-o-y in May from -0.7% in April, driven by price effects from rising retail prices of petroleum and consumer electronic products amid the surge in oil and chip prices. In real terms, growth in merchandise sales excluding autos likely worsened, due to the payback effects from the trade-in program.

- Retail sales growth in home appliances, furniture and sports & entertainment remained deeply subdued at -15.6% y-o-y, -8.7% and 8.0%, respectively, in May from -15.1%, -10.4% and -8.0% in April, weighed down by payback effects from the scaled back trade-in program.  
- Retail sales growth in petroleum products improved to -3.2% y-o-y in May from -6.5% April on higher retail petroleum prices. According to our estimates, growth in domestic retail petroleum prices increased to 25.6% y-o-y in May from 20.8% in April. Petroleum consumption in real terms has likely plunged by around 30% from May last year.  
- Retail sales growth in communication appliances plunged to 0.7% y-o-y in May from 6.2% in April, driven by both payback effects from the trade-in program and negative price effects as consumers reduced purchases when surging chip prices passed through to final selling prices. Meanwhile, growth in office appliances sales improved to -1.5% y-o-y in May from -6.9% in April, as rising prices more than offset volume effects.

Catering services growth drifted lower to 0.6% y-o-y in May from 2.2% in April, suggesting weak consumer sentiment amid the perennial property crisis. Growth in sales by designated restaurants with annual revenue above RMB2mn turned negative at -1.7% y-o-y in May, down from 0.9% in April. This likely reflects both lingering effects from the anti-involution campaign imposed last year, and weak household purchasing power and consumer sentiment despite the decent stock market performance amid the AI boom.

## The property contraction deepened further in May

Property investment growth worsened to -24.3% y-o-y in May from -20.1% in April, below the market consensus forecast of -15.0% but close to our more cautious forecast of -20.0%. New home sales growth fell to -13.1% y-o-y by floor space and to -9.5% by value in May from -9.5% and -7.7%l, respectively, in April. For other major property indicators, growth of new home starts, new home completions and funds for property investment reached -24.6% y-o-y, -19.9% and -21.5%, respectively, in May, compared with -26.6%, -18.8% and -21.8% in April.

## Home price declines widened again in May, despite resilience in top-tier cities

Average new home prices declined by 0.20% m-o-m in May, widening from a 0.19% decrease in April. Existing home prices, which might better reflect the trend of home prices in China, declined by 0.26% m-o-m in May, worsening again after the price decline narrowed over four straight months to the 0.23% decrease in April. Among the NBS sample of 70 cities, 10 cities recorded month-on-month increases in existing home prices in May, down from 12 in April and 13 in March.

By city tier, the change in average existing home prices in tier-1 cities edged down to 0.35% m-o-m in May from 0.40% in April. Positive gains were reported again across all tier-1 cities in May: 0.1% m-o-m in Beijing (April: 0.4%), 0.6% in Shanghai (0.7%), 0.6% in Guangzhou (0.1%) and 0.6% in Shenzhen (0.3%). Home price declines in tier-2 cities widened to -0.19% m-o-m in May from -0.10% in April, while the decline in tier-3/4 cities remained the deepest and unchanged at -0.35%.

The May home price data are largely in line with the Iceberg index, a leading indicator based on the lowest listing housing prices, which recorded a 0.3% m-o-m decline in May, following a 0.4% decrease in April. As the fruits of AI-driven growth are mainly reaped by a few selected “smart” cities, especially the four top-tier ones, a real property market recovery may only take place in those cities. This is especially the case, as most cities have lifted restrictions on home sales and purchases since late 2022, making a full-blown recovery of the national property market even more far-fetched. The dire situation in most part of China, mainly small cities, is likely to persist, due to sustained population flows and deeply pessimistic expectations. Indeed, the Iceberg index weekly data indicated a decline of 0.4% m-o-m in the first two weeks of June, worsening from a 0.3% decline in May and a 0.4% decline in April.

Fig. 1: China's major economic indicators

<table><tr><td>Indicators</td><td>Unit</td><td>May 26</td><td>Apr 26</td><td>Q1 26</td><td>Q4 25</td><td>2025</td><td>2024</td></tr><tr><td colspan="8">Economic survey</td></tr><tr><td>Official mfg PMI</td><td>Index</td><td>50.0</td><td>50.3</td><td>49.6</td><td>49.4</td><td>49.6</td><td>49.8</td></tr><tr><td>Official non-mfg PMI</td><td>Index</td><td>50.1</td><td>49.4</td><td>49.7</td><td>49.9</td><td>50.2</td><td>50.9</td></tr><tr><td>RatingDog mfg PMI</td><td>Index</td><td>51.8</td><td>52.2</td><td>51.1</td><td>50.2</td><td>50.3</td><td>50.8</td></tr><tr><td colspan="8">Activity</td></tr><tr><td>Industrial production (IP)</td><td>% y-o-y</td><td>4.5</td><td>4.1</td><td>6.1</td><td>5.0</td><td>5.9</td><td>5.8</td></tr><tr><td>Crude steel output (volume)</td><td>% y-o-y</td><td>-2.7</td><td>-2.8</td><td>-4.6</td><td>-11.1</td><td>-4.4</td><td>-1.7</td></tr><tr><td>Steel product output (volume)</td><td>% y-o-y</td><td>-2.8</td><td>-1.7</td><td>-1.7</td><td>-2.4</td><td>3.1</td><td>1.1</td></tr><tr><td>Electricity production (volume)</td><td>% y-o-y</td><td>4.2</td><td>2.6</td><td>3.4</td><td>3.6</td><td>2.2</td><td>4.6</td></tr><tr><td>Non-ferrous metal output (volume)</td><td>% y-o-y</td><td>2.2</td><td>2.8</td><td>3.6</td><td>4.2</td><td>3.9</td><td>4.3</td></tr><tr><td>Cement output (volume)</td><td>% y-o-y</td><td>-8.1</td><td>-10.8</td><td>-7.1</td><td>-10.2</td><td>-6.9</td><td>-9.5</td></tr><tr><td>Auto output (volume)</td><td>% y-o-y</td><td>-3.2</td><td>-2.6</td><td>-5.7</td><td>3.6</td><td>9.8</td><td>4.8</td></tr><tr><td>Retail sales</td><td>% y-o-y</td><td>-0.6</td><td>0.2</td><td>2.4</td><td>1.7</td><td>3.7</td><td>3.5</td></tr><tr><td>Merchandise excl. auto &amp; catering</td><td>% y-o-y</td><td>3.3</td><td>-0.7</td><td>3.4</td><td>4.2</td><td>4.9</td><td>3.8</td></tr><tr><td>Auto</td><td>% y-o-y</td><td>-16.1</td><td>-15.3</td><td>-9.1</td><td>-6.6</td><td>-1.5</td><td>-0.5</td></tr><tr><td>Catering</td><td>% y-o-y</td><td>0.6</td><td>2.2</td><td>4.2</td><td>3.1</td><td>3.2</td><td>5.3</td></tr><tr><td>Delivered value for exports (RMB)</td><td>% y-o-y</td><td>10.1</td><td>10.6</td><td>7.1</td><td>0.3</td><td>2.2</td><td>5.1</td></tr><tr><td>Fixed asset investment (FAI) ytd</td><td>% y-o-y</td><td>-4.1</td><td>-1.6</td><td>1.7</td><td>-3.8</td><td>-3.8</td><td>3.2</td></tr><tr><td>FAI</td><td>% y-o-y</td><td>-10.7</td><td>-8.0</td><td>1.7</td><td>-12.8</td><td>-3.8</td><td>3.2</td></tr><tr><td>Infrastructure investment</td><td>% y-o-y</td><td>-10.8</td><td>-3.7</td><td>9.2</td><td>-13.4</td><td>-1.5</td><td>9.2</td></tr><tr><td>Manufacturing investment</td><td>% y-o-y</td><td>-4.2</td><td>-4.3</td><td>4.1</td><td>-7.3</td><td>0.6</td><td>9.2</td></tr><tr><td colspan="8">Inflation</td></tr><tr><td>CPI</td><td>% y-o-y</td><td>1.2</td><td>1.2</td><td>0.9</td><td>0.6</td><td>0.0</td><td>0.2</td></tr><tr><td>Food price</td><td>% y-o-y</td><td>-1.7</td><td>-1.6</td><td>0.4</td><td>-0.5</td><td>-1.5</td><td>-0.6</td></tr><tr><td>Non-food price</td><td>% y-o-y</td><td>1.9</td><td>1.8</td><td>0.9</td><td>0.8</td><td>0.4</td><td>0.4</td></tr><tr><td>PPI</td><td>% y-o-y</td><td>3.9</td><td>2.8</td><td>-0.6</td><td>-2.1</td><td>-2.6</td><td>-2.2</td></tr><tr><td colspan="8">Trade</td></tr><tr><td>Exports (USD)</td><td>% y-o-y</td><td>19.4</td><td>14.1</td><td>14.7</td><td>3.8</td><td>5.5</td><td>5.8</td></tr><tr><td>Imports (USD)</td><td>% y-o-y</td><td>27.4</td><td>25.3</td><td>23.0</td><td>3.4</td><td

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
