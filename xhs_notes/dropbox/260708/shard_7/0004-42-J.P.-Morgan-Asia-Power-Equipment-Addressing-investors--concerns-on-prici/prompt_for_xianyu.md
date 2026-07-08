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

## Asia Power Equipment

## Addressing investors' concerns on pricing, policies, over-capacity and delay in transmission build-out

We have observed rising investor skepticism regarding the upcycle for Asian power equipment companies. In this note, we summarize investors' key questions and our responses. For Korean power equipment companies, we believe the key concerns include the recent flattening in T&D equipment prices, as indicated by monthly data (Figure 2-Figure 3), delays in ultra-high-voltage transmission lines in the U.S., and a high base for new orders in 1Q. Our view is that pricing for high-voltage T&D equipment is still holding up well, with $\sim 40\%$ OPM or above for UHV products, supported by delays in capacity expansion plans by some players, the difficulty for EM players such as China and India to penetrate the U.S. regulated market, and exceptionally strong demand from both utilities and data centers. While there have been delays in UHV transmission build-out in the U.S., we see this more as a near-term scheduling/phasing issue rather than a structural slowdown in transmission needs. The recent heatwave and spike in power prices (Figure 5) have brought grid constraints to the forefront, while decades-long underinvestment in transmission lines remains unresolved (Figure 6). Although upcoming 2Q26 results could be less exciting for names such as Hyosung Heavy, given a high base and potential order delays related to Middle East conflicts (see our 2Q preview), we view this as an opportunity to accumulate quality names. We see a good entry level for Hyosung Heavy if it falls below KRW 3,000k, implying $< 20\mathrm{x}2028\mathrm{E}$ P/E.

Figure 1: Asia Power Equipment Companies' 1-month share performance %  
![](images/2209d6d10cdb366b16711ca7b31a742da9d75c2b755a5df856e62e940001bed9.jpg)  
Source: Bloomberg Finance L.P., JPM. Priced as of 6 Jul 2026.

\- Have U.S. T&D equipment prices plateaued? We have noted recent concerns about potential overcapacity in gas turbines/engines (see note by our U.S. machinery analyst), and we have received questions on whether T&D equipment pricing has started to decline as capacity increases. Our takeaways are: (1) Our channel checks suggest high-voltage T&D equipment prices have held up well, given muted capacity expansion YTD; (2) While numerous power equipment manufacturers have announced capacity expansions, the pace of execution remains uncertain due to lengthy regulatory approval

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

## Power Equipment and Utilities

Stephen Tsui, CFA AC (852) 2800-8592 stephen.tsui@JPM.com JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Rishabh Gupta  
(91-22) 6157-3429  
rishabh.x.gupta@JPM.com  
JPM India Private Limited, JPM Tower, Santacruz(E), Mumbai - 400098, SEBI Registration: INH000001873, (91-22) 6157-3000.

(852) 2800-8546
vento.suen@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Alan Hon
(852) 2800-8573
alan.hon@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

processes and labor shortages. Supply growth is constrained and we have seen limited opportunities for Chinese and Indian suppliers to penetrate the regulated U.S. market (see our takeaway note from the investor tour). While the U.S. PPI for transformers appears to be flattening, this is a lagging indicator and includes T&D equipment across all voltage levels, which may not fully reflect pricing power for high-voltage T&D transformers and switchgear. Also, we believe margin expansion is a function of a more favorable geographical mix (i.e. higher US sales), and product mix (e.g. higher sales for UHV products, which carry 5-10ppt higher operating margin than other products).

Figure 2: US transformer PPI Rebased to 100 on Jan 2021  
![](images/7ca664ab14d8e8732e7a02e2c5ac305bb16fca65f897d31be7498da915173116.jpg)  
Source: FRED, Federal Reserve Bank of St. Louis, JPM.

Figure 3: Average unit value of South Korean transformer exports to the US (over 10MVA)  
![](images/e21e614d0f389fb7db816d2891403c4d3b4a63505625c62b441495690d2015d7.jpg)  
- Average unit value of South Korean transformer exports to the U.S. (over 10 MVA) (US\$/t)  
Source: Korea Customs, TRASS, JPM.

\- Would behind-the-meter generation for DCs dampen T&D demand? The US government has released policies to support behind-the-meter power generation for data centers (see note by our US clean energy analyst). This has sparked concerns that less transmission build-out and grid investments may be required. Our takeaways are: (1) While behind-the-meter generation is gaining momentum, the need to ramp up transmission investment remains. This is driven by renewable build-out (and the associated need for long-distance transmission), rising power consumption (from manufacturing reshoring and electrification), and replacement demand; (2) High-voltage T&D equipment is still required for behind-the-meter generation, as data centers grow in size and operate at higher voltages. For example, the Stargate data center in Texas requires extensive high-voltage infrastructure, including a $345\mathrm{kV}$ substation with five main power transformers and multiple high-voltage circuit breakers (Figure 4).

