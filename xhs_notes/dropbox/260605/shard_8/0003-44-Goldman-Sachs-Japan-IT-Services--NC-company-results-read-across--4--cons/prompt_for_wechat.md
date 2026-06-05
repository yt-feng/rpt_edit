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
# Japan IT Services: NC company results read-across (4) consulting/cloud: Future, SIGMAXYZ, Comture

In this report, we consider the implications for our IT services sector coverage from visits we made to three Not Covered companies (we have no investment views on these companies): Future (consulting/SI), SIGMAXYZ (consulting), and Comture (cloud integrator). Future is tracking in line with guidance, but conditions remain tough on an underlying basis, excluding one-time gains (initial licensing fees for its next-generation banking system). The company noted that new client acquisitions for its next-generation banking system are running slightly below internal assumptions. At SIGMAXYZ, multiple core system renewal (SaaS) projects have peaked out, and the consultant utilization rate is on a yoy downtrend as a result. While FY3/27 operating profit guidance is for an increase, the company expects a project lull to continue in 1H before an earnings recovery in 2H. At Comture, the downtrend in its gross margin still continues due to the impact of wage hikes and delays in passing on costs. Its FY3/26 operating profits missed guidance, and FY3/27 operating profit guidance is for a third consecutive year of modest profit growth, indicating that challenging conditions persist. In terms of read-across, we see expanding demand for shared systems for regional banks as a positive for earnings at BIPROGY (Buy), which has a strong presence in this area. Below, we outline our key takeaways from company commentary (see Exhibit 1/Exhibit 2/Exhibit 3/Exhibit 4 for company earnings).

# Future Corp. (4722.T) (consulting/SI)

(1) 1Q (Jan-Mar) results/2Q outlook: Operating profits came at ¥3.43 bn (+3% yoy), broadly in line with guidance. Growth was modest due to the drop-out of large-scale consulting and maintenance projects. No one-time gains (initial licensing fees for the next-generation banking system) were booked in 1Q. The company left 1H guidance unchanged, implying 2Q operating profit guidance of +2% yoy, but noted that the booking of initial licensing fees for the next-generation banking system could fall short of its assumptions (sales/profits of just under ¥1 bn were booked in 2Q12/25). Future assumes a yoy impact from higher-than-usual wage increases.

(2) Consulting business: 1Q sales increased +7% yoy, but operating profits declined slightly, by -0.4% yoy. On an underlying basis excluding initial licensing fees, this marked the fourth consecutive quarter of yoy operating profit decline, but the rate of decline narrowed substantially. By industry, growth was seen in finance (next-generation banking), services (projects in collaboration with

Chikai Tanaka, CFA

+81(3)4587-9840

chikai.tanaka@gs.com

GS Japan Co., Ltd.

Yuki Sato

+81(3)4587-8536 | yuki.z.sato@gs.com

GS Japan Co., Ltd.

Revamp), and others (for public sector). By phase, upstream processes such as grand design and basic design expanded. A large-scale unprofitable project for the distribution and wholesale sector is progressing as planned, with the current phase scheduled for cutover in July.

(3) Next-generation banking system: Future has acquired six banks as users to date. A large-scale project for the third bank, SBI Shinsei Bank, is currently in the grand design phase. Future said it expects full-scale development to begin in 2H, with cutover from FY12/29 onward. Given the project scale, the company noted that it will take a considerable amount of time, similar to the first and second banks. Acquisition of the seventh and subsequent bank clients is running slightly behind internal assumptions. As such, Future noted that the booking of initial licensing fees for the next-generation banking system in 1H could fall short of its assumptions.

(4) Business innovation business: The 1Q operating loss improved by +¥0.09 bn yoy. This was helped by factors such as improved profitability at Yocabito (an e-commerce business for outdoor/sports goods) following a narrowing of its product lineup. As Yocabito continues to post an operating loss, the company commented that it will consider options including a business transfer after restructuring. Meanwhile, Curiosity (a design studio) lost a large-scale project that had been factored into guidance, and will need to cover this with other projects going forward, according to Future.

# SIGMAXYZ (6088.T) (consulting)

(1) Guidance: FY3/27 operating profit guidance is for ¥6.6 bn (+9% yoy). While consulting demand is currently in a lull, management said it aims for profit growth centered on 2H. According to the company, (a) conditions will be tough through 1H due to the impact of the peak-out of large-scale projects for major clients, as well as the drop-out in 1Q (Apr-Jun) of one-time gains (a ¥0.2 bn reversal of bonus provisions), but it expects an earnings recovery in 2H once these impacts have run their course; (b) there has been no weakening of client investment appetite due to the situation in the Middle East, and the possibility of a future deterioration is not factored into guidance, but it needs to keep a close watch on developments as it has major clients in the air and marine transport sectors.

