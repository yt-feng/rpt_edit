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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China: Growth of both exports and imports quickened in May

Export growth in USD terms increased to 19.4% y-o-y in May (Consensus: 15.0%; NOM: 13.7%), above expectations and up further from 14.1% in April. Import growth also increased to 27.4% in May from 25.3% in April, slightly above market expectations (Consensus and NOM: 26.0%) and still highly elevated. As a result, the trade surplus widened to USD105.4bn in May from USD84.8bn in April. As we recently flagged, robust semiconductor trade remained the dominant driver of highly elevated export and import growth in May, with the divergence between value and volume growth widening further, as chip price increases continued to overwhelm quantity growth. We estimate chips contributed 5.9pp to headline export growth. Together with automatic data processing (ADP) equipment, which is also closely linked to the current global AI boom and contributed an additional 3.4pp, AI-related exports accounted for 9.3pp. This marks two consecutive months in which AI-related exports have accounted for around half of China's total export growth, underscoring the outsized role of the global AI supercycle. Moreover, price effects continued to play a major role in growth of both exports and imports in May.

Beyond the AI boom, export growth to the US surged to 37.3% y-o-y in May from 11.1% in April, driven by three factors, in our view. First, favourable base effects from last year's tariff war. Second, the net tariff reduction in late February after the US Supreme Court struck down the IEEPA-based tariffs – which was followed by the imposition of lower Section 122 tariffs – appears to have provided a tangible boost to China's exports to the US. Third, a sizeable proportion of demand for AI production came from the US.

On the import side, the energy shock and the semiconductor upcycle remained the two dominant forces. Crude oil imports increased further to 17.8% y-o-y in value terms in May (April: 15.4%), while they contracted sharply in volume terms by 29.0% (April: -19.5%), reflecting both the Strait of Hormuz supply disruption and Beijing's deliberate reduction of purchases amid elevated prices. Yet, by our estimates, crude oil contributed only 1.9pp to headline import growth, little changed from April's 1.8pp. The far larger driver was ICs, which alone contributed 10.8pp to May's import growth, confirming that the semiconductor price shock – rather than energy – remains the primary force behind China's elevated import performance. Growth of imports from South Korea rose further to 84.3% y-o-y in May from 63.4% in April, also signalling the strong tech import momentum.

## The strong value growth of semiconductor trade remained in full force

The ongoing AI-driven global technology supercycle continues to support semiconductor trade, with the price-volume divergence widening further in May.

- Growth of integrated circuit exports in value terms increased to 110.9% y-o-y in May from 99.6% in April, while it slowed further in volume terms to just 2.1% from 3.7%, implying a price contribution of 106.5pp, which represents a significant widening from April's 92.6pp.  
- ICs contributed 5.9pp to headline export growth in May – or 30.4% of the total – with the price effect alone accounting for the vast majority, underscoring the outsized impact that surging chip prices have had on nominal export growth.  
- On the import side, ICs account for a larger share of imports than exports. Growth of IC imports in value terms accelerated sharply to 68.0% y-o-y in May from 54.7% in April, while it turned negative in volume terms, falling to -1.0% (April: 11.2%), with price effects contributing 69.8pp to May growth, in a dramatic widening from April's 39.2pp.  
- By our calculations, ICs alone accounted for 10.8pp of headline May import growth – or 39.4% – with the price effect contributing the overwhelming majority. The sharp increase in the IC import price contribution from April's 39.2pp to May's 69.8pp likely reflected the pass-through of Q2 contract price increases for DRAM and NAND.

Export growth to most destinations remained solid with a further rebound to the US

## Research Analysts

## Asia Economics

Harrington Zhang - NIHK

harrington.zhang@NOM.com

+852 2252 2057

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Hannah Liu - NIHK

hannah.liu@NOM.com

+852 2252 1082

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

