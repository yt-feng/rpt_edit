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
Foreign Exchange FX Blog

Date

14 July 2026

# What is driving high-frequency FX?

Main highlights: US equities extended their rally over the past week, recovering from the volatility triggered by earlier geopolitical tensions. Against this backdrop, our high-frequency analysis shows a further strengthening in US equity–FX connectivity, with equity markets now driving more than 60% of the currency pairs in our sample.

Broader cross-asset drivers: The influence of US rates on FX dynamics also increased, underscoring their growing importance as a cross-asset driver. Oil's contribution to currency moves was broadly unchanged, while EM equities and copper saw a modest increase in influence, pointing to a slight broadening in the set of risk and commodity factors shaping FX performance.

Impact across individual FX pairs: US equities remain the dominant driver of USD/JPY, AUD/USD and USD/SGD. For EUR/USD, USD/CAD and USD/CNH, high-frequency moves are driven primarily by a combination of US equities and US rates, highlighting the joint importance of risk sentiment and interest-rate dynamics. Elsewhere, oil remains the key influence on EUR/NOK, consistent with the pair's close relationship with energy markets. USD/CHF is influenced by a broader mix of factors, with US equities, US rates and copper all playing important roles.

Historical impact over the past three months: US equities have been the dominant driver of USD/CHF, USD/SGD and NZD/USD, explaining market moves on more than 90% of trading days. US rates have been especially influential for NZD/USD and USD/CNH, accounting for more than 60% of trading days. EM equities have had the strongest impact on USD/CAD, EUR/NOK and USD/MXN, contributing on more than 20% of trading days. Oil remains the defining factor for EUR/NOK, driving the pair on more than 90% of trading days.

Correlation structure: Underlying cross-asset correlations continue to show a classic risk-on/risk-off pattern. US and EM equities are generally positively correlated with pro-cyclical assets, including AUD, NZD, GBP, EUR, SGD, MXN, ZAR, gold (XAU) and bitcoin (XBT), reflecting their shared sensitivity to global growth and investor risk appetite. By contrast, oil is negatively correlated with several currencies against the US dollar, notably ZAR, SGD, CHF, CNH, NZD, XAU and AUD. US rates also maintain broadly negative correlations with major currencies, with the strongest inverse relationships in SGD, ZAR, JPY, CHF, NZD, AUD, XAU, EUR and GBP.

Network view: Beyond predictive linkages, the correlation-based Minimum Spanning Tree (MST) shows how contemporaneous cross-market relationships are structured. The network continues to identify US interest rates as the primary hub in high-frequency FX dynamics, with the VIX remaining the second most important source of cross-asset connectivity. Within FX, USD/ZAR retains its role as a key bridge currency, linking rates, equities and commodities. Its central

Rohini Grover, Ph.D.

Strategist

position highlights its role as a key connector across asset classes, making it an important channel for cross-market spillovers.

Figure 1, Figure 3 and Figure 15 look at causality in FX. Figure 1 shows the currencies whose moves can be statistically predicted by other asset classes. Figure 3 ranks the drivers of FX (highest to lowest number of currencies, driven by a given asset). Figure 15 shows the relative importance of each asset in driving a given currency in the recent period. Figure 13 looks at contemporaneous correlations. We show the top 3 correlations between FX pairs and other asset classes. Figure 14 shows intra-FX correlations. We use Granger causality tests to measure causality. All statistics measured at 5-minute frequency. For further details, please see our updated methodology. For a summary of our FX quant tools, please also see DB FX research quant tools.

Figure 1: Significant connections from assets to currencies
Table 1: Significant connections from assets to currencies

