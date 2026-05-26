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
# European Rates Watch

# EGB supply, positioning & flows

# Futures positioning: Core and more core

Outstanding: Across the German curve, DU remains the most net-long contract (Exhibit 11). Positioning is net short in OE and even more so in RX, while UB sits close to neutral. Investors remain net long in Italian futures, and neutral in French.

Weekly change (Wed-Wed): Open interest increased for all German future contracts, with net positioning turning more long/less short across the curve (Exhibit 12). In contrast, positioning in Italian and French futures was led by added shorts However, as we begin to approach the rolling period, we grow increasingly hesitant in relying on futures positioning as proxy for broader market positioning/sentiment.

# French headwinds, long 10y EU vs France

Heading into the summer months, we see several headwinds for France that the market may be underappreciating. First, 45% of expected 2026 net French govt bond supply is scheduled for the Jun-Aug period. Second, with the budget season approaching, the verdict determining Le Pen's potential candidacy in July, and the eventual presidential race beginning, we remain concerned that political & fiscal risks would start to weigh on OATs early on. Current valuations do not appear to reflect this. Lastly, Moody's maintains a negative outlook; by the October review that outlook will have been in place for 12 months - within the typical 12–18 month window when outlook-driven rating actions often occur.

In the Global Rates Weekly, 22 May 2026 we recommend going long EU 3.75% Dec-35 vs FRTF 3.5% Nov-35 at 30bp, targeting 40bp with a stop at 25bp (tightest level this year, reached on Feb 25th). The risks are a larger increase in EU bond supply than currently communicated and growth/fiscal outperformance in France.

# Germany: Central Banks & banks step up purchases

In March 2026: leveraged investors net sold €3bn of German government securities (Exhibit 43), with the largest outflows seen in 30y (Exhibit 44). Bank net purchases reached past €13bn, with largest purchases seen in Bubills and 10y (Exhibit 45 & Exhibit 46). Central bank net purchases notably picked up to €32bn, with the 2-10y sector seeing the largest inflows (Exhibit 47 & Exhibit 48).

# Supply: Time for syndications?

We expect gross EGB supply at €15-18bn next week through auctions. In addition, we see potential for several syndications. First, Portugal cancelled their auction next week, indicating they may instead offer a syndication (expect 15-30y for €3bn). Spain has in the last two years offered a 10y syndication at the end of May (expect €10-15bn). Greece may also offer €2-3bn, with 5y/15y/30y tenor or dual-tenor offering. Lastly, there will be large redemptions paid on Jun 1 $^{st}$ that could be reinvested from next week.

# 25 May 2026

Rates Research

Europe

European Rates Research
MLI (UK)

Edvard Davidsson

Rates Strategist

MLI (UK)

edvard.davidsson@bofa.com

Sphia Salim

Rates Strategist

MLI (UK)

sphia.salim@bofa.com

Nathan Thomas, CFA

Rates Strategist

MLI (UK)

nathan.thomas@bofa.com

See Team Page for List of Analysts

For a complete list of our open trade recommendations, as well as our trade recommendations closed over the last 12 months,, see latest Global Rates Weekly

Abbreviations can be found in: Exhibit 50

# Supply: Next 2 weeks and 2026 estimates

# Global bond supply/redemptions next 2 weeks

Exhibit 1: Eurozone, UK and US government bond supply and C&R in the next two weeks

Higher coupon and redemption flows with relatively lower gross supply leads to a negative net supply of €33.55bn

