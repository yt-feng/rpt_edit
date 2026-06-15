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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Consumer Connection: Online Brand Tracker: May-26: Divergent 618 performance across most sectors; Cosmetics led, IMF/White Goods

We summarize the May updates of our Online Brand Tracker within. Key highlights:

1. Category performance: In May-26, we observe weak performance for consumer categories - With Tmall/Taobao/JD combined, Women's clothing was flat yoy while all other categories recorded a yoy decline. Sports shoes/Beauty/Supplements/Dairy/Sportswear/Small kitchen appliances/IMF/Beer/Pet Foods/White goods registered

-2%/-4%/-6%/-9%/-11%/-18%/-19%/-22%/-22%/-31% yoy declines. Note: Tracker data suggest a meaningful re-base in Beauty and Supplements for Tmall/Taobao numbers in 2025 Jan - May.

Considering Douyin/Tmall/Taobao/JD combined, we saw Beauty GMV growing at 14% yoy in May, accelerating vs. 11% in April, partially helped by a softer Women's Day in 1Q, along with increasing subsidies from platforms and local governments. At the same time, aggregate GMV for core brands (Exhibit 10) for

Sportswear/Condiments grew at 14%/47% yoy in May, accelerating vs. April at 9%/34%. Other categories recorded deceleration/decline, with Dairy/Women's Clothing/Pet Foods/Beer/IMF/White Goods at 3%/-1%/-8%/-8%/-24%/-33% yoy for core brands in May (Pet Food using industry yoy) vs. 11%/1%/18%/1%/-23%/-35% in April.

## 2. Domestic vs. MNC brands:

In Cosmetics, data show a rebound in local brands while MNCs continuing to outperform. We think the acceleration was partially helped by a softer Women's Day in 1Q, along with increasing subsidies from platforms and local governments. Local brands that rebounded were Forest Cabin/Botanee/Shanghai Jahwa/MGP/Proya/Shanghai Chicmax/Giant Biogene, recording 110%/43%/27%/22%/8%/7%/6% yoy GMV growth, while Bloomage/Yatsen saw GMV decline by 19%/36% yoy. For MNCs, Estee Lauder (EL)/L'Oreal/Shiseido delivered 36%/16%/11% yoy GMV growth, while LG H&H/Amore Corp/Kose were under pressure at -34%/-31%/-22% yoy. Estee Lauder group outperformed in the higher segment, while L'Oreal group was driven by dermocosmetics, albeit mass-market brands faced local brands' competition.

Besides accelerating in May and solid growth for key covered brands/western brands in phase I (see our 618 phase I pulse check: Beauty GMV is tracking well with likely improving ROI), for Jun 1-8 on Douyin, we note an ongoing robust profile for

Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Michelle Cheng

+852-2978-6631 | michelle.cheng@gs.com GS (Asia) L.L.C.

Sho Kawano

+81(3)4587-9905 |
sho.kawano@gs.com
GS Japan Co., Ltd.

Leaf Liu

+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

Nicolas Yi

+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

western MNCs with L'Oreal and EL Group at 50%+ yoy while local brands are mixed: Mao Geping is catching up at 60%+ yoy Jun-to-date, uplifting its 618-to date yoy to 40%+ yoy. Giant is accelerating on an easier base at 13% yoy Jun-to-date. To reflect the full picture, for the first 25 days of 618 (May 15 - June 8) on Douyin, Forest Cabin led with triple-digit% LFL growth, partly due to an easier base, followed by Proya/Botanee/MGP/Giant at 64%/51%/43%/20% LFL growth.

In Sportswear, looking at May data across Tmall, JD, and Douyin, we see an overall divergent brand performance in May, with Labor Day demand soft but 618 shopping festival promotion brought support for certain brands. We flag that due to cadence of the 618, promotion may diverge across brands; we suggest combining May - Jun sales to assess overall performance. In May, several outdoor names such as Arc'teryx and Descente, as well as niche premium brand Lulu saw deceleration in May partially on a high base, while adidas, Li Ning, Anta, Fila, Bosideng, Salomon accelerated from Apr possibly on 618 shopping festival promotion. We also flag that brands have been executing omni-channel strategies in both online (e.g.; emerging channels like Dewu) and offline, suggesting the sales data collected by data vendors may not reconcile with actual growth.

