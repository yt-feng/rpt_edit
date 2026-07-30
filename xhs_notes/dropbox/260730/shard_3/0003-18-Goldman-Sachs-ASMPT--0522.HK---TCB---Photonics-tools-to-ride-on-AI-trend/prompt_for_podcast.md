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
# ASMPT (0522.HK): TCB & Photonics tools to ride on AI trend; Booking value expected to grow in 3Q26; Neutral

3Q26 order to sustain at an elevated level. Despite the longer lead times for certain materials, management expects the sustained growth in 3Q26, and the bookings are expected to grow by a high single-digit percentage sequentially in 3Q26, following the 1Q / 2Q26 bookings growth at +45% / +24% QoQ, mainly driven by TCB and photonics tools. For the TCB tool, management holds a positive view on the global end demand, driven by (1) rising adoption of CPO in data centers, (2) rising computing power and agentic AI demand driving the high-end CPU and HBM demand, (3) technology migration of advanced packaging (e.g. panel-level packaging) supporting the performance improvement of AI chips, and (4) OSAT players in China market migrating to advanced packaging in the long run. Overall, management expects revenue growth for both SEMI and SMT businesses in 2026, supported by advanced AI application driving computing needs and the recovery of demand for some traditional application. We remain positive on ASMPT riding on the advanced packaging trend globally, while maintain Neutral on fair valuation.

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Yifan Hu  
+852-2978-0996 | yifan.hu@gs.com  
GS (Asia) L.L.C.

Exhibit 1: ASMPT's BB ratio was 1.43 by 2Q26 (vs. 1.43 by 1Q26)  
![](images/07ef6c9e61fd4a09f4dc234285450cc659fe820bf1cb95c09d3bd849b5fc6475.jpg)  
Source: Company data

Exhibit 2: ASMPT's revenues: Recovering trend  
![](images/6b81721a231628c33e350ca7c419abe838da8111000a67e7cafe48c9bb58dab6.jpg)  
Source: Company data

Earnings revision: We factor in ASMPT's 2Q26 result and raise our 2026E revenue and GM to reflect the stronger the expected 2Q26 performance. Our 2026E opex ratios are revised down, considering the higher revenue scale and operational efficiency improvement as shipments ramp up. Overall, our 2026E net income is largely unchanged, reflecting the higher than expected tax rate in 2Q26 and the impact of discontinued operation. Our 2027-28E estimates are largely unchanged.

Exhibit 3: Earnings revision

<table><tr><td rowspan="2">(HK$m)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td></tr><tr><td>Revenue</td><td>19,400</td><td>18,151</td><td>7%</td><td>22,334</td><td>22,356</td><td>0%</td><td>25,657</td><td>25,764</td><td>0%</td></tr><tr><td>Gross profit</td><td>8,075</td><td>7,315</td><td>10%</td><td>9,290</td><td>9,280</td><td>0%</td><td>10,737</td><td>10,771</td><td>0%</td></tr><tr><td>Operating income</td><td>2,553</td><td>2,009</td><td>27%</td><td>3,203</td><td>3,202</td><td>0%</td><td>3,862</td><td>3,866</td><td>0%</td></tr><tr><td>Pre tax profit</td><td>2,458</td><td>2,087</td><td>18%</td><td>3,214</td><td>3,223</td><td>0%</td><td>3,875</td><td>3,889</td><td>0%</td></tr><tr><td>Net income</td><td>1,552</td><td>1,560</td><td>0%</td><td>2,410</td><td>2,401</td><td>0%</td><td>2,868</td><td>2,878</td><td>0%</td></tr><tr><td>Margins</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross margin</td><td>41.6%</td><td>40.3%</td><td>1.3ppts</td><td>41.6%</td><td>41.5%</td><td>0.1ppts</td><td>41.8%</td><td>41.8%</td><td>0ppts</td></tr><tr><td>Operating margin</td><td>13.2%</td><td>11.1%</td><td>2.1ppts</td><td>14.3%</td><td>14.3%</td><td>0ppts</td><td>15.1%</td><td>15.0%</td><td>0.1ppts</td></tr><tr><td>Net margin</td><td>8.0%</td><td>8.6%</td><td>-0.6ppts</td><td>10.8%</td><td>10.7%</td><td>0.1ppts</td><td>11.2%</td><td>11.2%</td><td>0ppts</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derived our 12M TP based on 2030E discounted P/E to capture long-term growth opportunities. Our 12-month target price is updated to HK\$177 (vs. previously at HK\$206). Our target multiple is based on the refreshed correlation between peers' P/E vs. the sum of forward year NI growth and OPM, which is 24.9x 2030E discounted P/E target multiple, based on the company's NI YoY at 23% and OPM at 18% in 2031E. We apply the 24.9x target P/E on 2030E P/E and discount it back to 2027E with a COE of 11%. Our new TP implied 2027E P/E at 31x is around the company's historical avg.+1stv. forward trading P/E. Maintain Neutral.

