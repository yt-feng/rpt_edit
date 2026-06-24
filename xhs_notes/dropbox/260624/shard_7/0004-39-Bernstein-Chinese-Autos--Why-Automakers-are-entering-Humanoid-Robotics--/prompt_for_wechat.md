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
Asian Autos

# Chinese Autos: Why Automakers are entering Humanoid Robotics – and their competitive edge

![](images/35cbf05e8237d996e2a158865927fb0958353cd7475a5b042d55272cf3ecf0d4.jpg)

Eunice Lee, CFA

+852 2123 2606

eunice.lee@bernsteinsg.com

![](images/252709e4c672f6d03d5d4829017cb81796261cbe9f80aae451467713c7e97558.jpg)

Jay Huang, Ph.D.

+852 2123 2631

jay.huang@bernsteinsg.com

![](images/7f63c09b04fe567d4d780aac324d7a8ad07edd76bc23d641057418b9d730ded3.jpg)

Dien Wang, Ph.D.

+852 2123 2622

dien.wang@bernsteinsg.com

![](images/8171016b92d9240994c83a786da30674ba5cd4c285c1bb849006e5d21878a777.jpg)

Ethan Xu

+852 2123 2634

ethan.xu@bernsteinsg.com

![](images/6d7960ee48137e650c82c2e0bc2494d8929d5d077465695dec786f7405dabac0.jpg)

Weibin Liang, Ph.D.

+852 2123 2666

weibin.liang@bernsteinsg.com

From Tesla and Hyundai, to XPeng and Xiaomi, an increasing number of automotive OEMs are entering the humanoid robotics space. In this report, we explore the strategic rationale, assess their competitive advantages, and highlight key investment implications.

Auto OEMs' push into humanoid robotics is recent but accelerating. Auto OEMs began moving into humanoid robotics from 2020. Hyundai announced its acquisition of $80\%$ stake in Boston Dynamics in Dec 2020. Tesla then unveiled its "Tesla Bot" concept in August 2021. Since then, a growing number of Chinese OEMs have entered the field through: in-house development (e.g. XPeng and Xiaomi), subsidiary stakes (e.g. BYD's investments in PaXini and Zhiyuan), and strategic partnerships (e.g. Geely with UBTech). At the 2026 Beijing Auto Show, multiple OEMs (e.g. XPeng, Chery, BYD, etc.) showcased their humanoids, highlighting growing momentum in their broader tech strategies.

OEMs are entering humanoid robotics to boost productivity and unlock new revenue streams. Humanoids can further increase factory automation and drive structural cost reductions amid rising labor costs and workforce constraints. Applications may expand to consumer and service use cases (e.g., security, retail, home assistance), with some OEMs (e.g., Tesla, XPeng) viewing the TAM as comparable to or larger than autos over time.

Automakers have several advantages across hardware, software, and scale. There is significant overlap between vehicle and humanoid components—motors, reducers, sensors—as well as manufacturing. On the software side, there is partial overlap across robotics and autonomous driving in the development of VLA models and world models. With factory automation likely the first deployment wave, OEMs can pilot humanoids in-house, iterate rapidly, and scale deployments, accelerating learning while driving down unit costs. Strong balance sheets and R&D budgets further support long development cycles and talent attraction, positioning OEMs competitively in humanoid robotics.

