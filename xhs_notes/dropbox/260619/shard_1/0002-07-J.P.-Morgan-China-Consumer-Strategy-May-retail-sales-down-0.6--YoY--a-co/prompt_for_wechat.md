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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Consumer Strategy

May retail sales down $0.6\%$ YoY, a consecutive miss

China's May 2026 retail sales fell by $0.6\%$ YoY (the first decline since Dec-22), a sequential deterioration from Apr $(+0.2\%)$ and Mar $(+1.7\%)$ , missing Bloomberg consensus (down $0.2\%$ ). Durable goods continued to be the drag, including home durables (down $15\%$ on a high base); gold & jewelry (down $9\%$ ) - reflecting recent volatility in gold prices (though narrowing from down $21\%$ in Apr); and autos (down $16\%$ ). YTD weakening demand triggered further concerns among investors on topline growth for consumer companies, and we think there is a higher possibility that more companies may guide down during the 2Q26 result season. Investors agree that it's too early to call the bottom and hence need to stay selective and stick with quality names.

\- Stock views. We advise investors to focus on two groups: (I) quality names with limited downside and earlier earnings stabilization - Anta (OW) for a well-executed multi-brand portfolio and overseas upside; Nongfu (OW) for strong brand momentum and a margin buffer; Guming (OW) for a continued runway for network growth and improving brand equity. (II) Turnaround stories – Chagee (OW) for China GMV stabilization in 2QTD and upside in shareholder return; Luckin (OW) for better-than-feared SSS decline and earnings release from 2Q/3Q26. Investors may want to avoid those highly exposed to raw material hikes (CR Beverage, etc).

\- May 2026 retail sales breakdown. Online/offline: online retail sales grew by $3.4\%$ YoY, outpacing offline's $-1.8\%$ YoY. Top 5 YoY performing categories: soft drinks $(+6\%)$ , tobacco and alcohol $(+5\%)$ , medicine $(+4\%)$ , apparel & textile $(+4\%)$ and cosmetics $(+3\%)$ . Bottom 5 YoY performing categories: autos (down $16\%$ YoY), home appliance (down $16\%$ ), home furnishing (down $14\%$ ), gold & jewelry (down $9\%$ ) and furniture (down $9\%$ ).

\- CPI was up $1.2\%$ YoY in May (vs. $1.2\%$ in Apr), with food CPI down $1.7\%$ YoY and non-food CPI up $1.9\%$ YoY. Core CPI was up $1.1\%$ YoY (vs. $1.2\%$ in Apr).

\- Unemployment rate was $5.1\%$ in May, up 0.1ppt YoY and down 0.1ppt MoM.

\- Sector share price/valuation. China consumer staples/discretionary sector share prices are down $5.5\% / 2.7\%$ over the past one month (vs MSCI China/HSI Index $-3.7\% / -4.3\%$ ). Their forward P/E has de-rated $9.6\% / 6.5\%$ to $15.2x / 12.1x$ (vs MSCI China/HSI Index de-rating of $3\% / 3.7\%$ to $11.7x / 11.2x$ ).

## Consumer

Jessie Xu AC

(852) 2800-8590

jessie.j.xu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

## Qian Yao

(86-21) 6106 6277

qian.q.yao@JPM.com

SAC Registration Number: S1730521050001

JPM Securities (China) Company Limited

## Yibo Wu

(852) 2800-8559

yibo.wu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

## Carson Fan

(86-21) 6106-6294

rong.fan@JPM.com

SAC Registration Number: S1730522070002

JPM Securities (China) Company Limited

## Sylvia Hu

(86-21) 6106-6284

sylvia.hu@JPM.com

SAC Registration Number: S1730526010001

JPM Securities (China) Company Limited

## DS Kim

(852) 2800-8597

ds.kim@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

Table 1: China retail sales breakdown (YoY growth) and unemployment data

