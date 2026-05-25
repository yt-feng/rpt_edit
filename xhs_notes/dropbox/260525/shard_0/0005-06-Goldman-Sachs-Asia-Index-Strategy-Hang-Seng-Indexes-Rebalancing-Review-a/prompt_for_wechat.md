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

# Hang Seng Indexes Rebalancing Review and Flow Implications (June 2026)

What Happened? Hang Seng Indexes Company announced its quarterly index review results after market close on May 22 (Friday). All changes will be implemented after market close on June 6 (Friday).

Constituent Changes: Among major indexes, BeOne Medicines (6160), Aluminum Corp. of China (2600), and J&T Global Express (1519) will be added to the Hang Seng Index (HSI), bringing the total number of constituents from 90 to 93. Within the Hang Seng China Enterprises Index (HSCEI), Hansoh Pharma (3692) and Akeso (9926) will replace Sunny Optical (2382) and Haier Smart Home (6690). Within Hang Seng TECH (HSTECH), MiniMax (100) and Knowledge Atlas Tech (Zhipu) (2513) will replace Kingsoft (3888) and Kingdee (268). For the Hang Seng Composite Index (HSCI), 7 stocks will be added to the universe. In aggregate, $3.4\%$ , $2.8\%$ , and $4.5\%$ of the HSI, HSCEI, and HSTECH weights will be adjusted after re-capping and FAF/share changes.

Index Implications: The proforma index cap is expected to change to US\$2,150 billion for HSI (+4.5%), US\$1,410 billion for HSCEI (+2.3%), and US\$455 billion for HSTECH (+3.4%) after rebalancing and re-capping. Forward 12M P/E and EPS growth (2026–27 CAGR) are expected to change as follows: HSI from 11.1x to 11.2x and 11.3% to 11.6%; HSCEI from 10.1x to 10.2x and 11.8% to 11.9%; and HSTECH from 18.6x to 18.3x and 31.2% to 30.3% (Exhibit 1).

Sector Implications: Internet/Media & Entertainment (+US\$1.4bn) and Health Care (+US\$850mn) are expected to see the largest passive buying, while Tech H/W & Semis (-US\$1.0bn each), Energy, Banks, and Insurance & Financial Services (-US\$350-500mn each) may experience the largest outflows (Exhibit 2). In aggregate, the rebalancing could generate nearly US\$11bn in gross two-way passive flows.

Stock Implications: Top six stocks in the Hang Seng Family of Indexes expected to see the largest passive net buying flows are: Tencent (re-capping higher), BeOne Medicines (added to HSI), Baidu/NetEase (higher FAF), and Zhipu/Minimax (added to HSTECH), with potential inflows ranging from US\$200mn to US\$1.0bn. Stocks likely to see the largest passive outflows include SMIC/Meituan (re-capping lower), Kingdee/Kingsoft (removed from HSTECH), and CCB/AIA (mechanical weight adjustments), ranging from -US\$140mn to -US\$700mn (Exhibit 4).

Historical vs. Current Patterns: HSI and HSCEI additions have underperformed deletions pre-announcement, while HSTECH and HSCI additions have sharply

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

Mark Hung

+852-3465-4266 | mark.hung@gs.com

GS (Asia) L.L.C.

outperformed, albeit with a volatile path. Historically, HSI and HSCEI additions tend to outperform moderately post-announcement before reversing around the effective date, while for HSTECH and HSCI, the outperformance typically extends through to the effective date (from Exhibit 5).

Southbound implications: HSCI constituent changes typically affect Southbound (SB) eligibility, with stricter listing history, market cap, and liquidity requirements for stocks with WVR status. Historically, SB ownership rose by 1pp within two days after inclusion becomes effective, followed by 5pp over three months, with share prices often rallying beforehand and declining post-inclusion before stabilizing (Exhibit 4).

Exhibit 1: Hang Seng Indexes have announced their quarterly review results, with changes set to take effect after market close on June 5; In aggregate, the rebalancing could generate nearly US\$11bn in gross two-way passive flows 

