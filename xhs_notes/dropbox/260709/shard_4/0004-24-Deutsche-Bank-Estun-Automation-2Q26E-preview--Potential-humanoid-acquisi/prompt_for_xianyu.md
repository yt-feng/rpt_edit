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
# Industry Estun Automation

Asia
China
Hong Kong

Industrials
Manufacturing

Date
7 July 2026

Initiation of Coverage

# 2Q26E preview; Potential humanoid acquisition; Initiate H shares at Hold

Estun is scheduled to release full 1H26 results in the evening of 21 August. We see the possibility for the company to release a profit alert in July.

We expect Estun's net profit to grow strongly YoY in 1H26E off a very low base, posing the possibility for Estun to issue a positive profit alert in July. For 2026E, we forecast revenue of RMB6bn and net profit of RMB305mn/ 5% NPM, which are in line with the company's guidance. The potential acquisition of the humanoid robot business Codroid should contribute minimally to financials, but positively to valuation. This optimism is well-reflected in Estun's share price, especially the A shares, as investors are excited about synergies from Estun's no.1 position in China's industrial robot market and the lack of humanoid robot OEM investment targets in the Mainland China stock markets. In the near term, we think the market optimism around humanoid robots could continue to drive Estun's shares higher. On a 12M view, we reiterate our Sell rating with a target price of RMB31.4 for the A shares as we consider the 2026E P/S of 7.4x to be full vs humanoid robot peer UBTECH at 11x (based on BBG estimates), considering Estun's much smaller humanoid robot exposure. We initiate the H shares at Hold with a target price of HK\$23.6, as we think the valuation of 2026E P/S of 3.3x for the H shares points to balanced risk/reward.

## 1H26E preview: Strong profit growth off a very low base

For 2Q26E, we forecast Estun to deliver sales of RMB1.5bn (+15% YoY), net profit of RMB40mn (better than RMB-6mn loss in 2Q25 YoY; lower than RMB98mn in 1Q26 QoQ) and recurring net profit of RMB38mn (better than RMB-22mn loss in 2Q25 YoY and RMB19mn in 1Q26 QoQ).

For 1H26E, we forecast Estun to deliver sales of RMB2.7bn (+7% YoY), net profit of RMB138mn (+1960% YoY from RMB7mn in 1H25) and recurring net profit of RMB58mn (vs RMB-18mn loss in 1H25).

For sales, we expect the sales growth to improve to +15% YoY in 2Q26E from a decline of -2% in 1Q26 lifted by: (1) solid demand from battery and electronics end-markets; (2) the realisation of the 5-15% price increase adopted in 1Q26; and (3) a lower base.

## DB AG/Hong Kong

Iris Zheng, CFA
Research Analyst
+852-2203-5884

<table><tr><td colspan="4">Key Changes</td></tr><tr><td>Company</td><td>Target Price</td><td colspan="2">Rating</td></tr><tr><td>002747.SZ</td><td>20.00 to 31.40</td><td colspan="2">-</td></tr><tr><td colspan="4">Source: DB</td></tr><tr><td colspan="4">Companies featured</td></tr><tr><td colspan="3">Estun (002747.SZ),CNY46.03</td><td>Sell</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>P/E (x)</td><td>422.8</td><td>146.1</td><td>98.5</td></tr><tr><td>EV/EBITDA (x)</td><td>61.7</td><td>71.3</td><td>55.1</td></tr><tr><td>Price/book (x)</td><td>10.5</td><td>12.5</td><td>11.1</td></tr><tr><td colspan="3">Estun (2715.HK),HKD23.32</td><td>Hold</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>P/E (x)</td><td>-</td><td>64.1</td><td>43.2</td></tr><tr><td>EV/EBITDA (x)</td><td>-</td><td>33.6</td><td>25.9</td></tr><tr><td>Price/book (x)</td><td>0.0</td><td>5.5</td><td>4.9</td></tr><tr><td colspan="4">Source: DB</td></tr></table>

