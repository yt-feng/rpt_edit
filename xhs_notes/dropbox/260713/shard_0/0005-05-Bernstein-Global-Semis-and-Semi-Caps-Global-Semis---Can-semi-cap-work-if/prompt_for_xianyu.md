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
# Global Semis and Semi Caps

# Global Semis – Can semi cap work if memory doesn't?

![](images/01c2fd49923a219a60b78b6a875607c31b75fb94c9a57078289430c0c88fc9d9.jpg)

![](images/681f6f40f3aa86cee9df6ddfae70fd56ce0b1a68ae6c76de6050e55ba1f4709e.jpg)

![](images/67ca0bbe25e5b9ba438bc3ac8cd7dd7d20959499f23f894360eae34fc6e672e0.jpg)

![](images/dd3c79ab9294e4db2682b05f4bec03b58ef1a5f4c077acde82227d66a8497949.jpg)

![](images/d4c30776e69a5f1a7a7cd5d41210eb1ca07f23cac9a9d3607ff0c1af41a194f1.jpg)

![](images/c3005f03265a940c256a366b70abd60be9534ffeff29d4536d608e91eadc2b48.jpg)

![](images/84db3a915f1d2f83af3a9df50252abd5bca50f6f1cec58f80d20a0bfe8724c35.jpg)

David Dai, CFA  
+852 2918 5704  
david.dai@bernsteinsg.com

Mark Li  
+852 2123 2645  
mark.li@bernsteinsg.com

Stacy A. Rasgon, Ph.D.  
+1 213 559 5917  
stacy.rasgon@bernsteinsg.com

Juho Hwang  
+81 3 6777 6980  
juho.hwang@bernsteinsg.com

Carmine Milano, CFA +44 20 7762 1857 carmine.milano@bernsteinsg.com

Edward Hou, CFA  
+852 2123 2623  
edward.hou@bernsteinsg.com

Yipin Cai, CFA +852 2123 2669 yipin.cai@bernsteinsg.com

In the current volatile market, many investors agree with our long semi cap call, but worry that they are all correlated with memory share prices anyway. Today's note reviews the share price history and debunks the myth.

Historical correlation of memory and SPE share prices is not high. We use top 3 companies and top 5 WFE companies as benchmark. During 2012-2018, memory and SPE companies correlation was only 0.4. Since 2019 the correlation has increased, but only to 0.6. Conversely, SPE and SOX have had consistently high correlation of 0.8-0.9.

SPE and memory share prices can go in different directions. There have been a few noticeable periods: From Jan 2015-Dec 2016 WFE was up 21.9% while memory was down 16.2%, gaining 38.2% outperformance in two years; In Jan 2021-Dec 2022, WFE was up 15.3% while memory was down 34%, gaining 49% outperformance in two years. While we are positive on both WFE and memory from here, investors can still benefit from diversification between WFE and memory, rather than worrying that both must go up and down together. This is especially the case considering that WFE growth is needed to add memory capacity, which is the cause of memory price volatility.

Mean reversion? Memory and WFE performance might be the same in the long run... as was the case during 2011-2019. While memory outperformed WFE by a whopping $661\%$ since June 2025, it was just reversing the lengthy underperformance during 2019-June 2025, and only managed to catch up in Feb 2026 when both were up 36x in 15 years. Now that memory has significantly outperformed WFE, if mean reversion happens it could favor WFE from here.

Fundamentally, we like WFE long here. Memory capex is clearly accelerating; SK hynix has recently announced their KRW 100tn (\~\$67bn) additional investment in their new Cheongju fabs, and the Korean government seems to be considering measures to support the initiatives from Samsung and SK hynix in building fabs in the Southwestern Korea. We see consensus upward revision potential for WFE market and company EPS through 2028, and we expect further growth ahead.

