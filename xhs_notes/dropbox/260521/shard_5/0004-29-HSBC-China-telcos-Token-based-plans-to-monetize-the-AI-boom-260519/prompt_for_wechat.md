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
# China telcos

# Token-based plans to monetize the AI boom

Equities

Diversified

Telecommunications

China

- China Telecom announced a nationwide token package offering on 17 May, spurring investor enthusiasm   
- All three telcos introduced token-based subscription plans, but we expect little earnings impact in the near term   
◆ Retain Buy ratings for China Mobile (H/A), Hold for China Telecom (H/A), and Reduce for China Unicom (H/A)

Token-based plans gain traction: China telcos are packaging AI token usage into subscription plans, turning tokens into the industry's newest data unit and billing metric (i.e. token as the new GB). For example, China Mobile (CM)'s Jiangsu branch offered monthly token plans (unit price: Rmb2/million token) on 17 April accessing various LLMs such as DeepSeek. On 29 April, China Unicom (CU)'s Hubei branch introduced token plans (unit price: Rmb1.3/million token) and coding plans (pricing by requests) accessing MiniMax model. On 17 May, China Telecom (CT) launched a tiered token plan covering both individuals (cRmb10/30/50 per month for 10m/40m/80m token) and SMEs (cRmb40/160/300 per month for 15m/70m/150m token). These plans underpin China telcos' strategies to become utility-like AI infrastructure providers and monetize the skyrocketing AI-driven token consumption in China (from 100billion/day in early 2024 to over 140trn/day in March 2026).

But price competitiveness remains questionable: We think CT's H/A share price rose c6%/8% on 18 May because of the AI token plan launch and "Token Factory" procurement announcement. CT's Ningxia branch recently opened China's first telco-led "Token Factory" procurement. However, we think the price competitiveness of telcos' token plans are questionable. The price per token does not seem lower than Internet CSPs' C-end monthly subscriptions (see table 2). Moreover, we think model variety, computing power reliability, ecosystem of cloud offerings, and responsiveness of support team matter for individual and SME users. China's Internet CSPs such as Bytedance are early movers in token-based subscription offerings with more powerful proprietary LLMs than telcos. Therefore, we do not expect telcos to gain significant market share in the near to medium term.

Retain Buys for CM (H/A), Holds for CT (H/A), and Reduces for CU (H/A): We believe telcos' trials in the token-based model would enrich their cloud product offerings. But we see limited visibility on an earnings impact, and hence we keep our estimates and ratings unchanged. CM continues to be our preferred pick given a higher FY26e dividend yield (6.3%) and a more robust balance sheet.

1. China telcos: Summary of rating and target price changes, and valuation 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Currency</td><td rowspan="2">Price</td><td colspan="2">Target Price</td><td rowspan="2">Rating New</td><td rowspan="2">Upside/Downside</td><td rowspan="2">3m ADV (USD m)</td><td rowspan="2">EV/EBITDAx 2026e</td><td rowspan="2">PEx 2026e</td><td rowspan="2">Div Yield 2026e</td></tr><tr><td>Old</td><td>New Old</td></tr><tr><td>China Mobile</td><td>941 HK</td><td>HKD</td><td>86.40</td><td>94.00</td><td>94.00 Buy</td><td>Buy</td><td>+8.8%</td><td>209.8</td><td>3.8x</td><td>12.2x</td><td>6.3%</td></tr><tr><td>China Mobile A</td><td>600941 CH</td><td>RMB</td><td>100.35</td><td>111.00</td><td>111.00 Buy</td><td>Buy</td><td>+10.6%</td><td>134.8</td><td>5.4x</td><td>16.0x</td><td>4.7%</td></tr><tr><td>China Telecom</td><td>728 HK</td><td>HKD</td><td>5.64</td><td>5.60</td><td>5.60 Hold</td><td>Hold</td><td>-0.7%</td><td>39.1</td><td>2.5x</td><td>15.3x</td><td>5.0%</td></tr><tr><td>China Telecom A</td><td>601728 CH</td><td>RMB</td><td>6.82</td><td>6.30</td><td>6.30 Hold</td><td>Hold</td><td>-7.6%</td><td>126.3</td><td>3.8x</td><td>20.1x</td><td>3.6%</td></tr><tr><td>China Unicom</td><td>762 HK</td><td>HKD</td><td>7.94</td><td>6.50</td><td>6.50 Reduce</td><td>Reduce</td><td>-18.1%</td><td>26.3</td><td>1.2x</td><td>11.6x</td><td>5.4%</td></tr><tr><td>China Unicom A</td><td>600050 CH</td><td>RMB</td><td>4.92</td><td>4.10</td><td>4.10 Reduce</td><td>Reduce</td><td>-16.7%</td><td>136.5</td><td>2.8x</td><td>17.9x</td><td>3.3%</td></tr></table>