Thanks to a substantially low base and less restrictive tariffs, US-bound export growth rebounded further to its highest rate since March 2021. Export growth to most other destinations remained robust. On DM, export growth to the EU slowed modestly to $7.3\%$ y-o-y in May from $13.6\%$ in April, while export growth to Japan quickened to $10.7\%$ y-o-y from $4.2\%$ . Amid the semiconductor supercycle and deep processing trade along regional supply chains, export growth to South Korea accelerated to $42.7\%$ y-o-y in May from $25.2\%$ in April. On EM, export growth to ASEAN, India and Russia increased to $24.7\%$ y-o-y, $19.3\%$ and $39.3\%$ , respectively, in May from $15.6\%$ , $18.7\%$ and $25.9\%$ in April.

## Growth of both exports and imports with the US rebounded further

Export growth to the US rebounded further to $37.3\%$ y-o-y in May from $11.1\%$ in April, marking the highest reading since March 2021, thanks to the tariff-led low base, a temporary net tariff reduction and the domestic AI boom in the US.

- First, due to the unprecedented tariff war in early April 2025, export growth to the US slumped to -20.9% y-o-y in April and -35.2% in May 2025 from 8.8% March and 4.5% in Q1 2025, resulting in favourable base effects for this year.  
- Second, in late February 2026, the US Supreme Court struck down IEEPA-based tariffs (including the $10\%$ reciprocal baseline tariff and the $10\%$ fentanyl tariff); so following the Supreme Court ruling, the Trump administration immediately imposed a new $10\%$ temporary tariff based on the Section 122. Based on our estimates, following the termination of IEEPA-related tariffs and the imposition of Section 122 tariffs in late February, the effective US tariff rate on China dropped to $27.7\%$ in March. In mid-May, the US Treasury Secretary Scott Bessent confirmed that China in recent months has faced lower tariff rates due to US Supreme Court's decision striking down President Trump's global emergency duties, according to Reuters.

Import growth from the US also rebounded further to $20.4\%$ y-o-y in May from $9.0\%$ in April, thanks to a low base. Although May data on the amount of soybean imports from the US have not yet been released, overall soybean import growth in value terms plunged to $-10.3\%$ y-o-y in May from $49.3\%$ in April. As a result, China's trade surplus with the US widened to USD26.0bn in May from USD23.1bn in April and USD18.0bn in May 2025.

## Recent tariff policy developments

On 2 June, the Trump administration announced new Section 301 tariffs of $10.0 - 12.5\%$ on 60 trade partners, with $12.5\%$ on China, largely aimed at replicating the IEEPA tariff framework after Section 122 tariffs expire on 24 July. Our US economics team views the move mainly as an effort to preserve continuity in the trade regime rather than a meaningful escalation, and their estimate for the terminal effective tariff rate remains unchanged at $8 - 9\%$ . In our view, exporters might rush to frontload exports to the US in anticipation of likely higher tariffs in H2. However, according to the Ministry of Commerce, the US will likely keep its tariffs on China from exceeding the level agreed upon in Kuala Lumpur, which is around $30\%$ . Moreover, the new Board of Trade will likely reciprocally lower tariffs on about USD30bn worth of non-sensitive goods, which account for about $10\%$ of China's exports to the US in 2025.

## Surging export growth in electrical products

Export growth of electronic products in value terms continued to surge amid the global AI upcycle, primarily driven by price effects rather than real volumes. Growth of integrated circuit exports surged further to $111.0\%$ y-o-y in May from $100.0\%$ in April, as global chip prices remained elevated. Export growth of automatic data processing (ADP) equipment and components (mainly computers and parts thereof) rose to $66.1\%$ y-o-y in May from $46.9\%$ in April. Growth of mobile phone exports jumped to $43.9\%$ y-o-y in May from $11.0\%$ in April, which was also driven by price effect due to surging input costs.

On transport equipment, growth of auto exports (including chassis) remained elevated at $39.3\%$ y-o-y in May, though down slightly from $43.9\%$ April. Growth of auto spare part exports declined to $5.1\%$ y-o-y in May from $6.6\%$ in April. Growth of ship exports rebounded sharply to $29.7\%$ y-o-y in May from $-15.0\%$ in April.