(2) Consulting: Sales in 4Q3/26 declined -15% yoy, with sales to the top 10 clients down -35% yoy; both marked a third consecutive quarter of negative growth. Multiple core system renewal (SaaS) projects have peaked out, and as a result the utilization rate is in a yoy downtrend (the 4Q utilization rate was 70%, down -6 pp yoy). The company believes this trend could continue through 1H3/27. However, it noted that inquiries are on a recovery trend, centered on core system renewal projects, with particularly strong demand for AI consulting, such as data infrastructure development and AI utilization.

(3) Potential capital and business alliance: The company announced that it has begun considering a capital and business alliance with Core Concept Technologies (4371.T). Core Concept Technologies is a DX support and IT staffing company focused on mid-sized enterprises, with a strong presence in the manufacturing

sector. It does not engage in consulting, and therefore SIGMAXYZ believes it could have a complementary relationship with its own business, making it easy to create synergies. SIGMAXYZ's current equity stake in the company is $10.64\%$ , but it has stated its intention to raise its voting rights ratio to a level that would allow for equity-method accounting by the end of March 2027.

# Comture Corp. (3844.T) (cloud)

(1) Results: FY3/26 operating profits were ¥4.66 bn (+1% yoy), well below guidance (¥5.0 bn). This was largely due to sluggish demand for the core cloud solutions business, coupled with a greater-than-expected deterioration in profitability on account of a lack of progress with cost pass-throughs. On a yoy basis, although SG&A expenses were curbed by personnel adjustments in indirect departments, profit growth was modest due to headwinds such as a decline in the gross margin (-1.3 pp yoy) from wage hikes. However, on a quarterly basis, 4Q (Jan-Mar) saw a +7% yoy increase in operating profits, with some signs of recovery centered on cloud and infrastructure implementation (4Q orders were up +13% yoy).

(2) Order environment: 4Q3/26 orders increased +13% yoy, with the growth rate accelerating for the fourth consecutive quarter. In addition to a recovery in cloud solutions from US-based Salesforce, Microsoft, and ServiceNow, demand is strong in the data management/data lake fields. In particular, the company said that it believes that with the spread of generative AI, demand for the data management/data lake fields and AWS cloud (AI infrastructure) will continue to expand. On the other hand, it mentioned that growth in its core Salesforce cloud products could be sluggish, as the penetration rate among domestic customers is already quite high.

(3) Guidance: FY3/27 operating profit guidance is for ¥4.7 bn (+1% yoy), which would mark the third consecutive year of modest profit growth. While the order environment shows signs of bottoming out, and the company assumes demand will recover in FY3/27 centered on the cloud solutions business, AWS cloud (AI infrastructure), and the data management/data lake fields (digital solutions business) (sales guidance is for +10% yoy), it expects lackluster earnings growth. This is attributable to factors including a decline in the gross margin (-0.4 pp yoy) from wage hikes and an increase in SG&A expenses (+18%/+¥0.63 bn yoy) from depreciation and amortization (+¥0.3 bn cost increase) associated with the launch of an internal system, wage hikes, and investment in other systems. According to the company, in 1Q (Apr-Jun), in addition to an increase in SG&A expenses, it anticipates an impact from the drop-out of high-margin software for the financial sector that was booked in the same quarter of the previous year.

Exhibit 1: Future Corp. (4722.T): Earnings by business 

