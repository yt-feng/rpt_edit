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
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
ASIA INDEX STRATEGY

# FTSE China Index Series Review and Flow Implications (June 2026)

What Happened? FTSE Russell announced the results of its quarterly index review for the FTSE China Index Series after the market closed on June 3 (Wednesday). All changes will take effect after market close on June 18 (Thursday).

Constituent Changes: For the FTSE China 50, Yangtze Optical Fibre & Cable (H) (6869), and Giga Device Semiconductor (H) (3986) will replace China Tower (H) (788), and CRRC (H) (1766). For the FTSE China A50, Suzhou Dongshan Precision (A) (002384), Giga Device Semiconductor (A) (603986), Victory Giant Technology (A) (300476), Montage Technology (A) (688008), and Weichai Power (A) (000338) will replace Ping An Bank (A) (000001), China State Construction Eng. (A) (601668), Shenzhen Mindray Bio-Medical Elec. (A) (300760), Haitian Flavouring & Food (A) (603288), and Haier Smart Home (A) (600690). Weight adjustments will be around 3.5% for China 50 and 7.1% for China A50. (Exhibit 3)

Index Implications: Following the rebalancing, FTSE China 50 index's forward 12-month P/E and EPS growth (2026-27 CAGR) are expected to remain unchanged (9.3x and $10.2\%$ ), while trailing dividend yield would shift from $3.3\%$ to $3.2\%$ . For China A50 index, the corresponding metrics would change from 12.7x to 13.5x (fP/E), $2.6\%$ to $2.4\%$ (D/Y), and $13.9\%$ to $15.7\%$ (EPS growth). (Exhibit 1)

Sector Implications: Tech Hardware & Semis (+US\$550mn), Consumer Retail (+US\$330mn), and Internet/Media (+US\$140mn) are poised to see the largest passive inflows, while Insurance & Fins Services (-US\$130mn) and Energy (-US\$110mn) may face the biggest outflows. These changes reflect rebalancing for existing and pending constituents in FTSE China 50/A50, combined with potential flows from FTSE GEIS. Overall, we estimate that the FTSE rebalancing could generate around US\$3.0bn in gross two-way passive flows for China. (Exhibit 2)

Historical vs. Current Patterns: For the FTSE China 50, current additions have significantly outperformed relative to historical patterns, and post-announcement performance has tended to be volatile and mildly negative around/after the effective date (Exhibit 4). FTSE China A50 additions have outperformed deletions ahead of the announcement as well, while historical patterns suggest a post-announcement reversal, followed by a recovery around the effective date (Exhibit 5).

Alvin So, CFA

+852-2978-1585 | alvin.so@gs.com

GS (Asia) L.L.C.

Timothy Moe, CFA

+65-6889-1199 | timothy.moe@gs.com

GS (Singapore) Pte

Kinger Lau, CFA

+852-2978-1224 | kinger.lau@gs.com

GS (Asia) L.L.C.

Sunil Koul

+44(20)7051-4931 | sunil.koul@gs.com

GS International

Si Fu, Ph.D.

+852-2978-0200 | si.fu@gs.com

GS (Asia) L.L.C.

Kevin Wang, CFA

+852-2978-2446|kevin.wang@gs.com

GS (Asia) L.L.C.

Exhibit 1: FTSE Russell announced the quarterly review results for the China Index Series, with 2/5 stock changes in the China 50/A50, effective after market close on June 18

