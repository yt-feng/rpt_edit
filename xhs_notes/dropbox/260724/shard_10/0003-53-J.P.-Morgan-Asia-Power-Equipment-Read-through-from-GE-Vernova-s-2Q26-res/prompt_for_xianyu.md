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
# JPM

# Asia Power Equipment

## Read-through from GE Vernova's 2Q26 results

While GE Vernova (GEV.US; covered by Mark Strouse, OW) reported robust new-order growth and strong operating trends, the shares were down pre-market at the time of writing, alongside peers such as Siemens Energy, potentially reflecting concerns that gas-turbine order wins are nearing a plateau and end-of-decade oversupply risk (see note by our European Capital Goods analyst). Yet our Capital Goods analyst highlighted the strong conversion of GEV's slot reservations into orders, with demand/supply fundamentals healthy through the end of the decade, and management also said on the call that they see a clear pathway to grow turbine orders into 2027. Electrification momentum remains strong, with \~30% organic revenue growth YoY and \~4ppt EBITDA margin expansion; management cited substantial growth in switchgear, substations, transformers, and HVDC equipment, and expects 3Q EBITDA margin to expand sequentially. Data-center orders were exceptionally strong at US\$5bn (\~2x FY25), suggesting demand remains robust despite project-delay concerns. Overall, the results—especially Electrification—reinforce our positive view on order wins, margin expansion, and the data-center opportunity for transmission equipment; we maintain our positive stance on Asian names, with top picks including Hyosung Heavy, Hyundai Electric, and Wasion Holdings.

\- Summary of 2Q26 results: GEV reported 2Q pro forma EBITDA about 3% below consensus and revenue about 3% above expectations. The slight EBITDA miss was driven by lower-than-expected profitability at Wind and higher unallocated corporate costs during the quarter, while the core Power and Electrification segments beat. 2Q orders of \$24.2bn were above expectations, driven by Power segment orders of \$16.7bn and a modest beat from Electrification orders of \$6.3bn. See our U.S. Clean Energy analyst's First Take on the company (note). Power segment: New gas power contracts signed were approximately 20GW, above the 10–15GW guided by management and above the high-teens buy-side expectations we had heard going into the print. GEV now expects to end FY26 with at least 125GW of gas power backlog plus SRA, up from at least 110GW previously. The company also announced that the expansion to 20GW of gas power capacity is complete and that it remains on track for 24GW in FY28. Additionally, management noted it is utilizing lean and incremental machinery within the existing factory footprint to reach 30GW by 2030. Please see Table 4for the change in guidance.

\- Why the power equipment stocks slide post GEV results? Our EU Capital analyst attributed this to two reasons in his note on Siemens Energy (note). (1) On new order wins for gas turbines: The analyst notes that, of GEV's 20GW of new gas turbine orders this quarter, 18GW were slot reservation agreements and 2GW were new firm orders, which could be interpreted as “less firm” at first glance. But he argues this framing is misleading. He highlighted that GEV converted 10GW of slot reservation agreements into firm orders this quarter, implying total firm intake of 12GW (10+2), or \~3.7x quarterly deliveries. He adds that the backlog increased from 44GW to 53GW and slot reservations rose from 56GW to 63GW, which he views as consistent with strong demand relative to supply. (2) On capacity expansion for gas turbines: Our EU Capital Good analyst notes that GEV has raised capacity guidance to 30GW by 2030 versus 26GW by 2028 (incl. aeroderivatives). He views this as

See page 6 for analyst certification and important disclosures, including non-US analyst disclosures.

Power Equipment and Utilities

Stephen Tsui, CFA AC
(852) 2800-8592
stephen.tsui@JPM.com

Vento Suen

(852) 2800-8546

vento.suen@JPM.com

Alan Hon
(852) 2800-8573
alan.hon@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

incremental and not surprising given prior commentary on efficiency-driven output gains, though he says it has revived end-decade over-supply concerns. He estimates global supply vs. orders: FY24 \~50GW vs \~57GW; FY25 \~55GW vs \~100GW; FY26 \~64GW vs \~115–120GW; FY27 \~70GW vs \~110–120GW; FY28 \~80GW vs \~110–120GW. By FY30 he sees 90–95GW+ supply, with backlogs and pricing still supportive.

\- Gas turbine orders are not peaking this year: Management mentioned during the earnings call that they see a very clear pathway to continue growing their contracted GW on order beyond this year. While they are guiding for 125GW this year, they are confident that they will see very healthy growth above 125 gigawatts in '27 relative to year end '26. And they are very clearly continuing to grow the contracted backlog for the better part of the next six quarters.