<table><tr><td>(mn yen)Future (4722)</td><td>23/12</td><td>24/12</td><td>25/12</td><td>CoE26/12E</td><td>25/12Q1</td><td>Q2</td><td>Q3</td><td>Q4</td><td>26/12Q1</td></tr><tr><td>Sales</td><td>59,324</td><td>69,878</td><td>75,993</td><td>80,600</td><td>17,320</td><td>18,325</td><td>19,637</td><td>20,711</td><td>18,262</td></tr><tr><td>yoy</td><td>10.4%</td><td>17.8%</td><td>8.8%</td><td>6.1%</td><td>15.3%</td><td>2.2%</td><td>3.6%</td><td>15.3%</td><td>5.4%</td></tr><tr><td>Gross Profit</td><td>28,807</td><td>33,700</td><td>36,987</td><td></td><td>8,117</td><td>8,835</td><td>9,890</td><td>10,145</td><td>8,379</td></tr><tr><td>yoy</td><td>8.1%</td><td>17.0%</td><td>9.8%</td><td></td><td>11.3%</td><td>2.6%</td><td>2.7%</td><td>24.2%</td><td>3.2%</td></tr><tr><td>% of sales</td><td>48.6%</td><td>48.2%</td><td>48.7%</td><td></td><td>46.9%</td><td>48.2%</td><td>50.4%</td><td>49.0%</td><td>45.9%</td></tr><tr><td>SGA</td><td>15,106</td><td>19,033</td><td>20,810</td><td></td><td>4,782</td><td>5,061</td><td>5,286</td><td>5,681</td><td>4,946</td></tr><tr><td>yoy</td><td>4.7%</td><td>26.0%</td><td>9.3%</td><td></td><td>23.4%</td><td>-1.2%</td><td>7.1%</td><td>11.5%</td><td>3.4%</td></tr><tr><td>% of sales</td><td>25.5%</td><td>27.2%</td><td>27.4%</td><td></td><td>27.6%</td><td>27.6%</td><td>26.9%</td><td>27.4%</td><td>27.1%</td></tr><tr><td>Operating Profits</td><td>13,700</td><td>14,667</td><td>16,176</td><td>17,500</td><td>3,335</td><td>3,773</td><td>4,605</td><td>4,463</td><td>3,433</td></tr><tr><td>yoy</td><td>12.1%</td><td>7.1%</td><td>10.3%</td><td>8.2%</td><td>-2.4%</td><td>8.3%</td><td>-2.0%</td><td>45.5%</td><td>2.9%</td></tr><tr><td>% of sales</td><td>23.1%</td><td>21.0%</td><td>21.3%</td><td>21.7%</td><td>19.3%</td><td>20.6%</td><td>23.5%</td><td>21.5%</td><td>18.8%</td></tr><tr><td colspan="10"></td></tr><tr><td colspan="10">IT Consulting &amp; Service Business</td></tr><tr><td>Sales</td><td>50,750</td><td>60,798</td><td>67,445</td><td></td><td>15,517</td><td>16,227</td><td>17,612</td><td>18,089</td><td>16,538</td></tr><tr><td>yoy</td><td>11.6%</td><td>19.8%</td><td>10.9%</td><td></td><td>19.2%</td><td>5.5%</td><td>5.7%</td><td>14.9%</td><td>6.6%</td></tr><tr><td>% of sales</td><td>85.5%</td><td>87.0%</td><td>88.8%</td><td></td><td>89.6%</td><td>88.6%</td><td>89.7%</td><td>87.3%</td><td>90.6%</td></tr><tr><td colspan="10"></td></tr><tr><td>Service</td><td>15,466</td><td>19,761</td><td>23,487</td><td></td><td>5,769</td><td>5,753</td><td>5,987</td><td>5,978</td><td>6,046</td></tr><tr><td>yoy</td><td>-1.1%</td><td>27.8%</td><td>18.9%</td><td></td><td>51.4%</td><td>6.9%</td><td>18.3%</td><td>8.5%</td><td>4.8%</td></tr><tr><td>% of sales</td><td>30.5%</td><td>32.5%</td><td>34.8%</td><td></td><td>37.2%</td><td>35.5%</td><td>34.0%</td><td>33.0%</td><td>36.6%</td></tr><tr><td>Retail</td><td>11,210</td><td>15,811</td><td>14,828</td><td></td><td>3,968</td><td>3,592</td><td>3,367</td><td>3,901</td><td>3,592</td></tr><tr><td>yoy</td><td>25.5%</td><td>41.0%</td><td>-6.2%</td><td></td><td>20.9%</td><td>-9.6%</td><td>-15.4%</td><td>-14.8%</td><td>-9.5%</td></tr><tr><td>% of sales</td><td>22.1%</td><td>26.0%</td><td>22.0%</td><td></td><td>25.6%</td><td>22.1%</td><td>19.1%</td><td>21.6%</td><td>21.7%</td></tr><tr><td>Finance</td><td>13,179</td><td>13,576</td><td>15,934</td><td></td><td>2,890</td><td>3,436</td><td>4,971</td><td>4,637</td><td>3,201</td></tr><tr><td>yoy</td><td>15.5%</td><td>3.0%</td><td>17.4%</td><td></td><td>-11.9%</td><td>15.0%</td><td>9.5%</td><td>67.5%</td><td>10.8%</td></tr><tr><td>% of sales</td><td>26.0%</td><td>22.3%</td><td>23.6%</td><td></td><td>18.6%</td><td>21.2%</td><td>28.2%</td><td>25.6%</td><td>19.4%</td></tr><tr><td>Manufacturing</td><td>6,701</td><td>8,210</td><td>8,562</td><td></td><td>2,015</td><td>2,062</td><td>2,000</td><td>2,485</td><td>2,091</td></tr><tr><td>yoy</td><td>47.7%</td><td>22.5%</td><td>4.3%</td><td></td><td>-1.5%</td><td>-14.5%</td><td>-9.7%</td><td>61.6%</td><td>3.8%</td></tr><tr><td>% of sales</td><td>13.2%</td><td>13.5%</td><td>12.7%</td><td></td><td>13.0%</td><td>12.7%</td><td>11.4%</td><td>13.7%</td><td>12.6%</td></tr><tr><td>Others</td><td>4,193</td><td>3,438</td><td>4,631</td><td></td><td>873</td><td>1,385</td><td>1,286</td><td>1,087</td><td>1,606</td></tr><tr><td>yoy</td><td>-15.4%</td><td>-18.0%</td><td>34.7%</td><td></td><td>45.3%</td><td>122.7%</td><td>48.0%</td><td>-19.2%</td><td>84.0%</td></tr><tr><td>% of sales</td><td>8.3%</td><td>5.7%</td><td>6.9%</td><td></td><td>5.6%</td><td>8.5%</td><td>7.3%</td><td>6.0%</td><td>9.7%</td></tr><tr><td colspan="10"></td></tr><tr><td>Grand Design</td><td>10,138</td><td>13,799</td><td>18,640</td><td></td><td>4,309</td><td>4,227</td><td>4,925</td><td>5,179</td><td>5,463</td></tr><tr><td>yoy</td><td>6.2%</td><td>36.1%</td><td>35.1%</td><td></td><td>78.9%</td><td>32.1%</td><td>44.3%</td><td>8.4%</td><td>26.8%</td></tr><tr><td>% of sales</td><td>20.0%</td><td>22.7%</td><td>27.6%</td><td></td><td>27.8%</td><td>26.0%</td><td>28.0%</td><td>28.6%</td><td>33.0%</td></tr><tr><td>Design</td><td>4,880</td><td>3,173</td><td>4,875</td><td></td><td>899</td><td>938</td><td>1,303</td><td>1,735</td><td>1,416</td></tr><tr><td>yoy</td><td>-41.6%</td><td>-35.0%</td><td>53.6%</td><td></td><td>-17.6%</td><td>43.9%</td><td>84.6%</td><td>139.6%</td><td>57.5%</td></tr><tr><td>% of sales</td><td>9.6%</td><td>5.2%</td><td>7.2%</td><td></td><td>5.8%</td><td>5.8%</td><td>7.4%</td><td>9.6%</td><td>8.6%</td></tr><tr><td>Development</td><td>23,998</td><td>27,754</td><td>23,863</td><td></td><td>6,292</td><td>6,376</td><td>5,365</td><td>5,830</td><td>5,574</td></tr><tr><td>yoy</td><td>50.0%</td><td>15.7%</td><td>-14.0%</td><td></td><td>-4.3%</td><td>-19.9%</td><td>-21.1%</td><td>-9.1%</td><td>-11.4%</td></tr><tr><td>% of sales</td><td>47.3%</td><td>45.6%</td><td>35.4%</td><td></td><td>40.5%</td><td>39.3%</td><td>30.5%</td><td>32.2%</td><td>33.7%</td></tr><tr><td>Maintenance</td><td>8,056</td><td>10,199</td><td>11,153</td><td></td><td>2,914</td><td>2,703</td><td>2,808</td><td>2,728</td><td>3,080</td></tr><tr><td>yoy</td><td>1.6%</td><td>26.6%</td><td>9.4%</td><td></td><td>39.6%</td><td>9.7%</td><td>-5.5%</td><td>2.0%</td><td>5.7%</td></tr><tr><td>% of sales</td><td>15.9%</td><td>16.8%</td><td>16.5%</td><td></td><td>18.8%</td><td>16.7%</td><td>15.9%</td><td>15.1%</td><td>18.6%</td></tr><tr><td>Merchandise and others</td><td>3,677</td><td>5,871</td><td>8,911</td><td></td><td>1,100</td><td>1,983</td><td>3,213</td><td>2,615</td><td>1,003</td></tr><tr><td>yoy</td><td>0.7%</td><td>59.7%</td><td>51.8%</td><td></td><td>27.9%</td><td>80.9%</td><td>16.2%</td><td>127.2%</td><td>-8.8%</td></tr><tr><td>% of sales</td><td>7.2%</td><td>9.7%</td><td>13.2%</td><td></td><td>7.1%</td><td>12.2%</td><td>18.2%</td><td>14.5%</td><td>6.1%</td></tr><tr><td>Operating Profits</td><td>13,705</td><td>14,538</td><td>16,381</td><td></td><td>3,558</td><td>3,707</td><td>4,813</td><td>4,303</td><td>3,544</td></tr><tr><td>yoy</td><td>6.2%</td><td>6.1%</td><td>12.7%</td><td></td><td>0.7%</td><td>16.4%</td><td>4.3%</td><td>34.2%</td><td>-0.4%</td></tr><tr><td>% of sales</td><td>27.0%</td><td>23.9%</td><td>24.3%</td><td></td><td>22.9%</td><td>22.8%</td><td>27.3%</td><td>23.8%</td><td>21.4%</td></tr><tr><td colspan="10">Business Innovation Business</td></tr><tr><td>Sales</td><td>8,259</td><td>8,895</td><td>8,341</td><td></td><td>1,754</td><td>2,041</td><td>1,965</td><td>2,581</td><td>1,654</td></tr><tr><td>yoy</td><td>0.7%</td><td>7.7%</td><td>-6.2%</td><td></td><td>-9.7%</td><td>-18.6%</td><td>-13.2%</td><td>18.4%</td><td>-5.7%</td></tr><tr><td>% of sales</td><td>13.9%</td><td>12.7%</td><td>11.0%</td><td></td><td>10.1%</td><td>11.1%</td><td>10.0%</td><td>12.5%</td><td>9.1%</td></tr><tr><td>Operating Profits</td><td>-144</td><td>381</td><td>178</td><td></td><td>-118</td><td>51</td><td>-61</td><td>306</td><td>-25</td></tr><tr><td>yoy</td><td>N.M.</td><td>N.M.</td><td>-53.3%</td><td></td><td>N.M.</td><td>-82.0%</td><td>N.M.</td><td>1700.0%</td><td>N.M.</td></tr><tr><td>% of sales</td><td>-1.7%</td><td>4.3%</td><td>2.1%</td><td></td><td>-6.7%</td><td>2.5%</td><td>-3.1%</td><td>11.9%</td><td>-1.5%</td></tr><tr><td colspan="10">Others</td></tr><tr><td>Sales</td><td>314</td><td>185</td><td>206</td><td></td><td>48</td><td>56</td><td>62</td><td>40</td><td>63</td></tr><tr><td>OP</td><td>-123</td><td>-133</td><td>-84</td><td></td><td>-65</td><td>-65</td><td>139</td><td>-93</td><td>41</td></tr><tr><td>OP Adjustment</td><td>263</td><td>-119</td><td>-299</td><td></td><td>-39</td><td>79</td><td>-286</td><td>-53</td><td>-127</td></tr></table>

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 2: SIGMAXYZ (6088.T): Earnings by business 

