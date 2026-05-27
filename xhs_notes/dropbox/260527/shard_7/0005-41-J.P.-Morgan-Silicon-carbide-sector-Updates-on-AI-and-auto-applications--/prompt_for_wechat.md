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
# Silicon carbide sector

# Updates on AI and auto applications - AI a positive factor but how meaningful?

We provide our latest thoughts on the SiC sector, based on our industry research. We believe the data center power supply build and upcoming architecture migration from AC to HVDC (high voltage direct current) are bringing positive developments to the SiC sector. Although AI is generating strong sentiments for SiC-related stocks, we caution that expectations shall remain grounded on the contribution level. We think data centers could contribute a \$400-500mn or fewer to the SiC device TAM in 2028 or outer years. As the SiC device TAM was already built up by EV and could reach \$4.0-4.5bn in 2026, we think data center contribution could rise from current LSD to MSD to HSD within two to three years. AI will be a critical driver for the SiC sector, but its contribution level to the SiC device TAM could fall short of the bullish camp's expectations of 20-30%, in our view.

- Data center SiC MOS - long lead time and high price. Our industry research indicates that the lead time for AI SiC MOS has increased to 52 weeks. Additionally, prices for AI SiC MOS (high spec ones) are now at least twice as high as those for auto inverter SiC MOS, when comparing identical die size and Rds(On) specs. This encouraging dynamic is driven by exceptionally strong and urgent orders from AI customers, while qualified production capacity is temporarily limited to meet the surge in demand. Looking ahead, we think price reductions for AI SiC MOS could be much smaller than in the auto market, despite more qualified capacity.   
- Data centers potentially \$400-500mn or fewer to the SiC device TAM in 2028 or outer years. The push towards higher rack power densities is forcing upgrades of data center power architecture from AC to HVDC, and SiC enables more efficient, compact conversion at both the infra level (UPS and SST) and the server level (PSU). Our industry research suggests 1MW HVDC data center power build could have SiC content value of \$5.0-6.0k or slightly higher, based on its power module topology and device price. JPM teams have forecast an 80GW AI data center power new installment in 2028, implying a \$400-480mn contribution to the SiC device TAM, if HVDC penetration is 100%. Yet, the data center SiC TAM shall be smaller than this range, considering the mix between AC and HVDC.   
- SiC device TAM already built up by EV; data center contribution potentially rising to MSD to HSD in 2028 or outer years. Although AI is generating strong sentiment for SiC-related stocks, we caution that expectations should remain grounded on the contribution level. The Yole Group forecasts (link) that the global SiC device TAM will grow from \~\$3.7bn in 2025 to \~\$4.6bn in 2026, up 25% YoY due mainly to the accelerating 800V migration in EVs. In our view, SiC is already benefiting significantly from EV adoption, and we think the global SiC device TAM could be \$4.0-4.5bn in 2026. Data center contribution to the SiC device TAM could grow from currently low single digits to mid-to-high-single digits two to three years out. We believe data centers will be a very important driver for the SiC sector, but we suspect its contribution level could fall short of the bullish camp's

# Technology

# Jimmy Huang AC

(886-2) 2725-9865

jimmy.huang@JPM.com

JPM Securities (Taiwan) Limited

# Akinori Kanemoto

(81-3) 6736 8628

akinori.kanemoto@JPM.com

JPM Securities Japan Co., Ltd.

# Gokul Hariharan

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

expectations of 20-30% (of the TAM).

