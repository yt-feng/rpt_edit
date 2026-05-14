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
# Semiconductors - Asia-Pacific

# Semiconductor IP & distributor: raise PO and reiterate Buy on eMemory & WT Micro

Price Objective Change

# Flagging several positives learnt from 1Q26 earnings calls

Thanks to the benefits from node migration, sustained growth in AI-related products/solutions, and some green shoots in non-AI areas, as shared in the 1Q26 earnings calls, we lift our 2027-28E net income estimates for eMemory and WT Micro by 3-4% and 7-15% respectively. The estimate changes drive an increase in our PO for eMemory to NT\$5,500 (from NT\$4,950) based on DCF valuation (unchanged), and our PO for WT Micro to NT\$320 (from NT\$270) based on 11x 2027E P/E (unchanged). We reiterate our Buy rating on both names in view of their rising exposure to AI/datacenter-related businesses.

# eMemory: stronger growth profile on node migration

During the 1Q26 earnings call, eMemory's management cited sustained licensing activities in 3nm for AI (artificial intelligence) server-related projects, including controller chips, as well as extension toward high-speed interface solutions. Looking ahead, the company expects its licensing business to be boosted by increasing number of license projects from both foundry and fabless customers, while the growth in royalty revenue to continue to accelerate. Specifically, for 2026, we flag benefits from process node migration from the likes of OLED (organic light emitting diode) DDIC (display driver integrated circuit) to 16nm, and PMIC (power management integrated circuit) to 55nm from 8"-based process. In view of eMemory's solid position in eNVM (embedded non-volatile memory) IP (intellectual property) with content increase along with node advancement and penetration increase by PUF (physically unclonable function) solutions, we reiterate our Buy rating.

# WT Micro: continuous boost by datacenter business

WT Micro's 2Q26 revenue growth should still be mainly driven by datacenter and communication businesses (which are more relevant to AI servers), in our view. At the same time, we see some green shoots from non-AI-related businesses, thanks to Future Electronics' ongoing recovery. Specifically for AI-related businesses, we flag benefits from significantly higher ROWC (return on working capital) for the company, despite a softer GM (gross margin) profile. Eyeing on a ‘stronger for longer’ growth in datacenter business via Broadcom's TPU (tensor processing unit), we reiterate our Buy rating on WT Micro.

# 12 May 2026

Equity

Asia-Pacific

Semiconductors

Mike Yang >>

Research Analyst

BofA (Taiwan)

+886 2 2376 3729

mike.c.yang@bofa.com

Haas Liu >>

Research Analyst

BofA (Taiwan)

+886 2 2376 3727

haas.liu@bofa.com

Cathy Hsu >>

Research Analyst

BofA (Taiwan)

+886 2 2376 3726

cathy.hsu3@bofa.com

Exhibit 1: Summary of PO changes   
We raise our POs for eMemory and WT Micro in this report 

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td colspan="2">PO (NT$)</td></tr><tr><td>New</td><td>Old</td></tr><tr><td>eMemory</td><td>3529 TT</td><td>5500</td><td>4950</td></tr><tr><td>WT Micro</td><td>3036 TT</td><td>320</td><td>270</td></tr></table>

Source: BofA Global Research   
BofA GLOBAL RESEARCH

This research report provides general information only. No part of this report may be used or reproduced or quoted in any manner whatsoever in Taiwan by the press or other persons without the express written consent of BofA.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 7 to 10. Analyst Certification on page 5. Price Objective Basis/Risk on page 4.

Exhibit 2: Summary of changes in PO and valuation method

We raise our POs for eMemory and WT Micro with unchanged valuation method

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td colspan="2">PO (NT$)</td><td colspan="2">Valuation method</td></tr><tr><td>New</td><td>Old</td><td>New</td><td>Old</td></tr><tr><td>eMemory</td><td>3529 TT</td><td>5500</td><td>4950</td><td colspan="2">DCF (unchanged)</td></tr><tr><td>WT Micro</td><td>3036 TT</td><td>320</td><td>270</td><td colspan="2">11x 2027E P/E (unchanged)</td></tr></table>

Source: BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 3: Table of recommendations

Stocks mentioned with ratings in this report

<table><tr><td>BofA ticker</td><td>Ticker</td><td>Company name</td><td>Price (LC)</td><td>Rating</td></tr><tr><td>XYLWF</td><td>3529 TT</td><td>eMemory</td><td>NT$ 4115</td><td>C-1-7</td></tr><tr><td>XZOPF</td><td>3036 TT</td><td>WT Micro</td><td>NT$ 275.5</td><td>B-1-7</td></tr></table>

