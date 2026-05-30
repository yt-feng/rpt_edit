你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Global Memory Market

CPU adds fuel to the ‘higher and longer’ upcycle thesis and 28E TAM at \$1.7trn; valuation framework transition in progress

- Memory demands broaden out from GPU to CPU. CPU compute workload for AI is accelerating for orchestration (task coordination and logic), state management, and API execution. We have witnessed strong traction in Vera CPU adoption and expect major CSP customers to launch their own in-house CPU (e.g. Graviton/Axion) from 2H27 onwards. The CPU-to-GPU ratio has consistently trended up over the past three years (from 5.4:1 in '23 to 3.2:1 in '25) and we estimate it moving up to 2.4:1 by 28E (major reason behind 20-22% FY27E-28E server-grade DDR/LPDDR5 bit demand upward revision). We forecast AI CPU DRAM (headnode and standalone) demand at 11mn/17mn GB for FY27E-28E (19%/24% of total market demand). In the long term, Physical and World AI are the next areas of growth and a series of new applications (e.g. wearable and humanoid) are under development.   
- Higher Memory TAM, S-D shortage likely to worsen next year, LTA remains to ASP stabilization. Reflecting CoWoS model upward revisions (note), CPU memory upside, and CE demand degrade, we revise up our FY26E-28E memory TAM by 37-53% (vs Mar-26 model) and expect S-D shortage to worsen. This could theoretically add further upside risk to pricing for DRAM/NAND next year after a 220-250% y-y increase this year; however, we see a rather stable pricing trend supported by an increase in LTA contract sales mix. We estimate the Memory TAM will further expand to US\$1.3trn in 27E with \~50% market cap upside throughout next year using a 3.6x P/S multiple. Upside could be greater if we use the Market Cap to OP approach as memory stocks trade at a discount to their earnings (Figures 2-4 for details).   
- HBM ASP upside risk from tighter S-D, higher wafer allocation trend continues. We have introduced a new HBM S-D view with higher TAM (17-21% upward revision through 26E-28E) and the key changes are: i) ASIC demand acceleration (ASIC bit mix up from 33% in 26E to 39% in 27E), ii) NVDA Rubin GPU forecast cut in 26E offset by stronger GB build, iii) conservative HBM4E content assumption reflecting a longer 12Hi product life-cycle. Given the \$/bit crossover between HBM and non-HBM, we expect memory makers to turn vocal on raising HBM ASP next year (JPMe: +10% y-y on a like-for-like and +30% on a blended basis). As the HBM bit installation demand CAGR (+85% in the next three years) continues to outpace the rest of the market, we believe DRAM wafer capacity allocation to HBM will continue to rise (from 24% in 26E to 31% in 28E) adding greater pressure on conventional DRAM S-D.   
- Memory gains substantial value within CSP capex, higher hardware spending to add confidence to memory earnings. Memory is turning into a strategic asset (MU CEO interview) and we believe stable procurement is imperative for AI service operations for faster and high quality service quality. Memory as a % of total CSP hardware capex ranged between mid-teens % at the beginning of AI and is now anticipated to reach over half this year. Considering the importance of memory's role in AI compute systems, a higher value share is understandable, but many investors we have spoken to have

# Technology - Semiconductors

# Jay Kwon AC

(82-2) 758-5725

jay.h.kwon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

# Sangsik Lee

(82-2) 758 5146

sangsik.lee@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

# Neelay Y Kamath

(91-22) 6157 3764

neelay.kamath@jpmchase.com

JPM India Private Limited

# Harlan Sur

(1-415) 315-6700

harlan.sur@JPM.com

JPM Securities LLC

# Mio Shikanai

(81-3) 6736 1313

mio.shikanai@JPM.com

JPM Securities Japan Co., Ltd.

expressed concerns surrounding memory's further value share hike next year. This is one of the major reasons why memory stocks continue to trade at a discount to EPS. Higher CSP hardware capex (JPM hardware research for details) and greater longevity (more evidence on NVDA's 2030E US\$3-4trn spending outlook commentary) should help alleviate concerns on memory earnings, in our view. Delayed utility infrastructure readiness or a slower new AI business model pickup could negatively impact hardware capex spending and eventually related memory demand.

