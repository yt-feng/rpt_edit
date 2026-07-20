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
# China Brewing: Read across from Yanjing: Read across from Yanjing investor meeting: Widening divergence in key SKU performance

We observed a continued structural divergence within the beer industry in 2Q26 (preview here), expecting a c.4% volume decline for Tsingtao/Chongqing and a low-teens% contraction in Bud China, vs. maintained LSD% growth in CR Beer (Exhibit 4). Against a softer macro backdrop for the broader sector, we note that selected blockbuster SKUs/localized portfolios have continued to show notable resilience, gaining share through stronger channel penetration/incentives and solid execution. Specifically, CR Beer's Heineken and Yanjing Beer's flagship U8 in the premium/sub-premium segment have consistently outperformed in 2025-2026 YTD. According to Yanjing's recent public investor meeting, U8 has maintained close to 30% volume growth in 1Q26 after reaching c. 0.9mn KL in 2025, while the strategic rollout of the A10 portfolio is gaining early traction after its launch in end-March 2026. Looking into 2H26, we see weather swings/on-trade recovery as the key swing factors, and we reiterate our positive view on CR Beer given its beer growth visibility underpinned by a strong portfolio/solid execution, particularly as it moves into a lower base in 2H26, with an attractive risk/reward profile at 11x/10x 2026E/27E P/E and a 5.5% 2026E dividend yield on GSe.

Key takeaways from Yanjing's investor meeting on 16 July: 1) U8 continues to post strong gains in the Rmb8-10 sub-premium segment YTD: U8's sales volume grew nearly $30 \%$ and reached 0.9mn KL in 2025 from c.0.1mn KL in 2020 after launch (c.55% CAGR), and the strong momentum has carried over into 1Q26 with close to $30 \%$ yoy growth, with momentum accelerating further into July. U8 has been consistently expanding rapidly since its debut in 2019, with a c.30% volume CAGR maintained in 2023-25E, indicating that U8's nationalization/channel penetration are still in their high-growth phases, with the brand continuing to capture market share from competing SKUs in a similar pricing range (e.g., Tsingtao Classic/Snow Draft/Harbin Core+ etc.). 2) The premium portfolio continues to strengthen: Yanjing has officially launched A10 All-Malt Brew in the Rmb12-15 price range, positioned as the company's core SKU for premiumization in 1Q, and is actively expanding distribution coverage, with additional formats such as canned SKUs/smaller packs for nightlife channels to follow in 2H. 3) The regional portfolio remains resilient despite broader industry softness: Yanjing's regional flagship Liquan 1998 still delivered YoY volume growth in 1H26, despite severely unfavorable weather in Guangxi in 2Q26. Building on Liquan's proven regional expansion playbook, Yanjing plans to replicate the strategy with Huiquan 1983 this year for expansion in the Fujian/Jiangxi markets.

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Christina Liu  
+852-2978-6983 | christina.liu@gs.com  
GS (Asia) L.L.C.

Valerie Zhou  
+852-2978-0820 | valerie.zhou@gs.com  
GS (Asia) L.L.C.

Read across to our China Brewer coverage: 1) The sub-premium segment remains the sweet spot amid the consumption slowdown: Yanjing U8 is strategically positioned in the RMB 8–10 retail price segment, which still seems to be the “sweet spot” of China’s beer premiumization due to its mass upgrade path and relatively large addressable market with national scalability, while super-premium beer/craft beers (RMB 12\~15+) face distribution bottlenecks and niche appeal. 2) The “Large Single Product” (大单品) strategy remains an effective growth strategy: Yanjing U8’s success demonstrates that in a mature/flat-volume market, concentrating marketing/channel resources and brand equity into a single, highly recognizable mid-to-high-end product is likely still the more efficient way to scale.

## Related Reads:

Chongqing Brewery (600132.SS): NDR Takeaways: June saw easing pressure sequentially vs. Apr-May; O2O competition/cost trend to watch