For profitability, we forecast the GPM to improve to 31% in 2Q26E thanks to higher sales and price increase. We expect Estun to exercise stringent cost control of operating expenses. However, we anticipate the net profit to be lower in 2Q26E sequentially vs 1Q26 as 1Q26 benefited from a RMB87mn non-recurring gain. Furthermore, we expect asset impairments to step up sequentially on higher sales and automotive related sales with long receivable duration.

For 2026E, we forecast sales of RMB6bn (+23% YoY), net profit of RMB305mn (5.1% NPM; +578% YoY) and recurring net profit of RMB205mn (3.4% NPM; +2714% YoY). This is inline with the company's guidance of RMB6bn sales and 5% NPM.

In the evening of 2 July, Estun announced that the company is considering fully acquiring Codroid by cash. We think the potential acquisition is somewhat as expected, as Codroid is closely linked to Estun — Estun already owns 13.9535% of Codroid, and Estun's parent company Nanjing Pereste Technology owns 39.0698% of Codroid.

Founded in 2022, Codroid manufactures collaborative robots (cobots), embodied robots and core components. The key end-markets for Codroid include automotive, household appliance, electronics and food logistics.

In 2025, Codroid generated revenue of RMB50.2mn with net loss of RMB53mn. Therefore, we expect the acquisition to contribute minimally financially to Estun in the near future. However, we think Codroid's exposure to the humanoid robot business will lift/ has lifted market sentiment of Estun.

Figure 1: Financial details of Codroid

Financial performance of Codroid

<table><tr><td>RMB mn</td><td>2024</td><td>2025</td><td>4M26</td></tr><tr><td>Revenue</td><td>11.0</td><td>50.2</td><td>14.9</td></tr><tr><td>Net profit</td><td>(36.1)</td><td>(53.0)</td><td>(12.7)</td></tr><tr><td>NPM</td><td>-329%</td><td>-106%</td><td>-85%</td></tr><tr><td>Asset</td><td>121.9</td><td>82.8</td><td>80.4</td></tr><tr><td>Net asset</td><td>108.0</td><td>55.7</td><td>48.7</td></tr></table>

Source : Company data

Codroid has launched three embodied robots:

Codroid 02: A bipedal humanoid robot with height of 170cm and weight of 70kg. Total degree of freedom is 29 or 31. Payload per arm is 5kg.

C05-U: A wheeled humanoid robot with height of 138-168cm and weight of 32kg.

C05-L: Also a wheeled humanoid robot with height of 138-168cm and weight of 32kg.

Figure 2: Embodied robots from Codroid: Codroid 02 (LHS) and C05-L (RHS)

![](images/8f18f8ee7f596afb8a9bb4b04d03e01745e8eb1c52474b1fc833522eb4508b9b.jpg)

Source : Company data

A shares: Raise target price to RMB31.4; Reiterate Sell

We adjust our 2026/2027 net profit estimates by +8%/-10%, respectively, to reflect management's guidance for 2026E. We introduce new estimates for 2028E.

We increase our DCF-derived target price to RMB31.4 from RMB20 as we incorporate higher growth assumptions for the mid-term to reflect the embodied AI robot opportunities. Our target price is based on a three-stage DCF valuation. We use a terminal growth of 3.5%, a risk-free rate of 1.8%, an equity risk premium of 5%, and a beta of 1.61 to derive our WACC of 9.3%.

Estun's A shares are trading on 2026E/2027E P/E of 146x/98x, above its long-term one year forward P/E of 67.5x. The company is trading on 2026E P/S of 7.4x.

Upside risks are (1) sustained fast growth of robot market demand in both China and Europe; (2) Estun gaining meaningful market share in China and overseas thanks to new product offerings and strong customer recognition; and (3) humanoid robots contributing to group sales and earnings meaningfully in the foreseeable future.

H shares: Initiate at Hold with target price of HK\$23.6

