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
# Global Semiconductor Capital Equipment

# Global Semicap Tracker (Apr 26): Japan SPE +25% YoY

![](images/d067f5104f26a32dc7eadad5503fa603f27294b37c5dfd3696f4c06e9810fc5b.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/7d08b0c8fe1947a46cafe061c80b339cd20cb13aae55559f1f7b17c668013d5d.jpg)

Stacy A. Rasgon, Ph.D.

+1 213 559 5917

stacy.rasgon@bernsteinsg.com

![](images/240c1278538cee74ecc1dab16f13ea30f0c1688060a06ddece185a5fa85c10be.jpg)

Qingyuan Lin, Ph.D.

+852 2123 2654

qingyuan.lin@bernsteinsg.com

![](images/a33504427995ba78c80842aec6cd80180b4daf1d8deeaa1b2b74bd932f338528.jpg)

Juho Hwang

+852 2123 2632

juho.hwang@bernsteinsg.com

![](images/9951a0ef6204692975afc7ba9a7870420c51c229957382d5afff88cc6c0f0afc.jpg)

Alrick Shaw

+1 917 344 8454

alrick.shaw@bernsteinsg.com

![](images/1bd629b06c9fff725e819915f29d04bdc09f1349855f87a594b4213f783489cc.jpg)

Arpad von Nemes

+1 917 344 8461

arpad.vonnemes@bernsteinsg.com

![](images/ffbb132ffc036c321f661c99f7604f64e52cf4c387ad235f563164969ccf1376.jpg)

Zheng Cui

+852 2123 2694

zheng.cui@bernsteinsg.com

This tracker analyzes the billings data released by SEAJ whose members are Japanese suppliers & represent \~25% of the global wafer fab equipment (WFE) market. SEAJ released April data on 2nd June (dataset can be downloaded at SEAJ+SEMI Model).

Japan SPE saw YoY growth in April with Japan SPE billing of +13% in USD (+25% in JPY). 3M average billing was relatively stable at +6% MoM / +11% YoY in USD (+6% MoM / +14% YoY in JPY). Sequentially, April single month data was -38% MoM in JPY due to high base.

By equipment type, Japan front end equipment revenue (relevant to TEL) was +12% YoY in April. Assembly equipment revenue (relevant to DISCO) was +73% YoY due to easy comp. Testing equipment (relevant to Advantest) showed growth of +26% YoY. On a sequential basis, testing equipment is -14% MoM and 3M average was -7%.

For TEL, SEAJ data suggests downside to FQ1. Our regression suggests TEL's FQ1 revenue could be -18% QoQ, below the consensus of +6% QoQ. Note that SEAJ data has good $R^{2}$ (0.83) even with 1 month of data. We expect TEL revenue to grow strongly in this year driven by strong DRAM and advanced logic capex. Also for this quarter, we expect the next two months to improve and see strong growth as the first month of each quarter is usually slower.

For Advantest, SEAJ data suggests upside to FQ1. Regression suggests Advantest's revenue could be +13% QoQ, above the consensus of +3% QoQ. Note that SEAJ data has very high $R^{2}$ (0.95) even with 1 month of data. Although April single-month was negative MoM, this was from a very strong March and still was the 2nd highest single-month billings.

We forecast global WFE to be +21.4% YoY in CY2026, and +18.2% in CY2027 (WFE Model, Report Link). We expect CY2026 will see strong growth from DRAM and NAND spending. We believe the Japanese equipment companies will benefit from the rise of memory capex, and there should be more upside.

We maintain our Outperform on Disco, Advantest, Tokyo Electron, Kokusai and Lasertec within Japan semi. Within our US coverage we maintain our Outperform on LRCX, AMAT and KLAC. For Chinese semicap, we maintain our Outperform on NAURA, AMEC, and Piotech.

