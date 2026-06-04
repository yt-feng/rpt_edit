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
# Japan Technology: IT Services: NC company results read-across (3) Cybersecurity: Techmatrix, Digital Arts

In this report, we consider the implications for our IT services sector coverage from visits we made to two Not Covered companies, security vendors Techmatrix (network security/in-car software verification tools/medical cloud) and Digital Arts (network security/Web filtering software). Techmatrix's new consolidation of Medmain, which provides AI software and cloud services for pathological diagnosis support, resulted in its FY3/27 operating profit guidance being set below the target in the medium-term plan, and once the amortization of its intangible fixed assets is finalized, the company expects the consolidation to depress near-term earnings. While security in the information infrastructure business continues to perform well, other businesses continue to be a drag on earnings. For Digital Arts, the competitive environment for GIGA school software has intensified sharply, leading to a decline in market share, and its FY3/27 operating profit guidance is well below the target in the medium-term plan. While earnings continue to lag targets, the company is also seeing tailwinds such as expanding demand ahead of the security measures evaluation system that the Ministry of Economy, Trade and Industry (METI) plans to introduce.

In terms of read-across, security-related demand is robust overall, which is a tailwind for the domestic earnings of Trend Micro (Neutral), which is strong in this field. Additionally, increased investment spurred by the security measures evaluation system should also be a positive for the earnings of Otsuka (Sell), which handles related products. Below we outline our key takeaways from company commentary. (See earnings tables at Exhibit 2/Exhibit 3/Exhibit 4.)

## Techmatrix (3762.T) (network security/medical)

(1) Guidance: FY3/27 operating profit guidance calls for ¥8.2 bn (+6% yoy), below the target in the medium-term plan (¥8.6 bn). This is largely due to the new consolidation of Medmain, which provides AI software and cloud services for pathological diagnosis support (planned for consolidation from 1Q, with Techmatrix expecting this to depress operating profits by -¥0.4 bn). By segment, the company looks for a +10% yoy increase in operating profits in the information infrastructure business (security), where demand is strong. The struggling application services business is guided to improve by +¥0.35 bn yoy and return to profitability. The medical systems business, which will be impacted by Medmain's consolidation, is forecast to see a -43% yoy decline in profits. The company assumes one-off factors will depress profits by just over ¥100 mn yoy

Chikai Tanaka, CFA

+81(3)4587-9840

chikai.tanaka@gs.com

GS Japan Co., Ltd.

Yuki Sato

+81(3)4587-8536 | yuki.z.sato@gs.com

GS Japan Co., Ltd.

on net, namely the drop-out of impacts from a sales booking omission (which boosted 4Q3/26 operating profits by +¥166 mn in information infrastructure) and a revision of retirement benefit expenses (-¥50 mn impact in 4Q3/26). Additionally, losses are guided to narrow by a few hundred million yen in the Ed Tech business (systems for schools and the education industry), but the company forecasts it will remain in the red for now (and turn an operating profit in the latter half of the next medium-term plan).

(2) Information infrastructure business: 4Q3/26 operating profits rose by +48% yoy, and by +35% yoy on an underlying basis excluding the one-off factor of the sales booking omission. Growth has been driven by next-generation firewalls from US-based Palo Alto Networks, SOC (Security Operation Center) automation solutions, and mail security products from US-based Proofpoint (4Q order value rose +10% yoy; Exhibit 1). In addition, management noted the standalone recurring sales ratio (in FY3/26) was 88%, enhancing earnings stability. FY3/27 operating profit guidance is for ¥7.24 bn (solid growth of +10% yoy). As the company’s main products are mostly cloud-based, it is less susceptible to the impact of rising memory prices and longer parts procurement lead times. Storage products, which could be affected, account for a minor portion of sales in this business (less than 3%), and management said there has been no impact so far.  
(3) Medical systems business: FY3/27 operating profit guidance is for ¥0.76 bn (-43%/-¥0.57 bn yoy). The main reasons for the anticipated decline are the impact of the new consolidation of Medmain (a profit drag of c.¥0.4 bn), a temporary decrease in sales due to the shift from on-premise to cloud systems, and an increase in development investment for cloud services. According to the company, (a) Medmain is in an upfront investment phase and will probably take about five years to turn a profit, and (b) as PPA has not been completed, the amortization expense for intangible fixed assets has not been finalized (it is not included in guidance, and will be a downside factor for targets once finalized).