We initiate coverage of the H shares with a Hold recommendation and a target price of HK\$23.6. Our target price is derived by applying a 35% discount to our target price for the A shares — this discount is consistent with the average discount rate from our A/H share discount tracker which tracks close to 50 companies that were dual-listed since 2H24. Our target price for A shares is based on a three-stage DCF valuation. For 2026-28, we use our detailed forecasts. For the mid-term (2029-50), we use our mid-term assumptions, and for the years beyond, we use a terminal growth of 3.5%. We use a risk-free rate of 1.8%, an equity risk premium of 5%, and a beta of 1.61 to derive our WACC of 9.3%. We notice that currently humanoid robot related names such as Estun, Zhaowei, Sanhua and Lens are trading on a wider discount of over 50% on average, suggesting relatively more conservative attitude towards the humanoid robot opportunities among investors in the Hong Kong stock market. We think the risk/reward is balanced for the H shares considering the lower valuation and the growth opportunities. We therefore rate the H shares Hold.

## Estun's H shares are trading on 2026E/2027EP/E of 64x/43x, and 2026EP/S of 3.3x.

Upside risks are the same as those above for A shares. Downside risks are: (1) deteriorated robot market demand with revived pricing pressure; (2) minimal humanoid robot related sales contributed and rising costs for model training; and (3) heightened geopolitical risks weighing on Estun's overseas sales.

Figure 3: Estimate changes for A share

