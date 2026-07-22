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
CHINA CONSUMER DURABLES

# RVC 2Q26 preview: Domestic demand better-than-feared, still robust overseas demand, stable pricing/margin; Buy Roborock

Share prices of Roborock and Ecovacs, RVC leaders within our coverage, have underperformed the consumer durable peers/market YTD (c. -30% vs -17%/-1% of coverage average/CSI300), primarily due to investor concerns on: 1) domestic demand yoy growth pressure on high comp base, 2) potential overseas demand slowdown risk due to rising energy prices, and 3) potential margin pressure on competition from Dreame, and cyclical headwinds from cost inflation and FX. Despite such market concerns, we forecast generally resilient 2Q26 results as: 1) domestic growth has been better-than-feared supported by ongoing RVC penetration increase, 2) overseas demand (esp. in Europe) remains robust as leading players continue to expand into new markets/channels leveraging competitive products, 3) margin stays largely stable with Dreame signaling a scale back from its previous expansionary strategy (news link) while overall ASP stays steady. Additionally, we expect the FX headwinds to be partially offset by other non-recurring items including US tariff refund and investment gains.

Stock-wise, we expect Roborock to continue to outpace the industry driven by revenue growth acceleration (supported by share gains in RVC and expansion into wet-dry vacuum cleaners) and margin recovery (aided by scaling back on washer-dryer investment) in 2Q (+27%/+20% revenue/profits yoy growth in 2Q). In comparison, we expect Ecovacs to deliver healthy yet slightly slower growth mainly driven by overseas revenue growth and investment gain from its portfolio companies (+15%/+15% revenue/profits yoy growth in 2Q).

Demand/Growth: Cleaning appliances' demand remained robust on global level, and came above our previous expectations on more resilient domestic growth despite a challenging comp base, as well as strong overseas growth partly attributable to earlier Prime Day this year (June 23-26 in 2026 vs July 8-11 in 2025).

☐ In the domestic market, despite a high base last year boosted by trade-in stimulus, industry growth sequentially improved during 618, stronger than most other appliances categories on ongoing penetration increase and above previous market expectations in our view. Both Roborock and Ecovacs reported 20%+ cleaning appliances GMV yoy growth during 618, which could help make up the seasonal weakness before/after the major

Nicolas Yi
+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

Cecilia Tang
+86(21)2401-8738 |
cecilia.tang@goldmansachs.cn
GS (China) Securities
Company Limited

promotion event. Company wise, Roborock gained share notably (+10ppt/+13ppt to 35%/29% market share in RVC/wet dry vacuums on JD and Taobao+Tmall in 2Q26 per Moojing), while share for Ecovacs/Tineco was largely stable at \~30%.

☐ Overseas demand remained robust growth as shown from both app downloads and Amazon US sales data (\~40% yoy growth in 2Q). Roborock further outpaced the industry driven by share gains particularly in the US market aided by its penetration into key offline retailers including COSTCO. Ecovacs also recorded robust growth alongside the industry, together with strong growth from robotic lawn mowers (read-across from Ninebot).

\- Margins: We expect net profits to grow at a slower pace vs revenue growth to mainly reflect cost and FX headwinds, yet there are also positive factors including higher focus on expense ROI, company specific actions including scaling back loss-making business, investment gains and tariff refund. Pricing showed mixed trends where RVC generally came more resilient than wet dry vacuums in domestic market. Per Rororock and Ecovacs management teams, they have ceased to subsidize consumers out of their own pockets this year and aim to achieve stable RVC pricing. On Amazon US, although industry ASP is moving up, leading Chinese players' ASP showed diverging trends.

Going forward, we continue to forecast resilient and faster overseas revenue growth (vs the domestic market) driven by stronger overseas demand and leading Chinese players' global share gain. We remain cautious about the potential drag on demand from high energy prices but so far haven't seen any concrete signs of demand slowdown. Between Roborock and Ecovacs, we believe Roborock is better positioned in case of any industry-level demand slowdown considering: 1) the company has significantly enhanced its presence in key US offline retailers (i.e., COSTCO) which we expect to lend additional boost to its US sales growth, and 2) the company has been rolling out wet-dry vacuum cleaners in overseas markets (esp. in Europe and APAC) which we expect to drive incremental revenue growth in addition to core RVC.

