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
Global

Credit/Covered Bonds

# Covered Bonds and SSA Update

Date

25 May 2026

# CB in CA - LCR level 1, lower growth of global supra supply in 2026 - if any

# OSFI proposal - LCR Level 1 for CB - supportive for spreads

Last week, Canada's Office of the Superintendent of Financial Institutions (OSFI) launched a public consultation on the 2027 Liquidity Adequacy Requirements (LAR) Guideline. OSFI proposes to introduce a new Level 1B category of HQLA, including highly rated CB subject to a $7\%$ haircut. In our view, this is driven by Canadian banks willing to achieve "third country equivalence" in the EU going forward (i.e. Canadian CB to be recognized as LCR Level 1 in the EU, instead of LCR level 2A at best currently.

Under Basel III framework, highly-rated CB are typically eligible for Level 2A HQLA status, subject to a 15% haircut. Currently, in the EU, LCR Level 1 with a 7% haircut applies only to CB with EU Covered Premium Label. We highlight that the OSFI proposal (as current EU LCR rules for CB) goes beyond BIS recommendations. Under the latter, LCR Level 2A is currently still the highest HQLA category CB can achieve. The public consultation allows market participants to actively contribute to the process by submitting their feedback by 20 July 2026, ahead of the expected finalisation of the Guideline in Feb 2027 and the implementation anticipated on 1 May 2027.

In our view, given that Canadian banks have an outstanding CB volume of EUR 183.4bn equivalent (eq), with 46.5% denominated in EUR (30.5% in USD, 15% in GBP, 3% in CHF, 2.9% in CAD, 1.7% in AUD and 0.4% in NOK), they have a strong interest that the OSFI proposal for CB to be recognized as LCR Level 1B eligible in Canada becomes effective. The volume of retained Canadian CB declined significantly, down to one issue amounting to USD 5bn.

We are still somewhat cautious on strong demand for foreign CB by Canadian banks for their own LCR portfolios. For example, we understand that bonds issued by Canadian provinces are LCR Level 1 eligible in Canada (without the 7% haircut that would apply for CB). However, overall, the proposal by OSFI shows that regulatory support for CB is increasing further globally, particularly in countries making strong use of CB. While the proposal still takes until at least 1 May 2027 to become effective and the impact on the domestic CB market in Canada is not clear, on the margin, this is positive for spreads for Canadian CB. This is due to increased likelihood "third country equivalence" for Canadian CB in the EU going forward and potentially somewhat higher domestic CB supply by Canadian issuers and therefore lower international supply.

Bernd Volk

Strategist

+41-44-227-3710

Siddharth Garg

Research Associate

# Global supra supply remains high amid low supply by Worldbank

We provide annual supply of main supra issuers globally, including all currencies since 2021 and supply ytd (based in Bloomberg, including non-benchmark bonds and taps), in total and per issuer in EUR equivalent terms (Figure 1). We provide the same for EUR, USD, and GBP denominated bonds only, in each currency (Figures 2-4).

After a strong increase of supra supply for three consecutive years, ytd supply from main supras globally stands at EUR 254.7bn equivalent (eq), which is 52% of FY 2025 (EUR 489.4bn eq). While total ytd supply by non-European surpras declined by around 11% (link here), total ytd supply by European supras is up by around 8% (link here), with more to come from European supras (due to the EU having increased its FY supply indication by EUR 20bn to "around EUR 180bn" versus "around EUR 160bn" previously).

However, IBRD's ytd supply stands at EUR 16.7bn eq versus EUR 59.3bn eq for FY 2025. Regarding USD, ytd supply by IBRD stands at USD 12.9bn, 71% less than the FY 2025 USD denominated supply of USD 44.1bn. IFC's ytd supply stands at EUR 7.9bn eq versus EUR 24.2bn eq for FY 2025. It's ytd USD supply stands at USD 3.9bn which is 71% less than the USD 13.4bn issued in FY 2025. IDAWBG's ytd supply stands at EUR 2bn eq versus EUR 19.9bn eq for FY 2025, with ytd supply denominated exclusively in EUR (i.e., IDAWBG did not tap the USD or GBP market ytd).

In our view, total ytd supply by the main global supra issuers accounting for 52% versus FY 2025 leaves room for 2026 to end up with higher supply than 2025. Moreover, it is noteworthy that Worldbank entities have a financial from 1 July to 30 June of the following calendar year. However, it seems that the significant growth of global supra supply in the past two years will not be achieved in 2026, if any. For example, also on a ytd basis, supply by Worldbank entities declined significantly (link here).

