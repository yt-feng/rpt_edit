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
# China A-Shares Monthly Wrap

June 2026: All eyes on AI

\- Key market drivers: CSI-300/500/1000 recorded +1.8%/8.0%/4.8% in June, outperforming HSI's/HSCEI's -9.1%/-10.3%, respectively. Such a significant contrast reflects investor confidence in China's AI ecosystem, in particular the infrastructure side, while taking a more cautious and selective stance in the China internet space. Abundant liquidity onshore, as evidenced by A-share velocity surging to over 6%, supported such style preference for growth. Offshore investors we spoke with have increasingly been asking about the likelihood of another round of stimulus to be announced around the July politburo meeting, suggesting rising appetite to bottom-fish consumption proxies. That said, feedback from local clients we spoke with suggests expectations on stimulus remain low onshore.

\- Key sector moves: IT, Materials and Financials took the lead over the past month, while Utilities, Energy and Real Estate underperformed (Figure 1).

\- Earnings and valuation: Consensus CSI-300 2026E EPS growth stayed at $24\%$ at end-June. On 30 June, it traded at a 14.6x FTM P/E, or c1.7SD vs median since 2016, and at a 0.7x FTM PEG with FTM EPS y-y of $19.7\%$ . YTD, materials, IT and energy have recorded the strongest FTM EPS integer upward revisions, while communication services, consumer staples and utilities have recorded the biggest FTM EPS integer downward revisions.

\- Key macro data: China's May activity data improved in certain areas, but overall remained soft. IP improved to 0.2% m-m sa, or 4.5% y-y, rebounding from a sharp monthly contraction in April, though the trend pace slowed further to 1% 3m-3m saar. Retail sales softened further, falling 0.6% oya on a 0.1% m/m sa decline. Auto retail sales plunged a further 16.4% oya. FAI contracted sharply by 10.7% oya (vs -8.0% April), dragging ytd FAI further into contraction at -4.1% oya ytd (vs +1.7% in 1Q). By sector, real estate FAI (-24.3% oya) fell the most. May inflation continued the trend with CPI staying soft with PPI continuing to be firm, at a slower pace. AI-related cost pass-through is broadening into upstream semis and downstream electronics, adding a more durable inflation tailwind. Meanwhile, AI-related high-tech also boosted May exports, with a growing price lift (memory chips/modules, AI datacenter equipment, and new energy). FX reserves rose US\$31.7bn to \$3442.2bn. USD/CNY largely stayed flat and ended at c6.79, while the 10-year CGB yield ticked up to 1.72% at end June.

Figure 1: A-share sector returns and top/bottom stock returns (issue market cap >US\$5bn)

<table><tr><td colspan="3">A-share sector returns</td><td colspan="3">A-share stock returns</td><td colspan="3">HK &amp; US listed CN stock returns</td></tr><tr><td>Sector</td><td>1M (%)</td><td>YTD (%)</td><td>Ticker</td><td>Company</td><td>1M (%)</td><td>Ticker</td><td>Company</td><td>1M (%)</td></tr><tr><td>IT</td><td>19.6</td><td>63.1</td><td>002636.SZ</td><td>GDM</td><td>124.2</td><td>ACMR.O</td><td>ACM RESEARCH INC</td><td>37.3</td></tr><tr><td>Materials</td><td>2.7</td><td>9.8</td><td>002409.SZ</td><td>YOKE TECHNOLOGY</td><td>109.1</td><td>1347.HK</td><td>HUA HONG SEMICONDUCTOR LTD</td><td>33.4</td></tr><tr><td>Financials</td><td>-1.3</td><td>-12.4</td><td>000725.SZ</td><td>BOE</td><td>71.4</td><td>2359.HK</td><td>WUXI APTEC CO LTD</td><td>18.0</td></tr><tr><td>Healthcare</td><td>-3.1</td><td>-10.0</td><td>000811.SZ</td><td>YANTAI MOON</td><td>71.1</td><td>2611.HK</td><td>GTJA SECURITIES CO LTD</td><td>13.7</td></tr><tr><td>Industrials</td><td>-4.7</td><td>-0.2</td><td>000021.SZ</td><td>KAIFA</td><td>62.4</td><td>6869.HK</td><td>YANGTZE OPTICAL FIBRE AND CABLE ,</td><td>12.4</td></tr><tr><td>Cons. Discre.</td><td>-9.2</td><td>-17.7</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Communication services</td><td>-9.5</td><td>-16.9</td><td>002128.SZ</td><td>OPENCUT COAL</td><td>-25.3</td><td>2688.HK</td><td>ENN ENERGY HOLDINGS LTD</td><td>-26.3</td></tr><tr><td>Cons. Staples</td><td>-10.3</td><td>-19.6</td><td>000933.SZ</td><td>SHENHUO</td><td>-27.0</td><td>2382.HK</td><td>SUNNY OPTICAL TECHNOLOGY GROU $\dagger$ </td><td>-27.2</td></tr><tr><td>Real Estate</td><td>-10.6</td><td>-16.4</td><td>001979.SZ</td><td>CMSK</td><td>-27.1</td><td>0285.HK</td><td>BYD ELECTRONIC INTERNATIONAL CO</td><td>-28.3</td></tr><tr><td>Energy</td><td>-12.2</td><td>-0.8</td><td>002532.SZ</td><td>SHIMGE PUMP</td><td>-28.1</td><td>1378.HK</td><td>CHINA HONGQIAO GROUP LTD</td><td>-28.4</td></tr><tr><td>Utilities</td><td>-14.1</td><td>0.9</td><td>002379.SZ</td><td>LOFTEN</td><td>-30.5</td><td>6181.HK</td><td>LAOPU GOLD CO LTD</td><td>-31.3</td></tr></table>

