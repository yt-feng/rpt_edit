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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Regional Banks

4Q25/1Q26: NII recovery supports growth, while fees and AQ drive divergence; downgrade BoSH and BoBJ

1Q26 results for China regional banks (CRBs) showed a continued recovery in core earnings, supported by stronger NII growth (+16% y/y for JPM-covered CRBs) and early signs of NIM stabilization. PPOP growth improved to 13% y/y in 1Q, with improvements in opex control, while bottom-line growth (+7% y/y) was capped by higher credit costs. We believe the sector is entering a more stock-specific phase, where banks with stronger core earnings recoveries and better risk control should outperform. Our top picks are BoNB and CRCB. We downgrade BoBJ to UW from Neutral and BoSH to Neutral from OW.

\- 1Q26 key trends: Broad-based NII recovery, divergent performance in fees and credit costs. CRBs delivered improvements in 1Q26 operating trends, driven mainly by stronger NII and early NIM stabilization. However, this is not yet a clean profit recovery, as fee trends remain uneven, non-fees remain volatile, and rising credit costs offset part of the PPOP improvement. CRBs' average loan growth (5% q/q in 1Q) remains stronger than SOE banks' and system levels, with corporate lending the key driver. AQ indicators remain broadly stable, but retail and SME-related risks remain the key points to watch. The CET1 buffer weakens, which could be a threat that limits asset expansion and dividend stability, as CRBs are short of external capital raising channels.

\- Top picks: BoNB and CRCB. BoNB remains our top pick among CRBs, supported by the cleanest 1Q26 beat and the most visible fee upside. We believe the combination of NII recovery, fee acceleration, improving forward-looking AQ indicators and a positive FY25 dividend surprise should continue to support BoNB's valuation premium. We also like CRCB for its improving earnings trend, the scarcity value of an ROE recovery among A-share banks, and regional advantage in the Chengdu-Chongqing economic circle. We believe CRCB's valuation of a 0.54x 2026E P/B does not fully capture the upward ROE revision following strong FY25 results (please see our CRCB note here for details).

\- Rating changes: (1) We downgrade BoBJ to UW from Neutral, as we believe rising AQ risks and limited provision buffers could keep 2026E EPS growth in single digits (JPMe $5\%$ ) despite the depressed FY25 base, while its weak CET1 position may constrain loan growth and threaten dividend sustainability, implying downside risks to both EPS and DPS. Our 2026/27 profits forecasts are $-4\% / -5\%$ below Wind consensus, as we factor in higher credit cost assumptions than the Street to reflect rising risks in its loan book. (2) We downgrade BoSH to Neutral from OW, as its core earnings recovery is weaker than peers'. Meanwhile, management's strategy of stable low-single-digit EPS growth with a $c30\%$ payout ratio positioning the bank as a defensive yield name. We believe investor appetite for non-SOE bank dividend plays is fading, while regional bank investors increasingly seek higher-beta names with re-rating stories. That said, although BoSH's 2026E dividend yield of $5.5\%$ should protect downside, we see limited upside from here, given its below-peer NII/fee momentum and subdued loan growth.

See page 40 for analyst certification and important disclosures, including non-US analyst disclosures.

# China

# Banks & Financial Services

Haomin Chen AC

(86-21) 6106 6347

haomin.chen@JPM.com

SAC Registration Number: S1730524080002

JPM Securities (China) Company Limited

# Katherine Lei

(852) 2800-8552

katherine.lei@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

