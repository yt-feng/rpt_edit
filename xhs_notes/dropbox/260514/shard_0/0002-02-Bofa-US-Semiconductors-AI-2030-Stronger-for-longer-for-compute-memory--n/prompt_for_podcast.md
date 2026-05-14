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
# US Semiconductors

# AI 2030: Stronger for longer for compute, memory, networking

Price Objective Change

# AI data center TAM now \~\$1.7Tn by CY30, +45% CAGR

In-line with our view of stronger AI infra capex outlook (see Q1 cloud capex takeaways), we update our CY30 AI data center systems TAM outlook to \~\$1.7Tn AI DC vs. \~\$1.4Tn prior. Despite ongoing concerns around capex sustainability and the ability to fund them, we believe: 1) 2026 will continue to be a year of accelerating AI sales and ROIs (OpenAI, Anthropic upcoming IPOs likely to provide improving prospects), while 2) 2027 could see improving tokenomics/efficiency as new architecture compute/memory systems ramp. While the current supply chain bottlenecks could limit shipment of leading-edge components, we believe key AI compute, networking, and memory vendors that have planned properly should continue to deliver and outperform.

# Diversification of compute/memory additive to AI TAM

Within our new \~\$1.7Tn TAM, we raise our AI accelerator outlook to \~\$1.2Tn from \~\$1.0Tn on increased hyperscaler custom ASIC shipments (such as Google TPU, AWS Trainium), data center server CPU outlook to \~\$110bn (AI CPUs \$88bn) from \~\$80bn, and AI networking outlook to \~\$316bn from \~\$240bn on ongoing optics/switch ramp. Importantly, we flag the ongoing diversification of compute/memory components as AI workload tails elongate, but we view this as additive to overall TAM, not replacing existing workloads/components. For instance, we expect CPUs (in their new standalone racks) to work in tandem with existing GPU-CPU compute racks, and SRAM-based ultra-low-latency memory racks to coexist with HBM-based GPU racks.

# Memory still attractive, MU \$950 PO on sum-of-parts

Despite recent runs in memory stocks, we expect memory demand to continue outgrowing supply driven by AI, memory pricing to generally hold up (supply/demand sufficiency ratio not expected to rise above 110%), and memory (MU) earnings to remain relatively stable through CY28. Given capital, packaging, and power limitations, we view memory supply elasticity as now structurally lower, and thus expect memory vendors (demand) to outperform equipment vendors (supply) over the medium term. Accordingly, we raise MU estimates and PO to \$950 from \$500 on a much stronger mid-term pricing outlook, now based on sum-of-parts that values: 1) sustainable AI/HBM business at \~\$240/sh (27x CY27 PE, in-line with AI compute peers), and 2) traditional cyclical DRAM/NAND business at \~\$710/sh (3.1x CY27 P/B, in-line with historical upcycle).

# Top picks: NVDA, AVGO, MU, AMD, MRVL

1) NVDA: top sector pick, raise est./PO to \$320 from \$300. Upcoming catalysts include earnings, Computex tradeshow (possible new CPU launch), Vera Rubin launch, and 2H return of cash, per our recent report. 2) AVGO: recent frame contracts with Google and Meta provide FY27 certainty with potential upside to consensus \$110bn AI sales, though we don't expect another raise on the next call. 3) MU: raise est./PO per above. 4) AMD: CPU strength, July analyst day event, potential for additional GW wins without warrant requirements. 5) MRVL: raise est./PO to \$200 from \$125 on continued 800G/1.6T optics ramps, broad custom silicon demand strength vs. mgmt's conservative MSFT program ramp outlook in CY27 (only \~\$600mn contribution vs. \$2bn supply).

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.
Refer to important disclosures on page 29 to 32. Analyst Certification on page 27. Price Objective Basis/Risk on page 24.
12973153

# 13 May 2026

Equity

United States

Semiconductors

Vivek Arya

Research Analyst

BofAS

vivek.arya@bofa.com

Duksan Jang

Research Analyst

BofAS

duksan.jang@bofa.com

Michael Mani

Research Analyst

BofAS

michael.mani@bofa.com

