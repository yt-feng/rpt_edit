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
# JPM

## SK Telecom

## AI factory build-out emerges as next catalyst; upgrade to OW

SKT's share price has pulled back 27% from the latest peak (vs. KOSPI's -22%), reflecting investors' rationalized view on the Anthropic proxy trade, in our view. We expect volatility tied to the proxy trade to moderate as optimism appears largely priced in. We are instead focusing on SKT's growing investment case as an AI datacenter ("AI factory") player after its aggressive capacity expansion plan. We see room for meaningful progress, supported by SK Group's strong position across the global AI value chain—an increasingly important catalyst for the stock. We upgrade to OW and raise our SoTP-based Dec-27 PT by 38% to W110,000 (23% potential upside) on reflecting W3T value for the <0.3% stake in Anthropic and W3T for the AI DC business (plus submarine cable) (previous PT Dec-26 W80,000).

\- SKT's AI-led rerating should continue to set it apart from incumbent telco peers. The stock is up 69% YTD (vs. KT/LGU+ 0%/-2%; -27% from the peak in Jun-26), driven by AI-related strategy, fundamentals, and sentiment. The key swing factor has been the “Anthropic proxy” trade (see our prior note): SKT owns <0.3% of Anthropic, which we value at \$2.9B (W4.3T) based on the latest funding round valuation of \$965B in May-26 (link). This compares with SKT's W8T YTD market-cap uplift (or W15T from the June peak), suggesting residual over-exuberance around the implied value of the Anthropic stake. That said, we expect volatility tied to the proxy trade to moderate as optimism appears to be largely priced in.

\- SKT's AI exposure is becoming increasingly tangible across government-led initiatives, infrastructure and strategic stakes: 1) its consortium was selected as one of four finalists in Korea's Sovereign AI competition (alongside LG AI Research, Upstage and Motif Technologies), which—while monetization remains unclear—could open mid-to-long-term B2G AI opportunities; 2) on infrastructure, SKT is partnering with AWS to build a large-scale AI datacenter in Ulsan targeting 100MW by 2029 (with potential longer-term expansion to 1GW) and has also outlined broader AI DC ambitions of 5GW by 2035 and 15GW longer term; 3) in AI semis, SKT has indirect exposure to domestic fabless chipmaker Rebellion via its $62.5\%$ stake in SAPEON INC, which holds $26\%$ of Rebellion (preparing for an IPO in 1H27E; source: Digitimes).

\- SKT appears to be pursuing an aggressive AI datacenter build-out, with SK Broadband (SKBB; 100% owned) expected to be a key execution arm for the group's “AI DC factory” strategy. Following Chairman Chey’s long-term plan that includes W1,000T earmarked for AI datacenters, SKT/SKBB recently outlined 5GW of AI DC capacity for 2029–2035 (including the Ulsan project) and 15GW longer term. Given the scale of funding required (e.g., \~W75T per 1GW), we expect SKT to lean on project financing and capital from global big-tech partners to minimize its own burden. Potential AI token end-demand sources span global AI pure plays (e.g., OpenAI, Anthropic), hyperscalers (e.g., Amazon, Microsoft, Google), domestic enterprises/government/institutes, and SK Group captive demand.

\- AI DC upside is not yet fully reflected in SKT's valuation, and we are

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

## ▲Overweight

Previous: Neutral

See page 9 for analyst certification and important disclosures, including non-US analyst disclosures.

017670.KS, 017670 KS
Price (16 Jul 26):W89,400

▲ Price Target (Dec-27):W110,000
Prior (Dec-26):W80,000

## Internet and Telco

Stanley Yang AC
(82-2) 758-5712
stanley.yang@JPM.com

Benjamin Kim
(82-2) 758-5580
benjamin.kim@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

<table><tr><td colspan="4">Key Changes (FYE Dec)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EBIT - 26E (W bn)</td><td>1,852</td><td>1,932</td><td>4.3%</td></tr><tr><td>Adj. EBIT - 27E (W bn)</td><td>1,955</td><td>2,063</td><td>5.5%</td></tr></table>

## Quarterly Forecasts (FYE Dec)

