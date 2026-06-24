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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Precious Metals Comment Precious metals navigate no-man's land for now

## Downside risks to our views have increased materially

Gold has come under immense pressure as yields have risen further and the market continues to anticipate rate hikes. While there are some echoes to the previous bear market in gold, we think ultimately this time is different. We continue to see higher gold prices ahead as we expect the Fed to resume easing policy rates and as diversification trends both in the private as well as official sector continues. That said, timelines of our expected price forecast profile may be pushed out, with greater uncertainty on how long the current consolidation might extend. Economic data prints out of the US will be a key focus in the coming months, with any signs of softening likely to encourage re-engagement in gold. For now, summer trading conditions are likely to continue.

## White precious metals remain highly correlated with gold, but demand headwinds lie ahead

There's risk that slower growth would weigh on demand for the more industrial precious metals. Silver may have attractive overall demand prospects over the long term given its exposure to Al, renewable energy and electric vehicles, but for now any slowdown in industrial demand is likely to be a headwind. We think this will manifest more in silver's relative performance to gold, rather than its overall price direction i.e. the gold:silver ratio is likely to struggle to revisit previous lows. Platinum and palladium are both vulnerable to weaker auto demand. But silver and platinum have more potential to attract investor flows in a rising gold price environment. Meanwhile palladium continues to be challenged by increasing market share of battery electric vehicles, especially as China's exports of more affordable models continue to rise.

FX

Global

Joni Teves
Strategist
joni.teves@ubs.com
+65-6495 6851

## Is the market capitulating?

Comparing gold bull/bear markets

![](images/0d4c4e40c90a1576c28f883529c0a51be474dccb68dc01b2d6a26b3c7db7f4ab.jpg)  
Source: Bloomberg, UBS

## Is the market capitulating?

Comparing silver bull/bear markets  
![](images/ecf6446cc28c11305beba58851445fd50f5c924f67dc71292d2f09c1e55d5bb7.jpg)  
Source: Bloomberg, UBS

## Is the market capitulating?

![](images/64d97d4429cfb288e97c03a0eef57d955cbf787badf7b2e4fc597cbcc798771e.jpg)  
Source: Bloomberg, UBS

![](images/2e92f6349bed15a0b16fa323576842f3e23674239a20b1684ce7c8f1f7230bbe.jpg)  
Source: Bloomberg, UBS

![](images/7086fa1193db44effe176ca0d90c403bc0aa61f5abbfb23db1e9a6ae2a8be6e4.jpg)  
UBS

## There are challenges in the short run

Current sentiment scorecard  
![](images/19468897a1a03ce4b8a564bc035afcfce6beb5f8c58082676d312e9370078943.jpg)  
Source: UBS  
Sentiment scorecard in May

![](images/1610a7645c4b01e01327b8789e9fd33a508dbd9441217e436103203d4e076c1b.jpg)  
Source: UBS

## Underlying factors remain supportive