Source: LSEG Workspace (30 Jun 2026), Wind (30 Jun 2026). Data as of 30 Jun 2026 HKT market close.

## Equity Macro Research

Erin Zhang, CFA AC
(86-21) 6106 6328
erin.zhang@JPM.com
SAC Registration Number: S1730521090002
JPM Securities (China) Company Limited

(852) 2800-4323
tim.huang@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Rajiv Batra
(65) 6882-8151
rajiv.j.batra@JPM.com
JPM Securities Singapore Private Limited

## Greater China Economics

Feng Zhu
(852) 2800 1745
feng.zhu@JPM.com
JPM Chase Bank, N.A., Hong Kong Branch

Tingting Ge
(852) 2800-0143
tingting.ge@JPM.com
JPM Chase Bank, N.A., Hong Kong Branch

## Head of China Research

Alex Yao
(86 21) 6106 6505
alex.yao@JPM.com
SAC Registration Number: S1730523020001
JPM Securities (China) Company Limited

## Equity review and YTD returns

With key China equity return drivers summarized on the front page, we detail below the top- and bottom-ranked Wind A-share Level 1 sector returns.

## Top 3 performing sectors

\- IT (+20%) continued its lead on AI infrastructure proxies in June.

\- Materials (+3%) saw AI-related materials, e.g., fiber glass and MLCC materials, recording strong return, offset by the retreat in gold and aluminum names.

\- Financials (-1%) saw diverging performance between the outperforming non-bank financials, notably brokers as a catch-up beta trade, and the underperforming banks that suffer from penalties due to regulatory tightening

## Bottom 3 performing sectors

\- Utilities (-14%) corrected on overall macro weakness, while yield as a factor is also out of favor for now.

\- Energy (-12%) retreated on lower oil price due to a potential reopening of the Strait of Hormuz.

\- Real Estate (-11%) corrected as industry data fails to sustain strong momentum.

Figure 2: Market performance