Equity Ratings and Price Targets 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap ($ mn)</td><td rowspan="2">Price CCY</td><td rowspan="2">Price</td><td colspan="2">Rating</td><td colspan="4">Price Target</td></tr><tr><td>Cur</td><td>Prev</td><td>Cur</td><td>End Date</td><td>Prev</td><td>End Date</td></tr><tr><td>Bank of Beijing - A</td><td>601169 CH</td><td>16,045</td><td>CNY</td><td>5.17</td><td>UW</td><td>N</td><td>4.40</td><td>Dec-26</td><td>6.00</td><td>n/c</td></tr><tr><td>Bank of Hangzhou - A</td><td>600926 CH</td><td>14,137</td><td>CNY</td><td>16.24</td><td>N</td><td>n/c</td><td>15.60</td><td>Dec-26</td><td>n/c</td><td>n/c</td></tr><tr><td>Bank of Nanjing - A</td><td>601009 CH</td><td>16,701</td><td>CNY</td><td>11.00</td><td>OW</td><td>n/c</td><td>12.80</td><td>Dec-26</td><td>13.40</td><td>n/c</td></tr><tr><td>Bank of Ningbo - A</td><td>002142 CH</td><td>30,128</td><td>CNY</td><td>31.08</td><td>OW</td><td>n/c</td><td>38.80</td><td>Dec-26</td><td>38.20</td><td>n/c</td></tr><tr><td>Bank of Shanghai - A</td><td>601229 CH</td><td>19,310</td><td>CNY</td><td>9.26</td><td>N</td><td>OW</td><td>9.50</td><td>Dec-26</td><td>11.70</td><td>n/c</td></tr><tr><td>Changshu Rural Commercial Bank - A</td><td>601128 CH</td><td>2,893</td><td>CNY</td><td>7.19</td><td>UW</td><td>n/c</td><td>6.20</td><td>Dec-26</td><td>5.50</td><td>n/c</td></tr><tr><td>Chongqing Rural Commercial Bank - A</td><td>601077 CH</td><td>11,436</td><td>CNY</td><td>6.86</td><td>OW</td><td>n/c</td><td>8.30</td><td>Dec-26</td><td>n/c</td><td>n/c</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. n/c = no change. All prices as of 18 May 26.

# Table of contents

Valuation table 3

Key metrics in comparison....3

Top picks and avoid ....4

Rating changes 5

Downgrade BoBJ to UW from Neutral 5

Downgrade BoSH to Neutral from OW 7

4Q25-1Q26 result reviews 9

Core earnings recovery: NII improved further, fee divergence widened....9

Steady balance sheet expansion, with corporate lending the key driver ....11

Asset quality: Retail risks remained the main point to watch 13

Thin capital level becoming a bigger constraint....16

Bank of Beijing - A....18

Bank of Hangzhou - A....21

Bank of Nanjing - A....24

Bank of Ningbo - A....27

Bank of Shanghai - A....30

Changshu Rural Commercial Bank - A 34

Chongqing Rural Commercial Bank - A....37

# Valuation table

Table 1: Valuation table for China regional banks 

<table><tr><td rowspan="2">Company</td><td rowspan="2">BBG code</td><td rowspan="2">Share price (LC)</td><td rowspan="2">Rtg</td><td rowspan="2">PT (LC)</td><td rowspan="2">Mkt cap (US$ bn)</td><td colspan="2">P/E (x)</td><td colspan="2">P/B (x)</td><td colspan="2">Div. yield</td><td colspan="2">ROE</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>Ningbo-A</td><td>002142 CH</td><td>31.92</td><td>OW</td><td>38.80</td><td>31</td><td>6.7</td><td>6.0</td><td>0.86</td><td>0.77</td><td>4.2%</td><td>4.7%</td><td>13.5%</td><td>13.7%</td></tr><tr><td>CRCB-A</td><td>601077 CH</td><td>6.95</td><td>OW</td><td>8.30</td><td>11</td><td>6.1</td><td>5.6</td><td>0.54</td><td>0.50</td><td>4.9%</td><td>5.3%</td><td>9.2%</td><td>9.2%</td></tr><tr><td>Nanjing-A</td><td>601009 CH</td><td>11.26</td><td>OW</td><td>12.80</td><td>21</td><td>6.2</td><td>5.6</td><td>0.67</td><td>0.62</td><td>5.2%</td><td>5.7%</td><td>10.7%</td><td>10.8%</td></tr><tr><td>Shanghai-A</td><td>601229 CH</td><td>9.52</td><td>N</td><td>9.50</td><td>20</td><td>5.7</td><td>5.5</td><td>0.51</td><td>0.48</td><td>5.5%</td><td>5.6%</td><td>9.4%</td><td>9.0%</td></tr><tr><td>Hangzhou-A</td><td>600926 CH</td><td>16.63</td><td>N</td><td>15.60</td><td>18</td><td>5.9</td><td>5.4</td><td>0.81</td><td>0.72</td><td>4.2%</td><td>4.7%</td><td>14.3%</td><td>14.2%</td></tr><tr><td>Beijing-A</td><td>601169 CH</td><td>5.25</td><td>UW</td><td>4.40</td><td>16</td><td>6.2</td><td>5.9</td><td>0.38</td><td>0.36</td><td>4.8%</td><td>5.1%</td><td>6.3%</td><td>6.3%</td></tr><tr><td>CSRCB-A</td><td>601128 CH</td><td>7.27</td><td>UW</td><td>6.20</td><td>4</td><td>5.1</td><td>4.6</td><td>0.70</td><td>0.62</td><td>4.1%</td><td>4.6%</td><td>14.4%</td><td>14.3%</td></tr><tr><td colspan="6">City/rural banks average</td><td>6.0</td><td>5.5</td><td>0.64</td><td>0.58</td><td>4.7%</td><td>5.1%</td><td>11.1%</td><td>11.1%</td></tr></table>

