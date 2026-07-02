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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 30, 2026 03:12 PM GMT

Internet | North America

# Where Are We Trading Now: Will the AI Flows Move Toward Internet Thru EPS?

Internet names fell -6% (SPX/NDX -2/-5%) led by GOOGL -8% while AMZN/META both -5%. BKNG +6%, RDDT -5%, and RBLX -8%. AMZN/GOOGL/META 25X/23X/17X '26 EPS (-22%/-11%/-20% vs TTM avg).

MS & CO. LLC
Brian Nowak, CFA
Equity Analyst
Brian.Nowak@morganstanley.com +1 212 761-3365
Matthew Cost
Equity Analyst
Matthew.Cost@morganstanley.com +1 212 761-7252
Nathan Feather
Equity Analyst
Nathan.Feather@morganstanley.com +1 212 761-9812
Julian Herrera
Research Associate
Julian.Herrera@morganstanley.com +1 212 761-1784
Gregory Gao
Research Associate
Greg.Gao@morganstanley.com +1 212 296-3125
Kavya A Narayanan
Research Associate
Kavya.Narayanan@morganstanley.com +1 212 761-4183
Nikhil Javeri
Research Associate
Nikhil.Javeri1@morganstanley.com +1 212 761-3742
Cela VanLieshout
Research Associate
Cela.Vanlieshout1@morganstanley.com +1 212 761-2679

## INTERNET

## Comp Sheet