<table><tr><td>Sector</td><td>Jun 26 return</td><td>YTD return</td></tr><tr><td>CSI300</td><td>1.8%</td><td>7.5%</td></tr><tr><td>CSI500</td><td>8.0%</td><td>21.0%</td></tr><tr><td>CSI1000</td><td>4.8%</td><td>16.0%</td></tr><tr><td>Wind All A-shares</td><td>3.2%</td><td>11.5%</td></tr><tr><td>HSCEI</td><td>-10.3%</td><td>-15.2%</td></tr><tr><td>HSI</td><td>-9.1%</td><td>-10.7%</td></tr><tr><td>CSI300 Relative Growth</td><td>9.4%</td><td>26.9%</td></tr><tr><td>CSI300 Relative Value</td><td>-5.6%</td><td>-9.9%</td></tr><tr><td>Wind Dividend</td><td>-8.2%</td><td>-10.1%</td></tr></table>

Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 3: Wind A-share Level 2 sector indices' MTD/YTD returns  
![](images/9f0e9e558f336484593c6293858e8ae58aff0097accf912652cab891412b2b2a.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

## Fund flow, margin financing, issuance

EPFR data recorded -US\$0.4bn in net outflow from A-shares over 1-26 June 2026, led by outflows from Industrials, Financials, and Consumer Discretionary, with IT the only sector recording mild net inflow.

Figure 4: EPFR tracked net A-share flows  
![](images/99d129e68cd77d5b72109322dbc469b99a24cd2d6a95e49649baed7b512322b0.jpg)  
Source: EPFR (26 June 2026), JPM (26 June 2026).

Figure 5: Active global equity funds' China weights vs MSCI benchmarks  
![](images/f8dc6072121e42d1795808c003975771f829ae3cc8d378aee0b496311232c2e5.jpg)  
Source: EPFR, MSCI. Data as of end-May 2026.

Figure 6: Active AeJ/EM equity funds' China weights vs MSCI benchmarks  
![](images/8f42d27015fcc414e6c9246c941ffe6b352b029c62b537e9ff0efe0db34db361.jpg)  
Source: EPFR, MSCI. Data as of end-May 2026.

The A-share margin financing balance as a percentage of A-share market cap edged up to 2.85% at end-June (range of 1.8-3% since 2016), while gross margin buying as a percentage of total A-share turnover stayed around 10% (range of 5.3-12.8% since 2016).

Figure 7: A-share margin financing  
![](images/42be51334cc4f1ccce3ceed14c5fe179c3517765c8e3434b66c5a8f39b7e59cc.jpg)  
Source: Wind (29 June 2026), JPM (29 June 2026).

A-share equity mutual fund issuance remained stable Preliminary data recorded Rmb19bn/Rmb12bn equity/balanced fund issuance in June, while May's final numbers improved to Rmb26bn/Rmb56bn from the preliminary reading of Rm22bn/Rmb31bn.

Annual fundraising proceeds since 2016 have ranged Rmb40bn-419bn for equity funds (median Rmb143bn) and Rmb65bn-1,625bn for balanced funds (median Rmb234bn).

We estimate retail/controlling & strategic shareholders/domestic financial institutions/foreign investors held 43%/42%/12%/3% of A-shares' total market cap at end-2025, based on company shareholding data and the PBOC's statistics of foreign investors' holdings of A-shares, respectively.

## Figure 8: Onshore mutual fund issuance

Onshore mutual fund issuance (Rmb bn)  
![](images/0f52d90126af908c09ec5e16663a328be84f02f78d6556f9f4ee1cb3abead687.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026). Data as of 30 Jun 2026.

## CSI-300 EPS revisions and valuation

Consensus CSI-300 2026E EPS growth was 24% at end-June. On 30 June, it traded at a 14.6x FTM P/E, or c1.7SD vs median since 2016, and at a 0.7x FTM PEG with FTM EPS y-y of 19.7%.

Figure 9: CSI-300 FTM EPS revisions

<table><tr><td rowspan="2"></td><td rowspan="2">FTM EPS growth</td><td colspan="2">FTM EPS growth revision</td><td colspan="2">FTM EPS integer revision</td></tr><tr><td>Since end-Dec 2025</td><td>Since 20 Sep 2024</td><td>Since end-Dec 2025</td><td>Since 20 Sep 2024</td></tr><tr><td>Communication Services</td><td>11%</td><td>5%</td><td>9%</td><td>-13.4%</td><td>0.1%</td></tr><tr><td>Consumer Discretionary</td><td>13%</td><td>-2%</td><td>23%</td><td>-4.6%</td><td>55.4%</td></tr><tr><td>Consumer Staples</td><td>15%</td><td>5%</td><td>25%</td><td>-13.3%</td><td>8.3%</td></tr><tr><td>Energy</td><td>15%</td><td>8%</td><td>8%</td><td>14.6%</td><td>-17.8%</td></tr><tr><td>Financials</td><td>6%</td><td>1%</td><td>1%</td><td>1.9%</td><td>24.6%</td></tr><tr><td>Health Care</td><td>23%</td><td>13%</td><td>20%</td><td>2.0%</td><td>13.5%</td></tr><tr><td>Industrials</td><td>25%</td><td>1%</td><td>15%</td><td>2.9%</td><td>31.2%</td></tr><tr><td>IT</td><td>53%</td><td>10%</td><td>49%</td><td>25.5%</td><td>202.9%</td></tr><tr><td>Materials</td><td>38%</td><td>14%</td><td>18%</td><td>43.4%</td><td>69.0%</td></tr><tr><td>Utilities</td><td>3%</td><td>-3%</td><td>35%</td><td>-6.7%</td><td>44.2%</td></tr><tr><td>Real Estate</td><td>63%</td><td>-24%</td><td>-14.5%</td><td>-835.8%</td><td>-176.7%</td></tr><tr><td>CSI300</td><td>20%</td><td>5%</td><td>17%</td><td>5.7%</td><td>35.2%</td></tr></table>

Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 10: CSI-300 FTM P/E  
![](images/6996dda94f277e92f414d3d6c95a2b15bda9ba7a6e2ee463e07661f06450fed3.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 11: CSI-300 FTM P/E and EPS by sector  
![](images/d04f513dcc51a805fa9a47a17a812ebcb155378b30fb4012b83b02c07a1fcee3.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 12: CSI-300 consensus P/E-EPS metrics vs. other markets  
![](images/87768aa9016e06ccc11fc058d2e51b25c23a20653427cc72f7068c724b3255ac.jpg)  
Source: LSEG Workspace (30 Jun 2026), Wind (30 Jun 2026), JPM (30 Jun 2026). Note: All markets except for CSI-300 are based on MSCI market indices.

## Economic and political review

Average one-year CGB YTM ticked down by 1bp, and 10-year CGB YTM edged down 2bps. New loan creation returned to positive Rmb520bn, but quality was weak with most of the lift from corporate short-term loans and bill financing. Household loans and corporate medium- to long-term loans stayed in contraction, signaling genuine demand weakness. Loan growth slipped to 5.5% oya, a fresh record low; TSF softened to 7.7%..

## May activity recorded another month of broad weakness, though improved from April numbers.

Retail sales softened further, falling 0.6% oya on a 0.1% m/m sa decline. Auto retail sales plunged a further 16.4% oya (-1.1% m/m sa). Several categories recorded sharp declines: spending on household electronics fell 15.6% oya (vs -15.1% April), construction and decoration materials sales fell 13.6%, gold and silver jewelry fell 8.9%, and consumption of oil and related products fell 3.2%. Services spending continued to outperform: services retail sales grew 5.4% oya ytd in May, led by communications, software & information, leasing and business, financial, and transport and storage services. Online sales expanded further, with services outpacing goods.

FAI contracted sharply by 10.7% oya (vs -8.0% April), dragging ytd FAI further into contraction at -4.1% oya ytd (vs +1.7% in 1Q). By sector, real estate FAI (-24.3% oya) fell most and drove the decline, indicating a contraction stronger than seen in 1Q. Manufacturing (-4.2% oya) and infrastructure (-9.4%) also contracted. Within manufacturing, investment broadly cooled or contracted – led by special purpose equipment, chemicals, and pharmaceuticals – while high-tech manufacturing FAI held up better (electrical machinery and equipment, and computers, communications and other electronic equipment).

Industrial production improved to 4.5% oya. On a seasonally adjusted basis, IP rose 0.2%m/m sa but remained soft, rebounding from a sharp monthly contraction in April. The trend pace slowed further to 1.0%3m/3m saar. Industrial restructuring towards high-end manufacturing continued apace, with high-tech and equipment manufacturing outperforming, riding on the tech cycle upswing and policy support: growth accelerated to 15.1% oya and 9.5%, up from 12.8% and 7.2%, respectively. Production of 3D printing equipment, lithium-ion batteries, industrial robots and integrated circuits increased by 54.4%, 40.0%, 27.9%, and 22.9%, respectively. The pace of production of computers, communication and other electronic equipment accelerated to 17.0% oya, up from 15.6% in April.

On inflation, CPI inched up 0.1%m/m sa, or 1.2% y-y, as firmer communications/entertainment prices were offset by ongoing food-price deflation. PPI extended its upturn, rising 0.8%m/m sa or 3.9%oya. Relative to last month, the lift came from industrial upgrading and AI-driven compute demand, pushing up metals, electrical machinery and electronics prices.

Figure 13: Chinese consumer confidence and SME development  
![](images/4e5a3e67d10f0e21e94b94274e5bf78502a679491fdfdaa0cb0c42d19bbaf484.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 14: Chinese government bond yield to maturity (CGB YTM)  
![](images/e03969c9ac4f0027446191d67f3e66fd4d439eb1d60273481c1d2402a3957067.jpg)  
Source: Wind (30 Jun 2026), JPM (30 Jun 2026).

Figure 15: Key macro indicators

<table><tr><td>Macro indicators</td><td>2026-06F</td><td>2026-05F</td><td>2026-05</td><td>2026-04</td></tr><tr><td>CPI (%)</td><td>1.2</td><td>1.4</td><td>1.2</td><td>1.2</td></tr><tr><td>PPI (%)</td><td>4.2</td><td>3.5</td><td>3.9</td><td>2.8</td></tr><tr><td>Industrial production (%)</td><td>5.6</td><td>--</td><td>5.4</td><td>5.6</td></tr><tr><td>FAI YTD y-y (%)</td><td>-3.7</td><td>-1.7</td><td>-4.1</td><td>-1.6</td></tr><tr><td>Manufacturing FAI YTD y-y (%)</td><td>0.3</td><td>0.1</td><td>-0.4</td><td>1.2</td></tr><tr><td>Infrastructure FAI YTD y-y (%)</td><td>

[中间内容因长度限制已省略]

ies discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND

DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
