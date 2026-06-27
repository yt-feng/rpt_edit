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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# WEEKLY FUND FLOWS Tech Turbulence

## Global fund flows, week ending June 24

■ Flows into mutual funds and related investment products turned negative for equities but remained positive for fixed income.

Lexi Kanter  
+1(212)855-9701 | alexandra.kanter@gs.com GS & Co. LLC

Net flows into global equity funds turned slightly negative in the week ending June 24 (-\$5bn vs +\$126bn in the previous week). Within DM, US and Europe funds drove the net outflows. Within EM, Mainland China equity funds drove the net outflows while Taiwan equity funds saw net inflows. At the sector level, after several weeks of strong inflows, technology funds saw the largest net outflows (see chart of the week). We recently noted that the Dollar's resilience though software sell-off in February and tech-sector wobbles in recent days has reflected, in part, that the shock was not clearly US-negative, with global equities selling off alongside US equities. While we think equity volatility is likely to rise further, our expectation for a continued AI investment boom suggests that the relative equity impulse should remain a tailwind for the Dollar in our view.

\- Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have seen sustained inflows. In EM, hard-currency and local currency bond funds saw net inflows. Money market fund assets increased by -\$26bn.

Cross-border FX flows were broadly positive. USD, EUR and JPY saw the strongest net demand. CNY also saw net inflows after several weeks of net outflows.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>24-Jun</td><td>4wk avg</td><td>24-Jun</td></tr><tr><td>Equity</td><td>176,044</td><td>-4,992</td><td>0.14</td><td>-0.02</td></tr><tr><td>Fixed Income</td><td>96,021</td><td>16,374</td><td>0.24</td><td>0.17</td></tr><tr><td>of which: EM</td><td>9,434</td><td>3,220</td><td>0.33</td><td>0.45</td></tr><tr><td>Money Markets</td><td>119,227</td><td>-25,536</td><td>0.27</td><td>-0.23</td></tr><tr><td>FX Flows*</td><td>63,506</td><td>7,810</td><td>0.13</td><td>0.20</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds  
Source: EPFR, Haver Analytics, GS Global Investment Research

Chart of the Week  
![](images/2b9fa0ef68048af378bc5d45b1ece51c530be5730d8566116c6f2d816d03da61.jpg)  
Source: EPFR, Haver Analytics, GS Global Investment Research

## Global Fund Flow Trends

![](images/54b69ee64e165f9c9a2f762f9205f56fba202c3baab9d90809f99bee18aa2118.jpg)  
Source: EPFR, GS Global Investment Research

![](images/37befd72a4b8b76b40f1afb6ec7da226a252664b51b78ca11b6afd765d816b3f.jpg)  
Source: EPFR, GS Global Investment Research

![](images/7a23385b638c618de6d60cc13bcf90e9c3761e817608c9b07d97660e906bdf54.jpg)  
Source: EPFR, GS Global Investment Research

![](images/90ce7a9f798166dda67d3f4edd334512c640bb4db38bd36361b9d19e24f04818.jpg)  
Captures flows to sector-dedicated funds

![](images/73fbfdb5b4ddcdfe1a534676f2a90d63dc2ac39f4ef208c1123ef1eb34d23f0e.jpg)  
Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/3ad336da05b1d7442040736ca424787d92c08e9117e31cad09ac88cfa90d1cf6.jpg)  
Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

Source: EPFR, GS Global Investment Research  
![](images/90fa999810a30bacd9b79b52317b1af0e2493a30e74d3a3dd2d320736a9e705a.jpg)  
Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

![](images/d39cb9877c09557203fe1a96de2b1b47dc6da3f380c8e263fb169c3cdb26adf5.jpg)  
Source: EPFR, GS Global Investment Research

![](images/40180accf6b7308ef0fa930766b46bd547646260856665035e3d0d2a7135055d.jpg)  
Source: EPFR, GS Global Investment Research

## Total Unhedged Foreign Flows By Country

![](images/5bdde8a02aa6d6a2756560524d206e574370824899ba14db8846924634052f41.jpg)