For memory, though we don't think LTA can help much (replay of our recent webinar), the shortage & the imminent HBM price hike will still bring significant upward earnings revisions. We still like Samsung, SK hynix, & Micron esp. after the recent pullback (report). We rate KIOXIA Underperform on valuation & long-term threat from China (report).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2" colspan="3"></td><td colspan="2">10 Jul 2026</td><td rowspan="2">TTM Rel.</td><td rowspan="2" colspan="4">Reported EPS</td><td rowspan="2" colspan="3">Reported P/E (x)</td></tr><tr><td>Closing</td><td>Price</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td><td>Price</td><td>Target</td><td>Perf.</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>8035.JP (Tokyo Electron)</td><td>O</td><td>JPY</td><td>72,940</td><td>59,200</td><td>124.0%</td><td>JPY</td><td>1,250.88</td><td>1,504.14</td><td>1,848.77</td><td>58.3</td><td>48.5</td><td>39.5</td></tr><tr><td>ASML.NA (ASML)</td><td>O</td><td>EUR</td><td>1,569.00</td><td>2,300.00</td><td>109.8%</td><td>EUR</td><td>24.72</td><td>32.73</td><td>48.68</td><td>63.5</td><td>47.9</td><td>32.2</td></tr><tr><td>ASML (ASML)</td><td>O</td><td>USD</td><td>1,797.32</td><td>2,623.00</td><td>103.5%</td><td>USD</td><td>27.95</td><td>37.01</td><td>55.05</td><td>56.3</td><td>42.5</td><td>28.6</td></tr><tr><td>005930.KS (SEC- Samsung)</td><td>O</td><td>KRW</td><td>286,500</td><td>440,000</td><td>322.4%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>43.3</td><td>5.9</td><td>3.7</td></tr><tr><td>005935.KS (SEC-Pref - Samsung)</td><td>O</td><td>KRW</td><td>194,300</td><td>374,000</td><td>237.0%</td><td>KRW</td><td>6,611.53</td><td>48,393</td><td>77,273</td><td>29.4</td><td>4.0</td><td>2.5</td></tr><tr><td>SMSN.LI (Samsung)</td><td>O</td><td>USD</td><td>4,834.00</td><td>7,350.00</td><td>303.0%</td><td>USD</td><td>116.15</td><td>812.39</td><td>1,290.80</td><td>41.6</td><td>6.0</td><td>3.7</td></tr><tr><td>000660.KS (SK hynix)</td><td>O</td><td>KRW</td><td>2,201,000</td><td>3,300,000</td><td>612.1%</td><td>KRW</td><td>60,341</td><td>395,677</td><td>568,862</td><td>36.5</td><td>5.6</td><td>3.9</td></tr><tr><td>MU (Micron)</td><td>O</td><td>USD</td><td>979.30</td><td>1,300.00</td><td>674.8%</td><td>USD</td><td>8.29</td><td>67.39</td><td>158.99</td><td>118.2</td><td>14.5</td><td>6.2</td></tr><tr><td>6857.JP (Advantest)</td><td>O</td><td>JPY</td><td>29,830</td><td>39,200</td><td>117.3%</td><td>JPY</td><td>514.52</td><td>735.65</td><td>870.09</td><td>58.0</td><td>40.5</td><td>34.3</td></tr><tr><td>6146.JP (DISCO)</td><td>O</td><td>JPY</td><td>72,560</td><td>85,000</td><td>20.0%</td><td>JPY</td><td>1,246.28</td><td>1,733.62</td><td>2,127.33</td><td>58.2</td><td>41.9</td><td>34.1</td></tr><tr><td>6920.JP (Lasertec)</td><td>O</td><td>JPY</td><td>44,380</td><td>50,000</td><td>84.3%</td><td>JPY</td><td>937.82</td><td>893.18</td><td>976.61</td><td>47.3</td><td>49.7</td><td>45.4</td></tr><tr><td>6525.JP (Kokusai)</td><td>O</td><td>JPY</td><td>10,840</td><td>8,240.00</td><td>192.2%</td><td>JPY</td><td>128.63</td><td>200.23</td><td>260.07</td><td>84.3</td><td>54.1</td><td>41.7</td></tr><tr><td>7735.JP (Screen)</td><td>M</td><td>JPY</td><td>18,150</td><td>12,600</td><td>156.9%</td><td>JPY</td><td>486.61</td><td>572.60</td><td>662.24</td><td>37.3</td><td>31.7</td><td>27.4</td></tr><tr><td>BESI.NA (Besi)</td><td>O</td><td>EUR</td><td>255.30</td><td>280.00</td><td>82.8%</td><td>EUR</td><td>1.66</td><td>3.34</td><td>5.84</td><td>153.8</td><td>76.4</td><td>43.7</td></tr><tr><td>AMAT (Applied Materials)</td><td>O</td><td>USD</td><td>602.50</td><td>525.00</td><td>183.6%</td><td>USD</td><td>9.42</td><td>12.17</td><td>15.56</td><td>64.0</td><td>49.5</td><td>38.7</td></tr><tr><td>LRCX (Lam Research)</td><td>O</td><td>USD</td><td>350.33</td><td>340.00</td><td>226.0%</td><td>USD</td><td>4.14</td><td>5.68</td><td>7.98</td><td>84.7</td><td>61.7</td><td>43.9</td></tr><tr><td>KLAC</td><td>O</td><td>USD</td><td>231.52</td><td>197.50</td><td>128.7%</td><td>USD</td><td>3.33</td><td>3.69</td><td>5.12</td><td>69.6</td><td>62.7</td><td>45.2</td></tr><tr><td>285A.JP (KIOXIA)</td><td>U</td><td>JPY</td><td>77,000</td><td>40,000</td><td>2959.6%</td><td>JPY</td><td>1,014.00</td><td>10,013</td><td>9,656.84</td><td>75.9</td><td>7.7</td><td>8.0</td></tr><tr><td>JPL</td><td></td><td></td><td>2,639.99</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,593.41</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,575.39</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,947.59</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM</td><td></td><td></td><td>1,807.54</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate TEL (TP=¥59,200), Advantest (TP=¥39,200), Disco (TP=¥85,000), Lasertec (TP=¥50,000), Kokusai (TP=¥8,240.00), ASML (TP=€2,300.00) and Besi (TP=€280.00) Outperform.