Exhibit 1: Internet Comp Sheet: North America

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Price 6/26/2026</td><td rowspan="2">Mkt Cap ($ MM)</td><td rowspan="2">EV ($ MM)</td><td colspan="2">EV/Rev</td><td colspan="2">EV/GP</td><td colspan="2">EV/EBITDA</td><td colspan="2">FCF Yield</td><td colspan="2">EPS</td><td colspan="2">P/E</td><td rowspan="2">Short Interest</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="17">Digital Media</td></tr><tr><td>BMBL</td><td>$3.04</td><td>498</td><td>840</td><td>1.0x</td><td>1.0x</td><td>1.4x</td><td>1.4x</td><td>3.1x</td><td>3.6x</td><td>45.0%</td><td>28.2%</td><td>0.78</td><td>0.61</td><td>3.9x</td><td>5.0x</td><td>11.7%</td></tr><tr><td>CRTO</td><td>$17.66</td><td>900</td><td>741</td><td>0.6x</td><td>0.6x</td><td>0.7x</td><td>0.7x</td><td>2.0x</td><td>1.9x</td><td>14.4%</td><td>17.3%</td><td>4.24</td><td>4.97</td><td>4.2x</td><td>3.6x</td><td>2.2%</td></tr><tr><td>DUOL</td><td>$121.49</td><td>5,933</td><td>4,681</td><td>3.9x</td><td>3.5x</td><td>5.5x</td><td>5.0x</td><td>15.0x</td><td>13.4x</td><td>6.3%</td><td>6.1%</td><td>2.68</td><td>2.81</td><td>45.3x</td><td>43.3x</td><td>20.0%</td></tr><tr><td>DV</td><td>$10.82</td><td>1,776</td><td>1,602</td><td>2.0x</td><td>1.8x</td><td>2.4x</td><td>2.2x</td><td>5.7x</td><td>5.1x</td><td>10.7%</td><td>11.2%</td><td>0.62</td><td>0.76</td><td>17.5x</td><td>14.2x</td><td>7.5%</td></tr><tr><td>GOOGL</td><td>$337.39</td><td>4,128,979</td><td>3,972,694</td><td>8.0x</td><td>6.3x</td><td>13.0x</td><td>10.2x</td><td>16.3x</td><td>12.0x</td><td>0.5%</td><td>0.0%</td><td>14.73</td><td>15.61</td><td>22.9x</td><td>21.6x</td><td>1.5%</td></tr><tr><td>GRND</td><td>$14.34</td><td>2,635</td><td>3,002</td><td>5.6x</td><td>4.8x</td><td>7.5x</td><td>6.4x</td><td>13.2x</td><td>11.4x</td><td>5.5%</td><td>6.8%</td><td>0.55</td><td>0.65</td><td>26.0x</td><td>22.0x</td><td>32.7%</td></tr><tr><td>META</td><td>$550.25</td><td>1,410,841</td><td>1,388,487</td><td>5.4x</td><td>4.5x</td><td>7.3x</td><td>6.3x</td><td>9.3x</td><td>7.5x</td><td>0.9%</td><td>1.1%</td><td>32.83</td><td>34.16</td><td>16.8x</td><td>16.1x</td><td>1.4%</td></tr><tr><td>MNTN</td><td>$9.62</td><td>759</td><td>545</td><td>1.6x</td><td>1.3x</td><td>2.0x</td><td>1.7x</td><td>5.5x</td><td>4.4x</td><td>NA</td><td>NA</td><td>1.06</td><td>1.08</td><td>9.1x</td><td>8.9x</td><td>6.1%</td></tr><tr><td>MTCH</td><td>$37.17</td><td>9,343</td><td>12,294</td><td>3.5x</td><td>3.4x</td><td>4.7x</td><td>4.5x</td><td>9.2x</td><td>8.7x</td><td>10.3%</td><td>10.5%</td><td>2.61</td><td>3.14</td><td>14.2x</td><td>11.8x</td><td>4.6%</td></tr><tr><td>PINS</td><td>$20.82</td><td>14,104</td><td>14,386</td><td>2.9x</td><td>2.6x</td><td>3.7x</td><td>3.4x</td><td>10.1x</td><td>9.1x</td><td>9.0%</td><td>10.3%</td><td>0.59</td><td>0.70</td><td>35.2x</td><td>29.8x</td><td>15.5%</td></tr><tr><td>RDDT</td><td>$166.94</td><td>33,809</td><td>31,039</td><td>9.2x</td><td>6.7x</td><td>10.0x</td><td>7.4x</td><td>20.2x</td><td>14.1x</td><td>3.6%</td><td>5.1%</td><td>6.86</td><td>9.10</td><td>24.3x</td><td>18.3x</td><td>12.0%</td></tr><tr><td>SNAP</td><td>$4.41</td><td>8,322</td><td>8,988</td><td>1.3x</td><td>1.2x</td><td>2.3x</td><td>2.0x</td><td>6.5x</td><td>5.0x</td><td>7.7%</td><td>13.8%</td><td>(0.07)</td><td>0.17</td><td>NM</td><td>25.4x</td><td>8.8%</td></tr><tr><td>SSTK</td><td>$14.20</td><td>520</td><td>632</td><td>0.8x</td><td>0.9x</td><td>1.4x</td><td>1.5x</td><td>4.3x</td><td>4.9x</td><td>3.6%</td><td>NM</td><td>(1.02)</td><td>0.49</td><td>NM</td><td>29.2x</td><td>4.4%</td></tr><tr><td>TTD</td><td>$18.37</td><td>8,760</td><td>7,882</td><td>2.5x</td><td>2.2x</td><td>3.2x</td><td>2.9x</td><td>6.2x</td><td>5.6x</td><td>10.5%</td><td>12.0%</td><td>2.02</td><td>2.21</td><td>9.1x</td><td>8.3x</td><td>17.5%</td></tr><tr><td>YELP</td><td>$24.00</td><td>1,541</td><td>1,208</td><td>0.8x</td><td>0.8x</td><td>0.9x</td><td>0.9x</td><td>3.9x</td><td>3.7x</td><td>14.8%</td><td>16.3%</td><td>2.11</td><td>2.13</td><td>11.4x</td><td>11.2x</td><td>15.6%</td></tr><tr><td colspan="2">Digital Media Med.</td><td>7,127</td><td>6,281</td><td>2.7x</td><td>2.4x</td><td>3.5x</td><td>3.1x</td><td>7.9x</td><td>6.5x</td><td>7.7%</td><td>10.4%</td><td>$1.54</td><td>$1.64</td><td>17.1x</td><td>17.2x</td><td>8.1%</td></tr><tr><td colspan="17">eCommerce/Marketplace</td></tr><tr><td>AMZN</td><td>$232.69</td><td>2,530,271</td><td>2,506,256</td><td>3.0x</td><td>2.6x</td><td>5.9x</td><td>4.9x</td><td>11.3x</td><td>8.5x</td><td>NM</td><td>NM</td><td>9.50</td><td>11.32</td><td>24.5x</td><td>20.6x</td><td>1.0%</td></tr><tr><td>CHWY</td><td>$18.55</td><td>7,774</td><td>7,254</td><td>0.5x</td><td>0.5x</td><td>1.8x</td><td>1.6x</td><td>8.0x</td><td>6.6x</td><td>0.5%</td><td>0.1%</td><td>1.52</td><td>1.82</td><td>12.2x</td><td>10.2x</td><td>11.1%</td></tr><tr><td>EBAY</td><td>$107.87</td><td>49,297</td><td>50,645</td><td>4.1x</td><td>3.8x</td><td>5.6x</td><td>5.2x</td><td>13.6x</td><td>12.1x</td><td>6.1%</td><td>6.5%</td><td>6.03</td><td>6.76</td><td>17.9x</td><td>16.0x</td><td>3.9%</td></tr><tr><td>ETSY</td><td>$78.04</td><td>9,445</td><td>8,491</td><td>3.0x</td><td>3.0x</td><td>4.1x</td><td>4.1x</td><td>10.3x</td><td>10.1x</td><td>7.7%</td><td>7.2%</td><td>3.71</td><td>4.40</td><td>21.0x</td><td>17.7x</td><td>14.3%</td></tr><tr><td>FIGS</td><td>$11.60</td><td>2,275</td><td>1,970</td><td>2.7x</td><td>2.5x</td><td>4.0x</td><td>3.7x</td><td>20.6x</td><td>16.4x</td><td>5.2%</td><td>6.3%</td><td>0.24</td><td>0.31</td><td>49.3x</td><td>37.2x</td><td>9.2%</td></tr><tr><td>PTON</td><td>$5.72</td><td>2,645</td><td>1,483</td><td>0.6x</td><td>0.6x</td><td>1.2x</td><td>1.1x</td><td>3.1x</td><td>3.0x</td><td>19.6%</td><td>18.2%</td><td>0.12</td><td>0.27</td><td>45.9x</td><td>21.0x</td><td>14.3%</td></tr><tr><td>RVLV</td><td>$23.76</td><td>1,717</td><td>1,381</td><td>1.0x</td><td>0.9x</td><td>1.9x</td><td>1.7x</td><td>14.6x</td><td>10.3x</td><td>5.2%</td><td>5.6%</td><td>0.83</td><td>1.18</td><td>28.8x</td><td>20.2x</td><td>10.8%</td></tr><tr><td>WW</td><td>$15.99</td><td>160</td><td>625</td><td>1.0x</td><td>1.0x</td><td>1.4x</td><td>1.4x</td><td>5.8x</td><td>6.2x</td><td>18.7%</td><td>21.7%</td><td>(4.68)</td><td>(0.90)</td><td>NM</td><td>NM</td><td>21.2%</td></tr><tr><td colspan="2">eCommerce Med.</td><td>2,645</td><td>1,970</td><td>1.0x</td><td>1.0x</td><td>1.9x</td><td>1.7x</td><td>10.3x</td><td>8.5x</td><td>6.1%</td><td>6.8%</td><td>$1.52</td><td>$1.18</td><td>22.8x</td><td>20.2x</td><td>11.1%</td></tr><tr><td colspan="17">Shared Economy/Rideshare</td></tr><tr><td>CART</td><td>$47.46</td><td>12,036</td><td>11,544</td><td>2.8x</td><td>2.5x</td><td>3.8x</td><td>3.4x</td><td>9.0x</td><td>7.8x</td><td>8.1%</td><td>10.0%</td><td>2.62</td><td>3.48</td><td>18.1x</td><td>13.7x</td><td>10.3%</td></tr><tr><td>DASH</td><td>$183.09</td><td>81,475</td><td>75,942</td><td>4.3x</td><td>3.6x</td><td>8.4x</td><td>6.8x</td><td>21.3x</td><td>15.8x</td><td>3.2%</td><td>4.6%</td><td>2.28</td><td>4.04</td><td>80.4x</td><td>45.3x</td><td>5.1%</td></tr><tr><td>LYFT</td><td>$14.27</td><td>5,742</td><td>4,908</td><td>0.7x</td><td>0.6x</td><td>1.5x</td><td>1.4x</td><td>7.3x</td><td>6.2x</td><td>23.1%</td><td>24.0%</td><td>0.67</td><td>1.01</td><td>21.4x</td><td>14.1x</td><td>25.6%</td></tr><tr><td>UBER</td><td>$76.20</td><td>157,840</td><td>161,583</td><td>2.8x</td><td>2.4x</td><td>6.3x</td><td>5.3x</td><td>14.2x</td><td>11.4x</td><td>NM</td><td>NM</td><td>3.38</td><td>4.40</td><td>22.5x</td><td>17.3x</td><td>2.8%</td></tr><tr><td colspan="2">Shared Economy Med.</td><td>46,755</td><td>43,743</td><td>2.8x</td><td>2.4x</td><td>5.0x</td><td>4.4x</td><td>11.6x</td><td>9.6x</td><td>8.1%</td><td>10.0%</td><td>$2.45</td><td>$3.76</td><td>22.0x</td><td>15.7x</td><td>7.7%</td></tr><tr><td colspan="17">Gaming/Mobile App</td></tr><tr><td>APP</td><td>$477.08</td><td>161,601</td><td>162,356</td><td>19.6x</td><td>15.6x</td><td>21.6x</td><td>17.2x</td><td>23.3x</td><td>18.5x</td><td>3.5%</td><td>4.4%</td><td>15.24</td><td>19.75</td><td>31.3x</td><td>24.2x</td><td>5.0%</td></tr><tr><td>EA</td><td>$205.25</td><td>52,134</td><td>50,639</td><td>6.0x</td><td>5.3x</td><td>7.2x</td><td>6.3x</td><td>17.0x</td><td>13.7x</td><td>1.3%</td><td>4.6%</td><td>9.08</td><td>11.38</td><td>22.6x</td><td>18.0x</td><td>4.6%</td></tr><tr><td>LFTO</td><td>$27.39</td><td>5,088</td><td>6,703</td><td>7.8x</td><td>6.8x</td><td>9.1x</td><td>7.9x</td><td>13.8x</td><td>11.5x</td><td>5.3%</td><td>4.8%</td><td>0.16</td><td>1.23</td><td>171.2x</td><td>22.3x</td><td>2.5%</td></tr><tr><td>PLTK</td><td>$3.83</td><td>1,414</td><td>3,352</td><td>1.2x</td><td>1.2x</td><td>1.6x</td><td>1.6x</td><td>4.5x</td><td>4.4x</td><td>2.9%</td><td>19.2%</td><td>0.48</td><td>0.68</td><td>8.0x</td><td>5.6x</td><td>9.8%</td></tr><tr><td>RBLX</td><td>$47.56</td><td>35,432</td><td>33,241</td><td>5.3x</td><td>4.3x</td><td>6.5x</td><td>5.3x</td><td>19.4x</td><td>15.6x</td><td>3.8%</td><td>4.4%</td><td>(1.35)</td><td>(0.83)</td><td>NM</td><td>NM</td><td>4.9%</td></tr><tr><td>TTWO</td><td>$238.53</td><td>44,123</td><td>44,609</td><td>6.4x</td><td>4.8x</td><td>10.7x</td><td>7.0x</td><td>29.5x</td><td>15.9x</td><td>3.1%</td><td>4.3%</td><td>6.00</td><td>11.40</td><td>39.8x</td><td>20.9x</td><td>4.9%</td></tr><tr><td>U</td><td>$28.23</td><td>14,185</td><td>13,988</td><td>6.6x</td><td>5.7x</td><td>9.3x</td><td>6.5x</td><td>23.3x</td><td>18.9x</td><td>NM</td><td>2.0%</td><td>(0.90)</td><td>0.65</td><td>NM</td><td>43.4x</td><td>10.5%</td></tr><tr><td colspan="2">Video Game Med.</td><td>35,432</td><td>33,241</td><td>6.4x</td><td>5.3x</td><td>8.2x</td><td>6.4x</td><td>19.4x</td><td>15.6x</td><td>3.1%</td><td>4.4%</td><td>$0.48</td><td>$1.23</td><td>31.3x</td><td>21.6x</td><td>4.9%</td></tr><tr><td colspan="17">Travel</td></tr><tr><td>ABNB</td><td>$145.56</td><td>93,304</td><td>83,774</td><td>6.0x</td><td>5.6x</td><td>7.2x</td><td>6.7x</td><td>17.1x</td><td>15.9x</td><td>5.9%</td><td>6.1%</td><td>4.85</td><td>5.35</td><td>30.0x</td><td>27.2x</td><td>3.7%</td></tr><tr><td>EXPE</td><td>$262.80</td><td>32,842</td><td>34,469</td><td>2.1x</td><td>1.9x</td><td>2.3x</td><td>2.1x</td><td>8.3x</td><td>7.3x</td><td>11.2%</td><td>12.0%</td><td>20.39</td><td>23.40</td><td>12.9x</td><td>11.2x</td><td>6.6%</td></tr><tr><td>BKNG</td><td>$181.46</td><td>144,079</td><td>143,453</td><td>4.9x</td><td>4.5x</td><td>4.9x</td><td>4.5x</td><td>12.3x</td><td>11.1x</td><td>6.3%</td><td>7.0%</td><td>10.29</td><td>12.12</td><td>17.6x</td><td>15.0x</td><td>3.2%</td></tr><tr><td colspan="2">Travel Avg.</td><td>90,075</td><td>87,232</td><td>4.3x</td><td>4.0x</td><td>4.8x</td><td>4.4x</td><td>12.6x</td><td>11.4x</td><td>7.8%</td><td>8.4%</td><td>$11.84</td><td>$13.62</td><td>20.2x</td><td>17.8x</td><td>4.5%</td></tr><tr><td colspan="17">Real Estate Tech</td></tr><tr><td>COMP</td><td>$11.40</td><td>9,387</td><td>12,199</td><td>0.9x</td><td>0.8x</td><td>NA</td><td>NA</td><td>14.6x</td><td>10.5x</td><td>0.0%</td><td>0.0%</td><td>0.36</td><td>0.55</td><td>31.4x</td><td>20.6x</td><td>7.1%</td></tr><tr><td>Z</td><td>$31.15</td><td>7,465</td><td>7,017</td><td>2.4x</td><td>2.1x</td><td>3.2x</td><td>2.9x</td><td>9.1x</td><td>7.4x</td><td>8.8%</td><td>9.7%</td><td>2.12</td><td>2.58</td><td>14.7x</td><td>12.1x</td><td>9.5%</td></tr><tr><td>OPEN</td><td>$4.37</td><td>3,030</td><td>3,068</td><td>0.8x</td><td>0.4x</td><td>8.8x</td><td>5.5x</td><td>NM</td><td>23.5x</td><td>NM</td><td>NM</td><td>(0.58)</td><td>(0.45)</td><td>NM</td><td>NM</td><td>19.1%</td></tr><tr><td colspan="2">RE Tech Avg.</td><td>6,627</td><td>7,428</td><td>1.3x</td><td>1.1x</td><td>6.0x</td><td>4.2x</td><td>11.9x</td><td>13.8x</td><td>4.4%</td><td>4.9%</td><td>$0.63</td><td>$0.89</td><td>23.0x</td><td>16.3x</td><td>11.9%</td></tr><tr><td colspan="17"></td></tr><tr><td colspan="17"></td></tr><tr><td colspan="17"></td></tr><tr><td colspan="17"></td></tr><tr><td colspan="17"></td></tr><tr><td colspan="17"></td></tr><tr><td colspan="2"></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, MS estimates

