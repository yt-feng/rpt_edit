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
# WEEKLY FUND FLOWS

# Energy Flows Come and Go

## Global fund flows, week ending July 1

■ Flows into mutual funds and related investment products remained negative for equities and positive for fixed income.

Lexi Kanter  
+1(212)855-9701 | alexandra.kanter@gs.com GS & Co. LLC

\- Net flows into global equity funds remained negative in the week ending July 1 (-\$14bn vs -\$5bn in the previous week). Within DM, US funds drove the net outflows. Within EM, Mainland China and global EM benchmark funds drove the net outflows while Taiwan and Korea equity funds saw net inflows. At the sector level, technology funds saw renewed inflows after seeing the largest net outflows the previous week. Meanwhile, energy funds saw net outflows as energy prices have continued to grind lower (see Chart of the Week). We recently noted that despite this reversal lower in energy prices, the terms of trade (ToT) imprint on FX has so far proved more durable. We think this stickier ToT imprint reflects divergent macro impacts which flow through economic data and firm-level performance over time, and we remain wary of the parallel to the 2022 energy shock where ToT FX differentiation peaked several months after energy prices did.

\- Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have seen sustained inflows and flows into long-duration bond funds turned positive. In EM, hard-currency and local currency bond funds saw net inflows. Money market fund assets increased by -\$55bn.

Cross-border FX flows were largely positive across the G10 but negative elsewhere. USD and EUR saw the strongest net demand. Asia broadly saw net outflows; CNY saw renewed outflows after seeing inflows the previous week.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>1-Jul</td><td>4wk avg</td><td>1-Jul</td></tr><tr><td>Equity</td><td>139,067</td><td>-13,859</td><td>0.11</td><td>-0.04</td></tr><tr><td>Fixed Income</td><td>84,835</td><td>29,236</td><td>0.21</td><td>0.29</td></tr><tr><td>of which: EM</td><td>4,009</td><td>838</td><td>0.14</td><td>0.12</td></tr><tr><td>Money Markets</td><td>52,099</td><td>54,999</td><td>0.12</td><td>0.49</td></tr><tr><td>FX Flows*</td><td>60,550</td><td>3,811</td><td>0.09</td><td>0.02</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds

![](images/ca9912c6121530dc86ee6c9ff382e588895e5dc78002dc77e04228c9223650c5.jpg)  
Source: EPFR, Haver Analytics, GS Global Investment Research

## Global Fund Flow Trends

![](images/496edd8dc7cf5ab05f5dc52ff903015fedf29e4d701b75b2af8c6ff2938b4131.jpg)  
Source: EPFR, GS Global Investment Research

![](images/85e500b1f3a277a7ecb88975a45e1e5b4695e538ad8279688b1f70e0976210eb.jpg)  
Source: EPFR, GS Global Investment Research

![](images/99c28a0a97124998a39365aee4dbd1b223343dea6f840809cc827faa34b55292.jpg)  
Source: EPFR, GS Global Investment Research

![](images/ab8e31eef6302ac764b7867505e147cd49da513e0cb2eb833c93521c727b9120.jpg)  
Captures flows to sector-dedicated funds

![](images/f938f5258a96ccd5e232493954a7d2b7fdbc5a75c8513d776083c39de471e279.jpg)  
Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/0e95c07ada5e6102f9c59252dc4d5290ef29b7eadd38c382cc56b4d3314e5fa6.jpg)  
Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

Source: EPFR, GS Global Investment Research  
![](images/3c57dadcfb938e03c1542180f9a1ba0dd74fdcbea207c19ae3739ed060a15f3a.jpg)  
Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

![](images/6b15da3c9e5a9e111a4e436ee9e1bbf033271227207b3d43d9b9f0fea1dd52cb.jpg)  
Source: EPFR, GS Global Investment Research

![](images/681ee7c9932f69a75b8915d63bf1387bc6473dcea89ff45c340d8fc173d603f2.jpg)  
Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country  
![](images/d70b963579e790065d18d83fbc91c199bf0bb7d0ad54365bf5a8232de325d6bc.jpg)