<table><tr><td rowspan="2"></td><td rowspan="2">FTSE China Index Series</td><td colspan="2">Jun 2026 Review Summary</td></tr><tr><td>China 50</td><td>China A50</td></tr><tr><td rowspan="3">Stock Changes</td><td>Current # Constituents</td><td>50</td><td>50</td></tr><tr><td># Stocks Added / Deleted</td><td>2 / 2</td><td>5 / 5</td></tr><tr><td>% Weight Rebalanced</td><td>3.5%</td><td>7.1%</td></tr><tr><td rowspan="4">Liquidity</td><td>Proforma Index Cap (US$bn)</td><td>1,653</td><td>916</td></tr><tr><td>Proforma % Change</td><td>-3.8%</td><td>+3.0%</td></tr><tr><td>Proforma 3M ADVT (US$bn)</td><td>10.8</td><td>42.8</td></tr><tr><td>Proforma % Change</td><td>+6.7%</td><td>+22.4%</td></tr><tr><td rowspan="3">Valuations / Growth</td><td>NTM P/E (x)(Current / Proforma)</td><td>9.3x /9.3x</td><td>12.7x /13.5x</td></tr><tr><td>LTM Dividend Yield (%)(Current / Proforma)</td><td>3.3% /3.2%</td><td>2.6% /2.4%</td></tr><tr><td>2026-27 EPS Growth (%)(Current / Proforma)</td><td>10.2% /10.2%</td><td>13.9% /15.7%</td></tr><tr><td>Passive Flows (+FTSE GEIS)</td><td>Potential Gross Passive Buying + Selling (Two-way) (US$mn)</td><td>1,779</td><td>1,167</td></tr><tr><td rowspan="2">Trading Pattern Prior to Announce.</td><td>Return Since 20D Prior to Ann.(Additions / Deletions)</td><td>+28.4% /-1.1%</td><td>+16.7% /-4.1%</td></tr><tr><td>Share Turnover % Chg (Median 20D vs. Prior 3M) (Add / Del)</td><td>+23% /+19%</td><td>+55% /+6%</td></tr></table>

Note: Potential passive flows consider both FTSE China and Global Index rebalancing impact. Pricing is as of Jun 3, 2026

Source: FTSE Russell, FactSet, Refinitiv, EPFR, GS Global Investment Research

## Exhibit 2: Tech Hardware & Semis, Consumer Retail, and Internet/Media are poised to see the largest passive inflows, while Insurance & Fins Services and Energy may face the biggest outflows

Current vs. Proforma Sector Weights and Changes in FTSE China 50 / A50, and Aggregate Potential Passive Flows

<table><tr><td rowspan="2" colspan="2">GICS Sector/Industry</td><td colspan="3">China 50</td><td colspan="3">China A50</td><td colspan="3">Passive Flows (US$mn)</td></tr><tr><td>Current %</td><td>Proforma %</td><td>Chg (bps)</td><td>Current %</td><td>Proforma %</td><td>Chg (bps)</td><td>Gross Buying</td><td>Gross Selling</td><td>Net Flows</td></tr><tr><td rowspan="3">Financials</td><td>Banks</td><td>23.6%</td><td>24.1%</td><td>+49</td><td>18.2%</td><td>16.7%</td><td>-149</td><td>176</td><td>-257</td><td>-81</td></tr><tr><td>Insurance &amp; Other Financials</td><td>10.2%</td><td>9.7%</td><td>-46</td><td>7.9%</td><td>7.7%</td><td>-25</td><td>20</td><td>-146</td><td>-125</td></tr><tr><td>Real Estate</td><td>1.1%</td><td>1.1%</td><td>-3</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>-6</td><td>-6</td></tr><tr><td rowspan="7">Domestic / Global Cyclicals</td><td>Capital Goods</td><td>3.5%</td><td>3.2%</td><td>-27</td><td>12.5%</td><td>12.3%</td><td>-26</td><td>80</td><td>-129</td><td>-49</td></tr><tr><td>Transportation</td><td>0.5%</td><td>0.4%</td><td>-4</td><td>1.9%</td><td>1.9%</td><td>-1</td><td>7</td><td>-23</td><td>-16</td></tr><tr><td>Autos &amp; Components</td><td>3.8%</td><td>3.6%</td><td>-23</td><td>2.4%</td><td>2.3%</td><td>-7</td><td>0</td><td>-41</td><td>-41</td></tr><tr><td>Consumer Retail &amp; Services</td><td>22.6%</td><td>22.2%</td><td>-46</td><td>1.3%</td><td>0.7%</td><td>-62</td><td>455</td><td>-128</td><td>327</td></tr><tr><td>Tech Hardware &amp; Semis</td><td>5.5%</td><td>6.5%</td><td>+100</td><td>27.9%</td><td>33.2%</td><td>+532</td><td>658</td><td>-107</td><td>552</td></tr><tr><td>Software &amp; Services</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Internet/Media &amp; Entertainment</td><td>16.3%</td><td>17.0%</td><td>+77</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>210</td><td>-73</td><td>137</td></tr><tr><td rowspan="3">Commodities</td><td>Energy</td><td>5.1%</td><td>5.0%</td><td>-13</td><td>4.9%</td><td>4.5%</td><td>-41</td><td>0</td><td>-105</td><td>-105</td></tr><tr><td>Metals &amp; Mining</td><td>3.9%</td><td>3.9%</td><td>-6</td><td>4.6%</td><td>4.5%</td><td>-14</td><td>19</td><td>-29</td><td>-10</td></tr><tr><td>Chemicals &amp; Other Materials</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>1.1%</td><td>1.0%</td><td>-3</td><td>0</td><td>-3</td><td>-3</td></tr><tr><td rowspan="4">Defensives</td><td>Consumer Staples</td><td>0.8%</td><td>0.8%</td><td>-3</td><td>10.6%</td><td>9.6%</td><td>-105</td><td>2</td><td>-89</td><td>-88</td></tr><tr><td>Health Care</td><td>2.2%</td><td>2.1%</td><td>-3</td><td>3.3%</td><td>2.5%</td><td>-89</td><td>42</td><td>-70</td><td>-27</td></tr><tr><td>Utilities</td><td>0.3%</td><td>0.3%</td><td>+0</td><td>3.2%</td><td>3.1%</td><td>-9</td><td>5</td><td>-8</td><td>-3</td></tr><tr><td>Telecommunication Services</td><td>0.5%</td><td>0.0%</td><td>-51</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>-53</td><td>-53</td></tr></table>