Exhibit 2: Digital Ads vs. Travel/Shared Economy 1-Week Price Performance

<table><tr><td></td><td>Market Cap ($mn)</td><td>1 Week Performance</td></tr><tr><td colspan="3">Digital Ads</td></tr><tr><td>GOOGL</td><td>$4,128,979</td><td>-8.3%</td></tr><tr><td>META</td><td>$1,410,841</td><td>-4.7%</td></tr><tr><td>SNAP</td><td>$8,322</td><td>-5.4%</td></tr><tr><td>PINS</td><td>$14,104</td><td>2.7%</td></tr><tr><td>RDDT</td><td>$33,878</td><td>-4.6%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>-7.3%</td></tr><tr><td colspan="3">E-Commerce</td></tr><tr><td>AMZN</td><td>$2,530,271</td><td>-4.8%</td></tr><tr><td>CHWY</td><td>$7,774</td><td>1.9%</td></tr><tr><td>EBAY</td><td>$49,297</td><td>-0.3%</td></tr><tr><td>ETSY</td><td>$9,445</td><td>5.5%</td></tr><tr><td>FIGS</td><td>$2,275</td><td>-5.8%</td></tr><tr><td>PTON</td><td>$2,645</td><td>-0.9%</td></tr><tr><td>RVLV</td><td>$1,717</td><td>9.0%</td></tr><tr><td>WW</td><td>$160</td><td>-16.7%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>-4.6%</td></tr><tr><td colspan="3">Travel</td></tr><tr><td>ABNB</td><td>$93,304</td><td>2.2%</td></tr><tr><td>BKNG</td><td>$144,079</td><td>5.6%</td></tr><tr><td>EXPE</td><td>$32,842</td><td>9.1%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>4.9%</td></tr><tr><td colspan="3">Shared Economy</td></tr><tr><td>UBER</td><td>$157,840</td><td>6.4%</td></tr><tr><td>DASH</td><td>$81,475</td><td>5.6%</td></tr><tr><td>CART</td><td>$12,036</td><td>6.5%</td></tr><tr><td>LYFT</td><td>$5,742</td><td>-0.1%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>6.0%</td></tr></table>

