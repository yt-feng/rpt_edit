你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# China Consumer Connection: Online Brand Tracker: Apr-26: Diverged performance before 618; Pet foods led; Beauty/IMF/White Goods lag

We summarize the Apr updates of our Online Brand Tracker. Note that we also updated the data for Tmall/Taobao in 1Q26 and 1Q25 following the rebase of data in 2025 Jan - Apr from our data vendor. Key highlights:

# 1. Category performance: In Apr-26, we observe diverged performance for consumer categories - With Tmall/Taobao/JD combined, Supplements/Pet foods/Women's clothing/Sportswear/Dairy registered $11\% / 10\% / 9\% / 6\% / 6\%$ yoy growth, while Sports shoes/Small kitchen appliances/Beer/White

goods/IMF/Beauty lagged at -5%/-4%/-13%/-22%/-14%/-23% yoy decline. Noted we saw meaningful re-base for pet foods, white goods and Dairy for Tmall/Taobao numbers in 2025 Jan - Apr.

# 2. Domestic vs. MNC brands:

In cosmetics, We saw continued divergence across channels and brands in Apr, with Douyin remaining the key growth engine while Tmall/Taobao stayed under pressure and JD was mixed. Among local brands, Shanghai Jahwa/MGP/Forest Cabin delivered the strongest momentum in Apr, at 53%/36%/23% yoy respectively, mainly driven by Douyin or JD. Other domestic brands remained soft, with

# Proya/Giant Biogene/Shanghai Chicmax/Yatsen/Bloomage down

18%/16%/21%/29%/13% yoy respectively in Apr. For MNCs, L'Oreal/Estee Lauder finished Apr at 3%/4% yoy respectively, supported by Douyin, while Shiseido/LG H&H/Amore/Kose was under pressure, down 8%/50%/29%/27% yoy respectively in Apr.

# In sportswear, we see broad-based moderation versus 1Q26, mainly reflecting unfavorable weather and demand pull-forward during the CNY spending season.

Among the brands, several outdoor names such as Arc'teryx and Salomon, as well as niche premium brand Lululemon, saw more meaningful deceleration in April, likely due in part to a higher base. While most sports brands moderated, adidas, Fila, Puma, Xtep, Asics, and ON appeared relatively more resilient. We also note that brands have been executing omni-channel strategies in both online (e.g., emerging channels like Dewu) and offline, suggesting that sales here may not reflect the full picture.

Outperforming brands (Apr): Fila, Pop Mart, Forest Cabin, MGP, Wanpy, Zeal

Underperforming brands (Apr): Whoo, Midea, Nutrilon, Firmus

# Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

# Michelle Cheng

+852-2978-6631 | michelle.cheng@gs.com GS (Asia) L.L.C.

# Sho Kawano

+81(3)4587-9905 |
sho.kawano@gs.com
GS Japan Co., Ltd.

# Leaf Liu

+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

# Nicolas Yi

+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities Company Limited

# Relevant reads:

China Cosmetics: Monthly tracker: Apr-26: Growth slowdown before 618 though lapping on an easy base; MGP and Shanghai Jahwa led

Asia Pacific Textile, Apparel & Footwear: Monthly Tracker: OEM a mixed bag; Pou Sheng accelerated on an easy base

China Consumer Durables: Appliance Tracker: Mar 2026: Mixed domestic growth and exports pull-back on a high base; incorporate robotic lawn mowers data starting March

China IP Retailer and Toy Tracker: Apr update: Pop Mart US credit card sales under pressure with meaningfully higher base; Miniso accelerated IP launch around holiday

China Restaurants: Monthly Tracker: Apr update: sequentially better performance supported by spring break, yet decelerated into Labor Day

China Staples: Pet Food Monthly: Apr 2026: April accelerated vs Q1; China Pet Foods led; Gambol back for growth

China Consumer Staples Cost Index Tracker: Apr 2026: Packaging material cost trended high: PET up $54\% / 59\%$ YTD/yoy; Aluminum up $24\%$ yoy

We would like to thank Molly Dai, Christina Liu, Cecilia Tang, Lily Qi, Keira Liu, Xinyu Ruan, and Carol Chen for their contributions to this report.

# Category performance

# Category trends (JD/Tmall/Taobao)

