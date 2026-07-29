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
# LandMark (3081.TWO): 3Q26 QoQ growth on 800G / 1.6T SiPh ramp up; Capacity expansion to capture the strong demand; Buy

Landmark June revenues were up 128% YoY / 4% MoM to NT\$421m, or 1% higher than our previous estimates, resulting in strong 2Q26 revenues at NT\$1.2bn (+121% YoY, +35% QoQ), reflecting strong demand on 800G / 1.6T SiPh optical modules, better InP substrate supply, and Landmark's capacity expansion. With continuous capex spending and rising penetration of Silicon Photonics (SiPh), we expect to see sequential MoM growth in Jul to Sep at 5% / 5% / 7% MoM to NT\$442m / 464m / 498m. Maintain Buy.

Capacity expansion: In mid June, Landmark announced the company has obtained equipment from Aixtron with total value at \~NT\$837m, supporting its capacity expansion across InP epiwafer and CW lasers. The company also notes its plan of equipment procurement at NT\$3bn is approved by the board, supporting the company to further capture the strong demand on SiPh optical modules.

Allen Chang
+852-2978-2930 |
allen.k.chang@gs.com
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Exhibit 1: We expect Landmark July 2026E revenues to grow 144% YoY to NT\$442m
Landmark monthly/ quarterly revenues

<table><tr><td></td><td>Apr 2026</td><td>May 2026</td><td>Jun 2026</td><td>Jul 2026E</td><td>Aug 2026E</td><td>Sep 2026E</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td></tr><tr><td>Revenues (NT$m)</td><td>395</td><td>405</td><td>421</td><td>442</td><td>464</td><td>498</td><td>642</td><td>904</td><td>1,221</td><td>1,403</td></tr><tr><td>YoY</td><td>115%</td><td>119%</td><td>128%</td><td>144%</td><td>150%</td><td>167%</td><td>122%</td><td>99%</td><td>121%</td><td>154%</td></tr><tr><td>MoM/QoQ</td><td>15%</td><td>3%</td><td>4%</td><td>5%</td><td>5%</td><td>7%</td><td>16%</td><td>41%</td><td>35%</td><td>15%</td></tr><tr><td>GS estimates (NT$m)</td><td>347</td><td>361</td><td>416</td><td></td><td></td><td></td><td>629</td><td>875</td><td>1,123</td><td></td></tr><tr><td>Actual vs. GS</td><td>14%</td><td>12%</td><td>1%</td><td></td><td></td><td></td><td>2%</td><td>3%</td><td>9%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Earnings revision: We factor in Landmark 2Q26 revenues and revise up 2026E earnings by 1% mainly on higher revenues of 800G/ 1.6T SiPh CW laser, supported by strong demand and improving supply. We keep 2027-29E unchanged.

Exhibit 2: Earnings revision

<table><tr><td rowspan="2">NT$m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td></tr><tr><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td><td>Old</td><td>New</td><td>Diff %</td></tr><tr><td>Revenues</td><td>4,992</td><td>5,047</td><td>1%</td><td>9,370</td><td>9,365</td><td>0%</td><td>14,719</td><td>14,713</td><td>0%</td><td>22,078</td><td>22,080</td><td>0%</td></tr><tr><td>GP</td><td>2,746</td><td>2,778</td><td>1%</td><td>5,234</td><td>5,232</td><td>0%</td><td>8,387</td><td>8,384</td><td>0%</td><td>12,580</td><td>12,582</td><td>0%</td></tr><tr><td>OP</td><td>2,043</td><td>2,075</td><td>2%</td><td>4,370</td><td>4,367</td><td>0%</td><td>7,211</td><td>7,209</td><td>0%</td><td>10,839</td><td>10,840</td><td>0%</td></tr><tr><td>Pre-tax income</td><td>2,138</td><td>2,169</td><td>1%</td><td>4,467</td><td>4,464</td><td>0%</td><td>7,342</td><td>7,340</td><td>0%</td><td>10,970</td><td>10,971</td><td>0%</td></tr><tr><td>Net income</td><td>1,710</td><td>1,736</td><td>1%</td><td>3,573</td><td>3,571</td><td>0%</td><td>5,873</td><td>5,872</td><td>0%</td><td>8,776</td><td>8,777</td><td>0%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>GM</td><td>55.0%</td><td>55.0%</td><td>0ppts</td><td>55.9%</td><td>55.9%</td><td>0ppts</td><td>57.0%</td><td>57.0%</td><td>0ppts</td><td>57.0%</td><td>57.0%</td><td>0ppts</td></tr><tr><td>OPM</td><td>40.9%</td><td>41.1%</td><td>0.2ppts</td><td>46.6%</td><td>46.6%</td><td>0ppts</td><td>49.0%</td><td>49.0%</td><td>0ppts</td><td>49.1%</td><td>49.1%</td><td>0ppts</td></tr><tr><td>NM</td><td>34.3%</td><td>34.4%</td><td>0.1ppts</td><td>38.1%</td><td>38.1%</td><td>0ppts</td><td>39.9%</td><td>39.9%</td><td>0ppts</td><td>39.7%</td><td>39.8%</td><td>0ppts</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We employ a discounted P/E methodology (unchanged) and apply a 61.0x (unchanged) target P/E multiple on our 2029E EPS, discounted back to 2027E, at a COE of 10.5% (beta 1.7x, risk free rate 1.6%, and market risk premium at 5.1% - unchanged). Our target P/E multiple of 61.0x is derived from the PEG&M ratio of peers (unchanged) in the photonics supply chain, reflecting an industry re-rating of product mix upgrade and rising demand on optical solution. Consequently, our 12-month target price is now NT\$4,307.00 (vs. previously at NT\$4,307.27). The implied 2028E P/E at 75x is between company's avg. P/E at 56x and avg. +1 P/E at 82x. Maintain Buy.

