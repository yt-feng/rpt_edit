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
CHINA PROPERTY MONTHLY TRACKER

# Reinforced T-1 ASP resilience amid mixed May prints; Secondary listing vol picked up but still down yoy

## China Property

Finding the new balance of the China housing market; investing in the consolidators.

Explore >

![](images/d16e1db70188bca4246c32e37193f174b618068e7d5c004cc2f81575d2dc18c5.jpg)

May 70-city primary ASP decline pace was similar to Apr/Mar while secondary ASP decline widened sequentially, of which T1 remained strong; May primary sales (vol/val at -13%/-9% yoy) came slightly below/largely in-line with our expectation, and sluggish construction activities were moderately below GSe; secondary sales above GSe at +HSD% yoy; rent resilient in Tier-1 cities while continuing to trend lower in 50-cities; tracked developers' landbanking intensity mixed with margins remaining solid:

1) May ASP decline pace resembled both Apr and Mar in primary market at an average -0.2% mom while widened sequentially to -0.3% mom in the secondary market; of which, T1 cities continued to record solid performance, with primary/secondary ASP at +0.2%/+0.3% mom (respectively 4th/3rd consecutive month of positive mom), and T2 cities' primary/secondary ASP decline pace was similar to Apr at -0.1%/-0.2% mom in May. 13 Cities out of 70 cities recorded mom positive or flat secondary price change in May (vs. 16/17 in Apr/Mar) and among them, 10 cities had achieved 3 consecutive months of positive/flat mom through Mar to May. We also note that Shenzhen and Shanghai registered broad-based secondary transaction ASP improvements across most product types, and Beijing's high-end projects outperformed in May. 2) May nationwide property sales were above our high-frequency tracking, and was slightly below/largely inline with GSe in volume/value terms at -13%/-9% yoy. 3) Construction activities stayed weak as expected with new starts/completions decline (-25%/-20% yoy) both moderately below GSe, mirroring continued sluggish performance in FAI/land markets. Separately, 4) May secondary sales volume in 15 cities was above GSe at +8% yoy (vs. +4% in Apr), with secondary listing volume in 100 cities declining yoy for a third consecutive month, mom accelerating transaction turnover pace and marginally improving residential rental yields. Besides, 5) while 50-cities' average rent level continued to trend lower in May-26, we note that Tier-1 cities' rent had on average increased mom for three consecutive months, also outperforming May-24/-25 which both recorded negative mom trend. Top-performing cities since

## Yi Wang, CFA

+86(21)2401-8930 |
yi.wang@goldmansachs.cn
GS (China) Securities Company Limited

## Shi Xu

+86(21)2401-8929 |
shi.x.xu@goldmansachs.cn
GS (China) Securities
Company Limited

## Kaiyan Jing

+86(21)2411-8092 |
kaiyan.jing@goldmansachs.cn
GS (China) Securities Company Limited

Mar to May include: Shanghai, Shenzhen, Tianjin and Urumqi. 6) Tracked developers' new land acquisition pace were mixed in May, with their average land investment as share of contract sales decreasing compared to Apr, echoing the broader sluggish land market, and estimated project-level GPM solid at average c.23% in May (similar as 4M26 overall).

Looking into Jun 2026, we expect 1) primary and secondary ASPs to both decline at a slower pace, with T1's recovery momentum extending and key T2 potentially reverting to positive mom; 2) yoy declines likely to carry forward at current pace for new home sales volume and value, reflecting MTD sequential moderation and stronger base effects; 3) yoy declines to persist for completion and new starts, aligning with uninspiring value-chain indicators; 4) MSD % yoy improvements for secondary transaction volume, factoring in stable leading indicators and moderate comparison base.

What we watch out for: Signs of property price stabilization/inflection in core T1 cities (i.e. Shanghai and Shenzhen) and whether other key cities will follow suit; easing of secondary supply pressure and improvement of rental yields in high-tier cities; policy stimulus such as full relaxation of HPR in T1 cities.