Accordingly, we revise up our 2026E-28E EPS for our covered RVC companies by 3%-12% to reflect the above changes, and revise down exit multiples to reflect the higher growth uncertainty/volatility due to competition and geopolitical tensions. Combined, this leads to our 12m TPs remaining largely stable. We are Buy rated on Roborock as we expect faster growth driven by continuous global market share gains, new product expansion esp. wet dry vacuums and margin recovery after business strategy adjustment esp. in China. We are Sell rated on Ecovacs on a relative basis as we see rising domestic growth pressure for Ecovacs facing competition in both RVC and wet dry vacuums on a high base which we expect to lead to slower growth compared to Roborock.

Exhibit 1: RVC/wet dry vacuum industry sales growth showed qoq improvements helped by 618. Retail sales growth by channel, yoy %

![](images/7ef1aaaf02f13180fd0d4ff6449906d18a408796b33a7d9137145d8e960624be.jpg)  
Source: AVC

![](images/abdbf483af7a81b495ec7aa772724354a40924808f2628d9b48160cc69170028.jpg)

Exhibit 2: On pricing, wet dry vacuums showed more ASP pressure especially online, while RVC ASP has been relatively more resilient.

Retail ASP (Rmb, LHS) and yoy growth by channel (\%, RHS)

![](images/96f8c16bb01dfc54072991bf1b5ee6287edfd678ad87efd6296d97f4fccec6c2.jpg)

![](images/ef929c22d0969a49d4318307d92e1ff5ce3e6104a8a1feb8e19335a7f4b53fd4.jpg)  
Source: AVC, Data compiled by GS Global Investment Research

Exhibit 3: Ecovacs (Tineco)/Roborock remain market leaders in the China cleaning appliances market. On a YoY basis, Roborock gained 10ppt/13ppt to 35%/29% market share in RVC/wet dry vacuums in 2Q26, while Ecovacs/Tineco gained 2ppt/lost 3ppt to 30%/28%.

Online market share for RVC and wet dry vacuums on Taobao, Tmall and JD (%)

![](images/93794e2261e365e8cf99eecfbafc08cc7585204de211d5d3c411ec3ea773e34d.jpg)  
Source: Moojing, Data compiled by GS Global Investment Research

![](images/e630cf31e205cc0dd72d369f5614715ab1b27ba36802e1bc98f8c2cdc7085b5d.jpg)

Exhibit 4: RVC industry download growth in overseas markets remained robust at 40%+ yoy growth in 2Q26
Download growth of leading RVC apps (yoy %)

![](images/df3f8a10199184f9781a170514d513fb1d67d1172a893045b3a843074f83d410.jpg)  
Source: SensorTower, Data compiled by GS Global Investment Research

Exhibit 5: Roborock gained share with 55% yoy downloads growth in 2Q26  
Roborock's RVC market share based on app downloads  
![](images/c725c813400d33e7066318ef7d33695e7ddb4a8cc0f3c7e415d82674e9556f30.jpg)  
Source: SensorTower, Data compiled by GS Global Investment Research

Exhibit 6: Ecovacs' market share was down slightly in 1Q26 with \~30% yoy growth in 2Q26
RVC market share based on app downloads  
![](images/b43ba4d867a1f8ebf57daa5aec1e2901555941f84e785e0f440bd51f2416d56b.jpg)

![](images/113421002e26547bfa370ab0810a38f7a76019f80bb6d3b2712fbeda730cc81a.jpg)

![](images/33fc8b427c79e6f6ee2b37598650c44f7b5f2e68ce3c90884a1588a520fbc625.jpg)  
Source: SensorTower, Data compiled by GS Global Investment Research

![](images/fd9dd4e438a2f1c2ffdac901df7494bb45eff4aa1bb0a2a8e9a09f9f397bcfcc.jpg)

Exhibit 7: Amazon US sales data also showed robust sales growth especially in June supported by earlier Prime Day. Roborock and Ecovacs both gained shares in 2Q26.

Sales/Volume/ASP yoy growth by category & Market share/Sales/Volume/ASP yoy growth by company on EC channel (Amazon US)