Investment implications. Investors can gain exposure to humanoids 1) via OEMs or integrators through dedicated players (e.g. UBTech, Unitree), automakers, or tech firms. Within Chinese autos, XPeng (Market-Perform) and Xiaomi (Outperform) stand out. XPeng's humanoid features a highly human-like design and explicitly targets consumer and household uses, potentially enabling higher margins if the company successfully addresses emotional companionship. XPeng's leadership in autonomous driving and broader physical AI reinforces its credentials in this space. We maintain our Market-Perform rating given the long timeline, but see strong optionality. Xiaomi is another notable player, and we see humanoid as a natural extension of its "Human × Car × Home" ecosystem as AI agents evolve. Another approach is 2) via the supply chain. We prefer upstream components companies with exposure to broad robotics (not limited to the humanoid), broad customer base, proven success in expertise expansion, and high-quality core businesses, e.g. Shuanghuan, Hesai, and Tuopu (here). We view ROI for humanoid robots in auto manufacturing as compelling once payback falls below five years, vs. our current estimate of 7-8 years. Adoption should accelerate over the next 3-5 years, driven by advances in robotic intelligence, declining robot costs, and rising labor expenses.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">22 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>1211.HK (BYD)</td><td>O</td><td>HKD</td><td>78.35</td><td>136.00</td><td>(84.8)%</td><td>CNY</td><td>3.58</td><td>4.90</td><td>6.90</td><td>18.9</td><td>13.8</td><td>9.8</td></tr><tr><td>002594.CH (BYD)</td><td>O</td><td>CNY</td><td>87.59</td><td>124.00</td><td>(69.8)%</td><td>CNY</td><td>3.58</td><td>4.90</td><td>6.90</td><td>24.5</td><td>17.9</td><td>12.7</td></tr><tr><td>175.HK (Geely)</td><td>O</td><td>HKD</td><td>17.45</td><td>25.00</td><td>(39.2)%</td><td>CNY</td><td>1.67</td><td>1.82</td><td>2.26</td><td>9.0</td><td>8.3</td><td>6.7</td></tr><tr><td>2333.HK (Great Wall-H)</td><td>M</td><td>HKD</td><td>9.76</td><td>13.00</td><td>(63.5)%</td><td>CNY</td><td>1.16</td><td>1.21</td><td>1.40</td><td>7.3</td><td>7.0</td><td>6.0</td></tr><tr><td>2238.HK (GAC)</td><td>M</td><td>HKD</td><td>2.24</td><td>3.00</td><td>(66.2)%</td><td>CNY</td><td>(0.85)</td><td>(0.13)</td><td>(0.01)</td><td>(2.3)</td><td>(14.9)</td><td>(304.0)</td></tr><tr><td>LI (Li Auto)</td><td>M</td><td>USD</td><td>13.21</td><td>15.50</td><td>(74.9)%</td><td>CNY</td><td>1.13</td><td>(4.88)</td><td>2.27</td><td>79.1</td><td>(18.3)</td><td>39.4</td></tr><tr><td>2015.HK (Li Auto)</td><td>M</td><td>HKD</td><td>50.50</td><td>61.00</td><td>(97.5)%</td><td>CNY</td><td>0.57</td><td>(2.44)</td><td>1.13</td><td>77.1</td><td>(17.9)</td><td>38.4</td></tr><tr><td>9866.HK (NIO)</td><td>M</td><td>HKD</td><td>39.22</td><td>47.00</td><td>(0.4)%</td><td>CNY</td><td>(6.85)</td><td>(1.62)</td><td>(0.49)</td><td>(4.9)</td><td>(20.9)</td><td>(68.9)</td></tr><tr><td>NIO (NIO)</td><td>M</td><td>USD</td><td>5.02</td><td>6.00</td><td>21.5%</td><td>CNY</td><td>(6.85)</td><td>(1.62)</td><td>(0.49)</td><td>(5.0)</td><td>(21.0)</td><td>(69.1)</td></tr><tr><td>600104.CH (SAIC)</td><td>M</td><td>CNY</td><td>10.50</td><td>15.00</td><td>(79.4)%</td><td>CNY</td><td>0.89</td><td>0.97</td><td>1.05</td><td>11.9</td><td>10.8</td><td>10.0</td></tr><tr><td>1810.HK (Xiaomi)</td><td>O</td><td>HKD</td><td>23.72</td><td>43.00</td><td>(81.8)%</td><td>CNY</td><td>1.62</td><td>1.02</td><td>1.77</td><td>12.6</td><td>20.1</td><td>11.6</td></tr><tr><td>9868.HK (XPeng)</td><td>M</td><td>HKD</td><td>51.55</td><td>78.00</td><td>(75.9)%</td><td>CNY</td><td>(0.60)</td><td>(1.02)</td><td>0.23</td><td>(74.4)</td><td>(43.8)</td><td>197.2</td></tr><tr><td>XPEV (XPeng)</td><td>M</td><td>USD</td><td>13.21</td><td>20.00</td><td>(53.5)%</td><td>CNY</td><td>(1.20)</td><td>(2.03)</td><td>0.45</td><td>(74.7)</td><td>(44.0)</td><td>198.0</td></tr><tr><td>601689.CH (Tuopu)</td><td>O</td><td>CNY</td><td>60.19</td><td>75.00</td><td>(14.3)%</td><td>CNY</td><td>1.61</td><td>1.81</td><td>2.36</td><td>37.4</td><td>33.3</td><td>25.6</td></tr><tr><td>2050.HK (Sanhua)</td><td>M</td><td>HKD</td><td>26.70</td><td>27.00</td><td>(28.5)%</td><td>CNY</td><td>1.03</td><td>0.97</td><td>1.11</td><td>22.4</td><td>23.7</td><td>20.8</td></tr><tr><td>002050.CH (Sanhua)</td><td>M</td><td>CNY</td><td>45.23</td><td>39.00</td><td>34.3%</td><td>CNY</td><td>1.03</td><td>0.97</td><td>1.11</td><td>43.9</td><td>46.5</td><td>40.9</td></tr><tr><td>002472.CH (Shuanghuan)</td><td>O</td><td>CNY</td><td>42.11</td><td>60.00</td><td>(7.9)%</td><td>CNY</td><td>1.50</td><td>1.70</td><td>2.00</td><td>28.1</td><td>24.8</td><td>21.1</td></tr><tr><td>HSAI.US (Hesai)</td><td>O</td><td>USD</td><td>16.89</td><td>30.00</td><td>(53.8)%</td><td>CNY</td><td>2.92</td><td>3.31</td><td>5.27</td><td>39.1</td><td>34.5</td><td>21.7</td></tr><tr><td>2525.HK (Hesai)</td><td>O</td><td>HKD</td><td>129.90</td><td>238.00</td><td>NA</td><td>CNY</td><td>2.92</td><td>3.31</td><td>5.27</td><td>38.4</td><td>33.9</td><td>21.3</td></tr><tr><td>688017.CH (Leader Drive)</td><td>U</td><td>CNY</td><td>393.31</td><td>115.00</td><td>191.1%</td><td>CNY</td><td>0.69</td><td>0.83</td><td>0.96</td><td>568.0</td><td>471.5</td><td>409.0</td></tr><tr><td>300124.CH (Inovance)</td><td>O</td><td>CNY</td><td>68.95</td><td>82.00</td><td>(35.6)%</td><td>CNY</td><td>1.87</td><td>2.19</td><td>2.65</td><td>36.9</td><td>31.4</td><td>26.1</td></tr><tr><td>6324.JP (HDSI)</td><td>O</td><td>JPY</td><td>8,710.00</td><td>7,800.00</td><td>164.3%</td><td>JPY</td><td>16.99</td><td>57.37</td><td>79.51</td><td>512.7</td><td>151.8</td><td>109.5</td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,048.07</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,500.58</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JPL</td><td></td><td></td><td>2,676.74</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