- SiC substrate prices - 6" stabilized but 8" dropping. Prices for 6" SiC substrates have stabilized at \~Rmb1.5k since early 2026, vs Rmb3.0k in early 2025 and Rmb4.5k in early 2024. Some suppliers have shut down capacity given prices are below their production cash cost (Rmb1.5-2.0k, depending on scale). China's top 2 SiC substrate suppliers are operating at nearly full utilization rates for 6", but industry over-capacity prevents any meaningful price recovery. Prices for 8" SiC substrates have been in constant decline: \~Rmb7.0k in early 2025, Rmb5.5-6.0k in mid 2025, \~Rmb4.5k in early 2026 and \~Rmb4.0k in mid 2026. We expect 8" SiC substrate prices to further decline to Rmb 3.0-4.0k at end 2026 and Rmb2.5-3.5k in 2027. Customers request the pricing gap between 6" and 8" SiC substrates to be below 1.7x, based on wafer area difference. Even considering the production efficiency gain from 6" to 8", the price gap should be capped at 2.0x. Key triggers for the 8" price decline include improvements in yield and efficiency, as well as more effective supply from Chinese suppliers. The above prices are based on our industry research and refer to those offered by Chinese suppliers to large customers. A leading SiC substrate supplier talked about raising 8" prices. We believe it will be quite challenging to raise prices to major, important customers, if a supplier aims for market share. Our industry studies over the past four years and most recent industry discussions do not support the price hike expectation.   
- Auto inverter SiC MOS - ongoing price declines but increasing lead times. Prices for auto inverter SiC MOS also continue to decline rapidly in the China market. Prices from international IDMs could fall from \$6.0-6.5 in 2024 and \$5.0-5.5 in 2025 to \$3.0-3.5 in 2026 and potentially \$2.5 in 2027. Chinese suppliers could quote 15-30% lower, depending on product competency. On the positive side, lead time for auto SiC MOS has increased from 26 weeks (the basic manufacturing time) to 39 weeks, with some specs lengthening to 52 weeks, given the AI crowd-out effect. Pricing negotiation frequency has been reduced from quarterly to semi-annual for some cases, amid the lead time increase. However, whether prices for auto SiC MOS could stabilize into 2027 is not clear, as it depends on supply-side competition. If more Chinese SiC MOS suppliers are qualified for auto inverters, prices for SiC MOS will remain under pressure into 2027.   
- Fast-rising SiC penetration in China EVs. Ongoing SiC price declines drive SiC adoption to EV models priced \~Rmb150k. We think China's SiC EV shipments (excl. Tesla) reached 2.5mn units in 2025 and could rise to 4.0mn units or more in 2026, up 60% YoY or more. This would lift the SiC penetration rate from the mid-teens in 2025 to the low twenties in 2026. Additionally, SiC product iterations are improving on-resistance (Rds(On)), enabling a reduction in the number of SiC MOS dies per module in some EV models (i.e., 1200V modules from 48 to 42/36 dies, and 750V modules from 36 to 30/24 dies). Net-net, we believe the auto SiC device TAM will grow moderately in 2026.   
- Implications for A-share stocks. United Nova (UNT) is the leading Chinese supplier for SiC MOS, and it has mentioned the potential to increase SiC MOS (chip and module) revenue from Rmb1.5bn in 2025 to Rmb3.0bn in 2026 (implying a revenue mix of 18% and 28% in 2025 and 26) (JPM note). We believe UNT remains a key beneficiary of strong SiC MOS demand. UNT has sampled its 8” SiC MOS to an international AI server custoemr for qualification, which we believe is a CSP ASIC company. If UNT can pass qualification, we believe it would help ease the current supply tightness as UNT has mass production capabilities and UNT can ramp up more 8” SiC capacity in a timely manner. SICC is the most leading Chinese supplier for 6” and 8” SiC substrates and could benefit from increasing SiC adoption in datacenters and potentially advanced packaging in the mid to long term. SICC is ramping up its 8” SiC substrates meaningfully this year (i.e. potentially doubling YoY). However, we see continued pricing pressure for 8” SiC substrates through 2026 and we remain cautious on SICC stock, as we sense certain wrong expectations on SiC substrate pricing outlook.   
• Implications for Rohm (covered by Akinori Kanemoto). Against FY25 revenue of just

