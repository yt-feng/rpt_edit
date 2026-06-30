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
June 28, 2026 07:18 PM GMT

Electronic Components | Japan

# Investor Visits in Singapore & Hong Kong

We held 31 one-on-one meetings with institutional investors in Singapore and Hong Kong during June 22–26, and a group lunch meeting with institutional investors in both Singapore and Hong Kong, mainly discussing MLCCs and ABF package substrates.

## Key Takeaways

We expect Murata Mfg's MLCCs to continue to see ASP growth driven by improvements and changes in product mix; our rating remains OW.

The gap in corporate value between companies that implement price hikes readily and those that continuously enhance product competitiveness is likely to become more pronounced

While we expect Ibiden to continue expanding earnings, market consensus appears too high. Our rating remains UW.

Discussions focused mainly on MLCC and ABF package substrates: We assign investment ratings to 20 companies engaged in electronic components. In discussions with investors in Singapore and Hong Kong, the main topics included (1) the positioning of Murata and Taiyo Yuden in high value-added MLCCs for AI servers, (2) supply-demand and pricing of commoditized MLCCs, (3) differences between the MLCC market in 2018 and 2026, and (4) Ibiden's technological competitiveness and valuation in ABF package substrates.

Murata's MLCCs to see significant ASP growth even without price hikes due to increasing sales of high value-added products for AI servers: We expect that in AI server accelerator boards, the total capacitance required of MLCC increases at roughly twice the rate with each new generation of GPUs, while installation space remains limited, supporting continued growth in demand for compact, high-capacitance, high value-added MLCCs. Murata has advanced miniaturization and higher capacitance of MLCC not only by refining and homogenizing the particle size of barium titanate (key material) and increasing the number of layers, but also by narrowing the width of external electrodes to increase volume of dielectric layers. It plans to increase sales to AI/data centers by 85-90% YoY in F3/27, assuming volume growth of \~40% and ASP growth of \~50%. The ASP increase does not assume unit price hikes for identical products, but rather reflects a roughly 50% rise driven by a higher mix of high unit price, high value-added products. Investor interest in our meetings was almost entirely focused on the extent of price hikes in commoditized products, with little attention paid to the likelihood of earnings expansion driven by growth in high value-added products. We expect the gap in corporate value between companies that raise prices indiscriminately and those that continuously improve product competitiveness to become increasingly evident.

MS MUFG SECURITIES CO., LTD.+

Shoji Sato
Equity Analyst
Shoji.Sato@morganstanleymufg.com

+81 3 6836-8404

Sota Harashima
Equity Analyst
Sota.Harashima@morganstanleymufg.com

+81 3 6836-8897

![](images/40f727a5746906bc0ec6b26cd316ff403206ab99874ec09df1002bdaa5d1b708.jpg)

ELECTRONIC COMPONENTS

Japan
Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Market share ranking for AI server high value-added MLCCs is 1) Murata, 2) SEMCO, 3) Taiyo Yuden: We estimate MLCC market share in 2025 at 40.8% for Murata Manufacturing, 22.5% for SEMCO, and 11.3% for Taiyo Yuden. We estimate MLCC sales for AI/data centers accounted for 10-15% of Murata's total MLCC sales in F3/26, and forecast this will increase by 85–90% YoY in F3/27 to account for 20–25% of MLCC sales, and continue growing at a similar pace from F3/28 onward. For Taiyo Yuden, we estimate AI/data center MLCC sales accounted for 5–10% of total MLCC sales in F3/26, and will increase by 82-83% YoY in F3/27 to around 15% of MLCC sales, and continue expanding at a similar pace from F3/28 onward. Demand for MLCC such as 1608 size 100μF, 1005 size 47μF, and 0603 size 10μF is increasing significantly in AI servers, but it appears that only Murata can stably mass-produce all of these products. While the timing of when Taiyo Yuden will achieve stable mass production of all these MLCCs remains unclear, by the time it does so for products comparable to Murata's, we think Murata is likely to be mass-producing even smaller, higher-capacitance MLCCs. Although we expect Taiyo Yuden's earnings to benefit from increased sales of MLCC for AI servers/ data centers and higher utilization rates, we believe Murata remains the only company capable of stably supplying high value-added products, and thus the contribution of high value-added products to Taiyo Yuden's earnings will likely be limited. In addition, as Taiyo Yuden froze capex in 2H 2024, we estimate MLCC production capacity growth was limited to around 5% in F3/26, constraining its ability to capture new business.