<table><tr><td rowspan="2"></td><td rowspan="2"># of conn. from other assets(Over last 4 weeks)</td><td rowspan="2">Assets driving currencies(Over last 4 weeks)</td><td colspan="2">%tile rank</td></tr><tr><td>6M history</td><td>Since &#x27;16</td></tr><tr><td>NZDUSD</td><td>4</td><td>US EQ,US RATE,OIL,EM EQ</td><td>97%</td><td>94%</td></tr><tr><td>EURSEK</td><td>4</td><td>EU EQ,EU RATE,US EQ,US RATE</td><td>81%</td><td>92%</td></tr><tr><td>AUDJPY</td><td>4</td><td>AU EQ,US EQ,COPPER,VIX</td><td>31%</td><td>46%</td></tr><tr><td>GBPUSD</td><td>3</td><td>US EQ,US RATE,EM EQ</td><td>83%</td><td>78%</td></tr><tr><td>USDCHF</td><td>3</td><td>US EQ,US RATE,COPPER</td><td>86%</td><td>69%</td></tr><tr><td>EURCHF</td><td>3</td><td>EU EQ,US RATE,OIL</td><td>80%</td><td>72%</td></tr><tr><td>EURUSD</td><td>2</td><td>US EQ,US RATE</td><td>34%</td><td>46%</td></tr><tr><td>USDCAD</td><td>2</td><td>US EQ,US RATE</td><td>66%</td><td>51%</td></tr><tr><td>USDCNH</td><td>2</td><td>US EQ,US RATE</td><td>51%</td><td>53%</td></tr><tr><td>USDTRY</td><td>2</td><td>US EQ,OIL</td><td>96%</td><td>60%</td></tr><tr><td>USDJPY</td><td>1</td><td>US EQ</td><td>12%</td><td>25%</td></tr><tr><td>AUDUSD</td><td>1</td><td>US EQ</td><td>22%</td><td>26%</td></tr><tr><td>USDZAR</td><td>1</td><td>EM EQ</td><td>19%</td><td>26%</td></tr><tr><td>USDSGD</td><td>1</td><td>US EQ</td><td>10%</td><td>21%</td></tr><tr><td>EURNOK</td><td>1</td><td>OIL</td><td>0%</td><td>9%</td></tr><tr><td>XBTUSD</td><td>1</td><td>COPPER</td><td>41%</td><td>65%</td></tr><tr><td>USDMXN</td><td></td><td></td><td></td><td></td></tr><tr><td>EURPLN</td><td></td><td></td><td></td><td></td></tr><tr><td>XAUUSD</td><td></td><td></td><td></td><td></td></tr></table>

Source: DB

Figure 2: Extent to which other markets are driving FX (connections from other assets to FX)  
![](images/c5b9a1ae60ab55bdd3863e0abfc0bc81bc909a828882252c6a3ac2a03267bf03.jpg)  
Source: DB, EBS, Reuters; 4-week rolling average connections

Figure 3: Number of currencies driven by each asset  
![](images/95b2b8bf9ee5d19102f536c993f037577aecd7e5fc3f178935b80aabde5630ec.jpg)  
Source: DB, EBS, Reuters; Total number of currencies = 19

Figure 4: NZD/USD and USD/CNH are most driven by US rates over the past three months  
![](images/381fdc389dce7d78a3d14bc1431522514d38fb41fad872089624eca024359173.jpg)  
Source: DB

Figure 5: Correlation with US rates  
![](images/df5e6d30d458fc9cdf266909f09ec9378112ce15a42452f3efe1315668bd0783.jpg)  
Source: DB

Figure 6: USD/CHF and USD/SGD most driven by US equities over the past three months  
![](images/dd42baca504e94d4f7ca2330b4877fe1a8d91b7f5bd0fcb5fa875c4987dd89a0.jpg)  
Source: DB

Figure 7: Correlation with US equities  
![](images/034d8e8471fd2d655033260c757a9839615cce1bf314655efcc825f1a4b6f154.jpg)  
Source: DB

Figure 8: USD/CAD and EUR/NOK most driven by EM over the past three months  
![](images/7c02bd8ae50869f60e4433be93d0df423d73c21f97cafee5f7e28ce5b1485210.jpg)  
Source: DB

