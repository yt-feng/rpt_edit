你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
24 Jul 2026 05:48:38 ET | 13 pages

# MiniMax (0100.HK)

Key Takeaways from Senior Management Meeting

## CITI'S TAKE

On July 23, we attended a meeting for sell-side analysts hosted by MiniMax in Shanghai where Dr. Yan Junjie, Chairman and CEO, and Ms. Yun Yeyi, ED and COO, shared their thoughts and answered questions regarding the industry landscape, MiniMax's strategic focus i.e. extreme intelligence at extreme cost-efficiency, the company's edges in computing infrastructure, strategies to optimize each step of its training process, coding and agentic tasks as focus of improvement for next foundational model, and thoughts on multimodal capabilities with Hailuo 3 to launch soon. We believe MiniMax possesses edges in infrastructure, and with management presenting clearer strategies on optimizing training processes, we see an improving outlook for next version of the foundational model. Investor sentiment will likely remain skeptical until MiniMax proves the next version of its models can deliver better capabilities – hence we see Hailuo 3, to be launched soon, as a potential catalyst. Maintain Buy/High Risk.

Thoughts on industry landscape — Management believes the LLM industry is entering a phase of explosive growth with intense competition, characterized by persistent computing scarcity and high user churn. Over the next several months, model scale could further expand quickly, achieving 3tn-parameter levels, while application demand, especially in coding, autonomous agents, and multimodal content creation, is expected to surge exponentially. Computing supply, constrained by global production, will remain tight, resulting in reasonable margins for LLMs. For China market, management believes no single player has achieved absolute dominance, and this presents opportunity for a player who can deliver strong model capabilities with low cost. Management believes future success will depend not only on a single breakthrough but on sustained R&D while maintaining attractive pricing.

Strategies — MiniMax will focus on its strategy, extreme intelligence at extreme cost-efficiency, i.e. the company aims to offer the best possible performance per dollar spent, which will become increasingly important as token volumes explode. The upcoming 3tn-parameter model, which we expect will be released in \~Sep-Oct, has shown decent progress and will have a more mature update. Architecturally, MinimMax chooses sparse attention over linear attention variants, prioritizing inference speed and stability. (Continued below...)

Earnings Summary

<table><tr><td>Year to 31 Dec</td><td>Net Profit (US$M)</td><td>Diluted EPS (US$)</td><td>EPS growth (%)</td><td>P/E (x)</td><td>P/B (x)</td><td>ROE (%)</td><td>Yield (%)</td></tr><tr><td>2024A</td><td>-244</td><td>-2.25</td><td>-165.8</td><td>-11.3</td><td>-3.5</td><td>na</td><td>na</td></tr><tr><td>2025A</td><td>-251</td><td>-2.31</td><td>-2.7</td><td>-11.0</td><td>-1.0</td><td>na</td><td>na</td></tr><tr><td>2026E</td><td>-516</td><td>-1.64</td><td>28.8</td><td>-15.5</td><td>7.0</td><td>na</td><td>na</td></tr><tr><td>2027E</td><td>-571</td><td>-1.80</td><td>-9.7</td><td>-14.1</td><td>14.3</td><td>-67.4</td><td>na</td></tr><tr><td>2028E</td><td>-344</td><td>-1.07</td><td>40.4</td><td>na</td><td>37.1</td><td>-88.1</td><td>na</td></tr></table>

Source: Powered by dataCentral

<table><tr><td colspan="2">Buy / High Risk</td></tr><tr><td>Price (23 Jul 26 16:10)</td><td>HK$199.30</td></tr><tr><td>Target price</td><td>HK$533.00</td></tr><tr><td>Expected share price return</td><td>167.4%</td></tr><tr><td>Expected dividend yield</td><td>0.0%</td></tr><tr><td>Expected total return</td><td>167.4%</td></tr><tr><td>Market Cap</td><td>HK$69,603MUS$8,877M</td></tr></table>

## Price Performance

![](images/08b666a13775d9042598ab6cc34efcc6d7c9da4397e6f04a092024898d2302ba.jpg)

