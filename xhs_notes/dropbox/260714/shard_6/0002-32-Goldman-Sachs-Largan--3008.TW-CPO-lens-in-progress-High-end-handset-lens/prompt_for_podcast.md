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
# Largan (3008.TW): CPO lens in progress; High-end handset lens to ramp up in 3Q26; Buy

We are positive on Largan and expect sequential revenue growth ahead following the slow season in 2Q26, driven by the ramp up of new models at its major smartphone brand customers and launches of China smartphone flagship models. We expect premium smartphone brands to expand market share under high memory costs, and Largan's focus on high-end lens would continue to support peer outperformance with GM expansion. On CPO, despite its small contribution in the near term, we view it as a new market that could allow Largan to benefit from strong end demand and fast specification migration, supporting long term growth and valuation re-rating. Maintain Buy.

Exhibit 1: Largan revenues by products  
![](images/c52bcf395537ad93165296a75daaa4c577236c8e52d71382f0f1ced3f13b41bc.jpg)  
Source: GS Global Investment Research

## Key takeaways from 2Q26 earnings call

1. CPO opportunities: Management highlights its focus on FA and glass-molding PMLA for FAU in CPO switches. On FA, Largan aims to start sampling in coming 2-3 weeks, with customers usually taking 2-4 weeks for qualification. Largan will enter mass production once qualification is passed. The company aims to complete the pilot line for FA in late 3Q26. Overall, management commented the mass production timeline could be at mid 2027 the earliest. Management highlights it currently has one project aiming for mass production (one-row FA), while other projects (e.g. two-row FA, multi-row FA) are still at an POC (proof of concept) stage. High-precision alignment is the company's key advantage, which Largan has developed active alignment and testing equipment in house, and aims to deliver high-precision FA even when the purchased V-grooves or fibers are not of perfect quality.

Verena Jeng +852-2978-1681 | verena.jeng@gs.com GS (Asia) L.L.C.

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Yifan Hu  
+852-2978-0996 | yifan.hu@gs.com  
GS (Asia) L.L.C.

2. GlassBridge impact: Management highlights that GlassBridge is designed for edge coupling CPO switches while the current mainstream is grating coupling. Also, GlassBridge is still at an early stage for commercialization (i.e. takes time for mass production, ecosystem development, and customer qualification). Largan's FA is mainly used for grating coupling, and does not directly compete with GlassBridge. The precision level of FA for edge computing is also lower compared to grating coupling.

3. Near-term outlook: Largan 2Q26 revenues were up $17\%$ YoY, mainly driven by 10-19MPx handset lens. Management expects revenues to sequentially increase in both July and August, driven by new models from its major smartphone brand customer. Variable aperture lens are more difficult to produce compared to periscope lens given the more complicated design and higher requirements on particle control. GM in 2Q26 was $49.4\%$ mainly on major customers' model transitions, while variable aperture lens were in initial ramp up with room to enhance yield rate. 3Q26 GM could improve if new lens yield rates continue to improve. Management highlights handset lens would continue to benefit from specification upgrade in 2027E, such as more pieces of lenses for periscope lens, periscope lens with inner zooming, higher resolution in variable aperture lens, etc.

Earnings revisions: We raise 2027-28E net income by $2\%$ / $1\%$ mainly on higher revenues, reflecting our positive view on Largan's handset lens product mix upgrade on the back of premium smartphone models gaining more market share and Largan's leading market position in high-end lens, along with continuous specification upgrade. We factor in 2Q26 results (in line) and keep our 2026 estimates largely unchanged.

Exhibit 2: Earnings revision

