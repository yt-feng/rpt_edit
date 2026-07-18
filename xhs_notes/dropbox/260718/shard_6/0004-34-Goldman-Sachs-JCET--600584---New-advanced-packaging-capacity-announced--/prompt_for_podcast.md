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
# JCET (600584.SS): New advanced packaging capacity announced; 2Q26 NI guidance beat

JCET's 2Q26 net income mid-point guidance was at Rmb570m (+113% YoY, +96% QoQ) (link), which management attributes to (1) strong AI infrastructure spending driving JCET's revenue growth and utilization rate, (2) product mix upgrade towards high-end OSAT service, driving the profitability, and (3) disciplined cost control. JCET's GM improved from 12.6% in 1Q25 to 14.5% in 1Q26. We expect the company's net income to grow at +34% CAGR in 2026-28E, driven by AI infrastructure upcycle, product mix upgrade, and the company's capacity expansion to capture the rising demand.

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

New capacity for advanced packaging: JCET announced its new capacity for advanced packaging in Jun 2026 (link), with a total investment at Rmb7.8bn, aiming to complete the phase 1 investment (plant construction, equipment investment) in 2H28E. We expect the capacity expansion plan to further drive JCET shipments growth and product mix upgrade in the long run, enabling it to capture the rising advanced packaging end demand in the local market, such as AI computing chips, high-end consumer electronics, automotive electronics, etc.

Earnings revision: We factor in JCET's 2Q26 net income guidance and raise our 2026E net income by $5\%$ , mainly on higher revenues and GM. We raise our 2026E revenue to reflect JCET benefiting from the rising AI related end demand. Our 2026E net income is revised up to reflect the company's product mix upgrade towards high-end OSAT service and utilization rate improvement.

Exhibit 1: Earnings revision

<table><tr><td rowspan="2">(Rmb mn)</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td></tr><tr><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td><td>New</td><td>Old</td><td>Diff</td></tr><tr><td>Revenue</td><td>46,802</td><td>46,398</td><td>1%</td><td>53,869</td><td>53,869</td><td>0%</td><td>61,773</td><td>61,773</td><td>0%</td></tr><tr><td>Gross profit</td><td>6,878</td><td>6,769</td><td>2%</td><td>7,873</td><td>7,873</td><td>0%</td><td>9,599</td><td>9,599</td><td>0%</td></tr><tr><td>Operating income</td><td>2,834</td><td>2,746</td><td>3%</td><td>3,552</td><td>3,552</td><td>0%</td><td>4,892</td><td>4,892</td><td>0%</td></tr><tr><td>Net income</td><td>2,596</td><td>2,464</td><td>5%</td><td>3,349</td><td>3,349</td><td>0%</td><td>4,648</td><td>4,646</td><td>0%</td></tr><tr><td>Margins</td><td colspan="3"></td><td colspan="3"></td><td colspan="3"></td></tr><tr><td>Gross margin</td><td>14.7%</td><td>14.6%</td><td>0.1ppts</td><td>14.6%</td><td>14.6%</td><td>0ppts</td><td>15.5%</td><td>15.5%</td><td>0ppts</td></tr><tr><td>Operating margin</td><td>6.1%</td><td>5.9%</td><td>0.1ppts</td><td>6.6%</td><td>6.6%</td><td>0ppts</td><td>7.9%</td><td>7.9%</td><td>0ppts</td></tr><tr><td>Net margin</td><td>5.5%</td><td>5.3%</td><td>0.2ppts</td><td>6.2%</td><td>6.2%</td><td>0ppts</td><td>7.5%</td><td>7.5%</td><td>0ppts</td></tr></table>

Source: Company data, GS Global Investment Research

Valuation: We continue to derive our 12M TP based on 2030E discounted P/E to capture JCET's long-term growth opportunities, and our 12-month target price is unchanged at Rmb125. Our target multiple is based on the correlation between peers' P/E vs. the sum of forward year NI growth and OPM, which is 46x 2030E discounted P/E target multiple, based on the company's NI YoY at $18\%$ and OPM at $10\%$ in 2031E. We apply the 46x target P/E and discount it back to 2027E with a COE of 11%. Our new TP implied 2027E P/E at 67x is in line with the company's recent forward trading P/E range at \~60x. Maintain Neutral.

Exhibit 2: Target multiple is derived from the correlation between peers P/E and the sum of forward year earnings and OPM