We rate Screen (TP=¥12,600) Market-Perform.

Samsung Electronics: We rate Samsung Electronics Outperform with price target of KRW 440,000.

SK hynix : We rate SK hynix Outperform with price target of KRW 3,300,000.

Micron: We rate Micron Outperform with price target of US\$1,300.00.

KIOXIA: We rate KIOXIA Underperform with price target of JPY 40,000.

AMAT (Outperform, \$525.00): Exposure to key inflections is strong and valuation vs peers remains attractive.

LRCX (Outperform, \$340.00): The company is benefiting from key inflections (GAA, packaging, HBM, NAND upgrades) and CY26/27

commentary seems supportive.

KLAC (Outperform, \$197.50 PT): Amid positive WFE trends KLAC possesses structural growth drivers, a strong and durable competitive position, lower China replacement risk, and disciplined capital allocation, warranting premium valuation, in our view.

## DETAILS

Share price has been volatile recently, especially for memory stocks. A big question from investors today is whether semicap can still work if memory stocks stop working. As such, we conducted a historical analysis and conclude that while the overall correlation between memory and semicap is strong, there has been multiple instances where semicap continued to work even though memory stocks were muted.

Exhibit 1 shows the correlation between memory, semicap and the broader semiconductor sector. It can be observed that the correlation between semicap and the overall semis has been historically tight — averaging at 0.82, while memory has historically shown a weaker correlation with other sectors, with both correlations (vs. WFE and vs. SOX) averaging at 0.54. The monthly returns show a similar pattern as in Exhibit 2. WFE vs. SOX move more or less in tandem, whereas it is somewhat noticeable that memory moves idiosyncratically to the broader semiconductor peers, often for an.

EXHIBIT 1: Correlation between memory and other parts of semis has historically been lower and more volatile.  
2011-2026: 12-month rolling correlation of daily returns (Memory, WFE, SOX)  
![](images/4bf430ac069f0a71c8522f1d0bc9f19264f233b0ea3bc0c4e58b7cd65215c9be.jpg)  
Memory basket includes MU, SK hynix, and SEC. WFE basket includes AMAT, LRCX, ASML, KLAC and TEL. Source: Bloomberg, Bernstein analysis.

EXHIBIT 2: WFE vs. SOX correlation is usually more stable, but memory tends to move more idiosyncratically.  
2011-2026: 12-month rolling correlation of monthly returns (Memory, WFE, SOX)  
![](images/730d1fb1dd602ed5a199cac9d3499f48fb6714e4ec45541e5d7e08c74af20f9c.jpg)  
Source: Bloomberg, Bernstein analysis.

As we established above that semicap and the broader SOX is tightly correlated, we shift our attention to how memory and semicap correlates. Exhibit 3 adds the short-term (3-month) and long-term (24-month) perspective of how the two subsectors behave in relation to each other. Although the relationship itself is positive, but it is easily identifiable that the two sectors move between periods of stronger and weaker correlations.