Alicia Yap, CFA $^{AC}$ +852-2501-2773
alicia.yap@citi.com

Brian Gong
+852-2501-2747
brian.gong@citi.com

Nelson Cheung
nelson.cheung@citi.com

<table><tr><td>Profit &amp; Loss (US$m)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue</td><td>31</td><td>79</td><td>232</td><td>726</td><td>1,808</td></tr><tr><td>Cost of sales</td><td>-27</td><td>-59</td><td>-162</td><td>-461</td><td>-1,052</td></tr><tr><td>Gross profit</td><td>4</td><td>20</td><td>70</td><td>265</td><td>756</td></tr><tr><td>Gross Margin (%)</td><td>12.2</td><td>25.4</td><td>30.1</td><td>36.5</td><td>41.8</td></tr><tr><td>EBITDA (Adj)</td><td>-463</td><td>-1,870</td><td>-551</td><td>-608</td><td>-375</td></tr><tr><td>EBITDA Margin (Adj) (%)</td><td>na</td><td>na</td><td>na</td><td>-83.7</td><td>-20.8</td></tr><tr><td>Depreciation</td><td>-2</td><td>-1</td><td>-2</td><td>-5</td><td>-14</td></tr><tr><td>Amortisation</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>EBIT (Adj)</td><td>-258</td><td>-251</td><td>-516</td><td>-571</td><td>-344</td></tr><tr><td>EBIT Margin (Adj) (%)</td><td>na</td><td>na</td><td>na</td><td>-78.7</td><td>-19.0</td></tr><tr><td>Net interest</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>Associates</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Non-Op/Except/Other Adj</td><td>-207</td><td>-1,620</td><td>-37</td><td>-41</td><td>-45</td></tr><tr><td>Pre-tax profit</td><td>-465</td><td>-1,872</td><td>-554</td><td>-613</td><td>-390</td></tr><tr><td>Tax</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Extraord./Min.Int./Pref.div.</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Reported net profit</td><td>-465</td><td>-1,872</td><td>-554</td><td>-613</td><td>-390</td></tr><tr><td>Net Margin (%)</td><td>na</td><td>na</td><td>na</td><td>-84.5</td><td>-21.6</td></tr><tr><td>Core NPAT</td><td>-244</td><td>-251</td><td>-516</td><td>-571</td><td>-344</td></tr></table>

Price: HK\$199.30; TP: HK\$533.00; Market Cap: HK\$69,603m; Recomm: Buy/High Risk

<table><tr><td>Valuation ratios</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>PE (x)</td><td>-11.3</td><td>-11.0</td><td>-15.5</td><td>-14.1</td><td>-23.7</td></tr><tr><td>PB (x)</td><td>-3.5</td><td>-1.0</td><td>7.0</td><td>14.3</td><td>37.1</td></tr><tr><td>EV/EBITDA (x)</td><td>-18.6</td><td>-4.5</td><td>-14.9</td><td>-13.8</td><td>-23.7</td></tr><tr><td>FCF yield (%)</td><td>-9.4</td><td>-9.6</td><td>-5.7</td><td>-6.9</td><td>-4.8</td></tr><tr><td>Dividend yield (%)</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td></tr><tr><td>Payout ratio (%)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>ROE (%)</td><td>na</td><td>na</td><td>na</td><td>-72.4</td><td>-99.9</td></tr></table>

<table><tr><td>Cashflow (US$m)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>EBITDA</td><td>-463</td><td>-1,870</td><td>-551</td><td>-608</td><td>-375</td></tr><tr><td>Working capital</td><td>14</td><td>-4</td><td>69</td><td>33</td><td>-23</td></tr><tr><td>Other</td><td>191</td><td>1,614</td><td>37</td><td>41</td><td>45</td></tr><tr><td>Operating cashflow</td><td>-258</td><td>-260</td><td>-445</td><td>-534</td><td>-353</td></tr><tr><td>Capex</td><td>-1</td><td>-4</td><td>-7</td><td>-22</td><td>-36</td></tr><tr><td>Net acq/disposals</td><td>-503</td><td>28</td><td>-26</td><td>-27</td><td>-28</td></tr><tr><td>Other</td><td>72</td><td>13</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Investing cashflow</td><td>-431</td><td>37</td><td>-33</td><td>-49</td><td>-65</td></tr><tr><td>Dividends paid</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Financing cashflow</td><td>771</td><td>439</td><td>710</td><td>400</td><td>300</td></tr><tr><td>Net change in cash</td><td>83</td><td>219</td><td>229</td><td>-182</td><td>-118</td></tr><tr><td>Free cashflow to s/holders</td><td>-259</td><td>-264</td><td>-452</td><td>-555</td><td>-389</td></tr></table>