<table><tr><td rowspan="2">NT m</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td><td>Old</td><td>New</td><td>Chg</td></tr><tr><td>Revenue</td><td>65,588</td><td>65,503</td><td>0%</td><td>75,755</td><td>76,562</td><td>1%</td><td>84,529</td><td>85,021</td><td>1%</td></tr><tr><td>GP</td><td>33,715</td><td>33,681</td><td>0%</td><td>41,290</td><td>42,012</td><td>2%</td><td>47,458</td><td>47,968</td><td>1%</td></tr><tr><td>OP</td><td>25,982</td><td>25,995</td><td>0%</td><td>32,268</td><td>32,893</td><td>2%</td><td>37,306</td><td>37,757</td><td>1%</td></tr><tr><td>Net income</td><td>25,006</td><td>24,904</td><td>0%</td><td>28,536</td><td>28,976</td><td>2%</td><td>31,642</td><td>31,937</td><td>1%</td></tr><tr><td>EPS (Diluted)</td><td>185.88</td><td>185.12</td><td>0%</td><td>211.22</td><td>214.48</td><td>2%</td><td>235.08</td><td>237.27</td><td>1%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>51.4%</td><td>51.4%</td><td></td><td>54.5%</td><td>54.9%</td><td></td><td>56.1%</td><td>56.4%</td><td></td></tr><tr><td>OPM</td><td>39.6%</td><td>39.7%</td><td></td><td>42.6%</td><td>43.0%</td><td></td><td>44.1%</td><td>44.4%</td><td></td></tr><tr><td>NM</td><td>38.1%</td><td>38.0%</td><td></td><td>37.7%</td><td>37.8%</td><td></td><td>37.4%</td><td>37.6%</td><td></td></tr></table>

Source: GS Global Investment Research

Exhibit 3: Largan 2Q26 results snapshot

<table><tr><td>NT m</td><td>2Q25</td><td>1Q26</td><td>2Q26</td><td>QoQ</td><td>YoY</td><td>GS</td><td>Act / GS</td><td>Cons.</td><td>Act/Cons.</td></tr><tr><td>Revenue</td><td>11,673</td><td>15,544</td><td>13,665</td><td>-12%</td><td>17%</td><td>13,750</td><td>-1%</td><td>13,343</td><td>2%</td></tr><tr><td>GP</td><td>6,260</td><td>7,680</td><td>6,752</td><td>-12%</td><td>8%</td><td>6,820</td><td>-1%</td><td>6,649</td><td>2%</td></tr><tr><td>OP</td><td>4,879</td><td>5,812</td><td>5,148</td><td>-11%</td><td>6%</td><td>5,168</td><td>0%</td><td>5,095</td><td>1%</td></tr><tr><td>Net income</td><td>1,032</td><td>6,123</td><td>4,670</td><td>-24%</td><td>352%</td><td>5,139</td><td>-9%</td><td>4,776</td><td>-2%</td></tr><tr><td colspan="6">Margins</td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>53.6%</td><td>49.4%</td><td>49.4%</td><td></td><td></td><td>49.6%</td><td></td><td>49.8%</td><td></td></tr><tr><td>OPM</td><td>41.8%</td><td>37.4%</td><td>37.7%</td><td></td><td></td><td>37.6%</td><td></td><td>38.2%</td><td></td></tr><tr><td>NM</td><td>8.8%</td><td>39.4%</td><td>34.2%</td><td></td><td></td><td>37.4%</td><td></td><td>35.8%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research, Bloomberg

Compared to Bloomberg consensus, we are $1\%$ / $14\%$ higher in operating income in 2026 / 27E, mainly on higher revenues and GM, reflecting our positive view on Largan's leading market position in high-end lens and the company's pixel mix upgrade, along with market share gains by premium models under high memory costs.

Exhibit 4: GS vs. Bloomberg consensus

<table><tr><td rowspan="2">NT m</td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>GS</td><td>BB</td><td>Diff %</td><td>GS</td><td>BB</td><td>Diff %</td></tr><tr><td>Revenue</td><td>65,503</td><td>66,138</td><td>-1%</td><td>76,562</td><td>71,389</td><td>7%</td></tr><tr><td>GP</td><td>33,681</td><td>33,320</td><td>1%</td><td>42,012</td><td>36,980</td><td>14%</td></tr><tr><td>OP</td><td>25,995</td><td>25,709</td><td>1%</td><td>32,893</td><td>28,789</td><td>14%</td></tr><tr><td>Net income</td><td>24,904</td><td>24,795</td><td>0%</td><td>28,976</td><td>27,062</td><td>7%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GM</td><td>51.4%</td><td>50.4%</td><td></td><td>54.9%</td><td>51.8%</td><td></td></tr><tr><td>OPM</td><td>39.7%</td><td>38.9%</td><td></td><td>43.0%</td><td>40.3%</td><td></td></tr><tr><td>NM</td><td>38.0%</td><td>37.5%</td><td></td><td>37.8%</td><td>37.9%</td><td></td></tr></table>

Source: GS Global Investment Research, Bloomberg

We expect sequential revenue growth in coming three months, driven by the ramp up of new models from its major smartphone brand customers. The growing foldable phones would also bring specification upgrade (e.g. slim camera, under display camera), along with more flagship model launches in 2H26 with specification upgrade to support Largan's revenues and GM increase.