Source: Bloomberg, HSBC estimates. Note: Priced as at close of 18 May 2026.

# Piyush Choudhary\*, CFA

Head of Asia Telecoms

The Hongkong and Shanghai Banking Corporation

Limited, Singapore Branch

piyush.choudhary@hsbc.com.sg

+65 6658 0607

# Charlie Bai\*

Analyst, Asia Telecoms

The Hongkong and Shanghai Banking Corporation Limited

charlie.bai@hsbc.com.hk

+852 22887184

# Ritchie Sun\*, CFA

Analyst, Internet Research

The Hongkong and Shanghai Banking Corporation Limited

ritchie.k.h.sun@hsbc.com.hk

+852 2822 4392

\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/qualified pursuant to FINRA regulations

# Disclosures & Disclaimer

This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

Issuer of report: The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch

View HSBC Global Investment Research at:

https://www.research.hsbc.com

2. Comparing token-based subscription plans of telcos and China-based internet companies 

<table><tr><td>Player</td><td>Plan type</td><td>Price (CNY/month)</td><td>Tokens included (m)</td><td>CNY/m token</td></tr><tr><td>China Telecom</td><td>Individual</td><td>10</td><td>10</td><td>1.0</td></tr><tr><td>China Telecom</td><td>Individual</td><td>30</td><td>40</td><td>0.8</td></tr><tr><td>China Telecom</td><td>Individual</td><td>50</td><td>80</td><td>0.6</td></tr><tr><td>China Telecom</td><td>SME</td><td>40</td><td>15</td><td>2.7</td></tr><tr><td>China Telecom</td><td>SME</td><td>160</td><td>70</td><td>2.3</td></tr><tr><td>China Telecom</td><td>SME</td><td>300</td><td>150</td><td>2.0</td></tr><tr><td>China Mobile</td><td>Individual</td><td>5</td><td>2.5</td><td>2.0</td></tr><tr><td>China Mobile</td><td>Individual</td><td>20</td><td>10</td><td>2.0</td></tr><tr><td>China Mobile</td><td>Individual</td><td>40</td><td>20</td><td>2.0</td></tr><tr><td>China Unicom</td><td>Individual</td><td>7.5</td><td>6</td><td>1.3</td></tr><tr><td>China Unicom</td><td>Individual</td><td>15</td><td>12</td><td>1.3</td></tr><tr><td>China Unicom</td><td>Individual</td><td>22.5</td><td>18</td><td>1.3</td></tr><tr><td>Tencent Cloud</td><td>Individual</td><td>39</td><td>35</td><td>1.1</td></tr><tr><td>Tencent Cloud</td><td>Individual</td><td>99</td><td>100</td><td>1.0</td></tr><tr><td>Tencent Cloud</td><td>Individual</td><td>299</td><td>320</td><td>0.9</td></tr><tr><td>Tencent Cloud</td><td>Individual</td><td>599</td><td>650</td><td>0.9</td></tr><tr><td>Bytedance Cloud</td><td>Individual</td><td>19</td><td>50</td><td>0.4</td></tr><tr><td>Bytedance Cloud</td><td>Individual</td><td>99</td><td>200</td><td>0.5</td></tr><tr><td>Bytedance Cloud</td><td>Individual</td><td>199</td><td>400</td><td>0.5</td></tr></table>

