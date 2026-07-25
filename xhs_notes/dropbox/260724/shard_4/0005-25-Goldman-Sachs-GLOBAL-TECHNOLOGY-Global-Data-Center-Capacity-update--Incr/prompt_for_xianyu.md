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
GLOBAL TECHNOLOGY

# Global Data Center Capacity update: Increased capacity expectations, but continued tightness

We update our global data center capacity forecasts using the latest data from 451 Research's database and now forecast 217GW of global data center supply by 2030 (v. 168GW prior from our last update in February 2026), representing 116GW of additional capacity from 101GW in 2025 (restated higher from 74GW prior). This addition of 116GW would represent \$6 tn of capex, assuming a \$50B/GW rule-of-thumb while acknowledging that IT infrastructure costs continue to see upward pressure. We see this capex well-covered by current consensus expectations for hyperscale capex (\~\$1 tn/year on average), which does not include SpaceX AI capex, private company capex, or datacenter platform capex.

We've become more positive on the neocloud segment following several large data center lease announcements in the last 3 months including by TeraWulf (Anthropic), Hut8 (undisclosed IG tenant), and others. We estimate average lease rates were \$166/kw/month with base terms in the 15-20 year range.

There were also several GPU-as-a-service deals including SpaceX (Google, Anthropic, Reflection AI) and IREN (Nvidia, Perplexity, Figure). Notably, Nvidia announced a new credit support and revenue share model with Sharon AI and Firmus, providing a revenue backstop and thereby reducing the cost of capital for neoclouds to build out capacity for shorter-term leases and smaller deals. Prices ranged from >\$50/MW, which demonstrates the current scarcity of compute at scale, to <\$10/MW, which represents the Nvidia floor revenue in the Sharon AI deal.

For the US alone, we forecast 125 GW of IT Power data center supply by the end of 2030, where our Utilities team estimates \~108 GW of data center demand in the US on an annual average basis in 2030. This drives an expectation of a 3.5% power demand CAGR through 2030 with BTM capacity available to serve data center load of \~31 GW and \~22 GW of power delivery by 2030. We highlight select regulated utilities and IPPs as key beneficiaries of the inflection based on their regional exposure, including FE/TLN in PJM, SRE/VST/NRG in ERCOT, XEL in MISO, and DUK in the Southeast. Our GS SUSTAIN team continues to highlight the cross-sector investment theme of Reliability, driven by both AI/data center power growth and global investment to mitigate risks of physical/network/supply chain/power/water outages.

Michael Ng, CFA
+1(212)902-8618 | michael.ng@gs.com
GS & Co. LLC

Brian Singer, CFA
+1(212)902-8259 | brian.singer@gs.com
GS & Co. LLC

Carly Davenport
+1(212)357-1914 |
carly.davenport@gs.com
GS & Co. LLC

Lindsey Shema
+1(801)578-2673 |
lindsey.shema@gs.com
GS & Co. LLC

Yash Goenka, CFA
+1(212)934-6312 |
yash.goenka@gs.com
GS India SPL

Jaya Patel
+1(212)357-9901 | jaya.patel@gs.com
GS & Co. LLC

Xavier Zhang
+852-2978-6681 | xavier.zhang@gs.com
GS (Asia) L.L.C.

Brendan Corbett
+1(415)249-7440 |
brendan.corbett@gs.com
GS & Co. LLC

Zorayda Montemayor
+1(212)357-6403 |
zorayda.montemayor@gs.com
GS & Co. LLC

## Increasing global data center capacity to 217GW by 2030E (v. 101GW in 2025)

We update our global data center capacity forecasts for the latest updates to 451 Research's data center tracker (through C1Q26). Per 451 Research data center project tracking, we now expect \~217 GW of live global data center capacity by 2030, implying growth from \~101 GW in 2025 at a 17% 2025-2030 CAGR. This +116GW of capacity net addition over the next 5 years would approximate a cumulative \$5.8 bn capex assuming \$50 bn per GW, which should be covered by the forecast average \~\$1 tn hyperscale capex (per annum, using Visible Alpha Consensus Data), which has historically been revised higher and does not include SpaceX's AI capex, private AI lab capex, or datacenter platform capex.

1Q26 451 Research data for 2026-2030 annual global data center capacity was revised upwards by 5% on average v. 4Q25, and by 13% v. 3Q25. Per 451 Research, global data center capacity additions should predominantly be from retail/wholesale providers & hyperscalers (70-90% of total global net capacity additions annually through 2030) and be located in the US (\~60-70% of total global net adds through 2030).

