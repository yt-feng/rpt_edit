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
EQUITY: TECHNOLOGY

# More positive narratives about optical Quick Note

## 3Q26E revenue guidance lower but GM in line; maintain Neutral

Win Semi reported in-line 2Q26 GM of $28.2\%$ (vs. guidance of high-20%; standalone GM was $32.6\%$ ) with fab utilization rate improving to $65\%$ from $60\%$ in 1Q26. A strong opex control (14% of revenue) drove OPM up to $14.1\%$ and an earnings beat (Fig. 1). Management expects low-teens q-q revenue growth in 3Q26E with GM at low-30% (Fig. 2), believing optical will lead sequential growth in 3Q26E, followed by infrastructure, while cellular and Wi-Fi will be flat to slightly up. A richer product mix given that infrastructure revenue has risen to levels similar to that of cellular and falling depreciation (c.TWD700-800mn per quarter) remain the near-term drivers to Win Semi's GM improvements, in our view, and the company continues to deliver decent executions on both ends. During the earnings call, we think management was more optimistic, delivering a firm tone about its optical foundry business progress. The stock currently trades at 29x 2027F EPS or 3.1x 2027F BVPS. We are currently reviewing our earnings model.

## More positive developments in the optical foundry

Optical foundry booked the most significant q-q revenue growth in 2Q26 as photodetector (PD) started volume production for a major customer in the latter part of the quarter. Management expects greater demand volume into 3Q26E, and a customer provides a very upbeat demand forecast. Although Win Semi currently only has one strategic customer in the PD production, it is already busy meeting the demand and is not worried about the lack of other customers at this moment. On the laser front, the company has had vertical-cavity surface-emitting laser (VCSEL) and electro-absorption modulated laser (EML; long-haul) in production and will add mid-haul EML to the lineup in 2H26 and initial contribution from CW laser in 2H27. Management estimates high single-digit % of revenue from optical communication in 2026E with potential to move toward double-digits % in 2027E.

## Inventory balance increases to prepare for production ramp-up

Win Semi exited the quarter with TWD7.6bn of inventory (+48% q-q), and the company attributes most of the growth to raw material and chemical preparation in response to geopolitical uncertainty (e.g. export controls) and supply chain security amid the Middle East conflicts, ahead of peak seasonality. It also has entered into long-term agreements (LTAs) for critical materials to reduce supply chain risks, and works with the PD customers to secure substrate supply together.

## Satellite revenue contribution also on a growth trajectory

Win Semi notes that it serves satellite communications with GaAs and GaN technologies for power amplifiers (PA) and low-noise amplifiers (LNA) on the constellation as well as ground gateways. Within infrastructure, it estimates that current contributions from satellites and base stations are broadly commensurate. We gave an update on the low earth orbit (LEO) radio frequency (RF) supply chain in our Global Satellite anchor report, and flagged that a fast-growing satellite business in 2026-27F could continue to steer a favorable product mix for Win Semi, if SpaceX's (SPCX US, Not rated) commitment prevails (report).

26 July 2026

<table><tr><td>Rating Remains</td><td>Neutral</td></tr><tr><td>Target price Remains</td><td>TWD 590.00</td></tr><tr><td>Closing price 24 July 2026</td><td>TWD 341.50</td></tr></table>

## Research Analysts

Aaron Jeng, CFA - NITB
aaron.jeng@NOM.com
+886(2) 21769962

Eric Chen, CFA - NITB
eric.chen@NOM.com
+886(2) 21769965

Vivian Yang - NITB
vivian.yang@NOM.com
+886(2) 21769970

Fig. 1: Win Semi's 2Q26 results vs NOM forecasts and Bloomberg consensus