<table><tr><td rowspan="2"></td><td rowspan="2">Hang Seng Indexes</td><td colspan="4">June 2026 Review Summary</td></tr><tr><td>HSI</td><td>HSCEI</td><td>HS Tech</td><td>HSCI</td></tr><tr><td rowspan="3">Stock Changes</td><td>Current # Constituents</td><td>90</td><td>50</td><td>30</td><td>527</td></tr><tr><td># Stocks Added / Deleted</td><td>3/0</td><td>2/2</td><td>2/2</td><td>7/0</td></tr><tr><td>% Weight Rebalanced</td><td>3.4%</td><td>2.8%</td><td>4.5%</td><td>0.3%</td></tr><tr><td rowspan="4">Liquidity</td><td>Proforma Index Cap (US$bn)</td><td>2,150</td><td>1,407</td><td>453</td><td>3,307</td></tr><tr><td>Proforma % Change</td><td>+4.5%</td><td>+2.3%</td><td>+3.4%</td><td>+0.3%</td></tr><tr><td>Proforma 3M ADVT (US$bn)</td><td>14.8</td><td>12.1</td><td>8.6</td><td>24.4</td></tr><tr><td>Proforma % Change</td><td>+1.5%</td><td>+0.3%</td><td>+4.0%</td><td>+2.2%</td></tr><tr><td rowspan="3">Valuations / Growth</td><td>NTM P/E (x)(Current / Proforma)</td><td>11.1x/11.2x</td><td>10.1x/10.2x</td><td>18.6x/18.3x</td><td>11.6x/11.6x</td></tr><tr><td>LTM Dividend Yield (%) (Current / Proforma)</td><td>3.5%/3.4%</td><td>3.6%/3.5%</td><td>1.6%/1.6%</td><td>3.3%/3.3%</td></tr><tr><td>2026-27 EPS CAGR (%)(Current / Proforma)</td><td>11.3%/11.6%</td><td>11.8%/11.9%</td><td>31.2%/30.3%</td><td>14.5%/14.7%</td></tr><tr><td>Passive Flows</td><td>Potential Gross Passive Buying + Selling (Two-way) (US$mn)</td><td>3,855</td><td>695</td><td>4,488</td><td>-</td></tr><tr><td rowspan="2">Trading Pattern Prior to Announce.</td><td>Return Since 20D Prior to Ann.(Additions / Deletions)</td><td>-9.3%/-</td><td>-12.9%/+5.8%</td><td>+18.0%/-9.5%</td><td>+5.6%/-</td></tr><tr><td>Share Turnover % Chg (Avg 20D)(Additions / Deletions)</td><td>-4%/-</td><td>+1%/+12%</td><td>-35%/-2%</td><td>-21%/-</td></tr></table>

Note: Pricing is as of May 22, 2026   
Source: HSIL, FactSet, Refinitiv, EPFR, GS Global Investment Research

Exhibit 2: Internet/Media & Entertainment and Health Care are expected to see the largest passive buying, while Tech H/W & Semis, Energy, Banks, and Insurance & Financial Services may experience the largest outflows   
Current vs. Proforma Sector Weights and Changes in Major Hang Seng Indexes, and Aggregate Potential Passive Flows 

