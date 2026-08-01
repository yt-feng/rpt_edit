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
# Electronic Components Sector

MLCC eXchange: June 2026 trade data; will this be a summer of price hikes?

Japan Customs released the June 2026 trade statistics at 09:30 JST on July 30. We believe MLCC export trends by nation and region visible in the data shed some light on trends by application. In June, MLCC export volume followed seasonal patterns, while export value slightly exceeded seasonal trends. The trend line shows that export value continued to grow on a yen basis, as well as at a moderate pace on a US dollar basis, with double-digit YoY growth sustained on a 3MMA basis. Average selling price (in US dollars) also continues on a moderate uptrend. For automotive applications, export value to the US (in US dollars) is showing a moderate upward trend, while export value to Europe are exhibiting a slight downward trend, resulting in regional differences. Overall, the trend is shifting from flat to moderate growth. For IT applications, the overall uptrend continues. By region, export value to Taiwan declined MoM in June, but the overall upward trend remains intact. Our top pick among MLCC names is Murata Mfg.

## Our view

\- We have not changed our longer-term view on MLCC industry fundamentals, but the share prices of Japanese MLCC manufacturers (Murata Mfg, Taiyo Yuden, TDK) underwent a significant correction after peaking in mid-June. For MLCC stocks, especially Murata Mfg and Taiyo Yuden, market conditions for MLCCs began to tighten in earnest in late January–March, and over the following 2-3 months through June, the equity market quickly priced in 3-4 years of future earnings growth potential. Valuations have also declined to levels below the upper end of their historical ranges, and now appear to be at levels that can be explained by earnings two or three years out.

\- On the fundamentals side, supply-demand conditions tightened further, especially for mid- and high-end MLCCs. Each company is moving to increase production of MLCCs for AI servers, and as some manufacturers prioritize supply for AI servers, we expect supply of general-purpose and mid-range products to become even tighter heading into July-September. Concerns about MLCC supply-demand tightness and shortages are also rising among set manufacturers.

\- In the MLCC market, negotiations for annual contracts for cutting-edge products for AI servers in 2027 and price hike notifications to distributors are beginning to ramp up. Meanwhile, we believe some MLCC manufacturers are moving to start price hike negotiations with major direct customers over the summer, and we will closely monitor developments. Our channel checks indicate that some MLCC users are beginning to accept price increases from MLCC makers in order to secure volumes. In addition, some MLCC manufacturers have started negotiations for annual contracts in 2027 that involve significant price hikes not only for AI servers but also with major EMS, OEM, and ODM customers. We will continue to monitor the progress of these negotiations.

\- Some MLCC manufacturers have begun negotiations on price hikes due to supply-demand tightness, and we are watching closely to see how MLCC manufacturers will react to this trend. We believe that if manufacturers do not follow through on price hikes, they risk receiving a concentration of orders for unprofitable products, resulting in a situation where they are busy but not

See page 15 for analyst certification and important disclosures, including non-US analyst disclosures.

Japan Equity Research

Technology - Electronic Components

Akinori Kanemoto AC

(81-3) 6736 8628

akinori.kanemoto@JPM.com

Ikki Shibata

(81-3) 6736 8641

ikki.shibata@JPM.com

JPM Securities Japan Co., Ltd.

profitable.

\- If Japanese MLCC manufacturers raise prices in reaction to supply-demand tightness, we expect the psychological hurdle for negotiating price hikes to decrease for other electronic components, especially passive components.

## Summary of statistics

\- In June 2026, total export volume was 88.957 billion units (+6.5% YoY, +6.1% MoM), export value was \$448 million (+18.2% YoY, +8.9% MoM), and the average selling price was \$0.50 (+11.0% YoY, +2.6% MoM) (Figure 2). Over the past 10 years, seasonality has typically seen export volume rise 8.6% MoM and export value rise 4.9% MoM, but this June, volume followed seasonal patterns while value slightly exceeded seasonal trends. The trend line, however, shows export value remained on a growth trend on a yen basis. We maintain our view that a moderate upward trend continues in dollar terms. Total shipment value for April-June rose 14% QoQ in yen terms and 13% in US dollar terms, and increased 26% YoY in yen terms and 14% YoY in US dollar terms, maintaining strong momentum.

\- Automotive applications have a high weighting within exports to Europe (Germany, the Netherlands) and the US, and for these destinations, export volume was 9.995 billion units (+19.3% YoY, +16.2% MoM), export value was \$74.2 million (+6.3% YoY, +17.6% MoM), and the average selling price was \$0.74 (-10.9% YoY, +1.2% MoM). Over the past 10 years, seasonality has seen export volume rise 1.9% MoM and export value rise 1.2% MoM, but this June, both increased well above seasonal trends. The trend line shows export volume is rising slightly, but export value in US dollar terms remains flat. For export value, shipments to the US show a moderate upward trend, while those to Europe are on a slight downward trend, resulting in regional differences.

