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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

## China Quant Strategy

## Expensive leadership is starting to look fragile; hedge with low vol, high quality yielders

Our call favoring Growth over Value has worked well so far with Growth outperforming Value by 4.5% since June 15th. June's style tape was consistent with that view: Momentum and Growth rose 9.8% and 7.4%, respectively, while Value fell 7.5%. However, the market was again rewarding a narrow and increasingly expensive right tail while the broader universe was under pressure: MSCI China declined 7.1% in June and 73% of stocks moved lower with the market.

Valuation spreads suggest that the market was still paying up for winners even as the average stock remained weak, as the gap between Expensive and Cheap stocks widened in June. The Expensive group now trades at more than 6x the multiple of the Cheap group, with median P/E of 114.9x and 6.3x, respectively. Valuations of the winners are starting to look stretched.

Figure 1: Valuation Ratio: Expensive vs. Cheap  
![](images/5bd541536be461a055ce0423c38edf48da7a90f53f00224bf7c39f55d6e626f1.jpg)  
Source: JPM; MSCI, FactSet

That does not automatically make the expensive stocks wrong, nor the cheap stocks right. Expensive can stay expensive when earnings momentum, liquidity, and narrative all point in the same direction. But when the market pays almost any price for a small set of winners while most stocks are falling, the burden of proof shifts.

The current spread also differs from the COVID recovery spread peak in late 2020. While the cheap side looks more familiar (Banks, Insurance, Capital Goods, Utilities, and other lower-multiple groups), the expensive tail today is much more concentrated in Technology Hardware, Semiconductors, and Materials. That makes the June rally in Momentum and Growth look less like a broad endorsement of growth assets and more like a crowded, FOMO AI trade.

## See page 7 for analyst certification and important disclosures.

## APAC Quantitative Strategy

Evan Hu AC
(852) 2800-8508
evan.hu@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Robert Smith, PhD AC
(61-2) 9003-8808
robert.z.smith@JPM.com
JPM Securities Australia Limited

Arpan Singh
(91-22) 6157-3301
arpan.singh@jpmchase.com
JPM India Private Limited

Chris Chi
chris.chi@JPM.com
JPM Securities Australia Limited

Khuram Chaudhry
(44-20) 7134-6297
khuram.chaudhry@JPM.com
JPM Securities plc

Table 1: Thematic and Concentration Differences vs. Last Peak in 2020

<table><tr><td colspan="4">Expensive Stocks</td><td colspan="4">Cheap Stocks</td></tr><tr><td>Last Peak</td><td>Count</td><td>Now</td><td>Count</td><td>Last Peak</td><td>Count</td><td>Now</td><td>Count</td></tr><tr><td>BioPharma</td><td>21</td><td>Tech Hardware</td><td>31</td><td>REITs</td><td>36</td><td>Banks</td><td>36</td></tr><tr><td>Tech Hardware</td><td>14</td><td>Semis</td><td>26</td><td>Banks</td><td>29</td><td>Insurance</td><td>12</td></tr><tr><td>Cap Goods</td><td>13</td><td>Materials</td><td>15</td><td>Cap Goods</td><td>17</td><td>Cap Goods</td><td>8</td></tr><tr><td>Materials</td><td>12</td><td>Cap Goods</td><td>7</td><td>Energy</td><td>9</td><td>Utilities</td><td>8</td></tr><tr><td>Software</td><td>11</td><td>BioPharma</td><td>7</td><td>Materials</td><td>7</td><td>Materials</td><td>7</td></tr><tr><td>Fin Services</td><td>11</td><td>Software</td><td>4</td><td>Insurance</td><td>7</td><td>Transportation</td><td>4</td></tr><tr><td>Other</td><td>53</td><td>Other</td><td>11</td><td>Other</td><td>29</td><td>Other</td><td>26</td></tr></table>

Source: JPM; MSCI, FactSet

