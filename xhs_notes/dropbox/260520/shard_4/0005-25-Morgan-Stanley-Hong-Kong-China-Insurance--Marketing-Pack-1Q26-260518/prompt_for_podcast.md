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
May 18, 2026 10:11 AM GMT

# Investor Presentation | Asia Pacific

# Hong Kong/China Insurance: Marketing Pack 1Q26

Insurers finished 1Q26 with largely in-line earnings and high-quality life and P&C businesses. We think the 1Q earnings overhang has played out, and we see more upside risk from here, as markets have already rebounded since April.

MS ASIA LIMITED+

# Rick Zhao

Equity Analyst

Rick.Zhao@morganstanley.com +852 2239-7033

# Richard Xu, CFA

Equity Analyst

Richard.Xu@morganstanley.com +852 2848-6729

# Chenqian Liu

Research Associate

Chenqian.Liu@morganstanley.com +852 3963-0359

# HONG KONG/CHINA INSURANCE

# Asia Pacific

Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# MS

MS

Hong Kong/China Insurance

May 18, 2026

# Table of Contents

1. Hong Kong/China Insurance Share Price Performance and Valuation Comps   
2. 1Q26 Wrap-Up: Key Earnings, Life, P&C and Solvency   
3. FY25 Wrap-Up: Key Focus, Group Performance, Life, P&C, Investment, Capital   
4. Single Stock Names: AIA, Ping An, PICC P&C, CPIC, China Life   
5. Southbound Fund Flow Comps

# MS

MS

Hong Kong/China Insurance

May 18, 2026

1. Hong Kong/China Insurance Share Price Performance 

