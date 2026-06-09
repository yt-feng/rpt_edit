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
# Japan SMID Monitor: How do yuutai SMIDs perform during corrections?

In this month's edition of the Japan SMID Monitor, we focus on the performance of Japanese SMID stocks with kabunushi yuutai (or shareholder benefits) programs in place, versus those that do not. We first wrote about SMID companies with yuutai programs in Japan SMID Monitor: Measuring the impact of kabunushi yuutai (11 April 2025). We then followed this up with Japan Portfolio Strategy: Unequal equities - How do stocks with shareholder benefits perform during major market corrections? (3 June 2026), which focused more on the broader yuutai universe in Japan. Kabunushi yuutai or ‘shareholder benefits’ programs involve giving domestic Japanese retail investors some sort of in-kind gift or discount for owning a minimum number of shares in the company. Japanese domestic institutions and overseas investors are not eligible for these yuutai programs. One third of listed companies have yuutai programs in place and have tended to trade at a valuation premium to their sector peers, and their price action usually more resilient during corrections.

Japan SMID companies exhibit similar characteristics to their larger cap peers: Japanese SMID stocks with yuutai programs in place tend to have a higher number of retail shareholders, which provides a defensive overlay because retail shareholders usually behave in a contrarian manner during downturns (i.e., they buy when the market is falling), and also because they want to maintain their yuutai benefits even during corrections, so they are less inclined to sell (Exhibit 6).  
Japan SMID companies with yuutai have tended to provide downside protection during major market corrections: Yuutai companies have tended to provide superior volatility-adjusted returns during major market downturns, versus those that did not have yuutai programs in place. They have also tended to trade at a significant valuation premia to their sector peers (Exhibit 7).  
■ History suggests Japan SMID stocks with yuutai programs and high dividend yields should perform well during corrections: We have included in Exhibit 5 a screen of 19 Japanese SMID names which have some sort of yuutai program in place, and which are trading with a dividend yield of at least 3.0%.  
Individuals and Foreigners net bought TSE Growth, and sold TSE Standard: As can be seen in Exhibit 1 and Exhibit 2 below, for the month of May, individuals and foreigners net sold -¥12.6bn and -¥9.5bn of Standard cash equities, whilst buying ¥11.1bn and ¥15.5bn respectively of Growth cash.

Bruce Kirk, CFA

+81(3)4587-9950 | bruce.kirk@gs.com

GS Japan Co., Ltd.

Julius Chan

+81(3)4587-1789 | julius.chan@gs.com

GS Japan Co., Ltd.

Exhibit 1: TSE Standard net buying  
2-year chart as of May 29 2026, JPY bn  
![](images/d48e1b651dda341458186a9b863cad48dc7912cb8f93659b9b449801abdb10b5.jpg)

<details>
<summary>line chart</summary>

| Date   | Foreigners | Individuals + Investment Trusts | Business Corporations | Trust Banks |
|--------|------------|----------------------------------|------------------------|-------------|
| 5/24   | 0          | 0                                | 0                      | 0           |
| 8/24   | 50         | -50                              | 50                     | -50         |
| 11/24  | 75         | -75                              | 75                     | -75         |
| 2/25   | 100        | -100                             | 100                    | -100        |
| 5/25   | 125        | -125                             | 125                    | -125        |
| 8/25   | 150        | -150                             | 150                    | -150        |
| 11/25  | 175        | -175                             | 175                    | -175        |
| 2/26   | 200        | -200                             | 200                    | -200        |
| 4/26   | 225        | -225                             | 225                    | -225        |
</details>

Source: Bloomberg, Tokyo Stock Exchange

Exhibit 2: TSE Growth net buying  
2-year chart as of May 29 2026, JPY bn  
![](images/260c9ce7c1c691d9efd5e30563ef95abd1443d931fcb7cd2ada77ddc1e0c4af5.jpg)

<details>
<summary>line chart</summary>