\- Why would the US continue to ramp up T&D capex despite the proliferation of BTM?Recent events underscore that grid constraints remain a binding risk. During the late-June heatwave, PJM—the largest US grid operator—highlighted major transmission congestion alongside sharp wholesale price spikes, with spot power prices rising to \~US\$300/MWh (versus a more typical \~\$25–40/MWh, per Reuters). As peak loads rise with extreme weather and the generation mix shifts toward renewables, the system becomes more exposed to congestion and outage risk—especially when conditions tighten across a broad footprint. This pressure is compounded by structural demand growth from data centers and EVs; Reuters reported that PJM’s wholesale power costs rose 68% YoY in the first five months of 2026. In this context, expanding high-voltage transmission is a practical reliability and economic response: extra-high-voltage lines (e.g., 765 kV) can be materially more cost-efficient on a \$/MW basis than lower-voltage alternatives (often cited as \~75% lower per MW vs. 230 kV) for moving large blocks of power over long distances. More broadly, high-voltage AC and HVDC buildout is needed to deliver firm capacity to growing load centers and to integrate remote wind and solar resources, supporting grid stability as power flows and operating requirements evolve.

Figure 4: Illustration of Abilene Stargate 1 (1,200 MW Under Development)  
![](images/ba9b8f66ead07d95b3b613ecc2c62bbd3fb09b03466ddc54d8bd5b97ca25eb2a.jpg)  
Source: Lancium.

Figure 5: PJM 2027 forward ATC power prices US\$/MWh  
![](images/9575226e13d1b8ac490bbed52f44bd5dce4b6243b7396739e42760e865b776e2.jpg)

Figure 6: Miles of new $345\mathrm{kV}+$ transmission lines built over the last 15 years  
![](images/b5316406648ae3eb6c934ac06f4ca4ab3cde1ddb32f7c15731cf5afb82200215.jpg)  
Source: Bloomberg Finance L.P.  
Source: Grid Strategies.

\- Could the delay in approval of 765kV transmission lines post downside risks to equipment demand? The Public Utility Commission of Texas (PUC) has delayed decisions on several 765-kilovolt (kV) transmission projects, including the Longshore-to-Drill Hole route in West Texas and the Bell County East to Big Hill project in Central Texas. This has raised concerns about a broad-based delay in UHV transmission in the US, in our view. Overall, we believe the timing slippage raises “execution” concerns, not “demand” concerns. Admittedly, such UHV buildout could face knock-on permitting/solicitation bottlenecks, but we view this as a near-term scheduling/phasing issue rather than a structural slowdown in UHV need. Grid stress events reinforce the need for such build-out (see above).

Table 1: Examples of US 765kV projects in the pipeline

<table><tr><td>Project</td><td>Investment/Project Cost ($mn)</td><td>Length (miles)</td></tr><tr><td>AEP Texas, CPS Energy, Oncor and CNP Texas 765-kV STEP Eastern Backbone Regional Planning Group (RPG) Project</td><td>9,384</td><td>1,109</td></tr><tr><td>Oncor and AEPSC Drill Hole to Sand Lake to Solstice 765-kV Line Regional Planning Group (RPG) Project</td><td>742</td><td>104</td></tr><tr><td>Phantom - Crossroads - Potter 765 kV Ckt 1 New Line, Two Crossroads 765 kV Reactors</td><td>1,691</td><td>293</td></tr><tr><td>Anthem – Seminole 765 kV New Lines</td><td>1,277</td><td>131</td></tr><tr><td>Crawfish Draw - Phantom 765 kV Single-Circuit New Line</td><td>1,366</td><td>239</td></tr><tr><td>Seminole – SW Shreveport 765 kV New Line</td><td>2,372</td><td>315</td></tr><tr><td>Woodward - Crawfish Draw 765 kV New Line</td><td>1,790</td><td>264</td></tr><tr><td>MISO Tranche 2.1</td><td>12,738</td><td>1,754</td></tr><tr><td>Putnam County, West Virginia-Frederick County, Maryland</td><td></td><td>260</td></tr><tr><td>Campbell County, Virginia-Fauquier County, Virginia</td><td></td><td>155</td></tr><tr><td>John Amos to Welton Spring to Rocky Point</td><td></td><td>261</td></tr><tr><td>Joshua Falls – Yeat</td><td></td><td>156</td></tr><tr><td>Central Ohio</td><td></td><td>300</td></tr><tr><td>Marshall County, West Virginia, to Perry County, in central Pennsylvania</td><td>1,700</td><td>220</td></tr></table>

Note: Non-exhaustive.  
Source: Company data, JPM.

