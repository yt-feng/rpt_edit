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
# JPM

## ASMPT Ltd (0522)

## ASMPT: Strong operating leverage, TCB continues to grow, and Photonics becoming a new driver; Stay OW

ASMPT's 2Q26 results and 3Q26 guidance were both well ahead of street consensus, helped by strong operating leverage, recovery in mainstream SEMI/SMT business and continued strong momentum in TCB and Photonics. 1H26 results are impressive, given Memory TCB revenues have been in decline YoY due to delay in HBM4-related shipments to a major Korean customer. Looking ahead, we expect Memory TCB revenues to accelerate, while C2S logic TCB revenues from OSAT customers should accelerate meaningfully. In addition, Photonics is also likely to grow meaningfully, led by pluggable optical transceiver growth. We raise our 2026/27/28 EPS estimates by $7\% / 12\% / 9\%$ to reflect stronger revenue traction and better OP leverage and remain OW with an unchanged Jun-27 PT of HK\$225. Key catalysts from here on are (1) an acceleration of memory TCB orders and billings, (2) increased presence in Logic C2W as AI accelerators adopt Chiplets and SoIC packaging, (3) further growth in Optics packaging.

\- Strong TCB bookings led by Logic, C2W could be the next big breakthrough: ASMPT highlighted strong logic TCB momentum, with more than 50 TCB tools received for C2S from leading OSAT customers in July, supporting its 3Q26 bookings (guiding high-single-digit sequential growth). We believe the demand for C2S will continue to strengthen as OSATs' record high capex translates into equipment investment, with ASMPT capturing close to $100\%$ market share in the space. Looking ahead, we believe C2W could experience a big breakthrough, with more accelerators migrating to SoIC-based Chiplet packaging, which will mandate the use of TCB for the C2W step in CoWoS, to mitigate warpage for large package sizes. AMD MI450 is the first product moving in this direction, but we believe that 2H27 could see a bigger migration as SoIC demand picks up. Intel's EMIB-T is also likely to be a key driver for C2S demand, given that embedded die placement within substrates will require high-intensity fine-pitch TCB tools, in addition to the final C2S step. In the next 2 years, we expect logic TCB to remain the main driver for TCB growth, as C2W becomes a major new vector of growth.