Exhibit 4: The target multiple is derived from the correlation between peers P/E and the sum of forward year earnings and OPM

<table><tr><td></td><td>2030E P/E</td><td>2031E OPM</td><td>2031E NI YoY</td><td>Ratio</td></tr><tr><td>ASMPT</td><td>25</td><td>18%</td><td>23%</td><td>0.6</td></tr><tr><td></td><td>2027E P/E</td><td>2028E OPM</td><td>2028E NI YoY</td><td>Ratio</td></tr><tr><td>Applied materials</td><td>27</td><td>36%</td><td>20%</td><td>0.5</td></tr><tr><td>Accotest</td><td>53</td><td>50%</td><td>30%</td><td>0.7</td></tr><tr><td>LAM Research</td><td>31</td><td>38%</td><td>20%</td><td>0.5</td></tr><tr><td>Tokyo Electron</td><td>23</td><td>34%</td><td>21%</td><td>0.4</td></tr><tr><td>KLA</td><td>32</td><td>46%</td><td>20%</td><td>0.5</td></tr><tr><td>Piotech</td><td>78</td><td>16%</td><td>55%</td><td>1.1</td></tr><tr><td>Average</td><td></td><td></td><td></td><td>0.6</td></tr></table>

Average

Exhibit 5: ASMPT 12M forward P/E  
![](images/fcc07e4bd8a5cab3d8b28fad2af659276be20cb53927c7afeb87541b9f14e0ce.jpg)  
Source: Company data, GS Global Investment Research, Refinitiv Eikon  
Source: Refinitiv Eikon

Exhibit 6: ASMPT discounted P/E valuation