The gap between companies that implement price hikes at each opportunity and those that continuously enhance product competitiveness will become more evident over the medium to long term: Many Japanese electronic component companies, including Murata, combine strong technological competitiveness with cost competitiveness. Many of these companies earn high levels of profit supported by their advanced products, while also maintaining strong cost competitiveness in commoditized products. Prices from distributors to customers for commoditized MLCC appear to be rising. We infer that Murata adjusts prices flexibly in line with market conditions for commoditized products. Murata does not proactively implement price hikes for commoditized products because while such increases may maximize short-term profits, they risk lowering barriers to entry, facilitating entry by companies from China, South Korea, and Taiwan, and ultimately leading to share erosion over the medium to long term. In contrast, many companies in China, South Korea, and Taiwan that pursue short-term profit maximization through indiscriminate price increases appear not to allocate sufficient resources to R&D or to improving production technology to enhance product competitiveness. While rising prices for commoditized products may boost short-term profits for companies focused on these products, we argue that they are unlikely to contribute to medium- to long-term market share gains or expansion in corporate value.

While we expect Ibiden to continue expanding earnings, market expectations appear too high: We estimate Ibiden began volume shipments of ABF package substrates for NVIDIA's Rubin in 4Q F3/26, and expect sales of ABF package substrates for Rubin to exceed those for Blackwell in 1Q F3/27, driving continued earnings expansion through growth in high value-added ABF package substrates. We expect ABF package substrates to continue to become more value-added, driven in part by increases in SAP size. That said, we forecast OP at ¥94.7bn in F3/27 (company forecast ¥90bn, FactSet consensus ¥99.7bn), ¥128.5bn in F3/28 (company forecast ¥150bn, FS consensus ¥151.5bn), and ¥242.6bn in F3/31 (company forecast ¥300bn). While we expect continued earnings

growth, we believe market expectations for Ibiden are too high. We expect earnings expansion driven by EMIB-T; however, we believe meaningful contribution to Ibiden's earnings will materialize from F3/29 onward. While we expect pricing to significantly exceed that of existing ABF package substrates, we see it as difficult for EMIB-T products to achieve profit margins comparable to NVIDIA's existing offerings.

