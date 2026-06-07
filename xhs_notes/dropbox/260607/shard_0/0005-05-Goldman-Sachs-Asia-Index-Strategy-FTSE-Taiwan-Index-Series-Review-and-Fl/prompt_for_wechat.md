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

# FTSE Taiwan Index Series Review and Flow Implications (June 2026)

What Happened? FTSE Russell announced the results of its quarterly index review for the FTSE TWSE Taiwan Index Series after the market closed on June 5 (Friday). All changes will take effect after market close on June 18 (Thursday).

Constituent Changes: For the FTSE TWSE Taiwan 50, Zhen Ding (4958), BizLink (3665), Global Unichip (3443), and Nan Ya PCB (8046) will replace China Steel (2002), Formosa Plastics (1301), Hotai Motor (2207), and Caliway Biopharm (6919). For the FTSE Taiwan Dividend+, Winbond Electronics (2344), Nan Ya Plastics (1303), Nanya Technology (2408), Far Eastone (4904), and Chung-Hsin Electric (1513) will replace Makalot Industrial (1477), Tong Yang Industry (1319), Tung Ho Steel (2006), and Radiant Opto-Electronics (6176), with reweighting also causing notable flow impacts among existing constituents. Weight adjustments will be around $1.4\%$ for Taiwan 50 and $23.6\%$ for Taiwan Dividend+. (Exhibit 5)

Index Implications: Following the rebalancing, FTSE TWSE Taiwan 50 index's forward 12-month P/E and EPS growth (2026-27 CAGR) are expected to shift from 16.9x to 21.7x and $36.3\%$ to $36.2\%$ , while trailing dividend yield will remain unchanged $(1.4\%)$ . For Taiwan Dividend+ index, the corresponding metrics would change from 16.2x to 13.4x (fP/E), $3.4\%$ to $3.5\%$ (D/Y), and $17.6\%$ to $29.7\%$ (EPS growth). (Exhibit 1)

Sector Implications: Banks (+US\$1.0bn), Chemiclas (+US\$760mn), Telcos (+US\$590mn), and Capital Goods (+US\$460mn) are poised to see the largest passive inflows, while Tech Hardware & Semis (-US\$2.4bn) may face the biggest funding outflows. These changes reflect rebalancing for existing and pending constituents in FTSE Taiwan 50/Dividend+, combined with potential flows from FTSE GEIS. Overall, we estimate that the FTSE rebalancing could generate US\$13-14bn in gross two-way passive flows for Taiwan. (Exhibit 2)

Historical vs. Current Patterns: FTSE Taiwan 50 additions have underperformed deletions ahead of the announcement, while Dividend+ additions have significantly outperformed; historical patterns suggest post-announcement outperformance for both, followed by a potential reversal after the changes become effective. (Exhibit 3)

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

Exhibit 1: FTSE Russell announced the quarterly review results for the Taiwan Index Series, with 4/5 stock changes in the Taiwan 50/Dividend+, effective after market close on June 18

<table><tr><td rowspan="2"></td><td rowspan="2">FTSE Taiwan Index Series</td><td colspan="2">Jun 2026 Review Summary</td></tr><tr><td>Taiwan 50</td><td>Dividend+</td></tr><tr><td rowspan="3">Stock Changes</td><td>Current # Constituents</td><td>50</td><td>49</td></tr><tr><td># Stocks Added / Deleted</td><td>4 / 4</td><td>5 / 4</td></tr><tr><td>% Weight Rebalanced</td><td>1.4%</td><td>23.6%</td></tr><tr><td rowspan="4">Liquidity</td><td>Proforma Index Cap (US$bn)</td><td>3,156</td><td>889</td></tr><tr><td>Proforma % Change</td><td>+0.7%</td><td>+21.5%</td></tr><tr><td>Proforma 3M ADVT (US$bn)</td><td>15.9</td><td>8.3</td></tr><tr><td>Proforma % Change</td><td>+9.5%</td><td>+35.2%</td></tr><tr><td rowspan="6">Valuations / Growth</td><td>NTM P/E (x)</td><td>16.9x /</td><td>16.2x /</td></tr><tr><td>(Current / Proforma)</td><td>21.7x</td><td>13.4x</td></tr><tr><td>LTM Dividend Yield (%)</td><td>1.4% /</td><td>3.4% /</td></tr><tr><td>(Current / Proforma)</td><td>1.4%</td><td>3.5%</td></tr><tr><td>2026-27 EPS Growth (%)</td><td>36.3% /</td><td>17.6% /</td></tr><tr><td>(Current / Proforma)</td><td>36.2%</td><td>29.7%</td></tr><tr><td>Passive Flows (+FTSE GEIS)</td><td>Potential Gross Passive Buying + Selling (Two-way) (US$mn)</td><td>2,637</td><td>10,862</td></tr><tr><td rowspan="4">Trading Pattern Prior to Announce.</td><td>Return Since 20D Prior to Ann.</td><td>-8.2% /</td><td>+17.9% /</td></tr><tr><td>(Additions / Deletions)</td><td>+1.2%</td><td>+1.4%</td></tr><tr><td rowspan="2">Share Turnover % Chg (Median 20D vs. Prior 3M) (Add / Del)</td><td>+5% /</td><td>+52% /</td></tr><tr><td>-15%</td><td>+40%</td></tr></table>