Liam Pharr

Research Analyst

BofAS

liam.pharr@bofa.com

# Exhibit 1: 2030 AI TAM estimate changes, top picks, recent PO changes

Top picks, new/recent PO changes

<table><tr><td colspan="2">2030 AI TAM Estimate Changes</td></tr><tr><td>May &#x27;26</td><td>$1.7Tn</td></tr><tr><td>Feb. &#x27;26</td><td>$1.4Tn</td></tr><tr><td>Dec. &#x27;25</td><td>$1.2Tn</td></tr><tr><td>Jun. &#x27;25</td><td>$823bn</td></tr></table>

<table><tr><td colspan="2">Top Picks</td></tr><tr><td>Compute:</td><td>NVDA, AVGO, AMD, MRVL</td></tr><tr><td>Memory:</td><td>MU</td></tr><tr><td>Networking:</td><td>CRDO, MTSI</td></tr></table>

<table><tr><td></td><td colspan="3">New PO Changes</td></tr><tr><td></td><td>OLD</td><td>NEW</td><td>Rating</td></tr><tr><td>AMD</td><td>$450</td><td>$500</td><td>BUY</td></tr><tr><td>COHR</td><td>$365</td><td>$400</td><td>NEUTRAL</td></tr><tr><td>MRVL</td><td>$125</td><td>$200</td><td>BUY</td></tr><tr><td>MU</td><td>$500</td><td>$950</td><td>BUY</td></tr><tr><td>NVDA</td><td>$300</td><td>$320</td><td>BUY</td></tr></table>

<table><tr><td colspan="4">Recent PO Changes</td></tr><tr><td></td><td>Old</td><td>New</td><td>Rating</td></tr><tr><td>ALAB</td><td>$200</td><td>$240</td><td>NEUTRAL</td></tr><tr><td>ARM</td><td>$180</td><td>$245</td><td>NEUTRAL</td></tr><tr><td>INTC</td><td>$56</td><td>$96</td><td>U/P</td></tr><tr><td>LITE</td><td>$775</td><td>$1,100</td><td>NEUTRAL</td></tr><tr><td>LSCC</td><td>$88</td><td>$105</td><td>U/P</td></tr><tr><td>MTSI</td><td>$305</td><td>$410</td><td>BUY</td></tr></table>

Source: BofA Global Research

BofA GLOBAL RESEARCH

See glossary on page 22-23

# Contents

AI 2030 TAM Outlook Update 3

MRVL, PO raise to \$200 from \$125 4

COHR, PO raise to \$400 from \$365 6

LITE, maintain \$1100 PO, raise ests 7

AMD, PO raise to \$500 from \$450 8

NVDA, PO raise to \$320 from \$300 8

Cloud/Carrier Capex Overview 10

Capex sustainability: demand signals increasingly positive 12

Memory: structural higher floor with AI 15

Memory content per AI system scales faster than compute 15

Structurally lower supply elasticity 16

DRAM/NAND Pricing Trends 18

MU Estimate Changes 18

MU Valuation Analysis, \$950 PO 19

Global Semis Forecast Update 20

Glossary 22

# AI 2030 TAM Outlook Update

Of the overall global IT spend of \~\$6.3Tn today, we believe data center systems to represent \$772bn across both AI and non-AI. By CY30, we expect TAM to grow toward \~\$2.0Tn, growing at +32% CAGR CY25-30 and outpacing overall IT spend at +9% CAGR.

# AI Data Center Systems: \~\$1.7Tn by CY30

For AI data center systems specifically, we now see TAM growing to \~\$1.7Tn by CY30 from \$264bn in CY25, with AI servers representing \~75% of TAM at \$1.3Tn, followed by networking at \~20% of TAM at \$316bn, and storage at \~5% of TAM at \$81bn.