\- For major Asian markets with a high weighting of IT applications (China, Hong Kong, Taiwan, South Korea, Vietnam, the Philippines, and India), export volume was 71.595 billion units (+2.9% YoY, +4.4% MoM), export value was \$323.1 million (+20.1% YoY, +7.7% MoM), and the average selling price was \$0.45 (+16.7% YoY, +3.1% MoM). Seasonality over the past 10 years has seen export volume rise 10.0% MoM and export value rise 6.6% MoM, but this June, export volume fell short while export value generally tracked seasonal trends. In US dollar terms, export value to China in June was relatively strong, rising 12.2% YoY and 10.3% MoM. Although exports to Taiwan declined MoM, they remain on an upward trend. For exports to Taiwan, the average selling price rose sharply in June to \$0.54 (+57.9% YoY, +15.5% MoM). Exports to Hong Kong have also shown signs of a minor recovery since around last summer, while exports to South Korea remain flat.

Figure 1: MLCC Valuation Comp

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company</td><td rowspan="2">Share Price (LC)</td><td rowspan="2">Price Target (LC)</td><td rowspan="2">Return</td><td rowspan="2">JPM Rating</td><td rowspan="2">Market Capitalization (LC)</td><td colspan="2">P/E</td><td colspan="2">P/E Consensus(BBG)</td><td colspan="2">EV/EBITDA</td><td colspan="2">P/B</td><td colspan="2">ROE</td><td rowspan="2">Price YTD</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td>6981</td><td>Murata Mfg.</td><td>6,231</td><td>15,200</td><td>143.9%</td><td>OW</td><td>(JPY mn)</td><td>13,242,410</td><td>45.75</td><td>28.31</td><td>33.66</td><td>24.27</td><td>29.53</td><td>19.39</td><td>5.25</td><td>4.64</td><td>11.57%</td><td>17.42%</td></tr><tr><td>6976</td><td>Taiyo Yuden</td><td>9,005</td><td>22,500</td><td>149.9%</td><td>OW</td><td>(JPY mn)</td><td>1,267,691</td><td>65.67</td><td>29.04</td><td>41.18</td><td>23.01</td><td>28.21</td><td>18.06</td><td>4.05</td><td>3.63</td><td>6.86%</td><td>14.42%</td></tr><tr><td>6762</td><td>TDK</td><td>2,746</td><td>5,500</td><td>100.3%</td><td>OW</td><td>(JPY mn)</td><td>5,669,267</td><td>25.44</td><td>19.98</td><td>22.33</td><td>18.91</td><td>12.10</td><td>10.04</td><td>2.45</td><td>2.27</td><td>9.94%</td><td>11.80%</td></tr><tr><td>009150 KS Equity</td><td>SEMCO</td><td>1,050,000</td><td>2,400,000</td><td>128.6%</td><td>OW</td><td>(KRW mn)</td><td>79,698,174</td><td>55.88</td><td>26.80</td><td>55.88</td><td>26.80</td><td>40.77</td><td>40.77</td><td>7.39</td><td>5.94</td><td>13.98%</td><td>23.61%</td></tr><tr><td>2327 TT Equity</td><td>Yageo</td><td>507</td><td>1,030</td><td>103.2%</td><td>OW</td><td>(TWD mn)</td><td>1,058,519</td><td>26.35</td><td>16.26</td><td>26.35</td><td>16.26</td><td>25.75</td><td>25.75</td><td>5.11</td><td>3.34</td><td>21.47%</td><td>29.63%</td></tr><tr><td>Simple Average</td><td></td><td>-</td><td>-</td><td>-</td><td></td><td></td><td>100,936,061</td><td>43.82</td><td>24.08</td><td>35.88</td><td>21.85</td><td>27.27</td><td>22.80</td><td>4.85</td><td>3.97</td><td>12.76%</td><td>19.37%</td></tr><tr><td>TWSE</td><td>TAIEX</td><td>40,039</td><td>NA</td><td>-</td><td>-</td><td>(TWD mn)</td><td>130,659,974</td><td>18.55</td><td>14.40</td><td>18.55</td><td>14.40</td><td>17.63</td><td>17.63</td><td>4.04</td><td>3.40</td><td>21.60%</td><td>23.36%</td></tr><tr><td>TPX</td><td>TOPIX</td><td>3,974</td><td>NA</td><td>-</td><td>-</td><td>(JPY mn)</td><td>1,323,027,382</td><td>17.47</td><td>15.81</td><td>17.47</td><td>15.81</td><td>9.48</td><td>9.48</td><td>1.72</td><td>1.62</td><td>9.44%</td><td>10.13%</td></tr><tr><td>KOSPI</td><td>KOSPI</td><td>5,663</td><td>NA</td><td>-</td><td>-</td><td>(KRW mn)</td><td>4,519,788,233</td><td>5.78</td><td>4.20</td><td>5.78</td><td>4.20</td><td>8.80</td><td>8.80</td><td>1.43</td><td>1.10</td><td>24.75%</td><td>26.21%</td></tr></table>