<table><tr><td colspan="2">2013</td><td>YTD 2026</td></tr><tr><td>Gold Price ($/oz)</td><td>↓ -29%</td><td>↑ +1.2% YTD</td></tr><tr><td>Catalyst for gold weakness</td><td>Monetary policy regime shift; fear of central bank selling (Cyprus)</td><td>Stretched positions unwinding (Jan/Feb); Oil shock fuelling inflation and rate hike expectations; stronger USD &amp; higher real yields; fear of central bank selling</td></tr><tr><td>USD Index (BBDXY)</td><td>↑ stronger (+3% full year; +7% to peak)</td><td>→ choppy (+1.17% YTD; +4% trough to peak)</td></tr><tr><td>CPI Inflation (% YoY)</td><td>↓ Falling (2.0% → 1.0%)</td><td>↑ Rising (2.7% → 4.2%)</td></tr><tr><td>Real Yields (10Y TIPS %)</td><td>↑ Turned positive (major headwind)</td><td>↑Rising (+27bp net YTD; +54bp trough to peak)</td></tr><tr><td>Fed Funds Rate (%)</td><td>→ Held at 0.25%; Taper announced</td><td>→ Held at 3.75%; market pricing in 1.7 hikes by yearend</td></tr><tr><td>Fed Monetary Policy Stance</td><td>→ Shifting from accommodation to normalization</td><td>→ Pause after 175bp of cuts; watching 2-sided risks</td></tr><tr><td>US GDP Growth (%)</td><td>→ Moderate (2.1-2.5%)</td><td>→ Holding (2.8% → 2.6%)</td></tr><tr><td>US Unemployment Rate (%)</td><td>↓ Falling (8.1% → 6.2%)</td><td>↑ Rising (3.9% → 4.3%)</td></tr><tr><td>US Fiscal Deficit/GDP (%)</td><td>↑ Improving (-6.5% → -2.7%)</td><td>↑ Improving but at a wider gap (-6.9% → -5.95%)</td></tr><tr><td>US Debt/GDP (%)</td><td>→ Stable (~104%)</td><td>→ Elevated, stable (~137%)</td></tr><tr><td>US Credit Rating</td><td>→ Stable (post-2011 downgrade)</td><td>→ Stable but under pressure</td></tr><tr><td>Financial Conditions Index</td><td>↑ Easing (-1.1 → +1.0)</td><td>↑ Volatile but generally easing (-1.2 → +1.14)</td></tr><tr><td>S&amp;P 500 P/E Ratio</td><td>↑ Rising (14-15x → 16-17x)</td><td>→ Choppy and elevated (range 24-28x)</td></tr><tr><td>VIX Volatility</td><td>→ Low/moderate (avg 13-15)</td><td>↑ Easing (avg 19; peak 31)</td></tr><tr><td>Commodities (BCOM Index)</td><td>↓ -11.6%</td><td>↑ +15% YTD, though off the highs</td></tr><tr><td>Bond Market</td><td>↑ Yields surging (taper tantrum); US10y +127bp net</td><td>↑ Riisng, US10y+0.32bp net YTD, +73bp trough to peak</td></tr><tr><td>Geopolitical Risks</td><td>→ Regional tensions (China-Japan tensions over disputed islands; Syria conflict)</td><td>↑ Elevated global tensions (Middle East conflict, Russia/Ukraine war, US trade/tariff wars)</td></tr><tr><td>Macroeconomic Narrative</td><td>Improving fundamentals; reduced safe-haven demand</td><td>Elevated macro &amp; geopolitical uncertainty; risks to growth-inflation mix persist</td></tr></table>

Source: Bloomberg, UBS

## US economic data held up by AI

AI and tech are driving the strength in investment and likely supporting upper income households' consumption. AI-reliance implies vulnerabilities, but productivity gains present downside risks to gold.

![](images/58acec6172bd9281e7223ebf2a9cdda7d9313e29d1d7f2b17fa48c9c8eb204f8.jpg)  
Source: BEA, Haver, UBS

Our house view remains for Fed rate cuts from 2027

<table><tr><td>Variable</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027</td><td>2028</td></tr><tr><td>Change in real GDP</td><td>3.4</td><td>2.4</td><td>2.0</td><td>2.1</td><td>2.1</td><td>2.6</td></tr><tr><td>Unemployment rate</td><td>3.8</td><td>4.2</td><td>4.5</td><td>4.5</td><td>4.5</td><td>4.4</td></tr><tr><td>PCE inflation</td><td>2.9</td><td>2.6</td><td>2.8</td><td>3.3</td><td>2.2</td><td>1.9</td></tr><tr><td>Core PCE inflation</td><td>3.3</td><td>3.0</td><td>2.9</td><td>3.1</td><td>2.4</td><td>2.0</td></tr><tr><td>Federal funds rate</td><td>5.4</td><td>4.4</td><td>3.6</td><td>3.6</td><td>2.9</td><td>2.9</td></tr></table>

Note: Q4/Q4 % basis except the unemployment rate which is a Q4 quarterly average. The federal funds rate reflects the mid-point of the target range. Years after 2025 are forecasts.
Source: BEA, BLS, Haver, UBS

## UBS

## US debt sustainability remains a long-term concern

US debt held by the public over 100% of GDP – significantly higher than other sovereigns with AA+ rating

Budget deficit adjusted for student loan accounting (FY, % of GDP)

![](images/6ba8b3d87e4d7e795d0530763837742c80bc506c659e82ad65b958ad1c6aceeb.jpg)  
Source: CBO, Haver, UBS  
Debt Held by the Public as a Percentage of GDP (Fiscal Yr, %)

![](images/771b68fd665929e1a607f1a6e0c1850158927aaf6e0681da84fcbf836605cd15.jpg)  
Source: U.S. Treasury, Haver, UBS

## UBS

## Summer has come

![](images/9bc35ecfebac82ed6e86e1f095eb7342927d463f5f9156fb0c98fb20dd08cdf8.jpg)

## UBS

## Volatility has come down

![](images/8678264f26260982c7d4db024e6c2616937ab89e8809d8ba659383a797ee8ef2.jpg)  
Source: Bloomberg, UBS

Total bar & coin demand, % by region

## Physical demand supported by investment

Total physical demand has held up despite record high prices

