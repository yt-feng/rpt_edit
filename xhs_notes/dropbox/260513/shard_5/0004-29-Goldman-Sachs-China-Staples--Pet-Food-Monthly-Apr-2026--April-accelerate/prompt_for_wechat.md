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
# China Staples: Pet Food Monthly: Apr 2026: April accelerated vs Q1; China Pet Foods led; Gambol back for growth

In this monthly pet food tracker, we monitor: 1) domestic demand for pet food; 2) ASP trajectory and competitive dynamics within product/channel mix shifts; and 3) overseas demand and our monthly cost tracker. Note that we also updated the data in 1Q26 and 1Q25 following the rebase of data in 2025 Jan - Apr from our data vendor.

Overview:

1) In terms of GMV in Apr, Tmall/Taobao/JD/Douyin combined recorded 18% yoy growth, and came in stronger vs 1Q26 which was 9% yoy. Our covered local brands showed strong performance. Our covered domestic brands accelerated to +36% yoy vs +22% yoy in 1Q26. Global brands returned to growth with 20% yoy vs 4% decline in 1Q26 where Royal Canin outperformed on both Tmall/Douyin channel at 78% overall yoy. China Pet Foods led local brands at +64% yoy, thanks to Wanpy/Toptrees/Zeal at 67%/68%/38%, and we continue to see stronger customer acquisition for Toptrees as shown in Exhibit 14 and Exhibit 15; Gambol returned to growth at 12% yoy, with Myfoodie at 8% albeit Fregate came in negative at 1%. For Petpal, Meatyway grew 33% in Apr, accelerated vs 13% growth in 1Q26.   
2) On product discounts and Douyin ROI, we saw greater non-livestreaming sales mix (Exhibit 19) with shift towards merchants & E-shelf in Apr (Exhibit 18). The premiumization trend continues, as we saw top brands such as Rosy Fresh and Toptrees leading fan attraction on a yoy basis in Apr (Exhibit 15).   
3) Overseas demand and cost tracker: US total dog and cat food imports declined at 5% yoy in Mar vs 3% yoy growth in Feb. On costs, Apr saw higher raw material costs, with higher starch/PET/chicken/corn prices at 7%/47%/5%/6% yoy growth, resulting in our pet food cost index up by 6-8% for April. And we note RMB appreciation is likely to lead to FX losses among pet OEMs as well.

# Within our Pet Foods coverage, we are Neutral on China Pet Foods/Gambol.

While we acknowledge China Pet Food's rising domestic momentum and strong global supply chain to drive wallet share gains, we expect pressures on profitability in domestic market with heightened competition and overseas market with tariff sharing, FX losses and raw material headwinds. While Gambol maintains a leading position in China, we are Neutral rated on the stock on valuation and fierce competition in the premium-priced cat food segment. We maintain a Sell rating on Petpal, given pressures on domestic and overseas profitability and weaker bargaining power.

# Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

# Leaf Liu

+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

# Christina Liu

+852-2978-6983 | christina.liu@gs.com
GS (Asia) L.L.C.

Table of Contents 

<table><tr><td>Domestic online tracker</td><td>3</td></tr><tr><td>Overseas import demand</td><td>12</td></tr><tr><td>GS proprietary cost index</td><td>12</td></tr><tr><td>Disclosure Appendix</td><td>15</td></tr></table>

# Relevant reads:

China Consumer Staples: Pet food: 4Q25/1Q26 wrap: Results miss across the board; domestic competition to continue; d/g China Pet Foods to Neutral, Petpal to Sell

China Pet Foods (002891.SZ): First Take: 4Q25/1Q26 miss; fuels domestic growth but margin lower; 1Q26 overseas order rebound; Buy

Gambol Pet Group Co. (301498.SZ): Earnings Revision: 4Q25/1Q26 NP weak; In investment cycle to prioritize market share gain; Likely easier selling cost from 2H26; Neutral

