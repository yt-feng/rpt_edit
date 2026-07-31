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
# Cambricon Technology Corporation | Asia Pacific

# 2Q26 Preview: Delivery slippage clouds near-term upside; Keep OW

<table><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Cambricon Technology Corporation (688256.SS)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb1,528.00</td><td>Rmb1,408.00</td></tr></table>

We trim our estimates and lower our PT to Rmb1,408 as MLU580/590 deliveries have lagged expectations. We maintain our OW rating, supported by the structural growth outlook for China's domestic AI accelerator market.

2Q26 preview: modest delivery slippage prompts a small estimate cut. We expect Cambricon to report 2Q26 revenue of Rmb3.8bn (up 31% Q/Q) and EPS of Rmb2.09. We lower our prior revenue estimate by 2%, as supply-chain checks indicate slower-than-expected MLU580/590 deliveries. We attribute the shortfall mainly to production ramp, memory availability, and system-level delivery timing, rather than weaker underlying demand. However, slower order-to-revenue conversion suggests supply-chain execution remains a near-term constraint.

## The equity incentive plan appears more retention-oriented than a signal of

earnings potential. Cambricon plans to grant 5mn restricted shares at Rmb750 per share to 945 employees, covering 85% of staff. Revenue targets range from Rmb10.8bn–13.5bn in 2026 to Rmb47.6bn–59.5bn in 2028, while adjusted net profit is required to reach Rmb9.2bn in 2027 and Rmb13.8bn in 2028. As these targets are meaningfully below market expectations, we do not view them as management guidance. Instead, the broad coverage and discounted grant price suggest the plan is primarily an employee-retention mechanism.

## We remain constructive on China's domestic AI accelerator opportunity. We

recently raised our 2030 China AI chip TAM forecast to US\$91bn, implying a 23% CAGR over 2025–30 (see Raising China AI GPU TAM on recent geopolitical dynamics). WAIC 2026 (see our WAIC takeaways) also highlighted a shift in competition from standalone chips toward system-level scaling, with most vendors showcasing over 128-card SuperPod solutions. Prefill/decode disaggregation is also emerging as an important inference architecture, expanding the addressable market while raising requirements for system performance and software maturity.

Keep OW; lower PT to Rmb1,408. We cut our 2026/27/28E EPS by 6%/5%/8% to reflect slower deliveries and ongoing supply-chain uncertainty. Competition is also likely to intensify as peers launch new products in 2H26, testing Cambricon's relative performance and price-to-performance positioning. We nevertheless retain OW given the company's strategic position in China's domestic AI compute ecosystem and the structural growth outlook for local accelerator demand.

<table><tr><td colspan="2">Charlie Chan</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Charlie.Chan@morganstanley.com</td><td>+886 2 2730-1725</td></tr></table>

<table><tr><td colspan="2">Henry Zhao</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Henry.Zhao@morganstanley.com</td><td>+852 2239-7731</td></tr></table>

<table><tr><td colspan="2">Daniel Yen, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daniel.Yen@morganstanley.com</td><td>+886 2 2730-2863</td></tr></table>

<table><tr><td colspan="2">Daisy Dai, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Daisy.Dai@morganstanley.com</td><td>+852 2848-7310</td></tr></table>

<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td colspan="2">Tiffany Yeh</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td colspan="2">Lucas Wang</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Lucas.Wang@morganstanley.com</td><td>+886 2 2730-2875</td></tr></table>

Asia Summer School 2026

![](images/b77c6ddd0dd4eb21bc6f1a4856d4b293ecf905bf2d3a9c9a410dd113c3175ec0.jpg)

## Cambricon Technology Corporation (688256.SS, 688256 CG)

Greater China Technology Semiconductors | China

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>Rmb1,408.00</td></tr><tr><td>Up/downside to price target (%)</td><td>23</td></tr><tr><td>Shr price, close (Jul 29, 2026)</td><td>Rmb1,146.90</td></tr><tr><td>52-Week Range</td><td>Rmb1,620.00-449.66</td></tr><tr><td>Sh out, dil, curr (mn)</td><td>628</td></tr><tr><td>Mkt cap, curr (mn)</td><td>Rmb720,589.2</td></tr><tr><td>EV, curr (mn)</td><td>Rmb714,711.0</td></tr><tr><td>Avg daily trading value (mn)</td><td>Rmb13,346</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (Rmb)**</td><td>4.9</td><td>11.6</td><td>18.4</td><td>24.5</td></tr><tr><td>Prior EPS (Rmb)**</td><td>-</td><td>12.4</td><td>19.5</td><td>26.6</td></tr><tr><td>EPS (Rmb)§</td><td>-</td><td>10.5</td><td>16.9</td><td>27.0</td></tr></table>

Revenue, net (Rmb mn) 6,497.2 21,313.9 40,056.2 51,480.1

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