<table><tr><td>HK$m</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td></tr><tr><td>Revenue</td><td>14,697</td><td>12,850</td><td>13,989</td><td>19,400</td><td>22,334</td><td>25,657</td><td>29,505</td><td>33,931</td><td>38,682</td></tr><tr><td>Rev YoY %</td><td>-24%</td><td>-13%</td><td>9%</td><td>39%</td><td>15%</td><td>15%</td><td>15%</td><td>15%</td><td>14%</td></tr><tr><td>Gross margin</td><td>39.3%</td><td>40.0%</td><td>37.8%</td><td>41.6%</td><td>41.6%</td><td>41.8%</td><td>42.0%</td><td>42.3%</td><td>42.6%</td></tr><tr><td>Gross profit</td><td>5,774</td><td>5,138</td><td>5,286</td><td>8,075</td><td>9,290</td><td>10,737</td><td>12,392</td><td>14,353</td><td>16,478</td></tr><tr><td>Opex</td><td>4,669</td><td>4,648</td><td>4,718</td><td>5,522</td><td>6,087</td><td>6,875</td><td>7,760</td><td>8,822</td><td>9,670</td></tr><tr><td>Opex ratio</td><td>32%</td><td>36%</td><td>34%</td><td>28%</td><td>27%</td><td>27%</td><td>26%</td><td>26%</td><td>25%</td></tr><tr><td>OP income</td><td>1,104</td><td>490</td><td>568</td><td>2,553</td><td>3,203</td><td>3,862</td><td>4,632</td><td>5,531</td><td>6,808</td></tr><tr><td>OPM</td><td>8%</td><td>4%</td><td>4%</td><td>13%</td><td>14%</td><td>15%</td><td>16%</td><td>16%</td><td>18%</td></tr><tr><td>Non-op gains</td><td>(68)</td><td>(57)</td><td>645</td><td>(95)</td><td>11</td><td>13</td><td>13</td><td>13</td><td>13</td></tr><tr><td>Pre-tax profit</td><td>1,036</td><td>433</td><td>1,213</td><td>2,458</td><td>3,214</td><td>3,875</td><td>4,645</td><td>5,544</td><td>6,821</td></tr><tr><td>Tax expense</td><td>325</td><td>148</td><td>138</td><td>759</td><td>803</td><td>1,008</td><td>1,208</td><td>1,441</td><td>1,773</td></tr><tr><td>Minority interest</td><td>(4)</td><td>(3)</td><td>(0)</td><td>(11)</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net profit</td><td>715</td><td>288</td><td>1,074</td><td>1,710</td><td>2,410</td><td>2,868</td><td>3,437</td><td>4,102</td><td>5,047</td></tr><tr><td>YoY</td><td>-73%</td><td>-60%</td><td>273%</td><td>59%</td><td>41%</td><td>19%</td><td>20%</td><td>19%</td><td>23%</td></tr><tr><td>EPS</td><td>1.73</td><td>0.83</td><td>2.16</td><td>3.71</td><td>5.76</td><td>6.85</td><td>8.21</td><td>9.80</td><td>12.06</td></tr><tr><td>2030 Target P/E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>24.9x</td><td></td></tr><tr><td>12M target price (HK$)</td><td></td><td></td><td></td><td></td><td>177</td><td></td><td></td><td></td><td></td></tr><tr><td>TP implied P/E</td><td></td><td></td><td></td><td></td><td>31</td><td>26</td><td>22</td><td></td><td></td></tr><tr><td>COE assumption</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Beta</td><td>1.20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Risk free</td><td>3.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Market risk premium</td><td>6.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COE</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

Exhibit 7: ASMPT P&L summary

