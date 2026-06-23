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
- 已识别机构名：`Bernstein`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# U.S. Multi Industry & Electrical Equipment

# Data Center Chillers (1/3): Primer and free cooling economics

![](images/2d92f063532cd3e658f9ba79f9196f04f9412a3f6e9087271ea60c73c83f965d.jpg)  
Varun Govindaraj

+1 917 344 8543

varun.govindaraj@bernsteinsg.com

Specialist Sales

![](images/33c4e8f7ea650f0e27750430b3c96823f452fbefde675035cf30f6511742303f.jpg)

Steve Song

+1 917 344 8401

steve.song@bernsteinsg.com

Chillers are a critical part of data center cooling infrastructure both in liquid-cooled and air-cooled environments. They are responsible for creating chilled facility water that then pumps to CDUs to extract heat from the coolant or to CRAHs to reduce the temperature of air blowing through the data center. We size this as a \~\$8B market in 2026 (fully loaded cost including installation and ancillaries), but the growth outlook can vary significantly based on how you think chiller penetration changes. Assuming no such changes (our base case), we project a \~20% CAGR for the market with 2030 estimated at \~\$16.5B.

We often hear debates of when it makes sense to use air-cooled vs. water cooled units. As a quick primer, both types of chillers operate using a refrigerant cycle, but air-cooled units reject heat from the refrigerant into ambient air, while water-cooled units reject to another water loop (either a cooling tower or a dry cooler). Air-cooled units are lower capex, but much less energy efficient. Water-cooled units need more upfront investment and consume large quantities of water (if a cooling tower is used), but tend to consume less power for the same tonnage. So it really is a sensitivity analysis of what you think your operating conditions and input costs will be when making the decision.

To illustrate this, we looked at how much it would cost to run an 800 ton chiller (roughly 2.5 MW) - assuming it was air-cooled or water-cooled. When the compressor of the chiller ran 24X7, annual operating costs were roughly 25% higher for an air-cooled chiller vs. a water-cooled unit, implying a \~3 year payback on the cost differential. So water-cooled units are always better, right?

It is not that simple. This dynamic can change quite drastically when you take free-cooling into account. Free-cooling is a when the ambient temperature drops enough for the data center operator to tone down (and in some cases switch off) the compressor in the chiller. It's a bit of a misnomer, the cooling isn't entirely free (you still need some power) but it's a fraction of what you'd need with the compressor running at 100%.

Energy consumption drops significantly for both air-cooled and water-cooled units. However, water costs stay relatively constant for water-cooled chillers (assuming a cooling tower is used). So as you spend more time in a free cooling environment, you may run into a situation where it is actually cheaper to operate an air-cooled chiller vs. a water-cooled chiller. This could be why we are hearing people talk about air-cooled chillers gaining share in the market.

We also spent some time benchmarking chiller offerings by key players available or announced in the market (like we did with our earlier primer on CDUs). We do not find the differences to be as stark; while there are some variations between companies, and they all have their own edge, we think these variations in specs are far outweighed by the overwhelming supply shortage and demand we are seeing for chillers today.

This is the first of our three part series on chillers. In part two, we will discuss “chiller gate” in more depth and in part three dive into the economics of servicing a chiller unit.

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2"></td><td colspan="4">18 Jun 2026</td><td>TTM</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td></td><td></td><td rowspan="2">Closing Price</td><td rowspan="2">Price Target</td><td rowspan="2">Rel. Perf.</td><td rowspan="2">Cur</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td><td rowspan="2">2025A</td><td rowspan="2">2026E</td><td rowspan="2">2027E</td></tr><tr><td>Ticker</td><td>Rating</td><td>Cur</td></tr><tr><td>TT (Trane)</td><td>O</td><td>USD</td><td>483.40</td><td>550.00</td><td>(10.5)%</td><td>USD</td><td>13.06</td><td>14.96</td><td>17.61</td><td>37.0</td><td>32.3</td><td>27.4</td></tr><tr><td>CARR (Carrier)</td><td>M</td><td>USD</td><td>71.81</td><td>75.00</td><td>(22.9)%</td><td>USD</td><td>2.57</td><td>2.81</td><td>3.20</td><td>27.9</td><td>25.6</td><td>22.4</td></tr><tr><td>JCI (Johnson Controls)</td><td>O</td><td>USD</td><td>144.82</td><td>176.00</td><td>14.3%</td><td>USD</td><td>3.78</td><td>5.06</td><td>6.04</td><td>38.3</td><td>28.6</td><td>24.0</td></tr><tr><td>VRT (Vertiv)</td><td>O</td><td>USD</td><td>333.05</td><td>416.00</td><td>154.0%</td><td>USD</td><td>4.20</td><td>6.52</td><td>9.21</td><td>79.3</td><td>51.1</td><td>36.2</td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate TT Outperform with a target price of \$550.

