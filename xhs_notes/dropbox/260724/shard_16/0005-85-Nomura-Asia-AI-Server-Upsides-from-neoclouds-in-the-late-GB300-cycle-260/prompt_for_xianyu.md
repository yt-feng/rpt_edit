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

## Upsides from neoclouds in the late GB300 cycle

More aggressive capex from neoclouds, with moderate upsides from CSPs and more announcements from AMD

Near-term upsides from neoclouds will mitigate GB-VR transition impact in 2H26F In our prior anchor report on Asia AI Semi & Server in June 2026, we forecasted a product transition impact on AI server rack shipments during 2Q-3Q26F for nVidia's (NVDA US, Not rated) GB300 migration to VR200, as we observed that top CSPs would prefer to wait for new generation products, such as VR200, for better cost/performance, and we expected neoclouds will play a more important role to supply/lease more computing power to CSPs during this transitional period.

While we were right about neoclouds' capex upside on GB300, we underestimated the purchasing power from neoclouds, especially xAI (unlisted), which is now under SpaceX (SPCX US, Not rated). SpaceX listed on 12 June and raised a total of USD85.7bn. In late-June, SpaceX further announced to raise USD25bn in a debt sales. As shown in our Anchor Report – Global satellites – Fusion of satellites, connectivity, and AI, dated 13 June, SpaceX estimates a total addressable market (TAM) of USD28.5tn, with USD370bn from space, USD1.6tn from connectivity, and a majority USD26.5tn from AI. SpaceX plans to prioritize growth and investment to capture the opportunities in AI applications and compute infrastructure. SpaceX's capex grew 144%/86% in 1Q26/2025 to USD10.1bn/USD20.7bn, mainly driven by rising investments in the AI segment. AI capex consumed the largest portion of SpaceX's capex in 1Q26/2025 (61%/76% total capex), reaching USD7.7bn/12.7bn in 1Q26/2025, according to the company's prospectus.

From our supply chain observations, SpaceX/xAI raised its AI server rack orders to Dell (DELL US, Not rated) and Supermicro (SMCI US, Neutral) several times in late-May to early July. We believe total GB300 orders from xAI to related suppliers in 2026F could exceed 13k racks, much higher than our original 6-8k racks. And, the split of 1H:2H26F could be 3-5k:8-10k. We believe the order increase benefits for related components will concentrate in 3Q26F to early-4Q26F, and final rack delivery will be more smooth between 3Q26F and 4Q26F, or even 1Q27F.

Our view is echoed by Supermicro's preliminary business update for 4QFY26E (ending in Jun-26) on 21 July (Fig. 1), in which management estimated quarterly revenue to be near the low end of guidance (USD11.0-12.5bn) but non-GAAP GM to be in the range of 15-17% vs. guidance of 8.2-8.4% primarily supported by a favorable customer and product mix. In addition to a record backlog exiting the prior quarter, Supermicro noted further rising backlog level at the end of the fiscal quarter given total new order intakes in excess of USD60bn during 4QFY26E (ending in Jun-26), vs USD39bn viewed in early June, which are expected to be delivered over future quarters.

If we calculate the incremental increase of Supermicro's order backlog from USD39bn in early June to USD60bn in end-June, the USD21bn increase is roughly equivalent to 4.5-5.3k racks of GB300, if we assume a rack of GB300 is priced at USD4-4.5mn.

We also noticed similar sales strength/upsides from neocloud-related supply chain in June/2Q26F, such as Gigabyte (2376 TT, Buy; 2Q26 revenue beat our estimate by 20%), Wistron (3231 TT, Buy; 2Q26 revenue beat our forecast by 4%), and Asustek (2357 TT, Not rated; June revenue +54% m-m, +56% y-y, with 2Q26 revenue beating Bloomberg consensus estimate by 7%). Please note Nebius (NBIS US, Not rated) is a major customer of Gigabyte and Asustek, and Dell is a major client of Wistron.

## Research Analysts

Asia Technology
Anne Lee, CFA - NITB
anne.lee@NOM.com
+886(2) 21769966

Donnie Teng - NIHK
donnie.teng@NOM.com
+852 2252 1439

Aaron Jeng, CFA - NITB
aaron.jeng@NOM.com
+886(2) 21769962

Eric Chen, CFA - NITB
eric.chen@NOM.com
+886(2) 21769965

Fig. 1: Supermicro announced positive profit alerts on 21 July