<table><tr><td rowspan="2">15/05/26Company</td><td rowspan="2">Ticker</td><td rowspan="2">Price</td><td colspan="8">Absolute Performance (%)</td><td rowspan="2">Premium/(Discount)to A-shares</td></tr><tr><td>YTD</td><td>1W</td><td>1M</td><td>3M</td><td>6M</td><td>12M</td><td>2 YR</td><td>3 YR</td></tr><tr><td colspan="12">H share</td></tr><tr><td>AIA</td><td>1299-HK</td><td>87.65</td><td>9.7</td><td>1.2</td><td>4.5</td><td>9.2</td><td>6.4</td><td>33.1</td><td>39.3</td><td>7.9</td><td></td></tr><tr><td>Prudential</td><td>2378-HK</td><td>119.40</td><td>0.0</td><td>-1.9</td><td>1.8</td><td>3.0</td><td>8.1</td><td>34.5</td><td>55.3</td><td>5.5</td><td></td></tr><tr><td>FWD</td><td>1828-HK</td><td>30.32</td><td>-20.3</td><td>-3.4</td><td>-5.3</td><td>-20.2</td><td>-23.0</td><td>NA</td><td>NA</td><td>NA</td><td></td></tr><tr><td>PICC</td><td>2328-HK</td><td>15.39</td><td>-5.9</td><td>3.4</td><td>4.5</td><td>-7.1</td><td>-17.9</td><td>1.1</td><td>48.6</td><td>54.7</td><td></td></tr><tr><td>Ping An</td><td>2318-HK</td><td>62.15</td><td>-4.6</td><td>-5.3</td><td>-0.6</td><td>-11.7</td><td>3.7</td><td>33.2</td><td>54.8</td><td>7.8</td><td>(3.0)</td></tr><tr><td>China Pacific</td><td>2601-HK</td><td>33.22</td><td>-5.6</td><td>-6.3</td><td>-1.9</td><td>-10.8</td><td>-0.9</td><td>36.1</td><td>70.2</td><td>32.9</td><td>(16.7)</td></tr><tr><td>Zhong An</td><td>6060-HK</td><td>11.09</td><td>-31.1</td><td>-9.2</td><td>-12.5</td><td>-31.2</td><td>-32.3</td><td>-12.5</td><td>-26.3</td><td>-55.6</td><td></td></tr><tr><td>China Life</td><td>2628-HK</td><td>29.86</td><td>9.1</td><td>-4.5</td><td>8.9</td><td>-9.7</td><td>9.1</td><td>87.1</td><td>156.5</td><td>100.1</td><td>(26.8)</td></tr><tr><td>PICC Group</td><td>1339-HK</td><td>5.39</td><td>-20.1</td><td>-3.2</td><td>0.4</td><td>-17.8</td><td>-27.2</td><td>3.1</td><td>93.2</td><td>68.4</td><td>(32.9)</td></tr><tr><td>China Taiping</td><td>966-HK</td><td>21.78</td><td>16.5</td><td>-7.9</td><td>-0.9</td><td>-9.2</td><td>7.6</td><td>79.7</td><td>159.6</td><td>135.7</td><td></td></tr><tr><td>New China Life</td><td>1336-HK</td><td>49.90</td><td>-8.2</td><td>-5.8</td><td>5.1</td><td>-14.5</td><td>-2.8</td><td>54.3</td><td>194.9</td><td>122.8</td><td>(29.3)</td></tr><tr><td colspan="12">A share</td></tr><tr><td>Ping An</td><td>601318-CN</td><td>55.50</td><td>-18.9</td><td>-7.6</td><td>-5.5</td><td>-15.0</td><td>-8.5</td><td>2.3</td><td>32.6</td><td>4.3</td><td></td></tr><tr><td>China Pacific</td><td>601601-CN</td><td>34.57</td><td>-17.5</td><td>-6.3</td><td>-9.0</td><td>-19.4</td><td>-4.7</td><td>1.6</td><td>26.6</td><td>4.9</td><td></td></tr><tr><td>New China Life</td><td>601336-CN</td><td>61.12</td><td>-12.3</td><td>-6.0</td><td>-0.9</td><td>-21.3</td><td>-10.4</td><td>17.9</td><td>90.5</td><td>54.1</td><td></td></tr><tr><td>China Life</td><td>601628-CN</td><td>35.35</td><td>-22.3</td><td>-5.3</td><td>-6.2</td><td>-25.4</td><td>-19.9</td><td>-10.1</td><td>11.7</td><td>-14.2</td><td></td></tr><tr><td>PICC Group</td><td>601319-CN</td><td>6.96</td><td>-22.2</td><td>-4.9</td><td>-7.0</td><td>-21.6</td><td>-21.0</td><td>-15.9</td><td>29.9</td><td>5.3</td><td></td></tr><tr><td colspan="12">Index</td></tr><tr><td>HSCEI</td><td>160462</td><td>8,678</td><td>-2.6</td><td>-2.4</td><td>-0.5</td><td>-3.9</td><td>-7.7</td><td>2.0</td><td>28.7</td><td>27.8</td><td></td></tr><tr><td>HSI</td><td>180458</td><td>25,931</td><td>1.2</td><td>-1.8</td><td>-0.1</td><td>-2.4</td><td>-2.4</td><td>10.6</td><td>35.9</td><td>29.8</td><td></td></tr><tr><td>SHCOMP</td><td>180167</td><td>4,134</td><td>4.2</td><td>-1.1</td><td>2.7</td><td>1.3</td><td>3.6</td><td>22.3</td><td>32.5</td><td>25.6</td><td></td></tr><tr><td>MSCI China</td><td>MS302400</td><td>81</td><td>-3.4</td><td>-0.7</td><td>0.7</td><td>-3.9</td><td>-8.1</td><td>6.3</td><td>27.3</td><td>24.6</td><td></td></tr><tr><td>MSCI AxJ</td><td>899800</td><td>1,541</td><td>26.3</td><td>1.5</td><td>11.5</td><td>14.7</td><td>27.7</td><td>54.2</td><td>68.6</td><td>88.3</td><td></td></tr><tr><td>CSI 300 Financials</td><td>CSI00014</td><td>6,025</td><td>-10.3</td><td>-1.5</td><td>-2.4</td><td>-5.6</td><td>-10.8</td><td>-5.4</td><td>17.7</td><td>8.4</td><td></td></tr></table>

Note: Prices as close of May 15, 2026. Source: FactSet, MS.

# MS

MS

Hong Kong/China Insurance

May 18, 2026

1. Hong Kong/China Insurance: Valuation Comps 

