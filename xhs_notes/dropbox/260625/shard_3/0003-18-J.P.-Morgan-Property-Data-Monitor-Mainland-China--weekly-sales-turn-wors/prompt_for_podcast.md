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
# Property Data Monitor

Mainland China: weekly sales turn worse due to holidays; HK: home prices up another 0.6% W/W

## Mainland China

\- Iceberg 10-city real-time secondary weekly sales (冰山指数实时二手成交) dropped $0.05\%$ Y/Y (down from $+13\%$ Y/Y). Tier-1 cities' weekly sales dropped $3\%$ Y/Y (down from $+14\%$ ) (Table 1). The decline is mostly due to the Dragon Boat Festival. If we compare last week's data vs. the week with the same festival last year, 10-city & tier-1 sales would be up $15\% / 10\%$ Y/Y. Real-time sales generally lead the trend of official sales registrations by a few weeks.

\- Iceberg 10-city secondary listings (冰山指数二手挂牌量) fell further, down $0.2\%$ W/W. Tier-1 cities' listings dropped $0.5\%$ W/W, while Shanghai's dropped another $1.1\%$ W/W (prior: $-0.6\%$ ) (Table 2). The volume of secondary listings in tier-1 cities has been consistently coming down (down $2.6\%$ from the peak in March), and this is a key factor that will support continual secondary home price stabilization.

\- 60-city primary sales registrations (一手网签) fell $23\%$ Y/Y (more), mostly due to the inclusion of the 3-day Dragon Boat Festival (during public holidays, sales registrations are significantly lower than usual). Compared to the same 3-day Dragon Boat Festival period in 2025, sales registrations were up $60\%$ Y/Y (but the sample size is too small, hence we do not think this alone is representative).

\- 12-city secondary sales registrations (二手网签) fell $13\%$ Y/Y (Figure 7), reversing the positive Y/Y growth for the past 9 weeks (due to public holidays). Shanghai $(+12\%)$ is the only city with Y/Y growth among tier-1 cities. YTD, 12-city secondary sales have risen $5\%$ Y/Y (Shanghai: $+13\%$ ).

\- The Centraline tier-1 cities' secondary asking price index dropped mildly from 17.8 to 17.3 (Figure 3).

\- The Centaline manager confidence index dropped from 53 to 51 (Figure 4).

\- Southbound holdings rose 0.32% W/W (Table 7): Sunac +2.4%; CRL +0.9%

\- Share price moves (Figure 17): The sector dropped 13% last week, underperforming the HSI (-5%). The outperformer was Sunac (-5%). The underperformers were A-Living (-20%) and Longfor (-17%). For further discussion, please see our report China Property: Why the recent share price weakness?

• JPM top picks: COLI, CR Land, Jinmao and CR Mixc.

## Hong Kong SAR

\- The home price index rose 0.6% W/W (Figure 12). Home prices have risen 10.4% YTD, already reaching our full-year target of 10-15%. Looking ahead to 2H26, we expect slower price growth of <5%. For more discussion, please see our report HK Residential Property: Home prices already hit our full-year target; momentum may slow in 2H.

• Secondary transactions in the top 35 estates totaled 43 units, down 16%

## Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC
(852) 2800-8513
karl.chan@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

(852) 2800-8599
venus.choi@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Jocelyn Gao
(852) 2800-8529
jocelyn.gao@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## APAC Credit Research

Alvin Au AC
(852) 2800-8533
alvin.au@JPM.com
JPM Securities (Asia Pacific) Limited

Soo Chong Lim
(852) 2800-7387
soochong.lim@JPM.com
JPM Securities (Asia Pacific) Limited

Shirley Yau
(852) 2800-0566
shirley.yau@JPM.com
JPM Securities (Asia Pacific) Limited

See page 20 for analyst certification and important disclosures, including non-US analyst disclosures.

W/W & down 47% Y/Y (Figure 11), the lowest since CNY. This is partially due to adverse weather.

\- The Centa Salesman Index (CSI) (Figure 14) moderated from 69.6 last week to 68.2. A reading of $>50 =$ sentiment is positive and property prices are likely to rise.

\- The Centaline Valuation Index (CVI) rose from 82.7 last week to 86.2 this week.

\- Southbound holdings fell 0.07% W/W (Table 7): Hang Lung Prop -0.6%; Swire Prop +0.04%.

