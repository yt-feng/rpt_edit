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
# Supportive liquidity conditions continued in May, though rising pressure ahead

Equity Strategy

## Launching the monthly product China Flow Lens

We are launching a new product to track fund flows, positioning, and capital supply-demand indicators in China's equity market. The report aims to provide a structured framework to assess evolving liquidity conditions and their trading implications.

## A better capital supply/demand mix for A-shares

Overall, liquidity conditions continue to favor A-shares over Hong Kong equities. While domestic liquidity remains strong and the restock of “national team” capital provides downside support for A-shares, Hong Kong faces near-term headwinds from slowing southbound inflows, tighter cross-border capital rules, and an upcoming wave of lock-up expirations. As such, despite faster style and sector rotations since May, we expect A-shares to remain relatively better supported than H-shares in the coming months.

## Liquidity support in the near term, rising pressures ahead

Capital flows to foreign-domiciled China equity funds tracked by EPFR accelerated in May, in line with narrowing UW in China among active EM funds in Apr. At the same time, China's domestic ETFs – often used by the “national team” for market support – continued to see heavy redemptions over the past month. However, with ETF outflows YTD already exceeding the inflows seen in 2023-25, residual selling pressure could ease into 2H26, in our view. On the capital supply side, stronger hybrid fund issuances and share buybacks supported A-share liquidity in May, lifting ADTV to \~RMB3.2tn. However, southbound flows to Hong Kong turned negative, with a net outflow of HKD3.6bn (vs. +HKD56.5bn in Apr). On the demand side, IPO financing and restricted share unlocks eased notably. That said, the upcoming CXMT IPO and a surge in Hong Kong lock-up expirations – projected at \~HKD270bn in Jul and \~HKD400bn in Sep by WIND – are likely to exert liquidity pressure on A-share and Hong Kong markets in the next 3 months.

Exhibit 1: Capital supply dynamics still favor A shares vs. Hong Kong stocks  
A-share and Hong Kong secondary market liquidity dashboard

<table><tr><td>A-share market</td><td>May-26</td><td>Apr-26</td><td>Imp.</td><td>Hong Kong</td><td>May-26</td><td>Apr-26</td><td>Imp.</td></tr><tr><td>ADTV (RMB bn)</td><td>3182.5</td><td>2343.8</td><td>▲</td><td>ADTV (HKD bn)</td><td>292.8</td><td>253.4</td><td>▲</td></tr><tr><td>Margin trading as % of MT</td><td>10.1%</td><td>9.8%</td><td>▼</td><td></td><td></td><td></td><td></td></tr><tr><td>New fund issuances (bn)</td><td>70.1</td><td>46.4</td><td>▲</td><td>Share buybacks (HKD bn)</td><td>22.0</td><td>13.6</td><td>▲</td></tr><tr><td>Share buybacks (RMB bn)</td><td>17.1</td><td>11.0</td><td>▲</td><td>SB capital flows (HKD bn)</td><td>-3.6</td><td>56.5</td><td>▼</td></tr><tr><td>NB trading as % of turnover</td><td>6.2%</td><td>6.1%</td><td>▼</td><td></td><td></td><td></td><td></td></tr><tr><td>4-Week fund flows (USD mn)</td><td>347.4</td><td>51.6</td><td>▲</td><td>4-Week fund flows (USD mn)</td><td>587.5</td><td>824.6</td><td>▼</td></tr><tr><td>IPO financing (RMB bn)</td><td>11.1</td><td>21.2</td><td>▲</td><td>IPO financing (HKD bn)</td><td>13.4</td><td>43.1</td><td>▲</td></tr><tr><td>Lock-up expirations (RMB bn)</td><td>184.9</td><td>303.8</td><td>▲</td><td>Lock-up expirations (HKD bn)</td><td>26.9</td><td>27.8</td><td>▲</td></tr><tr><td>Share reductions (RMB bn)</td><td>49.3</td><td>37.1</td><td>▼</td><td></td><td></td><td></td><td></td></tr></table>

