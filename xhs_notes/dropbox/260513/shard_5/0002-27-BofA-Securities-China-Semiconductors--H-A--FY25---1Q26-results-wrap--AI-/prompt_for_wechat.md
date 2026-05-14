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
# China Semiconductors (H/A)

# FY25 & 1Q26 results wrap: AI-driven demand remains strong

Price Objective Change

# Mixed FY25 results amid ongoing sector divergence

This report summarizes the 1Q26/FY25 results for fabless & IDM companies under our coverage. A-share semiconductor companies reported mixed FY25 results, with a relatively balanced beat/miss profile and continued divergence across sub-sectors. Sector revenue grew at an average of c.15% YoY in 4Q25, supported primarily by recovery in computing-related demand, while profitability remained volatile. By segment, companies with memory chips exposure (e.g., Montage) delivered strong results, benefiting from DDR5 penetration and product upcycle tailwinds, whereas power semi (NCE, Silan) or vendors with major smartphone exposure (i.e. Goodix, Maxscend) generally reported soft results. H-share listed companies under our coverage reported mixed FY25 results, with Horizon Robotics delivering strong topline growth (+58% YoY). In addition, InnoScience and Black Sesame posted solid FY25 revenue growth at 46% YoY and 73% YoY, respectively, but remained loss-making, reflecting investment phase in emerging segments.

# 1Q26: clearer recovery momentum, led by AI demand

Encouragingly, 1Q26 marked a clearer acceleration in sector fundamentals, with revenue growth expanding to c.30% YoY on average and earnings growth rebounding more meaningfully. The improvement was primarily volume-driven, reflecting gradual demand recovery and early signs of AI-related demand ramp across computing and AIoT. Within our coverage, Montage and GigaDevice continued to outperform, while AI-related names (e.g., Rockchip) maintained solid growth momentum on product ramp-up and expanding end-market adoption. Overall, we continue to see a stable recovery trend, with AI-exposed and computing-related segments leading, while traditional power semis remain in a more gradual recovery phase.

# Preferred stock picks; estimates & PO changes

Considering growth visibility, earnings trajectory and structural positioning, we like Montage for its (1) sustained DDR5 upgrade cycle, (2) ramp-up of PCIe Retimer / other emerging products (e.g., MRCD / MDB), and (3) solid growth of CPU/server shipment. GigaDevice offers solid secular growth, driven by continued share gains in DRAM / MCU / NOR Flash and benefits from memory upcycle. InnoScience is also preferred for promising growth outlook with multiple long-term growth drivers (AIDC, auto, robotics). Horizon Robotics stands out on strong revenue growth and expanding design wins, benefiting from rising ADAS penetration and scaling of its next-generation automotive SoCs. We also see Rockchip and NCE Power as beneficiaries of AIoT and power semi demand recovery, respectively.

We revise our estimates and POs for Montage, Goodix, and Silan.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.
Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.
BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 24 to 26. Analyst Certification on page 22. Price Objective Basis/Risk on page 19.
12971999

# 11 May 2026

Equity

China

Semiconductors

Daley Li, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 5365

daley.li2@bofa.com

Owen Wang >>

Research Analyst

BofA (Hong Kong)

+852 3508 6533

owen.wang2@bofa.com

Harry Zhuang >>

Research Analyst

BofA (Hong Kong)

+852 3508 7998

harry.zhuang@bofa.com

See the list of acronyms in Exhibit 33.

Exhibit 1: We revise our POs for three semis companies under our coverage   
PO change 

<table><tr><td>Company</td><td>Old</td><td>New</td></tr><tr><td>Montage</td><td>BuyRMB220</td><td>BuyRMB251</td></tr><tr><td>Goodix</td><td>NeutralRMB89</td><td>NeutralRMB73</td></tr><tr><td>Silan</td><td>U/PRMB18.9</td><td>U/PRMB20.3</td></tr></table>

Source: BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 2: Our top picks for Buys are Montage, GigaDevice and Horizon Robotics

Investment thesis summary of our semiconductor coverage

