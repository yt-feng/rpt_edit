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
## Ninebot Ltd (689009.SS): 2Q26 Preview: Rev growth acceleration and share gains amid weak but improving beta, easing margin pressure; Buy

Ninebot is expected to release its 2Q26 results in on Aug 10. We expect the company to report sequential revenue growth acceleration (+27% yoy in 2Q26 vs +15% yoy in 1Q26) driven by accelerating growth from robotic lawn mowers and 2B scooters, while E2W, 2C scooters and all-terrain vehicle maintained similar robust revenue growth momentum as 1Q. On margins, we foresee continued yoy pressure due to FX and cost headwinds, but expect the margin pressure to notably narrow qoq (net profits -5% yoy in 2Q26 vs -55% in 1Q26) as FX denominated trade balance decreased and product mix tilted towards higher-margin robotic lawn mowers (RLM) and 2B E-scooters in 2Q26. If excluding FX negative impacts (expected FX losses in 2Q26 vs \~Rmb180mn FX gains last year), we expect DD% recurring profits growth.

Ninebot's share price has rebounded by 11% post its investor day (vs -5%/0% for CSI300/our coverage average), where management presented a clear five-year growth roadmap with continuous outperformance across different business segments. We still see favorable risk-reward with the stock trading at 15.5x 26E P/E (vs. 20x avg fwd PE in the past two years), with 4% dividend yield and Rmb150-300mn buyback for cancellation (implying 0.5%-1% of shareholder return). We expect sequential improvements into 2H, particularly recovery of E2W demand and easing cost inflation/FX headwinds, to drive re-rating of the stock. Key catalysts include sequential profits growth improvements from its incoming quarterly results, improving domestic E2W demand and final settlement of the anti-dumping investigation on robotic lawn mowers (EU decided not to impose provisional anti-dumping duties yet continued the investigation on June 19).

We fine-tune our 2026E-28E EPS forecasts by -1%-3%, reflecting revised cost and FX assumptions partially offset by improving product mix. Our unchanged 12-m TP of Rmb62 is based on a 16x exit P/E multiple applied to our 2028E EPS and discounted back to 2027E using a 9.5% cost of equity. Reiterate Buy on its intact structural growth thesis, improving near-term profitability/domestic demand, and overall favorable risk/reward.

## Relevant reports:

Ninebot Ltd (689009.SS): Chairman meeting takeaways: A clear five-year growth roadmap with continued outperformance; Buy

China Consumer Durables: EU anti-dumping investigation on Chinese RLMs to continue but not imposing provisional duties at this time

Nicolas Yi
+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

Cecilia Tang
+86(21)2401-8738 |
cecilia.tang@goldmansachs.cn
GS (China) Securities
Company Limited

Ninebot Ltd (689009.SS): Management call takeaways: Improving E2W demand with new products launch to boost growth and margins; Buy

Ninebot Ltd (689009.SS): 1Q26 Earnings review: Resilient rev showing intact competitiveness, margin impacted by cyclical factors; Buy

Exhibit 1: We fine-tune our 2026E-28E forecasts by -1%-3%, reflecting revised cost and FX assumptions partially offset by improving product mix
New vs Old