\- Memory TCB growth should restart in 2H26 with HBM4 orders; JEDEC relaxation could extend growth trajectory: Given the delay of HBM4 tool shipment to a major Korean customer, ASMPT's memory TCB revenues have declined YoY in 1H26 (Korea revenues down $65\%$ YoY). However, we believe memory TCB should regain momentum in 2H26, as HBM4 orders from the major Korean customercommence shipping, with continued strength entering 2027. Management also mentioned the potential stacking relaxation from JEDEC (loosen to 900-micron from current 775-micron standard), which could lead to a TCB lifecycle likely extending from HBM4 to HBM5. Based on our checks, we also see companies looking to reduce stack height for future HBM generations (e.g. some versions of NVDA Rubin and AMD MI450 could adopt 8 Hi HBM4, while 16 Hi is likely to remain niche even for HBM4e), which may limit the demand upside for TCB tools. ASMPT continues to engage with a leading memory maker (we believe SEC) for a joint evaluation program on HBM5 technology standard, using TCB, in our view. We view this as a positive signal for the adoption of its fluxless TCB in future HBM generations, cementing ASMPT's position with key Korean customers (JPMe

Sources for: Style Exposure – JPM Global Markets Strategy; all other tables are company data and JPM estimates.

## Overweight

0522.HK, 522 HK
Price (29 Jul 26):HK\$136.90

Price Target (Jun-27): HK\$225.00

## Technology and Telecoms

Gokul Hariharan AC
(852) 2800-8564
gokul.hariharan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jennifer Hsieh
(886-2) 2725-9868
jennifer.hsieh@JPM.com
JPM Securities (Taiwan) Limited

(886-2) 2725-9618
david.chou@JPM.com
JPM Securities (Taiwan) Limited

Jason Chen
(886-2) 2725-9864
jason.bh.chen@JPM.com
JPM Securities (Taiwan) Limited

Subham Singhania
(91-22) 6157-3801
subham.singhania@JPM.com
JPM India Private Limited

<table><tr><td colspan="4">Key Changes (FYE Dec)</td></tr><tr><td></td><td>Prev</td><td>Cur</td><td>Δ</td></tr><tr><td>Adj. EPS - 26E (HK$)</td><td>4.27</td><td>4.58</td><td>7.3%</td></tr><tr><td>Adj. EPS - 27E (HK$)</td><td>6.56</td><td>7.36</td><td>12.0%</td></tr></table>

<table><tr><td colspan="4">Adj. EPS (HK$)</td></tr><tr><td></td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Q1</td><td>0.20</td><td>0.61A</td><td>1.54</td></tr><tr><td>Q2</td><td>0.31</td><td>0.80A</td><td>1.78</td></tr><tr><td>Q3</td><td>(0.65)</td><td>1.53</td><td>2.14</td></tr><tr><td>Q4</td><td>2.29</td><td>1.64</td><td>1.89</td></tr><tr><td>FY</td><td>2.16</td><td>4.58</td><td>7.36</td></tr></table>

Style Exposure

<table><tr><td rowspan="2">Quant Factors</td><td rowspan="2">Current %Rank</td><td colspan="4">Hist %Rank (1=Top)</td></tr><tr><td>6M</td><td>1Y</td><td>3Y</td><td>5Y</td></tr><tr><td>Value</td><td>52</td><td>49</td><td>49</td><td>49</td><td>66</td></tr><tr><td>Growth</td><td>8</td><td>58</td><td>42</td><td>60</td><td>65</td></tr><tr><td>Momentum</td><td>2</td><td>82</td><td>96</td><td>16</td><td>74</td></tr><tr><td>Quality</td><td>82</td><td>84</td><td>85</td><td>40</td><td>37</td></tr><tr><td>Low Vol</td><td>77</td><td>60</td><td>75</td><td>66</td><td>83</td></tr></table>

See page 12 for analyst certification and important disclosures, including non-US analyst disclosures.

Price Performance  
![](images/a348b8044b94b7f90dac13eec77f57916f25a1da80c86be17b75275004fd787a.jpg)

— 0522.HK Price (HK\$) — HSI (rebased)

<table><tr><td></td><td>YTD</td><td>1m</td><td>3m</td><td>12m</td></tr><tr><td>Abs</td><td>76.8%</td><td>-36.9%</td><td>-16.8%</td><td>97.4%</td></tr><tr><td>Rel</td><td>76.1%</td><td>-49.0%</td><td>-15.6%</td><td>96.3%</td></tr></table>

## Company Data

<table><tr><td>Shares O/S (mn)</td><td>411</td></tr><tr><td>52-week range (HK$)</td><td>244.40-64.65</td></tr><tr><td>Market cap ($ mn)</td><td>7,172</td></tr><tr><td>Exchange rate</td><td>7.84</td></tr><tr><td>Free float (%)</td><td>75.2%</td></tr><tr><td>3M ADV (mn)</td><td>4.51</td></tr><tr><td>3M ADV ($ mn)</td><td>107.2</td></tr><tr><td>Volatility (90 Day)</td><td>83</td></tr><tr><td>Index</td><td>HSI</td></tr><tr><td>BBG ANR (Buy | Hold | Sell)</td><td>18|3|0</td></tr></table>

Key Metrics (FYE Dec)

<table><tr><td>HK$ in millions</td><td>FY25A</td><td>FY26E</td><td>FY27E</td><td>FY28E</td></tr><tr><td colspan="5">Financial Estimates</td></tr><tr><td>Revenue</td><td>14,146</td><td>19,615</td><td>24,586</td><td>27,281</td></tr><tr><td>Adj. EBIT</td><td>541</td><td>2,729</td><td>3,829</td><td>4,607</td></tr><tr><td>Adj. EBITDA</td><td>1,103</td><td>3,165</td><td>4,388</td><td>5,216</td></tr><tr><td>Adj. net income</td><td>902</td><td>1,916</td><td>3,079</td><td>3,699</td></tr><tr><td>Adj. EPS</td><td>2.16</td><td>4.58</td><td>7.36</td><td>8.84</td></tr><tr><td>BBG EPS</td><td>0.78</td><td>3.94</td><td>5.93</td><td>7.44</td></tr><tr><td>Cashflow from operations</td><td>121</td><td>3,439</td><td>2,768</td><td>3,312</td></tr><tr><td>FCFF</td><td>(411)</td><td>2,989</td><td>2,030</td><td>2,493</td></tr><tr><td colspan="5">Margins and Growth</td></tr><tr><td>Revenue Growth Y/Y (%)</td><td>6.9%</td><td>38.7%</td><td>25.3%</td><td>11.0%</td></tr><tr><td>EBIT margin</td><td>3.8%</td><td>13.9%</td><td>15.6%</td><td>16.9%</td></tr><tr><td>EBIT Growth Y/Y (%)</td><td>(3.1%)</td><td>404.6%</td><td>40.3%</td><td>20.3%</td></tr><tr><td>EBITDA margin</td><td>7.8%</td><td>16.1%</td><td>17.8%</td><td>19.1%</td></tr><tr><td>EBITDA Growth Y/Y (%)</td><td>(4.7%)</td><td>187.0%</td><td>38.6%</td><td>18.9%</td></tr><tr><td>Net margin</td><td>6.4%</td><td>9.8%</td><td>12.5%</td><td>13.6%</td></tr><tr><td>Adj. EPS growth</td><td>160.2%</td><td>111.7%</td><td>60.7%</td><td>20.1%</td></tr><tr><td colspan="5">Ratios</td></tr><tr><td>Adj. tax rate</td><td>10.9%</td><td>26.2%</td><td>25.7%</td><td>25.5%</td></tr><tr><td>Interest cover</td><td>14.4</td><td>664.0</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/Equity</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>Net debt/EBITDA</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>ROE</td><td>5.6%</td><td>10.5%</td><td>14.8%</td><td>15.5%</td></tr><tr><td colspan="5">Valuation</td></tr><tr><td>FCFF yield</td><td>(0.7%)</td><td>5.2%</td><td>3.5%</td><td>4.4%</td></tr><tr><td>Dividend yield</td><td>0.4%</td><td>0.6%</td><td>1.3%</td><td>0.0%</td></tr><tr><td>EV/Revenue</td><td>3.8</td><td>2.6</td><td>2.0</td><td>1.7</td></tr><tr><td>EV/EBITDA</td><td>49.0</td><td>15.9</td><td>11.2</td><td>9.0</td></tr><tr><td>Adj. P/E</td><td>63.3</td><td>29.9</td><td>18.6</td><td>15.5</td></tr></table>

## Summary Investment Thesis and Valuation

## Investment Thesis

We are OW on ASMPT, given we expect continued growth in Advanced Packaging and a strong recovery in mainstream SEMI and SMT solutions, driven by AI server boards and PMICs. Looking ahead, we expect memory TCB revenue to accelerate as HBM4 orders from a major Korean customer commence shipping and potential stacking relaxation from JEDEC likely extend the TCB life cycle. We believe C2S logic TCB revenue from OSAT customers to accelerate meaningfully with Intel's EMIB-T likely to be a key driver for C2S demand, given embedded die placement within substrates will require a high intensity of fine-pitch TCB tools. Moreover, we see bigger breakthroughs for C2W as SoIC adoption picks up in 2H27. Photonics is also likely to grow substantially, led by pluggable optical transceiver growth, while ASMPT is well positioned for CPO to capture more value in the TAM expansion as the adoption ramps up in the long term. With strong operating leverage coming through due to disciplined cost control, we see strong earnings growth ahead for ASMPT.

## Valuation

Our Jun-27 PT of HK\$225 is based on \~28x 12M forward EPS, two notches lower than the previous target multiple, while we raise our 27/28 EPS estimates by 12%/9% to reflect stronger revenue traction and better OP leverage.

![](images/9c38c28891a9daa35094122c5bbfa95ba47db2d7489fb64aa9dccacee0196db4.jpg)

<table><tr><td>Factors</td><td>6M Corr</td><td>1Y Corr</td></tr><tr><td>Market: MSCI Asia Pac ex JP</td><td>0.60</td><td>0.55</td></tr><tr><td>Region: Hong Kong</td><td>-0.30</td><td>-0.09</td></tr><tr><td>Macro:</td><td></td><td></td></tr><tr><td>Citi Economic Surprise - EM</td><td>-0.37</td><td>-0.38</td></tr><tr><td>JPM Global Equity Sentiment</td><td>0.39</td><td>0.30</td></tr><tr><td>JPM GBI-EM Global Div</td><td>-0.22</td><td>-0.18</td></tr><tr><td>Quant Styles:</td><td></td><td></td></tr><tr><td>DivYld</td><td>-0.42</td><td>-0.31</td></tr><tr><td>Value</td><td>-0.41</td><td>-0.26</td></tr><tr><td>Growth</td><td>0.44</td><td>0.23</td></tr></table>

30-35% market share).