Figure 9: Correlation with EM equities  
![](images/cb090070e0c45291245b78094ee0c955294a180a17b9a01e6e7d6e6a9b6cfee0.jpg)  
Source: DB

Figure 10: EUR/NOK most driven by Oil over the past three months  
![](images/0decf96b1038f512e475d73537dd8a9d578f0a54c5fed3163f24e9725de40b09.jpg)  
Source: DB

Figure 11: Correlation with Oil  
![](images/8afb439bc1dfa319abffda7ede916476eb4a5b1dbdb4d4d888aa972876f42e08.jpg)  
Source: DB

![](images/fcf97e171b239d46ca9a5d5eabdbc26e8f494dac88bdfa667384fdf7ccf3b91c.jpg)  
Source: DB, EBS, Reuters; 4-week rolling average connections

Figure 13: Cross-asset correlation

▲ Up (stronger correlation)/down (weaker correlation) against last week/month 5-day correlations

<table><tr><td rowspan="2">5 Day correlations</td><td colspan="3">First</td><td colspan="3">Second</td><td colspan="3">Third</td></tr><tr><td>Current</td><td>1 week ago</td><td>1 month ago</td><td>Current</td><td>1 week ago</td><td>1 month ago</td><td>Current</td><td>1 week ago</td><td>1 month ago</td></tr><tr><td>EURUSD</td><td>US RATE-54%</td><td>▲-47%</td><td>▲-49%</td><td>VIX-34%</td><td>▲-19%</td><td>▼-41%</td><td>COPPER34%</td><td>▼37%</td><td>▼45%</td></tr><tr><td>USDJPY</td><td>US RATE55%</td><td>▲49%</td><td>▲32%</td><td>EU RATE44%</td><td>▲31%</td><td>▲35%</td><td>UK RATE44%</td><td>▲33%</td><td>▲32%</td></tr><tr><td>GBPUSD</td><td>US RATE-44%</td><td>▲-43%</td><td>▼-51%</td><td>VIX-37%</td><td>▲-30%</td><td>▼-40%</td><td>COPPER31%</td><td>▼36%</td><td>▼46%</td></tr><tr><td>EURNOK</td><td>OIL-24%</td><td>▼-25%</td><td>▼-24%</td><td>VIX11%</td><td>▼26%</td><td>▼14%</td><td>EM EQ-8%</td><td>▼-11%</td><td>▲3%</td></tr><tr><td>EURSEK</td><td>US RATE48%</td><td>▲22%</td><td>▲39%</td><td>VIX47%</td><td>▲36%</td><td>▲39%</td><td>EU RATE37%</td><td>▲29%</td><td>▲36%</td></tr><tr><td>USDCHF</td><td>US RATE53%</td><td>▲49%</td><td>▲52%</td><td>UK RATE40%</td><td>▲31%</td><td>▼53%</td><td>EU RATE40%</td><td>▲36%</td><td>▼53%</td></tr><tr><td>EURCHF</td><td>US RATE29%</td><td>▲26%</td><td>▼32%</td><td>EU RATE25%</td><td>▼26%</td><td>▼28%</td><td>UK RATE25%</td><td>▲21%</td><td>▲25%</td></tr><tr><td>AUDJPY</td><td>VIX-50%</td><td>▲-29%</td><td>▲-30%</td><td>COPPER37%</td><td>▲19%</td><td>▲30%</td><td>US EQ37%</td><td>▲26%</td><td>▲29%</td></tr><tr><td>AUDUSD</td><td>US RATE-60%</td><td>▲-45%</td><td>▲-50%</td><td>VIX-54%</td><td>▲-39%</td><td>▼-61%</td><td>COPPER52%</td><td>▲44%</td><td>▼59%</td></tr><tr><td>NZDUSD</td><td>US RATE-64%</td><td>▲-50%</td><td>▲-42%</td><td>EU RATE-49%</td><td>▲-43%</td><td>▼-57%</td><td>VIX-47%</td><td>▲-38%</td><td>▼-52%</td></tr><tr><td>USDCAD</td><td>US RATE36%</td><td>▼36%</td><td>▲15%</td><td>VIX26%</td><td>▲22%</td><td>▼28%</td><td>COPPER-21%</td><td>▼-38%</td><td>▼-33%</td></tr><tr><td>XAUUSD</td><td>US RATE-58%</td><td>▲-47%</td><td>▲-43%</td><td>COPPER57%</td><td>▲55%</td><td>▼62%</td><td>US EQ46%</td><td>▲36%</td><td>▼48%</td></tr><tr><td>USDCNH</td><td>US RATE53%</td><td>▲43%</td><td>▲50%</td><td>VIX50%</td><td>▲31%</td><td>▲44%</td><td>UK RATE39%</td><td>▲32%</td><td>▼52%</td></tr><tr><td>USDSGD</td><td>US RATE68%</td><td>▲53%</td><td>▲51%</td><td>VIX51%</td><td>▲31%</td><td>▼54%</td><td>EU RATE51%</td><td>▲38%</td><td>▼55%</td></tr><tr><td>USDMXN</td><td>VIX49%</td><td>▲36%</td><td>▲48%</td><td>US RATE46%</td><td>▼49%</td><td>▲39%</td><td>US EQ-40%</td><td>▲-34%</td><td>▼-46%</td></tr><tr><td>USDZAR</td><td>US RATE65%</td><td>▲52%</td><td>▲48%</td><td>VIX56%</td><td>▲39%</td><td>▼57%</td><td>EU RATE48%</td><td>▲42%</td><td>▼53%</td></tr><tr><td>USDTRY</td><td>OIL10%</td><td>▲0%</td><td>▲-2%</td><td>EU RATE9%</td><td>▼10%</td><td>▲-5%</td><td>SZ EQ-6%</td><td>▲-4%</td><td>▲3%</td></tr><tr><td>EURPLN</td><td>US EQ-31%</td><td>▲-17%</td><td>▼-37%</td><td>VIX31%</td><td>▲26%</td><td>▼48%</td><td>COPPER-25%</td><td>▲-19%</td><td>▼-29%</td></tr><tr><td>XBTUSD</td><td>VIX-52%</td><td>▲-45%</td><td>▲-48%</td><td>US EQ46%</td><td>▲44%</td><td>▼49%</td><td>EM EQ33%</td><td>▲31%</td><td>▲12%</td></tr></table>