<table><tr><td rowspan="2">Ninebot Technology Co Ltd689009.SS</td><td rowspan="2">2022</td><td rowspan="2">2023</td><td rowspan="2">2024</td><td rowspan="2">2025</td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">Change</td></tr><tr><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Revenue</td><td>10,124</td><td>10,222</td><td>14,196</td><td>21,278</td><td>26,167</td><td>32,613</td><td>38,257</td><td>26,072</td><td>32,521</td><td>38,143</td><td>0.4%</td><td>0.3%</td><td>0.3%</td></tr><tr><td>Growth, yoy %</td><td>10.7%</td><td>1.0%</td><td>38.9%</td><td>49.9%</td><td>23.0%</td><td>24.6%</td><td>17.3%</td><td>22.5%</td><td>24.7%</td><td>17.3%</td><td>0.4%</td><td>-0.1%</td><td>0.0%</td></tr><tr><td>GPM</td><td>26.0%</td><td>26.9%</td><td>28.2%</td><td>29.6%</td><td>28.1%</td><td>28.7%</td><td>29.7%</td><td>28.3%</td><td>28.9%</td><td>29.8%</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td></tr><tr><td>GPM chg (bps)</td><td>275</td><td>92</td><td>134</td><td>139</td><td>(154)</td><td>62</td><td>95</td><td>(138)</td><td>64</td><td>93</td><td></td><td></td><td></td></tr><tr><td>EBIT</td><td>406</td><td>421</td><td>1,131</td><td>1,876</td><td>2,135</td><td>2,800</td><td>3,612</td><td>2,158</td><td>2,836</td><td>3,647</td><td>-1.1%</td><td>-1.2%</td><td>-1.0%</td></tr><tr><td>Growth, yoy %</td><td>-14.3%</td><td>3.8%</td><td>168.5%</td><td>65.8%</td><td>13.8%</td><td>31.2%</td><td>29.0%</td><td>15.0%</td><td>31.4%</td><td>28.6%</td><td>-1.3%</td><td>-0.2%</td><td>0.4%</td></tr><tr><td>OPM</td><td>4.0%</td><td>4.1%</td><td>8.0%</td><td>8.8%</td><td>8.2%</td><td>8.6%</td><td>9.4%</td><td>8.3%</td><td>8.7%</td><td>9.6%</td><td>-0.1%</td><td>-0.1%</td><td>-0.1%</td></tr><tr><td>OPM chg (bps)</td><td>(117)</td><td>11</td><td>385</td><td>85</td><td>(66)</td><td>43</td><td>85</td><td>(54)</td><td>44</td><td>84</td><td></td><td></td><td></td></tr><tr><td>Net income</td><td>451</td><td>598</td><td>1,084</td><td>1,758</td><td>1,726</td><td>2,533</td><td>3,212</td><td>1,787</td><td>2,568</td><td>3,253</td><td>-3.4%</td><td>-1.4%</td><td>-1.2%</td></tr><tr><td>Growth, yoy %</td><td>9.7%</td><td>32.7%</td><td>81.3%</td><td>62.2%</td><td>-1.8%</td><td>46.8%</td><td>26.8%</td><td>1.7%</td><td>43.7%</td><td>26.7%</td><td>-3.5%</td><td>3.1%</td><td>0.2%</td></tr><tr><td>NPM</td><td>4.5%</td><td>5.9%</td><td>7.6%</td><td>8.3%</td><td>6.6%</td><td>7.8%</td><td>8.4%</td><td>6.9%</td><td>7.9%</td><td>8.5%</td><td>-0.3%</td><td>-0.1%</td><td>-0.1%</td></tr><tr><td>EPS (CDR share)</td><td>0.63</td><td>0.84</td><td>1.53</td><td>2.47</td><td>2.40</td><td>3.52</td><td>4.46</td><td>2.48</td><td>3.56</td><td>4.52</td><td>-3.4%</td><td>-1.4%</td><td>-1.2%</td></tr></table>

Source: Company data, GS Global Investment Research

## Preview by segment

E2W: We expect Ninebot to continue to outperform peers with a teens% yoy growth in 2Q26 on back of market share gains against industry demand pressure. The above said, we note that industry demand has been in recovery trend since hitting trough in Jan-Feb. The yoy domestic demand decline has been narrowing vs 1Q (-13% yoy in 1H26 vs -17% yoy in 1Q26) as the industry enters peak season and players launch more new SKUs accordingly. Particularly, the decline notably narrowed to -4% yoy in June. Looking into 2H, we expect further improvement potential considering more contribution from recent new product launch, fading impacts from front-loaded demand due to trade-in subsidy boost/national standards transition, and a lower comp base especially into 4Q26.

\- Robotic lawn mowers: We expect Ninebot's robotic lawn mower sales to more than double during the peak season in 2Q26, extending the structural growth momentum as indicated by strong app downloads growth tracked by SensorTower in our monthly tracker. Looking into 2H, we expect RLM sales contribution to be lower due to weakening seasonality, but expect its yoy growth to remain robust as overall demand remains strong.

Electric scooters: We expect electric scooters sales to accelerate in 2Q vs 1Q, supported by 1) strong 2C growth extending the momentum in 1Q amid rising energy prices in Europe, and 2) delayed revenue recognition of 2B business from 1Q that would contribute a yoy growth in 2Q. Looking into 2H, we expect 2C growth to remain solid, while 2B growth to normalize.

Cost inflation impacts: On cost inflation, management mentioned they have implemented a round of price increase in Apr alongside new product launches under an updated cost structure to mitigation cost impacts, and plans a second round of price increase with a similar magnitude in July. We thus expect the likely largest

impacts from cost inflation in 2Q, and sequential easing pressure into 2H with price and mix adjustments gradually kicking in, together with recent input price pull-back.