<table><tr><td rowspan="2" colspan="2">GICS Sector/Industry</td><td colspan="3">HSI</td><td colspan="3">HSCEI</td><td colspan="3">HS Tech</td><td colspan="3">Passive Flows (US$mnn)</td></tr><tr><td>Current %</td><td>Proforma %</td><td>Change (bps)</td><td>Current %</td><td>Proforma %</td><td>Change (bps)</td><td>Current %</td><td>Proforma %</td><td>Change (bps)</td><td>Gross Buying</td><td>Gross Selling</td><td>Net Flows</td></tr><tr><td rowspan="3">Financials</td><td>Banks</td><td>21.8%</td><td>21.0%</td><td>-79</td><td>20.9%</td><td>20.4%</td><td>-47</td><td>0.0%</td><td>0.0%</td><td></td><td>61</td><td>-533</td><td>-472</td></tr><tr><td>Insurance &amp; Other Financials</td><td>12.5%</td><td>12.0%</td><td>-54</td><td>6.7%</td><td>6.6%</td><td>-15</td><td>0.0%</td><td>0.0%</td><td></td><td>57</td><td>-399</td><td>-343</td></tr><tr><td>Real Estate</td><td>4.5%</td><td>4.3%</td><td>-20</td><td>2.4%</td><td>2.4%</td><td>-6</td><td>0.0%</td><td>0.0%</td><td></td><td>98</td><td>-318</td><td>-219</td></tr><tr><td rowspan="7">Domestic / Global Cyclicals</td><td>Capital Goods</td><td>3.5%</td><td>3.6%</td><td>+15</td><td>0.7%</td><td>0.7%</td><td>-2</td><td>0.0%</td><td>0.0%</td><td></td><td>224</td><td>-159</td><td>65</td></tr><tr><td>Transportation</td><td>1.2%</td><td>1.4%</td><td>+18</td><td>0.7%</td><td>0.6%</td><td>-11</td><td>0.0%</td><td>0.0%</td><td></td><td>228</td><td>-75</td><td>153</td></tr><tr><td>Autos &amp; Components</td><td>3.4%</td><td>3.3%</td><td>-15</td><td>6.1%</td><td>5.9%</td><td>-15</td><td>14.6%</td><td>15.0%</td><td></td><td>268</td><td>-200</td><td>68</td></tr><tr><td>Consumer Retail &amp; Services</td><td>15.9%</td><td>15.8%</td><td>-13</td><td>18.3%</td><td>17.9%</td><td>-38</td><td>28.0%</td><td>27.4%</td><td></td><td>634</td><td>-801</td><td>-167</td></tr><tr><td>Tech Hardware &amp; Semis</td><td>6.7%</td><td>6.4%</td><td>-31</td><td>9.7%</td><td>9.0%</td><td>-72</td><td>25.7%</td><td>24.4%</td><td></td><td>177</td><td>-1,172</td><td>-995</td></tr><tr><td>Software &amp; Services</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.7%</td><td>0.6%</td><td>-1</td><td>4.5%</td><td>4.8%</td><td></td><td>516</td><td>-404</td><td>112</td></tr><tr><td>Internet/Media &amp; Entertainment</td><td>10.4%</td><td>11.4%</td><td>+104</td><td>12.1%</td><td>13.4%</td><td>+132</td><td>25.1%</td><td>26.5%</td><td></td><td>1,845</td><td>-438</td><td>1,407</td></tr><tr><td rowspan="3">Commodities</td><td>Energy</td><td>5.6%</td><td>5.3%</td><td>-24</td><td>8.3%</td><td>8.1%</td><td>-19</td><td>0.0%</td><td>0.0%</td><td></td><td>0</td><td>-493</td><td>-493</td></tr><tr><td>Metals &amp; Mining</td><td>2.3%</td><td>2.5%</td><td>+14</td><td>2.8%</td><td>2.8%</td><td>-6</td><td>0.0%</td><td>0.0%</td><td></td><td>138</td><td>-227</td><td>-89</td></tr><tr><td>Chemicals &amp; Other Materials</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td></td><td>18</td><td>-1</td><td>17</td></tr><tr><td></td><td>Consumer Staples</td><td>2.3%</td><td>2.2%</td><td>-10</td><td>1.2%</td><td>1.2%</td><td>-3</td><td>2.1%</td><td>2.0%</td><td></td><td>213</td><td>-97</td><td>116</td></tr><tr><td rowspan="3">Defensives</td><td>Health Care</td><td>3.2%</td><td>4.4%</td><td>+123</td><td>3.9%</td><td>5.0%</td><td>+116</td><td>0.0%</td><td>0.0%</td><td></td><td>922</td><td>-79</td><td>843</td></tr><tr><td>Utilities</td><td>2.6%</td><td>2.5%</td><td>-11</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td></td><td>198</td><td>-81</td><td>117</td></tr><tr><td>Telecommunication Services</td><td>4.0%</td><td>3.9%</td><td>-17</td><td>5.4%</td><td>5.3%</td><td>-12</td><td>0.0%</td><td>0.0%</td><td></td><td>0</td><td>-118</td><td>-118</td></tr></table>