Source: JPM estimates, Bloomberg Finance L.P. Note: Share prices as of 15 May 2026.

# Key metrics in comparison

Table 2: YoY trends in key operating metrics for regional banks in 4Q25 and 1Q26 

<table><tr><td rowspan="2">y/y change</td><td colspan="2">NII</td><td colspan="2">Net fees</td><td colspan="2">Revenues</td><td colspan="2">PPOP</td><td colspan="2">Net profits</td><td colspan="3">NIM</td></tr><tr><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>Q/Q</td></tr><tr><td>CRCB</td><td>11%</td><td>15%</td><td>-31%</td><td>4%</td><td>4%</td><td>8%</td><td>7%</td><td>13%</td><td>19%</td><td>5%</td><td>1.62%</td><td>1.69%</td><td>7 bps</td></tr><tr><td>CSRCB</td><td>3%</td><td>6%</td><td>216%</td><td>41%</td><td>1%</td><td>7%</td><td>4%</td><td>11%</td><td>3%</td><td>11%</td><td>2.41%</td><td>2.50%</td><td>9 bps</td></tr><tr><td>Ningbo</td><td>8%</td><td>14%</td><td>37%</td><td>82%</td><td>7%</td><td>10%</td><td>12%</td><td>15%</td><td>7%</td><td>10%</td><td>1.68%</td><td>1.73%</td><td>5 bps</td></tr><tr><td>Nanjing</td><td>38%</td><td>39%</td><td>N.M</td><td>-15%</td><td>16%</td><td>14%</td><td>21%</td><td>18%</td><td>8%</td><td>8%</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Shanghai</td><td>10%</td><td>5%</td><td>-4%</td><td>-17%</td><td>1%</td><td>4%</td><td>0%</td><td>5%</td><td>2%</td><td>1%</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Beijing</td><td>2%</td><td>10%</td><td>-16%</td><td>2%</td><td>-10%</td><td>14%</td><td>-20%</td><td>24%</td><td>-118%</td><td>6%</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Hangzhou</td><td>21%</td><td>21%</td><td>15%</td><td>-11%</td><td>0%</td><td>4%</td><td>-5%</td><td>6%</td><td>1%</td><td>10%</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Average</td><td>13%</td><td>16%</td><td>36%</td><td>12%</td><td>3%</td><td>9%</td><td>3%</td><td>13%</td><td>-11%</td><td>7%</td><td>1.90%</td><td>1.97%</td><td>7 bps</td></tr><tr><td>Average (excl. BoBJ)</td><td>16%</td><td>17%</td><td>66%</td><td>16%</td><td>5%</td><td>8%</td><td>6%</td><td>11%</td><td>4%</td><td>8%</td><td>1.90%</td><td>1.97%</td><td>7 bps</td></tr></table>

Source: 4Q25 and 1Q26 Company reports of JPM-covered regional banks. Note: Only CRCB, CSRCB and BoNB disclose quarterly NIM. Bank of Nanjing's 4Q25 fee trend is not meaningful, as it reported a Rmb0.9bn net fee loss in 4Q24.

Table 3: QoQ movement of asset quality and key B/S items in 4Q25 and 1Q26 