Export growth of some labor-intensive products broadly improved on the margin but remained negative in May. In particular, export growth of clothing, shoes, bags and toys came in at -4.1% y-o-y, -10.3%, -4.9% and -7.0%, respectively, in May from -2.2%, -17.1%, -11.4% and -12.4%, in April.

## Import growth remained elevated amid surging energy and chip prices

Import growth remained elevated at $27.4\%$ in May, up from $25.3\%$ in April and above market expectations (Consensus and NOM: 26.0%), driven by price effects from energy and AI-related tech products. On crude oil imports, its value growth climbed to 15.3% y-o-y in May from 13.2% in April, purely driven by surging global oil prices. In volume terms, however, it dipped further to -29.0% y-o-y in May from -20.0% in April.

For other types of imports, non-oil ordinary imports value growth was largely unchanged at 12.1% y-o-y in May, (April: 12.5%). Value growth of processing and assembly imports, which are more AI-related, surged further to 44.9% y-o-y in May from 34.8% in April, amid rising prices of AI-related products, including memory chips. Growth of integrated circuits in value terms surged further to 68.3% y-o-y in May from 54.6% in April, while in volume terms it turned negative, falling to -1.1% y-o-y from 11.3%.

Import volume growth for other key commodities were mixed. Volume growth of copper and coal improved to $3.6\%$ y-o-y and $-7.7\%$ , respectively, in May from $2.3\%$ and $-12.6\%$ in April. Volume growth of iron ore ticked down to $-0.4\%$ y-o-y in May from $0.7\%$ in April. Volume growth of soybeans plunged to $-15.3\%$ y-o-y in May from $41.0\%$ in April.

Fig. 1: Merchandise trade related indicators

<table><tr><td>Merchandise trade related indicators</td><td>May 26</td><td>Apr 26</td><td>Mar 26</td><td>Q1 26</td><td>2025</td><td>2024</td></tr><tr><td>Exports (% y-o-y)</td><td>19.4</td><td>14.1</td><td>2.5</td><td>14.7</td><td>5.5</td><td>5.8</td></tr><tr><td>By destination: the US</td><td>37.3</td><td>11.1</td><td>-26.0</td><td>-16.3</td><td>-20.0</td><td>4.9</td></tr><tr><td>European Union</td><td>7.3</td><td>13.6</td><td>8.9</td><td>21.1</td><td>8.4</td><td>3.0</td></tr><tr><td>Japan</td><td>10.7</td><td>4.2</td><td>3.5</td><td>6.9</td><td>3.5</td><td>-3.5</td></tr><tr><td>ASEAN</td><td>24.7</td><td>15.6</td><td>7.9</td><td>20.5</td><td>13.4</td><td>12.0</td></tr><tr><td>Imports (% y-o-y)</td><td>27.4</td><td>25.3</td><td>28.1</td><td>23.0</td><td>0.2</td><td>1.0</td></tr><tr><td>By origin: the US</td><td>20.8</td><td>10.5</td><td>1.1</td><td>-17.6</td><td>-14.6</td><td>-0.1</td></tr><tr><td>By type of trade:</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ordinary imports</td><td>12.5</td><td>12.8</td><td>16.8</td><td>11.8</td><td>-4.2</td><td>-3.1</td></tr><tr><td>Non-oil ordinary imports</td><td>12.1</td><td>12.5</td><td>23.3</td><td>16.4</td><td>-3.1</td><td>-2.8</td></tr><tr><td>Crude oil imports</td><td>15.3</td><td>13.2</td><td>-4.4</td><td>-4.7</td><td>-8.8</td><td>-3.9</td></tr><tr><td>Processing &amp; assembly imports</td><td>44.9</td><td>34.8</td><td>43.8</td><td>34.8</td><td>11.9</td><td>5.7</td></tr><tr><td>Commodities, in volume terms</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Crude oil</td><td>-29.0</td><td>-20.0</td><td>-2.8</td><td>8.9</td><td>4.4</td><td>-1.9</td></tr><tr><td>Iron ore</td><td>-0.4</td><td>0.7</td><td>11.5</td><td>10.5</td><td>1.8</td><td>4.9</td></tr><tr><td>Copper</td><td>3.6</td><td>2.3</td><td>-10.6</td><td>-14.2</td><td>-6.4</td><td>3.4</td></tr><tr><td>Coal</td><td>-7.7</td><td>-12.6</td><td>0.9</td><td>1.3</td><td>-9.6</td><td>14.4</td></tr><tr><td>Soybeans</td><td>-15.3</td><td>41.0</td><td>15.1</td><td>-3.1</td><td>6.5</td><td>5.7</td></tr><tr><td>Trade balance (USD bn)</td><td>105</td><td>85</td><td>51</td><td>263</td><td>1183</td><td>993</td></tr><tr><td>By destination: the US</td><td>26</td><td>23</td><td>17</td><td>65</td><td>280</td><td>361</td></tr></table>