Petpal Pet Nutrition Technology (300673.SZ): First take: FY25/1Q26: 4Q25 NI miss on weaker sales, fx loss; 1Q26 soft with margin pressure

Petpal Pet Nutrition Technology (300673.SZ): Post Holiday Consumer Tour: Gradual recovery in OEM/domestic orders while margins still under pressure; New Zealand factory to ramp up

Monthly Momentum of Pet Food Sector   
![](images/f9b629ca6ae7ec64f5d640453184142b2abafcd3a5f6a2c16e2c73519884572c.jpg)  
Leading domestic brands performance indicator

![](images/fa661f3b699bc28be0d86ec2444d8fa4ab2144d6b26799014e880b93960bc6d3.jpg)  
ASP trend indicator

![](images/79247a6a35747cc34e40303736900130ff8ac1107281a28bfd8fb9f59f273462.jpg)  
Douyin ROI

![](images/2c24beccb1c82e7e849a1dd1871e79754608dc8507a409fe50841c1e40e07f58.jpg)  
Overseas demand

![](images/36b2583edd89f9fce8f44628c337c49cd7e85f528bf7a51a5ecd4b311ac77457.jpg)  
Cost index   
Methodology: Red/Yellow/Green represents negative/neutral/positive for each indicator.

# Domestic online tracker

# Growth profile - Platform growth and Company growth

Exhibit 1: Category growth on Tmall, Taobao 

<table><tr><td></td><td>Apr-26</td><td>1Q26</td><td>4Q25</td><td>3Q25</td><td>2Q25</td><td>1Q25</td><td>2025</td></tr><tr><td>Category</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cat treats</td><td>7.9%</td><td>0.3%</td><td>-16.4%</td><td>-15.7%</td><td>-12.5%</td><td>-15.4%</td><td>-15.0%</td></tr><tr><td>Dog treats</td><td>-1.3%</td><td>-2.6%</td><td>-12.8%</td><td>-10.2%</td><td>-8.9%</td><td>-10.8%</td><td>-10.7%</td></tr><tr><td>Cat staple food</td><td>20.0%</td><td>0.6%</td><td>-9.4%</td><td>-3.0%</td><td>-4.2%</td><td>0.0%</td><td>-4.5%</td></tr><tr><td>Dog staple food</td><td>10.5%</td><td>-1.2%</td><td>-11.2%</td><td>-9.8%</td><td>-8.4%</td><td>-9.3%</td><td>-9.7%</td></tr><tr><td>Total</td><td>14.4%</td><td>-0.1%</td><td>-11.0%</td><td>-7.3%</td><td>-6.7%</td><td>-5.5%</td><td>-7.8%</td></tr></table>

Source: Moojing Market Intelligence, Data compiled by GS Global Investment Research

# Exhibit 2: Apr contributed around 8% of total annual GMV in 2025

Tmall/Taobao GMV distribution by month over 2020-2025

<table><tr><td rowspan="2" colspan="2"></td><td colspan="13">GMV contribution</td></tr><tr><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td><td></td></tr><tr><td rowspan="6">Pet food</td><td>2020</td><td>5%</td><td>6%</td><td>11%</td><td>6%</td><td>7%</td><td>10%</td><td>6%</td><td>8%</td><td>8%</td><td>8%</td><td>15%</td><td>9%</td><td></td></tr><tr><td>2021</td><td>8%</td><td>5%</td><td>7%</td><td>7%</td><td>7%</td><td>10%</td><td>7%</td><td>8%</td><td>8%</td><td>8%</td><td>16%</td><td>9%</td><td></td></tr><tr><td>2022</td><td>8%</td><td>6%</td><td>7%</td><td>7%</td><td>7%</td><td>12%</td><td>6%</td><td>7%</td><td>8%</td><td>8%</td><td>16%</td><td>9%</td><td></td></tr><tr><td>2023</td><td>6%</td><td>7%</td><td>8%</td><td>7%</td><td>6%</td><td>13%</td><td>7%</td><td>8%</td><td>8%</td><td>7%</td><td>16%</td><td>7%</td><td></td></tr><tr><td>2024</td><td>9%</td><td>6%</td><td>9%</td><td>8%</td><td>11%</td><td>6%</td><td>7%</td><td>7%</td><td>8%</td><td>11%</td><td>10%</td><td>8%</td><td></td></tr><tr><td>2025</td><td>9%</td><td>7%</td><td>10%</td><td>8%</td><td>10%</td><td>9%</td><td>6%</td><td>8%</td><td>7%</td><td>11%</td><td>9%</td><td>7%</td><td></td></tr></table>