The early July tape supports that interpretation. Month-to-date, Momentum is down 4.7% and Growth is down 4.5%, while Value has rebounded 7.4% and Low Volatility is up 8.0%. We would be careful not to overstate a few days of reversal. Short-term rotations can be noisy, and crowded trades can reassert themselves quickly. But the move is consistent with the setup: when valuations are stretched, dispersion is extreme, and leadership is narrow, the market might not need a major macro shock to rotate. It may only need investors to ask whether the winners are already priced for too much winning.

Figure 2: Key Style Performance in the Last Three Years  
![](images/40c190f7d6af30c5da310534df3c92dc200662907fc89b014aff17e6dd65008d.jpg)  
Source: JPM; MSCI, FactSet, I/B/E/S.

Against this backdrop, we recommend adding a defensive, high-quality Value hedge to Momentum, rather than simply OW Value over Growth or vice versa. The objective is not to position for an end to Momo/Growth leadership, but to participate if the market continues to rotate away from the most expensive winners and back toward cheaper, more defensive names.

Our proposed implementation is a combination of Low Vol, Div Yield, Quality and Size: stocks that sit at the intersection of bottom-third volatility, top-third yield, top-half Quality, and top-half market cap. The screen produces 31 stocks, with a median historical P/E of 12.3x and a median historical div yield of 5.5%. Sector exposure naturally tilts toward food & beverage, banks, appliances & apparel, energy, and transportation. We think this profile fits the current set-up: inexpensive enough to offer valuation support, income-backed to help cushion volatility, and quality-aware to reduce value-trap risk and preserve exposure to potential revaluation.

As an all-weather benchmark, our Multifactor Blend performed well in June. The long portfolio was down 2.0% vs. MSCI China down 7.1%. With the short book down 5.5%, the L/S gained 3.5%. For July, the Blend model adds to longs mainly energy, IT, materials, and brokers, including PetroChina, Sungrow Power, Kingboard Laminates, CITIC, Jiangxi Copper, etc. On the shorts, the model adds Wuliangye, HTSC, Hua Hong Semiconductor, Changan Auto, Hainan Airlines, etc.

Figure 3: Multifactor Blend: Long-Only vs. Market  
![](images/8a172930d32a598b24874d0b15816618573cbe33143f60a8e701a5b05c85a9b5.jpg)  
Source: JPM; MSCI, FactSet, I/B/E/S, Bloomberg Finance L.P.

Figure 4: Multifactor Blend: Long/Short  
![](images/f2fed78ad517ba39cb899ec9b1cbf2ff5504a0fcf939ba3d5b05804c8b223b1d.jpg)  
Source: JPM; MSCI, FactSet, I/B/E/S, Bloomberg Finance L.P.

We flagged that cross-sectional vol was already elevated at the $98^{th}$ percentile as of May. In June, it rose further to the 99th percentile of the past 10 years. Index vol also caught up, moving from the 29th percentile to the 77th percentile.

Figure 5: MSCI China Index Vol vs. Cross-Sectional Vol  
![](images/9a709f5995b44b980901afbb76071ed78ff158502d8fbb662f9c81f37663cad2.jpg)  
Source: JPM; MSCI, FactSet; As of Jun 30

Figure 6: Monthly Return Distribution of June  
![](images/1c4a592c0338fbc3bbe25e8125ec8c1519558aa2556a5f55905171dfc33c5f2d.jpg)  
Source: JPM; MSCI, FactSet

Figure 7: Stocks Matching the Direction of the Market  
![](images/d200aea265ac8425581ba30218324b7f3f7cd9cc3cffc070a07924a3f97fe8b8.jpg)  
Source: JPM; MSCI, FactSet. Note: Past performance is not an indicator of future results.

Figure 8: Stocks Near 52-Week Extremes  
![](images/6ca9f17a574650c5f0616b623bdce1c100d9d70517d2d29fe609066337adc21b.jpg)  
Source: JPM; MSCI, FactSet

Table 2: Low Vol, High Quality Yielders

