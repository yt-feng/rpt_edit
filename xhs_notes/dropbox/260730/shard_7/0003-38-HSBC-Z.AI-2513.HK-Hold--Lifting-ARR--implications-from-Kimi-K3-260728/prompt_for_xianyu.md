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
Z.AI (2513 HK)

Hold: Lifting ARR; implications from Kimi K3

\- Raise ARR assumptions; cut TP on lower margins in long term amid competition and higher share count

\- Competition intensifies, but Z.ai can potentially catch up with higher parameter size models

\- Maintain Hold, cut TP to HKD1,500 (from HKD1,900)

Estimate, TP changes: Z.ai (Zhipu) ARR reached USD1bn in July (per Bloomberg News on 17 July 2026), ahead of the guidance by December 2026. We raise ARR estimates to USD2bn (from USD1bn) in December 2026 and USD6.5bn (from USD2.4bn) in December 2027. Though the revenue mix shift to lower-margin API will dilute margins, we expect Z.ai to turn profitable in 2027 instead of 2028. However, we lower our TP to HKD1,500 (from HKD1,900), factoring in lower FCF assumptions to reflect more intense competition in pricing, higher share count after the HKD31bn H-share follow-on offerings in July 2026, and changes in exchange rate (USD-HKD). Our TP implies 14x P/ARR in December 2027 vs Anthropic's 8x (based on HSBC's global tech platforms team estimates on Anthropic's ARR and USD1.2trn valuation in secondary market transactions (Business Insider, 9 July 2026)). The premium is justified by faster ARR growth of $220\%$ for Z.ai vs Anthropic $(50\%)$ . Maintain Hold.

Implications from the Kimi K3 launch: (1) Scaling law continues: We think K3's intelligence leap is due to higher parameter size (rises from 1trn for K2.7 to 2.8trn). Z.ai could potentially catch up with the next model as GLM-5.2 only has 744bn parameters. (2) Competition intensifies: K3's launch suggests that Chinese open weight models could step up with 3trn parameter size models in 3Q26, including MiniMax and DeepSeek. We notice the iteration frequency from frontier labs has further accelerated in recent weeks, e.g., five leading US players (Anthropic, OpenAI, Google, SpaceXAI, Meta) all released model updates in July to date (exhibit 2). This shows that leadership in model capability has turned more temporary and frontier labs need to stay invested. (3) Computing power matters for ARR: K3 has much slower token throughput than peers and paused new to-C subscription two days after the launch. This suggests it lacks computing power. On the other hand, Z.ai has begun operating a 1GW data center (several clusters, each with over 10k domestic chips), with breakthrough in using domestic chips for inferencing (Bloomberg News, 21 July 2026) buffering compute power constraint. In addition, per Sina News on 21 July 2026, Z.ai acquired XCore Sigma (a heterogeneous AI compute software provider) to improve utilization of various types of chips. We believe these measures can support Z.ai to grow its ARR continuously amid robust user demand.

Catalysts and risks: (1) Launch of a new GLM in 3Q26 (+ve), (2) model iterations from competitors (-ve), (3) geopolitical risks related to potential ban of Chinese frontier models in the US market (-ve), (4) lock-up expiry (-ve): c38% of Z.ai's shares could be unlocked in early January 2027, and (5) fundraising/IPO of frontier labs could reduce the scarcity premium.

## Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

## Equities

Internet Software & Services

China

![](images/54992c5983a1d7154d7a50bb68d80c5e6ac2857888363817f138f3e71dc5672a.jpg)

MAINTAIN HOLD

TARGET PRICE (HKD)

PREVIOUS TARGET (HKD)

1,500.00

1,900.00

SHARE PRICE (HKD) UPSIDE/DOWNSIDE

1,281.00 +17.1%

(as of 27 Jul 2026)

## MARKET DATA

Market cap (HKDm) 586,584
Market cap (USDm) 74,796
3m ADTV (USDm) 648

