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
# China Supply Growth to Rapidly Eliminate Shortage; D/G to HOLD

YOFC has risen \~14x in the past 12 months due to AI-driven growth in demand for OF and optical modules. We estimate its OF ASP will rise 203% in 2026 to Rmb146/fkm, \~18% above the previous peak in 2018. Its preform+OF GM is forecast to rise to 86% in 2026 (48% in 2025). But we estimate global capacity will expand 69% by 2028 (100% in China), and more could come. Thus 2026 ASP would likely be the peak. Our SOTP valuation indicates limited upside. D/G to HOLD.

AI and military conflicts have boosted demand for OF. Optical fiber (OF) is a commodity. In 2025, China accounted for 56%/68% of global preform output/capacity. Global demand has taken off driven by 1) AI data center demand mainly in the US, and 2) use of drones in military conflicts in Ukraine and Iran (which could drop in 2027). In 2H25, the US AI supply chain faced a significant OF shortage as the western OF industry's capacity has been stagnant over the past 6 years, but the US was unwilling to buy from China. As demand continues to grow, we believe US players will have no choice but to start buying from China. YOFC is the largest OF maker globally with a 17% capacity share. Our industry checks indicate GOOG has qualified YOFC's OF, but the purchase from YOFC may not be direct.

ASP and GM to soar, but supply will increase significantly in 2027/8 esp in China. Datacom had been 10% of OF demand (80% telecom) until 2024. We est datacom will be 43% of demand in 2026 rising to 55% in 2027, implying 131%/65% YoY growth. Oversupply in China drove YOFC's OF ASP down to Rmb31/fkm in 2020. We est it gradually recovered to Rmb44 in 2025. Our industry checks suggest ASP has risen above Rmb100 in 2Q26, and some new DC-centric OF products (eg, G657A1/A2) could go above Rmb150/fkm even in LTAs. Since the unit cost of production has not changed materially, we est YOFC's GM on its preform+OF segment will rise from 48% in 2025 to 86% in 2026. Including low-margin cable products, YOFC's blended GM for its OF business is forecast to rise from 31% in 2025 to 53%. Given high operating leverage, we forecast a 10x YoY rise in EPS this year to Rmb11.44, implying 11x 2026E PE currently.

Significant industry capacity expansion would likely make 2026/27 profit the cyclical peak. Based on announced expansion plans and 12-18 months of buildout time, we estimate global capacity will increase 69% from now to 2028, with China's capacity doubling. YOFC is the only major player that has not discussed any expansion plan. Although we see it as a disciplined decision, YOFC could thus risk losing market share. Strong demand has also attracted M&A. LY iTech (002600 CH, HOLD) announced its acquisition of Futong, a financially distressed preform +OF maker. We est global capacity will cover 87%/85% of demand in 2027/28, indicating ASP could peak in 2026. Our new PT is based on an avg SOTP, with the OF business valued at the avg of 3.5x PB (2018 peak) and 14.1x 2027E PE (2sd above LT avg until mid-2025), and implies only 9% upside. D/G to HOLD.

<table><tr><td>FY (Dec)</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Rev. (MM)</td><td>14,252.0</td><td>27,944.0</td><td>29,353.0</td><td>26,283.0</td></tr><tr><td>Gross Profit Margin (%)</td><td>30.7</td><td>52.6</td><td>54.2</td><td>50.5</td></tr><tr><td>Net Profit</td><td>814.0</td><td>8,702.0</td><td>9,052.0</td><td>6,948.0</td></tr><tr><td>Cons. EPS</td><td>1.14</td><td>7.46</td><td>10.75</td><td>13.36</td></tr></table>

Please see analyst certifications, important disclosure information, and information regarding the status of non-US analysts on pages 11 - 16 of this report. \* JEF Hong Kong Limited

RATING | TARGET | ESTIMATE CHANGE

<table><tr><td>RATING</td><td>↓HOLD (BUY)</td></tr><tr><td>PRICE</td><td>HK$142.00^</td></tr><tr><td>PRICE TARGET | % TO PT</td><td>↑HK$153.74 (HK$10.73) | +8%</td></tr><tr><td>52W HIGH-LOW</td><td>HK$305.00 - HK$19.42</td></tr><tr><td>FLOAT (%) | ADV MM (USD)</td><td>47.8% | 554.12</td></tr><tr><td>MARKET CAP</td><td>HK$117.6B | $15.0B</td></tr><tr><td>TICKER</td><td>6869 HK</td></tr></table>

^Prior trading day's closing price unless otherwise noted.

