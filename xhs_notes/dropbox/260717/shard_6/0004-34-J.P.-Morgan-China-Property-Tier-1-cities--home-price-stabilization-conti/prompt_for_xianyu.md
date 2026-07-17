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
## China Property

## Tier-1 cities' home price stabilization continues, but overall trends diverge

The industry data for June shows divergent trends. While home prices in tier-1 cities continued to see positive M/M growth (+0.1% in primary; +0.3% in secondary) for the fourth consecutive month (notably, not driven by nationwide easing), 70-city home prices showed divergent trends, with primary M/M decline narrowing but secondary M/M decline widening. Residential sales value dropped 14% Y/Y in June, softening from -8% Y/Y in May (below our forecast of <10% Y/Y decline), although the top 100 developers' sales (which better reflect real-time trends) showed a milder 4% Y/Y decline in June (report). Construction activity remains weak with new starts seeing a 26% Y/Y decline, although we believe this helps reduce supply and thus home price stabilization. Overall, we stick to our view that (1) tier-1 cities' home prices will see a soft form of stabilization in FY26 (led by Shanghai); (2) both primary home prices and nationwide sales value will still be on a downtrend in FY26, but the decline magnitude will narrow. Against this backdrop of K-shaped stabilization, we'd stick to alphas (SOE developers with outperforming sales growth), including COLI, CR Land and Jinmao, which have all remained YTD outperformers (+7%/+23%/+12% vs. HSI -4%).

\- 70-city primary home prices – M/M decline narrowed from -0.20% in May to -0.15% in June. Meanwhile, tier-1 cities' primary prices posted positive growth for five consecutive months (+0.12% M/M, vs. May: +0.15%), led by Shanghai and Shenzhen (both +0.3% M/M) (Table 1). Home prices in top tier-2 cities also stayed marginally positive at +0.09% M/M (outperformers: Hangzhou and Ningbo +0.3% M/M). Wrapping up 1H26, tier-1 cities' primary home prices have risen 0.3%, led by Shanghai (+1.4%) but dragged down by Beijing (-0.8%) (Table 2).

\- 70-city secondary home prices – M/M decline widened from -0.26% in May to -0.32% in June. Meanwhile, tier-1 cities rose 0.3% M/M (positive growth for the fourth consecutive month), with all four cities seeing positive growth (Beijing: +0.1%; Shanghai and Guangzhou: both +0.4%; Shenzhen: +0.3%). That said, Centraline's tier-1 secondary home price index shows a slightly different trend. The index fell 0.2% M/M in June, turning negative for the first time after four months of positive growth. The index was dragged down mostly by a 0.8% M/M decline in Shenzhen and a 0.3% M/M decline in Guangzhou, while Shanghai remained the outperformer (+0.2% M/M). Wrapping up 1H26, tier-1 cities' secondary home prices have risen 0.9%, with Shanghai (+1.9%) and Beijing (+1.3%) outperforming. For the full year of 2026, we reiterate our view that tier-1 cities will see a soft form of stabilization in secondary home prices (with Shanghai likely outperforming with mild growth), on the back of a continual drop in secondary listings, which further dropped 1% M/M in June.

\- Sales value Y/Y decline widened in June: Residential sales value fell 12% Y/Y in June, widening from -7% Y/Y in May (Figure 7). Compared to the four-year average, the decline also marginally widened from -55% in May to -57% in June (Table 7). Wrapping up 1H26, sales have fallen 14% Y/Y. For the full year of 2026, we forecast a 10% Y/Y decline (revised down from -7%), implying -5% Y/Y in 2H26 given its lower base. In July month-to-date, high-frequency data are tracking a 7% Y/Y decline in primary sales volume. Thus, we expect the Y/Y decline to mildly narrow to 5-10% in July.

\- Construction remains weak: New starts fell 26% Y/Y in June (Table 9),

See page 16 for analyst certification and important disclosures, including non-US analyst disclosures.

Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