Source: FactSet, MS

Exhibit 3: Assessing Internet – Price Performance

<table><tr><td rowspan="2"></td><td colspan="2">Short interest %</td><td colspan="2">1 Week Price Move</td><td colspan="2">1 Month Price Move</td><td colspan="2">YTD</td></tr><tr><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3"></td><td>AMZN</td><td>1.0%</td><td>AMZN</td><td>-4.8%</td><td>AMZN</td><td>-12.3%</td><td>AMZN</td><td>0.8%</td></tr><tr><td>GOOGL</td><td>1.5%</td><td>GOOGL</td><td>-8.3%</td><td>GOOGL</td><td>-13.2%</td><td>GOOGL</td><td>7.8%</td></tr><tr><td>META</td><td>1.4%</td><td>META</td><td>-4.7%</td><td>META</td><td>-10.1%</td><td>META</td><td>-16.6%</td></tr></table>

<table><tr><td rowspan="2">Top 10</td><td colspan="2">Short interest %</td><td colspan="2">1 Week Price Move</td><td colspan="2">1 Month Price Move</td><td colspan="2">YTD</td></tr><tr><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>LYFT</td><td>25.6%</td><td>MNTN</td><td>15.2%</td><td>COMP</td><td>37.3%</td><td>ETSY</td><td>40.8%</td></tr><tr><td>2</td><td>WW</td><td>21.2%</td><td>COMP</td><td>13.9%</td><td>RVLV</td><td>22.5%</td><td>EBAY</td><td>23.8%</td></tr><tr><td>3</td><td>DUOL</td><td>20.0%</td><td>PLTK</td><td>9.7%</td><td>ETSY</td><td>21.3%</td><td>MTCH</td><td>15.1%</td></tr><tr><td>4</td><td>OPEN</td><td>19.1%</td><td>EXPE</td><td>9.1%</td><td>DASH</td><td>18.9%</td><td>COMP</td><td>7.9%</td></tr><tr><td>5</td><td>TTD</td><td>17.5%</td><td>RVLV</td><td>9.0%</td><td>EXPE</td><td>17.9%</td><td>GOOGL</td><td>7.8%</td></tr><tr><td>6</td><td>YELP</td><td>15.5%</td><td>SSTK</td><td>7.4%</td><td>CART</td><td>17.1%</td><td>ABNB</td><td>7.3%</td></tr><tr><td>7</td><td>PINS</td><td>15.5%</td><td>CART</td><td>6.5%</td><td>WW</td><td>15.5%</td><td>CART</td><td>5.5%</td></tr><tr><td>8</td><td>ETSY</td><td>14.3%</td><td>UBER</td><td>6.4%</td><td>RDDT</td><td>15.4%</td><td>FIGS</td><td>2.1%</td></tr><tr><td>9</td><td>PTON</td><td>14.3%</td><td>BKNG</td><td>5.6%</td><td>DUOL</td><td>14.1%</td><td>AMZN</td><td>0.8%</td></tr><tr><td>10</td><td>BMBL</td><td>12.5%</td><td>DASH</td><td>5.6%</td><td>PLTK</td><td>13.0%</td><td>EA</td><td>0.5%</td></tr></table>