Source: Company reports, Bloomberg Finance L.P. consensus estimates, and JPM estimates.  
Note: Samsung Electro-Mechanics (SEMCO) is covered by Jay Kwon, and Yageo is covered by Jerry Tsai. Ratings and price targets are from JPM. For other data, the three Japanese MLCC companies are based on JPM estimates, and both SEMCO and Yageo are based on Bloomberg consensus. The share prices and Bloomberg consensus are as of the market close on July 29, 2026.

Figure 2: June 2026 MLCC Trade Statistics Summary by Region

<table><tr><td>Export Quantity</td><td>mn units</td><td>YoY</td><td>MoM</td></tr><tr><td>Total</td><td>88,957</td><td>6.5%</td><td>6.1%</td></tr><tr><td>Main for IT</td><td>71,595</td><td>2.9%</td><td>4.4%</td></tr><tr><td>Main for Automotive</td><td>9,995</td><td>19.3%</td><td>16.2%</td></tr><tr><td>For Korea</td><td>6,314</td><td>-11.4%</td><td>3.4%</td></tr><tr><td>For China</td><td>27,634</td><td>-0.7%</td><td>7.2%</td></tr><tr><td>For Taiwan</td><td>12,216</td><td>-25.0%</td><td>-17.1%</td></tr><tr><td>For Hong Kong</td><td>17,351</td><td>45.8%</td><td>14.5%</td></tr><tr><td>For Vietnam</td><td>4,882</td><td>40.1%</td><td>25.8%</td></tr><tr><td>For India</td><td>3,199</td><td>8.8%</td><td>9.1%</td></tr><tr><td>For Germany &amp; Netherlands</td><td>4,566</td><td>25.9%</td><td>18.4%</td></tr><tr><td>For USA</td><td>5,430</td><td>14.2%</td><td>14.4%</td></tr></table>

<table><tr><td>Export Value</td><td>¥mn</td><td>YoY</td><td>MoM</td></tr><tr><td>Total</td><td>71,971</td><td>31.5%</td><td>10.7%</td></tr><tr><td>Main for IT</td><td>51,972</td><td>33.7%</td><td>9.4%</td></tr><tr><td>Main for Automotive</td><td>11,941</td><td>18.2%</td><td>19.5%</td></tr><tr><td>For Korea</td><td>4,800</td><td>5.5%</td><td>7.8%</td></tr><tr><td>For China</td><td>22,764</td><td>24.8%</td><td>12.1%</td></tr><tr><td>For Taiwan</td><td>10,674</td><td>31.8%</td><td>-2.7%</td></tr><tr><td>For Hong Kong</td><td>10,683</td><td>85.4%</td><td>14.3%</td></tr><tr><td>For Vietnam</td><td>2,128</td><td>47.8%</td><td>31.4%</td></tr><tr><td>For India</td><td>924</td><td>16.6%</td><td>15.4%</td></tr><tr><td>For Germany &amp; Netherlands</td><td>5,512</td><td>7.2%</td><td>13.2%</td></tr><tr><td>For USA</td><td>6,430</td><td>29.7%</td><td>25.5%</td></tr></table>

<table><tr><td>Export Value</td><td>$mn</td><td>YoY</td><td>MoM</td></tr><tr><td>Total</td><td>447.5</td><td>18.2%</td><td>8.9%</td></tr><tr><td>Main for IT</td><td>323.1</td><td>20.1%</td><td>7.7%</td></tr><tr><td>Main for Automotive</td><td>74.2</td><td>6.3%</td><td>17.6%</td></tr><tr><td>For Korea</td><td>29.8</td><td>-5.2%</td><td>6.0%</td></tr><tr><td>For China</td><td>141.5</td><td>12.2%</td><td>10.3%</td></tr><tr><td>For Taiwan</td><td>66.4</td><td>18.4%</td><td>-4.3%</td></tr><tr><td>For Hong Kong</td><td>66.4</td><td>66.7%</td><td>12.5%</td></tr><tr><td>For Vietnam</td><td>13.2</td><td>32.8%</td><td>29.3%</td></tr><tr><td>For India</td><td>5.7</td><td>4.8%</td><td>13.6%</td></tr><tr><td>For Germany &amp; Netherlands</td><td>34.3</td><td>-3.7%</td><td>11.4%</td></tr><tr><td>For USA</td><td>40.0</td><td>16.5%</td><td>23.5%</td></tr></table>