<table><tr><td colspan="4">Low Vol &amp; High Quality Yielders</td></tr><tr><td>SEDOL</td><td>Company</td><td>Sector</td><td>1M Return</td></tr><tr><td>BP3R2X9</td><td>China United Network Communications Limited Clas</td><td>Comm Svcs</td><td>-7.1%</td></tr><tr><td>BKPQZT6</td><td>JD.com, Inc. Class A</td><td>Cons Disc</td><td>-12.6%</td></tr><tr><td>B1YVKN8</td><td>ANTA Sports Products Ltd</td><td>Cons Disc</td><td>-6.3%</td></tr><tr><td>BQB7ZL7</td><td>Midea Group Co. Ltd. Class H</td><td>Cons Disc</td><td>1.3%</td></tr><tr><td>BD5CPP1</td><td>Midea Group Co. Ltd. Class A</td><td>Cons Disc</td><td>-2.3%</td></tr><tr><td>BP3R3G9</td><td>Haier Smart Home Co., Ltd. Class A</td><td>Cons Disc</td><td>-2.6%</td></tr><tr><td>BD5CPN9</td><td>Gree Electric Appliances, Inc. of Zhuhai Class A</td><td>Cons Disc</td><td>-4.6%</td></tr><tr><td>BP3R2F1</td><td>Kweichow Moutai Co., Ltd. Class A</td><td>Cons Staples</td><td>-8.7%</td></tr><tr><td>6972459</td><td>China Resources Beer Holdings Co Ltd</td><td>Cons Staples</td><td>-12.1%</td></tr><tr><td>BD5CPG2</td><td>Wuliangye Yibin Co., Ltd. Class A</td><td>Cons Staples</td><td>-13.1%</td></tr><tr><td>BTFRHX0</td><td>Foshan Haitian Flavouring &amp; Food Co., Ltd. Class</td><td>Cons Staples</td><td>-5.8%</td></tr><tr><td>BP3R2V7</td><td>Inner Mongolia Yili Industrial Group Co., Ltd. C</td><td>Cons Staples</td><td>-8.2%</td></tr><tr><td>BP3R820</td><td>Shanxi Xinghuacun Fen Wine Factory Co. Ltd. Clas</td><td>Cons Staples</td><td>-15.0%</td></tr><tr><td>B09N7M0</td><td>China Shenhua Energy Co Ltd</td><td>Energy</td><td>-11.1%</td></tr><tr><td>BP3R262</td><td>China Shenhua Energy Co. Ltd. Class A</td><td>Energy</td><td>-17.1%</td></tr><tr><td>BS7K5P8</td><td>Shaanxi Coal Industry Co., Ltd. Class A</td><td>Energy</td><td>-17.7%</td></tr><tr><td>B0LMTQ3</td><td>China Construction Bank Corp</td><td>Financials</td><td>-5.0%</td></tr><tr><td>B1G1QD8</td><td>Industrial &amp; Commercial Bank of China Ltd</td><td>Financials</td><td>-3.2%</td></tr><tr><td>B1DYPZ5</td><td>China Merchants Bank Co Ltd</td><td>Financials</td><td>-4.7%</td></tr><tr><td>6706250</td><td>PICC Property &amp; Casualty Co Ltd</td><td>Financials</td><td>-1.7%</td></tr><tr><td>BP3R273</td><td>China Merchants Bank Co., Ltd. Class A</td><td>Financials</td><td>-6.9%</td></tr><tr><td>B8RZJZ1</td><td>People&#x27;s Insurance Co Group of China Ltd/The</td><td>Financials</td><td>-9.5%</td></tr><tr><td>BP3R217</td><td>Industrial and Commercial Bank of China Limited</td><td>Financials</td><td>-2.4%</td></tr><tr><td>BD5CP95</td><td>Yunnan Baiyao Group Co. Ltd. Class A</td><td>Health Care</td><td>-5.4%</td></tr><tr><td>BMZ1C83</td><td>ZTO Express (Cayman) Inc. Class A</td><td>Industrials</td><td>-1.3%</td></tr><tr><td>B0B8Z18</td><td>China COSCO Holdings Co Ltd</td><td>Industrials</td><td>-8.3%</td></tr><tr><td>BP3R552</td><td>COSCO SHIPPING Holdings Co., Ltd. Class A</td><td>Industrials</td><td>-3.4%</td></tr><tr><td>BP3R358</td><td>CRRC Corporation Limited Class A</td><td>Industrials</td><td>-10.2%</td></tr><tr><td>BD5CH66</td><td>Zhejiang NHU Co. Ltd. Class A</td><td>Materials</td><td>-3.5%</td></tr><tr><td>BP3R2M8</td><td>China Yangtze Power Co., Ltd. Class A</td><td>Utilities</td><td>-4.9%</td></tr><tr><td>6333937</td><td>ENN Energy Holdings Ltd</td><td>Utilities</td><td>-23.1%</td></tr></table>