<table><tr><td>BofA Ticker</td><td>Company</td><td>Ticker</td><td>PO</td><td>Rating</td><td>Investment thesis</td></tr><tr><td>XRDFF</td><td>Montage</td><td>688008 CH</td><td>RMB251.0</td><td>Buy</td><td>1) Solid growth of memory interface and supporting chips on DDR5 sub-gen upgrade;2) Rapid emerging product (i.e., PCIe Retimer) ramp-up;3) Secular growth on enlarging interconnect chip Total Addressable Market (TAM).</td></tr><tr><td>XGXIF</td><td>GigaDevice</td><td>603986 CH</td><td>RMB455.0</td><td>Buy</td><td>1) Stronger growth of its DRAM business on price hike and share gain2) Solid recovery of NOR from modest price hike and demand recovery3) Market share gain potential in China MCU market and promising long-term growth outlook for its auto MCU business</td></tr><tr><td>HRZRF</td><td>Horizon Robotics</td><td>9660 HK</td><td>HK$11.9</td><td>Buy</td><td>1) Secular growth of autonomous driving SoC market,2) Leading market position,3) Promising share gain opportunity in China. Besides, we believe expansion into non-automotive market could be the second growth engine in the long term.</td></tr><tr><td>XRPXF</td><td>Rockchip</td><td>603893 CH</td><td>RMB235.0</td><td>Buy</td><td>1) A good proxy for booming AIoT SoCs;2) Strategic expansion into frontier markets such as automotive electronics and robotics</td></tr><tr><td>XSCHF</td><td>InnoScience</td><td>2577 HK</td><td>HK$92.0</td><td>Buy</td><td>1) A good proxy for rapid growth of global GaN power semi market2) NVIDIA partnership on 800V HVDC architecture which positions InnoScience as a key enabler of megawatt-scale computing with promising revenue upside</td></tr><tr><td>XVFFF</td><td>NCE Power</td><td>605111 CH</td><td>RMB47.0</td><td>Buy</td><td>1) Secular growth potential of China MOSFET market driven by emerging applications (EV, AI computing);2) Further market-share gain amid the localization tailwind;3) Potential margin improvement given favorable product mix change (i.e., high-end products).</td></tr><tr><td>BSIHF</td><td>Black Sesame</td><td>2533 HK</td><td>HK$20.0</td><td>Neutral</td><td>1) Secular growth of China&#x27;s autonomous driving SoC market,2) Solid revenue growth momentum ahead with new product launches and rising penetration among auto OEMs, while we think price upside should be limited due to low visibility to achieve breakeven in the near term.</td></tr><tr><td>XQPLF</td><td>Goodix</td><td>603160 CH</td><td>RMB73.0</td><td>Neutral</td><td>1) Gradually easing competition in fingerprint sensor market amid prolonged margin pressure;2) solid growth of touch control IC and emerging growth drivers from new products;3) Fair valuation trading around historical average P/E.</td></tr><tr><td>XMXSF</td><td>Maxscend</td><td>300782 CH</td><td>RMB50.0</td><td>U/P</td><td>1) Softer top-line growth ahead on slow ramp-up of new module products and muted industry smartphone shipment;2) N-T margin pressure on competition and higher depreciation costs (from XinZhuo project).</td></tr><tr><td>XDFRF</td><td>Silan</td><td>600460 CH</td><td>RMB20.3</td><td>U/P</td><td>1) Pricing pressure due to intensified competition of China power semi market2) Softer earnings from persistent margins pressure and higher depreciation expense3) Rich valuation.</td></tr></table>

Source: BofA Global Research

BofA GLOBAL RESEARCH

Exhibit 3: China semiconductor sector: FY25 & 1Q26 results wrap (A-share)

A-share semi companies reported mixed FY25 & 1Q26 results