widening from -24% Y/Y in May. We forecast new starts to drop 22% Y/Y for the full-year (revised down from -18%), implying a 21% Y/Y drop in 2H26. We expect new starts to remain weak due to soft land sales in 1H26 (-25% Y/Y). That said, with weaker new starts, there will be less supply in the primary market, and this may help stabilize home prices, which is the prerequisite for any sustainable market recovery. Completions fell 25% Y/Y in June (May: -20%) (Figure 9). For FY26, we expect a 20% Y/Y decline (revised down from -19%), implying an 18% Y/Y decline for the rest of the year.

## Home Price Trends

Table 1: Tier-1 cities – home price M/M growth (NBS and Centraline)

<table><tr><td></td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td></tr><tr><td colspan="14">Primary (NBS)</td></tr><tr><td>Beijing</td><td>-0.3%</td><td>0.0%</td><td>-0.4%</td><td>0.2%</td><td>-0.1%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.0%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td></tr><tr><td>Shanghai</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.2%</td><td>0.3%</td><td>0.4%</td><td>0.2%</td><td>0.3%</td></tr><tr><td>Guangzhou</td><td>-0.5%</td><td>-0.3%</td><td>-0.2%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>Shenzhen</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>-1.0%</td><td>-0.7%</td><td>-0.9%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.1%</td><td>0.4%</td><td>0.3%</td></tr><tr><td>Tier-1 Primary (NBS)</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td><td>-0.3%</td><td>-0.5%</td><td>-0.3%</td><td>-0.3%</td><td>0.0%</td><td>0.2%</td><td>0.1%</td><td>0.2%</td><td>0.1%</td></tr><tr><td colspan="14">Secondary (NBS)</td></tr><tr><td>Beijing</td><td>-1.0%</td><td>-1.1%</td><td>-1.2%</td><td>-0.9%</td><td>-1.1%</td><td>-1.3%</td><td>-1.3%</td><td>-0.2%</td><td>0.3%</td><td>0.6%</td><td>0.4%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-0.7%</td><td>-0.9%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.6%</td><td>-0.4%</td><td>0.2%</td><td>0.4%</td><td>0.7%</td><td>0.6%</td><td>0.4%</td></tr><tr><td>Guangzhou</td><td>-0.7%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.9%</td><td>-1.2%</td><td>-1.0%</td><td>-0.7%</td><td>-0.5%</td><td>0.2%</td><td>0.2%</td><td>0.1%</td><td>0.4%</td></tr><tr><td>Shenzhen</td><td>-0.5%</td><td>-0.9%</td><td>-0.8%</td><td>-1.0%</td><td>-0.9%</td><td>-1.0%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>0.4%</td><td>0.3%</td><td>0.6%</td><td>0.3%</td></tr><tr><td>Tier-1 Secondary (NBS)</td><td>-0.7%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.9%</td><td>-1.1%</td><td>-0.9%</td><td>-0.5%</td><td>-0.1%</td><td>0.4%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td></tr><tr><td colspan="14">Secondary (Centaline)</td></tr><tr><td>Beijing</td><td>-1.6%</td><td>-1.5%</td><td>-1.8%</td><td>-2.1%</td><td>-1.9%</td><td>-1.9%</td><td>-1.9%</td><td>-0.5%</td><td>1.2%</td><td>1.5%</td><td>0.2%</td><td>0.1%</td><td>0.1%</td></tr><tr><td>Shanghai</td><td>-1.4%</td><td>-1.7%</td><td>-1.7%</td><td>-1.5%</td><td>-2.2%</td><td>-2.0%</td><td>-2.8%</td><td>-0.5%</td><td>0.9%</td><td>1.0%</td><td>1.6%</td><td>0.9%</td><td>0.2%</td></tr><tr><td>Guangzhou</td><td>-1.4%</td><td>-1.2%</td><td>-1.8%</td><td>-1.4%</td><td>-2.0%</td><td>-1.9%</td><td>-1.3%</td><td>-0.8%</td><td>-1.5%</td><td>0.8%</td><td>-0.3%</td><td>-0.2%</td><td>-0.3%</td></tr><tr><td>Shenzhen</td><td>-0.5%</td><td>-1.1%</td><td>-1.0%</td><td>-1.5%</td><td>-0.5%</td><td>-1.0%</td><td>-1.6%</td><td>-1.3%</td><td>0.9%</td><td>0.1%</td><td>1.0%</td><td>0.1%</td><td>-0.8%</td></tr><tr><td>Tier-1 Secondary (Centaline)</td><td>-1.2%</td><td>-1.4%</td><td>-1.6%</td><td>-1.6%</td><td>-1.6%</td><td>-1.7%</td><td>-1.9%</td><td>-0.8%</td><td>0.4%</td><td>0.9%</td><td>0.6%</td><td>0.3%</td><td>-0.2%</td></tr></table>

