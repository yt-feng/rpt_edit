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

## US-Iran deal: A welcome relief for Asia

AI-boom and energy cost relief should position Asia for better performance. Thailand, Philippines, India, Korea stand to gain the most from lower oil prices.

- Positive for Asia: The US-Iran peace deal is positive for Asia's net energy importing economies through lower inflation (0.2-0.3pp for every 10% oil drop), improved current accounts (\~0.3% of GDP) and modest growth/fiscal benefits. Combined with strong AI-demand, this should position Asia for better performance. However, the macro benefits will likely be visible with a lag, as supply chain normalization will likely be gradual.  
- Key winners: Thailand, Philippines, India and South Korea stand to gain the most – Thailand via a lower import bill and inflation; Philippines through faster decline in inflation; India from reduced import costs and South Korea via a wider CA surplus.  
- Differentiation within Asia is still critical: While broadly positive, we remain cautious on Indonesia owing to policy uncertainty, while India might enjoy a ‘double bonanza’ from lower oil prices and the recent FCNR(B) measure, which should further boost the BOP surplus in Q3.  
- Central bank divergence persists: Lower oil prices will reduce hawkish pressure marginally, but policy paths remain highly divergent. We expect policy rates to be on hold for BI, RBI, RBA, BOT and PBoC; a delayed hike for Taiwan's CBC (December and March, versus June and December earlier) and continued hikes/policy tightening elsewhere (BSP, BNM, MAS, BOK and RBNZ).  
- FX strategy: We made a few changes to emphasize our stance of being selectively short USD and with a focus on RV trades driven by local factors. We initiate short USD/KRW with a conviction level of 1/5, reinitiate long EUR/INR (raise to 3/5 from 2), and lower the conviction level on our long SGD/IDR to 3/5 (from 4). We also maintain our short USD/CNH (4/5) and short USD/TWD (3/5).  
- In Asia rates, we focus on relative value after the latest rally. We maintain a receive position in Korea (2yfwd5y) at a conviction level of 3/5 (reduced from 4/5 earlier today). In India, we recommend a Sep-2s5s NDOIS flattener.

## The US-Iran peace deal: A turning point for Asia?

Following more than three months of conflict in the Middle East and the blockade of the Strait of Hormuz, the US and Iran have finally agreed upon an interim peace deal, which is expected to be formalized on 19 June in Switzerland. Brent crude oil prices have fallen sharply in response; they are currently less than USD83/bbl and 25% below month-ago levels. These prices are well below our baseline assumptions. We currently assume Brent crude will average USD93.9/bbl in 2026, but if oil prices settle closer to USD80/bbl, the full-year average would fall to USD85.4/bbl and oil prices in H2 2026 would be \~15% below our current assumptions.

Moreover, the benefits from reopening the Strait of Hormuz extends beyond oil. Other commodity prices – natural gas, urea – are also repricing lower (Figure 1). The peace deal is still fragile, but if it proves durable and commodity prices stay benign, this would positively impact Asia’s economic outlook, as the region is a large net energy importer and has been the most adversely impacted from the Middle East energy shock.

## How the Hormuz closure has impacted Asia so far

The closure of the Strait of Hormuz has proven less damaging to Asia's growth than initially feared, thanks to a strong AI-driven growth boost and sufficient availability of oil supplies (inventory drawdown and sourcing from alternate routes). However, the Iran war'

## Research Analysts

## Asia Economics

Sonal Varma - NSL

sonal.varma@NOM.com

Ting Lu - NIHK

ting.lu@NOM.com

Euben Paracuelles - NSL

euben.paracuelles@NOM.com

Aurodeep Nandi - NFASL

aurodeep.nandi@NOM.com

Jeong Woo Park - NSL

jeongwoo.park@NOM.com

Si Ying Toh, CFA - NSL

siying.toh@NOM.com

Jing Wang - NIHK

jing.wang@NOM.com

Harrington Zhang - NIHK