Chinese Autos: For our EV names, we rate BYD and Xiaomi Outperform, and XPeng, Li Auto, and NIO Market-Perform. Within our traditional Chinese OEMs coverage, we rate Geely Outperform and Great Wall, GAC, and SAIC Market-Perform.

Asian Industrial Technology: We rate Inovance and Harmonic Drive Outperform.

Asia Emerging Robotics: We rate Shuanghuan, Hesai and Tuopu Outperform, Sanhua Market-Perform and Leader Drive Underperform

## DETAILS

## RELATED RESEARCH REPORTS

12 Jun 2026 - Humanoid Robotics: A scientist, an inventor, an engineer, and a gardener walk into a room ...

26 May 2026 - Humanoid robots: The road toward attractive ROI in warehouses

27 Apr 2026 - Xiaomi: 2026 Investor Day takeaways — AI, Overseas, Memory, and Humanoid robotics

26 Apr 2026 - Chinese Autos: 2026 Beijing Auto Show takeaways — China as Battlefield or Launchpad?

27 Mar 2026 - Future of Tech: Physical AI -- Bridging industrial and humanoid robotics

26 Feb 2026 - Humanoid Robotics: The path to 1 million annual shipment

14 Jan 2026 - Asia Emerging Robotics: How can we view Tesla Optimus more positively?