Note: Potential passive flows consider both FTSE China and Global Index rebalancing impact. Pricing is as of Jun 3, 2026

Source: FactSet, Refinitiv, EPFR, GS Global Investment Research

Exhibit 3: FTSE China 50/A50: Stocks that may experience the most significant net passive buying or selling flows following the FTSE China and Global Equity Index Series (GEIS) rebalancing

<table><tr><td rowspan="2">BBG Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">Sector</td><td rowspan="2">Listed Mkt Cap (US$mn)</td><td rowspan="2">Free Float Cap (US$mn)</td><td rowspan="2">3M ADVT (US$mn)</td><td colspan="3">Potential Passive Flows (US$mn)</td><td rowspan="2">Net Passive Flows (US$mn)</td><td rowspan="2">Net Flows / 3M ADVT (days)</td><td rowspan="2">S3&#x27;s Short Interest 20D Chg (pp)</td><td rowspan="2">Days to Cover (1M ADVT)</td><td rowspan="2">S3&#x27;s HF Long Interest 20D Chg (pp)</td><td rowspan="2">Return since 20D prior to ann.</td><td rowspan="2">Return since 10D prior to ann.</td><td rowspan="2">Share Turnover % Chg (Median 20D vs. Prior 3M)</td><td colspan="2">Corporate Event Dates</td></tr><tr><td>China 50</td><td>China A50</td><td>All Cap / World</td><td>Expected Next Report</td><td>Ex-Dividend</td></tr><tr><td colspan="6">FTSE China 50/A50 Stocks with net passive buying following FTSE China and GEIS rebalancing</td><td colspan="3"></td><td>(ranked)</td><td>&gt;0.1</td><td colspan="8"></td></tr><tr><td>9988 HK</td><td>Alibaba Group</td><td>Consumer Retail &amp; Services</td><td>320,576</td><td>290,579</td><td>1,428</td><td>20</td><td>-</td><td>273</td><td>293</td><td>0.2</td><td>(0.2%)</td><td>1.6</td><td>0.0%</td><td>(6%)</td><td>(4%)</td><td>23%</td><td>Aug 28</td><td>Jun 10</td></tr><tr><td>700 HK</td><td>Tencent</td><td>Internet/Media &amp; Entertainment</td><td>560,323</td><td>380,436</td><td>1,802</td><td>119</td><td>-</td><td>90</td><td>208</td><td>0.1</td><td>0.0%</td><td>1.9</td><td>0.0%</td><td>2%</td><td>2%</td><td>37%</td><td>Aug 13</td><td></td></tr><tr><td>939 HK</td><td>CCB (H)</td><td>Banks</td><td>265,663</td><td>96,772</td><td>287</td><td>92</td><td>-</td><td>34</td><td>126</td><td>0.4</td><td>0.3%</td><td>6.3</td><td>0.0%</td><td>(4%)</td><td>(2%)</td><td>(11%)</td><td>Aug 14</td><td>Jul 2</td></tr><tr><td>6869 HK</td><td>Yangtze Optical Fibre &amp; Cable (H)</td><td>Tech Hardware &amp; Semis</td><td>12,523</td><td>11,834</td><td>575</td><td>110</td><td>-</td><td>(3)</td><td>107</td><td>0.2</td><td>(5.9%)</td><td>1.8</td><td>0.0%</td><td>19%</td><td>12%</td><td>(38%)</td><td>Aug 31</td><td></td></tr><tr><td>3986 HK</td><td>Giga Device Semiconductor (H)</td><td>Tech Hardware &amp; Semis</td><td>3,017</td><td>2,020</td><td>138</td><td>15</td><td>-</td><td>90</td><td>105</td><td>0.8</td><td>-</td><td>-</td><td>-</td><td>38%</td><td>4%</td><td>85%</td><td>Aug 21</td><td></td></tr><tr><td>9618 HK</td><td>JD.com</td><td>Consumer Retail &amp; Services</td><td>38,258</td><td>36,307</td><td>172</td><td>(10)</td><td>-</td><td>58</td><td>48</td><td>0.3</td><td>0.1%</td><td>6.3</td><td>0.0%</td><td>(1%)</td><td>(10%)</td><td>11%</td><td>Aug 14</td><td></td></tr><tr><td>3690 HK</td><td>Meituan</td><td>Consumer Retail &amp; Services</td><td>61,045</td><td>52,925</td><td>542</td><td>(39)</td><td>-</td><td>83</td><td>44</td><td>0.1</td><td>-</td><td>-</td><td>0.0%</td><td>(3%)</td><td>(3%)</td><td>(3%)</td><td>Jun 1</td><td></td></tr><tr><td>1658 HK</td><td>Postal Savings Bank of China (H)</td><td>Banks</td><td>12,795</td><td>6,056</td><td>22</td><td>3</td><td>-</td><td>26</td><td>29</td><td>1.3</td><td>0.3%</td><td>14.8</td><td>0.0%</td><td>(2%)</td><td>(0%)</td><td>(32%)</td><td>Aug 14</td><td>Jul 3</td></tr><tr><td>6160 HK</td><td>BeOne Medicines</td><td>Health Care</td><td>30,722</td><td>23,825</td><td>94</td><td>(2)</td><td>-</td><td>25</td><td>24</td><td>0.3</td><td>(0.3%)</td><td>3.7</td><td>0.0%</td><td>(9%)</td><td>(9%)</td><td>35%</td><td>Aug 6</td><td></td></tr><tr><td>2611 HK</td><td>Guotai Haitong (H)</td><td>Insurance &amp; Other Financials</td><td>6,491</td><td>3,903</td><td>20</td><td>1</td><td>-</td><td>19</td><td>20</td><td>1.0</td><td>(0.3%)</td><td>6.0</td><td>0.0%</td><td>6%</td><td>8%</td><td>11%</td><td>Aug 31</td><td></td></tr><tr><td>002384 C2</td><td>Suzhou Dongshan Precision (A)</td><td>Tech Hardware &amp; Semis</td><td>57,135</td><td>43,700</td><td>2,106</td><td>-</td><td>134</td><td>(1)</td><td>133</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>17%</td><td>0%</td><td>7%</td><td>Aug 26</td><td>May 27</td></tr><tr><td>603986 C1</td><td>Giga Device Semiconductor (A)</td><td>Tech Hardware &amp; Semis</td><td>46,883</td><td>40,844</td><td>2,214</td><td>-</td><td>108</td><td>0</td><td>108</td><td>0.0</td><td>-</td><td>-</td><td>-</td><td>43%</td><td>11%</td><td>84%</td><td>Aug 24</td><td>May 26</td></tr><tr><td>300476 C2</td><td>Victory Giant Technology (A)</td><td>Tech Hardware &amp; Semis</td><td>44,665</td><td>28,429</td><td>2,073</td><td>-</td><td>101</td><td>1</td><td>102</td><td>0.0</td><td>-</td><td>-</td><td>-</td><td>8%</td><td>6%</td><td>55%</td><td>Aug 26</td><td></td></tr><tr><td>688008 C1</td><td>Montage Technology (A)</td><td>Tech Hardware &amp; Semis</td><td>40,181</td><td>34,182</td><td>1,708</td><td>-</td><td>95</td><td>(0)</td><td>95</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>28%</td><td>(1%)</td><td>106%</td><td>Aug 31</td><td></td></tr><tr><td>000338 C2</td><td>Weichai Power (A)</td><td>Capital Goods</td><td>32,016</td><td>25,178</td><td>519</td><td>-</td><td>72</td><td>(1)</td><td>71</td><td>0.1</td><td>-</td><td>-</td><td>-</td><td>(6%)</td><td>(1%)</td><td>(12%)</td><td>Aug 14</td><td></td></tr><tr><td colspan="6">FTSE China 50/A50 Stocks with net passive selling following FTSE China and GEIS rebalancing</td><td colspan="3"></td><td colspan="10"></td></tr><tr><td>3988 HK</td><td>Bank of China</td><td>Banks</td><td>56,658</td><td>46,719</td><td>145</td><td>(20)</td><td>-</td><td>(40)</td><td>(60)</td><td>(0.4)</td><td>0.2%</td><td>5.1</td><td>0.0%</td><td>2%</td><td>1%</td><td>11%</td><td>Aug 14</td><td>Jul 2</td></tr><tr><td>788 HK</td><td>China Tower (H)</td><td>Telecommunication Services</td><td>6,014</td><td>5,129</td><td>21</td><td>(52)</td><td>-</td><td>(1)</td><td>(53)</td><td>(2.5)</td><td>(0.6%)</td><td>3.9</td><td>0.0%</td><td>(6%)</td><td>(3%)</td><td>46%</td><td>Aug 5</td><td></td></tr><tr><td>6030 HK</td><td>CITIC (H)</td><td>Insurance &amp; Other Financials</td><td>8,666</td><td>5,304</td><td>36</td><td>(8)</td><td>-</td><td>(45)</td><td>(53)</td><td>(1.5)</td><td>(0.4%)</td><td>8.3</td><td>(0.0%)</td><td>(6%)</td><td>1%</td><td>(2%)</td><td>Aug 28</td><td></td></tr><tr><td>1810 HK</td><td>Xiaomi</td><td>Tech Hardware &amp; Semis</td><td>80,828</td><td>62,456</td><td>670</td><td>(22)</td><td>-</td><td>(21)</td><td>(42)</td><td>(0.1)</td><td>-</td><td>-</td><td>(0.0%)</td><td>(7%)</td><td>(5%)</td><td>(4%)</td><td>Aug 14</td><td></td></tr><tr><td>1211 HK</td><td>BYD (H)</td><td>Autos &amp; Components</td><td>45,472</td><td>45,430</td><td>400</td><td>(24)</td><td>-</td><td>(11)</td><td>(35)</td><td>(0.1)</td><td>0.5%</td><td>11.0</td><td>(0.0%)</td><td>(6%)</td><td>3%</td><td>(11%)</td><td>Aug 14</td><td>Jun 11</td></tr><tr><td>9888 HK</td><td>Baidu</td><td>Internet/Media &amp; Entertainment</td><td>39,936</td><td>36,999</td><td>190</td><td>(13)</td><td>-</td><td>(20)</td><td>(33)</td><td>(0.2)</td><td>-</td><td>-</td><td>0.1%</td><td>1%</td><td>(1%)</td><td>51%</td><td>Aug 20</td><td></td></tr><tr><td>2318 HK</td><td>Ping An Insurance (H)</td><td>Insurance &amp; Other Financials</td><td>55,688</td><td>46,578</td><td>288</td><td>(20)</td><td>-</td><td>(12)</td><td>(32)</td><td>(0.1)</td><td>(0.5%)</td><td>32.3</td><td>-</td><td>(7%)</td><td>(2%)</td><td>5%</td><td>Aug 14</td><td>Jun 2</td></tr><tr><td>9999 HK</td><td>NetEase</td><td>Internet/Media &amp; Entertainment</td><td>81,177</td><td>44,545</td><td>147</td><td>(17)</td><td>-</td><td>(11)</td><td>(28)</td><td>(0.2)</td><td>0.2%</td><td>4.3</td><td>0.0%</td><td>7%</td><td>8%</td><td>10%</td><td>Aug 14</td><td>Jun 4</td></tr><tr><td>1766 HK</td><td>CRRC (H)</td><td>Capital Goods</td><td>2,945</td><td>2,854</td><td>15</td><td>(24)</td><td>-</td><td>(1)</td><td>(25)</td><td>(1.7)</td><td>0.7%</td><td>8.0</td><td>0.0%</td><td>4%</td><td>3%</td><td>(8%)</td><td>Aug 24</td><td>Jun 22</td></tr><tr><td>1398 HK</td><td>ICBC (H)</td><td>Banks</td><td>75,309</td><td>62,192</td><td>186</td><td>(8)</td><td>-</td><td>(17)</td><td>(25)</td><td>(0.1)</td><td>0.2%</td><td>6.3</td><td>0.0%</td><td>(3%)</td><td>(2%)</td><td>(18%)</td><td>Aug 3</td><td></td></tr><tr><td>1919 HK</td><td>COSCO Shipping</td><td>Transportation</td><td>5,220</td><td>4,546</td><td>47</td><td>(4)</td><td>-</td><td>(15)</td><td>(19)</td><td>(0.4)</td><td>-</td><td>-</td><td>-</td><td>1%</td><td>(3%)</td><td>28%</td><td>Aug 14</td><td>May 28</td></tr><tr><td>2020 HK</td><td>ANTA Sports</td><td>Consumer Retail &amp; Services</td><td>27,335</td><td>12,523</td><td>85</td><td>(6)</td><td>-</td><td>(11)</td><td>(17)</td><td>(0.2)</td><td>(0.0%)</td><td>11.2</td><td>0.2%</td><td>(3%)</td><td>(2%)</td><td>(15%)</td><td>Aug 27</td><td></td></tr><tr><td>386 HK</td><td>China Petroleum &amp; Chemical (H)</td><td>Energy</td><td>13,322</td><td>12,366</td><td>88</td><td>(5)</td><td>-</td><td>(12)</td><td>(17)</td><td>(0.2)</td><td>(0.1%)</td><td>12.0</td><td>-</td><td>(7%)</td><td>(3%)</td><td>(22%)</td><td>Aug 14</td><td>Jun 8</td></tr><tr><td>2628 HK</td><td>China Life Insurance (H)</td><td>Insurance &amp; Other Financials</td><td>27,041</td><td>25,511</td><td>194</td><td>(10)</td><td>-</td><td>(7)</td><td>(17)</td><td>(0.1)</td><td>2.3%</td><td>5.3</td><td>0.0%</td><td>(7%)</td><td>(4%)</td><td>1%</td><td>Aug 14</td><td>Jun 30</td></tr><tr><td>857 HK</td><td>PetroChina (H)</td><td>Energy</td><td>28,941</td><td>28,614</td><td>200</td><td>(7)</td><td>-</td><td>(9)</td><td>(16)</td><td>(0.1)</td><td>-</td><td>-</td><td>0.1%</td><td>(8%)</td><td>(5%)</td><td>(21%)</td><td>Aug 14</td><td>Jun 18</td></tr><tr><td>000001 C2</td><td>Ping An Bank (A)</td><td>Banks</td><td>31,798</td><td>14,176</td><td>149</td><td>-</td><td>(72)</td><td>(1)</td><td>(72)</td><td>(0.5)</td><td>-</td><td>-</td><td>-</td><td>(3%)</td><td>2%</td><td>19%</td><td>Aug 24</td><td></td></tr><tr><td>601668 C1</td><td>China State Construction Eng. (A)</td><td>Capital Goods</td><td>29,698</td><td>11,227</td><td>156</td><td>-</td><td>(66)</td><td>(0)</td><td>(67)</td><td>(0.4)</td><td>-</td><td>-</td><td>-</td><td>(3%)</td><td>(1%)</td><td>(25%)</td><td>Aug 28</t

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
