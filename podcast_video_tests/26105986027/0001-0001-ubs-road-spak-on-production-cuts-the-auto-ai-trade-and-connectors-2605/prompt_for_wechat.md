你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 1800 字，允许上下浮动 15%。
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
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来社群继续拆完整报告。
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
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Road & Spak

# On production cuts, the auto AI trade, and connectors

# On production forecast changes

On Friday, S&P Global Mobility cut their 2026 global production forecast by -0.5% vs. prior to now show a -2.4% y/y decline vs. -1.8% prior. While this is still right around the 2% most suppliers guided to, the cut over 2Q-4Q26 was -1.2% y/y and shows a -2.6% y/y decline for the remaining 9 months. 1Q26 was revised higher by +1.6% (mainly driven by China, but also Middle East, S. Asia and Europe). So essentially, the "strong 1Q26" that eased some concerns was a little more cyclically aided than thought. And S&P indicated "early evidence that some production is effectively being pulled forward as OEMs guard against potential feedstock/part shortages." In looking at the cut over the remaining 3 quarters, \~41% of that is in China, 16% in S. Asia, 13% each in Europe, J/K and only 5% (\~42k units) in NA. So the mix of the cut isn't too bad for NA suppliers. Further, we'd note that our models are based on China/Europe numbers that are still \~1%/0.4% below S&P, though we are higher in NA. S&P did cut 2027 production by -1.3% and now shows +0.8% y/y growth but with more sizable cuts in NA/Europe which tend to matter more (and our models are built on an LVP number -1% below S&P. After speaking with S&P, our understanding is this was mostly macro driven cut with some caution on supply shortages. The macro factor certainly still has time to change. Our sense is that they did a larger cut now to avoid the potential for "death by a thousand cuts". This does set up potential for positive revisions if macro concerns ease.

# Is the auto AI trade dead already?

Our note from last week had a lot of traction and sparked many interesting conversations with clients. And auto names with other business angles away from auto (and particularly if associated with AI data centers) rallied (even if they did sell off on Friday). F was clearly the poster child. We do like their BESS opportunity (see our note from a month ago here and ask for our BESS model) given their CATL relationship for technology (which others are unlikely to be able to get now), the PTC qualification which lowers their cost, and our view that their product is likely FEOC compliant which makes it ITC (48E) eligible for customers creating another cost advantage. These factors may help "lock out" some competitors. While this won't be easy, they do appear to have the potential to do "cell through installation" in what today is a fairly fragmented value chain. But, even we can agree there is such a thing as too much too soon, so we weren't surprised to see F give some back on Friday. As for what's next, CEO Farley did mention on the 1Q26 call that "we are very active in contracting customers as we speak. We've had a lot of inbounds and a lot of interest..." Kentucky SOP is scheduled for 4Q27 so they do need to work on getting orders. Still, we'd keep expectations in check believing we could get a steady drip of additional information on BESS progress and customers. Still, the enthusiasm we've seen for F, BWA shows us that if a company can credibly capture the imagination of generalists on a non-auto theme, then when combined with inexpensive valuations there is the potential for re-rating. We believe this is because many other AI-linked names already screen more expensive. See our note linked above for what companies are doing outside of autos, but high on our list for potential beneficiaries from this theme are ST and APTV.

# Early feedback on APH, TEL note

Last Friday, we also made the case the APH and TEL were approaching valuation support which made them easier to own on an earning revision basis. See the note here. Additionally, we think they look attractive relative to other industrial AI names. Now, the AI opportunity here is more known, but also debated with the shift to optical from copper. We believe that for that reason, early feedback was more sympathetic to APH

# Equities

Americas

Automobiles

Joseph Spak, CFA

Analyst

joseph.spak@ubs.com

+1-212-713 3089

Robert Saltzman

Analyst

robert.saltzman@ubs.com

+1-212-713 2992

Alejandro Nuno

Associate Analyst

alejandro.nuno@ubs.com

+1-212-713 3886

Gabriel Gonzales, CFA

Associate Analyst

gabriel.gonzales@ubs.com

+1-212-713 4866

than TEL, given investors feel more comfortable with APH's portfolio and positioning in optical (CCS). However, we believe both look like they have good downside valuation support, and a positive bias to earnings revisions over the coming years.

# VALUATION

Figure 1: Comp Sheet   
(in USD \$mm, except per share data) 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Share Price 05/15/2026</td><td rowspan="2">Price Target</td><td rowspan="2">Div. Yield</td><td rowspan="2">Rating</td><td rowspan="2">All-in Return</td><td rowspan="2">Market Cap. (USD)</td><td rowspan="2">Enterprise Value (USD)</td><td colspan="3">EV/Sales</td><td colspan="3">EV/EBITDA</td><td colspan="3">P/E</td><td colspan="3">FCF Yield</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="21">US Automakers</td></tr><tr><td>Ford Motor Company</td><td>F</td><td>$13.47</td><td>$14</td><td>4.1%</td><td>Buy</td><td>8%</td><td>$54,836</td><td>$46,556</td><td>0.3x</td><td>0.2x</td><td>0.2x</td><td>3.6x</td><td>3.3x</td><td>3.1x</td><td>8.3x</td><td>7.2x</td><td>6.5x</td><td>1.8%</td><td>6.9%</td><td>6.9%</td></tr><tr><td>General Motors Company</td><td>GM</td><td>$75.21</td><td>$102</td><td>0.8%</td><td>Buy</td><td>36%</td><td>$69,644</td><td>$70,045</td><td>0.4x</td><td>0.4x</td><td>0.4x</td><td>3.7x</td><td>3.4x</td><td>3.3x</td><td>5.9x</td><td>5.3x</td><td>5.1x</td><td>10.5%</td><td>16.4%</td><td>15.3%</td></tr><tr><td>Mean</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.3x</td><td>0.3x</td><td>0.3x</td><td>3.6x</td><td>3.4x</td><td>3.2x</td><td>7.1x</td><td>6.3x</td><td>5.8x</td><td>6.1%</td><td>11.6%</td><td>11.1%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.3x</td><td>0.3x</td><td>0.3x</td><td>3.6x</td><td>3.4x</td><td>3.2x</td><td>7.1x</td><td>6.3x</td><td>5.8x</td><td>6.1%</td><td>11.6%</td><td>11.1%</td></tr><tr><td colspan="21">US BEV Automakers</td></tr><tr><td>Tesla, Inc.</td><td>TSLA</td><td>$425.05</td><td>$364</td><td>0.0%</td><td>Neutral</td><td>-14%</td><td>$1,503,827</td><td>$1,468,714</td><td>14.3x</td><td>12.4x</td><td>10.5x</td><td>95.1x</td><td>73.8x</td><td>54.4x</td><td>221.3x</td><td>174.1x</td><td>132.8x</td><td>-0.5%</td><td>-0.1%</td><td>0.1%</td></tr><tr><td>Rivian Automotive, Inc. Class A</td><td>RIVN</td><td>$14.09</td><td>$16</td><td>0.0%</td><td>Neutral</td><td>14%</td><td>$17,592</td><td>$17,232</td><td>2.4x</td><td>1.5x</td><td>1.0x</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Lucid Group, Inc.</td><td>LCID</td><td>$6.07</td><td>--</td><td>0.0%</td><td>Not rated</td><td>NA</td><td>$1,991</td><td>$4,007</td><td>2.0x</td><td>1.0x</td><td>0.6x</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Mean</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6.2x</td><td>5.0x</td><td>4.0x</td><td>95.1x</td><td>73.8x</td><td>54.4x</td><td>221.3x</td><td>174.1x</td><td>132.8x</td><td>-0.5%</td><td>-0.1%</td><td>0.1%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2.4x</td><td>1.5x</td><td>1.0x</td><td>95.1x</td><td>73.8x</td><td>54.4x</td><td>221.3x</td><td>174.1x</td><td>132.8x</td><td>-0.5%</td><td>-0.1%</td><td>0.1%</td></tr><tr><td colspan="21">US Auto Suppliers</td></tr><tr><td>Adient plc</td><td>ADNT</td><td>$21.06</td><td>$33</td><td>0.0%</td><td>Buy</td><td>57%</td><td>$1,670</td><td>$3,690</td><td>0.2x</td><td>0.2x</td><td>0.2x</td><td>4.1x</td><td>3.7x</td><td>NA</td><td>10.0x</td><td>6.2x</td><td>5.1x</td><td>8.0%</td><td>12.0%</td><td>14.6%</td></tr><tr><td>Aptiv PLC</td><td>APTV</td><td>$55.18</td><td>$80</td><td>0.0%</td><td>Buy</td><td>45%</td><td>$11,797</td><td>$15,165</td><td>1.2x</td><td>1.1x</td><td>1.1x</td><td>6.3x</td><td>6.0x</td><td>5.6x</td><td>9.4x</td><td>9.0x</td><td>8.5x</td><td>6.4%</td><td>9.6%</td><td>11.3%</td></tr><tr><td>Autoliv Inc.</td><td>ALV</td><td>$115.00</td><td>$110</td><td>2.9%</td><td>Neutral*</td><td>-1%</td><td>$8,637</td><td>$10,726</td><td>1.0x</td><td>0.9x</td><td>0.9x</td><td>6.7x</td><td>6.3x</td><td>5.8x</td><td>11.0x</td><td>9.5x</td><td>8.4x</td><td>8.4%</td><td>8.8%</td><td>9.6%</td></tr><tr><td>BorgWarner Inc.</td><td>BWA</td><td>$63.81</td><td>$61</td><td>1.0%</td><td>Neutral</td><td>-3%</td><td>$13,292</td><td>$15,466</td><td>1.1x</td><td>1.0x</td><td>1.0x</td><td>7.1x</td><td>6.7x</td><td>6.4x</td><td>12.3x</td><td>10.9x</td><td>9.9x</td><td>7.2%</td><td>8.0%</td><td>8.5%</td></tr><tr><td>Dana Incorporated</td><td>DAN</td><td>$33.27</td><td>$42</td><td>1.4%</td><td>Buy</td><td>28%</td><td>$3,899</td><td>$4,843</td><td>0.6x</td><td>0.6x</td><td>0.6x</td><td>6.0x</td><td>5.4x</td><td>5.0x</td><td>13.1x</td><td>9.3x</td><td>7.5x</td><td>9.7%</td><td>8.9%</td><td>9.9%</td></tr><tr><td>Dauch Corporation</td><td>DCH</td><td>$6.43</td><td>$9.50</td><td>0.0%</td><td>Buy</td><td>48%</td><td>$1,575</td><td>$6,392</td><td>0.6x</td><td>0.6x</td><td>0.6x</td><td>4.6x</td><td>4.2x</td><td>3.9x</td><td>8.5x</td><td>5.8x</td><td>4.4x</td><td>0.7%</td><td>20.3%</td><td>28.3%</td></tr><tr><td>Gentex Corporation</td><td>GNTX</td><td>$22.89</td><td>$26</td><td>2.1%</td><td>Neutral</td><td>16%</td><td>$4,840</td><td>$4,676</td><td>1.7x</td><td>1.7x</td><td>1.6x</td><td>7.6x</td><td>7.1x</td><td>6.7x</td><td>11.5x</td><td>10.3x</td><td>9.1x</td><td>8.3%</td><td>8.8%</td><td>8.8%</td></tr><tr><td>Lear Corporation</td><td>LEA</td><td>$134.44</td><td>$141</td><td>2.2%</td><td>Neutral</td><td>7%</td><td>$6,930</td><td>$9,772</td><td>0.4x</td><td>0.4x</td><td>0.4x</td><td>5.6x</td><td>5.2x</td><td>5.0x</td><td>9.1x</td><td>7.8x</td><td>7.0x</td><td>8.1%</td><td>9.2%</td><td>10.3%</td></tr><tr><td>Magna International Inc.</td><td>MGA</td><td>$60.69</td><td>$62</td><td>3.1%</td><td>Neutral</td><td>5%</td><td>$16,876</td><td>$22,767</td><td>0.5x</td><td>0.5x</td><td>0.5x</td><td>5.3x</td><td>5.2x</td><td>4.9x</td><td>9.0x</td><td>8.0x</td><td>7.3x</td><td>10.2%</td><td>10.8%</td><td>12.1%</td></tr><tr><td>Mobileye Global, Inc. Class A</td><td>MBLY</td><td>$10.08</td><td>$10</td><td>0.0%</td><td>Neutral</td><td>-1%</td><td>$8,231</td><td>$6,887</td><td>3.5x</td><td>3.1x</td><td>2.5x</td><td>24.1x</td><td>17.9x</td><td>11.0x</td><td>37.1x</td><td>28.1x</td><td>16.0x</td><td>2.0%</td><td>3.6%</td><td>5.4%</td></tr><tr><td>PHINIA Inc.</td><td>PHIN</td><td>$76.89</td><td>$76</td><td>1.5%</td><td>Neutral</td><td>0%</td><td>$2,976</td><td>$3,622</td><td>1.0x</td><td>1.0x</td><td>1.0x</td><td>7.0x</td><td>6.7x</td><td>6.7x</td><td>12.6x</td><td>11.4x</td><td>10.7x</td><td>7.9%</td><td>8.4%</td><td>9.0%</td></tr><tr><td>QuantumScape Corporation Class A</td><td>QS</td><td>$8.02</td><td>$2.50</td><td>0.0%</td><td>Sell</td><td>-69%</td><td>$4,900</td><td>$4,065</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Visteon Corporation</td><td>VC</td><td>$111.83</td><td>$130</td><td>1.1%</td><td>Buy</td><td>17%</td><td>$3,053</td><td>$2,911</td><td>0.8x</td><td>0.7x</td><td>0.7x</td><td>6.1x</td><td>5.7x</td><td>5.4x</td><td>13.1x</td><td>11.5x</td><td>10.4x</td><td>5.7%</td><td>6.7%</td><td>7.0%</td></tr><tr><td>Versigent PLC</td><td>VGNT</td><td>$43.08</td><td>$49</td><td>0.0%</td><td>Buy</td><td>14%</td><td>$3,054</td><td>$5,191</td><td>0.6x</td><td>0.5x</td><td>0.5x</td><td>5.3x</td><td>4.9x</td><td>4.6x</td><td>6.3x</td><td>6.2x</td><td>5.6x</td><td>8.8%</td><td>13.2%</td><td>12.4%</td></tr><tr><td>Mean (ex-MBLY)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.8x</td><td>0.8x</td><td>0.8x</td><td>6.0x</td><td>5.6x</td><td>5.4x</td><td>10.5x</td><td>8.8x</td><td>7.8x</td><td>7.4%</td><td>10.4%</td><td>11.8%</td></tr><tr><td>Median (ex-MBLY)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.7x</td><td>0.7x</td><td>0.6x</td><td>6.0x</td><td>5.5x</td><td>5.4x</td><td>10.5x</td><td>9.1x</td><td>7.9x</td><td>8.0%</td><td>9.0%</td><td>10.1%</td></tr><tr><td colspan="21">Connectors &amp; Sensors</td></tr><tr><td>Amphenol Corporation Class A</td><td>APH</td><td>$125.68</td><td>$178</td><td>0.4%</td><td>Buy</td><td>42%</td><td>$162,089</td><td>$176,352</td><td>5.3x</td><td>4.7x</td><td>4.2x</td><td>16.2x</td><td>13.8x</td><td>12.9x</td><td>26.5x</td><td>22.6x</td><td>20.1x</td><td>3.8%</td><td>4.6%</td><td>5.1%</td></tr><tr><td>TE Connectivity plc</td><td>TEL</td><td>$203.55</td><td>$261</td><td>1.5%</td><td>Buy</td><td>30%</td><td>$60,046</td><td>$65,345</td><td>3.3x</td><td>3.1x</td><td>2.9x</td><td>12.4x</td><td>11.3x</td><td>10.2x</td><td>18.2x</td><td>16.2x</td><td>14.6x</td><td>5.4%</td><td>6.2%</td><td>7.0%</td></tr><tr><td>Sensata Technologies Holding PLC</td><td>ST</td><td>$48.54</td><td>$48</td><td>1.0%</td><td>Buy</td><td>0%</td><td>$7,116</td><td>$9,373</td><td>2.4x</td><td>2.3x</td><td>2.2x</td><td>10.5x</td><td>10.1x</td><td>9.3x</td><td>13.1x</td><td>12.1x</td><td>11.1x</td><td>6.8%</td><td>7.9%</td><td>9.3%</td></tr><tr><td>Mean</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3.7x</td><td>3.4x</td><td>3.1x</td><td>13.1x</td><td>11.7x</td><td>10.8x</td><td>19.3x</td><td>16.9x</td><td>15.3x</td><td>5.4%</td><td>6.2%</td><td>7.1%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3.3x</td><td>3.1x</td><td>2.9x</td><td>12.4x</td><td>11.3x</td><td>10.2x</td><td>18.2x</td><td>16.2x</td><td>14.6x</td><td>5.4%</td><td>6.2%</td><td>7.0%</td></tr><tr><td colspan="21">Auto Internet</td></tr><tr><td>CarGurus, Inc. Class A</td><td>CARG</td><td>$28.92</td><td>$37</td><td>0.0%</td><td>Neutral</td><td>28%</td><td>$2,750</td><td>$2,678</td><td>2.6x</td><td>2.4x</td><td>2.2x</td><td>8.0x</td><td>7.1x</td><td>6.5x</td><td>11.4x</td><td>9.9x</td><td>9.0x</td><td>9.4%</td><td>12.3%</td><td>14.6%</td></tr><tr><td>Cars.com, Inc.</td><td>CARS</td><td>$10.00</td><td>$12</td><td>0.0%</td><td>Neutral</td><td>20%</td><td>$596</td><td>$983</td><td>1.3x</td><td>1.3x</td><td>1.3x</td><td>4.6x</td><td>4.5x</td><td>4.4x</td><td>4.6x</td><td>3.9x</td><td>4.4x</td><td>23.7%</td><td>24.8%</td><td>24.0%</td></tr><tr><td>Carvana Co. Class A</td><td>CVNA</td><td>$67.83</td><td>$104</td><td>0.0%</td><td>Buy</td><td>53%</td><td>$76,507</td><td>$79,419</td><td>2.9x</td><td>2.3x</td><td>1.9x</td><td>26.6x</td><td>20.1x</td><td>16.3x</td><td>44.8x</td><td>32.7x</td><td>24.4x</td><td>1.3%</td><td>1.8%</td><td>2.0%</td></tr><tr><td>Autotrader Group PLC</td><td>AUTO-GB</td><td>£4.91</td><td>£4.70</td><td>2.2%</td><td>Sell**</td><td>-2%</td><td>$6,555</td><td>$6,535</td><td>7.4x</td><td>NM</td><td>NM</td><td>11.3x</td><td>NM</td><td>NM</td><td>12.7x</td><td>11.5x</td><td>NA</td><td>6.8%</td><td>7.2%</td><td>NA</td></tr><tr><td>Mean</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3.6x</td><td>2.0x</td><td>1.8x</td><td>12.6x</td><td>10.5x</td><td>9.1x</td><td>18.4x</td><td>14.5x</td><td>12.6x</td><td>10.3%</td><td>11.5%</td><td>13.6%</td></tr><tr><td>Median</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2.7x</td><td>2.3x</td><td>1.9x</td><td>9.7x</td><td>7.1x</td><td>6.5x</td><td>12.0x</td><td>10.7x</td><td>9.0x</td><td>8.1%</td><td>9.8%</td><td>14.6%</td></tr></table>

Source: FactSet, Visible Alpha, UBS estimates. Note: Priced midday as of 05/15/26. Trading multiples based on consensus estimates, except F/GM EV/EBITDA based on UBS forecast. For F/GM EV/EBITDA, EV calculated as market cap. + auto net debt + NCI - 0.7x book value of captive finance company - underfunded pension/OPEB and EBITDA is Auto EBITDA + non service pension costs/(income). For CVNA, market cap utilizes current price \* class A shares outstanding assuming full conversion of LLC units. ADNT and TEL are calendarized from FY Sept.; \*ALV is covered by UBS analyst Juan Perez-Carrascosa; \*\*AUTO-GB is covered by UBS analyst Jo Barnet-Lamb.

# PERFORMANCE

Figure 2: US Automotive coverage stock performance, past week   
![](images/c2bc1f5df21188b276acb6c1252784a590572b648f9c6a7220bfb3c3a780f269.jpg)

<details>
<summary>bar</summary>

| Stock | Performance |
|-------|-------------|
| F     | 9%          |
| MBLY  | 8%          |
| ST    | 7%          |
| QS    | 6%          |
| BWA   | 5%          |
| S&P 500 | 0%        |
| TSLA  | -1%         |
| GNTX  | -2%         |
| APH   | -2%         |
| TEL   | -2%         |
| DCH   | -2%         |
| VC    | -2%         |
| RIVN  | -2%         |
| DAN   | -3%         |
| PHIN  | -4%         |
| MGA   | -4%         |
| LEA   | -4%         |
| GM    | -4%         |
| APTV  | -4%         |
| ADNT  | -6%         |
| CVNA  | -13%        |
| CARS  | -14%        |
| CARG  | -15%        |
</details>

Source: FactSet

Figure 3: US Automotive coverage stock performance, last 3 months   
![](images/db8adb79069d829fad84f721b8365817f9d646450956943a0d3179aa48784139.jpg)

<details>
<summary>bar</summary>

| Stock | Performance |
|-------|-------------|
| ST    | 30%         |
| S&P 500 | 9%          |
| MBLY  | 8%          |
| CARG  | 8%          |
| VC    | 6%          |
| QS    | 3%          |
| BWA   | 2%          |
| TSLA  | 2%          |
| PHIN  | 2%          |
| DAN   | 0%          |
| CVNA  | -1%         |
| LEA   | -3%         |
| F     | -5%         |
| GM    | -7%         |
| GNTX  | -8%         |
| CARS  | -9%         |
| DCH   | -11%        |
| MGA   | -12%        |
| APH   | -15%        |
| TEL   | -15%        |
| ADNT  | -21%        |
| RIVN  | -22%        |
| APTV  | -23%        |
</details>

Source: FactSet

Figure 4: US Automotive coverage stock performance, last 12 months   
![](images/6bebe3f64f8914e03970f98bdf7102d3b7f156d05236e7f6960ebc732c0ac134.jpg)

<details>
<summary>bar</summary>

Stock performance, 12 months
| Stock | Performance (%) |
| :--- | :--- |
| DAN | 109 |
| BWA | 94 |
| QS | 87 |
| ST | 76 |
| PHIN | 73 |
| MGA | 67 |
| GM | 51 |
| APH | 46 |
| DCH | 44 |
| LEA | 43 |
| ADNT | 38 |
| VC | 29 |
| S&P 500 | 25 |
| F | 25 |
| TSLA | 24 |


[中间内容因长度限制已省略]

ed Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS Securities LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS Securities LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

# Credit Suisse Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of Credit Suisse Wealth Management. Your personal data will be processed in accordance with the Credit Suisse privacy statement accessible at your domicile through the official Credit Suisse website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local Credit Suisse entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by Credit Suisse Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. Credit Suisse Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/a9ce15564d72a064fec4837defbcac69f5b48ef086a37dc1a8f974c8b725a4c6.jpg)
"""
