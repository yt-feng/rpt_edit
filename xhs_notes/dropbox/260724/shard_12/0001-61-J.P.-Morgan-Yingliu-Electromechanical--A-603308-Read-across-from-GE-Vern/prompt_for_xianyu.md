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

# Yingliu Electromechanical - A

## Read-across from GE Vernova's 2Q26 results

GE Vernova's (GEV US, covered by Mark Strouse) 2Q26 gas turbine update supports the view that OEM backlogs are still extending and supplier slots remain constrained, which is constructive for upstream hot-end component makers like Yingliu, even though GEV is not a direct customer today. In 2Q26, GEV signed \~20GW of new gas power contracts and raised its FY26E exit expectation for gas backlog+SRA to at least 125GW versus at least 110GW previously. Gas backlog expanded 44GW to 53GW Q/Q and SRAs increased 56GW to 63GW for GEV, showing the order funnel remains full with continued conversion. We see this as consistent with sustained pricing discipline and longer lead-time visibility across the supply chain. We stay OW on Yingliu with a Dec-27 PT Rmb95, trading at FY28E P/E \~20x.

\- GEV provides a constructive industry signal. GEV highlighted the gas turbines under contract increased 100GW to 116GW sequentially, with management targeting at least 125GW by year-end (previously at least 110 GW). GEV also noted 1H26 gas equipment order pricing running >20% above 4Q25 levels, and it expects 2H26 pricing to stay at the higher end of the 10–20% uplift range versus 4Q25 – see our U.S analyst's First Take on the GEV result (note). In addition, GEV outlined a pathway to 30GW of annual gas output by 2030 via lean and incremental machinery within the existing footprint. We view incremental OEM capacity additions as directionally positive for upstream suppliers because they raise the volume ceiling for castings and pull forward qualification and procurement planning.

\- Siemens Energy signals backlog extension and pricing strength. The Siemens Energy (ENR GR, covered by Phil Buller) read-through framework continues to point to backlogs extending through 2027-2028, alongside a still-strong pricing environment even as supply gradually rises later in the decade. See our European Capital Goods analyst's comment (note). This matters for Yingliu because Siemens Energy is expected to be the most important direct customer ramp over the next 2–3 years, with procurement volume rising \~10x.

\- Oversupply debate not going away. Investor concern is whether OEM capacity expansion creates over-supply late-decade, but GEV framed industry supply/demand as “very balanced” over the next \~6 years for heavy-duty equipment. Our European analyst’s framework suggests global supply of \~64GW in FY26 versus demand trending \~115–120GW, rising to \~70GW in FY27 against \~110–120GW demand, and \~80GW in FY28 against \~110–120GW demand. By FY30, supply could reach \~90GW+ or \~95GW+, including incremental GEV additions, where balance may start to tighten, but we still expect backlogs to extend over the next 2-3 years.

Overweight

603308.SS, 603308 CH
Price (22 Jul 26):Rmb43.57
Price Target (Dec-27):Rmb95.00

Infrastructure, Industrials & Transport

Jenny Qiu, CFA AC
(852) 2800 8503
jenny.qiu@JPM.com

Karen Li, CFA
(852) 2800-8589
karen.yy.li@JPM.com

Sunny Su
(852) 2800 8551
sunny.su@JPM.com

Mufan Shi
(852) 2800-8502
mufan.shi@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 4 for analyst certification and important disclosures, including non-US analyst disclosures.

Figure 1: GEV's backlog + SRAs (GW)  
![](images/5ca6677952f08deaf08ed98ebfcaca69b96acacda3a03d96b4989391565f8750.jpg)  
Source: JPM, GE Vernova company reports.

Table 1: Global gas turbine components and OEM comps