We rate CARR Market-perform with a target price of \$75.

We rate JCI Outperform with a target price of \$176.

We rate VRT Outperform with a target price of \$416.

Annual Operating costs (water + power)

EXHIBIT 1: When should you buy an air-cooled vs. water-cooled chiller?  
Annual OpEx differential in an 800-ton chiller (air-cooled vs. water-cooled)  
![](images/6af81d57c3f770314d309d6a71cb98ebdc48008641b3f1cac027d02a602b1952.jpg)  
If cooling tower needs to be active (which we think it does) to enable free cooling in a water-cooled chiller, water usage makes an air-cooled chiller seem more attractive in free-cooling heavy environments  
However, this is based on national averages for power and water costs; reality-will look quite different based on the region of operation  
Source: Bernstein Analysis and Estimates

EXHIBIT 2: Trade-offs by chiller type and regional variation  
Deciding between air-cooled and water-cooled chillers based on geography  
![](images/fae5fd5c704dd345de906797de48765297d59874bf561e1132daa94ee0b96b87.jpg)  
Note: Power costs are \$10.25, \$6.26, \$6.7, \$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from EIA; Water costs are \$12.5, \$11, \$20, \$10 for NoVa, DFW, ATL, ORD pulled from regional sites (actual industrial rates may vary); Numbers by region assume an 800-ton chiller operating

![](images/b978e33c91f1e72028954058aa51fc15486e68053709be44eeb7ba2c6f1fdf57.jpg)

Source: Bernstein Analysis

## What is a chiller?

A chiller is a piece of equipment, which, as the name suggests, reduces the temperature of a stream of matter (usually a liquid). In the context of a data center, chillers are useful not only for liquid cooling (to cool the FWS) but also in air cooled environments where cold water flows to a CRAH to reduce the temperature of air that flows through it. Any chiller runs through a refrigerant compression cycle; this has four stages of operation as described below.

Evaporator: The warm liquid that needs to be chilled exchanges heat with cold liquid refrigerant in the chiller. This refrigerant picks up heat from the warm water and cools it, evaporating in the process.

Compressor: The most energy intensive part of a chiller. A compressor (scroll, screw, centrifugal) compresses the gaseous refrigerant, increasing its temperature. This is done to create a higher temperature gradient which makes heat transfer easier at a later stage.

Condenser: The hot, high-pressure, gaseous refrigerant comes into thermal contact with another stream of heat rejection (usually cool water in the case of a water-cooled chiller or ambient air in the case of an air-cooled chiller). The difference in temperature between the hot refrigerant and the cool heat sink facilitates heat rejection from the former to the latter. The refrigerant temperature lowers, and it condenses as a result (reverting to a liquid state).

Expansion valve: High pressure, liquid refrigerant passes through an expansion valve. This rapidly reduces pressure, which in turn reduces the temperature of the refrigerant (but keeps it in a liquid state). From here, the liquid refrigerant flows back to the evaporator and the cycle repeats.

EXHIBIT 3: Physics of Chiller Operation  
![](images/6dcd6a142214db143eef56f7fa8128117ab3a1866af7651a02faa444d10bed68.jpg)

## Types of chillers

In general, comparisons are made between two types of chillers - air-cooled and water-cooled. The differences due to how the condenser rejects heat to the environment; if air is used it is air-cooled, if water is used (either through a dry cooler, or more commonly a cooling tower) it is water-cooled. There are some performance trade-offs from choosing one type of chiller vs. another. Air-cooled units are much less energy efficient (\~30% worse than water-cooled unit) but have lower up front capex and do not require any water to operate. In contrast, water cooled chillers are much better at heat transfer to the environment, so the compressor needs to do less work reducing their energy bill. But they do need water in most cases (although some dry cooler configurations solve that issue) which can shift the balance (especially in free-cooling environments where power usage for both air-cooled and water-cooled chillers drops significantly while water consumption stays relatively constant). We explore this cost-benefit analysis later in our note.