<table><tr><td>Free float</td><td>10%</td></tr><tr><td>BBG</td><td>2513 HK</td></tr><tr><td>RIC</td><td>2513.HK</td></tr></table>

FINANCIALS AND RATIOS (CNY)

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>HSBC EPS</td><td>-19.95</td><td>-5.37</td><td>3.72</td><td>18.83</td></tr><tr><td>HSBC EPS (prev)</td><td>-19.95</td><td>-7.08</td><td>-4.46</td><td>0.99</td></tr><tr><td>Change (%)</td><td>0.0</td><td>24.2</td><td>nm</td><td>1,799.8</td></tr><tr><td>Consensus EPS</td><td>-10.80</td><td>-9.70</td><td>-8.81</td><td>-3.04</td></tr><tr><td>PE (x)</td><td>nm</td><td>nm</td><td>297.7</td><td>58.7</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>EV/EBITDA (x)</td><td>nm</td><td>nm</td><td>198.6</td><td>34.6</td></tr><tr><td>ROE (%)</td><td>52.8</td><td>-19.2</td><td>5.5</td><td>25.8</td></tr></table>

52-WEEK PRICE (HKD)  
![](images/069f65e24bb345fbf4ef0e645db479c6187e01343a38134e3b1bec7f812e490f.jpg)  
Source: LSEG IBES, HSBC estimates

## Ritchie Sun\*, CFA

Analyst, Internet Research
The Hongkong and Shanghai Banking Corporation Limited
ritchie.k.h.sun@hsbc.com.hk
+852 2822 4392

## Charlene Liu\*

Head of Internet and Gaming Research, Asia Pacific  
The Hongkong and Shanghai Banking Corporation  
Limited, Singapore Branch  
charlene.r.liu@hsbc.com.sg  
+65 6658 0615

## Peishan Wang\*

Analyst, Internet Research
The Hongkong and Shanghai Banking Corporation Limited
peishan.wang@hsbc.com.hk
+852 3941 7008

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited

## View HSBC Global Investment Research at:

https://www.research.hsbc.com

## Financials & valuation: Z.AI

Financial statements

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Profit &amp; loss summary (CNYm)</td></tr><tr><td>Revenue</td><td>724</td><td>7,206</td><td>29,176</td><td>66,237</td></tr><tr><td>EBITDA</td><td>-3,517</td><td>-3,186</td><td>2,291</td><td>12,687</td></tr><tr><td>Depreciation &amp; amortisation</td><td>-270</td><td>-721</td><td>-2,042</td><td>-2,981</td></tr><tr><td>Operating profit/EBIT</td><td>-3,787</td><td>-3,906</td><td>249</td><td>9,706</td></tr><tr><td>Net interest</td><td>-74</td><td>-84</td><td>-84</td><td>-84</td></tr><tr><td>PBT</td><td>-4,718</td><td>-3,930</td><td>229</td><td>9,690</td></tr><tr><td>HSBC PBT</td><td>-4,718</td><td>-3,930</td><td>229</td><td>9,690</td></tr><tr><td>Taxation</td><td>0</td><td>0</td><td>0</td><td>-969</td></tr><tr><td>Net profit</td><td>-1,918</td><td>-3,910</td><td>249</td><td>8,741</td></tr><tr><td>HSBC net profit</td><td>-3,182</td><td>-2,628</td><td>2,001</td><td>11,154</td></tr><tr><td colspan="5">Cash flow summary (CNYm)</td></tr><tr><td>Cash flow from operations</td><td>-2,246</td><td>-690</td><td>6,300</td><td>19,311</td></tr><tr><td>Capex</td><td>-23</td><td>-735</td><td>-2,013</td><td>-3,113</td></tr><tr><td>Cash flow from investment</td><td>-376</td><td>-735</td><td>-2,013</td><td>-3,113</td></tr><tr><td>Dividends</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Change in net debt</td><td>-98</td><td>-44,694</td><td>-4,281</td><td>-16,192</td></tr><tr><td>FCF equity</td><td>-2,269</td><td>-1,425</td><td>4,287</td><td>16,198</td></tr><tr><td colspan="5">Balance sheet summary (CNYm)</td></tr><tr><td>Intangible fixed assets</td><td>90</td><td>90</td><td>90</td><td>90</td></tr><tr><td>Tangible fixed assets</td><td>854</td><td>868</td><td>839</td><td>972</td></tr><tr><td>Current assets</td><td>3,571</td><td>48,395</td><td>52,896</td><td>69,028</td></tr><tr><td>Cash &amp; others</td><td>2,745</td><td>47,440</td><td>51,721</td><td>67,913</td></tr><tr><td>Total assets</td><td>4,854</td><td>49,753</td><td>54,288</td><td>70,621</td></tr><tr><td>Operating liabilities</td><td>12,275</td><td>13,598</td><td>16,054</td><td>21,154</td></tr><tr><td>Gross debt</td><td>605</td><td>605</td><td>605</td><td>605</td></tr><tr><td>Net debt</td><td>-2,140</td><td>-46,835</td><td>-51,116</td><td>-67,308</td></tr><tr><td>Shareholders&#x27; funds</td><td>-8,093</td><td>35,508</td><td>37,608</td><td>48,861</td></tr><tr><td>Invested capital</td><td>-10,505</td><td>-11,683</td><td>-13,950</td><td>-18,977</td></tr></table>