<table><tr><td>EBITDA (Rmb mn)</td><td>2,211.2</td><td>7,351.1</td><td>13,619.5</td><td>18,105.7</td></tr><tr><td>ModelWare net inc (Rmb mn)</td><td>2,059.2</td><td>6,859.4</td><td>11,641.7</td><td>15,447.5</td></tr><tr><td>P/E</td><td>186.8</td><td>96.9</td><td>62.2</td><td>46.9</td></tr><tr><td>P/BV</td><td>32.5</td><td>36.5</td><td>25.5</td><td>17.5</td></tr><tr><td>RNOA (%)</td><td>57.8</td><td>92.4</td><td>100.3</td><td>123.6</td></tr><tr><td>ROE (%)</td><td>37.9</td><td>57.9</td><td>64.0</td><td>54.5</td></tr><tr><td>EV/EBITDA</td><td>171.3</td><td>96.9</td><td>51.6</td><td>38.3</td></tr><tr><td>Div yld (%)</td><td>0.0</td><td>0.1</td><td>0.2</td><td>0.3</td></tr><tr><td>FCF yld ratio (%)*</td><td>0.8</td><td>0.4</td><td>1.5</td><td>1.7</td></tr><tr><td>Leverage (EOP) (%)</td><td>(49.6)</td><td>(44.0)</td><td>(61.2)</td><td>(66.6)</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare framework  
§ = Consensus data is provided by Refinitiv Estimates  
\*\* = Based on consensus methodology  
e = MS estimates

AlphaSignals Earnings Preview

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">Cambricon Technology Corporation 688256.SS</td></tr><tr><td>Revenue Q/Q growth</td><td>↓ Likely downside surprise</td><td>↓ Modest revision lower</td></tr><tr><td colspan="3">*Likely impact to consensus EPS is for the next 12 monthsSource: Company data, MS</td></tr></table>

# China – AI accelerators: Localization gains traction amid robust AI infrastructure spending

China's AI compute industry can be globally competitive, given strong system design and infrastructure

More broadly, we believe China's AI GPU race is no longer solely a chip-specification contest. While domestic silicon still trails the US by roughly two generations at the chip level, the effective gap is narrowing through multi-die design, advanced packaging, rack-scale system architecture, optical networking, and software-hardware co-optimization. This is why we think system-level competitiveness matters more than ever. In a market that is increasingly dominated by inference and utilization, vendors that deliver the most attractive real-world token economics at an acceptable software migration cost are likely to capture customer budgets, even without access to leading-edge process technology.

From an investment perspective, this leads to a simple conclusion: the sector should not be valued as a monolithic policy theme. Instead, investors should differentiate among vendors based on their ability to achieve shipment scale, ecosystem credibility, and pricing discipline, and those that may struggle to convert technical potential into durable revenues and margins. We therefore evaluate the group through a two-dimensional framework of economics × execution, combining TCO, token cost, TPS, and performance-per-dollar with qualitative factors such as foundry access, software ecosystem maturity, CSP relationships, and roadmap credibility. In our view, this framework remains the most effective way to distinguish likely long-term winners from those that may struggle to translate technical capabilities into sustainable revenue and margin growth as the industry consolidates.

What has become clearer through our recent channel checks is that economics, not ideology, is driving adoption. At our China Summit, major LLM developers indicated they are willing to deploy local GPUs as long as token cost is competitive. This aligns with our core finding that domestic accelerators already offer materially lower TCO than Nvidia products available in China, and that leading Chinese chips can achieve broad cost-per-token parity in inference workloads. In other words, purchasing decisions are increasingly driven by deployment economics rather than absolute peak silicon performance. This matters because China's AI demand is becoming more inference-heavy, more recurring, and more utilization-driven, structurally favoring solutions optimized for cost efficiency, software adaptation, and availability rather than headline benchmark leadership.

Exhibit 1: Relative strengths of US and China AI industries  
![](images/313b69d84743c71e68b433899606d822aca0ed66e5e3365b0a3d92731037350e.jpg)  
Source: MS

Exhibit 2: Domestic chips have lower TCO and comparable per token cost (AI LLM inference) vs. NVIDIA's processors for China  
![](images/863530895197b527e12a2859249d7725eba7a8181174b08676f021776fad87b2.jpg)  
Source: Company data, MS estimates

## China AI GPU TAM

China's AI GPU demand is concentrated among a small number of large buyer groups, whose capex decisions ultimately define the size of the addressable market.

\- The first group comprises China's CSPs – including ByteDance, Alibaba and Tencent – which procure AI chips both to train and run inference on proprietary models and to deploy AI infrastructure for external cloud customers.

\- The second group includes China's telecom operators, SOEs and municipal governments – the so-called sovereign-AI buyers – where demand is driven by national AI infrastructure build-out, data sovereignty, and public-sector applications.