harrington.zhang@NOM.com

Nabila Amani - NSL

nabila.amani@NOM.com

Yiru Chen - NSL

yiru.chen1@NOM.com

Lattakit Lapudomkarn - NSL

lattakit.lapudomkarn@NOM.com

Hannah Liu - NIHK

hannah.liu@NOM.com

## Australia Economics

Andrew Ticehurst - NAL

andrew.ticehurst@NOM.com

## Asia FX Strategy

Craig Chan - NSL

craig.chan@NOM.com

Wee Choon Teo - NSL

weechoon.teo@NOM.com

Vicky Chen - NSL

vicky.chen1@NOM.com

Manthan Shingala - NSL

manthan.shingala1@NOM.com

## Asia Rates Strategy

Albert Leung - NIHK

albert.leung1@NOM.com

Nathan Sribalasundaram - NSL

nathan.sribalasundaram@NOM.com

Clair Gao, CFA - NIHK

clair.gao@NOM.com

s true toll has manifested through higher inflation, currency depreciation and fiscal strain on many economies. Central banks accordingly pivoted in a hawkish direction.

Fig. 1: Commodity prices since the start of 2026  
![](images/d26b1c4bc3cde3b1f8955d6802293bf3896eabf1c94308efafafbf18b3037f44.jpg)  
Note: We use daily prices for all commodities (latest: 15 June) except for Middle East urea (weekly prices; latest: 12 June). Source: Bloomberg and NOM Global Economics.

## Supply-chain normalization: A gradual process

Even with the peace deal announced, the unwinding of supply-chain disruptions caused by the Strait of Hormuz closure is likely to be a more gradual process. The deal itself remains fragile, due to deep mutual distrust. There are logistical challenges (clearing the mines, clearing the stranded ships), insurance costs remain high and shipping confidence will only return gradually as vessels test the waters. Oil wells shuttered must be restarted, and as oil flows resume, a surge in restocking demand is inevitable. The entire energy supply chain – oil and refined products (jet fuel, diesel, gasoline), petrochemicals (polymers, plastics, naphtha), fertilizers, industrial metals and minerals (aluminum, sulphur, helium) all face a multi-month normalisation timeline.

## A positive economic impact on Asia

Nevertheless, the US-Iran peace deal offers a welcome reprieve for Asia, with the potential for stronger growth, lower inflation and reduced twin current account and fiscal pressures (Figure 2).

## Lower imports

A lower import bill is likely to be the most immediate impact. On average, every 10% fall in the price of oil improves Asia's current account (CA) balance by \~0.3% of GDP. The top three economies that would experience the most visible improvement include Thailand (every 10% oil price fall improves its CA by 0.5pp), India (0.4pp) and South Korea (0.3pp).

## Easing inflation, but gradually

The easing of inflationary pressures will likely be more gradual, given the role of fiscal policy in capping the upside in energy prices, manufacturing margins still under pressure and lags in supply chain normalisation. Every 10% decline in oil prices, on average, lowers Asia's CPI inflation by 0.2-0.3pp, but as pipeline price pressures continued to rise in May, CPI inflation benefits will likely take 2-3 months to materialise. We expect the impact of lower oil prices to be most visible in the Philippines, which has market-determined fuel prices. Lower oil and fertilizer prices can also help keep the lid on food inflation, although with 2026 an El Niño year, medium-term risks to food inflation remain.

## Growth and fiscal benefits

We also expect some benefits to growth and fiscal relief for governments, but this impact should be more marginal in comparison with the current account and inflation benefits. On fiscal balances, we maintain our forecasts for slightly wider deficits in India (to 4.6% of GDP in FY27 versus the 4.3% budget target) and Indonesia (to 3% of GDP in 2026, with increased below-the-line spending).

Fig. 2: Impact of fall in oil prices on Asian economies