EXHIBIT 4: Air-cooled vs. Water-cooled Chillers  
![](images/0f1aed57bc5d063446552c0c445400e6387c556380d09312d8d6b8a48e68ad16.jpg)  
Source: Bernstein Analysis and Estimates, Company Reports

More as a point of clarification, we would also like to highlight the different types of compressors in chillers. OEMs regularly talk about scroll vs. screw vs. centrifugal chillers, and it is worth understanding how they differ. Scroll chillers generally do not see data center applications; they are small, simple, silent units with limited ability to scale. Screw compressors are mid-sized units and see data center deployment. They are more complex and better at handling variable loads. Finally, centrifugal compressors see deployment in large scale data center environments; most OEM flagship products launched today are centrifugal chillers. These are the most complex, and require significant engineering to stand up but also deliver the most cooling power.

EXHIBIT 5: Comparison of compressors  
![](images/ab239313df6ab8afd5d2f07392bf67d9d1a3c260fa1d157cced00457e55052da.jpg)  
Source: Images from Atlas Copco and Engineeringlearn.com

Most appropriate for data center loads

Source: Bernstein Analysis

## How big is the market?

We have seen a wide dispersion of market sizes for chillers. Part of it also depends on what you are referencing - just the unit, or all the ancillary pieces that come with it? We have used a top-down estimate to size the overall market using GW added as a starting point. While we do have a base / bull / bear case for chillers in the exhibit below, these are based on variation in chiller penetration (not in terms of GW added). Our approach is as follows.

First, we look at new GW capacity being added each year. This creates a thermal baseline in terms of power consumed. Most of that power is released from chips, with an additional factor (assumed to be 1.2x in our model) to account for power wastage and headroom for safety. Next, we assume a cost per ton of \$1,500. This is a blend of both air cooled and water cooled chiller capex and includes the unit, engineering + commissioning + any supporting equipment that is needed (pumps, cooling towers, etc.). Finally, we multiply this by the share of GW that are cooled using chillers (75% in 2026 since it is how the majority of cooling takes place, but with base, bear, and bull cases for chillers based on how that could evolve). We size the fully loaded market for chillers at \~\$8B in 2026, growing to \~\$16.5B in 2030 assuming chillers continue to cool the same share of DC compute. In our bear case, where dry coolers steal share, the number drops to \~\$9B, while in the bull case where chillers gain share we size it at \~\$20B. This implies annual growth rates of \~20%, <5%, and >25% in the base, bear, and bull cases respectively.

Naturally, this model is sensitive to any assumptions you may have (especially GW added which can vary substantially between sources). The benefit of our approach is that one can relatively easily modify these assumptions and see what the market would be accordingly.

EXHIBIT 6: Chiller Market Size (Fully loaded) by Scenario  
![](images/f13686c112d0e19e53cd5822f750545784bd4c284241ea4147abee1da00b615e.jpg)  
Source: Bernstein Analysis and Estimates, McKinsey Data Center Model (for GW), CSE mag for cost per ton with 3% annual inflation

## Air vs. Water ... what's better?

Both air-cooled and water-cooled chillers have clear niches. Generally, air-cooled chillers make more sense when power costs are low (because they consume more power at a given tonnage vs. water-cooled chillers) or if water costs are high / water is limited / unavailable. In contrast, water-cooled chillers make sense in water-rich environments / when water costs are low or when power costs are high (since they are more energy efficient). When running at 100%, the extra cost of using water in a water-cooled chiller is more than offset by the savings in power.

However, this dynamic does change when you start to leverage free cooling (especially if you have a water-side economizer). In this environment, the compressor is switched off / used less, significantly reducing power consumption. But water consumption from a cooling tower continues, which keeps water costs relatively constant. At very high free cooling ratios, this could mean that the power savings from using a water-cooled chiller are actually offset by the cost of water. Given the increased focus on

water management in data centers (some counties have even capped the amount of water a data center can consume) we think it could help make the case for air-cooled chillers long-term over water-cooled units. The only exception is when the water-cooled chiller uses a dry cooler vs. a cooling tower (which JCI now advertises as possible with their new York HT chiller unit, although this likely comes with higher power costs due to higher lift).