Summary of key market indicators in May 2026 and GS forecasts for Jun 2026

<table><tr><td colspan="3">(nationwide, unless stated otherwise)</td><td>May-26</td><td>5M26</td><td>May vs. Apr</td><td>May vs. GSe</td><td>June GSe</td></tr><tr><td rowspan="3">Primary sales</td><td>Volume</td><td>yoy</td><td>-13%</td><td>-11%</td><td></td><td>Below</td><td>Down low-teens % yoy</td></tr><tr><td>Value</td><td>yoy</td><td>-9%</td><td>-14%</td><td></td><td>Inline</td><td>Down c.10% yoy</td></tr><tr><td>Price</td><td>70 cities mom</td><td>-0.2% (May)</td><td>-0.2% (Apr)</td><td></td><td>Inline</td><td>Narrower declining pace; T1 cities recovery to continue</td></tr><tr><td rowspan="2">Secondary sales</td><td>Volume</td><td>15 cities yoy</td><td>8%</td><td>-3%</td><td></td><td>Above</td><td>Up MSD % yoy</td></tr><tr><td>Price</td><td>70 cities mom</td><td>-0.3% (May)</td><td>-0.2% (Apr)</td><td></td><td>Below</td><td>Narrower declining pace; T1 cities recovery to continue</td></tr><tr><td rowspan="2">Construction</td><td>New starts</td><td>yoy</td><td>-25%</td><td>-23%</td><td></td><td>Below</td><td>Down high-twenties % yoy</td></tr><tr><td>Completion</td><td>yoy</td><td>-20%</td><td>-23%</td><td></td><td>Below</td><td>Down c.20% yoy</td></tr><tr><td colspan="3"></td><td>May-26</td><td>5M26</td><td>May vs. Apr</td><td></td><td></td></tr><tr><td rowspan="4">Developers&#x27; Landbanking(6 coverage DPs)</td><td>Intensity</td><td>as % of sales</td><td>20%</td><td>21%</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Strategy*</td><td>% Top-10</td><td>87%</td><td>78%</td><td></td><td></td><td rowspan="3">Remain regionally-focused and profitability-oriented;land replenishment pace to sequentially recover</td></tr><tr><td>% Class I</td><td>95%</td><td>91%</td><td></td><td></td></tr><tr><td>Profitability</td><td>Project GPM</td><td>23%</td><td>24%</td><td></td><td></td></tr></table>

<table><tr><td>What to watch</td><td>Signs of property price stabilization/positive inflection in core T1 cities, and whether rest cities follow suitWhether secondary listing balance in high-tier cities to trend lowerImproving rental yields and signs of rent stabilization in high tier citiesHousing Provident Fund reforms, large-scale mortgage interest subsidies or further commercial mortgage rate cutsWhether core districts of T-1 cities could fully remove housing purchase restrictionsPro-employment/demand stimulus to boost broader income outlookMore funding supports to urban renewal/urban village redevelopmentImpact of commercial property REITs pilot on developers&#x27; liquidityAccelerating government inventory buybacks from non-LGFV developersOther improvement to developers&#x27; financing, e.g. expansion of Whitelist project, etc.</td></tr></table>

\*By attributable land acquisition value.  
Source: NBS, Centraline, CREIS, CRIC, GS Global Investment Research

## Related reports:

China Property: Positioning ahead (No.2): Share rally - what's priced in

China Property: Positioning ahead of Tier-1 cities turnaround

China Property: 2026 Outlook: New uncertainties from continued weak housing market

China Real Estate: Slower margin/growth recovery for SOEs, heightened liquidity pressure for POEs; downgrade Seazen to Sell and Longfor to Neutral

China Property Monthly Tracker: Apr ASP strengthened further yet sales/construction

below GSe; more modest expectations into May

China Property: Expert call series: Ongoing structural divergence along the recovery path

China Property: Expert remains cautious on market outlook, stressing the need to accelerate de-stocking efforts