<table><tr><td>USD bn</td><td>4QFY26 preliminary</td><td>Guidance</td><td>3QFY26</td><td>Remarks</td></tr><tr><td>Revenue</td><td>Near the low end of guidance</td><td>11.0-12.5</td><td>10.2</td><td></td></tr><tr><td>Non-GAAP GM</td><td>15-17%</td><td>8.2-8.4%</td><td>10.1%</td><td>Primarily due to a favorable customer and product mix.</td></tr><tr><td>Backlog</td><td>Received &gt;USD60bn new orders in 4QFY26</td><td></td><td>Record backlog</td><td>Expected to be delivered over future quarters.</td></tr></table>

Source: Company data, NOM

AMD strengthening its strategic partnerships with OpenAI, Meta, and Anthropic, through MI450-series

We have been flagging AMD's (AMD US, Not rated) rising traction in MI455 and notice AMD's top customers for MI455 are OpenAI (unlisted; through Oracle [ORCL US, Not rated] and Microsoft [MSFT US, Not rated]), Meta (META US, Not rated), Anthropic (unlisted), and several neoclouds (report). With MI455 getting ready, various cloud companies recently announced more detailed cooperation with AMD, as shown in Fig. 2.

\- Oracle first announced to deploy AMD's MI450-series GPUs, with an initial deployment of 50k starting in 3Q26 and expanding in 2027E and beyond (news).

\- OpenAI announced to deploy multiple generations of AMD AI GPUs to power 6GW compute capacity, starting with MI450 GPUs in 2H26E (news).

\- Meta will deploy multiple generations of AMD AI GPUs to power 6GW compute capacity, starting with customized MI450 GPUs in 2H26E (news).

\- Microsoft is adopting AMD Helios rack solutions powered by MI455X (news).

\- AMD and Anthropic announced a strategic partnership with AMD committing to up to USD5bn equity investments and Anthropic deploying 2GW of AMD Helios MI450 starting 1H27E (news).

If we assume 1GW datacenter deployment roughly requires of 250k MI450 chips by assuming certain redundancy, OpenAI and Meta's 6GW multi-year deployment plans will require roughly 167k CoWoS wafer each.

Anthropic's 2GW MI450 series deployment is roughly equivalent to 500k MI450 chips, or 6.9k racks in 2027F, and consumes 55.6k CoWoS wafers, accounting for $40\%$ of our 138k CoWoS wafer assumption for AMD's MI-series in 2027F.

We are not sure how many years OpenAI and Meta's plans will take to complete. However, if the plans are split into only two to three years, our 138k CoWoS wafer assumption may not be enough to serve for OpenAI, Meta, and Anthropic in 2027F.

Fig. 2: Announced deployments of AMD MI450 series GPUs

<table><tr><td>Company</td><td>Announcement timeline</td><td>Deployment scale Chip (units)</td><td>Capacity (GW)</td><td>Deployment start</td><td>Implied CoWoS wafer demand (kpcs; if all MI450)</td><td>Remarks</td></tr><tr><td>Oracle</td><td>10/14/2025</td><td>50,000</td><td></td><td>3Q26</td><td>6</td><td>50k units of MI450 series.</td></tr><tr><td>OpenAI</td><td>10/6/2025</td><td></td><td>6</td><td>2H26</td><td>167</td><td>Multiple generations of AMD AI GPU.</td></tr><tr><td>Meta</td><td>2/24/2026</td><td></td><td>6</td><td>2H26</td><td>167</td><td>Multiple generations of AMD AI GPU.</td></tr><tr><td>Microsoft</td><td>7/20/2026</td><td>TBA</td><td></td><td>TBA</td><td></td><td>Adoption of MI455X Helios.</td></tr><tr><td>Anthropic</td><td>7/22/2026</td><td></td><td>2</td><td>1H27</td><td>56</td><td>MI450 series Helios.</td></tr></table>

Note: AMD MI455 Helios TDP could range in 225-245kW; we assume some redundancy in deriving implied GPU units. Source: Company data, NOM estimates

We raise our nVidia downstream module/rack assumptions to capture the upside from GB300

We maintain our CoWoS volume and allocation forecasts published in our Asia AI Semi & Server anchor report in June. However, in light of the recent order upsides from neoclouds and some recovery of Meta's GB300 rack shipments in 2H26F, we raise our module and rack shipment assumptions for nVidia.