<table><tr><td colspan="4">Adj. EPS (W)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>1,698</td><td>1,486A</td><td>1,800</td></tr><tr><td>Q2</td><td>391</td><td>1,634</td><td>1,778</td></tr><tr><td>Q3</td><td>(783)</td><td>1,452</td><td>1,582</td></tr><tr><td>Q4</td><td>456</td><td>1,069</td><td>1,120</td></tr><tr><td>FY</td><td>1,762</td><td>5,641</td><td>6,279</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>60</td><td>42</td><td>42</td><td>37</td><td>28</td></tr><tr><td>Growth</td><td>38</td><td>94</td><td>46</td><td>48</td><td>85</td></tr><tr><td>Momentum</td><td>29</td><td>91</td><td>32</td><td>72</td><td>56</td></tr><tr><td>Quality</td><td>57</td><td>66</td><td>13</td><td>18</td><td>55</td></tr><tr><td>Low Vol</td><td>7</td><td>2</td><td>1</td><td>91</td><td>2</td></tr><tr><td>ESGQ</td><td>96</td><td>97</td><td>21</td><td>-</td><td>22</td></tr></table>

Price Performance  
![](images/116793eacd9a061a5f7fc2ec083649fe1a4e796c5ecf8521739bb22ea83a30d1.jpg)

— 017670.KS Price (W) — KOSPI (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>67.1%</td><td>-11.2%</td><td>-7.4%</td><td>59.9%</td></tr><tr><td>Rel</td><td>5.3%</td><td>10.6%</td><td>-17.0%</td><td>-54.1%</td></tr></table>

Company Data

<table><tr><td>Shares O/S (mn)</td><td>219</td></tr><tr><td>52-week range (W)</td><td>140,300-51,400</td></tr><tr><td>Market cap ($ mn)</td><td>13,166</td></tr><tr><td>Exchange rate</td><td>1,486</td></tr><tr><td>Free float (%)</td><td>61.8%</td></tr><tr><td>3M ADV (th)</td><td>2,590.0</td></tr><tr><td>3M ADV ($ mn)</td><td>183.2</td></tr><tr><td>Volatility (90 Day)</td><td>68</td></tr><tr><td>Index</td><td>KOSPI</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>16|11|4</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>W in billions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td></tr><tr><td colspan="4">Financial Estimates</td></tr><tr><td>Revenue</td><td>17,099</td><td>17,655</td><td>17,892</td></tr><tr><td>Adj. EBITDA</td><td>4,663</td><td>5,497</td><td>5,670</td></tr><tr><td>Adj. EBIT</td><td>1,073</td><td>1,932</td><td>2,063</td></tr><tr><td>Adj. net income</td><td>375</td><td>1,201</td><td>1,337</td></tr><tr><td>Adj. EPS</td><td>1,762</td><td>5,641</td><td>6,279</td></tr><tr><td>Reported EPS</td><td>1,762</td><td>5,641</td><td>6,279</td></tr><tr><td>BBG EPS</td><td>1,764</td><td>5,595</td><td>6,088</td></tr><tr><td>Cashflow from operations</td><td>3,924</td><td>4,666</td><td>4,834</td></tr><tr><td>FCFF</td><td>1,136</td><td>1,798</td><td>1,895</td></tr><tr><td colspan="4">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>(4.7%)</td><td>3.2%</td><td>1.3%</td></tr><tr><td>EBITDA margin</td><td>27.3%</td><td>31.1%</td><td>31.7%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>(15.5%)</td><td>17.9%</td><td>3.1%</td></tr><tr><td>EBIT margin</td><td>6.3%</td><td>10.9%</td><td>11.5%</td></tr><tr><td>Net margin</td><td>2.2%</td><td>6.8%</td><td>7.5%</td></tr><tr><td>Adj. EPS growth</td><td>(73.0%)</td><td>220.2%</td><td>11.3%</td></tr><tr><td colspan="4">Ratios</td></tr><tr><td>Adj. tax rate</td><td>28.8%</td><td>27.0%</td><td>25.0%</td></tr><tr><td>Interest cover</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net debt/Equity</td><td>0.7</td><td>0.7</td><td>0.6</td></tr><tr><td>Net debt/EBITDA</td><td>2.0</td><td>1.7</td><td>1.7</td></tr><tr><td>ROCE</td><td>3.4%</td><td>5.8%</td><td>6.1%</td></tr><tr><td>ROE</td><td>3.1%</td><td>8.9%</td><td>9.1%</td></tr><tr><td colspan="4">Valuation</td></tr><tr><td>FCFF yield</td><td>6.0%</td><td>9.4%</td><td>10.0%</td></tr><tr><td>Dividend yield</td><td>1.9%</td><td>4.0%</td><td>4.0%</td></tr><tr><td>EV/Revenue</td><td>1.2</td><td>1.2</td><td>1.2</td></tr><tr><td>EV/EBITDA</td><td>4.6</td><td>3.9</td><td>3.8</td></tr><tr><td>Adj. P/E</td><td>50.7</td><td>15.8</td><td>14.2</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

SKT's share price has pulled back 27% from the latest peak (vs. KOSPI's -22%), reflecting investors' rationalized view on the Anthropic proxy trade, in our view. We expect volatility tied to the proxy trade to moderate as optimism appears to be largely priced in. We are instead focusing on SKT's growing investment case as an AI datacenter (“AI factory”) player after its aggressive capacity expansion plan. We see room for meaningful progress, supported by SK Group's strong position across the global AI value chain—an increasingly important catalyst for the stock. We upgrade to OW and raise our SoTP-based PT by 38% to W110,000 (23% potential upside) on reflecting W3T value for the <0.3% stake in Anthropic and W3T for the AI DC business (plus submarine cable).