Source: General Administration of Customs, Wind, NOM Global Economics

Fig. 2: Export by key product

<table><tr><td rowspan="2">Major export goods (in USD terms)</td><td>May 26</td><td>Apr 26</td><td>Q1 26</td><td>2025</td><td>2024</td><td>May 26</td></tr><tr><td colspan="5">y-o-y, %</td><td>Contribution to export growth (pp)</td></tr><tr><td>Vehicle</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Motor vehicles and chassis</td><td>39.3</td><td>43.9</td><td>58.5</td><td>21.4</td><td>15.5</td><td>1.49</td></tr><tr><td>Automobile spare parts</td><td>5.1</td><td>6.6</td><td>4.7</td><td>2.5</td><td>6.6</td><td>0.13</td></tr><tr><td>Electrical products</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Automatic data processing equipment and components</td><td>66.1</td><td>46.9</td><td>26.7</td><td>-1.4</td><td>9.9</td><td>3.38</td></tr><tr><td>Integrated circuits</td><td>111.0</td><td>100.0</td><td>77.5</td><td>26.6</td><td>17.3</td><td>5.91</td></tr><tr><td>Mobile phones</td><td>43.9</td><td>11.0</td><td>-4.7</td><td>-9.4</td><td>-3.2</td><td>0.95</td></tr><tr><td>Audio-video equipment and parts</td><td>19.1</td><td>8.2</td><td>13.2</td><td>5.5</td><td>4.6</td><td>0.19</td></tr><tr><td>Liquid crystal display panels</td><td>-5.2</td><td>-3.4</td><td>15.3</td><td>11.0</td><td>9.0</td><td>-0.05</td></tr><tr><td>Mechanical products</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Universal mechanical equipment</td><td>2.4</td><td>-3.4</td><td>7.1</td><td>6.1</td><td>14.2</td><td>0.04</td></tr><tr><td>Ships</td><td>29.7</td><td>-15.0</td><td>48.7</td><td>27.0</td><td>57.3</td><td>0.39</td></tr><tr><td>Medical devices</td><td>17.3</td><td>14.9</td><td>11.5</td><td>6.0</td><td>7.0</td><td>0.09</td></tr><tr><td>Property-related products</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Ceramic products</td><td>-53.2</td><td>-55.9</td><td>9.2</td><td>-3.3</td><td>-15.7</td><td>-0.35</td></tr><tr><td>Home electric appliances</td><td>9.5</td><td>7.2</td><td>1.5</td><td>-3.9</td><td>14.0</td><td>0.25</td></tr><tr><td>Lighting and parts</td><td>-11.8</td><td>-19.7</td><td>-5.3</td><td>-12.4</td><td>-0.2</td><td>-0.13</td></tr><tr><td>Furniture and parts</td><td>1.9</td><td>-3.7</td><td>3.0</td><td>-6.2</td><td>5.7</td><td>0.03</td></tr><tr><td>Commodities &amp; industrial products</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Steel products</td><td>-2.3</td><td>-8.3</td><td>-10.8</td><td>-1.3</td><td>-1.1</td><td>-0.05</td></tr><tr><td>Unwrought aluminum and aluminum products</td><td>38.4</td><td>31.5</td><td>16.5</td><td>-3.3</td><td>15.2</td><td>0.23</td></tr><tr><td>Petroleum products</td><td>35.6</td><td>8.3</td><td>3.6</td><td>-8.5</td><td>-13.3</td><td>0.32</td></tr><tr><td>Rare earth</td><td>237.4</td><td>196.5</td><td>-9.0</td><td>4.6</td><td>-36.0</td><td>0.01</td></tr><tr><td>Agricultural products</td><td>5.1</td><td>3.8</td><td>5.3</td><td>1.1</td><td>4.1</td><td>0.14</td></tr><tr><td>Aquatic products</td><td>-1.2</td><td>0.9</td><td>-3.8</td><td>0.0</td><td>1.3</td><td>-0.01</td></tr><tr><td>Grain</td><td>-25.5</td><td>-13.9</td><td>8.8</td><td>27.3</td><td>-18.9</td><td>-0.02</td></tr><tr><td>Fertilizers</td><td>7.5</td><td>46.0</td><td>22.6</td><td>57.9</td><td>-11.5</td><td>0.02</td></tr><tr><td>Chinese herbs &amp; medicines</td><td>-1.2</td><td>9.1</td><td>10.8</td><td>-7.2</td><td>-0.4</td><td>0.00</td></tr><tr><td>Labor intensive products</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Plastic products</td><td>12.7</td><td>8.0</td><td>7.5</td><td>-1.4</td><td>5.2</td><td>0.37</td></tr><tr><td>Bags &amp; containers</td><td>-4.9</td><td>-11.4</td><td>-1.1</td><td>-13.5</td><td>-3.3</td><td>-0.05</td></tr><tr><td>Garments and clothing accessories</td><td>-4.1</td><td>-2.2</td><td>-0.4</td><td>-5.0</td><td>0.0</td><td>-0.18</td></tr><tr><td>Footwear</td><td>-10.3</td><td>-17.1</td><td>-8.0</td><td>-11.3</td><td>-5.0</td><td>-0.13</td></tr><tr><td>Toys</td><td>-7.0</td><td>-12.3</td><td>-14.8</td><td>-12.7</td><td>-1.7</td><td>-0.07</td></tr><tr><td>Textile, yarn and fabrics</td><td>-0.3</td><td>1.0</td><td>2.8</td><td>0.4</td><td>5.5</td><td>-0.01</td></tr><tr><td>Electrical-mechanical products</td><td>27.4</td><td>20.3</td><td>21.4</td><td>8.3</td><td>7.4</td><td>16.40</td></tr><tr><td>Hi-tech products</td><td>51.0</td><td>39.1</td><td>28.6</td><td>7.4</td><td>4.7</td><td>12.00</td></tr></table>