<table><tr><td>(HK$m)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td><td>3Q26E</td><td>4Q26E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>3,125</td><td>3,244</td><td>3,661</td><td>3,959</td><td>3,967</td><td>4,936</td><td>5,172</td><td>5,325</td><td>19,363</td><td>14,697</td><td>12,850</td><td>13,989</td><td>19,400</td><td>22,334</td><td>25,657</td></tr><tr><td>Gross profit</td><td>1,278</td><td>1,283</td><td>1,306</td><td>1,419</td><td>1,566</td><td>2,092</td><td>2,179</td><td>2,238</td><td>7,966</td><td>5,774</td><td>5,138</td><td>5,286</td><td>8,075</td><td>9,290</td><td>10,737</td></tr><tr><td>Operating expense</td><td>(1,118)</td><td>(1,087)</td><td>(1,255)</td><td>(1,258)</td><td>(1,181)</td><td>(1,306)</td><td>(1,518)</td><td>(1,518)</td><td>(4,729)</td><td>(4,669)</td><td>(4,648)</td><td>(4,718)</td><td>(5,522)</td><td>(6,087)</td><td>(6,875)</td></tr><tr><td>Operating income</td><td>160</td><td>197</td><td>50</td><td>161</td><td>385</td><td>786</td><td>661</td><td>720</td><td>3,237</td><td>1,104</td><td>490</td><td>568</td><td>2,553</td><td>3,203</td><td>3,862</td></tr><tr><td>Pre tax profit</td><td>107</td><td>132</td><td>(222)</td><td>1,196</td><td>445</td><td>645</td><td>652</td><td>715</td><td>3,413</td><td>1,036</td><td>433</td><td>1,213</td><td>2,458</td><td>3,214</td><td>3,875</td></tr><tr><td>Net income</td><td>84</td><td>131</td><td>(270)</td><td>957</td><td>254</td><td>335</td><td>459</td><td>504</td><td>2,620</td><td>715</td><td>345</td><td>902</td><td>1,552</td><td>2,410</td><td>2,868</td></tr><tr><td>EPS (HK$)</td><td>0.20</td><td>0.32</td><td>(0.65)</td><td>2.30</td><td>0.61</td><td>0.80</td><td>1.10</td><td>1.21</td><td>6.35</td><td>1.73</td><td>0.83</td><td>2.17</td><td>3.72</td><td>5.77</td><td>6.86</td></tr><tr><td>Margins / ratio</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Gross margin</td><td>40.9%</td><td>39.6%</td><td>35.7%</td><td>35.8%</td><td>39.5%</td><td>42.4%</td><td>42.1%</td><td>42.0%</td><td>41.1%</td><td>39.3%</td><td>40.0%</td><td>37.8%</td><td>41.6%</td><td>41.6%</td><td>41.8%</td></tr><tr><td>Opex ratio</td><td>-35.8%</td><td>-33.5%</td><td>-34.3%</td><td>-31.8%</td><td>-29.8%</td><td>-26.5%</td><td>-29.3%</td><td>-28.5%</td><td>-24.4%</td><td>-31.8%</td><td>-36.2%</td><td>-33.7%</td><td>-28.5%</td><td>-27.3%</td><td>-26.8%</td></tr><tr><td>Operating margin</td><td>5.1%</td><td>6.1%</td><td>1.4%</td><td>4.1%</td><td>9.7%</td><td>15.9%</td><td>12.8%</td><td>13.5%</td><td>16.7%</td><td>7.5%</td><td>3.8%</td><td>4.1%</td><td>13.2%</td><td>14.3%</td><td>15.1%</td></tr><tr><td>Net margin</td><td>2.7%</td><td>4.0%</td><td>-7.4%</td><td>24.2%</td><td>6.4%</td><td>6.8%</td><td>8.9%</td><td>9.5%</td><td>13.5%</td><td>4.9%</td><td>2.7%</td><td>6.4%</td><td>8.0%</td><td>10.8%</td><td>11.2%</td></tr><tr><td>QoQ</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Revenue</td><td>3%</td><td>4%</td><td>13%</td><td>8%</td><td>0%</td><td>24%</td><td>5%</td><td>3%</td><td rowspan="6" colspan="7"></td></tr><tr><td>Gross profit</td><td>15%</td><td>0%</td><td>2%</td><td>9%</td><td>10%</td><td>34%</td><td>4%</td><td>3%</td></tr><tr><td>Operating income</td><td>nm</td><td>23%</td><td>-74%</td><td>219%</td><td>139%</td><td>104%</td><td>-16%</td><td>9%</td></tr><tr><td>Pre tax profit</td><td>nm</td><td>24%</td><td>nm</td><td>nm</td><td>-63%</td><td>45%</td><td>1%</td><td>10%</td></tr><tr><td>Net income</td><td>1806%</td><td>57%</td><td>nm</td><td>nm</td><td>-73%</td><td>32%</td><td>37%</td><td>10%</td></tr><tr><td>EPS</td><td>1798%</td><td>57%</td><td>nm</td><td>nm</td><td>-74%</td><td>32%</td><td>37%</td><td>10%</td></tr><tr><td>YoY</td><td colspan="4"></td><td colspan="4"></td><td colspan="7"></td></tr><tr><td>Revenue</td><td>0%</td><td>-3%</td><td>9%</td><td>31%</td><td>27%</td><td>52%</td><td>41%</td><td>35%</td><td>-12%</td><td>-24%</td><td>-13%</td><td>9%</td><td>39%</td><td>15%</td><td>15%</td></tr><tr><td>Gross profit</td><td>-3%</td><td>-4%</td><td>-5%</td><td>27%</td><td>23%</td><td>63%</td><td>67%</td><td>58%</td><td>-11%</td><td>-28%</td><td>-11%</td><td>3%</td><td>53%</td><td>15%</td><td>16%</td></tr><tr><td>Operating income</td><td>-33%</td><td>46%</td><td>-72%</td><td>nm</td><td>141%</td><td>300%</td><td>1210%</td><td>347%</td><td>-22%</td><td>-66%</td><td>-56%</td><td>16%</td><td>349%</td><td>25%</td><td>21%</td></tr><tr><td>Pre tax profit</td><td>-59%</td><td>-32%</td><td>nm</td><td>nm</td><td>317%</td><td>388%</td><td>nm</td><td>-40%</td><td>-17%</td><td>-70%</td><td>-58%</td><td>180%</td><td>103%</td><td>31%</td><td>21%</td></tr><tr><td>Net income</td><td>-54%</td><td>-3%</td><td>nm</td><td>21716%</td><td>203%</td><td>155%</td><td>nm</td><td>-47%</td><td>-17%</td><td>-73%</td><td>-52%</td><td>161%</td><td>72%</td><td>55%</td><td>19%</td></tr><tr><td>EPS</td><td>-54%</td><td>-3%</td><td>nm</td><td>21617%</td><td>203%</td><td>155%</td><td>nm</td><td>-48%</td><td>-18%</td><td>-73%</td><td>-52%</td><td>160%</td><td>72%</td><td>55%</td><td>19%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price target methodology and risks - ASMPT