| Date   | Foreigners | Individuals + Investment Trusts | Business Corporations | Trust Banks |
|--------|------------|----------------------------------|------------------------|-------------|
| 5/24   | 0          | 0                                | 0                      | 0           |
| 8/24   | -50        | 50                               | 0                      | 0           |
| 11/24  | -100       | 100                              | 0                      | 0           |
| 2/25   | -150       | 150                              | 0                      | 0           |
| 5/25   | -200       | 200                              | 0                      | 0           |
| 8/25   | -250       | 300                              | 0                      | 0           |
| 11/25  | -300       | 450                              | 0                      | 0           |
| 2/26   | -350       | 600                              | 0                      | 0           |
</details>

Source: Bloomberg, Tokyo Stock Exchange

## GS Covered Japan SMID Stocks

Exhibit 3: GS covered SMID stocks ranked by monthly performance

Data as of May 29 2026

<table><tr><td>Ticker</td><td>Name</td><td>Analyst</td><td>1W</td><td>2W</td><td>1M</td><td>3M</td><td>6M</td><td>YTD</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>Daiki Takayama</td><td>63%</td><td>119%</td><td>125%</td><td>209%</td><td>355%</td><td>319%</td></tr><tr><td>6324</td><td>Harmonic Drive Systems</td><td>Yuichiro Isayama</td><td>11%</td><td>10%</td><td>64%</td><td>71%</td><td>152%</td><td>106%</td></tr><tr><td>6966</td><td>Mitsui High-tec Inc.</td><td>Kota Yuzawa</td><td>37%</td><td>42%</td><td>53%</td><td>17%</td><td>29%</td><td>34%</td></tr><tr><td>4443</td><td>Sansan Inc.</td><td>Norihiro Miyazaki</td><td>14%</td><td>28%</td><td>30%</td><td>43%</td><td>0%</td><td>-3%</td></tr><tr><td>6254</td><td>NOM Micro Science</td><td>Takeru Adachi</td><td>-8%</td><td>-7%</td><td>22%</td><td>30%</td><td>47%</td><td>54%</td></tr><tr><td>4205</td><td>Zeon</td><td>Atsushi Ikeda</td><td>4%</td><td>-2%</td><td>19%</td><td>2%</td><td>23%</td><td>22%</td></tr><tr><td>5253</td><td>Cover Corp.</td><td>Norihiro Miyazaki</td><td>-9%</td><td>9%</td><td>16%</td><td>-8%</td><td>-4%</td><td>6%</td></tr><tr><td>6508</td><td>Meidensha</td><td>Ryo Harada</td><td>-9%</td><td>-8%</td><td>16%</td><td>29%</td><td>74%</td><td>81%</td></tr><tr><td>3923</td><td>Rakus Co.</td><td>Norihiro Miyazaki</td><td>7%</td><td>24%</td><td>16%</td><td>15%</td><td>-19%</td><td>-3%</td></tr><tr><td>6754</td><td>Anritsu</td><td>Ryo Harada</td><td>-1%</td><td>7%</td><td>14%</td><td>50%</td><td>92%</td><td>103%</td></tr><tr><td>6055</td><td>Japan Material</td><td>Takeru Adachi</td><td>3%</td><td>3%</td><td>14%</td><td>-6%</td><td>21%</td><td>33%</td></tr><tr><td>6951</td><td>JEOL</td><td>Shuhei Nakamura</td><td>8%</td><td>2%</td><td>12%</td><td>3%</td><td>48%</td><td>41%</td></tr><tr><td>6407</td><td>CKD</td><td>Yuichiro Isayama</td><td>-3%</td><td>-3%</td><td>12%</td><td>18%</td><td>154%</td><td>114%</td></tr><tr><td>4061</td><td>Denka</td><td>Atsushi Ikeda</td><td>16%</td><td>16%</td><td>11%</td><td>22%</td><td>64%</td><td>63%</td></tr><tr><td>4369</td><td>Tri Chemical Laboratories Inc</td><td>Atsushi Ikeda</td><td>8%</td><td>10%</td><td>11%</td><td>-1%</td><td>35%</td><td>39%</td></tr><tr><td>4202</td><td>Daicel</td><td>Atsushi Ikeda</td><td>5%</td><td>12%</td><td>8%</td><td>-19%</td><td>1%</td><td>-5%</td></tr><tr><td>6674</td><td>GS Yuasa Corp.</td><td>Kota Yuzawa</td><td>7%</td><td>2%</td><td>6%</td><td>18%</td><td>58%</td><td>75%</td></tr><tr><td>6622</td><td>Daihen</td><td>Ryo Harada</td><td>-3%</td><td>-6%</td><td>6%</td><td>9%</td><td>82%</td><td>59%</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>Makoto Kuroda</td><td>-4%</td><td>-2%</td><td>5%</td><td>-5%</td><td>11%</td><td>6%</td></tr><tr><td>4194</td><td>Visional</td><td>Norihiro Miyazaki</td><td>0%</td><td>5%</td><td>5%</td><td>7%</td><td>-25%</td><td>-22%</td></tr><tr><td>7581</td><td>Saizeriya</td><td>Sho Kawano</td><td>1%</td><td>4%</td><td>3%</td><td>-24%</td><td>-9%</td><td>-3%</td></tr><tr><td>9616</td><td>Kyoritsu Maintenance</td><td>Norihiro Miyazaki</td><td>1%</td><td>6%</td><td>3%</td><td>-6%</td><td>-12%</td><td>-11%</td></tr><tr><td>4912</td><td>Lion</td><td>Takashi Miyazaki</td><td>1%</td><td>5%</td><td>3%</td><td>-12%</td><td>-2%</td><td>-2%</td></tr><tr><td>5032</td><td>ANYCOLOR</td><td>Norihiro Miyazaki</td><td>-1%</td><td>5%</td><td>2%</td><td>-26%</td><td>-55%</td><td>-41%</td></tr><tr><td>6592</td><td>Mabuchi Motor</td><td>Daiki Takayama</td><td>0%</td><td>-3%</td><td>2%</td><td>-16%</td><td>12%</td><td>8%</td></tr><tr><td>2222</td><td>Kotobuki Spirits Co.</td><td>Norihiro Miyazaki</td><td>4%</td><td>-2%</td><td>0%</td><td>5%</td><td>13%</td><td>14%</td></tr><tr><td>7988</td><td>Nifco Inc.</td><td>Kota Yuzawa</td><td>10%</td><td>0%</td><td>-1%</td><td>-18%</td><td>-6%</td><td>-7%</td></tr><tr><td>4922</td><td>Kose Holdings</td><td>Takashi Miyazaki</td><td>6%</td><td>8%</td><td>-1%</td><td>-10%</td><td>9%</td><td>7%</td></tr><tr><td>3116</td><td>Toyota Boshoku</td><td>Kota Yuzawa</td><td>2%</td><td>0%</td><td>-3%</td><td>-28%</td><td>-6%</td><td>-9%</td></tr><tr><td>8570</td><td>Aeon Financial Service Co.</td><td>Makoto Kuroda</td><td>-3%</td><td>-3%</td><td>-3%</td><td>-14%</td><td>-4%</td><td>-13%</td></tr><tr><td>9706</td><td>Japan Airport Terminal</td><td>Norihiro Miyazaki</td><td>-2%</td><td>-4%</td><td>-4%</td><td>-9%</td><td>7%</td><td>10%</td></tr><tr><td>2229</td><td>Calbee Inc</td><td>Takashi Miyazaki</td><td>-2%</td><td>0%</td><td>-4%</td><td>-6%</td><td>-2%</td><td>-3%</td></tr><tr><td>6432</td><td>Takeuchi MFG</td><td>Takeru Adachi</td><td>1%</td><td>-4%</td><td>-5%</td><td>-9%</td><td>-4%</td><td>1%</td></tr><tr><td>5805</td><td>SWCC</td><td>Ryo Harada</td><td>8%</td><td>-5%</td><td>-5%</td><td>-4%</td><td>39%</td><td>44%</td></tr><tr><td>4478</td><td>freee K.K.</td><td>Chikai Tanaka, CFA</td><td>-6%</td><td>-3%</td><td>-5%</td><td>-2%</td><td>-30%</td><td>-30%</td></tr><tr><td>4587</td><td>PeptiDream</td><td>Akinori Ueda, Ph.D.</td><td>-9%</td><td>-2%</td><td>-5%</td><td>-22%</td><td>-38%</td><td>-33%</td></tr><tr><td>6728</td><td>Ulvac</td><td>Shuhei Nakamura</td><td>1%</td><td>0%</td><td>-6%</td><td>-9%</td><td>42%</td><td>34%</td></tr><tr><td>6770</td><td>Alps Alpine</td><td>Daiki Takayama</td><td>1%</td><td>-2%</td><td>-7%</td><td>-7%</td><td>7%</td><td>9%</td></tr><tr><td>6103</td><td>Okuma</td><td>Yuichiro Isayama</td><td>1%</td><td>-15%</td><td>-8%</td><td>-13%</td><td>8%</td><td>12%</td></tr><tr><td>7014</td><td>Namura Shipbuilding Co.</td><td>Norihiro Miyazaki</td><td>-2%</td><td>-15%</td><td>-10%</td><td>-33%</td><td>-19%</td><td>6%</td></tr><tr><td>4483</td><td>JMDC</td><td>Akinori Ueda, Ph.D.</td><td>2%</td><td>6%</td><td>-15%</td><td>-32%</td><td>-34%</td><td>-29%</td></tr><tr><td>7383</td><td>Net Protections Holdings</td><td>Makoto Kuroda</td><td>-8%</td><td>-18%</td><td>-17%</td><td>-34%</td><td>-41%</td><td>-32%</td></tr></table>