![](images/95027443e08fc8d1bbfdd19e35704778959f25876f741a56f27f26a174cc0519.jpg)

![](images/55e0ce35f01bb06a8ca3241599ab3e56ca4142d176d2859588ab6a45f50f1c38.jpg)

![](images/d749c3da14defb52934ae22f782a5c753aefe08c67228225163c38aa0585c364.jpg)  
Source: EPFR, GS Global Investment Research

![](images/ce80ab0a9139497f15f5715074065b7d82ec74db12306c053f43745974c9edad.jpg)

![](images/4d7499ab1ed92cc0c24c2666fccd1dd910c61379b2d16e584799879e4238dbd4.jpg)

Net Unhedged Flows into US Equity Funds

![](images/458e915ec77757c26b64cbd7ba549235324ba82d341707e14eca90108a4c8b10.jpg)  
Source: EPFR, Haver Analytics, GS Global Investment Research

Fixed Income & Equity Flows

<table><tr><td rowspan="3"></td><td colspan="8">Global Fund Flows</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>24-Jun</td><td>17-Jun</td><td>10-Jun</td><td>3-Jun</td><td>4wk avg</td><td>24-Jun</td></tr><tr><td>Total Equity</td><td>176,044</td><td>-4,992</td><td>126,425</td><td>31,494</td><td>23,118</td><td>0.14</td><td>-0.02</td><td>3.11</td></tr><tr><td>Global Benchmarks1</td><td>57,967</td><td>14,361</td><td>15,116</td><td>11,857</td><td>16,633</td><td>0.19</td><td>0.19</td><td>2.50</td></tr><tr><td>Including US</td><td>43,945</td><td>9,300</td><td>8,317</td><td>11,963</td><td>14,364</td><td>0.21</td><td>0.18</td><td>2.85</td></tr><tr><td>Excluding US</td><td>14,022</td><td>5,061</td><td>6,799</td><td>-107</td><td>2,270</td><td>0.15</td><td>0.22</td><td>1.02</td></tr><tr><td>Developed Markets2</td><td>147,691</td><td>-8,294</td><td>120,798</td><td>15,132</td><td>20,055</td><td>0.18</td><td>-0.04</td><td>3.57</td></tr><tr><td>US</td><td>148,705</td><td>-8,548</td><td>119,189</td><td>17,350</td><td>20,714</td><td>0.23</td><td>-0.05</td><td>3.48</td></tr><tr><td>Western Europe</td><td>-7,419</td><td>-1,294</td><td>-1,173</td><td>-3,904</td><td>-1,048</td><td>-0.09</td><td>-0.06</td><td>-0.86</td></tr><tr><td>UK-dedicated</td><td>-1,296</td><td>-676</td><td>185</td><td>-163</td><td>-643</td><td>-0.10</td><td>-0.21</td><td>0.71</td></tr><tr><td>Other</td><td>-6,123</td><td>-618</td><td>-1,359</td><td>-3,740</td><td>-405</td><td>-0.09</td><td>-0.04</td><td>-0.94</td></tr><tr><td>Japan</td><td>976</td><td>475</td><td>1,166</td><td>784</td><td>-1,449</td><td>0.02</td><td>0.04</td><td>0.09</td></tr><tr><td>Other</td><td>5,428</td><td>1,073</td><td>1,616</td><td>901</td><td>1,838</td><td>0.32</td><td>0.26</td><td>1.92</td></tr><tr><td>Emerging Markets3</td><td>-29,614</td><td>-11,059</td><td>-9,489</td><td>4,506</td><td>-13,571</td><td>-0.24</td><td>-0.37</td><td>-1.57</td></tr><tr><td>Global EM Benchmarks</td><td>-6,896</td><td>-508</td><td>-570</td><td>-2,865</td><td>-2,953</td><td>-0.12</td><td>-0.04</td><td>-1.17</td></tr><tr><td>Mainland China</td><td>-31,188</td><td>-10,367</td><td>-9,051</td><td>-2,136</td><td>-9,633</td><td>-1.17</td><td>-1.58</td><td>-1.30</td></tr><tr><td>Taiwan</td><td>9,308</td><td>1,077</td><td>1,031</td><td>5,234</td><td>1,966</td><td>0.99</td><td>0.44</td><td>2.86</td></tr><tr><td>Korea</td><td>3,835</td><td>-536</td><td>-76</td><td>5,892</td><td>-1,444</td><td>0.53</td><td>-0.24</td><td>0.70</td></tr><tr><td>India</td><td>-1,562</td><td>-69</td><td>-416</td><td>-461</td><td>-616</td><td>-0.48</td><td>-0.08</td><td>-1.32</td></tr><tr><td>Brazil</td><td>-685</td><td>-196</td><td>-64</td><td>-198</td><td>-228</td><td>-0.72</td><td>-0.84</td><td>-1.34</td></tr><tr><td>Other</td><td>-2,427</td><td>-461</td><td>-344</td><td>-960</td><td>-662</td><td>-0.16</td><td>-0.12</td><td>-0.72</td></tr><tr><td colspan="9">Equity Sector Flows</td></tr><tr><td>Commodities/Materials</td><td>402</td><td>-1,082</td><td>1,879</td><td>-1,198</td><td>804</td><td>0.02</td><td>-0.42</td><td>-0.05</td></tr><tr><td>Consumer Goods</td><td>-5,632</td><td>74</td><td>-781</td><td>-2,039</td><td>-2,885</td><td>-0.67</td><td>0.04</td><td>-1.88</td></tr><tr><td>Energy</td><td>-4,559</td><td>-2,556</td><td>-526</td><td>-1,034</td><td>-443</td><td>-0.36</td><td>-0.82</td><td>-0.95</td></tr><tr><td>Financials</td><td>-1,023</td><td>-1,371</td><td>2,467</td><td>1,715</td><td>-3,833</td><td>-0.06</td><td>-0.31</td><td>-0.28</td></tr><tr><td>Health Care</td><td>1,599</td><td>687</td><td>536</td><td>1,109</td><td>-734</td><td>0.10</td><td>0.18</td><td>0.95</td></tr><tr><td>Industrials</td><td>9,190</td><td>-2,487</td><td>6,288</td><td>1,165</td><td>4,224</td><td>0.82</td><td>-0.87</td><td>1.69</td></tr><tr><td>Infrastructure</td><td>4,171</td><td>2,077</td><td>473</td><td>657</td><td>965</td><td>0.75</td><td>1.53</td><td>2.25</td></tr><tr><td>Real Estate</td><td>4,064</td><td>2,110</td><td>1,529</td><td>-295</td><td>720</td><td>0.17</td><td>0.36</td><td>2.51</td></tr><tr><td>Technology</td><td>34,976</td><td>-23,832</td><td>38,281</td><td>18,828</td><td>1,699</td><td>0.38</td><td>-1.00</td><td>2.75</td></tr><tr><td>Telecom</td><td>178</td><td>-1,144</td><td>953</td><td>824</td><td>-456</td><td>0.05</td><td>-1.38</td><td>-0.11</td></tr><tr><td>Utilities</td><td>771</td><td>346</td><td>-379</td><td>-463</td><td>1,268</td><td>0.10</td><td>0.19</td><td>0.39</td></tr><tr><td>High Beta4</td><td>2,550</td><td>-3,400</td><td>5,216</td><td>310</td><td>425</td><td>0.08</td><td>-0.49</td><td>-0.05</td></tr><tr><td>Low Beta4</td><td>-971</td><td>907</td><td>132</td><td>-1,779</td><td>-230</td><td>-0.04</td><td>0.13</td><td>0.36</td></tr><tr><td>Total Fixed Income</td><td>96,021</td><td>16,374</td><td>19,160</td><td>20,065</td><td>40,422</td><td>0.24</td><td>0.17</td><td>1.52</td></tr><tr><td>Developed Markets5</td><td>86,667</td><td>13,375</td><td>19,521</td><td>21,047</td><td>32,724</td><td>0.24</td><td>0.15</td><td>1.54</td></tr><tr><td>Government</td><td>13,107</td><td>-94</td><td>1,623</td><td>4,957</td><td>6,621</td><td>0.20</td><td>-0.01</td><td>0.26</td></tr><tr><td>Mortgage-backed</td><td>3,306</td><td>477</td><td>609</td><td>1,180</td><td>1,039</td><td>0.27</td><td>0.16</td><td>0.86</td></tr><tr><td>Municipal</td><td>7,389</td><td>1,226</td><td>2,509</td><td>1,593</td><td>2,060</td><td>0.26</td><td>0.17</td><td>1.58</td></tr><tr><td>Agg-type</td><td>31,225</td><td>7,592</td><td>3,861</td><td>7,172</td><td>12,599</td><td>0.27</td><td>0.26</td><td>1.37</td></tr><tr><td>IG Credit</td><td>8,509</td><td>865</td><td>3,771</td><td>1,446</td><td>2,427</td><td>0.18</td><td>0.08</td><td>0.49</td></tr><tr><td>High yield</td><td>7,087</td><td>1,857</td><td>2,096</td><td>-86</td><td>3,221</td><td>0.25</td><td>0.27</td><td>0.79</td></tr><tr><td>Bank loan</td><td>2,308</td><td>486</td><td>1,020</td><td>998</td><td>-195</td><td>0.32</td><td>0.27</td><td>0.23</td></tr><tr><td>Long-duration6</td><td>-5,852</td><td>-1,183</td><td>-1,046</td><td>537</td><td>-4,159</td><td>-0.24</td><td>-0.23</td><td>-2.16</td></tr><tr><td>Short-duration6</td><td>19,378</td><td>1,123</td><td>3,506</td><td>6,173</td><td>8,576</td><td>0.21</td><td>0.05</td><td>0.61</td></tr><tr><td>Inflation-protected</td><td>2,660</td><td>69</td><td>885</td><td>361</td><td>1,344</td><td>0.38</td><td>0.04</td><td>1.51</td></tr><tr><td>Emerging Markets</td><td>9,434</td><td>3,220</td><td>193</td><td>-242</td><td>6,264</td><td>0.33</td><td>0.45</td><td>1.23</td></tr><tr><td>Hard</td><td>1,296</td><td>578</td><td>267</td><td>-561</td><td>1,012</td><td>0.12</td><td>0.21</td><td>0.76</td></tr><tr><td>Blend</td><td>440</td><td>142</td><td>52</td><td>28</td><td>217</td><td>0.16</td><td>0.21</td><td>0.54</td></tr><tr><td>Local</td><td>7,699</td><td>2,500</td><td>-127</td><td>291</td><td>5,034</td><td>0.52</td><td>0.67</td><td>1.24</td></tr><tr><td>Money Markets</td><td>119,227</td><td>-25,536</td><td>25,110</td><td>-2,475</td><td>122,128</td><td>0.27</td><td>-0.23</td><td>0.49</td></tr></table>