Source: Company data

Valuation and risks 

<table><tr><td colspan="2"></td><td>Valuation</td><td>Risk</td></tr><tr><td>China Mobile 941 HK 600941 CH</td><td>Current price: HKD86.40 RMB100.35 Target price: HKD94.00 RMB111.00 Upside: H: 8.8%A: 10.6%</td><td>Methodology: DCF-based sum-of-the-parts (SOTP) valuation approach. Assumptions: We use a DCF-based SOTP valuation approach to better capture the value of China Mobile&#x27;s core telecom business in China as well as its investments in other entities. Detailed assumptions are provided in the SOTP table.H-share target price: Our approach returns a fair value target price of HKD94.00 per share (unchanged). This implies upside of c9% from the current share price. We maintain our Buy rating. The company has strong FY26 dividend yield support, the highest among China telcos.RMB counter (80941 HK, RMB75.15) - target price of RMB81.00 (unchanged). We convert our H-share target price of HKD94.00 to RMB based on an RMB-HKD assumption of 1.16 (unchanged).Secondary listing: A-share target price: We apply a premium of 36% (based on the three-month average premium of the A-shares relative to the H-shares) to our H-share target price to derive our A-share target price of RMB111.00. This implies upside of c11% from the current share price, and we upgrade our rating to Buy from Hold. The company has strong FY26 dividend yield support, the highest among China telcos.Piyush Choudhary*, CFA | piyush.choudhary@hsbc.com.sg | +65 6658 0607</td><td>Key H/A downside risksFaster-than-expected decline in consumer mobile revenue due to market share lossMore intense competition in the mobile and home broadband marketsFurther RMB depreciation could reduce the value of China Mobile-H&#x27;s dividend</td></tr><tr><td>China Telecom 728 HK 601728 CH</td><td>Current price: HKD5.64 RMB6.82 Target price: HKD5.60 RMB6.30 Downside: H: -0.7%A: -7.6%</td><td>Methodology: DCF-based sum-of-the-parts (SOTP) valuation approach. Assumptions: We use a DCF-based SOTP valuation approach to better capture the value of China Telecom&#x27;s core telecom business in China as well as its investments in other entities. Detailed assumptions are provided in the SOTP table.H-share target price: Our approach returns a fair value target price of HKD5.60 (unchanged). This implies downside of c1% from the current share price and we maintain our Hold rating.Secondary listing: A-share target price: We apply a premium of 31% (based on the three-month average premium of the A-shares relative to the H-shares) to our H-share target price to derive our A-share target price of RMB6.30 (unchanged). This implies downside of c8% from the current share price and we maintain our Hold rating, as we like the shares&#x27; high exposure to the cloud and IDC market, and we think it is best positioned for AI growth in China.Piyush Choudhary*, CFA | piyush.choudhary@hsbc.com.sg | +65 6658 0607</td><td>Key H/A downside risksMore intense competition in the mobile and home broadband marketHigher-than-expected marketing expensesFurther RMB depreciation would reduce the value of China Telecom-H&#x27;s dividendKey H/A upside risksFaster-than-expected growth and profitability improvementsLower-than-expected capex</td></tr><tr><td>China Unicom 762 HK 600050 CH</td><td>Current price: HKD7.94 RMB4.92 Target price: HKD6.50 RMB4.10 Downside: H: 18.1%A: 16.7%</td><td>Methodology: DCF-based sum-of-the-parts (SOTP) valuation approach. Assumptions: We use a DCF-based SOTP valuation approach to better capture the value of China Unicom&#x27;s core telecom business in China as well as its investments in other entities. Detailed assumptions are provided in the SOTP table.H-share target price: Our approach returns a fair value target price of HKD6.50 (unchanged). This implies downside of c18% from the current share price and we maintain our Reduce rating, as we think the shares are fairly valued, given the company&#x27;s reliance on non-operating income.Secondary listing: A-share target price: We apply a premium of 67% (based on the three-month average premium of the A-shares relative to the H-shares) to our H-share target price to derive our A-share target price of RMB4.10 (unchanged). This implies downside of c17% from the current share price and we maintain our Hold rating, as we think the shares are fairly valued, given the company&#x27;s reliance on non-operating income.Piyush Choudhary*, CFA | piyush.choudhary@hsbc.com.sg | +65 6658 0607</td><td>Key H/A upside risksFaster-than-expected growth and profitability improvements in the CDSA businessHigher-than-expected payout ratioLower-than-expected capex</td></tr></table>