<table><tr><td rowspan="2">Company</td><td rowspan="2">TRSL</td><td rowspan="2">CCY Trading</td><td rowspan="2">Price (LC)</td><td rowspan="2">Market Cap (USD mn)</td><td rowspan="2">Turn-over (USD mn)</td><td rowspan="2">Rating</td><td rowspan="2">PT</td><td rowspan="2">Upside</td><td colspan="2">P/Group EV</td><td colspan="2">P/B</td><td colspan="2">P/E</td><td colspan="2">Dividend Yield %</td><td colspan="2">ROE %</td><td colspan="2">VNB growth %</td></tr><tr><td>2026 E</td><td>2027 E</td><td>2026 E</td><td>2027 E</td><td>2026 E</td><td>2027 E</td><td>2026 E</td><td>2027 E</td><td>2026 E</td><td>2027 E</td><td>2026 E</td><td>2027 E</td></tr><tr><td colspan="21">Regional Life Insurers</td></tr><tr><td>AIA</td><td>1299-HK</td><td>HKD</td><td>87.80</td><td>117,782</td><td>292.3</td><td>O</td><td>109.0</td><td>24%</td><td>1.21</td><td>1.07</td><td>2.35</td><td>2.10</td><td>14.4</td><td>12.8</td><td>2.5</td><td>2.8</td><td>17.4</td><td>17.4</td><td>14.7</td><td>14.9</td></tr><tr><td>FWD</td><td>1828-HK</td><td>HKD</td><td>30.32</td><td>6,522</td><td>3.4</td><td>O</td><td>42.5</td><td>40%</td><td>0.71</td><td>0.61</td><td>0.66</td><td>0.62</td><td>13.4</td><td>10.7</td><td>NA</td><td>NA</td><td>4.1</td><td>5.1</td><td>12.5</td><td>12.8</td></tr><tr><td colspan="21">Chinese Life insurers</td></tr><tr><td>Ping An</td><td>2318-HK</td><td>HKD</td><td>62.45</td><td>144,377</td><td>327.1</td><td>O</td><td>92.0</td><td>47%</td><td>0.61</td><td>0.57</td><td>0.90</td><td>0.82</td><td>6.6</td><td>5.8</td><td>5.3</td><td>5.7</td><td>14.3</td><td>14.7</td><td>16.0</td><td>16.5</td></tr><tr><td>China Life</td><td>2628-HK</td><td>HKD</td><td>29.90</td><td>107,900</td><td>221.9</td><td>O</td><td>38.9</td><td>30%</td><td>0.46</td><td>0.42</td><td>1.10</td><td>0.99</td><td>7.9</td><td>7.1</td><td>3.6</td><td>3.9</td><td>14.8</td><td>14.6</td><td>21.0</td><td>13.5</td></tr><tr><td>China Pacific</td><td>2601-HK</td><td>HKD</td><td>33.20</td><td>40,821</td><td>73.9</td><td>O</td><td>46.0</td><td>39%</td><td>0.42</td><td>0.38</td><td>0.83</td><td>0.76</td><td>6.8</td><td>6.3</td><td>4.3</td><td>4.6</td><td>12.9</td><td>12.6</td><td>10.7</td><td>11.5</td></tr><tr><td>PICC Group</td><td>1339-HK</td><td>HKD</td><td>5.41</td><td>30,546</td><td>42.4</td><td>O</td><td>7.7</td><td>42%</td><td>0.49</td><td>0.44</td><td>0.60</td><td>0.54</td><td>4.6</td><td>4.2</td><td>4.7</td><td>5.2</td><td>13.9</td><td>13.6</td><td>16.5</td><td>13.9</td></tr><tr><td>China Taiping</td><td>966-HK</td><td>HKD</td><td>21.80</td><td>10,003</td><td>28.8</td><td>E</td><td>25.7</td><td>18%</td><td>0.33</td><td>0.30</td><td>0.67</td><td>0.62</td><td>7.2</td><td>6.6</td><td>5.6</td><td>6.1</td><td>9.5</td><td>9.8</td><td>11.8</td><td>12.4</td></tr><tr><td>New China Life</td><td>1336-HK</td><td>HKD</td><td>49.80</td><td>19,835</td><td>82.9</td><td>U</td><td>44.8</td><td>-10%</td><td>0.43</td><td>0.40</td><td>1.11</td><td>1.01</td><td>7.5</td><td>7.5</td><td>3.7</td><td>4.0</td><td>14.4</td><td>14.3</td><td>9.5</td><td>9.2</td></tr><tr><td colspan="21">Non-Life Insurers</td></tr><tr><td>PICC P&amp;C</td><td>2328-HK</td><td>HKD</td><td>15.39</td><td>43,705</td><td>64.1</td><td>O</td><td>20.5</td><td>33%</td><td>NA</td><td>NA</td><td>0.95</td><td>0.88</td><td>7.5</td><td>6.9</td><td>5.6</td><td>6.1</td><td>13.3</td><td>13.3</td><td>NA</td><td>NA</td></tr><tr><td>Zhong An</td><td>6060-HK</td><td>HKD</td><td>11.11</td><td>2,390</td><td>64.1</td><td>O</td><td>18.1</td><td>63%</td><td>NA</td><td>NA</td><td>0.61</td><td>0.58</td><td>14.9</td><td>13.0</td><td>NA</td><td>NA</td><td>4.2</td><td>4.6</td><td>NA</td><td>NA</td></tr><tr><td colspan="21">A share Insurers</td></tr><tr><td>Ping An</td><td>601318-CN</td><td>CNY</td><td>55.50</td><td>148,086</td><td>617.3</td><td>O</td><td>84.0</td><td>51%</td><td>0.62</td><td>0.58</td><td>0.92</td><td>0.84</td><td>6.8</td><td>6.0</td><td>5.2</td><td>5.5</td><td>14.3</td><td>14.7</td><td>16.0</td><td>16.5</td></tr><tr><td>China Pacific</td><td>601601-CN</td><td>CNY</td><td>34.54</td><td>49,014</td><td>200.6</td><td>O</td><td>47.2</td><td>37%</td><td>0.50</td><td>0.46</td><td>1.00</td><td>0.91</td><td>8.1</td><td>7.6</td><td>3.6</td><td>3.9</td><td>12.9</td><td>12.6</td><td>10.7</td><td>11.5</td></tr><tr><td>China Life</td><td>601628-CN</td><td>CNY</td><td>35.36</td><td>147,271</td><td>105.9</td><td>E</td><td>44.7</td><td>26%</td><td>0.62</td><td>0.58</td><td>1.50</td><td>1.35</td><td>10.7</td><td>9.7</td><td>2.6</td><td>2.8</td><td>14.8</td><td>14.6</td><td>21.0</td><td>13.5</td></tr><tr><td>PICC Group</td><td>601319-CN</td><td>CNY</td><td>6.96</td><td>45,355</td><td>103.1</td><td>E</td><td>8.7</td><td>25%</td><td>0.73</td><td>0.65</td><td>0.89</td><td>0.80</td><td>6.8</td><td>6.2</td><td>3.2</td><td>3.5</td><td>13.9</td><td>13.6</td><td>16.5</td><td>13.9</td></tr><tr><td>New China Life</td><td>601336-CN</td><td>CNY</td><td>61.22</td><td>28,141</td><td>193.7</td><td>U</td><td>62.9</td><td>3%</td><td>0.61</td><td>0.56</td><td>1.58</td><td>1.43</td><td>10.6</td><td>10.6</td><td>2.6</td><td>2.8</td><td>14.4</td><td>14.3</td><td>9.5</td><td>9.2</td></tr></table>