China Property: Housing trade-in program refined in Shanghai, more effectively supporting upgrade demand

China Property: 3RL removal not new, but raise market expectations on timely policy support to strengthen YTD positive momentum

China Property: Potential housing provident fund (HPF) reform might help to stabilize market

China Property: Potential new round of policy stimulus would be positive on both housing market and consumption

China Property: What would it take to clear China's housing inventory (No. 3): Forming a positive feedback loop is the key

## Summary of key market indicators and GS forecasts

May 70-city primary ASP decline pace was similar to Apr/Mar while secondary ASP decline widened sequentially, of which T1 remained strong; May primary sales (vol/val at -13%/-9% yoy) came slightly below/largely in-line with our expectation, and sluggish construction activities were moderately below GSe; secondary sales above GSe at +HSD% yoy; rent resilient in Tier-1 cities while continuing to trend lower in 50-cities; tracked developers' landbanking intensity mixed with margins remaining solid:

1) May ASP decline pace resembled both Apr and Mar in primary market at an average -0.2% mom while widened sequentially to -0.3% mom in the secondary market; of which, T1 cities continued to record solid performance, with primary/secondary ASP at +0.2%/+0.3% mom (respectively 4th/3rd consecutive month of positive mom), and T2 cities' primary/secondary ASP decline pace was similar to Apr at -0.1%/-0.2% mom in May. 13 Cities out of 70 cities recorded mom positive or flat secondary price change in May (vs. 16/17 in Apr/Mar) and among them, 10 cities had achieved 3 consecutive months of positive/flat mom through Mar to May. We also note that Shenzhen and Shanghai registered broad-based secondary transaction ASP improvements across most product types, and Beijing's high-end projects outperformed in May. 2) May nationwide property sales were above our high-frequency tracking, and was slightly below/largely inline with GSe in volume/value terms at -13%/-9% yoy. 3) Construction activities stayed weak as expected with new starts/completions decline (-25%/-20% yoy) both moderately below GSe, mirroring continued sluggish performance in FAI/land markets. Separately, 4) May secondary sales volume in 15 cities was above GSe at +8% yoy (vs. +4% in Apr), with secondary listing volume in 100 cities declining yoy for a third consecutive month, mom accelerating transaction turnover pace and marginally improving residential rental yields. Besides, 5) while 50-cities' average rent level continued to trend lower in May-26, we note that Tier-1 cities' rent had on average increased mom for three consecutive months, also outperforming May-24/-25 which both recorded negative mom trend. Top-performing cities since Mar to May include: Shanghai, Shenzhen, Tianjin and Urumqi.

Tracked developers' new land acquisition pace was mixed in May, with Poly A and Greentown accelerated landbanking while the rest of the developers slowed down their investment intensities, echoing sluggish broader land market activity. Our covered stronger SOE developers on average spent 20% of their May contract sales in land acquisition, which on average carry c.23% project level GPM, with 95% exposure to Tier-1 & 2 cities and 78% exposure to Top-10 cities; overall their 5M26 land investment on average accounted for 21% of contract sales and carried c.24% GPM.

Looking into Jun 2026, we expect 1) primary and secondary ASPs to both decline at a slower pace, with T1's recovery momentum extending and key T2 potentially reverting to positive mom; 2) yoy declines likely to carry forward at current pace for new home sales volume and value, reflecting MTD sequential moderation and stronger base effects; 3) yoy declines to persist for completion and new starts, aligning with uninspiring value-chain indicators; 4) MSD % yoy improvements for secondary transaction volume, factoring in stable leading indicators and moderate comparison base.