Exhibit 1: Firewalls, mail security, and software quality assurance driving growth  
Techmatrix: Information infrastructure and application services businesses: Sales growth by product (yoy; cumulative basis)

<table><tr><td rowspan="2">Sales growth rate (y-y)</td><td colspan="4">25/3</td><td colspan="4">26/3</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td></tr><tr><td colspan="9"></td></tr><tr><td>Load balancers</td><td>5%~10%</td><td>5%~10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>-5%~+5%</td></tr><tr><td>Next-Generation Firewall etc</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>&gt;10%</td><td>&gt;10%</td></tr><tr><td>Antivirus etc</td><td>-5%~+5%</td><td>-5%~+5%</td><td>-5%~+5%</td><td>-5%~+5%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td></tr><tr><td>Storage products</td><td>-5%~-10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>&gt;10%</td><td>&lt;-10%</td><td>&lt;-10%</td><td>&lt;-10%</td></tr><tr><td>Security-related operation &amp; monitoring</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>&lt;-10%</td><td>&lt;-10%</td><td>-5%~-10%</td><td>-5%~+5%</td></tr><tr><td>Next-Generation Mail security</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td></tr><tr><td colspan="9"></td></tr><tr><td>Business Solution field</td><td>&gt;10%</td><td>&gt;10%</td><td>-5%~+5%</td><td>-5%~+5%</td><td>-5%~-10%</td><td>-5%~-10%</td><td>-5%~+5%</td><td>5%~10%</td></tr><tr><td>Software Quality Assurance field</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td></tr><tr><td>CRM field</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>5%~10%</td><td>5%~10%</td><td>-5%~+5%</td></tr><tr><td>EdTech field</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td><td>5%~10%</td><td>&gt;10%</td><td>&gt;10%</td><td>&gt;10%</td></tr></table>

Source: Company data, Data compiled by GS Global Investment Research

## Digital Arts (2326.T) (network security)

(1) Results: FY3/26 operating profits came to ¥4.79 bn (+5% yoy), substantially missing guidance (¥5.61 bn). The main reasons cited were a decline in share for GIGA school projects amid intensified price competition with rivals, a reduction in the size of public sector projects due to changes in procurement policy (from multi-year to single-year contracts), and a delay in sales recognition due to an increasing cloud ratio. According to management, all of these factors are ongoing.

(2) Guidance: FY3/27 operating profit guidance is for ¥5.4 bn (+13% yoy), which is well below the target in the medium-term plan (¥7.8 bn). The main reasons are the same as for the underperformance in FY3/26. On a yoy basis, although communication costs (AWS server fees) are expected to increase with the rising cloud ratio, the company expects double-digit % profit growth due to greater demand for GIGA school and school DX projects, a full-year contribution from the new Z-FILTER product, and operational efficiencies from AI.

(3) Public business: Order value (contract value) for GIGA school projects is on an upward trend, but it missed company expectations in 4Q3/26. Until 3Q, the company had a dominant market share due to its technological lead, but in 4Q, several competitors launched an offensive with prices at about half of the company's, resulting in a decline in cumulative market share from $95\%$ (at end-3Q) to $70\%$ (at end-4Q). Management said the cumulative market share assumption for end-FY3/27 is $70\%$ , which is higher than the level in the first GIGA school phase $(53\%)$ , and the company will need to acquire new customers. Digital Arts thinks competitors' price offensive may continue, so it also plans to propose slightly lower-than-usual prices to some customers.

(4) Enterprise business: 4Q3/26 sales grew by just +1% yoy, hampered by a decline in on-premise sales. FY3/27 sales guidance is for a +10% yoy increase, with growth expected for the new Z-FILTER product. Z-FILTER has many more functions than i-FILTER (firewall/antivirus, etc.), and while the monthly unit price is set at 3-4x the previous level, it is cheaper than products from foreign vendors and is competitive. Per the company, the contract value pipeline is c.¥1 bn, mainly from existing customers, of which it expects ¥0.9 bn to be booked in FY3/27. While not factored into plans, the company noted that corporate security investment is highly likely to expand ahead of the security measures evaluation system that METI plans to introduce, and that this could become a tailwind for a range of its products.

