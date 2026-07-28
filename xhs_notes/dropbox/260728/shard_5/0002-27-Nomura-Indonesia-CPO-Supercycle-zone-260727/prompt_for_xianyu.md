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
EQUITY: AGRI-RELATED

## Supercycle zone

Continued inventory depletion to boost CPO prices

Production likely to be flat or decline

We believe global crude palm oil (CPO) production is either going to be stagnant or decline in the medium term, even without the Middle East war disruption. Our main thesis is CPO yield erosion will continue, as plantation age profile is heavily skewed towards older trees in Indonesia and Malaysia (which together account for \~85% of global CPO production, see Fig. 6). We think that Indonesia, as the largest producer globally, has been too slow in replanting its smallholder's plantation (small-scale farmers – 45% of Indonesia's total plantation area); at this acute stage, we believe cost incurred to rejuvenate smallholder farmers' plantations would be massive, given the large accumulated area. On top of that, there is a shortage of quality palm oil seeds, suggesting Indonesia's CPO production may suffer long-term production yield pressure, unless the government reopens large new plantation areas. We also believe the confiscated plantation lands under SOE might produce less harvest yields due to inefficient operations, given the lack of skilled manpower. Currently, the confiscated lands are close to 1mn ha, or an estimated \~8% of total Indonesia planted area. Additional production yield pressure would also come from expensive fertilizer prices as smallholder farmers are most likely to reduce fertilizer usage. The same might happen to other crops (i.e. soybean and sunflower), which would translate to a lower global vegetable oil yield as well. Moreover, El Nino – one of investors' biggest concerns and has been slowly strengthening towards 2H26F – could put further pressure on production, although we expect a lagged yield impact (i.e. to 2027F)

## Accelerating Biofuel expansion

Indonesia's biodiesel program is the biggest factor to influence global CPO prices as it has historically contributed $>65\%$ of global incremental CPO demand, according to USDA. We estimate Indonesia's B50 implementation will add $\sim 4\mathrm{mn}$ tons of demand (vs. 4.7mn tons estimated global demand in 2026F and 2027F), likely pushing CPO prices to new highs. We believe the Indonesia government might expand the biodiesel program to beyond B50 given its main goal is to eliminate diesel fuel imports. With narrowing spreads between biodiesel and diesel fuel, we believe the country's CPO fund budget can afford to subsidize B50 with a minimal levy hike. Conservatively, we assume CPO fund would need to raise the levy by another $2.5 - 5\%$ to run the B50 mandate, which is still accretive for upstream producers as CPO price hikes will compensate for a higher levy. Additional demand booster also comes from energy scarcity amid geopolitical tension, forcing more countries to accelerate biofuel blending such as Malaysia, Brazil, the Philippines, and the US (see Fig. 17-18). Therefore, demand for overall vegetable oils should structurally increase, in our view.

## Structurally high CPO prices

We believe CPO prices are entering a supercycle, with high prices sustaining in the long run, and likely even longer than the commodity boom cycle 15 years ago. We also believe CPO companies could generate higher profits and accumulate more cashflow than in the past. We forecast the average CPO Rotterdam price to reach USD1,412/ton in 2026F and USD1,497/ton in 2027F versus USD1,307/ton in 2025, and expect domestic prices to witness a similar rising trend.

Our view of a multiyear CPO price expansion is based on our assumptions that: 1) demand structurally would exceed supply – we estimate Indonesia and Malaysia total CPO inventory will reach <4mn tons in 2026/27F, the lowest in the past decade; 2) other vegetable oil prices would remain elevated, supporting CPO prices – driven by less

## Research Analysts

Indonesia Research Team
Raghavendra Divekar, CFA - NSM
raghavendra.divekar@NOM.com
+603 2027 6893

## Onshore expert

Sandy Ham (sandy.ham@verdhana.id),

Samuel Christian
(samuel.christian@verdhana.id),

Jody Wijaya (jody.wijaya@verdhana.id),

Nayla Yasmin
(nayla.yasmin@verdhana.id),

The onshore experts, who are employed by PT Verdhana Sekuritas Indonesia (“Verdhana”) and are not licensed outside Indonesia, have contributed to the content of this report under a partnership agreement between NOM and Verdhana.

Production Complete: 2026-07-27 09:01 UTC

fertilizer usage and higher biofuel blending amid geopolitical tension; and 3) no optimal substitute for CPO products.