<table><tr><td>(mn yen) Sigmaxys (6088)</td><td>24/3</td><td>25/3</td><td>26/3</td><td>CoE 27/3E</td><td>26/3 Q1</td><td>Q2</td><td>Q3</td><td>Q4</td></tr><tr><td>Sales</td><td>22,411</td><td>26,294</td><td>23,831</td><td>25,300</td><td>6,243</td><td>6,316</td><td>5,468</td><td>5,805</td></tr><tr><td>yoy</td><td>29.3%</td><td>17.3%</td><td>-9.4%</td><td>6.2%</td><td>4.5%</td><td>-4.1%</td><td>-21.0%</td><td>-14.8%</td></tr><tr><td>Gross Profit</td><td>10,010</td><td>11,732</td><td>11,783</td><td></td><td>2,949</td><td>3,000</td><td>2,784</td><td>3,050</td></tr><tr><td>yoy</td><td>19.5%</td><td>17.2%</td><td>0.4%</td><td></td><td>10.6%</td><td>0.6%</td><td>-9.0%</td><td>0.9%</td></tr><tr><td>% of sales</td><td>44.7%</td><td>44.6%</td><td>49.4%</td><td></td><td>47.2%</td><td>47.5%</td><td>50.9%</td><td>52.5%</td></tr><tr><td>SGA</td><td>5,777</td><td>6,093</td><td>5,718</td><td></td><td>1,331</td><td>1,420</td><td>1,437</td><td>1,530</td></tr><tr><td>yoy</td><td>12.4%</td>

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