<table><tr><td></td><td colspan="4">Impact of every 10% fall in oil prices</td><td colspan="4">NOM&#x27;s 2026 baseline projections (Assuming Brent crude oil price of US$93.9/bbl in 2026)</td></tr><tr><td></td><td>GDP growth (pp)</td><td>CPI inflation* (pp)</td><td>Current account (% of GDP)</td><td>Fiscal balance (% of GDP)</td><td>Real GDP (% y-o-y)</td><td>CPI inflation* (% y-o-y)</td><td>Current account (% of GDP)</td><td>Fiscal balance (% of GDP)</td></tr><tr><td>China</td><td>0.00</td><td>-0.10</td><td>0.20</td><td>0.01</td><td>4.5</td><td>0.9</td><td>3.4</td><td>-5.4</td></tr><tr><td>Hong Kong</td><td>0.00</td><td>-0.07</td><td>0.07</td><td>0.01</td><td>4.8</td><td>1.9</td><td>7.5</td><td>-1.2</td></tr><tr><td>India</td><td>0.15</td><td>-0.50</td><td>0.40</td><td>0.05</td><td>6.9</td><td>4.2</td><td>-1.9</td><td>-4.4</td></tr><tr><td>Indonesia</td><td>-0.05</td><td>-0.10</td><td>0.20</td><td>0.20</td><td>5.2</td><td>3.1</td><td>-2.0</td><td>-3.0</td></tr><tr><td>Malaysia</td><td>-0.04</td><td>-0.22</td><td>-0.02</td><td>0.00</td><td>5.2</td><td>2.3</td><td>2.0</td><td>-3.5</td></tr><tr><td>Philippines</td><td>0.07</td><td>-0.50</td><td>0.37</td><td>0.00</td><td>4.6</td><td>5.5</td><td>-4.8</td><td>-5.1</td></tr><tr><td>Singapore</td><td>-0.01</td><td>-0.14</td><td>-0.03</td><td>0.00</td><td>4.6</td><td>2.2</td><td>16.9</td><td>0.5</td></tr><tr><td>South Korea</td><td>0.05</td><td>-0.30</td><td>0.30</td><td>0.10</td><td>2.4</td><td>2.7</td><td>15.5</td><td>-2.0</td></tr><tr><td>Taiwan</td><td>0.03</td><td>-0.10</td><td>0.20</td><td>0.20</td><td>9.9</td><td>2.0</td><td>21.3</td><td>-1.4</td></tr><tr><td>Thailand</td><td>0.08</td><td>-0.30</td><td>0.50</td><td>0.20</td><td>1.8</td><td>1.5</td><td>1.4</td><td>-5.8</td></tr></table>

Note: \*For Singapore, we calculate the impact on MAS core inflation.  
Source: Bloomberg and NOM Global Economics.

## Winners from lower oil prices

Most Asian economies will benefit from lower energy prices, but we expect Thailand, the Philippines, India and South Korea to gain the most (Figures 3 and 4).

As Asia's largest net oil importer relative to GDP, Thailand should benefit from a lower import bill and a fall in cost-push inflation. India imports over 85% of its crude oil needs, and lower oil prices directly translate into reduced import costs, a narrower current account deficit, lower inflation and fiscal relief from reduced subsidy burdens for oil and fertilizers. In the Philippines, with no fuel subsidies and immediate pass-through to consumers, inflation surged the most to 7.2% y-o-y in April, and lower oil prices should lead to a faster inflation decline and reduce pressure on the current account. In South Korea, lower oil prices combined with gains from the ongoing AI boom should widen the current account surplus to above our current estimate of 15.5% of GDP in 2026 (already a record-high), and reduce goods price inflation.

Fig. 3: Net energy imports versus share of energy in CPI across Asia  
![](images/ce4e10427998cf13a3f19937ca8a78ec30beb9ea8c40fee206c6bb2ed14bd24f.jpg)

<details>
<summary>scatterplot</summary>

