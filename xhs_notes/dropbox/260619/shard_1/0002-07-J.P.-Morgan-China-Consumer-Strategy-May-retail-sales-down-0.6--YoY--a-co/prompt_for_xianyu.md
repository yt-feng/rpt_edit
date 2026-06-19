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

Source: National Bureau of Statistics. Note: Food and beverage = Staple food + soft drinks + alcohol and tobacco. Apparel and accessories = apparel + cosmetics + gold & jewelry + sporting goods; hom

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into

which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
