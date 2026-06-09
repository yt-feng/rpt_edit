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
# China Quant Strategy

Calm Surface, Violent Undercurrents

MSCI China's headline realized volatility sits at the 29th percentile of its 10-year range (17% annualized vs. 22% avg) - the index looks calm. But beneath the surface, cross-sectional volatility has surged to the 98th percentile (16% vs. 10% avg). Individual stocks are diverging from each other at nearly the widest spread in a decade.

This divergence of low index vol vs. extreme stock-level vol signals a collapse in intra-stock correlation. The market appears not moving as individual stock moves are canceling each other out, not because nothing is happening (obviously).

The return dispersion is not only extremely large but also highly asymmetric. The distribution of stock returns in May was highly right-skewed (skewness = 2.56). The median stock fell 3.6%, but a handful of outsized winners pulled the mean to just -0.6%. Data on market participation and extremes breadth also show that most stocks declined, but the winners won big (Figure 1, 3, 4).

Who are the winners? A factor perspective is through the size: large caps are dominating. The large vs. small cap return spread was +6.1% in May, nearly the highest level in the last two years (Figure 2).

Our Multifactor Blend benefited directly from this dispersion regime. In May, the long book returned +3.0% while MSCI China fell 3.0%. With the shorts down 4.2%, the long/short combination delivered +7.2% on the month. With dispersion at decade-wide levels, a handful of stocks did most of the work. On the long side in particular, two outliers were responsible for the bulk of the alpha: Datang International Power (+109%) and Lenovo (+105%), followed by a cluster of A-share semis (Giga Device +51%, Suzhou TFC +49%, Montage Tech +47%).

To position for June, the Blend adds to the longs the H-shares of China Construction Bank and ICBC, alongside several A-share regional banks and IT supply-chain names (Suzhou Dongshan, Shengyi Tech, Shenzhen Longsys), etc.; it cuts some consumer/internet names (JD.com, Midea, Pop Mart) and parts of the commodity/cyclical bucket (Shaanxi Coal, China Hongqiao, Qinghai Salt Lake, COSCO Shipping), etc. See inside sections for more details.

MSCI China Realized Vol  
![](images/cc5440280adf50c0a16710c90ec7c4cc1fde11bc3462cfd961c74fa44e6966d2.jpg)

<details>
<summary>line chart</summary>

| Year | Rolling 21-Day Realized Volatility |
| ---- | ---------------------------------- |
| '16  | ~15%                               |
| '17  | ~18%                               |
| '18  | ~25%                               |
| '19  | ~30%                               |
| '20  | ~45%                               |
| '21  | ~35%                               |
| '22  | ~70%                               |
| '23  | ~60%                               |
| '24  | ~30%                               |
| '25  | ~55%                               |
| '26  | ~20%                               |
</details>

Source: JPM; MSCI, FactSet; As of May 31

MSCI China Cross-Sectional Vol  
![](images/a7f9a01b62ab07e8b57073e7e49d22a95f002696ab045ab633047affc25b1af9.jpg)

<details>
<summary>line chart</summary>

| Year | Cross-Sectional Volatility |
| ---- | -------------------------- |
| '16  | ~7%                        |
| '17  | ~8%                        |
| '18  | ~10%                       |
| '19  | ~9%                        |
| '20  | ~11%                       |
| '21  | ~14%                       |
| '22  | ~18%                       |
| '23  | ~22%                       |
| '24  | ~10%                       |
| '25  | ~14%                       |
| '26  | ~16%                       |
</details>

Source: JPM; MSCI, FactSet; As of May 31

## APAC Quantitative Strategy

## Evan Hu AC

(852) 2800-8508

evan.hu@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Robert Smith, PhD AC

(61-2) 9003-8808

robert.z.smith@JPM.com

JPM Securities Australia Limited

## Arpan Singh

(91-22) 6157-3301

arpan.singh@jpmchase.com

JPM India Private Limited

## Chris Chi

chris.chi@JPM.com

JPM Securities Australia Limited

## Global Head of Quant Strategy

## Khuram Chaudhry

(44-20) 7134-6297

khuram.chaudhry@JPM.com

JPM Securities plc

Figure 1: MSCI China Monthly Return Distribution of May  
![](images/c2c4da07a18ea6d2680d738b9ae496ca937c091a8d6ad9da6e03d044d30c6e6f.jpg)

<details>
<summary>histogram</summary>

| Statistic | Value   |
| --------- | ------- |
| Mean      | -0.6%   |
| Median    | -3.6%   |
| Skew      | 2.56    |
</details>