EXHIBIT 7: Water costs can overtake power in modes with high free cooling (assumes use of cooling tower)  
![](images/ca49a0e6511e9ffd654e54e277e0ff7b47f88a5b9e5df89db7c9574d77fd763d.jpg)  
However, this is based on national averages for power and water costs; reality-will look quite different based on the region of operation

## Source: Bernstein Analysis and Estimates

There is some variation by geography, largely dependent on the ration of power to water costs. In areas like Atlanta, where water costs seem to be high, air-cooled outperform water cooled chillers with as little as 50% free cooling while in most other key data center markets in the US, it takes more free cooling before the attractiveness flips. We are hearing from players in the space that air-cooled chillers are gaining popularity over water-cooled units (although the latter still remains important).

EXHIBIT 8: Air-cooled vs. Water-cooled; when do you deploy it?  
![](images/6dc0dcbafa47114b80c660b0ff34571a50ce2bb71c35263a2e396404bad31e4d.jpg)  
Note: Power costs are \$10.25, \$6.26, \$6.7, \$9.19 per 100 kWh for NoVa, DFW, ATL, ORD from EIA; Water costs are \$12.5, \$11, \$20, \$10 for NoVa, DFW, ATL, ORD pulled from regional sites (actual industrial rates may vary); Numbers by region assume an 800-ton chiller operating

Source: Bernstein Analysis and Estimates, EIA

We reached our estimates on water consumption using EPA guidelines on cooling towers; $\sim 1.8$ gallon per ton-hour of cooling as evaporation and another $\sim 0.5$ gallons per ton-hour for blow down (purge of liquid to eliminate dissolved solids).

EXHIBIT 9: How much water does a water-cooled chiller use?  
![](images/7a90ec667bdc679adbcc90e7fe4ed83bc6b9f9d9a4b633d2d2a830d3c4a3dfe7.jpg)  
Source: EPA, Bernstein Analysis and Estimates

## Competitor benchmarking of products

Broadly, we think Trane, JCI, and Carrier all have strong products. On the air-cooled side, JCI and Carrier have announced new products in 2026 (we have not been able to find anything from Trane). As a result, some metrics (restart time, capacity per square foot) seem to lag flagship products from competitors (although it is very likely Trane will announce a new product at some point). Vertiv is taking a different positioning to the market with a trim cooler; it still has a chiller in it but seems to operate like a dry cooler for most of the time (enabling lower energy costs). Visually, it looks like an air cooled chiller. Vertiv does have a separate chiller line as well, but we could not find it displayed on their US website.

On the water cooled side, all three major chiller players have their own areas of differentiation. Trane has the biggest product at 21MW. JCI advertises its lift of $110^{0}\mathrm{F}$ which enables use of a dry cooler even in hot climates and eliminates water usage. Carrier talks about a short restart time under 3 minutes. Many of these products still do not have full spec sheets available, so we will need to wait and see before passing a verdict. But given the current market we are in, it really doesn't matter all that much. These are all great products (unlike with CDUs where we saw meaningful differentiation among Vertiv, Trane, Carrier, JCI) and given the commentary on demand, we expect these companies to continue to see strong order booking and the broader chiller space to remain capacity-constrained.

EXHIBIT 10: Comparison of flagship air-cooler chiller specs.  
Data Center Chiller Comparison

<table><tr><td rowspan="2">Company / Product</td><td colspan="4">Air-Cooled</td></tr><tr><td>TT</td><td>JCI</td><td>CARR</td><td>VRT</td></tr><tr><td>Model number</td><td>TCAB850</td><td>YDAM</td><td>AquaEdge 30CF</td><td>CoolLoop Trim Cooler1</td></tr><tr><td>Announce date</td><td>Mar 2025</td><td>Feb 2026</td><td>Feb 2026</td><td>Mar 2025</td></tr><tr><td>Capacity</td><td>Up to 3 MW</td><td>Up to 3.5 MW</td><td>“More than” 3 MW</td><td>Up to 3 MW</td></tr><tr><td>Pump type</td><td>Centrifugal</td><td>Centrifugal</td><td>Centrifugal</td><td>Unclear</td></tr><tr><td>Bearing type</td><td>M

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