| Country     | Share of energy in CPI basket, % | Net energy imports, % of GDP |
| ----------- | -------------------------------- | ---------------------------- |
| Singapore   | 3.8                              | 4.8                          |
| Taiwan      | 3.8                              | 4.8                          |
| South Korea | 7.5                              | 5.6                          |
| New Zealand | 7.0                              | 2.1                          |
| China       | 6.8                              | 1.8                          |
| Philippines | 9.2                              | 3.8                          |
| Malaysia    | 9.0                              | 0.5                          |
| India       | 10.2                             | 3.4                          |
| Thailand    | 11.8                             | 7.0                          |
| Indonesia   | 11.5                             | -0.5                         |
| Australia   | 6.2                              | -4.5                         |
</details>

Note: Data on net energy imports as a percentage of GDP are as of 2024, while data on share of energy in CPI basket are the latest available.  
Source: CEIC, ITC Trademap and NOM Global Economics.

Fig. 4: Energy trade balance (exports minus imports), % of GDP, 2024

<table><tr><td></td><td colspan="5">Trade balance (% of GDP)</td></tr><tr><td></td><td>Energy (total)</td><td>Crude oil</td><td>Refined petroleum products</td><td>LNG</td><td>Coal</td></tr><tr><td>Thailand</td><td>-7.1</td><td>-6.3</td><td>0.8</td><td>-1.3</td><td>-0.3</td></tr><tr><td>South Korea</td><td>-5.7</td><td>-4.6</td><td>1.3</td><td>-1.6</td><td>-0.9</td></tr><tr><td>Singapore</td><td>-5.0</td><td>-4.8</td><td>0.3</td><td>-0.6</td><td>0.0</td></tr><tr><td>Taiwan</td><td>-5.0</td><td>-3.0</td><td>0.6</td><td>-1.5</td><td>-1.2</td></tr><tr><td>Philippines</td><td>-3.9</td><td>-0.8</td><td>-2.4</td><td>-0.2</td><td>-0.6</td></tr><tr><td>Japan</td><td>-3.7</td><td>-1.7</td><td>-0.2</td><td>-1.0</td><td>-0.7</td></tr><tr><td>India</td><td>-3.5</td><td>-3.9</td><td>1.7</td><td>-0.4</td><td>-0.9</td></tr><tr><td>New Zealand</td><td>-2.2</td><td>0.2</td><td>-2.3</td><td>0.0</td><td>0.0</td></tr><tr><td>China</td><td>-2.1</td><td>-1.7</td><td>0.1</td><td>-0.2</td><td>-0.2</td></tr><tr><td>Malaysia</td><td>-0.4</td><td>-1.8</td><td>-0.2</td><td>2.6</td><td>-1.1</td></tr><tr><td>Indonesia</td><td>0.5</td><td>-0.6</td><td>-1.3</td><td>0.5</td><td>1.9</td></tr><tr><td>Australia</td><td>4.2</td><td>0.1</td><td>-1.6</td><td>2.5</td><td>3.1</td></tr></table>

Note: We use HS codes 2709, 2710, 271111 and 2701 for crude oil, refined petroleum products, LNG and coal respectively. Excluded Hong Kong from the analysis as some data are unavailable.  
Source: ITC Trademap and NOM Global Economics.

## Differentiation within Asia is still critical

While lower oil prices provide a broad-based tailwind across Asia, country-specific differentiation will still be important. We remain more cautious on Indonesia and Thailand. Indonesia faces persistent policy uncertainty, concerns over BI independence, disruptions from the state commodity export agency on goods exports and credit rating concerns, while Thailand's structural constraints (ageing population, productivity challenges, China shock) remain intact. By contrast, India could enjoy a "double bonanza": not only does it benefit from lower oil prices, but the recent FCNR(B) announcement should lead to USD55bn in inflows, on our estimates, further boosting the BOP surplus.

## Asian central banks: Less hawkish at the margin, but divergence persists