<table><tr><td>(Rmb mn)</td><td colspan="3">Revenue</td><td colspan="3">Revenue YoY (%)</td><td colspan="3">Net profit / (loss)</td><td colspan="3">Net profit / (loss) YoY (%)</td><td rowspan="2">FY25 Beat/In-line/Miss</td><td rowspan="2">1Q26 Beat/In-line/Miss</td></tr><tr><td>Company</td><td>9M25</td><td>4Q25</td><td>1Q26</td><td>9M25</td><td>4Q25</td><td>1Q26</td><td>9M25</td><td>4Q25</td><td>1Q26</td><td>9M25</td><td>4Q25</td><td>1Q26</td></tr><tr><td>Montage</td><td>4,058</td><td>1,399</td><td>1,461</td><td>58%</td><td>31%</td><td>20%</td><td>1,632</td><td>603</td><td>847</td><td>67%</td><td>39%</td><td>61%</td><td>In-line</td><td>Beat</td></tr><tr><td>GigaDevice</td><td>6,832</td><td>2,372</td><td>4,188</td><td>21%</td><td>39%</td><td>119%</td><td>1,083</td><td>565</td><td>1,461</td><td>30%</td><td>109%</td><td>523%</td><td>Beat</td><td>Beat</td></tr><tr><td>Rockchip</td><td>3,141</td><td>1,261</td><td>1,205</td><td>45%</td><td>29%</td><td>36%</td><td>780</td><td>260</td><td>329</td><td>122%</td><td>7%</td><td>57%</td><td>In-line</td><td>In-line</td></tr><tr><td>NCE Power</td><td>1,385</td><td>492</td><td>517</td><td>2%</td><td>4%</td><td>15%</td><td>335</td><td>59</td><td>95</td><td>1%</td><td>-42%</td><td>-13%</td><td>Miss</td><td>In-line</td></tr><tr><td>Goodix</td><td>3,521</td><td>1,215</td><td>969</td><td>9%</td><td>5%</td><td>-9%</td><td>677</td><td>160</td><td>117</td><td>51%</td><td>3%</td><td>-40%</td><td>Miss</td><td>Miss</td></tr><tr><td>Maxscend</td><td>2,769</td><td>957</td><td>828</td><td>-18%</td><td>-15%</td><td>9%</td><td>(171)</td><td>(122)</td><td>(144)</td><td>-140%</td><td>418%</td><td>210%</td><td>In-line</td><td>Miss</td></tr><tr><td>Silan</td><td>9,713</td><td>3,339</td><td>3,519</td><td>19%</td><td>9%</td><td>17%</td><td>349</td><td>49</td><td>209</td><td>1109%</td><td>-74%</td><td>41%</td><td>Miss</td><td>Miss</td></tr><tr><td>Average</td><td></td><td></td><td></td><td>20%</td><td>15%</td><td>30%</td><td></td><td></td><td></td><td>177%</td><td>66%</td><td>120%</td><td></td><td></td></tr><tr><td>Median</td><td></td><td></td><td></td><td>19%</td><td>9%</td><td>17%</td><td></td><td></td><td></td><td>51%</td><td>7%</td><td>57%</td><td></td><td></td></tr></table>

Source: Companies, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 4: H-share semi companies under our coverage reported mixed FY25 results

China semiconductor sector: FY25 results wrap (H-share)

<table><tr><td>(Rmb mn)</td><td colspan="2">Revenue</td><td colspan="2">Revenue YoY (%)</td><td colspan="2">Net profit / (loss)</td><td colspan="2">Net profit / (loss) YoY (%)</td><td rowspan="2">FY25 Beat/In-line/Miss</td></tr><tr><td>Company</td><td>2H25</td><td>FY25</td><td>2H25</td><td>FY25</td><td>2H25</td><td>FY25</td><td>2H25</td><td>FY25</td></tr><tr><td>Horizon Robotics</td><td>2,192</td><td>3,758</td><td>51%</td><td>58%</td><td>(5,236)</td><td>(10,469)</td><td>-170%</td><td>n.m.</td><td>Beat</td></tr><tr><td>InnoScience</td><td>660</td><td>1,213</td><td>49%</td><td>46%</td><td>(412)</td><td>(841)</td><td>-26%</td><td>-20%</td><td>Slightly miss</td></tr><tr><td>Black Sesame</td><td>569</td><td>822</td><td>94%</td><td>73%</td><td>(662)</td><td>(1,425)</td><td>-16%</td><td>n.m.</td><td>Beat</td></tr></table>

Source: Companies, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 5: China semiconductors: estimates changes

We cut earnings forecasts in FY26-27E for Silan and Goodix and raise revenue and earnings forecasts in FY26-28E for Montage