<table><tr><td rowspan="2">Bottom 10</td><td colspan="2">Short interest %</td><td colspan="2">1 Week Price Move</td><td colspan="2">1 Month Price Move</td><td colspan="2">YTD</td></tr><tr><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td><td>Ticker</td><td>6/26/2026</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>AMZN</td><td>1.0%</td><td>WW</td><td>-16.7%</td><td>SNAP</td><td>-23.3%</td><td>Z</td><td>-54.3%</td></tr><tr><td>2</td><td>META</td><td>1.4%</td><td>GOOGL</td><td>-8.3%</td><td>TTD</td><td>-17.2%</td><td>TTD</td><td>-51.6%</td></tr><tr><td>3</td><td>GOOGL</td><td>1.5%</td><td>RBLX</td><td>-7.7%</td><td>GOOGL</td><td>-13.2%</td><td>SNAP</td><td>-45.4%</td></tr><tr><td>4</td><td>CRTO</td><td>2.2%</td><td>FIGS</td><td>-5.8%</td><td>Z</td><td>-12.8%</td><td>WW</td><td>-45.3%</td></tr><tr><td>5</td><td>UBER</td><td>2.8%</td><td>SNAP</td><td>-5.4%</td><td>CHWY</td><td>-12.7%</td><td>CHWY</td><td>-43.9%</td></tr><tr><td>6</td><td>BKNG</td><td>3.2%</td><td>AMZN</td><td>-4.8%</td><td>AMZN</td><td>-12.3%</td><td>RBLX</td><td>-41.3%</td></tr><tr><td>7</td><td>ABNB</td><td>3.7%</td><td>META</td><td>