If we define periods of weaker fit as 12-month rolling correlation below 0.4, three periods (June 2013 - Nov 2014 / Nov 2015 - Jan 2016 / Jun 2017 - Dec 2017) fit under this category. Conversely, two periods of strong fit — as defined as 12-month rolling correlation of above 0.7 — appear during Apr 2019 - Dec 2019 / Mar 2020 - Mar 2021. Of note, July 2026 month-to-date averages at 0.6, slightly above historical mean of 0.54.

EXHIBIT 3: And if we look at shorter term, correlation between memory and WFE can be much more volatile.  
2011-2026: Rolling correlation of daily returns (Memory vs. WFE)  
![](images/a1e7b131eb473161ab420c3185c73fe7b7d4e790f959ecd0c9771afbf889a243.jpg)  
Source: Bloomberg, Bernstein analysis.

These periods of weak / strong fits (Exhibit 4) suggest that daily correlation should not be interpreted as cumulative return dispersion. Historically, low Memory-WFE correlation has not always resulted in large return divergence, and likewise, high Memory-WFE correlation has not necessarily resulted in similar returns. In particular, episodes #4 and #5 show that WFE can materially outperform memory even during strong-correlation periods, while episode #3 shows that weak daily correlation can still end up with almost identical cumulative returns. This indicates that sector correlation captures common semiconductor factor exposure, but relative returns remain driven heavily by subsector-specific drivers.

We believe this distinction is important because historical data shows that memory and WFE can share broad semiconductor beta while still delivering meaningfully different return outcomes. Therefore, the relevant investment question is not simply whether memory and WFE are correlated, but whether the current volatility is memory-specific or broad enough to impair WFE fundamentals as well.

EXHIBIT 4: Weak or strong correlation does not reliably predict Memory-WFE return gaps. Return dispersion depends more on subsector drivers than on correlation alone

<table><tr><td>Episode #</td><td>Start</td><td>End</td><td>Average Corr.</td><td>Memory Return</td><td>WFE Return</td><td>Memory – WFE Dispersion</td></tr><tr><td>1</td><td>01/06/2013</td><td>16/11/2014</td><td>0.320</td><td>66.9%</td><td>43.7%</td><td>23.2%</td></tr><tr><td>2</td><td>31/10/2015</td><td>29/01/2016</td><td>0.385</td><td>(22.2%)</td><td>(0.2%)</td><td>(22.1%)</td></tr><tr><td>3</td><td>23/06/2017</td><td>01/01/2018</td><td>0.353</td><td>19.9%</td><td>19.2%</td><td>0.7%</td></tr><tr><td>4</td><td>18/04/2019</td><td>13/12/2019</td><td>0.716</td><td>16.3%</td><td>40.6%</td><td>(24.3%)</td></tr><tr><td>5</td><td>11/03/2020</td><td>10/03/2021</td><td>0.753</td><td>73.9%</td><td>93.7%</td><td>(19.8%)</td></tr></table>

Source: Bloomberg, Bernstein analysis.

Now that we have established that semicap has historically been able to outperform memory both when the correlation is weak or strong, we move beyond the statistical observation and discuss what was actually happening in the real world during each period, dissecting different semiconductor cycles.

The cycle-regime table (Exhibit 5) is intended to answer that question. Rather than using rolling-correlation breakpoints that are purely statistical and somewhat artificial, the regimes below are grouped around recognizable semiconductor supply / demand backdrops such as memory up/downcycles, COVID / chip shortage, HBM and AI capex.

EXHIBIT 5: Most of the time memory and WFE moved in the same direction but there has been at least two cycles where they moved in completely different directions.

<table><tr><td>Cycle regime</td><td>Average 
Corr.</td><td>Memory Return</td><td>WFE Return</td><td>Memory – WFE Dispersion</td></tr><tr><td>2012-14 Memory consolidation / recovery</td><td>0.414</td><td>159.1%</td><td>118.2%</td><td>41.0%</td></tr><tr><td>2015-16 Semi downturn</td><td>0.457</td><td>(16.2%)</td><td>21.9%</td><td>(38.2%)</td></tr><tr><td>2017-19 Memory peak</td><td>0.542</td><td>108.9%</td><td>132.4%</td><td>(23.5%)</td></tr><tr><td>2020 COVID</td><td>0.739</td><td>36.9%</td><td>52.2%</td><td>(15.2%)</td></tr><tr><td>2021-22 Chip shortage / rates</td><td>0.600</td><t

[中间内容因长度限制已省略]

e you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively "Bloomberg"). Bloomberg or Bloomberg's licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg's licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