Figure 14: Cross-currency correlation

<table><tr><td>5 Day correlations</td><td>EURUSD</td><td>USDJPY</td><td>GBPUSD</td><td>USDCHF</td><td>AUDUSD</td><td>NZDUSD</td><td>USDCAD</td><td>XAUUSD</td><td>USDCNH</td><td>USDSGD</td><td>USDMXN</td><td>USDTRY</td><td>USDZAR</td><td>XBTUSD</td></tr><tr><td rowspan="4">Current1 month ago</td><td>USDSGD ▲</td><td>USDSGD ▲</td><td>EURUSD ▼</td><td>EURUSD ▼</td><td>NZDUSD ▲</td><td>AUDUSD ▲</td><td>AUDUSD ▲</td><td>USDZAR ▼</td><td>USDSGD ▲</td><td>AUDUSD ▼</td><td>USDZAR ▼</td><td>EURSEK ▲</td><td>USDSGD ▲</td><td>XAUUSD ▲</td></tr><tr><td>-82%</td><td>72%</td><td>79%</td><td>-76%</td><td>89%</td><td>89%</td><td>-63%</td><td>-61%</td><td>72%</td><td>-85%</td><td>67%</td><td>5%</td><td>76%</td><td>35%</td></tr><tr><td>-82%</td><td>60%</td><td>85%</td><td>-77%</td><td>76%</td><td>76%</td><td>-60%</td><td>-61%</td><td>71%</td><td>-87%</td><td>69%</td><td>-1%</td><td>75%</td><td>32%</td></tr><tr><td>NZDUSD ▲</td><td>NZDUSD ▲</td><td>AUDUSD ▼</td><td>NZDUSD ▼</td><td>USDSGD ▲</td><td>USDSGD ▲</td><td>NZDUSD ▲</td><td>USDSGD ▼</td><td>AUDUSD ▼</td><td>NZDUSD ▲</td><td>AUDUSD ▼</td><td>GBPUSD ▲</td><td>AUDUSD ▼</td><td>USDZAR ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>80%</td><td>-63%</td><td>70%</td><td>-69%</td><td>-85%</td><td>-84%</td><td>-62%</td><td>-60%</td><td>-69%</td><td>-84%</td><td>-66%</td><td>-5%</td><td>-73%</td><td>-32%</td></tr><tr><td>75%</td><td>-62%</td><td>77%</td><td>-74%</td><td>-87%</td><td>-71%</td><td>-49%</td><td>-61%</td><td>-69%</td><td>-71%</td><td>-72%</td><td>1%</td><td>-77%</td><td>-36%</td></tr><tr><td>GBPUSD ▼</td><td>EURUSD ▲</td><td>USDSGD ▼</td><td>GBPUSD ▼</td><td>EURUSD ▼</td><td>EURUSD ▲</td><td>USDCFH ▲</td><td>AUDUSD ▼</td><td>NZDUSD ▲</td><td>EURUSD ▲</td><td>USDSGD ▼</td><td>AUDUSD ▲</td><td>NZDUSD ▼</td><td>USDSGD ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>79%</td><td>-63%</td><td>-69%</td><td>-68%</td><td>78%</td><td>80%</td><td>59%</td><td>58%</td><td>-66%</td><td>-82%</td><td>65%</td><td>4%</td><td>-68%</td><td>-30%</td></tr><tr><td>85%</td><td>-59%</td><td>-75%</td><td>-74%</td><td>80%</td><td>75%</td><td>43%</td><td>66%</td><td>-65%</td><td>-82%</td><td>68%</td><td>0%</td><td>-70%</td><td>-34%</td></tr><tr><td>AUDUSD ▼</td><td>AUDUSD ▲</td><td>NZDUSD ▼</td><td>USDSGD ▼</td><td>USDZAR ▼</td><td>GBPUSD ▼</td><td>EURUSD ▲</td><td>NZDUSD ▼</td><td>EURUSD ▼</td><td>USDZAR ▲</td><td>NZDUSD ▲</td><td>EURCHF ▲</td><td>USDMXN ▼</td><td>AUDUSD ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>78%</td><td>-59%</td><td>69%</td><td>68%</td><td>-73%</td><td>69%</td><td>-59%</td><td>54%</td><td>-65%</td><td>76%</td><td>-62%</td><td>4%</td><td>67%</td><td>29%</td></tr><tr><td>80%</td><td>-55%</td><td>75%</td><td>68%</td><td>-77%</td><td>75%</td><td>-58%</td><td>58%</td><td>-66%</td><td>75%</td><td>-59%</td><td>0%</td><td>69%</td><td>37%</td></tr><tr><td>USDCHF ▼</td><td>USDCHF ▲</td><td>USDCHF ▼</td><td>AUDUSD ▼</td><td>GBPUSD ▼</td><td>USDCFH ▼</td><td>GBPUSD ▲</td><td>USDMXN ▼</td><td>GBPUSD ▼</td><td>USDJPY ▲</td><td>EURUSD ▼</td><td>USDZAR ▲</td><td>XAUUSD ▼</td><td>USDMXN ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>-76%</td><td>57%</td><td>-68%</td><td>-66%</td><td>70%</td><td>-69%</td><td>-57%</td><td>-47%</td><td>-56%</td><td>72%</td><td>-60%</td><td>-4%</td><td>-61%</td><td>-26%</td></tr><tr><td>-77%</td><td>56%</td><td>-74%</td><td>-68%</td><td>77%</td><td>-74%</td><td>-54%</td><td>-54%</td><td>-63%</td><td>60%</td><td>-67%</td><td>-1%</td><td>-61%</td><td>-32%</td></tr><tr><td>USDCNH</td><td>GBPUSD ▼</td><td>USDCAD ▲</td><td>EURCHF ▲</td><td>USDCNH ▼</td><td>USDZAR ▼</td><td>USDSGD ▲</td><td>AUDJPY ▼</td><td>USDZAR ▼</td><td>USDCNH ▲</td><td>GBPUSD ▼</td><td>EURPLN ▲</td><td>EURUSD ▼</td><td>NZDUSD ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>-65%</td><td>-55%</td><td>-57%</td><td>59%</td><td>-69%</td><td>-68%</td><td>55%</td><td>42%</td><td>54%</td><td>72%</td><td>-53%</td><td>3%</td><td>-59%</td><td>25%</td></tr><tr><td>-66%</td><td>-57%</td><td>-54%</td><td>57%</td><td>-69%</td><td>-70%</td><td>55%</td><td>51%</td><td>63%</td><td>71%</td><td>-60%</td><td>0%</td><td>-66%</td><td>33%</td></tr><tr><td>USDJPY ▲</td><td>USDZAR ▲</td><td>USDCNH ▼</td><td>USDCAD ▲</td><td>USDMXN ▼</td><td>USDCNH ▼</td><td>USDJPY ▲</td><td>EURUSD ▼</td><td>USDCFH ▼</td><td>GBPUSD ▼</td><td>USDCNH ▼</td><td>USDCNH ▼</td><td>USDCNH ▼</td><td>EURSEK ▲</td></tr><tr><td rowspan="3">Current1 month ago</td><td>-63%</td><td>52%</td><td>-56%</td><td>59%</td><td>-66%</td><td>-66%</td><td>45%</td><td>41%</td><td>54%</td><td>-69%</td><td>52%</td><td>2%</td><td>54%</td><td>-21%</td></tr><tr><td>-59%</td><td>48%</td><td>-63%</td><td>43%</td><td>-72%</td><td>-65%</td><td>33%</td><td>53%</td><td>58%</td><td>-75%</td><td>55%</td><td>-4%</td><td>63%</td><td>-21%</td></tr><tr><td>USDMXN ▼</td><td>USDCNH ▼</td><td>USDJPY ▼</td><td>USDJPY ▲</td><td>USDCHF ▼</td><td>USDPY ▲</td><td>USDCNH ▲</td><td>USDCNH ▼</td><td>USDMXN ▼</td><td>USDCFH ▼</td><td>XAUUSD ▼</td><td>EURUSD ▼</td><td>USDJPY ▲</td><td>EURPLN ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>-60%</td><td>50%</td><td>-55%</td><td>57%</td><td>-66%</td><td>-63%</td><td>41%</td><td>-40%</td><td>52%</td><td>68%</td><td>-47%</td><td>-2%</td><td>52%</td><td>-20%</td></tr><tr><td>-67%</td><td>54%</td><td>-57%</td><td>56%</td><td>-68%</td><td>-62%</td><td>38%</td><td>-53%</td><td>55%</td><td>68%</td><td>-54%</td><td>3%</td><td>48%</td><td>-21%</td></tr><tr><td>USDZAR ▼</td><td>USDMXN ▲</td><td>USDMXN ▼</td><td>USDCNH ▼</td><td>USDCAD ▲</td><td>USDCAD ▲</td><td>USDMXN ▼</td><td>USDCHF ▼</td><td>USDJPY ▼</td><td>USDMXN ▼</td><td>USDJPY ▲</td><td>USDCAD ▼</td><td>GBPUSD ▼</td><td>USDCNH ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>-59%</td><td>46%</td><td>-53%</td><td>54%</td><td>-63%</td><td>-62%</td><td>39%</td><td>-39%</td><td>50%</td><td>65%</td><td>46%</td><td>-2%</td><td>-51%</td><td>-20%</td></tr><tr><td>-66%</td><td>40%</td><td>-60%</td><td>58%</td><td>-60%</td><td>-49%</td><td>44%</td><td>-49%</td><td>54%</td><td>68%</td><td>40%</td><td>3%</td><td>-66%</td><td>-29%</td></tr><tr><td>USDCAD ▲</td><td>USDCAD ▲</td><td>USDZAR ▼</td><td>USDZAR ▼</td><td>AUDJPY ▼</td><td>USDMXN ▲</td><td>USDZAR ▼</td><td>GBPUSD ▼</td><td>USDCAD ▲</td><td>XAUUSD ▼</td><td>USDCHF ▼</td><td>USDCHF ▼</td><td>USDSGD ▲</td><td>AUDJPY ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>-59%</td><td>45%</td><td>-51%</td><td>49%</td><td>59%</td><td>-62%</td><td>38%</td><td>38%</td><td>41%</td><td>-60%</td><td>43%</td><td>2%</td><td>49%</td><td>19%</td></tr><tr><td>-58%</td><td>33%</td><td>-66%</td><td>62%</td><td>84%</td><td>-59%</td><td>43%</td><td>53%</td><td>38%</td><td>-61%</td><td>50%</td><td>-2%</td><td>62%</td><td>31%</td></tr><tr><td>XAUUSD ▼</td><td>XAUUSD ▼</td><td>EURSEK ▼</td><td>USDMXN ▼</td><td>USDJPY ▲</td><td>XAUUSD ▼</td><td>AUDJPY ▼</td><td>USDJPY ▼</td><td>XAUUSD ▼</td><td>USDCAD ▲</td><td>USDCAD ▼</td><td>USDSGD ▲</td><td>EURSEK ▼</td><td>GBPUSD ▼</td></tr><tr><td rowspan="3">Current1 month ago</td><td>41%</td><td>-37%</td><td>-39%</td><td>43%</td><td>-59%</td><td>54%</td><td>-36%</td><td>-37%</td><td>-40%</td><td>55%</td><td>39%</td><td>1%</td><td>44%</td><td>17%</td></tr><tr><td>53%</td><td>-44%</td><td>-43%</td><td>50%</td><td>-55%</td><td>58%</td><td>-54%</td><td>-44%</td><td>-53%</td><td>55%</td><td>44%</td><td>1%</td><td>48%</td><td>27%</td></tr><tr><td>EURSEK ▼</td><td>EURSEK ▲</td><td>XAUUSD ▼<