<table><tr><td rowspan="2"></td><td rowspan="2">BBG Ticker</td><td rowspan="2">JPM Rating</td><td rowspan="2">Last Price LC</td><td rowspan="2">JPM PT LC</td><td rowspan="2">Upside/Downside</td><td rowspan="2">Mkt Cap US$Mn</td><td rowspan="2">YTD Stock perf.</td><td colspan="3">P/E (x)</td><td colspan="3">EPS growth Y/Y</td><td colspan="2">PEG</td><td colspan="2">ROE (%)</td></tr><tr><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY28E</td><td>FY26E</td><td>FY27E</td><td>FY26E</td><td>FY27E</td></tr><tr><td colspan="18">Gas Turbine Components</td></tr><tr><td>Yingliu</td><td>603308 CH</td><td>OW</td><td>45</td><td>95</td><td>110%</td><td>4,544</td><td>8%</td><td>47</td><td>30</td><td>19</td><td>90%</td><td>58%</td><td>56%</td><td>0.8</td><td>0.5</td><td>11.7</td><td>16.8</td></tr><tr><td>Howmet Aerospace</td><td>HWM US</td><td>OW</td><td>281</td><td>310</td><td>10%</td><td>112,310</td><td>37%</td><td>56</td><td>47</td><td>40</td><td>37%</td><td>17%</td><td>19%</td><td>3.2</td><td>2.5</td><td>34.3</td><td>34.7</td></tr><tr><td>Doncasters</td><td>DPC US</td><td>NC</td><td>47</td><td>NA</td><td>NA</td><td>7,002</td><td>NA</td><td>114</td><td>60</td><td>47</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>Wedge Industrial</td><td>000534 CH</td><td>NC</td><td>25</td><td>NA</td><td>NA</td><td>1,913</td><td>16%</td><td>38</td><td>26</td><td>18</td><td>41%</td><td>45%</td><td>49%</td><td>0.8</td><td>0.5</td><td>17.6</td><td>20.4</td></tr><tr><td>Himile Mechanical</td><td>002595 CH</td><td>NC</td><td>49</td><td>NA</td><td>NA</td><td>8,454</td><td>-15%</td><td>20</td><td>17</td><td>15</td><td>18%</td><td>15%</td><td>16%</td><td>1.3</td><td>1.1</td><td>21.3</td><td>21.0</td></tr><tr><td colspan="8">Average</td><td>55</td><td>36</td><td>28</td><td>46%</td><td>34%</td><td>35%</td><td>1.5</td><td>1.2</td><td>21.2</td><td>23.2</td></tr><tr><td colspan="18">Gas Turbine OEMs</td></tr><tr><td>GE Vernova</td><td>GEV US</td><td>OW</td><td>985</td><td>1,302</td><td>32%</td><td>262,347</td><td>51%</td><td>44</td><td>41</td><td>29</td><td>198%</td><td>8%</td><td>39%</td><td>5.3</td><td>1.0</td><td>39.6</td><td>35.7</td></tr><tr><td>Siemens Energy</td><td>ENR GY</td><td>OW</td><td>152</td><td>235</td><td>54%</td><td>149,762</td><td>27%</td><td>31</td><td>23</td><td>22</td><td>204%</td><td>32%</td><td>8%</td><td>1.0</td><td>2.8</td><td>34.4</td><td>33.9</td></tr><tr><td>Mitsubishi Heavy Industries</td><td>7011 JP</td><td>NC</td><td>3,895</td><td>NA</td><td>NA</td><td>80,586</td><td>1%</td><td>45</td><td>32</td><td>27</td><td>7%</td><td>42%</td><td>18%</td><td>1.1</td><td>1.7</td><td>11.6</td><td>13.0</td></tr><tr><td>Baker Hughes</td><td>BKR US</td><td>OW</td><td>57</td><td>74</td><td>31%</td><td>56,151</td><td>24%</td><td>23</td><td>20</td><td>17</td><td>-2%</td><td>19%</td><td>20%</td><td>1.3</td><td>1.0</td><td>12.5</td><td>12.5</td></tr><tr><td>Doosan Enerbility</td><td>034020 KS</td><td>OW</td><td>71,300</td><td>130,000</td><td>82%</td><td>31,119</td><td>-6%</td><td>139</td><td>68</td><td>46</td><td>N.A</td><td>104%</td><td>48%</td><td>1.3</td><td>1.4</td><td>4.1</td><td>7.9</td></tr><tr><td>Caterpillar Inc</td><td>CAT US</td><td>OW</td><td>889</td><td>1,165</td><td>31%</td><td>409,609</td><td>55%</td><td>35</td><td>29</td><td>26</td><td>34%</td><td>21%</td><td>13%</td><td>1.7</td><td>2.2</td><td>97.3</td><td>N.A</td></tr><tr><td>Yantai Jereh</td><td>002353 CH</td><td>OW</td><td>135</td><td>162</td><td>20%</td><td>20,432</td><td>91%</td><td>40</td><td>27</td><td>25</td><td>14%</td><td>47%</td><td>7%</td><td>0.8</td><td>3.9</td><td>14.1</td><td>18.0</td></tr><tr><td>Dongfang Electric</td><td>1072 HK</td><td>NC</td><td>23</td><td>NA</td><td>NA</td><td>13,249</td><td>-9%</td><td>14</td><td>12</td><td>11</td><td>21%</td><td>23%</td><td>6%</td><td>0.6</td><td>1.9</td><td>10.5</td><td>11.7</td></tr><tr><td>Shanghai Electric</td><td>2727 HK</td><td>NC</td><td>3</td><td>NA</td><td>NA</td><td>13,533</td><td>-14%</td><td>31</td><td>24</td><td>18</td><td>84%</td><td>28%</td><td>38%</td><td>1.1</td><td>0.6</td><td>2.6</td><td>3.2</td></tr><tr><td colspan="8">Average</td><td>45</td><td>31</td><td>24</td><td>70%</td><td>36%</td><td>22%</td><td>1.6</td><td>1.8</td><td>25.2</td><td>17.0</td></tr></table>