<table><tr><td rowspan="2">(TWD mn)</td><td colspan="8">2Q26</td></tr><tr><td>Actual</td><td>q-q</td><td>NMR</td><td>q-q</td><td>Diff.</td><td>BBG</td><td>q-q</td><td>Diff.</td></tr><tr><td>Revenue</td><td>5,257</td><td>14.5%</td><td>5,276</td><td>14.9%</td><td>-0.4%</td><td>5,298</td><td>15.4%</td><td>-0.8%</td></tr><tr><td>Gross profit</td><td>1,485</td><td>22.8%</td><td>1,484</td><td>22.8%</td><td>0.0%</td><td>1,550</td><td>28.2%</td><td>-4.2%</td></tr><tr><td>- Opex</td><td>(743)</td><td>-4.5%</td><td>(868)</td><td>11.6%</td><td>-14.4%</td><td>(845)</td><td>8.6%</td><td>-12.1%</td></tr><tr><td>Operating profit</td><td>742</td><td>72.2%</td><td>617</td><td>43.0%</td><td>20.3%</td><td>705</td><td>63.5%</td><td>5.3%</td></tr><tr><td>Pretax profit</td><td>1,188</td><td>123.4%</td><td>522</td><td>-1.9%</td><td>127.6%</td><td>717</td><td>34.8%</td><td>65.7%</td></tr><tr><td>Net profit</td><td>977</td><td>83.1%</td><td>525</td><td>-1.6%</td><td>86.1%</td><td>656</td><td>23.1%</td><td>48.8%</td></tr><tr><td>EPS (TWD)</td><td>2.30</td><td>83.1%</td><td>1.24</td><td>-1.6%</td><td>86.1%</td><td>1.51</td><td>20.0%</td><td>52.6%</td></tr><tr><td>Margin</td><td>Actual</td><td></td><td>NMR</td><td></td><td>Diff.</td><td>BBG</td><td></td><td>Diff.</td></tr><tr><td>Gross margin</td><td>28.2%</td><td></td><td>28.1%</td><td></td><td>11bps</td><td>29.3%</td><td></td><td>-101bps</td></tr><tr><td>- Opex ratio</td><td>-14.1%</td><td></td><td>-16.4%</td><td></td><td>232bps</td><td>-16.0%</td><td></td><td>182bps</td></tr><tr><td>Operating margin</td><td>14.1%</td><td></td><td>11.7%</td><td></td><td>243bps</td><td>13.3%</td><td></td><td>81bps</td></tr><tr><td>Pretax margin</td><td>22.6%</td><td></td><td>9.9%</td><td></td><td>1,271bps</td><td>13.5%</td><td></td><td>907bps</td></tr><tr><td>Net margin</td><td>18.6%</td><td></td><td>9.9%</td><td></td><td>863bps</td><td>12.4%</td><td></td><td>619bps</td></tr></table>

Source: Company data, Bloomberg Finance L.P. consensus, NOM estimates

Fig. 2: Win Semi's 3Q26E guidance vs NOM forecasts and Bloomberg consensus

<table><tr><td colspan="10">3Q26E</td></tr><tr><td>(TWD mn)</td><td>Guidance</td><td>q-q</td><td>NMR</td><td>q-q</td><td>Diff.</td><td>BBG</td><td>q-q</td><td>Diff.</td><td>Remarks</td></tr><tr><td>Revenue</td><td>5,888</td><td>12.0%</td><td>6,200</td><td>17.5%</td><td>-5.0%</td><td>5,655</td><td>6.7%</td><td>4.1%</td><td>Up low-teens q-q</td></tr><tr><td>Gross profit</td><td>1,884</td><td>26.9%</td><td>1,974</td><td>33.0%</td><td>-4.5%</td><td>1,772</td><td>14.4%</td><td>6.3%</td><td></td></tr><tr><td>- Opex</td><td></td><td></td><td>(879)</td><td>1.3%</td><td></td><td>(882)</td><td>4.3%</td><td></td><td></td></tr><tr><td>Operating profit</td><td></td><td></td><td>1,094</td><td>77.5%</td><td></td><td>891</td><td>26.4%</td><td></td><td></td></tr><tr><td>Pretax profit</td><td></td><td></td><td>1,000</td><td>91.6%</td><td></td><td>923</td><td>28.8%</td><td></td><td></td></tr><tr><td>Net profit</td><td></td><td></td><td>921</td><td>75.6%</td><td></td><td>815</td><td>24.2%</td><td></td><td></td></tr><tr><td>EPS (TWD)</td><td></td><td></td><td>2.17</td><td>75.6%</td><td></td><td>1.87</td><td>23.9%</td><td></td><td></td></tr><tr><td>Margin</td><td>Guidance</td><td></td><td>NMR</td><td></td><td>Diff.</td><td>BBG</td><td></td><td>Diff.</td><td>Remarks</td></tr><tr><td>Gross margin</td><td>32.0%</td><td></td><td>31.8%</td><td></td><td>17bps</td><td>31.3%</td><td></td><td>66bps</td><td>Low-30%</td></tr><tr><td>- Opex ratio</td><td></td><td></td><td>-14.2%</td><td></td><td></td><td>-15.6%</td><td></td><td></td><td></td></tr><tr><td>Operating margin</td><td></td><td></td><td>17.7%</td><td></td><td></td><td>15.7%</td><td></td><td></td><td></td></tr><tr><td>Pretax margin</td><td></td><td></td><td>16.1%</td><td></td><td></td><td>16.3%</td><td></td><td></td><td></td></tr><tr><td>Net margin</td><td></td><td></td><td>14.9%</td><td></td><td></td><td>14.4%</td><td></td><td></td><td></td></tr></table>