Exhibit 1: Electronic Components Industry: Gaps between recent share prices and PTs (base, bull, bear case fair value)

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">Rating</td><td rowspan="2">Price26/6/26</td><td rowspan="2">Target PriceBase</td><td colspan="5">% Difference</td></tr><tr><td></td><td>-68%</td><td></td><td>16%</td><td>44%</td></tr><tr><td>MURATA MANUFACTURING</td><td>6981</td><td>Overweight</td><td>10,770</td><td>12,500</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TDK</td><td>6762</td><td>Overweight</td><td>3,575</td><td>4,900</td><td></td><td>-58%</td><td></td><td>37%</td><td>88%</td></tr><tr><td>HIROSE ELECTRIC</td><td>6806</td><td>Overweight</td><td>29,660</td><td>36,600</td><td></td><td></td><td>-28%</td><td>23%</td><td>68%</td></tr><tr><td>NITERRA</td><td>5334</td><td>Overweight</td><td>10,845</td><td>12,600</td><td></td><td>-66%</td><td></td><td>16%</td><td>29%</td></tr><tr><td>ALPS ALPINE</td><td>6770</td><td>Overweight</td><td>1,982</td><td>3,000</td><td></td><td></td><td>-24%</td><td></td><td>51%</td></tr><tr><td>MEIKO ELECTRONICS</td><td>6787</td><td>Equal-weight</td><td>30,250</td><td>39,200</td><td></td><td></td><td>-44%</td><td></td><td>30%</td></tr><tr><td>MINEBEA MITSUMI</td><td>6479</td><td>Equal-weight</td><td>4,805</td><td>5,300</td><td></td><td></td><td>-50%</td><td>10%</td><td>6%</td></tr><tr><td>KYOCERA</td><td>6971</td><td>Equal-weight</td><td>3,411</td><td>4,000</td><td></td><td></td><td>-56%</td><td>17%</td><td>47%</td></tr><tr><td>NICHICON</td><td>6996</td><td>Equal-weight</td><td>4,300</td><td>4,700</td><td></td><td></td><td>-67%</td><td>9%</td><td></td></tr><tr><td>NIHON DEMPA KOGYO</td><td>6779</td><td>Equal-weight</td><td>3,890</td><td>4,900</td><td></td><td></td><td>-74%</td><td></td><td>26%</td></tr><tr><td>HAMAMATSU PHOTONICS</td><td>6965</td><td>Equal-weight</td><td>2,625</td><td>3,000</td><td></td><td></td><td>-62%</td><td>14%</td><td>52%</td></tr><tr><td>KOA</td><td>6999</td><td>Equal-weight</td><td>2,929</td><td>3,000</td><td></td><td></td><td>-56%</td><td>2%</td><td></td></tr><tr><td>MABUCHI MOTOR</td><td>6592</td><td>Equal-weight</td><td>1,609</td><td>1,750</td><td></td><td></td><td></td><td>-25%</td><td>43%</td></tr><tr><td>JAE</td><td>6807</td><td>Equal-weight</td><td>2,276</td><td>2,600</td><td></td><td></td><td></td><td></td><td>85%</td></tr><tr><td>CMK</td><td>6958</td><td>Equal-weight</td><td>657</td><td>790</td><td></td><td></td><td>-38%</td><td></td><td>20%</td></tr><tr><td>DAISHINKU</td><td>6962</td><td>Underweight</td><td>923</td><td>840</td><td></td><td></td><td>-76%</td><td>-9%</td><td></td></tr><tr><td>NIPPON CHEMI-CON</td><td>6997</td><td>Underweight</td><td>5,590</td><td>3,500</td><td></td><td></td><td>-73%</td><td>-37%</td><td>27%</td></tr><tr><td>IBIDEN</td><td>4062</td><td>Underweight</td><td>24,000</td><td>13,000</td><td></td><td></td><td>-75%</td><td>-46%</td><td></td></tr><tr><td>TAIYO YUDEN</td><td>6976</td><td>Underweight</td><td>16,780</td><td>12,500</td><td></td><td></td><td>-55%</td><td>-26%</td><td>31%</td></tr><tr><td colspan="4"></td><td>-200%</td><td>-150%</td><td>-100%</td><td>-50%</td><td>0%</td><td>50%</td></tr></table>

Source: FactSet, MS

Exhibit 2: Sales and OP for coverage electronic components companies