12 Jan 2026 - Humanoid Robotics: Who plays where

12 Nov 2025 - Asia Emerging Robotics: Embrace the Humanoid Era - Initiating Coverage of Shuanghuan, Hesai, Tuopu, Sanhua and Leader Drive

6 Nov 2025 - Robotics Chips: Short primer on the 'brains' for industrial and humanoid robots

5 Mar 2025 - Future of Tech: The hierarchy of infinities -- comparing Humanoid/Industrial Robot and Autonomous Driving technologies

3 Mar 2025 - Future of Tech: The Humanoid Robot industry, 2025-2050

## AUTO OEM'S HUMANOID INITIATIVES AND PROGRESS

## AUTO OEMS' PUSH INTO HUMANOID ROBOTICS IS RECENT BUT ACCELERATING

Auto OEMs began moving into humanoid robotics from 2020. Hyundai announced its acquisition of an approximately 80% stake in Boston Dynamics in December 2020, signaling its intent to build a broader robotics platform beyond vehicles. Tesla then unveiled its “Tesla Bot” concept (later named Optimus) at its AI Day in August 2021, putting general-purpose humanoids firmly on the automotive agenda.

Since then, a growing number of Chinese OEMs have entered the field through different routes: 1) in-house development (for example XPeng's IRON robot and Xiaomi's humanoid projects), 2) subsidiary stakes (such as BYD's investments in PaXini and Zhiyuan), and 3) strategic partnerships (for instance Geely–Zeekr's collaboration with UBTech). This momentum has become increasingly visible at major industry events. At the 2026 Beijing Auto Show, multiple OEM-linked humanoids, including XPeng's IRON, Chery's AiMOGA, and BYD-related Zhiyuan AgiBot, were showcased publicly, underscoring how rapidly humanoid robotics is being woven into Chinese automakers' broader technology narratives.

## INDUSTRY FRONTRUNNER WITH PLANS FOR NEARER-TERM COMMERCIALIZATION

\- Tesla is developing its humanoid robot Optimus, progressing from Gen 1 (2022) to Gen 2 and Gen 2.5 prototypes by 2025, reflecting rapid iteration in hardware and software. Its strategy starts with manufacturing applications, with a long-term ambition to expand into consumer and household scenarios. Tesla targets limited commercialization in 2026 and volume shipments in 2027. A key constraint is that dexterous hand capability remains a major bottleneck, limiting real-world deployment readiness despite strong system-level progress.

\- Hyundai, the parent company of Boston Dynamics, is pursuing an aggressive humanoid roadmap, transitioning Atlas from R&D to industrial deployment. Production-ready Atlas robots are being introduced into real factory environments, with initial applications in parts sequencing and heavy-duty manufacturing tasks. The group is targeting annual production capacity of up to 30,000 units by 2028, alongside internal rollout of over 25,000 robots across Hyundai facilities. This combination of fullstack control, large-scale manufacturing plans, and clear volume targets positions Hyundai as the leading OEM in humanoid robot industrialization.

\- XPeng is one of the more ambitious OEMs in humanoid robotics, with its IRON robot evolving through multiple generations during 2024-2025. A key milestone was its 2025 AI Day debut, where IRON's natural, catwalk-like walk went viral—so lifelike that audience questioned whether a human was inside. This showcased a major breakthrough in human-like locomotion and established XPeng as a frontrunner in embodied intelligence. The company targets mass production by end-2026 and global deliveries in 2027, focusing on both industrial and retail/service use cases such as showroom assistants and patrol robots, aiming for near-term commercialization.