Source: BofA Global Research, company data   
BofA GLOBAL RESEARCH

Exhibit 4: Earnings estimate changes – eMemory

We raise 2027/28E EPS by 4%/5% after baking in the assumption of stronger revenue growth

<table><tr><td rowspan="2">NT$mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td></tr><tr><td>Revenue</td><td>5,274</td><td>5,306</td><td>-1%</td><td>6,722</td><td>6,531</td><td>3%</td><td>8,146</td><td>7,861</td><td>4%</td></tr><tr><td>Gross profit</td><td>5,274</td><td>5,306</td><td>-1%</td><td>6,722</td><td>6,531</td><td>3%</td><td>8,146</td><td>7,861</td><td>4%</td></tr><tr><td>Gross margin</td><td>100.0%</td><td>100.0%</td><td>0.0ppt</td><td>100.0%</td><td>100.0%</td><td>0.0ppt</td><td>100.0%</td><td>100.0%</td><td>0.0ppt</td></tr><tr><td>Opt income</td><td>3,486</td><td>3,552</td><td>-2%</td><td>4,729</td><td>4,697</td><td>1%</td><td>5,964</td><td>5,856</td><td>2%</td></tr><tr><td>OPM</td><td>66.1%</td><td>67.0%</td><td>-0.9ppt</td><td>70.4%</td><td>71.9%</td><td>-1.6ppt</td><td>73.2%</td><td>74.5%</td><td>-1.3ppt</td></tr><tr><td>Pretax income</td><td>3,598</td><td>3,657</td><td>-2%</td><td>4,924</td><td>4,811</td><td>2%</td><td>6,166</td><td>5,979</td><td>3%</td></tr><tr><td>Pretax margin</td><td>68.2%</td><td>68.9%</td><td>-0.7ppt</td><td>73.2%</td><td>73.7%</td><td>-0.4ppt</td><td>75.7%</td><td>76.1%</td><td>-0.4ppt</td></tr><tr><td>Net income</td><td>3,069</td><td>3,098</td><td>-1%</td><td>4,194</td><td>4,068</td><td>3%</td><td>5,245</td><td>5,056</td><td>4%</td></tr><tr><td>EPS (NT$)</td><td>41.1</td><td>41.1</td><td>0%</td><td>56.2</td><td>54.0</td><td>4%</td><td>70.2</td><td>67.1</td><td>5%</td></tr></table>

Source: BofA Global Research estimates   
BofA GLOBAL RESEARCH

Exhibit 5: BofAe vs consensus – eMemory

We are 12%/3% ahead of consensus for 2026/27E EPS, due partly to the assumption of stronger operating leverage

<table><tr><td rowspan="2">NT$mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>BofA</td><td>Consensus</td><td>Diff</td><td>BofA</td><td>Consensus</td><td>Diff</td></tr><tr><td>Revenue</td><td>5,274</td><td>4,944</td><td>7%</td><td>6,722</td><td>6,703</td><td>0%</td></tr><tr><td>Gross profit</td><td>5,274</td><td>4,944</td><td>7%</td><td>6,722</td><td>6,703</td><td>0%</td></tr><tr><td>GPM</td><td>100.0%</td><td>100.0%</td><td>0.0ppt</td><td>100.0%</td><td>100.0%</td><td>0.0ppt</td></tr><tr><td>Opt income</td><td>3,486</td><td>3,214</td><td>8%</td><td>4,729</td><td>4,681</td><td>1%</td></tr><tr><td>OPM</td><td>66.1%</td><td>65.0%</td><td>1.1ppt</td><td>70.4%</td><td>69.8%</td><td>0.5ppt</td></tr><tr><td>Pretax income</td><td>3,598</td><td>3,309</td><td>9%</td><td>4,924</td><td>4,806</td><td>2%</td></tr><tr><td>Pretax margin</td><td>68.2%</td><td>66.9%</td><td>1.3ppt</td><td>73.2%</td><td>71.7%</td><td>1.5ppt</td></tr><tr><td>Net income</td><td>3,069</td><td>2,745</td><td>12%</td><td>4,194</td><td>4,062</td><td>3%</td></tr><tr><td>EPS (NT$)</td><td>41.1</td><td>36.8</td><td>12%</td><td>56.2</td><td>54.4</td><td>3%</td></tr></table>

Source: BofA Global Research estimates, Bloomberg   
BofA GLOBAL RESEARCH