Priced at 18 May 2026   
\* Employed by a non-US affiliate of HSBC Securities (USA) Inc, and is not registered/ qualified pursuant to FINRA regulations   
Source: Bloomberg, HSBC estimates

# 3. China Mobile: SOTP valuation assumptions

<table><tr><td></td><td>Valuation method</td><td>Valuation assumptions/rationale</td></tr><tr><td>Core telecom assets</td><td>DCF</td><td>Cost of equity at 8.05% comprising a risk-free rate of 4.25%, a beta of 0.8, equity risk premium of 4.75%, country risk premium of 0%. We apply a cost of debt of 3.5%, a debt-to-capital ratio of 5%, and a terminal growth rate of 0%. All our inputs remain unchanged. This leads to a WACC of 7.78%.</td></tr><tr><td>Fair value of SPDB</td><td>Average market price</td><td>We value China Mobile&#x27;s 18% stake in SPD Bank (600000 CH, CMP RMB9.08, Hold, covered by Angel Sun) by applying a 20% holding company discount to the three-month average of the stock price.</td></tr><tr><td>Fair value of China Tower</td><td>HSBC TP</td><td>We value its 28% stake in China Tower (788 HK, CMP HKD10.94, Hold) using HSBC&#x27;s target price of HKD11.40, applying a 20% holding company discount.</td></tr><tr><td colspan="2">Fair value of other associatesSource: HSBC estimates. Priced at 18 May 2026</td><td>We reflect CM&#x27;s 7.8% stake in True Corp and 9.7% stake in Iflytek and all other associates – combined under &quot;fair value of other associates/investments&quot;, discounted at 20% holding company discount.</td></tr></table>

# 4. China Mobile: SOTP table

<table><tr><td></td><td>Stake</td><td>RMBm</td><td>RMB/share</td><td>HKD/share</td><td>Contribution</td></tr><tr><td>Assessed EV of telecoms assets</td><td></td><td>1,410,781</td><td>68.1</td><td>78.7</td><td>84.1%</td></tr><tr><td>Add: fair value of SPDB</td><td>18.0%</td><td>50,589</td><td>2.4</td><td>2.8</td><td>3.0%</td></tr><tr><td>Add: fair value of China Tower</td><td>27.9%</td><td>38,555</td><td>1.9</td><td>2.1</td><td>2.3%</td></tr><tr><td>Add: value of other associates/investments</td><td></td><td>14,110</td><td>0.7</td><td>0.8</td><td>0.8%</td></tr><tr><td>Less: minority interests</td><td></td><td>(4,507)</td><td>(0.2)</td><td>(0.3)</td><td>-0.3%</td></tr><tr><td>Less: (net debt)/cash</td><td></td><td>168,087</td><td>8.1</td><td>9.4</td><td>10.0%</td></tr><tr><td>Fair equity value</td><td></td><td>1,677,615</td><td>81</td><td>94</td><td></td></tr><tr><td>Number of Shares outstanding (m)</td><td></td><td>20,724</td><td></td><td></td><td></td></tr><tr><td>Fair value per share, RMB</td><td></td><td>81</td><td></td><td></td><td></td></tr><tr><td>Fair value per share, HKD</td><td></td><td>94</td><td></td><td></td><td></td></tr></table>

Source: HSBC estimates. Note: Priced at 18 May 2026. 1) Percentage contribution to target price may not add up to 100% due to rounding. 2) We convert our RMB target price to HKD based on our FX team's end-2026e RMB-HKD rate of 1.16.

# 5. China Telecom: SOTP valuation assumptions