<table><tr><td>YOY GROWTH %</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Total retail sales</td><td>12.5%</td><td>-0.3%</td><td>7.2%</td><td>3.5%</td><td>4.6%</td><td>5.4%</td><td>2.7%</td><td>1.7%</td><td>3.5%</td><td>2.4%</td><td>0.2%</td><td>-0.6%</td></tr><tr><td>Retail sales ex-auto</td><td>13.0%</td><td>-0.4%</td><td>7.4%</td><td>4.0%</td><td>5.2%</td><td>5.8%</td><td>3.4%</td><td>2.8%</td><td>4.2%</td><td>3.5%</td><td>1.8%</td><td>1.0%</td></tr><tr><td>Retail sales of large retailers</td><td>13.4%</td><td>1.4%</td><td>6.5%</td><td>2.7%</td><td>5.7%</td><td>6.4%</td><td>2.0%</td><td>-0.8%</td><td>3.1%</td><td>2.2%</td><td>-4.4%</td><td>-4.9%</td></tr><tr><td>Online physical goods sales</td><td>12.0%</td><td>6.2%</td><td>8.4%</td><td>6.5%</td><td>5.7%</td><td>6.3%</td><td>5.5%</td><td>2.3%</td><td>4.8%</td><td>7.5%</td><td>0.2%</td><td>2.6%</td></tr><tr><td>Total retail sales</td><td>12.4%</td><td>-0.2%</td><td>7.2%</td><td>3.5%</td><td>4.6%</td><td>5.4%</td><td>2.7%</td><td>1.7%</td><td>3.5%</td><td>2.4%</td><td>0.2%</td><td>-0.6%</td></tr><tr><td>Urban</td><td>12.5%</td><td>-0.3%</td><td>7.1%</td><td>3.4%</td><td>4.5%</td><td>5.5%</td><td>2.5%</td><td>1.5%</td><td>3.4%</td><td>2.3%</td><td>-0.1%</td><td>-0.9%</td></tr><tr><td>Rural</td><td>12.1%</td><td>0.0%</td><td>8.0%</td><td>4.2%</td><td>4.8%</td><td>4.9%</td><td>3.8%</td><td>2.8%</td><td>4.0%</td><td>3.0%</td><td>2.1%</td><td>1.5%</td></tr><tr><td>Total retail sales</td><td>12.5%</td><td>-0.2%</td><td>7.2%</td><td>3.5%</td><td>4.6%</td><td>5.4%</td><td>2.7%</td><td>1.7%</td><td>3.5%</td><td>2.4%</td><td>0.2%</td><td>-0.6%</td></tr><tr><td>Catering sales</td><td>18.6%</td><td>-6.3%</td><td>20.4%</td><td>5.4%</td><td>4.7%</td><td>3.9%</td><td>1.9%</td><td>3.0%</td><td>3.4%</td><td>4.2%</td><td>2.2%</td><td>0.6%</td></tr><tr><td>Goods sales</td><td>11.8%</td><td>0.5%</td><td>5.8%</td><td>3.2%</td><td>4.6%</td><td>5.6%</td><td>2.8%</td><td>1.5%</td><td>3.5%</td><td>2.2%</td><td>-0.1%</td><td>-0.7%</td></tr><tr><td>Total retail sales</td><td>12.5%</td><td>-0.3%</td><td>7.2%</td><td>3.5%</td><td>4.6%</td><td>5.4%</td><td>2.7%</td><td>1.7%</td><td>3.5%</td><td>2.4%</td><td>0.2%</td><td>-0.6%</td></tr><tr><td>Offline sales</td><td>12.6%</td><td>-2.5%</td><td>6.8%</td><td>2.4%</td><td>4.3%</td><td>5.1%</td><td>1.7%</td><td>1.5%</td><td>3.1%</td><td>0.9%</td><td>0.2%</td><td>-1.8%</td></tr><tr><td>Offline goods sales</td><td>11.7%</td><td>-1.8%</td><td>4.6%</td><td>1.9%</td><td>4.2%</td><td>5.4%</td><td>1.7%</td><td>1.1%</td><td>3.1%</td><td>0.3%</td><td>-0.1%</td><td>-2.2%</td></tr><tr><td>Offline service sales</td><td>18.6%</td><td>-6.3%</td><td>20.4%</td><td>5.4%</td><td>4.7%</td><td>3.9%</td><td>1.9%</td><td>3.0%</td><td>3.4%</td><td>4.2%</td><td>2.2%</td><td>0.6%</td></tr><tr><td>Online physical goods sales</td><td>12.0%</td><td>6.2%</td><td>8.4%</td><td>6.5%</td><td>5.7%</td><td>6.3%</td><td>5.5%</td><td>2.3%</td><td>4.8%</td><td>7.5%</td><td>0.2%</td><td>2.6%</td></tr><tr><td>Online sales - overall</td><td>14.1%</td><td>4.0%</td><td>11.0%</td><td>7.2%</td><td>7.9%</td><td>9.1%</td><td>9.4%</td><td>5.8%</td><td>7.9%</td><td>8.0%</td><td>2.3%</td><td>3.4%</td></tr><tr><td>Online service and virtual goods sa</td><td>25.3%</td><td>-8.5%</td><td>27.5%</td><td>11.1%</td><td>19.8%</td><td>24.0%</td><td>21.2%</td><td>29.2%</td><td>23.3%</td><td>8.9%</td><td>6.1%</td><td>5.0%</td></tr><tr><td>Online physical goods sales</td><td>12.0%</td><td>6.2%</td><td>8.4%</td><td>6.5%</td><td>5.7%</td><td>6.3%</td><td>5.5%</td><td>2.3%</td><td>4.8%</td><td>7.5%</td><td>0.2%</td><td>2.6%</td></tr><tr><td>Retail sales of large retailers</td><td>13.4%</td><td>1.4%</td><td>6.5%</td><td>2.7%</td><td>5.7%</td><td>6.4%</td><td>2.0%</td><td>-0.8%</td><td>3.1%</td><td>2.2%</td><td>-4.4%</td><td>-4.9%</td></tr><tr><td>Catering sales</td><td>23.6%</td><td>-5.9%</td><td>20.9%</td><td>2.9%</td><td>4.7%</td><td>2.6%</td><td>0.5%</td><td>1.2%</td><td>2.2%</td><td>3.8%</td><td>0.9%</td><td>-1.7%</td></tr><tr><td>Goods sales</td><td>12.8%</td><td>1.9%</td><td>5.5%</td><td>2.7%</td><td>5.8%</td><td>6.7%</td><td>2.2%</td><td>-1.0%</td><td>3.2%</td><td>2.0%</td><td>-4.9%</td><td>-5.2%</td></tr><tr><td>Staple foods</td><td>10.8%</td><td>8.7%</td><td>5.2%</td><td>9.9%</td><td>12.2%</td><td>12.3%</td><td>7.2%</td><td>6.2%</td><td>9.3%</td><td>10.0%</td><td>4.1%</td><td>1.9%</td></tr><tr><td>Soft drinks</td><td>20.4%</td><td>5.3%</td><td>3.2%</td><td>2.1%</td><td>-0.5%</td><td>-0.8%</td><td>3.0%</td><td>3.9%</td><td>1.4%</td><td>6.7%</td><td>3.6%</td><td>6.1%</td></tr><tr><td>Tobacco &amp; Alcohol</td><td>21.2%</td><td>2.3%</td><td>10.6%</td><td>5.7%</td><td>6.3%</td><td>4.5%</td><td>2.4%</td><td>-1.0%</td><td>3.1%</td><td>16.0%</td><td>11.7%</td><td>4.8%</td></tr><tr><td>Apparel &amp; textiles</td><td>12.7%</td><td>-6.5%</td><td>12.9%</td><td>0.3%</td><td>3.4%</td><td>2.7%</td><td>5.0%</td><td>3.3%</td><td>3.6%</td><td>9.3%</td><td>3.6%</td><td>3.8%</td></tr><tr><td>Cosmetics</td><td>14.0%</td><td>-4.5%</td><td>5.1%</td><td>-1.1%</td><td>3.1%</td><td>2.6%</td><td>7.4%</td><td>8.2%</td><td>5.4%</td><td>5.9%</td><td>4.7%</td><td>2.5%</td></tr><tr><td>Gold &amp; jewelry</td><td>29.9%</td><td>-1.1%</td><td>13.3%</td><td>-3.1%</td><td>6.9%</td><td>17.3%</td><td>12.6%</td><td>16.7%</td><td>13.0%</td><td>12.6%</td><td>-21.3%</td><td>-8.9%</td></tr><tr><td>Home &amp; personal care</td><td>14.4%</td><td>-0.7%</td><td>2.7%</td><td>3.0%</td><td>6.8%</td><td>7.8%</td><td>6.3%</td><td>3.3%</td><td>6.0%</td><td>5.9%</td><td>3.5%</td><td>1.6%</td></tr><tr><td>Sporting &amp; entertainment</td><td></td><td></td><td>11.1%</td><td>11.0%</td><td>25.5%</td><td>19.5%</td><td>7.8%</td><td>6.3%</td><td>14.1%</td><td>1.9%</td><td>-8.0%</td><td>-8.0%</td></tr><tr><td>Home appliances</td><td>10.0%</td><td>-3.9%</td><td>0.5%</td><td>12.2%</td><td>19.3%</td><td>40.4%</td><td>3.3%</td><td>-17.7%</td><td>8.3%</td><td>0.0%</td><td>-15.1%</td><td>-15.6%</td></tr><tr><td>Medicine</td><td>9.9%</td><td>12.4%</td><td>5.2%</td><td>3.1%</td><td>2.1%</td><td>0.7%</td><td>2.9%</td><td>3.1%</td><td>2.2%</td><td>2.5%</td><td>4.2%</td><td>4.0%</td></tr><tr><td>Office staples</td><td>18.8%</td><td>4.4%</td><td>-6.1%</td><td>-0.3%</td><td>21.7%</td><td>28.7%</td><td>11.5%</td><td>11.5%</td><td>17.3%</td><td>9.3%</td><td>-6.9%</td><td>-1.5%</td></tr><tr><td>Furniture</td><td>14.4%</td><td>-7.5%</td><td>2.8%</td><td>3.6%</td><td>18.0%</td><td>27.2%</td><td>8.1%</td><td>0.6%</td><td>12.1%</td><td>1.9%</td><td>-10.4%</td><td>-8.7%</td></tr><tr><td>Telecom</td><td>14.6%</td><td>-3.4%</td><td>7.0%</td><td>10.0%</td><td>27.0%</td><td>21.5%</td><td>17.7%</td><td>21.6%</td><td>21.8%</td><td>20.8%</td><td>6.2%</td><td>0.7%</td></tr><tr><td>Oil &amp; gas</td><td>21.2%</td><td>9.7%</td><td>6.6%</td><td>0.3%</td><td>-0.1%</td><td>-6.7%</td><td>-5.1%</td><td>-8.3%</td><td>-5.0%</td><td>-6.4%</td><td>-6.5%</td><td>-3.2%</td></tr><tr><td>Autos</td><td>7.6%</td><td>0.7%</td><td>5.9%</td><td>-0.5%</td><td>-0.8%</td><td>2.3%</td><td>-3.0%</td><td>-6.5%</td><td>-2.3%</td><td>-9.0%</td><td>-15.3%</td><td>-16.1%</td></tr><tr><td>Home furnishing</td><td>20.4%</td><td>-6.2%</td><td>-7.8%</td><td>-2.0%</td><td>0.0%</td><td>5.2%</td><td>-3.0%</td><td>-12.5%</td><td>-3.3%</td><td>-4.7%</td><td>-13.8%</td><td>-13.6%</td></tr><tr><td>Real GDP</td><td>8.4%</td><td>3.0%</td><td>5.2%</td><td>5.0%</td><td>5.4%</td><td>5.2%</td><td>4.8%</td><td>4.5%</td><td>5.0%</td><td>5.0%</td><td></td><td></td></tr><tr><td>CPI</td><td>0.9%</td><td>2.0%</td><td>0.2%</td><td>0.2%</td><td>-0.1%</td><td>0.0%</td><td>0.1%</td><td>0.6%</td><td>0.1%</td><td>0.8%</td><td>1.2%</td><td>1.2%</td></tr><tr><td>Food CPI</td><td>-1.4%</td><td>2.9%</td><td>-0.3%</td><td>-0.6%</td><td>-1.4%</td><td>-0.3%</td><td>-2.8%</td><td>-0.5%</td><td>-1.3%</td><td>0.4%</td><td>-1.6%</td><td>-1.7%</td></tr><tr><td>Non-food CPI</td><td>1.4%</td><td>1.8%</td><td>0.4%</td><td>0.4%</td><td>0.2%</td><td>0.0%</td><td>0.8%</td><td>0.8%</td><td>0.5%</td><td>1.0%</td><td>1.8%</td><td>1.9%</td></tr><tr><td>Core CPI (ex-food &amp; energy)</td><td>0.8%</td><td>0.9%</td><td>0.7%</td><td>0.5%</td><td>0.3%</td><td>0.6%</td><td>1.0%</td><td>1.2%</td><td>0.8%</td><td>1.2%</td><td>1.2%</td><td>1.1%</td></tr><tr><td>PPI</td><td>8.1%</td><td>4.2%</td><td>-3.0%</td><td>-2.2%</td><td>-2.3%</td><td>-3.2%</td><td>-1.6%</td><td>-2.1%</td><td>-2.3%</td><td>-0.6%</td><td>2.8%</td><td>3.9%</td></tr><tr><td>Unemployment rate</td><td>5.1%</td><td>5.6%</td><td>5.2%</td><td>5.1%</td><td>5.3%</td><td>5.0%</td><td>5.3%</td><td>5.1%</td><td>5.2%</td><td>5.3%</td><td>5.2%</td><td>5.1%</td></tr><tr><td>16-24 year-old</td><td>14.3%</td><td>17.6%</td><td>--</td><td>15.8%*</td><td>16.5%*</td><td>15.1%*</td><td>17.8%*</td><td>16.9%*</td><td>16.6%*</td><td>16.4%*</td><td>16.3%*</td><td></td></tr><tr><td>25-29 year-old</td><td></td><td></td><td></td><td>6.7%*</td><td>7.1%*</td><td>6.9%*</td><td>7.4%*</td><td>7.1%*</td><td>7.1%*</td><td>7.2%*</td><td>7.4%*</td><td></td></tr><tr><td>25-59 year old</td><td>4.5%</td><td>4.8%</td><td>--</td><td>4.0%*</td><td>4.1%*</td><td>4.0%*</td><td>4.0%*</td><td>3.8%*</td><td>4.0%*</td><td>4.2%*</td><td>4.2%*</td><td></td></tr></table>