\- Momentum remains strong for the electrification segment: The electrification segment posted 64% revenue growth to US\$3.6bn in 2Q26 (29% if we exclude the impact from the acquisition of Prolec), and more than a doubling of EBITDA to \$671mn. EBITDA margin expanded by almost 4ppt yoy to 18.4%, while orders remained strong at 1.7x of revenue and reached \$6.3bn in 2Q26 (+66%). The company guided to modest EBITDA margin expansion sequentially. Management raised its full-year revenue guidance to \$14.5-15bn (vs 14-14.5bn). Management noted strength across products with substantial growth in switchgear, substations, transformers and HVDC equipment. We believe the strong orders and margin expansion of GEV show the cycle of HV transmission equipment is ongoing in the U.S. This should have a positive read-through to the Asian names, particularly the Korean power equipment names that will report results in the next two weeks.

US\$5bn of data center orders in 1H26, 2x FY25 level: The company booked \$2.7 billion of data center orders in electrification, bringing total segment data center orders to over \$5 billion in the first half of '26 (\~35%+ of the total \$14bn of orders), more than double the full-year 25 level. The company offers a wide range of products to DCs, including power generation equipment, software and controls (like EMS solutions). The company guided to \$300 million directional scope per gigawatt today, while they see upside to the number if the company launches more new products like medium voltage UPS, solid state transformers and others (entitlement could be 2-3x what their scope oper GW is today). Overall, we believe GEV's strong DC orders show that transmission equipment is not just coming from regulated utilities/grids, while DCs (for both front-of-the-meter and behind-the-meter generation) also post strong demand. Note that Hyundai Electric and Hyosung Heavy only had \~10% of new orders from data centers, and we expect a higher portion of DC orders in the upcoming 2Q results.

\- More progress on solid-state transformers: GEV has completed the build-out of 5-MW SST prototype for indoor applications that will be delivered to their first hyperscaler later this year and, in parallel, have started development of a 6-megawatt SST for outdoor applications. Orders may come as early as 2027. For the latest SST developments in China, please refer to our expert call takeaway note.

Figure 1: Backlog + SRAs GW  
![](images/1e4b54a2d40c06544a7c358d0a502e8f16ee4ea90fb7e690a7075d2cf140bf9d.jpg)  
■ Firm Order Backlog ■ Slot Reservation Agreements

Source: JPM, Company Reports  
Table 1: GEV 2Q Results

<table><tr><td>(in $ Millions except per share)</td><td>2Q26Actual</td><td>2Q26JPMe</td><td>Actual vs JPMe</td><td>2Q26 Street</td><td>Actual vs Street</td></tr><tr><td colspan="6">Financials</td></tr><tr><td>Power revenue</td><td>5,477</td><td>5,529</td><td>-1%</td><td>5,556</td><td>-1%</td></tr><tr><td>y/y growth</td><td>15.1%</td><td>16.2%</td><td></td><td>16.8%</td><td></td></tr><tr><td>Wind revenue</td><td>2,026</td><td>1,906</td><td>6%</td><td>1,870</td><td>8%</td></tr><tr><td>y/y growth</td><td>-9.8%</td><td>-15.1%</td><td></td><td>-16.7%</td><td></td></tr><tr><td>Electrification revenue</td><td>3,637</td><td>3,489</td><td>4%</td><td>3,379</td><td>8%</td></tr><tr><td>y/y growth</td><td>65.2%</td><td>58.5%</td><td></td><td>53.5%</td><td></td></tr><tr><td>Intersegment revenue</td><td>-36</td><td>-102</td><td></td><td>20</td><td></td></tr><tr><td>Total revenue</td><td>11,104</td><td>10,821</td><td>3%</td><td>10,825</td><td>3%</td></tr><tr><td>y/y growth</td><td>21.9%</td><td>18.8%</td><td></td><td>18.8%</td><td></td></tr><tr><td>Power PF EBITDA</td><td>1,031</td><td>1,000</td><td>3%</td><td>992</td><td>4%</td></tr><tr><td>Power PF EBITDA Margin</td><td>18.8%</td><td>18.1%</td><td></td><td>17.9%</td><td></td></tr><tr><td>Wind PF EBITDA</td><td>-275</td><td>-255</td><td>-8%</td><td>-248</td><td>-11%</td></tr><tr><td>Wind PF EBITDA Margin</td><td>-13.6%</td><td>-13.4%</td><td></td><td>-13.2%</td><td></td></tr><tr><td>Electrification PF EBITDA</td><td>671</td><td>646</td><td>4%</td><td>610</td><td>10%</td></tr><tr><td>Electrification PF EBITDA Margin</td><td>18.4%</td><td>18.5%</td><td></td><td>18.0%</td><td></td></tr><tr><td>Other PF EBITDA</td><td>-177</td><td>-128</td><td>-38%</td><td>-123</td><td>-44%</td></tr><tr><td>Total PF EBITDA</td><td>1,250</td><td>1,263</td><td>-1%</td><td>1,290</td><td>-3%</td></tr><tr><td>Total PF EBITDA Margin</td><td>11.3%</td><td>11.7%</td><td></td><td>11.9%</td><td></td></tr><tr><td>Total FCF</td><td>5,107</td><td>1,007</td><td>407%</td><td>1,299</td><td>293%</td></tr></table>