On the other hand, with recently increased inflation, plenty of geopolitical challenges, stretched sovereign budgets in most countries and the consensus seeing an increased need for defence spending in many countries, we expect global supra supply to end up close to or at historically high levels also in 2026 (with the EU being the key driver of growing supply in 2026).

Despite ongoing high supply, with sovereign debt typically at staggeringly high levels and the direction of travel remaining upward, supras with high paid-in and callable capital and ratings being not strongly linked to the respective shareholders seem have assets. This is due to, for example, their typical preferred creditor status (PCS), which could become extremely important in times of further worsening sovereign credit quality. In our view, supras will be particularly needed in case of sovereign bond defaults.

Figure 1: Total annual supply (including all currencies) by main supra issuers globally since 2021 (EUR bn equivalent) 

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 Ytd</td></tr><tr><td>EU</td><td>132.5</td><td>118.3</td><td>115.9</td><td>138.1</td><td>152.6</td><td>83.8</td></tr><tr><td>EIB</td><td>55.3</td><td>44.3</td><td>49.9</td><td>63.4</td><td>64.2</td><td>41.2</td></tr><tr><td>EFSF</td><td>16.5</td><td>19.5</td><td>20.0</td><td>20.0</td><td>21.5</td><td>14.0</td></tr><tr><td>NIB</td><td>7.1</td><td>9.5</td><td>7.3</td><td>9.2</td><td>9.1</td><td>4.6</td></tr><tr><td>EBRD</td><td>13.4</td><td>5.4</td><td>11.1</td><td>25.9</td><td>26.4</td><td>13.0</td></tr><tr><td>ESM</td><td>7.7</td><td>8.0</td><td>7.8</td><td>6.0</td><td>6.7</td><td>2.5</td></tr><tr><td>COE</td><td>4.6</td><td>6.0</td><td>7.0</td><td>6.2</td><td>5.9</td><td>4.8</td></tr><tr><td>EUROF</td><td>0.8</td><td>1.8</td><td>1.5</td><td>0.7</td><td>0.9</td><td>1.1</td></tr><tr><td>IBRD</td><td>45.9</td><td>26.0</td><td>46.4</td><td>57.3</td><td>59.3</td><td>16.7</td></tr><tr><td>ASIA</td><td>29.8</td><td>31.9</td><td>26.7</td><td>30.3</td><td>37.8</td><td>24.8</td></tr><tr><td>Restricted</td><td>7.1</td><td>6.9</td><td>9.3</td><td>9.1</td><td>9.3</td><td>6.9</td></tr><tr><td>IADB</td><td>20.7</td><td>16.0</td><td>17.4</td><td>19.6</td><td>19.5</td><td>9.5</td></tr><tr><td>IFC</td><td>10.2</td><td>9.1</td><td>15.4</td><td>10.4</td><td>24.2</td><td>7.9</td></tr><tr><td>CAF</td><td>3.6</td><td>3.3</td><td>6.1</td><td>5.0</td><td>7.5</td><td>5.3</td></tr><tr><td>AFDB</td><td>8.0</td><td>8.8</td><td>4.8</td><td>7.0</td><td>9.8</td><td>8.4</td></tr><tr><td>IDAWBG</td><td>8.5</td><td>6.3</td><td>4.1</td><td>14.4</td><td>19.9</td><td>2.0</td></tr><tr><td>IDBINV</td><td>1.3</td><td>2.3</td><td>2.0</td><td>2.2</td><td>2.6</td><td>1.3</td></tr><tr><td>EURDEV</td><td>0.5</td><td>0.0</td><td>0.2</td><td>0.1</td><td>0.2</td><td>0.0</td></tr><tr><td>IINVBK</td><td>0.4</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NEWDEV</td><td>4.7</td><td>2.0</td><td>4.3</td><td>3.7</td><td>4.5</td><td>3.4</td></tr><tr><td>BSTDBK</td><td>0.6</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.3</td></tr><tr><td>CABEI</td><td>1.3</td><td>1.3</td><td>1.8</td><td>2.3</td><td>2.8</td><td>2.5</td></tr><tr><td>NADB</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.1</td><td>0.0</td><td>0.0</td></tr><tr><td>ISDB</td><td>3.7</td><td>2.6</td><td>4.7</td><td>4.1</td><td>5.0</td><td>0.9</td></tr><tr><td>Total</td><td>384.1</td><td>329.4</td><td>363.6</td><td>435.2</td><td>489.4</td><td>254.7</td></tr></table>