<table><tr><td>Per share data</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Reported EPS ($)</td><td>-4.28</td><td>-17.23</td><td>-1.77</td><td>-1.94</td><td>-1.22</td></tr><tr><td>Core EPS ($)</td><td>-2.25</td><td>-2.31</td><td>-1.64</td><td>-1.80</td><td>-1.07</td></tr><tr><td>DPS ($)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CFPS ($)</td><td>-2.38</td><td>-2.39</td><td>-1.42</td><td>-1.69</td><td>-1.10</td></tr><tr><td>FCFPS ($)</td><td>-2.39</td><td>-2.43</td><td>-1.44</td><td>-1.75</td><td>-1.22</td></tr><tr><td>BVPS ($)</td><td>-7.36</td><td>-24.37</td><td>3.61</td><td>1.78</td><td>0.69</td></tr><tr><td>Wtd avg ord shares (m)</td><td>109</td><td>109</td><td>314</td><td>315</td><td>318</td></tr><tr><td>Wtd avg diluted shares (m)</td><td>109</td><td>109</td><td>314</td><td>317</td><td>320</td></tr></table>

<table><tr><td>Growth rates</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Sales revenue (%)</td><td>782.2</td><td>158.9</td><td>193.5</td><td>212.8</td><td>149.2</td></tr><tr><td>EBIT (Adj) (%)</td><td>-169.3</td><td>2.7</td><td>-105.8</td><td>-10.6</td><td>39.8</td></tr><tr><td>Core NPAT (%)</td><td>-174.2</td><td>-2.7</td><td>-105.8</td><td>-10.6</td><td>39.8</td></tr><tr><td>Core EPS (%)</td><td>-165.8</td><td>-2.7</td><td>28.8</td><td>-9.7</td><td>40.4</td></tr></table>

<table><tr><td>Balance Sheet (US$m)</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Cash &amp; cash equiv.</td><td>289</td><td>508</td><td>737</td><td>555</td><td>437</td></tr><tr><td>Accounts receivables</td><td>7</td><td>11</td><td>19</td><td>30</td><td>50</td></tr><tr><td>Inventory</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Net fixed &amp; other tangibles</td><td>2</td><td>2</td><td>14</td><td>37</td><td>75</td></tr><tr><td>Goodwill &amp; intangibles</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Financial &amp; other assets</td><td>610</td><td>565</td><td>626</td><td>681</td><td>783</td></tr><tr><td>Total assets</td><td>911</td><td>1,088</td><td>1,398</td><td>1,305</td><td>1,347</td></tr><tr><td>Accounts payable</td><td>51</td><td>58</td><td>111</td><td>126</td><td>144</td></tr><tr><td>Short-term debt</td><td>19</td><td>35</td><td>45</td><td>445</td><td>745</td></tr><tr><td>Long-term debt</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Provisions &amp; other liab</td><td>1,639</td><td>3,643</td><td>109</td><td>171</td><td>239</td></tr><tr><td>Total liabilities</td><td>1,710</td><td>3,737</td><td>265</td><td>743</td><td>1,129</td></tr><tr><td>Shareholders&#x27; equity</td><td>-799</td><td>-2,648</td><td>1,133</td><td>562</td><td>218</td></tr><tr><td>Minority interests</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Total equity</td><td>-799</td><td>-2,648</td><td>1,133</td><td>562</td><td>218</td></tr><tr><td>Net debt (Adj)</td><td>-269</td><td>-472</td><td>-692</td><td>-109</td><td>308</td></tr><tr><td>Net debt to equity (Adj) (%)</td><td>na</td><td>na</td><td>-61.0</td><td>-19.4</td><td>141.4</td></tr></table>