![](images/ea769f4b8d87572b5690c09a50afb439629d91bbcf13510d8ecc3ec0af1b6170.jpg)

![](images/2e2c952b66813578931dabebf5abe6e3711ecb5b22a953908756a3914def798a.jpg)

![](images/5883dd395103a3affd1fa69ba2481ac2c310bda39f4b26a3ce3cfba8932c70d9.jpg)  
Source: EPFR, GS Global Investment Research

![](images/2cb81206dc731f05eccbe3a69660b891bbb0d0f8224af336dac461bab69ad1e7.jpg)

![](images/72517eba809ab603d1f815b578ea3cb91f4de8356552ba97e072c8d04c330bcc.jpg)

Net Unhedged Flows into US Equity Funds

![](images/c82467a2126b56c27c023554038d30026531845b7d218ec4d1ff24c7e22444e6.jpg)  
Source: EPFR, Haver Analytics, GS Global Investment Research

Fixed Income & Equity Flows

<table><tr><td rowspan="3"></td><td colspan="8">Global Fund Flows</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>1-Jul</td><td>24-Jun</td><td>17-Jun</td><td>10-Jun</td><td>4wk avg</td><td>1-Jul</td></tr><tr><td>Total Equity</td><td>139,067</td><td>-13,859</td><td>-4,992</td><td>126,425</td><td>31,494</td><td>0.11</td><td>-0.04</td><td>2.12</td></tr><tr><td>Global Benchmarks1</td><td>50,255</td><td>8,921</td><td>14,361</td><td>15,116</td><td>11,857</td><td>0.17</td><td>0.12</td><td>2.00</td></tr><tr><td>Including US</td><td>35,165</td><td>5,584</td><td>9,300</td><td>8,317</td><td>11,963</td><td>0.17</td><td>0.10</td><td>2.09</td></tr><tr><td>Excluding US</td><td>15,090</td><td>3,337</td><td>5,061</td><td>6,799</td><td>-107</td><td>0.16</td><td>0.14</td><td>1.17</td></tr><tr><td>Developed Markets2</td><td>108,886</td><td>-18,751</td><td>-8,294</td><td>120,798</td><td>15,132</td><td>0.14</td><td>-0.09</td><td>2.29</td></tr><tr><td>US</td><td>110,784</td><td>-17,207</td><td>-8,548</td><td>119,189</td><td>17,350</td><td>0.17</td><td>-0.10</td><td>2.28</td></tr><tr><td>Western Europe</td><td>-10,075</td><td>-3,704</td><td>-1,294</td><td>-1,173</td><td>-3,904</td><td>-0.12</td><td>-0.18</td><td>-1.26</td></tr><tr><td>UK-dedicated</td><td>-734</td><td>-81</td><td>-676</td><td>185</td><td>-163</td><td>-0.06</td><td>-0.02</td><td>1.21</td></tr><tr><td>Other</td><td>-9,341</td><td>-3,623</td><td>-618</td><td>-1,359</td><td>-3,740</td><td>-0.13</td><td>-0.21</td><td>-1.39</td></tr><tr><td>Japan</td><td>4,280</td><td>1,855</td><td>475</td><td>1,166</td><td>784</td><td>0.09</td><td>0.15</td><td>0.68</td></tr><tr><td>Other</td><td>3,897</td><td>306</td><td>1,073</td><td>1,616</td><td>901</td><td>0.23</td><td>0.07</td><td>1.15</td></tr><tr><td>Emerging Markets3</td><td>-20,073</td><td>-4,030</td><td>-11,059</td><td>-9,489</td><td>4,506</td><td>-0.16</td><td>-0.13</td><td>-1.12</td></tr><tr><td>Global EM Benchmarks</td><td>-5,956</td><td>-2,013</td><td>-508</td><td>-570</td><td>-2,865</td><td>-0.11</td><td>-0.14</td><td>-1.03</td></tr><tr><td>Mainland China</td><td>-27,283</td><td>-5,729</td><td>-10,367</td><td>-9,051</td><td>-2,136</td><td>-1.04</td><td>-0.88</td><td>-1.12</td></tr><tr><td>Taiwan</td><td>9,768</td><td>2,426</td><td>1,077</td><td>1,031</td><td>5,234</td><td>1.03</td><td>0.97</td><td>2.95</td></tr><tr><td>Korea</td><td>9,825</td><td>4,545</td><td>-536</td><td>-76</td><td>5,892</td><td>1.22</td><td>2.12</td><td>2.46</td></tr><tr><td>India</td><td>-1,196</td><td>-250</td><td>-69</td><td>-416</td><td>-461</td><td>-0.37</td><td>-0.30</td><td>-1.07</td></tr><tr><td>Brazil</td><td>-608</td><td>-151</td><td>-196</td><td>-64</td><td>-198</td><td>-0.65</td><td>-0.65</td><td>-1.19</td></tr><tr><td>Other</td><td>-4,624</td><td>-2,859</td><td>-461</td><td>-344</td><td>-960</td><td>-0.30</td><td>-0.75</td><td>-1.92</td></tr><tr><td colspan="9">Equity Sector Flows</td></tr><tr><td>Commodities/Materials</td><td>-2,245</td><td>-1,843</td><td>-1,082</td><td>1,879</td><td>-1,198</td><td>-0.24</td><td>-0.72</td><td>-0.60</td></tr><tr><td>Consumer Goods</td><td>-2,335</td><td>412</td><td>74</td><td>-781</td><td>-2,039</td><td>-0.28</td><td>0.20</td><td>-0.45</td></tr><tr><td>Energy</td><td>-9,718</td><td>-5,602</td><td>-2,556</td><td>-526</td><td>-1,034</td><td>-0.78</td><td>-1.81</td><td>-2.10</td></tr><tr><td>Financials</td><td>6,819</td><td>4,008</td><td>-1,371</td><td>2,467</td><td>1,715</td><td>0.38</td><td>0.89</td><td>1.16</td></tr><tr><td>Health Care</td><td>4,835</td><td>2,502</td><td>687</td><td>536</td><td>1,109</td><td>0.31</td><td>0.62</td><td>1.90</td></tr><tr><td>Industrials</td><td>5,778</td><td>812</td><td>-2,487</td><td>6,288</td><td>1,165</td><td>0.51</td><td>0.28</td><td>0.78</td></tr><tr><td>Infrastructure</td><td>4,022</td><td>815</td><td>2,077</td><td>473</td><td>657</td><td>0.72</td><td>0.54</td><td>2.11</td></tr><tr><td>Real Estate</td><td>3,114</td><td>-230</td><td>2,110</td><td>1,529</td><td>-295</td><td>0.13</td><td>-0.04</td><td>1.98</td></tr><tr><td>Technology</td><td>49,214</td><td>15,937</td><td>-23,832</td><td>38,281</td><td>18,828</td><td>0.53</td><td>0.66</td><td>3.92</td></tr><tr><td>Telecom</td><td>3,797</td><td>3,163</td><td>-1,144</td><td>953</td><td>824</td><td>1.13</td><td>3.77</td><td>2.29</td></tr><tr><td>Utilities</td><td>54</td><td>550</td><td>346</td><td>-379</td><td>-463</td><td>0.01</td><td>0.30</td><td>-0.02</td></tr><tr><td>High Beta4</td><td>3,030</td><td>904</td><td>-3,400</td><td>5,216</td><td>310</td><td>0.10</td><td>0.13</td><td>0.00</td></tr><tr><td>Low Beta4</td><td>-703</td><td>38</td><td>907</td><td>132</td><td>-1,779</td><td>-0.03</td><td>0.01</td><td>0.49</td></tr><tr><td>Total Fixed Income</td><td>84,835</td><td>29,236</td><td>16,374</td><td>19,160</td><td>20,065</td><td>0.21</td><td>0.29</td><td>1.13</td></tr><tr><td>Developed Markets5</td><td>82,179</td><td>28,237</td><td>13,375</td><td>19,521</td><td>21,047</td><td>0.23</td><td>0.31</td><td>1.34</td></tr><tr><td>Government</td><td>11,221</td><td>4,736</td><td>-94</td><td>1,623</td><td>4,957</td><td>0.17</td><td>0.29</td><td>0.04</td></tr><tr><td>Mortgage-backed</td><td>2,560</td><td>293</td><td>477</td><td>609</td><td>1,180</td><td>0.21</td><td>0.10</td><td>0.34</td></tr><tr><td>Municipal</td><td>7,188</td><td>1,859</td><td>1,226</td><td>2,509</td><td>1,593</td><td>0.26</td><td>0.26</td><td>1.49</td></tr><tr><td>Agg-type</td><td>27,840</td><td>9,215</td><td>7,592</td><td>3,861</td><td>7,172</td><td>0.24</td><td>0.32</td><td>1.03</td></tr><tr><td>IG Credit</td><td>9,383</td><td>3,301</td><td>865</td><td>3,771</td><td>1,446</td><td>0.20</td><td>0.29</td><td>0.65</td></tr><tr><td>High yield</td><td>7,217</td><td>3,350</td><td>1,857</td><td>2,096</td><td>-86</td><td>0.26</td><td>0.48</td><td>0.80</td></tr><tr><td>Bank loan</td><td>3,309</td><td>806</td><td>486</td><td>1,020</td><td>998</td><td>0.46</td><td>0.44</td><td>0.58</td></tr><tr><td>Long-duration6</td><td>-569</td><td>1,124</td><td>-1,183</td><td>-1,046</td><td>537</td><td>-0.03</td><td>0.22</td><td>-1.14</td></tr><tr><td>Short-duration6</td><td>17,378</td><td>6,576</td><td>1,123</td><td>3,506</td><td>6,173</td><td>0.19</td><td>0.28</td><td>0.43</td></tr><tr><td>Inflation-protected</td><td>1,610</td><td>294</td><td>69</td><td>885</td><td>361</td><td>0.23</td><td>0.17</td><td>0.92</td></tr><tr><td>Emerging Markets</td><td>4,009</td><td>838</td><td>3,220</td><td>193</td><td>-242</td><td>0.14</td><td>0.12</td><td>0.40</td></tr><tr><td>Hard</td><td>446</td><td>162</td><td>578</td><td>267</td><td>-561</td><td>0.04</td><td>0.06</td><td>0.43</td></tr><tr><td>Blend</td><td>142</td><td>-81</td><td>142</td><td>52</td><td>28</td><td>0.05</td><td>-0.12</td><td>0.10</td></tr><tr><td>Local</td><td>3,421</td><td>757</td><td>2,500</td><td>-127</td><td>291</td><td>0.23</td><td>0.20</td><td>0.32</td></tr><tr><td>Money Markets</td><td>52,099</td><td>54,999</td><td>-25,536</td><td>25,110</td><td>-2,475</td><td>0.12</td><td>0.49</td><td>-0.39</td></tr></table>

