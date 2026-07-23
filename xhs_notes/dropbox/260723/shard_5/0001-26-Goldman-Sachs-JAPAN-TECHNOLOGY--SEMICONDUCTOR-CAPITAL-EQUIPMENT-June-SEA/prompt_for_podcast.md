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
# JAPAN TECHNOLOGY: SEMICONDUCTOR CAPITAL EQUIPMENT

# June SEAJ data: Front-end equipment leads strong demand; we revise GSe; Buy on Lasertec/Ebara/Disco/Tokyo Electron

## Strong start to FY in April-June

According to June 2026 data released after the July 21 close by the Semiconductor Equipment Association of Japan (SEAJ), monthly sales of Japanese semiconductor production equipment in April-June averaged ¥513.6 bn (+27% yoy, +7.0% qoq). SEAJ updated its demand forecast for Japanese semiconductor production equipment on July 2, forecasting FY3/27 sales of ¥6.55 tn (+26% yoy) and FY3/28 sales of ¥7.40 tn (+13% yoy).

## Front-end equipment demand particularly strong

Per SEAJ, whereas back-end equipment demand (centered on inspection equipment) was strong until FY3/26, front-end equipment demand is driving growth thus far in FY3/27, with strong demand across a broad range of applications, including HBM and leading-edge logic as well as commodity DRAM and SSD (NAND). The SEAJ noted that the demand outlook is currently being revised upward almost every month, suggesting that customer requests for accelerated delivery of ordered equipment are continuing.

## Retain Buy ratings on Lasertec/Ebara/Disco/Tokyo Electron

With the market environment remaining strong overall, we see substantial upside to the share prices of companies whose earnings growth outpaces market consensus forecasts, and we maintain our Buy ratings on Lasertec (on CL), Ebara, Disco, and Tokyo Electron. We also revise our earnings estimates for five companies following an update to our USD/JPY assumption, from ¥155 to ¥160.

Shuhei Nakamura
+81(3)4587-9932 |
shuhei.nakamura@gs.com
GS Japan Co., Ltd.

Kaho Otake
+81(3)4587-7498 | kaho.otake@gs.com
GS Japan Co., Ltd.

Exhibit 1: Japan SPE sales (3-MMA)  
![](images/022846138b9a7dc9e0db449ac4b4b163c125a6626d9d0ce61986b79ae662e397.jpg)  
Source: SEAJ

Exhibit 2: Ratings and 12m target prices for our SPE coverage

<table><tr><td rowspan="2">Company Name</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="2">Price target (¥)</td><td rowspan="2">Current price (¥)</td><td rowspan="2">Up/downside</td></tr><tr><td>New</td><td>Old</td></tr><tr><td>Lasertec</td><td>6920.T</td><td>Buy*</td><td>70,000</td><td>67,000</td><td>42,990</td><td>+63%</td></tr><tr><td>Disco</td><td>6146.T</td><td>Buy</td><td>100,000</td><td>100,000</td><td>68,590</td><td>+46%</td></tr><tr><td>Ebara</td><td>6361.T</td><td>Buy</td><td>7,900</td><td>7,800</td><td>5,593</td><td>+41%</td></tr><tr><td>Tokyo Electron</td><td>8035.T</td><td>Buy</td><td>83,000</td><td>83,000</td><td>65,960</td><td>+26%</td></tr><tr><td>Advantest</td><td>6857.T</td><td>Neutral</td><td>35,000</td><td>34,000</td><td>29,585</td><td>+18%</td></tr><tr><td>Kokusai Electric</td><td>6525.T</td><td>Neutral</td><td>9,500</td><td>9,500</td><td>8,741</td><td>+9%</td></tr><tr><td>Ulvac</td><td>6728.T</td><td>Neutral</td><td>10,300</td><td>10,300</td><td>9,800</td><td>+5%</td></tr><tr><td>JEOL</td><td>6951.T</td><td>Neutral</td><td>8,300</td><td>7,700</td><td>8,351</td><td>-1%</td></tr><tr><td>Tokyo Seimitsu</td><td>7729.T</td><td>Sell</td><td>15,000</td><td>15,000</td><td>18,255</td><td>-18%</td></tr><tr><td>SCREEN HD</td><td>7735.T</td><td>Sell</td><td>12,500</td><td>12,500</td><td>16,500</td><td>-24%</td></tr></table>

\*APAC Conviction List

Source: GS Global Investment Research, LSEG Data & Analytics

Exhibit 3: Reflecting changes in forex assumptions Our old vs. new estimates and comparison with consensus