Green shades denote positive divergence from median, with darker shades indicating higher difference from median.

Exhibit 3: China Pet Foods led in yoy growth in Apr-26; Gambol returned to growth and Petpal strengthened in April vs 1Q26 

<table><tr><td rowspan="2">Company brand GMV yoy growth</td><td colspan="4">Apr-26</td><td colspan="4">1Q26</td><td colspan="4">4Q25</td><td colspan="4">3Q25</td><td colspan="4">2Q25</td><td colspan="4">1Q25</td><td colspan="4">2025</td></tr><tr><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td><td>Tmall/Taobao</td><td>JD</td><td>Douyin</td><td>Total</td></tr><tr><td>Total Pet Foods</td><td>14%</td><td>-3%</td><td>33%</td><td>18%</td><td>0%</td><td>-27%</td><td>45%</td><td>9%</td><td>-11%</td><td>9%</td><td>53%</td><td>8%</td><td>-7%</td><td>6%</td><td>n.a.</td><td>n.a.</td><td>-7%</td><td>32%</td><td>n.a.</td><td>n.a.</td><td>-5%</td><td>-35%</td><td>n.a.</td><td>n.a.</td><td>7%</td><td>14%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Local brands - covered</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gambol</td><td>4%</td><td>48%</td><td>6%</td><td>12%</td><td>10%</td><td>-41%</td><td>3%</td><td>-1%</td><td>18%</td><td>16%</td><td>16%</td><td>17%</td><td>17%</td><td>16%</td><td>48%</td><td>27%</td><td>24%</td><td>-25%</td><td>73%</td><td>22%</td><td>19%</td><td>-26%</td><td>95%</td><td>23%</td><td>20%</td><td>-6%</td><td>49%</td><td>21%</td></tr><tr><td>Myfoodie</td><td>7%</td><td>35%</td><td>-5%</td><td>8%</td><td>3%</td><td>-60%</td><td>-10%</td><td>-14%</td><td>10%</td><td>5%</td><td>-2%</td><td>5%</td><td>-4%</td><td>1%</td><td>16%</td><td>3%</td><td>11%</td><td>-36%</td><td>44%</td><td>4%</td><td>1%</td><td>-30%</td><td>60%</td><td>5%</td><td>5%</td><td>-16%</td><td>24%</td><td>4%</td></tr><tr><td>Balance Nutrition</td><td>217%</td><td>-87%</td><td>174%</td><td>173%</td><td>132%</td><td>-57%</td><td>286%</td><td>187%</td><td>134%</td><td>-36%</td><td>564%</td><td>226%</td><td>125%</td><td>-17%</td><td>n.a.</td><td>n.a.</td><td>82%</td><td>-4%</td><td>n.a.</td><td>n.a.</td><td>67%</td><td>-44%</td><td>n.a.</td><td>n.a.</td><td>109%</td><td>-26%</td><td>n.a.</td><td>n.a.</td></tr><tr><td>Fregiate</td><td>-21%</td><td>121%</td><td>-7%</td><td>-1%</td><td>10%</td><td>51%</td><td>-12%</td><td>6%</td><td>22%</td><td>73%</td><td>16%</td><td>26%</td><td>94%</td><td>116%</td><td>87%</td><td>94%</td><td>65%</td><td>56%</td><td>108%</td><td>75%</td><td>90%</td><td>10%</td><td>218%</td><td>103%</td><td>51%</td><td>64%</td><td>74%</td><td>59%</td></tr><tr><td>China Pet Food</td><td>69%</td><td>150%</td><td>19%</td><td>64%</td><td>36%</td><td>67%</td><td>86%</td><td>54%</td><td>17%</td><td>72%</td><td>99%</td><td>45%</td><td>7%</td><td>19%</td><td>77%</td><td>25%</td><td>0%</td><td>27%</td><td>81%</td><td>21%</td><td>-7%</td><td>-35%</td><td>58%</td><td>-4%</td><td>5%</td><td>23%</td><td>82%</td><td>24%</td></tr><tr><td>Warpy</td><td>55%</td><td>92%</td><td>71%</td><td>67%</td><td>24%</td><td>5%</td><td>163%</td><td>44%</td><td>0%</td><td>11%</td><td>167%</td><td>28%</td><td>-7%</td><td>3%</td><td>148%</td><td>14%</td><td>-6%</td><td>11%</td><td>127%</td><td>13%</td><td>-14%</td><td>-44%</td><td>88%</td><td>-15%</td><td>-7%</td><td>-5%</td><td>140%</td><td>11%</td></tr><tr><td>Zeal</td><td>58%</td><td>15%</td><td>26%</td><td>38%</td><td>-13%</td><td>60%</td><td>35%</td><td>8%</td><td>-31%</td><td>58%</td><td>61%</td><td>0%</td><td>-28%</td><td>20%</td><td>43%</td><td>0%</td><td>-37%</td><td>138%</td><td>52%</td><td>4%</td><td>-8%</td><td>-62%</td><td>95%</td><td>1%</td><td>-27%</td><td>34%</td><td>59%</td><td>1%</td></tr><tr><td>Toplines</td><td>94%</td><td>340%</td><td>-19%</td><td>68%</td><td>93%</td><td>168%</td><td>48%</td><td>93%</td><td>59%</td><td>191%</td><td>69%</td><td>82%</td><td>53%</td><td>46%</td><td>50%</td><td>50%</td><td>24%</td><td>38%</td><td>66%</td><td>38%</td><td>11%</td><td>7%</td><td>28%</td><td>15%</td><td>40%</td><td>80%</td><td>57%</td><td>52%</td></tr><tr><td>Petpal</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Meatway</td><td>23%</td><td>93%</td><td>17%</td><td>33%</td><td>15%</td><td>15%</td><td>5%</td><td>13%</td><td>-6%</td><td>32%</td><td>10%</td><td>2%</td><td>7%</td><td>16%</td><td>58%</td><td>21%</td><td>32%</td><td>-40%</td><td>19%</td><td>11%</td><td>54%</td><td>-48%</td><td>61%</td><td>20%</td><td>15%</td><td>-17%</td><td>34%</td><td>11%</td></tr><tr><td>Covered - simple avg.</td><td>32%</td><td>97%</td><td>14%</td><td>36%</td><td>20%</td><td>14%</td><td>31%</td><td>22%</td><td>10%</td><td>40%</td><td>42%</td><td>21%</td><td>10%</td><td>17%</td><td>61%</td><td>24%</td><td>19%</td><td>-13%</td><td>57%</td><td>18%</td><td>22%</td><td>-36%</td><td>72%</td><td>13%</td><td>13%</td><td>0%</td><td>55%</td><td>19%</td></tr><tr><td>Nourse</td><td>64%</td><td>143%</td><td>356%</td><td>207%</td><td>9%</td><td>-3%</td><td>300%</td><td>112%</td><td>-23%</td><td>-11%</td><td>300%</td><td>65%</td><td>-11%</td><td>-18%</td><td>160%</td><td>39%</td><td>-30%</td><td>-32%</td><td>116%</td><td>0%</td><td>-5%</td><td>-43%</td><td>5%</td><td>-8%</td><td>-19%</td><td>-27%</td><td>143%</td><td>23%</td></tr><tr><td>Yanuan</td><td>8%</td><td>7%</td><td></td><td>-13%</td><td>-11%</td><td>-40%</td><td></td><td>-32%</td><td>-14%</td><td>51%</td><td></td><td>-7%</td><td>-28%</td><td>4%</td><td></td><td>-28%</td><td>-22%</td><td>-31%</td><td></td><td>-30%</td><td>-6%</td><td>-39%</td><td></td><td>-17%</td><td>-17%</td><td>-8%</td><td></td><td>-20%</td></tr><tr><td>Keres</td><td>-9%</td><td>-42%</td><td>13%</td><td>-15%</td><td>-14%</td><td>-53%</td><td>13%</td><td>-21%</td><td>-29%</td><td>24%</td><td>28%</td><td>-12%</td><td>-21%</td><td>2%</td><td>-32%</td><td>-17%</td><td>-10%</td><td>-46%</td><td>-19%</td><td>-23%</td><td>-20%</td><td>-37%</td><td>1%</td><td>-24%</td><td>-20%</td><td>-18%</td><td>-7%</td><td>-19%</td></tr><tr><td>Pure &amp; natural</td><td>32%</td><td>-89%</td><td>55%</td><td>0%</td><td>1%</td><td>-88%</td><td>47%</td><td>-10%</td><td>-19%</td><td>-11%</td><td>51%</td><td>-5%</td><td>-18%</td><td>-15%</td><td>95%</td><td>1%</td><td>-27%</td><td>-18%</td><td>36%</td><td>-16%</td><td>-3%</td><td>-48%</td><td>27%</td><td>-15%</td><td>-18%</td><td>-22%</td><td>51%</td><td>-10%</td></tr><tr><td>Honest bite</td><td>19%</td><td>-8%</td><td>-33%</td><td>-5%</td><td>0%</td><td>-38%</td><td>9%</td><td>-3%</td><td>8%</td><td>59%</td><td>16%</td><td>18%</td><td>32%</td><td>80%</td><td>45%</td><td>42%</td><td>24%</td><td>86%</td><td>103%</td><td>50%</td><td>76%</td><td>125%</td><td>62%</td><td>78%</td><td>30%</td><td>81%</td><td>52%</td><td>42%</td></tr><tr><td>Roay Fresh</td><td>66%</td><td>141%</td><td>46%</td><td>72%</td><td>18%</td><td>-276%</td><td>38%</td><td>53%</td><td>77%</td><td>82%</td><td>39%</td><td>69%</td><td>15%</td><td>83%</td><td>55%</td><td>31%</td><td>9%</td><td>22%</td><td>116%</td><td>25%</td><td>23%</td><td>-2%</td><td>167%</td><td>33%</td><td>31%</td><td>47%</td><td>75%</td><td>41%</td></tr><tr><td>Other local - simple avg.</td><td>30%</td><td>25%</td><td>87%</td><td>41%</td><td>0%</td><td>9%</td><td>81%</td><td>16%</td><td>0%</td><td>32%</td><td>87%</td><td>21%</td><td>-5%</td><td>23%</td><td>65%</td><td>12%</td><td>-9%</td><td>-3%</td><td>70%</td><td>1%</td><td>11%</td><td>-7%</td><td>52%</td><td>8%</td><td>-2%</td><td>9%</td><td>63%</td><td>10%</td></tr><tr><td>Global brands</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Royal Canin</td><td>75%</td><td>85%</td><td>81%</td><td>78%</td><td>34%</td><td>-18%</td><td>68%</td><td>22%</td><td>4%</td><td>36%</td><td>38%</td><td>17%</td><td>8%</td><td>9%</td><td>89%</td><td>11%</td><td>7%</td><td>-17%</td><td>186%</td><td>3%</td><td>21%</td><td>-18%</td><td>315%</td><td>11%</td><td>9%</td><td>3%</td><td>113%</td><td>11%</td></tr><tr><td>Instinct</td><td>1%</td><td>-99%</td><td>-27%</td><td>-40%</td><td>-6%</td><td>-82%</td><td>-97%</td><td>-32%</td><td>-37%</td><td>-29%</td><td>-92%</td><td>-38%</td><td>-28%</td><td>-14%</td><td>-24%</td><td>-24%</td><td>9%</td><td>-26%</td><td>86%</td><td>-2%</td><td>-1%</td><td>-7%</td><td>271%</td><td>2%</td><td>-16%</td><td>-21%</td><td>-8%</td><td>-17%</td></tr><tr><td>Orijlan</td><td>35%</td><td>21%</td><td>79%</td><td>35%</td><td>6%</td><td>-60%</td><td>175%</td><td>-2%</td><td>-5%</td><td>51%</td><td>61%</td><td>18%</td><td>-7%</td><td>-11%</td><td>-20%</td><td>-9%</td><td>-5%</td><td>-25%</td><td>82%</td><td>-6%</td><td>-21%</td><td>-15%</td><td>-5%</td><td>8%</td><td>0%</td><td>1%</td><td>33%</td><td>4%</td></tr><tr><td>Acania</td><td>37%</td><td>-98%</td><td>123%</td><td>7%</td><td>-1%</td><td>-60%</td><td>152%</td><td>-5%</td><td>-11%</td><td>65%</td><td>35%</td><td>11%</td><td>-12%</td><td>32%</td><td>-39%</td><td>-8%</td><td>5%</td><td>49%</td><td>37%</td><td>17%</td><td>36%</td><td>20%</td><td>4%</td><td>30%</td><td>2%</td><td>46%</td><td>10%</td><td>12%</td></tr><tr><td>Global brands - simple avg.</td><td>37%</td><td>-23%</td><td>64%</td><td>20%</td><td>8%</td><td>-55%</td><td>75%</td><td>-4%</td><td>-12%</td><td>31%</td><td>10%</td><td>2%</td><td>-10%</td><td>4%</td><td>2%</td><td>-8%</td><td>4%</td><td>-5%</td><td>98%</td><td>-3%</td><td>19%</td><td>-5%</td><td>146%</td><td>13%</td><td>-1%</td><td>7%</td><td>37%</td><td>2%</td></tr></table>

