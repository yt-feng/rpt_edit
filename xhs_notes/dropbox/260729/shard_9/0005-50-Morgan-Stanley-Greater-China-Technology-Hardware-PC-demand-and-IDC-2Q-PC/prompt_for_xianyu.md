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
July 27, 2026 12:06 AM GMT

Greater China Technology Hardware | Asia Pacific

# PC demand and IDC 2Q PC Shipment Data

Intel's view on PC demand being resilient in 1H and weakening in 2H echoes our view. And on Agentic AI, we continue to view Wiwynn (Server ODM), Unimicron (CPU ABF), NYPCB (Networking ABF), Lotes/FIT (CPU socket and other peripheral connectors/cables), and GCE (Server PCB) as key beneficiaries.

Implications for our coverage from the Intel (covered by Joseph Moore) earnings call and commentary: Intel mentioned the 15% Client revenue growth was primarily driven by higher ASPs, which were a function of higher high-end mix and price increases to pass through cost inflation, not units. This aligns with our checks with PC OEM/ODM that they have been prioritizing those more profitable, high-end PC models. Intel continues to expect PC demand to weaken in 2H26, guiding for total unit consumption to decline "low-double-digits" y/y in 2026 (Lenovo guided for 2H PC market to see high-teens y/y unit declines), with its 3Q Client revenue guided to be flattish q/q. This implies a fall in PC shipment units in 2H26, which aligns with our forecast of major ODMs' NB builds being sub-seasonal at down 5% q/q (-15% y/y) in 3Q, reflecting a weakened demand outlook in 2H.