Outperforming brands (May): Estee Lauder, Winona, Forest Cabin, Fancl, Nongfu, Haidilao

Underperforming brands (May): Nutrilon, Timage, QuadHA, Mead Johnson, Wyeth, Midea

## Relevant reads:

China Cosmetics: Monthly tracker: May-26: accelerating versus 1Q; local brands rebound likely on subsidies; MNCs continue to be strong June to date

Asia Pacific Textile, Apparel & Footwear: Monthly Tracker: OEM May trends mixed; Pou Sheng slightly moderated

China Consumer Durables: Appliance Tracker: Apr 2026: Weakening domestic demand and exports resuming growth with mixed performance across products, 618 in focus

China IP Retailer and Toy Tracker: May update: Pop Mart China online growth decelerated with higher base; Miniso/Bloks accelerating IP/product launch

China Restaurants: Monthly Tracker: May update: Trends turn softer but divergence across brands; FMD high base effect kicking in

China Pet Food Monthly: May 2026: softer pricing causes sales to moderate; China Pet Foods GMV growth led

China Consumer Staples Cost Index Tracker: May 2026: PET cost easing but still high; Aluminum sequentially trended down

We would like to thank Molly Dai, Christina Liu, Cecilia Tang, Lily Qi, Keira Liu, Xinyu Ruan, and Carol Chen for their contributions to this report.

## Category performance

## Category trends (JD/Tmall/Taobao)

Baby and Supplements: Online sales growth of the IMF category declined by 19% yoy in May on Tmall/Taobao/JD combined, worsening vs. 1Q26 at an 11% yoy decline. Online sales of the Supplements category declined by 10% yoy in May vs. -8% yoy in 1Q26.

Cosmetics: With Tmall/Taobao/JD combined, Beauty online GMV declined 4% yoy in May, weakening from 1% yoy decline in 1Q26.

Consumer Durables: Sales growth remained under pressure yoy in May with relative outperformance of small kitchen appliances and RVC. Compared to Apr, most appliances categories showed a widened yoy decline, while RVC and wet dry vacuums recorded narrower decline.

Exhibit 1: In May-26, we observe weak performance for consumer categories - With Tmall/Taobao/JD combined, Women's clothing was flat yoy while all other categories recorded yoy declines. Sports shoes/Beauty/Supplements/Dairy/Sportswear/Small kitchen appliances/IMF/Beer/Pet Foods/White goods registered $-2\% / -4\% / -6\% / -9\% / -11\% / -18\% / -19\% / -22\% / -22\% / -31\%$ yoy decline. Note: Tracker data suggest a meaningful re-base for Beauty for Tmall/Taobao numbers in 2025 Jan - May.  
Snapshot of category sales growth (% yoy)