[中间内容因长度限制已省略]

t has likely been in contact with the company that is the subject of this research for confirmation/clarification of data, facts, statements, permission to use company-sourced material in the report, and/or site-visit attendance. Without prior approval from Research Management, analysts may not accept from current or potential Banking clients the costs of travel, accommodations, or other expenses incurred by analysts attending site visits, conferences, social events, and the like. Similarly, without prior approval from Research Management and Anti-Bribery and Corruption ("ABC") team, analysts may not accept perks or other items of value for their personal use from issuers they cover.

Additional information relative to securities, other financial products or issuers discussed in this report is available upon request. This report may not be reproduced, distributed or published without DB's prior written consent.

Backtested, hypothetical or simulated performance results have inherent limitations. Unlike an actual performance record based on trading actual client portfolios, simulated results are achieved by means of the retroactive application of a backtested model itself designed with the benefit of hindsight. Taking into account historical events the backtesting of performance also differs from actual account performance because an actual investment strategy may be adjusted any time, for any reason, including a response to material, economic or market factors. The backtested performance includes hypothetical results that do not reflect the reinvestment of dividends and other earnings or the deduction of advisory fees, brokerage or other commissions, and any other expenses that a client would have paid or actually paid. No representation is made that any trading strategy or account will or is likely to achieve profits or losses similar to those shown. Alternative modeling techniques or assumptions might produce significantly different results and prove to be more appropriate. Past hypothetical backtest results are neither an indicator nor guarantee of future returns. Actual results will vary, perhaps materially, from the analysis.