China Resources Beer: APAC Consumer & Leisure Corporate Day 2026 Takeaways - Full year targets maintained with sequentially improved June and intact premiumization; Heineken maintaining 20%+ growth; Reiterate Buy

Budweiser APAC: APAC Consumer & Leisure Corporate Day 2026 Takeaways - Delayed recovery in China; O2O/Premium/new Products remained key growth strategy

Budweiser APAC (1876.HK): 2Q26 Preview: China under pressure with delayed recovery under unfavorable weather/channel mix while Korea recovered on easier comps and India remains strong

Competition Landscape  
Exhibit 1: Premium beer SKU map  
![](images/4eee729eed8f5c440e2374b875fe57a5b82ec8229f18628779e511f26e44df30.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 2: We expect premiumization to remain intact in 2025-28E  
![](images/6fb6e39216d3ba2b2f3f45d1cf5aa9e57a0cbdba7425a3a810404d7725053879.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 3: Yanjing significantly gained share in the premium segment over the past five years on U8 success  
![](images/292b3ae8439ab64d9bca3f0bf0bba00229cfa16597a2a7c5ef36b6cfb8c74f9f.jpg)  
Source: Company data, GS Global Investment Research

## China Brewers 2Q26/2026 earnings forecast summary

Exhibit 4: 2Q26 forecasts in detail – by company/region

<table><tr><td>2Q26E</td><td>ASP growth</td><td>Volume growth</td><td>Sales growth</td><td>Unit COGS growth</td><td>GPM YoY Chg</td><td>Premium Vol growth</td><td>Recurring EBITDA growth</td><td>Recurring EBITDA MARGIN</td><td>Recurring EBIT growth</td><td>Recurring NP growth</td></tr><tr><td>CRB - Beer (1H26)</td><td>0.8%</td><td>3.0%</td><td>3.8%</td><td>0.5%</td><td>0.2pp</td><td>7.0%</td><td>5.6%</td><td>35.7%</td><td>7.1%</td><td></td></tr><tr><td>CRB - Overall (1H26)</td><td></td><td></td><td>3.4%</td><td></td><td>-0.4pp</td><td></td><td>-5.4%</td><td>35.0%</td><td>6.4%</td><td>7.0%</td></tr><tr><td>Bud China</td><td>-1.0%</td><td>-10.0%</td><td>-10.9%</td><td></td><td></td><td></td><td>-25.0%</td><td>31.6%</td><td></td><td></td></tr><tr><td>Bud West</td><td>-0.2%</td><td>-6.5%</td><td>-6.7%</td><td></td><td></td><td></td><td>-20.0%</td><td>26.5%</td><td></td><td></td></tr><tr><td>Bud East</td><td>-0.7%</td><td>6.2%</td><td>5.5%</td><td></td><td></td><td></td><td>19.0%</td><td>28.5%</td><td></td><td></td></tr><tr><td>Bud APAC</td><td>0.6%</td><td>-5.0%</td><td>-4.4%</td><td></td><td>-1.0pp</td><td></td><td>-13.7%</td><td>26.9%</td><td>-16.7%</td><td>-15.3%</td></tr><tr><td>Tsingtao</td><td>0.5%</td><td>-4.6%</td><td>-4.1%</td><td>-0.2%</td><td>0.4pp</td><td>3.0%</td><td></td><td></td><td>-3.6%</td><td>-4.7%</td></tr><tr><td>Chongqing</td><td>0.1%</td><td>-4.5%</td><td>-4.4%</td><td>-1.2%</td><td>0.9pp</td><td></td><td></td><td></td><td>-4.8%</td><td>-4.4%</td></tr></table>

1) Organic ASP, volume, sales and EBITDA growth for Budweiser excl. forex, but recurring EBIT/reported NP growth under forex impact; 2) GPM for Tsingtao: after sales tax + COGS. Remaining companies GPM after COGS.

Source: GS Global Investment Research