<table><tr><td colspan="2">Sales</td><td colspan="6">FY1</td><td colspan="5">FY2</td><td colspan="5">FY3</td></tr><tr><td>(JPY mn)</td><td>FY-end</td><td>(CoE)</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td></tr><tr><td>Ebara</td><td>12</td><td>1,020,000</td><td>1,043,100</td><td>1,043,100</td><td>0.0%</td><td>1,048,221</td><td>-0%</td><td>1,193,200</td><td>1,193,200</td><td>0.0%</td><td>1,147,195</td><td>+4%</td><td>1,330,800</td><td>1,330,800</td><td>0.0%</td><td>1,228,000</td><td>+8%</td></tr><tr><td>Advantest</td><td>3</td><td>1,420,000</td><td>1,555,100</td><td>1,555,100</td><td>0.0%</td><td>1,488,000</td><td>+5%</td><td>1,887,000</td><td>1,887,000</td><td>0.0%</td><td>1,850,000</td><td>+2%</td><td>2,028,800</td><td>2,028,800</td><td>0.0%</td><td>2,055,881</td><td>-1%</td></tr><tr><td>Lasertec</td><td>6</td><td>220,000</td><td>229,300</td><td>229,300</td><td>0.0%</td><td>228,500</td><td>+0%</td><td>288,400</td><td>285,700</td><td>+0.9%</td><td>285,000</td><td>+1%</td><td>410,100</td><td>400,800</td><td>+2.3%</td><td>349,400</td><td>+17%</td></tr><tr><td>JEOL</td><td>3</td><td>164,000</td><td>167,600</td><td>165,900</td><td>+1.0%</td><td>170,800</td><td>-2%</td><td>185,100</td><td>183,600</td><td>+0.8%</td><td>185,908</td><td>-0%</td><td>199,300</td><td>197,600</td><td>+0.9%</td><td>207,800</td><td>-4%</td></tr><tr><td>SCREEN Holdings</td><td>3</td><td>725,000</td><td>740,400</td><td>740,400</td><td>0.0%</td><td>739,850</td><td>+0%</td><td>853,200</td><td>853,200</td><td>0.0%</td><td>848,448</td><td>+1%</td><td>931,800</td><td>931,800</td><td>0.0%</td><td>931,800</td><td>0%</td></tr></table>

<table><tr><td colspan="2">Operating profit</td><td colspan="6">FY1</td><td colspan="5">FY2</td><td colspan="5">FY3</td></tr><tr><td>(JPY mn)</td><td>FY-end</td><td>(CoE)</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td></tr><tr><td>Ebara</td><td>12</td><td>125,000</td><td>138,700</td><td>137,600</td><td>+0.8%</td><td>134,650</td><td>+3%</td><td>189,500</td><td>188,000</td><td>+0.8%</td><td>161,400</td><td>+17%</td><td>234,400</td><td>232,900</td><td>+0.6%</td><td>190,738</td><td>+23%</td></tr><tr><td>Advantest</td><td>3</td><td>627,500</td><td>751,400</td><td>734,200</td><td>+2.3%</td><td>690,000</td><td>+9%</td><td>943,500</td><td>919,200</td><td>+2.6%</td><td>873,640</td><td>+8%</td><td>985,200</td><td>960,900</td><td>+2.5%</td><td>984,900</td><td>+0%</td></tr><tr><td>Lasertec</td><td>6</td><td>100,000</td><td>107,800</td><td>107,800</td><td>0.0%</td><td>105,900</td><td>+2%</td><td>140,800</td><td>139,300</td><td>+1.1%</td><td>136,000</td><td>+4%</td><td>212,200</td><td>206,700</td><td>+2.7%</td><td>170,000</td><td>+25%</td></tr><tr><td>JEOL</td><td>3</td><td>26,500</td><td>28,700</td><td>27,900</td><td>+2.9%</td><td>28,200</td><td>+2%</td><td>34,800</td><td>34,100</td><td>+2.1%</td><td>35,083</td><td>-1%</td><td>37,700</td><td>36,900</td><td>+2.2%</td><td>39,117</td><td>-4%</td></tr><tr><td>SCREEN Holdings</td><td>3</td><td>150,000</td><td>155,900</td><td>155,200</td><td>+0.5%</td><td>160,900</td><td>-3%</td><td>184,000</td><td>183,300</td><td>+0.4%</td><td>193,477</td><td>-5%</td><td>202,700</td><td>202,000</td><td>+0.3%</td><td>231,997</td><td>-13%</td></tr></table>