## Valuation

Our Dec-27 PT of W110,000 (previously W80,000) is based on a SoTP valuation: (1) a DCF for the telco business, (2) the latest funding-round valuation for SKT's Anthropic stake, and (3) an EV/EBIT multiple for the AI datacenter business.

![](images/fc887d7bae64617aa05374baa91884f01bdaf886d56403887594c860110c4f04.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.48</td><td>0.42</td></tr><tr><td>Region: Korea</td><td>0.10</td><td>0.20</td></tr><tr><td colspan="3">Macro:</td></tr><tr><td>Generic 1st &#x27;CO&#x27; Future</td><td>-0.34</td><td>-0.21</td></tr><tr><td>JPM GBI-EM Global Div</td><td>0.30</td><td>0.19</td></tr><tr><td>JPM China A-shares Sentiment</td><td>-0.12</td><td>-0.16</td></tr><tr><td colspan="3">Quant Styles:</td></tr><tr><td>LowVol</td><td>0.12</td><td>0.17</td></tr><tr><td>DivYld</td><td>0.07</td><td>0.11</td></tr><tr><td>Value</td><td>0.11</td><td>0.10</td></tr></table>

incrementally more constructive on the strategy given (1) SK Group's strong positioning across the global AI value chain, (2) rising investment interest from global AI service and infrastructure players in Korea as a potential AI ecosystem hub, (3) a funding approach skewed toward external capital (project finance/partners), and (4) attractive unit economics (c. 15–20% OPM). For context, versus CoreWeave's long-term target (active capacity >1GW, secured >3.5GW by 2027 and >8GW by 2030), we assume SKT reaches \~0.5GW of active AI DC capacity by 2030–2031. On this basis, we estimate W3T of AI DC (plus submarine cable) value, applying a 6.6x EV/EBIT multiple (2030\~2031E, in line with CoreWeave, based on Bloomberg consensus estimates).

\- SOTP-based PT increased to W110,000 (23% potential upside): We move to a SoTP valuation framework comprising: 1) a DCF-derived value of W17.6T value for the core telco business (wireless and fixed line, including legacy datacenter operation), 2) W3T for <0.3% stake of Anthropic (a 30% NAV discount), and 3) W3T for the AI DC business (plus submarine cable), valued at 6.6x EV/EBIT on 2030\~2031E earnings.

Figure 1: SK Telecom: Share performance since Jan-25  
![](images/78ef5c7dae9c84a52fee1fd44b87895cf05306eab4346946025d1373ae861298.jpg)  
Source: Bloomberg Finance L.P.

Figure 2: SK Telecom: YTD share performance
2026/1/1 indexed as 100  
![](images/618e866963cb7661172e28a862baff944006809894a24c123dc43d22dc637625.jpg)  
Source: Bloomberg Finance L.P.