Exhibit 5: FY2026 forecasts in detail – by company/region

<table><tr><td>2026E</td><td>ASP growth</td><td>Volume growth</td><td>Sales growth</td><td>Unit COGS growth</td><td>GPM YoY Chg</td><td>Premium Vol growth</td><td>Recurring EBITDA growth</td><td>Recurring EBITDA MARGIN</td><td>Recurring EBIT growth</td><td>Recurring NP growth</td></tr><tr><td>CRB - Beer</td><td>3.2%</td><td>0.1%</td><td>3.3%</td><td>3.2%</td><td>-0.1pp</td><td>6.5%</td><td>4.0%</td><td>26.5%</td><td>4.4%</td><td></td></tr><tr><td>CRB - Overall</td><td></td><td></td><td>2.8%</td><td></td><td>-0.1pp</td><td></td><td>6.2%</td><td>26.9%</td><td>3.8%</td><td>4.3%</td></tr><tr><td>Bud China</td><td>-0.2%</td><td>-1.6%</td><td>-1.8%</td><td></td><td></td><td></td><td>-9.2%</td><td>31.7%</td><td></td><td></td></tr><tr><td>Bud West</td><td>0.7%</td><td>0.4%</td><td>1.1%</td><td></td><td></td><td></td><td>-7.3%</td><td>25.2%</td><td></td><td></td></tr><tr><td>Bud East</td><td>0.9%</td><td>-0.4%</td><td>0.5%</td><td></td><td></td><td></td><td>2.0%</td><td>30.1%</td><td></td><td></td></tr><tr><td>Bud APAC</td><td>0.7%</td><td>0.3%</td><td>1.0%</td><td></td><td>-0.1pp</td><td></td><td>-5.0%</td><td>26.3%</td><td>-2.9%</td><td>-5.9%</td></tr><tr><td>Tsingtao</td><td>0.9%</td><td>-1.9%</td><td>-1.0%</td><td>-0.1%</td><td>0.6pp</td><td>2.0%</td><td>2.6%</td><td>20.7%</td><td>3.4%</td><td>1.5%</td></tr><tr><td>Chongqing</td><td>0.1%</td><td>-1.2%</td><td>-1.1%</td><td>0.6%</td><td>-0.1pp</td><td>1.1%</td><td>-1.4%</td><td>25.1%</td><td>-2.1%</td><td>-1.2%</td></tr></table>

1) Organic ASP, volume, sales and EBITDA growth for Budweiser excl. forex, but recurring EBIT/reported NP growth under forex impact; 2) GPM for Tsingtao: after sales tax + COGS. Remaining companies GPM after COGS.

Source: GS Global Investment Research

## Beer Monthly Tracker

Exhibit 6: Monthly volume table 2024-2026 by GSe