- Within AI servers, we see AI accelerators to represent \~\$1.2Tn TAM by CY30 from just \$120bn in CY24 and \$197bn in CY25, or the vast majority of server spend.   
- We expect HBM to remain \~14-20% of overall accelerator spend, reaching \$168bn TAM by CY30, though likely declines toward the lower-end of the range as memory tier broadens and types diversify for agentic AI workloads.   
- We see overall server CPU to grow to \$110bn in CY30 from \~\$28bn in CY25 (+31% CAGR), while AI CPUs specifically could grow to \~\$88bn in CY30 from \$9bn in CY25 (+57% CAGR).   
- AI connectivity is expected to grow at a +45% CAGR to \$110bn in CY30 from \$17bn in CY25, driven by optical connectivity growing at +42% to \$88bn and copper connectivity growing at +61% to \$22bn.

For non-AI data center systems, we see TAM growth of a modest +7% CAGR.

Exhibit 2: We see AI Data Center Systems TAM to reach \~\$1.7Tn by CY30, +45% CAGR, with AI accelerators representing \~\$1.2Tn within that Data Center Systems TAM Breakout – AI vs. non-AI 

<table><tr><td>TAM ($bn)</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>CAGR &#x27;25-&#x27;30</td></tr><tr><td>Overall IT Spend (1)</td><td>$4,594.2</td><td>$4,693.0</td><td>$5,038.7</td><td>$5,563.8</td><td>$6,316.5</td><td>$6,985.3</td><td>$7,468.4</td><td>$8,085.5</td><td>$8,726.2</td><td>9%</td></tr><tr><td>Data Center Systems TAM ($bn) (2)</td><td>$227.1</td><td>$237.6</td><td>$333.5</td><td>$505.6</td><td>$772.4</td><td>$1,126.3</td><td>$1,490.3</td><td>$1,796.3</td><td>$2,041.5</td><td>32%</td></tr><tr><td>YoY (%)</td><td></td><td>5%</td><td>40%</td><td>52%</td><td>53%</td><td>46%</td><td>32%</td><td>21%</td><td>14%</td><td></td></tr><tr><td>AI Data Center Systems TAM ($bn)</td><td>$23.0</td><td>$63.2</td><td>$160.2</td><td>$264.1</td><td>$547.7</td><td>$865.7</td><td>$1,192.2</td><td>$1,482.2</td><td>$1,705.8</td><td>45%</td></tr><tr><td>YoY (%)</td><td></td><td>174%</td><td>154%</td><td>65%</td><td>107%</td><td>58%</td><td>38%</td><td>24%</td><td>15%</td><td></td></tr><tr><td>AI % of Overall IT Spend (1)</td><td>0.5%</td><td>1.3%</td><td>3.2%</td><td>4.7%</td><td>8.7%</td><td>12.4%</td><td>16.0%</td><td>18.3%</td><td>19.5%</td><td></td></tr><tr><td>AI % of Data Center Systems TAM (2)</td><td>10.1%</td><td>26.6%</td><td>48.0%</td><td>52.2%</td><td>70.9%</td><td>76.9%</td><td>80.0%</td><td>82.5%</td><td>83.6%</td><td></td></tr><tr><td>AI Servers</td><td>$16.3</td><td>$49.5</td><td>$130.4</td><td>$216.0</td><td>$425.1</td><td>$673.6</td><td>$927.9</td><td>$1,144.8</td><td>$1,308.5</td><td>43%</td></tr><tr><td>AI CPUs</td><td>$1.2</td><td>$2.1</td><td>$4.0</td><td>$9.3</td><td>$24.5</td><td>$40.8</td><td>$58.6</td><td>$72.5</td><td>$87.6</td><td>57%</td></tr><tr><td>AI Accelerators</td><td>$14.3</td><td>$45.0</td><td>$120.2</td><td>$196.5</td><td>$381.1</td><td>$603.2</td><td>$830.1</td><td>$1,026.1</td><td>$1,170.6</td><td>43%</td></tr><tr><td>HBM</td><td>$1.6</td><td>$4.2</td><td>$17.4</td><td>$34.5</td><td>$76.8</td><td>$105.5</td><td>$120.5</td><td>$139.9</td><td>$168.3</td><td>37%</td></tr><tr><td>HBM (% of Accelerators)</td><td>11%</td><td>9%</td><td>14%</td><td>18%</td><td>20%</td><td>17%</td><td>15%</td><td>14%</td><td>14%</td><td></td></tr><tr><td>Other (DDR/SSD/motherboard/power/etc.)</td><td>$0.8</td><td>$2.4</td><td>$6.2</td><td>$10.3</td><td>$19.5</td><td>$29.6</td><td>$39.1</td><td>$46.1</td><td>$50.3</td><td>37%</td></tr><tr><td>AI Networking</td><td>$5.6</td><td>$10.4</td><td>$21.6</td><td>$34.6</td><td>$95.3</td><td>$150.8</td><td>$207.5</td><td>$266.8</td><td>$316.1</td><td>56%</td></tr><tr><td>AI Switching (Back/Front-End)</td><td>$2.2</td><td>$4.6</td><td>$8.8</td><td>$12.5</td><td>$30.9</td><td>$52.6</td><td>$71.2</td><td>$103.9</td><td>$128.7</td><td>59%</td></tr><tr><td>AI SmartNIC</td><td>$0.9</td><td>$2.0</td><td>$3.3</td><td>$4.8</td><td>$23.5</td><td>$39.7</td><td>$59.0</td><td>$68.7</td><td>$77.6</td><td>75%</td></tr><tr><td>AI Connectivity/Other Networking</td><td>$2.5</td><td>$3.8</td><td>$9.5</td><td>$17.4</td><td>$40.9</td><td>$58.5</td><td>$77.4</td><td>$94.2</td><td>$109.8</td><td>45%</td></tr><tr><td>Optical</td><td>$1.9</td><td>$3.4</td><td>$8.6</td><td>$15.3</td><td>$35.8</td><td>$49.5</td><td>$62.3</td><td>$76.0</td><td>$87.7</td><td>42%</td></tr><tr><td>Electrical/Copper</td><td>$0.6</td><td>$0.4</td><td>$0.9</td><td>$2.1</td><td>$5.1</td><td>$9.0</td><td>$15.1</td><td>$18.2</td><td>$22.1</td><td>61%</td></tr><tr><td>DAC</td><td>$0.5</td><td>$0.4</td><td>$0.6</td><td>$0.8</td><td>$1.3</td><td>$1.8</td><td>$2.1</td><td>$2.4</td><td>$2.6</td><td>26%</td></tr><tr><td>ACC</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.4</td><td>$1.2</td><td>$2.1</td><td>$3.1</td><td>$6.0</td><td>180%</td></tr><tr><td>AEC</td><td>$0.1</td><td>$0.1</td><td>$0.2</td><td>$1.2</td><td>$3.4</td><td>$6.0</td><td>$10.9</td><td>$12.8</td><td>$13.6</td><td>62%</td></tr><tr><td>AI Storage</td><td>$1.1</td><td>$3.2</td><td>$8.2</td><td>$13.5</td><td>$27.3</td><td>$41.2</td><td>$56.8</td><td>$70.6</td><td>$81.2</td><td>43%</td></tr><tr><td>Non-AI Data Center TAM ($bn)</td><td>$204.1</td><td>$174.4</td><td>$173.3</td><td>$241.5</td><td>$224.8</td><td>$260.7</td><td>$298.1</td><td>$314.1</td><td>$335.7</td><td>7%</td></tr><tr><td>YoY (%)</td><td></td><td>-15%</td><td>-1%</td><td>39%</td><td>-7%</td><td>16%</td><td>14%</td><td>5%</td><td>7%</td><td></td></tr></table>