For 2026F, we raise our GB/VR rack shipment assumption from 54.5k units to 62k units for 2026F (see Fig. 4). Of this, we assume VR200 to account for 15% in 2026F (vs prior 15-20%), with concentration in 4Q26F, as we observe the module level ramp of VR200 is 1-2 months later than original expectation, if no further delay, and recent order increases are

mostly on GB300. We expect the delivery of the newly added GB300 racks will likely extend from 2H26F to 1Q27F, and the sizes of the new orders are large enough to mitigate the GB-to-VR transitional impacts in 2H26F, which we were concerned about earlier.

We also moderately raise our 2027F GB/VR racks to 66k vs prior 62k racks, with upsides coming from GB300, pushed out of VR200 rack delivery, and a potential transition from Rubin to Rubin Ultra happening in 2Q27F.

Our HGX vs GB/VR mix assumption for nVidia modules is shifting more to GB/VR types, from HGX, as a large portion of the new orders is in the GB300 configuration. We change our HGX:GB/VR mix assumption to 27%/73% for 2026F, vs our previous estimate of 30%/70%. For 2027F, we tweak our HGX:GB/VR mix assumption to 19%:81%, from prior 20%:80%, as we consider the new GB300 orders and believe VR200 demand will outpace supply in the initial stage.

Potential neocloud beneficiaries – Wistron, Bizlink, Auras, AVC, Delta, Lite-On, and Gigabyte

We believe recent downstream AI server order upsides from neoclouds will provide more benefit to “downstream” components (e.g., power, thermal, cable/connector) and ODMs as their shipments are linked to rack shipments, rather than CoWoS output. The order catch-up in downstream will help to eliminate the upstream and downstream buffer/gap, as shown in Fig. 4.

We believe xAI mainly gives orders to Dell and Supermicro, and SpaceX is also evaluating to approach ODMs (news), such as Hon Hai (2317 TT, Buy), as a potential diversification of supply, in light of its growing demand. We believe Wistron (3231 TT, Buy) will benefit, as it supplies L10 of GB300/VR200 for Dell. Gigabyte (2376 TT, Buy) also has sizeable neocloud exposure through its supply to Nebius, and may potentially benefit from this trend.

For components, we notice that Dell and Supermicro mainly purchase power supply units (PSU) of GB300 from Taiwan-based suppliers, such as Delta (2308 TT, Buy) and Lite-On (2301 TT, Buy). Auras (3324 TT, Buy) is one of the major cold plate suppliers to Supermicro and also supplies some to Dell. AVC (3017 TT, Buy) also has some share in Dell and Supermicro.

We remain positive on Bizlink (3665 TT, Buy, covered by Kenny Chen) with growing content value of power and data cabling, given higher power consumption and data transmission in next-generation AI datacenter/servers (both for GPU and ASIC platform) in 2026-28F. Our recent market survey suggests the headwind for 1Q26 GM erosion, caused by a temporary HPC product's delivery pause, has been largely resolved entering 2Q26F; in addition, the customer's demand not only resumed in 2Q26F but also accelerate its AI infrastructure spending, which in our view should benefit Bizlink's 2H26-1H27F AEC revenue growth and GM recovery. We believe after the acquisition of Interplex (unlisted) in 2H26F, Bizlink's dollar content value and product offerings in AI datacenter/servers should grow further, with a higher market share in 2027-28F vs in 2025-26F.

## Potential beneficiaries of AMD MI450

Recent strategic announcements from AMD and top cloud/AI customers may imply upside to our CoWoS assumption for AMD in 2027F, but the ambiguity of the multi-year deployment plans with OpenAI and Meta make us not change our CoWoS assumptions at this moment. We will wait for clarity regarding the patterns of deployment in the next few years. But sentiment-wise, those partnerships could be positive for the AMD MI450 supply chain. We believe Wiwynn (6669 TT, Buy) is the major ODM of MI450 for Meta; EMC (2383 TT, Buy) is one of the major CCL suppliers; SCC (002916 CH, Buy; covered by Bing Duan) is a major supplier of MI4xx motherboard; Wistron is the mass production assembler of MI4xx UBB modules; Delta is a major supplier of 12kW PSU; and AVC is one of the major thermal component suppliers.

k units of racks

Fig. 3: Our quarterly forecasts for GB/VR rack shipments  
![](images/aa9107fc2db783ac0511d55388235f2f4b6247837ccd451a6c4323bf0a109112.jpg)  
Source: NOM estimates

Fig. 4: Our assumptions of global server market and nVidia's AI GPU supply and demand