<table><tr><td rowspan="2">Company</td><td rowspan="2">Rmb mn</td><td colspan="3">FY26E</td><td colspan="3">FY27E</td><td colspan="3">FY28E</td><td rowspan="2">Reason for estimates revision</td></tr><tr><td>New</td><td>Old</td><td>Diff (%)</td><td>New</td><td>Old</td><td>Diff (%)</td><td>New</td><td>Old</td><td>Diff (%)</td></tr><tr><td rowspan="2">Montage</td><td>Revenue</td><td>7,570</td><td>7,448</td><td>1.6</td><td>10,481</td><td>10,250</td><td>2.3</td><td>13,567</td><td>13,317</td><td>1.9</td><td rowspan="2">Better demand outlook for CPU as discussed in recent Intel and AMD results, we think it will be positive for Montage&#x27;s shipment of memory interface chip ahead.</td></tr><tr><td>Net profit</td><td>3,945</td><td>3,850</td><td>2.5</td><td>5,335</td><td>5,104</td><td>4.5</td><td>6,955</td><td>6,652</td><td>4.6</td></tr><tr><td rowspan="2">Silan</td><td>Revenue</td><td>15,549</td><td>16,084</td><td>-3.3</td><td>17,769</td><td>18,236</td><td>-2.6</td><td>19,634</td><td>N.A</td><td>N.A</td><td rowspan="2">Faster revenue growth ahead on demand recovery and new products ramp-up. Lower earnings forecast due to N-T margin pressure due to increased depreciation from project &#x27;Xinzhuo&#x27;, and high R&amp;D expenses</td></tr><tr><td>Net profit</td><td>808</td><td>875</td><td>-7.6</td><td>1,065</td><td>1,085</td><td>-1.8</td><td>1,272</td><td>N.A</td><td>N.A</td></tr><tr><td rowspan="2">Goodix</td><td>Revenue</td><td>5,408</td><td>6,069</td><td>-10.9</td><td>6,257</td><td>7,065</td><td>-11.4</td><td>7,336</td><td>N.A</td><td>N.A</td><td rowspan="2">Slower revenue growth ahead due to weaker demand and lower ASP of capaCitive/optical products on competition. Better earnings recovery ahead on margins improvement and effective cost control.</td></tr><tr><td>Net profit</td><td>846</td><td>958</td><td>-11.7</td><td>931</td><td>1,074</td><td>-13.4</td><td>960</td><td>N.A</td><td>N.A</td></tr></table>

Source: BofA Global Research estimates   
BofA GLOBAL RESEARCH

# Capex upcycle to drive solid demand

Globally, consensus projects that aggregated capex across top-5 U.S cloud vendors can grow +60% YoY in CY26E, according to BofA U.S Semiconductor Team (report link). Meanwhile, total server capex in China is expected to further rise 25% YoY in 2026E per our estimate. We see promising growth outlook for Montage's memory interface chips (used in traditional server) and PCIe Retimer (used in AI server), with wider AI adoption for agentic AI and stronger capex by internet companies / cloud service providers (CSP).

# Exhibit 6: Summary of Cloud Capex Outlook (incl. leases)

Consensus aggregate projections suggest cloud capex across major U.S cloud vendors can grow +60%/+17% YoY in CY26/27E