\- AI start-ups (e.g., DeepSeek, MiniMax) and auto OEMs (e.g., Xpeng, Xiaomi) also procure AI chips, although their purchase volumes currently remain smaller than those of the first two groups.

We forecast China's AI chip TAM to reach US\$91bn by 2030, up 36% from our previous estimate of US\$67bn previously, implying a 23% CAGR over 2025-30. The upward revision is driven primarily by the following factors:

\- We added a new category (China CSP's overseas AI data center using domestic GPUs). In the short term, China CSPs may turn to more GPU rental to fulfill the strong computing demand, while in the medium to longer term, we believe domestic Chinese AI GPUs could see adoption in overseas deployments.

Accordingly, we assume no contribution from this category until 2027, but expect domestic GPUs to account for 3%/10%/20% of overseas AI infrastructure capex in 2028/29/30, respectively.

\- Bytedance reportedly is planning to sharply increase its capital spending in 2026 and 2027 to strengthen its position in the domestic AI market and expand internationally – reports indicate 2027 capex could reach US\$100 bn if economic and business conditions are favourable; we assume US\$80bn (approximately Rmb542bn) in our model to remain conservative.

\- We added Kingsoft Cloud to our database. Its capex increased significantly to Rmb3bn, with full-year 2026 capital investments projected to exceed Rmb15-20bn to meet explosive AI and cloud demand.

\- We revised up sovereign and SOE-related TAM assumptions to US\$9bn, up from US\$7bn previously. Recent media reports (Bloomberg, Jun 9) indicated that China is considering up to Rmb2tn of investment over the next five years for building data centres across the country. While we have not yet seen detailed policy guidance, we believe SOEs and local governments are likely to increase spending on AI infrastructure over time.

We expect China's AI chip self-sufficiency to rise from $42\%$ in 2025 to $70\%$ in 2030e. We expect leading-node capacity expansion and continued chip-performance improvement to drive domestic AI-chip revenue growth.

Exhibit 3: We expect China AI chip TAM to grow to US\$91bn by 2030E  
![](images/80d1ced5d45e20cc5891ce229a490e5c32a1fa78aa228f2b2ced38700394291a.jpg)  
Source: Company data, MS (E) estimates

Exhibit 4: We expect China AI chip self-sufficiency to reach 70% in 2030E  
![](images/233d937669eda3054145bad9338dc12e65e7db9f5b61c03f59a3ad8c21e3cb5d.jpg)  
Source: Company data, MS (e) estimates

Exhibit 5: Nvidia's 5090 price continues to rise in China  
![](images/bddf567c8cda2b162680cef25f712948d891cf43ded35c1a8c236dd8631f6c3a.jpg)  
Source: Taobao, MS

Exhibit 6: Average token price for China's mainstream AI LLMs  
![](images/51f5c2d58c6e2a074147e03acf0c73e5f43cf8ad3a67183fca5ab62219bb2097.jpg)  
Source: Company data, MS

Exhibit 7: Surge in ByteDance (Volcano Engine/Doubao) tokens indicates high AI demand  
![](images/428ead4097bf8606fd30e6d78e59213373c0ea1d8cb01550ea206b539a781836.jpg)  
Source: Company data, MS. ByteDance numbers represent monthly run-rate based on daily numbers.

Exhibit 8: Chinese CSP's capex will be a key demand driver for China's AI GPU  
![](images/d5c71be5f234308eb150a6429d921c41642f4e34776d6f563c49989d2ad621f2.jpg)  
Source: Company data, MS (E) estimates

## Earnings estimate revisions and quarterly financials

We lower our revenue forecasts by 2%/5%/8% for 2026, 2027 and 2028: This primarily reflects slower-than-expected deliveries of MLU580/590, as our supply-chain checks suggest that production ramp-up, component availability and system-level delivery remain less mature than we previously assumed. While underlying demand for domestic AI accelerators remains robust, we now expect a slower conversion of customer orders into recognized revenue, particularly through 2H26 and into 2027. With regard to profitability, we maintain our gross margin assumptions unchanged at 51%, 50% and 49% for 2026–28. As a result, we reduce our EPS estimates by 6%, 5% and 8% for 2026, 2027 and 2028, respectively.

Exhibit 9: Cambricon: Earnings estimate revisions

<table><tr><td>US$ mn</td><td>New &#x27;26</td><td>Old&#x27;26E</td><td>Diff.</td><td>New &#x27;27</td><td>Old&#x27;27E</td><td>Diff.</td><td>New &#x27;28</td><td>Old&#x27;28E</td><td>Diff.</td></tr><tr><td>Net sales</td><td>21,314</td><td>22,869</td><td>-7%</td><td>40,056</td><td>42,274</td><td>-5%</td><td>51,480</td><td>55,971</td><td>-8%</td></tr><tr><td>Gross profit</td><td>10,858</td><td>11,637</td><td>-7%</td><td>19,908</td><td>21,011</td><td>-5%</td><td>25,344</td><td>27,558</td><td>-8%</td></tr><tr><td>Operating profit</td><td>7,351</td><td>7,868</td><td>-7%</td><td>13,619</td><td>14,374</td><td>-5%</td><td>18,106</td><td>19,682</td><td>-8%</td></tr><tr><td>Pretax Income</td><td>7,258</td><td>7,776</td><td>-7%</td><td>13,696</td><td>14,451</td><td>-5%</td><td>18,173</td><td>19,750</td><td>-8%</td></tr><tr><td>Net income</td><td>6,859</td><td>7,332</td><td>-6%</td><td>11,642</td><td>12,283</td><td>-5%</td><td>15,448</td><td>16,788</td><td>-8%</td></tr><tr><td>EPS for consensus</td><td>11.64</td><td>12.39</td><td>-6%</td><td>18.44</td><td>19.45</td><td>-5%</td><td>24.46</td><td>26.59</td><td>-8%</td></tr><tr><td colspan="10">Margins</td></tr><tr><td>Gross margin</td><td>50.9%</td><td>50.9%</td><td></td><td>49.7%</td><td>49.7%</td><td></td><td>49.2%</td><td>49.2%</td><td></td></tr><tr><td>Operating margin</td><td>34.5%</td><td>34.4%</td><td></td><td>34.0%</td><td>34.0%</td><td></td><td>35.2%</td><td>35.2%</td><td></td></tr><tr><td>Pretax margin</td><td>34.1%</td><td>34.0%</td><td></td><td>34.2%</td><td>34.2%</td><td></td><td>35.3%</td><td>35.3%</td><td></td></tr><tr><td>Net margin</td><td>32.2%</td><td>32.1%</td><td></td><td>29.1%</td><td>29.1%</td><td></td><td>30.0%</td><td>30.0%</td><td></td></tr><tr><td>Opex %</td><td>16.5%</td><td>16.5%</td><td></td><td>15.7%</td><td>15.7%</td><td></td><td>14.1%</td><td>14.1%</td><td></td></tr></table>

Source: MS (e) estimates

Exhibit 10: Cambricon: Quarterly financials

<table><tr><td>(Rmb mn)</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total revenues</td><td>1,111.4</td><td>1,769.2</td><td>1,726.8</td><td>1,889.8</td><td>2,884.7</td><td>3,777.4</td><td>5,678.2</td><td>8,973.6</td><td>6,497.2</td><td>21,313.9</td><td>40,056.2</td><td>51,480.1</td></tr><tr><td>Q/Q Change</td><td>12.4%</td><td>59.2%</td><td>-2.4%</td><td>9.4%</td><td>52.6%</td><td>30.9%</td><td>50.3%</td><td>58.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Y/Y Change</td><td>4229.6%</td><td>4424.9%</td><td>1332.5%</td><td>91.0%</td><td>159.6%</td><td>113.5%</td><td>228.8%</td><td>374.8%</td><td>453.2%</td><td>228.0%</td><td>87.9%</td><td>28.5%</td></tr><tr><td>Cost of Sales</td><td>489.1</td><td>780.5</td><td>790.2</td><td>854.0</td><td>1,317.4</td><td>1,813.1</td><td>2,839.0</td><td>4,486.7</td><td>2,913.9</td><td>10,456.3</td><td>20,147.9</td><td>26,136.0</td></tr><tr><td>Percent of Revenues</td><td>44%</td><td>44%</td><td>46%</td><td>45%</td><td>46%</td><td>48%</td><td>50%</td><td>50%</td><td>45%</td><td>49%</td><td>50%</td><td>51%</td></tr><tr><td>Gross Profit</td><td>622.3</td><td>988.7</td><td>936.6</td><td>1,035.7</td><td>1,567.3</td><td>1,964.3</td><td>2,839.2</td><td>4,486.9</td><td>3,583.3</

[中间内容因长度限制已省略]

></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$136.80</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$442.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$203.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb68.01</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$3,235.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb705.99</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$328.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb706.39</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb91.69</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,515.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb100.74</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$375.50</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$67.20</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,205.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$110.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$133.00</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$291.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$136.90</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb56.05</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb90.00</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb29.90</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb284.00</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$39.48</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb71.68</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$23.30</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb90.39</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb82.45</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb64.86</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb23.57</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb87.60</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$607.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,305.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$12,910.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$91.80</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$148.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb97.28</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb364.03</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$91.80</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$269.60</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb207.50</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$491.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$106.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$561.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$49.55</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$697.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb52.59</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$118.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$105.50</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$183.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb107.51</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb329.63</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$890.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$485.50</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$11.64</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$5,620.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$4,790.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$209.68</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$5,290.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