\- Share price moves (Figure 18): The sector dropped $4.4\%$ last week, marginally outperforming the HSI $(-4.7\%)$ . The outperformer was HKL $(-1\%)$ , followed by Hysan and JM (both $-2\%$ ), while Champion REIT and NWD (both $-8\%$ ) underperformed.

JPM top picks: Developers – CKA, Sino; landlords – Swire Prop & HKL; conglomerates – JM & CKH.

## Credit View (by Alvin Au)

\- The JACI China HY Property index rose 0.3% (vs China HY: +0.16%) last week, resuming the uptrend after a brief correction the previous week. This brings YTD returns to +6.4%.

\- Seazen: Debtwire reported that Seazen is planning a Rmb2bn tap of private REIT as soon as in June. This is on top of a Rmb616mn private REIT issued in Nov 2025 backed by its Shanghai Qingpu Wuyue Plaza, and the developer will add two more shopping malls in Tianjin and Nantong as underlying assets for this tap. We think the scale of the tap is material, as it more than covers the Rmb1.7bn of onshore maturities for the rest of 2026. Management mentioned earlier that it is planning to launch a public REIT as an additional funding channel later in 2026 as well.

\- Continued K-shape for China's housing market as reflected in May 2026 NBS data: Top-tier cities remain solid as all four tier-1 cities report positive m/m increase in secondary home price (for the third month in a row). However, the broader industry remains weak with the 70-city m/m decline marginally widening from -0.23% in April to -0.26% in May (see details in equity report). As market fragmentation continues, we continue to prefer credits with IP transformation stories, solid debt servicing ability and decent valuations.

JPM top picks: LNGFOR '29s (84 offer, 9.9% ytm) and SHUION '29s (101.5 offer, 9.1% ytm).

## Table Of Contents

Mainland China.... 1
Hong Kong SAR.... 1
Credit View (by Alvin Au).... 2
1. Mainland China – real-time secondary sales & listings .... 4
2. Mainland China – leading indicators from Centraline.... 5
3. Mainland China – Weekly primary sales registrations .... 6
4. Mainland China – Weekly secondary sales registrations. .... 7
5. Hong Kong – Residential market update .... 8
6. Hong Kong – Tourist arrivals and resident departures .... 12
7. Share price update .... 13
8. Credit recommendations .... 17
9. Equity valuation summary .... 18

## 1. Mainland China – real-time secondary sales & listings

Table 1: Iceberg 10-city real time secondary weekly sales 冰山指数实时二手每周成交 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of units</td><td colspan="6">Y/Y</td><td colspan="6">4-week rolling Y/Y</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier 1</td><td>Top-10</td></tr><tr><td>24-May-26</td><td>3,795</td><td>6,014</td><td>2,460</td><td>1,396</td><td>13,665</td><td>31,096</td><td>11%</td><td>14%</td><td>17%</td><td>15%</td><td>14%</td><td>13%</td><td>16%</td><td>16%</td><td>26%</td><td>24%</td><td>18%</td><td>17%</td></tr><tr><td>31-May-26</td><td>3,799</td><td>5,488</td><td>2,694</td><td>1,391</td><td>13,372</td><td>30,110</td><td>19%</td><td>11%</td><td>35%</td><td>29%</td><td>19%</td><td>22%</td><td>16%</td><td>18%</td><td>26%</td><td>25%</td><td>20%</td><td>19%</td></tr><tr><td>7-Jun-26</td><td>3,817</td><td>5,597</td><td>2,462</td><td>1,257</td><td>13,133</td><td>29,310</td><td>22%</td><td>16%</td><td>17%</td><td>36%</td><td>19%</td><td>16%</td><td>15%</td><td>13%</td><td>23%</td><td>25%</td><td>16%</td><td>16%</td></tr><tr><td>14-Jun-26</td><td>3,980</td><td>5,580</td><td>2,416</td><td>1,126</td><td>13,102</td><td>29,372</td><td>16%</td><td>18%</td><td>8%</td><td>0%</td><td>14%</td><td>13%</td><td>17%</td><td>15%</td><td>19%</td><td>19%</td><td>16%</td><td>16%</td></tr><tr><td>21-Jun-26</td><td>3,288</td><td>4,528</td><td>1,881</td><td>1,011</td><td>10,708</td><td>25,055</td><td>1%</td><td>-5%</td><td>-4%</td><td>-6%</td><td>-3%</td><td>0%</td><td>14%</td><td>20%</td><td>14%</td><td>14%</td><td>12%</td><td>13%</td></tr></table>

Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 1: Iceberg 10-city real time secondary daily sales 冰山指数实时二手每日成交 (十大城市)  
![](images/4cc37c7fdafb79b314a5c3deae11c02976f5733b8ee8601ac220aca5d11afcac.jpg)  
Source: Iceberg Index  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Table 2: Iceberg 10-city secondary listing volume 冰山指数二手挂牌量 (十大城市)

