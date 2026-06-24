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
# U.S. Semiconductors and Semiconductor Capital Equipment Bernstein Semi Cycle Tearsheet: The only game in town?

![](images/f16d8bd038a3618ecc41a1bc744b5b84ebf34c76a5c9fa73a13d46ef7b419ab4.jpg)

Stacy A. Rasgon, Ph.D.

+1 213 559 5917

stacy.rasgon@bernsteinsg.com

![](images/3d207974b298157df790004035d14b45ac2378da2d3d63043d08c14ba4a2ce22.jpg)

Alrick Shaw

+1 917 344 8454

alrick.shaw@bernsteinsg.com

![](images/95e0494e4c8fa49460295ac62e83d0b5ec5a17fd447b47e92f8bb68ab197bd59.jpg)

Arpad von Nemes

+1 917 344 8461

arpad.vonnemes@bernsteinsg.com

The only game in town? The AI theme has grown so large that it is now dragging everything in the space along with it (except, perversely, the AI compute names themselves). But the appetite to play the constraint/bottlenecks has continued as attention rolls from one to the other (hitting memory, semicap, optical/networking, analog/power, and, most recently, CPUs), and even intensified as investors pursue what, for many of them, remains the only game in town.

Step right up? But if you've been there, you've been rewarded with the SOX now returning $107\%$ YTD, dwarfing the S&P $(+9\%)$ . And while expectations and valuations have spiked over the last three months we continue to gain some solace in the fact that the performance so far this year has largely been driven by earnings growth, with forward EPS for the SOX up $75\%$ since the beginning of the year.

(Almost) everyone's a winner? So far AI demand continues to show no signs of slowing with all signs right now pointing to continued multi-year visibility and tight supply/capacity in virtually all needed components, and even many non-AI names have broadly been able to construct AI narratives. Overall we remain bullish on AI demand, and our AI compute names (perversely the only “losers” so far as “bottlenecks” have attracted more attention) are growing almost absurdly attractive if one believes the current trajectory has legs (which we suspect it does).

Own both NVDA and AVGO. We get the desire to play the bottlenecks instead, but they won't ultimately work if these don't; in the meantime demand shows no signs of slowing, and both stocks screen unreasonably cheap (NVDA and AVGO both rated OP).

Buy AMD on CPU and AI. We recently upgraded the stock (better late than never) on CPU and AI/GPU upside, and believe fundamentals can support a \$20 EPS in 2028, suggesting more to go. And we are feeling better about Intel than we have in a long time as both the market (CPU) and narrative (foundry, Trump etc.) grow more supportive, though fundamentals remain on the challenging side (AMD rated OP, INTC rated MP).

Semicap growing (much) more expensive but stay long as WFE still has upside, in our view. We like all names but lean toward AMAT if we had to pick on DRAM exposure and valuation (AMAT, KLAC, and LRCX all rated OP).

Torn on Qualcomm...We believe their smartphone business is in for some pain but clearly underestimated the appetite of investors to buy into any new halfway-credible datacenter story; we shall see if the upcoming analyst day can act as a further catalyst. (QCOM rated MP).