BERNSTEIN TICKER TABLE 

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">2 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>ClosingPrice</td><td>PriceTarget</td><td>Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>8035.JP (Tokyo Electron)</td><td>O</td><td>JPY</td><td>53,710</td><td>59,200</td><td>93.5%</td><td>JPY</td><td>1,250.88</td><td>1,504.14</td><td>1,848.77</td><td>42.9</td><td>35.7</td><td>29.1</td></tr><tr><td>6146.JP (DISCO)</td><td>O</td><td>JPY</td><td>64,200</td><td>85,000</td><td>57.0%</td><td>JPY</td><td>1,246.28</td><td>1,733.62</td><td>2,127.33</td><td>51.5</td><td>37.0</td><td>30.2</td></tr><tr><td>6525.JP (Kokusai)</td><td>O</td><td>JPY</td><td>7,449.00</td><td>8,240.00</td><td>112.1%</td><td>JPY</td><td>128.63</td><td>200.23</td><td>274.61</td><td>57.9</td><td>37.2</td><td>27.1</td></tr><tr><td>6857.JP (Advantest)</td><td>O</td><td>JPY</td><td>26,320</td><td>39,200</td><td>227.1%</td><td>JPY</td><td>534.21</td><td>735.65</td><td>870.09</td><td>49.3</td><td>35.8</td><td>30.2</td></tr><tr><td>7735.JP (Screen)</td><td>M</td><td>JPY</td><td>11,315</td><td>12,600</td><td>83.9%</td><td>JPY</td><td>486.61</td><td>572.60</td><td>662.24</td><td>23.3</td><td>19.8</td><td>17.1</td></tr><tr><td>6920.JP (Lasertec)</td><td>O</td><td>JPY</td><td>39,250</td><td>50,000</td><td>133.7%</td><td>JPY</td><td>937.82</td><td>893.18</td><td>976.61</td><td>41.9</td><td>43.9</td><td>40.2</td></tr><tr><td>AMAT (Applied Materials)</td><td>O</td><td>USD</td><td>458.17</td><td>525.00</td><td>162.8%</td><td>USD</td><td>9.42</td><td>12.17</td><td>15.56</td><td>48.7</td><td>37.7</td><td>29.5</td></tr><tr><td>LRCX (Lam Research)</td><td>O</td><td>USD</td><td>317.12</td><td>340.00</td><td>255.9%</td><td>USD</td><td>4.14</td><td>5.68</td><td>7.98</td><td>76.7</td><td>55.9</td><td>39.8</td></tr><tr><td>KLAC</td><td>O</td><td>USD</td><td>1,940.04</td><td>1,975.00</td><td>125.9%</td><td>USD</td><td>33.28</td><td>36.93</td><td>51.22</td><td>58.3</td><td>52.5</td><td>37.9</td></tr><tr><td>688012.CH (AMEC)</td><td>O</td><td>CNY</td><td>282.80</td><td>500.00</td><td>91.1%</td><td>CNY</td><td>3.40</td><td>4.95</td><td>7.18</td><td>83.2</td><td>57.2</td><td>39.4</td></tr><tr><td>002371.CH (NAURA)</td><td>O</td><td>CNY</td><td>602.80</td><td>680.00</td><td>44.8%</td><td>CNY</td><td>5.66</td><td>10.22</td><td>16.41</td><td>106.5</td><td>59.0</td><td>36.7</td></tr><tr><td>688072.CH (Piotech)</td><td>O</td><td>CNY</td><td>596.00</td><td>580.00</td><td>254.6%</td><td>CNY</td><td>3.32</td><td>8.12</td><td>12.40</td><td>179.5</td><td>73.4</td><td>48.1</td></tr><tr><td>JPL</td><td></td><td></td><td>2,578.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,599.96</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>2,032.77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended   
AMAT, LRCX, KLAC estimate is Adjusted EPS; AMAT, LRCX, KLAC valuation is Adjusted P/E (x);   
Source: Bloomberg, Bernstein estimates and analysis.

# INVESTMENT IMPLICATIONS

Tokyo Electron: Outperform, PT=¥59,200. TEL is the #4 SPE supplier globally and the biggest Japanese SPE supplier with major presence in 6 product segments. It is expected to gain share and expand margins with competitive pricing after yen depreciation.

DISCO: Outperform, PT=¥85,000. DISCO is the dominant supplier of grinders and dicers with \~85% market share. The growing usage of dicers/grinders driven by advanced packaging is sustainable, especially for HBM and CoWoS in the near term, and hybrid bonding for HBM/3D stacking NAND/backside power delivery network in the midterm.

Kokusai: Outperform, PT=¥8,240.00. Batch ALD should see more adoption in advanced nodes especially GAA (gate-all-around). The biggest use of batch ALD is in NAND, and NAND capex recovery is accelerating.

Lasertec: Outperform, PT=¥50,000. As major supplier for mask inspection (\~50% share) and sole supplier for actinic inspection, Lasertec delivered phenomenal growth in the past, but saw deceleration in recent years. We expect reacceleration from TAM expansion driven by the new A200HiT tool penetrating more actinic inspection at wafer fabs.