<table><tr><td></td><td>2030E P/E</td><td>2031E OPM</td><td>2031E NI YoY</td><td>Ratio</td></tr><tr><td>JCET</td><td>46</td><td>10%</td><td>18%</td><td>1.6</td></tr><tr><td></td><td>2027E P/E</td><td>2028E OPM</td><td>2028E NI YoY</td><td>Ratio</td></tr><tr><td>Huatian</td><td>68</td><td>5%</td><td>23%</td><td>2.5</td></tr><tr><td>TSMC</td><td>20</td><td>58%</td><td>35%</td><td>0.2</td></tr><tr><td>Forehope</td><td>92</td><td>8%</td><td>38%</td><td>2.0</td></tr><tr><td>Amkor</td><td>35</td><td>10%</td><td>6%</td><td>2.3</td></tr><tr><td>ASE</td><td>29</td><td>26%</td><td>29%</td><td>0.5</td></tr><tr><td>Tongfu</td><td>58</td><td>7%</td><td>21%</td><td>2.1</td></tr><tr><td>Avg.</td><td></td><td></td><td></td><td>1.6</td></tr></table>

Source: Company data, GS Global Investment Research, Refinitiv Eikon

Exhibit 3: JCET discounted P/E

<table><tr><td>Rmb mn</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>2031E</td></tr><tr><td>Revenue</td><td>29,661</td><td>35,962</td><td>38,871</td><td>46,802</td><td>53,869</td><td>61,773</td><td>69,700</td><td>75,489</td><td>81,760</td></tr><tr><td>Rev YoY %</td><td>-12%</td><td>21%</td><td>8%</td><td>20%</td><td>15%</td><td>15%</td><td>13%</td><td>8%</td><td>8%</td></tr><tr><td>Gross margin</td><td>13.7%</td><td>13.1%</td><td>14.1%</td><td>14.7%</td><td>14.6%</td><td>15.5%</td><td>16.1%</td><td>16.6%</td><td>17.0%</td></tr><tr><td>Gross profit</td><td>4,049</td><td>4,696</td><td>5,499</td><td>6,878</td><td>7,873</td><td>9,599</td><td>11,235</td><td>12,511</td><td>13,899</td></tr><tr><td>Opex</td><td>2,503</td><td>2,975</td><td>3,593</td><td>4,044</td><td>4,321</td><td>4,707</td><td>5,171</td><td>5,375</td><td>5,396</td></tr><tr><td>Opex ratio</td><td>8%</td><td>8%</td><td>9%</td><td>9%</td><td>8%</td><td>8%</td><td>7%</td><td>7%</td><td>7%</td></tr><tr><td>OP income</td><td>1,547</td><td>1,721</td><td>1,906</td><td>2,834</td><td>3,552</td><td>4,892</td><td>6,064</td><td>7,136</td><td>8,503</td></tr><tr><td>OPM</td><td>5%</td><td>5%</td><td>5%</td><td>6%</td><td>7%</td><td>8%</td><td>9%</td><td>9%</td><td>10%</td></tr><tr><td>Non-op gains</td><td>(25)</td><td>(72)</td><td>(168)</td><td>34</td><td>169</td><td>272</td><td>262</td><td>297</td><td>297</td></tr><tr><td>Pre-tax profit</td><td>1,522</td><td>1,649</td><td>1,738</td><td>2,868</td><td>3,721</td><td>5,164</td><td>6,325</td><td>7,433</td><td>8,800</td></tr><tr><td>Net profit</td><td>1,471</td><td>1,610</td><td>1,565</td><td>2,596</td><td>3,349</td><td>4,648</td><td>5,693</td><td>6,690</td><td>7,920</td></tr><tr><td>YoY</td><td>-54%</td><td>9%</td><td>-3%</td><td>66%</td><td>29%</td><td>39%</td><td>22%</td><td>18%</td><td>18%</td></tr><tr><td>EPS</td><td>0.82</td><td>0.90</td><td>0.87</td><td>1.45</td><td>1.87</td><td>2.60</td><td>3.18</td><td>3.74</td><td>4.43</td></tr><tr><td>2030 Target P/E</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>46.0x</td><td></td></tr><tr><td>12M target price (Rmb)</td><td></td><td></td><td></td><td></td><td>125</td><td></td><td></td><td></td><td></td></tr><tr><td>TP implied P/E</td><td></td><td></td><td></td><td></td><td>67</td><td>48</td><td>39</td><td></td><td></td></tr><tr><td colspan="10">COE assumption</td></tr><tr><td>Beta</td><td>1.20</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Risk free</td><td>3.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Market risk premium</td><td>6.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>COE</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, GS Global Investment Research