Note: Potential passive flows consider both FTSE Taiwan and Global Index rebalancing impact. Pricing is as of Jun 5, 2026  
Source: FTSE Russell, FactSet, Refinitiv, GS Global Investment Research

## Exhibit 2: Banks, Chemicals, Telcos, and Capital Goods are poised to see the largest passive inflows, while Tech Hardware & Semis may face the biggest funding outflows

Current vs. Proforma Sector Weights and Changes in FTSE TWSE Taiwan 50 / Dividend+, and Aggregate Potential Passive Flows

<table><tr><td rowspan="2" colspan="2">GICS Sector/Industry</td><td colspan="3">Taiwan 50</td><td colspan="3">Taiwan Dividend+</td><td colspan="3">Passive Flows (US$mn)</td></tr><tr><td>Current %</td><td>Proforma %</td><td>Chg (bps)</td><td>Current %</td><td>Proforma %</td><td>Chg (bps)</td><td>Gross Buying</td><td>Gross Selling</td><td>Net Flows</td></tr><tr><td rowspan="3">Financials</td><td>Banks</td><td>4.2%</td><td>4.2%</td><td>-1</td><td>16.8%</td><td>21.1%</td><td>+428</td><td>1,157</td><td>-168</td><td>989</td></tr><tr><td>Insurance &amp; Other Financials</td><td>3.1%</td><td>3.1%</td><td>+0</td><td>6.0%</td><td>5.8%</td><td>-17</td><td>164</td><td>-185</td><td>-21</td></tr><tr><td>Real Estate</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="7">Domestic / Global Cyclicals</td><td>Capital Goods</td><td>0.0%</td><td>0.4%</td><td>+39</td><td>0.3%</td><td>0.9%</td><td>+57</td><td>454</td><td>-1</td><td>453</td></tr><tr><td>Transportation</td><td>0.3%</td><td>0.3%</td><td>-0</td><td>4.5%</td><td>4.7%</td><td>+28</td><td>65</td><td>-2</td><td>62</td></tr><tr><td>Autos &amp; Components</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>1.1%</td><td>0.7%</td><td>-33</td><td>6</td><td>-87</td><td>-81</td></tr><tr><td>Consumer Retail &amp; Services</td><td>0.1%</td><td>0.0%</td><td>-14</td><td>0.8%</td><td>0.5%</td><td>-27</td><td>20</td><td>-193</td><td>-173</td></tr><tr><td>Tech Hardware &amp; Semis</td><td>90.0%</td><td>90.2%</td><td>+29</td><td>63.5%</td><td>53.1%</td><td>-1042</td><td>3,153</td><td>-5,518</td><td>-2,365</td></tr><tr><td>Software &amp; Services</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Internet/Media &amp; Entertainment</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>0</td><td>0</td></tr><tr><td rowspan="4">Commodities</td><td>Energy</td><td>0.1%</td><td>0.1%</td><td>-0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>-5</td><td>-5</td></tr><tr><td>Metals &amp; Mining</td><td>0.2%</td><td>0.0%</td><td>-22</td><td>0.9%</td><td>0.7%</td><td>-25</td><td>11</td><td>-254</td><td>-243</td></tr><tr><td>Chemicals &amp; Other Materials</td><td>0.7%</td><td>0.5%</td><td>-21</td><td>0.7%</td><td>4.8%</td><td>+401</td><td>931</td><td>-177</td><td>754</td></tr><tr><td>Consumer Staples</td><td>0.4%</td><td>0.4%</td><td>-0</td><td>2.0%</td><td>2.8%</td><td>+78</td><td>181</td><td>-1</td><td>180</td></tr><tr><td rowspan="3">Defensives</td><td>Health Care</td><td>0.1%</td><td>0.0%</td><td>-10</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>2</td><td>-79</td><td>-77</td></tr><tr><td>Utilities</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0.0%</td><td>0.0%</td><td>+0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Telecommunication Services</td><td>0.9%</td><td>0.9%</td><td>-1</td><td>2.3%</td><td>4.8%</td><td>+255</td><td>592</td><td>-7</td><td>586</td></tr></table>

