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
## Taiwan ODMs

In-line May sales with initial ramp of Amazon T3 servers

Most Taiwan ODMs reported largely in-line revenue in May with sustained server momentum and flattish NB shipment trends. General server demand remains resilient with likely double-digit QoQ shipment growth in 2Q26. For AI servers, we expect double-digit NVL72 rack shipment growth in 2Q26. We also saw resumed component momentum for AWS ASIC in May, implying an uptick in Trianium 3 system shipments in the coming months. For PCs, 2Q26 NB ODM outlook appears to be largely flattish QoQ. We expect a declining trend into 2H26, dragged by price elasticity impact. VGA/MB shipments appear to be down double digit % QoQ/YoY in 2Q26 and likely to see continued weakness into 2H26, due to a lack of new product and end demand weakness. iPhone EMS revenues were resilient in May driven by m/s gains and inventory preparation ahead of the China 618 sales season, but we are cautious on the 2H26 iPhone demand on the potential memory-led price elasticity impact. In the server ODM space, we prefer Wiwynn > Quanta > Hon Hai > Wistron. We stay OW on Delta given the growing AI datacenter power/thermal TAM and potential product price hikes. ASPEED and Lotes are key beneficiaries of general server strength. In the PC space, our top avoids are Micro-Star and ASUSTek.

- AI servers: Continued GB300 ramp, AWS ASIC to pick up in June. We saw continued GB300 shipment ramp in May and forecast double-digit NVL72 shipment growth in 2Q26. We see potential air pockets into 3Q26 due to product transition and anticipate VR200 system ramp in 4Q26. Overall, we estimate 65-70k NVL72 rack shipments this year. For ASIC servers, we saw component pull-in demand (e.g. server slide, power supply, chassis, CCL/PCB) for the Trainium 3 project in May and expect an initial system ramp in June, which bodes well for Wiwiynn.  
- General servers: Robust general server momentum. We saw continued general server shipment growth in May. Server shipments appear to have grown double-digits QoQ in 2Q26, which is in line with our expectations and Lotes's 2Q26 server ODM forecast (+15% QoQ). Supply chain feedback suggests accelerating momentum into 2H26 with better CPU supply. Overall, we forecast traditional server shipments to grow 20% YoY this year (vs. 30-40% demand growth due to supply constraints) and to see sustained momentum into next year due to order backlogs.  
- PCs: Demand weakness and margin pressure in coming quarters: Aggregated NB ODM shipments were up slightly MoM in May. April-May aggregated shipments were largely in line with our estimate of flattish to slightly up QoQ for 2Q26. Initial NB ODM feedback indicates a sub-seasonal 2H26 outlook (1H/2H split at \~55%/45%) and double-digit shipment decline, which echoes our cautious view from price elasticity impact. This, coupled with emerging margin pressure for PC brands in the next few quarters, could drive potential earnings downside and valuation de-rating of PC stocks, in our view.

## Technology - Hardware

## Albert Hung AC

(886-2) 2725-9875

albert.hung@jpmchase.com

JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Anthony Leng

(886-2) 2725-9240

anthony.leng@JPM.com

JPM Securities (Taiwan) Limited

## Gokul Hariharan

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

- VGA/motherboard: Double-digit shipment declines on end demand weakness. Micro-Star's MB/VGA shipments appear to have declined double digits QoQ/YoY in 2Q26 due to end demand weakness. ASUSTek and MSI have seen weaker-than-expected PC component demand, likely due to memory-led negative price elasticity. Looking ahead, we expect continued weakness into 2H26 due to the lack of new products and lackluster end demand. Overall, we forecast double-digit declines for MB/VGA shipments this year. This is negative for Micro-Star and ASUSTek, which have $40 - 50\% / 20\%$ revenue exposure from PC components, respectively.  
- Robust 1H26 iPhone demand, followed by sub-seasonal iPhone EMS build outlook in 2H. Hon Hai/Pegatron iPhone revenues were up double digits/ flattish MoM in May respectively, which were above-seasonal trends, likely driven by some m/s gains and pull-in demand ahead of the China 618 sales season. Our iPhone supply chain analyst, William Yang, expects a 7% YoY decline for 2H26 iPhone EMS build (vs. +9% YoY in 1H26) due to fewer new model launches and potential demand weakness.  
- 800V HVDC datacenter power on track to ramp late 2026/early 2027 with small volumes. We have previously highlighted the earlier-than-expected production introduction of HVDC (800v and +/- 400v) vs. our earlier expectation of a 2H27 launch. Our industry research suggests that key power system integrators are on track to introduce HVDC (800V and ±400V) in 4Q26/1Q27. HVDC is not required for VR200 racks, so we anticipate only 10–20% penetration in the VR200 cycle (still an incremental positive vs. our prior assumptions). Early deployments should skew toward ±400V given data center readiness, but we still expect meaningful power content uplift driven by sidecar power rack adoption.