Prices: Primary: We see primary ASPs in T1s and key T2s to be supported by product mix upgrades (e.g. superior quality with higher net-to-gross ratio and better ceiling heights) and limited new home supply competition (esp. in core areas). For example, Hangzhou's 6 high-profile, recently-launched ultra-luxury home projects recorded rather strong prices and sell-through momentum. Secondary: We see 1) easing secondary listing supply pressure, driven by rising rental yields (especially by low-total-price housing units) and property owners' reluctance to sell at deeply discounted prices; and 2) structural performance divergence for different product positionings (catering to high-yield buyers, home upgraders, etc.) in different cities. The latest average transaction price (subject to mix change) in Beike's 15 monitored cities recorded stable trends since May. Looking ahead, we expect primary and secondary ASPs to both decline at a slower pace in Jun, with T1's recovery momentum extending and key T2 potentially reverting to positive mom.

Primary volume: We expect yoy declines to carry forward current pace into upcoming month, factoring in 1) mom moderation in new home sales volume in MTD June in monitored cities; 2) a sequentially stronger base from prior year (June-25 saw 54% mom improvement). As a result, we estimate low-teens % yoy decline for national sales volume and c.10% yoy decline for sales value in June 2026.

Secondary volume: MTD June market activities largely carried forward May pace with transaction volumes -2% mom. Factoring in the stable momentum in leading indicators, coupled with a moderate year-ago base (June-25 was flattish mom), we forecast June 2026 secondary volume in 15 large cities to improve MSD % yoy.

Construction: We anticipate a c.20% yoy decline for completions and a high-twenties % yoy decline for new starts in June 2026, considering 1) seasonal tailwinds, with historical trends showing average mom improvements of +52% for completions and +26% for new starts since 2021; that said, 2) MTD-June value chain indicators momentum remain uninspiring: for completions, expedited sequential decline in glass prices, and inventories continue to edge higher from end-May levels; for new starts, cement shipment ratios plateaued mom at mid-40s% range in MTD June, down from \~50% in the prior year.

Developers' land banking: According to CREIS, the Top-5 cities in MTD Jun by land transaction value were respectively Beijing, Shenzhen, Hangzhou, Jinhua and Yancheng. Some high-profile land sales included a Shenzhen Nanshan district land plot acquired by Poly H (0119.HK, NC) at a land cost of Rmb109k/sqm and a Hangzhou Shangcheng district land plot acquired jointly by Greentown and Hangzhou Metro Group at a land consideration of Rmb2.1bn. Looking ahead, we expect developers to continue to be regionally-focused, profitability-oriented and disciplined, synchronizing their investment pace with contract sales performance.