over JPY 40bn (JPM estimate; +14% YoY, with SiC devices/modules +41% YoY), the company is planning FY26 revenue of just under JPY 55bn (JPM estimate; +30% YoY, with devices/modules +55% YoY). In FY26, management plans to offset the loss of its external 6-inch wafer sales business with growth in device/module revenue. For xEV inverter applications, China accounts for more than half of FY25 sales, but toward FY28 the China mix is expected to decline while Japan/Korea/Europe/US increase. SiC MOSFETs for AI servers have already ramped in FY25, and the company plans to lift the revenue mix to 10% in FY26. On the technology front, mass production of 8-inch wafers is scheduled to start in FY26 - initially deployed in its 4th-generation platform, followed by the rollout of 5th-generation MOS to improve yields and productivity. Including the impact of the impairment taken at FY25 year-end, the company is targeting a return to profitability by FY28.

# Bookshelf – (China) SiC sector reports

- Sep 2025 - Silicon Carbide Sector - Our takes on CoWoS SiC carrier / thermal interface material; GlobalWafers at SEMICON Taiwan - Report link   
- Sep 2025 - Silicon Carbide Sector - News reports on CoWoS SiC interposer; we view this as only a concept and R&D direction, without further visibility - Report link   
- May 2025 - China Silicon Carbide Sector - Renesas abandons plan to produce SiC chips, with Chinese overproduction being one key reason - Report link   
- Apr 2025 - China Silicon Carbide Sector - Key takeaways from our SiC substrate expert call; solid SiC EV model pipeline at the Shanghai Auto Show - Report link   
- Apr 2025- China Silicon Carbide Sector - Increased competition; Updating views on substrates, device, equipment, applications and stocks - Report link   
- Dec 2024 - China Tech - Geopolitical dynamics on mature node semis: US Section 301 investigation and international IDMs' local-for-local strategies - Report link   
- Dec 2024 - China Silicon Carbide Sector - 2024 recap: A tough year for 6" substrates. 2025 outlook: Industry focusing on ramp of 8" substrates & auto SiC MOS; robust growth for China SiC EV - Report link   
- Nov 2024 - China Silicon Carbide Sector - Key takeaways from Axcelis 3Q24 earnings call; China SiC device capacity build dynamics - Report link   
- Nov 2024 - Silicon Carbide Sector - Recent industry dynamics on SiC/Si hybrid modules for EV inverters - Report link   
- Sept 2024 - Silicon Carbide Sector - 8" SiC partnership of Episil Tech and VIS - Report link   
- Aug 2024 - China Silicon Carbide Sector - Read-through from Silan Micro's 1H24 print and earnings call - Report link   
- Jul 2024 - China Silicon Carbide Sector - China auto market landscape and substrate/device 8" transition as focal points; better demand in 2H24 - Report link   
- Jun 2024 - China Silicon Carbide Sector - China auto SiC MOS: Hyper demand growth, rising competition and green shoots of localization - Report link   
- Jun 2024 - United Nova - Chinese leader in auto SiC MOS; Solid revenue growth but lingering profitability pressure; Initiate at Neutral - Report link   
- Mar 2024 - China Silicon Carbide Sector - China substrate competitive landscape updates from TanKeBlue and implications for SICC - Report link   
- Feb 2024 - China Silicon Carbide Sector - Post-CNY checks: ‘Materials’ a back-end loaded 2024 and initial sign of over-supply; implications for Device Equipment - Report link   
- Jan 2024 - China Silicon Carbide Sector - Chinese SiC epi maker EpiWorld IPO prospectus; implications for SICC and SiC industry - Report link   
- Nov 2023 - China Silicon Carbide Sector - On-the-ground checks and key themes for 2024 - Report link   
- Aug 2023 - China Silicon Carbide Sector - Implications from three global SiC power device makers' earnings calls - Report link   
- Jun 2023 - Silicon Carbide Sector - Our views on Chinese progress in substrates, device and equipment; OW SICC and Rohm - Report link