<table><tr><td>(in RMB mn)</td><td>2025</td><td>DBe 2026E</td><td>DBe Old est. s</td><td>New Old est.</td><td>BBG cons</td><td>DBe vs BBG</td><td>DBe 2027E</td><td>DBe Old est. s</td><td>New Old est.</td><td>BBG cons</td><td>DBe vs BBG</td><td>DBe 2028E</td><td>BBG cons</td><td>DBe vs BBG</td></tr><tr><td>Revenue</td><td>4,888</td><td>6,001</td><td>6,443</td><td>-6.9%</td><td>5,785</td><td>3.7%</td><td>7,069</td><td>7,884</td><td>-10.3%</td><td>6,675</td><td>5.9%</td><td>8,309</td><td>7,580</td><td>9.6%</td></tr><tr><td>Revenue YoY</td><td>21.9%</td><td>22.8%</td><td>22.2%</td><td></td><td>18.4%</td><td></td><td>17.8%</td><td>22.4%</td><td></td><td>15.4%</td><td></td><td>17.5%</td><td>13.6%</td><td></td></tr><tr><td>COGS</td><td>(3,448)</td><td>(4,138)</td><td>(4,561)</td><td></td><td></td><td></td><td>(4,860)</td><td>(5,566)</td><td></td><td></td><td></td><td>(5,703)</td><td></td><td></td></tr><tr><td>Gross profit</td><td>1,440</td><td>1,863</td><td>1,882</td><td>-1.0%</td><td></td><td></td><td>2,209</td><td>2,317</td><td>-4.7%</td><td></td><td></td><td>2,606</td><td></td><td></td></tr><tr><td>Gross margin</td><td>29.5%</td><td>31.0%</td><td>29.2%</td><td></td><td></td><td></td><td>31.3%</td><td>29.4%</td><td></td><td></td><td></td><td>31.4%</td><td></td><td></td></tr><tr><td>Business tax and surplus</td><td>(24)</td><td>(29)</td><td>(32)</td><td></td><td></td><td></td><td>(34)</td><td>(39)</td><td></td><td></td><td></td><td>(40)</td><td></td><td></td></tr><tr><td>Selling exp</td><td>(449)</td><td>(480)</td><td>(515)</td><td></td><td></td><td></td><td>(530)</td><td>(591)</td><td></td><td></td><td></td><td>(623)</td><td></td><td></td></tr><tr><td>Admin exp</td><td>(410)</td><td>(431)</td><td>(503)</td><td></td><td></td><td></td><td>(465)</td><td>(528)</td><td></td><td></td><td></td><td>(502)</td><td></td><td></td></tr><tr><td>R&amp;D exp</td><td>(419)</td><td>(468)</td><td>(515)</td><td></td><td></td><td></td><td>(551)</td><td>(591)</td><td></td><td></td><td></td><td>(648)</td><td></td><td></td></tr><tr><td>Finance cost</td><td>(153)</td><td>(153)</td><td>(120)</td><td></td><td></td><td></td><td>(153)</td><td>(120)</td><td></td><td></td><td></td><td>(153)</td><td></td><td></td></tr><tr><td>Other gain&amp;loss</td><td>85</td><td>50</td><td>100</td><td></td><td></td><td></td><td>50</td><td>100</td><td></td><td></td><td></td><td>50</td><td></td><td></td></tr><tr><td>Operating income (reported)</td><td>70</td><td>351</td><td>296</td><td>18.8%</td><td></td><td></td><td>525</td><td>547</td><td>-4.0%</td><td></td><td></td><td>689</td><td></td><td></td></tr><tr><td>OP margin</td><td>1.4%</td><td>5.9%</td><td>4.6%</td><td></td><td></td><td></td><td>7.4%</td><td>6.9%</td><td></td><td></td><td></td><td>8.3%</td><td></td><td></td></tr><tr><td>Non-operating income</td><td>21</td><td>21</td><td>27</td><td></td><td></td><td></td><td>21</td><td>27</td><td></td><td></td><td></td><td>21</td><td></td><td></td></tr><tr><td>Non-operating exp</td><td>(13)</td><td>(13)</td><td>(11)</td><td></td><td></td><td></td><td>(13)</td><td>(11)</td><td></td><td></td><td></td><td>(13)</td><td></td><td></td></tr><tr><td>Profit before tax</td><td>77</td><td>359</td><td>312</td><td></td><td></td><td></td><td>533</td><td>563</td><td></td><td></td><td></td><td>697</td><td></td><td></td></tr><tr><td>Tax exp</td><td>(32)</td><td>(54)</td><td>(37)</td><td></td><td></td><td></td><td>(80)</td><td>(68)</td><td></td><td></td><td></td><td>(104)</td><td></td><td></td></tr><tr><td>Tax rate</td><td>41.5%</td><td>15.0%</td><td>12.0%</td><td></td><td></td><td></td><td>15.0%</td><td>12.0%</td><td></td><td></td><td></td><td>15.0%</td><td></td><td></td></tr><tr><td>Minority</td><td>(0)</td><td>(0)</td><td>8</td><td></td><td></td><td></td><td>(0)</td><td>9</td><td></td><td></td><td></td><td>(1)</td><td></td><td></td></tr><tr><td>Minority%</td><td>0.8%</td><td>0.1%</td><td>-2.9%</td><td></td><td></td><td></td><td>0.1%</td><td>-1.8%</td><td></td><td></td><td></td><td>0.1%</td><td></td><td></td></tr><tr><td>Reported net profit</td><td>45</td><td>305</td><td>283</td><td>7.9%</td><td>256</td><td>19.0%</td><td>452</td><td>505</td><td>-10.3%</td><td>333</td><td>36.0%</td><td>592</td><td>427</td><td>38.5%</td></tr><tr><td>Net margin (reported)</td><td>0.9%</td><td>5.1%</td><td>4.4%</td><td></td><td>4.4%</td><td></td><td>6.4%</td><td>6.4%</td><td></td><td>5.0%</td><td></td><td>7.1%</td><td>5.6%</td><td></td></tr><tr><td>Net profit YoY</td><td>-105.5%</td><td>578.0%</td><td>360.9%</td><td></td><td></td><td></td><td>48.4%</td><td>78.5%</td><td></td><td></td><td></td><td>30.8%</td><td></td><td></td></tr><tr><td rowspan="2">Non-recurring item as % of reported net profit</td><td>38</td><td>100</td><td>-</td><td></td><td></td><td></td><td>100</td><td>-</td><td></td><td></td><td></td><td>100</td><td></td><td></td></tr><tr><td>83.8%</td><td>0.0%</td><td>0.0%</td><td></td><td></td><td></td><td>0.0%</td><td>0.0%</td><td></td><td></td><td></td><td>0.0%</td><td></td><td></td></tr><tr><td>Recurring net profit</td><td>7</td><td>205</td><td>283</td><td>-27.5%</td><td></td><td></td><td>352</td><td>505</td><td>-30.2%</td><td></td><td></td><td>492</td><td></td><td></td></tr><tr><td>Net margin (recurring)</td><td>0.1%</td><td>3.4%</td><td>4.4%</td><td></td><td></td><td></td><td>5.0%</td><td>6.4%</td><td></td><td></td><td></td><td>5.9%</td><td></td><td></td></tr><tr><td>EPS (basic) (in Rmb)</td><td>0.05</td><td>0.32</td><td>0.33</td><td>-3.1%</td><td>0.27</td><td>17.1%</td><td>0.47</td><td>0.58</td><td>-19.4%</td><td>0.35</td><td>34.3%</td><td>0.61</td><td>0.45</td><td>37.1%</td></tr><tr><td>EPS YoY</td><td>-105.5%</td><td>510.2%</td><td>360.9%</td><td></td><td></td><td></td><td>48.4%</td><td>78.5%</td><td></td><td></td><td></td><td>30.8%</td><td></td><td></td></tr><tr><td>End shares</td><td>871</td><td>968</td><td>870</td><td></td><td></td><td></td><td>968</td><td>870</td><td></td><td></td><td></td><td>968</td><td></td><td></td></tr><tr><td>DPS (in Rmb)</td><td>-</td><td>-</td><td>-</td><td></td><td>0.05</td><td></td><td>-</td><td>-</td><td></td><td>0.07</td><td></td><td>-</td><td>0.09</td><td></td></tr><tr><td>Payout rate</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td></td><td>18.6%</td><td></td><td>0.0%</td><td>0.0%</td><td></td><td>19.8%</td><td></td><td>0.0%</td><td>19.7%</td><td></td></tr></table>