Source: BofA Global Research estimates, Gartner, Mercury Research, IDC, LightCounting, 650 Group

BofA GLOBAL RESEARCH

Exhibit 3: We expect NVDA to generally maintain \~65-70%+ AI accelerator share over time

AI accelerator (GPU/ASIC/XPU) potential sales power by vendor

<table><tr><td>AI Accelerator Sales Power</td><td>CY24</td><td>CY25</td><td>CY26E</td><td>CY27E</td><td>CY28E</td><td>CY29E</td><td>CY30E</td></tr><tr><td>Nvidia ($bn)</td><td>$102.2</td><td>$162.4</td><td>$295.2</td><td>$436.9</td><td>$585.4</td><td>$714.2</td><td>$800.0</td></tr><tr><td>YoY</td><td></td><td>59%</td><td>82%</td><td>48%</td><td>34%</td><td>22%</td><td>12%</td></tr><tr><td>Implied Share</td><td>85%</td><td>83%</td><td>77%</td><td>72%</td><td>71%</td><td>70%</td><td>68%</td></tr><tr><td>AMD ($bn)</td><td>$5.0</td><td>$6.6</td><td>$14.7</td><td>$32.1</td><td>$44.6</td><td>$63.4</td><td>$80.1</td></tr><tr><td>YoY</td><td></td><td>34%</td><td>122%</td><td>118%</td><td>39%</td><td>42%</td><td>26%</td></tr><tr><td>Implied Share</td><td>4%</td><td>3%</td><td>4%</td><td>5%</td><td>5%</td><td>6%</td><td>7%</td></tr><tr><td>Broadcom ($bn)</td><td>$9.3</td><td>$16.2</td><td>$47.2</td><td>$89.5</td><td>$135.3</td><td>$162.4</td><td>$181.9</td></tr><tr><td>YoY</td><td></td><td>75%</td><td>192%</td><td>89%</td><td>51%</td><td>20%</td><td>12%</td></tr><tr><td>Implied Share</td><td>8%</td><td>8%</td><td>12%</td><td>15%</td><td>16%</td><td>16%</td><td>16%</td></tr><tr><td>Marvell ($bn)</td><td>$0.7</td><td>$1.3</td><td>$1.5</td><td>$3.0</td><td>$4.3</td><td>$6.5</td><td>$8.8</td></tr><tr><td>YoY</td><td></td><td>87%</td><td>14%</td><td>99%</td><td>45%</td><td>49%</td><td>36%</td></tr><tr><td>Implied Share</td><td>1%</td><td>1%</td><td>0%</td><td>0%</td><td>1%</td><td>1%</td><td>1%</td></tr><tr><td>Others/TBD ($bn)</td><td>$3.1</td><td>$9.9</td><td>$22.4</td><td>$41.8</td><td>$60.4</td><td>$79.7</td><td>$99.8</td></tr><tr><td>YoY</td><td></td><td>219%</td><td>126%</td><td>86%</td><td>45%</td><td>32%</td><td>25%</td></tr><tr><td>Implied Share</td><td>3%</td><td>5%</td><td>6%</td><td>7%</td><td>7%</td><td>8%</td><td>9%</td></tr><tr><td>Total Market ($bn)</td><td>$120.2</td><td>$196.5</td><td>$381.1</td><td>$603.2</td><td>$830.1</td><td>$1,026.1</td><td>$1,170.6</td></tr><tr><td>YoY</td><td></td><td>63%</td><td>94%</td><td>58%</td><td>38%</td><td>24%</td><td>14%</td></tr></table>