Note: Overall gross buying/selling and net passive flows are based on our estimates across all Hang Seng Indexes changes. Pricing is as of May 22, 2026

Exhibit 3: Stocks that may experience the most significant net passive buying or selling flows (25 stocks each) following the Hang Seng Indexes rebalancing (Underlined bold numbers indicate additions or deletions) 

<table><tr><td rowspan="2">BBG Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">Sector</td><td rowspan="2">Listed Mkt Cap (US$mn)</td><td rowspan="2">Free Float Cap* (US$mn)</td><td rowspan="2">3M ADVT (US$mn)</td><td colspan="4">Potential Passive Flows * (US$mn)</td><td rowspan="2">Net Passive Flows (US$mn)</td><td rowspan="2">Net Flows / 3M ADVT (days)</td><td rowspan="2">S3&#x27;s Short Interest 20D Chg (pp)</td><td rowspan="2">Days to Cover (1M ADVT)</td><td rowspan="2">S3&#x27;s HF Long Interest 20D Chg (pp)</td><td rowspan="2">Return since 20D prior to ann.</td><td rowspan="2">Share Turnover % Chg (Median 20D vs. Prior 3M)</td><td colspan="2">Corporate Event Dates</td></tr><tr><td>HSI</td><td>HSCEI</td><td>HS Tech</td><td>Others</td><td>Expected Next Report</td><td>Ex-Dividend</td></tr><tr><td colspan="6">Stocks with potential net passive buying following Hang Seng Indexes rebalancing</td><td colspan="4"></td><td>(ranked).</td><td>&gt;0.1</td><td colspan="7"></td></tr><tr><td>700 HK</td><td>Tencent</td><td>Internet/Media &amp; Entertainment</td><td>510,885</td><td>318,821</td><td>1,772</td><td>458</td><td>103</td><td>413</td><td>-</td><td>974</td><td>0.5</td><td>0.1%</td><td>2.0</td><td>0.0%</td><td>(10%)</td><td>15%</td><td>Aug 13</td><td>-</td></tr><tr><td>6160 HK</td><td>BeOne Medicines</td><td>Health Care</td><td>33,333</td><td>27,091</td><td>93</td><td>755</td><td>(6)</td><td>-</td><td>-</td><td>749</td><td>8.1</td><td>(0.0%)</td><td>4.3</td><td>0.1%</td><td>2%</td><td>15%</td><td>Aug 6</td><td>-</td></tr><tr><td>9888 HK</td><td>Baidu</td><td>Internet/Media &amp; Entertainment</td><td>37,515</td><td>25,819</td><td>187</td><td>95</td><td>35</td><td>409</td><td>-</td><td>539</td><td>2.9</td><td>-</td><td>-</td><td>0.0%</td><td>6%</td><td>18%</td><td>Aug 20</td><td>-</td></tr><tr><td>9999 HK</td><td>NetEase</td><td>Internet/Media &amp; Entertainment</td><td>70,555</td><td>35,233</td><td>143</td><td>58</td><td>25</td><td>249</td><td>-</td><td>332</td><td>2.3</td><td>0.4%</td><td>5.7</td><td>0.0%</td><td>6%</td><td>1%</td><td>Aug 14</td><td>Jun 4</td></tr><tr><td>2513 HK</td><td>Knowledge Atlas Tech (Zhipu) (H)</td><td>Software &amp; Services</td><td>28,529</td><td>2,349</td><td>213</td><td>-</td><td>-</td><td>316</td><td>0</td><td>316</td><td>1.5</td><td>-</td><td>-</td><td>-</td><td>37%</td><td>(49%)</td><td>-</td><td>-</td></tr><tr><td>100 HK</td><td>MiniMax</td><td>Software &amp; Services</td><td>19,677</td><td>1,445</td><td>201</td><td>-</td><td>-</td><td>199</td><td>0</td><td>199</td><td>1.0</td><td>-</td><td>-</td><td>-</td><td>(1%)</td><td>(21%)</td><td>-</td><td>-</td></tr><tr><td>1211 HK</td><td>BYD (H)</td><td>Autos &amp; Components</td><td>42,569</td><td>42,549</td><td>416</td><td>(51)</td><td>(9)</td><td>248</td><td>-</td><td>188</td><td>0.5</td><td>1.4%</td><td>10.9</td><td>0.0%</td><td>(9%)</td><td>(16%)</td><td>Aug 14</td><td>Jun 11</td></tr><tr><td>9961 HK</td><td>Trip.com</td><td>Consumer Retail &amp; Services</td><td>32,981</td><td>20,568</td><td>126</td><td>29</td><td>12</td><td>134</td><td>-</td><td>175</td><td>1.4</td><td>0.2%</td><td>4.9</td><td>0.0%</td><td>(11%)</td><td>(17%)</td><td>Jun 3</td><td>-</td></tr><tr><td>9988 HK</td><td>Alibaba Group</td><td>Consumer Retail &amp; Services</td><td>308,655</td><td>294,214</td><td>1,500</td><td>72</td><td>20</td><td>80</td><td>-</td><td>172</td><td>0.1</td><td>(0.2%)</td><td>1.5</td><td>0.0%</td><td>(4%)</td><td>2%</td><td>Aug 28</td><td>Jun 10</td></tr><tr><td>1519 HK</td><td>J&amp;T Global Express</td><td>Transportation</td><td>8,605</td><td>6,204</td><td>35</td><td>163</td><td>-</td><td>-</td><td>-</td><td>163</td><td>4.7</td><td>0.2%</td><td>8.6</td><td>0.0%</td><td>(17%)</td><td>(15%)</td><td>Aug 21</td><td>-</td></tr><tr><td>3750 HK</td><td>CATL (H)</td><td>Capital Goods</td><td>18,765</td><td>15,158</td><td>359</td><td>157</td><td>-</td><td>-</td><td>-</td><td>157</td><td>0.4</td><td>-</td><td>-</td><td>(0.1%)</td><td>(1%)</td><td>44%</td><td>Jul 30</td><td>-</td></tr><tr><td>2600 HK</td><td>Aluminum of China (H)</td><td>Metals &amp; Mining</td><td>5,341</td><td>5,048</td><td>92</td><td>138</td><td>-</td><td>-</td><td>-</td><td>138</td><td>1.5</td><td>(0.2%)</td><td>4.1</td><td>0.1%</td><td>(9%)</td><td>(4%)</td><td>Aug 14</td><td>Jun 30</td></tr><tr><td>9926 HK</td><td>Akeso</td><td>Health Care</td><td>14,108</td><td>10,662</td><td>140</td><td>-</td><td>95</td><td>-</td><td>-</td><td>95</td><td>0.7</td><td>(0.0%)</td><td>6.4</td><td>0.0%</td><td>(11%)</td><td>7%</td><td>Aug 26</td><td>-</td></tr><tr><td>2602 HK</td><td>Onewo (H)</td><td>Real Estate</td><td>2,515</td><td>565</td><td>4</td><td>-</td><td>-</td><td>-</td><td>80</td><td>80</td><td>20.2</td><td>1.0%</td><td>12.3</td><td>0.0%</td><td>0%</td><td>8%</td><td>Aug 18</td><td>-</td></tr><tr><td>6186 HK</td><td>China Feihe</td><td>Consumer Staples</td><td>3,680</td><td>1,750</td><td>9</td><td>-</td><td>-</td><td>-</td><td>76</td><td>76</td><td>8.0</td><td>(1.8%)</td><td>18.5</td><td>-</td><td>(11%)</td><td>(13%)</td><td>Aug 28</td><td>Jun 9</td></tr><tr><td>1128 HK</td><td>Wynn Macau</td><td>Consumer Retail &amp; Services</td><td>3,729</td><td>1,088</td><td>4</td><td>-</td><td>-</td><td>-</td><td>71</td><td>71</td><td>18.3</td><td>0.3%</td><td>26.2</td><td>0.0%</td><td>(1%)</td><td>12%</td><td>May 28</td><td>Jun 1</td></tr><tr><td>3311 HK</td><td>China State Construction Int&#x27;l</td><td>Capital Goods</td><td>6,061</td><td>2,096</td><td>10</td><td>-</td><td>-</td><td>-</td><td>67</td><td>67</td><td>6.9</td><td>(0.5%)</td><td>17.2</td><td>(0.0%)</td><td>(0%)</td><td>62%</td><td>Aug 20</td><td>Jun 17</td></tr><tr><td>1810 HK</td><td>Xiaomi</td><td>Tech Hardware &amp; Semis</td><td>80,953</td><td>59,610</td><td>696</td><td>(93)</td><td>(17)</td><td>177</td><td>-</td><td>67</td><td>0.1</td><td>-</td><td>-</td><td>(0.0%)</td><td>(4%)</td><td>(18%)</td><td>May 26</td><td>-</td></tr><tr><td>3998 HK</td><td>Bosideng Int&#x27;l</td><td>Consumer Retail &amp; Services</td><td>6,323</td><td>2,541</td><td>14</td><td>-</td><td>-</td><td>-</td><td>66</td><td>66</td><td>4.9</td><td>1.0%</td><td>24.2</td><td>(0.0%)</td><td>(3%)</td><td>(13%)</td><td>Jun 26</td><td>-</td></tr><tr><td>293 HK</td><td>Cathay Pacific Airways</td><td>Transportation</td><td>9,616</td><td>1,661</td><td>26</td><td>-</td><td>-</td><td>-</td><td>66</td><td>66</td><td>2.5</td><td>0.4%</td><td>5.8</td><td>0.0%</td><td>7%</td><td>(25%)</td><td>Mar 11</td><td>-</td></tr><tr><td>220 HK</td><td>Uni-President China</td><td>Consumer Staples</td><td>4,234</td><td>1,208</td><td>10</td><td>-</td><td>-</td><td>-</td><td>65</td><td>65</td><td>6.6</td><td>0.0%</td><td>0.0</td><td>-</td><td>3%</td><td>57%</td><td>Aug 6</td><td>Jun 9</td></tr><tr><td>902 HK</td><td>Huaneng Power Int&#x27;l.</td><td>Utilities</td><td>3,899</td><td>3,464</td><td>33</td><td>-</td><td>-</td><td>-</td><td>65</td><td>65</td><td>1.9</td><td>1.9%</td><td>11.8</td><td>-</td><td>3%</td><td>11%</td><td>Jul 29</td><td>-</td></tr><tr><td>1368 HK</td><td>Xtep Int&#x27;l</td><td>Consumer Retail &amp; Services</td><td>1,504</td><td>812</td><td>7</td><td>-</td><td>-</td><td>-</td><td>63</td><td>63</td><td>8.6</td><td>-</td><td>-</td><td>0.0%</td><td>(3%)</td><td>70%</td><td>Aug 18</td><td>-</td></tr><tr><td>2282 HK</td><td>MGM China</td><td>Consumer Retail &amp; Services</td><td>5,025</td><td>1,184</td><td>8</td><td>-</td><td>-</td><td>-</td><td>62</td><td>62</td><td>7.8</td><td>1.3%</td><td>13.1</td><td>-</td><td>(5%)</td><td>2%</td><td>Jul 30</td><td>-</td></tr><tr><td>6818 HK</td><td>China Everbright Bank (H)</td><td>Banks</td><td>4,903</td><td>1,264</td><td>6</td><td>-</td><td>-</td><td>-</td><td>61</td><td>61</td><td>10.6</td><td>0.2%</td><td>11.8</td><td>(0.0%)</td><td>(4%)</td><td>1%</td><td>Mar 30</td><td>-</td></tr><tr><td colspan="6">Stocks with potential net passive selling following Hang Seng Indexes rebalancing</td><td colspan="4"></td><td>(ranked).</td><td>&gt;0.1</td><td colspan="7"></td></tr><tr><td>981 HK</td><td>SMIC</td><td>Tech Hardware &amp; Semis</td><td>56,950</td><td>40,796</td><td>704</td><td>(51)</td><td>(9)</td><td>(632)</td><td>-</td><td>(691)</td><td>(1.0)</td><td>0.4%</td><td>0.6</td><td>0.0%</td><td>24%</td><td

[中间内容因长度限制已省略]

me have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
