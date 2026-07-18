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
# Xiaomi Corp. (1810.HK)

Xiaomi Robotics: Integrating Hardware Ontologies, Data, and Models to Scale up; Buy

## What's new

We continue to see catalysts in EV and AI playing out in 3Q26 as we outlined in prior notes (Setting the scene for a catalyst-rich 3Q on Jun 24 and Sharpening the scene on Jul 10). Xiaomi Robotics on Jul 13-15 announced several achievements:

1) Humanoid deployment: Xiaomi humanoids have improved the task success rate to 98% at self-tapping nut loading stations by Jul, from 90%+ in Mar when they were initially deployed, which is just 1pp behind experienced human workers. From July, humanoids have started taking on new logistics tasks such as sorting flexible center console side covers and folding returnable boxes with a 90% success rate, and achieved long-duration continuous operations with flexible workpieces for the first time. Despite the apparent gap in speed and volume, this places Xiaomi alongside global leaders (e.g. Figure AI) in deploying humanoids to active automotive production lines.

## 2) Embodied data/scene synthesis: Xiaomi-Robotics-U0, a

38B-parameter unified generative model, is designed to synthesize high-fidelity robot trajectories and physical interaction scenarios and mitigate the bottleneck of real-world data scarcity. The model uniquely unifies text-to-image generation, any-to-image editing, multi-view embodied scene generation, embodied transfer, and embodied video generation into a single architecture, allowing autoregressive scaling across modalities while preserving the geometric integrity and perspective consistency. As per Xiaomi, Robotics-U0 outperforms GPT-Image-2 in embodied scene generation and embodied transfer, and ranks No.1 on WorldArena, a unified benchmark for embodied world models evaluation.

## 3) Robot foundation model: Xiaomi-Robotics-1, a

Vision-Language-Action (VLA) foundation model designed for end-to-end physical execution, was released as the cognitive and

## BUY

Timothy Zhao
+852-2978-2673 | timothy.zhao@gs.com
GS (Asia) L.L.C.

Ronald Keung, CFA
+852-2978-0856 | ronald.keung@gs.com
GS (Asia) L.L.C.

Eunice Liu
+852-2978-7472 | eunice.liu@gs.com
GS (Asia) L.L.C.

## Key Data

Market cap: HK\$708.8bn / \$90.4bn
Enterprise value: HK\$510.2bn / \$65.1bn
3m ADTV: HK\$4.7bn / \$596.8mn
China
China Internet Verticals
M&A Rank: 3
Leases incl. in net debt & EV?: No