Source: Moojing Market Intelligence, Chanmama, Data compiled by GS Global Investment Research

Exhibit 4: Douyin channel mix increased in April vs 1Q26 for most brands 

<table><tr><td rowspan="2">Each channel GMV % of total GMV</td><td colspan="2">Apr-26</td><td colspan="2">1Q26</td><td colspan="2">4Q25</td><td colspan="2">3Q25</td><td colspan="2">2Q25</td><td colspan="2">1Q25</td><td colspan="2">2025</td><td colspan="2">2024</td></tr><tr><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td><td>Tmall/Taobao</td><td>Douyin</td></tr><tr><td colspan="17">Local brands</td></tr><tr><td>Gambol</td><td>57%</td><td>43%</td><td>59%</td><td>41%</td><td>64%</td><td>36%</td><td>55%</td><td>45%</td><td>62%</td><td>38%</td><td>61%</td><td>39%</td><td>60%</td><td>40%</td><td>66%</td><td>34%</td></tr><tr><td>Myfoodie</td><td>59%</td><td>41%</td><td>61%</td><td>39%</td><td>61%</td><td>39%</td><td>56%</td><td>44%</td><td>62%</td><td>38%</td><td>61%</td><td>39%</td><td>59%</td><td>41%</td><td>65%</td><td>35%</td></tr><tr><td>Balance Nutrition</td><td>35%</td><td>65%</td><td>39%</td><td>61%</td><td>43%</td><td>57%</td><td>42%</td><td>58%</td><td>35%</td><td>65%</td><td>52%</td><td>48%</td><td>42%</td><td>58%</td><td>65%</td><td>35%</td></tr><tr><td>Fr

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
