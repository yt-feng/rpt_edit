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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Base Metals Supply & Demand Tracker

Chinese exports are the relief valve for ex-China aluminium tightness

## Copper:

- China's apparent and end-use copper consumption diverge markedly. Our consumption-weighted end-use indicator for Chinese copper demand declined by 4% yoy (now +1.2% yoy YTD through 4M26) amid continued weakness in renewables installations and white goods production (Figure 22). The slowdown comes despite continued strong grid demand, EV production and product exports which work to offset weakness in other sectors. At the same time, Chinese apparent consumption was remarkable in April (+9% yoy), with inventory draws boosting overall figures reflecting the level of inventory destock across the supply chain over the 4Q25/1Q26 buyers strike in China. More recently, drawing momentum in Chinese inventory has leveled off in recent weeks as copper prices have ranged between \$13,500-14,000/mt (Figure 23).  
- US tariff review forthcoming. Later this month, by June 30, 2026, the US Commerce Secretary is to provide the President with an update on whether additional Section 232 copper tariff modifications are necessary. Our view remains that it is more likely than not that the Trump administration will enact an escalating tariff as was laid out in last July's original executive order (i.e. starting at $15\%$ in 2027, increasing to $30\%$ a year later) to 1) ensure that all the copper that has already been imported into the US stays onshore and 2) keep this excess US inventory as a critical reserve, rather than enact policy which incentivizes it to quickly destock in the coming years. A continued strong import pull into the US in the coming quarters would continue to strain ex-US cathode supply, particularly over periods where China's import arb is also open.

## Aluminium:

- Chinese aluminium semis and finished product exports are the relief valve for ex-China tightness. As LME inventories continue to draw lower to 330 kmt, Chinese visible inventory levels are still sitting near multi-year highs at \~1.4 mmt. With the semis export arb from China to rest of Asia open and at attractive levels (Figure 72), we continue to expect strong exports out of China to accelerate weekly withdrawals from onshore aluminium inventory in China (Figure 53 & Figure 55). So far, in the last 6 weeks only around 90 kmt has been drawn from SHFE and regional warehouses in China as production levels have risen and imports of aluminum have remained firm, with drawing activity only picking up since mid-May.  
- Producers in China are reaping the rewards of higher aluminium prices. Refined production in China in April grew by 3.4% yoy, running at an annualized level of 45 mmt, contributing to YTD growth of \~4% yoy according to CRU (Figure 70). Chinese producers are currently highly incentivized to keep churning out production towards the limiting cap amid elevated aluminium prices. We continue to monitor for disruptions of bauxite exports from Guinea, as this could become a serious bottleneck for Chinese producers

## Global Commodities Research

## Gregory C. Shearer

(44-20) 7134-8161

gregory.c.shearer@JPM.com

JPM Securities plc

## Ali A. Ibrahim

(44-20) 3493-6438

ali.ibrahim@JPM.com

JPM Securities plc

## Ananyashree Gupta

(91-22) 6157 3627

ananyashree.gupta@jpmchase.com

JPM India Private Limited

Contents

<table><tr><td>Base Metals Supply &amp; Demand Tracker</td><td>1</td></tr><tr><td>Global demand indicators</td><td>3</td></tr><tr><td>China demand indicators</td><td>5</td></tr><tr><td>Copper</td><td>9</td></tr><tr><td>Aluminium</td><td>16</td></tr><tr><td>Zinc</td><td>21</td></tr><tr><td>Nickel</td><td>25</td></tr><tr><td>JPM metals price forecasts</td><td>28</td></tr></table>

as $75\%$ of the country's bauxite imports come from Guinea alone. While bauxite imports from Guinea were up by $13\%$ yoy in April, a sharp change here could eventually threaten Chinese output and potentially also influence Chinese policy around exports as domestic supply security becomes more critical.

## Zinc:

- Chinese concentrate imports cooled in April though refined output stayed strong. China's zinc concentrate imports fell by nearly $10\%$ yoy in April, as a lack of concentrate availability is beginning to emerge with spot TCs in China flipping to negative territory since the end of March. Smelter production, on the other hand, remained robust increasing by $5\%$ yoy in April, as smelters work through concentrate inventory following strong imports in 1Q26. Even tighter concentrate markets could eventually weigh on Chinese output, which remains a risk for a tighter than expected refined balance this year.  
- Subdued demand continues to show via elevated and stagnant visible inventory. Total SHFE + social warehouse inventories in China have stabilized near 264 kmt as galvaniser operating rates remain subdued and construction activity remains lifeless in China (Figure 76). Galvaniser demand continues to remain below the 5-yr average, while apparent demand is down by 12% yoy as of April (Figure 78& Figure 86).

## Nickel:

\- Visible inventory builds stagnate. While inventory on SHFE continues to rise, LME stocks modestly declined from a peak in February, leading to net inventory growth of 70 kmt YTD to a total inventory level of \~470 kmt. Meanwhile, Indonesia's policy framework is set to weigh on producer margins amid higher ore benchmarks, potentially weighing on refined output somewhat this year, though the market remains focused on any upcoming additions to Indonesia's ore quota into the summer.

## China demand indicators:

- China's grid investment remains solid as renewables remain under pressure. Following a sharp jump at the start of the year, April grid spend rose by $9\%$ yoy, resulting in $>30\%$ growth yoy on a ytd basis (Figure 5). However, renewable installations continue to stumble, coming off the rapid pace of installations in 1H2025. Solar installations in April decelerated to $\sim 9.5\mathrm{GW}$ in April, decreasing by $79\%$ yoy, while wind installations declined by $7\%$ yoy to 5.4GW (Figure 7 & Figure 8).  
- NEV production in China rebounded in April. Total EV and PHEV production through April in China rose by 4% yoy while EV sales increased by 2.5% yoy in April. US EV sales continued to struggle while other regions such as Europe saw healthy EV sales. Overall, global passenger vehicle sales decreased by 10% yoy in April, with China and US taking the biggest hit (Figure 1).  
- White goods demand stumbled in April. Our estimate for total aggregate white goods copper demand in China decreased by 3% yoy in April, driven by a 9% decline in AC production.

## Global demand indicators

Table 1: Global metals monthly price change heatmap  
Percent change, MoM & YoY