Note: Prices as close of May 15, 2026. Source: Company data, FactSet, MS (E) estimates.

# MS

MS

Hong Kong/China Insurance

May 18, 2026

# 2. 1Q26 Wrap-up: Key Earnings

Most CN insurers saw earnings declines in 1Q26   
![](images/ca12dadc6ca5065fd50679063d48b3e0515566a97ef600f49a4fad7e272c95b8.jpg)

<details>
<summary>bar</summary>

| Company | 1Q25 (Rmb bn) | 1Q26 (Rmb bn) | Change (%) |
| :--- | :--- | :--- | :--- |
| Ping An* | 37.9 | 40.8 | 8 |
| China Life | 28.8 | 19.5 | -32 |
| CPIC | 9.6 | 10.0 | 4 |
| PICC Group | 12.8 | 8.8 | -31 |
| PICC | 11.3 | 8.6 | -24 |
| NCI | 5.9 | 6.5 | 11 |
| TP Life | 3.0 | 3.2 | 6 |
| ZhongAn | 0.6 | 0.2 | -70 |
</details>

\*OPAT for Ping An, while NPAT down 7% y-y

Insurers' annualized gross investment yield in 1Q26 decline across peers   
![](images/1e6c257983274ec317fbba571dbdef274239c66d49935f3000395bbf85101c0e.jpg)