- Enterprise SSD leads NAND TAM expansion, capex upward revision not yet meaningful. We see a clear trend in customers' preference for high-density and high-speed SSD with meaningful content growth (JPMe: over 40% GB per server increase y-y). We estimate the eSSD market to be over 500EB in 26E (43% of total NAND bit demand) and we forecast it to rise to over 1,100EB in the next two years at a +52% CAGR. Considering the ASP premium, eSSD value TAM could be over US\$300bn (larger than HBM TAM) in the next two years. On technology upfront, SLC based high speed SSD is gaining stronger traction on top of mainstream TLC SSD and we expect to see various solutions hitting the market from 2H26E (high I/OPs, HBF, and others). A growing SLC mix could be in favor of NAND S-D (higher bit per wafer trade-off vs TLC/QLC) as capex spending continues to remain below historical peak levels.   
- Capex acceleration to debottleneck the supply shortage. Sharp memory economics improvement and a multi-year shortage outlook incentivize suppliers to accelerate capex spending (JPMe: US\$450bn in the next three years vs US\$300bn from Dec-25 model). DRAM: CY28-end WSPM at 2.8mn (880k increase from CY25-end) with three years accumulated capex of US\$364bn. 60% of incremental WSPM allocation to HBM and capex-to-sales average at 13% in the next three years. EUV procurement and infrastructure build out capacity is a key bottleneck. NAND: CY28-end WSPM at 1.44mn (165k increase from CY25-end) with US\$86bn spending (three year combined basis). Majority of spend is on tech migration and greenfield capacity impact materializing from 2H28. Relatively lower priority vs DRAM among top 3 producers, but we are beginning to see evidence of 2029 greenfield projects.   
- China Competition Assessment. Volume share gains continue (DRAM share from 6% in '25 to 8-11% in 26E-28E and NAND share from 12% in '25 to 12-16% in 26E-28E) with above-industry capacity build out trends (DRAM/NAND capacity shares each at 18%/19% by CY28-end) and improving supply-chain localization. While all suppliers benefit from favorable S-D dynamics, inferior product mix likely limits the value share gain potential (DRAM/NAND value share at 10%/12% by CY28E). Key monitoring points are: 1) DRAM WSPM allocation amount to HBM (greater HBM wafer mix would result in tighter conventional DRAM S-D) and 2) Equipment export restriction policy update (i.e. MATCH Act - link).   
- Investment recommendations. The global memory sector continues to outperform the respective index and ecosystem peers 2026-YTD and we maintain our multi-year bullish view on the sector. Fundamental key drivers remain: a) AI demand broadening out to CPU, b) rising HBM wafer allocation with greater trade loss ratio, and c) supply discipline in NAND (i.e. under-investment continuing) with potential supply constraints via SLC demand pickup. We acknowledge that the path to a new valuation framework will likely be a patchy one; however, we argue that AI has introduced a new spectrum of demand profiles and view a new valuation approach as necessary (GMM: “LTA paves the path for a new valuation framework” for details). Our top buy ideas include Korea Memory (SKH > SEC in the near-term), Kioxia in Japan, Micron in the U.S. We also like Winbond from Taiwan (covered by Jimmy Huang). For the broader supply chain in Asia, we like TEL (SPE) in Japan and SIMO (covered by Gokul Hariharan) in the controller solution space. Lastly, we view the risk-reward balance as unfavorable in selective stocks (Hanmi).

# Key charts

Figure 1: Aggregate market cap vs leading memory market revenue trend (1Q ahead)   
![](images/09f922416ad0dd5b27d03ca14a84a10651bfbfeecd0d8ae967781ca1700663c9.jpg)

<details>
<summary>line</summary>

| Date    | Aggregate market cap rebased to 2014 (LHS) | Memory market revenue 1-Q ahead (RHS) |
|---------|---------------------------------------------|----------------------------------------|
| Dec-14  | ~100                                        | ~10                                    |
| Dec-15  | ~150                                        | ~15                                    |
| Dec-16  | ~200                                        | ~20                                    |
| Dec-17  | ~250                                        | ~25                                    |
| Dec-18  | ~300                                        | ~30                                    |
| Dec-19  | ~350                                        | ~35                                    |
| Dec-20  | ~400                                        | ~40                                    |
| Dec-21  | ~350                                        | ~35                                    |
| Dec-22  | ~300                                        | ~30                                    |
| Dec-23  | ~350                                        | ~35                                    |
| Dec-24  | ~400                                        | ~40                                    |
| Dec-25  | ~1,500                                      | ~1,50                                  |
| Dec-26  | ~2,000                                      | ~2,00                                  |
| Dec-27  | ~2,500                                      | ~2,50                                  |
</details>