The method for computing individual E,S,G and composite ESG scores set forth herein is a novel method developed by the Research department within DB AG, computed using a systematic approach without human intervention. Different data providers, market sectors and geographies approach ESG analysis and incorporate the findings in a variety of ways. As such, the ESG scores referred to herein may differ from equivalent ratings developed and implemented by other ESG data providers in the market and may also differ from equivalent ratings developed and implemented by other divisions within the DB Group. Such ESG scores also differ from other ratings and rankings that have historically been applied in research reports published by DB AG. Further, such ESG scores do not represent a formal or official view of DB AG.

It should be noted that the decision to incorporate ESG factors into any investment strategy may inhibit the ability to participate in certain investment opportunities that otherwise would be consistent with your investment objective and other principal investment strategies. The returns on a portfolio consisting primarily of sustainable investments may be lower or higher than portfolios where ESG factors, exclusions, or other sustainability issues are not considered, and the investment opportunities available to such portfolios may differ. Companies may not necessarily meet high performance standards on all aspects of ESG or sustainable investing issues; there is also no guarantee that any company will meet expectations in connection with corporate responsibility, sustainability, and/or impact performance.

Copyright © 2026 DB AG

David Folkerts-Landau  
Group Chief Economist and Global Head of Research

<table><tr><td>Pam Finelli
COO and Head of Fixed Income Research</td><td>Steve Pollard
Global Head of Company Research and Sales</td><td>Jim Reid
Global Head of Macro and Thematic Research</td><td>Tim Rokossa
Head of European Company Research</td></tr><tr><td>Matthew Barnard
Head of Americas
Company Research</td><td>Debbie Jones
Global Head of Sustainability and Data Innovation, Research</td><td>Robin Winkler
Head of German Macro Research</td><td>Sameer Goel
Global Head of EM &amp; APAC Research</td></tr><tr><td>Francis Yared
Global Head of Rates Research</td><td>George Saravelos
Global Head of FX Research</td><td>Peter Hooper
Vice-Chair of Research</td><td>Nilendra de-Mel
Head of APAC &amp; Middle East Product Development</td></tr></table>