\- Is AIDC capex losing steam? Meta (META US, Neutral, covered by JPM's Doug Anmuth) is exploring the creation of an AI infrastructure business that would allow external developers to rent access to its AI models and underlying compute capacity (see note). In our view, this has raised concerns among some investors about potential overcapacity in AIDC. Our analyst believes that monetizing infrastructure would give Meta greater flexibility and help the company recoup part of its substantial investment, similar to what we have seen with other large infrastructure players. Our analysts forecast AI capex rising meaningfully from US\$600bn in 2026E to approximately US\$1.4tn by 2030E (Figure 7). The long-term outlook for AI infrastructure investment remains robust: total AI capex spending is now expected to reach \$5.5tn through 2030, up from \$5.1tn in prior forecasts, which is expected to drive 138GW of new data center capacity.

Figure 7: Growth to ramp-up sharply in 2027  
![](images/784c063deb44ca595b4fcd62564851f83422102e79c1840879904fc1891a2ada.jpg)  
Source: JPM.

Figure 8: Anticipated AI capex funding sources  
![](images/1f658307ec553fbc76223da07282950a7ff9dbd89c0ff40a534c9d740ca744bf.jpg)  
Source: JPM.

\- Have Hyundai Electric/Hyosung Heavy reached peak multiples? HDE and Hyosung Heavy trade at 25x 2027E P/E on average, versus LS Electric at >40x. We believe their valuation discount reflects limited direct exposure to data centers. Note that HDE/HYS derived almost 90% of new orders from utilities and grids last year; as a result, investors may view them as purer T&D plays, while LS Electric commands a premium given its higher direct exposure to data centers (30–50% of new orders this year, on our estimates). That said, we think the valuation gap could gradually narrow if HDE/HYS increase their direct exposure to data centers. Local news reported that HDE recently won a US data center order with a contract value of >US\$700mn. For Hyosung Heavy, the company has announced plans to establish a joint venture with Quanta Services (PWR US, OW, covered by JPM's Mark Strouse) to supply circuit breakers to data centers, utilities, and other customers. These developments suggest further progress on data center order wins, and we believe investor perception could improve as the companies demonstrate additional DC project wins.

\- Is the upside from domestic opportunities priced in? The Korean government and major AI companies shared their long-term vision for an AI mega-project last week, including a >KRW 4,700tn long-term investment plan (see note by our Tech analyst). The investment timeline is distant (through 2040E/2033E for Samsung/SK Group, respectively), and actual capacity build-out execution is highly dependent on industry supply-demand dynamics, given the cyclical nature of the memory industry. Yet our Tech analyst believes this is a long-term positive for power infrastructure suppliers. We believe the Street has only priced in single-digit growth in domestic power equipment demand over the next few years, which could lead to potential earnings revisions in the medium term once we have more details on the domestic T&D capex plan and the broader mega tech investment plan.

\- Would Korean electrical equipment companies suffer from concentration risk due to country exposure? One key pushback we’ve received from investors on Korean power equipment names is country exposure: the companies we cover have a high concentration of new orders from the US market. This has raised concerns about heavy reliance on US order momentum tied to the tech capex cycle. That said, we are seeing increasing progress in winning orders outside the US. For example, Hyosung Heavy Industries has signed a long-term agreement with AusNet (operator of Victoria’s transmission network in Australia) to supply UHV transformers and reactors, with a contract value of KRW 310bn. This follows another win in March: a KRW 142bn ESS order in Queensland. Note that Hyosung has a leading market share in the ultra-high voltage circuit breaker market in India and India accounted for \~5-10% of Hyosung’s Heavy Industries revenue last year. LS Electric also aims to accelerate its push into Europe, which could become its next strategic market (per Korea Times). Note that the company is attempting to obtain more certifications in Europe to open paths into its green procurement market. Hyundai Electric also saw a >15% increase in Europe revenue in 1Q26.

\- Would capacity expansion by Indian players lead to over-capacity issues for T&D equipment? Some investors are concerned that the US T&D market's demand/supply outlook could deteriorate, driven by meaningful capacity expansion plans by Indian players, and CG Power has also reported a US order win for power transformers for a large-scale US data center project. Our view is that we are not aware of Indian players winning AIDC-related orders in the US in any meaningful way—unlike Chinese players, where multiple companies have already announced order wins (see our takeaway note from the data center conference)—and it therefore does not appear that Indian players are materially gaining share in electrical equipment for US data centers. While the Indian subsidiaries of GE Vernova and Hitachi are expanding T&D equipment capacity, they do not contract directly with data center customers; orders are primarily routed through their parent companies. Domestic demand in India also remains strong (see our initiation note on India power equipment).

Table 2: Power Equipment Valuation Comps

<table><tr><td rowspan="2"></td><td rowspan="2">Ticker</td><td rowspan="2">JPM rating</td><td rowspan="2">Share price (LC)</td><td rowspan="2">Mkt Cap (USDm)</td><td rowspan="2">Daily liquidity (USDm)</td><td colspan="2">PE (x)</td><td colspan="2">P/BV (x)</td><td colspan="2">Dividend yield (%)</td><td colspan="2">ROE (%)</td><td colspan="2">EV/EBITDA (x)</td></tr><tr><td>2026E</td><td>2027E</td>

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
