你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
July 8, 2026 06:45 AM GMT

Asia-Pacific Technology | Asia Pacific

# AI Supply Chain: Further Updates on 2027 CoWoS Allocation and ASIC Dynamics

AMD's 2027 CoWoS allocation remains at 240k for now, with combined MI455/MI450 shipments at 1.5mn. TPU MP timing skews toward 4Q. Blackwell chip "inventory" turned out to be a supply chain buffer and will be fully consumed by 2026. We expect \~7mn Rubin chips and 90k NVL72 racks in 2027.

Further updates on our AMD CoWoS allocation: We published our preliminary 2027 CoWoS allocation last week and received many investor queries on AMD's (covered by Joe Moore) CoWoS number. Some MI300 series and upcoming MI500 production will still run in 2027. However, the MI400 series will come in two versions: (1) MI455: the standard version with 2 compute dies and 12 HBM4 12hi, paired with the Helios rack (18 CPUs and 72 GPUs), with Microsoft, AWS, and Oracle as key customers; (2) MI450: a Meta-customized, half-size chip paired with 1 compute die and 6 HBM4 12hi (9 CPUs and 36 GPUs). We still expect AMD's 2027 CoWoS at 240k, but do not rule out execution risk, given its prior record of trimming CoWoS bookings in 2026. 2027 chip shipments: MI455 1mn and MI450 500k. For CPU, Venice is AMD's first CPU adopting CoWoS, and we see CoW production concentrated in OSATs—ASE/SPIL, Amkor, and Powertech. Total CPU chip shipments could reach 5.7–6mn units in 2027 vs. 1mn in 2026.

Google TPU progress update: Our industry checks suggest KYEC's 3Q26 revenue could grow close to 10% Q/Q, below our initial 15% Q/Q expectation, mainly due to slight Rubin and Sunfish delays and MediaTek's smartphone SoC order trim. We do see Sunfish shipments largely in 4Q, with full-year volume at 960k units. With Sunfish and Rubin pushed out, we believe more revenue will concentrate in 4Q26 or 1Q27 without order cuts. Many investors asked about Zebrafish delays; we still see its 4Q26 volume ramp unchanged.

Comparing the Blackwell chip/rack shipment and Rubin chip/rack shipment: We provided a chip vs. rack shipment comparison for Blackwell in last June's AI tracker. We now include HGX (8-GPU per server) in our chip consumption model, and treat 9 HGX servers as equivalent to one NVL72 rack. We expect 5.4mn Blackwell units in 2026, and chip volume could meet Grace Blackwell NVL72 demand by 2H26. Our latest checks also suggest close to 7mn Rubin and Rubin Ultra units in 2027, while total Rubin NVL72 server racks could reach 90k in 2027 (Exhibit 12). All Blackwell chip "inventory" turned out to be a supply-chain buffer and will be fully consumed by 2026, so we see no need to worry about inventory issues. We think Rubin will follow a similar pattern.

(continued on the next page)

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

Tiffany Yeh
Equity Analyst
Tiffany.Yeh@morganstanley.com +886 2 7712-3032

Lucas Wang
Research Associate
Lucas.Wang@morganstanley.com +886 2 2730-2875

Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

<table><tr><td colspan="2">Henry Zhao</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Henry.Zhao@morganstanley.com</td><td>+852 2239-7731</td></tr></table>

![](images/665af0b2f2a11c200f6c4fefea39123ff15ffbb6ddce31b21705523c0a95f13b.jpg)  
Asia Summer School 2026

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Meta ASIC progress update: On the other hand, Meta cancelled its original 2nm ASIC Olympus earlier this year; a new 2nm chip, code-named Apollo, succeeds it. Broadcom (covered by Joe Moore) will continue design services, with mass production in 1Q28. For GUC, we think it is likely to win one of the Meta ASIC projects led by the Rivos team, possibly a side project from the usual MTIA product line. The AI ASIC targets tape-out in 1H27, with potential CoWoS out by 2027 year-end or 1H28.

# Introducing Our 2027 Global CoWoS Capacity Update And Comparing Chip Shipments vs. Racks

We published our preliminary 2027 CoWoS allocation last week and received lots of investor queries around AMD's (covered by Joe Moore) CoWoS number. There will still be some production of the MI300 series and the upcoming MI500 in 2027.

However, for the MI400 series, there will be two versions coming: 1) MI455: the standard version, including 2 compute dies and 12 HBM4 12hi, pairing with the Helios rack (18 CPUs and 72 GPUs), with key customers being Microsoft, AWS and Oracle; 2) MI450:

customized version for Meta, with the chip being half size pairing with 1 compute die and 6 HBM4 12hi (9 CPUs and 36 GPUs) (see Exhibit 1). We still expect AMD's CoWoS to be 240k in 2027, but do not rule out execution risk, given its prior record of trimming CoWoS bookings in 2026. We estimate chip shipments in 2027 will be 1mn for MI455 and 500k for MI450.

For CPU, Venice is AMD's first CPU to adopt CoWoS, and we see CoW production concentrating in OSATs, including ASE/SPIL, Amkor and Powertech. We expect total chip shipments of 5.7-6mn units in 2027 vs. 1mn units in 2026.

Exhibit 1: AI HBM consumption: up to 50bn Gb in 2027

<table><tr><td colspan="5">General assumptions</td><td colspan="6">HBM assumptions</td></tr><tr><td>AI chip vendor</td><td>Product name</td><td>CoWoS capacity allocation (k wafers)</td><td>Chips per CoWoS wafer</td><td>Implied shipments (k)</td><td>HBM chip density (GB)</td><td>HBM chip units</td><td>Total HBM size (GB)</td><td>HBM generation</td><td>HBM vendor</td><td>Total HBM demand (k GB)</td></tr><tr><td colspan="11">AI GPU (2027e)</td></tr><tr><td rowspan="4">NVIDIA</td><td>B300</td><td>40</td><td>14</td><td>560</td><td>36</td><td>8</td><td>288</td><td>HBM3e 12hi</td><td>Hynix/Micron</td><td>161,280</td></tr><tr><td>Vera CPU</td><td>250</td><td>23</td><td>5,750</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rubin R200</td><td>740</td><td>8</td><td>5,920</td><td>36</td><td>8</td><td>288</td><td>HBM4 12hi</td><td>Hynix/Micron/Samsung</td><td>1,704,960</td></tr><tr><td>Rubin Ultra</td><td>130</td><td>8</td><td>1,040</td><td>48</td><td>8</td><td>384</td><td>HBM4e 12hi</td><td>Hynix/Micron/Samsung</td><td>399,360</td></tr><tr><td rowspan="5">AMD</td><td>MI350 series</td><td>24</td><td>12</td><td>288</td><td>36</td><td>8</td><td>288</td><td>HBM3e 12hi</td><td>Samsung/Micron</td><td>82,944</td></tr><tr><td>MI455</td><td>157</td><td>7</td><td>1,099</td><td>36</td><td>12</td><td>432</td><td>HBM4 12hi</td><td>Samsung/Micron</td><td>474,768</td></tr><tr><td>MI450 (for Meta)</td><td>35</td><td>14</td><td>490</td><td>36</td><td>6</td><td>216</td><td>HBM4 12hi</td><td>Samsung/Micron</td><td>105,840</td></tr><tr><td>MI500 (Arcadia)</td><td>24</td><td>4</td><td>96</td><td>48</td><td>16</td><td>768</td><td>HBM4e 12hi</td><td>Samsung/Micron</td><td>73,728</td></tr><tr><td>Venice CPU</td><td>270</td><td>21</td><td>5,670</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">AI ASIC (2027e)</td></tr><tr><td rowspan="4">Google</td><td>TPU v7p (Ironwood; AVGO)</td><td>13</td><td>16</td><td>208</td><td>24</td><td>8</td><td>192</td><td>HBM3e 8hi</td><td>Hynix/Samsung</td><td>39,936</td></tr><tr><td>TPU v8i (Sunfish; AVGO)</td><td>330</td><td>12</td><td>3,960</td><td>36</td><td>8</td><td>288</td><td>HBM3e 12hi</td><td>Samsung/Hynix/Micron</td><td>1,140,480</td></tr><tr><td>TPU v8t (Zebrafish; MediaTek)</td><td>180</td><td>20</td><td>3,600</td><td>36</td><td>6</td><td>216</td><td>HBM3e 12hi</td><td>Samsung/Hynix/Micron</td><td>777,600</td></tr><tr><td>TPU v9 (Humufish; MediaTek)</td><td></td><td></td><td>400</td><td>48</td><td>12</td><td>576</td><td>HBM4e 12hi</td><td>Samsung/Hynix/Micron</td><td>230,400</td></tr><tr><td>AWS</td><td>Trainium 3</td><td>140</td><td>17</td><td>2,380</td><td>36</td><td>4</td><td>144</td><td>HBM3e 12hi</td><td>Hynix/Samsung/Micron</td><td>342,720</td></tr><tr><td>GUC&#x27;s customers</td><td></td><td>60</td><td>20</td><td>1,200</td><td>24</td><td>6</td><td>144</td><td>HBM3e 8hi</td><td>Samsung?</td><td>172,800</td></tr><tr><td>Microsoft</td><td>Maia 300</td><td>50</td><td>11</td><td>550</td><td>36</td><td>8</td><td>288</td><td>HBM4 12hi</td><td>Samsung</td><td>158,400</td></tr><tr><td>Meta</td><td>MTIA 3 (Iris)</td><td>55</td><td>10</td><td>550</td><td>36</td><td>8</td><td>288</td><td>HBM3e 12hi</td><td>Samsung/Hynix/Micron</td><td>158,400</td></tr><tr><td>Others</td><td></td><td>18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total</td><td></td><td>2,664</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6,077,256</td></tr></table>