Source : Bloomberg Finance LP, DB

Figure 2: Total EUR denominated annual supply by main supra issuers globally since 2021 (EUR bn) 

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 Ytd</td></tr><tr><td>EU</td><td>132.5</td><td>118.3</td><td>115.9</td><td>138.1</td><td>152.6</td><td>83.8</td></tr><tr><td>EIB</td><td>26.5</td><td>23.3</td><td>24.4</td><td>29.8</td><td>33.1</td><td>20.6</td></tr><tr><td>EFSF</td><td>16.5</td><td>19.5</td><td>20.0</td><td>20.0</td><td>21.5</td><td>14.0</td></tr><tr><td>NIB</td><td>0.7</td><td>1.3</td><td>0.9</td><td>2.7</td><td>2.0</td><td>0.2</td></tr><tr><td>EBRD</td><td>2.3</td><td>0.4</td><td>0.4</td><td>1.8</td><td>1.6</td><td>0.8</td></tr><tr><td>ESM</td><td>6.0</td><td>8.0</td><td>5.0</td><td>6.0</td><td>5.0</td><td>2.5</td></tr><tr><td>COE</td><td>2.1</td><td>3.9</td><td>3.2</td><td>3.2</td><td>2.1</td><td>1.1</td></tr><tr><td>EUROF</td><td>0.6</td><td>1.4</td><td>0.9</td><td>0.7</td><td>0.4</td><td>1.1</td></tr><tr><td>IBRD</td><td>6.1</td><td>1.5</td><td>8.4</td><td>6.6</td><td>6.7</td><td>0.2</td></tr><tr><td>ASIA</td><td>1.3</td><td>2.0</td><td>0.1</td><td>3.8</td><td>3.8</td><td>2.6</td></tr><tr><td>Restricted</td><td>0.0</td><td>0.2</td><td>1.5</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>IADB</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.1</td><td>0.0</td></tr><tr><td>IFC</td><td>0.3</td><td>0.0</td><td>0.0</td><td>0.1</td><td>0.0</td><td>0.3</td></tr><tr><td>CAF</td><td>1.3</td><td>0.6</td><td>1.0</td><td>0.2</td><td>2.0</td><td>1.0</td></tr><tr><td>AFDB</td><td>0.1</td><td>2.8</td><td>0.0</td><td>0.6</td><td>1.0</td><td>0.1</td></tr><tr><td>IDAWBG</td><td>3.8</td><td>6.0</td><td>0.6</td><td>3.9</td><td>9.3</td><td>2.0</td></tr><tr><td>IDBINV</td><td>0.0</td><td>0.7</td><td>0.5</td><td>0.0</td><td>0.5</td><td>0.0</td></tr><tr><td>EURDEV</td><td>0.3</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>IINVBK</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NEWDEV</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.1</td><td>0.0</td><td>0.1</td></tr><tr><td>BSTDBK</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>CABEI</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NADB</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>ISDB</td><td>0.0</td><td>0.0</td><td>0.9</td><td>1.2</td><td>1.4</td><td>0.0</td></tr><tr><td>Total</td><td>200.5</td><td>189.7</td><td>183.6</td><td>219.6</td><td>244.1</td><td>131.3</td></tr></table>

Source : Bloomberg Finance LP, DB