Source: Bloomberg Finance L.P., JPM estimates. Estimates for Not Covered (NC) companies are based on Bloomberg consensus data. Japanese names have financial years ending March. DPC just listed in Jun 2026 so no forecast data, As of July 23, 2026.

# Investment Thesis, Valuation and Risks

Yingliu Electromechanical - A (Overweight; Price Target: Rmb95.00)

## Investment Thesis

Yingliu is China's largest high-temperature alloy and precision casting supplier positioned across gas turbine and aero-engine hot-end components, with access to global OEMs including Baker Hughes, Siemens Energy, Ansaldo, Doosan, GE Aerospace, Safran and Rolls-Royce. Its core appeal is scarcity: Yingliu's FY25A gas turbine revenue was only Rmb1B, implying about 2% global blade market share, but we expect this to rise to 10% by 2030 as OEMs diversify suppliers. Gas turbines are the near-term growth engine, supported by AIDC power demand and industry undersupply, with global gas turbine demand expected to exceed 100GW annually from 2026 to 2035 while 2026 manufacturing capacity is only 64GW. Aero engines provide a second growth leg, as Yingliu is the only China-based hot-end supplier to GE Aerospace, Safran and Rolls-Royce, with long-term contracts extending to 2030–2032.

## Valuation

We derive our Rmb95 Dec-27 PT by applying 40x FY28E P/E to Yingliu's FY28E EPS, using Howmet's average FY27E–FY28E P/E of around 40x as the key benchmark and noting our US analyst's 48x FY28E target multiple for Howmet.

## Risks to Rating and Price Target

Downside risks include: 1) slower-than-expected gas turbine demand growth if alternative power solutions such as gas engines gain share; 2) delayed customer ramp-up at key OEMs, including Baker Hughes, Siemens Energy and Ansaldo; 3) lower-than-expected GPM improvement due to weaker production yield, pricing or product mix; and 4) geopolitical or export-control risks affecting Russian client exposure or access to imported US/EU equipment needed for capacity expansion.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Yingliu Electromechanical - A or related entities.

\- Debt Position: JPM may hold a position in the debt securities of Yingliu Electromechanical - A or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Yingliu Electromechanical - A (603308.SS, 603308 CH) Price Chart  
![](images/ef134463995c0d2801b28530daf91eedc8b4b81ff28bc4e9eea7a975e1d71c94.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>01-Jun-26</td><td>OW</td><td>64.67</td><td>95</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Jun 01, 2026. All share prices are as of market close on the previous business day.  
The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.  
JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Qiu, Jenny : Air China - A (601111.SS), Air China - H (0753.HK), Beijing Capital International Airport (0694.HK), China Eastern Airlines - A (600115.SS), China Eastern Airlines - H (0670.HK), China Railway Group Limited - A (601390.SS), China Railway Group Limited - H (0390.HK), China Southern Airlines - A (600029.SS), China Southern Airlines - H (1055.HK), China State Construction (3311) (3311.HK), Daqin Railway - A (601006.SS), Guangzhou Baiyun International Airport - A (600004.SS), Jiangsu Expressway - A (600377.SS), Jiangsu Expressway - H (0177.HK), Shanghai International Airport - A (600009.SS), Shenzhen Airport Co Ltd -

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