Exhibit 2: AI wafer consumption: at least US\$47bn in 2027

<table><tr><td>AI chip vendor</td><td>Product name</td><td>CoWoS capacity allocation (k wafers)</td><td>Chips per CoWoS wafer</td><td>Implied shipments (k)</td><td>Compute die size</td><td>Geometry</td><td>Compute die units</td><td>Wafer consumption (k wafers)</td><td>Wafer price (US$)</td><td>Wafer revenue TAM (US$ mn)</td></tr><tr><td colspan="11">AI GPU (2027e)</td></tr><tr><td rowspan="4">NVIDIA</td><td>B300</td><td>40</td><td>14</td><td>560</td><td>850</td><td>4nm</td><td>2</td><td>44</td><td>23,042</td><td>1,024</td></tr><tr><td>Vera CPU</td><td>250</td><td>23</td><td>5,750</td><td>850</td><td>3nm</td><td>1</td><td>228</td><td>27,300</td><td>6,229</td></tr><tr><td>Rubin R200</td><td>740</td><td>8</td><td>5,920</td><td>850</td><td>3nm</td><td>2</td><td>470</td><td>27,300</td><td>12,827</td></tr><tr><td>Rubin Ultra</td><td>130</td><td>8</td><td>1,040</td><td>850</td><td>3nm</td><td>2</td><td>58</td><td>27,300</td><td>1,588</td></tr><tr><td rowspan="5">AMD</td><td>MI350 series</td><td>24</td><td>12</td><td>288</td><td>110</td><td>3nm</td><td>8</td><td>8</td><td>27,300</td><td>229</td></tr><tr><td>MI455</td><td>157</td><td>7</td><td>1,099</td><td>850</td><td>2nm</td><td>2</td><td>13</td><td>30,000</td><td>400</td></tr><tr><td>MI450 (for Meta)</td><td>35</td><td>14</td><td>490</td><td>850</td><td>2nm</td><td>1</td><td>3</td><td>30,000</td><td>89</td></tr><tr><td>MI500 (Arcadia)</td><td>24</td><td>4</td><td>96</td><td></td><td>2nm</td><td></td><td></td><td>30,000</td><td></td></tr><tr><td>Venice CPU</td><td>270</td><td>21</td><td>5,670</td><td></td><td>2nm</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">AI ASIC (2027e)</td></tr><tr><td rowspan="4">Google</td><td>TPU v7p (Ironwood; AVGO)</td><td>13</td><td>16</td><td>208</td><td>700</td><td>3nm</td><td>2</td><td>14</td><td>27,300</td><td>371</td></tr><tr><td>TPU v8i (Sunfish; AVGO)</td><td>330</td><td>12</td><td>3,960</td><td>800</td><td>3nm</td><td>2</td><td>296</td><td>27,300</td><td>8,075</td></tr><tr><td>TPU v8t (Zebrafish; MediaTek)</td><td>180</td><td>20</td><td>3,600</td><td>800</td><td>3nm</td><td>2</td><td>269</td><td>27,300</td><td>7,341</td></tr><tr><td>TPU v9 (Humufish; MediaTek)</td><td></td><td></td><td>400</td><td>850</td><td>2nm</td><td>2</td><td>32</td><td>27,300</td><td>867</td></tr><tr><td>AWS</td><td>Trainium 3</td><td>140</td><td>17</td><td>2,380</td><td>700</td><td>3nm</td><td>2</td><td>127</td><td>27,300</td><td>3,465</td></tr><tr><td>GUC&#x27;s customers</td><td></td><td>60</td><td>20</td><td>1,200</td><td>645</td><td>4nm</td><td>1</td><td>29</td><td>23,042</td><td>674</td></tr><tr><td>Microsoft</td><td>Maia 300</td><td>50</td><td>11</td><td>550</td><td>850</td><td>2nm</td><td>1</td><td>29.1</td><td>30,000</td><td>873</td></tr><tr><td>Meta</td><td>MTIA 3 (Iris)</td><td>55</td><td>10</td><td>550</td><td>850</td><td>3nm</td><td>2</td><td>44</td><td>27,300</td><td>1,192</td></tr><tr><td>Others</td><td></td><td>18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Total</td><td></td><td>2,664</td><td></td><td></td><td></td><td></td><td></td><td>1,700</td><td></td><td>46,208</td></tr></table>