<table><tr><td colspan="2">Net profit</td><td colspan="6">FY1</td><td colspan="5">FY2</td><td colspan="5">FY3</td></tr><tr><td>(JPY mn)</td><td>FY-end</td><td>(CoE)</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td></tr><tr><td>Ebara</td><td>12</td><td>99,500</td><td>112,800</td><td>112,000</td><td>+0.7%</td><td>104,700</td><td>+8%</td><td>135,500</td><td>134,400</td><td>+0.8%</td><td>111,150</td><td>+22%</td><td>168,500</td><td>167,300</td><td>+0.7%</td><td>133,699</td><td>+26%</td></tr><tr><td>Advantest</td><td>3</td><td>465,500</td><td>542,700</td><td>530,300</td><td>+2.3%</td><td>512,000</td><td>+6%</td><td>681,300</td><td>663,800</td><td>+2.6%</td><td>647,450</td><td>+5%</td><td>711,700</td><td>694,200</td><td>+2.5%</td><td>737,367</td><td>-3%</td></tr><tr><td>Lasertec</td><td>6</td><td>72,000</td><td>79,300</td><td>79,300</td><td>0.0%</td><td>76,300</td><td>+4%</td><td>100,200</td><td>99,100</td><td>+1.1%</td><td>95,540</td><td>+5%</td><td>150,900</td><td>147,000</td><td>+2.7%</td><td>120,750</td><td>+25%</td></tr><tr><td>JEOL</td><td>3</td><td>21,300</td><td>21,700</td><td>21,100</td><td>+2.8%</td><td>21,525</td><td>+1%</td><td>26,100</td><td>25,600</td><td>+2.0%</td><td>26,100</td><td>0%</td><td>28,200</td><td>27,600</td><td>+2.2%</td><td>28,900</td><td>-2%</td></tr><tr><td>SCREEN Holdings</td><td>3</td><td>88,000</td><td>114,200</td><td>113,700</td><td>+0.4%</td><td>117,118</td><td>-2%</td><td>132,600</td><td>132,100</td><td>+0.4%</td><td>144,013</td><td>-8%</td><td>146,000</td><td>145,500</td><td>+0.3%</td><td>163,400</td><td>-11%</td></tr></table>

<table><tr><td colspan="2">EPS</td><td colspan="6">FY1</td><td colspan="5">FY2</td><td colspan="5">FY3</td></tr><tr><td>(JPY)</td><td>FY-end</td><td>(CoE)</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td><td>GSE New</td><td>GSE Old</td><td>New vs. Old</td><td>BBG</td><td>vs. BBG</td></tr><tr><td>Ebara</td><td>12</td><td>217.9</td><td>248.1</td><td>246.4</td><td>+0.7%</td><td>229.4</td><td>+8%</td><td>302.1</td><td>299.6</td><td>+0.8%</td><td>247.2</td><td>+22%</td><td>384.2</td><td>381.5</td><td>+0.7%</td><td>301.5</td><td>+27%</td></tr><tr><td>Advantest</td><td>3</td><td>641.6</td><td>757.9</td><td>740.4</td><td>+2.4%</td><td>705.7</td><td>+7%</td><td>967.6</td><td>942.1</td><td>+2.7%</td><td>892.9</td><td>+8%</td><td>1,010.8</td><td>985.2</td><td>+2.6%</td><td>1,057.7</td><td>-4%</td></tr><tr><td>Lasertec</td><td>6</td><td>801.9</td><td>884.7</td><td>884.7</td><td>0.0%</td><td>849.3</td><td>+4%</td><td>1,117.9</td><td>1,105.6</td><td>+1.1%</td><td>1,065.9</td><td>+5%</td><td>1,683.6</td><td>1,640.1</td><td>+2.7%</td><td>1,343.0</td><td>+25%</td></tr><tr><td>JEOL</td><td>3</td><td>432.6</td><td>445.6</td><td>433.3</td><td>+2.8%</td><td>432.3</td><td>+3%</td><td>535.9</td><td>525.7</td><td>+2.0%</td><td>511.7</td><td>+5%</td><td>579.0</td><td>566.7</td><td>+2.2%</td><td>566.6</td><td>+2%</td></tr><tr><td>SCREEN Holdings</td><td>3</td><td>581.7</td><td>604.0</td><td>601.3</td><td>+0.4%</td><td>628.3</td><td>-4%</td><td>701.3</td><td>698.6</td><td>+0.4%</td><td>769.5</td><td>-9%</td><td>772.1</td><td>769.5</td><td>+0.3%</td><td>866.6</td><td>-11%</td></tr></table>