Ratio, growth and per share analysis

## Hold

Valuation data

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td>EV/sales</td><td>695.9</td><td>63.7</td><td>15.6</td><td>6.6</td></tr><tr><td>EV/EBITDA</td><td>nm</td><td>nm</td><td>198.6</td><td>34.6</td></tr><tr><td>EV/IC</td><td></td><td></td><td></td><td></td></tr><tr><td>PE*</td><td>nm</td><td>nm</td><td>297.7</td><td>58.7</td></tr><tr><td>PB</td><td></td><td>15.3</td><td>15.8</td><td>13.4</td></tr><tr><td>FCF yield (%)</td><td>-0.4</td><td>-0.3</td><td>0.8</td><td>3.2</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

\* Based on HSBC EPS (diluted)

ESG metrics

<table><tr><td>Environmental Indicators</td><td>12/2025a</td><td>Governance Indicators</td><td>12/2025a</td></tr><tr><td>GHG emission intensity*</td><td>5.9</td><td>No. of board members</td><td>9</td></tr><tr><td>Energy intensity*</td><td>11.2</td><td>Average board tenure (years)</td><td>1.1</td></tr><tr><td>CO2 reduction policy</td><td>Yes</td><td>Female board members (%)</td><td>22.2</td></tr><tr><td>Social Indicators</td><td>12/2025a</td><td>Board members independence (%)</td><td>33.3</td></tr><tr><td>Employee costs as % of revenues</td><td>188.2</td><td></td><td></td></tr><tr><td>Employee turnover (%)</td><td>n.a</td><td></td><td></td></tr><tr><td>Diversity policy</td><td>Yes</td><td></td><td></td></tr></table>