## Top picks

In terms of top picks, we select CPO names that have: 1) high production yields; 2) low cash cost; and 3) improved dividend yield. Our top picks are in the order of Triputra Agro Persada (TAPG IJ [BUY – TP 2,500]; it has a high production yield, the lowest cash cost amongst peers, and the highest dividend yield in ASEAN) > Dharma Satya Nusantara (DSNG IJ [BUY – TP 2,100]; high production yield and deleveraging advantages) > London Sumatra Indonesia (LSIP IJ [BUY – TP 2,450]; has one of the cheapest valuations).

We value Indonesia plantation firms at an average 25% discount to peers in Malaysia, which we believe already reflected market concerns about export-agency uncertainty and the associated widened Indo-Malaysia CPO price discount; we therefore see these risks as highly priced in at current levels. On the export-governance front, we do not see the role of Danantara Sumberdaya Indonesia (DSI) (unlisted), Indonesia's export body that monitors exports and verifies agents, posing a material harm to the CPO ecosystem. We expect DSI to stay as a monitoring intermediary rather than becoming a sole trader, and we deem it unlikely to become a fully monopsony model to be enforced as it would risk disrupting trading activity, compressing local CPO prices, and inflicting losses on farmers, the knock-on effects of which would likely weigh on the Rupiah, widen Indonesia's trade deficit, and ultimately pressure the government's political standing. In a worst-case scenario (i.e. the government experiments with the sole trader model), we expect a period of turbulence, although we believe a quick policy correction would follow if damage to farmer incomes and the Rupiah becomes apparent.

Fig. 1: Stocks for action

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="2">Target Px (IDR)</td><td rowspan="2">Last Px (IDR)21-Jul</td><td rowspan="2">Upside(%)</td><td colspan="2">Target P/E (x)</td><td colspan="2">Implied P/E (x)</td></tr><tr><td>Old</td><td>New</td><td>Old</td><td>New</td><td>FY26F</td><td>FY27F</td></tr><tr><td>Triputra Agro Persada</td><td>TAPG IJ</td><td>Buy (~)</td><td>2,700</td><td>2,500 (▼)</td><td>1,610</td><td>55%</td><td>13.0</td><td>12.0 (▼)</td><td>7.6</td><td>6.9</td></tr><tr><td>Dharma Satya Nusantara</td><td>DSNG IJ</td><td>Buy (initiation)</td><td>-</td><td>2,100</td><td>1,230</td><td>71%</td><td>-</td><td>10.0</td><td>5.8</td><td>5.2</td></tr><tr><td>London Sumatera</td><td>LSIP IJ</td><td>Buy (initiation)</td><td>-</td><td>2,450</td><td>1,340</td><td>83%</td><td>-</td><td>8.0</td><td>4.4</td><td>4.2</td></tr></table>

Source: Bloomberg Finance L.P., company data, NOM estimates

## How we value Indonesia CPO stocks

We argue that CPO prices should rise higher than 2010-2020 levels as the current weakness in supply is more acute while demand from biodiesel continues to rise, which should push CPO prices into a strong upcycle. Moreover, other vegetable oil substitutes have similar supply and demand dynamics and should support CPO prices. Indeed, CPO prices have sustainably stayed above USD1,000/ton since 2023 (vs. an average cash cost of USD770/ton), delivering large profitability for CPO players. We use a conservative target multiple of 8-12x PE to value Indonesia CPO stocks, compared to 21x average ASEAN P/E in 2010-2020), also at a 25% discount to Malaysia CPO stocks on average, as we incorporate higher risks of potential unfavourable government policies and ESG discount. Our three preferred CPO stocks are TAPG > DSNG > LSIP.

We choose TAPG as our top pick, in view of its: 1) high productivity, backed by a relatively young plantation age profile of \~15 years old; 2) lowest cash cost among domestic listed companies, thanks to its operational excellence; and 3) has the highest dividend yield. The company has the capability to pay high dividend as it has largely completed its infrastructure buildout and is in a significant net cash position.

DSNG is our second pick. The company also has a similar plantation age profile, and hence is producing high output. The company is also gradually reducing debt, boosting its NPAT further. However, management is actively developing downstream businesses and accelerating its replanting program, which could put a cap on its dividend payout ratio.