<table><tr><td></td><td>Global Metals Price Heatmap</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>2023</td><td>2024</td><td>2025</td><td>2026 YTD</td></tr><tr><td rowspan="16">Metals Prices</td><td>LME Copper</td><td>4.1%</td><td>3.9%</td><td>-2.6%</td><td>3.0%</td><td>3.7%</td><td>6.0%</td><td>2.8%</td><td>11.0%</td><td>5.9%</td><td>1.4%</td><td>-9.3%</td><td>5.3%</td><td>5.0%</td><td>2.2%</td><td>2.4%</td><td>41.7%</td><td>10.5%</td></tr><tr><td>LME Aluminium</td><td>1.9%</td><td>6.3%</td><td>-1.3%</td><td>2.0%</td><td>2.5%</td><td>7.6%</td><td>-0.6%</td><td>4.4%</td><td>5.0%</td><td>-0.1%</td><td>3.8%</td><td>0.2%</td><td>5.5%</td><td>0.3%</td><td>7.0%</td><td>17.4%</td><td>21.7%</td></tr><tr><td>LME Zinc</td><td>1.1%</td><td>5.0%</td><td>0.3%</td><td>2.1%</td><td>5.0%</td><td>3.2%</td><td>0.0%</td><td>2.0%</td><td>9.1%</td><td>-2.5%</td><td>-8.3%</td><td>4.2%</td><td>5.3%</td><td>-10.6%</td><td>12.1%</td><td>4.7%</td><td>14.5%</td></tr><tr><td>LME Nickel</td><td>-1.2%</td><td>-0.1%</td><td>-1.8%</td><td>3.2%</td><td>-1.2%</td><td>-0.1%</td><td>-2.6%</td><td>12.3%</td><td>7.9%</td><td>-0.6%</td><td>-5.0%</td><td>13.8%</td><td>-2.1%</td><td>-44.7%</td><td>-7.7%</td><td>8.6%</td><td>11.3%</td></tr><tr><td>LME Lead</td><td>0.0%</td><td>4.4%</td><td>-3.6%</td><td>1.0%</td><td>-0.1%</td><td>1.4%</td><td>-1.8%</td><td>1.5%</td><td>-0.1%</td><td>-2.3%</td><td>-3.5%</td><td>2.8%</td><td>3.1%</td><td>-9.8%</td><td>-5.6%</td><td>3.0%</td><td>-0.1%</td></tr><tr><td>LME Tin</td><td>-3.0%</td><td>10.9%</td><td>-3.0%</td><td>7.1%</td><td>1.1%</td><td>1.9%</td><td>8.5%</td><td>3.6%</td><td>28.1%</td><td>11.1%</td><td>-23.4%</td><td>5.3%</td><td>12.6%</td><td>2.4%</td><td>14.4%</td><td>39.4%</td><td>33.4%</td></tr><tr><td>LME Cobalt spot</td><td>0.0%</td><td>-1.1%</td><td>0.0%</td><td>0.0%</td><td>5.1%</td><td>39.3%</td><td>0.0%</td><td>9.9%</td><td>5.5%</td><td>0.1%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>-44.3%</td><td>-15.4%</td><td>117.8%</td><td>5.6%</td></tr><tr><td>LME Lithium Hydroxide</td><td>-6.9%</td><td>-3.2%</td><td>-2.1%</td><td>5.4%</td><td>11.9%</td><td>1.0%</td><td>5.8%</td><td>10.1%</td><td>62.0%</td><td>-4.3%</td><td>12.5%</td><td>3.5%</td><td>7.8%</td><td>-80.4%</td><td>-42.9%</td><td>18.5%</td><td>83.4%</td></tr><tr><td>COMEX Copper</td><td>2.6%</td><td>7.5%</td><td>-13.4%</td><td>3.8%</td><td>7.5%</td><td>4.8%</td><td>1.9%</td><td>9.6%</td><td>4.3%</td><td>1.4%</td><td>-9.7%</td><td>5.6%</td><td>7.8%</td><td>2.1%</td><td>3.5%</td><td>41.1%</td><td>12.8%</td></tr><tr><td>SHFE Copper</td><td>0.5%</td><td>2.4%</td><td>-1.9%</td><td>1.0%</td><td>5.1%</td><td>4.8%</td><td>0.0%</td><td>13.1%</td><td>8.3%</td><td>-4.2%</td><td>-7.8%</td><td>5.8%</td><td>3.6%</td><td>4.4%</td><td>6.8%</td><td>33.7%</td><td>6.8%</td></tr><tr><td>SHFE Aluminium</td><td>0.6%</td><td>2.8%</td><td>-0.5%</td><td>0.6%</td><td>0.0%</td><td>2.5%</td><td>1.1%</td><td>5.6%</td><td>10.6%</td><td>-6.0%</td><td>0.1%</td><td>-1.3%</td><td>-0.5%</td><td>4.5%</td><td>1.0%</td><td>14.7%</td><td>6.8%</td></tr><tr><td>SHFE Zinc</td><td>-0.7%</td><td>-0.5%</td><td>-0.6%</td><td>-1.3%</td><td>-1.0%</td><td>2.0%</td><td>0.2%</td><td>4.1%</td><td>12.2%</td><td>-6.0%</td><td>-6.3%</td><td>0.4%</td><td>5.1%</td><td>-9.5%</td><td>19.0%</td><td>-9.4%</td><td>6.3%</td></tr><tr><td>Spot Gold</td><td>0.0%</td><td>0.4%</td><td>-0.4%</td><td>4.8%</td><td>11.9%</td><td>3.7%</td><td>5.9%</td><td>1.9%</td><td>13.3%</td><td>7.9%</td><td>-15.2%</td><td>-1.1%</td><td>-1.7%</td><td>13.1%</td><td>27.2%</td><td>64.6%</td><td>3.3%</td></tr><tr><td>Spot Silver</td><td>1.1%</td><td>9.5%</td><td>1.7%</td><td>8.2%</td><td>17.4%</td><td>4.4%</td><td>16.0%</td><td>26.8%</td><td>18.9%</td><td>10.1%</td><td>-24.1%</td><td>-1.9%</td><td>2.1%</td><td>-0.7%</td><td>21.5%</td><td>148.0%</td><td>1.1%</td></tr><tr><td>Spot Platinum</td><td>9.1%</td><td>28.5%</td><td>-5.0%</td><td>6.1%</td><td>14.9%</td><td>-0.1%</td><td>6.1%</td><td>23.3%</td><td>6.5%</td><td>7.9%</td><td>-18.5%</td><td>1.7%</td><td>-3.4%</td><td>-7.7%</td><td>-8.5%</td><td>127.0%</td><td>-8.7%</td></tr><tr><td>Spot Palladium</td><td>3.2%</td><td>13.6%</td><td>8.3%</td><td>-7.9%</td><td>14.3%</td><td>14.1%</td><td>1.1%</td><td>11.4%</td><td>5.7%</td><td>4.4%</td><td>-19.4%</td><td>3.6%</td><td>-11.2%</td><td>-38.6%</td><td>-17.1%</td><td>77.5%</td><td>-19.6%</td></tr></table>