Baby and supplements: Online sales growth of IMF category declined by 22% yoy in Apr on Tmall/Taobao/JD combined, worsened vs 1Q26 at 11% yoy decline. Online sales of supplements category declined by 14% yoy in Apr vs -17% yoy in 1Q26.

Cosmetics: With Tmall/Taobao/JD combined, beauty online GMV declined $23\%$ yoy in Apr, weakening from $-6\%$ yoy decline in 1Q26.

Consumer durables: Sales growth remained under pressure yoy in Apr. Compared to Mar, major (kitchen) appliances, projectors and furniture showed similar yoy declines. Small kitchen appliances showed narrower yoy decline compared to Mar, while cleaning appliances recorded widened yoy decrease in Apr.

Exhibit 1: In Apr-26, we observe diverged performance for consumer categories - With Tmall/Taobao/JD combined, Supplements/Pet foods/Women's clothing/Sportswear/Dairy registered $11\% / 10\% / 9\% / 6\% / 6\%$ yoy growth, while Sports shoes/Small kitchen appliances/Beer/White goods/IMF/Beauty lagged at $-5\% / -4\% / -13\% / -22\% / -14\% / -23\%$ yoy decline.   
Snapshot of category sales growth (% yoy) 

<table><tr><td rowspan="2">Category</td><td colspan="3">Apr-26</td><td colspan="3">1Q26</td><td colspan="3">4Q25</td><td>3Q25</td><td>2Q25</td><td>1Q25</td><td>4Q24</td><td>3Q24</td><td>2Q24</td><td>1Q24</td></tr><tr><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Tmall/Tmall+ Taobao</td><td>JD</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td><td>Total (Tmall+ Taobao+JD)</td></tr><tr><td>Beer</td><td>-9%</td><td>-16%</td><td>-13%</td><td>-1%</td><td>-17%</td><td>-9%</td><td>-23%</td><td>5%</td><td>-10%</td><td>-7%</td><td>-4%</td><td>-1%</td><td>6%</td><td>12%</td><td>1%</td><td>6%</td></tr><tr><td>Dairy</td><td>-2%</td><td>18%</td><td>6%</td><td>-38%</td><td>-24%</td><td>-33%</td><td>-38%</td><td>16%</td><td>-17%</td><td>n.a.</td><td>n.a.</td><td>-1%</td><td>5%</td><td>-12%</td><td>-11%</td><td>15%</td></tr><tr><td>IMF</td><td>14%</td><td>-24%</td><td>-14%</td><td>2%</td><td>-19%</td><td>-11%</td><td>-3%</td><td>7%</td><td>4%</td><td>4%</td><td>19%</td><td>5%</td><td>3%</td><td>10%</td><td>9%</td><td>5%</td></tr><tr><td>Skincare</td><td>-28%</td><td>-7%</td><td>-23%</td><td>-6%</td><td>-8%</td><td>-6%</td><td>-14%</td><td>12%</td><td>-7%</td><td>-4%</td><td>-1%</td><td>1%</td><td>1%</td><td>-9%</td><td>-3%</td><td>-18%</td></tr><tr><td>Cosmetics</td><td>-23%</td><td></td><td></td><td>-4%</td><td></td><td></td><td>-8%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sportswear</td><td>2%</td><td>32%</td><td>6%</td><td>29%</td><td>-5%</td><td>26%</td><td>-7%</td><td>7%</td><td>-5%</td><td>6%</td><td>-3%</td><td>6%</td><td>-3%</td><td>-3%</td><td>-12%</td><td>-6%</td></tr><tr><td>Sports shoes</td><td>-6%</td><td>-3%</td><td>-5%</td><td>7%</td><td>-15%</td><td>4%</td><td>-9%</td><td>11%</td><td>-4%</td><td>10%</td><td>2%</td><td>12%</td><td>-12%</td><td>-8%</td><td>2%</td><td>-1%</td></tr><tr><td>Women&#x27;s clothing</td><td>4%</td><td>17%</td><td>9%</td><td>32%</td><td>-58%</td><td>25%</td><td>30%</td><td>108%</td><td>17%</td><td>4%</td><td>7%</td><td>-6%</td><td>-5%</td><td>-6%</td><td>-5%</td><td>0%</td></tr><tr><td>White goods</td><td>-25%</td><td>-19%</td><td>-22%</td><td>-8%</td><td>-51%</td><td>-15%</td><td>-18%</td><td>5%</td><td>-3%</td><td>4%</td><td>6%</td><td>5%</td><td>10%</td><td>14%</td><td>-4%</td><td>-4%</td></tr><tr><td>Small kitchen appliances</td><td>-2%</td><td>-8%</td><td>-4%</td><td>-2%</td><td>-27%</td><td>-1%</td><td>-19%</td><td>68%</td><td>-12%</td><td>8%</td><td>-9%</td><td>1%</td><td>2%</td><td>-17%</td><td>-6%</td><td>-20%</td></tr><tr><td>Condiments</td><td>-19%</td><td>n.a.</td><td>n.a.</td><td>-16%</td><td>n.a.</td><td>n.a.</td><td>-20%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>-3%</td><td>-8%</td><td>-17%</td><td>9%</td><td>9%</td></tr><tr><td>Pet foods</td><td>14%</td><td>-3%</td><td>10%</td><td>0%</td><td>-60%</td><td>-5%</td><td>-11%</td><td>82%</td><td>-6%</td><td>-4%</td><td>4%</td><td>-3%</td><td>-6%</td><td>-13%</td><td>-9%</td><td>2%</td></tr><tr><td>Supplements</td><td>6%</td><td>21%</td><td>11%</td><td>-9%</td><td>-8%</td><td>-8%</td><td>-21%</td><td>14%</td><td>-11%</td><td>5%</td><td>-10%</td><td>-7%</td><td>-1%</td><td>-29%</td><td>-12%</td><td>-11%</td></tr></table>

