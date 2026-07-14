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

<table><tr><td colspan="5">Top Longs</td></tr><tr><td>SEDOL</td><td>Company</td><td>Sector</td><td>Rank</td><td>1M Return</td></tr><tr><td>BD5CG58</td><td>Zhejiang Century Huatong Group Co., Ltd. Class A</td><td>Comm Svcs</td><td>39</td><td>-3.6%</td></tr><tr><td>6531827</td><td>Geely Automobile Holdings Ltd</td><td>Cons Disc</td><td>34</td><td>-8.1%</td></tr><tr><td>BN6PP37</td><td>Pop Mart International Group Limited</td><td>Cons Disc</td><td>26</td><td>-10.9%</td></tr><tr><td>6718255</td><td>Great Wall Motor Co Ltd</td><td>Cons Disc</td><td>46</td><td>-15.4%</td></tr><tr><td>BZ04KX9</td><td>Yadea Group Holdings Ltd</td><td>Cons Disc</td><td>21</td><td>-16.7%</td></tr><tr><td>BP3R4T9</td><td>HUAYU Automotive Systems Company Limited Class A</td><td>Cons Disc</td><td>29</td><td>-7.4%</td></tr><tr><td>BMGWW30</td><td>Nongfu Spring Co., Ltd. Class H</td><td>Cons Staples</td><td>37</td><td>-7.5%</td></tr><tr><td>BD5CMC7</td><td>Yantai Jereh Oilfield Services Group Co., Ltd. C</td><td>Energy</td><td>15</td><td>8.8%</td></tr><tr><td>BD5CG92</td><td>Inner Mongolia Dian Tou Energy Corporation Limit</td><td>Energy</td><td>33</td><td>-25.5%</td></tr><tr><td>6718976</td><td>China Life Insurance Co Ltd</td><td>Financials</td><td>31</td><td>-5.3%</td></tr><tr><td>B2Q5H56</td><td>China Pacific Insurance Group Co Ltd</td><td>Financials</td><td>53</td><td>-10.9%</td></tr><tr><td>B5730Z1</td><td>New China Life Insurance Co Ltd</td><td>Financials</td><td>20</td><td>-5.1%</td></tr><tr><td>BZ169C6</td><td>CHINA INTERNATIONAL CAPITA-H</td><td>Financials</td><td>22</td><td>8.3%</td></tr><tr><td>6264048</td><td>China Taiping Insurance Holdings Co Ltd</td><td>Financials</td><td>7</td><td>-9.4%</td></tr><tr><td>BYW5MY8</td><td>Bank of Jiangsu Co., Ltd. Class A</td><td>Financials</td><td>49</td><td>-4.8%</td></tr><tr><td>BD5CN46</td><td>Hithink RoyalFlush Information Network Co., Ltd.</td><td>Financials</td><td>1</td><td>5.5%</td></tr><tr><td>BGHH0L6</td><td>WuXi AppTec Co., Ltd. Class H</td><td>Health Care</td><td>51</td><td>17.9%</td></tr><tr><td>BY9D3L9</td><td>3SBio Inc</td><td>Health Care</td><td>5</td><td>-8.8%</td></tr><tr><td>B3ZVDV0</td><td>Sinopharm Group Co Ltd</td><td>Health Care</td><td>4</td><td>-1.2%</td></tr><tr><td>BHWLWV4</td><td>WuXi AppTec Co., Ltd. Class A</td><td>Health Care</td><td>50</td><td>22.2%</td></tr><tr><td>BP3R4Z5</td><td>Shanghai Pharmaceuticals Holding Co. Ltd. Class</td><td>Health Care</td><td>9</td><td>-6.8%</td></tr><tr><td>BD5CL42</td><td>China Resources Sanjiu Medical &amp; Pharmaceutical</td><td>Health Care</td><td>19</td><td>-8.3%</td></tr><tr><td>6218089</td><td>Lenovo Group Ltd</td><td>IT</td><td>13</td><td>-4.2%</td></tr><tr><td>B1HHFV6</td><td>Kingboard Laminates Holdings Ltd</td><td>IT</td><td>48</td><td>83.2%</td></tr><tr><td>BFFJRM7</td><td>Zhongji Innolight Co., Ltd. Class A</td><td>IT</td><td>3</td><td>9.0%</td></tr><tr><td>BNHPMD5</td><td>Cambricon Technologies Corp. Ltd. Class A</td><td>IT</td><td>14</td><td>21.4%</td></tr><tr><td>BD761B9</td><td>Eoptolink Technology Inc., Ltd. Class A</td><td>IT</td><td>2</td><td>20.1%</td></tr><tr><td>BG20N99</td><td>Foxconn Industrial Internet Co., Ltd. Class A</td><td>IT</td><td>25</td><td>-2.0%</td></tr><tr><td>B1YBT08</td><td>Sunny Optical Technology Group Co Ltd</td><td>IT</td><td>24</td><td>-26.2%</td></tr><tr><td>BD5CF28</td><td>Suzhou Dongshan Precision Manufacturing Co., Ltd</td><td>IT</td><td>45</td><td>22.8%</td></tr><tr><td>BP3RC39</td><td>Shengyi Technology Co., Ltd. Class A</td><td>IT</td><td>52</td><td>23.6%</td></tr><tr><td>BK71F77</td><td>Montage Technology Co., Ltd. Class A</td><td>IT</td><td>58</td><td>22.1%</td></tr><tr><td>BL5P4J3</td><td>Suzhou TFC Optical Communication Co., Ltd. Class</td><td>IT</td><td>18</td><td>-7.0%</td></tr><tr><td>BD76164</td><td>Victory Giant Technology (HuiZhou) Co., Ltd. Cla</td><td>IT</td><td>17</td><td>-6.3%</td></tr><tr><td>B29SHS5</td><td>BYD Electronic International Co Ltd</td><td>IT</td><td>16</td><td>-27.8%</td></tr><tr><td>BPXYTJ5</td><td>Yuanjie Semiconductor Technology Co., Ltd. Class</td><td>IT</td><td>6</td><td>66.0%</td></tr><tr><td>BGQYNN1</td><td>Xinyi Solar Holdings Ltd.</td><td>IT</td><td>55</td><td>-22.7%</td></tr><tr><td>BD5CP28</td><td>TCL Technology Group Corporation Class A</td><td>IT</td><td>47</td><td>38.3%</td></tr><tr><td>BD5CLB9</td><td>Inspur Electronic Information Industry Co., Ltd.</td><td>IT</td><td>60</td><td>8.0%</td></tr><tr><td>BQWRJD6</td><td>Shengyi Electronics Co., Ltd. Class A</td><td>IT</td><td>8</td><td>-3.9%</td></tr><tr><td>BD5CNJ1</td><td>Zhejiang Dahua Technology Co. Ltd. Class A</td><td>IT</td><td>28</td><td>-1.5%</td></tr><tr><td>BK71BV3</td><td>Shanghai Friendess Electronics Technology Corpor</td><td>IT</td><td>57</td><td>-7.3%

[中间内容因长度限制已省略]

mance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 12 Jul 2026 02:08 PM HKT

Disseminated 12 Jul 2026 03:04 PM HKT
"""