- Apr 2023 - Japan Electronic Components - Power semiconductor industry and position of Japanese manufacturers - Report link   
- Apr 2023 - Silicon Carbide Sector - Asian SiC foundries riding on strong market demand and localization benefits; HANA & Episil Tech - Report link   
- Feb 2023 - First Principles - Silicon Carbide: Key growth driver for European semi device makers - Report link   
- Feb 2023 - Networking & Hardware: The Silicon Carbide (SiC) Cheat Sheet - Report link   
- Feb 2023 - Silicon Carbide Deep Dive: Substrate and Asia focus; positive about the SiC sector and OW WOLF, COHR, Rohm and SICC - Report link   
- Feb 2023 - SICC - Initiate pure China SiC substrate play at OW, on TAM expansion, localization and power SiC ramp - Report link

Companies Discussed in This Report (all prices in this report as of market close on 25 May 2026, unless otherwise indicated) Rohm (6963)(6963.T/¥5,030/OW), United Nova - A(688469.SS/Rmb8.25/N)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

# Important Disclosures

• Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to Rohm (6963), United Nova - A or related entities.   
- Beneficial Ownership (1% or more): JPM beneficially owns 1% or more of a class of common equity securities of Rohm (6963) or related entities.   
- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Rohm (6963) or related entities.   
- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: Rohm (6963) or related entities.   
- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: Rohm (6963) or related entities.   
- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Rohm (6963) or related entities.   
• Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from Rohm (6963) or related entities.   
- Debt Position: JPM may hold a position in the debt securities of Rohm (6963), United Nova - A or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Rohm (6963) (6963.T, 6963 JP) Price Chart   
![](images/193400243368fa87774217881b94a46f0c42f44bdd75bf4229cf19d662263d42.jpg)

<details>
<summary>line</summary>

| Date       | Price(Y) |
| ---------- | -------- |
| Sep 23     | 3,750    |
| Jan 24     | 3,700    |
| May 24     | 3,400    |
| Sep 25     | 1,900    |
| Jan 26     | 2,700    |
| May 26     | 2,500    |
| May 26     | 3,900    |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Y)</td><td>Price Target (Y)</td></tr><tr><td>30-May-23</td><td>OW</td><td>3042</td><td>3,750</td></tr><tr><td>28-Nov-23</td><td>OW</td><td>2725</td><td>3,700</td></tr><tr><td>18-Mar-24</td><td>OW</td><td>2472</td><td>3,400</td></tr><tr><td>22-Jul-25</td><td>N</td><td>1888</td><td>1,900</td></tr><tr><td>10-Oct-25</td><td>OW</td><td>2294</td><td>2,700</td></tr><tr><td>04-Dec-25</td><td>OW</td><td>2116</td><td>2,500</td></tr><tr><td>04-Apr-26</td><td>OW</td><td>3608</td><td>3,900</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Aug 12, 2001. All share prices are as of market close on the previous business day. Break in coverage Jul 04, 2024 - Jul 22, 2025.

United Nova - A (688469.SS, 688469 CH) Price Chart   
![](images/375aad2828e9bb8ba172793407eb03ba9336617c8c195bd692220f47bce22f6d.jpg)

<details>
<summary>line</summary>

| Date       | Price(Rmb) |
| ---------- | ---------- |
| May 24     | N Rmb4.1   |
| Sep 24     | N Rmb3.8   |
| Jan 25     | N Rmb4.5   |
| May 25     | N Rmb4.7   |
| Sep 25     | N Rmb5.3   |
| Jan 26     | N Rmb6.3   |
</details>

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>21-Jun-24</td><td>N</td><td>3.98</td><td>4.1</td></tr><tr><td>02-Sep-24</td><td>N</td><td>3.65</td><td>3.8</td></tr><tr><td>29-Oct-24</td><td>N</td><td>4.79</td><td>4.1</td></tr><tr><td>10-Feb-25</td><td>N</td><td>4.91</td><td>4.5</td></tr><tr><td>02-May-25</td><td>N</td><td>4.64</td><td>4.7</td></tr><tr><td>05-Aug-25</td><td>N</td><td>5.18</td><td>5.3</

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 25 May 2026 11:15 PM HKT

Disseminated 25 May 2026 11:15 PM HKT
"""