<table><tr><td rowspan="19">Europe</td><td>Date</td><td>Settle</td><td>Country</td><td>Sector</td><td>Amount (bn)</td><td>Bond</td><td>Type</td><td>Date</td><td>Country</td><td>Sector</td><td>Amt (bn)</td><td>Bond</td><td>Type</td></tr><tr><td>25-May</td><td>27-May</td><td>BE</td><td>10y</td><td>1.3-1.7(e)</td><td>BGB 3.4% 06/36</td><td>Tap</td><td>25-May</td><td>FR</td><td>-</td><td>32.9</td><td>OAT 0.5% 05/26</td><td>R</td></tr><tr><td>25-May</td><td>27-May</td><td>BE</td><td>17y</td><td></td><td>BGB 3.45% 06/43</td><td>Tap</td><td>25-May</td><td>AS</td><td>3-23y</td><td>0.7</td><td>RAGB</td><td>C</td></tr><tr><td>26-May</td><td>28-May</td><td>IT</td><td>2y</td><td>2.25-2.5</td><td>BTPShort 2.2% 02/28</td><td>Tap</td><td>25-May</td><td>FR</td><td>0-46y</td><td>20.2</td><td>OAT</td><td>C</td></tr><tr><td>26-May</td><td>28-May</td><td>IT</td><td>5y</td><td>1.0-1.5</td><td>BTP€I 1.1% 08/31</td><td>Tap</td><td>25-May</td><td>IT</td><td>7y</td><td>0.4</td><td>BTP 2.85% 02/33</td><td>C</td></tr><tr><td>26-May</td><td>28-May</td><td>IT</td><td>20y</td><td>0.75-1.0</td><td>BTP€I 2.25% 02/46</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27-May</td><td>29-May</td><td>GE</td><td>15y</td><td>1.0</td><td>DBR 2.6% 05/41</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27-May</td><td>29-May</td><td>GE</td><td>30y</td><td>1.0</td><td>DBR 2.9% 08/56</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28-May</td><td>01-Jun</td><td>IT</td><td>TBA</td><td>7.0-9.0(e)</td><td>5y BTPS, 10y BTPS, CCTeu</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28-May</td><td>01-Jun</td><td>FI</td><td>TBA</td><td>0.4</td><td>ORI Facility</td><td>ORI</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>€14.7-18.1(e)</td><td></td><td></td><td></td><td></td><td>Total week</td><td>€54.2</td></tr><tr><td>02-Jun</td><td>04-Jun</td><td>GE</td><td>2y</td><td>5.0</td><td>BKO 2.5% 06/28</td><td>Tap</td><td>1-Jun</td><td>SP</td><td>-</td><td>23.6</td><td>SPGB 2.8 05/26</td><td>R</td></tr><tr><td>04-Jun</td><td>08-Jun</td><td>FR</td><td>&gt;8y</td><td>10.5-13.5(e)</td><td>&gt;8y OAT</td><td>Tap</td><td>1-Jun</td><td>IT</td><td>-</td><td>19.9</td><td>BTPS 1.6 06/26</td><td>R</td></tr><tr><td>04-Jun</td><td>09-Jun</td><td>SP</td><td>TBA</td><td>5.5-6.5(e)</td><td>SPGB/SPGB€I</td><td>TBA</td><td>1-Jun</td><td>SP</td><td>0-5y</td><td>3.3</td><td>SPGB</td><td>C</td></tr><tr><td>05-Jun</td><td>09-Jun</td><td>BE</td><td>TBA</td><td>0.5(e)</td><td>ORI Facility</td><td>ORI Facility</td><td>1-Jun</td><td>IT</td><td>0-10y</td><td>4.0</td><td>BTP/BTP Italia, Italy Float</td><td>C</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4-Jun</td><td>BE</td><td>-</td><td>0.2</td><td>BGBRT</td><td>R</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4-Jun</td><td>IT</td><td>6y</td><td>0.2</td><td>BTPS 1.85% 06/32</td><td>C</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5-Jun</td><td>IT</td><td>4y</td><td>0.5</td><td>BTP 3.25% 03/30</td><td>C</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Total week</td><td>€15.15-20.65 (e)</td><td></td><td></td><td></td><td></td><td>Total week</td><td>€51.7</td></tr><tr><td rowspan="7">UK</td><td>27-May</td><td>28-May</td><td>UK</td><td>7y</td><td>4.0</td><td>UKT 4.125% 03/33</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28-May</td><td>29-May</td><td>UK</td><td>4y</td><td>1.0</td><td>UKT 0.375% 10/30</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28-May</td><td>29-May</td><td>UK</td><td>13y</td><td>1.0</td><td>UKT 1.125% 01/39</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Total week</td><td>£4.0+</td><td></td><td></td><td></td><td></td><td>Total week</td><td>£0.0</td></tr><tr><td>02-Jun</td><td>03-Jun</td><td>UK</td><td>11y</td><td>TBA</td><td>Green UKT 4.625% 03/37</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>03-Jun</td><td>04-Jun</td><td>UK</td><td>9y</td><td>TBA</td><td>UKTI 1.125% 09/35</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Total week</td><td>TBA</td><td></td><td></td><td></td><td></td><td>Total week</td><td>£0.0</td></tr><tr><td rowspan="6"></td><td>26-May</td><td>01-Jun</td><td>US</td><td>2y</td><td>69.0</td><td>T</td><td>New</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27-May</td><td>29-May</td><td>US</td><td>2y</td><td>28.0</td><td>FRN</td><td>Tap</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>27-May</td><td>01-Jun</td><td>US</td><td>5y</td><td>70.0</td><td>T</td><td>New</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>28-May</td><td>01-Jun</td><td>US</td><td>7y</td><td>44.0</td><td>T</td><td>New</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Total week</td><td>$142.0</td><td></td><td></td><td></td><td></td><td>Total week</td><td>$0.0</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>Total week</td><td>$0.0</td><td></td><td></td><td></td><td></td><td>Total week</td><td>$0.0</td></tr></table>