Advantest: Outperform, PT=¥39,200. Benefits from rising testing intensity for HBM and Blackwell. As the dominant supplier for HBM tester (\~65%) and Nvidia AI GPU (100% share), Advantest is able to lift the ASP and margin with product migration, especially with HBM4 in 2025.

Screen: Market-Perform, PT=¥12,600. Leading supplier in cleaning equipment with the lowest valuation in our coverage, but also the one with the least specific growth drivers. Cleaning intensity is not increasing, and the market is competitive with both global rivals (TEL, Lam) and Chinese (ACMR, Naura). Declining China revenue contribution presents margin downside risk.

AMAT (Outperform, \$525.00): We maintain a positive view on secular WFE growth and see a number of drivers for AMAT including SAM growth, an increasing services narrative, and capital return.

LRCX (Outperform, \$340.00): The company is benefiting from key inflections (GAA, packaging, HBM, NAND upgrades) and CY26 commentary seems supportive.

KLAC (Outperform, \$1,975.00): Amid positive WFE trends KLAC possesses structural growth drivers, a strong and durable competitive position, lower China replacement risk, and disciplined capital allocation, warranting premium valuation.

NAURA (Outperform, CNY 680.00): As the domestic WFE leader, NAURA has the broadest product portfolio covering Deposition (PVD, CVD), Dry Etch (ICP), Thermo Processes, and Cleaning, as well as a more diverse client base covering leading logic, DRAM, NAND players, benefiting from the WFE domestic substitution in China with acceleration share gain.

AMEC (Outperform, CNY 500.00): Primarily focus on Dry Etch (CCP, ICP) with rapid expansion in Deposition (ALD, LPCVD, EPI), commonly perceived as the domestic WFE company with the best technology and widest global recognition, continue to benefit from the WFE domestic substitution in China with acceleration share gain.

Piotech (Outperform, CNY 580.00): Rising domestic WFE vendor primarily focus on Deposition (PECVD, HDPCVD, SACVD, ALD) with expansion in W2W and C2W hybrid bonding equipment for advanced packaging. Piotech has a strong track record of product innovation, which will allow it to benefit from the WFE domestic substitution in China with acceleration share gain.

# DETAILS

This tracker analyzes the billings data released by SEAJ whose members are Japanese suppliers & represent \~25% of the global wafer fab equipment (WFE) market. SEAJ released April data on 2nd June (dataset can be downloaded at SEAJ+SEMI Model). As usual, we examine the data on both a single-month and 3-month-average basis as the single-month data reflects near-term inflection on a more timely basis and the 3-month moving average reduces the influence of seasonality and reveals the underlying trend better. We also provide the read-across for Tokyo Electron (TEL) and Advantest based on a regression analysis.

April SPE billings were +13% YoY in USD (+25% in JPY). 3M average SPE billings were +11% in USD (+14% YoY in JPY). We forecast the WFE market to be up +21.4% YoY in CY2026 & +18.2% in CY2027.

- On 3-month basis, April billings of Japanese equipment suppliers continued the cyclical upward swing that began in mid-CY2023 (Exhibit 1). Sequentially 3M average was +6%.   
- On single month basis, April billings of Japanese suppliers was at ¥442 bn (-38% MoM / +25% YoY in JPY) (Exhibit 2).   
- By equipment type, Japan front end equipment revenue (relevant to TEL) was +12% YoY in April. Assembly equipment revenue (relevant to DISCO) was +73% YoY due to easy comp. Testing equipment (relevant to Advantest) grew +26% YoY. (Exhibit 3-Exhibit 6).   
- We forecast global WFE to be +21.4% YoY in CY2026, and +18.2% in CY2027 (WFE Model, Report Link). We expect CY2026 will see strong growth from DRAM and NAND spending.

EXHIBIT 1: On three-month moving average basis, April SEAJ billings was +14% YoY in JPY.   
![](images/bdf59f71452a877e8a8aa028d1d3bceba7ec429ded50389cc241658280788179.jpg)  
Source: SEAJ and Bernstein analysis.

EXHIBIT 2: April single-month billings data was -38% MoM and +25% YoY in JPY.   
![](images/7ac4c87c354125374d6832d7a0f8b5f05ea89adec8fae445b55538b04675fa08.jpg)

<details>
<summary>bar_line</summary>