<table><tr><td rowspan="2">(JPY bn)</td><td colspan="3">F25</td><td colspan="5">F26</td><td rowspan="2">F21</td><td rowspan="2">F22</td><td rowspan="2">F23</td><td rowspan="2">F24</td><td rowspan="2">F25</td><td rowspan="2">F26e</td><td rowspan="2">F27e</td><td rowspan="2">F28e</td><td rowspan="2">F29e</td><td rowspan="2">F30e</td><td colspan="2">F26Ce</td><td>F26Ce</td><td>F26e</td><td>F27e</td><td>F28e</td><td>+1Q</td></tr><tr><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1Qe</td><td>2Qe</td><td>3Qe</td><td>4Qe</td><td>1He</td><td>2He</td><td>FSE</td><td>FSE</td><td>FSE</td><td>FSE</td><td></td></tr><tr><td colspan="26">Sales</td></tr><tr><td>USD/JPY-Average Rate</td><td></td><td>144.5</td><td>147.5</td><td>154.0</td><td>156.9</td><td>155.0</td><td>155.0</td><td>155.0</td><td>112.4</td><td>135.4</td><td>144.5</td><td>152.5</td><td>150.6</td><td>155.0</td><td>155.0</td><td>155.0</td><td>155.0</td><td>155.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>IBIDEN</td><td>4062</td><td>97.5</td><td>98.0</td><td>103.1</td><td>117.6</td><td>117.8</td><td>122.5</td><td>132.1</td><td>137.6</td><td>401.1</td><td>417.5</td><td>370.5</td><td>369.4</td><td>416.2</td><td>509.8</td><td>614.5</td><td>730.2</td><td>877.6</td><td>976.4</td><td>230.0</td><td>270.0</td><td>500.0</td><td>516.3</td><td>646.3</td><td>796.5</td></tr><tr><td>NITERRA</td><td>5334</td><td>169.9</td><td>181.2</td><td>174.9</td><td>205.2</td><td>200.1</td><td>202.2</td><td>205.4</td><td>205.6</td><td>491.7</td><td>562.6</td><td>614.5</td><td>653.0</td><td>731.2</td><td>813.2</td><td>854.8</td><td>919.7</td><td>990.6</td><td>1,068.3</td><td>391.0</td><td>399.0</td><td>790.0</td><td>786.3</td><td>841.3</td><td>959.4</td></tr><tr><td>MINEBEA MITSUMI</td><td>6479</td><td>366.9</td><td>411.4</td><td>453.9</td><td>432.2</td><td>417.1</td><td>440.7</td><td>436.7</td><td>416.6</td><td>1,124.1</td><td>1,292.2</td><td>1,402.1</td><td>1,522.7</td><td>1,664.4</td><td>1,711.2</td><td>1,766.0</td><td>1,839.2</td><td>1,910.5</td><td>1,985.6</td><td>846.5</td><td>843.5</td><td>1,690.0</td><td>1,693.7</td><td>1,775.1</td><td>1,838.8</td></tr><tr><td>MABUCHI MOTOR</td><td>6592</td><td>47.0</td><td>48.0</td><td>52.1</td><td>53.4</td><td>50.4</td><td>55.5</td><td>57.6</td><td>55.3</td><td>134.6</td><td>156.7</td><td>178.7</td><td>196.2</td><td>200.4</td><td>218.8</td><td>233.7</td><td>249.0</td><td>265.8</td><td>283.8</td><td>104.6</td><td>108.4</td><td>213.0</td><td>210.5</td><td>220.3</td><td>232.6</td></tr><tr><td>TDK</td><td>6762</td><td>535.8</td><td>647.6</td><td>675.2</td><td>646.3</td><td>651.8</td><td>703.2</td><td>719.3</td><td>693.7</td><td>1,902.1</td><td>2,180.8</td><td>2,103.9</td><td>2,204.8</td><td>2,504.8</td><td>2,768.0</td><td>3,020.6</td><td>3,295.6</td><td>3,600.9</td><td>3,938.7</td><td></td><td></td><td>2,580.0</td><td>2,694.5</td><td>2,885.6</td><td>3,126.2</td></tr><tr><td>ALPS ALPINE</td><td>6770</td><td>238.9</td><td>266.8</td><td>255.5</td><td>258.3</td><td>251.5</td><td>271.0</td><td>276.0</td><td>266.0</td><td>802.9</td><td>933.1</td><td>964.1</td><td>990.4</td><td>1,019.5</td><td>1,064.5</td><td>1,157.6</td><td>1,222.2</td><td>1,300.1</td><td>1,385.1</td><td>508.0</td><td>537.0</td><td>1,045.0</td><td>1,047.1</td><td>1,089.9</td><td>1,117.6</td></tr><tr><td>NIHON DEMP A KOGYO</td><td>6779</td><td>12.7</td><td>14.0</td><td>13.2</td><td>14.8</td><td>14.8</td><td>15.3</td><td>15.6</td><td>16.2</td><td>45.4</td><td>52.5</td><td>50.3</td><td>53.1</td><td>54.6</td><td>61.9</td><td>66.6</td><td>72.4</td><td>79.7</td><td>89.1</td><td>29.5</td><td>31.1</td><td>60.6</td><td>61.9</td><td>66.6</td><td>72.4</td></tr><tr><td>MEIKO ELECTRONICS</td><td>6787</td><td>53.1</td><td>58.4</td><td>60.5</td><td>68.5</td><td>73.7</td><td>78.2</td><td>85.2</td><td>86.7</td><td>151.3</td><td>167.3</td><td>179.5</td><td>206.8</td><td>240.6</td><td>323.8</td><td>412.9</td><td>482.1</td><td>539.7</td><td>595.1</td><td></td><td></td><td>320.0</td><td>320.7</td><td>397.6</td><td>471.1</td></tr><tr><td>HIROSE ELECTRIC</td><td>6806</td><td>49.0</td><td>53.1</td><td>54.5</td><td>54.7</td><td>57.2</td><td>58.9</td><td>59.5</td><td>59.0</td><td>163.7</td><td>183.2</td><td>165.5</td><td>189.4</td><td>211.3</td><td>234.6</td><td>254.6</td><td>275.4</td><td>298.2</td><td>323.4</td><td>115.0</td><td>115.0</td><td>230.0</td><td>230.6</td><td>248.3</td><td>268.6</td></tr><tr><td>JAE</td><td>6807</td><td>51.6</td><td>58.8</td><td>56.3</td><td>61.1</td><td>55.6</td><td>61.9</td><td>57.0</td><td>60.6</td><td>225.1</td><td>235.9</td><td>225.8</td><td>221.6</td><td>227.9</td><td>235.1</td><td>236.9</td><td>245.1</td><td>248.0</td><td>251.3</td><td>120.0</td><td>120.0</td><td>240.0</td><td>237.2</td><td>246.3</td><td>257.2</td></tr><tr><td>CMK</td><td>6958</td><td>22.8</td><td>24.4</td><td>25.8</td><td>27.2</td><td>23.8</td><td>25.6</td><td>26.7</td><td>27.5</td><td>81.5</td><td>83.8</td><td>90.6</td><td>95.5</td><td>100.2</td><td>103.6</td><td>106.2</td><td>109.2</td><td>112.5</td><td>116.2</td><td></td><td></td><td>104.0</td><td>104.8</td><td>109.6</td><td>114.6</td></tr><tr><td>DAISHINKU</td><td>6962</td><td>9.4</td><td>10.2</td><td>10.0</td><td>10.0</td><td>10.2</td><td>10.6</td><td>10.1</td><td>10.0</td><td>41.3</td><td>38.4</td><td>39.3</td><td>38.6</td><td>39.6</td><td>40.9</td><td>43.4</td><td>46.2</td><td>49.1</td><td>52.3</td><td></td><td></td><td>41.0</td><td>41.1</td><td>43.6</td><td>46.2</td></tr><tr><td>HAMAMATSU PHOTONICS</td><td>6965</td><td>50.6</td><td>56.2</td><td>48.7</td><td>56.6</td><td>51.9</td><td>60.6</td><td>58.2</td><td>62.1</td><td>169.0</td><td>208.8</td><td>221.4</td><td>204.0</td><td>212.1</td><td>232.8</td><td>245.8</td><td>265.7</td><td>287.6</td><td>311.9</td><td>112.5</td><td>119.5</td><td>232.0</td><td>231.2</td><td>245.8</td><td>262.7</td></tr><tr><td>KYOCERA</td><td>6971</td><td>478.0</td><td>513.3</td><td>530.6</td><td>548.2</td><td>468.0</td><td>492.0</td><td>495.5</td><td>496.0</td><td>1,838.9</td><td>2,025.3</td><td>2,004.2</td><td>2,014.5</td><td>2,070.2</td><td>1,951.5</td><td>1,977.2</td><td>2,102.9</td><td>2,236.8</td><td>2,379.3</td><td></td><td></td><td>1,940.0</td><td>2,016.9</td><td>2,097.7</td><td>2,219.3</td></tr><tr><td>TAIYO YUDEN</td><td>6976</td><td>84.8</td><td>92.8</td><td>88.5</td><td>89.2</td><td>94.2</td><td>101.2</td><td>107.1</td><td>108.8</td><td>349.6</td><td>319.5</td><td>322.6</td><td>341.4</td><td>355.3</td><td>411.3</td><td>475.1</td><td>523.8</td><td>573.9</td><td>624.8</td><td></td><td></td><td>384.0</td><td>396.3</td><td>447.5</td><td>515.3</td></tr><tr><td>MURATA MANUFACTURING</td><td>6981</td><td>416.2</td><td>486.6</td><td>467.5</td><td>460.6</td><td>466.2</td><td>535.5</td><td>532.0</td><td>510.5</td><td>1,812.5</td><td>1,686.8</td><td>1,640.2</td><td>1,743.4</td><td>1,830.9</td><td>2,044.2</td><td>2,449.7</td><td>2,830.5</td><td>3,292.2</td><td>3,860.7</td><td>960.0</td><td>1,000.0</td><td>1,960.0</td><td>2,030.6</td><td>2,359.5</td><td>2,814.6</td></tr><tr><td>NICHICON</td><td>6996</td><td>39.6</td><td>41.1</td><td>43.5</td><td>45.5</td><td>42.5</td><td>44.4</td><td>49.4</td><td>50.7</td><td>142.2</td><td>184.7</td><td>181.6</td><td>175.8</td><t

