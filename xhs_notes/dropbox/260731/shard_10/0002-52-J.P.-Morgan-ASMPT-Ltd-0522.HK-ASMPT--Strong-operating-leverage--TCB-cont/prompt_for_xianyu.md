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

<table><tr><td rowspan="2">HK$ million</td><td colspan="3">2Q26</td><td colspan="2">Variance</td><td colspan="

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