Source: BofA Global Research estimates   
BofA GLOBAL RESEARCH

# MRVL: raise PO to \$200 from \$125

Along with our AI DC TAM model above, we raise our AI networking TAM forecast across the board for CY26-30. Specifically, we expect AI connectivity TAM to rise \~\$6bn-\$14bn over that time frame, with Ethernet Transceivers accounting for the majority of increase and CPOs also contributing modestly.

For CY27/28, we see Ethernet Transceivers TAM to increase \~\$7bn/\~\$10bn, benefiting MRVL who supplies DSPs, TIAs, laser/modulator drivers inside. We also raise CPO forecast where MRVL supplies silicon photonics PFs (photonic fabric) via Celstial AI.

Exhibit 4: We raise Ethernet Transceivers TAM by \~\$7bn/\~\$10bn in CY27/28E

AI Networking TAM Estimate Changes (New vs. Old Delta)

<table><tr><td colspan="7">Estimate Changes</td></tr><tr><td>Sales ($mn)</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>AI Networking</td><td>$0.8</td><td>$16.8</td><td>$27.9</td><td>$36.1</td><td>$54.4</td><td>$70.9</td></tr><tr><td>AI Switching (Back/Front-End)</td><td>($0.5)</td><td>$9.1</td><td>$18.8</td><td>$18.1</td><td>$32.4</td><td>$45.0</td></tr><tr><td>AI SmartNIC</td><td>$0.0</td><td>$2.2</td><td>$2.2</td><td>$7.6</td><td>$10.1</td><td>$11.6</td></tr><tr><td>AI Connectivity/Other Networking</td><td>$1.3</td><td>$5.6</td><td>$7.0</td><td>$10.3</td><td>$11.9</td><td>$14.2</td></tr><tr><td>Optical</td><td>$1.3</td><td>$5.7</td><td>$7.5</td><td>$11.0</td><td>$13.1</td><td>$15.2</td></tr><tr><td>AOC</td><td>$0.0</td><td>($0.1)</td><td>($0.2)</td><td>($0.2)</td><td>($0.4)</td><td>($0.3)</td></tr><tr><td>Ethernet Transceiver</td><td>$1.3</td><td>$5.5</td><td>$7.2</td><td>$10.2</td><td>$12.5</td><td>$14.8</td></tr><tr><td>100G</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td></tr><tr><td>200G</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td><td>$0.0</td></tr><tr><td>400G</td><td>$0.4</td><td>$0.6</td><td>$0.4</td><td>$0.2</td><td>$0.1</td><td>$0.0</td></tr><tr><td>800G</td><td>$0.8</td><td>$3.3</td><td>$4.1</td><td>$4.8</td><td>$3.7</td><td>$2.3</td></tr><tr><td>1.6T</td><td>$0.1</td><td>$1.5</td><td>$2.6</td><td>$4.7</td><td>$5.9</td><td>$6.4</td></tr><tr><td>3.2T</td><td>$0.0</td><td>$0.0</td><td>$0.1</td><td>$0.5</td><td>$2.9</td><td>$6.0</td></tr><tr><td>CPO</td><td>($0.0)</td><td>$0.2</td><td>$0.5</td><td>$1.1</td><td>$1.0</td><td>$0.8</td></tr><tr><td>LPO/LRO</td><td>$0.0</td><td>$0.1</td><td>($0.0)</td><td>($0.1)</td><td>($0.1)</td><td>($0.1)</td></tr><tr><td>Electrical/Copper</td><td>$0.0</td><td>($0.1)</td><td>($0.5)</td><td>($0.7)</td><td>($1.2)</td><td>($1.0)</td></tr><tr><td>DAC</td><td>$0.0</td><td>($0.0)</td><td>($0.1)</td><td>($0.1)</td><td>($0.2)</td><td>($0.1)</td></tr><tr><td>ACC</td><td>$0.0</td><td>($0.0)</td><td>($0.1)</td><td>($0.1)</td><td>($0.2)</td><td>($0.3)</td></tr><tr><td>AEC</td><td>$0.0</td><td>($0.1)</td><td>($0.4)</td><td>($0.5)</td><td>($0.8)</td><td>($0.6)</td></tr></table>

Source: BofA Global Research estimates   
BofA GLOBAL RESEARCH

# MRVL Impact: DSP, TIAs, drivers, CPO

MRVL's primary optics revenue source today is the DSP, which accounts for \~20-25% of the total BOM in 800G/1.6T optical transceivers. A \~\$10bn transceiver TAM increase in CY28 would translate to \~\$2bn in DSP TAM. We estimate MRVL can maintain \~60-70% share at these generations (800G/1.6T), potentially resulting in \~\$1.2bn+ of additional opportunities for MRVL DSPs.

Combined with MRVL's positioning in TIAs (\~5%+ of BOM), drivers (\~5%+ of BOM), we raise MRVL's non-CPO optics forecast for CY27/28, with a greater revision for CY28 given its increasing exposure/confidence to deliver 1.6T generation products.

Given our already previously strong MRVL optics forecast (+37%/+14% YoY in CY27/28E vs. cloud capex +25%/+10% YoY), we do not fully incorporate the TAM/share outlook rev

[中间内容因长度限制已省略]

ons, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first

obtaining express permission from an authorized officer of BofA.

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