[中间内容因长度限制已省略]

organ Stanley International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Electronic Components

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/26/2026)</td></tr><tr><td colspan="3">Shoji Sato</td></tr><tr><td>ALPS ALPINE (6770.T)</td><td>O (03/17/2026)</td><td>¥1,982</td></tr><tr><td>Hamamatsu Photonics (6965.T)</td><td>E (06/17/2026)</td><td>¥2,625</td></tr><tr><td>Ibiden (4062.T)</td><td>U (02/04/2026)</td><td>¥24,000</td></tr><tr><td>Kyocera (6971.T)</td><td>E (06/25/2020)</td><td>¥3,411</td></tr><tr><td>Mabuchi Motor (6592.T)</td><td>E (11/03/2022)</td><td>¥1,609</td></tr><tr><td>Minebea Mitsumi (6479.T)</td><td>E (10/23/2025)</td><td>¥4,805</td></tr><tr><td>Murata Manufacturing (6981.T)</td><td>O (11/26/2025)</td><td>¥10,770</td></tr><tr><td>Nidec (6594.T)</td><td>NR (09/05/2025)</td><td>¥2,543</td></tr><tr><td>Niterra (5334.T)</td><td>O (01/17/2024)</td><td>¥10,845</td></tr><tr><td>Taiyo Yuden (6976.T)</td><td>U (06/17/2026)</td><td>¥16,780</td></tr><tr><td>TDK (6762.T)</td><td>O (08/02/2022)</td><td>¥3,575</td></tr><tr><td colspan="3">Sota Harashima</td></tr><tr><td>CMK (6958.T)</td><td>E (02/28/2025)</td><td>¥657</td></tr><tr><td>Daishinku (6962.T)</td><td>U (06/17/2026)</td><td>¥923</td></tr><tr><td>Hirose Electric (6806.T)</td><td>O (07/10/2024)</td><td>¥29,660</td></tr><tr><td>IRISO Electronics (6908.T)</td><td>E (08/02/2022)</td><td>¥2,957</td></tr><tr><td>Japan Aviation Electronics Industry (6807.T)</td><td>E (01/17/2024)</td><td>¥2,276</td></tr><tr><td>KOA (6999.T)</td><td>E (06/17/2026)</td><td>¥2,929</td></tr><tr><td>Meiko Electronics (6787.T)</td><td>E (04/03/2026)</td><td>¥30,250</td></tr><tr><td>Nichicon (6996.T)</td><td>E (11/10/2021)</td><td>¥4,300</td></tr><tr><td>Nihon Dempa Kogyo (6779.T)</td><td>E (03/07/2024)</td><td>¥3,890</td></tr><tr><td>Nippon Chemi-Con (6997.T)</td><td>U (09/20/2024)</td><td>¥5,590</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS MUFG
"""