The peace deal and the resulting oil price decline have marginally reduced hawkish pressures across Asian central banks, but large divergences across policy paths remain, reflecting heterogeneous domestic growth-inflation dynamics (Figure 5).

- HOLD (BI, RBI, RBA, BOT, PBoC): The peace deal strengths our view that BI will leave policy rates unchanged this week and beyond, although this is contingent on a stabilisation of IDR. We maintain our forecast for the RBI to stay on hold this year, even as headline inflation inches up, due to low underlying inflation. The RBA appears done with its tightening cycle, and we maintain our view that it may be able to deliver a rate cut around May 2027, as core inflation moves towards target. Amid low inflation and weak domestic demand, we also expect BOT and PBoC to leave rates unchanged this year.  
- DELAYED HIKE (CBC): Easing inflationary pressures are likely to reinforce the CBC's dovish stance, so we push out the timing we assign to the first 12.5bp hike to December from our previous forecast of June. We now expect 12.5bp rate hikes in December and March next year (terminal rate: 2.25%).  
- HIKE (BSP, BNM, MAS, BOK, RBNZ): Despite lower oil prices, we expect rate hikes / policy tightening in a few economies. For BSP, we expect 75bp of cumulative rate hikes (including a 25bp hike this week), as core inflation remains elevated. BNM is likely to hike by 25bp in Q4, amid robust growth and strong labor markets, and we continue to expect another slight S\$NEER slope increase by the MAS in July, as it faces rising core inflation pressures and broad-based growth. We also maintain our forecast for 75bp of cumulative hikes by the BOK (25bp in each of July, October and January 2027), as the BOK's May meeting emphasized positive spillovers from the semiconductor upcycle to the broader economy, growing demand-driven inflation pressures and the need to narrow the interest rate differential with the US. In New Zealand, we continue to forecast three 25bp rate hikes, commencing in September, to bring rates closer to neutral, but we see a risk that tightening could commence at the coming meeting on 8 July.

Fig. 5: NOM's central bank policy base case versus what-if scenario

<table><tr><td></td><td>Current monetary policy baseline</td><td>Central bank:What if oil falls below USD80/bbl and stays there?</td></tr><tr><td>China</td><td>No RRR or rate cuts for 2026</td><td>Maintain baseline forecast, as an ample interbank liquidity environment and falling CGB yields suggest limited scope for high-profile easing measures.</td></tr><tr><td>India</td><td>Policy hold at 5.25% through 2026</td><td>No change to our baseline forecast</td></tr><tr><td>Indonesia</td><td>Policy rate unchanged at 5.50% after 75bp in hikes so far, but significant risk of more hikes</td><td>On-hold and lower risk of additional hikes</td></tr><tr><td>Malaysia</td><td>25bp policy rate hike</td><td>No change to our baseline forecast</td></tr><tr><td>Philippines</td><td>75bp of additional hikes but measured approach (3 x 25bp)</td><td>Rising risk of another 50bp in hikes</td></tr><tr><td>Singapore</td><td>Expect another slight S$NEER slope increase by the MAS at the upcoming July MAS policy announcement (+0.5% slope appreciation)</td><td>No change to our baseline forecast</td></tr><tr><td>South Korea</td><td>3 x 25bp hikes (Jul 2026, Oct 2026, and Jan 2027); terminal rate at 3.25%</td><td>Maintain our baseline forecast of 3 x 25bp rate hikes. The BOK&#x27;s hawkish stance, supported by positive spillovers from the semiconductor upcycle to the broader economy, the rising risk of demand-driven inflation, and concerns over the Korea-US interest rate differential, is likely to remain intact despite lower oil prices.</td></tr><tr><td>Taiwan</td><td>Following the US-Iran interim agreement, we now delay the timing of our rate hike call to Dec 2026 and Mar 2027 (versus Jun and Dec 2026); terminal rate at 2.25%.</td><td>Could further delay rate hikes as lower oil prices are likely to strengthen the CBC&#x27;

[中间内容因长度限制已省略]

ER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