Source: JPM; MSCI, FactSet

Figure 2: Large vs. Small Cap Return Spread  
![](images/6e7ede8b480a7ad8705c1d47935d96183e655cecb5f6d27bad1fed0e78fd7523.jpg)

<details>
<summary>bar chart</summary>

| Month | Large vs. Small Cap Return Spread (%) |
|---|---|
| A | 2.0 |
| M | 2.4 |
| J | 6.1 |
| J | -0.3 |
| A | 3.4 |
| S | 0.2 |
| O | 1.1 |
| N | 0.8 |
| D | 3.5 |
| J | 1.9 |
| F | 1.9 |
| M | 1.4 |
| A | 2.9 |
| M | 1.3 |
| J | 2.3 |
| J | 3.4 |
| A | 2.4 |
| S | 1.9 |
| O | 0.8 |
| N | 2.0 |
| D | 1.6 |
| J | 2.0 |
| F | 0.8 |
| M | 4.7 |
| A | 4.5 |
| M | 6.1 |
</details>

Source: JPM; MSCI, FactSet; Large = top 50% by free float market cap.

Figure 3: Stocks Matching the Direction of the Market  
![](images/c50f0f45955f71ea5f37a5d6f6522fd9c3cb77e693401a2c71c7602f93594448.jpg)

<details>
<summary>bar chart</summary>

| Month | Up Month (%) | Down Month (%) |
| :--- | :--- | :--- |
| Jun | 63 | 0 |
| Jul '25 | 71 | 0 |
| Aug | 78 | 0 |
| Sep | 50 | 0 |
| Oct | 0 | 54 |
| Nov | 0 | 66 |
| Dec | 0 | 44 |
| Jan '26 | 61 | 0 |
| Feb | 0 | 40 |
| Mar | 0 | 80 |
| Apr | 70 | 0 |
| May | 0 | 67 |
</details>

Source: JPM; MSCI, FactSet

Figure 4: Stocks Near 52-Week Extremes  
![](images/2cf35e897a1403061dc103a4e66b0032cd6e029b2dce20fe9a949414329a1686.jpg)

<details>
<summary>area chart</summary>

| Month    | % Near 52W high | % Near 52W low |
| -------- | --------------- | -------------- |
| January  | ~15%            | ~0%            |
| February | ~18%            | ~0%            |
| March    | ~16%            | ~0%            |
| April    | ~5%             | ~30%           |
| May      | ~10%            | ~10%           |
| June     | ~8%             | ~30%           |
</details>

Source: JPM; MSCI, FactSet

Figure 5: Multifactor Blend: Long-Only vs. Market  
![](images/b0a7c06598e574032a1ac81f2da934ea8b115c234d29cff7662a331883891af8.jpg)

<details>
<summary>line chart</summary>

| Date     | Blend L/O | MSCI China |
| -------- | --------- | ---------- |
| 30-Apr   | 0%        | 0%         |
| 07-May   | ~3%       | ~3.5%      |
| 14-May   | ~5%       | ~3%        |
| 21-May   | ~-1%      | ~-2%       |
| 28-May   | ~3%       | ~-3%       |
</details>

Figure 6: Multifactor Blend: Long/Short  
![](images/e5dc0968a467fe44251f1c2cf299da044fb801edfaa9c0ef9bb503a1e08c5746.jpg)

<details>
<summary>line chart</summary>

| Date     | Blend Long | Blend Short | Blend L/S |
| -------- | ---------- | ----------- | --------- |
| 30-Apr   | 0%         | 0%          | 0%        |
| 07-May   | 3%         | 4%          | -1%       |
| 14-May   | 5%         | 4%          | 1%        |
| 21-May   | 1%         | -3%         | 4%        |
| 28-May   | 3%         | -4%         | 7%        |
</details>

Table 1: Multifactor Blend: Long Positions for June