Our third preferred stock is LSIP despite its older plantation age profile, but its cash cost remains very efficient compared to peers, in our view. Besides, we think LSIP's current valuation is inexpensive.

These three stocks are domestic CPO players, not exporters; thus, we believe it would be more relevant to use Indonesia final local CPO prices to analyze their businesses.

Downside risks to our investment views are mainly unfavourable government policies, especially if DSI (Indonesia export body) acts as sole trader. But we view this scenario as unlikely as a monopsony model is not feasible. Even if the government were to experiment on this model, it would only be temporary as the authorities will likely change the policy considering the significant damage inflicted on farmers income and the Rupiah. Therefore, in this report, we assume DSI would act only as an agent to monitor and supervise the sector.

Fig. 2: ASEAN CPO firms' operating cashflow (OCF) yield improvement aligns with CPO price movement  
![](images/3267f7db433958c4738306abc9eb98cdcc9b050a531c6038d2ccf6c5dd1e7d89.jpg)  
Source: Company data, NOM

Fig. 3: ASEAN CPO firms' valuation (P/E) versus CPO price  
![](images/d434062be8d3a37ae12d9fefe77c9b83bfd3b34321e34bc5baee099eab9d6a4e.jpg)  
Source: Company data, NOM

Fig. 4: CPO peer comparison  
Indonesia CPO stocks under our coverage have better growth and cheaper valuations than the regional peer average