Source: WSTS, OMDIA, Bloomberg Finance L.P., JPM estimates. Note: Market cap includes SEC, SK Hynix, Micron, Nanya Technology, Western Digital. Kioxia / SNDK added from 1Q25 and excluded WDC.

Figure 2: Memory TAM vs peak mkt cap/TAM analysis US\$bn, peak mkt cap/TAM (x)   
![](images/73c4d967ac7e10a20d5bb947653dd15891f9f165355acf635c8f6ca76fdf0170.jpg)

<details>
<summary>bar_line</summary>

| Year | Peak market cap. (US$bn) - LHS | Mkt cap / memory TAM - RHS |
| :--- | :--- | :--- |
| 2018 | 450 | 2.9 |
| 2021 | 663 | 4.3 |
| 2025 | 1,075 | 5.0 |
| 2026E YTD | 3,271 | 3.7 |
| 2027E (forecast) | 4,814 | 3.6 |
| 2028E (forecast) | 6,052 | 3.6 |
The chart also notes that 47% upside on 27E TAM (3.6x P/S multiple) and 85% upside on 28E TAM? The data points are annotated with percentages (47% and 85%) indicating relative multiples or changes between the two metrics.
</details>

Source: Bloomberg Finance L.P., WSTS, Company data, JPM estimates. Note: only considered SEC, SKH, and MU market cap.

Figure 3: Memory TAM vs peak mkt cap/memory OP analysis   
![](images/bda90e58679df28679e74095a7480e7a2cb496a55bd2e1d62ac5cc161183ab52.jpg)

<details>
<summary>bar_line</summary>

| Year | Peak market cap. (US$bn) - LHS | Mkt cap / memory OP - RHS |
| :--- | :--- | :--- |
| 2018 | 450 | 6.0 |
| 2021 | 663 | 15.8 |
| 2025 | 1,075 | 16.6 |
| 2026E YTD | 3,271 | 4.9 |
| 2027E (forecast) | 6,180 | 6.0 |
| 2028E (forecast) | 7,675 | 6.0 |
Higher upside potential on profit base vs. P/S 89% upside on 27E OP
</details>

Source: Bloomberg Finance L.P., WSTS, Company data, JPM estimates. Note: only considered SEC, SKH, and MU market cap.

Figure 4: Memory TAM vs Memory OPM   
![](images/da6c05953c2f1fbc5f3f7488ab22a965158b06f7b4baee79f986e40c4ff9ee52.jpg)

<details>
<summary>bar_line</summary>

| Year | Memory TAM (US$bn) | Memory OPM (%) |
| :--- | :--- | :--- |
| 2018 | 155 | 48 |
| 2021 | 153 | 27 |
| 2025 | 214 | 30 |
| 2026E (forecast) | 896 | 75 |
| 2027E (forecast) | 1,337 | 77 |
| 2028E (forecast) | 1,681 | 76 |
New norm OPM at high-70%
</details>

Source: Bloomberg Finance L.P., WSTS, Company data, JPM estimates. Note: only considered SEC, SKH, and MU market cap.

Figure 5: CSP capex and AI memory % share   
![](images/d3f9314746fc84e6f41cb8414996e832cd20742e27f7300831ff3951481e8bcd.jpg)

<details>
<summary>bar_line</summary>

| Year | JPMe CSP capex (US$bn) | NVDAe CSP capex (US$bn) | Memory as % of CSP capex (RHS) (%) |
| :--- | :--- | :--- | :--- |
| 2022 | 150 | - | 20 |
| 2023 | 160 | - | 9 |
| 2024 | 250 | - | 15 |
| 2025 | 400 | - | 16 |
| 2026E | 669 | - | 52 |
| 2027E | 991 | 1000 | 73 |
| 2030E | - | - | - |
CSP hardware capex move up critical for memory to keep value share above 50?
</details>

Source: Company data, Bloomberg Finance L.P., JPM estimates.

Table 1: Market cap changes across AI ecosystem partners   
US\$bn, % 