Source : Company data, DB estimates, consensus from Bloomberg Finance LP

Figure 4: Financials (annual): Estun revenue in 2025 resumed growth trend after a decline in 2024  
![](images/f350f71ed3a42d6d661a23fe7e2b1822fdd14982b8e5b5c134d99b93f0f46d83.jpg)  
Source : Company data, DB estimates

![](images/b190ec3c3ed38b7915c0993dca998ae4eed64a86f0543c0a6e136a140ceab2ac.jpg)

Figure 5: Financials (quarterly): net profit reached a record high in 1Q26, primarily driven by non-operating fair value changes in equity investments  
![](images/83908218b77d7c249fe481c27e35b8251bebf48fb93f1c0e2bb5b55af028a557.jpg)  
Source : Company data, DB

![](images/5794e9f21f28eba91d970bc3124539211b3ad302f35d0b8f7b9e27133e7c9882.jpg)  
Figure 6: Estun was the largest robot manufacturer in the China industrial robot market in 1Q26 (by unit)

![](images

[中间内容因长度限制已省略]

ted performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG. It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

<table><tr><td>DB AG21 MoorfieldsLondon EC2Y 9DBUnited KingdomTel: (44) 20 7545 8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, South Tower,Singapore 048583TeL: +65 6423 8001</td></tr></table>

<table><tr><td colspan="4">David Folkerts-LandauGroup Chief Economist and Global Head of Research</td></tr><tr><td>Pam FinelliCOO and Head of Fixed Income Research</td><td>Steve PollardGlobal Head of Company Research and Sales</td><td>Jim ReidGlobal Head of Macro and Thematic Research</td><td>Tim RokossaHead of European Company Research</td></tr><tr><td>Matthew BarnardHead of AmericasCompany Research</td><td>Debbie JonesGlobal Head of Sustainability and Data Innovation, Research</td><td>Robin WinklerHead of German Macro Research</td><td>Sameer GoelGlobal Head of EM &amp; APAC Research</td></tr><tr><td>Francis YaredGlobal Head of Rates Research</td><td>George SaravelosGlobal Head of FX Research</td><td>Peter HooperVice-Chair of Research</td><td>Nilendra de-MelHead of APAC &amp; Middle East Product Development</td></tr></table>

## International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr></table>
"""