Source: Bloomberg, GS Global Investment Research, Company data

Exhibit 4: Forex sensitivity for SPE coverage USD/JPY sensitivity : FY3/27E operating profit basis (%)  
![](images/ebfe8c0bc5913c641bd77b39af8f7db6ba34d5be5d04079a525aaa3a1db15b0b.jpg)  
Source: Company data, GS Global Investment Research

Exhibit 5: Target price risks and methodology for companies in our coverage

<table><tr><td>Company Name (rating)</td><td>Ticker</td><td>12-m TP (¥)</td><td>Methodology</td><td>Risks</td></tr><tr><td>DISCO (Buy)</td><td>6146.T</td><td>100,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 50%.</td><td>(-) slowdown or share loss in AI-related demand (-) slowdown in China demand or tightening of export controls (-) rapid yen appreciation against the USD</td></tr><tr><td>Ebara (Buy)</td><td>6361.T</td><td>7,900</td><td>Based on the correlation between P/B and our FY12/27E ROE estimates.</td><td>(-) Semiconductor capex enters a downcycle (-) Increasing competitiveness of Chinese CMP system makers (-) Slow adoption of new technology in semiconductor devices (-) Decline in crude oil/LNG prices, oil refining/petrochemical margins</td></tr><tr><td>Kokusai Electric (Neutral)</td><td>6525.T</td><td>9,500</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates.</td><td>(+/-) Changes in investment at key customers (+/-) Additional changes in export controls (+/-) Changes in the competitive landscape due to strategic changes at competitors</td></tr><tr><td>Ulvac (Neutral)</td><td>6728.T</td><td>10,300</td><td>Based on the global SPE sector average multiple of 18X and our FY6/28E estimates. We then apply a sector-relative discount of 50%.</td><td>(+/-) Effects of margin improvement from structural reforms materializing faster/slower than expected (+/-) Fluctuations in the timing of sales recognition due to changes in production lead times (+/-) Changes in the competitive environment for core sputtering equipment</td></tr><tr><td>Advantest (Neutral)</td><td>6857.T</td><td>35,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 40%.</td><td>(+/-) fluctuations in customer capex appetite (+/-) fluctuations in market share (+/-) trends in tester demand for China (+/-) FX fluctuations for JPY/USD</td></tr><tr><td>Lasertec (Buy)*</td><td>6920.T</td><td>70,000</td><td>Based on the global SPE sector average multiple of 18X and the average of our FY6/28E estimates. We then apply a sector-relative premium of 50%.</td><td>(-) Decline in market share due to new entrants (-) Lack of progress in ACTIS adoption by wafer fabs (-) Weaker customer investment appetite for leading-edge process nodes (-) Rapid appreciation of the yen against the US dollar</td></tr><tr><td>JEOL (Neutral)</td><td>6951.T</td><td>8,300</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative discount of 50%.</td><td>(+/-) substantial changes in investment appetite at major mask shops (+/-) changes in market share for multi-beam mask writers (+/-) sharp fluctuations in the USD/JPY exchange rate.</td></tr><tr><td>Tokyo Seimitsu (Sell)</td><td>7729.T</td><td>15,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates, to which we apply a sector-relative discount of 40%.</td><td>(+) greater-than-expected semiconductor orders (especially related to generative AI) (+) substantial beat in the metrology instruments segment (+) greater shareholder returns than we expect</td></tr><tr><td>SCREEN HD (Sell)</td><td>7735.T</td><td>12,500</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates, to which we apply a sector-relative discount of 40%.</td><td>(+) higher profit margins in the SPE business (+) market share gains due to company-specific factors (+) enhancement of shareholder returns (+) a market shift in favor of value stocks</td></tr><tr><td>Tokyo Electron (Buy)</td><td>8035.T</td><td>83,000</td><td>Based on the global SPE sector average multiple of 18X and our FY3/28E estimates. We then apply a sector-relative premium of 30%.</td><td>(-) prolonged inventory adjustment phase in the semiconductor industry (-) further strengthening of export restrictions (-) depressed valuation multiple amid upward pressure on interest rates and other factors</td></tr></table>

\*APAC Conviction List

Source: GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Shuhei Nakamura and Kaho Otake, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Shuhei Nakamura GS Japan Co., Ltd., Kaho Otake GS Japan Co., Ltd..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our

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