<table><tr><td rowspan="2"></td><td colspan="6">Sales (% yoy)</td><td colspan="6">Volume (% yoy)</td><td colspan="6">ASP (% yoy)</td></tr><tr><td>Jun-25</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2Q26</td><td>MoM Trend</td><td>Jun-25</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2Q26</td><td>MoM Trend</td><td>Jun-25</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2Q26</td><td>MoM Trend</td></tr><tr><td colspan="19">Amazon US</td></tr><tr><td>RVC</td><td>56%</td><td>6%</td><td>-16%</td><td>131%</td><td>39%</td><td>▲</td><td>54%</td><td>-17%</td><td>-18%</td><td>64%</td><td>11%</td><td>▲</td><td>1%</td><td>28%</td><td>3%</td><td>41%</td><td>26%</td><td>▲</td></tr><tr><td rowspan="2"></td><td colspan="6">Market share</td><td colspan="6">Market share chg (% yoy)</td><td colspan="6">Sales (% yoy)</td></tr><tr><td>Jun-25</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2Q26</td><td>YoY Trend</td><td>Jun-25</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2Q26</td><td>MoM Trend</td><td>Jun-25</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>2Q26</td><td>MoM Trend</td></tr><tr><td colspan="19">RVC</td></tr><tr><td>iRobot</td><td>10%</td><td>9%</td><td>8%</td><td>22%</td><td>16%</td><td>▲</td><td>-5%</td><td>-5%</td><td>-2%</td><td>12%</td><td>5%</td><td>▲</td><td>5%</td><td>-32%</td><td>-34%</td><td>397%</td><td>96%</td><td>▲</td></tr><tr><td>Roborock</td><td>20%</td><td>29%</td><td>32%</td><td>32%</td><td>31%</td><td>▲</td><td>3%</td><td>5%</td><td>10%</td><td>12%</td><td>9%</td><td>▲</td><td>79%</td><td>28%</td><td>25%</td><td>267%</td><td>99%</td><td>▲</td></tr><tr><td>Ecovacs</td><td>4%</td><td>6%</td><td>5%</td><td>22%</td><td>15%</td><td>▲</td><td>1%</td><td>-2%</td><td>-1%</td><td>18%</td><td>9%</td><td>▲</td><td>119%</td><td>-15%</td><td>-29%</td><td>397%</td><td>240%</td><td>▲</td></tr><tr><td>Dreame</td><td>3%</td><td>13%</td><td>11%</td><td>9%</td><td>10%</td><td>▲</td><td>-1%</td><td>6%</td><td>8%</td><td>6%</td><td>6%</td><td>▼</td><td>6%</td><td>98%</td><td>153%</td><td>567%</td><td>219%</td><td>▲</td></tr><tr><td>Shark</td><td>16%</td><td>9%</td><td>11%</td><td>12%</td><td>11%</td><td>▼</td><td>-3%</td><td>0%</td><td>-4%</td><td>-4%</td><td>-2%</td><td>▼</td><td>35%</td><td>7%</td><td>-36%</td><td>68%</td><td>13%</td><td>▲</td></tr><tr><td>Eufy</td><td>23%</td><td>6%</td><td>10%</td><td>8%</td><td>8%</td><td>▼</td><td>11%</td><td>-7%</td><td>-15%</td><td>-15%</td><td>-12%</td><td>■</td><td>193%</td><td>-51%</td><td>-66%</td><td>-16%</td><td>-45%</td><td>▲</td></tr></table>

Source: Moojing, Data compiled by GS Global Investment Research

Exhibit 8: Industry ASP is still moving up on Amazon US. Leading Chinese players' ASP have showed divergent trends. ASP and 12-m moving average ASP of RVC on Amazon US (USD)  
![](images/d4989b418141e8ef74cd6e17c809a689ee3b585801c2aa8657f141ff8b6e518a.jpg)  
Source: Moojing, Data compiled by GS Global Investment Research

![](images/afc02b0f3ba6ab765640d328f40b6903f133fb363426c907b88f00fec4d3a524.jpg)

## Summary of key changes

Exhibit 9: We revise down 12m TP for Ecovacs and Roborock by 13-14% to reflect 9-15% EPS downward revision and lower target multiples

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Latest close</td><td rowspan="2">Valuation method</td><td rowspan="2">COE</td><td colspan="2">Multiple</td><td colspan="4">Target Price</td><td colspan="3">EPS change</td><td colspan="2">Trading P/E</td><td colspan="2">TP implied P/E</td><td colspan="3">Growth, yoy %</td><td colspan="2">Dividend yield</td></tr><tr><td>new</td><td>old</td><td>new</td><td>old</td><td>change</td><td>U/D %</td><td>26E</td><td>27E</td><td>28E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>25A</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td></tr><tr><td>Ecovacs</td><td>603486.SS</td><td>Sell</td><td>Rmb 55.3</td><td>Discounted P/E</td><td>9.5%</td><td>16</td><td>17</td><td>56.0</td><td>55.0</td><td>2%</td><td>1.3%</td><td>5%</td><td>6%</td><td>6%</td><td>17.4x</td><td>15.5x</td><td>17.6x</td><td>15.7x</td><td>118%</td><td>5%</td><td>12%</td><td>2%</td><td>2%</td></tr><tr><td>Roborock</td><td>688169.SS</td><td>Buy</td><td>Rmb 102.2</td><td>Discounted P/E</td><td>9.5%</td><td>17</td><td>18</td><td>170.0</td><td>170.0</td><td></td><td>66.3%</td><td>12%</td><td>5%</td><td>3%</td><td>13.0x</td><td>10.3x</td><td>21.6x</td><td>17.2x</td><td>-31%</td><td>49%</td><td>26%</td><td>1%</td><td>1%</td></tr></table>