<table><tr><td rowspan="2">Week ending</td><td colspan="6">No. of secondary listings (&#x27;000 units)</td><td colspan="6">W/W</td></tr><tr><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier-1</td><td>Top-10</td><td>BJ</td><td>SH</td><td>GZ</td><td>SZ</td><td>Tier-1</td><td>Top-10</td></tr><tr><td>25-May-26</td><td>120</td><td>85</td><td>137</td><td>89</td><td>431</td><td>1,559</td><td>-0.6%</td><td>-0.5%</td><td>-0.2%</td><td>0.2%</td><td>-0.3%</td><td>0.0%</td></tr><tr><td>1-Jun-26</td><td>120</td><td>84</td><td>137</td><td>89</td><td>430</td><td>1,556</td><td>-0.2%</td><td>-0.6%</td><td>-0.1%</td><td>-0.1%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>8-Jun-26</td><td>119</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,555</td><td>-0.2%</td><td>-0.4%</td><td>-0.2%</td><td>0.1%</td><td>-0.2%</td><td>-0.1%</td></tr><tr><td>15-Jun-26</td><td>120</td><td>84</td><td>137</td><td>89</td><td>429</td><td>1,559</td><td>0.3%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.0%</td><td>0.2%</td></tr><tr><td>22-Jun-26</td><td>119</td><td>83</td><td>137</td><td>88</td><td>427</td><td>1,556</td><td>-0.4%</td><td>-1.1%</td><td>-0.1%</td><td>-0.8%</td><td>-0.5%</td><td>-0.2%</td></tr></table>

Source: Iceberg Index

Figure 2: Iceberg tier-1 cities secondary listing volume 冰山指数二手挂牌量 (一线城市)  
![](images/8fc9e902063edb0d36195c2f744d5ab28e6566e14a5d86f94abb7cb3677ccf9c.jpg)  
Source: Iceberg Index

## 2. Mainland China – leading indicators from Centraline

Figure 3: Centraline secondary asking price index vs. NBS secondary home price index M/M in tier-1 cities

![](images/ea98acb5442960e7a8ade382ed3867ccb4e339ea8ea3b9b79d20089b41603454.jpg)  
Source: Centraline, Wind, NBS.  
Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).  
Figure 4: Centraline secondary manager confidence index in tier-1 cities vs. three-month rolling secondary sales

![](images/e5e3b7e8e40ee9da8834478dc6e83053cca0aed7c70dfdf5fc569c19b26d31c2.jpg)  
Source: Centraline, Wind. Note: The index surveys managers across the country for their judgment on the market outlook.

# 3. Mainland China – Weekly primary sales registrations

Figure 5: 60-city weekly primary sales registrations (一手网签) – compared with 2019-24  
![](images/95d0ab1478fb3f8db01a19b1326c6f4957650dbfdebc49777325cecf2626880d.jpg)  
Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 6: 60-city weekly primary sales registrations (一手网签)  
![](images/495684aef95b1ce19fbcdace00e3704b53cece7fbf20849e5ea0b86eebb35efc.jpg)  
Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Table 3: 60-city weekly primary sales registrations (一手网签) by tier