Analog in recovery, though expensive. In our coverage both TXN and ADI have already been growing double digits for a year or more, suggesting that not only have we hit bottom we might be heading (for some) into mid-cycle, and both stocks remain quite expensive especially as datacenter, while fast growing, remains small. NXPI is cheaper, and has admittedly handled this cycle well, but has a bit too much auto for us to be comfortable (TXN, ADI and NXPI all rated MP).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">22 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>AMD (Advanced Micro)</td><td>O</td><td>USD</td><td>551.63</td><td>600.00</td><td>304.9%</td><td>USD</td><td>4.17</td><td>6.98</td><td>14.61</td><td>132.2</td><td>79.1</td><td>37.7</td></tr><tr><td>ADI (Analog Devices)</td><td>M</td><td>USD</td><td>445.48</td><td>430.00</td><td>69.9%</td><td>USD</td><td>7.79</td><td>12.40</td><td>14.65</td><td>57.2</td><td>35.9</td><td>30.4</td></tr><tr><td>AVGO (Broadcom)</td><td>O</td><td>USD</td><td>392.13</td><td>550.00</td><td>31.6%</td><td>USD</td><td>6.82</td><td>11.60</td><td>18.69</td><td>57.5</td><td>33.8</td><td>21.0</td></tr><tr><td>INTC (Intel)</td><td>M</td><td>USD</td><td>140.94</td><td>100.00</td><td>543.4%</td><td>USD</td><td>0.43</td><td>1.07</td><td>1.50</td><td>330.6</td><td>131.7</td><td>93.7</td></tr><tr><td>NVDA (NVIDIA)</td><td>O</td><td>USD</td><td>208.65</td><td>315.00</td><td>19.8%</td><td>USD</td><td>4.77</td><td>9.19</td><td>12.52</td><td>43.7</td><td>22.7</td><td>16.7</td></tr><tr><td>NXPI (NXP Semiconductors)</td><td>M</td><td>USD</td><td>323.24</td><td>270.00</td><td>29.4%</td><td>USD</td><td>11.81</td><td>14.58</td><td>16.45</td><td>27.4</td><td>22.2</td><td>19.6</td></tr><tr><td>QCOM (Qualcomm )</td><td>M</td><td>USD</td><td>221.90</td><td>140.00</td><td>21.4%</td><td>USD</td><td>12.03</td><td>10.64</td><td>9.77</td><td>18.4</td><td>20.9</td><td>22.7</td></tr><tr><td>TXN (Texas Instruments)</td><td>M</td><td>USD</td><td>332.28</td><td>250.00</td><td>42.4%</td><td>USD</td><td>5.45</td><td>7.62</td><td>8.22</td><td>61.0</td><td>43.6</td><td>40.4</td></tr><tr><td>AMAT (Applied Materials)</td><td>O</td><td>USD</td><td>640.18</td><td>525.00</td><td>252.6%</td><td>USD</td><td>9.42</td><td>12.17</td><td>15.56</td><td>68.0</td><td>52.6</td><td>41.2</td></tr><tr><td>LRCX (Lam Research)</td><td>O</td><td>USD</td><td>409.54</td><td>340.00</td><td>327.4%</td><td>USD</td><td>4.14</td><td>5.68</td><td>7.98</td><td>99.0</td><td>72.1</td><td>51.3</td></tr><tr><td>KLAC</td><td>O</td><td>USD</td><td>269.16</td><td>197.50</td><td>191.4%</td><td>USD</td><td>3.33</td><td>3.69</td><td>5.12</td><td>80.9</td><td>72.9</td><td>52.5</td></tr><tr><td>SPX</td><td></td><td></td><td>7,472.79</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

TXN estimate is Reported EPS; TXN valuation is Reported P/E (x); NVDA base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

AMD (Outperform, \$600.00): Expectations remain high, but exposure to AI demand driving both a CPU and GPU story can provide substantial growth.

ADI (Market-Perform, \$430.00): ADI is executing well with both cyclical and idiosyncratic drivers, though may be closer to peak, and valuations remain elevated.

AVGO (Outperform, \$550.00): A strong 2026 AI trajectory seems set to accelerate into 2027 and beyond, bolstered by software, cash deployment, and superb margins & FCF.

INTC (Market-Perform, \$100.00): Server strength is helping the company get back on their feet, and narrative/headlines may fuel the vibe for now.

NVDA (Outperform, \$315.00): The datacenter opportunity is enormous, and still early, with material upside still possible.

NXPI (Market-Perform, \$270.00): The pace and makeup of recovery remains open for debate.

QCOM (Market-Perform, \$140.00): Memory headwinds appear likely to pressure smartphone builds and numbers appear high; we shall see if datacenter dream is enough to attract buyers.

TXN (Market-Perform, \$250.00): TXN shares feel fully valued in the current environment.

AMAT (Outperform, \$525.00): Exposure to key inflections is strong & valuation vs peers is attractive.

LRCX (Outperform, \$340.00): The company is benefiting from key inflections (GAA, packaging, HBM, NAND upgrades) and CY26/27

commentary seems supportive.

KLAC (Outperform, \$197.50): Amid positive WFE trends KLAC possesses structural growth drivers, a strong and durable competitive position, lower China replacement risk, and disciplined capital allocation, warranting premium valuation.

## DETAILS

The AI theme has grown so large that it is now dragging almost everything in the space along with it (except, perversely, the AI compute names themselves even as their own fundamentals look like they continue to move up and to the right). But the appetite to play the constraint/bottlenecks has continued as attention rolls from one to the other (hitting memory, semicap, optical/networking, analog/power, and, most recently, CPUs), and even intensified as investors pursue what, for many of them, remains the only game in town.

But if you've been there, you've been significantly rewarded with the SOX now returning an astonishing 107% YTD, dwarfing the S&P by over 11x (9%) with many names up even more than that. And while expectations and valuations have spiked over the last three months (and with “bubble” commentary increasing apace) we continue to gain some solace in the fact that the performance so far this year has largely been driven by earnings growth, with forward EPS for the SOX up 75% since the beginning of the year (hence we feel we there could be far more craziness to come before we enter the true realm of the bubble...).