Exhibit 5: Largan monthly revenue preview

<table><tr><td></td><td>Apr 2026</td><td>May 2026</td><td>Jun 2026</td><td>Jul 2026E</td><td>Aug 2026E</td><td>Sep 2026E</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td></tr><tr><td>Rev (NT$m)</td><td>5,362</td><td>4,593</td><td>3,712</td><td>4,826</td><td>6,756</td><td>7,285</td><td>15,544</td><td>13,665</td><td>18,866</td></tr><tr><td>YoY</td><td>24%</td><td>43%</td><td>-10%</td><td>-11%</td><td>13%</td><td>17%</td><td>7%</td><td>17%</td><td>7%</td></tr><tr><td>MoM/QoQ</td><td>-1%</td><td>-14%</td><td>-19%</td><td>30%</td><td>40%</td><td>8%</td><td>-10%</td><td>-12%</td><td>38%</td></tr><tr><td>GS estimates (NT$m)</td><td>4,769</td><td>3,243</td><td>3,795</td><td></td><td></td><td></td><td>14,180</td><td>13,750</td><td></td></tr><tr><td>Act. Vs. GS</td><td>12%</td><td>42%</td><td>-2%</td><td></td><td></td><td></td><td>10%</td><td>-1%</td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 6: Largan P&L