<table><tr><td>Year to</td><td>12/2025a</td><td>12/2026e</td><td>12/2027e</td><td>12/2028e</td></tr><tr><td colspan="5">Y-o-y % change</td></tr><tr><td>Revenue</td><td>131.9</td><td>894.9</td><td>304.9</td><td>127.0</td></tr><tr><td>EBITDA</td><td></td><td></td><td></td><td>453.8</td></tr><tr><td>Operating profit</td><td></td><td></td><td></td><td>3,804.0</td></tr><tr><td>PBT</td><td></td><td></td><td></td><td>4,131.7</td></tr><tr><td>HSBC EPS</td><td></td><td></td><td></td><td>406.8</td></tr><tr><td colspan="5">Ratios (%)</td></tr><tr><td>Revenue/IC (x)</td><td>-0.1</td><td>-0.6</td><td>-2.3</td><td>-4.0</td></tr><tr><td>ROIC</td><td>45.1</td><td>35.2</td><td>-1.9</td><td>-53.1</td></tr><tr><td>ROE</td><td>52.8</td><td>-19.2</td><td>5.5</td><td>25.8</td></tr><tr><td>ROA</td><td>-102.2</td><td>-14.4</td><td>0.4</td><td>14.0</td></tr><tr><td>EBITDA margin</td><td>-485.5</td><td>-44.2</td><td>7.9</td><td>19.2</td></tr><tr><td>Operating profit margin</td><td>-522.8</td><td>-54.2</td><td>0.9</td><td>14.7</td></tr><tr><td>EBITDA/net interest (x)</td><td></td><td></td><td>27.2</td><td>150.4</td></tr><tr><td>Net debt/equity</td><td>0.0</td><td>-132.0</td><td>-136.1</td><td>-138.0</td></tr><tr><td>Net debt/EBITDA (x)</td><td>0.6</td><td>14.7</td><td>-22.3</td><td>-5.3</td></tr><tr><td colspan="5">CF from operations/net debt</td></tr><tr><td colspan="5">Per share data (CNY)</td></tr><tr><td>EPS Rep (diluted)</td><td>-12.03</td><td>-7.99</td><td>0.46</td><td>14.76</td></tr><tr><td>HSBC EPS (diluted)</td><td>-19.95</td><td>-5.37</td><td>3.72</td><td>18.83</td></tr><tr><td>DPS</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Book value</td><td>-50.73</td><td>72.53</td><td>69.84</td><td>82.48</td></tr></table>

Source: Company data, HSBC  
\* GHG intensity and energy intensity are measured in kg and kWh respectively against revenue in USD '000s

<table><tr><td colspan="2">Issuer information</td></tr><tr><td>Share price (HKD)</td><td>1,281.00</td></tr><tr><td>Target price (HKD)</td><td>1,500.00</td></tr><tr><td>RIC (Equity)</td><td>2513.HK</td></tr><tr><td>Bloomberg (Equity)</td><td>2513 HK</td></tr><tr><td>Market cap (USDm)</td><td>74,796</td></tr></table>

<table><tr><td colspan="2">Free float</td><td>4%</td></tr><tr><td>Sector</td><td colspan="2">Internet Software &amp; Services</td></tr><tr><td>Country/Region</td><td></td><td>China</td></tr><tr><td>Analyst</td><td></td><td>Ritchie Sun, CFA</td></tr><tr><td>Contact</td><td></td><td>+852 2822 4392</td></tr></table>

Price relative  
![](images/d04a5a70145cd7079ef3763ff5ae9e58e3841b0d4aec97ce7b5ca227952faa7b.jpg)  
Source: HSBC  
Note: Priced at close of 27 Jul 2026

## Competition

Exhibit 1: Comparison between Z.ai and Moonshot on key metrics

<table><tr><td>Company</td><td>Z.ai</td><td>Moonshot</td></tr><tr><td colspan="3">Key model metrics</td></tr><tr><td>Flagship model</td><td>GLM-5.2</td><td>Kimi K3</td></tr><tr><td>Release date</td><td>13-Jun-26</td><td>16-Jul-26</td></tr><tr><td>Core architecture</td><td>DeepSeek Sparse Attention (DSA) + IndexShare</td><td>Kimi Delta Attention (KDA) + Attention Residuals (AttnRes) + Stable LatentMoE</td></tr><tr><td>Total parameters (bn)</td><td>744</td><td>2,800</td></tr><tr><td>Activated parameters (bn)</td><td>40</td><td>104</td></tr><tr><td>Activation ratio (%)</td><td>5.4%</td><td>3.7%</td></tr><tr><td>Experts</td><td>8 out of 256 experts</td><td>16 out of 896 experts</td></tr><tr><td>Training data scale (trn tokens)</td><td>30</td><td>n.a.</td></tr><tr><td>Context window (m)</td><td>1</td><td>1</td></tr><tr><td>Modality</td><td>Text</td><td>Native multi-modal</td></tr><tr><td colspan="3">Cost vs. Intelligence vs. Speed</td></tr><tr><td colspan="3">API pricing (USD)</td></tr><tr><td>Input (Cache hit)</td><td>0.26</td><td>0.3</td></tr><tr><td>Input (Cache miss)</td><td>1.4</td><td>3</td></tr><tr><td>Output</td><td>4.4</td><td>15</td></tr><tr><td>Cost per task (USD)</td><td>0.32</td><td>0.72</td></tr><tr><td>Artificial Analysis Intelligence Index</td><td>51</td><td>57</td></tr><tr><td>Output speed (tps)</td><td>211</td><td>33</td></tr><tr><td colspan="3">Financial metrics</td></tr><tr><td>Latest ARR (USDbn)</td><td>1</td><td>0.3</td></tr><tr><td>Latest ARR date</td><td>Jul-26</td><td>Jun-26</td></tr><tr><td>Latest valuation (USDbn)</td><td>76</td><td>50</td></tr><tr><td>P/ARR (x)</td><td>76</td><td>167</td></tr></table>