<table><tr><td rowspan="2">Week ending</td><td colspan="6">60-City</td><td colspan="6">Tier-1</td><td colspan="6">Tier-2</td><td colspan="6">Tier-3/4</td></tr><tr><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td>No. of units</td><td>Y/Y</td><td>W/W</td><td>4 week rolling Y/Y</td><td>vs. 18-21 avg</td><td></td><td></td><td></td><td></td></tr><tr><td>19-Apr-26</td><td>21,159</td><td>6%↑</td><td>15%↑</td><td>-1%↑</td><td>-69%↑</td><td>3,726</td><td>5%↑</td><td>13%↑</td><td>9%↑</td><td>-35%↓</td><td>12,813</td><td>18%↑</td><td>15%↑</td><td>3%↑</td><td>-70%↑</td><td>4,620</td><td>-16%↑</td><td>16%↑</td><td>-18%↑</td><td>-77%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>26-Apr-26</td><td>23,318</td><td>-7%↓</td><td>10%↓</td><td>1%↑</td><td>-60%↑</td><td>4,297</td><td>6%↑</td><td>15%↑</td><td>11%↑</td><td>-23%↑</td><td>13,879</td><td>-6%↓</td><td>8%↓</td><td>4%↑</td><td>-60%↑</td><td>5,142</td><td>-16%↓</td><td>11%↓</td><td>-10%↑</td><td>-73%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>3-May-26</td><td>21,384</td><td>-4%↑</td><td>-8%↓</td><td>-4%↓</td><td>-65%↓</td><td>4,223</td><td>12%↑</td><td>-2%↓</td><td>6%↓</td><td>-14%↑</td><td>12,503</td><td>3%↑</td><td>-10%↓</td><td>2%↓</td><td>-66%↓</td><td>4,658</td><td>-25%↓</td><td>-9%↓</td><td>-22%↓</td><td>-75%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>10-May-26</td><td>20,449</td><td>-2%↑</td><td>-4%↑</td><td>-2%↑</td><td>-67%↓</td><td>3,523</td><td>2%↓</td><td>-17%↓</td><td>6%↓</td><td>-29%↓</td><td>12,116</td><td>3%↑</td><td>-3%↑</td><td>3%↑</td><td>-68%↓</td><td>4,810</td><td>-15%↑</td><td>3%↑</td><td>-18%↑</td><td>-76%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>17-May-26</td><td>24,282</td><td>3%↑</td><td>19%↑</td><td>-2%↓</td><td>-62%↑</td><td>4,874</td><td>22%↑</td><td>38%↑</td><td>11%↑</td><td>-17%↑</td><td>13,822</td><td>4%↑</td><td>14%↑</td><td>1%↓</td><td>-64%↑</td><td>5,586</td><td>-10%↑</td><td>16%↑</td><td>-17%↑</td><td>-72%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>24-May-26</td><td>24,411</td><td>-10%↓</td><td>1%↓</td><td>-3%↓</td><td>-65%↓</td><td>5,032</td><td>11%↓</td><td>3%↓</td><td>12%↑</td><td>-18%↓</td><td>13,964</td><td>-11%↓</td><td>1%↓</td><td>-1%↓</td><td>-68%↓</td><td>5,415</td><td>-22%↓</td><td>-3%↓</td><td>-18%↓</td><td>-73%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>31-May-26</td><td>31,094</td><td>14%↑</td><td>27%↑</td><td>1%↑</td><td>-53%↑</td><td>5,784</td><td>28%↑</td><td>15%↑</td><td>16%↑</td><td>9%↑</td><td>17,992</td><td>15%↑</td><td>29%↑</td><td>3%↑</td><td>-55%↑</td><td>7,318</td><td>2%↑</td><td>35%↑</td><td>-11%↑</td><td>-65%↑</td><td></td><td></td><td></td><td></td></tr><tr><td>7-Jun-26</td><td>21,851</td><td>17%↑</td><td>-30%↓</td><td>5%↑</td><td>-66%↓</td><td>3,572</td><td>1%↓</td><td>-38%↓</td><td>16%↓</td><td>-29%↓</td><td>13,011</td><td>31%↑</td><td>-28%↓</td><td>8%↑</td><td>-67%↓</td><td>5,268</td><td>0%↓</td><td>-28%↓</td><td>-8%↑</td><td>-74%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>14-Jun-26</td><td>19,881</td><td>-7%↓</td><td>-9%↑</td><td>3%↓</td><td>-69%↓</td><td>3,188</td><td>-2%↓</td><td>-11%↑</td><td>11%↓</td><td>-40%↓</td><td>12,051</td><td>-2%↓</td><td>-7%↑</td><td>6%↓</td><td>-69%↓</td><td>4,642</td><td>-19%↓</td><td>-12%↑</td><td>-10%↓</td><td>-76%↓</td><td></td><td></td><td></td><td></td></tr><tr><td>21-Jun-26</td><td>20,899</td><td>-23%↓</td><td>5%↑</td><td>-1%↓</td><td>-73%↓</td><td>3,447</td><td>-11%↓</td><td>8%↑</td><td>5%↓</td><td>-56%↓</td><td>13,511</td><td>-15%↓</td><td>12%↑</td><td>5%↓</td><td>-71%↓</td><td>3,941</td><td>-46%↓</td><td>-15%↓</td><td>-17%↓</td><td>-83%↓</td><td></td><td></td><td></td><td></td></tr></table>