Exhibit 3: Landmark discounted P/E

<table><tr><td>(NT$ mn)</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td><td>2032E</td></tr><tr><td>Milestones</td><td colspan="3">5G infrastructure cycle</td><td colspan="3">SiPh in AI data center</td><td colspan="5">CPO</td></tr><tr><td>SiPh Rev contribution</td><td>13%</td><td>35%</td><td>42%</td><td>70%</td><td>87%</td><td>93%</td><td>96%</td><td>96%</td><td>96%</td><td>96%</td><td>96%</td></tr><tr><td>SiPh GP contribution</td><td>15%</td><td>25%</td><td>41%</td><td>71%</td><td>90%</td><td>95%</td><td>97%</td><td>97%</td><td>97%</td><td>97%</td><td>97%</td></tr><tr><td>Revenue</td><td>2,381</td><td>1,056</td><td>1,208</td><td>2,203</td><td>5,047</td><td>9,365</td><td>14,713</td><td>22,080</td><td>32,915</td><td>46,081</td><td>63,592</td></tr><tr><td>YoY</td><td>27%</td><td>-56%</td><td>14%</td><td>82%</td><td>129%</td><td>86%</td><td>57%</td><td>50%</td><td>49%</td><td>40%</td><td>38%</td></tr><tr><td>Gross profit</td><td>759</td><td>138</td><td>239</td><td>941</td><td>2,778</td><td>5,232</td><td>8,384</td><td>12,582</td><td>18,756</td><td>26,258</td><td>36,300</td></tr><tr><td>Gross margin</td><td>31.9%</td><td>13.1%</td><td>19.8%</td><td>42.7%</td><td>55.0%</td><td>55.9%</td><td>57.0%</td><td>57.0%</td><td>57.0%</td><td>57.0%</td><td>57.1%</td></tr><tr><td>Operating profit</td><td>335</td><td>-280</td><td>-112</td><td>508</td><td>2,075</td><td>4,367</td><td>7,209</td><td>10,840</td><td>16,193</td><td>22,762</td><td>31,666</td></tr><tr><td>YoY</td><td>-18%</td><td>-184%</td><td>-60%</td><td>-555%</td><td>308%</td><td>111%</td><td>65%</td><td>50%</td><td>49%</td><td>41%</td><td>39%</td></tr><tr><td>Operating margin</td><td>14%</td><td>-27%</td><td>-9%</td><td>23%</td><td>41%</td><td>47%</td><td>49%</td><td>49%</td><td>49%</td><td>49%</td><td>50%</td></tr><tr><td>Pre-tax profit</td><td>378</td><td>-264</td><td>-68</td><td>525</td><td>2,169</td><td>4,464</td><td>7,340</td><td>10,971</td><td>16,323</td><td>22,893</td><td>31,797</td></tr><tr><td>Net profit</td><td>330</td><td>-212</td><td>-55</td><td>411</td><td>1,736</td><td>3,571</td><td>5,872</td><td>8,777</td><td>13,059</td><td>18,314</td><td>25,437</td></tr><tr><td>EPS (NT$, diluted)</td><td>3.26</td><td>-2.10</td><td>-0.54</td><td>4.21</td><td>17.06</td><td>35.10</td><td>57.71</td><td>86.26</td><td>128.34</td><td>180.00</td><td>250.00</td></tr><tr><td>YoY</td><td>-2%</td><td>n.a.</td><td>n.a.</td><td>n.a.</td><td>322%</td><td>106%</td><td>64%</td><td>49%</td><td>49%</td><td>40%</td><td>39%</td></tr><tr><td>TP implied P/E</td><td></td><td></td><td></td><td></td><td>253</td><td>123</td><td>75</td><td>50</td><td>34</td><td>24</td><td>17</td></tr></table>