<table><tr><td></td><td>Valuation method</td><td>Valuation assumptions/rationale</td></tr><tr><td>Core telecom assets</td><td>DCF</td><td>Cost of equity at 8.05% comprising a risk-free rate of 4.25%, a beta of 0.8, an equity risk premium of 4.75%, and a country risk premium of 0%. We apply a cost of debt of 3.5%, a debt-to-capital ratio of 10%, and a terminal growth rate of 0%. All our inputs remain unchanged. This leads to a WACC of 7.51%.</td></tr><tr><td>Fair value of China Tower</td><td>HSBC TP</td><td>We value China Telecom&#x27;s 20.5% stake in China Tower (788 HK, CMP HKD10.94, Hold) using HSBC&#x27;s target price of HKD11.40, applying a 20% holding company discount.</td></tr><tr><td>Fair value of other associates</td><td></td><td>We value other associates using the company&#x27;s reported book value (excluding the value of the China Tower stake).</td></tr></table>

Source: HSBC estimates. Priced at 18 May 2026

# 6. China Telecom SOTP valuation

<table><tr><td></td><td>Stake</td><td>RMBm</td><td>RMB/share</td><td>HKD/share</td><td>Contribution</td></tr><tr><td>Assessed EV of telecoms assets</td><td></td><td>304,730</td><td>3.33</td><td>3.85</td><td>69%</td></tr><tr><td>Add: fair value of China Tower stake</td><td>20.5%</td><td>28,298</td><td>0.31</td><td>0.36</td><td>6%</td></tr><tr><td>Add: value of associates</td><td></td><td>3,464</td><td>0.04</td><td>0.04</td><td>1%</td></tr><tr><td>Less: minority interests</td><td></td><td>4,162</td><td>0.05</td><td>0.05</td><td>1%</td></tr><tr><td>Less: (net debt)/cash</td><td></td><td>99,705</td><td>1.09</td><td>1.26</td><td>23%</td></tr><tr><td>Fair equity value</td><td></td><td>440,359</td><td>4.81</td><td>5.56</td><td></td></tr><tr><td>Number of shares outstanding (m)</td><td></td><td>91,507</td><td></td><td></td><td></td></tr><tr><td>Fair value per share, RMB</td><td></td><td>4.81</td><td></td><td></td><td></td></tr><tr><td>Fair value per share, HKD</td><td></td><td>5.60</td><td></td><td></td><td></td></tr></table>

Source: HSBC estimates. Note: Priced at 18 May 2026. 1) Percentage contribution to target price may not add up to 100% due to rounding. 2) We convert our RMB target price to HKD based on our FX team's end-2026e RMB-HKD rate of 1.16.

# 7. China Unicom: SOTP valuation assumptions

<table><tr><td></td><td>Valuation method</td><td>Valuation assumptions/rationale</td></tr><tr><td>Core telecom assets</td><td>DCF</td><td>Cost of equity at 8.65% comprising a risk-free rate of 4.25%, a beta of 0.9, an equity risk premium of 4.75%, and a country risk premium of 0%. We apply a cost of debt of 3.5%, a debt-to-capital ratio of 10%, and a terminal growth rate of -0.5%. All our inputs remain unchanged. This leads to a WACC of 8.05%.</td></tr><tr><td>Fair value of China Tower</td><td>HSBC TP</td><td>We value its 20.5% stake in China Tower (788 HK, CMP HKD10.94, Hold), using HSBC&#x27;s target price of HKD11.40, applying a 20% holding company discount.</td></tr><tr><td>Fair value of other associates</td><td></td><td>We value other associates using the company&#x27;s reported book value (excluding the value of the China Tower stake).</td></tr></table>

Source: HSBC estimates. Priced at 18 May 2026

# 8. China Unicom: SOTP table