Source: FactSet, Data compiled by GS Global Investment Research

Exhibit 4: GS covered SMID stocks by analyst, 1M performance and consensus valuations

Data as of May 29 2026

<table><tr><td>Ticker</td><td>Name</td><td>Analyst</td><td>1M price return</td><td>P/B</td><td>P/E NTM</td><td>ROE FY26E</td><td>DY FY26E</td></tr><tr><td>4587</td><td>PeptiDream</td><td>Akinori Ueda, Ph.D.</td><td>-5%</td><td>2.8</td><td>9.1</td><td>30.4</td><td>0.0</td></tr><tr><td>4483</td><td>JMDC</td><td>Akinori Ueda, Ph.D.</td><td>-15%</td><td>2.2</td><td>20.0</td><td>9.9</td><td>0.7</td></tr><tr><td>4205</td><td>Zeon</td><td>Atsushi Ikeda</td><td>19%</td><td>1.1</td><td>13.8</td><td>8.1</td><td>3.5</td></tr><tr><td>4061</td><td>Denka</td><td>Atsushi Ikeda</td><td>11%</td><td>1.2</td><td>19.1</td><td>7.4</td><td>2.3</td></tr><tr><td>4369</td><td>Tri Chemical Laboratories Inc.</td><td>Atsushi Ikeda</td><td>11%</td><td>3.4</td><td>23.7</td><td>13.4</td><td>1.0</td></tr><tr><td>4202</td><td>Daicel</td><td>Atsushi Ikeda</td><td>8%</td><td>1.0</td><td>8.1</td><td>12.6</td><td>4.8</td></tr><tr><td>4478</td><td>freee K.K.</td><td>Chikai Tanaka, CFA</td><td>-5%</td><td>6.4</td><td>36.7</td><td>4.7</td><td>0.0</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>Daiki Takayama</td><td>125%</td><td>5.4</td><td>72.0</td><td>7.3</td><td>0.6</td></tr><tr><td>6592</td><td>Mabuchi Motor</td><td>Daiki Takayama</td><td>2%</td><td>1.1</td><td>18.0</td><td>6.1</td><td>3.1</td></tr><tr><td>6770</td><td>Alps Alpine</td><td>Daiki Takayama</td><td>-7%</td><td>0.9</td><td>15.1</td><td>6.1</td><td>2.9</td></tr><tr><td>6966</td><td>Mitsui High-tec Inc.</td><td>Kota Yuzawa</td><td>53%</td><td>1.6</td><td>21.5</td><td>7.2</td><td>1.9</td></tr><tr><td>6674</td><td>GS Yuasa Corp.</td><td>Kota Yuzawa</td><td>6%</td><td>1.7</td><td>16.7</td><td>9.9</td><td>1.4</td></tr><tr><td>7988</td><td>Nifco Inc.</td><td>Kota Yuzawa</td><td>-1%</td><td>1.4</td><td>10.5</td><td>12.8</td><td>2.8</td></tr><tr><td>3116</td><td>Toyota Boshoku</td><td>Kota Yuzawa</td><td>-3%</td><td>0.8</td><td>8.0</td><td>10.3</td><td>3.9</td></tr><tr><td>8304</td><td>Aozora Bank</td><td>Makoto Kuroda</td><td>5%</td><td>0.8</td><td>12.7</td><td>6.1</td><td>3.7</td></tr><tr><td>8570</td><td>Aeon Financial Service Co.</td><td>Makoto Kuroda</td><td>-3%</td><td>0.7</td><td>14.1</td><td>4.4</td><td>3.5</td></tr><tr><td>7383</td><td>Net Protections Holdings</td><td>Makoto Kuroda</td><td>-17%</td><td>1.7</td><td>15.9</td><td>9.9</td><td>0.0</td></tr><tr><td>4443</td><td>Sansan Inc.</td><td>Norihiro Miyazaki</td><td>30%</td><td>14.2</td><td>23.8</td><td>35.8</td><td>0.0</td></tr><tr><td>5253</td><td>Cover Corp.</td><td>Norihiro Miyazaki</td><td>16%</td><td>5.3</td><td>13.7</td><td>29.5</td><td>0.0</td></tr><tr><td>3923</td><td>Rakus Co.</td><td>Norihiro Miyazaki</td><td>16%</td><td>13.7</td><td>17.6</td><td>71.3</td><td>0.6</td></tr><tr><td>4194</td><td>Visional</td><td>Norihiro Miyazaki</td><td>5%</td><td>4.7</td><td>15.9</td><td>23.0</td><td>0.0</td></tr><tr><td>9616</td><td>Kyoritsu Maintenance</td><td>Norihiro Miyazaki</td><td>3%</td><td>1.6</td><td>11.5</td><td>14.5</td><td>1.9</td></tr><tr><td>5032</td><td>ANYCOLOR</td><td>Norihiro Miyazaki</td><td>2%</td><td>8.0</td><td>9.7</td><td>59.9</td><td>3.1</td></tr><tr><td>2222</td><td>Kotobuki Spirits Co.</td><td>Norihiro Miyazaki</td><td>0%</td><td>6.7</td><td>22.2</td><td>27.3</td><td>1.9</td></tr><tr><td>9706</td><td>Japan Airport Terminal</td><td>Norihiro Miyazaki</td><td>-4%</td><td>2.1</td><td>18.2</td><td>11.9</td><td>1.9</td></tr><tr><td>7014</td><td>Namura Shipbuilding Co.</td><td>Norihiro Miyazaki</td><td>-10%</td><td>1.9</td><td>11.8</td><td>16.8</td><td>1.6</td></tr><tr><td>6508</td><td>Meidensha</td><td>Ryo Harada</td><td>16%</td><td>2.6</td><td>22.2</td><td>12.3</td><td>1.4</td></tr><tr><td>6754</td><td>Anritsu</td><td>Ryo Harada</td><td>14%</td><td>4.4</td><td>40.6</td><td>10.1</td><td>1.1</td></tr><tr><td>6622</td><td>Daihen</td><td>Ryo Harada</td><td>6%</td><td>2.4</td><td>21.3</td><td>10.8</td><td>1.4</td></tr><tr><td>5805</td><td>SWCC</td><td>Ryo Harada</td><td>-5%</td><td>4.5</td><td>20.7</td><td>20.1</td><td>1.8</td></tr><tr><td>7581</td><td>Saizeriya</td><td>Sho Kawano</td><td>3%</td><td>2.2</td><td>18.7</td><td>10.3</td><td>0.6</td></tr><tr><td>6951</td><td>JEOL</td><td>Shuhei Nakamura</td><td>12%</td><td>2.4</td><td>16.0</td><td>14.9</td><td>1.9</td></tr><tr><td>6728</td><td>Ulvac</td><td>Shuhei Nakamura</td><td>-6%</td><td>2.1</td><td>19.4</td><td>8.5</td><td>1.7</td></tr><tr><td>4912</td><td>Lion</td><td>Takashi Miyazaki</td><td>3%</td><td>1.4</td><td>17.2</td><td>7.9</td><td>2.1</td></tr><tr><td>4922</td><td>Kose Holdings</td><td>Takashi Miyazaki</td><td>-1%</td><td>1.1</td><td>23.8</td><td>4.6</td><td>2.7</td></tr><tr><td>2229</td><td>Calbee Inc</td><td>Takashi Miyazaki</td><td>-4%</td><td>1.7</td><td>18.7</td><td>9.1</td><td>2.3</td></tr><tr><td>6254</td><td>NOM Micro Science</td><td>Takeru Adachi</td><td>22%</td><td>4.5</td><td>21.5</td><td>22.4</td><td>1.6</td></tr><tr><td>6055</td><td>Japan Material</td><td>Takeru Adachi</td><td>14%</td><td>3.4</td><td>19.3</td><td>16.6</td><td>1.5</td></tr><tr><td>6432</td><td>Takeuchi MFG</td><td>Takeru Adachi</td><td>-5%</td><td>1.7</td><td>12.0</td><td>12.6</td><td>3.2</td></tr><tr><td>6324</td><td>Harmonic Drive Systems</td><td>Yuichiro Isayama</td><td>64%</td><td>9.2</td><td>122.3</td><td>6.5</td><td>0.3</td></tr><tr><td>6407</td><td>CKD</td><td>Yuichiro Isayama</td><td>12%</td><td>2.9</td><td>24.7</td><td>11.0</td><td>1.6</td></tr><tr><td>6103</td><td>Okuma</td><td>Yuichiro Isayama</td><td>-8%</td><td>1.0</td><td>15.2</td><td>6.8</td><td>2.7</td></tr></table>