Exhibit 1: Global Data Center Capacity should scale to \~217 MW by 2030 (+116 GW v. 2025)
Gloabl Data Center Capacity (MWs) & year-over-year change (%)  
![](images/07e654f8119ef6af815b10f558c2664ec99b2aad820f4e86e1fed7edd2801a24.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research

Exhibit 2: Global Data Center Capacity forecasts for 2026-2030 have been revised upwards over time (+5% v. 4Q25 forecasts, +13% v. 3Q25 forecasts)
Global Data Center Capacity forecast estimates over time (MW)  
![](images/bf7d2775fd5905b8d43fa9cb86e42360cb343ceef75f5653f21fb5052fbe2df6.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research

Exhibit 3: Global data center capacity net adds should predominantly be cloud/crypto/wholesale/retail capacity Share of global data center capacity net adds by vertical (%)  
![](images/49b9d59c3db30138f76d13d5e4da5843f5ef87b9980d97d12cc4c9ce0bb83434.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research

Exhibit 4: Global data center capacity net adds should predominantly be in North America
Share of global data center capacity net adds by region (%)  
![](images/d3427b03fc495ad9ef9c3f6c730400097427ac5fd0d71264d9f7d31e11e0a2d7.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research

Exhibit 5: US data center capacity should grow to \~125 GW by 2030 (+76 GW from 2025)  
US data center capacity (MW) & year-over-year change (%); end of period capacity  
![](images/98cbd74a0eb44952ca7dcaad9bbe36671eae4f05f5d54984c01f43fae6c2143e.jpg)

Exhibit 6: US data center capacity should be led by Cloud/Wholesale/Retail providers & hyperscale-owned facilities  
Share of US data center capacity (MW) by vertical (%)  
![](images/35ebf39652460e510d5a748db8e00882a895b69b32e3dceb5e1d3275588b2c71.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research  
Source: 451 Research, Data compiled by GS Global Investment Research

Increased data center capacity estimates may prove conservative given increasing expectations for data center equipment capex, which 650 Group estimates should now reach \~\$2.3 trillion by 2030 (+320% vs. \$555 bn in 2025). We continue to view data center supply & demand conditions as extremely tight given continued compression of data center vacancy rates (per CBRE), which should continue to support pricing power for data center operators in releasing existing capacity or leasing newly added capacity, which is in-line with commentary from Flexential during our June 2026 Denver bus tour, where the company stated it expects to see pricing per kilowatt approach \$250 later this year (v. \~\$70 in 2021).

Exhibit 7: US capacity add forecasts have also been revised upwards over time (+6% v. 4Q25; +12% v. 1Q26)
US net add forecasts (MW)  
![](images/d4d3b9749c6545280a02a7f60af3891f2d0502d05099127dea7e14813fb68add.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research

Exhibit 8: Data center vacancy rates have compressed significantly over time
Data Center Vacancy rates across select US markets  
![](images/2628cb8adc8cd22cfb932b5a78bce5e4606431b555f4a1c327348dba2c18b55d.jpg)  
Source: CBRE

Exhibit 9: Average Net IT Power (MW) per site should grow over time towards \~67 MW by 2030 (v. \~26 MW in 2025)
Average Net IT Power (MW) per site & year-over-year change (%)  
![](images/6876a802d05b329733fcbdcca4475cc88ee4edc9e85df9e4819206c57d8bc15a.jpg)  
Source: 451 Research, Data compiled by GS Global Investment Research

Exhibit 10: Data Center equipment spend should more than triple by 2030 to \$2.3 trillion (v. \$444 bn in 2025)
Cloud Data Center Equipment spend (\$, mn) & year-over-year change (%)  
![](images/f0a9847de1cb73bc09b8143b4049e289a69c61f394c7fd8dac3f26a7aad1d239.jpg)  
Source: 650 Group, Data compiled by GS Global Investment Research

Exhibit 11: AI/Cloud player spend should grow to \~\$1.2 trillion by 2030 at a 22% 2025-2030 CAGR Consensus capex estimates on select AI players/Cloud players (\$, mn)

<table><tr><td>Select US cloud</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>AAPL</td><td>10,264</td><td>12,262</td><td>11,394</td><td>13,161</td><td>14,250</td><td>15,114</td><td>15,849</td></tr><tr><td>AMZN</td><td>82,999</td><td>131,819</td><td>203,623</td><td>238,651</td><td>258,537</td><td>262,932</td><td>271,362</td></tr><tr><td>META</td><td>37,256</td><td>69,691</td><td>136,723</td><td>174,523</td><td>189,094</td><td>204,024</td><td>215,239</td></tr><tr><td>GOOGL</td><td>52,535</td><td>91,447</td><td>187,786</td><td>265,836</td><td>292,538</td><td>305,685</td><td>320,552</td></tr><tr><td>MSFT</td><td>54,514</td><td>91,008</td><td>153,736</td><td>200,931</td><td>228,709</td><td>253,712</td><td>261,779</td></tr><tr><td>ORCL</td><td>14,041</td><td>38,439</td><td>74,066</td><td>98,594</td><td>98,727</td><td>89,046</td><td>74,028</td></tr><tr><td>CRWV</td><td>8,702</td><td>10,309</td><td>33,987</td><td>39,769</td><td>36,829</td><td>41,233</td><td>55,367</td></tr><tr><td>Total capex ($, mn)</td><td>260,311</td><td>444,975</td><td>801,314</td><td>1,031,465</td><td>1,118,683</td><td>1,171,747</td><td>1,214,176</td></tr><tr><td>Year-over-year growth</td><td>53%</td><td>71%</td><td>80%</td><td>29%</td><td>8%</td><td>5%</td><td>4%</td></tr></table>

Source: Visible Alpha Consensus Data

Neocloud cost of capital to decline following NVIDIA credit support. Earlier this month, Nvidia announced a new revenue sharing and credit-support model with AI clouds. In this new business model, the neoclouds receive a minimum revenue guarantee on GPU capacity (e.g., revenue per GPU per hour), which reduces the risk for the neocloud as well as its cost of financing to purchase the GPUs. Neoclouds can then provide access to enterprise, startup, and AI native customers that otherwise may have a more difficult time securing short-term capacity, with revenue generated beyond the minimum revenue guarantee being split with Nvidia. This new model was first announced with Firmus (Private) and Sharon AI (SHAZ, Not Covered), which has a 6-year deal with Nvidia for 40,000 GB300 GPUs.

Agentic workloads to support continued demand tightness as growing end-user demand more than offsetting new capacity and improved compute efficiency. Our channel checks, including an Expert Network Series call with a former Director of AI Transformation at Microsoft, helped us better understand the vision of end-user demand, which should be supported by multi-agent systems: a network of AI agents that can work autonomously but still need a cloud-based AI agent to help orchestrate workloads. Enterprises continue to be in the early stages of the deployment of agents, with many still experimenting, which should be a positive sign for future demand once experimentation transitions into full production.

## Implications for global data center power demand growth

## This section authored by Brian Singer, GS SUSTAIN

On the back of greater data center capacity, recent increases from our TMT team to their AI server shipments forecasts and our US power team's regional outlook on data center power demand, we raise our global forecasts for data center power demand through 2030. We see $170\%$ global data center power demand growth in 2030 vs. 2025 levels (117% previously), which also incorporates estimated historical data center power demand following recent reports by the DOE and IEA.

## We now see 7 Ps driving data center power demand growth/constraints:

Pervasiveness of AI. Greater industry AI capex has contributed to increased server shipments and data center capacity. Ultimate returns-enhancing AI outcomes will be critical to longevity.

Productivity of chips/servers/models. We continue to assume energy intensity reductions for AI (compute per unit of power) at a faster pace than for non-AI. However, pent-up demand for tokens/compute is likely to continue until there is more corporate/government confidence that reducing budgets will not sacrifice competitive positioning or until demand for tokens/compute has been sufficiently defined. At that point, we believe AI will shift from the Appraisal/Hopes & Dreams Phase to the Execution/Efficiency phase, characterized by downward revisions to budgets in response to productivity gains.

Price of power. This remains a key community concern (in addition to reliability of power/water), though we believe hyperscalers continue to have financial flexibility via strong balance sheets. We do not believe the US Green Reliability Premium will limit hyperscaler willingness to take an all-of-the-above approach to power sourcing.

Policy. Permitting and execution risk continue to be sources of industry frustration, even as there appears to be bipartisan support for speeding up processes. Increased attention to risks of delays driven by US community pushback to data center development is driving greater connectivity between corporates, investors and communities on potential solutions. The key areas of pushback from communities/broader consumers are: risk of power reliability issues, risk of rising power prices, risk of depletion of water supply, noise and warming impact from rejected heat. Broadly, there are solutions (take-or-pay contracting, interruptibility, closed-loop cooling/chillers, waste heat capture) that can mitigate these risks. However, perception and broader NIMBY concerns could supersede innovation/solutions.

Parts availability. Constraints in the timing/availability of power generation equipment continue to drive how data center power will be sourced as part of an overall all-in strategy — renewables/battery storage/simple cycle natural gas in the shorter term, natural gas combined cycle in the medium term, nuclear in the longer term. Natural gas combined cycle generator manufacturer GE Vernova highlighted on its 2Q26 earnings call on July 22 that it expects to have more than 50% of its capacity contracted for 2031 by the end of 2026.

People availability. We continue to expect >500K new jobs to meet overall US power demand growth. Of this, we believe more than 200K are needed to meet transmission and distribution needs. We continue to see risks that skilled labor availability constraints — particularly for electricians — represents a key risk to execution. This is also, in our view, helping to drive greater consideration for behind-the-meter power solutions that require less electricity transmission. Time-to-market priorities and long lead times for grid connectivity are driving behind-the-meter solutions — largely natural gas — that our US Utilities team expects will drive \~30% of the data center growth through 2030.

■ Physical environment. Ambient conditions — heat, humidity and drought — where data centers are being built are increasingly a driver of both stock performance and innovation. Higher heat, humidity and drought risks limit cooling technology selection optionality for data centers and require greater power demand in affected regions where minimizing direct water demand is a priority. Our analysis suggests that 56%/55% of new global/US data centers are set to be built in areas with elevated physical risk to heat, humidity and/or drought. Based on our analysis of data center location and type, we expect that 43% of new data center capacity will deploy white space direct-to-chip or immersion cooling inside the data center. Separately, we expect 56% of new data center capacity will deploy gray space chillers, adiabatic systems or m

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