<table><tr><td></td><td>Jan</td><td>Feb</td><td>March</td><td>April</td><td>May</td><td>Jun</td><td>2025EJul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td><td>2026EJan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td></tr><tr><td>CRB</td><td colspan="2">up MSD%</td><td>positive growth</td><td>positive growth, slightly faster than 1Q</td><td>up LSD%</td><td>minor positive growth</td><td>up 4-5%</td><td>up LSD%</td><td>up LSD%</td><td>slightly positive</td><td>flattish to slightly positive</td><td>flattish</td><td>positive</td><td>Positive growth; Jan+Feb Heineken up by DD%</td><td>Slightly growth</td><td>Up LSD%, similar to 1Q26</td><td>slower than April trend</td><td>Sequentially faster MoM</td></tr><tr><td>Bud APAC China</td><td colspan="2">down MSD%</td><td>decline</td><td>down LSD%</td><td>down HSD%</td><td>down HSD%</td><td>down low teens%</td><td>down c.Mid teens %</td><td>down SD%</td><td>Minor decline</td><td>Down 7-8%</td><td>down DD%</td><td>Likely negative</td><td>Volume under pressure</td><td>up 3-4%</td><td>Volume declined by low teens% (super premium up by low teens%, premium down by low teens%, core down by mid teens%)</td><td>down 12~13%</td><td>HSD% decline</td></tr><tr><td>Tsingtao</td><td>down MSD%</td><td>up MSD%</td><td>up DD%</td><td>down LSD%</td><td>up MSD%</td><td>flattish</td><td>flattish</td><td>up 1.5%</td><td>up 3%</td><td>down HSD%</td><td>up 1.1%</td><td>up 12%</td><td>volume down c.MSD%</td><td>down 9.5%</td><td>up 5-6%</td><td>Volume declined by 7.5%</td><td>down 9%</td><td>largely flattish, improving vs. April/May</td></tr><tr><td>Chongqing</td><td colspan="2">positive growth</td><td>up LSD%</td><td>largely steady</td><td>flattish to minor decline</td><td>down LSD%</td><td>minor decline</td><td>down LSD%</td><td>up MSD%</td><td>Minor decline</td><td>up slightly %</td><td>up slightly %</td><td>Jan-Feb</td><td>negative on relatively high base</td><td>positive growth</td><td>Volume down by LSD%</td><td>HSD% decline</td><td>SD% decline</td></tr><tr><td>Bairun</td><td colspan="2">RTD cocktails down c.10%</td><td></td><td></td><td>RTD cocktail sales down teens%</td><td></td><td>RTD cocktail down c.high teens%</td><td>DD% growth in RTD drinks due to low base</td><td>flattish</td><td></td><td>offline shipment up 30%</td><td></td><td>up DD%+ on calendar shift</td><td></td><td></td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td></tr><tr><td>Yanjing</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD% positive growth</td></tr><tr><td>Industry</td><td colspan="2">-4.90%</td><td>1.90%</td><td>4.80%</td><td>1.30%</td><td>-0.20%</td><td>1.90%</td><td>-1.80%</td><td>3.10%</td><td>-1.00%</td><td>-5.80%</td><td>-8.70%</td><td colspan="2">6.50%</td><td>0.20%</td><td>-0.10%</td><td>-6.20%</td><td></td></tr></table>

Source: GS Global Investment Research

## Valuation Comp

Exhibit 7: China beer coverage valuation comp