<table><tr><td>US$bn</td><td>Top 4 CSP</td><td>AI semi</td><td>Foundry</td><td>Memory</td><td>AI ecosystem mkt cap.</td><td>SOX</td><td>NASDAQ index</td><td>DOW Jones index</td></tr><tr><td>1Q24</td><td>8,122</td><td>3,226</td><td>632</td><td>595</td><td>12,575</td><td>5,795</td><td>39,807</td><td>5,254</td></tr><tr><td>2Q24</td><td>8,871</td><td>4,109</td><td>772</td><td>623</td><td>14,376</td><td>6,991</td><td>39,119</td><td>5,460</td></tr><tr><td>3Q24</td><td>8,652</td><td>4,113</td><td>784</td><td>491</td><td>14,039</td><td>6,900</td><td>42,330</td><td>5,762</td></tr><tr><td>4Q24</td><td>9,243</td><td>4,667</td><td>850</td><td>395</td><td>15,156</td><td>7,306</td><td>42,544</td><td>5,882</td></tr><tr><td>1Q25</td><td>8,162</td><td>3,651</td><td>711</td><td>423</td><td>12,947</td><td>6,040</td><td>42,002</td><td>5,612</td></tr><tr><td>2Q25</td><td>10,027</td><td>5,448</td><td>940</td><td>557</td><td>16,972</td><td>8,481</td><td>44,095</td><td>6,205</td></tr><tr><td>3Q25</td><td>10,979</td><td>6,427</td><td>1,111</td><td>721</td><td>19,238</td><td>10,022</td><td>46,398</td><td>6,688</td></tr><tr><td>4Q25</td><td>11,508</td><td>6,594</td><td>1,280</td><td>1,145</td><td>20,526</td><td>10,608</td><td>48,063</td><td>6,846</td></tr><tr><td>1Q26</td><td>9,907</td><td>6,122</td><td>1,424</td><td>1,411</td><td>18,863</td><td>10,738</td><td>46,342</td><td>6,529</td></tr><tr><td>2Q26YTD</td><td>12,435</td><td>8,233</td><td>1,948</td><td>3,369</td><td>25,986</td><td>15,469</td><td>50,669</td><td>7,564</td></tr></table>

% chaqnes 

<table><tr><td>2Q24</td><td>9%</td><td>27%</td><td>22%</td><td>5%</td><td>14%</td><td>21%</td><td>-2%</td><td>4%</td></tr><tr><td>3Q24</td><td>-2%</td><td>0%</td><td>1%</td><td>-21%</td><td>-2%</td><td>-1%</td><td>8%</td><td>6%</td></tr><tr><td>4Q24</td><td>7%</td><td>13%</td><td>8%</td><td>-19%</td><td>8%</td><td>6%</td><td>1%</td><td>2%</td></tr><tr><td>1Q25</td><td>-12%</td><td>-22%</td><td>-16%</td><td>7%</td><td>-15%</td><td>-17%</td><td>-1%</td><td>-5%</td></tr><tr><td>2Q25</td><td>23%</td><td>49%</td><td>32%</td><td>31%</td><td>31%</td><td>40%</td><td>5%</td><td>11%</td></tr><tr><td>3Q25</td><td>9%</td><td>18%</td><td>18%</td><td>30%</td><td>13%</td><td>18%</td><td>5%</td><td>8%</td></tr><tr><td>4Q25</td><td>5%</td><td>3%</td><td>15%</td><td>59%</td><td>7%</td><td>6%</td><td>4%</td><td>2%</td></tr><tr><td>1Q26</td><td>-14%</td><td>-7%</td><td>11%</td><td>23%</td><td>-8%</td><td>1%</td><td>-4%</td><td>-5%</td></tr><tr><td>2Q26YTD</td><td>26%</td><td>34%</td><td>37%</td><td>139%</td><td>38%</td><td>44%</td><td>9%</td><td>16%</td></tr></table>

mkt cap. mix within the AI ecosystem 

<table><tr><td>1Q24</td><td>65%</td><td>26%</td><td>5%</td><td>5%</td><td>100%</td><td rowspan="4"></td></tr><tr><td>2Q24</td><td>62%</td><td>29%</td><td>5%</td><td>4%</td><td>100%</td></tr><tr><td>3Q24</td><td>62%</td><td>29%</td><td>6%</td><td>3%</td><td>100%</td></tr><tr><td>4Q24</td><td>61%</td><td>31%</td><td>6%</td><td>3%</td><td>100%</td></tr><tr><td>1Q25</td><td>63%</td><td>28%</td><td>5%</td><td>3%</td><td>100%</td><td rowspan="4"></td></tr><tr><td>2Q25</td><td>59%</td><td>32%</td><td>6%</td><td>3%</td><td>100%</td></tr><tr><td>3Q25</td><td>57%</td><td>33%</td><td>6%</td><td>4%</td><td>100%</td></tr><tr

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 May 2026 09:53 PM HKT

Disseminated 29 May 2026 09:54 PM HKT
"""