International Production Locations

<table><tr><td>DB AG</td><td>DB AG</td><td>DB AG</td><td>Deutsche Securities Inc.</td></tr><tr><td>DB Place</td><td>Equity Research</td><td>Filiale Hongkong</td><td>1-3-1 Azabudai</td></tr><tr><td>Level 16</td><td>Mainzer Landstrasse 11-17</td><td>International Commerce Centre</td><td>Azabudai Hills Mori JP Tower</td></tr><tr><td>Corner of Hunter &amp; Phillip Streets</td><td>60329 Frankfurt am Main Germany</td><td>1 Austin Road West, Kowloon,</td><td>Minato-ku, Tokyo 106-0041</td></tr><tr><td>Sydney, NSW 2000 Australia</td><td>Tel: (49) 69 910 00</td><td>Hong Kong</td><td>Japan</td></tr><tr><td>Tel: (61) 2 8258 1234</td><td></td><td>Tel: (852) 2203 8888</td><td>Tel: (81) 3 6730 1000</td></tr></table>

DB AG  
21 Moorfields  
London EC2Y 9DB  
United Kingdom  
Tel: (44) 20 7545 8000

DB AG  
Filiale Singapur  
One Raffles Quay, South Tower  
Singapore 048583  
Tel: (65) 6423 8001
"""