As for servers, demand still runs well ahead of supply, improving late 3Q into 4Q, though management admitted Intel will still be under-shipping in Q4. This aligns with our recent supply chain checks that legacy server CPU fulfillment rates currently hover around 80-90% (depends on CPU vendors) at some major server ODMs, with no signs of easing tightness in the near term. On long-term growth outlook, Intel wouldn't endorse AMD's US\$220B-by-2030 TAM (see Joe's report on AMD Advancing AI event recap and takeaways), but guided server growth "well north of a double-digit CAGR", with ASP uplift from rising core counts. Another striking claim on the call was that the CPU-to-GPU ratio is now near parity, vs. the 1:3-4 CPU-to-GPU ratio for inference suggested by Intel management last quarter. This boosts our confidence that general server demand will likely see another year of 20-30%+ y/y (more supply-driven) growth for the ODMs (clouds) in 2027.

"The industry as facing one of the most severe supply constraints in its history" – leading-edge logic, wafers, memory and substrates – expected to persist, according to Intel. Its most-challenged links are back-end inputs including substrates, T-glass and memory, among which substrate was singled out as key bottleneck on the packaging side. Intel also admitted there are some requirements "in terms of putting money up in advance of getting the substrates". Intel has been expressing concerns about the supply tightness of substrates for a couple of quarters now, but to our knowledge it is the first time that it has said it has made "prepayments" to its suppliers in order to secure sufficient supply. This hints at a tighter supply environment vs. three months ago and reaffirms our view that substrate suppliers remain well-positioned to raise prices for substrates in a seller's market.

MS TAIWAN LIMITED+

Howard Kao
Equity Analyst
Howard.Kao@morganstanley.com +886 2 2730-2989

Irene Yen
Research Associate
Irene.Yen@morganstanley.com +886 2 2730-2869

MS ASIA LIMITED+

Andy Meng, CFA
Equity Analyst
Andy.Meng@morganstanley.com

+852 2239-7689

![](images/2e17d0f5f4d55ede0c4ee04e1f1ede7c95094bf9a966a89a47ac576a61e305f8.jpg)

GREATER CHINA TECHNOLOGY HARDWARE
Asia Pacific
Industry View In-Line

Exhibit 1: Our preferred stocks are mostly related to AI and cloud, which we believe are more defensive vs. consumer electronics

<table><tr><td>Company</td><td>Ticker</td><td>Rating</td><td>Rating</td><td>Closing Price (LC)</td><td>PT (LC)</td><td>Upside to PT</td></tr><tr><td>Wistron</td><td>1321.TW</td><td>OW</td><td>Overweight</td><td>179.00</td><td>210.00</td><td>17%</td></tr><tr><td>FIT Hon Teng</td><td>6088.HK</td><td>OW</td><td>Overweight</td><td>5.33 HKD</td><td>12.00 HKD</td><td>125%</td></tr><tr><td>FII</td><td>601138.SS</td><td>OW</td><td>Overweight</td><td>60.25</td><td>82.80</td><td>37%</td></tr><tr><td>Wiwynn</td><td>6669.TW</td><td>OW</td><td>Overweight</td><td>5,730.00</td><td>7,500.00</td><td>31%</td></tr><tr><td>Quanta</td><td>2382.TW</td><td>OW</td><td>Overweight</td><td>328.00</td><td>385.00</td><td>17%</td></tr><tr><td>Delta</td><td>2308.TW</td><td>OW</td><td>Overweight</td><td>1,785.00</td><td>2,700.00</td><td>51%</td></tr><tr><td>GCE</td><td>2368.TW</td><td>OW</td><td>Overweight</td><td>901.00</td><td>1,660.00</td><td>84%</td></tr><tr><td>Genovo</td><td>9568.HK</td><td>OW</td><td>Overweight</td><td>24.34 HKD</td><td>30.00 HKD</td><td>23%</td></tr><tr><td>Giga-Byte</td><td>2376.TW</td><td>EW</td><td>Equal-Weight</td><td>354.50</td><td>375.00</td><td>6%</td></tr><tr><td>Lotes</td><td>3533.TW</td><td>EW</td><td>Equal-Weight</td><td>1,970.00</td><td>2,350.00</td><td>19%</td></tr></table>

Source: Company data, MS estimates. Note: Priced as of July 24, 2026.

For more details on Intel's result, please see Joseph Moore's July 24, 2026 result note.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# IDC's Preliminary 2Q26 Global PC Shipment Data, by Vendor

Preliminary 2Q26 PC shipments (excluding workstations) were above our estimate: According to IDC, 2Q26 desktop and notebook shipments came in at 66.2M (\~flat q/q, -5% y/y), 5% above our estimate of \~63M. It's the first decline after nine consecutive quarters of growth. IDC cite a persistent memory chip shortage as the reason for the reversal.

IDC think there is a disconnect between units and dollars: shipments are falling, but revenue is climbing because vendors are pushing through price increases faster than demand is dropping. And IDC don't expect another round of inventory pull-forward, which points to a sharp slowdown in growth rates in 2H26. According to IDC, vendors are bracing for further price hikes into 2027, and channels are already flagging concerns about elevated inventory at these higher price points.

IDC also note that amid the decline, two additional underlying trends stand out. The first is the growing risk that sustained cost pressure from the memory shortage could temper the broader PC upgrade cycle, even as interest in on-device AI processing continues to grow amid rising cloud compute costs. The second is further vendor consolidation, as top brands such as Apple, Dell, and Lenovo use their scale across adjacent business lines, including smartphones and servers, to secure memory supply and squeeze out smaller competitors.

## Lenovo – Maintained #1 position

• Market share (including Fujitsu): 24.4% (+2bp q/q, +72bp y/y)

• Shipments (including Fujitsu): 16.6mn units (flat q/q, -2% y/y)

## HP – Maintained #2 position

• Market share: 19.1% (+119bp q/q, -86bp y/y)

• Shipments: 13.0mn units (+7% q/q, -9% y/y)

## Dell – Maintained #3 position

• Market share: 13.6% (-152bp q/q, flat y/y)

• Shipments: 9.3mn units (-10% q/q, -5% y/y)

## Apple – Maintained #4 position

• Market share: 9.9% (+55bp q/q, +135bp y/y)

• Shipments: 6.7mn units (+6% q/q, +10% y/y)

## Asustek – Maintained #5 position

• Market share: 7.4% (+31bp q/q, +38bp y/y)

• Shipments: 5.0mn units (+5% q/q, flat y/y)

Exhibit 2: PC brand NB/DT mix (2025)  
PC brand NB/DT mix (2025)  
![](images/559aab303d829df8b4d572ede960f3e141eed8e0bbb7ddd131159c5a69fdb401.jpg)  
Source: IDC, MS.

Exhibit 3: PC brand commercial/consumer mix (2025)  
PC brand consumer/commercial mix (2025)  
![](images/1eac17e50e3b8cca68e98faffc46e85f48d889497c33fcccf5c65650fb02a31e.jpg)  
Source: IDC, MS.

Exhibit 4: NB ODM commercial/consumer mix (2025)  
![](images/c920e3c6f57329585745490edbb9654171c0e3a76289415826ddfd2ffcaba457.jpg)  
Source: IDC, MS.

Exhibit 5:  
MS PC forecasts  
![](images/5e3568a2f123f4374d80255d7e264a28d3c77b5d36b0f8439cbe6211148e1aea.jpg)  
Source: IDC, MS. E = MS estimates.

## Key Takeaways from Intel's 2Q26 Earnings Call

Details on the quarter: Below is an excerpt from Joseph Moore's July 24, 2026 report, Intel Corporation: Strong earnings, higher spending (24 Jul 2026).

Details on the quarter: June non-GAAP revenue of \$16.128bn came in above the Street and our estimate of \$14.417bn and \$14.458bn, respectively. By segment, Client Computing and Physical AI Group (CCPG) revenue was \$8.877bn (up 12.8% y/y), Data Center & AI (DCAI) was \$6.262bn (up 59% y/y), and Intel Foundry (IFS) revenue was \$5.765bn (up 30.5% y/y). Gross margin of 41.8% (up 75bps q/q and 1212bps y/y) was ahead of the Street and our estimate of 39.8% and 39.5%, respectively. Non-GAAP EPS of \$0.43 came in ahead of the Street at \$0.21 and our estimate of \$0.24.

Details on guidance: Revenue was guided to \$16.3bn at the midpoint (up 1.1% q/q and 25.4% y/y), above the Street at \$15.067bn and our estimate of \$15.092bn. Gross margin of 42.0% was above our estimate of 40.5% and the Street also at 40.5%. EPS guidance of \$0.38 was above the Street at \$0.27 and our estimate of \$0.30.

Exhibits

US PC Vendor Ranking, 2Q26  
Exhibit6: Worldwide PC Vendor Ranking, 2Q26  
Worldwide PC Vendor Ranking, 2Q26

<table><tr><td>Rank</td><td>Vendor</td><td>2Q26 Shipments</td><td>2Q26 Market share</td><td>1Q26 Shipments</td><td>1Q26 Market share</td><td>2Q25 Shipments</td><td>2Q25 Market share</td><td>QoQ</td><td>YoY</td></tr><tr><td>1</td><td>Lenovo</td><td>16,622</td><td>24.4%</td><td>16,541</td><td>24.4%</td><td>16,974</td><td>23.7%</td><td>0%</td><td>-2%</td></tr><tr><td>2</td><td>HP</td><td>13,002</td><td>19.1%</td><td>12,140</td><td>17.9%</td><td>14,294</td><td>19.9%</td><td>7%</td><td>-9%</td></tr><tr><td>3</td><td>Dell</td><td>9,290</td><td>13.6%</td><td>10,286</td><td>15.1%</td><td>9,774</td><td>13.6%</td><td>-10%</td><td>-5%</td></tr><tr><td>4</td><td>Apple</td><td>6,724</td><td>9.9%</td><td>6,326</td><td>9.3%</td><td>6,107</td><td>8.5%</td><td>6%</td><td>10%</td></tr><tr><td>5</td><td>ASUS</td><td>5,014</td><td>7.4%</td><td>4,780</td><td>7.0%</td><td>5,002</td><td>7.0%</td><td>5%</td><td>0%</td></tr><tr><td></td><td>Others</td><td>17,526</td><td>25.7%</td><td>17,822</td><td>26.2%</td><td>19,577</td><td>27.3%</td><td>-2%</td><td>-10%</td></tr><tr><td></td><td>Total</td><td>68,178</td><td></td><td>67,895</td><td></td><td>71,728</td><td></td><td>0%</td><td>-5%</td></tr></table>

Note: Shipments in '000s. Source: IDC; MS.

Exhibit7: US PC Vendor Ranking, 2Q26

<table><tr><td>Rank</td><td>Vendor</td><td>2Q26 Shipments</td><td>2Q26 Market share</td><td>1Q26 Shipments</td><td>1Q26 Market share</td><td>2Q25 Shipments</td><td>2Q25 Market share</td><td>QoQ</td><td>YoY</td></tr><tr><td>1</td><td>HP</td><td>4,593</td><td>25.5%</td><td>3,227</td><td>20.3%</td><td>4,769</td><td>25.1%</td><td>42%</td><td>-4%</td></tr><tr><td>2</td><td>Dell</td><td>4,051</td><td>22.5%</td><td>3,959</td><td>24.9%</td><td>4,507</td><td>23.8%</td><td>2%</td><td>-10%</td></tr><tr><td>3</td><td>Lenovo</td><td>3,380</td><td>18.8%</td><td>3,146</td><td>19.8%</td><td>3,417</td><td>18.0%</td><td>7%</td><td>-1%</td></tr><tr><td>4</td><td>Apple</td><td>2,870</td><td>15.9%</td><td>2,686</td><td>16.9%</td><td>2,860</td><td>15.1%</td><td>7%</td><td>0%</td></tr><tr><td>5</td><td>Acer</td><td>1,291</td><td>7.2%</td><td>892</td><td>5.6%</td><td>1,144</td><td>6.0%</td><td>45%</td><td>13%</td></tr><tr><td></td><td>Others</td><td>1,832</td><td>10.2%</td><td>1,980</td><td>12.5%</td><td>2,271</td><td>12.0%</td><td>-7%</td><td>-19%</td></tr><tr><td></td><td>Total</td><td>18,017</td><td></td><td>15,890</td><td></td><td>18,968</td><td></td><td>13%</td><td>-5%</td></tr></table>

Note: Shipments in '000s. Source: IDC, MS.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Howard Kao; Andy Meng, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management pol

[中间内容因长度限制已省略]

<tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>O (07/15/2026)</td><td>HK$121.10</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb90.27</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb27.35</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,046.51</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$24.56</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb35.00</td></tr><tr><td colspan="3">Derrick Yang</td></tr><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,220.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$581.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,425.00</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,380.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$25.50</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$943.00</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,205.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb5.79</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,095.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,080.00</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$1,785.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$191.00</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$54.60</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,410.00</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$313.00</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$49.50</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$7,735.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb37.32</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$214.50</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb5.04</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb6.15</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb224.61</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$30.05</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$771.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$189.50</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$37.20</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$5.33</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb60.25</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$354.50</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$901.00</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$252.50</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb85.31</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$1,760.00</td></tr><tr><td>Lenovo (0992.HK)</td><td>O (07/10/2026)</td><td>HK$24.34</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$1,970.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$1,110.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$88.40</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$328.00</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb118.71</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb332.81</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$839.00</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$333.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$179.00</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$5,730.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$642.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$482.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

© 2026 MS
"""