Source: JPM estimates, Company Reports

Table 2: GEV Electrification Key Performance Metrics US\$mn

<table><tr><td colspan="5">Orders</td></tr><tr><td>US$mn</td><td>1Q&#x27;25</td><td>2Q&#x27;25</td><td>1Q&#x27;26</td><td>2Q&#x27;26</td></tr><tr><td>Equipment</td><td>2,808</td><td>2,746</td><td>6,421</td><td>5,667</td></tr><tr><td>Services</td><td>557</td><td>537</td><td>691</td><td>680</td></tr><tr><td>Total Orders</td><td>3,366</td><td>3,283</td><td>7,112</td><td>6,347</td></tr><tr><td>y/y % (organic)</td><td></td><td></td><td></td><td></td></tr><tr><td>Equipment</td><td></td><td></td><td>99%</td><td>72%</td></tr><tr><td>Services</td><td></td><td></td><td>18%</td><td>31%</td></tr><tr><td>Total Orders</td><td></td><td></td><td>86%</td><td>66%</td></tr><tr><td>US$mn</td><td>1Q&#x27;25 YTD</td><td>2Q&#x27;25 YTD</td><td>1Q&#x27;26 YTD</td><td>2Q&#x27;26 YTD</td></tr><tr><td>Equipment</td><td>2,808</td><td>5,555</td><td>6,421</td><td>12,089</td></tr><tr><td>Services</td><td>557</td><td>1,094</td><td>691</td><td>1,371</td></tr><tr><td>Total Orders</td><td>3,366</td><td>6,649</td><td>7,112</td><td>13,460</td></tr><tr><td>y/y % (organic)</td><td></td><td></td><td></td><td></td></tr><tr><td>Equipment</td><td></td><td></td><td>99%</td><td>85%</td></tr><tr><td>Services</td><td></td><td></td><td>18%</td><td>25%</td></tr><tr><td>Total Orders</td><td></td><td></td><td>86%</td><td>76%</td></tr><tr><td colspan="5">Segment Revenues and EBITDA</td></tr><tr><td>US$mn</td><td>1Q&#x27;25</td><td>2Q&#x27;25</td><td>1Q&#x27;26</td><td>2Q&#x27;26</td></tr><tr><td>Power Transmission</td><td>692</td><td>759</td><td>1,380</td><td>1,877</td></tr><tr><td>Grid Systems Integration</td><td>390</td><td>579</td><td>691</td><td>806</td></tr><tr><td>Power Conversion &amp; Storage</td><td>381</td><td>411</td><td>477</td><td>539</td></tr><tr><td>Grid Automation &amp; Software</td><td>378</td><td>412</td><td>411</td><td>416</td></tr><tr><td>Total Segment Revenues</td><td>1,840</td><td>2,162</td><td>2,959</td><td>3,637</td></tr><tr><td>Equipment</td><td>1,391</td><td>1,673</td><td>2,501</td><td>3,130</td></tr><tr><td>Services</td><td>448</td><td>488</td><td>459</td><td>507</td></tr><tr><td>Total Segment Revenues</td><td>1,840</td><td>2,162</td><td>2,959</td><td>3,637</td></tr><tr><td>Segment EBITDA</td><td>205</td><td>314</td><td>528</td><td>671</td></tr><tr><td>Segment EBITDA margin</td><td>11.1%</td><td>14.5%</td><td>17.8%</td><td>18.4%</td></tr><tr><td>y/y (organic)</td><td></td><td></td><td></td><td></td></tr><tr><td>Equipment</td><td></td><td></td><td>39%</td><td>36%</td></tr><tr><td>Services</td><td></td><td></td><td>-5%</td><td>6%</td></tr><tr><td>Total Segment Revenues</td><td></td><td></td><td>29%</td><td>29%</td></tr><tr><td>Segment EBITDA margin</td><td></td><td></td><td>590 bps</td><td>700bps</td></tr><tr><td>US$mn</td><td>1Q&#x27;25 YTD</td><td>2Q&#x27;25 YTD</td><td>1Q&#x27;26 YTD</td><td>2Q&#x27;26 YTD</td></tr><tr><td>Power Transmission</td><td>692</td><td>1,451</td><td>1,380</td><td>3,256</td></tr><tr><td>Grid Systems Integration</td><td>390</td><td>968</td><td>691</td><td>1,497</td></tr><tr><td>Power Conversion &amp; Storage</td><td>381</td><td>792</td><td>477</td><td>1,016</td></tr><tr><td>Grid Automation &amp; Software</td><td>378</td><td>790</td><td>411</td><td>827</td></tr><tr><td>Total Segment Revenues</td><td>1,840</td><td>4,001</td><td>2,959</td><td>6,597</td></tr><tr><td>Equipment</td><td>1,391</td><td>3,065</td><td>2,501</td><td>5,631</td></tr><tr><td>Services</td><td>448</td><td>937</td><td>459</td><td>966</td></tr><tr><td>Total Segment Revenues</td><td>1,840</td><td>4,001</td><td>2,959</td><td>6,597</td></tr><tr><td>Segment EBITDA</td><td>205</td><td>519</td><td>528</td><td>1,200</td></tr><tr><td>Segment EBITDA margin</td><td>11.1%</td><td>13.0%</td><td>17.8%</td><td>18.2%</td></tr><tr><td>y/y (organic)</td><td></td><td></td><td></td><td></td></tr><tr><td>Equipment</td><td></td><td></td><td>39%</td><td>37%</td></tr><tr><td>Services</td><td></td><td></td><td>-5%</td><td>1%</td></tr><tr><td>Total Segment Revenues</td><td></td><td></td><td>29%</td><td>29%</td></tr><tr><td>Segment EBITDA margin</td><td></td><td></td><td>590 bps</td><td>650bps</td></tr></table>