Source: I/B/E/S, Toyo Keizai, FactSet, Data compiled by GS Global Investment Research

## SMID Yuutai + dividends screen

Our SMID Y+D screen includes companies with yuutai programs in place, and which also offer a relatively high cash dividend of at least 3% to all shareholders. Our full screening criteria were as follows:

■ 6M ADTV of over US\$5mn and with a market cap of ¥50-500bn.  
■ Yuutai program in place.  
■ FY0 dividend yield > 3%.  
■ Listed for at least 3 years.

Exhibit 5: SMID Yuutai + Dividends Screen  
Data as of May 1, 2026, rebalanced semiannually

<table><tr><td rowspan="3">Ticker</td><td rowspan="3">Company Name</td><td rowspan="3">GICS Sector</td><td rowspan="3">Quoted Price (JPY)</td><td>50 - 500</td><td>&gt;5</td><td colspan="2">&gt;0</td><td>&gt;3</td></tr><tr><td colspan="2">Size and Liquidity</td><td colspan="2">Valuations</td><td>Returns</td></tr><tr><td>Mkt Cap(JPY bn)</td><td>6M ADTV(US$ mn)</td><td>FY1 P/E(x)</td><td>FY1 P/B(x)</td><td>FY0 D/Y(%)</td></tr><tr><td colspan="9">Yuutai + dividend screen</td></tr><tr><td>1860</td><td>TODA CORP</td><td>Industrials</td><td>1415.0</td><td>450.0</td><td>6.4</td><td>13.8</td><td>1.1</td><td>4.1</td></tr><tr><td>9076</td><td>SEINO HOLDINGS</td><td>Industrials</td><td>2391.5</td><td>448.8</td><td>7.6</td><td>16.1</td><td>0.9</td><td>4.3</td></tr><tr><td>6141</td><td>DMG MORI CO LTD</td><td>Industrials</td><td>3000.0</td><td>427.0</td><td>25.0</td><td>31.5</td><td>1.2</td><td>3.5</td></tr><tr><td>6417</td><td>SANKYO CO LTD</td><td>Consumer Discretionary</td><td>1834.5</td><td>421.9</td><td>13.1</td><td>7.5</td><td>1.5</td><td>4.9</td></tr><tr><td>6592</td><td

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