GS Forecast

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Revenue (Rmb mn)</td><td>457,286.6</td><td>479,154.1</td><td>566,666.6</td><td>670,393.3</td></tr><tr><td>EBITDA (Rmb mn)</td><td>56,657.7</td><td>36,636.9</td><td>48,745.1</td><td>60,973.7</td></tr><tr><td>EPS (Rmb)</td><td>1.47</td><td>1.02</td><td>1.36</td><td>1.73</td></tr><tr><td>P/E (X)</td><td>30.6</td><td>23.2</td><td>17.4</td><td>13.8</td></tr><tr><td>P/B (X)</td><td>4.5</td><td>2.1</td><td>1.9</td><td>1.6</td></tr><tr><td>Dividend yield (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>N debt/EBITDA (ex lease,X)</td><td>(2.9)</td><td>(4.7)</td><td>(3.9)</td><td>(3.4)</td></tr><tr><td>CROCI (%)</td><td>28.1</td><td>17.0</td><td>19.0</td><td>20.3</td></tr><tr><td>FCF yield (%)</td><td>1.9</td><td>2.0</td><td>3.4</td><td>4.0</td></tr><tr><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td>EPS (Rmb)</td><td>0.23</td><td>0.20</td><td>0.27</td><td>0.32</td></tr></table>

GS Factor Profile

![](images/fc4439cda2d5c2a8ed9b88bbe789dc297808f610d31819e675ccf3d5b3f8a09b.jpg)  
Source: Company data, GS estimates. See disclosures for details.

## Xiaomi Corp. (1810.HK) Rating since Oct 19, 2023

Ratios & Valuation

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>P/E (X)</td><td>30.6</td><td>23.2</td><td>17.4</td><td>13.8</td></tr><tr><td>P/B (X)</td><td>4.5</td><td>2.1</td><td>1.9</td><td>1.6</td></tr><tr><td>FCF yield (%)</td><td>1.9</td><td>2.0</td><td>3.4</td><td>4.0</td></tr><tr><td>EV/EBITDAR (X)</td><td>17.5</td><td>12.0</td><td>8.8</td><td>6.7</td></tr><tr><td>EV/EBITDA (excl. leases) (X)</td><td>17.5</td><td>12.0</td><td>8.8</td><td>6.7</td></tr><tr><td>CROCI (%)</td><td>28.1</td><td>17.0</td><td>19.0</td><td>20.3</td></tr><tr><td>ROE (%)</td><td>18.3</td><td>8.6</td><td>10.4</td><td>11.7</td></tr><tr><td>Net debt/equity (%)</td><td>(61.4)</td><td>(57.9)</td><td>(55.9)</td><td>(54.0)</td></tr><tr><td>Net debt/equity (excl. leases) (%)</td><td>(61.4)</td><td>(57.9)</td><td>(55.9)</td><td>(54.0)</td></tr><tr><td>Interest cover (X)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Days inventory outst, sales</td><td>57.3</td><td>64.4</td><td>60.8</td><td>59.7</td></tr><tr><td>Receivable days</td><td>46.9</td><td>47.7</td><td>43.6</td><td>42.2</td></tr><tr><td>Days payable outstanding</td><td>144.1</td><td>142.3</td><td>127.3</td><td>117.3</td></tr><tr><td>DuPont ROE (%)</td><td>15.6</td><td>8.1</td><td>9.8</td><td>11.0</td></tr><tr><td>Turnover (X)</td><td>0.9</td><td>0.9</td><td>1.0</td><td>1.0</td></tr><tr><td>Leverage (X)</td><td>1.9</td><td>1.8</td><td>1.8</td><td>1.7</td></tr><tr><td>Gross cash invested (ex cash) (Rmb)</td><td>193,679.1</td><td>226,261.1</td><td>261,292.4</td><td>303,166.7</td></tr><tr><td>Average capital employed (Rmb)</td><td>230,839.6</td><td>286,628.9</td><td>309,387.5</td><td>335,633.3</td></tr><tr><td>BVPS (Rmb)</td><td>9.97</td><td>11.20</td><td>12.60</td><td>14.40</td></tr></table>

Income Statement (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue</td><td>457,286.6</td><td>479,154.1</td><td>566,666.6</td><td>670,393.3</td></tr><tr><td>Cost of goods sold</td><td>(355,480.8)</td><td>(378,237.8)</td><td>(442,877.5)</td><td>(521,559.7)</td></tr><tr><td>SG&amp;A</td><td>(39,867.4)</td><td>(42,521.3)</td><td>(46,836.4)</td><td>(51,873.4)</td></tr><tr><td>R&amp;D</td><td>(33,132.2)</td><td>(39,991.0)</td><td>(47,748.6)</td><td>(56,518.7)</td></tr><tr><td>Other operating inc./(exp.)</td><td>19,094.7</td><td>8,026.1</td><td>8,026.1</td><td>8,026.1</td></tr><tr><td>EBITDA</td><td>56,657.7</td><td>36,636.9</td><td>48,745.1</td><td>60,973.7</td></tr><tr><td>Depreciation &amp; amortization</td><td>(8,756.7)</td><td>(10,206.8)</td><td>(11,514.9)</td><td>(12,506.0)</td></tr><tr><td>EBIT</td><td>47,900.9</td><td>26,430.1</td><td>37,230.2</td><td>48,467.7</td></tr><tr><td>Net interest inc./(exp.)</td><td>1,745.9</td><td>2,513.0</td><td>2,689.9</td><td>2,568.2</td></tr><tr><td>Income/(loss) from associates</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Pre-tax profit</td><td>49,646.9</td><td>28,943.2</td><td>39,920.1</td><td>51,035.9</td></tr><tr><td>Provision for taxes</td><td>(8,080.4)</td><td>(4,905.0)</td><td>(7,007.9)</td><td>(8,766.7)</td></tr><tr><td>Minority interest</td><td>77.0</td><td>51.3</td><td>51.3</td><td>25.7</td></tr><tr><td>Preferred dividends</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Net inc. (pre-exceptionals)</td><td>41,643.4</td><td>24,089.5</td><td>32,963.6</td><td>42,294.9</td></tr><tr><td>Post-tax exceptionals</td><td>(2,400.1)</td><td>2,950.2</td><td>3,342.9</td><td>3,952.6</td></tr><tr><td>Net inc. (post-exceptionals)</td><td>39,243.2</td><td>27,039.8</td><td>36,306.5</td><td>46,247.4</td></tr><tr><td>EPS (basic, pre-except) (Rmb)</td><td>1.62</td><td>0.93</td><td>1.27</td><td>1.62</td></tr><tr><td>EPS (diluted, pre-except) (Rmb)</td><td>1.56</td><td>0.91</td><td>1.24</td><td>1.58</td></tr><tr><td>EPS (basic, post-except) (Rmb)</td><td>1.53</td><td>1.05</td><td>1.40</td><td>1.77</td></tr><tr><td>EPS (diluted, post-except) (Rmb)</td><td>1.47</td><td>1.02</td><td>1.36</td><td>1.73</td></tr><tr><td>DPS (Rmb)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Div. payout ratio (%)</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

Growth & Margins (%)

<table><tr><td colspan="5">Growth &amp; Margins (%)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Total revenue growth</td><td>25.0</td><td>4.8</td><td>18.3</td><td>18.3</td></tr><tr><td>EBITDA growth</td><td>83.8</td><td>(35.3)</td><td>33.0</td><td>25.1</td></tr><tr><td>EPS growth</td><td>37.2</td><td>(30.5)</td><td>33.2</td><td>26.7</td></tr><tr><td>DPS growth</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>EBIT margin</td><td>10.5</td><td>5.5</td><td>6.6</td><td>7.2</td></tr><tr><td>EBITDA margin</td><td>12.4</td><td>7.6</td><td>8.6</td><td>9.1</td></tr><tr><td>Net income margin</td><td>9.1</td><td>5.0</td><td>5.8</td><td>6.3</td></tr></table>

Price Performance  
![](images/43718a7f8aa9aaad734738205a46805608258661ba3d555ff928250701c350de.jpg)  
Source: FactSet. Price as of 16 Jul 2026 close.

Balance Sheet (Rmb mn)

<table><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Cash &amp; cash equivalents</td><td>26,914.4</td><td>34,852.2</td><td>51,238.7</td><td>71,749.5</td></tr><tr><td>Accounts receivable</td><td>61,546.1</td><td>63,567.3</td><td>71,669.0</td><td>83,210.5</td></tr><tr><td>Inventory</td><td>80,989.5</td><td>88,082.8</td><td>100,709.1</td><td>118,601.2</td></tr><tr><td>Other current assets</td><td>85,360.8</td><td>85,360.8</td><td>85,360.8</td><td>85,360.8</td></tr><tr><td>Total current assets</td><td>254,810.8</td><td>271,863.1</td><td>308,977.8</td><td>358,922.1</td></tr><tr><td>Net PP&amp;E</td><td>27,950.3</td><td>36,504.1</td><td>45,549.0</td><td>55,533.9</td></tr><tr><td>Net intangibles</td><td>8,319.4</td><td>8,732.5</td><td>9,263.9</td><td>9,973.3</td></tr><tr><td>Total investments</td><td>87,149.5</td><td>94,149.5</td><td>101,149.5</td><td>108,149.5</td></tr><tr><td>Other long-term assets</td><td>129,866.0</td><td>129,866.0</td><td>129,866.0</td><td>129,866.0</td></tr><tr><td>Total assets</td><td>508,096.0</td><td>541,115.2</td><td>594,806.2</td><td>662,444.8</td></tr><tr><td>Accounts payable</td><td>146,051.4</td><td>148,794.3</td><td>160,202.4</td><td>175,010.7</td></tr><tr><td>Short-term debt</td><td>13,202.2</td><td>13,202.2</td><td>13,202.2</td><td>13,202.2</td></tr><tr><td>Short-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>33,151.9</td><td>33,115.2</td><td>35,495.1</td><td>38,446.3</td></tr><tr><td>Total current liabilities</td><td>192,405.5</td><td>195,111.7</td><td>208,899.7</td><td>226,659.2</td></tr><tr><td>Long-term debt</td><td>22,921.4</td><td>22,921.4</td><td>22,921.4</td><td>22,921.4</td></tr><tr><td>Long-term lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other long-term liabilities</td><td>26,445.8</td><td>26,628.4</td><td>26,820.1</td><td>27,021.5</td></tr><tr><td>Total long-term liabilities</td><td>49,367.2</td><td>49,549.8</td><td>49,741.6</td><td>49,942.9</td></tr><tr><td>Total liabilities</td><td>241,772.7</td><td>244,661.5</td><td>258,641.3</td><td>276,602.1</td></tr><tr><td>Preferred shares</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total common equity</td><td>266,218.7</td><td>296,349.1</td><td>336,060.3</td><td>385,738.1</td></tr><tr><td>Minority interest</td><td>104.6</td><td>104.6</td><td>104.6</td><td>104.6</td></tr><tr><td>Total liabilities &amp; equity</td><td>508,096.0</td><td>541,115.2</td><td>594,806.2</td><td>662,444.8</td></tr><tr><td>Net debt, adjusted</td><td>(71,572.9)</td><td>(79,510.7)</td><td>(95,897.3)</td><td>(116,408.0)</td></tr></table>

<table><tr><td colspan="5">Cash Flow (Rmb mn)</td></tr><tr><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Net income</td><td>41,643.4</td><td>24,089.5</td><td>32,963.6</td><td>42,294.9</td></tr><tr><td>D&amp;A add-back</td><td>8,756.7</td><td>10,206.8</td><td>11,514.9</td><td>12,506.0</td></tr><tr><td>Minority interest add-back</td><td>(77.0)</td><td>(51.3)</td><td>(51.3)</td><td>(25.7)</td></tr><tr><td>Net (inc)/dec working capital</td><td>(14,220.5)</td><td>(6,225.7)</td><td>(6,748.3)</td><td>(11,472.8)</td></tr><tr><td>Other operating cash flow</td><td>(1,960.3)</td><td>3,579.2</td><td>4,109.0</td><td>4,840.4</td></tr><tr><td>Cash flow from operations</td><td>34,142.4</td><td>31,598.5</td><td>41,787.8</td><td>48,142.8</td></tr><tr><td>Capital expenditures</td><td>(12,769.2)</td><td>(19,173.8)</td><td>(21,091.2)</td><td>(23,200.3)</td></tr><tr><td>Acquisitions</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Divestitures</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Others</td><td>(58,909.6)</td><td>(4,487.0)</td><td>(4,310.1)</td><td>(4,431.8)</td></tr><tr><td>Cash flow from investing</td><td>(71,678.7)</td><td>(23,660.7)</td><td>(25,401.3)</td><td>(27,632.1)</td></tr><tr><td>Repayment of lease liabilities</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Dividends paid (common &amp; pref)</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Inc/(dec) in debt</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other financing cash flows</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Cash flow from financing</td><td>30,789.3</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Total cash flow</td><td>(6,747.1)</td><td>7,937.8</td><td>16,386.6</td><td>20,510.8</td></tr><tr><td>Free cash flow</td><td>21,373.2</td><td>12,424.8</td><td>20,696.7</td><td>24,942.5</td></tr></table>

Source: Company data, GS estimates.

physical control layer. The model features large-scale pre-training involving 100k hours of real-world robot operation trajectories and 10k hours of cross-ontology post-training, which demonstrates a clean scaling behavior in VLM, and enables cross-ontology adaptation i.e. bipedal, quad, dual-arm, or wheeled systems. The model achieves state-of-the-art (SOTA) across multiple benchmarks (Exhibit 4), outperforming baseline open-source models such as Pi-0.5.

## Implications

Robotics: We see Xiaomi has completed the initial integration of its robotics framework across ontology/body, data and models, which may lead to a self-reinforcing loop (Exhibit 1) toward general-purpose industrial and domestic automation. We believe Xiaomi has clear advantages in deployment scenarios including its own manufacturing factories and a vast home AIoT ecosystem. Real-world deployment failures are analyzed and fed back into the scene generative model to synthesize similar edge-case scenarios; this synthetic data retrains the core foundation model, which is then redeployed to the physical hardware.

That said, we believe there remains a gap between Xiaomi and global leaders in real-world execution (e.g. Figure03 models deployed at BMW Group Plant Spartanburg demonstrated fast speed for similar tasks) and model capabilities (e.g. with closed-source models such as Physical Intelligence's Pi-0.7, Figure's Helix 02, Optimus, and Gemini Robotics 1.5). Meanwhile, Xiaomi has not disclosed detailed architecture, such as cost structure, performance parameters, etc.

AI monetization: As mentioned in our prior note, physical intelligence including embodied AI as one of the three monetization paths within Xiaomi's AI strategy. We expect Xiaomi Robotics to focus on more structured to-B commercial scenarios over the next 3-5 years, e.g. massive humanoid deployment at Xiaomi's factories (smart EV, smartphone and home appliance) and its partner factories, which resembles Tesla's strategy for Optimus in our view.

Valuation: Post +24% share price performance QTD (vs. +3% for HSTECH) partially thanks to favorable flow, the current market cap implies 1) 15x 2026E P/E or 14x 12m-fwd P/E on Xiaomi core ex. smart EV, AI and other new initiatives; 2) 1.3x 2026E P/S on smart EV (vs. 0.75x as of Jun-end) driven by stronger sentiment on the upcoming SkyNomad launch, compared to 0.8x average P/S multiple of its domestic peers (BYD, Li Auto, XPeng and NIO); we believe there remains valuation upside for Xiaomi EV considering the faster revenue growth (GSe Xiaomi EV revenue 30%+ yoy in 2026E/27E vs. peer average mid-teen %), as well as potentially improved visibility into 2027E sales post the SkyNomad launch over the next month or so; 3) 0 value on AI, robotics and other new initiatives. 3Q26 may provide a potential turnaround opportunity from both narrative and financial perspectives, in our view.