![](images/bfc4a5aaf49dc57b0de1b4abba302b5de3129150b5736c4c2c3b71ac3e11fe49.jpg)  
Source: WGC, UBS  
Asia accounts for over 70% of physical investment demand

![](images/ef0d08c09062efbf8b3dd12465f742d4a3c81a16e737fb80a4a84d1192dba10f.jpg)  
Source: WGC, UBS  
Strong growth seen across most regions

![](images/586e1209fe0adc899b68af59f8129908accf397fbb953d7d85563fc03b69156d.jpg)  
Source: WGC, UBS

## Official gold reserves are misunderstood

Poland's gold reserves USD value

![](images/bb3df30cd714399a3c6378a74d5e0f3df7f3112d70e6aad7e23741e89ac3b3ae.jpg)  
Gold Value at Constant Prices (Jan-2024 prices) Gold Value at Current Prices  
Source: IMF, Haver, UBS  
Turkey's gold reserves USD value

![](images/0f9fda1ff6f06c607f3ccbbbce07cef7d4e0720114888f6be5fa3eeda8f4c54a.jpg)  
Source: Haver, IMF, UBS

## UBS

## Official sector participation is expanding

The composition of top buyers in 2022...

![](images/21a8e4d1f3b092522adeb91748a058d126783779c9241fbc7d87e26303e4060d.jpg)  
Source: IMF, WGC, UBS  
...is different from the top buyers in 2026 YTD

![](images/aa60360d446a7f8d6e0b676051663927dd144dce456e7866534281ed17035791.jpg)  
Source: IMF, WGC, UBS  
As some central banks slow down purchases, others have room to step up

![](images/8f429fbda462cef8b4c445ef52450dd2164e9111d7f56733126cffb52bff9f42.jpg)  
Source: IMF, WGC, UBS  
Growth in assets of other official institutions suggests there is room for them to also diversify into gold

![](images/4ea065aa3b70c05c091ce2c95e1661da31e2013ac5afc0ec8a6c3f2fed25ecce.jpg)  
Source: industry estimates, UBS

## There is room for gold diversification to continue...

We think the market as a whole remains largely underinvested

![](images/c8f9167ecda79f014d2c328f02b6726f9a38a922a260ab58dae5480fae479db8.jpg)  
Source: Bloomberg, CFTC, various funds, industry estimates, UBS calculations  
Growth in total assets under management creates space for gold diversification

![](images/010fd53ba9e605533c00fac0397ce980c4bb10144c3da3c15737d07661cc8748.jpg)  
Source: Industry estimates, UBS calculations  
The potential impact of a 1% increase in gold allocations depends on the speed & timing of execution

![](images/3ef0b1e37ae6d841d1b8e29eac465f3b9dda669337b71241d418a031c680124d.jpg)  
Source: Industry estimates, UBS calculations

## ...amid a growing list of long-term concerns

![](images/e84a786a0a5a0de462fad1d93d98e91ea22a623cf88b41542ff8f8e567fe4fa7.jpg)

Elevated macro and geopolitical uncertainty

![](images/92e39292edc1b4d0db9f2095d5158286c8a46bdf2daf27874b4c41a604d997d3.jpg)

Downside risks to growth

![](images/6095011b712821718f6627406f27cd65b8c286c74a05e1cc7562bbfa3068b796.jpg)

Upside risks to inflation

![](images/3ca5645aa8625ffda3d03eccd5a0ebdd970a843835fdd4ac18ef59d46e212302.jpg)

## Stagflation risks

![](images/2147f4dfbe877592543314000a00cd90bd6477ecd38f014d67e81286f266f111.jpg)

## De-dollarisation, asset rotation, diversification

![](images/29e34b47119c4fe19e28b3a7933f9c261b86a0795494479432eae55211e991bd.jpg)

Shifting global
political and trade
relationships

![](images/d7a79ffeae3d043c26a39a0836ad5a9b9b48213f47aa3ae06b583f573ab4b592.jpg)

Source: UBS

## Fed independence and credibility

![](images/6e92ad8f60e0a679cf2f592da7858dd5aca5abade844cbfa52b8dab18c8bd150.jpg)

## Fiscal and debt sustainability

![](images/33538685f32a700c331d4631f890502ff3aca2afb798eaa0a28f070d071c8410.jpg)

Higher volatility and potential liquidity issues

## UBS

Downside risks to gold prices
Rebalancing
Sharp equity selloff
Significantly lower central bank purchases/signs of strategic selling
Better-than-expected US growth
Hawkish Fed
Higher real rates, stronger US dollar
Source: UBS

## White precious metals face demand headwinds