<table><tr><td rowspan="2"></td><td colspan="2">NPL ratio</td><td colspan="2">SML ratio</td><td colspan="2">NPL coverage</td><td colspan="2">LLR</td><td colspan="2">Loan growth</td><td colspan="2">Deposit growth</td><td colspan="2">Asset growth</td></tr><tr><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td><td>4Q25</td><td>1Q26</td></tr><tr><td>CRCB</td><td>-4 bps</td><td>-1 bps</td><td>NA</td><td>NA</td><td>2 pcts</td><td>-2 pcts</td><td>18 bps</td><td>-43 bps</td><td>2%</td><td>4%</td><td>0%</td><td>8%</td><td>1%</td><td>6%</td></tr><tr><td>CSRCB</td><td>0 bps</td><td>-1 bps</td><td>NA</td><td>NA</td><td>-12 pcts</td><td>-13 pcts</td><td>-9 bps</td><td>-14 bps</td><td>0%</td><td>5%</td><td>-1%</td><td>5%</td><td>0%</td><td>4%</td></tr><tr><td>Ningbo</td><td>0 bps</td><td>0 bps</td><td>6 bps</td><td>-8 bps</td><td>-3 pcts</td><td>-4 pcts</td><td>-4 bps</td><td>3 bps</td><td>1%</td><td>9%</td><td>-1%</td><td>11%</td><td>1%</td><td>6%</td></tr><tr><td>Nanjing</td><td>0 bps</td><td>0 bps</td><td>10 bps</td><td>-11 bps</td><td>0 pcts</td><td>-7 pcts</td><td>1 bps</td><td>-7 bps</td><td>1%</td><td>8%</td><td>2%</td><td>9%</td><td>2%</td><td>6%</td></tr><tr><td>Shanghai</td><td>0 bps</td><td>0 bps</td><td>3 bps</td><td>1 bps</td><td>-10 pcts</td><td>-4 pcts</td><td>-14 bps</td><td>-2 bps</td><td>0%</td><td>3%</td><td>-4%</td><td>5%</td><td>0%</td><td>2%</td></tr><tr><td>Beijing</td><td>0 bps</td><td>3 bps</td><td>NA</td><td>NA</td><td>4 pcts</td><td>-2 pcts</td><td>6 bps</td><td>3 bps</td><td>1%</td><td>1%</td><td>2%</td><td>4%</td><td>1%</td><td>0%</td></tr><tr><td>Hangzhou</td><td>0 bps</td><td>0 bps</td><td>-1 bps</td><td>-5 bps</td><td>-11 pcts</td><td>-21 pcts</td><td>-8 bps</td><td>-16 bps</td><td>5%</td><td>8%</td><td>7%</td><td>5%</td><td>3%</td><td>3%</td></tr><tr><td>Average</td><td>-1 bps</td><td>0 bps</td><td>4 bps</td><td>-6 bps</td><td>-4 bps</td><td>-7 bps</td><td>-2 bps</td><td>-11 bps</td><td>1%</td><td>5%</td><td>1%</td><td>7%</td><td>1%</td><td>4%</td></tr></table>

Source: 4Q25 and 1Q26 Company reports of JPM-covered regional banks.

# Top picks and avoid

Performance diverged among regional banks, and we prefer names with clearer core earnings recoveries and lower EPS downside risks. CRBs' earnings recovery in 1Q26 was driven mainly by stronger NII growth and early signs of NIM stabilization, supported by decent “good start” loan demand/pricing and deposit cost savings. Fee growth was divergent, with BoNB taking the lead. However, bottom-line profit growth was capped by higher credit costs, while capital buffers and dividend visibility became more important differentiators. Our top picks are BoNB and CRCB, while we avoid BoBJ.

# Top picks