Source: CREIS.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

## 4. Mainland China – Weekly secondary sales registrations

Figure 7: 12-city daily secondary sales registrations (二手网签)  
![](images/90533d0fea4223e7cc20bfda78727e14303567cf638afc71fcfb1e0d8222103f.jpg)  
Source: Wind.  
Note: The decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

Figure 8: 12-city secondary sales registrations (二手网签) 7-day moving average  
Secondary sales 7-day moving average - 12-city  
![](images/c59f6193b7be64a24c850b878391878d758dfe8bcd180bd0247c5b682bb3a8f6.jpg)  
Source: Wind.  
Note: The Y/Y decline in the week ending 21 June 2026 is due to the Dragon Boat Festival.

## 5. Hong Kong – Residential market update

Table 4: Hong Kong primary residential projects – Latest sell-through rates and upcoming launches

<table><tr><td colspan="2">Project</td><td>Location</td><td>Developer</td><td>Launch Date</td><td>ASP (HK$ psf)</td><td>Total no. of units</td><td>Units launched</td><td>Units sold</td><td>Sell- through</td><td>vs. previous phase</td><td>vs. secondary prices</td></tr><tr><td colspan="12">Major primary new launches since May 2026</td></tr><tr><td rowspan="4">Lime SPARK</td><td rowspan="4">形瑁</td><td rowspan="4">Tsuen Wan</td><td rowspan="4">SHKP</td><td>9-May-26</td><td>16 - 18K</td><td>462</td><td>154</td><td>154</td><td>100%</td><td>-</td><td>14%</td></tr><tr><td>16-May-26</td><td>17 - 19K</td><td></td><td>121</td><td>121</td><td>100%</td><td>4%</td><td>19%</td></tr><tr><td>23-May-26</td><td>18 - 20K</td><td></td><td>87</td><td>87</td><td>100%</td><td>3%</td><td>22%</td></tr><tr><td>30-May-26</td><td>18 - 20K</td><td></td><td>52</td><td>52</td><td>100%</td><td>3%</td><td>26%</td></tr><tr><td rowspan="5">Highwood Ph2</td><td rowspan="5">壹沐2期</td><td rowspan="5">To Kwa Wan</td><td rowspan="5">Henderson</td><td>9-May-26</td><td>19 - 24K</td><td>415</td><td>150</td><td>150</td><td>100%</td><td>14%</td><td>14%</td></tr><tr><td>13-May-26</td><td>19 - 24K</td><td></td><td>50</td><td>50</td><td>100%</td><td>4%</td><td>22%</td></tr><tr><td>17-May-26</td><td>20 - 26K</td><td></td><td>50</td><td>42</td><td>84%</td><td>2%</td><td>25%</td></tr><tr><td>23-May-26</td><td>20 - 27K</td><td></td><td>35</td><td>29</td><td>83%</td><td>1%</td><td>26%</td></tr><tr><td>31-May-26</td><td>22 - 27K</td><td></td><td>23</td><td>5</td><td>22%</td><td>13%</td><td>35%</td></tr><tr><td rowspan="2">PORTO</td><td rowspan="2"></td><td rowspan="2">Ap Lei Chau</td><td rowspan="2">Wang On</td><td>9-May-26</td><td>20 - 25K</td><td>174</td><td>86</td><td>55</td><td>64%</td><td>-</td><td>31%</td></tr><tr><td>24-May-26</td><td>24 - 31K</td><td></td><td>6</td><td>1</td><td>17%</td><td>5%</td><td>61%</td></tr><tr><td rowspan="3">One Victoria Cove Ph3</td><td rowspan="3">首岸3期</td><td rowspan="3">Hung Hom</td><td rowspan="3">Henderson/Hysan/ Empire/URA</td><td>10-May-26</td><td>21 - 23K</td><td>288</td><td>130</td><td>130</td><td>100%</td><td>16%</td><td>20%</td></tr><tr><td>14-May-26</td><td>20 - 24K</td><td></td><td>70</td><td>61</td><td>87%</td><td>4%</td><td>25%</td></tr><tr><td>19-May-26</td><td>22 - 24K</td><td></td><td>58</td><td>49</td><td>84%</td><td>2%</td><td>28%</td></t

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and

should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