Exhibit 6: Income statement - eMemory

We expect the company's revenue growth to sustain at $20 + \%$ level during 2026-28E

<table><tr><td>NT$mn; %</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>1,094</td><td>1,020</td><td>1,384</td><td>1,777</td><td>1,663</td><td>1,367</td><td>1,697</td><td>1,996</td><td>3,849</td><td>5,274</td><td>6,722</td><td>8,146</td></tr><tr><td>Cost of Revenue</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Gross profit</td><td>1,094</td><td>1,020</td><td>1,384</td><td>1,777</td><td>1,663</td><td>1,367</td><td>1,697</td><td>1,996</td><td>3,849</td><td>5,274</td><td>6,722</td><td>8,146</td></tr><tr><td>Operating exp</td><td>(432)</td><td>(413)</td><td>(451)</td><td>(492)</td><td>(491)</td><td>(471)</td><td>(500)</td><td>(531)</td><td>(1,597)</td><td>(1,788)</td><td>(1,993)</td><td>(2,182)</td></tr><tr><td>Operating income</td><td>662</td><td>606</td><td>933</td><td>1,284</td><td>1,172</td><td>896</td><td>1,197</td><td>1,464</td><td>2,252</td><td>3,486</td><td>4,729</td><td>5,964</td></tr><tr><td>Non-opt net</td><td>33</td><td>26</td><td>27</td><td>26</td><td>47</td><td>49</td><td>50</td><td>47</td><td>32</td><td>112</td><td>194</td><td>202</td></tr><tr><td>Income before tax</td><td>695</td><td>633</td><td>960</td><td>1,310</td><td>1,220</td><td>945</td><td>1,247</td><td>1,512</td><td>2,285</td><td>3,598</td><td>4,924</td><td>6,166</td></tr><tr><td>Income Tax</td><td>(99)</td><td>(101)</td><td>(139)</td><td>(190)</td><td>(183)</td><td>(147)</td><td>(181)</td><td>(219)</td><td>(366)</td><td>(529)</td><td>(729)</td><td>(921)</td></tr><tr><td>Net income</td><td>596</td><td>532</td><td>821</td><td>1,120</td><td>1,037</td><td>799</td><td>1,066</td><td>1,293</td><td>1,912</td><td>3,069</td><td>4,194</td><td>5,245</td></tr><tr><td>EPS (NT$)</td><td>8.0</td><td>7.1</td><td>11.0</td><td>15.0</td><td>13.9</td><td>10.7</td><td>14.3</td><td>17.3</td><td>25.6</td><td>41.1</td><td>56.2</td><td>70.2</td></tr><tr><td colspan="13">Margin; tax rate</td></tr><tr><td>Gross margin</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>Operating expenses</td><td>39%</td><td>41%</td><td>33%</td><td>28%</td><td>30%</td><td>34%</td><td>29%</td><td>27%</td><td>41%</td><td>34%</td><td>30%</td><td>27%</td></tr><tr><td>Operating margin</td><td>61%</td><td>59%</td><td>67%</td><td>72%</td><td>70%</td><td>66%</td><td>71%</td><td>73%</td><td>59%</td><td>66%</td><td>70%</td><td>73%</td></tr><tr><td>Pretax margin</td><td>64%</td><td>62%</td><td>69%</td><td>74%</td><td>73%</td><td>69%</td><td>73%</td><td>76%</td><td>59%</td><td>68%</td><td>73%</td><td>76%</td></tr><tr><td>Net margin</td><td>54%</td><td>52%</td><td>59%</td><td>63%</td><td>62%</td><td>58%</td><td>63%</td><td>65%</td><td>50%</td><td>58%</td><td>62%</td><td>64%</td></tr><tr><td>Tax rate</td><td>14%</td><td>16%</td><td>15%</td><td>15%</td><td>15%</td><td>16%</td><td>15%</td><td>15%</td><td>16%</td><td>15%</td><td>15%</td><td>15%</td></tr><tr><td colspan="13">Sequential growth %</td></tr><tr><td>Revenue</td><td>4%</td><td>-7%</td><td>36%</td><td>28%</td><td>-6%</td><td>-18%</td><td>24%</td><td>18%</td><td>7%</td><td>37%</td><td>27%</td><td>21%</td></tr><tr><td>Gross profit</td><td>4%</td><td>-7%</td><td>36%</td><td>28%</td><td>-6%</td><td>-18%</td><td>24%</td><td>18%</td><td>7%</td><td>37%</td><td>27%</td><td>21%</td></tr><tr><td>Operating exp</td><td>5%</td><td>-4%</td><td>9%</td><td>9%</td><td>0%</td><td>-4%</td><td>6%</td><td>6%</td><td>-1%</td><td>12%</td><td>11%</td><td>10%</td></tr><tr><td>Operating income</td><td>4%</td><td>-8%</td><td>54%</td><td>38%</td><td>-9%</td><td>-24%</td><td>34%</td><td>22%</td><td>13%</td><td>55%</td><td>36%</td><td>26%</td></tr><tr><td>Net income</td><td>6%</td><td>-11%</td><td>54%</td><td>36%</td><td>-7%</td><td>-23%</td><td>34%</td><td>21%</td><td>4%</td><td>61%</td><td>37%</td><td>25%</td></tr></table>