<details>
<summary>bar</summary>

| Company | 1Q25 (%) | 1Q26 (%) |
| :--- | :--- | :--- |
| CPIC | 4.0 | 3.2 |
| PICC | 4.8 | 2.8 |
| China Life | 2.8 | 2.2 |
| NCI | 5.7 | 2.1 |
| PICC Group | 0.0 | 2.0 |
</details>

Annualized ROE declined across insurers in 1Q26, but still healthy   
![](images/f52b48057f15cd310aa1fc9bb8495367de866f266a858b9914332cf303e5640a.jpg)

<details>
<summary>bar</summary>

| Entity | Blue Bar (%) | Yellow Bar (%) |
| :--- | :--- | :--- |
| NCI | 26.7 | 22.1 |
| Ping An* | 16.2 | 16.2 |
| China Life | 22.1 | 13.1 |
| CPIC | 13.9 | 12.9 |
| PICC P&C | 17.1 | 11.9 |
| PICC Group | 18.8 | 11.2 |
-5ppts indicated by red arrow; -0ppts indicated by red arrow; -9ppts indicated by red arrow; -1ppts indicated by red arrow; -5ppts indicated by red arrow; -8ppts indicated by red arrow.
</details>

\*OPAT ROE for Ping An

Insurers' BVPS saw broad-based increase in 1Q26...   
![](images/dbfcc3000eccad13ad99c8486fe5ea932b3af8f91ef7b0b86649ff3cd1564058.jpg)

<details>
<summary>bar</summary>

| Company | Q-Q % |
| :--- | :--- |
| Ping An | 1.8 |
| NCI | 10.7 |
| CPIC | 5.8 |
| China Life | 0.5 |
| PICC | 1.8 |
| PICC Group | 3.4 |
</details>

Earnings breakdown in 1Q26 – insurance results are steady while investment results decline   
![](images/f0118546eeac167cf036236ed83c41a5e14ca45580ed6c29ccbddfb99ca7b095.jpg)

<details>
<summary>bar_stacked</summary>

| Category | Quarter | Insurance results (Rmb bn) | Investment results (Rmb bn) | Others (Rmb bn) |
| :--- | :--- | :--- | :--- | :--- |
| Ping An | 1Q25 | 27 | -12 | 34 |
| Ping An | 1Q26 | 28 | -15 | 35 |
| China Life | 1Q25 | 26 | -2 | -2 |
| China Life | 1Q26 | 24 | -3 | -2 |
| PICC Group | 1Q25 | 15 | -3 | 6 |
| PICC Group | 1Q26 | 16 | -4 | -3 |
| PICC | 1Q25 | 9 | -1 | 5 |
| PICC | 1Q26 | 10 | 0 | 2 |
| CPIC | 1Q25 | 9 | -1 | 4 |
| CPIC | 1Q26 | 10 | -1 | 1 |
| NCI | 1Q25 | 4 | -1 | 3 |
| NCI | 1Q26 | 5 | -1 | 2 |
</details>

\* Earnings before tax and asso&JV

...while insurers' total assets showed diversified q-q trends in 1Q26   
![](images/73688404d5352edbc38c5009415ae5015047c50082b2da6d5f759d4d20b699ef.jpg)

<details>
<summary>bar</summary>

| Company | Q-Q % |
| :--- | :--- |
| Ping An | 1.9 |
| China Life | 1.6 |
| CPIC | 2.6 |
| PICC Group | -0.2 |
| NCI | -2.4 |
| PICC | -1.8 |
</details>

Source: Company data; MS

# MS

MS

Hong Kong/China Insurance