<table><tr><td>NT$m</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenues</td><td>14,579</td><td>11,673</td><td>17,677</td><td>17,219</td><td>15,544</td><td>13,665</td><td>18,866</td><td>17,428</td><td>48,842</td><td>59,458</td><td>61,148</td><td>65,503</td><td>76,562</td><td>85,021</td></tr><tr><td>GP</td><td>7,965</td><td>6,260</td><td>8,352</td><td>8,260</td><td>7,680</td><td>6,752</td><td>9,339</td><td>9,910</td><td>23,808</td><td>31,209</td><td>30,837</td><td>33,681</td><td>42,012</td><td>47,968</td></tr><tr><td>OP income</td><td>6,086</td><td>4,879</td><td>6,265</td><td>6,329</td><td>5,812</td><td>5,148</td><td>7,094</td><td>7,940</td><td>17,821</td><td>24,033</td><td>23,558</td><td>25,995</td><td>32,893</td><td>37,757</td></tr><tr><td>Net income</td><td>6,443</td><td>1,032</td><td>7,080</td><td>6,720</td><td>6,123</td><td>4,670</td><td>6,699</td><td>7,411</td><td>17,902</td><td>25,915</td><td>21,275</td><td>24,904</td><td>28,976</td><td>31,937</td></tr><tr><td>EPS, diluted (NT$)</td><td>47.73</td><td>7.70</td><td>52.61</td><td>49.17</td><td>46.11</td><td>34.57</td><td>49.59</td><td>54.86</td><td>132.62</td><td>191.44</td><td>157.21</td><td>185.12</td><td>214.48</td><td>237.27</td></tr><tr><td colspan="9">YoY</td><td colspan="6"></td></tr><tr><td>Revenues</td><td>29%</td><td>6%</td><td>-7%</td><td>-5%</td><td>7%</td><td>17%</td><td>7%</td><td>1%</td><td>2%</td><td>22%</td><td>3%</td><td>7%</td><td>17%</td><td>11%</td></tr><tr><td>GP</td><td>43%</td><td>18%</td><td>-13%</td><td>-23%</td><td>-4%</td><td>8%</td><td>12%</td><td>20%</td><td>-9%</td><td>31%</td><td>-1%</td><td>9%</td><td>25%</td><td>14%</td></tr><tr><td>OP income</td><td>54%</td><td>25%</td><td>-20%</td><td>-24%</td><td>-5%</td><td>6%</td><td>13%</td><td>25%</td><td>-13%</td><td>35%</td><td>-2%</td><td>10%</td><td>27%</td><td>15%</td></tr><tr><td>Net income</td><td>5%</td><td>-77%</td><td>7%</td><td>-23%</td><td>-5%</td><td>352%</td><td>-5%</td><td>10%</td><td>-21%</td><td>45%</td><td>-18%</td><td>17%</td><td>16%</td><td>10%</td></tr><tr><td>EPS, diluted (NT$)</td><td>5%</td><td>-77%</td><td>7%</td><td>-22%</td><td>-3%</td><td>349%</td><td>-6%</td><td>12%</td><td>-21%</td><td>44%</td><td>-18%</td><td>18%</td><td>16%</td><td>11%</td></tr><tr><td colspan="9">QoQ</td><td colspan="6"></td></tr><tr><td>Revenues</td><td>-20%</td><td>-20%</td><td>51%</td><td>-3%</td><td>-10%</td><td>-12%</td><td>38%</td><td>-8%</td><td rowspan="5" colspan="6"></td></tr><tr><td>GP</td><td>-26%</td><td>-21%</td><td>33%</td><td>-1%</td><td>-7%</td><td>-12%</td><td>38%</td><td>6%</td></tr><tr><td>OP income</td><td>-27%</td><td>-20%</td><td>28%</td><td>1%</td><td>-8%</td><td>-11%</td><td>38%</td><td>12%</td></tr><tr><td>Net income</td><td>-26%</td><td>-84%</td><td>586%</td><td>-5%</td><td>-9%</td><td>-24%</td><td>43%</td><td>11%</td></tr><tr><td>EPS, diluted (NT$)</td><td>-24%</td><td>-84%</td><td>583%</td><td>-7%</td><td>-6%</td><td>-25%</td><td>43%</td><td>11%</td></tr><tr><td colspan="9">Margins</td><td colspan="6"></td></tr><tr><td>GM</td><td>54.6%</td><td>53.6%</td><td>47.2%</td><td>48.0%</td><td>49.4%</td><td>49.4%</td><td>49.5%</td><td>56.9%</td><td>48.7%</td><td>52.5%</td><td>50.4%</td><td>51.4%</td><td>54.9%</td><td>56.4%</td></tr><tr><td>OPM</td><td>41.7%</td><td>41.8%</td><td>35.4%</td><td>36.8%</td><td>37.4%</td><td>37.7%</td><td>37.6%</td><td>45.6%</td><td>36.5%</td><td>40.4%</td><td>38.5%</td><td>39.7%</td><td>43.0%</td><td>44.4%</td></tr><tr><td>NM</td><td>44.2%</td><td>8.8%</td><td>40.1%</td><td>39.0%</td><td>39.4%</td><td>34.2%</td><td>35.5%</td><td>42.5%</td><td>36.7%</td><td>43.6%</td><td>34.8%</td><td>38.0%</td><td>37.8%</td><td>37.6%</td></tr><tr><td colspan="9">Ratios</td><td colspan="6"></td></tr><tr><td>Opex ratio</td><td>13%</td><td>12%</td><td>12%</td><td>11%</td><td>12%</td><td>12%</td><td>12%</td><td>11%</td><td>12%</td><td>12%</td><td>12%</td><td>12%</td><td>12%</td><td>12%</td></tr><tr><td>Tax rate</td><td>15%</td><td>42%</td><td>12%</td><td>17%</td><td>15%</td><td>22%</td><td>16%</td><td>16%</td><td>19%</td><td>19%</td><td>17%</td><td>17%</td><td>22%</td><td>24%</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive our target price from 2027E PE, and update our target PE multiple from 29.5x to 29.2x. Our target PE multiple (29.2x) is derived from (1) peers' avg. ratio of trading PE to forward year fundamentals (NI YoY and OPM), which is at 0.5x (vs. 0.5x previously), and (2) Largan's forward year fundamentals: 2027-28E NI YoY at 13% on avg. (vs. 13% previously) and OPM at 44% on avg (vs. 43% previously). The new target PE multiple of 29.2x is within Largan's historical trading range of 8.0x to 31.2x, reflecting our positive view on Largan's expansion from handset lens to CPO lens. Our new target price is at NT\$6,263 (vs. NT\$6,231 previously). Maintain Buy.