Source: BofA Global Research estimates, company data   
BofA GLOBAL RESEARCH

Exhibit 7: Earnings estimate changes – WT Micro

We raise 2026-28E net income by 7-21% after baking in the assumption of stronger revenue growth

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">BofA 26 (E)</td><td colspan="3">BofA 27 (E)</td><td colspan="3">BofA 28 (E)</td></tr><tr><td>New</td><td>Old</td><td>Diff (%)</td><td>New</td><td>Old</td><td>Diff (%)</td><td>New</td><td>Old</td><td>Diff (%)</td></tr><tr><td>Total sales</td><td>2,232,442</td><td>2,024,764</td><td>10.3</td><td>2,815,628</td><td>2,508,893</td><td>12.2</td><td>3,332,383</td><td>3,074,776</td><td>8.4</td></tr><tr><td>Gross profit</td><td>73,521</td><td>64,408</td><td>14.1</td><td>89,256</td><td>78,582</td><td>13.6</td><td>104,080</td><td>96,034</td><td>8.4</td></tr><tr><td>Gross margin</td><td>3.3%</td><td>3.2%</td><td>0.1 ppt</td><td>3.2%</td><td>3.1%</td><td>0.0 ppt</td><td>3.1%</td><td>3.1%</td><td>0.0 ppt</td></tr><tr><td>Operating profit</td><td>44,286</td><td>35,662</td><td>24.2</td><td>56,027</td><td>47,357</td><td>18.3</td><td>68,125</td><td>61,531</td><td>10.7</td></tr><tr><td>Operating margin</td><td>2.0%</td><td>1.8%</td><td>0.2 ppt</td><td>2.0%</td><td>1.9%</td><td>0.1 ppt</td><td>2.0%</td><td>2.0%</td><td>0.0 ppt</td></tr><tr><td>Pretax income</td><td>38,854</td><td>32,389</td><td>20.0</td><td>49,304</td><td>42,949</td><td>14.8</td><td>61,550</td><td>57,294</td><td>7.4</td></tr><tr><td>Pretax margin</td><td>1.7%</td><td>1.6%</td><td>0.1 ppt</td><td>1.8%</td><td>1.7%</td><td>0.0 ppt</td><td>1.8%</td><td>1.9%</td><td>0.0 ppt</td></tr><tr><td>Net income</td><td>30,712</td><td>25,449</td><td>20.7</td><td>37,137</td><td>32,409</td><td>14.6</td><td>46,400</td><td>43,188</td><td>7.4</td></tr><tr><td>Net margin</td><td>1.4%</td><td>1.3%</td><td>0.1 ppt</td><td>1.3%</td><td>1.3%</td><td>0.0 ppt</td><td>1.4%</td><td>1.4%</td><td>0.0 ppt</td></tr><tr><td>EPS (NT$)</td><td>24.70</td><td>19.40</td><td>27.3</td><td>29.86</td><td>24.70</td><td>20.9</td><td>37.31</td><td>32.92</td><td>13.4</td></tr></table>

Source: BofA Global Research estimates   
BofA GLOBAL RESEARCH

Exhibit 8: BofAe vs consensus – WT Micro

We are $27\% / 20\%$ ahead of consensus for 2026/27E net income, given the assumptions of stronger revenue growth and operating leverage