Source: Company data, JPM.

Table 3: Financials of Power and Electrification Segments US\$ mn

<table><tr><td>US$ mn</td><td>1Q&#x27;25</td><td>2Q&#x27;25</td><td>3Q&#x27;25</td><td>4Q&#x27;25</td><td>1Q&#x27;26</td><td>2Q&#x27;26</td><td>2Q&#x27;26 y/y % (organic)</td></tr><tr><td colspan="8">Power</td></tr><tr><td>Segment Revenue</td><td>4,449</td><td>4,785</td><td>4,863</td><td>5,776</td><td>4,971</td><td>5,477</td><td>14%</td></tr><tr><td>Equipment</td><td>1,491</td><td>1,504</td><td>1,744</td><td>1,946</td><td>1,885</td><td>1,965</td><td>30%</td></tr><tr><td>Services</td><td>2,958</td><td>3,280</td><td>3,119</td><td>3,830</td><td>3,086</td><td>3,512</td><td>7%</td></tr><tr><td>Segment EBITDA</td><td>517</td><td>785</td><td>651</td><td>982</td><td>811</td><td>1,031</td><td></td></tr><tr><td>Segment EBITDA margin</td><td>11.6%</td><td>16.4%</td><td>13.4%</td><td>17.0%</td><td>16.3%</td><td>18.8%</td><td>320bps</td></tr><tr><td colspan="8">Electrification</td></tr><tr><td>Segment Revenue</td><td>1,840</td><td>2,162</td><td>2,565</td><td>2,921</td><td>2,959</td><td>3,637</td><td>29%</td></tr><tr><td>Equipment</td><td>1,391</td><td>1,673</td><td>2,035</td><td>2,279</td><td>2,501</td><td>3,130</td><td>36%</td></tr><tr><td>Services</td><td>448</td><td>488</td><td>530</td><td>642</td><td>459</td><td>507</td><td>6%</td></tr><tr><td>Segment EBITDA</td><td>205</td><td>314</td><td>387</td><td>494</td><td>528</td><td>671</td><td></td></tr><tr><td>Segment EBITDA margin</td><td>11.1%</td><td>14.5%</td><td>15.1%</td><td>16.9%</td><td>17.8%</td><td>18.4%</td><td>700bps</td></tr></table>

Source: Company data, JPM.

Table 4: GEV Guidance

<table><tr><td></td><td>April 22 Guidance</td><td>July 22 Guidance</td></tr><tr><td colspan="3">GE Vernova</td></tr><tr><td>Total Revenue</td><td>$44.5B-$45.5B</td><td>$45.5B-$46.5B</td></tr><tr><td>Adjusted EBITDA Margin</td><td>12%-14%</td><td>12%-14%</td></tr><tr><td>Free Cash Flow</td><td>$6.5B-$7.5B</td><td>$11.5B-$12.5B</td></tr><tr><td colspan="3">Power</td></tr><tr><td>Organic Revenue Growth</td><td>16%-18%</td><td>18%-20%</td></tr><tr><td>Segmen

[中间内容因长度限制已省略]

ent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All

Completed 23 Jul 2026 12:41 AM HKT
"""