Source: Company data, Bloomberg Finance L.P. consensus, NOM estimates

Fig. 3: Win Semi - revenue mix

<table><tr><td></td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td>Cellular</td><td>45-50%</td><td>40-45%</td><td>35-40%</td><td>25-30%</td><td>30-35%</td><td>30-35%</td><td>30-35%</td><td>25-30%</td><td>30-35%</td><td>30-35%</td></tr><tr><td>Wi-Fi</td><td>10-15%</td><td>15-20%</td><td>15-20%</td><td>10-15%</td><td>10-15%</td><td>15-20%</td><td>15-20%</td><td>15-20%</td><td>15-20%</td><td>10-15%</td></tr><tr><td>Infrastructure</td><td>20-25%</td><td>25-30%</td><td>25-30%</td><td>35-40%</td><td>30-35%</td><td>30-35%</td><td>30-35%</td><td>30-35%</td><td>30-35%</td><td>30-35%</td></tr><tr><td>Optical &amp; Others</td><td>15%</td><td>12%</td><td>16%</td><td>21%</td><td>17%</td><td>13%</td><td>16%</td><td>17%</td><td></td><td></td></tr><tr><td>Optical</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5-10%</td><td>10-15%</td></tr><tr><td>Others</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>6%</td><td>5%</td></tr></table>

Source: Company data, NOM

## Win Semi: 1Q26 analyst briefing summary

## Below comments are from Win Semi's management, unless otherwise stated:

## Results summary

• Revenue was TWD5.257bn (+15% q-q, +39% y-y) vs. guidance of mid-teens q-q growth.

\- Consolidated GM was $28.2\%$ (vs guidance of high-20s), down from $26.3\%$ in 1Q26. Product mix improvement, shipment growth and initial dilution from new product ramp together affected GM; standalone GM was $32.6\%$ (+0.5pp q-q).

Foundry UTR was $65\%$ in 2Q26 vs. $60\%$ in 1Q26.

Depreciation was TWD760mn. As Win Semi re-initiated project spendings from 2H25, management does not expect further significant drop in depreciation.

\- Capex was TWD129mn (re-initiated project-based spending from 2H25). Maintains full-year capex budget of TWD2-3bn.

\- OPM increased to $14.1\%$ in 2Q26 from $9.4\%$ in 1Q26. Opex ratio was down to $14\%$ in 2Q26 from $17\%$ in 1Q26.

\- <TWD800mn/quarter in 1H26.

\- Non-operating gain was TWD447mn in 2Q26, including FX gains of TWD144mn and interest expense TWD143mn.

• 2Q26 revenue mix

• Cellular (30-35% of revenue)

Infrastructure (30-35%)

Wi-Fi (10-15%)

Optical (10-15%)

Others (5%)

• 3Q26E guidance

Consolidated revenue to grow low-teens q-q.

Consolidated GM in low-30s.

## Management remarks

\- Router demand was soft in 2Q26 and shipments were down q-q. Other applications saw growth q-q.

\- Cellular PA momentum picked up further in 2Q26 given that smartphones would be entering traditional high season. Cellular was up single-digit q-q.

\- Infrastructure benefited from data center and aerospace demand, with decent q-q growth.

\- Optical had new applications entering production in late-2Q26. Optical had the most significant q-q growth among all applications.

\- High-margin infrastructure revenue mix is now on par with cellular. Optical also had good growth.

\- Memory shortage and some material price inflation could lead to uncertainty in smartphone demand during the peak season but Win Semi focuses on the mid-/high-tier Android and iOS. Cellular and Wi-Fi PA demand do not see much difference in pull-in momentum vs. prior years at Win Semi. But management thinks it has to monitor the sell-through status after product launches.