Source: WIND, EPFR. Note: ▲/ ▶/ ▼ denote whether an indicator's movement is supportive, neutral, adverse to market liquidity relative to the previous month. A ▶ is assigned when the MoM change falls within 5%. See full exhibit on page 8  
BofA GLOBAL RESEARCH

## 12 June 2026

Equity Strategy

China

Patrick Pan, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 4601

patrick.pan2@bofa.com

Winnie Wu >>

Research Analyst

BofA (Hong Kong)

+852 3508 3058

winnie.wu@bofa.com

Gina Wu >>

Strategist

BofA (Hong Kong)

+852 3508 8008

gina.wu@bofa.com

## Glossary

ADR: American depositary receipt  
ADTV: average daily trading value

CGB: China government bond

EM: emerging market

Imp.: Impact

MLF: Medium-term lending facility

MT: market turnover

"National team": state-backed institutional investors that step in to stabilize the market during periods of sharp volatility

OMO: open market operations

OW: overweight

PBOC: People's Bank of China

SB/NB: southbound/northbound

UW: underweight

## Supportive liquidity conditions continue

## Launching the new product of China Flow Lens

We are launching a monthly strategy product to track liquidity dynamics and investor sentiment in China's stock market. By integrating fund flows, positioning, and indicators on both capital supply and demand, the report offers a structured framework for assessing how liquidity and sentiment evolve – and what it implies for trading direction. Over the past decade, fund flow data have shown a strong correlation with China equities, particularly during market reversals triggered by major events. For instance, flows to foreign-domiciled China equity funds turned positive swiftly during the post-COVID reopening in late 2022 and again amid policy easing in September 2024.