Treasuries, BofA Global Research. (e) = estimate, C= Coupon, R= Redemption   
Source: Treasuries, BofA Global Research.

BofA GLOBAL RESEARCH

Exhibit 2: Weekly DV01 of gross issuance: past and BofA estimates for remainder of 2Q26   
DV01 of gross EGB issuance expected to drop in this second half of Q2   
![](images/ddb7efacd5fa99bc1aae8691d89ea849b89c55a33195d83e96361e29c8569f0c.jpg)

<details>
<summary>bar</summary>

| Date     | Value |
| -------- | ----- |
| 5-Jan    | 53    |
| 6-Jan    | 43    |
| 7-Jan    | 32    |
| 8-Jan    | 28    |
| 9-Feb    | 55    |
| 10-Feb   | 34    |
| 11-Feb   | 18    |
| 12-Feb   | 28    |
| 1-Mar    | 45    |
| 2-Jun    | 12    |
| 3-Jun    | 14    |
| 4-Jun    | 19    |
| 5-Jun    | 13    |
| 6-Jun    | 20    |
| 7-Jun    | 48    |
| 8-Jun    | 6     |
| 9-Jun    | 15    |
| 10-Jun   | 34    |
| 11-Jun   | 19    |
| 12-Jun   | 19    |
| 1-Mar    | 34    |
| 2-May    | 31    |
| 3-May    | 19    |
| 4-May    | 22    |
| 5-May    | 17    |
</details>

Source: Treasuries, BofA Global Research calculations   
BofA GLOBAL RESEARCH

# Gross and net supply estimates for 2026

# Exhibit 3: 2026 vs 2025 gross and net supply.

WAM of 2026 issuance is lower than WAM of issuance at this point last year.

<table><tr><td>2026</td><td>Austria</td><td>Belgium</td><td>Finland</td><td>France</td><td>Germany</td><td>Greece</td><td>Ireland</td><td>Italy</td><td>Netherlands</td><td>Portugal</td><td>Spain</td><td>Total</td></tr><tr><td>Gross EUR Bond Issuance</td><td>40</td><td>52</td><td>24</td><td>360</td><td>351</td><td>8</td><td>12</td><td>378</td><td>50</td><td>24</td><td>177</td><td>1475</td></tr><tr><td>Change versus 2025</td><td>0</td><td>6</td><td>-3</td><td>17</td><td>60</td><td>0</td><td>4</td><td>4</td><td>9</td><td>2</td><td>5</td><td>105</td></tr><tr><td>% completed</td><td>52%</td><td>62%</td><td>50%</td><td>50%</td><td>44%</td><td>54%</td><td>69%</td><td>42%</td><td>47%</td><td>46%</td><td>46%</td><td>46%</td></tr><tr><td>% completed versus 2025</td><td>-16%</td><td>0%</td><td>-2%</td><td>-5%</td><td>-1%</td><td>-43%</td><td>8%</td><td>-2%</td><td>-3%</td><td>-13%</td><td>-9%</td><td>-4%</td></tr><tr><td>WAM of 2026 supply YTD, years</td><td>12.5</td><td>13.6</td><td>11.2</td><td>10.8</td><td>9.9</td><td>10.1</td><td>12.1</td><td>8.5</td><td>10.7</td><td>9.2</td><td>10.7</td><td>10.2</td></tr><tr><td>Change vs same period in 2025, y</td><td>-0.8</td><td>3.1</td><td>-1.9</td><td>-0.5</td><td>-1.2</td><td>-3.1</td><td>-10.8</td><td>-0.1</td><td>-3.8</td><td>-3.9</td><td>1.0</td><td>-0.5</td></tr><tr><td>Buyback assumptions</td><td>0</td><td>5</td><td>0</td><td>50</td><td>0</td><td>0</td><td>0</td><td>20</td><td>0</td><td>0</td><td>0</td><td>75</td></tr><tr><td>Net of buybacks</td><td>40</td><td>47</td><td>24</td><td>310</td><td>351</td><td>8</td><td>12</td><td>358</td><td>50</td><td>24</td><td>177</td><td>1401</td></tr><tr><td>Change versus 2025</td><td>-0</td><td>4</td><td>-3</td><td>15</td><td>60</td><td>0</td><td>4</td><td>16</td><td>9</td><td>4</td><td>5</td><td>114</td></tr><tr><td>Total Redemptions</td><td>32</td><td>26</td><td>11</td><td>172</td><td>219</td><td>5</td><td>12</td><td>253</td><td>29</td><td>9</td><td>121</td><td>889</td></tr><tr><td>Net of redemptions &amp; buybacks (1)</td><td>8</td><td>21</td><td>13</td><td>138</td><td>132</td><td>3</td><td>0</td><td>105</td><td>21</td><td>15</td><td>56</td><td>511</td></tr><tr><td>Change versus 2025</td><td>-10</td><td>0</td><td>-2</td><td>11</td><td>32</td><td>-3</td><td>4</td><td>-6</td><td>0</td><td>8</td><td>5</td><td>40</td></tr><tr><td>Net Bill issuance (2)</td><td>3</td><td>2</td><td>-2</td><td>-2</td><td>27</td><td>-2</td><td>0</td><td>5</td><td>13</td><td>5</td><td>5</td><td>54</td></tr><tr><td>Change versus 2025</td><td>4</td><td>-1</td><td>-4</td><td>-8</td><td>40</td><td>-2</td><td>0</td><td>4</td><td>11</td><td>4</td><td>0</td><td>48</td></tr><tr><td>Total net bills &amp; bonds (3) = (1) + (2)</td><td>11</td><td>23</td><td>10</td><td>136</td><td>159</td><td>1</td><td>0</td><td>110</td><td>34</td><td>20</td><td>61</td><td>565</td></tr><tr><td>Change versus 2025</td><td>-6</td><td>-1</td><td>-7</td><td>3</td><td>72</td><td>-4</td><td>4</td><td>-1</td><td>11</td><td>12</td><td>5</td><td>87</td></tr></table>