Pricing as of July 20, 2026.  
Source: Company data, GS Global Investment Research

Exhibit 10: We revise up Roborock's 2026E-28E EPS by $3 - 12\%$

<table><tr><td rowspan="2">Roborock688169.SS</td><td rowspan="2">2021</td><td rowspan="2">2022</td><td rowspan="2">2023</td><td rowspan="2">2024</td><td rowspan="2">2025</td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">Change</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>5,837</td><td>6,629</td><td>8,654</td><td>11,945</td><td>18,695</td><td>22,189</td><td>25,623</td><td>29,320</td><td>21,660</td><td>25,055</td><td>28,682</td><td>2.4%</td><td>2.3%</td><td>2.2%</td></tr><tr><td>Growth, yoy %</td><td>28.8%</td><td>13.6%</td><td>30.5%</td><td>38.0%</td><td>56.5%</td><td>18.7%</td><td>15.5%</td><td>14.4%</td><td>15.9%</td><td>15.7%</td><td>14.5%</td><td>2.8%</td><td>-0.2%</td><td>-0.1%</td></tr><tr><td>GPM</td><td>48.1%</td><td>49.3%</td><td>55.1%</td><td>50.1%</td><td>42.3%</td><td>42.7%</td><td>43.4%</td><td>43.9%</td><td>42.7%</td><td>43.5%</td><td>44.1%</td><td>0.0%</td><td>-0.1%</td><td>-0.2%</td></tr><tr><td>GPM chg (bps)</td><td></td><td>116</td><td>587</td><td>(500)</td><td>(779)</td><td>34</td><td>76</td><td>41</td><td>30</td><td>88</td><td>57</td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>1,316</td><td>1,154</td><td>2,016</td><td>1,574</td><td>1,002</td><td>1,730</td><td>2,246</td><td>2,758</td><td>1,558</td><td>2,126</td><td>2,666</td><td>11.0%</td><td>5.7%</td><td>3.5%</td></tr><tr><td>Growth, yoy %</td><td>-6.6%</td><td>-12.3%</td><td>74.7%</td><td>-21.9%</td><td>-36.4%</td><td>72.7%</td><td>29.8%</td><td>22.8%</td><td>55.5%</td><td>36.5%</td><td>25.4%</td><td>17.2%</td><td>-6.6%</td><td>-2.6%</td></tr><tr><td>OPM</td><td>22.5%</td><td>17.4%</td><td>23.3%</td><td>13.2%</td><td>5.4%</td><td>7.8%</td><td>8.8%</td><td>9.4%</td><td>7.2%</td><td>8.5%</td><td>9.3%</td><td>0.6%</td><td>0.3%</td><td>0.1%</td></tr><tr><td>OPM chg (bps)</td><td></td><td>(514)</td><td>588</td><td>(1,011)</td><td>(782)</td><td>244</td><td>97</td><td>64</td><td>183</td><td>129</td><td>81</td><td></td><td></td><td></td></tr><tr><td>Net income</td><td>1,402</td><td>1,183</td><td>2,051</td><td>1,977</td><td>1,363</td><td>2,036</td><td>2,563</td><td>3,090</td><td>1,813</td><td>2,446</td><td>2,997</td><td>12.3%</td><td>4.8%</td><td>3.1%</td></tr><tr><td>Growth, yoy %</td><td>2.4%</td><td>-15.6%</td><td>73.3%</td><td>-3.6%</td><td>-31.0%</td><td>49.3%</td><td>25.9%</td><td>20.5%</td><td>33.0%</td><td>34.9%</td><td>22.5%</td><td>16.3%</td><td>-9.0%</td><td>-2.0%</td></tr><tr><td>NPM</td><td>24.0%</td><td>17.9%</td><td>23.7%</td><td>16.5%</td><td>7.3%</td><td>9.2%</td><td>10.0%</td><td>10.5%</td><td>8.4%</td><td>9.8%</td><td>10.5%</td><td>0.8%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>EPS</td><td>15.00</td><td>9.02</td><td>11.14</td><td>7.64</td><td>5.26</td><td>7.86</td><td>9.89</td><td>11.92</td><td>7.00</td><td>9.44</td><td>11.57</td><td>12.3%</

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