\*LME is 3-month rolling forward, except cobalt which is spot. Lithium hydroxide and SHFE prices are futures contracts. Prices as of $5^{\text{th}}$ June 2026.  
Source: Bloomberg Finance L.P.

Table 2: Global manufacturing PMI by country

<table><tr><td></td><td></td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td rowspan="5">Groups</td><td>JPM Global</td><td>50.1</td><td>50.6</td><td>50.3</td><td>49.8</td><td>49.5</td><td>50.4</td><td>49.7</td><td>50.9</td><td>50.7</td><td>50.7</td><td>50.5</td><td>50.4</td><td>50.9</td><td>51.8</td><td>51.3</td><td>52.6</td></tr><tr><td>Developed Markets</td><td>49.3</td><td>50.0</td><td>49.1</td><td>49.1</td><td>50.0</td><td>50.5</td><td>49.2</td><td>50.9</td><td>50.3</td><td>50.3</td><td>50.5</td><td>50.5</td><td>51.4</td><td>51.8</td><td>52.0</td><td>53.8</td></tr><tr><td>Emerging Markets</td><td>50.8</td><td>51.1</td><td>51.3</td><td>50.5</td><td>49.2</td><td>50.4</td><td>50.1</td><td>50.9</td><td>51.2</td><td>51.2</td><td>50.5</td><td>50.4</td><td>50.6</td><td>52.0</td><td>50.7</td><td>51.6</td></tr><tr><td>European Union</td><td>46.7</td><td>47.8</td><td>48.6</td><td>49.1</td><td>49.2</td><td>49.2</td><td>49.6</td><td>50.4</td><td>49.7</td><td>49.7</td><td>49.5</td><td>48.8</td><td>49.5</td><td>50.5</td><td>51.3</td><td>52.0</td></tr><tr><td>Eurozone</td><td>46.6</td><td>47.6</td><td>48.6</td><td>49.0</td><td>49.4</td><td>49.5</td><td>49.8</td><td>50.7</td><td>49.8</td><td>49.8</td><td>49.6</td><td>48.8</td><td>49.5</td><td>50.8</td><td>51.6</td><td>52.2</td></tr><tr><td rowspan="4">Asia Pacific</td><td>China (Caixin/Markit)</td><td>50.1</td><td>50.8</td><td>51.2</td><td>50.4</td><td>48.3</td><td>50.4</td><td>49.5</td><td>50.5</td><td>51.2</td><td>51.2</td><td>49.9</td><td>50.1</td><td>50.3</td><td>52.1</td><td>50.8</td><td>52.2</td></tr><tr><td>China (Official PMI)</td><td>49.1</td><td>50.2</td><td>50.5</td><td>49.0</td><td>49.5</td><td>49.7</td><td>49.3</td><td>49.4</td><td>49.8</td><td>49.8</td><td>49.2</td><td>50.1</td><td>49.3</td><td>49.0</td><td>50.4</td><td>50.3</td></tr><tr><td>India</td><td>57.7</td><td>56.3</td><td>58.1</td><td>58.2</td><td>57.6</td><td>58.4</td><td>59.1</td><td>59.3</td><td>57.7</td><td>57.7</td><td>56.6</td><td>55.0</td><td>55.4</td><td>56.9</td><td>53.9</td><td>54.7</td></tr><tr><td>Japan</td><td>48.7</td><td>49.0</td><td>48.4</td><td>48.7</td><td>49.4</td><td>50.1</td><td>48.9</td><td>49.7</td><td>48.5</td><td>48.5</td><td>48.7</td><td>50.0</td><td>51.5</td><td>53.0</td><td>51.6</td><td>55.1</td></tr><tr><td rowspan="5">Europe</td><td>France</td><td>45.0</td><td>45.8</td><td>48.5</td><td>48.7</td><td>49.8</td><td>48.1</td><td>48.2</td><td>50.4</td><td>48.2</td><td>48.2</td><td>47.8</td><td>50.7</td><td>51.2</td><td>50.1</td><td>50.0</td><td>52.8</td></tr><tr><td>Germany</td><td>45.0</td><td>46.5</td><td>48.3</td><td>48.4</td><td>48.3</td><td>49.0</td><td>49.1</td><td>49.8</td><td>49.5</td><td>49.5</td><td>48.2</td><td>47.0</td><td>49.1</td><td>50.9</td><td>52.2</td><td>51.4</td></tr><tr><td>Italy</td><td>46.3</td><td>47.4</td><td>46.6</td><td>49.3</td><td>49.2</td><td>48.4</td><td>49.8</td><td>50.4</td><td>49.0</td><td>49.0</td><td>50.6</td><td>47.9</td><td>48.1</td><td>50.6</td><td>51.3</td><td>52.1</td></tr><tr><td>Spain</td><td>50.9</td><td>49.7</td><td>49.5</td><td>48.1</td><td>50.5</td><td>51.4</td><td>51.9</td><td>54.3</td><td>51.5</td><td>51.5</td><td>51.5</td><td>49.6</td><td>49.2</td><td>50.0</td><td>48.7</td><td>51.7</td></tr><tr><td>United Kingdom</td><td>48.3</td><td>46.9</td><td>44.9</td><td>45.4</td><td>46.4</td><td>47.7</td><td>48.0</td><td>47.0</td><td>46.2</td><td>46.2</td><td>50.2</td><td>50.6</td><td>51.8</td><td>51.7</td><td>51.0</td><td>53.7</td></tr><tr><td rowspan="4">Americas</td><td>Canada</td><td>51.6</td><td>47.8</td><td>46.3</td><td>45.3</td><td>46.1</td><td>45.6</td><td>46.1</td><td>48.3</td><td>47.7</td><td>47.7</td><td>48.4</td><td>48.6</td><td>50.4</td><td>51.0</td><td>50.0</td><td>53.3</td></tr><tr><td>Mexico</td><td>49.1</td><td>47.6</td><td>46.5</td><td>44.8</td><td>46.7</td><td>46.3</td><td>49.1</td><td>50.2</td><td>49.6</td><td>49.6</td><td>47.3</td><td>46.1</td><td>46.3</td><td>47.1</td><td>48.9</td><td>47.7</td></tr><tr><td>United States</td><td>51.2</td><td>52.7</td><td>50.2</td><td>50.2</td><td>52.0</td><td>52.9</td><td>49.8</td><td>53.0</td><td>52.0</td><td>52.0</td><td>52.2</td><td>51.8</td><td>52.4</td><td>51.6</td><td>52.3</td><td>54.5</td></tr><tr><td>US ISM</td><td>50.5</td><td>50.0</td><td>48.9</td><td>48.8</td><td>48.6</td><td>49.0</td><td>48.4</td><td>48.9</td><td>48.9</td><td>48.9</td><td>48.0</td><td>47.9</td><td>52.6</td><td>52.4</td><td>52.7</td><td>52.7</td></tr></table>