So far AI demand continues to show no signs of slowing; indeed all signs right now point to continued multi-year visibility and tight supply/capacity in virtually all needed components (something we suspect will not be resolving anytime soon); even non-AI names (with areas, especially in consumer electronics that will likely be adversely impacted especially on memory shortages as datacenters hoover up precious bits) have broadly been able to construct AI narratives. Overall we remain bullish on AI demand, and our AI compute names (perversely the only “losers” so far as “bottlenecks” have attracted more attention) are growing almost absurdly attractive if one believes the current trajectory has legs (which we suspect it does).

To that end, we would still own both NVDA and AVGO as key beneficiaries of AI demand and with valuations that scream attractive. We have turned more positive on the CPU trade as well (recently upgrading AMD partially on that call) and actually feel better about Intel than we have in some time (though while narrative and market are going their way fundamentals remain somewhat challenging for now). Semicap is growing more expensive but we would stay long as WFE outlook clearly has further upside; we like all our names but would lean a bit more toward AMAT on valuation. We are torn on QCOM; we believe their smartphone business is likely in for some pain but clearly underestimated the appetite for investors to latch onto any new halfway-credible datacenter story. And while our analog coverage looks to be well into recovery, valuations keep us sidelined.

We would own both NVDA and AVGO. The biggest question we are getting right now is “what will make these go up?” We suppose we get the sustainability worries but the companies actually doing the spending continue to show no signs of slowing, and ultimately the “bottlenecks” don’t work if these two don’t. Both appear unreasonably cheap as well, on numbers that are probably still too low; NVDA’s new “\$1T” number for Blackwell/Rubin through CY27 suggests likely material upside to current estimates, and AVGO’s \$100B AI revenue number (even without a raise) feels conservative to us (NVDA and AVGO rated OP, AMD rated MP).