<table><tr><td>2029E target P/E</td><td>61.0</td></tr><tr><td>Target multiple x EPS</td><td>5,262</td></tr><tr><td>Discounted back to 2027; TP (NTD)</td><td>4,307.0</td></tr><tr><td>Implied 2027 P/E</td><td>123</td></tr></table>

<table><tr><td colspan="2">COE assumption</td></tr><tr><td>Beta</td><td>1.7</td></tr><tr><td>Risk free</td><td>1.6%</td></tr><tr><td>Market risk premium</td><td>5.1%</td></tr><tr><td>COE</td><td>10.5%</td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 4: Landmark 12M forward P/E  
![](images/748ea0b716260a3afd2bdeae6766b3e5c29f6ea728f6a8c70e0ffbd185795e2c.jpg)  
Source: Eikon Datastream

Exhibit 5: The target P/E is derived from peers correlation between P/E to sum of NI YoY and OPM

<table><tr><td>Valuatoin</td><td>2029E P/E</td><td>2030 NI YoY</td><td>2030 OPM</td><td>PEG&amp;M</td></tr><tr><td>Landmark</td><td>61</td><td>49%</td><td>49%</td><td>0.62</td></tr><tr><td>Peers</td><td>2026E P/E</td><td>2027 NI YoY</td><td>2027 OPM</td><td>PEG&amp;M</td></tr><tr><td>Mitac</td><td>11</td><td>16%</td><td>5%</td><td>0.5</td></tr><tr><td>HG Tech</td><td>34</td><td>31%</td><td>14%</td><td>0.8</td></tr><tr><td>Shennan</td><td>35</td><td>47%</td><td>19%</td><td>0.5</td></tr><tr><td>Avg.</td><td>34</td><td>32%</td><td>25%</td><td>0.62</td></tr></table>

Exhibit 6: Landmark P&L Summary

<table><tr><td>NT$ mn</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td></tr><tr><td colspan="15">Income statement</td></tr><tr><td>Revenue</td><td>1,056</td><td>1,208</td><td>2,203</td><td>5,047</td><td>9,365</td><td>14,713</td><td>455</td><td>553</td><td>553</td><td>642</td><td>904</td><td>1,221</td><td>1,403</td><td>1,518</td></tr><tr><td>Gross profit</td><td>138</td><td>239</td><td>941</td><td>2,778</td><td>5,232</td><td>8,384</td><td>147</td><td>240</td><td>241</td><td>313</td><td>495</td><td>670</td><td>773</td><td>839</td></tr><tr><td>OP income</td><td>(280)</td><td>(112)</td><td>508</td><td>2,075</td><td>4,367</td><td>7,209</td><td>45</td><td>150</td><td>105</td><td>209</td><td>373</td><td>516</td><td>529</td><td>657</td></tr><tr><td>Pretax income</td><td>(264)</td><td>(68)</td><td>525</td><td>2,169</td><td>4,464</td><td>7,340</td><td>53</td><td>121</td><td>124</td><td>227</td><td>397</td><td>539</td><td>553</td><td>681</td></tr><tr><td>Net income</td><td>(212)</td><td>(55)</td><td>411</td><td>1,736</td><td>3,571</td><td>5,872</td><td>42</td><td>97</td><td>99</td><td>190</td><td>318</td><td>432</td><td>442</td><td>544</td></tr><tr><td>EPS (NT$)</td><td>(2.10)</td><td>(0.54)</td><td>4.21</td><td>17.06</td><td>35.10</td><td>57.71</td><td>0.42</td><td>0.95</td><td>0.97</td><td>1.87</td><td>3.12</td><td>4.24</td><td>4.34</td><td>5.35</td></tr><tr><td colspan="15">Margins</td></tr><tr><td>Gross margin</td><td>13.1%</td><td>19.8%</td><td>42.7%</td><td>55.0%</td><td>55.9%</td><td>57.0%</td><td>32.3%</td><td>43.3%</td><td>43.6%</td><td>48.7%</td><td>54.8%</td><td>54.9%</td><td>55.1%</td><td>55.3%</td></tr><tr><td>Operating margin</td><td>-26.5%</td><td>-9.3%</td><td>23.1%</td><td>41.1%</td><td>46.6%</td><td>49.0%</td><td>9.8%</td><td>27.0%</td><td>19.0%</td><td>32.5%</td><td>41.3%</td><td>42.2%</td><td>37.7%</td><td>43.3%</td></tr><tr><td>Net margin</td><td>-20.0%</td><td>-4.5%</td><td>18.7%</td><td>34.4%</td><td>38.1%</td><td>39.9%</td><td>9.3%</td><td>17.5%</td><td>17.9%</td><td>29.6%</td><td>35.1%</td><td>35.3%</td><td>31.5%</td><td>35.9%</td></tr><tr><td colspan="15">YoY</td></tr><tr><td>Revenue</td><td>-56%</td><td>14%</td><td>82%</td><td>129%</td><td>86%</td><td>57%</td><td>40%</td><td>103%</td><td>71%</td><td>122%</td><td>99%</td><td>121%</td><td>154%</td><td>136%</td></tr><tr><td>Gross profit</td><td>-82%</td><td>73%</td><td>294%</td><td>195%</td><td>88%</td><td>60%</td><td>638%</td><td>503%</td><td>171%</td><td>247%</td><td>237%</td><td>180%</td><td>221%</td><td>168%</td></tr><tr><td>OP income</td><td>na</td><td>na</td><td>na</td><td>308%</td><td>111%</td><td>65%</td><td>18%</td><td>na</td><td>1176%</td><td>na</td><td>734%</td><td>245%</td><td>404%</td><td>214%</td></tr><tr><td>Net income</td><td>na</td><td>na</td><td>na</td><td>322%</td><td>106%</td><td>64%</td><td>20%</td><td>na</td><td>1139%</td><td>2233%</td><td>651%</td><td>346%</td><td>346%</td><td>186%</td></tr><tr><td colspan="15">QoQ</td></tr><tr><td>Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td>57%</td><td>22%</td><td>0%</td><td>16%</td><td>41%</td><td>35%</td><td>15%</td><td>8%</td></tr><tr><td>Gross profit</td><td></td><td></td><td></td><td></td><td></td><td></td><td>63%</td><td>63%</td><td>1%</td><td>30%</td><td>58%</td><td>35%</td><td>15%</td><td>8%</td></tr><tr><td>OP income</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-849%</td><td>234%</td><td>-30%</td><td>99%</td><td>79%</td><td>38%</td><td>3%</td><td>24%</td></tr><tr><td>Net income</td><td></td><td></td><td></td><td></td><td></td><td></td><td>418%</td><td>129%</td><td>2%</td><td>92%</td><td>67%</td><td>36%</td><td>2%</td><td>23%</td></tr><tr><td>EBITDA</td><td></td><td></td><td></td><td></td><td></td><td></td><td>55%</td><td>81%</td><td>-21%</td><td>69%</td><td>52%</td><td>31%</td><td>2%</td><td>21%</td></tr></table>