<table><tr><td rowspan="2">(NT$mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>BofAe</td><td>Consensus</td><td>Diff (%)</td><td>BofAe</td><td>Consensus</td><td>Diff (%)</td></tr><tr><td>Total sales</td><td>2,232,442</td><td>2,033,962</td><td>9.8</td><td>2,815,628</td><td>2,596,421</td><td>8.4</td></tr><tr><td>Gross profit</td><td>73,521</td><td>65,087</td><td>13.0</td><td>89,256</td><td>77,893</td><td>14.6</td></tr><tr><td>Gross margin</td><td>3.3%</td><td>3.2%</td><td>0.1 ppt</td><td>3.2%</td><td>3.0%</td><td>0.2 ppt</td></tr><tr><td>Operating profit</td><td>44,286</td><td>34,785</td><td>27.3</td><td>56,027</td><td>43,534</td><td>28.7</td></tr><tr><td>Operating margin</td><td>2.0%</td><td>1.7%</td><td>0.3 ppt</td><td>2.0%</td><td>1.7%</td><td>0.3 ppt</td></tr><tr><td>Pretax income</td><td>38,854</td><td>31,114</td><td>24.9</td><td>49,304</td><td>39,710</td><td>24.2</td></tr><tr><td>Pretax margin</td><td>1.7%</td><td>1.5%</td><td>0.2 ppt</td><td>1.8%</td><td>1.5%</td><td>0.2 ppt</td></tr><tr><td>Net income</td><td>30,712</td><td>24,267</td><td>26.6</td><td>37,137</td><td>30,888</td><td>20.2</td></tr><tr><td>Net margin</td><td>1.4%</td><td>1.2%</td><td>0.2 ppt</td><td>1.3%</td><td>1.2%</td><td>0.1 ppt</td></tr><tr><td>EPS (NT$)</td><td>24.70</td><td>19.52</td><td>26.6</td><td>29.86</td><td>24.84</td><td>20.2</td></tr></table>

Source: BofA Global Research estimates, Bloomberg

# Exhibit 8: BofAe vs consensus – WT Micro

We are 27%/20% ahead of consensus for 2026/27E net income, given the assumptions of stronger revenue growth and operating leverage

(NT\$mn)

2026E

2027E

BofA GLOBAL RESEARCH

# Exhibit 9: Income statement – WT Micro

We expect the company's operating margin to stay at $\sim 2\%$ in 2026-28E

<table><tr><td>NT$mn; %</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>494,273</td><td>559,915</td><td>591,489</td><td>586,765</td><td>611,205</td><td>680,694</td><td>747,116</td><td>776,613</td><td>1,177,949</td><td>2,232,442</td><td>2,815,628</td><td>3,332,383</td></tr><tr><td>Cost of Revenue</td><td>-477,229</td><td>-541,438</td><td>-572,266</td><td>-567,988</td><td>-591,341</td><td>-658,911</td><td>-723,582</td><td>-752,538</td><td>-1,130,325</td><td>-2,158,921</td><td>-2,726,372</td><td>-3,228,303</td></tr><tr><td>Gross profit</td><td>17,044</td><td>18,477</td><td>19,223</td><td>18,776</td><td>19,864</td><td>21,782</td><td>23,534</td><td>24,075</td><td>47,624</td><td>73,521</td><td>89,256</td><td>104,080</td></tr><tr><td>Operating exp</td><td>-7,100</td><td>-7,055</td><td>-7,423</td><td>-7,657</td><td>-8,007</td><td>-8,236</td><td>-8,442</td><td>-8,543</td><td>-26,742</td><td>-29,235</td><td>-33,228</td><td>-35,955</td></tr><tr><td>Operating income</td><td>9,944</td><td>11,422</td><td>11,800</td><td>11,119</td><td>11,857</td><td>13,546</td><td>15,092</td><td>15,532</td><td>20,882</td><td>44,286</td><td>56,027</td><td>68,125</td></tr><tr><td>Non-opt net</td><td>-922</td><td>-1,525</td><td>-1,441</td><td>-1,544</td><td>-1,670</td><td>-1,680</td><td>-1,673</td><td>-1,699</td><td>-3,483</td><td>-5,432</td><td>-6,723</td><td>-6,575</td></tr><tr><td>Income before tax</td><td>9,022</td><td>9,898</td><td>10,359</td><td>9,575</td><td>10,187</td><td>11,865</td><td>13,418</td><td>13,834</td><td>17,399</td><td>38,854</td><td>49,304</td><td>61,550</td></tr><tr><td>Income Tax</td><td>-2,006</td><td>-1,980</td><td>-2,072</td><td>-2,011</td><td>-2,343</td><td>-3,441</td><td>-3,220</td><td>-3,043</td><td>-3,833</td><td>-8,068</td><td>-12,048</td><td>-15,0

[中间内容因长度限制已省略]

ions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
