你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：一句主判断，不超过 32 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Global Physical AI

EQUITY: AUTOS & AUTO PARTS

# Humanoid commercialization

How Boston Dynamics and Figure AI are de-risking the scaling playbook

Since our February anchor report, the investment thesis for Physical AI has shifted from technical viability to commercial scalability. Breakthroughs in mid-May 2026 – specifically as seen in Boston Dynamics' (unlisted) investor presentation (May 18) and Figure AI's (unlisted) six-consecutive days' autonomous endurance showcase (started on May 14) – shows that the industry has crossed the chasm from R&D cost centers to scalable operational assets. Our key takeaway from the two events is clear: the industry is rapidly nearing deployment of humanoids at logistics and industrial sites, and the market is moving into a winner-take-all race driven by mass production unit economics and proprietary data flywheels.

# Boston Dynamics (Hyundai): De-risking manufacturing and securing backlogs

Boston Dynamics' May 18 presentation in Boston outlined a highly disciplined, commercially mature strategy for its all-electric Atlas model, addressing historical investor concerns regarding high BOM and bespoke engineering.

- BOM reduction via component standardization: To unlock true mass production margins, Boston Dynamics has consolidated its complex hydraulic history into just two types of standardized commercial actuators across the entire robot. This drastically simplifies supply chain dependencies and reduces manufacturing capex.   
- The payload and adaptability breakthrough: In the May 18 demonstration, Atlas utilized whole-body control to lift and transport a 23kg (50lbs) mini-refrigerator. In training, the underlying Reinforcement Learning (RL) model successfully scaled to handle weights up to 45kg (100lbs), proving the software's resilience against weight variations. The hardware payload capacity allows it to target heavy-duty industrial tasks (like automotive parts sequencing and steel knitting) that lighter competitors cannot touch.

# Figure AI's logistics showcase and the commercial flywheel

While Boston Dynamics proves heavy-payload capability (up to 50kg), Figure AI is demonstrating the exact operational endurance required to replace human shifts at scale.

- Logistics as the near-term TAM unlock: While automotive giants serve as high-profile validation partners, logistics fulfillment centers represent an immediate, massive total addressable market (TAM). Automotive lines require millimeter-level precision and carry immense safety/liability friction, while logistics (picking, sorting, placing) features a lower precision threshold but infinite volume. For companies such as Coupang (CPNG US, Buy), transitioning from human labor to Robot-as-a-Service (RaaS) models will compress variable opex and permanently insulate margins from labor-intensive models.

\- The ‘BotQ’ factory unit economics: Figure AI has successfully scaled production from one unit per day to one robot per hour (an annualized run-rate capability of 12k+ units). By transitioning from low-volume machining to automotive-grade high-volume die-casting, they are rapidly driving down the marginal cost per robot.

\- Operational de-risking at BMW: Figure AI humanoids completed an 11-month filed deployment at BMW's (BMW GR, Not rated) Spartanburg plant, autonomously moving $90\mathrm{k}+$ critical components with zero teleoperation. This multi-quarter data point severely de-risks the long-term investment requirements.

# Research Analysts

Korea Autos & Auto Parts

# Angela Hong - NFIK

angela.hong@NOM.com

+822 3783 2360

# South Korea Internet & New Media

# Won Kang - NFIK

won.kang@NOM.com

+822 3783 2316

Fig. 1: Global humanoid comparison 

<table><tr><td>Manufacturer</td><td>Boston Dynamics</td><td>Tesla</td><td>UBTECH Robotics</td><td>Unitree Robotics</td><td>Figure AI</td><td>Apptronik</td><td>Agility</td></tr><tr><td>Humanoid</td><td>Atlas</td><td>Optimus Gen-3</td><td>Walker S2</td><td>H2</td><td>Figure 03</td><td>Apollo</td><td>Digit</td></tr><tr><td>Price</td><td>na</td><td>USD20-30k (target)</td><td>USD68k-120k</td><td>USD30k</td><td>USD20k</td><td>USD50k (target)</td><td>USD250k (pilot)</td></tr><tr><td>Number of actuators</td><td>31</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td><td>na</td></tr><tr><td>Key suppliers</td><td>Hyundai Mobis (actuator)LG Innotek (vision system)NVIDIA (compute)DeepMind (AI model)Samsung SDI (battery)</td><td>Tuopu, Sanhua (actuator)Shuanghuan, Nidec, Leaderdrive, Slin (reducer)Moons&#x27; Electric, Fengqiu Technology (motor)Lingyun (torque sensor)SEMCO (camera module)Samsung Elec (compute)xAI (AI model)LGES (battery)</td><td>In-house actuatorNVIDIA (compute)Huawei (AI model)</td><td>In-house actuatorIntel (processor/camera)Livox (LiDAR)Orbbec (vision)Dingzhi Tech. (Motor)NVIDIA (compute)DeepSeek (AI model)</td><td>In-house actuatorLG Innotek (camera module)NVIDIA (compute)OpenAI (AI model)</td><td>In-house actuatorTexas Instruments (motor control system)NVIDIA (compute)DeepMind (AI model)</td><td>In-house actuatorIntel (camera)NVIDIA (compute)AWS (cloud infra)</td></tr><tr><td>Degrees of Freedom</td><td>56</td><td>40+</td><td>52</td><td>31</td><td>30+</td><td>71</td><td>28</td></tr><tr><td>Payload (kg)</td><td>50</td><td>20</td><td>15</td><td>15</td><td>20</td><td>25</td><td>16</td></tr><tr><td>Height (cm)</td><td>190</td><td>173</td><td>176</td><td>182</td><td>172</td><td>173</td><td>175</td></tr><tr><td>Weight (kg)</td><td>90</td><td>57</td><td>70</td><td>70</td><td>61</td><td>73</td><td>65</td></tr><tr><td>Walking speed (km/h)</td><td>9</td><td>8</td><td>7.2</td><td>5.4</td><td>4.3</td><td>3.4</td><td>5</td></tr><tr><td>Run time</td><td>4 hours</td><td>12 hours</td><td>2 hours</td><td>3 hours</td><td>5 hours</td><td>4 hours</td><td>4 hours</td></tr><tr><td>Auto OEM partner</td><td>HMG</td><td>In-house</td><td>BYD, Geely, NIO</td><td>Dongfeng</td><td>BMW</td><td>Mercedes-Benz</td><td>Toyota</td></tr><tr><td>Others</td><td>Max. reach of 2.3m</td><td>-</td><td>Max. reach of 1.8m</td><td>-</td><td>3-second cycle time for parcel sorting</td><td>-</td><td>-</td></tr></table>