Exhibit 7: Largan peers comparison

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td rowspan="2">PE 2027E</td><td colspan="2">NI YoY</td><td colspan="2">OPM</td><td rowspan="2">Ratio</td></tr><tr><td>2027E</td><td>2028E</td><td>2027E</td><td>2028E</td></tr><tr><td>Largan</td><td>3008.TW</td><td>Buy</td><td>18.4</td><td>16%</td><td>10%</td><td>43.0%</td><td>44.4%</td><td>0.3</td></tr><tr><td>Largan (TP implied)</td><td>3008.TW</td><td>Buy</td><td>29.2</td><td>16%</td><td>10%</td><td>43.0%</td><td>44.4%</td><td>0.5</td></tr><tr><td colspan="9">Peers</td></tr><tr><td>AAC</td><td>2018.HK</td><td>Buy</td><td>12.0</td><td>12%</td><td>12%</td><td>9.7%</td><td>10.0%</td><td>0.6</td></tr><tr><td>Genius</td><td>3406.TW</td><td>NC</td><td>14.5</td><td>11%</td><td>7%</td><td>20.4%</td><td>20.7%</td><td>0.5</td></tr><tr><td>T&amp;S</td><td>300570.SZ</td><td>NC</td><td>55.2</td><td>90%</td><td>52%</td><td>24.7%</td><td>24.0%</td><td>0.6</td></tr><tr><td>VPEC</td><td>2455.TW</td><td>Buy</td><td>34.8</td><td>55%</td><td>40%</td><td>33.4%</td><td>35.3%</td><td>0.4</td></tr><tr><td>Average</td><td></td><td></td><td>29.1</td><td>42%</td><td>28%</td><td>22.1%</td><td>22.5%</td><td>0.5</td></tr></table>

NC: Not Covered; data from Bloomberg consensus  
Source: GS Global Investment Research, Bloomberg

Exhibit 8: Largan 12M forward PE ratio  
![](images/b23297b250e554f8f82ff20bc0b6673c367a85bf68b13fe4df74047827291167.jpg)  
Source: Company data, GS Global Investment Research, Bloomberg

Exhibit 9: Largan QFII holdings  
![](images/102242d153d21e7a5620f2787bf7be606a7eb2e59bdacace6336ba960dfddbe5.jpg)  
Source: TEJ

## Price Target Risks and Methodology - Largan

Valuation: We are Buy rated on Largan and have a 12-month target price of NT\$6,263, which is based on 2027E P/E. Our target P/E multiple of 29.2x is derived from (1) peers' avg. ratio of trading PE to forward year fundamentals (NI YoY and OPM), which is at 0.5x, and (2) Largan's forward year fundamentals: 2027-28E NI YoY at 13% on avg. and OPM at 44% on avg. The target PE multiple of 29.2x is within Largan's historical trading range of 8.0x to 31.2x, reflecting our positive view on Largan's expansion from handset lens to CPO lens.

Key risks: (1) slower-than-expected smartphone market growth, (2) fiercer competition in handset lenses, (3) slower-than-expected smartphone camera lens specification upgrades or Largan's handset lens pixel mix upgrade, (4) slower-than-expected CPO lens ramp up, and (5) fiercer competition in CPO lens.

<table><tr><td>3008.TW</td><td>12m Price Target: NT$6,263.00</td><td>Price: NT$4,345.00</td><td>Upside: 44.1%</td></tr></table>

<table><tr><td>Buy</td><td colspan="5">GS Forecast</td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11">Market cap: NT$584.5bn / $18.1bn Enterprise value: NT$457.3bn / $14.2bn 3m ADTV: NT$9.3bn / $292.5mn Taiwan Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: No</td><td>Revenue (NT$ mn) New</td><td>61,147.9</td><td>65,503.4</td><td>76,561.8</td><td>85,020.5</td></tr><tr><td>Revenue (NT$ mn) Old</td><td>61,147.9</td><td>65,588.5</td><td>75,755.3</td><td>84,529.2</td></tr><tr><td>EBITDA (NT$ mn)</td><td>31,290.3</td><td>34,560.3</td><td>41,440.9</td><td>46,364.1</td></tr><tr><td>EPS (NT$) New</td><td>159.41</td><td>187.34</td><td>217.11</td><td>239.29</td></tr><tr><td>EPS (NT$) Old</td><td>159.41</td><td>188.11</td><td>213.81</td><td>237.08</td></tr><tr><td>P/E (X)</td><td>14.8</td><td>23.2</td><td>20.0</td><td>18.2</td></tr><tr><td>P/B (X)</td><td>1.7</td><td>2.9</td><td>2.7</td><td>2.5</td></tr><tr><td>Dividend yield (%)</td><td>3.3</td><td>2.1</td><td>2.4</td><td>2.7</td></tr><tr><td>CROCI (%)</td><td>12.5</td><td>16.0</td><td>16.1</td><td>15.8</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (NT$)</td><td>34.99</td><td>50.20</td><td>55.53</td><td>50.33</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 13 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Verena Jeng

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