\- Photonics a new growth driver, led by pluggable now; well positioned in CPO: ASMPT stated that its Photonics revenue has reached US\$75mn in 1H26 (tripled YoY) and outlined its involvement in several process steps for pluggable transceivers (SMT for DSP and passive component attach and SEMI for transceiver attach, chip-on-submount assembly, and electrical/optical accessories) and CPO (SEMI for EIC on PIC, optical engines on substrate, and FAU/micro-lens attach). While the revenue is primarily driven by 800G/1.6T pluggable transceivers at the moment, we believe ASMPT is well positioned in CPO, as ASMPT Amicra is a dominant player in pluggable transceivers die-attach and the company has already engaged with several leading CPO players on TCB, Hybrid Bonding and Ultra-precision photonics solutions. We thus expect ASMPT's die-attach TAM to likely grow 2-3x in the next 2-3 years, as the industry embraces more CPO solutions.

\- Mainstream SEMI solutions growing rapidly, led by rising OSAT utilization: Mainstream SEMI (including wire bond and die bonders) grew substantially in 1H26, supported by high utilization at leading OSATs. The primary drivers are rising AI-peripheral demand (e.g., power management) along with a recovery in traditional applications (consumer, industrial, and auto). Management expects strength across both AI and traditional segments to carry into 2H26. While we have not seen a broad-based recovery in mainstream end demand, tight OSAT supply should continue to support expansion even in mainstream, as AI demand crowds out capacity. We now expect mainstream SEMI to grow $59\% / 15\%$ in 2026/27.