Note: Key products are recombined items by HS code. Agricultural, electronic-mechanical and high-tech products are broader categories that may overlap with each other and other key products.  
Source: General Administration of Customs, NOM Global Economics.

Fig. 3: Export growth, import growth and the trade balance  
![](images/ab6f27526178f94c8deb1306d70cc80217069ffa195ef5d1c4ff94c2859fd4db.jpg)

<details>
<summary>line chart</summary>

| Date   | Trade balance (rhs) | Imports | Exports |
|--------|---------------------|---------|---------|
| Jan-18 | ~15                 | ~20     | ~10     |
| Jan-19 | ~20                 | ~25     | ~5      |
| Jan-20 | ~30                 | ~10     | ~0      |
| Jan-21 | ~40                 | ~50     | ~50     |
| Jan-22 | ~60                 | ~30     | ~20     |
| Jan-23 | ~70                 | ~10     | ~-10    |
| Jan-24 | ~60                 | ~5      | ~-5     |
| Jan-25 | ~70                 | ~10     | ~5      |
| Jan-26 | ~75                 | ~25     | ~20     |
</details>

Note: We use the average of January-March data to largely smooth out the CNY distortions.  
Source: General Administration of Customs, Wind, NOM Global Economics

Fig. 5: Growth of integrated circuit imports rose to $68\%$ y-o-y in April, with a sharp divergence be

[中间内容因长度限制已省略]

34. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
