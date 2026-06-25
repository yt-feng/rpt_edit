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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Asia-Pacific Technology | Asia Pacific

# AI Supply Chain: Preliminary 2027 TSMC CoWoS Allocation

Nvidia's GPU and CPU remain the key drivers of TSMC's 2027 CoWoS demand. With improved ABF substrate supply sourcing, MediaTek's 2027 and 2028 TPU shipments could show upside.

Into 2027, Nvidia likely remains the major user of TSMC's CoWoS capacity: At Computex in early June, in response to our question about TSMC's capacity allocation, Nvidia's CEO indicated that it has secured sufficient TSMC capacity to support robust growth in 2027. In our previous episode, we had raised our 2027 TSMC CoWoS capacity assumption to 200kwpm by year-end (from 170kwpm), implying \~60% Y/Y growth for the global AI XPU industry. Based on our industry checks, we break down TSMC's customer mix. Nvidia uses TSMC's CoWoS-L as the single source for its AI GPU products (e.g., Blackwell and Rubin). Its 2027 CoWoS-L consumption could reach \~910k, up \~40% Y/Y. Strong CoWoS-R bookings by Nvidia aslo suggest very strong Vera CPU shipments (almost doubling). Taken together, this is consistent with Joe Moore's forecast for Nvidia's data center revenue to rise 52% Y/Y over a similar period.

Google's TPU ASIC is the second-largest user of TSMC CoWoS: MediaTek's booking for 180k CoWoS-S implies \~3.6mn units of TPU v8t (ZebraFish), above our 2.5mn shipment assumption, where we incorporate potential ABF substrate shortages. However, if MediaTek can help Google source more T-Glass, there may be upside to our shipment assumption. Our checks suggest that the new 2nm TPU codename TriggerFish is the inferencing-focused version of HumuFish, in line with our previous understanding that all TPUs are capable of both training and inferencing. We believe TriggerFish may also support TPU leasing services. Meanwhile, we believe Broadcom bookings of 365k CoWoS-S likely include Google TPU v7 (Ironwood), v8i (SunFish), Tomahawk 5/6, and other smaller ASICs. If we assume 330k of Broadcom's CoWoS-S is allocated to TPU v8i (SunFish), this would imply \~3.9mn units, with larger die size and higher chip value vs. MediaTek's TPU v8t (ZebraFish). Overall, both design service partners appear positioned to benefit from growth in the TPU TAM in 2027.

CPU starting to consume significant 2.5D advanced packaging capacity: This echoes Joe Moore's recent Taiwan field trip observations: growing CPU demand for agentic AI (link). In addition, based on our CoWoS consumption forecasts, Nvidia's 3nm Vera CPU could grow to 5.75mn units in 2027, while AMD's 2nm Venice CPU may reach 6.75mn units in 2027 vs. \~1.25mn in 2026. For Taiwan AI semi supply chain stocks: 1) MediaTek (Google TPU) is our Top Pick; 2) Aspeed remains the best proxy for CPU server BMC; and 3) we reiterate OW on TSMC, ASE (AMD Venice CPU), KYEC (Nvidia GPU and Google TPU supply chain), Winway, MPI, and Hon Precision in chip manufacturing.

MS TAIWAN LIMITED+

Charlie Chan
Equity Analyst
Charlie.Chan@morganstanley.com +886 2 2730-1725

Daniel Yen, CFA
Equity Analyst
Daniel.Yen@morganstanley.com +886 2 2730-2863

MS ASIA LIMITED+
Daisy Dai, CFA
Equity Analyst
Daisy.Dai@morganstanley.com +852 2848-7310

MS TAIWAN LIMITED+
Tiffany Yeh
Equity Analyst
Tiffany.Yeh@morganstanley.com +886 2 7712-3032

Lucas Wang
Research Associate
Lucas.Wang@morganstanley.com +886 2 2730-2875

Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

Henry Zhao
Research Associate
Henry.Zhao@morganstanley.com +852 2239-7731

![](images/d4f637f945185b202e2acdeebd809407a4c828947ef60add24c33fc5a8aedab0.jpg)  
Asia Summer School 2026

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Introducing Our 2027 Global CoWoS Capacity Update