<table><tr><td>CapEx ($mn)</td><td>C1Q25</td><td>C2Q25</td><td>C3Q25</td><td>C4Q25</td><td>C1Q26E</td><td>C2Q26E</td><td>C3Q26E</td><td>C4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td></tr><tr><td>Top 5 US</td><td>82,419</td><td>104,919</td><td>121,279</td><td>139,046</td><td>158,943</td><td>168,660</td><td>183,689</td><td>203,364</td><td>161,255</td><td>261,106</td><td>447,663</td><td>714,656</td><td>834,625</td></tr><tr><td>Google</td><td>17,197</td><td>22,446</td><td>23,953</td><td>27,851</td><td>35,704</td><td>42,134</td><td>47,327</td><td>53,086</td><td>32,251</td><td>52,535</td><td>91,447</td><td>178,251</td><td>210,288</td></tr><tr><td>Microsoft (incl. leases)</td><td>21,400</td><td>24,200</td><td>34,900</td><td>37,500</td><td>35,221</td><td>38,004</td><td>38,737</td><td>41,713</td><td>41,200</td><td>75,600</td><td>118,000</td><td>153,675</td><td>175,336</td></tr><tr><td>Amazon (incl. leases)</td><td>25,019</td><td>32,183</td><td>35,095</td><td>39,522</td><td>42,686</td><td>47,605</td><td>51,029</td><td>56,404</td><td>52,729</td><td>82,999</td><td>131,819</td><td>197,725</td><td>219,034</td></tr><tr><td>Meta (incl. leases)</td><td>12,941</td><td>17,010</td><td>18,829</td><td>22,140</td><td>26,698</td><td>29,851</td><td>32,511</td><td>36,366</td><td>28,140</td><td>39,227</td><td>70,920</td><td>125,426</td><td>154,626</td></tr><tr><td>Oracle</td><td>5,862</td><td>9,080</td><td>8,502</td><td>12,033</td><td>18,635</td><td>11,065</td><td>14,085</td><td>15,795</td><td>6,935</td><td>10,745</td><td>35,477</td><td>59,580</td><td>75,342</td></tr><tr><td>YoY %</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Top 5 US</td><td>67.10%</td><td>71.80%</td><td>80.50%</td><td>66.50%</td><td>92.80%</td><td>60.80%</td><td>51.50%</td><td>46.30%</td><td>-0.60%</td><td>61.90%</td><td>71.40%</td><td>59.60%</td><td>16.80%</td></tr><tr><td>Google</td><td>43.20%</td><td>70.20%</td><td>83.40%</td><td>95.10%</td><td>107.60%</td><td>87.70%</td><td>97.60%</td><td>90.60%</td><td>2.40%</td><td>62.90%</td><td>74.10%</td><td>94.90%</td><td>18.00%</td></tr><tr><td>Microsoft (incl. leases)</td><td>52.90%</td><td>27.40%</td><td>74.50%</td><td>65.90%</td><td>64.60%</td><td>57.00%</td><td>11.00%</td><td>11.20%</td><td>45.10%</td><td>83.50%</td><td>56.10%</td><td>30.20%</td><td>14.10%</td></tr><tr><td>Amazon (incl. leases)</td><td>67.60%</td><td>82.70%</td><td>55.20%</td><td>42.00%</td><td>70.60%</td><td>47.90%</td><td>45.40%</td><td>42.70%</td><td>-17.20%</td><td>57.40%</td><td>58.80%</td><td>50.00%</td><td>10.80%</td></tr><tr><td>Meta (incl. leases)</td><td>92.70%</td><td>100.80%</td><td>104.70%</td><td>49.20%</td><td>106.30%</td><td>75.50%</td><td>72.70%</td><td>64.30%</td><td>-12.20%</td><td>39.40%</td><td>80.80%</td><td>76.90%</td><td>23.30%</td></tr><tr><td>Oracle</td><td>250.20%</td><td>224.50%</td><td>269.20%</td><td>203.10%</td><td>217.90%</td><td>21.90%</td><td>65.70%</td><td>31.30%</td><td>3.80%</td><td>54.90%</td><td>230.20%</td><td>67.90%</td><td>26.50%</td></tr></table>

Source: BofA Global Research estimates, Bloomberg   
BofA GLOBAL RESEARCH

# Exhibit 7: We estimate China's total server capex to increase $25\%$ YoY in 2026E

Total server capex in China

<table><tr><td></td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2025-28E CAGR</td></tr><tr><td>Total server capex (Rmb bn)</td><td>284</td><td>379</td><td>475</td><td>550</td><td>625</td><td>18%</td></tr><tr><td>YoY (%)</td><td>60%</td><td>34%</td><td>25%</td><td>16%</td><td>14%</td><td></td></tr><tr><td>AI server capex (Rmb bn)</td><td>180</td><td>267</td><td>350</td><td>414</td><td>478</td><td>22%</td></tr><tr><td>YoY (%)</td><td>115%</td><td>48%</td><td>31%</td><td>18%</td><td>15%</td><td></td></tr><tr><td>Traditional server capex (Rmb bn)</td><td>104</td><td>113</td><td>125</td><td>136</td><td>147</td><td></td></tr><tr><td>YoY (%)</td><td>11%</td><td>9%</td><td>11%</td><td>9%</td><td>8%</td><td></td></tr></table>

Source: Companies, CIC, BofA Global Research estimates; Note: Include major Internet companies / CSPs, telecom operators and others.   
BofA GLOBAL RESEARCH

# Memory upcycles to continue

According to BofA Global Memory Tech Team (report on 30 Apr), the memory “supercycle” is expected to continue into 2027-2028. Key catalysts should be tight chip supply vs strongly rising AI chip demand. The capex is strongly rising, but actual chip productio

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