Figure 3: Total USD denominated annual supply by main supra issuers globally since 2021 (USD bn) 

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 Ytd</td></tr><tr><td>EU</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>EIB</td><td>20.5</td><td>15.0</td><td>18.1</td><td>28.1</td><td>22.6</td><td>16.6</td></tr><tr><td>EFSF</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NIB</td><td>3.7</td><td>3.7</td><td>3.0</td><td>2.8</td><td>3.2</td><td>1.8</td></tr><tr><td>EBRD</td><td>6.7</td><td>1.8</td><td>4.7</td><td>9.6</td><td>18.1</td><td>10.3</td></tr><tr><td>ESM</td><td>2.0</td><td>0.0</td><td>3.0</td><td>0.0</td><td>2.0</td><td>0.0</td></tr><tr><td>COE</td><td>1.5</td><td>1.0</td><td>2.0</td><td>2.5</td><td>2.5</td><td>2.5</td></tr><tr><td>EUROF</td><td>0.0</td><td>0.5</td><td>0.7</td><td>0.0</td><td>0.6</td><td>0.0</td></tr><tr><td>IBRD</td><td>35.6</td><td>17.3</td><td>29.9</td><td>41.3</td><td>44.1</td><td>12.9</td></tr><tr><td>ASIA</td><td>22.5</td><td>21.6</td><td>20.0</td><td>18.2</td><td>21.8</td><td>17.9</td></tr><tr><td>Restricted</td><td>6.2</td><td>4.2</td><td>4.2</td><td>4.8</td><td>6.0</td><td>4.2</td></tr><tr><td>IADB</td><td>21.3</td><td>13.6</td><td>13.8</td><td>15.1</td><td>16.0</td><td>7.2</td></tr><tr><td>IFC</td><td>5.6</td><td>3.3</td><td>6.8</td><td>5.5</td><td>13.4</td><td>3.9</td></tr><tr><td>CAF</td><td>1.7</td><td>1.7</td><td>3.7</td><td>2.8</td><td>3.6</td><td>3.0</td></tr><tr><td>AFDB</td><td>5.6</td><td>3.8</td><td>2.6</td><td>5.0</td><td>6.4</td><td>6.1</td></tr><tr><td>IDAWBG</td><td>2.0</td><td>0.0</td><td>2.5</td><td>10.0</td><td>8.0</td><td>0.0</td></tr><tr><td>IDBINV</td><td>1.1</td><td>1.3</td><td>1.5</td><td>1.8</td><td>2.0</td><td>1.0</td></tr><tr><td>EURDEV</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>IINVBK</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NEWDEV</td><td>4.4</td><td>0.2</td><td>3.0</td><td>1.9</td><td>1.5</td><td>2.5</td></tr><tr><td>BSTDBK</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.4</td></tr><tr><td>CABEI</td><td>0.5</td><td>0.6</td><td>1.4</td><td>1.5</td><td>1.6</td><td>2.1</td></tr><tr><td>NADB</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>ISDB</td><td>4.3</td><td>2.8</td><td>4.1</td><td>3.3</td><td>4.1</td><td>1.0</td></tr><tr><td>Total</td><td>145.3</td><td>92.3</td><td>125.0</td><td>154.0</td><td>177.5</td><td>93.5</td></tr></table>

Source : Bloomberg Finance LP, DB

Figure 4: Total GBP denominated annual supply by main supra issuers globally since 2021 (GBP bn) 

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 Ytd</td></tr><tr><td>EU</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>EIB</td><td>4.4</td><td>1.4</td><td>2.1</td><td>3.0</td><td>3.3</td><td>3.0</td></tr><tr><td>EFSF</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NIB</td><td>0.8</td><td>1.3</td><td>1.0</td><td>0.8</td><td>0.9</td><td>0.5</td></tr><tr><td>EBRD</td><td>0.6</td><td>0.0</td><td>0.1</td><td>1.2</td><td>2.6</td><td>0.7</td></tr><tr><td>ESM</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>COE</td><td>0.7</td><td>0.7</td><td>1.0</td><td>0.2</td><td>0.3</td><td>0.9</td></tr><tr><td>EUROF</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>IBRD</td><td>1.5</td><td>1.5</td><td>1.1</td><td>3.1</td><td>2.5</td><td>1.0</td></tr><tr><td>ASIA</td><td>1.7</td><td>2.4</td><td>2.1</td><td>3.3</td><td>3.5</td><td>1.9</td></tr><tr><td>Restricted</td><td>0.2</td><td>0.6</td><td>1.0</td><td>0.8</td><td>0.5</td><td>0.5</td></tr><tr><td>IADB</td><td>0.4</td><td>1.6</td><td>1.4</td><td>2.6</td><td>2.5</td><td>1.2</td></tr><tr><td>IFC</td><td>0.8</td><td>1.0</td><td>1.6</td><td>2.3</td><td>4.6</td><td>0.4</td></tr><tr><td>CAF</td><td>0.0</td><td>0.0</td><td>0.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>AFDB</td><td>1.2</td><td>0.7</td><td>0.3</td><td>0.0</td><td>1.6</td><td>1.5</td></tr><tr><td>IDAWBG</td><td>2.5</td><td>0.0</td><td>0.8</td><td>0.8</td><td>1.2</td><td>0.0</td></tr><tr><td>IDBINV</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.3</td></tr><tr><td>EURDEV</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>IINVBK</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>NEWDEV</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>BSTDBK</td><td>0.1</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>CABEI</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.8</td><td>0.5</td></tr><tr><td>NADB</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>ISDB</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Source : Bloomberg Finance LP, DB