Source: BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 4: Forecasted European government bond gross supply in 2026 Monthly supply throughout the year 

<table><tr><td></td><td>01</td><td>02</td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td><td>08</td><td>09</td><td>10</td><td>11</td><td>12</td><td></td></tr><tr><td>AT</td><td>9</td><td>2</td><td>5</td><td>3</td><td>2</td><td>2</td><td>2</td><td>5</td><td>2</td><td>2</td><td>2</td><td>2</td><td>40</td></tr><tr><td>BE</td><td>8</td><td>9</td><td>4</td><td>4</td><td>8</td><td>4</td><td>4</td><td>4</td><td>3</td><td>3</td><td>1</td><td>1</td><td>52</td></tr><tr><td>FI</td><td>3</td><td>2</td><td>2</td><td>5</td><td>1</td><td>2</td><td>0</td><td>5</td><td>1</td><td>2</td><td>2</td><td>0</td><td>24</td></tr><tr><td>FR</td><td>40</td><td>39</td><td>27</td><td>44</td><td>35</td><td>31</td><td>33</td><td>25</td><td>31</td><td>27</td><td>29</td><td>0</td><td>360</td></tr><tr><td>GE</td><td>42</td><td>27</td><td>35</td><td>31</td><td>31</td><td>29</td><td>34</td><td>28</td><td>33</td><td>33</td><td>23</td><td>9</td><td>351</td></tr><tr><td>GR</td><td>4</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>8</td></tr><tr><td>IR</td><td>5</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>0</td><td>12</td></tr><tr><td>IT</td><td>40</td><td>36</td><td>36</td><td>38</td><td>36</td><td>42</td><td>23</td><td>11</td><td>40</td><td>44</td><td>25</td><td>6</td><td>378</td></tr><tr><td>NL</td><td>6</td><td>2</td><td>9</td><td>4</td><td>5</td><td>4</td><td>3</td><td>0</td><td>9</td><td>3</td><td>5</td><td>0</td><td>50</td></tr><tr><td>PO</td><td>6</td><td>2</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>0</td><td>7</td><td>0</td><td>0</td><td>0</td><td>24</td></tr><tr><td>SP</td><td>31</td><td>21</td><td>12</td><td>17</td><td>29</td><td>12</td><td>15</td><td>5</td><td>13</td><td>11</td><td>11</td><td>0</td><td>177</td></tr><tr><td colspan="13">To</td><td>147</td></tr><tr><td>t.</td><td>192</td><td>139</td><td>132</td><td>152</td><td>149</td><td>127</td><td>115</td><td>84</td><td>142</td><td>128</td><td>98</td><td>17</td><td>5</td></tr></table>

Source: BofA Global Research. Note: Numbers are expressed in EUR bn   
BofA GLOBAL RESEARCH