Sportswear, sports shoes, women's clothing are from Tmall only. For condiments, we use Tmall+Taobao only as JD data is not meaningful on a yoy basis after the platform's category reclassification.   
Source: Moojing

# Category performance (Tmall/Taobao)

Exhibit 2: YoY monthly/quarterly trends at Tmall/Taobao in Apr 

<table><tr><td>Category</td><td>Value</td><td>Volume</td><td>ASP</td><td>Value</td><td>Volume</td><td>ASP</td></tr><tr><td colspan="7">IMF, Pet Foods, Supplements, Beauty and Jewelry</td></tr><tr><td>IMF</td><td></td><td></td><td></td><td>Pet foods</td><td></td><td></td></tr><tr><td>Jul-25</td><td>11%</td><td>-2%</td><td>13%</td><td>Jul-25</td><td>-9%</td><td>-10%</td></tr><tr><td>Aug-25</td><td>-3%</td><td>-8%</td><td>6%</td><td>Aug-25</td><td>-1%</td><td>-5%</td></tr><tr><td>Sep-25</td><td>1%</td><td>-4%</td><td>6%</td><td>Sep-25</td><td>-13%</td><td>-1%</td></tr><tr><td>Oct-25</td><td>-13%</td><td>-21%</td><td>10%</td><td>Oct-25</td><td>-9%</td><td>-12%</td></tr><tr><td>Nov-25</td><td>-1%</td><td>1%</td><td>-2%</td><td>Nov-25</td><td>-14%</td><td>-8%</td></tr><tr><td>Oct-Nov-25</td><td>-6%</td><td>-10%</td><td>4%</td><td>Oct-Nov-25</td><td>-11%</td><td>-10%</td></tr><tr><td>Dec-25</td><td>7%</td><td>3%</td><td>4%</td><td>Dec-25</td><td>-11%</td><td>6%</td></tr><tr><td>Jan-26</td><td>12%</td><td>19%</td><td>-6%</td><td>Jan-26</td><td>4%</td><td>-23%</td></tr><tr><td>Feb-26</td><td>-7%</td><td>-15%</td><td>9%</td><td>Feb-26</td><td>-10%</td><td>-4%</td></tr><tr><td>Jan-Feb-26</td><td>3%</td><td>3%</td><td>1%</td><td>Jan-Feb-26</td><td>-3%</td><td>10%</td></tr><tr><td>Mar-26</td><td>-1%</td><td>4%</td><td>-5%</td><td>Mar-26</td><td>5%</td><td>4%</td></tr><tr><td>Apr-26</td><td>14%</td><td>14%</td><td>33%</td><td>Apr-26</td><td>14%</td><td>0%</td></tr><tr><td>1Q25</td><td>11%</td><td>-13%</td><td>28%</td><td>1Q25</td><td>-19%</td><td>-19%</td></tr><tr><td>2Q25</td><td>-7%</td><td>-14%</td><td>7%</td><td>2Q25</td><td>-7%</td><td>-14%</td></tr><tr><td>3Q25</td><td>2%</td><td>-5%</td><td>8%</td><td>3Q25</td><td>-7%</td><td>-5%</td></tr><tr><td>4Q25</td><td>-3%</td><td>-6%</td><td>4%</td><td>4Q25</td><td>-11%</td><td>-6%</td></tr><tr><td>1Q26</td><td>2%</td><td>3%</td><td>-1%</td><td>1Q26</td><td>0%</td><td>8%</td></tr><tr><td>Supplements</td><td></td><td></td><td></td><td>Shiclare</td><td></td><td></td></tr><tr><td>Jul-25</td><td>4%</td><td>-13%</td><td>18%</td><td>Jul-25</td><td>-10%</td><td>-23%</td></tr><tr><td>Aug-25</td><td>0%</td><td>34%</td><td>-25%</td><td>Aug-25</td><td>-2%</td><td>-16%</td></tr><tr><td>Sep-25</td><td>-3%</td><td>27%</td><td>-24%</td><td>Sep-25</td><td>-11%</td><td>-16%</td></tr><tr><td>Oct-25</td><td>2%</td><td>-12%</td><td>16%</td><td>Oct-25</td><td>-16%</td><td>-35%</td></tr><tr><td>Nov-25</td><td>-35%</td><td>-29%</td><td>-9%</td><td>Nov-25</td><td>-14%</td><td>-14%</td></tr><tr><td>Oct-Nov-25</td><td>-21%</td><td>-21%</td><td>2%</td><td>Oct-Nov-25</td><td>-15%</td><td>-20%</td></tr><tr><td>Dec-25</td><td>-19%</td><td>-21%</td><td>2%</td><td>Dec-25</td><td>-7%</td><td>-15%</td></tr><tr><td>Jan-Feb-26</td><td>-17%</td><td>-18%</td><td>2%</td><td>Jan-Feb-26</td><td>-4%</td><td>-3%</td></tr><tr><td>Mar-26</td><td>8%</td><td>2%</td><td>6%</td><td>Mar-26</td><td>-9%</td><td>-7%</td></tr><tr><td>Apr-26</td><td>6%</td><td>-14%</td><td>24%</td><td>Apr-26</td><td>-28%</td><td>-29%</td></tr><tr><td>1Q25</td><td>-20%</td><td>-20%</td><td>0%</td><td>1Q25</td><td>1%</td><td>-13%</td></tr><tr><td>2Q25</td><td>-20%</td><td>-19%</td><td>-1%</td><td>2Q25</td><td>-3%</td><td>-16%</td></tr><tr><td>3Q25</td><td>0%</td><td>17%</td><td>-12%</td><td>3Q25</td><td>-8%</td><td>-18%</td></tr><tr><td>4Q25</td><td>-21%</td><td>-21%</td><td>2%</td><td>4Q25</td><td>-14%</td><td>-19%</td></tr><tr><td>1Q26</td><td>-9%</td><td>-11%</td><td>3%</td><td>1Q26</td><td>-4%</td><td>-4%</td></tr><tr><td>Color makeup</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Jul-25</td><td>-6%</td><td>-29%</td><td>31%</td><td></td><td></td><td></td></tr><tr><td>Aug-25</td><td>3%</td><td>-24%</td><td>35%</td><td></td><td></td><td></td></tr><tr><td>Sep-25</td><td>-8%</td><td>-20%</td><td>15%</td><td></td><td></td><td></td></tr><tr><td>Oct-25</td><td>-7%</td><td>-19%</td><td>15%</td><td></td><td></td><td></td></tr><tr><td>Nov-25</td><td>-13%</td><td>-19%</td><td>7%</td><td></td><td></td><td></td></tr><tr><td>Sep-25</td><td>-10%</td><td>-19%</td><td>11%</td><td></td><td></td><td></td></tr><tr><td>Oct-Nov-25</td><td>-10%</td><td>-19%</td><td>11%</td><td></td><td></td><td></td></tr><tr><td>Dec-25</td><td>-2%</td><td>-6%</td><td>5%</td><td></td><td></td><td></td></tr><tr><td>Oct-Nov-25</td><td>-41%</td><td>-36%</td><td>6%</td><td>Oct-Nov-25</td><td>-19%</td><td>-25%</td></tr><tr><td>Mar-26</td><td>-12%</td><td>-16%</td><td>5%</td><td></td><td></td><td></td></tr><tr><td>Apr-26</td><td>-23%</td><td>-26%</td><td>5%</td><td></td><td></td><td></td></tr><tr><td>1Q25</td><td>-3%</td><td>-21%</td><td>23%</td><td></td><td></td><td></td></tr><tr><td>2Q25</td><td>-7%</td><td>-30%</td><td>32%</td><td></td><td></td><td></td></tr><tr><td>3Q25</td><td>-4%</td><td>-24%</td><td>26%</td><td></td><td></td><td></td></tr><tr><td>4Q25</td><td>-8%</td><td>-16%</td><td>9%</td><td></td><td></td><td></td></tr><tr><td>1Q26</td><td>-4%</td><td>-6%</td><td>2%</td><td></td><td></td><td></td></tr><tr><td colspan="7">Packaged F&amp;B and Alcohol</td></tr><tr><td>Dairy</td><td></td><td></td><td></td><td>Condiments</td><td></td><td></td></tr><tr><td>Jul-25</td><td>-24%</td><td>-27%</td><td>4%</td><td>Jul-25</td><td>-17%</td><td>-22%</td></tr><tr><td>Aug-25</td><td>-15%</td><td>-22%</td><td>9%</td><td>Aug-25</td><td>-17%</td><td>-24%</td></tr><tr><td>Sep-25</td><td>-15%</td><td>-15%</td><td>0%</td><td>Sep-25</td><td>-13%</td><td>-16%</td></tr><tr><td>Oct-25</td><td>-25%</td><td>-26%</td><td>2%</td><td>Oct-25</td><td>-7%</td><td>-25%</td></tr><tr><td>Nov-25</td><td>-51%</td><td>-43%</td><td>-14%</td><td>Nov-25</td><td>-27%</td><td>-26%</td></tr><tr><td>Oct-Nov-25</td><td>-41%</td><td>-36%</td><td>6%</td><td>Oct-Nov-25</td><td>-19%</td><td>-25%</td></tr><tr><td>Dec-25</td><td>-31%</td><td>-23%</td><td>-11%</td><td>Dec-25</td><td>-21%</td><td>-14%</td></tr><tr><td>Jan-Feb-26</td><td>-40%</td><td>-32%</td><td>-12%</td><td>Jan-Feb-26</td><td>-14%</td><td>1%</td></tr><tr><td>Mar-26</td><td>-33%</td><td>-29%</td><td>-6%</td><td>Mar-26</td><td>-19%</td><td>-4%</td></tr><tr><td>Apr-26</td><td>-2%</td><td>-12%</td><td>11%</td><td>Apr-26</td><td>-19%</td><td>-12%</td></tr><tr><td>1Q25</td><td>-1%</td><td>-3%</td><td>2%</td><td>1Q25</td><td>-3%</td><td>9%</td></tr><tr><td>2Q25</td><td>-24%</td><td>-31%</td><td>10%</td><td>2Q25</td><td>-14%</td><td>-27%</td></tr><tr><td>3Q25</td><td>-18%</td><td>-21%</td><td>4%</td><td>3Q25</td><td>-15%</td><td>-21%</td></tr><tr><td>4Q25</td><td>-38%</td><td>-32%</td><td>-8%</td><td>4Q25</td><td>-20%</td><td>-22%</td></tr><tr><td>1Q26</td><td>-38%</td><td>-31%</td><td>-10%</td><td>1Q26</td><td>-16%</td><td>0%</td></tr><tr><td>Snacks (seeds/notes)</td><td></td><td></td><td></td><td>Water</td><td></td><td></td></tr><tr><td>Jul-25</td><td>10%</td><td>-29%</td><td>26%</td><td>Jul-25</td><td>-27%</td><td>-58%</td></tr><tr><td>Aug-25</td><td>-11%</td><td>-36%</td><td>40%</td><td>Aug-25</td><td>-21%</td><td>-53%</td></tr><tr><td>Sep-25</td><td>-15%</td><td>-27%</td><td>15%</td><td>Sep-25</td><td>-17%</td><td>-40%</td></tr><tr><td>Oct-25</td><td>-16%</td><td>-35%</td><td>28%</td><td>Oct-25</td><td>-34%</td><td>-41%</td></tr><tr><td>Nov-25</td><td>-38%</td><td>-31%</td><td>-10%</td><td>Nov-25</td><td>-36%</td><td>-50%</td></tr><tr><td>Oct-Nov-25</td><td>-30%</td><td>-33%</td><td>7%</td><td>Oct-Nov-25</td><td>-35%</td><td>-46%</td></tr><tr><td>Dec-25</td><td>-34%</td><td>-25%</td><td>-13%</td><td>Dec-25</td><td>-23%</td><td>-37%</td></tr><tr><td>Jan-Feb-26</td><td>-25%</td><td>6%</td><td>-28%</td><td>Jan-Feb-26</td><td>-24%</td><td>-42%</td></tr><tr><td>Mar-26</td><td>-29%</td><td>-40%</td><td>19%</td><td>Mar-26</td><td>6%</td><td>21%</td></tr><tr><td>Apr-26</td><td>-7%</td><td>-18%</td><td>13%</td><td>Apr-26</td><td>-7%</td><td>-12%</td></tr><tr><td>1Q25</td><td>-10%</td><td>-10%</td><td>-1%</td><td>1Q25</td><td>12%</td><td>-18%</td></tr><tr><td>2Q25</td><td>-15%</td><td>-22%</td><td>10%</td><td>2Q25</td><td>19%</td><td>-53%</td></tr><tr><td>3Q25</td><td>-13%</td><td>-30%</td><td>26%</td><td>3Q25</td><td>-22%</td><td>-51%</td></tr><tr><td>4Q25</td><td>-32%</td><td>-30%</td><td>0%</td><td>4Q25</td><td>-32%</td><td>-44%</td></tr><tr><td>1Q26</td><td>-26%</td><td>-8%</td><td>-18%</td><td>1Q26</td><td>-15%</td><td>-25%</td></tr><tr><td>Wine</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Jul-25</td><td>-8%</td><td>-17%</td><td>7%</td><td>Jul-25</td><td>-28%</td><td>-36%</td></tr><tr><td>Aug-25</td><td>10%</td><td>-4%</td><td>9%</td><td>Aug-25</td><td>-25%</td><td>-31%</td></tr><tr><td>Sep-25</td><td>4%</td><td>-6%</td><td>9%</td><td>Sep-25</td><td>-10%</td><td>-27%</td></tr><tr><td>Oct-25</td><td>-39%</td><td>-31%</td><td>9%</td><td>Oct-25</td><td>-36%</td><td>-32%</td></tr><tr><td>Nov-25</td><td>-23%</td><td>-21%</td><td>9%</td><td>Nov-25</td><td>-23%</td><td>-25%</td></tr><tr><td>Oct-Nov-25</td><td>-30%</td><td>-26%</td><td>9%</td><td>Oct-Nov-25</td><td>-29%</td><td>-29%</td></tr><tr><td>Dec-25</td><td>-20%</td><td>4%</td><td>9%</td><td>Dec-25</td><td>-4%</td><td>1%</td></tr><tr><td>Jan-Feb-26</td><td>-27%</td><td>-13%</td><td>8%</td><td>Jan-Feb-26</td><td>-10%</td><td>7%</td></tr><tr><td>Mar-26</td><td>25%</td><td>60%</td><td>9%</td><td>Mar-26</td><td>32%</td><td>33%</td></tr><tr><td>Apr-26</td><td>0%</td><td>0%</td><td>11%</td><td>Apr-26</td><td>-9%</td><td>-10%</td></tr><tr><td>1Q24</td><td>-16%</td><td>19%</td><td>-30%</td><td>1Q24</td><td>16%</td><td>97%</td></tr><tr><td>2Q24</td><td>-12%</td><td>23%</td><td>-28%</td><td>2Q24</td><td>6%</td><td>55%</td></tr><tr><td>3Q24</td><td>-25%</td><td>13%</td><td>-34%</td><td>3Q24</td><td>15%</td><td>53%</td></tr><tr><td>4Q24</td><td>-12%</td><td>7%</td><td>-18%</td><td>4Q24</td><td>12%</td><td>5%</td></tr><tr><t

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