![](images/e9e7fc836baf90f63fd5adb894f0a3197d7c43c8b9c8648fa96b5edf7efb2c9d.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: JCET P&L summary

<table><tr><td>(Rmb m)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="16">Income statement</td></tr><tr><td>Revenue</td><td>9,335</td><td>9,270</td><td>10,064</td><td>10,202</td><td>9,171</td><td>11,282</td><td>12,727</td><td>13,623</td><td>33,762</td><td>29,661</td><td>35,962</td><td>38,871</td><td>46,802</td><td>53,869</td><td>61,773</td></tr><tr><td>Gross profit</td><td>1,179</td><td>1,327</td><td>1,434</td><td>1,559</td><td>1,334</td><td>1,696</td><td>1,854</td><td>1,992</td><td>5,752</td><td>4,049</td><td>4,696</td><td>5,499</td><td>6,878</td><td>7,873</td><td>9,599</td></tr><tr><td>OP</td><td>354</td><td>427</td><td>508</td><td>617</td><td>413</td><td>655</td><td>835</td><td>930</td><td>3,265</td><td>1,547</td><td>1,721</td><td>1,906</td><td>2,834</td><td>3,552</td><td>4,892</td></tr><tr><td>EBITDA</td><td>1,363</td><td>1,437</td><td>1,518</td><td>1,627</td><td>1,423</td><td>1,860</td><td>2,040</td><td>2,331</td><td>6,929</td><td>4,992</td><td>5,261</td><td>5,944</td><td>7,654</td><td>8,504</td><td>9,986</td></tr><tr><td>Net income</td><td>203</td><td>267</td><td>483</td><td>611</td><td>290</td><td>578</td><td>821</td><td>907</td><td>3,231</td><td>1,471</td><td>1,610</td><td>1,565</td><td>2,596</td><td>3,349</td><td>4,648</td></tr><tr><td>EPS (Rmb)</td><td>0.11</td><td>0.15</td><td>0.27</td><td>0.34</td><td>0.16</td><td>0.32</td><td>0.46</td><td>0.51</td><td>1.82</td><td>0.82</td><td>0.90</td><td>0.87</td><td>1.45</td><td>1.87</td><td>2.60</td></tr><tr><td colspan="16">Margins</td></tr><tr><td>Gross margin</td><td>12.6%</td><td>14.3%</td><td>14.3%</td><td>15.3%</td><td>14.5%</td><td>15.0%</td><td>14.6%</td><td>14.6%</td><td>17.0%</td><td>13.7%</td><td>13.1%</td><td>14.1%</td><td>14.7%</td><td>14.6%</td><td>15.5%</td></tr><tr><td>OPM</td><td>3.8%</td><td>4.6%</td><td>5.0%</td><td>6.1%</td><td>4.5%</td><td>5.8%</td><td>6.6%</td><td>6.8%</td><td>9.7%</td><td>5.2%</td><td>4.8%</td><td>4.9%</td><td>6.1%</td><td>6.6%</td><td>7.9%</td></tr><tr><td>EBITDA margin</td><td>14.6%</td><td>15.5%</td><td>15.1%</td><td>15.9%</td><td>15.5%</td><td>16.5%</td><td>16.0%</td><td>17.1%</td><td>20.5%</td><td>16.8%</td><td>14.6%</td><td>15.3%</td><td>16.4%</td><td>15.8%</td><td>16.2%</td></tr><tr><td>Net margin</td><td>2.2%</td><td>2.9%</td><td>4.8%</td><td>6.0%</td><td>3.2%</td><td>5.1%</td><td>6.4%</td><td>6.7%</td><td>9.6%</td><td>5.0%</td><td>4.5%</td><td>4.0%</td><td>5.5%</td><td>6.2%</td><td>7.5%</td></tr><tr><td colspan="16">Ratios</td></tr><tr><td>Opex ratio</td><td>8.8%</td><td>9.7%</td><td>9.2%</td><td>9.2%</td><td>10.0%</td><td>9.2%</td><td>8.0%</td><td>7.8%</td><td>7.4%</td><td>8.4%</td><td>8.3%</td><td>9.2%</td><td>8.6%</td><td>8.0%</td><td>7.6%</td></tr><tr><td>Tax rate</td><td>24.6%</td><td>12.4%</td><td>20.7%</td><td>-11.1%</td><td>8.7%</td><td>10.0%</td><td>10.0%</td><td>10.0%</td><td>1.8%</td><td>3.4%</td><td>2.2%</td><td>9.7%</td><td>9.9%</td><td>10.0%</td><td>10.0%</td></tr><tr><td colspan="16">QoQ</td></tr><tr><td>Revenue</td><td>-15%</td><td>-1%</td><td>9%</td><td>1%</td><td>-10%</td><td>23%</td><td>13%</td><td>7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Gross profit</td><td>-20%</td><td>12%</td><td>8%</td><td>9%</td><td>-14%</td><td>27%</td><td>9%</td><td>7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Operating income</td><td>-29%</td><td>21%</td><td>19%</td><td>21%</td><td>-33%</td><td>59%</td><td>27%</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Net income</td><td>-62%</td><td>31%</td><td>81%</td><td>27%</td><td>-53%</td><td>99%</td><td>42%</td><td>11%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EBITDA</td><td>-11%</td><td>5%</td><td>6%</td><td>7%</td><td>-13%</td><td>31%</td><td>10%</td><td>14%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="16">YoY</td></tr><tr><td>Revenue</td><td>36%</td><td>7%</td><td>6%</td><td>-7%</td><td>-2%</td><td>22%</td><td>26%</td><td>34%</td><td>11%</td><td>-12%</td><td>21%</td><td>8%</td><td>20%</td><td>15%</td><td>15%</td></tr><tr><td>Gross profit</td><td>41%</td><td>7%</td><td>24%</td><td>6%</td><td>13%</td><td>28%</td><td>29%</td><td>28%</td><td>2%</td><td>-30%</td><td>16%</td><td>17%</td><td>25%</td><td>14%</td><td>22%</td></tr><tr><td>Operating income</td><td>118%</td><td>-15%</td><td>-9%</td><td>24%</td><td>17%</td><td>53%</td><td>64%</td><td>51%</td><td>5%</td><td>-53%</td><td>11%</td><td>11%</td><td>49%</td><td>25%</td><td>38%</td></tr><tr><td>Net income</td><td>50%</td><td>-45%</td><td>6%</td><td>15%</td><td>43%</td><td>116%</td><td>70%</td><td>48%</td><td>9%</td><td>-54%</td><td>9%</td><td>-3%</td><td>66%</td><td>29%</td><td>39%</td></tr><tr><td>EBITDA</td><td>30%</td><td>3%</td><td>5%</td><td>18%</td><td>4%</td><td>30%</td><td>34%</td><td>43%</td><td>4%</td><td>-28%</td><td>5%</td><td>13%</td><td>29%</td><td>11%</td><td>17%</td></tr></table>

Source: Company data, GS Global Investment Research

## Price Target Risks and Methodology - JCET

Valuation: We are Neutral-rated on JCET with a 12-month target price of Rmb125, which is based on 46x 2030E discounted P/E (discounted back to 2027E). Our target P/E is derived from correlation between peers P/E to the sum of NI YoY and OPM.

Key upside risks: Faster-/slower-than-expected semis capex expansion in China; Faster-/slower-than-expected technology development; Faster-/slower-than-expected shipments ramp up of advanced packaging.

<table><tr><td>600584.SS</td><td colspan="2">12m Price Target: Rmb125.00</td><td colspan="2">Price: Rmb85.49</td><td colspan="2">Upside: 46.2%</td></tr><tr><td colspan="2">Neutral</td><td colspan="5">GS Forecast</td></tr><tr><td colspan="2"></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td colspan="2">Market cap:</td><td>Revenue (Rmb mn) New</td><td>38,871.3</td><td>46,802.4</td><td>53,868.6</td><td>61,772.8</td></tr><tr><td colspan="2">Rmb153.0bn / $22.6bn</td><td>Revenue (Rmb mn) Old</td><td>38,871.3</td><td>46,398.1</td><td>53,868.6</td><td>61,772.8</td></tr><tr><td colspan="2">Enterprise value:</td><td>EBITDA (Rmb mn)</td><td>5,944.3</td><td>7,654.0</td><td>8,503.6</td><td>9,986.5</td></tr><tr><td colspan="2">Rmb162.8bn / $24.1bn</td><td>EPS (Rmb) New</td><td>0.87</td><td>1.45</td><td>1.87</td><td>2.60</td></tr><tr><td colspan="2">3m ADTV: Rmb16.6bn / $2.4bn</td><td>EPS (Rmb) Old</td><td>0.87</td><td>1.38</td><td>1.87</td><td>2.60</td></tr><tr><td colspan="2">China</td><td>P/E (X)</td><td>41.8</td><td>58.9</td><td>45.7</td><td>32.9</td></tr><tr><td colspan="2">Greater China Technology</td><td>P/B (X)</td><td>2.1</td><td>4.6</td><td>4.2</td><td>3.8</td></tr><tr><td colspan="2">M&amp;A Rank: 3</td><td>Dividend yield (%)</td><td>0.4</td><td>0.3</td><td>0.3</td><td>0.5</td></tr><tr><td colspan="2">Leases incl. in net debt &amp; EV?: Yes</td><td>CROCI (%)</td><td>8.2</td><td>15.0</td><td>12.5</td><td>12.7</td></tr><tr><td colspan="2"></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td colspan="2"></td><td>EPS (Rmb)</td><td>0.16</td><td>0.32</td><td>0.46</td><td>0.51</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 17 Jul 2026 close.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high 

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