Exhibit 5: Projected supply net of coupons, redemptions, buybacks and QE   
Monthly net supply through the year 

<table><tr><td></td><td>01</td><td>02</td><td>03</td><td>04</td><td>05</td><td>06</td><td>07</td><td>08</td><td>09</td><td>10</td><td>11</td><td>12</td><td>To.t</td></tr><tr><td>AT</td><td>9</td><td>0</td><td>-2</td><td>3</td><td>2</td><td>2</td><td>-2</td><td>5</td><td>2</td><td>-9</td><td>2</td><td>2</td><td>15</td></tr><tr><td>BE</td><td>8</td><td>9</td><td>-7</td><td>3</td><td>8</td><td>-11</td><td>3</td><td>3</td><td>3</td><td>2</td><td>0</td><td>0</td><td>21</td></tr><tr><td>FI</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>2</td><td>0</td><td>5</td><td>-1</td><td>2</td><td>2</td><td>0</td><td>17</td></tr><tr><td>FR</td><td>36</td><td>11</td><td>17</td><td>12</td><td>-4</td><td>26</td><td>26</td><td>21</td><td>7</td><td>19</td><td>-4</td><td>-4</td><td>163</td></tr><tr><td>GE</td><td>42</td><td>6</td><td>15</td><td>0</td><td>30</td><td>9</td><td>30</td><td>5</td><td>13</td><td>18</td><td>21</td><td>-11</td><td>177</td></tr><tr><td>GR</td><td>3</td><td>-1</td><td>0</td><td>2</td><td>0</td><td>-1</td><td>-1</td><td>0</td><td>2</td><td>0</td><td>0</td><td>0</td><td>4</td></tr><tr><td>IR</td><td>5</td><td>0</td><td>1</td><td>0</td><td>-6</td><td>0</td><td>0</td><td>0</td><td>2</td><td>2</td><td>0</td><td>0</td><td>4</td></tr><tr><td>IT</td><td>12</td><td>17</td><td>17</td><td>4</td><td>18</td><td>23</td><td>7</td><td>-21</td><td>12</td><td>38</td><td>10</td><td>-12</td><td>126</td></tr><tr><td>NL</td><td>-4</td><td>2</td><td>9</td><td>4</td><td>5</td><td>4</td><td>-8</td><td>0</td><td>9</td><td>3</td><td>5</td><td>0</td><td>30</td></tr><tr><td>PO</td><td>6</td><td>2</td><td>1</td><td>4</td><td>2</td><td>1</td><td>-3</td><td>0</td><td>7</td><td>-1</td><td>0</td><td>0</td><td>18</td></tr><tr><td>SP</td><td>15</td><td>21</td><td>12</td><td>0</td><td>14</td><td>12</td><td>-7</td><td>5</td><td>13</td><td>-13</td><td>11</td><td>0</td><td>83</td></tr><tr><td>Tot.</td><td>135</td><td>67</td><td>64</td><td>32</td><td>69</td><td>67</td><td>45</td><td>24</td><td>68</td><td>61</td><td>48</td><td>-25</td><td>657</td></tr></table>

Source: BofA Global Research. Note: Numbers are expressed in EUR bn   
BofA GLOBAL RESEARCH

# Syndication projections and results

# Exhibit 6: BofA expectations in terms of syndications by country

Most countries will conduct their first syndication in January, with a likely focus on the 10y sector. We also discuss what historical patterns imply for other syndications.

<table><tr><td rowspan="2">Country</td><td rowspan="2">Syndications Syndications done YTD</td><td rowspan="2">Exp. no. of syndications left</td><td colspan="3">Next syndication - BofA expectations</td><td rowspan="2">Remaining syndications</td></tr><tr><td>Timing</td><td>Tenor</td><td>Amount</td></tr><tr><td>Austria</td><td>2</td><td>1</td><td>Sep/Oct</td><td>Combined multiple tenors</td><

[中间内容因长度限制已省略]

y not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating

to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

# Research Analysts

Mark Capleton

Rates Strategist

MLI (UK)

mark.capleton@bofa.com

Edvard Davidsson

Rates Strategist

MLI (UK)

edvard.davidsson@bofa.com

Ronald Man

Rates Strategist

MLI (UK)

ronald.man@bofa.com

Ralf Preusser, CFA

Rates Strategist

MLI (UK)

ralf.preusser@bofa.com

Sphia Salim

Rates Strategist

MLI (UK)

sphia.salim@bofa.com

Agne Stengeryte, CFA

Rates Strategist

MLI (UK)

agne.stengeryte@bofa.com

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
"""
