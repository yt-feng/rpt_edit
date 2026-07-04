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
- 已识别机构名：`UBS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# UBS Global I/O Semiconductors Cloud AI: TSMC and ASE driving faster CoWoS expansion, unlocking larger TAM

## CoWoS capacity upside in 2026-27 across TSMC and ASE

We view TSMC and broader industry CoWoS expansion as a leading indicator of cloud AI demand over the next 2-3 years. Capacity expansion over the next 12-18 months is progressing faster than we expected a month ago, suggesting stronger underlying cloud AI demand. TSMC's CoWoS capacity expansion is re-accelerating and we now expect capacity to reach 130k/180k wpm by end-2026/27 vs our prior estimates of 120k / 150k wpm. We believe this reflects a much larger advanced packaging TAM over the next several years, with a meaningful portion likely to remain on CoWoS even as Intel EMIB-T and TSMC CoPoS enter mass production in 2028. ASE has also been accelerating its full-process capacity expansion for 2027. We now forecast its full-process CoWoS capacity to more than double from 20kwpm at end-2026E to \~50kwpm end-2027E vs prior estimate of 40kwpm. (See our ASE note). Overall, we estimate industry CoWoS capacity may rise from 160kwpm at end-2026 to 250kwpm by end-2027.

## Robust server CPU demand; Nvidia Rubin ramp to accelerate in H226

On the demand side, we believe server CPU continues to show upside into 2027. ASE's faster CoWoS expansion should be underpinned by higher AMD Venice volumes, which we estimate at 4mn units in 2027, up from 1.3mn in 2026. AMD's CoWoS demand could grow 232% in 2027E with a strong ramp of Venice server CPU and MI450/455. We also lift Nvidia's Vera CPU units to 5.5mn units in 2027 from 1.6mn in 2026, implying 57% growth in Nvidia's CoWoS demand in 2027. Rubin GPU ramp was slower in Q226 due to redesigns, but we anticipate a steep pick up in H226 to reach 2.1mn for 2026. We forecast Google TPU chipset units to rise from 4.1mn in 2026 to 9.0mn in 2027, with MediaTek expected to support 4mn units of TPU v8t capacity. Amazon Trainium 3 demand is growing and we lift 2026/27E unit estimates to 1.8mn/2.8mn (from 1.7m/2.3m). See our CoWoS supply vs demand analysis in Figure 2-Figure 12.

## More diversified supply ahead, but TSMC should remain the largest player

As previously noted, we anticipate advanced packaging supply to become more diversified from 2027-28 onward. We see increasing opportunities for ASE and Amkor in H226/2027, mainly driven by server CPUs. Intel's EMIB-T is gaining traction, but we believe Intel may face resource and capacity constraints in 2028, and will likely prioritise internal products and Google/MediaTek's TPU v9 initially. Overall, we think TSMC's advanced packaging sales should sustain solid \~50% growth over the next five years on its leading market share, rising content through 3D stacking, and tech upgrades such as CoPoS and co-packaged optics.

## Stock recommendations; ASE/GPTC price target raised to NT\$835/\$5,000

Along the semiconductor supply chain for cloud AI, our top picks are TSMC (the industry's leading cloud AI foundry), MediaTek (design services for Google TPU), and ASE (advanced packaging & testing). We estimate backend, including advanced packaging, to reach \~12%/15% of TSMC sales in 2026/27E, and our recent Q226 earnings preview raised our sales and EPS estimates on stronger cloud AI demand. MediaTek is a Buy and a Key Call. We lift our ASE price target to NT\$835 from NT\$660. Critical equipment suppliers for advanced packaging & testing could also benefit from the cloud AI ramp-up, and we like GPTC, Chroma, Hon Precision, and ASMPT. We raise our GPTC price target to NT\$5,000 (from NT\$4,000) based on 33x 2027-28E PE (vs 33x 2027E PE previously). See page 6. KYEC remains well positioned in the final test space. We like Aspeed for its strong BMC outlook, GUC for its robust Google CPU upside potential, and Alchip for its Amazon Trainium3 and Trainium4 opportunities.

## Equities

Asia
Semiconductors

Sunny Lin
Analyst
sunny.lin@ubs.com
+886-2-8722 7346

Randy Abrams
Analyst
randy.abrams@ubs.com
+886-2-8722 7338

Nicolas Gaudois
Analyst
nicolas.gaudois@ubs.com
+65-6495 5148

Timothy Arcuri
Analyst
timothy.arcuri@ubs.com
+1-415-352 5676

Jerry Su
Analyst
jerry.su@ubs.com
+886-28-722 7306

Shingo Hirata, CFA
Analyst
shingo.hirata@ubs.com
+81-3-5208 6224

Ryan Sun
Associate Analyst
ryan-za.sun@ubs.com
+886-2-8722 7267

Christine Chen
Associate Analyst
christine.chen@ubs.com
+886-2-8722 7352

Diana Chang
Analyst
diana.chang@ubs.com
+886-2-8722 7335

Jimmy Yoon
Analyst
jimmy.yoon@ubs.com
+65-6495 4617

Figure 1: Valuation comparison

<table><tr><td rowspan="2">Company name</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">Market cap (US$m)</td><td rowspan="2">Price target (LC)</td><td rowspan="2">Share price (LC)</td><td colspan="2">EPS growth (%)</td><td colspan="2">P/E (x)</td><td colspan="2">P/BV (x)</td><td colspan="2">ROE (%)</td><td colspan="2">Dividend yield (%)</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="16">Foundry</td></tr><tr><td>TSMC</td><td>2330.TW</td><td>Buy</td><td>1,961,379</td><td>3,400</td><td>2,410</td><td>50.7</td><td>39.5</td><td>24.1</td><td>17.3</td><td>8.5</td><td>6.3</td><td>40.5</td><td>41.7</td><td>0.9</td><td>1.2</td></tr><tr><td colspan="16">Fabless</td></tr><tr><td>Alchip</td><td>3661.TW</td><td>Buy</td><td>10,670</td><td>6,000</td><td>4,180</td><td>122.6</td><td>37.9</td><td>27.1</td><td>19.7</td><td>6.7</td><td>5.5</td><td>27.3</td><td>30.7</td><td>0.9</td><td>0.8</td></tr><tr><td>Aspeed</td><td>5274.TWO</td><td>Buy</td><td>19,569</td><td>22,000</td><td>16,495</td><td>88.4</td><td>69.9</td><td>84.3</td><td>49.6</td><td>51.9</td><td>32.7</td><td>75.5</td><td>80.9</td><td>0.5</td><td>0.9</td></tr><tr><td>GUC</td><td>3443.TW</td><td>Buy</td><td>20,367</td><td>6,260</td><td>4,845</td><td>84.2</td><td>99.4</td><td>93.4</td><td>46.9</td><td>37.7</td><td>23.4</td><td>46.1</td><td>61.7</td><td>0.3</td><td>0.4</td></tr><tr><td>MediaTek</td><td>2454.TW</td><td>Buy</td><td>213,677</td><td>6,500</td><td>4,245</td><td>(3.4)</td><td>183.2</td><td>66.4</td><td>23.5</td><td>17.3</td><td>12.8</td><td>25.7</td><td>62.7</td><td>1.3</td><td>1.2</td></tr><tr><td colspan="16">Semi-backend</td></tr><tr><td>ASE</td><td>3711.TW</td><td>Buy</td><td>94,923</td><td>835</td><td>680</td><td>87.6</td><td>66.5</td><td>38.7</td><td>23.2</td><td>7.7</td><td>6.4</td><td>20.9</td><td>30.0</td><td>0.9</td><td>1.7</td></tr><tr><td>KYEC</td><td>2449.TW</td><td>Buy</td><td>12,951</td><td>380</td><td>338</td><td>57.0</td><td>69.7</td><td>33.0</td><td>19.4</td><td>7.4</td><td>6.0</td><td>23.5</td><td>34.1</td><td>1.7</td><td>2.0</td></tr><tr><td colspan="16">Equipment</td></tr><tr><td>ASMPT</td><td>0522.HK</td><td>Buy</td><td>12,695</td><td>200</td><td>240</td><td>106.1</td><td>41.2</td><td>45.7</td><td>32.4</td><td>5.5</td><td>5.0</td><td>12.4</td><td>16.1</td><td>0.6</td><td>1.1</td></tr><tr><td>Chroma ATE</td><td>2360.TW</td><td>Buy</td><td>28,840</td><td>2,960</td><td>2,160</td><td>63.5</td><td>37.6</td><td>47.7</td><td>34.6</td><td>21.3</td><td>16.4</td><td>51.2</td><td>53.4</td><td>0.4</td><td>0.9</td></tr><tr><td>GPTC</td><td>3131.TWO</td><td>Buy</td><td>3,328</td><td>5,000</td><td>3,630</td><td>72.6</td><td>57.5</td><td>46.3</td><td>29.4</td><td>17.2</td><td>13.0</td><td>41.7</td><td>50.3</td><td>0.9</td><td>1.5</td></tr><tr><td>Hon Precision</td><td>7769.TW</td><td>Buy</td><td>36,535</td><td>8,800</td><td>6,470</td><td>46.8</td><td>87.0</td><td>57.8</td><td>30.9</td><td>16.7</td><td>12.5</td><td>31.6</td><td>46.3</td><td>0.8</td><td>1.2</td></tr></table>

Source: LSEG, UBS estimates. Note: Priced as of 30 June 2026.

Figure 2: Total CoWoS interposer wafer demand

<table><tr><td>Interposer Wafer Demand (kps)</td><td>Q126E</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Nvidia</td><td>128</td><td>154</td><td>231</td><td>278</td><td>256</td><td>296</td><td>335</td><td>351</td><td>174</td><td>444</td><td>791</td><td>1,238</td></tr><tr><td>AMD</td><td>11</td><td>11</td><td>30</td><td>77</td><td>86</td><td>107</td><td>110</td><td>124</td><td>37</td><td>42</td><td>129</td><td>427</td></tr><tr><td>ASICs and others</td><td>77</td><td>97</td><td>105</td><td>108</td><td>162</td><td>202</td><td>218</td><td>226</td><td>147</td><td>193</td><td>387</td><td>809</td></tr><tr><td>Google TPU - Broadcom</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>60</td><td>76</td><td>195</td><td>338</td></tr><tr><td>Google TPU - MediaTek</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0</td><td>0</td><td>20</td><td>182</td></tr><tr><td>Amazon Trainium - Alchip</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>26</td><td>5</td><td>72</td><td>132</td></tr><tr><td>Amazon Trainium - Marvell</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>17</td><td>38</td><td>18</td><td>4</td></tr><tr><td>Meta</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>7</td><td>8</td><td>6</td><td>25</td></tr><tr><td>Others</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>38</td><td>66</td><td>67</td><td>78</td></tr><tr><td>Total</td><td>216</td><td>262</td><td>365</td><td>463</td><td>504</td><td>605</td><td>664</td><td>702</td><td>358</td><td>679</td><td>1,307</td><td>2,475</td></tr></table>

Source: Company data, UBS estimates

Figure 3: Breakdown of CoWoS demand

<table><tr><td>ASIC vendor as a % of CoWoS wafers demand</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Google</td><td>17%</td><td>11%</td><td>16%</td><td>21%</td></tr><tr><td>Broadcom</td><td>17%</td><td>11%</td><td>15%</td><td>14%</td></tr><tr><td>MediaTek</td><td>0%</td><td>0%</td><td>2%</td><td>7%</td></tr><tr><td>Amazon</td><td>12%</td><td>6%</td><td>7%</td><td>6%</td></tr><tr><td>Alchip</td><td>7%</td><td>1%</td><td>6%</td><td>5%</td></tr><tr><td>Marvell</td><td>5%</td><td>6%</td><td>1%</td><td>0%</td></tr><tr><td>Meta</td><td>2%</td><td>1%</td><td>0%</td><td>1%</td></tr><tr><td>Intel / Habana</td><td>2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Microsoft</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Tesla</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Others</td><td>8%</td><td>9%</td><td>5%</td><td>5%</td></tr><tr><td>Total ASIC</td><td>41%</td><td>28%</td><td>30%</td><td>33%</td></tr><tr><td colspan="5">GPU vendors as a % of CoWoS wafers demand</td></tr><tr><td>Nvidia</td><td>49%</td><td>65%</td><td>61%</td><td>50%</td></tr><tr><td>AMD</td><td>10%</td><td>6%</td><td>10%</td><td>17%</td></tr><tr><td>Total GPU</td><td>59%</td><td>72%</td><td>70%</td><td>67%</td></tr><tr><td>Total</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr></table>

Source: Company data, UBS estimates

Figure 4: Nvidia's supply chain build units

<table><tr><td>Nvidia Supply Chain Build Units (k chips)</td><td>Q126E</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Ampere</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>134</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Hopper</td><td>180</td><td>251</td><td>215</td><td>100</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4,086</td><td>1,402</td><td>746</td><td>0</td></tr><tr><td>Blackwell B200/B300 and GB200/GB300</td><td>1,703</td><td>1,855</td><td>1,715</td><td>953</td><td>350</td><td>111</td><td>81</td><td>0</td><td>314</td><td>5,520</td><td>6,226</td><td>543</td></tr><tr><td>Rubin R200 and VR200</td><td>0</td><td>70</td><td>678</td><td>1,339</td><td>1,544</td><td>1,797</td><td>1,450</td><td>672</td><td>0</td><td>0</td><td>2,087</td><td>5,463</td></tr><tr><td>Rubin R300 and VR300</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>137</td><td>639</td><td>1,416</td><td>0</td><td>0</td><td>0</td><td>2,191</td></tr><tr><td>Vera CPU</td><td>0</td><td>100</td><td>428</td><td>1,054</td><td>1,025</td><td>1,180</td><td>1,543</td><td>1,754</td><td>0</td><td>0</td><td>1,582</td><td>5,502</td></tr><tr><td>Total</td><td>1,883</td><td>2,275</td><td>3,036</td><td>3,446</td><td>2,919</td><td>3,226</td><td>3,713</td><td>3,841</td><td>4,534</td><td>6,921</td><td>10,641</td><td>13,699</td></tr></table>

Source: Company data, UBS estimates

Figure 5: AMD's supply chain build units

<table><tr><td>AMD Supply Chain Build Units (k chips)</td><td>Q126E</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>MI300 + MI325X + MI308X+MI355X</td><td>163</td><td>170</td><td>87</td><td>89</td><td>93</td><td>82</td><td>15</td><td>4</td><td>544</td><td>626</td><td>508</td><td>194</td></tr><tr><td>MI400</td><td>0</td><td>0</td><td>38</td><td>225</td><td>295</td><td>433</td><td>415</td><td>369</td><td>0</td><td>0</td><td>263</td><td>1,513</td></tr><tr><td>MI500</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>66</td><td>177</td><td>0</td><td>0</td><td>0</td><td>242</td></tr><tr><td>Venice CPU</td><td>0</td><td>0</td><td>400</td><td>900</td><td>900</td><td>1,000</td><td>1,000</td><td>1,100</td><td>0</td><td>0</td><td>1,300</td><td>4,000</td></tr><tr><td>Others</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>3</td><td>3</td><td>4</td><td>11</td><td>4</td><td>6</td><td>12</td></tr><tr><td>Total</td><td>164</td><td>171</td><td>526</td><td>1,216</td><td>1,291</td><td>1,518</td><td>1,498</td><td>1,653</td><td>555</td><td>630</td><td>2,077</td><td>5,961</td></tr></table>

Source: Company data, UBS estimates

Figure 6: ASIC's supply chain build units

<table><tr><td>ASIC Supply Chain Build Units (k chips)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Google TPU - Broadcom</td><td>2,045</td><td>2,565</td><td>3,680</td><td>5,000</td></tr><tr><td>Google TPU - MediaTek</td><td>0</td><td>0</td><td>450</td><td>4,000</td></tr><tr><td>Amazon Trainium - Alchip</td><td>1,000</td><td>176</td><td>1,800</td><td>3,100</td></tr><tr><td>Amazon Trainium - Marvell</td><td>600</td><td>1,335</td><td>605</td><td>145</td></tr><tr><td>Meta</td><td>348</td><td>421</td><td>175</td><td>425</td></tr><tr><td>Others</td><td>277</td><td>222</td><td>192</td><td>190</td></tr><tr><td>Total</td><td>4,270</td><td>4,719</td><td>7,072</td><td>13,590</td></tr></table>

Source: Company data, UBS estimates. Note: Others include Intel's Habana, Microsoft's Maia, Tesla's Dojo, etc.

Figure 7: SolC volume

<table><tr><td>SolC (kps)</td><td>Q126E</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>SolC volume</td><td>14</td><td>17</td><td>23</td><td>29</td><td>41</td><td>49</td><td>54</td><td>57</td><td>20</td><td>42</td><td>82</td><td>202</td></tr></table>

Source: Company data, UBS estimates

Figure 8: TSMC's back-end sales analysis

<table><tr><td>TSMC&#x27;s backend sales (US$m)</td><td>Q126E</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Sales from adv packaging</td><td>2,693</td><td>3,236</td><td>4,421</td><td>5,684</td><td>5,924</td><td>7,135</td><td>7,959</td><td>8,713</td><td>5,240</td><td>8,899</td><td>16,034</td><td>29,730</td></tr><tr><td>Sales from bumping &amp; testing</td><td>919</td><td>1,039</td><td>1,122</td><td>1,156</td><td>1,179</td><td>1,320</td><td>1,505</td><td>1,580</td><td>2,348</td><td>3,156</td><td>4,236</td><td>5,584</td></tr><tr><td>Total TSMC&#x27;s backend sales</td><td>3,613</td><td>4,275</td><td>5,543</td><td>6,840</td><td>7,102</td><td>8,455</td><td>9,464</td><td>10,293</td><td>7,588</td><td>12,056</td><td>20,270</td><td>35,314</td></tr><tr><td>% of TSMC&#x27;s sales</td><td>10.1%</td><td>10.6%</td><td>12.4%</td><td>14.8%</td><td>14.7%</td><td>15.5%</td><td>15.2%</td><td>15.6%</td><td>8.4%</td><td>9.8%</td><td>12.1%</td><td>15.3%</td></tr></table>

Source: Company data, UBS estimates

Figure 9: Industry CoWoS capacity  
![](images/c2850c32ae5453cb14a8eae6882967e7104c9e84f73f375a512087c99c4c3f90.jpg)  
Source: Company data, UBS estimates

Figure 10: TSMC vs. non-TSMC CoWoS capacity  
![](images/95a3fd904ba66b7c82c150b9446b9687fe94dcd0b1cde58adf26170e16921da4.jpg)  
Source: Company data, UBS estimates. Note: Non-TSMC CoWoS capacity includes ASE and Amkor.

Figure 11: Industry CoWoS capacity vs. Nvidia's volume  
![](images/da0011ae0419a07a664412e5ee6486626e247c5433b097dada911fdfeda1a765.jpg)  
Source: Company data, UBS estimates

Figure 12: CoWoS demand from major customers  
![](images/a4b32c32213eee105acba42c13832b0c87b8207660cb5306d3f9231a9794dc11.jpg)  
Source: Company data, UBS estimates

Figure 13: N3 supply & demand analysis

<table><tr><td rowspan="2">Client</td><td rowspan="2">Products</td><td rowspan="2">Die size (mm2)</td><td colspan="10">N3 capacity requirement (kwpm)</td></tr><tr><td>Q126E</td><td>Q226E</td><td>Q326E</td><td>Q426E</td><td>2026 demand (k)</td><td>Q127E</td><td>Q227E</td><td>Q327E</td><td>Q427E</td><td>2027 demand (k)</td></tr><tr><td rowspan="3">Nvidia</td><td>Rubin</td><td>1,628</td><td>0</td><td>2</td><td>15</td><td>29</td><td>137</td><td>34</td><td>39</td><td>32</td><td>15</td><td>360</td></tr><tr><td>Rubin Ultra</td><td>1,628</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>4</td><td>16</td><td>36</td><td>169</td></tr><tr><td>Vera CPU</td><td>800</td><td>0</td><td>1</td><td>5</td><td>11</td><td>51</td><td>11</td><td>13</td><td>17</td><td>19</td><td>178</td></tr><tr><td rowspan="4">Broadcom</td><td>Google - TPU v7 Ironwood</td><td>1,400</td><td>6</td><td>11</td><td>16</td><td>21</td><td>158</td><td>14</td><td>8</td><td>6</td><td>0</td><td>85</td></tr><tr><td>Google - TPU v8i</td><td>1,400</td><td>0</td><td>0</td><td>2</td><td>4</td><td>18</td><td>7</td><td>17</td><td>25</td><td>35</td><td>250</td></tr><tr><td>Meta - MTIA v3</td><td>1,600</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>1</td><td>1</td><td>2</td><td>3</td><td>19</td></tr><tr><td>OpenAI</td><td>1,600</td><td>0</td><td>0</td><td>0</td><td>3</td><td>11</td><td>3</td><td>4</td><td>4</td><td>1</td><td>36</td></tr><tr><td>AMD</td><td>MI355</td><td>840</td><td>2</td><td>2</td><td>1</td><td>1</td><td>17</td><td>1</td><td>1</td><td>0</td><td>0</td><td>7<

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