Source: National Bureau of Statistics. Note: (1) Feb = January & February combined; (2) China retail sales = Offline service (i.e. catering) + offline goods + online physical goods. (3) Online retail sales = online physical goods sales (included in China retail sales) + online service & virtual goods sales (not included in China retail sales). (4) Retail sales growth by category is based on survey of larger retailers. Large retailers = wholesalers with annual revenue above Rmb20mn + retailers with annual revenue above Rmb5mn + hotel/restaurants with annual revenue above Rmb2mn. (5) % growth data is subjected to rounding error.

Figure 1: China retail sales YoY trend  
![](images/fb30b68dd517b5874a1b1e2a6a242b20e60f2ce2f4def7d47345258ee3303a60.jpg)

<details>
<summary>line chart</summary>

| Month | Value (%) |
|---|---|
| Apr-25 | 5.1 |
| May-25 | 6.4 |
| Jun-25 | 4.8 |
| Jul-25 | 3.7 |
| Aug-25 | 3.4 |
| Sep-25 | 3.0 |
| Oct-25 | 2.9 |
| Nov-25 | 1.3 |
| Dec-25 | 0.9 |
| Jan-26 | 2.8 |
| Feb-26 | 1.7 |
| Mar-26 | 0.2 |
| Apr-26 | -0.6 |
| May-26 | -0.6 |
</details>