Source: JPM; MSCI, FactSet, I/B/E/S, Bloomberg Finance L.P.; As of Jun 30. Note: Past performance is not an indicator of future results.

Figure 9: Multifactor Blend: Long Positions for July

<table><tr><td colspan="5">Top Longs</td></tr><tr><td>SEDOL</td><td>Company</td><td>Sector</td><td>Rank</td><td>1M Return</td></tr><tr><td>BD5CG58</td><td>Zhejiang Century Huatong Group Co., Ltd. Class A</td><td>Comm Svcs</td><td>39</td><td>-3.6%</td></tr><tr><td>6531827</td><td>Geely Automobile Holdings Ltd</td><td>Cons Disc</td><td>34</td><td>-8.1%</td></tr><tr><td>BN6PP37</td><td>Pop Mart International Group Limited</td><td>Cons Disc</td><td>26</td><td>-10.9%</td></tr><tr><td>6718255</td><td>Great Wall Motor Co Ltd</td><td>Cons Disc</td><td>46</td><td>-15.4%</td></tr><tr><td>BZ04KX9</td><td>Yadea Group Holdings Ltd</td><td>Cons Disc</td><td>21</td><td>-16.7%</td></tr><tr><td>BP3R4T9</td><td>HUAYU Automotive Systems Company Limited Class A</td><td>Cons Disc</td><td>29</td><td>-7.4%</td></tr><tr><td>BMGWW30</td><td>Nongfu Spring Co., Ltd. Class H</td><td>Cons Staples</td><td>37</td><td>-7.5%</td></tr><tr><td>BD5CMC7</td><td>Yantai Jereh Oilfield Services Group Co., Ltd. C</td><td>Energy</td><td>15</td><td>8.8%</td></tr><tr><td>BD5CG92</td><td>Inner Mongolia Dian Tou Energy Corporation Limit</td><td>Energy</td><td>33</td><td>-25.5%</td></tr><tr><td>6718976</td><td>China Life Insurance Co Ltd</td><td>Financials</td><td>31</td><td>-5.3%</td></tr><tr><td>B2Q5H56</td><td>China Pacific Insurance Group Co Ltd</td><td>Financials</td><td>53</td><td>-10.9%</td></tr><tr><td>B5730Z1</td><td>New China Life Insurance Co Ltd</td><td>Financials</td><td>20</td><td>-5.1%</td></tr><tr><td>BZ169C6</td><td>CHINA INTERNATIONAL CAPITA-H</td><td>Financials</td><td>22</td><td>8.3%</td></tr><tr><td>6264048</td><td>China Taiping Insurance Holdings Co Ltd</td><td>Financials</td><td>7</td><td>-9.4%</td></tr><tr><td>BYW5MY8</td><td>Bank of Jiangsu Co., Ltd. Class A</td><td>Financials</td><td>49</td><td>-4.8%</td></tr><tr><td>BD5CN46</td><td>Hithink RoyalFlush Information Network Co., Ltd.</td><td>Financials</td><td>1</td><td>5.5%</td></tr><tr><td>BGHH0L6</td><td>WuXi AppTec Co., Ltd. Class H</td><td>Health Care</td><td>51</td><td>17.9%</td></tr><tr><td>BY9D3L9</td><td>3SBio Inc</td><td>Health Care</td><td>5</td><td>-8.8%</td></tr><tr><td>B3ZVDV0</td><td>Sinopharm Group Co Ltd</td><td>Health Care</td><td>4</td><td>-1.2%</td></tr><tr><td>BHWLWV4</td><td>WuXi AppTec Co., Ltd. Class A</td><td>Health Care</td><td>50</td><td>22.2%</td></tr><tr><td>BP3R4Z5</td><td>Shanghai Pharmaceuticals Holding Co. Ltd. Class</td><td>Health Care</td><td>9</td><td>-6.8%</td></tr><tr><td>BD5CL42</td><td>China Resources Sanjiu Medical &amp; Pharmaceutical</td><td>Health Care</td><td>19</td><td>-8.3%</td></tr><tr><td>6218089</td><td>Lenovo Group Ltd</td><td>IT</td><td>13</td><td>-4.2%</td></tr><tr><td>B1HHFV6</td><td>Kingboard Laminates Holdings Ltd</td><td>IT</td><td>48</td><td>83.2%</td></tr><tr><td>BFFJRM7</td><td>Zhongji Innolight Co., Ltd. Class A</td><td>IT</td><td>3</td><td>9.0%</td></tr><tr><td>BNHPMD5</td><td>Cambricon Technologies Corp. Ltd. Class A</td><td>IT</td><td>14</td><td>21.4%</td></tr><tr><td>BD761B9</td><td>Eoptolink Technology Inc., Ltd. Class A</td><td>IT</td><td>2</td><td>20.1%</td></tr><tr><td>BG20N99</td><td>Foxconn Industrial Internet Co., Ltd. Class A</td><td>IT</td><td>25</td><td>-2.0%</td></tr><tr><td>B1YBT08</td><td>Sunny Optical Technology Group Co Ltd</td><td>IT</td><td>24</td><td>-26.2%</td></tr><tr><td>BD5CF28</td><td>Suzhou Dongshan Precision Manufacturing Co., Ltd</td><td>IT</td><td>45</td><td>22.8%</td></tr><tr><td>BP3RC39</td><td>Shengyi Technology Co., Ltd. Class A</td><td>IT</td><td>52</td><td>23.6%</td></tr><tr><td>BK71F77</td><td>Montage Technology Co., Ltd. Class A</td><td>IT</td><td>58</td><td>22.1%</td></tr><tr><td>BL5P4J3</td><td>Suzhou TFC Optical Communication Co., Ltd. Class</td><td>IT</td><td>18</td><td>-7.0%</td></tr><tr><td>BD76164</td><td>Victory Giant Technology (HuiZhou) Co., Ltd. Cla</td><td>IT</td><td>17</td><td>-6.3%</td></tr><tr><td>B29SHS5</td><td>BYD Electronic International Co Ltd</td><td>IT</td><td>16</td><td>-27.8%</td></tr><tr><td>BPXYTJ5</td><td>Yuanjie Semiconductor Technology Co., Ltd. Class</td><td>IT</td><td>6</td><td>66.0%</td></tr><tr><td>BGQYNN1</td><td>Xinyi Solar Holdings Ltd.</td><td>IT</td><td>55</td><td>-22.7%</td></tr><tr><td>BD5CP28</td><td>TCL Technology Group Corporation Class A</td><td>IT</td><td>47</td><td>38.3%</td></tr><tr><td>BD5CLB9</td><td>Inspur Electronic Information Industry Co., Ltd.</td><td>IT</td><td>60</td><td>8.0%</td></tr><tr><td>BQWRJD6</td><td>Shengyi Electronics Co., Ltd. Class A</td><td>IT</td><td>8</td><td>-3.9%</td></tr><tr><td>BD5CNJ1</td><td>Zhejiang Dahua Technology Co. Ltd. Class A</td><td>IT</td><td>28</td><td>-1.5%</td></tr><tr><td>BK71BV3</td><td>Shanghai Friendess Electronics Technology Corpor</td><td>IT</td><td>57</td><td>-7.3%</td></tr><tr><td>BFCCR07</td><td>Yealink Network Technology Co. Ltd. Class A</td><td>IT</td><td>23</td><td>-6.7%</td></tr><tr><td>BT9QPW8</td><td>Contemporary Amperex Technology Co., Limited Cla</td><td>Industrials</td><td>43</td><td>-5.8%</td></tr><tr><td>BHQPSY7</td><td>Contemporary Amperex Technology Co., Ltd. Class</td><td>Industrials</td><td>42</td><td>-7.6%</td></tr><tr><td>6196152</td><td>CITIC Ltd</td><td>Industrials</td><td>38</td><td>-16.1%</td></tr><tr><td>BD5CGB4</td><td>Sungrow Power Supply Co., Ltd. Class A</td><td>Industrials</td><td>56</td><td>-10.9%</td></tr><tr><td>BP91NG5</td><td>Ningbo Deye Technology Co., Ltd. Class A</td><td>Industrials</td><td>12</td><td>-8.5%</td></tr><tr><td>BP3R5T6</td><td>Yutong Bus Co., Ltd. Class A</td><td>Industrials</td><td>27</td><td>-17.3%</td></tr><tr><td>BQ3RQ89</td><td>Dajin Heavy Industry Co., Ltd. Class A</td><td>Industrials</td><td>11</td><td>-20.6%</td></tr><tr><td>B60FNV8</td><td>China Gold International Resources Corp. Ltd.</td><td>Materials</td><td>10</td><td>-18.5%</td></tr><tr><td>BD5CF40</td><td>Yintai Gold Co., Ltd. Class A</td><td>Materials</td><td>54</td><td>-24.5%</td></tr><tr><td>BSY22K1</td><td>Shandong Hongqiao Aluminum Industry Holding Comp</td><td>Materials</td><td>44</td><td>-30.7%</td></tr><tr><td>BZOD1S8</td><td>Chifeng Jilong Gold Mining Co., Ltd. Class A</td><td>Materials</td><td>40</td><td>-21.4%</td></tr><tr><td>BD5M0H8</td><td>Hunan Valin Steel Co., Ltd. Class A</td><td>Materials</td><td>59</td><td>-9.7%</td></tr><tr><td>BMXWXT6</td><td>China Resources Mixc Lifestyle Services Ltd.</td><td>Real Estate</td><td>36</td><td>-9.8%</td></tr><tr><td>BZBY9R5</td><td>C&amp;D International Investment Group Ltd.</td><td>Real Estate</td><td>35</td><td>-14.5%</td></tr><tr><td>6099671</td><td>Huaneng Power International Inc</td><td>Utilities</td><td>41</td><td>-18.6%</td></tr><tr><td>6913168</td><td>Guangdong Investment Ltd</td><td>Utilities</td><td>30</td><td>-7.1%</td></tr><tr><td>6081690</td><td>Beijing Enterprises Holdings Ltd</td><td>Utilities</td><td>32</td><td>-10.6%</td></tr></table>

Source: JPM; MSCI, FactSet, I/B/E/S, Bloomberg Finance L.P.; As of Jun 30

Figure 10: Multifactor Blend: Short Positions for July

<table><tr><td colspan="5">Top Shorts</td></tr><tr><td>SEDOL</td><td>Company</td><td>Sector</td><td>Rank</td><td>1M Return</td></tr><tr><td>BD5CN13</td><td>Kunlun Tech Co., Ltd. Class A</td><td>Comm Svcs</td><td>23</td><td>-8.4%</td></tr><tr><td>BGJW376</td><td>Meituan Dianping Class B</td><td>Cons Disc</td><td>42</td><td>-6.8%</td></tr><tr><td>BPR9XV6</td><td>NIO Inc. Class A</td><td>Cons Disc</td><td>50</td><td>-8.9%</td></tr><tr><td>BP6FB33</td><td>XPeng, Inc.

[中间内容因长度限制已省略]

dates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 Jul 2026 02:08 PM HKT

Disseminated 12 Jul 2026 03:04 PM HKT
"""