<table><tr><td rowspan="2">Company</td><td rowspan="2">Bloomberg Ticker</td><td rowspan="2">M Cap US$ mn</td><td rowspan="2">Rating</td><td rowspan="2">Target Price LC</td><td rowspan="2">Last Price 21-Jul-26</td><td rowspan="2">Upside (%)</td><td colspan="2">NPAT Growth (%)</td><td colspan="2">P/E (x)</td><td colspan="2">P/B (x)</td><td colspan="2">ROE (%)</td><td colspan="2">Dividend Yield (%)</td></tr><tr><td>FY26F</td><td>FY27F</td><td>FY26F</td><td>FY27F</td><td>FY26F</td><td>FY27F</td><td>FY26F</td><td>FY27F</td><td>FY26F</td><td>FY27F</td></tr><tr><td colspan="17">Malaysia</td></tr><tr><td>SD Guthrie</td><td>SDG MK</td><td>11,144</td><td>Buy</td><td>7.20</td><td>6.59</td><td>9%</td><td>7%</td><td>2%</td><td>16.5</td><td>16.1</td><td>2.1</td><td>2.0</td><td>13.2</td><td>12.6</td><td>3.0</td><td>3.0</td></tr><tr><td>Johor Plantations Group</td><td>JPG MK</td><td>1,229</td><td>Buy</td><td>2.20</td><td>2.01</td><td>9%</td><td>-4%</td><td>-2%</td><td>15.5</td><td>15.5</td><td>1.6</td><td>1.5</td><td>10.8</td><td>10.1</td><td>3.5</td><td>3.5</td></tr><tr><td>IOI Corporation</td><td>IOI MK</td><td>6,901</td><td>Neutral</td><td>4.60</td><td>4.49</td><td>2%</td><td>1%</td><td>-1%</td><td>18.0</td><td>18.0</td><td>2.1</td><td>2.0</td><td>12.1</td><td>11.3</td><td>2.7</td><td>2.9</td></tr><tr><td>Kuala Lumpur Kepong</td><td>KLK MK</td><td>5,730</td><td>Neutral</td><td>24</td><td>21.02</td><td>14%</td><td>79%</td><td>8%</td><td>15.8</td><td>14.7</td><td>1.6</td><td>1.5</td><td>10.1</td><td>10.4</td><td>3.8</td><td>4.3</td></tr><tr><td>Genting Plantations</td><td>GENP MK</td><td>1,250</td><td>Not Rated</td><td>na</td><td>5.70</td><td>na</td><td>2%</td><td>0%</td><td>14.1</td><td>14.0</td><td>1.0</td><td>0.9</td><td>7.1</td><td>6.9</td><td>4.2</td><td>4.4</td></tr><tr><td>Sarawak Oil Palms</td><td>SOP MK</td><td>1,138</td><td>Not Rated</td><td>na</td><td>5.12</td><td>na</td><td>8%</td><td>2%</td><td>9.5</td><td>9.3</td><td>1.0</td><td>0.9</td><td>11.2</td><td>10.6</td><td>3.4</td><td>3.5</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td>15.2%</td><td>1.6%</td><td>14.9</td><td>14.6</td><td>1.6</td><td>1.5</td><td>10.7</td><td>10.3</td><td>3.4</td><td>3.6</td></tr><tr><td colspan="17">Singapore</td></tr><tr><td>Wilmar International</td><td>WIL SP</td><td>18,927</td><td>Neutral</td><td>3.50</td><td>3.91</td><td>-10%</td><td>11%</td><td>11%</td><td>12.1</td><td>11.2</td><td>1.1</td><td>1.1</td><td>7.1</td><td>7.6</td><td>5.6</td><td>6.0</td></tr><tr><td>First Resources</td><td>FR SP</td><td>4,309</td><td>Not Rated</td><td>na</td><td>3.59</td><td>na</td><td>9%</td><td>2%</td><td>12.3</td><td>12.4</td><td>3.0</td><td>2.7</td><td>22.6</td><td>21.5</td><td>5.5</td><td>6.0</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td>10.2%</td><td>6.8%</td><td>12.2</td><td>11.8</td><td>2.0</td><td>1.9</td><td>14.8</td><td>14.6</td><td>5.5</td><td>6.0</td></tr><tr><td colspan="17">Indonesia</td></tr><tr><td>Triputra Agro Persada</td><td>TAPG IJ</td><td>1,793</td><td>Buy</td><td>2,500</td><td>1,610</td><td>55%</td><td>13%</td><td>11%</td><td>7.6</td><td>6.9</td><td>2.7</td><td>2.6</td><td>36.5</td><td>38.6</td><td>13.0</td><td>14.3</td></tr><tr><td>Dharma Satya Nusantara</td><td>DSNG IJ</td><td>723</td><td>Buy</td><td>2,100</td><td>1,230</td><td>71%</td><td>21%</td><td>11%</td><td>5.8</td><td>5.2</td><td>1.0</td><td>0.9</td><td>18.0</td><td>17.5</td><td>5.1</td><td>6.7</td></tr><tr><td>London Sumatera</td><td>LSIP IJ</td><td>513</td><td>Buy</td><td>2,450</td><td>1,340</td><td>83%</td><td>11%</td><td>5%</td><td>4.4</td><td>4.2</td><td>0.6</td><td>0.5</td><td>14.1</td><td>13.5</td><td>6.9</td><td>7.2</td></tr><tr><td>Astra Agro Lestari</td><td>AALI IJ</td><td>697</td><td>Not Rated</td><td>na</td><td>6,450</td><td>na</td><td>9%</td><td>4%</td><td>7.2</td><td>6.9</td><td>0.5</td><td>0.5</td><td>6.7</td><td>5.7</td><td>5.6</td><td>5.5</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td>13.4%</td><td>7.7%</td><td>6.3</td><td>5.8</td><td>1.2</td><td>1.1</td><td>18.8</td><td>18.8</td><td>7.6</td><td>8.4</td></tr></table>

Note: Bloomberg consensus estimates for Not rated stocks  
Source: Bloomberg Finance L.P., NOM estimates

Fig. 5: CPO companies cash cost comparison (USD/ton) (2025)  
TAPG has most efficient cash cost owing to operational excellence and productive yield.  
![](images/8d8a2e9f29e2a4dcba26ac5024bc3975cc5b3aac013973108f4fde7ae544a198.jpg)  
Source: Company data, NOM

## Risks that could undermine our thesis

\- Assigning DSI as a sole trader can disrupt the supply chain of the CPO industry, such as weakening local CPO prices significantly. In terms of operation, we believe implementing a monopsony model in the CPO industry will bring extreme high risks, given lack of capability in terms of human resources, infrastructures, and capital. Politically, it also produces additional complexity as there are many conflicts of interests and law enforcements issues. An instant implementation of a sole trader model would immediately destroy local CPO prices as export trading activities will deteriorate in a rapid pace, resulting in massive losses for farmers, and at the same time damage government popularity significantly, in our view. This policy will also widen trade deficit considerably, as well as weaken the Rupiah and Indonesia's fiscal position. All in all, we think the total damage would be too big. That said, logicall

[中间内容因长度限制已省略]

Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE

BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://no-NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities Malaysia Sdn. Bhd., Malaysia. All rights reserved.
"""