Source: Company data, Robozaps, NOM

Fig. 2: Major humanoid companies — funding rounds and valuations 

<table><tr><td>Company</td><td>Date</td><td>Funding Round</td><td>Capital Raised</td><td>Valuation</td><td>Major Investors</td></tr><tr><td rowspan="3">Boston Dynamics</td><td>Jun-21</td><td>Acquisition</td><td>USD880mn</td><td>USD1.1bn</td><td>Hyundai Motor Group</td></tr><tr><td>Jun-17</td><td>Acquisition</td><td>USD100mn</td><td>USD100mn</td><td>Softbank Group</td></tr><tr><td>Dec-13</td><td>Acquisition</td><td>undisclosed</td><td>undisclosed</td><td>Google</td></tr><tr><td rowspan="3">Raiwnbow Robotics</td><td>Dec-24</td><td>Secondary share acquisition via call option exercise</td><td>KRW267.5bn</td><td>KRW1.3tn</td><td>Samsung Electronics</td></tr><tr><td>1Q23</td><td>Initial equity investment</td><td>KRW86.8bn</td><td>KRW590bn</td><td>Samsung Electronics</td></tr><tr><td>Feb-21</td><td>IPO</td><td>KRW26.5bn</td><td>KRW100bn</td><td>-</td></tr><tr><td rowspan="3">Figure AI</td><td>May-25</td><td>Series C</td><td>USD1.5bn</td><td>USD39bn</td><td>Park Venture Capital, Intel Capital, Salesforce, Samsung NEXT ventures</td></tr><tr><td>Feb-24</td><td>Series B</td><td>USD675mn</td><td>USD2.6bn</td><td>NVIDIA, Microsoft, Bezos Expedition, OpenAI, LG Technology Ventures</td></tr><tr><td>May-23</td><td>Series A</td><td>USD70mn</td><td>USD400mn</td><td>Parkway Venture Capital</td></tr><tr><td rowspan="3">Apptronik</td><td>Feb-26</td><td>Series A</td><td>USD935mn</td><td>USD5.3bn</td><td>B Capital Group, Capital Factory, Google, Mercedes-Benz Group, Samsung NEXT ventures</td></tr><tr><td>Feb-23</td><td>Seed Round</td><td>USD13.9mn</td><td>USD109mn</td><td>Terex, Berch Capital and WorldQuant Ventures</td></tr><tr><td>May-22</td><td>Seed Round</td><td>USD14.4mn</td><td>USD59.4mn</td><td>Grit Ventures, Perot Jain, Capital Factory</td></tr><tr><td rowspan="5">Agility Robotics</td><td>Jun-25</td><td>Series C3</td><td>USD400mn</td><td>USD2.15bn</td><td>WP Global Partners, Kirra Global, Palo Alto Capital</td></tr><tr><td>Oct-24</td><td>Series C</td><td>USD105mn</td><td>USD955mn</td><td>Amazon Industrial Innovation Fund, Schaeffler Group USA, Gaingels</td></tr><tr><td>Apr-22</td><td>Series B</td><td>USD150mn</td><td>USD550mn</td><td>Playground Global, DCVC</td></tr><tr><td>Oct-20</td><td>Later Stage VC (Series A)</td><td>USD20mn</td><td>USD50mn</td><td>Playground Global, DCVC</td></tr><tr><td>Feb-18</td><td>Early Stage VC (Series A)</td><td>USD8mn</td><td>USD25mn</td><td>Sony Innovation Fund, Coal Hill Ventures, Playground Global</td></tr><tr><td rowspan="3">Unitree</td><td>Jun-25</td><td>Series C</td><td>USD97mn</td><td>USD1.7bn</td><td>China Mobile, Tencent holdings, Alibaba Group, Geely Capital</td></tr><tr><td>Feb-24</td><td>Series B</td><td>USD140mn</td><td>-</td><td>Gold Stone Investment</td></tr><tr><td>Feb-21</td><td>Series A</td><td>USD10mn</td><td>-</td><td>Shunwei Capital</td></tr></table>

Source: Company data, NOM

# Appendix A-1

This report has been produced by NOM Financial Investment (Korea) Co., Ltd. (NFIK), Korea.

See Disclaimers for NOM Group entity details.

# Analyst Certification

We, Angela Hong and Won Kang, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

# Important Disclosures

# Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

# Distribution of ratings (NOM Group)

The distribution of all ratings published by NOM Group Global Equity Research is as follows:

57% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 34% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

41% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

2% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 0% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 31 March 2026.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation

# Definition of NOM Group's equity research rating system and sectors

The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

# STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

# SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

# Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

# Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd. ('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other membe

[中间内容因长度限制已省略]

TABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Financial Investment (Korea) Co., Ltd., Korea. All rights reserved.
"""