Source: Bloomberg Finance L.P.

Table 3: Global light vehicle production growth  
Percent change

<table><tr><td>QoQ</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td><td>2024</td><td>2025</td><td>2026E</td><td>2027F</td></tr><tr><td>Europe</td><td>0.5%</td><td>2.4%</td><td>-13.4%</td><td>12.0%</td><td>0.8%</td><td>-1.6%</td><td>-11.9%</td><td>11.0%</td><td>0.0%</td><td>4.2%</td><td>-12.6%</td><td>11%</td><td></td><td></td><td></td><td></td></tr><tr><td>China</td><td>-24.5%</td><td>8.0%</td><td>7.8%</td><td>17.1%</td><td>-32.1%</td><td>13.9%</td><td>10.4%</td><td>14.6%</td><td>-26.4%</td><td>16.8%</td><td>-8.6%</td><td>26%</td><td></td><td></td><td></td><td></td></tr><tr><td>Japan/Korea</td><td>-5.4%</td><td>-0.4%</td><td>-3.3%</td><td>6.0%</td><td>0.0%</td><td>-4.1%</td><td>-6.4%</td><td>2.0%</td><td>-0.5%</td><td>1.0%</td><td>-3.5%</td><td>6%</td><td></td><td></td><td></td><td></td></tr><tr><td>North America</td><td>4.2%</td><td>5.0%</td><td>0.3%</td><td>-9.9%</td><td>4.1%</td><td>4.0%</td><td>0.0%</td><td>-9.9%</td><td>4.0%</td><td>6.1%</td><td>-2.2%</td><td>-1%</td><td></td><td></td><td></td><td></td></tr><tr><td>Other</td><td>4.4%</td><td>-4.9%</td><td>6.9%</td><td>1.1%</td><td>0.1%</td><td>-7.2%</td><td>4.6%</td><td>-3.4%</td><td>2.4%</td><td>4.6%</td><td>5.4%</td><td>-2%</td><td></td><td></td><td></td><td></td></tr><tr><td>Global</td><td>-8.9%</td><td>3.0%</td><td>0.8%</td><td>7.4%</td><td>-11.9%</td><td>2.7%</td><td>1.2%</td><td>5.2%</td><td>-9.7%</td><td>8.3%</td><td>-5.3%</td><td>11%</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="17">YoY</td></tr><tr><td>Europe</td><td>-5.3%</td><td>-0.3%</td><td>3.8%</td><td>-0.2%</td><td>0.2%</td><td>-3.8%</td><td>-2.0%</td><td>-2.9%</td><td>-3.7%</td><td>2.0%</td><td>1.1%</td><td>0.9%</td><td>-4.4%</td><td>-0.7%</td><td>-2.1%</td><td>0.0%</td></tr><tr><td>China</td><td>14.5%</td><td>11.0%</td><td>14.6%</td><td>2.8%</td><td>-7.5%</td><td>-2.4%</td><td>-0.1%</td><td>-2.2%</td><td>6.1%</td><td>8.8%</td><td>-10.0%</td><td>-0.7%</td><td>3.6%</td><td>10.0%</td><td>-2.9%</td><td>0.5%</td></tr><tr><td>Japan/Korea</td><td>7.0%</td><td>0.3%</td><td>0.8%</td><td>-3.5%</td><td>2.1%</td><td>-1.7%</td><td>-4.8%</td><td>-8.4%</td><td>-8.9%</td><td>-4.1%</td><td>-1.2%</td><td>2.7%</td><td>-6.4%</td><td>1.0%</td><td>-3.2%</td><td>-3.0%</td></tr><tr><td>North America</td><td>-5.0%

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 08 Jun 2026 04:46 PM BST

Disseminated 08 Jun 2026 04:46 PM BST
"""