Figure 3: Anthropic valuation history  
![](images/9e46fc346fc4c7cbe76b7ef0820266ba082476f40addd4dbfe9bf79f23ed524a.jpg)  
Source: News articles (MK News, Han Kyung, Business Insider and others), Company data.
Note: July-2026 data based on implied valuation on the secondary market, not a funding round (link).

Table 2: SK Telecom: AI datacenter capacity plan

<table><tr><td>Timeline</td><td>Target Capacity</td><td>Key Plan</td></tr><tr><td>By Nov.2027</td><td>40MW</td><td>Buildout of Ulsan AI datacenter in partnership with AWS</td></tr><tr><td>By 2029</td><td>100MW</td><td>1st phase expansion of the Ulsan datacenter</td></tr><tr><td>By 2035</td><td>5GW</td><td>Scale Ulsan to ~1GW, secure ~1GW in the Yeongnam region, and additional data center capacity</td></tr><tr><td>Long-term</td><td>15GW</td><td>Complete a 15GW scale AI datacenter infrastructure</td></tr></table>

Source: Local news (MK News, Han Kyung, and others), Company data.

Table 3: SK Telecom: SoTP valuation
Wtrn  
Figure 4: CoreWeave: EV/EBIT valuation  
![](images/d66230f2de7275fa597bb6f93202a790dc1cd57125f0d9e724219c2988dbf9de.jpg)  
Source: Bloomberg Finance L.P.

<table><tr><td></td><td>Value</td></tr><tr><td>Total equity value</td><td>23.6</td></tr><tr><td>(1) Telco value (DCF)</td><td>17.6</td></tr><tr><td>(2) Anthropic stake value</td><td>3.0</td></tr><tr><td>Latest funding valuation</td><td>1,448</td></tr><tr><td>% of stake</td><td>0.3%</td></tr><tr><td>Stake value</td><td>4.3</td></tr><tr><td>% NAV discount</td><td>-30%</td></tr><tr><td>(3) AI DC value (0.5GW by 2030-2031E)</td><td>3.0</td></tr><tr><td>Rev (incd. submarine cable)</td><td>3.0</td></tr><tr><td>% EBIT margin</td><td>15%</td></tr><tr><td>EBIT</td><td>0.45</td></tr><tr><td>Target EV/EBIT multiple</td><td>6.6x</td></tr><tr><td>Outstanding shares (in mn)</td><td>214.8</td></tr><tr><td>Target price (W)</td><td>110,000</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates.

Table 4: SK Telecom: Telco business DCF valuation
Wbn

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>EBIT (1- tax)</td><td>1,082</td><td>1,257</td><td>1,367</td><td>1,422</td><td>805</td><td>1,449</td><td>1,547</td><td></td><td></td><td></td></tr><tr><td>Net interest</td><td>-243</td><td>-270</td><td>-320</td><td>-316</td><td>-310</td><td>-329</td><td>-298</td><td></td><td></td><td></td></tr><tr><td>D&amp;A</td><td>3,820</td><td>3,755</td><td>3,750</td><td>3,695</td><td>3,590</td><td>3,565</td><td>3,607</td><td></td><td></td><td></td></tr><tr><td>CapEx</td><td>-3,307</td><td>-3,046</td><td>-3,081</td><td>-2,559</td><td>-2,323</td><td>-2,403</td><td>-2,474</td><td></td><td></td><td></td></tr><tr><td>Spectrum payment</td><td>-465</td><td>-465</td><td>-465</td><td>-465</td><td>-465</td><td>-465</td><td>-465</td><td></td><td></td><td></td></tr><tr><td>NWC &amp; Others</td><td>373</td><td>416</td><td>150</td><td>286</td><td>-161</td><td>-19</td><td>-22</td><td></td><td></td><td></td></tr><tr><td>Consolidated FCF</td><td>1,259</td><td>1,648</td><td>1,402</td><td>2,063</td><td>1,136</td><td>1,798</td><td>1,895</td><td>1,989</td><td>2,089</td><td>2,193</td></tr><tr><td>Cost of Debt</td><td>4.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cost of Equity</td><td>11.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tax rate</td><td>24.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Risk free rate</td><td>4.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Market risk premium</td><td>7.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Beta</td><td>1.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Debt/Capital</td><td>44%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Equity/Capital</td><td>56%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WACC</td><td>8.4%</td><td></td><td></td><td></td><td></td><

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