\- Chery is currently one of the more advanced OEMs in China on commercialization, with its humanoid robot “Moyin” achieving global delivery of 220 units in 2025 and further deployments across public service scenarios such as policing and medical guidance. Chery’s humanoid robot are available for purchase for RMB 285.8k (US\$41k) through e-commerce channels like JD.com (LINK). Chery stands out for having the first meaningful batch delivery among OEMs, a diversified product ecosystem (including robot dogs and service robots), and a clear three-stage roadmap from companion robots to public service and eventually household applications.

\- GAC has developed the GoMate humanoid series (now at the 4th-generation GoMate Mini), targeting applications in elderly care, security, and industrial environments, with pilot production planned for 2026 and mass production in 2027. Incrementally, GAC differentiates itself through innovations such as a wheel-legged hybrid mobility structure and by spinning off a dedicated robotics subsidiary to accelerate commercialization in a more market-oriented structure.

## EARLY INDUSTRIAL DEPLOYER WITH REAL FACTORY VALIDATION

\- BMW has rapidly progressed humanoid robotics from pilot testing to real production environments, building on early collaborations with Figure's robots in 2025. At its Spartanburg plant, humanoids supported the production of over 30k vehicles through tasks such as sheet-metal handling, demonstrating reliability in high-throughput settings. The company is now expanding pilots to Europe, with deployments in Leipzig targeting battery assembly, intralogistics, and component production from summer 2026. BMW's strategy emphasizes iterative scaling through live manufacturing validation, positioning humanoids as flexible co-workers rather than committing to immediate mass production

\- Toyota is among the first OEMs to convert humanoid pilots into commercial deployment through a Robots-as-a-Service (RaaS) model with Agility Robotics. Following a successful pilot, Toyota signed a 2026 agreement to deploy Digit humanoids in production, focusing on logistics tasks such as parts handling and line feeding. Initial deployments remain small-scale, but Toyota's asset-light RaaS approach enables flexible scaling while reducing upfront costs and technology risk.

## EMERGING PLAYERS WITH STRONG POTENTIAL IN THE LONG TERM

\- Xiaomi has been developing humanoid robots since 2020, launching CyberOne in 2022 and more recently open-sourcing its Xiaomi-Robotics-0 embodied AI model in 2026. Its current focus is on manufacturing scenarios such as inspection and assembly, though no clear mass production timeline has been announced. Xiaomi has demonstrated strong technical progress, including achieving over 90% success rates in real factory tasks and advancing high-precision dexterous hand capabilities, supported by its strength in AI foundation models and embodied intelligence.

\- BYD is advancing an internally developed humanoid robot project (codename “Yao Shun Yu”), initiated in 2022 and supported by partnerships such as its embodied intelligence lab with HKUST. BYD stands out for its deep vertical integration across batteries, motors, semiconductors, and precision manufacturing, as well as its potential to leverage its global dealership network for future commercialization.

\- Li Auto is taking a differentiated approach by framing robotics under a broader “space robot” concept, incorporating wheeled robots for manufacturing and future humanoids potentially for household use. While mass production plans are not disclosed, the company has established dedicated robotics business units. Li Auto is notable for its emphasis on AI, including heavy investment in large models such as Mind GPT, and its vision of integrating robots into a wider in-car, wearable, and intelligent ecosystem.

EXHIBIT 1: Overview of Auto OEMs progresses in humanoid robots

<table><tr><td rowspan="2">OEM</td><td rowspan="2">Platform</td><td rowspan="2">Timeline</td><td colspan="2">Progress &amp; Goals</td></tr><tr><td>Application</td><td>Shipment</td></tr><tr><td>Tesla</td><td>Optimus(In-house)</td><td>Aug 2021: Unveiled conceptual design at AI DaySep 2022: Gen 1 prototype was shownSep 2023: Video showing Optimus sorting coloured blocksDec 2023: Gen 2 was showcasedMay 2024: Footage of Optimus performing tasks in a Tesla factory</td><td>- Deploy Optimus inside Tesla factories for &quot;boring, repetitive and dangerous&quot; tasks- Longer term, commercialize for industrial and domestic use</td><td>- Targetin

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