SEAJ Monthly Billings (Single Month)
| Date | SEMI Single Month Billings (JPY bn) | Billings YoY (%) |
|---|---|---|
| Jan-16 | 75 | 23 |
| Apr-16 | 100 | 14 |
| Jul-16 | 120 | 25 |
| Oct-16 | 180 | 34 |
| Jan-17 | 100 | 56 |
| Apr-17 | 250 | 40 |
| Jul-17 | 150 | 59 |
| Oct-17 | 180 | 27 |
| Jan-18 | 200 | 43 |
| Apr-18 | 150 | 43 |
| Jul-18 | 180 | 21 |
| Oct-18 | 150 | 54 |
| Jan-19 | 300 | 19 |
| Apr-19 | 150 | -5 |
| Jul-19 | 180 | 19 |
| Oct-19 | 150 | 30 |
| Jan-20 | 180 | 23 |
| Apr-20 | 200 | 38 |
| Jul-20 | 200 | 38 |
| Oct-20 | 150 | 23 |
| Jan-21 | 180 | 33 |
| Apr-21 | 380 | 64 |
| Jul-21 | 250 | 45 |
| Oct-21 | 300 | 60 |
| Jan-22 | 380 | 75 |
| Apr-22 | 450 | 50 |
| Jul-22 | 350 | 38 |
| Oct-22 | 380 | 52 |
| Jan-23 | 500 | 25 |
| Apr-23 | 350 | -15 |
| Jul-23 | 250 | -30 |
| Oct-23 | 380 | -15 |
| Jan-24 | 380 | -15 |
| Apr-24 | 550 | 60 |
| Jul-24 | 320 | -15 |
| Oct-24 | 380 | -15 |
| Jan-25 | 550 | -15 |
| Apr-25 | 600 | -15 |
| Jul-25 | 450 | -15 |
| Oct-25 | 550 | -15 |
| Jan-26 | 720 | -15 |
| Apr-26 | 450 | -15 |
The chart displays the monthly total billings in JPY billions and their year-over-year growth percentages for each month from January to April of the following year. The data is presented in a single column format with the same columns for the years. The bars represent "Billings YoY" and the line represents "SEMI Single Month Billings". The red dashed line indicates a baseline or target value around -2% to +9%.
</details>

Source: SEAJ and Bernstein analysis.

EXHIBIT 3: Monthly billings for Japanese WFE was +12% YoY / -50% MoM.   
![](images/0f9d53760321fcdccbb7f7379ef67ddd7ab7e14e36fbd4215adfe6fbee729682.jpg)

<details>
<summary>line</summary>

| Month    | YoY     | 3M avg (YoY) |
| -------- | ------- | ------------ |
| Jan-22   | 85%     | 85%          |
| May-22   | -30%    | 0%           |
| Sep-22   | 50%     | 40%          |
| Jan-23   | -10%    | 0%           |
| May-23   | -20%    | -10%         |
| Sep-23   | -40%    | -30%         |
| Jan-24   | 30%     | 0%           |
| May-24   | 85%     | 40%          |
| Sep-24   | 70%     | 30%          |
| Jan-25   | 10%     | 20%          |
| May-25   | -10%    | 0%           |
| Sep-25   | -30%    | 0%           |
| Jan-26   | 15%     | 5%           |
</details>

Source: SEAJ, Bernstein analysis.

EXHIBIT 4: Monthly billings for Japanese assembly SPE was +73% YoY / -39% MoM.   
![](images/418392ad5a462f58f86844fc628f616e05327581813b41363d3f6d621e7f632b.jpg)

<details>
<summary>line</summary>

| Month    | YoY     | 3M avg (YoY) |
| -------- | ------- | ------------ |
| Jan-22   | 60%     | 80%          |
| May-22   | -10%    | 10%          |
| Sep-22   | 30%     | 15%          |
| Jan-23   | -30%    | -10%         |
| May-23   | -40%    | -20%         |
| Sep-23   | -20%    | -15%         |
| Jan-24   | 35%     | 20%          |
| May-24   | 80%     | 70%          |
| Sep-24   | 30%     | 50%          |
| Jan-25   | 10%     | 15%          |
| May-25   | -20%    | 10%          |
| Sep-25   | 30%     | 15%          |
| Jan-26   | -10%    | -5%          |
</details>

Source: SEAJ, Bernstein analysis.