- BoNB remains our top pick among regional banks, supported by the cleanest 1Q26 beat and the most visible fee upside. BoNB delivered a strong combination of core earnings recovery, fee acceleration, improving forward-looking AQ indicators and a positive dividend surprise. NII grew 14% y/y in 1Q26, supported by quality loan expansion and loan mix optimization, while fee income surged 82% y/y, significantly outperforming peers and highlighting its differentiated wealth management franchise. The bank also raised its cash dividend payout ratio to 28% in FY25 from 23% in FY24, a positive surprise to the market. Although CET1 remains a key investor concern, with the 1Q26 CET1 ratio at 9.25%, we believe BoNB's stronger earnings quality, wealth management upside and improving AQ trend should continue to support its premium valuation.   
- CRCB is our preferred recovery name, as its ROE recovery remains scarce among A-share banks and is not fully reflected in valuation, in our view. CRCB's 1Q26 results showed a continued earnings recovery, with revenue and pretax profit up $8\%$ and $12\%$ y/y, respectively. We like CRCB for its improving earnings trend, relatively high capital buffer, the scarcity value of ROE recovery among A-share banks, and leverage to the growth of the Chengdu-Chongqing economic circle. The key pushback remains retail AQ, but we believe the valuation does not fully reflect the durability and quality of earnings recovery if credit costs remain manageable (please see our upgrade note here for details).

# Top avoid

\- We avoid BoBJ, as rising AQ risks, limited earnings buffers and weak CET1 position imply downside risks to both EPS and DPS. BoBJ reported a 4Q25 loss due mainly to one-off impairment charges on financial investment assets, but we do not expect earnings to rebound meaningfully despite the depressed FY25 base, as loan provisioning pressure may rise alongside worsening AQ trends. The NPL ratio rose 3bps q/q in 1Q26, credit cost increased 64bps y/y, to 0.98%, and the SML/overdue loan ratios deteriorated by 11bps/43bps h/h in 2H25. BoBJ also has the lowest NPL coverage ratio among our covered regional banks, at 198% in 1Q26, limiting its ability to smooth earnings through provision release. Meanwhile, its CET1 ratio was only 8.59%, just 84bps above the regulatory minimum, which may constrain loan growth and dividend sustainability. We believe this makes BoBJ less able to participate in a potential macro recovery and leaves both EPS and DPS vulnerable to downside risks.

# Rating changes

# Downgrade BoBJ to UW from Neutral

We downgrade Bank of Beijing (BoBJ) to Underweight from Neutral with a Dec-26 PT of Rmb4.40 (16% potential downside) for the following reasons:

\- Weak earnings visibility with rising AQ risks, despite the low FY25 base. BoBJ reported a loss in 4Q25, dragged mainly by one-off impairment charges on financial investment assets, leading to a 24% y/y contraction in FY25 profits. The one-off nature suggests the sharp 4Q25 provision spike is unlikely to repeat, but such an event shows a lapse in risk management, and we do not expect a meaningful rebound in FY26 profit growth. The underlying asset quality trend continues to weaken, as indicated by the deterioration in asset quality leading indicators, such as the 12bps/43bps h/h rise in the SML ratio/overdue loan ratio at end-2025 (Figure 3), the ongoing rise in the NPL ratio (+3bps q/q) and the sharp surge in credit cost (+35bps y/y) in 1Q26 (Figure 4), dragged on mainly by consumption, mortgage and property-related loans. We expect rising loan provisioning pressure and structurally higher normalized credit costs going forward. Therefore, despite the depressed FY25 base, we expect net profit growth to be moderate in 2026, at \~5% y/y. We expect BoBJ's credit cost to rise to 99bps (+23bps y/y) in 2026, but this remains below the 116bps average during the last AQ upcycle in 2015-20, suggesting downside risks to EPS if credit costs normalize closer to historical stress-cycle levels (Figure 5). Our sensitivity analysis shows that the drag on net profit for every further 5bps increase in credit cost would be \~4.4% in 2026E (Table 4).

\- Weaker earnings buffers than at peers. BoBJ's NPL coverage ratio was $198\%$ in 1Q26, the lowest among our covered regional banks (Figure 6), indicating weaker ability to cushion earnings growth with provision release. BoBJ's OCI reserve buffer is also limited. Its OCI reserve as a $\%$ of revenue was $2\%$ in 2025 vs. peers' average of $5\%$ (Figure 7).

\- Capital constraint may limit loan expansion and weaken leverage to a macro recovery. BoBJ's CET1 ratio was only 8.59% in 1Q26, with only an 84bps buffer above the regulatory minimum requirement, the lowest among peers (Figure 2). Per the company, the bank plans to follow a “capital-constrained asset growth” approa

[中间内容因长度限制已省略]

ore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