For definitions of the items in this table, please click here.

Computing infrastructure as a key edge — Management believes its self-built computing infrastructure is its important key competitive edge, operating on one of the largest GPU clusters among independent Chinese AI firms. By building its own data centers last year, MiniMax was able to lock in lower hardware prices before the recent surge. This early bet gives them a structural cost advantage that competitors who rely on cloud rentals can’t easily replicate, according to management. More importantly, owning the full stack provides MiniMax the capability for deep integration like custom networking and proprietary storage solutions. As a result, its cluster utilization exceeds 90% above the industry norm. With GPU vendors now iterating annually, MiniMax’s ability to procure the right chips at the right time through strategic planning becomes an important competitive edge, according to management.

■ Strategies to optimize training — MiniMax has clear strategies to optimize each step of its model training. For pre-training, the next-version model will scale to 3tn-parameter level, and MiniMax is optimizing through compressing KV cache usage, which will make its next model more advanced. For post-training data distribution, to ensure sufficient source diversity and complexity of data, MiniMax is recruiting domain experts from critical fields to curate high-quality and complex data and collecting high quality data through screening and mining on internet. Beyond data collection, high quality data requires rigorous cleaning and processing. Lastly, reinforcement learning (RL) stabilizes model capabilities and raises their ceiling. MiniMax has achieved decent progress on pre-training for its next model, and management believes RL remains underdeveloped in the domestic model industry, presenting ample room for improvement, and MiniMax has invested heavily in this area.

■ Focus of the next-version model — The upcoming 3tn-parameter model will focus on two primary areas:

\- Coding – The goal is to achieve world-class proficiency in solving isolated programming problems, leveraging high-quality data from sources such as GitHub, open-source codebases and internally curated examples. MiniMax believes that coding serves as a foundational capability for almost all downstream applications.

\- Agentic tasks – MiniMax actively recruits domain experts in fields such as cybersecurity, chip design, law and others. These experts do not merely label data, but interact with the model through real problem-solving processes.

\- Thoughts on multimodal model — MiniMax has high conviction in native multimodal architectures, believing that true intelligence requires unified perception including understanding scene, text, image and videos. During the training on the next-version foundational model, the company introduced an “information density” filter, prioritizing high density multi-modal data. The company believes that multimodal capabilities are becoming a standard requirement for major frontier models, evidenced by US peers’ focus on visual input and native multimodal capabilities. MiniMax sees strong potential of video generation model and will launch its next version Hailuo soon.

## Removing Downside 30-Day Short-Term View on MiniMax (0100.HK)

Direction: Downside

Date Added: 03 Jul 2026

Category: Special situations and Valuation

In our previous note published on July 3rd, we opened a Downside 30-Day Short-Term View on the stock as we were cautious amid selling pressure post the IPO lock-up expiration on July 9th. The share price is down >40% in the past 20 days, which we believe likely largely reflects the dissipation of the overhang, and hence we now close our Downside 30-Day Short-Term View. With the upcoming release of Hailuo 3 and possible future release of 3tn-parameter model in the next few months, any better-than-expected traction of these models would likely support neutralizing negative sentiment on the stock.

## MiniMax

## Company description

MiniMax is a pure-play model company, focusing on global, multi-modality (text, video, audio, music) models with strategic emphasis on modality integration (LLM +VLM). Since its inception in 2021, the company has strived to create models capable of handling text, video, audio and music. As of December 31, 2025, MiniMax had served more than 236m users across over 200 countries and regions, as well as 214,000 enterprise customers and developers from more than 100 countries and regions.

## Investment strategy

We rate the MiniMax stock as Buy/High Risk. Our investment thesis is based on the company's: 1) advanced technological breakthroughs and quick new model

[中间内容因长度限制已省略]

eipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party

involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