Exhibit 2: Techmatrix (3762.T): Earnings by segment

<table><tr><td rowspan="2">(mn yen) Techmatrix (3762)</td><td rowspan="2">24/3</td><td rowspan="2">25/3</td><td rowspan="2">26/3</td><td rowspan="2">CoE 27/3E</td><td colspan="4">26/3</td></tr><tr><td>Q1</td><td>Q2</td><td>Q3</td><td>Q4</td></tr><tr><td>Order</td><td>68,446</td><td>82,866</td><td>89,009</td><td></td><td>20,544</td><td>23,098</td><td>21,261</td><td>24,106</td></tr><tr><td>yoy</td><td>15.1%</td><td>21.1%</td><td>7.4%</td><td></td><td>-5.2%</td><td>7.5%</td><td>20.9%</td><td>8.9%</td></tr><tr><td>Order Backlog</td><td>68,566</td><td>88,155</td><td>105,431</td><td></td><td>92,836</td><td>98,420</td><td>102,073</td><td>105,431</td></tr><tr><td>yoy</td><td>30.8%</td><td>28.6%</td><td>19.6%</td><td></td><td>21.4%</td><td>21.7%</td><td>21.3%</td><td>19.6%</td></tr><tr><td>Sales</td><td>53,303</td><td>64,882</td><td>71,734</td><td>81,800</td><td>15,863</td><td>17,514</td><td>17,608</td><td>20,748</td></tr><tr><td>yoy</td><td>16.0%</td><td>21.7%</td><td>10.6%</td><td>14.0%</td><td>15.3%</td><td>2.6%</td><td>10.8%</td><td>14.3%</td></tr><tr><td>Gross Profit</td><td>18,203</td><td>20,555</td><td>22,575</td><td></td><td>4,931</td><td>5,562</td><td>5,562</td><td>6,521</td></tr><tr><td>yoy</td><td>11.2%</td><td>12.9%</td><td>9.8%</td><td></td><td>14.8%</td><td>5.3%</td><td>7.0%</td><td>12.9%</td></tr><tr><td>% of sales</td><td>34.1%</td><td>31.7%</td><td>31.7%</td><td></td><td>31.1%</td><td>31.8%</td><td>31.6%</td><td>31.4%</td></tr><tr><td>SGA</td><td>12,310</td><td>13,561</td><td>14,829</td><td></td><td>3,659</td><td>3,667</td><td>3,652</td><td>3,851</td></tr><tr><td>yoy</td><td>10.2%</td><td>10.2%</td><td>9.4%</td><td></td><td>14.6%</td><td>9.4%</td><td>6.6%</td><td>7.3%</td></tr><tr><td>% of sales</td><td>23.1%</td><td>20.9%</td><td>20.7%</td><td></td><td>23.1%</td><td>20.9%</td><td>20.7%</td><td>18.6%</td></tr><tr><td>Other sales</td><td>24</td><td>38</td><td>35</td><td></td><td>3</td><td>9</td><td>15</td><td>8</td></tr><tr><td>Other costs</td><td>67</td><td>363</td><td>21</td><td></td><td>0</td><td>3</td><td>2</td><td>15</td></tr><tr><td>Operating Profits</td><td>5,850</td><td>6,668</td><td>7,760</td><td>8,200</td><td>1,274</td><td>1,901</td><td>1,922</td><td>2,663</td></tr><tr><td>yoy</td><td>14.7%</td><td>14.0%</td><td>16.4%</td><td>5.7%</td><td>14.4%</td><td>-0.5%</td><td>8.1%</td><td>42.6%</td></tr><tr><td>% of sales</td><td>11.0%</td><td>10.3%</td><td>10.8%</td><td>10.0%</td><td>8.0%</td><td>10.9%</td><td>10.9%</td><td>12.8%</td></tr><tr><td colspan="5"></td><td colspan="4"></td></tr><tr><td colspan="5">I Information Infrastructure Business</td><td colspan="4"></td></tr><tr><td>Order</td><td>47,652</td><td>60,482</td><td>64,134</td><td></td><td>14,878</td><td>16,928</td><td>16,024</td><td>16,304</td></tr><tr><td>yoy</td><td>17.3%</td><td>26.9%</td><td>6.0%</td><td></td><td>-8.6%</td><td>3.6%</td><td>22.5%</td><td>10.3%</td></tr><tr><td>Order Backlog</td><td>49,861</td><td>66,366</td><td>78,880</td><td></td><td>69,746</td><td>73,943</td><td>77,153</td><td>78,880</td></tr><tr><td>yoy</td><td>34.0%</td><td>33.1%</td><td>18.9%</td><td></td><td>23.4%</td><td>22.4%</td><td>21.0%</td><td>18.9%</td></tr><tr><td>External Sales</td><td>35,006</td><td>45,586</td><td>51,620</td><td>59,500</td><td>11,498</td><td>12,731</td><td>12,814</td><td>14,577</td></tr><tr><td>yoy</td><td>19.5%</td><td>30.2%</td><td>13.2%</td><td>15.3%</td><td>19.7%</td><td>2.3%</td><td>12.6%</td><td>19.9%</td></tr><tr><td>% of sales</td><td>65.7%</td><td>70.3%</td><td>72.0%</td><td>72.7%</td><td>72.5%</td><td>72.7%</td><td>72.8%</td><td>70.3%</td></tr><tr><td>Operating Profits</td><td>3,973</td><td>5,274</td><td>6,580</td><td>7,240</td><td>1,257</td><td>1,670</td><td>1,715</td><td>1,938</td></tr><tr><td>yoy</td><td>28.6%</td><td>32.7%</td><td>24.8%</td><td>10.0%</td><td>33.6%</td><td>3.2%</td><td>21.9%</td><td>48.2%</td></tr><tr><td>% of sales</td><td>11.3%</td><td>11.5%</td><td>12.7%</td><td>12.2%</td><td>10.9%</td><td>13.1%</td><td>13.3%</td><td>13.2%</td></tr><tr><td colspan="5">II Application Service Business</td><td colspan="4"></td></tr><tr><td>Order</td><td>9,074</td><td>9,924</td><td>10,938</td><td></td><td>2,789</td><td>2,487</td><td>2,146</td><td>3,516</td></tr><tr><td>yoy</td><td>16.3%</td><td>9.4%</td><td>10.2%</td><td></td><td>5.6%</td><td>14.1%</td><td>15.5%</td><td>8.4%</td></tr><tr><td>Order Backlog</td><td>5,327</td><td>6,071</td><td>7,125</td><td></td><td>6,558</td><td>6,631</td><td>6,347</td><td>7,125</td></tr><tr><td>yoy</td><td>19.5%</td><td>14.0%</td><td>17.4%</td><td></td><td>11.8%</td><td>15.1%</td><td>16.8%</td><td>17.4%</td></tr><tr><td>External Sales</td><td>8,205</td><td>9,177</td><td>9,884</td><td>11,130</td><td>2,302</td><td>2,414</td><td>2,430</td><td>2,738</td></tr><tr><td>yoy</td><td>12.4%</td><td>11.8%</td><td>7.7%</td><td>12.6%</td><td>9.5%</td><td>5.7%</td><td>11.2%</td><td>5.0%</td></tr><tr><td>% of sales</td><td>15.4%</td><td>14.1%</td><td>13.8%</td><td>13.6%</td><td>14.5%</td><td>13.8%</td><td>13.8%</td><td>13.2%</td></tr><tr><td>Operating Profits</td><td>317</td><td>142</td><td>-148</td><td>200</td><td>-45</td><td>-9</td><td>-53</td><td>-42</td></tr><tr><td>yoy</td><td>22.4x</td><td>-55.4%</td><td>N.M.</td><td>N.M.</td><td>N.M.</td><td>N.M.</td><td>N.M.</td><td>N.M.</td></tr><tr><td>% of sales</td><td>3.7%</td><td>1.5%</td><td>-1.5%</td><td>1.8%</td><td>-1.9%</td><td>-0.3%</td><td>-2.1%</td><td>-1.5%</td></tr><tr><td colspan="5">III Medical Systems Business</td><td colspan="4"></td></tr><tr><td>Order</td><td>11,719</td><td>12,459</td><td>13,936</td><td></td><td>2,876</td><td>3,685</td><td>3,090</td><td>4,285</td></tr><tr><td>yoy</td><td>6.3%</td><td>6.3%</td><td>11.9%</td><td></td><td>5.0%</td><td>23.7%</td><td>17.0%</td><td>4.5%</td></tr><tr><td>Order Backlog</td><td>13,377</td><td>15,717</td><td>19,425</td><td></td><td>16,531</td><td>17,846</td><td>18,572</td><td>19,425</td></tr><tr><td>yoy</td><td>24.6%</td><td>17.5%</td><td>23.6%</td><td></td><td>17.5%</td><td>21.5%</td><td>23.8%</td><td>23.6%</td></tr><tr><td>External Sales</td><td>10,092</td><td>10,119</td><td>10,229</td><td>11,170</td><td>2,062</td><td>2,370</td><td>2,364</td><td>3,433</td></tr><tr><td>yoy</td><td>8.0%</td><td>0.3%</td><td>1.1%</td><td>9.2%</td><td>0.4%</td><td>0.6%</td><td>1.7%</td><td>1.4%</td></tr><tr><td>% of sales</td><td>18.9%</td><td>15.6%</td><td>14.3%</td><td>13.7%</td><td>13.0%</td><td>13.5%</td><td>13.4%</td><td>16.5%</td></tr><tr><td>Operating Profits</td><td>1,560</td><td>1,253</td><td>1,329</td><td>760</td><td>63</td><td>239</td><td>260</td><td>767</td></tr><tr><td>yoy</td><td>-21.8%</td><td>-19.7%</td><td>6.1%</td><td>-42.8%</td><td>-42.7%</td><td>22.5%</td><td>7.6%</td><td>8.5%</td></tr><tr><td>% of sales</td><td>15.5%</td><td>12.4%</td><td>8.8%</td><td>9.6%</td><td>3.0%</td><td>10.1%</td><td>11.0%</td><td>22.3%</td></tr></table>