Note: Potential passive flows consider both FTSE Taiwan and Global Index rebalancing impact. Pricing is as of Jun 5, 2026

Source: FactSet, Refinitiv, EPFR, GS Global Investment Research

Exhibit 3: FTSE Taiwan 50: Additions have underperformed deletions in the two weeks ahead of the announcement; historical trends suggest post-announcement outperformance, followed by a potential reversal after the effective date  
![](images/4df7c3ba9989bcd007605ca32767e7c099b6193bade1c060f5422d980d185192.jpg)

<details>
<summary>line chart</summary>

| # workdays before/after index review announcement date | Past Add/Del Median | Current (5-Jun-26) |
| ---------------------------------------------------- | ------------------- | ------------------ |
| -20                                                  | 90                  | 120                |
| -15                                                  | 95                  | 100                |
| -10                                                  | 100                 | 110                |
| -5                                                   | 100                 | 105                |
| 0                                                    | 100                 | 100                |
| 5                                                    | 100                 | 100                |
| 10                                                   | 100                 | 100                |
| 15                                                   | 95                  | 100                |
| 20                                                   | 95                  | 100                |
</details>

Source: FactSet, GS Global Investment Research

Exhibit 4: FTSE Taiwan Dividend+: Additions have significantly outperformed deletions; historical trends suggest moderate post-announcement outperformance to continue before the effective date  
![](images/37a18900cf578f77e597c45d82875409a7636d307baadcc156d5695c9d64159d.jpg)

<details>
<summary>line chart</summary>

| # workdays before/after index review announcement date | Past 20-80%ile Range | Past Add/Del Median | Current (5-Jun-26) |
| ----------------------------------------------------- | --------------------- | ------------------- | ------------------ |
| -20                                                   | ~100                  | ~97                 | ~85                |
| -15                                                   | ~102                  | ~98                 | ~92                |
| -10                                                   | ~104                  | ~99                 | ~88                |
| -5                                                    | ~103                  | ~100                | ~100               |
| 0                                                     | ~102                  | ~100                | ~108               |
| 5                                                     | ~103                  | ~100                | —                  |
| 10                                                    | ~104                  | ~101                | —                  |
| 15                                                    | ~105                  | ~101                | —                  |
| 20                                                    | ~106                  | ~102                | —                  |
</details>

Exhibit 5: FTSE TWSE Taiwan: Stocks that may experience the most significant net passive buying or selling flows following the FTSE TWSE Taiwan and Global Equity Index Series (GEIS) rebalancing