Source: Company data, GS Global Investment Research

Price Target Risks and Methodology - LandMark Optoelectronics Corp.

Valuation: We employ a discounted P/E methodology, applying a 61x target P/E multiple on our 2029E EPS, then discount it back to 2027E at a COE of 10.5% (beta 1.7x, risk free rate 1.6% and market risk premium at 5.1%), to derive our 12-month target price of NT\$4,307. Our target P/E multiple is based on the same PEG&M ratio as peers in the photonics supply chain. We are Buy-rated on LandMark.

Key risk: Slower-than-expected SiPh penetration; stronger-than-expected competition; Integrated Device Manufacturers (IDMs) offering Epitaxial (EPI) wafers in-house.

<table><tr><td>3081.TWO</td><td>12m Price Target: NT$4,307.00</td><td colspan="2">Price: NT$1,805.00</td><td colspan="2">Upside: 138.6%</td></tr><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="9">Market cap: NT$175.4bn / $5.4bnEnterprise value:NT$173.5bn / $5.4bn3m ADTV: NT$6.4bn / $201.2mnTaiwanGreater China TechnologyM&amp;A Rank: 3Leases incl. in net debt &amp; EV?: No</td><td>Revenue (NT$ mn) New</td><td>2,202.8</td><td>5,047.0</td><td>9,364.7</td><td>14,713.3</td></tr><tr><td>Revenue (NT$ mn) Old</td><td>2,202.8</td><td>4,991.6</td><td>9,370.4</td><td>14,719.0</td></tr><tr><td>EBITDA (NT$ mn)</td><td>842.9</td><td>2,442.2</td><td>4,756.7</td><td>7,617.8</td></tr><tr><td>EPS (NT$) New</td><td>4.21</td><td>17.06</td><td>35.10</td><td>57.71</td></tr><tr><td>EPS (NT$) Old</td><td>4.21</td><td>16.81</td><td>35.12</td><td>57.73</td></tr><tr><td>P/E (X)</td><td>85.8</td><td>105.8</td><td>51.4</td><td>31.3</td></tr><tr><td>P/B (X)</td><td>9.1</td><td>43.4</td><td>37.1</td><td>29.9</td></tr><tr><td>Dividend yield (%)</td><td>0.9</td><td>0.8</td><td>1.6</td><td>2.6</td></tr><tr><td>CROCI (%)</td><td>10.8</td><td>31.1</td><td>61.5</td><td>107.1</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (NT$)</td><td>3.12</td><td>4.24</td><td>4.34</td><td>5.35</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 27 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Ting Song, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Ting Song GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assig

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