Source: National Bureau of Statistics.

Figure 2: China retail sales YoY trend – key categories  
![](images/eeb1ad7ba9d02237ceb1aa458667e0895792f8ddf048b4cded58c950f1566e86.jpg)

<details>
<summary>line chart</summary>

| Month   | Food and beverage | Apparel and accessories | Home durables | Autos |
|---------|-------------------|--------------------------|---------------|-------|
| Apr-25  | 10%               | 8%                       | 35%           | 0%    |
| May-25  | 12%               | 8%                       | 45%           | 0%    |
| Jun-25  | 8%                | 5%                       | 28%           | 0%    |
| Jul-25  | 7%                | 4%                       | 22%           | 0%    |
| Aug-25  | 6%                | 6%                       | 12%           | 0%    |
| Sep-25  | 5%                | 5%                       | 5%            | 0%    |
| Oct-25  | 8%                | 10%                      | -10%          | -5%   |
| Nov-25  | 7%                | 5%                       | -20%          | -10%  |
| Dec-25  | 5%                | 3%                       | -18%          | -5%   |
| Jan-26  | 10%               | 8%                       | 5%            | -5%   |
| Feb-26  | 12%               | 10%                      | -5%           | -10%  |
| Mar-26  | 10%               | 8%                       | -10%          | -15%  |
| Apr-26  | 8%                | 0%                       | -15%          | -20%  |
| May-26  | 5%                | 0%                       | -18%          | -20%  |
</details>