<table><tr><td rowspan="2">nVidia</td><td colspan="4">Current forecast</td><td colspan="2">Old forecast (June 2026)</td><td colspan="2">Change</td></tr><tr><td>2024</td><td>2025</td><td>2026F</td><td>2027F</td><td>2026F</td><td>2027F</td><td>2026F</td><td>2027F</td></tr><tr><td>Supply: CoWoS-based GPU unit supply (k units)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A100</td><td>134</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>H100/200/20</td><td>4,932</td><td>476</td><td>-</td><td></td><td>-</td><td></td><td></td><td></td></tr><tr><td>B200/300 (if assuming no B300A)</td><td>263</td><td>5,265</td><td>5,835</td><td>225</td><td>5,835</td><td>225</td><td>0%</td><td>0%</td></tr><tr><td>Rubin</td><td></td><td></td><td>2,024</td><td>9,093</td><td>2,024</td><td>9,093</td><td>0%</td><td>0%</td></tr><tr><td>Total (a)</td><td>5,329</td><td>5,741</td><td>7,859</td><td>9,318</td><td>7,859</td><td>9,318</td><td>0%</td><td>0%</td></tr><tr><td>Module: GPU unit forecasts (k units)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HGX</td><td>4,538</td><td>1,527</td><td>2,126</td><td>1,522</td><td>1,976</td><td>1,426</td><td>8%</td><td>7%</td></tr><tr><td>GB or VR (Oberon)</td><td>78</td><td>3,234</td><td>5,663</td><td>6,515</td><td>4,613</td><td>5,704</td><td>23%</td><td>14%</td></tr><tr><td>Total (b)</td><td>4,616</td><td>4,761</td><td>7,789</td><td>8,036</td><td>6,589</td><td>7,130</td><td>18%</td><td>13%</td></tr><tr><td>The gap of module level/ GPU volume [1-b/a]</td><td>13%</td><td>17%</td><td>1%</td><td>14%</td><td>16%</td><td>23%</td><td></td><td></td></tr><tr><td>Server type mix% for AI GPUs using CoWoS (%)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>HGX</td><td>98%</td><td>32%</td><td>27%</td><td>19%</td><td>30%</td><td>20%</td><td></td><td></td></tr><tr><td>GB or VR (Oberon)</td><td>2%</td><td>68%</td><td>73%</td><td>81%</td><td>70%</td><td>80%</td><td></td><td></td></tr><tr><td>AI server units (k)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>A/H/B/R100/200/20/300 (8 GPUs per server)</td><td>567</td><td>191</td><td>266</td><td>190</td><td>247</td><td>178</td><td>8%</td><td>7%</td></tr><tr><td>GB200/300/VR... (4 GPUs per server)</td><td>20</td><td>809</td><td>1,416</td><td>1,629</td><td>1,153</td><td>1,426</td><td>23%</td><td>14%</td></tr><tr><td># of NVL72 Racks (ideal) (K racks)</td><td>0.15</td><td>45.9</td><td>78.6</td><td>90.5</td><td>64.1</td><td>79.2</td><td></td><td></td></tr><tr><td>Potential yield loss, or component bottlenecks?</td><td>65%</td><td>49%</td><td>21%</td><td>27%</td><td>15%</td><td>22%</td><td></td><td></td></tr><tr><td># of NVL72 Racks (reality) (K racks)</td><td>0.1</td><td>23.2</td><td>62.0</td><td>66.0</td><td>54.5</td><td>62.0</td><td></td><td></td></tr></table>

<table><tr><td rowspan="2">Overall server market</td><td colspan="4">Current forecast</td><td colspan="2">Old forecast (June 2026)</td><td colspan="2">Change</td></tr><tr><td>2024</td><td>2025</td><td>2026F</td><td>2027F</td><td>2026F</td><td>2027F</td><td>2026F</td><td>2027F</td></tr><tr><td>General/CPU server units (k)</td><td>11,444</td><td>13,600</td><td>17,820</td><td>22,490</td><td>17,820</td><td>22,490</td><td>0%</td><td>0%</td></tr><tr><td>AI server units (k)</td><td>877</td><td>1,475</td><td>2,532</td><td>4,

[中间内容因长度限制已省略]

ted affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia ('Saudi Arabia') or a 'Market Counterparty' or a 'Professional Client' (as defined by the Dubai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, Nlplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but

not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Copyright © 2026 NOM International (Hong Kong) Ltd., Taipei Branch, Taiwan. All rights reserved.
"""