<table><tr><td colspan="5">Top Longs</td></tr><tr><td>SEDOL</td><td>Company</td><td>Sector</td><td>Rank</td><td>1M Return</td></tr><tr><td>BD5CG58</td><td>ZHEJIANG CENTURY A(HK-C)</td><td>Comm Svcs</td><td>15</td><td>-7.7%</td></tr><tr><td>BD6QVW1</td><td>GIANT NETWORK A (HK-C)</td><td>Comm Svcs</td><td>20</td><td>-19.8%</td></tr><tr><td>6531827</td><td>GEELY AUTOMOBILE HLDGS</td><td>Cons Disc</td><td>23</td><td>-17.9%</td></tr><tr><td>BN4MKV3</td><td>NEW ORIENTAL EDUCATION</td><td>Cons Disc</td><td>49</td><td>-12.3%</td></tr><tr><td>B4MGD82</td><td>TAL EDUCATION GROUP ADR</td><td>Cons Disc</td><td>26</td><td>-12.7%</td></tr><tr><td>BZ04KX9</td><td>YADEA GROUP HOLDINGS</td><td>Cons Disc</td><td>25</td><td>-6.4%</td></tr><tr><td>BP3R2D9</td><td>SAIC MOTOR CORP A (HK-C)</td><td>Cons Disc</td><td>33</td><td>-9.7%</td></tr><tr><td>BP3R4T9</td><td>HUAYU AUTO SYS A (HK-C)</td><td>Cons Disc</td><td>36</td><td>-9.6%</td></tr><tr><td>BMGWW30</td><td>NONGFU SPRING CO H</td><td>Cons Staples</td><td>32</td><td>-6.1%</td></tr><tr><td>B01B1L9</td><td>CHINA MENGNIU DAIRY CO</td><td>Cons Staples</td><td>39</td><td>-2.3%</td></tr><tr><td>BD5CMC7</td><td>YANTAI JEREH OIL A(HK-C)</td><td>Energy</td><td>14</td><td>3.5%</td></tr><tr><td>B0LMTQ3</td><td>CHINA CONSTRUCTION BK H</td><td>Financials</td><td>38</td><td>-3.3%</td></tr><tr><td>B1G1QD8</td><td>ICBC H</td><td>Financials</td><td>47</td><td>-3.0%</td></tr><tr><td>6718976</td><td>CHINA LIFE INSURANCE H</td><td>Financials</td><td>48</td><td>0.9%</td></tr><tr><td>B2Q5H56</td><td>CHINA PACIFIC INS GRP H</td><td>Financials</td><td>57</td><td>-7.7%</td></tr><tr><td>B1W0JF2</td><td>CHINA CITIC BANK H</td><td>Financials</td><td>44</td><td>-8.6%</td></tr><tr><td>B5730Z1</td><td>NEW CHINA LIFE INS H</td><td>Financials</td><td>19</td><td>-5.4%</td></tr><tr><td>6264048</td><td>CHINA TAIPING INSURANCE</td><td>Financials</td><td>3</td><td>-10.9%</td></tr><tr><td>BD5CN46</td><td>HITHINK ROYAL A (HK-C)</td><td>Financials</td><td>6</td><td>-2.1%</td></tr><tr><td>BGHH0L6</td><td>WUXI APPTEC CO H</td><td>Health Care</td><td>22</td><td>-3.0%</td></tr><tr><td>BY9D3L9</td><td>3SBIO</td><td>Health Care</td><td>9</td><td>-20.1%</td></tr><tr><td>B3ZVDV0</td><td>SINOPHARM GROUP CO H</td><td>Health Care</td><td>8</td><td>-8.4%</td></tr><tr><td>BHWLWV4</td><td>WUXI APPTEC A (HK-C)</td><td>Health Care</td><td>17</td><td>-4.9%</td></tr><tr><td>BP3R4Z5</td><td>SHANGHAI PHARMA A (HK-C)</td><td>Health Care</td><td>29</td><td>-2.6%</td></tr><tr><td>6218089</td><td>LENOVO GROUP</td><td>IT</td><td>31</td><td>105.4%</td></tr><tr><td>BSBND71</td><td>YANGTZE OPTICAL FIBRE H</td><td>IT</td><td>51</td><td>14.1%</td></tr><tr><td>BFFIRM7</td><td>ZHONGJI INNO A(HK-C)</td><td>IT</td><td>4</td><td>36.7%</td></tr><tr><td>BG20N99</td><td>FOXCONN INDL A (HK-C)</td><td>IT</td><td>35</td><td>17.9%</td></tr><tr><td>B1YBT08</td><td>SUNNY OPTICAL TECH</td><td>IT</td><td>46</td><td>31.5%</td></tr><tr><td>BNHPMD5</td><td>CAMBRICON TECH A (HK-C)</td><td>IT</td><td>13</td><td>16.0%</td></tr><tr><td>BD761B9</td><td>EOPTOLINK TECH A (HK-C)</td><td>IT</td><td>1</td><td>35.7%</td></tr><tr><td>BD5CF28</td><td>SUZHOU DONGSHAN A (HK-C)</td><td>IT</td><td>53</td><td>15.2%</td></tr><tr><td>BL5P4J3</td><td>SUZHOU TFC A (HK-C)</td><td>IT</td><td>21</td><td>49.5%</td></tr><tr><td>B29SHS5</td><td>BYD ELECTRONIC INTL</td><td>IT</td><td>16</td><td>10.2%</td></tr><tr><td>BD76164</td><td>VICTORY GIANT A (HK-C)</td><td>IT</td><td>10</td><td>13.3%</td></tr><tr><td>BD5C7Z5</td><td>WUS PRINTED A (HK-C)</td><td>IT</td><td>54</td><td>30.6%</td></tr><tr><td>BNHSQK9</td><td>SHENZHEN LONGSYS A(HK-C)</td><td>IT</td><td>59</td><td>38.8%</td></tr><tr><td>BPXYTJ5</td><td>YUANJIE SEMICON A (HK-C)</td><td>IT</td><td>2</td><td>5.6%</td></tr><tr><td>BQWRJD6</td><td>SHENGYI ELECTS A (HK-C)</td><td>IT</td><td>5</td><td>27.2%</td></tr><tr><td>BD5CLB9</td><td>INSPUR ELECTRS A (HK-C)</td><td>IT</td><td>30</td><td>-6.4%</td></tr><tr><td>BD5CP28</td><td>TCL TECHNOLOGY A (HK-C)</td><td>IT</td><td>18</td><td>1.2%</td></tr><tr><td>BD5CGD6</td><td>WUHAN GUIDE INF A (HK-C)</td><td>IT</td><td>56</td><td>-12.4%</td></tr><tr><td>BD5CNJ1</td><td>ZHEJIANG DAHUA A (HK-C)</td><td>IT</td><td>55</td><td>-7.0%</td></tr><tr><td>BK71BV3</td><td>SHANGHAI BOCHU A (HK-C)</td><td>IT</td><td>40</td><td>16.0%</td></tr><tr><td>BFCCR07</td><td>YEALINK NETWORK A (HK-C)</td><td>IT</td><td>42</td><td>3.5%</td></tr><tr><td>BT9QPW8</td><td>CONTEMPORARY H</td><td>Industrials</td><td>50</td><td>22.4%</td></tr><tr><td>BHQPSY7</td><td>CONTEMPORARY AMP A(HK-C)</td><td>Industrials</td><td>45</td><td>-1.8%</td></tr><tr><td>BP91NG5</td><td>NINGBO DEYE TECH A(HK-C)</td><td>Industrials</td><td>11</td><td>9.7%</td></tr><tr><td>BP3R5T6</td><td>YUTONG BUS CO A (HK-C)</td><td>Industrials</td><td>27</td><td>-2.3%</td></tr><tr><td>B60FNV8</td><td>CHINA GOLD INTL RES (CN)</td><td>Materials</td><td>7</td><td>-9.3%</td></tr><tr><td>BSD3B20</td><td>ZIJIN GOLD INTL</td><td>Materials</td><td>58</td><td>-14.0%</td></tr><tr><td>BQ3RQ45</td><td>ZANGGE MINING A (HK-C)</td><td>Materials</td><td>60</td><td>-12.7%</td></tr><tr><td>BP3R585</td><td>ZHONGJIN GOLD A (HK-C)</td><td>Materials</td><td>34</td><td>-12.8%</td></tr><tr><td>BSY22K1</td><td>SHANDONG HONGQIA A(HK-C)</td><td>Materials</td><td>12</td><td>-13.8%</td></tr><tr><td>BZ0D1S8</td><td>CHIFENG JILONG A (HK-C)</td><td>Materials</td><td>37</td><td>-10.5%</td></tr><tr><td>BMXWXT6</td><td>CHINA RESOURCES MIXC</td><td>Real Estate</td><td>41</td><td>-11.2%</td></tr><tr><td>6099671</td><td>HUANENG POWER INTL H</td><td>Utilities</td><td>52</td><td>16.3%</td></tr><tr><td>6340078</td><td>KUNLUN ENERGY</td><td>Utilities</td><td>43</td><td>-5.1%</td></tr><tr><td>6913168</td><td>GUANGDONG INVESTMENT</td><td>Utilities</td><td>24</td><td>2.0%</td></tr><tr><td>6081690</td><td>BEIJING ENTERPRISES HLDG</td><td>Utilities</td><td>28</td><td>-0.6%</td></tr></table>