<table><tr><td>ASP</td><td>JPY</td><td>YoY</td><td>MoM</td></tr><tr><td>Total</td><td>0.81</td><td>23.5%</td><td>4.3%</td></tr><tr><td>Main for IT</td><td>0.73</td><td>29.9%</td><td>4.8%</td></tr><tr><td>Main for Automotive</td><td>1.19</td><td>-0.9%</td><td>2.9%</td></tr><tr><td>For Korea</td><td>0.76</td><td>19.0%</td><td>4.2%</td></tr><tr><td>For China</td><td>0.82</td><td>25.7%</td><td>4.6%</td></tr><tr><td>For Taiwan</td><td>0.87</td><td>75.7%</td><td>17.4%</td></tr><tr><td>For Hong Kong</td><td>0.62</td><td>27.2%</td><td>-0.2%</td></tr><tr><td>For Vietnam</td><td>0.44</td><td>5.5%</td><td>4.4%</td></tr><tr><td>For India</td><td>0.29</td><td>7.2%</td><td>5.8%</td></tr><tr><td>For Germany &amp; Netherlands</td><td>1.21</td><td>-14.9%</td><td>-4.4%</td></tr><tr><td>For USA</td><td>1.18</td><td>13.6%</td><td>9.7%</td></tr></table>

Source: Ministry of Finance, JPM.

<table><tr><td>ASP</td><td>US cents</td><td>YoY</td><td>MoM</td></tr><tr><td>Total</td><td>0.50</td><td>11.0%</td><td>2.6%</td></tr><tr><td>Main for IT</td><td>0.45</td><td>16.7%</td><td>3.1%</td></tr><tr><td>Main for Automotive</td><td>0.74</td><td>-10.9%</td><td>1.2%</td></tr><tr><td>For Korea</td><td>0.47</td><td>6.9%</td><td>2.5%</td></tr><tr><td>For China</td><td>0.51</td><td>13.0%</td><td>2.9%</td></tr><tr><td>For Taiwan</td><td>0.54</td><td>57.9%</td><td>15.5%</td></tr><tr><td>For Hong Kong</td><td>0.38</td><td>14.3%</td><td>-1.8%</td></tr><tr><td>For Vietnam</td><td>0.27</td><td>-5.2%</td><td>2.8%</td></tr><tr><td>For India</td><td>0.18</td><td>-3.6%</td><td>4.1%</td></tr><tr><td>For Germany &amp; Netherlands</td><td>0.75</td><td>-23.5%</td><td>-5.9%</td></tr><tr><td>For USA</td><td>0.74</td><td>2.1%</td><td>7.9%</td></tr></table>

# Total MLCC Exports

Figure 3: MLCC Export Quantity (thousands of units)  
![](images/f598f6b560512747a3045b3dca6a522040a2da96c22ec8fa1e3ff0e452ecefce.jpg)  
Source: Ministry of Finance, JPM.

Figure 4: MLCC Export Weight (kg)  
![](images/a5205e82dc0a88f4eaa5189fa6c3619abc64b16115561520126bd7367ddc85bb.jpg)  
Source: Ministry of Finance, JPM.

Figure 5: MLCC Export Value (¥ thousand)  
![](images/63b762104be17a677bc722feff2a804814b6dd9b3dd1d9b14e834edab15bc08d.jpg)  
Source: Ministry of Finance, JPM.

Figure 6: MLCC Export Value (\$mn)  
![](images/9830d28cb4d3e6543feba46ee1086ee1ace9668cc4fc528ebf3ce3f73a237938.jpg)  
Source: Ministry of Finance, JPM.

Figure 7: MLCC Export ASP (¥)  
![](images/5e52c3f0061146e3996f5271fb7523612ab8ddcdb7c10b97f09ef1a0ef294de1.jpg)  
Source: Ministry of Finance, JPM.

Figure 8: MLCC Export ASP (US cents)  
![](images/48b1b22ff10efe919556187f008b2a2ae6cbfb530db1f56621bd5b3e99b9dbf6.jpg)  
Source: Ministry of Finance, JPM.

# Total IT Application-Related Exports by Region (China, Hong Kong, South Korea, Taiwan, India, Philippines, Vietnam)

Figure 9: MLCC Export Quantity (thousands of units)  
![](images/a3857aa863da7c41f178ab0d818bccac83590114c84bfe2281fbff4c9f0d4329.jpg)  
Source: Ministry of Finance, JPM.

Figure 10: MLCC Export Weight (kg)  
![](images/1a3d7d80c2e2e5fc220447dac160c4f3bc88fd3bc6e28b5617dc1d0d78252962.jpg)  
Source: Ministry of Finance, JPM.

Figure 11: MLCC Export Value (¥ thousand)  
![](images/b72a20526715b078005399a6cb7bb0d8f0f37a02

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