Valuation methodology: We are Neutral-rated on ASMPT with a 12-month target price of HK\$177, which is based on 24.9x 2030E discounted P/E (discounted back to 2027E). Our target P/E is derived from correlation between peers P/E to the sum of NI YoY and OPM.

Key upside/downside risks: 1) customers' faster-/slower-than-expected adoption of Advanced Packaging tools; 2) stronger-/weaker-than-expected demand from automotive customers; and 3) stronger-/weaker-than-expected demand for traditional IC packaging and SMT equipment.

<table><tr><td>0522.HK</td><td colspan="2">12m Price Target: HK$177.00</td><td colspan="2">Price: HK$139.50</td><td colspan="2">Upside: 26.9%</td></tr><tr><td colspan="2">Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td rowspan="11" colspan="2">Market cap: HK$57.5bn / $7.3bn Enterprise value: HK$55.1bn / $7.0bn 3m ADTV: HK$844.0mn / $107.7mn China Greater China Technology M&amp;A Rank: 3 Leases incl. in net debt &amp; EV?: No</td><td>Revenue (HK$ mn) New</td><td>13,989.1</td><td>19,400.0</td><td>22,334.3</td><td>25,656.9</td></tr><tr><td>Revenue (HK$ mn) Old</td><td>14,146.5</td><td>18,151.1</td><td>22,356.3</td><td>25,764.4</td></tr><tr><td>EBITDA (HK$ mn)</td><td>1,210.8</td><td>3,160.8</td><td>3,815.4</td><td>4,479.2</td></tr><tr><td>EPS (HK$) New</td><td>2.17</td><td>3.72</td><td>5.77</td><td>6.86</td></tr><tr><td>EPS (HK$) Old</td><td>2.17</td><td>3.55</td><td>5.75</td><td>6.89</td></tr><tr><td>P/E (X)</td><td>31.2</td><td>37.5</td><td>24.2</td><td>20.3</td></tr><tr><td>P/B (X)</td><td>1.7</td><td>3.3</td><td>3.2</td><td>3.0</td></tr><tr><td>Dividend yield (%)</td><td>2.1</td><td>1.7</td><td>2.7</td><td>3.2</td></tr><tr><td>CROCI (%)</td><td>3.0</td><td>11.1</td><td>14.8</td><td>16.3</td></tr><tr><td></td><td>6/26</td><td>9/26E</td><td>12/26E</td><td>3/27E</td></tr><tr><td>EPS (HK$)</td><td>0.80</td><td>1.10</td><td>1.21</td><td>1.37</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 28 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading 

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