Figure 5: Full names of European supras in Figures above 

<table><tr><td>Ticker</td><td>Names</td></tr><tr><td>EU</td><td>European Union</td></tr><tr><td>EIB</td><td>European Investment Bank</td></tr><tr><td>EFSF</td><td>European Financial Stability Facility</td></tr><tr><td>NIB</td><td>Nordic Investment Bank</td></tr><tr><td>EBRD</td><td>European Bank for Reconstruction and Development</td></tr><tr><td>ESM</td><td>European Stability Mechanism</td></tr><tr><td>COE</td><td>Council of Europe Development Bank</td></tr><tr><td>EUROF</td><td>Eurofima</td></tr><tr><td></td><td></td></tr></table>

Source : Bloomberg Finance LP, DB

Figure 6: Full names of non-European supras in Figures above 

<table><tr><td>Ticker</td><td>Names</td></tr><tr><td>ASIA</td><td>Asian Development Bank</td></tr><tr><td>IBRD</td><td>International Bank for Reconstruction &amp; Development</td></tr><tr><td>IADB</td><td>Inter-American Development Bank</td></tr><tr><td>AFDB</td><td>African Development Bank</td></tr><tr><td>IFC</td><td>International Finance Corp</td></tr><tr><td>CAF</td><td>Corp Andina de Fomento</td></tr><tr><td>NEWDEV</td><td>New Development Bank/The</td></tr><tr><td>CABEI</td><td>Central American Bank for Economic Integration</td></tr><tr><td>IDAWBG</td><td>International Development Association</td></tr><tr><td>IDBINV</td><td>Inter-American Investment Corp</td></tr><tr><td>ISDB</td><td>Isdb Trust Services NO 2 SARL</td></tr><tr><td>BSTDBK</td><td>Black Sea Trade &amp; Development Bank</td></tr><tr><td>EURDEV</td><td>Eurasian Development Bank</td></tr><tr><td>IINVBK</td><td>International Investment Bank</td></tr><tr><td>NADB</td><td>North American Development Bank</td></tr></table>

Source : Bloomberg Finance LP

# Appendix 1

# Important Disclosures

\*Other information available upon request

\*Prices are current as of the end of the previous trading session unless otherwise indicated and are sourced from local exchanges via Reuters, Bloomberg and other vendors. Other information is sourced from DB, subject companies, and other sources. For further information regarding disclosures relevant to DB, please visit our global disclosure look-up page on our website at https://research.db.com/Research/Disclosures/FICCDisclosures. Aside from within this report, important risk and conflict disclosures can also be found at https://research.db.com/Research/Disclosures/Disclaimer. Investors are strongly encouraged to review this information before investing.

# Analyst Certifi

[中间内容因长度限制已省略]

ysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

# David Folkerts-Landau

Group Chief Economist and Global Head of Research

Pam Finelli
Global Chief Operating Officer
Research

Steve Pollard
Global Head of Company
Research and Sales

Jim Reid
Global Head of
Macro and Thematic Research

Tim Rokossa
Head of Germany
Research

Gerry Gallagher
Head of European
Company Research

Matthew Barnard
Head of Americas
Company Research

Peter Milliken
Head of APAC
Company Research

Debbie Jones
Global Head of Sustainability
and Data Innovation, Research

Sameer Goel
Global Head of EM & APAC
Research

Francis Yared
Global Head of Rates Research

George Saravelos
Global Head of FX Research

Peter Hooper
Vice-Chair of Research

International Production Locations 

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip</td><td>60329 Frankfurt am Main</td><td>Centre,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Streets</td><td>Germany</td><td>1 Austin Road West,Kowloon,</td><td>Japan</td></tr><tr><td>Sydney, NSW 2000</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Tel: (81) 3 6730 1000</td></tr><tr><td>Australia</td><td></td><td>Tel: (852) 2203 8888</td><td></td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td></td><td></td></tr><tr><td>DB AG</td><td>DB Securities Inc.</td><td>DB AG</td><td></td></tr><tr><td>21 Moorfields</td><td>The DB Center</td><td>Filiale Singapur</td><td></td></tr><tr><td>London EC2Y 9DB</td><td>1 Columbus Circle</td><td>One Raffles Quay, South</td><td></td></tr><tr><td>United Kingdom</td><td>New York, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>
"""