Exhibit 2: Fund flow data show a strong correlation with China stocks  
Monthly capital flows to foreign-domiciled China funds (USD bn) vs. MSCI China and CSI 300 indices  
![](images/35d09e546f68e353edc9744612f7bcc32d6be5bb5e9b1c9640ffbb2d33b60b93.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Fund flows (RHS) | MSCI China | CSI 300 |
|--------|------------------|----------|---------|
| Jan-17 | 1000             | 1000     | 1000    |
| Jul-17 | 1100             | 1200     | 1100    |
| Jan-18 | 1200             | 1600     | 1200    |
| Jul-18 | 1300             | 1400     | 1300    |
| Jan-19 | 1400             | 1300     | 1400    |
| Jul-19 | 800              | 1200     | 1200    |
| Jan-20 | 1200             | 1300     | 1300    |
| Jul-20 | 1500             | 1600     | 1500    |
| Jan-21 | 1800             | 1900     | 1600    |
| Jul-21 | 1400             | 1700     | 1500    |
| Jan-22 | 1300             | 1500     | 1400    |
| Jul-22 | 1600             | 700      | 1300    |
| Jan-23 | 1400             | 1200     | 1200    |
| Jul-23 | 1200             | 900      | 1100    |
| Jan-24 | 1100             | 800      | 1000    |
| Jul-24 | 900              | 700      | 900     |
| Jan-25 | 50               | 60       | 80      |
| Jul-25 | 1300             | 1400     | 1300    |
| Jan-26 | 1200             | 1500     | 1400    |
</details>

Source: WIND, EPFR  
BofA GLOBAL RESEARCH

## Fund flows and market allocation: recovering inflows – but for how long?

Following a slowdown in April this year, capital flows into foreign-domiciled China equity funds, tracked by EPFR, re-accelerated in May, with rolling 4-week net flows to active China funds turning positive again after March. By market, both A-share and Hong Kong-focused China funds saw solid inflows. In contrast, funds benchmarking the MSCI China Index continued to experience redemptions over the past 3 months, albeit at a moderating pace. While EPFR's coverage represents only a relatively small portion of the overall market, we believe the data still provides a useful indication of the broad direction of fund flows in the short term.

Exhibit 3: Foreign investors revisit A-share and Hong Kong stocks, but remain cautious on Chinese ADRs  
Weekly capital flows to foreign-domiciled China funds benchmarking against MSCI China, A-share indices, and Hong Kong indices (USD mn)

<table><tr><td>Benchmarks</td><td>4-Mar</td><td>11-Mar</td><td>18-Mar</td><td>25-Mar</td><td>1-Apr</td><td>8-Apr</td><td>15-Apr</td><td>22-Apr</td><td>29-Apr</td><td>6-May</td><td>13-May</td><td>20-May</td><td>27-May</td></tr><tr><td>China (Total)</td><td>2,194.9</td><td>-2,126.5</td><td>-1,106.9</td><td>1,723.4</td><td>-2,439.4</td><td>-271.9</td><td>328.9</td><td>385.5</td><td>-371.1</td><td>-1,016.7</td><td>935.3</td><td>2,809.8</td><td>-1,931.7</td></tr><tr><td>MSCI China</td><td>-302.0</td><td>-563.9</td><td>-229.9</td><td>-29.8</td><td>-209.8</td><td>30.4</td><td>67.0</td><td>-430.0</td><td>-492.8</td><td>-27.5</td><td>-152.0</td><td>-41.8</td><td>-35.2</td></tr><tr><td>A-share indices</td><td>-151.8</td><td>-423.0</td><td>-111.2</td><td>-110.0</td><td>-152.8</td><td>-41.9</td><td>205.1</td><td>-80.2</td><td>-31.3</td><td>3.1</td><td>307.0</td><td>120.2</td><td>-82.9</td></tr><tr><td>H-share indices</td><td>2,721.6</td><td>-914.0</td><td>-437.0</td><td>2043.8</td><td>-1,976.4</td><td>-259.1</td><td>262.9</td><td>470.6</td><td>350.1</td><td>-900.4</td><td>103.9</td><td>1,733.8</td><td>-349.7</td></tr></table>

Source: EPFR. Note: A-share index benchmarks include MSCI China A Share, MSCI China A 50, CSI 300, SSE Composite Index, SSE 50, Shenzhen ChiNext, and CSI 800. H-share index benchmarks include HSI, Hang Seng China Enterprise, and Hang Seng Tech. China (total) represents a broad universe of all EPFR-tracked foreign-domiciled funds with a China investment mandate, whose benchmarks also include other China-specific indices or multi-market indices (i.e., $70\% * \mathrm{CSI}300 + 30\% * \mathrm{HSI}$ ). AUM for funds linked to China (total)/MSCI China/A-share indices/H-share indices was USD194.4bn/USD27.7bn/USD16.1bn/USD47.0bn as of May 27  
BofA GLOBAL RESEARCH

It is also worth noting that heavy redemptions of China's domestic ETFs tracking broad market indices (i.e., SSE 50, CSI 300, CSI 500, CSI 1000, and ChiNext Index) – a key trading channel used by China's “national team” (Note: “national team” refers to state-backed institutional investors that step in to stabilize the market during periods of sharp declines or volatility) in market aid – persisted over the past month. However, against the market rebound over the past 2 years, cumulative YTD outflows from domestic ETFs have exceeded the inflows seen in 2023-25, suggesting that prior support has been largely unwound and that selling pressure could gradually ease in 2H26. While the retreat of “national team” weighed on A-share sentiment during the sharp rally in Jan 2026, looking ahead, it should reserve policy capacity for future market support in case of potential market turbulence, in our view.

Exhibit 4: Stock selling by China's "national team" continues  
Cumulative capital flows to China's domestic ETF funds (USD bn)  
![](images/3ca32e39debe65a3809f73a22cf21eeb93ad77593005cf64fa7746ea2370c849.jpg)

<details>
<summary>line chart</summary>

| Date | Value |
|---|---|
| Jan-22 | 0 |
| Apr-22 | -5 |
| Jul-22 | -10 |
| Oct-22 | 5 |
| Jan-23 | 10 |
| Apr-23 | 5 |
| Jul-23 | 15 |
| Oct-23 | 30 |
| Jan-24 | 80 |
| Apr-24 | 90 |
| Jul-24 | 100 |
| Oct-24 | 160 |
| Jan-25 | 145 |
| Apr-25 | 160 |
| Jul-25 | 155 |
| Oct-25 | 150 |
| Jan-26 | 150 |
| Apr-26 | -30 |
</details>

Source: EPFR  
BofA GLOBAL RESEARCH

Exhibit 5: SSE new account opening +11% MoM in May  
New account openings at the Shanghai Stock Exchange ('000)  
![](images/a8edb86d0fc1c08a6a6f7bac11a0e507feb0caccd5a28d51cb5f583a69f7bef0.jpg)

<details>
<summary>bar chart</summary>

| Date | Value |
|---|---|
| Jan-21 | 3600 |
| Feb-21 | 2700 |
| Mar-21 | 4100 |
| Apr-21 | 2800 |
| May-21 | 2500 |
| Jun-21 | 2700 |
| Jul-21 | 3200 |
| Aug-21 | 2800 |
| Sep-21 | 1700 |
| Oct-21 | 2300 |
| Nov-21 | 2400 |
| Dec-21 | 2300 |
| Jan-22 | 4000 |
| Feb-22 | 2100 |
| Mar-22 | 2300 |
| Apr-22 | 2400 |
| May-22 | 2100 |
| Jun-22 | 2300 |
| Jul-22 | 1900 |
| Aug-22 | 1800 |
| Sep-22 | 1700 |
| Oct-22 | 1600 |
| Nov-22 | 1500 |
| Dec-22 | 1400 |
| Jan-23 | 3300 |
| Feb-23 | 1800 |
| Mar-23 | 1700 |
| Apr-23 | 1800 |
| May-23 | 1700 |
| Jun-23 | 1600 |
| Jul-23 | 1500 |
| Aug-23 | 1400 |
| Sep-23 | 1300 |
| Oct-23 | 1400 |
| Nov-23 | 1500 |
| Dec-23 | 1600 |
| Jan-24 | 1900 |
| Feb-24 | 1800 |
| Mar-24 | 1700 |
| Apr-24 | 1600 |
| May-24 | 1500 |
| Jun-24 | 1400 |
| Jul-24 | 1300 |
| Aug-24 | 1200 |
| Sep-24 | 1100 |
| Oct-24 | 1000 |
| Nov-24 | 900 |
| Dec-24 | 800 |
| Jan-25 | 6800 |
| Feb-25 | 2700 |
| Mar-25 | 1900 |
| Apr-25 | 1800 |
| May-25 | 1700 |
| Jun-25 | 1600 |
| Jul-25 | 1500 |
| Aug-25 | 1600 |
| Sep-25 | 1700 |
| Oct-25 | 1800 |
| Nov-25 | 1900 |
| Dec-25 | 2600 |
| Jan-26 | 5900 |
| Feb-26 | 4600 |
| Mar-26 | 4500 |
| Apr-26 | 4400 |
| May-26 | 4300 |
| Jun-26 | 4400 |
| Jul-26 | 4500 |
| Aug-26 | 4600 |
| Sep-26 | 4700 |
| Oct-26 | 4800 |
| Nov-26 | 4900 |
| Dec-26 | 5800 |
</details>

Source: WIND. Note: This indicator is not included in our dashboard given the uncertainty around its release timing.  
BofA GLOBAL RESEARCH

In the charts below, we examine global EM funds' market allocations as of April 2026, which better reflect global fund managers' positioning than fund flows. According to the EPFR data, active funds notably expanded their exposure to South Korea and Taiwan stocks in April, funded by reductions in China and India holdings. However, these shifts can be distorted by market cap movements in other markets as well as existing positions. To mitigate such impact, we compare market exposure of active funds vs. passive funds (as proxies of market weights) and track how the gap evolves MoM.

Overall, we find active global EM funds' underweights in China and Taiwan actually narrowed in April, while underweights in India widened. Meanwhile, we observed that global EM fund managers turned more constructive on South Korea.

Exhibit 6: EM funds' exposure to South Korea and Taiwan stocks soar  
Market allocations by active global EM funds (%)  
![](images/af2c70bf41bdff9bb32783105930c0d1a544feadd2b53999508baaa522eed1fe.jpg)

<details>
<summary>line chart</summary>

| Date | Brazil | China | India | S. Korea | Taiwan |
|---|---|---|---|---|---|
| Jan-21 | 4.5 | 32.5 | 9.5 | 11.5 | 11.5 |
| Jul-21 | 4.8 | 30.0 | 10.5 | 11.0 | 12.0 |
| Jan-22 | 4.0 | 27.0 | 11.5 | 10.5 | 13.0 |
| Jul-22 | 6.0 | 29.0 | 12.5 | 10.0 | 12.5 |
| Jan-23 | 6.5 | 22.0 | 13.5 | 10.5 | 12.0 |
| Jul-23 | 7.0 | 27.0 | 14.0 | 11.0 | 13.0 |
| Jan-24 | 7.5 | 23.0 | 15.0 | 11.5 | 14.0 |
| Jul-24 | 6.5 | 20.0 | 17.0 | 10.5 | 16.0 |
| Jan-25 | 6.0 | 26.0 | 14.5 | 9.0 | 17.5 |
| Jul-25 | 6.5 | 24.0 | 13.0 | 10.5 | 18.0 |
| Jan-26 | 7.0 | 20.0 | 9.5 | 17.0 | 21.0 |
</details>

Source: EPFR  
BofA GLOBAL RESEARCH

Exhibit 7: Active funds reduce their UW positions on China  
Active and passive global EM funds' exposure to China stocks $(\%)$  
![](images/738f8aae180db94298cd25568cc9060e4f16b735120b452eb94315f331dfb42d.jpg)

<details>
<summary>line chart</summary>

| Date   | Active | Passive |
|--------|--------|---------|
| Jan-21 | 33.0   | 32.0    |
| Jul-21 | 30.0   | 29.0    |
| Jan-22 | 27.0   | 28.0    |
| Jul-22 | 26.0   | 30.0    |
| Jan-23 | 28.0   | 27.0    |
| Jul-23 | 24.0   | 25.0    |
| Jan-24 | 20.0   | 21.0    |
| Jul-24 | 19.0   | 20.0    |
| Jan-25 | 26.0   | 27.0    |
| Jul-25 | 25.0   | 26.0    |
| Jan-26 | 20.0   | 21.0    |
</details>

Source: EPFR  
BofA GLOBAL RESEARCH

Exhibit 8: Active funds reduce their UW positions on Taiwan  
Active and passive global EM funds' exposure to Taiwan stocks (%)  
![](images/9efa4ecc5e097b68e87c844319e45248848172635b97201e964292f95dacd000.jpg)

<details>
<summary>line chart</summary>

| Date   | Active | Passive |
|--------|--------|---------|
| Jan-21 | 11.5   | 14.0    |
| Jul-21 | 12.5   | 15.5    |
| Jan-22 | 14.0   | 16.5    |
| Jul-22 | 11.0   | 15.0    |
| Jan-23 | 13.0   | 17.0    |
| Jul-23 | 13.5   | 16.5    |
| Jan-24 | 15.0   | 18.0    |
| Jul-24 | 17.0   | 20.0    |
| Jan-25 | 18.0   | 19.5    |
| Jul-25 | 16.0   | 18.5    |
| Jan-26 | 22.0   | 23.0    |
</details>

Exhibit 9: Active funds 

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