<table><tr><td rowspan="2"></td><td rowspan="2">Company</td><td rowspan="2">Rating</td><td rowspan="2">Ccy</td><td rowspan="2">Price 7/16/2026</td><td rowspan="2">12-m TP</td><td rowspan="2">+/-</td><td colspan="3">PE</td><td colspan="3">TP Implied PE</td><td rowspan="2">26-28E Rev CAGR</td><td rowspan="2">26-28E NP CAGR</td><td colspan="3">EV/EBITDA</td><td rowspan="2">ROE 2026E</td><td rowspan="2">Div yield 2026E</td><td rowspan="2">YTD perf %</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="21">Beer</td></tr><tr><td>1876.HK</td><td>Budweiser APAC</td><td>Buy</td><td>HKD</td><td>6.49</td><td>7.60</td><td>17%</td><td>18X</td><td>16X</td><td>14X</td><td>21X</td><td>19X</td><td>17X</td><td>4%</td><td>12%</td><td>6X</td><td>5X</td><td>5X</td><td>6%</td><td>5.1%</td><td>-14%</td></tr><tr><td>0291.HK</td><td>China Resources Beer</td><td>Buy</td><td>HKD</td><td>23.74</td><td>36.45</td><td>54%</td><td>11X</td><td>10X</td><td>10X</td><td>17X</td><td>16X</td><td>15X</td><td>2%</td><td>7%</td><td>6X</td><td>5X</td><td>4X</td><td>17%</td><td>5.5%</td><td>-9%</td></tr><tr><td>0168.HK</td><td>Tsingtao Brewery (H)</td><td>Buy</td><td>HKD</td><td>44.92</td><td>54.00</td><td>20%</td><td>12X</td><td>11X</td><td>10X</td><td>14X</td><td>13X</td><td>12X</td><td>2%</td><td>6%</td><td>6X</td><td>6X</td><td>5X</td><td>14%</td><td>6.3%</td><td>-8%</td></tr><tr><td>600600.SS</td><td>Tsingtao Brewery (A)</td><td>Neutral</td><td>CNY</td><td>52.86</td><td>58.70</td><td>11%</td><td>16X</td><td>15X</td><td>14X</td><td>17X</td><td>16X</td><td>15X</td><td>2%</td><td>6%</td><td>9X</td><td>8X</td><td>8X</td><td>14%</td><td>4.6%</td><td>-14%</td></tr><tr><td>600132.SS</td><td>Chongqing Brewery</td><td>Neutral</td><td>CNY</td><td>43.70</td><td>43.00</td><td>-2%</td><td>17X</td><td>17X</td><td>16X</td><td>17X</td><td>16X</td><td>15X</td><td>2%</td><td>5%</td><td>6X</td><td>6X</td><td>5X</td><td>35%</td><td>5.7%</td><td>-16%</td></tr><tr><td>002568.SZ</td><td>Shanghai Bairun</td><td>Neutral</td><td>CNY</td><td>18.18</td><td>18.60</td><td>2%</td><td>25X</td><td>21X</td><td>n.a.</td><td>25X</td><td>22X</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>16X</td><td>14X</td><td>n.a.</td><td>14%</td><td>2.0%</td><td>-17%</td></tr><tr><td>Avg.</td><td></td><td></td><td></td><td></td><td></td><td></td><td>16X</td><td>15X</td><td>13X</td><td>19X</td><td>17X</td><td>15X</td><td>3%</td><td>6%</td><td>8X</td><td>7X</td><td>5X</td><td>17%</td><td>4.8%</td><td>-13%</td></tr><tr><td>ABI.BR</td><td>Anheuser-Busch InBev</td><td>Buy</td><td>EUR</td><td>70.72</td><td>85.00</td><td>20%</td><td>18X</td><td>16X</td><td>14X</td><td>22X</td><td>19X</td><td>17X</td><td>3%</td><td>0%</td><td>10X</td><td>10X</td><td>9X</td><td>11%</td><td>1.7%</td><td>29%</td></tr><tr><td>CARLb.CO</td><td>Carlsberg</td><td>Buy</td><td>DKK</td><td>934.80</td><td>1100.00</td><td>18%</td><td>14X</td><td>13X</td><td>12X</td><td>16X</td><td>15X</td><td>14X</td><td>3%</td><td>8%</td><td>10X</td><td>9X</td><td>8X</td><td>27%</td><td>3.3%</td><td>12%</td></tr><tr><td>HEIN.AS</td><td>Heineken</td><td>Buy</td><td>EUR</td><td>76.64</td><td>90.00</td><td>17%</td><td>14X</td><td>13X</td><td>12X</td><td>17X</td><td>16X</td><td>15X</td><td>3%</td><td>6%</td><td>8X</td><td>8X</td><td>8X</td><td>14%</td><td>2.6%</td><td>10%</td></tr><tr><td>2503.T</td><td>Kirin Holdings</td><td>Sell</td><td>JPY</td><td>2862.50</td><td>2400.00</td><td>-16%</td><td>12X</td><td>14X</td><td>13X</td><td>10X</td><td>12X</td><td>11X</td><td>1%</td><td>-7%</td><td>9X</td><td>9X</td><td>9X</td><td>12%</td><td>2.6%</td><td>22%</td></tr><tr><td>2587.T</td><td>Suntory Beverage &amp; Food Ltd</td><td>Buy</td><td>JPY</td><td>4660.00</td><td>5300.00</td><td>14%</td><td>17X</td><td>16X</td><td>15X</td><t

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