Exhibit 1: Summary of the latest property development activity in China  
YTD national property market development data comparison

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Latest trend</td><td colspan="2">GSe</td><td colspan="12">Key national property data summary</td></tr><tr><td>May-26</td><td>5M26</td><td>Jun-Dec 26E</td><td>2026E</td><td>2025</td><td>2024</td><td>2023</td><td>2022</td><td>2021</td><td>2020</td><td>2019</td><td>2018</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td></tr><tr><td rowspan="2">GFA sold</td><td>(mn sqm)</td><td>61</td><td>313</td><td>531</td><td>845</td><td>881</td><td>965</td><td>1,108</td><td>1,211</td><td>1,614</td><td>1,588</td><td>1,554</td><td>1,562</td><td>1,554</td><td>1,460</td><td>1,215</td><td>1,153</td></tr><tr><td>YoY</td><td>-13.2%</td><td>-10.8%</td><td>0%</td><td>-4%</td><td>-9%</td><td>-13%</td><td>-9%</td><td>-25%</td><td>2%</td><td>2%</td><td>0%</td><td>1%</td><td>6%</td><td>20%</td><td>5%</td><td>-8%</td></tr><tr><td rowspan="2">Property sales</td><td>(Rmb tn)</td><td>0.6</td><td>2.9</td><td>5.0</td><td>7.9</td><td>8.4</td><td>9.6</td><td>11.6</td><td>12.4</td><td>17.0</td><td>16.3</td><td>15.0</td><td>14.1</td><td>12.7</td><td>11.2</td><td>8.4</td><td>7.4</td></tr><tr><td>YoY</td><td>-9.3%</td><td>-13.5%</td><td>0%</td><td>-6%</td><td>-13%</td><td>-17%</td><td>-6%</td><td>-27%</td><td>5%</td><td>8%</td><td>6%</td><td>11%</td><td>13%</td><td>33%</td><td>14%</td><td>-7%</td></tr><tr><td rowspan="2">ASP</td><td>(Rmb/sqm)</td><td>10,501</td><td>9,376</td><td>9,362</td><td>9,367</td><td>9,527</td><td>9,952</td><td>10,457</td><td>10,233</td><td>10,546</td><td>10,248</td><td>9,673</td><td>9,045</td><td>8,160</td><td>7,699</td><td>6,932</td><td>6,427</td></tr><tr><td>YoY</td><td>4.5%</td><td>-3.0%</td><td>-1%</td><td>-2%</td><td>-4%</td><td>-5%</td><td>2%</td><td>-3%</td><td>3%</td><td>6%</td><td>7%</td><td>11%</td><td>6%</td><td>11%</td><td>8%</td><td>2%</td></tr><tr><td rowspan="2">GFA new starts</td><td>(mn sqm)</td><td>40</td><td>179</td><td>299</td><td>479</td><td>588</td><td>738</td><td>959</td><td>1,199</td><td>1,989</td><td>2,244</td><td>2,272</td><td>2,095</td><td>1,787</td><td>1,669</td><td>1,545</td><td>1,796</td></tr><tr><td>YoY</td><td>-24.6%</td><td>-22.6%</td><td>-16%</td><td>-19%</td><td>-20%</td><td>-23%</td><td>-20%</td><td>-40%</td><td>-11%</td><td>-1%</td><td>8%</td><td>17%</td><td>7%</td><td>8%</td><td>-14%</td><td>-11%</td></tr><tr><td rowspan="2">GFA completions</td><td>(mn sqm)</td><td>22</td><td>141</td><td>454</td><td>595</td><td>603</td><td>737</td><td>1,019</td><td>854</td><td>1,014</td><td>912</td><td>959</td><td>944</td><td>1,015</td><td>1,061</td><td>1,000</td><td>1,075</td></tr><tr><td>YoY</td><td>-20.0%</td><td>-23.4%</td><td>8%</td><td>-1%</td><td>-18%</td><td>-28%</td><td>19%</td><td>-16%</td><td>11%</td><td>-5%</td><td>2%</td><td>-7%</td><td>-4%</td><td>6%</td><td>-7%</td><td>6%</td></tr><tr><td rowspan="2">Property FAI</td><td>(Rmb tn)</td><td>0.6</td><td>3.0</td><td>4.3</td><td>7.3</td><td>8.3</td><td>10.0</td><td>11.2</td><td>12.4</td><td>13.8</td><td>13.2</td><td>12.4</td><td>11.3</td><td>10.3</td><td>9.7</td><td>9.1</td><td>9.0</td></tr><tr><td>YoY</td><td>-24.4%</td><td>-16.2%</td><td>-8%</td><td>-12%</td><td>-17%</td><td>-11%</td><td>-10%</td><td>-10%</td><td>5%</td><td>6%</td><td>10%</td><td>10%</td><td>6%</td><td>7%</td><td>1%</td><td>10%</td></tr></table>

Source: NBS, CREIS, GS Global Investment Research

Exhibit 2: May-26 70-city ASP index was -0.2%/-0.3% mom (vs. -0.2%/-0.2% mom for Apr), with 16/10 cities (vs. 14/12 in Apr) recording sequentially improved ASPs and 2/3 cities (vs. 7/4 in Apr) recording sequentially flattened ASPs in primary/secondary  
![](images/878759c24c217347858a017cac2908afd7f4e788f660eaf1900dbdd10c8b9e80.jpg)

<details>
<summary>line chart</summary>

| Date     | No. of cities where primary ASP increased mom (RHS) | 

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for

equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