Source: Company data, Bloomberg, Artificial Analysis (data as of 27 July 2026). Note: share price is as of 27 July 2026

Exhibit 2: More companies have launched model iterations in July 2026

<table><tr><td rowspan="2"></td><td colspan="20">Major product launch since 2025</td></tr><tr><td>Launch time</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Jul-26</td></tr><tr><td rowspan="13">Foundation model</td><td>GLM</td><td>Realtime</td><td colspan="5">Z1-Rumination</td><td>4.5</td><td>4.5v</td><td>4.6</td><td></td><td></td><td>4.7</td><td></td><td>5.0</td><td>5.0 Turbo</td><td>5.1/5v-turbo</td><td>5.1-highspeed</td><td>5.2</td><td></td></tr><tr><td>Opus</td><td></td><td></td><td></td><td></td><td>4</td><td></td><td></td><td>4.1</td><td></td><td></td><td>4.5</td><td></td><td></td><td>4.6</td><td></td><td>4.7</td><td>4.8</td><td></td><td>5</td></tr><tr><td>Fable</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Fable 5</td><td></td></tr><tr><td>Sonnet</td><td></td><td></td><td></td><td></td><td>4</td><td></td><td></td><td></td><td>4.5</td><td></td><td></td><td></td><td></td><td>4.6</td><td></td><td></td><td></td><td>5</td><td></td></tr><tr><td>Gemini</td><td></td><td></td><td>2.5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td><td>3.1</td><td></td><td></td><td>3.5 flash</td><td></td><td>3.6 flash</td></tr><tr><td>GPT</td><td></td><td>4.5</td><td></td><td></td><td></td><td></td><td></td><td>5</td><td></td><td></td><td>5.1</td><td>5.2</td><td></td><td>5.3-Codex</td>

[中间内容因长度限制已省略]

nal Investor as defined in SFA. The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch accepts legal responsibility for the contents of reports. This publication is not a prospectus as defined in the SFA. It may not be further distributed in whole or in part for any purpose. The Hongkong and Shanghai Banking Corporation Limited Singapore Branch is regulated by the Monetary Authority of Singapore. Recipients in Singapore should contact a "Hongkong and Shanghai Banking Corporation Limited, Singapore Branch" representative in respect of any matters arising from, or in connection with this report. Please refer to The Hongkong and Shanghai Banking Corporation Limited Singapore Branch's website at www.business.hsbc.com.sg for contact details. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. Should you wish to use AI technology (computational, statistical, machine-learning or other artificial intelligence techniques to infer or learn from data to find patterns, take actions, make decisions, or generate output) to help you analyse, summarise or evaluate this publication and/or any other research materials provided to you by HSBC, you shall seek HSBC consent in advance of any such use and not upload this publication and/or any other research materials produced by HSBC to an AI system or otherwise use AI technology in connection with the research services HSBC provides to you without our consent.

© Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.
"""