Source: NBS, Centraline

Figure 1: Tier-1 cities – secondary home price index (NBS and Centraline) with major nationwide easing/narrative change  
![](images/b91643ce60bd577670e8b7a881801a6076cfe3b59b374471e93eea6ddedbee3d.jpg)  
Source: NBS, Centraline

Figure 2: Tier-1 cities – secondary home price M/M growth (NBS vs. Centraline)  
![](images/7d5f1523927654dc38f30a25a0ad5f26fb86f3f1137f0c2e58a4b62f637c356b.jpg)  
Note: Key nationwide policy easing / government's narrative change on housing market is shown as green. Source: NBS, Centraline

Table 2: Tier-1 cities – annual home price growth

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 YTD</td><td>vs. peak</td></tr><tr><td colspan="8">Primary (NBS)</td></tr><tr><td>70-city</td><td>2.0%</td><td>-2.3%</td><td>-0.9%</td><td>-5.8%</td><td>-3.1%</td><td>-1.4%</td><td>-13.7%</td></tr><tr><td>Tier-1 average</td><td>4.6%</td><td>2.6%</td><td>-0.2%</td><td>-4.0%</td><td>-1.7%</td><td>0.3%</td><td>-6.7%</td></tr><tr><td>Beijing</td><td>5.2%</td><td>5.8%</td><td>1.9%</td><td>-5.5%</td><td>-2.3%</td><td>-0.8%</td><td>-8.8%</td></tr><tr><td>Shanghai</td><td>4.4%</td><td>4.3%</td><td>4.3%</td><td>5.3%</td><td>4.8%</td><td>1.4%</td><td>0.0%</td></tr><tr><td>Guangzhou</td><td>5.1%</td><td>0.5%</td><td>-3.2%</td><td>-9.1%</td><td>-4.7%</td><td>0.2%</td><td>-17.4%</td></tr><tr><td>Shenzhen</td><td>3.6%</td><td>-0.3%</td><td>-3.6%</td><td>-6.0%</td><td>-4.4%</td><td>0.3%</td><td>-15.4%</td></tr><tr><td colspan="8">Secondary (NBS)</td></tr><tr><td>70-city</td><td>0.9%</td><td>-3.8%</td><td>-4.1%</td><td>-8.1%</td><td>-6.1%</td><td>-2.0%</td><td>-23.0%</td></tr><tr><td>Tier-1 average</td><td>5.4%</td><td>0.5%</td><td>-3.4%</td><td>-6.8%</td><td>-6.9%</td><td>0.9%</td><td>-16.9%</td></tr><tr><td>Beijing</td><td>8.4%</td><td>3.8%</td><td>-2.0%</td><td>-4.4%</td><td>-8.4%</td><td>1.3%</td><td>-15.2%</td></tr><tr><td>Shanghai</td><td>6.7%</td><td>2.6%</td><td>-3.4%</td><td>-3.5%</td><td>-5.9%</td><td>1.9%</td><td>-12.5%</td></tr><tr><td>Guangzhou</td><td>5.9%</td><td>-0.6%</td><td>-5.2%</td><td>-10.9%</td><td>-7.7%</td><td>-0.3%</td><td>-24.3%</td></tr><tr><td>Shenzhen</td><td>0.6%</td><td>-3.7%</td><td>-3.1%</td><td>-8.0%</td><td>-5.4%</td><td>0.6%</td><td>-20.3%</td></tr><tr><td colspan="8">Secondary (Centaline)</td></tr><tr><td>Tier-1 average</td><td>10.4%</td><td>-4.2%</td><td>-12.2%</td><td>-12.7%</td><td>-12.5%</td><td>1.2%</td><td>-39.4%</td></tr><tr><td>Beijing</td><td>14.3%</td><td>5.3%</td><td>-11.4%</td><td>-13.5%</td><td>-13.3%</td><td>2.7%</td><td>-36.4%</td></tr><tr><td>Shanghai</td><td>14.3%</td><td>-5.9%</td><td>-11.8%</td><td>-13.3%</td><td>-13.1%</td><td>4.2%</td><td>-36.9%</td></tr><tr><td>Guangzhou</td><td>12.6%</td><td>-3.9%</td><td>-11.4%</td><td>-13.7%</td><td>-14.5%</td><td>-2.2%</td><td>-41.0%</td></tr><tr><td>Shenzhen</td><td>0.5%</td><td>-12.1%</td><td>-14.1%</td><td>-10.1%</td><td>-9.2%</td><td>0.1%</td><td>-43.1%</td></tr></table>