1. Primarily MSCI World and MSCI ACWI benchmarks. 2. Sum of DM country- and region-dedicated funds; excludes global DM benchmark funds (e.g. MSCI World funds). 3. Sum of Global EM benchmark funds and EM country- and region-dedicated funds. 4. High beta funds include commodity, financial, & industrial sector funds. Low beta funds include consumer goods, real estate, & utility sector funds. 5. Benchmarks may include some investment grade EM bonds; categories below include DM & EM funds. 6. Long-duration includes long-term Agg-type, long-term corporate, and long-term government bond funds. Short-duration includes short-term Agg-type, short-term corporate, and short-term government bond funds.  
Source: EPFR, Haver Analytics, GS Global Investment Research

<table><tr><td rowspan="3"></td><td colspan="8">FX Flows1</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>24-Jun</td><td>17-Jun</td><td>10-Jun</td><td>3-Jun</td><td>4wk avg</td><td>24-Jun</td></tr><tr><td>Total</td><td>76,509</td><td>20,814</td><td>22,519</td><td>13,416</td><td>19,761</td><td>0.12</td><td>0.13</td><td>1.18</td></tr><tr><td>G10</td><td>72,079</td><td>16,767</td><td>20,480</td><td>14,275</td><td>20,557</td><td>0.17</td><td>0.16</td><td>2.40</td></tr><tr><td>USD</td><td>43,987</td><td>9,605</td><td>11,092</td><td>11,126</td><td>12,164</td><td>0.18</td><td>0.16</td><td>1.91</td></tr><tr><td>EUR</td><td>8,410</td><td>2,352</td><td>2,852</td><td>731</td><td>2,474</td><td>0.16</td><td>0.17</td><td>1.45</td></tr><tr><td>GBP</td><td>5,191</td><td>960</td><td>1,801</td><td>590</td><td>1,840</td><td>0.13</td><td>0.09</td><td>0.94</td></tr><tr><td>AUD</td><td>1,205</td><td>248</td><td>313</td><td>161</td><td>482</td><td>0.15</td><td>0.12</td><td>1.68</td></tr><tr><td>NZD</td><td>57</td><td>21</td><td>13</td><td>8</td><td>16</td><td>0.12</td><td>0.17</td><td>0.68</td></tr><tr><td>CAD</td><td>3,423</td><td>724</td><td>931</td><td>557</td><td>1,210</td><td>0.25</td><td>0.21</td><td>2.73</td></tr><tr><td>CHF</td><td>1,982</td><td>492</td><td>610</td><td>120</td><td>759</td><td>0.12</td><td>0.11</td><td>0.96</td></tr><tr><td>NOK</td><td>221</td><td>126</td><td>45</td><td>-106</td><td>156</td><td>0.05</td><td>0.12</td><td>-0.04</td></tr><tr><td>SEK</td><td>812</td><td>250</td><td>257</td><td>102</td><td>203</td><td>0.09</td><td>0.11</td><td>0.56</td></tr><tr><td>JPY</td><td>6,793</td><td>1,988</td><td>2,568</td><td>986</td><td>1,252</td><td>0.18</td><td>0.20</td><td>1.82</td></tr><tr><td>Asia</td><td>-2,490</td><td>2,758</td><td>-295</td><td>31</td><td>-4,983</td><td>-0.03</td><td>0.11</td><td>-0.46</td></tr><tr><td>CNY</td><td>-4,533</td><td>1,535</td><td>-1,761</td><td>-685</td><td>-3,623</td><td>-0.15</td><td>0.20</td><td>-0.91</td></tr><tr><td>HKD</td><td>528</td><td>154</td><td>179</td><td>68</td><td>126</td><td>0.11</td><td>0.13</td><td>1.18</td></tr><tr><td>INR</td><td>-2,177</td><td>-55</td><td>-454</td><td>-766</td><td>-902</td><td>-0.19</td><td>-0.02</td><td>-1.65</td></tr><tr><td>KRW</td><td>3,623</td><td>774</td><td>1,305</td><td>1,881</td><td>-336</td><td>0.18</td><td>0.15</td><td>1.41</td></tr><tr><td>MYR</td><td>-43</td><td>12</td><td>1</td><td>-51</td><td>-5</td><td>-0.03</td><td>0.03</td><td>-0.38</td></tr><tr><td>SGD</td><td>522</td><td>125</td><td>156</td><td>71</td><td>170</td><td>0.15</td><td>0.14</td><td>2.00</td></tr><tr><td>TWD</td><td>-670</td><td>129</td><td>180</td><td>-535</td><td>-444</td><td>-0.03</td><td>0.02</td><td>-0.62</td></tr><tr><td>THB</td><td>28</td><td>6</td><td>30</td><td>1</td><td>-9</td><td>0.02</td><td>0.01</td><td>0.04</td></tr><tr><td>IDR</td><td>222</td><td>69</td><td>58</td><td>60</td><td>36</td><td>0.11</td><td>0.14</td><td>0.58</td></tr><tr><td>PHP</td><td>11</td><td>9</td><td>11</td><td>-13</td><td>4</td><td>0.01</td><td>0.05</td><td>0.01</td></tr><tr><td>Americas</td><td>-625</td><td>252</td><td>29</td><td>-950</td><td>44</td><td>-0.04</td><td>0.06</td><td>-0.65</td></tr><tr><td>ARS</td><td>51</td><td>33</td><td>3</td><td>-4</td><td>19</td><td>0.15</td><td>0.37</td><td>0.22</td></tr><tr><td>BRL</td><td>-808</td><td>122</td><td>-8</td><td>-702</td><td>-221</td><td>-0.09</td><td>0.05</td><td>-0.95</td></tr><tr><td>MXN</td><td>-31</td><td>30</td><td>-17</td><td>-177</td><td>132</td><td>-0.01</td><td>0.03</td><td>-0.44</td></tr><tr><td>CLP</td><td>31</td><td>33</td><td>15</td><td>-40</td><td>23</td><td>0.02</td><td>0.10</td><td>-0.20</td></tr><tr><td>PEN</td><td>0</td><td>8</td><td>4</td><td>-28</td><td>16</td><td>0.00</td><td>0.04</td><td>-0.29</td></tr><tr><td>COP</td><td>132</td><td>26</td><td>32</td><td>0</td><td>74</td><td>0.15</td><td>0.12</td><td>0.51</td></tr><tr><td>EMEA</td><td>739</td><td>205</td><td>420</td><td>-29</td><td>143</td><td>0.07</td><td>0.08</td><td>0.16</td></tr><tr><td>CZK</td><td>222</td><td>14</td><td>166</td><td>10</td><td>33</td><td>0.26</td><td>0.06</td><td>2.03</td></tr><tr><td>HUF</td><td>45</td><td>15</td><td>18</td><td>-9</td><td>21</td><td>0.04</td><td>0.06</td><td>0.05</td></tr><tr><td>PLN</td><td>209</td><td>49</td><td>61</td><td>54</td><td>45</td><td>0.11</td><td>0.10</td><td>0.33</td></tr><tr><td>RON</td><td>60</td><td>8</td><td>17</td><td>3</td><td>33</td><td>0.09</td><td>0.05</td><td>0.28</td></tr><tr><td>RUB</td><td>4</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0.10</td><td>0.14</td><td>0.51</td></tr><tr><td>TRY</td><td>-36</td><td>24</td><td>14</td><td>-41</td><td>-33</td><td>-0.04</td><td>0.10</td><td>-0.51</td></tr><tr><td>ILS</td><td>305</td><td>69</td><td>97</td><td>59</td><td>81</td><td>0.16</td><td>0.14</td><td>1.18</td></tr><tr><td>ZAR</td><td>-69</td><td>26</td><td>46</td><td>-104</td><td>-38</td><td>-0.02</td><td>0.03</td><td>-0.43</td></tr><tr><td>Frontier</td><td>-69</td><td>11</td><td>-18</td><td>-65</td><td>3</td><td>-0.03</td><td>0.02</td><td>-0.45</td></tr><tr><td>UAH</td><td>7</td><td>1</td><td>1</td><td>-1</td><td>5</td><td>0.10</td><td>0.07</td><td>0.32</td></tr><tr><td>EGP</td><td>20</td><td>6</td><td>2</td><td>-2</td><td>14</td><td>0.06</td><td>0.07</td><td>0.02</td></tr><tr><td>NGN</td><td>10</td><td>3</td><td>2</td><td>-4</td><td>10</td><td>0.04</td><td>0.05</td><td>0.13</td></tr><tr><td>KWD</td><td>-4</td><td>0</td><td>1</td><td>-4</td><td>-2</td><td>-0.04</td><td>0.01</td><td>-0.43</td></tr><tr><td>SAR</td><td>-101</td><td>1</td><td>-24</td><td>-55</td><td>-24</td><td>-0.08</td><td>0.00</td><td>-0.70</td></tr></table>

Note: AUM is calculated at the domicile level.  
1. FX flows are measured as cross-border equity and fixed income fund flows (based on the domicile of underlying funds), excludi

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