<table><tr><td>FY (Dec)</td><td colspan="3">CHANGE TO JEFe</td><td colspan="2">JEF vs CONS</td></tr><tr><td></td><td>2026</td><td colspan="2">2027</td><td>2026</td><td>2027</td></tr><tr><td>REV</td><td>+98%</td><td colspan="2">NA</td><td>+12%</td><td>-7%</td></tr><tr><td>EPS</td><td>+838%</td><td colspan="2">NA</td><td>+53%</td><td>+11%</td></tr><tr><td>2026 (RMB)</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>FY</td></tr><tr><td>EPS</td><td>--</td><td>--</td><td>--</td><td>--</td><td>↑11.44</td></tr><tr><td>PREV</td><td></td><td></td><td></td><td></td><td>1.22</td></tr></table>

![](images/3b674b31ed2bad56fc188c2eb2ebe073c66d9bd17867bd91a886bcb7662edced.jpg)  
Source: Company data, JEF

Chart 2 - LT PE Chart (Exclude AI Rally)  
![](images/677dbe8492cbe62e8bef97e7318ffa1a2ee0eb0c3fc7dd1651bff02a5c176348.jpg)  
Source: Factset, JEF

Chart 3 - LT PB Chart (Exclude AI Rally)  
![](images/2a323b2e4020dd65ccd847aec65a506d1bd0f2748db796827e725439231ae547.jpg)  
Source: Factset, JEF  
Edison Lee, CFA \* | Equity Analyst
852 3743 8009 | edison.lee@JEF.com

Annie Ping, CFA, FRM \* | Equity Associate +852 3767 1273 | annie.ping@JEF.com

+852 3743 8750 | nick.cheng@JEF.com

Jacky He \* | Equity Analyst
+852 3743 8084 | jacky.he@JEF.com

Matt Ma \* | Equity Analyst
852 3767 1109 | matt.ma@JEF.com

## The Long View: YOFC

## Investment Thesis

\- China Telecom/China Unicom's provincial tenders are at \~Rmb80/fkm, reflecting their willingness to pay market prices. China Mobile's tender result should be out soon.

\- China's 5G capex peaked in 2021, and the next telecom investment cycle remains distant. Future 6G deployment may leverage existing fiber networks, limiting incremental OF demand from telecom capex.

\- AI demand is driving NT price hikes, but aggressive industry capacity expansion esp in China could cap upside and eventually pressure pricing beyond 2027-28.

\- Management have done a good job of pursuing export sales and diversifying into optical modules and AOC. But its optical module business is an A-share listed company that investors could invest in separately.

Risk/Reward - 12 Month View  
![](images/65386968bb1e1984a22454868931a2a161393bdb2a298230fabffb1b369c013d.jpg)

## Base Case,

## HK\$153.74, +8%

• China has 4.2m 5G base stations by 2027.

\- ASP of all OFC to grow by 90% in 2026, but fall after 2028 because the capacity expansion will eliminate the shortage.

• GM of preform+OF combined to rise from 47.5% in 2025 to 85.5% in 2027, then fall to 69.4% in 2030.

\- Export sales would be $>50\%$ of total rev in 2026-2030.

\- PT of HK\$153.74 based on SOTP valuation, with TP of OF business based on the average of 14.1x 27E PE and 3.56x 28E PB, alongside HK\$9.52 of EverProX, HK\$3.17 of diversified biz. PT implies 11.2x/14.5x 2027E/28E P/E.

## Upside Scenario, HK\$283.32, +100%

• We expect same 5G BTS & backbone transmission build.

\- ASP of all OFC to grow by 94% in 2026, but fall after 2028 because the capacity expansion will eliminate the shortage.

• GM of preform+OF combined to rise from 47.5% in 2025 to 89.9% in 2027, then fall to 83.0% in 2030.

\- PT of HK\$283.32 based on SOTP valuation, with TP of OF business based on the average of 15.0x 27E PE and 5.00x 28E PB, alongside HK\$19.02 of EverProX, HK\$3.17 of diversified biz. PT implies 13.5x/16.0x 2027E/28E P/E.

## Downside Scenario, HK\$55.6, -61%

• We expect same 5G BTS & backbone transmission build.

\- ASP of all OFC to grow by 58% in 2026, but fall after 2027 because the capacity expansion will eliminate the shortage.

• GM of preform+OF combined to rise from 47.5% in 2025 to 77.9% in 2026, then fall to 54.2% in 2030.

\- PT of HK\$55.60 based on SOTP valuation, with TP of OF business based on the average of 14.1x 27E PE and 3.56x 28E PB, alongside HK\$8.15 of EverProX, HK\$3.17 of diversified biz. PT implies 10.3x 2027E P/E.

## Sustainability Matters

## Top Material Issues:

1) Address climate change, strengthen environmental compliance, and build a sustainable supply chain. 2) Drive innovation in next-generation optical communication technologies while maintaining product quality and data security.

## Key ESG Targets:

1) Reduce GHG emissions intensity by 50% by 2028 (vs. 2021 baseline) and achieve carbon neutrality by 2055. 2) Maintain 100% compliance for wastewater, exhaust gas, and waste emissions, while improving energy efficiency and renewable energy usage. 3) Strengthen information security, business continuity, and global compliance management, while achieving 100% supplier CSR and integrity commitment coverage.

## Key Questions for Mgmt:

1) What compliance system has YOFC built to meet regulatory requirements in overseas countries? 2) How is YOFC progressing toward its decarbonization targets? 3) What are YOFC's key R&D priorities under its AI-2030 strategy, and how will they support long-term growth and competitiveness?

## Catalysts

## Positive:

\- Higher-than-expected growth in SiC, AOC, optical modules, submarine cable, and telecom engineering revenue.

\- Announcement of domestic CSP OF tender with feasible price.

• Higher-than-expected growth in OF price.

## Negative:

\- More announcement of OF capacity expansion.

\- Faster-than-expected capacity expansion.

\- New telco tenders with lower-than-expected price.

Table 1 - Announced Capacity Expansion (2026-2028)

<table><tr><td>Players</td><td>Δ Capacity (ton)</td></tr><tr><td>China</td><td>14,700</td></tr><tr><td>Futong (M&amp;A by Lingyi iTech)</td><td>500</td></tr><tr><td>ZTT</td><td>850</td></tr><tr><td>Fiberhome</td><td>1,200</td></tr><tr><td>Hengtong</td><td>1,500</td></tr><tr><td>ETERN</td><td>600</td></tr><tr><td>Tongding</td><td>1,250</td></tr><tr><td>Hangzhou Cable</td><td>1,200</td></tr><tr><td>Far East</td><td>1,800</td></tr><tr><td>Qinghai Zhongli</td><td>300</td></tr><tr><td>SDGI</td><td>300</td></tr><tr><td>Han&#x27;s Laser*</td><td>2,000</td></tr><tr><td>Hoshine Silicon Industry*</td><td>3,200</td></tr><tr><td>Japan</td><td>3,200</td></tr><tr><td>Fujikura</td><td>1,300</td></tr><tr><td>Furukawa</td><td>1,900</td></tr><tr><td>US</td><td>1,500</td></tr><tr><td>Corning</td><td>1,500</td></tr><tr><td>Global Total</td><td>19,400</td></tr></table>

Source: Company data, JEF \*new entrants

Table 2 - YOFC's Valuation Table (@HKD 142.00)

<table><tr><td>Dec 31, Rmb m</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td></tr><tr><td>Revenue</td><td>12,197</td><td>14,252</td><td>27,944</td><td>29,353</td><td>26,283</td><td>22,904</td><td>20,429</td><td>19,780</td><td>19,248</td></tr><tr><td>YoY</td><td>-9%</td><td>17%</td><td>96%</td><td>5%</td><td>-10%</td><td>-13%</td><td>-11%</td><td>-3%</td><td>-3%</td></tr><tr><td>vs consensus</td><td></td><td></td><td>12.0%</td><td>-7.0%</td><td>-31.3%</td><td></td><td></td><td></td><td></td></tr><tr><td>Adj. EBITDA</td><td>1,726</td><td>2,717</td><td>12,123</td><td>13,054</td><td>10,388</td><td>7,755</td><td>5,639</td><td>4,656</td><td>3,688</td></tr><tr><td>YoY</td><td>3%</td><td>57%</td><td>346%</td><td>8%</td><td>-20%</td><td>-25%</td><td>-27%</td><td>-17%</td><td>-21%</td></tr><tr><td>vs consensus</td><td></td><td></td><td>41.7%</td><td>5.0%</td><td>-27.3%</td><td></td><td></td><td></td><td></td></tr><tr><td>Net profit (to parent)</td><td>676</td><td>814</td><td>8,702</td><td>9,052</td><td>6,948</td><td>4,710</td><td>2,912</td><td>2,150</td><td>1,408</td></tr><tr><td>YoY</td><td>-48%</td><td>20%</td><td>969%</td><td>4%</td><td>-23%</td><td>-32%</td><td>-38%</td><td>-26%</td><td>-35%</td></tr><tr><td>vs consensus</td><td></td><td></td><td>41.2%</td><td>2.0%</td><td>-37.0%</td><td></td><td></td><td></td><td></td></tr><tr><td>EPS (Rmb)</td><td>0.89</td><td>1.07</td><td>11.44</td><td>11.90</td><td>9.14</td><td>6.19</td><td>3.83</td><td>2.83</td><td>1.85</td></tr><tr><td>YoY</td><td>-48%</td><td>20%</td><td>969%</td><td>4%</td><td>-23%</td><td>-32%</td><td>-38%</td><td>-26%</td><td>-35%</td></tr><tr><td>vs consensus</td><td></td><td></td><td>53.4%</td><td>10.7%</td><td>-31.6%</td><td></td><td></td><td></td><td></td></tr><tr><td>EV/EBITDA x</td><td>60.4</td><td>38.4</td><td>8.6</td><td>8.0</td><td>10.0</td><td>13.4</td><td>18.5</td><td>22.4</td><td>28.3</td></tr><tr><td>PEx</td><td>137.1</td><td>114.6</td><td>10.7</td><td>10.3</td><td>13.4</td><td>19.8</td><td>32.0</td><td>43.4</td><td>66.2</td></tr><tr><td>Adjusted PEx</td><td>135.1</td><td>112.9</td><td>10.6</td><td>10.1</td><td>13.2</td><td>19.5</td><td>31.5</td><td>42.7</td><td>65.2</td></tr><tr><td>PBx</td><td>8.0</td><td>6.8</td><td>4.7</td><td>3.6</td><td>3.1</td><td>2.8</td><td>2.6</td><td>2.5</td><td>2.5</td></tr><tr><td>FCF yield to mkt cap</td><td>0.4%</td><td>2.1%</td><td>3.0%</td><td>9.1%</td><td>8.7%</td><td>6.3%</td><td>4.7%</td><td>3.2%</td><td>7.5%</td></tr><tr><td>Dividend yield</td><td>0.2%</td><td>0.2%</td><td>2.8%</td><td>2.9%</td><td>2.2%</td><td>1.5%</td><td>0.9%</td><td>0.7%</td><td>0.5%</td></tr><tr><td>EV/IC</td><td>5.5</td><td>5.5</td><td>4.4</td><td>4.2</td><td>4.3</td><td>4.4</td><td>4.6</td><td>4.8</td><td>7.4</td></tr><tr><td>ROAE</td><td>4.5%</td><td>4.9%</td><td>42.0%</td><td>33.8%</td><td>21.6%</td><td>13.0%</td><td>7.5%</td><td>5.3%</td><td>3.4%</td></tr><tr><td>ROIC</td><td>5.1%</td><td>6.9%</td><td>45.9%</td><td>43.2%</td><td>35.3%</td><td>26.6%</td><td>18.9%</td><td>15.7%</td><td>14.3%</td></tr></table>