Source: National Bureau of Statistics. Note: Food and beverage = Staple food + soft drinks + alcohol and tobacco. Apparel and accessories = apparel + cosmetics + gold & jewelry + sporting goods; home durables = home appliance + home furnishing materials + furniture.

Figure 3: Retail sales yoy growth ranked by category – May 2026  
![](images/8be062b65cae2ad0f0e1ae381c7ccf4347113db429565c2589fa9f47d0543d34.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (%) |
|---|---|
| Autos | -16 |
| Home appliances | -16 |
| Furnishing | -14 |
| GD & JEW | -9 |
| Furniture | -9 |
| Sporting | -8 |
| Large retailers | -5 |
| Oil & gas | -3 |
| Catering | -2 |
| Office staples | -2 |
| Overall Telecom | -1 |
| HPC | 1 |
| Staple foods | 2 |
| Cosmetics | 2 |
| AP & TX | 3 |
| Medicine | 4 |
| TB & AL | 4 |
| Soft drinks | 5 |
| Soft drinks | 6 |
</details>

Source: National Bureau of Statistics. "TB & AL" = tobacco & alcohol; "AP & TX" = apparel & textiles; "GD & JEW" = gold & jewelry; "HPC" = home & personal care

Figure 4: Change in yoy growth by category (May 26 vs Apr 26)  
![](images/786588e409a5a1e9db5544d34dd0ee2fb84b13290b3fc5308224cac109a099d4.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (%) |
|---|---|
| TB & A | -7 |
| Telecom | -6 |
| Catering | -3 |
| Cosmetics | -2 |
| Staple foods | -2 |
| HPC | -2 |
| Autos | -1 |
| Overall | -1 |
| Large retailers | -1 |
| Home appliances | -1 |
| Medicine | 0 |
| Sporting | 0 |
| AP & TX | 0 |
| Furnishing | 0 |
| Furniture | 2 |
| Soft drinks | 3 |
| Oil & gas | 3 |
| Office staples | 5 |
| GD & JEW | 12 |
</details>

Source: National Bureau of Statistics. "TB & AL" = tobacco & alcohol; "AP & TX" = apparel & textiles; "GD & JEW" = gold & jewelry; "HPC" = home & personal care

Figure 5: Unemployment rate – overall  
![](images/d55f6ebbde184ef914ad29aeed16ffe99ecf221738e0ab81680eeb93b672adea.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 (%) | 2023 (%) | 2024 (%) | 2025 (%) | 2026 (%) |
|---|---|---|---|---|---|
| Jan | 5.2 | 5.5 | 5.3 | 5.2 | 5.1 |
| Feb | 5.3 | 5.6 | 5.3 | 5.3 | 5.3 |
| Mar | 5.7 | 5.4 | 5.2 | 5.3 | 5.4 |
| Apr | 6.1 | 5.2 | 5.0 | 5.1 | 5.2 |
| May | 5.9 | 5.2 | 5.0 | 5.0 | 5.1 |
| Jun | 5.5 | 5.2 | 5.0 | 5.0 | - |
| Jul | 5.4 | 5.3 | 5.1 | 5.2 | - |
| Aug | 5.3 | 5.2 | 5.3 | 5.3 | - |
| Sep | 5.5 | 5.0 | 5.0 | 5.3 | - |
| Oct | 5.6 | 4.9 | 4.9 | 5.1 | - |
| Nov | 5.7 | 4.9 | 4.9 | 5.1 | - |
| Dec | 5.5 | 4.9 | 4.9 | 5.1 | - |
</details>

Source: National Bureau of Statistics

Figure 6: Unemployment rate – 16-24 years old  
![](images/5e537a5567c6b0099ff2520c1007677d10698a9d7e20d4961c6ce0c5fb5ed6e4.jpg)

<details>
<summary>line chart</summary>

| Month | 2022  | 2023  | 2024  | 2025  | 2026  |
|-------|-------|-------|-------|-------|-------|
| Jan   | 15.5% | 17.0% | 14.5% | 16.5% | 16.0% |
| Feb   | 15.8% | 17.5% | 15.0% | 16.8% | 16.2% |
| Mar   | 16.0% | 18.5% | 15.5% | 17.0% | 16.5% |
| Apr   | 16.5% | 19

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into

which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