Source: Company data, MS (e) estimates. Note: Estimates are compiled using our Asian supply chain checks.

Exhibit 3: CoWoS allocation breakdown by CoW vendor

<table><tr><td>(k wafer)</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2023</td><td>2024</td><td>2025e</td><td>2026e</td><td>2027e</td></tr><tr><td>NVIDIA</td><td>53</td><td>200</td><td>425</td><td>780</td><td>1,222</td><td>45%</td><td>54%</td><td>62%</td><td>56%</td><td>45%</td></tr><tr><td>TSMC</td><td></td><td></td><td>390</td><td>680</td><td>1,090</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>390</td><td>650</td><td>910</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>0</td><td>20</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>0</td><td>10</td><td>130</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Non-TSMC</td><td></td><td></td><td>35</td><td>100</td><td>132</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td>35</td><td>100</td><td>132</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>20</td><td>20</td><td>12</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>15</td><td>80</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Broadcom</td><td>23</td><td>68</td><td>85</td><td>300</td><td>484</td><td>20%</td><td>18%</td><td>12%</td><td>22%</td><td>18%</td></tr><tr><td>TSMC</td><td></td><td></td><td>83</td><td>260</td><td>420</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>15</td><td>55</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>83</td><td>245</td><td>365</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>2</td><td>30</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\dagger$ </td><td></td><td></td><td>0</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>2</td><td>30</td><td>40</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td></td><td>10</td><td>24</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>10</td><td>24</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AMD</td><td>7</td><td>40</td><td>60</td><td>130</td><td>530</td><td>6%</td><td>11%</td><td>9%</td><td>9%</td><td>20%</td></tr><tr><td>TSMC</td><td></td><td></td><td>60</td><td>80</td><td>240</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>70</td><td>230</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td>60</td><td>10</td><td>10</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td>0</td><td>50</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td>0</td><td>50</td><td>170</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Amkor</td><td></td><td></td><td></td><td>0</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td></td><td>0</td><td>120</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Xilinx</td><td>3</td><td>10</td><td>10</td><td>10</td><td>10</td><td>3%</td><td>3%</td><td>1%</td><td>1%</td><td>0%</td></tr><tr><td>MediaTek</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td>3%</td><td>7%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-S</td><td></td><td></td><td></td><td>40</td><td>180</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AWS/Annapurna</td><td></td><td></td><td>60</td><td>62</td><td>90</td><td></td><td></td><td></td><td>4%</td><td>3%</td></tr><tr><td>TSMC</td><td></td><td></td><td>60</td><td>32</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>60</td><td>32</td><td>54</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td></td><td>30</td><td>36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td></td><td>30</td><td>36</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AWS/Alchip</td><td>9</td><td>16</td><td>5</td><td>26</td><td>36</td><td>8%</td><td>4%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td>Intel Habana</td><td>0</td><td>7</td><td>9</td><td>0</td><td>0</td><td>0%</td><td>2%</td><td>1%</td><td>0%</td><td>0%</td></tr><tr><td>Marvell</td><td>1</td><td>18</td><td>15</td><td>17</td><td>64</td><td>1%</td><td>5%</td><td>2%</td><td>1%</td><td>2%</td></tr><tr><td>TSMC</td><td></td><td></td><td></td><td>5</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-L</td><td></td><td></td><td></td><td>5</td><td>50</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td>15</td><td>0</td><td>0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASE/SPIL</td><td></td><td></td><td></td><td>12</td><td>14</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CoWoS-R</td><td></td><td></td><td></td><td>12</td><td>14</td><td></td><td

[中间内容因长度限制已省略]

or Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$180.00</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$539.50</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$305.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb91.42</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$3,995.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb833.99</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$396.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb806.39</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb99.46</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,145.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb129.10</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$551.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$73.45</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,465.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$163.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$175.00</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$409.50</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$190.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb87.30</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$186.00</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb119.39</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb47.29</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb342.60</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$54.95</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb100.99</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$30.40</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb146.00</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb128.45</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb82.00</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb29.19</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb134.90</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$926.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,525.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$14,415.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$114.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb116.00</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb620.00</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$138.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$333.60</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb253.20</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$544.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$158.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$650.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$71.20</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$817.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb56.56</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$168.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$105.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$210.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb169.17</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb627.90</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$974.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$587.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$14.05</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,055.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,310.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$294.90</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$7,705.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