Source: NBS, Centraline

# 70-city home price index

Figure 3: 70-city primary and secondary home price M/M trend  
![](images/7c726fe85f9a966ca5faa198150aa909e36eba5d210df97b75eed56c38e03c9c.jpg)  
Note: nationwide easing is marked as green.
Source: NBS

Figure 4: NBS 70-city home price index – primary M/M growth by tier  
![](images/2bc80d1a635afecd155945bb78a16b722d6b4820ce8974746c7057dc4801ec52.jpg)  
Source: NBS

Figure 5: NBS 70-city price index – % of cities with home price increment (primary)  
![](images/068cd7fc29bc55fd8505dbc3690c70b77dc70dfccd705734727995eaf4353817.jpg)

Figure 6: NBS 70-city price index – % of cities with home price increment (secondary)  
![](images/21cb67ab526593369b9529b9ad7e3ebf8c2612a909c190a624e7b170016236ab.jpg)  
Source: NBS

Table 3: 70-city price index (primary) – top 15 cities' M/M growth

<table><tr><td></td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>LTM</td></tr><tr><td>Wuxi</td><td>-0.2%</td><td>-0.5%</td><td>-0.3%</td><td>-0.6%</td><td>-1.0%</td><td>-0.2%</td><td>-0.2%</td><td>-0.4%</td><td>-0.2%</td><td>-0.4%</td><td>0.0%</td><td>0.3%</td><td>-3.7%</td></tr><tr><td>Zhengzhou</td><td>-0.6%</td><td>-0.4%</td><td>-0.6%</td><td>-0.8%</td><td>-0.6%</td><td>-0.9%</td><td>-0.4%</td><td>-0.2%</td><td>-0.1%</td><td>-0.1%</td><td>-0.2%</td><td>-0.1%</td><td>-5.0%</td></tr><tr><td>Hangzhou</td><td>-0.3%</td><td>0.4%</td><td>0.3%</td><td>0.1%</td><td>-0.2%</td><td>-0.3%</td><td>-0.3%</td><td>0.2%</td><td>0.2%</td><td>0.4%</td><td>0.5%</td><td>0.3%</td><td>1.3%</td></tr><tr><td>Jinan</td><td>-0.3%</td><td>-0.6%</td><td>-0.4%</td><td>-0.7%</td><td>-0.4%</td><td>-0.2%</td><td>-0.4%</td><td>-0.3%</td><td>-0.1%</td><td>-0.2%</td><td>-0.1%</td><td>-0.1%</td><td>-3.8%</td></tr><tr><td>Fuzhou</td><td>-0.5%</td><td>0.0%</td><td>-0.4%</td><td>-0.6%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.7%</td><td>-0.5%</td><td>-0.3%</td><td>-0.4%</td><td>-0.2%</td><td>-5.5%</td></tr><tr><td>Beijing</td><td>0.0%</td><td>-0.4%</td><td>0.2%</td><td>-0.1%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.0%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td><td>-2.0%</td></tr><tr><td>Hefei</td><td>-0.1%</td><td>0.2%</td><td>0.0%</td><td>0.1%</td><td>0.3%</td><td>0.0%</td><td>0.1%</td><td>0.0%</td><td>0.1%</td><td>0.0%</td><td>0.1%</td><td>-0.4%</td><td>0.4%</td></tr><tr><td>Tianjin</td><td>-0.3%</td><td>-0.5%</td><td>-0.6%</td><td>-0.7%</td><td>-0.4%</td><td>-0.6%</td><td>-0.8%</td><td>-0.4%</td><td>-0.3%</td><td>0.0%</td><td>-0.1%</td><td>-0.1%</td><td>-4.8%</td></tr><tr><td>Wuhan</td><td>-0.7%</td><td>-0.5%</td><td>-0.4%</td><td>-0.6%</td><td>-0.5%</td><td>0.0%</td><td>0.1%</td><td>0.1%</td><td>-0.5%</td><td>0.0%</td><td>0.2%</td><td>0.1%</td><td>-2.7%</td></tr><tr><td>Nanjing</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>-0.7%</td><td>0.2%</td><td>0.0%</td><td>-0.4%</td><td>0.3%</td><td>-0.3%</td><td>0.3%</td><td>-0.4%</td><td>0.2%</td><td>-2.5%</td></tr><tr><td>Shanghai</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.2%</td><td>0.3%</td><td>0.4%</td><td>0.2%</td><td>0.3%</td><td>3.0%</td></tr><tr><td>Guangzhou</td><td>-0.3%</td><td>-0.2%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.2%</td><td>-2.8%</td></tr><tr><td>Xiamen</td><td>-0.6%</td><td>-0.5%</td><td>-0.7%</td><td>-0.4%</td><td>-0.3%</td><td>-0.5%</td><td>0.1%</td><td>0.1%</td><td>-0.2%</td><td>-0.1%</td><td>0.2%</td><td>0.3%</td><td>-2.6%</td></tr><tr><td>Chengdu</td><td>-0.2%</td><td>-0.2%</td><td>-0.6%</td><td>-1.0%</td><td>-0.7%</td><td>-0.7%</td><td>-0.6%</td><td>-0.3%</td><td>-0.3%</td><td>-0.2%</td><td>-0.1%</td><td>-0.3%</td><td>-5.2%</td></tr><tr><td>Shenzhen</td><td>-0.6%</td><td>-0.4%</td><td>-1.0%</td><td>-0.7%</td><td>-0.9%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.1%</td><td>0.4%</td><td>0.3%</td><td>-3.8%</td></tr><tr><td>Average</td><td>-0.3%</td><td>-0.3%</td><td>-0.4%</td><td>-0.5%</td><td>-0.4%</td><td>-0.4%</td><td>-0.3%</td><td>-0.1%</td><td>-0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>-2.6%</td></tr></table>

Source: NBS

Table 4: 70-city price index (secondary) – top 15 cities' M/M growth

<table><tr><td></td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>LTM</td></tr><tr><td>Wuxi</td><td>-0.7%</td><td>-0.8%</td><td>-0.5%</td><td>-1.0%</td><td>-0.5%</td><td>-0.8%</td><td>-0.7%</td><td>-0.5%</td><td>0.2%</td><td>0.0%<

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