Global median growth swinging down to 2.1% in May  
![](images/0d87f5bdf1b527389971b542415182afba40a8dbcd76cda259dde32d1f688216.jpg)  
Source: Haver, CEIC, UBS calculations

## Watch silver and platinum trading in China

Shanghai Futures Exchange silver trading activity

![](images/145d99229cfc6cc3287514daf6a1ac00a94fa82e3d15b836b2f872cde707505c.jpg)  
Source: Bloomberg, SHFE, UBS  
Guangzhou Futures Exchange platinum trading activity

![](images/382ee07dfae6832b5ce8efecc118cd251099644dfc956e2effea17c81df72000.jpg)  
Source: Bloomberg, SHFE, UBS

## Electric vehicle trends continue to weigh on Pd

EV wholesale penetration in China  
![](images/3e9fa36dcf8c6914a5c6d0abfbd1adfc08bd9c13ec8814e4af886f51003983c2.jpg)  
Source: CPCA, UBS

![](images/07358d78c7f01fdf8ceb7d7358e21732b51ff852d0c05eb90f363fda448b40d8.jpg)  
Source: CPCA, UBS

## UBS

## Risks to our views have increased materially

<table><tr><td colspan="2"></td><td>old</td><td>base case</td><td>upside</td><td>downside</td><td>new vs old forecast</td><td>base case vs spot</td><td>risks to base case</td></tr><tr><td rowspan="2">Gold</td><td>end-2026</td><td>5,600</td><td>5,600</td><td>6,000</td><td>3,800</td><td>0%</td><td>19%</td><td></td></tr><tr><td>end-2027</td><td>5,000</td><td>5,000</td><td>6,000</td><td>3,500</td><td>0%</td><td>6%</td><td></td></tr><tr><td rowspan="2">Silver</td><td>end-2026</td><td>120</td><td>120</td><td>150</td><td>65</td><td>0%</td><td>38%</td><td></td></tr><tr><td>end-2027</td><td>90</td><td>90</td><td>135</td><td>55</td><td>0%</td><td>4%</td><td></td></tr><tr><td rowspan="2">Platinum</td><td>end-2026</td><td>2,700</td><td>2,700</td><td>3,000</td><td>1,900</td><td>0%</td><td>28%</td><td></td></tr><tr><td>end-2027</td><td>2,500</td><td>2,500</td><td>3,000</td><td>1,675</td><td>0%</td><td>18%</td><td></td></tr><tr><td rowspan="2">Palladium</td><td>end-2026</td><td>1,900</td><td>1,900</td><td>2,450</td><td>1,400</td><td>0%</td><td>27%</td><td></td></tr><tr><td>end-2027</td><td>1,700</td><td>1,700</td><td>2,150</td><td>1,250</td><td>0%</td><td>14%</td><td></td></tr></table>

Source: UBS

UBS

## Valuation Method and Risk Statement

Risks of multi-asset investing include but are not limited to market risk, credit risk, interest rate risk, and foreign exchange risk. Correlations of returns among different asset classes may deviate from historical patterns. Geopolitical events and policy shocks pose risks that can reduce asset returns. Valuations may be adversely affected during times of high market volatility, thin liquidity, and economic dislocation. All options discussions are 'over-the-counter'. Losses on some options trades are potentially unlimited unless hedged/neutralised.

## Required Disclosures

This document has been prepared by UBS AG, Singapore Branch, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 22 June 2026 07:02 AM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.

## UBS AG, Singapore Branch: Joni Teves.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies d

[中间内容因长度限制已省略]

inions in such this publication or material are not made or provided to you, and (ii) to the maximum extent permitted by law (a) indemnify UBS and its associates or related entities (and their respective Directors, officers, agents and Advisors) (each a 'Relevant Person') for any loss, damage, liability or claim any of them may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material (b) waive any rights or remedies you may have against any Relevant Person for (or in respect of) any loss, damage, liability or claim you may incur or suffer as a result of, or in connection with, your unauthorised reliance on this publication or material. Korea: Distributed in Korea by UBS Pte. Ltd., Seoul Branch. This report may have been edited or contributed to from time to time by affiliates of UBS Pte. Ltd., Seoul Branch. This material is intended for professional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) 2/F, 3 North Avenue, Maker Maxity, Bandra Kurla Complex, Bandra (East), Mumbai (India) 400051. Phone: +912261556000. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr. Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email : parameshwaran.s@ubs.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company/companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch, which is licensed and regulated by Taiwan Financial Supervisory Commission. Save for securities/instruments that are traded in a Taiwan organized exchange, this material should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl.Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