<table><tr><td rowspan="2">Category</td><td colspan="3">May-26</td><td colspan="3">Apr-26</td><td colspan="3">1Q26</td><td colspan="3">4Q25</td><td>3Q25</td><td>2Q25</td><td>1Q25</td></tr><tr><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td></td></tr><tr><td>Beer</td><td>-4%</td><td>-35%</td><td>-22%</td><td>-9%</td><td>-16%</td><td>-13%</td><td>-1%</td><td>-17%</td><td>-9%</td><td>-23%</td><td>5%</td><td>-10%</td><td>-7%</td><td>-4%</td><td>-1%</td></tr><tr><td>Dairy</td><td>-21%</td><td>11%</td><td>-9%</td><td>-2%</td><td>18%</td><td>6%</td><td>-38%</td><td>-24%</td><td>-33%</td><td>-38%</td><td>16%</td><td>-17%</td><td>n.a.</td><td>n.a.</td><td>-1%</td></tr><tr><td>IMF</td><td>-2%</td><td>-26%</td><td>-19%</td><td>14%</td><td>-24%</td><td>-14%</td><td>2%</td><td>-19%</td><td>-11%</td><td>-3%</td><td>7%</td><td>4%</td><td>4%</td><td>19%</td><td>5%</td></tr><tr><td>Skincare</td><td>5%</td><td>-17%</td><td>-4%</td><td>-3%</td><td>-7%</td><td>-4%</td><td>0%</td><td>-8%</td><td>-1%</td><td>-14%</td><td>12%</td><td>-7%</td><td>-4%</td><td>-15%</td><td>1%</td></tr><tr><td>Cosmetics</td><td>-9%</td><td></td><td></td><td>-3%</td><td></td><td></td><td>1%</td><td></td><td></td><td>-8%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sportswear</td><td>-15%</td><td>21%</td><td>-11%</td><td>2%</td><td>32%</td><td>6%</td><td>29%</td><td>-5%</td><td>26%</td><td>-7%</td><td>7%</td><td>-5%</td><td>6%</td><td>-3%</td><td>6%</td></tr><tr><td>Sports shoes</td><td>-3%</td><td>3%</td><td>-2%</td><td>-6%</td><td>-3%</td><td>-5%</td><td>7%</td><td>-15%</td><td>4%</td><td>-9%</td><td>11%</td><td>-4%</td><td>10%</td><td>2%</td><td>12%</td></tr><tr><td>Women&#x27;s clothing</td><td>-1%</td><td>19%</td><td>0%</td><td>16%</td><td>17%</td><td>16%</td><td>7%</td><td>-58%</td><td>8%</td><td>-4%</td><td>108%</td><td>-3%</td><td>-13%</td><td>-16%</td><td>-6%</td></tr><tr><td>White goods</td><td>-50%</td><td>-8%</td><td>-31%</td><td>-25%</td><td>-19%</td><td>-22%</td><td>-8%</td><td>-51%</td><td>-15%</td><td>-18%</td><td>5%</td><td>-3%</td><td>4%</td><td>6%</td><td>5%</td></tr><tr><td>Small kitchen appliances</td><td>-15%</td><td>-23%</td><td>-18%</td><td>-2%</td><td>-8%</td><td>-4%</td><td>-2%</td><td>-27%</td><td>-1%</td><td>-19%</td><td>68%</td><td>-12%</td><td>8%</td><td>-9%</td><td>1%</td></tr><tr><td>Condiments</td><td>-12%</td><td>n.a.</td><td>n.a.</td><td>-19%</td><td>n.a.</td><td>n.a.</td><td>-16%</td><td>n.a.</td><td>n.a.</td><td>-20%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3%</td></tr><tr><td>Pet foods</td><td>-7%</td><td>-45%</td><td>-22%</td><td>14%</td><td>-3%</td><td>10%</td><td>0%</td><td>-60%</td><td>-5%</td><td>-11%</td><td>82%</td><td>-6%</td><td>-4%</td><td>3%</td><td>-3%</td></tr><tr><td>Supplements</td><td>-7%</td><td>-3%</td><td>-6%</td><td>6%</td><td>21%</td><td>11%</td><td>-9%</td><td>-8%</td><td>-8%</td><td>-21%</td><td>14%</td><td>-11%</td><td>5%</td><td>-11%</td><td>-7%</td></tr></table>

Sportswear, sports shoes, women's clothing are from Tmall only. For Condiments, we use Tmall+Taobao only as JD data is not meaningful on a yoy basis after the platform's category reclassification.  
Source: Moojing

## Category performance (Tmall/Taobao)

Exhibit 2: YoY monthly/quarterly trends at Tmall/Taobao in May