Source: JPM; MSCI, FactSet, I/B/E/S, Bloomberg Finance L.P.; As of May 31

Table 2: Multifactor Blend: Short Positions for June

<table><tr><td colspan="5">Top Shorts</td></tr><tr><td>SEDOL</td><td>Company</td><td>Sector</td><td>Rank</td><td>1M Return</td></tr><tr><td>BD5CN13</td><td>KUNLUN TECH CO A (HK-C)</td><td>Comm Svcs</td><td>16</td><td>-9.2%</td></tr><tr><td>BGJW376</td><td>MEITUAN B</td><td>Cons Disc</td><td>13</td><td>-11.8%</td></tr><tr><td>BP6FB33</td><td>XPENG (HK)</td><td>Cons Disc</td><td>33</td><td>4.6%</td></tr><tr><td>BMW5M00</td><td>LI AUTO (HK)</td><td>Cons Disc</td><td>42</td><td>-14.4%</td></tr><tr><td>BJLFLB4</td><td>BAIC BLUEPARK A (HK-C)</td><td>Cons Disc</td><td>47</td><td>-13.2%</td></tr><tr><td>BP3R477</td><td>GUANGZHOU AUTO A (HK-C)</td><td>Cons Disc</td><td>11</td><td>-12.8%</td></tr><tr><td>BD5CQP8</td><td>CCOOP GROUP A (HK-C)</td><td>Cons Disc</td><td>15</td><td>0.4%</td></tr><tr><td>BD5CPF1</td><td>JIANGSU YANGHE A (HK-C)</td><td>Cons Staples</td><td>12</td><td>-6.9%</td></tr><tr><td>BP3R5Q3</td><td>YONGHUI SUPERST A (HK-C)</td><td>Cons Staples</td><td>4</td><td>-2.7%</td></tr><tr><td>BP3R5S5</td><td>YANKUANG ENERGY A (HK-C)</td><td>Energy</td><td>54</td><td>-3.7%</td></tr><tr><td>BP3R682</td><td>SHANXI LUAN ENV A (HK-C)</td><td>Energy</td><td>46</td><td>0.0%</td></tr><tr><td>BD5CKB2</td><td>SHANXI COKING A(HK-C)</td><td>Energy</td><td>40</td><td>-2.3%</td></tr><tr><td>BD8P9J9</td><td>BANK OF SHANGHAI A(HK-C)</td><td>Financials</td><td>59</td><td>-2.8%</td></tr><tr><td>BZ0D003</td><td>ORIENT SEC CO A (HK-C)</td><td>Financials</td><td>48</td><td>0.6%</td></tr><tr><td>BD6QTV6</td><td>CNPC CAPITAL A (HK-C)</td><td>Financials</td><td>29</td><td>-16.6%</td></tr><tr><td>BK96BF0</td><td>CHINA ZHESHANG A (HK-C)</td><td>Financials</td><td>60</td><td>2.0%</td></tr><tr><td>BFB4KN8</td><td>ZHESHANG SEC A (HK-C)</td><td>Financials</td><td>26</td><td>-3.2%</td></tr><tr><td>BYYFJ78</td><td>SDIC CAPITAL CO A (HK-C)</td><td>Financials</td><td>52</td><td>-3.1%</td></tr><tr><td>BP3R6Z9</td><td>SOOCHOW SEC A (HK-C)</td><td>Financials</td><td>56</td><td>-1.5%</td></tr><tr><td>BFY9KS5</td><td>CAITONG SEC A (HK-C)</td><td>Financials</td><td>43</td><td>-4.2%</td></tr><tr><td>BK94886</td><td>TIANFENG SEC A(HK-C)</td><td>Financials</td><td>35</td><td>-5.5%</td></tr><tr><td>BD5CNY6</td><td>GUOYUAN SEC CO A (HK-C)</td><td>Financials</td><td>30</td><td>-2.1%</td></tr><tr><td>BLFJ7Y1</td><td>AKESO (CN)</td><td>Health Care</td><td>49</td><td>-13.1%</td></tr><tr><td>BP3R7Z6</td><td>ZHANGZHOU PIENTZ A(HK-C)</td><td>Health Care</td><td>51</td><td>-9.7%</td></tr><tr><td>BD5LWT1</td><td>HEBEI CHANGSHAN A (HK-C)</td><td>Health Care</td><td>9</td><td>0.7%</td></tr><tr><td>BL61WD0</td><td>CSPC INNOVATION A (HK-C)</td><td>Health Care</td><td>38</td><td>-11.0%</td></tr><tr><td>BMXTWX4</td><td>BEIJING WANTAI A (HK-C)</td><td>Health Care</td><td>2</td><td>-11.0%</td></tr><tr><td>BD5CJY8</td><td>CHONGQING ZHIFEI A(HK-C)</td><td>Health Care</td><td>1</td><td>-9.4%</td></tr><tr><td>BD5CDB3</td><td>CHANGCHUN HIGH A (HK-C)</td><td>Health Care</td><td>36</td><td>-12.4%</td></tr><tr><td>BS5YNY7</td><td>HORIZON ROBOTICS B</td><td>IT</td><td>58</td><td>-27.1%</td></tr><tr><td>B28XTR4</td><td>GCL TECHNOLOGY HOLDINGS</td><td>IT</td><td>8</td><td>-7.8%</td></tr><tr><td>BMDJ6Q5</td><td>PONY AI</td><td>IT</td><td>32</td><td>6.5%</td></tr><tr><td>BNR4NR3</td><td>NATIONAL SILICON A(HK-C)</td><td>IT</td><td>19</td><td>35.7%</td></tr><tr><td>BP3R3R0</td><td>SANAN OPTOELEC A (HK-C)</td><td>IT</td><td>25</td><td>15.5%</td></tr><tr><td>BD5M1Y2</td><td>ZHEJIANG JINGSH A (HK-C)</td><td>IT</td><td>57</td><td>20.7%</td></tr><tr><td>BP3RCK6</td><td>TONGWEI CO A (HK-C)</td><td>IT</td><td>7</td><td>-14.2%</td></tr><tr><td>BK4XS11</td><td>MAXSCEND A (HK-C)</td><td>IT</td><td>21</td><td>9.6%</td></tr><tr><td>BNHPM68</td><td>JINKO SOLAR A (HK-C)</td><td>IT</td><td>10</td><td>-11.0%</td></tr><tr><td>BNRLFT0</td><td>XINJIANG DAQO A (HK-C)</td><td>IT</td><td>18</td><td>-11.7%</td></tr><tr><td>BD5CMT4</td><td>TCL ZHONGHUAN A (HK-C)</td><td>IT</td><td>5</td><td>13.7%</td></tr><tr><td>BD5CM72</td><td>GUANGZHOU HAIGE A (HK-C)</td><td>IT</td><td>37</td><td>-0.3%</td></tr><tr><td>BP3R6C6</td><td>YONYOU NETWORK A (HK-C)</td><td>IT</td><td>23</td><td>-10.4%</td></tr><tr><td>BNHPNF4</td><td>EVERDISPLAY OPTR A(HK-C)</td><td>IT</td><td>22</td><td>5.0%</td></tr><tr><td>BMVB500</td><td>JA SOLAR TECH A (HK-C)</td><td>IT</td><td>31</td><td>-15.4%</td></tr><tr><td>BK4PZC7</td><td>WINGTECH TECH A (HK-C)</td><td>IT</td><td>20</td><td>-25.8%</td></tr><tr><td>BP3R518</td><td>AECC AVIATION A (HK-C)</td><td>Industrials</td><td>53</td><td>-9.4%</td></tr><tr><td>BNHPGJ9</td><td>ROBOTECHNIK INT A (HK-C)</td><td>Industrials</td><td>24</td><td>33.9%</td></tr><tr><td>BP3R4G6</td><td>AIR CHINA A (HK-C)</td><td>Industrials</td><td>28</td><td>2.2%</td></tr><tr><td>BP3R5X0</td><td>CHINA EAST AIR A (HK-C)</td><td>Industrials</td><td>27</td><td>2.6%</td></tr><tr><td>BP3R6G0</td><td>CHINA STH AIRL A (HK-C)</td><td>Industrials</td><td>55</td><td>2.5%</td></tr><tr><td>BP3R4K0</td><td>METALLURGICAL A (HK-C)</td><td>Industrials</td><td>44</td><td>-2.5%</td></tr><tr><td>BP3R488</td><td>INNER MONGOL BAO A(HK-C)</td><td>Materials</td><td>41</td><td>-11.8%</td></tr><tr><td>BP3R5D0</td><td>SHANDONG GOLD A (HK-C)</td><td>Materials</td><td>50</td><td

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 07 Jun 2026 05:58 PM HKT

Disseminated 07 Jun 2026 05:58 PM HKT
"""