Source: Company, Factset, JEF

<table><tr><td colspan="2">PB</td></tr><tr><td colspan="2">OF - total</td></tr><tr><td>28E P/Bx</td><td>3.56x</td></tr><tr><td>OF BV (Rmb mn)</td><td>29,061</td></tr><tr><td>OF equity value</td><td>103,456</td></tr><tr><td>OF TP</td><td>124.96</td></tr><tr><td colspan="2">PE</td></tr><tr><td colspan="2">OF - total</td></tr><tr><td>27E P/Ex</td><td>14.1x</td></tr><tr><td>OF EPS</td><td>9.37</td></tr><tr><td>OF TP</td><td>132</td></tr><tr><td>OF TP</td><td>132.13</td></tr><tr><td colspan="2">OF</td></tr><tr><td>Average OF TP (Rmb)</td><td>121.78</td></tr><tr><td colspan="2">EverproX (300548 CH)</td></tr><tr><td>YOFC&#x27;s stake in EverproX</td><td>19.03%</td></tr><tr><td>Holdco discount</td><td>19.03%</td></tr><tr><td>Equity value per share (Rmb)</td><td>8.22</td></tr><tr><td colspan="2">Diversified biz</td></tr><tr><td>Equity value per share (Rmb)</td><td>2.74</td></tr><tr><td>SOTP PT (Rmb)</td><td>132.73</td></tr><tr><td>SOTP PT (HKD)</td><td>153.74</td></tr><tr><td>Upside (downside)</td><td>8.3%</td></tr></table>

Source: Company, JEF

<table><tr><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td></tr><tr><td colspan="8">Income Statement Assumptions</td></tr><tr><td colspan="8">Capacity</td></tr><tr><td>Preform (ton)</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td></tr><tr><td>previous</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td><td>4,000</td></tr><tr><td>Optical fibers (m fkm)</td><td>81</td><td>81</td><td>81</td><td>81</td><td>81</td><td>81</td><td>81</td></tr><tr><td>previous</td><td>81</td><td>81</td><td>81</td><td>81</td><td>81</td><td>81</td><td>81</td></tr><tr><td>Optical fiber cables (m fkm)</td><td>23</td><td>23</td><td>23</td><td>23</td><td>23</td><td>23</td><td>23</td></tr><tr><td>previous</td><td>23</td><td>23</td><td>23</td><td>23</td><td>23</td><td>23</td><td>23</td></tr><tr><td colspan="8">Capacity utilization</td></tr><tr><td>Optical fiber preforms</td><td>96%</td><td>99%</td><td>95%</td><td>95%</td><td>95%</td><td>95%</td><td>95%<

[中间内容因长度限制已省略]

the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