May 18, 2026

# 2. 1Q26 Wrap-up: Life

Insurers saw very healthy y-y growth in APE in 1Q26   
![](images/bbabc1df52844fd23ee621da2507eb8438e993eef6c2d639d010b777d70fe0d4.jpg)

<details>
<summary>bar</summary>

| Entity | Value (%) |
| :--- | :--- |
| PICC Life | 47 |
| CPIC* | 42 |
| NCI | 20 |
| AIA* | 16 |
| PICC Health | 11 |
| FWD* | 4 |
</details>

\* Agency APE for CPIC

Insurers FYP y-y trends were diversified in 1Q26, due to structure optimization   
![](images/ca8398723149d6272bf5096296a563442a8387ff5d21d5dbbc34f3ae6fc62cae.jpg)

<details>
<summary>bar</summary>

| Company | Value (%) |
| :--- | :--- |
| Ping An | 46 |
| China Life | 30 |
| PICC Health | 17 |
| NCI | 3 |
| CPIC | -8 |
| PICC Life | -13 |
</details>

Most China life insurers' VNB margin increase in 1Q26   
![](images/507e7a2401757d92165883ebdb8a216e9da7928a1e3cde41ba90c9a438a05c7a.jpg)

<details>
<summary>bar</summary>

| Company | 1Q25 (%) | 1Q26 (%) |
| :--- | :--- | :--- |
| AIA | 58 | 56 |
| FWD | 42 | 44 |
| Ping An | 28 | 23 |
| China Life* | 14 | 20 |
| CPIC | 14 | 16 |
| NCI* | 13 | 15 |
</details>

AIA and FWD were under APE basis while China insurers under FYP basis

FYP channel mix - agency channel was still very healthy while banca down due to SP cut   
![](images/575cd7a96fba56d794b1dbf142c25b435822d15c5b3642d13202f0d4931af2ff.jpg)

<details>
<summary>bar_stacked</summary>

| Rating | Quarter | Agency (Rmb bn) | Banca (Rmb bn) | Others (Rmb bn) |
| :--- | :--- | :--- | :--- | :--- |
| CPIC | 1Q25 | 14 | 20 | 9 |
| CPIC | 1Q26 | 18 | 12 | 8 |
| NCI | 1Q25 | 12 | 15 | 2 |
| NCI | 1Q26 | 15 | 13 | 2 |
</details>

Insurers FYP y-y trends were diversified in 1Q26, due to structure optimization   
![](images/f190c8f689bd283da0f753dd4901e557ac23f5f46cffff8beb309c828b0478cf.jpg)

<details>
<summary>bar</summary>

| Company | Value (%) |
| :--- | :--- |
| China Life | 76 |
| AIA CN* | 26 |
| NCI | 25 |
| PICC Life | 21 |
| Ping An L&H | 21 |
| AIA* | 13 |
| CPIC | 10 |
| FWD* | 7 |
</details>

\*AIA Group, AIA CN and FWD were under CER basis

Most insurers' agent number increased q-q in 1Q26   
![](images/5da5c4ef7828cb16625b58dbfc37221e2c703d82b5b5c47fd304d356bbfa1d59.jpg)

<details>
<summary>bar</summary>

| Company | FY25 | 1Q26 | Change (%) |
| :--- | :--- | :--- | :--- |
| China Life | 587 | 594 | +1.2 |
| Ping An | 351 | 332 | -5.4 |
| CPIC | 181 | 187 | +3.3 |
| Taiping Life | 167 | 183 | +9.6 |
</details>

Source: Company data; MS

# MS

MS

Hong Kong/China Insurance

May 18, 2026

# 2. 1Q26 Wrap-up: P&C and Solvency

Core solvency ratios trend mixed for insurers in 1Q26 q-q   
![](images/f7ab633281b38e7de48824bcb9238c6d411402ce811bf06ca5721b00d821cca9.jpg)

<details>
<summary>bar</summary>

| Company | 4Q25 (%) | 1Q26 (%) | Change (ppts) |
| :--- | :--- | :--- | :--- |
| China Life | 129 | 157 | +28 |
| CPIC Life | 157 | 146 | -11 |
| Taiping Life | 143 | 134 | -10 |
| Ping An Life | 123 | 131 | +8 |
| NCI | 135 | 131 | -5 |
| PICC Life | 134 | 122 | -12 |
</details>