\- Strong OP leverage coming through, should continue for the next few quarters: ASMPT delivered strong operating leverage in 2Q26, with OPM reaching \~16% (revenue up 24% QoQ while operating profit more than doubled QoQ)—significantly above our and consensus expectations of 10.6% and 10.2%, respectively. We expect ASMPT to continue benefiting from robust operating leverage over the next several quarters, underpinned by strong revenue growth and tighter OPEX control, despite 2H26 OPEX likely to increase HoH given commission expenses. Accordingly, we raise our OPM estimates to 14%/16%/17% for 2026/27/28 and lift our 2026/27/28 EPS estimates by 7–12% to reflect stronger revenue traction and improved operating leverage.

\- Strategic options still open for SMT, recent improvement in backlog should result in a higher exit valuation: ASMPT's SMT continues to show strong results in 2Q26, with bookings hitting a record-high in 2Q26, primarily driven by AI server demand with a decent recovery in mainstream sectors. We expect SMT revenue momentum to keep strengthening in the near term (JPMe $31\%$ YoY in 2026) as the backlog gets delivered. We believe that the company is still exploring strategic options for the SMT business and recent improvements in both billing and backlog should imply a higher exit valuation. The disposal proceeds should support ASMPT's accelerated investments in Advanced Packaging and other rapid-growing segments in SEMI, in our view.

# Key charts and tables

HK\$ in millions, %  
Figure 1: ASMPT annual revenue and yoy trend  
![](images/f27b067e2c8146d9a1639d8285d87de2b2126698206569dc06a1387c76fd6181.jpg)  
Source: Company data and JPM estimates.

Figure 2: ASMPT quarterly revenue and yoy trend  
![](images/ea43bcd78501a8b6b08c1d1634a66544360a7061da562acbf88eb3462eb009b6.jpg)  
Source: Company data and JPM estimates.

Figure 3: ASMPT gross profit and GM trend  
![](images/01ab6688b1901ed54c1f968764ddfa54d10727fc23ed91297182d2a2abdcc906.jpg)  
Source: Company data and JPM estimates.

Figure 4: ASMPT operating profit and OPM trend  
![](images/4d7749774f0d0e7d3f18bf4c9044332f74478669c97eeeae0e7e5835e87879ed.jpg)  
Source: Company data and JPM estimates.

Figure 5: ASMPT net profit and yoy trend  
![](images/f3f0393571fa7319b8da46e72e5ff7f7998b605f874471d0a8e3e308487f697f.jpg)  
Source: Company data and JPM estimates.

Figure 6: Semiconductor revenue and yoy trend HK\$ in millions, %  
![](images/006337cea4126df8de13bd09a18370727c82a783fbb03feb8ba899ecff9a6add.jpg)  
Source: Company data and JPM estimates.