Exhibit 1: We see Xiaomi has completed the initial integration of its robotics framework across ontology, data and models

![](images/818e0b48c81f25e748463739fbfc9269b61210b19c697ea60e929bf289584ca1.jpg)  
Source: GS Global Investment Research

Exhibit 2: Xiaomi has entered the robotics industry since 2021  
Xiaomi Robotics milestones in 2026 by year

## Xiaomi Robotics milestones

2026 is the inflection point: Humanoids/dexterous hands, synthetic-data engines and robot foundation model start reinforcing each other

![](images/fad2dfb8ed49546bc56810c98b7cfadd79d714ab871d87e06584829f6b5c788c.jpg)  
Source: Company data, Data compiled by GS Global Investment Research

## Exhibit 3: Xiaomi Robotics has achieved early-stage integration of hardware ontology, data and models. Xiaomi Robotics milestones in 2026 by month

## Xiaomi Robotics milestones

2026 month-by-month: Integration of hardware ontology, data and models  
![](images/aa2a1105183464780ffb383c5947cbf833d29450a87e809539bb35b1ee4acd45.jpg)  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 4: Xiaomi-Robotics-1 achieves SOTA across multiple benchmarks e.g. RoboCasa and RoboDojo

<table><tr><td colspan="5">RoboCasa365</td><td colspan="5">RoboDojo-Sim</td></tr><tr><td>Rank</td><td>Company/Institute</td><td>Model</td><td>Release date</td><td>Score</td><td>Rank</td><td>Company/Institute</td><td>Model</td><td>Release date</td><td>Score</td></tr><tr><td>1</td><td>Xiaomi</td><td>Xiaomi-Robotics-1</td><td>Jul-26</td><td>57.4</td><td>1</td><td>Xiaomi</td><td>Xiaomi-Robotics-1</td><td>Jul-26</td><td>20.1</td></tr><tr><td>2</td><td>Alibaba</td><td>ABot-M0.6</td><td>Feb-26</td><td>46.6</td><td>2</td><td>Tencent</td><td>Hy-Embodied-0.5-VLA</td><td>Jun-26</td><td>13.1</td></tr><tr><td>3</td><td>Alibaba</td><td>ABot-M0.5</td><td>Feb-26</td><td>40.3</td><td>3</td><td>HKUST &amp; THU</td><td>Spatial Forcing</td><td>Oct-25</td><td>12.4</td></tr><tr><td>4</td><td>RLWRLD</td><td>RLDX-1</td><td>May-26</td><td>36.0</td><td>4</td><td>Physical Intelligence</td><td>π0.5</td><td>Apr-25</td><td>11.4</td></tr><tr><td>5</td><td>World Agents</td><td>WorldDreamer</td><td>Jun-26</td><td>35.3</td><td>5</td><td>AIR &amp; THU</td><td>X-VLA</td><td>Oct-25</td><td>10.1</td></tr><tr><td>6</td><td>Nvidia</td><td>GR00T N1.5</td><td>Mar-25</

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
