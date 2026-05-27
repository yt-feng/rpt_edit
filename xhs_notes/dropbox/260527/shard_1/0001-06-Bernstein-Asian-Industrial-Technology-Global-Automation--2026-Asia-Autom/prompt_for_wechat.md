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
# Asian Industrial Technology

# Global Automation: 2026 Asia Automation tour takeaways

![](images/f179b8850dbc70180d7443198d406df12edd63de09bc56b2af9633f5f6c4b98c.jpg)

Jay Huang, Ph.D.

+852 2123 2631

jay.huang@bernsteinsg.com

![](images/3c04895723449ce306a18b6c689cc5552c5bc47e9d42fe6cc0453601052512dd.jpg)

Weibin Liang, Ph.D.

+852 2123 2666

weibin.liang@bernsteinsg.com

![](images/2d59ce3da97d0d27211914132225f63b424775d6fbd73ff34b3552effb6508fb.jpg)

Dien Wang, Ph.D.

+852 2123 2622

dien.wang@bernsteinsg.com

We visited 14 automation companies in China and Japan in our annual tour this month, including publicly listed Inovance, Leader Drive, MOONS' Electric (not covered), Keyence, FANUC, SMC, DMG Mori (not covered), Yaskawa (not covered), Omron (not covered), THK (not covered), Nabtesco (not covered), and private companies Mech-Mind, Fourier, and OYMotion. We summarize the key takeaways below and update company models post the tour and recent earnings results.

Confirmation of broad-based global FA upcycle. By region, in China, both Inovance (April orders +40% YoY) and Japan FA companies confirmed continued strength despite weak April FAI data. RoW growth is accelerating (Exhibit 1). By end industry, semiconductors and AI-related investments lead the growth, but they typically only account for 5-25% of automation demand. All other verticals, including automotive, are also recovering at different paces. FA companies in general have not seen abnormal “advance orders” from customers, indicating that current demand is largely not due to customers’ inventory buildup. Our view is that peak growth is 1H26 in China and 1Q27 globally, with the upcycle lasting >1 year after the peak.