<table><tr><td rowspan="2">BBG Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">Sector</td><td rowspan="2">Listed Mkt Cap (US$mn)</td><td rowspan="2">Free Float Cap (US$mn)</td><td rowspan="2">3M ADVT (US$mn)</td><td colspan="3">Potential Passive Flows (US$mn)</td><td rowspan="2">Net Passive Flows (US$mn)</td><td rowspan="2">Net Flows / 3M ADVT (days)</td><td rowspan="2">S3&#x27;s Short Interest 20D Chg (pp)</td><td rowspan="2">Days to Cover (1M ADVT)</td><td rowspan="2">S3&#x27;s HF Long Interest 20D Chg (pp)</td><td rowspan="2">Return since 20D prior to ann.</td><td rowspan="2">Return since 10D prior to ann.</td><td rowspan="2">Share Turnover % Chg (Median 20D vs. Prior 3M)</td><td colspan="2">Corporate Event Dates</td></tr><tr><td>Taiwan 50</td><td>Taiwan Dividend +</td><td>All Cap / World</td><td>Expected Next Report</td><td>Ex-Dividend</td></tr><tr><td colspan="6">FTSE Taiwan 50/Dividend+ Stocks with net passive buying following FTSE Taiwan and GEIS rebalancing</td><td colspan="3"></td><td>(ranked)</td><td>&gt;0.2</td><td colspan="8"></td></tr><tr><td>2344 TT</td><td>Winbond Electronics</td><td>Tech Hardware &amp; Semis</td><td>25,672</td><td>17,489</td><td>803</td><td>(6)</td><td>953</td><td>(6)</td><td>941</td><td>1.2</td><td>(0.2%)</td><td>0.8</td><td>0.0%</td><td>51%</td><td>30%</td><td>52%</td><td>Aug 5</td><td></td></tr><tr><td>1303 TT</td><td>Nan Ya Plastics</td><td>Chemicals &amp; Other Materials</td><td>27,979</td><td>17,495</td><td>241</td><td>(3)</td><td>912</td><td>(1)</td><td>908</td><td>3.8</td><td>-</td><td>-</td><td>-</td><td>18%</td><td>21%</td><td>(32%)</td><td>Jul 10</td><td>Jul 8</td></tr><tr><td>2408 TT</td><td>Nanya Technology</td><td>Tech Hardware &amp; Semis</td><td>43,314</td><td>16,334</td><td>1,114</td><td>3</td><td>833</td><td>6</td><td>842</td><td>0.8</td><td>(0.9%)</td><td>0.3</td><td>0.0%</td><td>31%</td><td>16%</td><td>52%</td><td>Jul 10</td><td>Jul 7</td></tr><tr><td>4904 TT</td><td>Far Eastone Telecom</td><td>Telecommunication Services</td><td>11,695</td><td>6,514</td><td>20</td><td>(1)</td><td>571</td><td>(0)</td><td>569</td><td>28.1</td><td>(0.0%)</td><td>0.5</td><td>0.0%</td><td>6%</td><td>6%</td><td>30%</td><td>Jul 10</td><td>Jul 8</td></tr><tr><td>4958 TT</td><td>Zhen Ding Technology</td><td>Tech Hardware &amp; Semis</td><td>16,896</td><td>11,600</td><td>481</td><td>314</td><td>-</td><td>15</td><td>329</td><td>0.7</td><td>(1.9%)</td><td>0.6</td><td>0.0%</td><td>26%</td><td>(2%)</td><td>24%</td><td>Aug 12</td><td>Jun 8</td></tr><tr><td>3665 TT</td><td>BizLink</td><td>Capital Goods</td><td>13,361</td><td>11,366</td><td>234</td><td>321</td><td>-</td><td>0</td><td>322</td><td>1.4</td><td>(0.3%)</td><td>1.4</td><td>(0.0%)</td><td>(20%)</td><td>(1%)</td><td>(27%)</td><td>Aug 20</td><td>Jul 15</td></tr><tr><td>2887 TT</td><td>TS Financial</td><td>Banks</td><td>22,563</td><td>20,510</td><td>75</td><td>1</td><td>311</td><td>4</td><td>316</td><td>4.2</td><td>0.2%</td><td>2.4</td><td>0.1%</td><td>20%</td><td>20%</td><td>101%</td><td>Aug 31</td><td></td></tr><tr><td>2884 TT</td><td>E.SUN Financial</td><td>Banks</td><td>17,195</td><td>15,207</td><td>41</td><td>(7)</td><td>304</td><td>(5)</td><td>292</td><td>7.2</td><td>0.1%</td><td>6.2</td><td>0.0%</td><td>3%</td><td>7%</td><td>34%</td><td>Aug 11</td><td></td></tr><tr><td>3443 TT</td><td>Global Unichip</td><td>Tech Hardware &amp; Semis</td><td>18,741</td><td>11,075</td><td>310</td><td>290</td><td>-</td><td>(11)</td><td>278</td><td>0.9</td><td>(0.2%)</td><td>0.3</td><td>0.0%</td><td>(15%)</td><td>(14%)</td><td>16%</td><td>Jul 31</td><td>Jun 8</td></tr><tr><td>2886 TT</td><td>Mega Financial</td><td>Banks</td><td>19,848</td><td>15,237</td><td>37</td><td>(3)</td><td>188</td><td>(0)</td><td>185</td><td>5.1</td><td>0.1%</td><td>1.6</td><td>0.0%</td><td>4%</td><td>5%</td><td>36%</td><td>Aug 31</td><td></td></tr><tr><td>1216 TT</td><td>Uni-President Enterprises</td><td>Consumer Staples</td><td>13,291</td><td>10,995</td><td>31</td><td>(1)</td><td>181</td><td>1</td><td>180</td><td>5.7</td><td>0.2%</td><td>12.7</td><td>0.0%</td><td>1%</td><td>3%</td><td>57%</td><td>Aug 7</td><td>Jul 30</td></tr><tr><td>3231 TT</td><td>Wistron</td><td>Tech Hardware &amp; Semis</td><td>17,790</td><td>16,426</td><td>247</td><td>(9)</td><td>190</td><td>(8)</td><td>173</td><td>0.7</td><td>0.4%</td><td>1.8</td><td>0.0%</td><td>17%</td><td>18%</td><td>72%</td><td>Aug 12</td><td>Jul 8</td></tr><tr><td>2890 TT</td><td>SinoPac Financial</td><td>Banks</td><td>15,269</td><td>13,256</td><td>31</td><td>2</td><td>150</td><td>4</td><td>157</td><td>5.0</td><td>(0.0%)</td><td>0.3</td><td>-</td><td>5%</td><td>12%</td><td>65%</td><td>Aug 24</td><td></td></tr><tr><td>8046 TT</td><td>Nan Ya PCB</td><td>Tech Hardware &amp; Semis</td><td>18,031</td><td>5,987</td><td>483</td><td>148</td><td>-</td><td>1</td><td>149</td><td>0.3</td><td>0.0%</td><td>0.3</td><td>0.0%</td><td>(1%)</td><td>(10%)</td><td>(5%)</td><td>Aug 6</td><td>Jun 25</td></tr><tr><td>2880 TT</td><td>Hua Nan Financial</td><td>Banks</td><td>16,675</td><td>11,489</td><td>32</td><td>(5)</td><td>157</td><td>(4)</td><td>148</td><td>4.6</td><td>0.7%</td><td>2.4</td><td>0.0%</td><td>5%</td><td>9%</td><td>106%</td><td>Aug 28</td><td></td></tr><tr><td>1513 TT</td><td>Chung-Hsin Electric &amp; Machinery</td><td>Capital Goods</td><td>2,990</td><td>2,417</td><td>46</td><td>-</td><td>131</td><td>(1)</td><td>130</td><td>2.8</td><td>3.5%</td><td>3.3</td><td>0.0%</td><td>8%</td><td>9%</td><td>81%</td><td>Aug 12</td><td>Jul 9</td></tr><tr><td>2883 TT</td><td>KGI Financial Holding</td><td>Insurance &amp; Other Financials</td><td>14,782</td><td>13,823</td><td>46</td><td>(3)</td><td>133</td><td>(1)</td><td>129</td><td>2.8</td><td>0.1%</td><td>0.7</td><td>0.0%</td><td>21%</td><td>27%</td><td>50%</td><td>Aug 19</td><td></td></tr><tr><td>2382 TT</td><td>Quanta Computer</td><td>Tech Hardware &amp; Semis</td><td>49,596</td><td>34,197</td><td>323</td><td>(5)</td><td>97</td><td>(0)</td><td>92</td><td>0.3</td><td>3.3%</td><td>4.9</td><td>0.1%</td><td>15%</td><td>24%</td><td>141%</td><td>Aug 10</td><td></td></tr><tr><td>2603 TT</td><td>Evergreen Marine (Taiwan)</td><td>Transportation</td><td>16,239</td><td>11,190</td><td>109</td><td>(2)</td><td>54</td><td>(0)</td><td>52</td><td>0.5</td><td>1.0%</td><td>7.2</td><td>-</td><td>10%</td><td>6%</td><td>171%</td><td>Aug 13</td><td>Jun 17</td></tr><tr><td>4938 TT</td><td>Pegatron</td><td>Tech Hardware &amp; Semis</td><td>8,268</td><td>5,977</td><td>44</td><td>-</td><td>23</td><td>5</td><td>29</td><td>0.7</td><td>-</td><td>-</td><td>0.0%</td><td>15%</td><td>20%</td><td>28%</td><td>Aug 13</td><td>Jun 15</td></tr><tr><td colspan="6">FTSE Taiwan 50/Dividend+ Stocks with net passive selling following FTSE Taiwan and GEIS rebalancing</td><td colspan="3"></td><td colspan="2"></td><td colspan="8"></td></tr><tr><td>2454 TT</td><td>MediaTek</td><td>Tech Hardware &amp; Semis</td><td>225,822</td><td>203,496</td><td>1,107</td><td>(29)</td><td>(1,859)</td><td>(2)</td><td>(1,889)</td><td>(1.7)</td><td>(0.1%)</td><td>0.2</td><td>0.0%</td><td>18%</td><td>11%</td><td>(9%)</td><td>J

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