P&C insurers earnings performance y-y   
![](images/28e8ea5b7430612ab54e513379328fed44927c1f57499be22aea38f8bddaa584.jpg)

<details>
<summary>bar</summary>

| Company | 1Q25 (Rmb bn) | 1Q26 (Rmb bn) | Change (%) |
| :--- | :--- | :--- | :--- |
| PICC P&C | 11.3 | 8.6 | -24 |
| Ping An P&C | 3.2 | 2.8 | -13 |
| CPIC P&C | 2.0 | 2.1 | +2 |
</details>

Source: Company data; MS

P&C insurers' CoR saw y-y improvement in 1Q26   
![](images/64298a5d4cef4752e5c93c2277dbccea378645faa0b090bacb01096a0dfde828.jpg)

<details>
<summary>bar</summary>

| Company | 1Q25 (%) | 1Q26 (%) | Change (ppt) |
| :--- | :--- | :--- | :--- |
| PICC | 94.5 | 94.2 | -0.3 |
| Ping An P&C | 96.6 | 95.8 | -0.8 |
| CPIC P&C | 97.4 | 96.4 | -1.0 |
</d

[中间内容因长度限制已省略]

 Saudi Arabia, and is directed at Sophisticated investors only.

MS Hong Kong Securities Limited is the liquidity provider/market maker for securities of AIA Group Ltd, China Life Insurance Co Ltd, China Pacific Insurance Group Co Ltd, New China Life Insurance Company Ltd, PICC Group, PICC P&C Company Ltd, Ping An Insurance Group Co of China Ltd, ZhongAn Online P & C Insurance Co Ltd listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Hong Kong/China Insurance 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/18/2026)</td></tr><tr><td colspan="3">Richard Xu, CFA</td></tr><tr><td>AIA Group Ltd (1299.HK)</td><td>O (12/12/2023)</td><td>HK$86.65</td></tr><tr><td>FWD Group Holdings Ltd (1828.HK)</td><td>O (08/13/2025)</td><td>HK$30.50</td></tr><tr><td>Ping An Insurance Group Co of China Ltd (2318.HK)</td><td>O (05/30/2023)</td><td>HK$61.85</td></tr><tr><td>Ping An Insurance Group Co of China Ltd (601318.SS)</td><td>O (05/30/2023)</td><td>Rmb54.89</td></tr><tr><td colspan="3">Rick Zhao</td></tr><tr><td>China Life Insurance Co Ltd (601628.SS)</td><td>E (05/30/2023)</td><td>Rmb34.75</td></tr><tr><td>China Life Insurance Co Ltd (2628.HK)</td><td>O (05/30/2023)</td><td>HK$29.76</td></tr><tr><td>China Pacific Insurance Group Co Ltd (601601.SS)</td><td>O (06/07/2024)</td><td>Rmb33.87</td></tr><tr><td>China Pacific Insurance Group Co Ltd (2601.HK)</td><td>O (05/30/2023)</td><td>HK$32.94</td></tr><tr><td>China Taiping Insurance Holdings Co Ltd (0966.HK)</td><td>E (05/30/2023)</td><td>HK$21.42</td></tr><tr><td>New China Life Insurance Company Ltd (601336.SS)</td><td>U (05/30/2023)</td><td>Rmb60.12</td></tr><tr><td>New China Life Insurance Company Ltd (1336.HK)</td><td>U (07/31/2025)</td><td>HK$49.14</td></tr><tr><td>PICC Group (1339.HK)</td><td>O (09/23/2024)</td><td>HK$5.26</td></tr><tr><td>PICC Group (601319.SS)</td><td>E (07/31/2025)</td><td>Rmb6.84</td></tr><tr><td>PICC P&amp;C Company Ltd (2328.HK)</td><td>O (05/30/2023)</td><td>HK$15.43</td></tr><tr><td>ZhongAn Online P &amp; C Insurance Co Ltd (6060.HK)</td><td>O (05/30/2023)</td><td>HK$11.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.

© 2026 MS
"""