Operating profits by business include internal transactions  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 3: Digital Arts (2326.T): Earnings by segment

<table><tr><td>(mn yen)Digital Arts (2326)</td><td>24/3</td><td>25/3</td><td>26/3</td><td>CoE27/3E</td><td>26/3Q1</td><td>Q2</td><td>Q3</td><td>Q4</td></tr><tr><td>Contracts</td><td>10,838</td><td>10,570</td><td>16,604</td><td>13,500</td><td>2,306</td><td>4,323</td><td>4,246</td><td>5,729</td></tr><tr><td>yoy</td><td>6.4%</td><td>-2.5%</td><td>57.1%</td><td>-18.7%</td><td>15.7%</td><td>71.3%</td><td>81.3%</td><td>54.3%</td></tr><tr><td>yoy excl. effects of DAC deconsolidation</td><td></td><td>22.3%</td><td>-</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>License Products and Others</td><td>7,479</td><td>5,373</td><td>5,192</td><td></td><td>927</td><td>1,313</td><td>1,451</td><td>1,501</td></tr><tr><td>yoy</td><td>10.1%</td><td>-28.2%</td><td>-3.4%</td><td></td><td>-14.6%</td><td>-10.1%</td><td>17.7%</td><td>-5.8%</td></tr><tr><td>Cloud Service Products</td><td>3,359</td><td>5,197</td><td>11,412</td><td></td><td>1,379</td><td>3,009</td><td>2,795</td><td>4,229</td></tr><tr><td>yoy</td><td>-1.1%</td><td>54.7%</td><td>119.6%</td><td></td><td>52.2%</td><td>183.1%</td><td>152.0%</td><td>99.6%</td></tr><tr><td>Order Backlog</td><td>5,651</td><td>6,243</td><td>12,006</td><td></td><td>6,279</td><td>7,903</td><td>9,286</td><td>12,006</td></tr><tr><td>yoy</td><td>-10.6%</td><td>10.5%</td><td>92.3%</td><td></td><td>16.1%</td><td>48.1%</td><td>77.1%</td><td>92.3%</td></tr><tr><td>Sales</td><td>11,512</td><td>9,982</td><td>10,835</td><td>12,000</td><td>2,270</td><td>2,722</td><td>2,843</td><td>3,000</td></tr><tr><td>yoy</td><td>10.3%</td><td>-13.3%</td><td>8.5%</td><td>10.8%</td><td>1.6%</td><td>4.5%</td><td>16.7%</td><td>10.8%</td

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