Buy AMD on CPU and AI. We are growing more positive on the agentic CPU trend and in fact recently upgraded the stock (better late than never) on both CPU and AI/GPU upside, and believe fundamentals can support a \$20 EPS in 2028, suggesting more to go. And we are admittedly feeling better about Intel than we have in a long time as both the market (CPU demand so strong they are able to sell off products that by their own admission remain deficient) and narrative (yield progress, foundry datapoints, and Trump's largesse) grow more supportive, though fundamentals still remain on the challenging side for us (AMD rated OP, INTC rated MP).

Semicap is growing (much) more expensive but we would remain long. We think WFE continues to have an upward bias with particular strength in DRAM, leading edge, and packaging, and everything we are hearing on the AI demand side ultimately translates to more chips, more wafers, and more tools. We like all our names (AMAT, KLAC, and LRCX), and would likely lean a bit toward the first on DRAM exposure and valuation (AMAT, KLAC, LRCX all rated OP, and correcting KLAC model/PT for recent 10:1 split).

Torn on Qualcomm...We admittedly made a bad call on QCOM, downgrading the stock to Market Perform in March after pushing it as a top pick all last year, right in front of a datacenter love-fest that sent the stock up 70%+ in a matter of weeks (oops). Our rationale however was that their smartphone business is likely in for a world of pain on the back of memory-induced demand destruction (which seems to be happening) though we clearly underestimated appetite to buy any new halfway-credible datacenter story. The company has an analyst day this week though that we shall see if it can act as a further catalyst... (QCOM rated MP).

Analog in recovery, though expensive...In our coverage both TXN and ADI appear in solid recovery, though both remain quite expensive (30-40x P/FE) especially as the datacenter portions, while fast-growing, remain relatively small (\~10% of revenues or so). NXPI is cheaper, and has admittedly handled this cycle well, but has a bit too much auto for us to be comfortable (with auto seemingly later cycle than industrial) and is now filling their channel. Of the three TXN's story is now probably resonating the most given the end of their capex cycle and consequent increase in FCF though If we had to own one we'd probably go for ADI (better mix in industrial with solid defense and ATE exposure, and more honesty about possibility of auto pull-forward, and 10 turns cheaper than TXN) (TXN, ADI and NXPI all rated MP).

## TEARSHEET

1. Near-term revenue estimates are above seasonal. Negative impact, and similar vs March.

2. Q2/Q3 estimates are above seasonal. Negative impact, and worse vs March.

3. Negative revisions appear to have troughed. Recall that one typically wants to buy semi stocks after numbers have come down, but before they trough. Neutral impact, and mostly unchanged vs March.

4. Channel inventory days ticked down slightly and now sit above average though a bit below the high end of the historical range; \$ are still growing. Neutral to negative impact, though a bit better vs March.

5. Semiconductor company days of inventory ticked up again and remain very high, and \$ are growing. Negative impact, and mostly unchanged vs March.

6. Relative valuations at a \~60% premium to the S&P, up hugely vs our check 3 months ago (+6%). Negative impact, and worse vs March.

7. Sector crowding is very high relative to the market and above the high end of the historical range vs TMT. Negative impact, and worse vs March.

EXHIBIT 1: Expectations and valuations have risen in Q2

<table><tr><td>Indicator</td><td>Dec-25</td><td>Mar-26</td><td>Jun-26</td><td>Notes</td></tr><tr><td>Current Qtr Revenue Estimates</td><td></td><td></td><td></td><td>2Q26 growth expectations are above seasonal (Exhibits 45-46)</td></tr><tr><td>Forward Revenue Estimates</td><td></td><td></td><td></td><td>Q3/Q4 estimates are above seasonal (Exhibits 45-46)</td></tr><tr><td>Earnings Revisions</td><td></td><td></td><td></td><td>The pace of negative revisions appears to have troughed( Exhibits 47-48)</td></tr><tr><td>Channel Inventories</td><td></td><td></td><td></td><td>Inventory days ticked down bit and remain above average though a bit below the high end of the historical range. $ grew markedly QoQ and YoY (Exhibits 49-50, 53)</td></tr><tr><td>Semi Inventories</td><td></td><td></td><td></td><td>Inventory days went up and remain well above the high end of the historical range. $ grew markedly QoQ and YoY (Exhibits 51-52, 54)</td></tr><tr><td>Valuation relative to S&amp;P 500</td><td></td><td></td><td></td><td>Relative valuation for semis are at a 60% premium to the S&amp;P, up markedly QoQ (Exhibits 55-56)</td></tr><tr><td>Crowding</td><td></td><td></td><td></td><td>Semis crowding vs the market and vs TMT rose markedly QoQ, well above historical average relative to the market and TMT (Exhibits 57-58)</td></tr></table>

Source: Company reports, Bloomberg, Bernstein estimates and analysis

Stacy A. Rasgon, Ph.D. +1 213 559 5917 stacy.rasgon@bernsteinsg.com

## SELECTED KEY RESEARCH FROM THE LAST THREE MONTHS

## Blackbooks:

• 27 Mar 2026 - Artificial Intelligence: The AI Infrastructure Value Chain

• 29 Apr 2026 - The Future of Tech: 2026 Edition

• 21 May 2026 - Artificial Intelligence: Sooner or Later

## Industry updates and research:

• 2 Apr 2026 - U.S. Semiconductors - Datacenters in space - technologically viable or pie in the sky?

• 6 Apr 2026 - Quick Take: ASML/Global Semicap - Can MATCH trap China's semiconductor ambitions once and for all?

• 7 May 2026 - Global Analog Semis: How to explain, and what could potentially close, the valuation gap

• 11 May 2026 - Global Semiconductors and Semiconductor Capital Equipment - What to make of an earnings supercycle?

• 12 May 2026 - U.S. Semiconductors: Deconstructing 2026 (so far...)

• 20 May 2026 - US Industrials & Tech: The Data Center Project Pipeline - Capacity, Construction & Cancellations (April '26)

• 21 May 2026 - Global Semiconductor Equipment: \$200bn WFE in sight

• 21 May 2026 - China Semicap: The surging memory capacity expansion

• 28 May 2026 - China Semicap: 2025 WFE Competitive dynamics in China

\- 2 Jun 2026 - U.S. Semiconductors and Semicap Equipment: Conversations with 5 CEOs at Bernstein's 2026 Strategic Decisions Conference

• 10 Jun 2026 - US Industrials & Tech: The Data Center Project Pipeline - Capacity, Construction & Cancellations (May '26)

• 17 Jun 2026 - Global Semis: The CPU Renaissance? Beneficiaries of a \$223bn TAM...

## All things AI:

\- 17 Apr 2026 - Global Semis & Asia Hardware: Artificial Intelligence... Sooner or Later - Energizing the Future of AI Data Centers

• 22 Apr 2026 - 1Q26 AI Server Pulse: Chasing Scarcity

• 8 May 2026 - IREN: The NVIDIA blessing!

• 9 May 2026 - Artificial Intelligence: Inside the War for AI Data Center Connectivity

• 8 Jun 2026 - AI Value Chain: How much does a GW of Vera Rubin data center capacity actually cost?

## All things Auto:

\- 11 May 2026 - China Smart Driving Chips Tracker (1Q26): NOA penetration temporari

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