<table><tr><td>Category</td><td>Value</td><td>Volume</td><td>ASP</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td colspan="7">MF, Pat Foods, Supplements, Beauty and Jewelry</td></tr><tr><td colspan="7">MAY</td></tr><tr><td>Jul-25</td><td>11%</td><td>-2%</td><td>13%</td><td>Jul-25</td><td>-9%</td><td>-10%</td></tr><tr><td>Aug-25</td><td>-3%</td><td>-8%</td><td>6%</td><td>Aug-25</td><td>0%</td><td>-5%</td></tr><tr><td>Sep-25</td><td>1%</td><td>-4%</td><td>6%</td><td>Sep-25</td><td>-13%</td><td>-1%</td></tr><tr><td>Oct-25</td><td>-13%</td><td>-21%</td><td>10%</td><td>Oct-25</td><td>-21%</td><td>-12%</td></tr><tr><td>Nov-25</td><td>-1%</td><td>1%</td><td>-2%</td><td>Nov-25</td><td>-14%</td><td>-8%</td></tr><tr><td>Oct-Nov-25</td><td>-6%</td><td>-10%</td><td>4%</td><td>Oct-Nov-25</td><td>-11%</td><td>-10%</td></tr><tr><td>Dec-25</td><td>7%</td><td>3%</td><td>4%</td><td>Dec-25</td><td>-16%</td><td>-8%</td></tr><tr><td>Jan-26</td><td>12%</td><td>19%</td><td>-6%</td><td>Jan-26</td><td>4%</td><td>23%</td></tr><tr><td>Feb-26</td><td>-7%</td><td>-15%</td><td>9%</td><td>Feb-26</td><td>-10%</td><td>-4%</td></tr><tr><td>Jan-Feb-26</td><td>3%</td><td>3%</td><td>1%</td><td>Jan-Feb-26</td><td>-3%</td><td>10%</td></tr><tr><td>Mar-26</td><td>-1%</td><td>4%</td><td>-5%</td><td>Mar-26</td><td>5%</td><td>4%</td></tr><tr><td>Apr-26</td><td>14%</td><td>-14%</td><td>33%</td><td>Apr-26</td><td>14%</td><td>0%</td></tr><tr><td>May-26</td><td>-2%</td><td>-4%</td><td>2%</td><td>May-26</td><td>-7%</td><td>-1%</td></tr><tr><td>1Q25</td><td>11%</td><td>-13%</td><td>28%</td><td>1Q25</td><td>-19%</td><td>-19%</td></tr><tr><td>Mar-25</td><td>-7%</td><td>-14%</td><td>7%</td><td>Mar-25</td><td>-7%</td><td>-14%</td></tr><tr><td>3Q25</td><td>2%</td><td>-5%</td><td>8%</td><td>3Q25</td><td>-7%</td><td>-5%</td></tr><tr><td>4Q25</td><td>-3%</td><td>-6%</td><td>4%</td><td>4Q25</td><td>-11%</td><td>-6%</td></tr><tr><td>1Q26</td><td>2%</td><td>3%</td><td>-1%</td><td>1Q26</td><td>0%</td><td>8%</td></tr><tr><td colspan="7">Supplements</td></tr><tr><td>Jul-25</td><td>4%</td><td>-13%</td><td>18%</td><td>Jul-25</td><td>-10%</td><td>-23%</td></tr><tr><td>Aug-25</td><td>0%</td><td>34%</td><td>-25%</td><td>Aug-25</td><td>-2%</td><td>-16%</td></tr><tr><td>Sep-25</td><td>-3%</td><td>27%</td><td>-24%</td><td>Sep-25</td><td>-11%</td><td>-16%</td></tr><tr><td>Oct-25</td><td>2%</td><td>-12%</td><td>16%</td><td>Oct-25</td><td>-16%</td><td>-25%</td></tr><tr><td>Nov-25</td><td>-35%</td><td>-29%</td><td>-9%</td><td>Nov-25</td><td>-14%</td><td>-14%</td></tr><tr><td>Oct-Nov-25</td><td>-21%</td><td>-21%</td><td>2%</td><td>Oct-Nov-25</td><td>-15%</td><td>-20%</td></tr><tr><td>Dec-25</td><td>-19%</td><td>-21%</td><td>2%</td><td>Dec-25</td><td>-7%</td><td>-15%</td></tr><tr><td>Jan-Feb-26</td><td>-17%</td><td>-18%</td><td>2%</td><td>Jan-Feb-26</td><td>-1%</td><td>-3%</td></tr><tr><td>Mar-26</td><td>8%</td><td>2%</td><td>6%</td><td>Mar-26</td><td>1%</td><td>-3%</td></tr><tr><td>Apr-26</td><td>6%</td><td>-14%</td><td>24%</td><td>Apr-26</td><td>-3%</td><td>-16%</td></tr><tr><td>May-26</td><td>-7%</td><td>-6%</td><td>-2%</td><td>May-26</td><td>5%</td><td>7%</td></tr><tr><td>1Q25</td><td>-20%</td><td>-20%</td><td>0%</td><td>1Q25</td><td>-5%</td><td>-15%</td></tr><tr><td>2Q25</td><td>-22%</td><td>-20%</td><td>-2%</td><td>2Q25</td><td>-23%</td><td>-28%</td></tr><tr><td>3Q25</td><td>0%</td><td>17%</td><td>-12%</td><td>3Q25</td><td>-8%</td><td>-18%</td></tr><tr><td>4Q25</td><td>-21%</td><td>-21%</td><td>2%</td><td>4Q25</td><td>-14%</td><td>-19%</td></tr><tr><td>1Q26</td><td>-9%</td><td>-11%</td><td>3%</td><td>1Q26</td><td>0%</td><td>-3%</td></tr><tr><td colspan="7">Color makeup</td></tr><tr><td>Jul-25</td><td>-6%</td><td>-29%</td><td>31%</td><td></td><td></td><td></td></tr><tr><td>Aug-25</td><td>3%</td><td>-24%</td><td>35%</td><td></td><td></td><td></td></tr><tr><td>Sep-25</td><td>-8%</td><td>-20%</td><td>15%</td><td></td><td></td><td></td></tr><tr><td>Oct-25</td><td>-7%</td><td>-19%</td><td>15%</td><td></td><td></td><td></td></tr><tr><td>Nov-25</td><td>-13%</td><td>-19%</td><td>7%</td><td></td><td></td><td></td></tr><tr><td>Oct-Nov-25</td><td>-10%</td><td>-19%</td><td>11%</td><td></td><td></td><td></td></tr><tr><td>Dec-25</td><td>-2%</td><td>-6%</td><td>5%</td><td></td><td></td><td></td></tr><tr><td>Jan-Feb-26</td><td>4%</td><td>4%</td><td>0%</td><td></td><td></td><td></td></tr><tr><td>Mar-26</td><td>-4%</td><td>-12%</td><td>10%</td><td></td><td></td><td></td></tr><tr><td>Apr-26</td><td>-3%</td><td>-16%</td><td>16%</td><td></td><td></td><td></td></tr><tr><td>May-26</td><td>-9%</td><td>-8%</td><td>-1%</td><td></td><td></td><td></td></tr><tr><td>1Q25</td><td>-8%</td><td>-25%</td><td>22%</td><td></td><td></td><td></td></tr><tr><td>2Q25</td><td>-18%</td><td>-35%</td><td>26%</td><td></td><td></td><td></td></tr><tr><td>3Q25</td><td>-4%</td><td>-24%</td><td>26%</td><td></td><td></td><td></td></tr><tr><td>4Q25</td><td>-8%</td><td>-16%</td><td>9%</td><td></td><td></td><td></td></tr><tr><td>1Q26</td><td>1%</td><td>-2%</td><td>3%</td><td></td><td></td><td></td></tr><tr><td colspan="7">Packaged FAS and Alcohol</td></tr><tr><td colspan="7">Dairy</td></tr><tr><td>Jul-25</td><td>-34%</td><td>-27%</td><td>4%</td><td>Jul-25</td><td>-17%</td><td>-22%</td></tr><tr><td>Aug-25</td><td>-15%</td><td>-22%</td><td>9%</td><td>Aug-25</td><td>-17%</td><td>-24%</td></tr><tr><td>Sep-25</td><td>-15%</td><td>-15%</td><td>0%</td><td>Sep-25</td><td>-13%</td><td>-16%</td></tr><tr><td>Oct-25</td><td>-25%</td><td>-26%</td><td>2%</td><td>Oct-25</td><td>-7%</td><td>-25%</td></tr><tr><td>Nov-25</td><td>-51%</td><td>-43%</td><td>-14%</td><td>Nov-25</td><td>-27%</td><td>-26%</td></tr><tr><td>Oct-Nov-25</td><td>-41%</td><td>-36%</td><td>-6%</td><td>Oct-Nov-25</td><td>-19%</td><td>-25%</td></tr><tr><td>Dec-25</td><td>-31%</td><td>-23%</td><td>-11%</td><td>Dec-25</td><td>-21%</td><td>-14%</td></tr><tr><td>Jan-Feb-26</td><td>-40%</td><td>-32%</td><td>-12%</td><td>Jan-Feb-26</td><td>-14%</td><td>1%</td></tr><tr><td>Mar-26</td><td>-33%</td><td>-29%</td><td>-6%</td><td>Mar-26</td><td>-19%</td><td>-4%</td></tr><tr><td>Apr-26</td><td>-2%</td><td>-12%</td><td>11%</td><td>Apr-26</td><td>-19%</td><td>-12%</td></tr><tr><td>May-26</td><td>-21%</td><td>-6%</td><td>-17%</td><td>May-26</td><td>-12%</td><td>8%</td></tr><tr><td>1Q25</td><td>-1%</td><td>-3%</td><td>2%</td><td>1Q25</td><td>-3%</td><td>9%</td></tr><tr><td>2Q25</td><td>-24%</td><td>-31%</td><td>10%</td><td>2Q25</td><td>-14%</td><td>-27%</td></tr><tr><td>3Q25</td><td>-18%</td><td>-21%</td><td>4%</td><td>3Q25</td><td>-15%</td><td>-21%</td></tr><tr><td>4Q25</td><td>-38%</td><td>-32%</td><td>-8%</td><td>4Q25</td><td>-23%</td><td>-28%</td></tr><tr><td>1Q26</td><td>-38%</td><td>-31%</td><td>-10%</td><td>1Q26</td><td>-16%</td><td>0%</td></tr><tr><td colspan="7">Snacks (seedmuts)</td></tr><tr><td>Jul-25</td><td>-10%</td><td>-29%</td><td>26%</td><td>Jul-25</td><td>-27%</td><td>-58%</td></tr><tr><td>Aug-25</td><td>-11%</td><td>-36%</td><td>40%</td><td>Aug-25</td><td>-21%</td><td>-53%</td></tr><tr><td>Sep-25</td><td>-15%</td><td>-27%</td><td>15%</td><td>Sep-25</td><td>-17%</td><td>-40%</td></tr><tr><td>Oct-25</td><td>-16%</td><td>-35%</td><td>28%</td><td>Oct-25</td><td>-34%</td><td>-41%</td></tr><tr><td>Nov-25</td><td>-38%</td><td>-31%</td><td>-10%</td><td>Nov-25</td><td>-26%</td><td>-30%</td></tr><tr><td>Oct-Nov-25</td><td>-30%</td><td>-33%</td><td>7%</td><td>Oct-Nov-25</td><td>-35%</td><td>-46%</td></tr><tr><td>Dec-25</td><td>-34%</td><td>-25%</td><td>-13%</td><td>Dec-25</td><td>-23%</td><td>-37%</td></tr><tr><td>Jan-Feb-26</td><td>-25%</td><td>6%</td><td>-28%</td><td>Jan-Feb-26</td><td>-19%</td><td>-39%</td></tr><tr><td>Mar-26</td><td>-29%</td><td>-40%</td><td>19%</td><td>Mar-26</td><td>18%</td><td>29%</td></tr><tr><td>Apr-26</td><td>-7%</td><td>-18%</td><td>13%</td><td>Apr-26</td><td>11%</td><td>-3%</td></tr><tr><td>May-26</td><td>-7%</td><td>-2%</td><td>-5%</td><td>May-26</td><td>21%</td><td>45%</td></tr><tr><td>Jun-Feb-26</td><td>-10%</td><td>-10%</td><td>-1%</td><td>1Q25</td><td>32%</td><td>-55%</td></tr><tr><td>7Q25</td><td>-16%</td><td>-24%</td><td>11%</td><td>7Q25</td><td>-23%</td><td>-55%</td></tr><tr><td>8Q25</td><td>-13%</td><td>-30%</td><td>26%</td><td>8Q25</td><td>-22%</td><td>-51%</td></tr><tr><td>9Q25</td><td>-32%</td><td>-30%</td><td>0%</td><td>9Q25</td><td>-32%</td><td>-44%</td></tr><tr><td>1Q26</td><td>-26%</td><td>-8%</td><td>-18%</td><td>1Q26</td><td>-8%</td><

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