Table 1: May sales summary

<table><tr><td>NT$ bn</td><td>May&#x27;26 sales</td><td>MoM (%)</td><td>YoY (%)</td><td>JPMe 2Q26</td><td>Apr-May aggregate sales as % of JPMe</td><td>Consensus 2Q26</td><td>Apr-May aggregate sales as % of Consensus</td></tr><tr><td colspan="8">PC brands</td></tr><tr><td>Asus</td><td>62.7</td><td>-19%</td><td>7%</td><td>236.0</td><td>59%</td><td>241.3</td><td>58%</td></tr><tr><td>Acer</td><td>26.2</td><td>-16%</td><td>37%</td><td>N.A.</td><td>N.A.</td><td>78.5</td><td>73%</td></tr><tr><td>MSI</td><td>15.8</td><td>-3%</td><td>-24%</td><td>55.9</td><td>57%</td><td>52.9</td><td>61%</td></tr><tr><td>Gigabyte</td><td>49.1</td><td>-6%</td><td>5%</td><td>N.A.</td><td>N.A.</td><td>131.9</td><td>77%</td></tr><tr><td colspan="8">Notebook ODMs</td></tr><tr><td>Wistron</td><td>290.2</td><td>2%</td><td>39%</td><td>860.5</td><td>67%</td><td>857.0</td><td>67%</td></tr><tr><td>Compal</td><td>70.5</td><td>-2%</td><td>22%</td><td>220.3</td><td>65%</td><td>216.5</td><td>66%</td></tr><tr><td>Inventec</td><td>82.8</td><td>-2%</td><td>35%</td><td>240.0</td><td>70%</td><td>213.7</td><td>78%</td></tr><tr><td>Quanta</td><td>311.5</td><td>-8%</td><td>94%</td><td>992.2</td><td>66%</td><td>950.5</td><td>69%</td></tr><tr><td colspan="8">iPhone EMS</td></tr><tr><td>Hon Hai</td><td>859.4</td><td>3%</td><td>40%</td><td>2,346.2</td><td>72%</td><td>2,366.0</td><td>71%</td></tr><tr><td>Pegatron</td><td>96.0</td><td>10%</td><td>12%</td><td>278.2</td><td>66%</td><td>276.2</td><td>66%</td></tr><tr><td colspan="8">Server</td></tr><tr><td>Wiwynn</td><td>84.1</td><td>2%</td><td>18%</td><td>271.8</td><td>61%</td><td>276.8</td><td>60%</td></tr><tr><td>ASPEED</td><td>1.3</td><td>0%</td><td>69%</td><td>3.8</td><td>67%</td><td>3.7</td><td>70%</td></tr><tr><td colspan="8">Components</td></tr><tr><td>Delta</td><td>59.0</td><td>0%</td><td>44%</td><td>188.7</td><td>62%</td><td>185.5</td><td>63%</td></tr><tr><td>Lotes</td><td>3.0</td><td>-10%</td><td>9%</td><td>10.2</td><td>63%</td><td>10.1</td><td>64%</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates.

Table 2: NVL72 rack shipment estimates

<table><tr><td>NVL72 (unit)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>Jan</td><td>Feb</td><td>Mar</td><td>1Q26</td><td>Apr</td><td>May</td><td>Jun</td><td>2Q26</td><td>2025</td><td>2026</td></tr><tr><td>Hon Hai</td><td>400</td><td>1,500</td><td>4,200</td><td>5,800</td><td>2,000</td><td>1,900</td><td>2,626</td><td>6,526</td><td>2,259</td><td>2,446</td><td>2,549</td><td>7,253</td><td>11,900</td><td>31,596</td></tr><tr><td>Quanta</td><td>150</td><td>1,400</td><td>1,600</td><td>3,300</td><td>1,300</td><td>1,300</td><td>1,800</td><td>4,400</td><td>1,750</td><td>1,550</td><td>1,900</td><td>5,200</td><td>6,450</td><td>19,400</td></tr><tr><td>Wistron</td><td>150</td><td>1,800</td><td>1,350</td><td>2,500</td><td>950</td><td>1,550</td><td>1,379</td><td>3,879</td><td>1,350</td><td>1,350</td><td>1,400</td><td>4,100</td><td>5,800</td><td>14,779</td></tr><tr><td>Others</td><td>200</td><td>300</td><td>850</td><td>1,700</td><td></td><td></td><td></td><td>2,195</td><td></td><td></td><td></td><td>2,447</td><td>3,050</td><td></td></tr><tr><td>Total</td><td>900</td><td>5,000</td><td>8,000</td><td>13,300</td><td></td><td></td><td></td><td>17,000</td><td></td><td></td><td></td><td>19,000</td><td>27,200</td><td>70,000</td></tr></table>