EXHIBIT 5: Monthly billings for Japanese testers was +26% YoY.   
![](images/262074e06997f1da2d1688f3ee472819b7e18acac3133299b1d0934efa062658.jpg)

<details>
<summary>line</summary>

| Date   | YoY     | 3M avg (YoY) |
|--------|---------|--------------|
| Jan-22 | ~40%    | ~30%         |
| May-22 | ~70%    | ~50%         |
| Sep-22 | ~10%    | ~60%         |
| Jan-23 | ~40%    | ~30%         |
| May-23 | ~-40%   | ~-20%        |
| Sep-23 | ~-20%   | ~-10%        |
| Jan-24 | ~20%    | ~-5%         |
| May-24 | ~80%    | ~60%         |
| Sep-24 | ~100%   | ~80%         |
| Jan-25 | ~180%   | ~100%        |
| May-25 | ~220%   | ~110%        |
| Sep-25 | ~40%    | ~50%         |
| Jan-26 | ~50%    | ~40%         |
</details>

Source: SEAJ, Bernstein analysis.

EXHIBIT 6: Monthly billings for Japanese testers was -14% MoM.   
![](images/1cfcd4bbef74d69315e76a06154aa56aa36153ae5d97ab9bdef22072b9fc5fcc.jpg)

<details>
<summary>line</summary>

| Month    | MoM     | 3M avg (MoM) |
| -------- | ------- | ------------ |
| Jan-22   | -50%    | 0%           |
| May-22   | 75%     | 0%           |
| Sep-22   | -25%    | 0%           |
| Jan-23   | 125%    | 0%           |
| May-23   | -75%    | -25%         |
| Sep-23   | 40%     | 0%           |
| Jan-24   | 130%    | 0%           |
| May-24   | -60%    | 0%           |
| Sep-24   | 40%     | 0%           |
| Jan-25   | -25%    | 0%           |
| May-25   | 45%     | 0%           |
| Sep-25   | -25%    | 0%           |
| Jan-26   | 35%     | 0%           |
</details>

Source: SEAJ, Bernstein analysis.

# April data suggests a downside for TEL / upside for Advantest in the June Quarter.

- As detailed in our previous trackers, SEAJ billings data (single month basis) can be used to estimate TEL quarterly SPE (semiconductor production equipment) revenue & hence the corporate revenue in the same quarter. The regression output is shown in Exhibit 7. Our regression suggests -18% QoQ for TEL's SPE revenue in the June quarter (equivalent to -18% total sales). This is below consensus of +6% QoQ (Exhibit 8, Exhibit 9).   
- Likewise, SEAJ billings data for testers can be used to estimate Advantest quarterly SPE revenue in the same quarter. The regression output is shown in Exhibit 10. We find the regression suggests +13% QoQ in Advantest's June quarter tester revenue. This is above consensus of +3% QoQ (Exhibit 11, Exhibit 12).

EXHIBIT 7: Our regression yields a decent correlation and should have good prediction power.   
TEL Quarterly SPE Sales vs. SEAJ 2M Billings of 1QCY23-4QCY25   
![](images/941626afaab1233af560a682aa51e1b31b7726b017ae4677bccfb402767630e4.jpg)

<details>
<summary>scatter</summary>

| SEAJ (JPY bn) | TEL (JPY bn) |
| ------------- | ------------ |
| 100           | 150          |
| 200           | 250          |
| 300           | 350          |
| 400           | 450          |
| 500           | 550          |
| 600           | 650          |
| 700           | 750          |
| 800           | 850          |
</details>

EXHIBIT 8: Our regression suggests TEL JunQ revenue could miss consensus. 

<table><tr><td rowspan="2"></td><td colspan="2">Revenue (JPY bn)</td><td rowspan="2">QoQ</td></tr><tr><td>4QFY26(1QCY26)</td><td>1QFY26E(2QCY26E)</td></tr><tr><td>SPE</td><td>703</td><td>575</td><td>-18%</td></tr><tr><td>Non-SPE</td><td>9</td><td>9</td><td></td></tr><tr><td>Total</td><td>712</td><td></td><td></td></tr><tr><td>Predicted by Regression</td><td></td><td>584</td><td>-18%</td></

[中间内容因长度限制已省略]

learning or artificial intelligence system, or as a prompt or input into any such system. You also may not, without Bernstein's express written consent, do any of the foregoing in connection with your own internal machine learning or artificial intelligence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient

makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engage in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek for independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