In our previous report (see Asia-Pacific Technology: Taiwan Computex preview: NVIDIA's Vera CPU and Rubin GPU seen as the main show (27 May 2026)), we lifted our TSMC 2027 CoWoS capacity assumption to 200kwpm from 170kwpm and trimmed our SolC capacity build forecasts. Strong AI GPU and CPU demand has led TSMC to further expand CoWoS capacity at its AP7 fab. Our checks suggest that TSMC is converting its Fab 15A 28nm/22nm space into 55nm interposer production.

On the other hand, we expect the non-TSMC camp to expand CoWoS capacity to 80kwpm by end-2027e. For ASE/SPIL, we expect FoCoS+CoWoS capacity to rise from 30kwpm at 2026-end to 50kwpm at 2027-end, with expansion focused on CoWoS-L and CoWoS-R. For Amkor, we expect CoWoS capacity to increase from 20kwpm at 2026-end to 30kwpm at 2027-end, also focused on CoWoS-L and CoWoS-R.

Exhibit 1: Global CoWoS demand breakdown: 2026e vs. 2027e  
Global CoWoS capacity demand by key customer  
![](images/c7ab7703a695302d108474c3b57b27314189ce8e2b7722eab2ff3e866c640337.jpg)  
Source: Company data, MS (e) estimates; note: estimates are complied using our supply chain checks

Exhibit 2: Global CoWoS demand Y/Y growth profile

<table><tr><td>Y/Y</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td></tr><tr><td>NVIDIA</td><td>119%</td><td>280%</td><td>113%</td><td>84%</td><td>57%</td></tr><tr><td>Broadcom</td><td>56%</td><td>191%</td><td>25%</td><td>253%</td><td>61%</td></tr><tr><td>AMD</td><td>485%</td><td>470%</td><td>50%</td><td>117%</td><td>308%</td></tr><tr><td>Xilinx</td><td>63%</td><td>242%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>AWS/Annapurna</td><td></td><td></td><td></td><td>3%</td><td>45%</td></tr><tr><td>AWS/Alchip</td><td></td><td>71%</td><td>(69%)</td><td>420%</td><td>38%</td></tr><tr><td>Marvell</td><td>(22%)</td><td>1438%</td><td>(17%)</td><td>13%</td><td>276%</td></tr><tr><td>GUC</td><td></td><td>(15%)</td><td>300%</td><td>600%</td><td>329%</td></tr><tr><td>Cisco</td><td></td><td></td><td>36%</td><td>67%</td><td>10%</td></tr><tr><td>Others</td><td>23%</td><td>(49%)</td><td>50%</td><td>(33%)</td><td>20%</td></tr><tr><td>Total demand</td><td>95%</td><td>218%</td><td>85%</td><td>102%</td><td>93%</td></tr></table>

Source: Company data, MS (e) estimates; note: estimates are complied using our supply chain checks

## 2027 CoWoS allocation assumptions

## CoWoS update (Exhibit 3):

\- Nvidia's total CoWoS consumption increases 57% Y/Y, to 1,222k:

• CoWoS-L consumption increases 40% Y/Y, to 910k, with production focusing on Rubin and Blackwell in 1H27, followed by Rubin Ultra in 2H27.

• For CoWoS-R, we see TSMC and Amkor production focused on Vera CPU, which implies production of 5.75mn. We see this coming from both Vera Rubin/Vera Rubin Ultra racks and standalone Vera CPU rack demand.

• CoWoS-S production includes both Quantum and Spectrum switch IC, with production across TSMC, SPIL, and Amkor.

• AMD's total CoWoS consumption increases 308% Y/Y to 530k:

• We see TSMC mainly in charge of GPU-related production. We see MI455 as the key focus for 2027, with minor production for MI500 series (chip code name Arcadia) in late 2027. Total TSMC CoWoS-L booking increases 200% Y/Y in 2027e, to 240k.

• We see the non-TSMC camp, including ASE/SPIL, Amkor, and Powertech, being mainly in charge of Venice CPU, high-end PC CPU, and gaming GPU production. We see Venice CPU's CoWoS booking increasing from 50k in 2026 to 270k in 2027, implying 6.75mn units of CPU production, supporting strong demand from agentic AI.

• We see Xilinx's demand remaining flat Y/Y at 10k of CoWoS bookings.

\- Broadcom's total CoWoS consumption rises 61% Y/Y, to 484k:

• We see CoWoS-L booking increasing from 15k in 2026 to 55k in 2027, mainly for Meta's MTIAv3 ASIC Iris.

• For Google TPU, we see Ironwood and Sunfish together accounting for 343k of CoWoS-S bookings, implying 4,168k of TPU chips. We also see a slight increase in Broadcom's smaller AI ASIC customers in 2027.

• MediaTek's total CoWoS consumption increases from 40k in 2026 to 180k in 2027:

• This is mainly for TSMC's CoWoS-S capacity for TPU v8t ZebraFish.

• We also see around 400k units of chip production from Intel EMIB-T for the 2nm TPU v9 (HumuFish) TPU in 2027.

\- Separately, our checks suggest the new 2nm TPU codename TriggerFish is the inferencing-focused version of HumuFish, in line with our previous understanding that all TPUs are capable of both training and inferencing, and we believe TriggerFish may also support TPU leasing services.

\- AWS/Annapurna's CoWoS-R booking increases from 62k in 2026e to 90k in 2027e:
    • Although Annapurna is still in charge of the front-end booking for Trainium 3, we see it placing 54k of CoWoS-R at TSMC and 36k at ASE.

\- Alchip increases CoWoS-R booking 38% Y/Y, to 36k, with all of its bookings at TSMC.

• Marvell's total booking increases from 17k in 2026e to 64k in 2027e:

• Microsoft Maia 300 consumes around 50k of CoWoS-L booking at TSMC.

• For Trainium 3, we see it having 14k of CoWoS-R booking at ASE.

\- GUC's total CoWoS booking increases from 14k in 2026e to 60k in 2027e:
    - We believe demand is mainly driven by multiple customers.

Exhibit 3: Global CoWoS demand breakdown with newly introduced 2027e numbers

<table><tr><td>(k wafer)</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2023</td><td>2024</td><td>2025e</td><td>2026e</td><td>2027e</td></tr><tr><td>NVIDIA</td><td>53</td><td>200</td><td>425</td><td>780</td><td>1,222</td><td>45%</td><td>54%</td><td>62%</td><td>56%</td><td>45%</td></tr><tr><td>TSMC</td><td></td><td></td><td>390</td><td>680</td><td>1,090</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>390</td><td>650</td><td>910</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>0</td><td>20</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>0</td><td>10</td><td>130</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non-TSMC</td><td></td><td></td><td>35</td><td>100</td><td>132</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td>35</td><td>100</td><td>132</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>20</td><td>20</td><td>12</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>15</td><td>80</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Broadcom</td><td>23</td><td>68</td><td>85</td><td>300</td><td>484</td><td>20%</td><td>18%</td><td>12%</td><td>22%</td><td>18%</td></tr><tr><td>TSMC</td><td></td><td></td><td>83</td><td>260</td><td>420</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>15</td><td>55</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>83</td><td>245</td><td>365</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>2</td><td>30</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>2</td><td>30</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td></td><td>10</td><td>24</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>10</td><td>24</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AMD</td><td>7</td><td>40</td><td>60</td><td>130</td><td>530</td><td>6%</td><td>11%</td><td>9%</td><td>9%</td><td>20%</td></tr><tr><td>TSMC</td><td></td><td></td><td>60</td><td>80</td><td>240</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>70</td><td>230</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>60</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>0</td><td>50</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>50</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td></td><td>0</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>0</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Xilinx</td><td>3</td><td>10</td><td>10</td><td>10</td><td>10</td><td>3%</td><td>3%</td><td>1%</td><td>1%</td><td>0%</td></tr><tr><td>MediaTek</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td>3%</td><td>7%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AWS/Annapurna</td><td></td><td></td><td>60</td><td>62</td><td>90</td><td></td><td></td><td></td><td>4%</td><td>3%</td></tr><tr><td>TSMC</td><td></td><td></td><td>60</td><td>32</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>60</td><td>32</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td></td><td>30</td><td>36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td></td><td>30</td><td>36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AWS/Alchip</td><td>9</td><td>16</td><td>5</td><td>26</td><td>36</td><td>8%</td><td>4%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td>Intel Habana</td><td>0</td><td>7</td><td>9</td><td>0</td><td>0</td><td>0%</td><td>2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Marvell</td><td>1</td><td>18</td><td>15</td><td>17</td><td>64</td><td>1%</td><td>5%</td><td>2%</td><td>1%</td><td>2%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td>5</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td></td><td>5</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>15</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td></td><td>12</td><td>14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td></td><td>12</td><td>14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GUC</td><td>1</td><td>1</td><td>2</td><td>14</td><td>60</td><td>1%</td><td>0%</td><td>0%</td><td>1%</td><td>2%</td></tr><tr><td>Cisco</td><td></td><td>2</td><td>3</td><td>5</td><td>6</td><td></td><td>1%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Others</td><td>20</td><td>10</td><td>15</td><td>10</td><td>12</td><td>17%</td><td>3%</td><td>2%</td><td>1%</td><td>0%</td></tr><tr><td>Total demand</td><td>117</td><td>372</td><td>689</td><td>1,394</td><td>2,694</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr></table>

Source: Company data, MS (e) estimates; note: estimates are complied using our supply chain checks

Exhibit 4: Global CoWoS capacity expansion by year end and by vendor  
![](images/a7084417499473a11f75642d394a074ecb8bc291be9e9ef74ff61566afa94ac5.jpg)  
Source: Company data, MS (e) estimates

Exhibit 5: Global CoWoS consumption, by customer  
![](images/87865b1d53d80130ac9b5e59615a0a76b3b1234b264b9045a6b8e8a48c5a7e84.jpg)  
NVIDIA Broadcom AMD Xilinx AWS/Annapurna AWS/Alchip Marvell GUC MediaTek Intel Habana Others  
Source: Company data, MS (e) estimates; note: estimates are compiled using our supply chain checks

## Exhibit 6:

AI HBM consumption: up to 51bn Gb in 2027

<table><tr><td>AI chip vendor</td><td>Product name</td><td>CoWoS capacity allocation (k wafers)</td><td>Chips per CoWoS wafer</td><td>Implied shipments (k)</td><td>HBM chip density (GB)</td><td>HBM chip units</td><td>Total HBM size (GB)</td><td>HBM generation</td><td>HBM vendor</td><td>Total HBM demand (k GB)</td></tr><tr><td colspan="11">AI GPU (2027e)</td></tr><tr><td rowspan="4">NVIDIA</td><td>B300</td><td>40</td><td>14</td><td>560</td><td>36</td><td>8</td><td>288</td><td>HBM3e 12hi</td><td>Hynix/Micron</td><td>161,280</td></tr><tr><td>Vera CPU</td><td>250</td><td>23</td><td>5,750</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rubin R200</td><td>740</td><td>8</td><td>5,920</td><td>36</td><td>8</td><td>288</td><td>HBM4 12hi</td><td>Hynix/Micron/Samsung</td><td>1,704,960</td></tr><tr><td>Rubin Ultra</td><td>130</td><td>8</td><td>1,040</td><td>48</td><td>8</td><td>384</td><td>HBM4e 12hi</td><td>Hynix/Micron/Samsung</td><td>399,360</td></tr><tr><td rowspan="4">AMD</td><td>MI350 series</td><td>24</td><td>12</td><td>288</td><td>36</td><td>8</td><td>288</td><td>HBM3e 12hi</td><td>Samsung/Micron</td><td>82,944</td></tr><tr><td>MI400 series</td><td>192</td><td>10</td><td>1,920</td><td>36</td><td>12</td><td>432</td><td>HBM4 12hi</td><td>Samsung/Micron</td><td>829,440</td></tr><tr><td>MI500 (Arcadia)</td><td>24</td><td>4</td><td>96</td><td>48</td><td>16</td><td>768</td><td>HBM4e 12hi</td><td>Samsung/Micron</td><td>73,728</td></tr><tr><td>Venice CPU</td><td>270</td><td>25</td><td>6,750</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">AI ASIC (2027e)</td></tr><tr><td rowspan="4">Google</td><td>TPU v7p (Ironwood; AVGO)</td><td>13</td><td>16</td><td>208</td><td>24</td><td>8</td><td>192</td><td>HBM3e 8hi</td><td>Hynix/Samsung</td><td>39,936</td></tr><tr><td>TPU 

[中间内容因长度限制已省略]

udeng Precision (3680.TWO)</td><td>O (11/25/2025)</td><td>NT$537.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$166.30</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$735.50</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$329.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb113.92</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$4,535.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb768.98</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$454.50</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb747.49</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb87.70</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,430.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb137.16</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$645.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$77.85</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,490.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$170.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$186.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$522.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$194.70</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb80.80</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$166.00</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb101.30</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb47.04</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$72.10</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb86.09</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$27.88</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb163.37</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb138.80</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb81.91</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb35.38</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb132.96</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,050.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,425.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$18,505.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$122.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb122.50</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb640.99</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$172.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$408.20</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb258.00</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$544.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$194.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$661.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$78.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$863.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.06</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$211.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$108.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$220.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb161.79</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb596.01</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,170.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$685.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$18.54</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,810.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,680.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$336.90</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