<table><tr><td></td><td>Stake</td><td>RMBm</td><td>RMB/share</td><td>HKD/share</td><td>Contribution</td></tr><tr><td>Assessed EV of telecoms assets</td><td></td><td>62,011</td><td>2.0</td><td>2.3</td><td>36%</td></tr><tr><td>Add: fair value of China Tower stake</td><td>20.6%</td><td>28,505</td><td>0.9</td><td>1.1</td><td>17%</td></tr><tr><td>Add: value of associates</td><td></td><td>28,431</td><td>0.9</td><td>1.1</td><td>17%</td></tr><tr><td>Less: minority interests</td><td></td><td>2,525</td><td>0.1</td><td>0.1</td><td>1%</td></tr><tr><td>Less: (net debt) / cash</td><td></td><td>50,369</td><td>1.6</td><td>1.9</td><td>29%</td></tr><tr><td>Fair equity value</td><td></td><td>171,842</td><td>5.6</td><td>6.5</td><td></td></tr><tr><td>Number of shares out

[中间内容因长度限制已省略]

s may act as market maker or have assumed an underwriting commitment in the securities of companies discussed in this document (or in related investments), may sell them to or buy them from customers on a principal basis and may also perform or seek to perform investment banking or underwriting services for or relating to those companies. The document is intended to be distributed in its entirety. Unless governing law permits otherwise, you must contact a HSBC Group member in your home jurisdiction if you wish to use HSBC Group services in effecting a transaction in any investment mentioned in this document.

In the UK, this publication is distributed by HSBC Bank plc for the information of its Clients (as defined in the Rules of FCA) and those of its affiliates only. Nothing herein excludes or restricts any duty or liability to a customer which HSBC Bank plc has under the Financial Services and Markets Act 2000 or under the Rules of FCA and PRA. A recipient who chooses to deal with any person who is not a representative of HSBC Bank plc in the UK will not enjoy the protections afforded by the UK regulatory regime. HSBC Bank plc is regulated by the Financial Conduct Authority and the Prudential Regulation Authority.

In the European Economic Area, this publication has been distributed by HSBC Continental Europe or by such other HSBC affiliate from which the recipient receives relevant services.

In Japan, this publication has been distributed by HSBC Securities (Japan) Co., Ltd.. It may not be further distributed in whole or in part for any purpose. In Korea, this publication is distributed by either The Hongkong and Shanghai Banking Corporation Limited, Seoul Securities Branch ("HBAP SLS") or The Hongkong and Shanghai Banking Corporation Limited, Seoul Branch ("HBAP SEL") for the general information of professional investors specified in Article 9 of the Financial Investment Services and Capital Markets Act ("FSCMA"). This publication is not a prospectus as defined in the FSCMA. It may not be further distributed in whole or in part for any purpose. Both HBAP SLS and HBAP SEL are regulated by the Financial Services Commission and the Financial Supervisory Service of Korea. In Australia, this publication has been distributed by The Hongkong and Shanghai Banking Corporation Limited (ABN 65 117 925 970, AFSL 301737) for the general information of its "wholesale" customers (as defined in the Corporations Act 2001). Where distributed to retail customers, this research is distributed by HSBC Bank Australia Limited (ABN 48 006 434 162, AFSL No. 232595). These respective entities make no representations that the products or services mentioned in this document are available to persons in Australia or are necessarily suitable for any particular person or appropriate in accordance with local law. No consideration has been given to the particular investment objectives, financial situation or particular needs of any recipient.

HSBC Securities (USA) Inc. accepts responsibility for the content of this research report prepared by its non-US foreign affiliate. The information contained herein is under no circumstances to be construed as investment advice and is not tailored to the needs of the recipient. All US persons receiving and/or accessing this report and wishing to effect transactions in any security discussed herein should do so with HSBC Securities (USA) Inc. in the United States and not with its non-US foreign affiliate, the issuer of this report. HSBC México, S.A., Institución de Banca Múltiple, Grupo Financiero HSBC is authorized and regulated by Secretaría de Hacienda y Crédito Público and Comisión Nacional Bancaria y de Valores (CNBV). In Brazil, this document has been distributed by Banco HSBC SA ("HSBC Brazil"), and/or its affiliates. As required by Resolution No. 20/2021 of the Securities and Exchange Commission of Brazil (Comissão de Valores Mobiliários), potential conflicts of interest concerning (i) HSBC Brazil and/or its affiliates; and (ii) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited, Singapore Branch.

[1279679]
"""