Source: JPM estimates, Company data.

Table 3: Taiwan ODM 2Q26 NB guidance

<table><tr><td>Companies</td><td>Ticker</td><td>2Q26 guidance - new</td><td>2Q26 guidance - old</td></tr><tr><td>Wistron</td><td>3231 TT</td><td>5-10% QoQ decline</td><td>5-10% QoQ decline</td></tr><tr><td>Compal</td><td>2324 TT</td><td>Single digit QoQ growth</td><td>Single digit QoQ growth</td></tr><tr><td>Inventec</td><td>2356 TT</td><td>Flattish QoQ</td><td>Flattish QoQ</td></tr><tr><td>Quanta</td><td>2382 TT</td><td>Slight QoQ growth</td><td>Flattish to slight QoQ growth</td></tr><tr><td>Pegatron</td><td>4938 TT</td><td>Below seasonality</td><td>Below seasonality</td></tr></table>

Source: Company data.

Table 4: Quarterly notebook shipments by ODM

<table><tr><td>Qrtly shipments</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td></tr><tr><td>Wistron (3231 TT)</td><td>4,600</td><td>5,100</td><td>5,200</td><td>5,300</td><td>4,900</td><td>5,900</td><td>6,400</td><td>6,900</td><td>6,100</td><td>5,612</td></tr><tr><td>Compal (2324 TT)</td><td>7,500</td><td>8,700</td><td>8,300</td><td>7,800</td><td>7,000</td><td>7,100</td><td>7,100</td><td>6,830</td><td>5,900</td><td>6,195</td></tr><tr><td>Inventec (2356 TT)</td><td>4,500</td><td>4,900</td><td>5,200</td><td>5,400</td><td>5,000</td><td>5,600</td><td>5,400</td><td>5,300</td><td>5,400</td><td>5,400</td></tr><tr><td>Quanta (2382 TT)</td><td>10,500</td><td>11,700</td><td>12,600</td><td>11,100</td><td>10,800</td><td>12,100</td><td>12,700</td><td>10,900</td><td>10,000</td><td>10,428</td></tr><tr><td>Pegatron (4938 TT)</td><td>1,585</td><td>2,040</td><td>2,500</td><td>1,950</td><td>1,885</td><td>2,375</td><td>2,400</td><td>2,410</td><td>1,800</td><td>1,800</td></tr><tr><td>Total (K units)</td><td>28,685</td><td>32,440</td><td>33,800</td><td>31,550</td><td>29,585</td><td>33,075</td><td>34,000</td><td>32,340</td><td>29,200</td><td>29,435</td></tr><tr><td colspan="11"></td></tr><tr><td>QoQ Growth</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td></tr><tr><td>Wistron (3231 TT)</td><td>-13%</td><td>11%</td><td>2%</td><td>2%</td><td>-8%</td><td>20%</td><td>8%</td><td>8%</td><td>-12%</td><td>-8%</td></tr><tr><td>Compal (2324 TT)</td><td>-10%</td><td>16%</td><td>-5%</td><td>-6%</td><td>-10%</td><td>1%</td><td>0%</td><td>-4%</td><td>-14%</td><td>5%</td></tr><tr><td>Inventec (2356 TT)</td><td>0%</td><td>9%</td><td>6%</td><td>4%</td><td>-7%</td><td>12%</td><td>-4%</td><td>-2%</td><td>2%</td><td>0%</td></tr><tr><td>Quanta (2382 TT)</td><td>1%</td><td>11%</td><td>8%</td><td>-12%</td><td>-3%</td><td>12%</td><td>5%</td><td>-14%</td><td>-8%</td><td>4%</td></tr><tr><td>Pegatron (4938 TT)</td><td>-4%</td><td>29%</td><td>23%</td><td>-22%</td><td>-3%</td><td>26%</td><td>1%</td><td>0%</td><td>-25%</td><td>0%</td></tr><tr><td>Total (m units)</td><td>-5%</td><td>13%</td><td>4%</td><td>-7%</td><td>-6%</td><td>12%</td><td>3%</td><td>-5%</td><td>-10%</td><td>1%</td></tr><tr><td colspan="11"></td></tr><tr><td>Y/Y Growth</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td></tr><tr><td>Wistron (3231 TT)</td><td>18%</td><td>11%</td><td>0%</td><td>0%</td><td>7%</td><td>16%</td><td>23%</td><td>30%</td><td>24%</td><td>-5%</td></tr><tr><td>Compal (2324 TT)</td><td>-1%</td><td>0%</td><td>-11%</td><td>-6%</td><td>-7%</td><td>-18%</td><td>-14%</td><td>-12%</td><td>-16%</td><td>-13%</td></tr><tr><td>Inventec (2356 TT)</td><td>2%</td><td>0%</td><td>6%</td><td>20%</td><td>11%</td><td>14%</td><td>4%</td><td>-2%</td><td>8%</td><td>-4%</td></tr><tr><td>Quanta (2382 TT)</td><td>-3%</td><td>-7%</td><td>-4%</td><td>7%</td><td>3%</td><td>3%</td><td>1%</td><td>-2%</td><td>-7%</td><td>-14%</td></tr><tr><td>Pegatron (4938 TT)</td><td>-7%</td><td>-2%</td><td>0%</td><td>18%</td><td>19%</td><td>16%</td><td>-4%</td><td>24%</td><td>-5%</td><td>-24%</td></tr><tr><td>Total (m units)</td><td>1%</td><td>-1%</td><td>-3%</td><td>5%</td><td>3%</td><td>2%</td><td>1%</td><td>3%</td><td>-1%</td><td>-11%</td></tr></table>