Physical AI differentiation. Many companies talk the talk, but FANUC really walks the walk. It received orders of thousands of units a few months after its debut last December, compared to \~200 units by Yaskawa 2.5 years after the initial announcement. We analyzed FANUC's unique strengths in Physical AI previously (here), and another important difference is that all of FANUC's robots, rather than a specific line (e.g. Yaskawa's Motoman Next), can be used in Physical AI platforms such as those from Nvidia and Google (both covered). Like us, FANUC sees Physical AI not as a disruptive technology or near-term growth multiplier, but a complementary technology to continuously expand the scope of robotic applications (see here), and to allow inexperienced customers to adopt existing robotic applications with ease.

Toward the first commercial adoption of humanoid robots. There has been general excitement about humanoid robots becoming useful beyond entertainment and research. First killer applications are emerging in warehouses and factories for various types of material handling (see here and here). Humanoid volume growth is 200%+ YoY based on comments from players in China. In plant visits, we further confirm that humanoid robots are to complement rather than replace industrial robots. Even in the world's most automated factory, where FANUC robots are making their own copies, human workers are still present for packaging, loading/ unloading, inspection and testing, and harness installation. These tasks have proved difficult to automate with existing FA equipment and are suited for humanoid robots in the future. FA components companies are adjusting their approach to be more integrated: from individual components (reducers and motors) to actuator modules (Harmonic Drive, Inovance) and even the entire robots (Inovance), in order to protect margins and accelerate application development.

Continued on the next page (competition in China, pricing power and margins) ...

# DETAILS

# Continued from the front page

Asymmetric impact from competition in China. All Japanese FA companies acknowledge the improvement of Chinese technologies. Keyence (see here) and FANUC were able to maintain stable share through innovation, making themselves moving targets to competition, but one needs to be in the right segments to do this. Yaskawa allows its market share to decline to maintain margins in China. Omron introduces “low-end” China only SKUs, hoping to regain market share. We are doubtful that this approach will be effective.

Pricing power and margins. Facing increasing costs of input, general inflation and U.S. tariffs, FA companies have shown clear differentiation in pricing power. And this is not a function of the level of concentration in the market. The best innovators in fragmented markets, such as Keyence and FANUC, pass through the additional costs entirely. Others, such as SMC and Harmonic Drive, albeit in more concentrated markets, can only partially pass through the costs. Companies have also shown different willingness and ability to maintain margins through the recent cycle (Exhibit 2). We view stable margin, or meaningful recovery of margin in upcycles, as testimony to the quality of operation and management. On this metric, Keyence and AirTAC clearly outperformed the rest. FANUC and Harmonic Drive are making genuine efforts to drive margin recovery, although previous high levels are difficult to achieve. SMC seems to allow margin erosion without clear plan or intention to improve.

In light of the latest earning results, we have updated our forecasts for SMC (model), Harmonic Drive (model), IPG Photonics (model), Han's Laser (model), Estun (model), and Hikvision (model). Please see discussion in investment implications and updated financial summary (Exhibit 7 to Exhibit 12) for more details.

EXHIBIT 1: The global factory automation upcycle is accelerating.   
![](images/12007dc4eb83c3a37331ecd6616bb71e1910d72e94871d36c3d26789cc675c1e.jpg)  
Note: Yaskawa, Mitsubishi, Nabtesco, and Omron are not covered by Bernstein.   
Source: Company results, Bernstein analysis

EXHIBIT 2: FA companies have also shown different willingness and ability to maintain margins through the recent cycle   
FA companies' operating profit margin trends   
![](images/ae6e059478ef2e815f4b2352d3fafd933402cd3bc0d3631c94807a256e8a4e94.jpg)

<details>
<summary>line</summary>

| Quarter | Keyence (LHS) | FANUC | SMC | Yaskawa | Harmonic Drive | AirTAC |
|---------|---------------|-------|-----|---------|----------------|--------|
| 2Q21    | 55%           | 45%   | 48% | 22%     | 27%            | 35%    |
| 3Q21    | 56%           | 42%   | 53% | 23%     | 22%            | 33%    |
| 4Q21    | 55%           | 40%   | 49% | 22%     | 33%            | 30%    |
| 1Q22    | 54%           | 38%   | 47% | 21%     | 26%            | 28%    |
| 2Q22    | 53%           | 37%   | 49% | 22%     | 25%            | 30%    |
| 3Q22    | 54%           | 36%   | 48% | 23%     | 26%            | 31%    |
| 4Q22    | 53%           | 38%   | 48% | 23%     | 30%            | 30%    |
| 1Q23    | 54%           | 35%   | 47% | 24%     | 23%            | 31%    |
| 2Q23    | 51%           | 28%   | 45% | 22%     | 15%            | 30%    |
| 3Q23    | 50%           | 30%   | 41% | 21%     | 6%             | 31%    |
| 4Q23    | 50%           | 34%   | 43% | 20%     | 4%             | 31%    |
| 1Q24    | 51%           | 30%   | 35% | 24%     | -1%            | 31%    |
| 2Q24    | 50%           | 29%   | 41% | 18%     | -1%            | 30%    |
| 3Q24    | 51%           | 36%   | 39% | 19%     | -1%            | 31%    |
| 4Q24    | 50%           | 30%   | 36% | 18%     | -1%            | 30%    |
| 1Q25    | 54%           | 37%   | 38% | 21%     | -1%            | 31%    |
| 2Q25    | 50%           | 35%   | 36% | 18%     | -1%            | 30%    |
| 3Q25    | 50%           | 34%   | 37% | 19%     | -1%            | 31%    |
| 4Q25    | 50%           | 33%   | 36% | 17%     | -1%            | 30%    |
| 1Q26    | 54%           | 38%   | 37% | 19%     | -1%            | 31%    |
| 26Y Guidance | -             | -     | -   | -       | -              | -      |
| AirTAC (dotted line) - AirTAC (dashed line) - AirTAC (solid line) - SMC (dashed line) - Yaskawa (solid line) - Harmonic Drive (dashed line) - Harmonic Drive (dashed line) - AirTAC (dashed line) - SMC (dashed line) - Yaskawa (dashed line) - AirTAC (dashed line) - SMC (dashed line) - AirTAC (dashed line) - SMC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC (dashed line) - AirTAC.<lcel><lcel><lcel><lcel><lcel><lcel><lcel><nl>
</details>

Note: Fiscal year 2026 of Keyence, FANUC, SMC and Harmonic Drive ends in March 2027; Fiscal year 2026 of Yaskawa (not covered) ends in February 2027. Source: Bloomberg, companies' results and comments, Bernstein analysis.

EXHIBIT 3: Keyence's microscope with laser-based element analysis remained unique in the market for two years after its launch.   
![](images/545412ca1368cbd64b46db8c9f0ed5bee629afdfc93db29b84fcb194c4764ebf.jpg)

<details>
<summary>text_image</summary>

CMOS
Laser
source
Spectrometer
REYENCE
EVA
XHA
</details>

Hardware design for Laser-based element analysis

![](images/561531fc9ae38ce3fa38cfb997a23bd8a9cfb5a1857864578fa201038c826325.jpg)

<details>
<summary>text_image</summary>

有機物
C: 59.5%
O: 25.1%
H: 8.7%
K: 6.7%
二ッケル
Ni: 90.9%
K: 8.7%
Na: 0.4%
カリウム化合物
O: 53.3%
K: 35.0%
Cu: 10.1%
Na: 1.6%
</details>

Analysis results   
![](images/1554f2cf769073c25f7edd4b9a91fbe0ff455f01a8f0ccc27683f5d075552795.jpg)

<details>
<summary>text_image</summary>

Nanosecond
laser pulse
Plasma emission
</details>

Principle of Laser-based element analysis   
Source: Keyence, Bernstein analysis

EXHIBIT 4: Mech-Mind demonstrates highly flexible autonomous path and posture planning for robotics applications, including bin picking and dimension checking.   
![](images/cdc76be62ee7e5c954ec7bd77414fc0993aff5c442b4d27ca0bb43363fe96606.jpg)

<details>
<summary>text_image</summary>

MECH NIND
(基于自研3D深度学习)
Bio-Riding of Draft® triple bolt
used by Advanced 30°ptersum
MECH NIND
</details>

![](images/0c7cf135b1433d83c501e63a9ff0967e78a22d21a3eacd1f4476632dfdc06376.jpg)

<details>
<summary>text_image</summary>

黑色异形体波栅无序器
基于自研3D波栅学习器
Step Closing of Duct-Engel Note
and by Advanced 3D Optimal
MECHEN
PUMA 20016
MA No. 20016
</details>

Highly flexible autonomous path and posture planning

Source: Bernstein photo and analysis

EXHIBIT 5: Demonstration of path planning for bin picking application   
![](images/60339e6c7a7aa51c42d8620f358c1e45a680eb1090ff33972a5317c6c2a8a152.jpg)

<details>
<summary>text_image</summary>

智能优化
尝试次数统计
模型编辑器
速度 100% 加速度 100%
机器人
真实机器人的移动
关节角 工具位置
关节位置
J1
J2
J3
J4
J5 8
J6
沿连线移动_1
沿连线移动_2
沿连线移动_3
沿连线移动_4
沿连线移动_5
沿连线移动_6
沿连线移动_7
沿连线移动_8
沿连线移动_9
沿连线移动_10
</details>

Source: Bernstein photo

EXHIBIT 6: Mech-Mind demonstrates multiple applications using 3D vision for robot guiding.   
![](images/e15830f1e5b36b9aa282f306edbd8c57f8e7e117b0536536d1d2b36edd6c2fa8.jpg)

<details>
<summary>text_image</summary>

超高精度，实现焊缝精准定位
</details>

Arc welding

![](images/018c2be268fe49c100aa5f39fbf2a86ed8a45844e04b7b7e948c8923087bdb34.jpg)

<details>
<summary>natural_image</summary>

Industrial robotic arm in a factory setting, handling machinery with no visible text or symbols
</details>

Bin-picking from a deep box

![](images/3f16c644178550a0cdde34d7cb41d67d804f36fc3d0476ff14ce43c326175063.jpg)

<details>
<summary>text_image</summary>

自研温度补偿技术
薄壁精度20mm
表面压力20厚重点
</details>

Large part measurement   
Source: Bernstein photo and analysis

EXHIBIT 7: Hikvision financial summary 

<table><tr><td>RMB Million</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue</td><td>63,503</td><td>81,420</td><td>83,166</td><td>89,340</td><td>92,496</td><td>92,508</td><td>97,129</td><td>103,469</td><td>111,353</td><td>120,278</td><td>130,031</td></tr><tr><td>Gross Profit</td><td>29,546</td><td>36,091</td><td>35,170</td><td>39,703</td><td>40,542</td><td>42,440</td><td>44,511</td><td>47,273</td><td>50,778</td><td>54,542</td><td>58,846</td></tr><tr><td>Operating Profit</td><td>15,197</td><td>18,474</td><td>14,783</td><td>16,039</td><td>14,312</td><td>16,963</td><td>19,439</td><td>21,486</td><td>23,031</td><td>24,189</td><td>26,019</td></tr><tr><td>Profit before Tax</td><td>15,273</td><td>18,468</td><td>14,855</td><td>16,099</td><td>14,343</td><td>17,013</td><td>19,633</td><td>21,693</td><td>23,254</td><td>24,430</td><td>26,279</td></tr><tr><td>Attributable Net Profit</td><td>13,386</td><td>16,800</td><td>12,837</td><td>14,108</td><td>11,977</td><td>14,195</td><td>16,435</td><td>18,181</td><td>19,494</td><td>20,482</td><td>22,033</td></tr><tr><td>EBITDA</td><td>16,515</td><td>19,227</td><td>14,954</td><td>16,835</td><td>16,213</td><td>18,542</td><td>21,497</td><td>23,400</td><td>25,059</td><td>26,355</td><td>28,337</td></tr><tr><td>EPS (Basic) (RMB)</td><td>1.45</td><td>1.81</td><td>1.37</td><td>1.52</td><td>1.30</td><td>1.55</td><td>1.79</td><td>1.98</td><td>2.13</td><td>2.23</td><td>2.40</td></tr><tr><td>EPS (Diluted) (RMB)</td><td>1.45</td><td>1.81</td><td>1.37</td><td>1.52</td><td>1.30</td><td>1.55</td><td>1.79</td><td>1.98</td><td>2.13</td><td>2.23</td><td>2.40</td></tr><tr><td>P/B (x)</td><td>5.6</td><td>4.7</td><td>4.4</td><td>3.9</td><td>3.7</td><td>3.5</td><td>3.3</td><td>3.0</td><td>2.7</td><td>2.5</td><td>2.3</td></tr><tr><td>P/E (x)</td><td>22.1</td><td>17.7</td><td>23.4</td><td>21.1</td><td>24.7</td><td>20.7</td><td>17.9</td><td>16.1</td><td>15.0</td><td>14.3</td><td>13.3</td></tr><tr><td>EV/IC (x)</td><td>7.5</td><td>5.9</td><td>4.9</td><td>4.5</td><td>4.0</td><td>4.3</td><td>4.1</td><td>3.7</td><td>3.4</td><td>3.1</td><td>2.9</td></tr><tr><td>EV/EBITDA (x)</td><td>16.0</td><td>13.7</td><td>17.6</td><td>15.7</td><td>16.3</td><td>14.2</td><td>12.3</td><td>11.3</td><td>10.5</td><td>10.0</td><td>9.3</td></tr><tr><td>ROIC (excl. Goodwill)</td><td>42%</td><td>43%</td><td>26%</td><td>26%</td><td>21%</td><td>23%</td><td>27.6%</td><td>28.3%</td><td>27.8%</td><td>26.7%</td><td>26.4%</td></tr><tr><td>ROE</td><td>27%</td><td>29%</td><td>20%</td><td>20%</td><td>15%</td><td>17%</td><td>18.8%</td><td>18.9%</td><td>18.3%</td><td>17.5%</td><td>17.2%</td></tr><tr><td>Gross Margin</td><td>46.5%</td><td>44.3%</td><td>42.3%</td><td>44.4%</td><td>43.8%</td><td>45.9%</td><td>45.8%</td><td>45.7%</td><td>45.6%</td><td>45.3%</td><td>45.3%</td></tr><tr><td>Operating Profit Margin</td><td>23.9%</td><td>22.7%</td><td>17.8%</td><td>18.0%</td><td>15.5%</td><td>18.3%</td><td>20.0%</td><td>20.8%</td><td>20.7%</td><td>20.1%</td><td>20.0%</td></tr><tr><td>Net Margin</td><td>21.5%</td><td>21.5%</td><td>16.3%</td><td>17.0%</td><td>14.2%</td><td>16.7%</td><td>18.4%</td><td>19.1%</td><td>19.0%</td><td>18.5%</td><td>18.4%</td></tr><tr><td>EBITDA Margin</td><td>26.0%</td><td>23.6%</td><td>18.0%</td><td>18.8%</td><td>17.5%</td><td>20.0%</td><td>22.1%</td><td>22.6%</td><td>22.5%</td><td>21.9%</td><td>21.8%</td></tr><tr><td>Revenue Growth</td><td>10.1%</td><td>28.2%</td><td>2.1%</td><td>7.4%</td><td>3.5%</td><td>0.0%</td><td>5.0%</td><td>6.5%</td><td>7.6%</td><td>8.0%</td><td>8.1%</td></tr><tr><td>Operating Profit Growth</td><td>10.9%</td><td>21.6%</td><td>(20.0%)</td><td>8.5%</td><td>(10.8%)</td><td>18.5%</td><td>14.6%</td><td>10.5%</td><td>7.2%</td><td>5.0%</td><td>7.6%</td></tr><tr><td>Attributable Net Profit Growth</td><td>7.8%</td><td>25.5%</td><td>(23.6%)</td><td>9.9%</td><td>(15.1%)</td><td>18.5%</td><td>15.8%</td><td>10.6%</td><td>7.2%</td><td>5.1%</td><td>7.6%</td></tr><tr><td>EBITDA Growth</td><td>19.5%</td><td>16.4%</td><td>(22.2%)</td><td>12.6%</td><td>(3.7%)</td><td>14.4%</td><td>15.9%</td><td>8.9%</td><td>7.1%</td><td>5.2%</td><td>7.5%</td></tr></table>

Source: Hikvision, Bernstein analysis and estimates

EXHIBIT 8: Harmonic Drive financial summary 

<table><tr><td>(in Mn YEN)</td><td>FY2021</td><td>FY2022</td><td>FY2023</td><td>FY2024</td><td>FY2025</td><td>FY2026E</td><td>FY2027E</td><td>FY2028E</td><td>FY2029E</td></tr><tr><td>Revenue</td><td>57,088</td><td>71,527</td><td>55,796</td><td>55,646</td><td>59,558</td><td>68,732</td><td>77,481</td><td>86,915</td><td>97,433</td></tr><tr><td>Gross profit</td><td>22,426</td><td>25,786</td><td>15,606</td><td>14,854</td><td>18,133</td><td>21,766</td><td>25,581</td><td>28,772</td><td>32,897</td></tr><tr><td>Operating profit</td><td>8,740</td><td>10,225</td><td>125</td><td>7</td><td>2,568</td><td>6,810</td><td>9,417</td><td>10,955</td><td>13,411</td></tr><tr><td>Pre-tax Profit</td><td>9,012</td><td>10,195</td><td>(27,606)</td><td>4,780</td><td>2,294</td><td>6,790</td><td>9,410</td><td>10,958</td><td>13,423</td></tr><tr><td>Attributable Net Income</td><td>6,644</td><td>7,596</td><td>(24,807)</td><td>3,474</td><td>1,609</td><td>5,432</td><td>7,528</td><td>8,766</td><td>10,738</td></tr><tr><td>EBITDA</td><td>16,994</td><td>19,800</td><td>10,487</td><td>8,030</td><td>9,929</td><td>15,733</td><td>16,345</td><td>17,997</td><td>20,607</td></tr><tr><td>EPS (Basic, attributable) (YEN)</td><td>69</td><td>80</td><td>(261)</td><td>37</td><td>17</td><td>57</td><td>80</td><td>93</td><td>113</td></tr><tr><td>P/B (x)</td><td>7.8</td><td>7.3</td><td>9.6</td><td>9.6</td><td>9.4</td><td>9.0</td><td>8.5</td><td>7.9</td><td>7.4</td></tr><tr><td>P/E (x)</td><td>115.9</td><td>100.4</td><td>n.a.</td><td>218.8</td><td>470.9</td><td>139.4</td><td>100.6</td><td>86.4</td><td>70.5</td></tr><tr><td>EV/IC (x)</td><td>6.7</td><td>6.1</td><td>8.3</td><td>9.4</td><td>9.1</td><td>9.5</td><td>9.1</td><td>8.8</td><td>8.4</td></tr><tr><td>EV/EBITDA (x)</td><td>44.4</td><td>38.1</td><td>71.9</td><td>93.9</td><td>75.9</td><td>47.9</td><td>46.1</td><td>41.9</td><td>36.6</td></tr><tr><td>ROIC (excl. investment)</td><td>5.8%</td><td>6.5%</td><td>0.1%</td><td>0.0%</td><td>2.2%</td><td>6.7%</td><td>9.3%</td><td>10.4%</td><td>12.2%</td></tr><tr><td>ROE (excl. comprehensive income)</td><td>7.1%</td><td>8.5%</td><td>(32.7%)</td><td>5.5%</td><td>2.6%</td><td>8.5%</td><td>11.0%</td><td>11.8%</td><td>13.2%</td></tr><tr><td>Gross Margin</td><td>39.3%</td><td>36.1%</td><td>28.0%</td><td>26.7%</td><td>30.4%</td><td>31.7%</td><td>33.0%</td><td>33.1%</td><td>33.8%</td></tr><tr><td>Operating profit Margin</td><td>15.3%</td><td>14.3%</td><td>0.2%</td><td>0.0%</td><td>4.3%</td><td>9.9%</td><td>12.2%</td><td>12.6%</td><td>13.8%</td></tr><tr><td>Net Margin (attributable)</td><td>11.6%</td><td>10.6%</td><td>(44.5%)</td><td>6.2%</td><td>2.7%</td><td>7.9%</td><td>9.7%</td><td>10.1%</td><td>11.0%</td></tr><tr><td>EBITDA Margin</td><td>29.8%</td><td>27.7%</td><td>18.8%</td><td>14.4%</td><td>

[中间内容因长度限制已省略]

 learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