Figure 8: Semiconductor bookings and yoy trend  
Figure 7: SMT revenue and yoy trend HK\$ in millions, %  
![](images/460708591818a2d22aa5822613fafd37593c4579ecf039cea01a63dccbc0a61b.jpg)  
Source: Company data and JPM estimates.

Figure 9: SMT bookings and yoy trend  
![](images/1d6df4a1d77cfa0927b79998ee658cecd1f6bf9aa87ab7c94c5c71592adb03eb.jpg)  
Source: Company data.

![](images/a371ca6edbd32d13da93ef3cb25e12e754538f704e96ecdcab7a46e2ffc97da6.jpg)

## Earnings Review

Table 1: ASMPT Earnings Review

<table><tr><td rowspan="2">HK$ million</td><td colspan="3">2Q26</td><td colspan="2">Variance</td><td colspan="2">Growth</td></tr><tr><td>Actual</td><td>JPMe</td><td>BBG</td><td>vs. JPMe</td><td>vs. Consensus</td><td>Q/Q</td><td>Y/Y</td></tr><tr><td>Revenues</td><td>4,936</td><td>4,790</td><td>4,464</td><td>3%</td><td>11%</td><td>24%</td><td>45%</td></tr><tr><td>Gross profit</td><td>2,093</td><td>1,872</td><td>1,771</td><td>12%</td><td>18%</td><td>34%</td><td>55%</td></tr><tr><td>GM (%)</td><td>42.4%</td><td>39.1%</td><td>39.7%</td><td>333 bps</td><td>272 bps</td><td>292 bps</td><td>269 bps</td></tr><tr><td>Operating profit</td><td>787</td><td>506</td><td>455</td><td>55%</td><td>73%</td><td>104%</td><td>364%</td></tr><tr><td>OPM (%)</td><td>15.9%</td><td>10.6%</td><td>10.2%</td><td>536 bps</td><td>573 bps</td><td>622 bps</td><td>1096 bps</td></tr><tr><td>Net profit</td><td>418</td><td>408</td><td>340</td><td>2%</td><td>23%</td><td>65%</td><td>218%</td></tr><tr><td>EPS (HK$)</td><td>1.01</td><td>0.98</td><td>0.81</td><td>4%</td><td>24%</td><td>66%</td><td>221%</td></tr><tr><td>Adj. net profit</td><td>638</td><td>408</td><td>340</td><td>56%</td><td>87%</td><td>124%</td><td>194%</td></tr><tr><td>Adj. EPS (HK$)</td><td>1.53</td><td>0.98</td><td>0.81</td><td>57%</td><td>88%</td><td>119%</td><td>189%</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates.

## Estimate revisions

Table 2: ASMPT quarterly estimate revisions

<table><tr><td rowspan="2">HK$ million</td><td colspan="3">Revised</td><td colspan="3">Prior</td><td colspan="3">Change (%)</td></tr><tr><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td></tr><tr><td>Revenues (HK$ in mn)</td><td>5,275</td><td>5,437</td><td>5,698</td><td>4,939</td><td>4,748</td><td>4,883</td><td>7%</td><td>15%</td><td>17%</td></tr><tr><td>Gross profit</td><td>2,191</td><td>2,213</td><td>2,332</td><td>1,976</td><td>1,917</td><td>2,003</td><td>11%</td><td>15%</td><td>16%</td></tr><tr><td>GM (%)</td><td>41.5%</td><td>40.7%</td><td>40.9%</td><td>40.0%</td><td>40.4%</td><td>41.0%</td><td>152bps</td><td>31bps</td><td>-9bps</td></tr><tr><td>Operating profit</td><td>778</td><td>779</td><td>820</td><td>646</td><td>636</td><td>696</td><td>20%</td><td>22%</td><td>18%</td></tr><tr><td>OPM (%)</td><td>14.7%</td><td>14.3%</td><td>14.4%</td><td>13.1%</td><td>13.4%</td><td>14.2%</td><td>167bps</td><td>93bps</td><td>14bps</td></tr><tr><td>Pretax profit</td><td>851</td><td>854</td><td>902</td><td>727</td><td>715</td><td>770</td><td>17%</td><td>19%</td><td>17%</td></tr><tr><td>Net profit</td><td>641</td><td>686</td><td>643</td><td>548</td><td>575</td><td>550</td><td>17%</td><td>19%</td><td>17%</td></tr><tr><td>EPS (HK$)</td><td>1.53</td><td>1.64</td><td>1.54</td><td>

[中间内容因长度限制已省略]

erial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such

opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