FX: We expect smaller drag from FX in 2Q vs 1Q (-Rmb248mn in 1Q primarily due to a combination of the company's large trade balance with European subsidiaries on robotic lawn mowers ahead of peak season and the sharp move in the EUR/CNY FX rate in a short period of time), considering the decreasing trade balance, enhanced hedging strategy and smaller magnitude of FX change. That said, we expect FX to continue to be a drag yoy considering its meaningful contribution in 2Q25 (Rmb227mn financial income in 2Q25).

Exhibit 2: Ninebot's key financials (Rmb mn)

<table><tr><td>Major P&amp;L items</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total sales/revenues</td><td>9,146</td><td>10,124</td><td>10,222</td><td>14,196</td><td>21,278</td><td>26,167</td><td>32,613</td><td>38,257</td></tr><tr><td>yoy %</td><td>52.4%</td><td>10.7%</td><td>1.0%</td><td>38.9%</td><td>49.9%</td><td>23.0%</td><td>24.6%</td><td>17.3%</td></tr><tr><td>Gross profit</td><td>2,124</td><td>2,630</td><td>2,750</td><td>4,008</td><td>6,305</td><td>7,349</td><td>9,363</td><td>11,345</td></tr><tr><td>Gross margin</td><td>23.2%</td><td>26.0%</td><td>26.9%</td><td>28.2%</td><td>29.6%</td><td>28.1%</td><td>28.7%</td><td>29.7%</td></tr><tr><td>change (bps)</td><td>(446)</td><td>275</td><td>92</td><td>134</td><td>139</td><td>(154)</td><td>62</td><td>95</td></tr><tr><td>SG&amp;A</td><td>(1,652)</td><td>(2,151)</td><td>(2,372)</td><td>(2,835)</td><td>(4,451)</td><td>(5,237)</td><td>(6,586)</td><td>(7,757)</td></tr><tr><td>As % of sales</td><td>18.1%</td><td>21.2%</td><td>23.2%</td><td>20.0%</td><td>20.9%</td><td>20.0%</td><td>20.2%</td><td>20.3%</td></tr><tr><td>EBITDA</td><td>595</td><td>566</td><td>619</td><td>1,339</td><td>2,084</td><td>2,428</td><td>3,137</td><td>4,023</td></tr><tr><td>EBIT (operating profit)</td><td>474</td><td>406</td><td>421</td><td>1,131</td><td>1,876</td><td>2,135</td><td>2,800</td><td>3,612</td></tr><tr><td>yoy %</td><td>123.2%</td><td>-14.3%</td><td>3.8%</td><td>168.5%</td><td>65.8%</td><td>13.8%</td><td>31.2%</td><td>29.0%</td></tr><tr><td>EBIT margin</td><td>5.2%</td><td>4.0%</td><td>4.1%</td><td>8.0%</td><td>8.8%</td><td>8.2%</td><td>8.6%</td><td>9.4%</td></tr><tr><td>Net income to shareholders</td><td>411</td><td>451</td><td>598</td><td>1,084</td><td>1,758</td><td>1,726</td><td>2,533</td><td>3,212</td></tr><tr><td>yoy %</td><td>458.8%</td><td>9.7%</td><td>32.7%</td><td>81.3%</td><td>62.2%</td><td>-1.8%</td><td>46.8%</td><td>26.8%</td></tr><tr><td>EPS - basic</td><td>5.83</td><td>6.34</td><td>8.37</td><td>15.32</td><td>24.72</td><td>23.96</td><td>35.16</td><td>44.59</td></tr><tr><td>EPS - fully diluted (analyst)</td><td>5.36</td><td>5.72</td><td>7.54</td><td>13.66</td><td>23.18</td><td>23.96</td><td>35.16</td><td>44.59</td></tr><tr><td>Dividend payout ratio</td><td>0%</td><td>0%</td><td>34%</td><td>75%</td><td>68%</td><td>68%</td><td>68%</td><td>68%</td></tr><tr><td>Segmental information</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Electric two wheeled vehicle</td><td>1,334</td><td>2,663</td><td>4,232</td><td>7,211</td><td>11,859</td><td>14,222</td><td>18,303</td><td>21,020</td></tr><tr><td>Electric self-balancing &amp; kick-scooter</td><td>6,405</td><td>5,537</td><td>3,488</td><td>3,381</td><td>4,329</td><td>5,065</td><td>5,571</td><td>6,128</td></tr><tr><td>Robot</td><td>21</td><td>121</td><td>252</td><td>895</td><td>2,002</td><td>3,303</td><td>4,393</td><td>5,711</td></tr><tr><td>Off-road vehicle</td><td>560</td><td>587</td><td>698</td><td>976</td><td>1,138</td><td>1,366</td><td>1,502</td><td>1,653</td></tr><tr><td>Others</td><td>825</td><td>1,217</td><td>1,552</td><td>1,733</td><td>1,950</td><td>2,212</td><td>2,843</td><td>3,745</td></tr><tr><td>Group revenue</td><td>9,146</td><td>10,124</td><td>10,222</td><td>14,196</td><td>21,278</td><td>26,167</td><td>32,613</td><td>38,257</td></tr><tr><td>% yoy</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Electric two wheeled vehicle</td><td>208.8%</td><td>99.6%</td><td>58.9%</td><td>70.4%</td><td>64.5%</td><td>19.9%</td><td>28.7%</td><td>14.8%</td></tr><tr><td>Electric self-balancing &amp; kick-scooter</td><td>21.7%</td><td>-13.6%</td><td>-37.0%</td><td>-3.1%</td><td>28.1%</td><td>17.0%</td><td>10.0%</td><td>10.0%</td></tr><tr><td>Robot</td><td>174.7%</td><td>466.7%</td><td>109.1%</td><td>254.8%</td><td>123.6%</td><td>65.0%</td><td>33.0%</td><td>30.0%</td></tr><tr><td>Off-road vehicle</td><td></td><td>4.8%</td><td>19.0%</td><td>39.8%</td><td>16.6%</td><td>20.0%</td><td>10.0%</td><td>10.0%</td></tr><tr><td>Others</td><td>174.5%</td><td>47.5%</td><td>27.5%</td><td>11.7%</td><td>12.5%</td><td>13.4%</td><td>28.6%</td><td>31.7%</td></tr><tr><td>Group revenue</td><td>52.4%</td><td>10.7%</td><td>1.0%</td><td>38.9%</td><td>49.9%</td><td>23.0%</td><td>24.6%</td><td>17.3%</td></tr><tr><td>Revenue mix</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Electric two wheeled vehicle</td><td>14.6%</td><td>26.3%</td><td>41.4%</td><td>50.8%</td><td>55.7%</td><td>54.4%</td><td>56.1%</td><td>54.9%</td></tr><tr><td>Electric self-balancing &amp; kick-scooter</td><td>70.0%</td><td>54.7%</td><td>34.1%</td><td>23.8%</td><td>20.3%</td><td>19.4%</td><td>17.1%</td><td>16.0%</td></tr><tr><td>Robot</td><td>0.2%</td><td>1.2%</td><td>2.5%</td><td>6.3%</td><td>9.4%</td><td>12.6%</td><td>13.5%</td><td>14.9%</td></tr><tr><td>Off-road vehicle</td><td>6.1%</td><td>5.8%</td><td>6.8%</td><td>6.9%</td><td>5.3%</td><td>5.2%</td><td>4.6%</td><td>4.3%</td></tr><tr><td>Others</td><td>9.0%</td><td>12.0%</td><td>15.2%</td><td>12.2%</td><td>9.2%</td><td>8.5%</td><td>8.7%</td><td>9.8%</td></tr><tr><td>Group revenue</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>GPM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Electric two wheeled vehicle</td><td>11.2%</td><td>16.2%</td><td>19.3%</td><td>21.1%</td><td>23.8%</td><td>20.9%</td><td>21.9%</td><td>22.2%</td></tr><tr><td>Electric self-balancing &amp; kick-scooter</td><td>25.1%</td><td>29.4%</td><td>29.4%</td><td>33.3%</td><td>27.7%</td><td>26.7%</td><td>26.7%</td><td>26.7%</td></tr><tr><td>Robot</td><td>36.2%</td><td>49.1%</td><td>53.1%</td><td>51.1%</td><td>52.3%</td><td>48.3%</td><td>47.3%</td><td>48.1%</td></tr><tr><td>Off-road vehicle</td><td></td><td></td><td>24.6%</td><td>22.1%</td><td>21.2%</td><td>21.2%</td><td>21.2%</td><td>21.2%</td></tr><tr><td>Others</td><td>-24.2%</td><td>-6.3%</td><td>38.7%</td><td>39.6%</td><td>51.2%</td><td>51.7%</td><td>51.9%</td><td>52.1%</td></tr><tr><td>Group gross margin</td><td>23.2%</td><td>26.0%</td><td>26.9%</td><td>28.2%</td><td>29.6%</td><td>28.1%</td><td>28.7%</td><td>29.7%</td></tr><tr><td>By geography</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Domestic</td><td>4,700</td><td>4,385</td><td>5,413</td><td>8,423</td><td>13,350</td><td>15,712</td><td>19,794</td><td>22,510</td></tr><tr><td>Overseas</td><td>4,446</td><td>5,739</td><td>4,809</td><td>5,772</td><td>7,928</td><td>10,455</td><td>12,819</td><td>15,746</td></tr><tr><td>Group revenue</td><td>9,146</td><td>10,124</td><td>10,222</td><td>14,196</td><td>21,278</td><td>26,167</td><td>32,613</td><td>38,257</td></tr><tr><td>Geographic growth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Domestic</td><td>35.2%</td><td>-6.7%</td><td>23.4%</td><td>55.6%</td><td>58.5%</td><td>17.7%</td><td>26.0%</td><td>13.7%</td></tr><tr><td>Overseas</td><td>76.0%</td><td>29.1%</td><td>-16.2%</td><td>20.0%</td><td>37.3%</td><td>31.9%</td><td>22.6%</td><td>22.8%</td></tr><tr><td>Group revenue</td><td>52.4%</td><td>10.7%</td><td>1.0%</td><td>38.9%</td><td>49.9%</td><td>23.0%</td><td>24.6%</td><td>17.3%</td></tr><tr><td>GPM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Domestic</td><td>18.8%</td><td>19.5%</td><td>21.8%</td><td>23.1%</td><td>25.8%</td><td>22.9%</td><td>23.9%</td><td>24.2%</td></tr><tr><td>Overseas</td><td>27.9%</td><td>30.9%</td><td>32.7%</td><td>35.8%</td><td>36.0%</td><td>35.8%</td><td>36.1%</td><td>37.4%</td></tr><tr><td>Group gross margin</td><td>23.2%</td><td>26.0%</td><td>26.9%</td><td>28.2%</td><td>29.6%</td><td>28.1%</td><td>28.7%</td><td>29.7%</td></tr><tr><td>% of sales</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SG&amp;A</td><td>18.1%</td><td>21.2%</td><td>23.2%</td><td>20.0%</td><td>20.9%</td><td>20.0%</td><td>20.2%</td><td>20.3%</td></tr><tr><td>Sales expense</td><td>6.5%</td><td>9.1%</td><td>10.0%</td><td>7.8%</td><td>8.8%</td><td>8.3%</td><td>8.4%</td><td>8.6%</td></tr><tr><td>.. A&amp;P</td><td>1.3%</td><td>3.2%</td><td>3.0%</td><td>2.9%</td><td>3.2%</td><td>3.0%</td><td>3.1%</td><td>3.3%</td></tr><tr><td>.. Payroll</td><td>1.9%</td><td>1.8%</td><td>2.6%</td><td>2.3%</td><td>3.0%</td><td>2.8%</td><td>2.8%</td><td>2.8%</td></tr><tr><td>.. Other sales expense</td><td>3.3%</td><td>4.1%</td><td>4.5%</td><td>2.5%</td><td>2.6%</td><td>2.4%</td><td>2.5%</td><td>2.5%</td></tr><tr><td>Admin. expense</td><td>11.2%</td><td>11.7%</td><td>12.6%</td><td>11.7%</td><td>11.5%</td><td>11.1%</td><td>11.1%</td><td>11.1%</td></tr><tr><td>.. R&amp;D expense</td><td>5.5%</td><td>5.8%</td><td>6.0%</td><td>5.8%</td><td>5.9%</td><td>5.9%</td><td>5.9%</td><td>5.9%</td></tr><tr><td>.. Other admin. expense</td><td>5.7%</td><td>5.9%</td><td>6.6%</td><td>5.9%</td><td>5.6%</td><td>5.3%</td><td>5.3%</td><td>5.2%</td></tr></table>

Source: Company data, GS Global Investment Research

## Investment Thesis, Valuation and Risks

Investment thesis: We expect Ninebot to grow as an emerging global leader in micro-mobility and robotic lawn mowers, driven by: 1) Further market share gain in core domestic E2W with rising membership fee contribution supported by its product R&D strength as smart functions play a more important role in products, together with channel expansion and wider product offerings via its dual-brand; 2) Rapidly growing robotic lawn mower business riding on the structural growth of robotic adoption vs. traditional. We view Ninebot as better positioned to gain share leveraging its comprehensive product portfolio, established brand, and stronger presence in the offline channel; 3) Overseas expansion potential: We see near-term revenue a

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