1. Primarily MSCI World and MSCI ACWI benchmarks. 2. Sum of DM country- and region-dedicated funds; excludes global DM benchmark funds (e.g. MSCI World funds). 3. Sum of Global EM benchmark funds and EM country- and region-dedicated funds. 4. High beta funds include commodity, financial, & industrial sector funds. Low beta funds include consumer goods, real estate, & utility sector funds. 5. Benchmarks may include some investment grade EM bonds; categories below include DM & EM funds. 6. Long-duration includes long-term Agg-type, long-term corporate, and long-term government bond funds. Short-duration includes short-term Agg-type, short-term corporate, and short-term government bond funds.

<table><tr><td rowspan="3"></td><td colspan="8">FX Flows1</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>1-Jul</td><td>24-Jun</td><td>17-Jun</td><td>10-Jun</td><td>4wk avg</td><td>1-Jul</td></tr><tr><td>Total</td><td>60,550</td><td>3,811</td><td>20,805</td><td>22,519</td><td>13,416</td><td>0.09</td><td>0.02</td><td>0.66</td></tr><tr><td>G10</td><td>59,065</td><td>7,573</td><td>16,737</td><td>20,480</td><td>14,275</td><td>0.14</td><td>0.07</td><td>1.65</td></tr><tr><td>USD</td><td>36,654</td><td>4,825</td><td>9,611</td><td>11,092</td><td>11,126</td><td>0.15</td><td>0.08</td><td>1.35</td></tr><tr><td>EUR</td><td>7,140</td><td>1,215</td><td>2,342</td><td>2,852</td><td>731</td><td>0.13</td><td>0.09</td><td>1.08</td></tr><tr><td>GBP</td><td>4,180</td><td>850</td><td>939</td><td>1,801</td><td>590</td><td>0.10</td><td>0.08</td><td>0.56</td></tr><tr><td>AUD</td><td>521</td><td>-192</td><td>238</td><td>313</td><td>161</td><td>0.07</td><td>-0.10</td><td>0.37</td></tr><tr><td>NZD</td><td>49</td><td>6</td><td>23</td><td>13</td><td>8</td><td>0.10</td><td>0.05</td><td>0.45</td></tr><tr><td>CAD</td><td>2,321</td><td>112</td><td>721</td><td>931</td><td>557</td><td>0.17</td><td>0.03</td><td>1.56</td></tr><tr><td>CHF</td><td>1,248</td><td>22</td><td>495</td><td>610</td><td>120</td><td>0.07</td><td>0.01</td><td>0.30</td></tr><tr><td>NOK</td><td>122</td><td>66</td><td>117</td><td>45</td><td>-106</td><td>0.03</td><td>0.07</td><td>-0.47</td></tr><tr><td>SEK</td><td>776</td><td>166</td><td>252</td><td>257</td><td>102</td><td>0.08</td><td>0.07</td><td>0.48</td></tr><tr><td>JPY</td><td>6,054</td><td>503</td><td>1,998</td><td>2,568</td><td>986</td><td>0.16</td><td>0.05</td><td>1.53</td></tr><tr><td>Asia</td><td>-911</td><td>-3,453</td><td>2,807</td><td>-295</td><td>31</td><td>-0.01</td><td>-0.14</td><td>-0.29</td></tr><tr><td>CNY</td><td>-2,617</td><td>-1,727</td><td>1,556</td><td>-1,761</td><td>-685</td><td>-0.09</td><td>-0.24</td><td>-0.51</td></tr><tr><td>HKD</td><td>376</td><td>-15</td><td>145</td><td>179</td><td>68</td><td>0.08</td><td>-0.01</td><td>0.70</td></tr><tr><td>INR</td><td>-1,843</td><td>-571</td><td>-51</td><td>-454</td><td>-766</td><td>-0.17</td><td>-0.21</td><td>-1.43</td></tr><tr><td>KRW</td><td>3,733</td><td>-257</td><td>804</td><td>1,305</td><td>1,881</td><td>0.19</td><td>-0.05</td><td>1.44</td></tr><tr><td>MYR</td><td>-95</td><td>-57</td><td>11</td><td>1</td><td>-51</td><td>-0.07</td><td>-0.17</td><td>-0.65</td></tr><tr><td>SGD</td><td>374</td><td>20</td><td>127</td><td>156</td><td>71</td><td>0.10</td><td>0.02</td><td>1.31</td></tr><tr><td>TWD</td><td>-1,016</td><td>-794</td><td>133</td><td>180</td><td>-535</td><td>-0.04</td><td>-0.14</td><td>-0.83</td></tr><tr><td>THB</td><td>-22</td><td>-58</td><td>6</td><td>30</td><td>1</td><td>-0.01</td><td>-0.14</td><td>-0.22</td></tr><tr><td>IDR</td><td>201</td><td>18</td><td>67</td><td>58</td><td>60</td><td>0.11</td><td>0.04</td><td>0.52</td></tr><tr><td>PHP</td><td>-4</td><td>-11</td><td>9</td><td>11</td><td>-13</td><td>0.00</td><td>-0.06</td><td>-0.11</td></tr><tr><td>Americas</td><td>-1,248</td><td>-569</td><td>241</td><td>29</td><td>-950</td><td>-0.08</td><td>-0.15</td><td>-0.91</td></tr><tr><td>ARS</td><td>21</td><td>-11</td><td>33</td><td>3</td><td>-4</td><td>0.06</td><td>-0.12</td><td>-0.20</td></tr><tr><td>BRL</td><td>-1,020</td><td>-426</td><td>115</td><td>-8</td><td>-702</td><td>-0.12</td><td>-0.21</td><td>-1.09</td></tr><tr><td>MXN</td><td>-246</td><td>-80</td><td>27</td><td>-17</td><td>-177</td><td>-0.06</td><td>-0.08</td><td>-0.82</td></tr><tr><td>CLP</td><td>-9</td><td>-17</td><td>32</td><td>15</td><td>-40</td><td>-0.01</td><td>-0.05</td><td>-0.41</td></tr><tr><td>PEN</td><td>-39</td><td>-23</td><td>9</td><td>4</td><td>-28</td><td>-0.04</td><td>-0.10</td><td>-0.54</td></tr><tr><td>COP</td><td>45</td><td>-12</td><td>25</td><td>32</td><td>0</td><td>0.05</td><td>-0.06</td><td>-0.09</td></tr><tr><td>EMEA</td><td>489</td><td>-108</td><td>205</td><td>420</td><td>-29</td><td>0.05</td><td>-0.04</td><td>-0.06</td></tr><tr><td>CZK</td><td>195</td><td>6</td><td>14</td><td>166</td><td>10</td><td>0.23</td><td>0.03</td><td>1.64</td></tr><tr><td>HUF</td><td>14</td><td>-8</td><td>14</td><td>18</td><td>-9</td><td>0.01</td><td>-0.03</td><td>-0.21</td></tr><tr><td>PLN</td><td>131</td><td>-34</td><td>50</td><td>61</td><td>54</td><td>0.07</td><td>-0.07</td><td>0.02</td></tr><tr><td>RON</td><td>28</td><td>1</td><td>7</td><td>17</td><td>3</td><td>0.04</td><td>0.01</td><td>-0.09</td></tr><tr><td>RUB</td><td>4</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0.10</td><td>0.07</td><td>0.49</td></tr><tr><td>TRY</td><td>-8</td><td>-5</td><td>24</td><td>14</td><td>-41</td><td>-0.01</td><td>-0.02</td><td>-0.32</td></tr><tr><td>ILS</td><td>266</td><td>40</td><td>71</td><td>97</td><td>59</td><td>0.14</td><td>0.08</td><td>0.89</td></tr><tr><td>ZAR</td><td>-141</td><td>-107</td><td>24</td><td>46</td><td>-104</td><td>-0.05</td><td>-0.15</td><td>-0.60</td></tr><tr><td>Frontier</td><td>-123</td><td>-52</td><td>12</td><td>-18</td><td>-65</td><td>-0.06</td><td>-0.11</td><td>-0.62</td></tr><tr><td>UAH</td><td>1</td><td>-1</td><td>1</td><td>1</td><td>-1</td><td>0.02</td><td>-0.04</td><td>-0.13</td></tr><tr><td>EGP</td><td>2</td><td>-4</td><td>6</td><td>2</td><td>-2</td><td>0.01</td><td>-0.04</td><td>-0.27</td></tr><tr><td>NGN</td><td>-3</td><td>-4</td><td>3</td><td>2</td><td>-4</td><td>-0.01</td><td>-0.06</td><td>-0.26</td></tr><tr><td>KWD</td><td>-3</td><td>-1</td><td>0</td><td>1</td><td>-4</td><td>-0.03</td><td>-0.03</td><td>-0.36</td></tr><tr><td>SAR</td><td>-120</td><td>-43</td><td>2</td><td>-24</td><td>-55</td><td>-0.09</td><td>-0.14</td><td>-0.78</td></tr></table>

Note: AUM is calculated at the domicile level.  
1. FX flows are measured as cross-border equity and fixed income fund flows (based on th

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