Source: Company data, JPM estimates.

Figure 1: Aggregated top 3 MB vendors' quarterly shipments and qoq trend  
![](images/eab412d12435ce2b0c4dc5c942d531ff215ec0cbdb13fdc45e01467f9b6e752b.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Aggregated Top 3 motherboard vendor shipment (K unit) | qoq % (%) |
|---|---|---|
| 1Q19 | 8,500 | 1 |
| 2Q19 | 9,000 | 0 |
| 3Q19 | 14,500 | 20 |
| 4Q19 | 8,000 | -6 |
| 1Q20 | 12,500 | 3 |
| 2Q20 | 13,500 | 16 |
| 3Q20 | 12,800 | 16 |
| 4Q20 | 12,500 | -3 |
| 1Q21 | 12,800 | -2 |
| 2Q21 | 12,500 | -9 |
| 3Q21 | 12,800 | -1 |
| 4Q21 | 12,500 | 10 |
| 1Q22 | 11,500 | -10 |
| 2Q22 | 9,500 | -16 |
| 3Q22 | 10,500 | 11 |
| 4Q22 | 9,500 | 4 |
| 1Q23 | 11,500 | -5 |
| 2Q23 | 10,500 | 7 |
| 3Q23 | 11,500 | 0 |
| 4Q23 | 11,500 | -3 |
| 1Q24 | 11,500 | -2 |
| 2Q24 | 11,500 | 5 |
| 3Q24 | 11,500 | 1 |
| 4Q24 | 11,500 | 1 |
| 1Q25 | 12,500 | 14 |
| 2Q25 | 13,500 | 6 |
| 3Q25 | 12,800 | -5 |
| 4Q25 | 12,500 | -8 |
| 1Q26 | 11,500 | -11 |
</details>

Source: Company data, JPM estimates.

Figure 3: Aggregated top 3 MB vendors' quarterly shipments and yoy trend  
![](images/4c51cceee1a5be83e473f058885a0ba475201011ecc8e5f2ff53f4549efe8b1d.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Quarter | Aggregated Top 3 motherboard vendor shipment (K unit) | yoy (%) |
|---|---|---|
| 1Q19 | 9000 | -9 |
| 2Q19 | 9500 | 6 |
| 3Q19 | 10500 | 11 |
| 4Q19 | 11000 | 13 |
| 1Q20 | 12000 | 16 |
| 2Q20 | 13000 | 34 |
| 3Q20 | 12500 | 30 |
| 4Q20 | 13500 | 35 |
| 1Q21 | 12800 | 27 |
| 2Q21 | 12000 | 0 |
| 3Q21 | 13000 | -15 |
| 4Q21 | 12500 | -4 |
| 1Q22 | 11500 | -12 |
| 2Q22 | 9500 | -19 |
| 3Q22 | 10500 | -9 |
| 4Q22 | 11000 | -14 |
| 1Q23 | 11500 | -9 |
| 2Q23 | 10800 | 10 |
| 3Q23 | 11500 | 6 |
| 4Q23 | 11800 | 2 |
| 1Q24 | 11500 | 4 |
| 2Q24 | 11800 | 1 |
| 3Q24 | 12000 | -1 |
| 4Q24 | 12500 | 0 |
| 1Q25 | 13500 | 5 |
| 2Q25 | 14500 | 22 |
| 3Q25 | 13800 | 23 |
| 4Q25 | 13500 | 17 |
| 1Q26 | 11500 | -6 |
| 2Q26 | 11000 | -17 |
</details>

Source: Company data. JPM estimates.

Figure 2: Aggregated top 3 VGA card vendors' quarterly shipments and qoq trend  
![](images/e2fec9a126de00befc3a7c95085a89c9b30f82b5f7ecfd654679442ff152a0db.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Aggregated Top 3 VGA card vendor shipment (K unit) | qoq (%) |
|---|---|---|
| 1Q19 | 3500 | -5 |
| 2Q19 | 3000 | -12 |
| 3Q19 | 4000 | 30 |
| 4Q19 | 4000 | -1 |
| 1Q20 | 4500 | 9 |
| 2Q20 | 5000 | 14 |
| 3Q20 | 5000 | 4 |
| 4Q20 | 5000 | -2 |
| 1Q21 | 5000 | 1 |
| 2Q21 | 5000 | 1 |
| 3Q21 | 5000 | -11 |
| 4Q21 | 5000 | 6 |
| 1Q22 | 5000 | -13 |
| 2Q22 | 4500 | -1 |
| 3Q22 | 4000 | 2 |
| 4Q22 | 4000 | -17 |
| 1Q23 | 3500 | 22 |
| 2Q23 | 3500 | -3 |
| 3Q23 | 4500 | -2 |
| 4Q23 | 4500 | -4 |
| 1Q24 | 4500 | 8 |
| 2Q24 | 4500 | -3 |
| 3Q24 | 4500 | 0 |
| 4Q24 | 4500 | -3 |
| 1Q25 | 5500 | 22 |
| 2Q25 | 5500 | -6 |
| 3Q25 | 5500 | -2 |
| 4Q25 | 5500 | -8 |
| 1Q26 | 4500 | -9 |
</details>

Source: Company data, JPM estimates.

Figure 4: Aggregated top 3 VGA card vendors' quarterly shipments and yoy trend  
![](images/df72394784180f72231cb5dbbf6924acd2188500b1ab03230edb93860c1d9dbb.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | Aggregated Top 3 VGA card vendor shipment (K unit) | yoy (%) |
|---|---|---|
| 1Q19 | 3400 | -33 |
| 2Q19 | 3000 | -20 |
| 3Q19 | 3800 | 16 |
| 4Q19 | 3500 | 8 |
| 1Q20 | 4200 | 12 |
| 2Q20 | 4500 | 39 |
| 3Q20 | 4800 | 22 |
| 4Q20 | 5000 | 29 |
| 1Q21 | 5100 | 27 |
| 2Q21 | 4900 | 15 |
| 3Q21 | 4800 | -1 |
| 4Q21 | 4900 | -5 |
| 1Q22 | 5200 | 3 |
| 2Q22 | 4500 | -7 |
| 3Q22 | 3900 | -18 |
| 4Q22 | 3800 | -18 |
| 1Q23 | 3900 | -2 |
| 2Q23 | 3800 | -27 |
| 3Q23 | 3300 | 3 |
| 4Q23 | 3600 | 7 |
| 1Q24 | 3800 | 6 |
| 2Q24 | 4100 | 23 |
| 3Q24 | 4300 | 9 |
| 4Q24 | 4500 | 3 |
| 1Q25 | 4700 | -2 |
| 2Q25 | 5100 | 29 |
| 3Q25 | 5300 | 20 |
| 4Q25 | 5000 | 20 |
| 1Q26 | 4800 | 10 |
| 2Q26 | 4300 | -18 |
</details>

Source: Company data. JPM estimates.

Companies Discussed in This Report (all prices in this report as of market close on 10 June 2026, unless otherwise indicated) ASPEED Technology Inc.(5274.TWO/NT\$16,840.00/OW), ASUSTek Computer(2357.TW/NT\$796.00/UW), Delta Electronics, Inc.(2308.TW/NT\$2,200.00/OW), Hon Hai Precision(2317.TW/NT\$263.00/OW), Lotes(3533.TW/NT\$2,175.00/OW), Micro-Star International Co., Ltd.(2377.TW/NT\$132.00/N), Quanta Computer Inc.(2382.TW/NT\$380.50/OW), Wistron Corporation(3231.TW/NT\$158.00/N), Wiwynn Corp(6669.TW/NT\$5,065.00/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report o

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 10 Jun 2026 10:51 PM HKT

Disseminated 10 Jun 2026 10:51 PM HKT
"""
