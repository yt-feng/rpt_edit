你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

<table><tr><td>(k wafer)</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2023</td><td>2024</td><td>2025e</td><td>2026e</td><td>2027e</td></tr><tr><td>NVIDIA</td><td>53</td><td>200</td><td>425</td><td>780</td><td>1,222</td><td>45%</td><td>54%</td><td>62%</td><td>56%</td><td>45%</td></tr><tr><td>TSMC</td><td></td><td></td><td>390</td><td>680</td><td>1,090</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>390</td><td>650</td><td>910</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>0</td><td>20</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>0</td><td>10</td><td>130</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non-TSMC</td><td></td><td></td><td>35</td><td>100</td><td>132</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td>35</td><td>100</td><td>132</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>20</td><td>20</td><td>12</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>15</td><td>80</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Broadcom</td><td>23</td><td>68</td><td>85</td><td>300</td><td>484</td><td>20%</td><td>18%</td><td>12%</td><td>22%</td><td>18%</td></tr><tr><td>TSMC</td><td></td><td></td><td>83</td><td>260</td><td>420</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>15</td><td>55</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>83</td><td>245</td><td>365</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>2</td><td>30</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>2</td><td>30</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td></td><td>10</td><td>24</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>10</td><td>24</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AMD</td><td>7</td><td>40</td><td>60</td><td>130</td><td>530</td><td>6%</td><td>11%</td><td>9%</td><td>9%</td><td>20%</td></tr><tr><td>TSMC</td><td></td><td></td><td>60</td><td>80</td><td>240</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>70</td><td>230</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>60</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>0</td><td>50</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>50</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td></td><td>0</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>0</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Xilinx</td><td>3</td><td>10</td><td>10</td><td>10</td><td>10</td><td>3%</td><td>3%</td><td>1%</td><td>1%</td><td>0%</td></tr><tr><td>MediaTek</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td>3%</td><td>7%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AWS/Annapurna</td><td></td><td></td><td>60</td><td>62</td><td>90</td><td></td><td></td><td></td><td>4%</td><td>3%</td></tr><tr><td>TSMC</td><td></td><td></td><td>60</td><td>32</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>60</td><td>32</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td></td><td>30</td><td>36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td></td><td>30</td><td>36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AWS/Alchip</td><td>9</td><td>16</td><td>5</td><td>26</td><td>36</td><td>8%</td><td>4%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td>Intel Habana</td><td>0</td><td>7</td><td>9</td><td>0</td><td>0</td><td>0%</td><td>2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Marvell</td><td>1</td><td>18</td><td>15</td><td>17</td><td>64</td><td>1%</td><td>5%</td><td>2%</td><td>1%</td><td>2%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td>5</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td></td><td>5</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>15</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td></td><td>12</td><td>14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td></td><td>12</td><td>14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GUC</td><td>1</td><td>1</td><td>2</td><td>14</td><td>60</td><td>1%</td><td>0%</td><td>0%</td><td>1%</td><td>2%</td></tr><tr><td>Cisco</td><td></td><td>2</td><td>3</td><td>5</td><td>6</td><td></td><td>1%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Others</td><td>20</td><td>10</td><td>15</td><td>10</td><td>12</td><td>17%</td><td>3%</td><td>2%</td><td>1%</td><td>0%</td></tr><tr><td>Total demand</td

[中间内容因长度限制已省略]

grated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb87.70</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,430.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb137.16</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$645.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$77.85</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,490.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$170.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$186.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$522.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$194.70</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb80.80</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$166.00</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb101.30</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb47.04</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$72.10</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb86.09</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$27.88</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb163.37</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb138.80</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb81.91</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb35.38</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb132.96</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,050.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,425.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$18,505.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$122.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb122.50</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb640.99</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$172.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$408.20</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb258.00</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$544.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$194.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$661.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$78.60</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$863.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.06</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$211.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$108.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$220.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb161.79</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb596.01</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,170.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$685.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$18.54</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,810.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,680.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$336.90</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