[中间内容因长度限制已省略]

stment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Internet

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/29/2026)</td></tr><tr><td colspan="3">Brian Nowak, CFA</td></tr><tr><td>Airbnb Inc (ABNB.O)</td><td>U (12/06/2022)</td><td>$147.17</td></tr><tr><td>Alphabet Inc. (GOOGL.O)</td><td>O (08/11/2015)</td><td>$353.65</td></tr><tr><td>Amazon.com Inc (AMZN.O)</td><td>O (04/24/2015)</td><td>$240.14</td></tr><tr><td>Booking Holdings Inc (BKNG.O)</td><td>O (02/23/2026)</td><td>$182.41</td></tr><tr><td>DoorDash Inc (DASH.O)</td><td>O (02/21/2024)</td><td>$184.82</td></tr><tr><td>Expedia Inc. (EXPE.O)</td><td>E (01/09/2019)</td><td>$265.28</td></tr><tr><td>Instacart (CART.O)</td><td>E (01/29/2024)</td><td>$47.23</td></tr><tr><td>Lyft Inc (LYFT.O)</td><td>E (10/24/2019)</td><td>$15.25</td></tr><tr><td>Meta Platforms Inc (META.O)</td><td>O (03/20/2023)</td><td>$562.60</td></tr><tr><td>Pinterest Inc (PINS.N)</td><td>O (07/20/2025)</td><td>$21.88</td></tr><tr><td>Reddit Inc (RDDT.N)</td><td>O (12/08/2024)</td><td>$174.39</td></tr><tr><td>Snap Inc. (SNAP.N)</td><td>E (07/22/2024)</td><td>$4.42</td></tr><tr><td>Uber Technologies Inc (UBER.N)</td><td>O (06/04/2019)</td><td>$75.50</td></tr><tr><td colspan="3">Matthew Cost</td></tr><tr><td>AppLovin Corp (APP.O)</td><td>O (04/10/2025)</td><td>$498.76</td></tr><tr><td>Compass, Inc. (COMP.N)</td><td>E (01/12/2026)</td><td>$12.00</td></tr><tr><td>Criteo SA (CRTO.O)</td><td>E (01/26/2016)</td><td>$18.60</td></tr><tr><td>DoubleVerify Holdings Inc (DV.N)</td><td>E (06/25/2024)</td><td>$10.92</td></tr><tr><td>Electronic Arts Inc (EA.O)</td><td>E (08/04/2021)</td><td>$205.05</td></tr><tr><td>Liftoff Mobile Inc. (LFTO.O)</td><td>E (06/29/2026)</td><td>$25.47</td></tr><tr><td>MNTN Inc (MNTN.N)</td><td>E (06/16/2025)</td><td>$9.03</td></tr><tr><td>Opendoor Technologies Inc (OPEN.O)</td><td>E (07/24/2023)</td><td>$4.60</td></tr><tr><td>Playtika Holding Corp (PLTK.O)</td><td>E (11/27/2022)</td><td>$3.91</td></tr><tr><td>Roblox Corporation (RBLX.N)</td><td>O (11/04/2024)</td><td>$54.34</td></tr><tr><td>Shutterstock Inc (SSTK.N)</td><td>E (07/28/2022)</td><td>$14.13</td></tr><tr><td>Take-Two Interactive Software (TTWO.O)</td><td>O (02/01/2018)</td><td>$247.15</td></tr><tr><td>Trade Desk Inc (TTD.O)</td><td>E (09/10/2025)</td><td>$18.65</td></tr><tr><td>Unity Software Inc (U.N)</td><td>O (09/02/2024)</td><td>$28.31</td></tr><tr><td>Webtoon Entertainment Inc (WBTN.O)</td><td>E (07/22/2024)</td><td>$12.04</td></tr><tr><td>Yelp Inc (YELP.N)</td><td>U (01/10/2019)</td><td>$24.63</td></tr><tr><td>Zillow Group Inc (Z.O)</td><td>E (04/18/2018)</td><td>$31.38</td></tr><tr><td colspan="3">Nathan Feather</td></tr><tr><td>Bumble Inc. (BMBL.O)</td><td>E (03/08/2021)</td><td>$3.20</td></tr><tr><td>Chewy Inc (CHWY.N)</td><td>O (10/31/2023)</td><td>$19.42</td></tr><tr><td>Duolingo Inc (DUOL.O)</td><td>E (02/27/2026)</td><td>$116.03</td></tr><tr><td>eBay Inc (EBAY.O)</td><td>O (04/18/2024)</td><td>$110.80</td></tr><tr><td>Etsy Inc (ETSY.N)</td><td>E (07/20/2025)</td><td>$79.66</td></tr><tr><td>FIGS, Inc. (FIGS.N)</td><td>E (02/29/2024)</td><td>$11.08</td></tr><tr><td>Grindr Inc. (GRND.N)</td><td>E (02/24/2026)</td><td>$14.44</td></tr><tr><td>Match Group Inc (MTCH.O)</td><td>E (04/18/2024)</td><td>$38.73</td></tr><tr><td>Peloton Interactive, Inc. (PTON.O)</td><td>E (03/14/2022)</td><td>$5.77</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$23.61</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$16.40</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