\- Win Semi has extended GaAs pHEMT and GaN to low-earth orbit and other aerospace applications. Win Semi plays an important role in satellite communication, regardless of which camps.

\- In AI data centers, Win Semi gradually has a more comprehensive portfolio of GaAs/InP driver IC and optical laser.

\- US and Android high-end handset model launches in 3Q26 and new optical communication applications for data centers will be driving revenue growth in 3Q26.

## Q&A

## - Outlook

Optical will lead growth in 3Q26, followed by Infrastructure given Win Semi's aerospace clientele. Cellular and Wi-Fi will be flat to up slightly.

## • Optical communication

\- AI revenue was primarily driver IC last year and AI made up low single-digit % of revenue last year. With more optical projects entering mass production, AI made up high single-digit % of revenue (multiple times y-y growth). Management expects sequential growth into 2H26E.

\- Thinks optical communication revenue will move toward double-digit % of revenue in 2027E, with more resource inputs driving the revenue scale toward similar size as Cellular/Infrastructure.

\- PD entered mass production in late 2Q26. The volume will be greater in 3Q26E.

PD growth is significant at this moment. Laser will grow, but there are many types of laser. Win Semi can cover VCSEL, EML, CW laser, etc. with client engagement ongoing. EML and VCSEL are in production with more volume onwards; CW laser adoption is relatively less now and the development and qualification are ongoing. Win Semi expects CW laser to have partial contribution (e.g. epitaxy, wafer process) in 2H27E, and has to wait till 2027-28E for more meaningful contribution.

\- PD production focuses on one single customer now. Win Semi is optimistic about PD in the future, and the customer has a very upbeat demand forecast. Win Semi has to work hard to meet the demand already and does not worry about stalled business given the lack of other customers.

\- Win Semi's optical supports cover epitaxy and wafer process. In optical communications, customers may have their own options of epitaxy (e.g. third-party epitaxy or full process at Win Semi).

\- Win Semi does not provide MOCVD tool units.

Data center VCSEL has been in production since 2025. EML (mid/long-haul) will enter into production in 2H26 (some long-haul customers were already in production in 2025).

Has LTAs for critical materials to reduce supply chain risks. Win Semi works with the PD customer in securing substrate supply.

## - Infrastructure

Satellite communication includes PA and LNA on the constellation as well as ground gateways. Mobile antenna contribution is less meaningful (part of ground terminal). Win Semi has different technologies (GaAs or GaN) supporting intra-satellite or satellite-gateway communication.

\- Within infrastructure, current contributions from base station and satellite are broadly commensurate.

Infrastructure revenues (satellite/base station) are project-based, not recurring. Base station revenue was much higher than satellite last year, but new satellite deployments and direct-to-cell applications are adding to the satellite scale this year. Whether satellite revenue will exceed that of base station is pending monitoring because 5G is now at the late build cycle, but customers are in talks with Win Semi with regard to 6G.

\- Handset direct-to-cell is positive for Win Semi, and it will add to RF devices on satellites.

\- Positive on satellite growth in the long run.

Satellite and base station are the two major applications in infrastructure. Defense volume is lower.

Satellite GaN devices come along with more frequency bands and higher power requirements (e.g. direct-to-cell).

## - Depreciation

\- Win Semi initiated some project spendings from 2H25, and the spending will roll into the depreciable asset base upon installation and qualification. Win Semi has no clear picture about the roll-in timeline given uncertainty of semiconductor equipment delivery lead time, but TWD700mn+/quarter of current depreciation charge is broadly the bottom level.

\- Does not anticipate $>1$ bn/quarter of depreciation this year. We may see TWD800mn/quarter plus or minus given more recognition of depreciable assets (optical and GaN investments).

## - Inventory

\- Inventory dollar balance increase is mainly due to raw materials. Geopolitics and the tension in Middle East affect the supply situation of raw materials and chemicals. Win Semi built up inventories in 2Q26 in preparation for future production ramp-up.

\- Inventory balance increase 

[中间内容因长度限制已省略]

inancial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.
For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:
THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.
This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.
An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.
The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.
Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:
http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Taipei Branch, Taiwan. All rights reserved.
"""
