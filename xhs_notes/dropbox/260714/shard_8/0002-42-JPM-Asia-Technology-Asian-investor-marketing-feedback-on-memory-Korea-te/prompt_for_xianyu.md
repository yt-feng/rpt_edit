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

## Asia Technology

## Asian investor marketing feedback on memory/Korea tech and holdcos

We met with over 50 investors in Hong Kong last week. In this note we highlight the key areas of investor interest and feedback and try to answer FAQs from the meetings.

Areas of investor interest: all about memory, weak sentiment prior to June-quarter print. After strong share performance in April/May, major Asian memory stocks have fallen 30% since their peak in June to the July 13 close (vs. MXAP/SOX index -6%/-11% as of July 10) due mainly to: i) a growing disconnect between CSP datacenter hardware capex and memory TAM (i.e. sell-side memory TAM expectations moving ahead of CSP's capex projections; ii) Y-Y pricing momentum and secondary delta (q-q pricing momentum) slowing post 2Q26, and iii) lower June quarter EPS print expectations (SEC 2Q26 OP expectations seeing downward revision prior to print last week: note). Most investors that we spoke with agree that favorable mid-to-long term memory fundamentals are in place over the next 12-24 months but are worried about crowded positioning and elevated volatility amidst rising ETF product trading activity in the market. We think the nature of investor concern hasn't changed dramatically compared to three months ago when the market had exactly the same debate (note). From a broader cycle perspective, we believe we are in a transitional stage from “infrastructure buildout: growth momentum acceleration coupled with beat & raise” to “optimization: growth refinement and earnings durability proof”. While we expect CSP datacenter hardware capex spending projections to move up, the degree of upward revision is unclear before the actual results print in (70% the memory sentiment driver at this point, in our view). This is likely to weigh on the memory share sentiment in the short-term before risk-on trade resumes after the CSP result print, and we believe sustainability of earnings durability is the more important share price driver in the midterm. In Asia, we maintain our positive view on major memory makers: SEC (OW), Kioxia (OW), and Nanya Tech (OW).

Demystifying memory industry dynamics and sentiment via answering to FAQ. In this section, we share key FAQs from investors during the meeting. Aside from usual S-D dynamic questions, “LTA” and “HBM pricing” were two key topics during the meetings. Compared to 3M/6M ago, we generally sense more optimism surrounding the LTA concept and witness questions evolving into understanding the LTA in the context of how memory suppliers plan to establish long-term relationships with key customers. Yet, still the majority of investors (more than half) tend to take a cautious view on the LTA concept. On the HBM side, we sense a big gap between our expectations and investors (2x ASP y-y increase next year). Lastly, while investors acknowledge the upside from AI-grade CPU (memory team view & server team view), we believe the degree of upside is not well understood.

\- How much CSP capex hike should happen to justify memory value TAM? Our May-2026 published Memory Industry TAM for 2026E-2027E stands at US\$348-720bn and this represents 50-70% of CSP hardware capex estimates projected from our U.S. hardware research team. Many investors view the hyperscale players' capex to be underestimated by the market (mainly sell-side consensus) and expect it to move up to US\$1trn/US\$1.5trn for the respective forecast period in next 3-6M. Capex upward revision is likely to lower the

See page 7 for analyst certification and important disclosures, including non-US analyst disclosures.

Technology - Semiconductors

Jay Kwon AC
(82-2) 758-5725
jay.h.kwon@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

Sangsik Lee

(82-2) 758 5146

sangsik.lee@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

Neelay Y Kamath
(91-22) 6157 3764
neelay.kamath@jpmchase.com
JPM India Private Limited

memory's value share within capex, alleviating the concern on the sustainability trajectory. This was also a large part of the share price trigger in April's result season, in our view. On the other hand, if CSP hardware capex spending hikes move up by a marginal amount, this could be taken negatively to memory suppliers' share sentiment.

\- Where are we in terms of LTA progress? How big is LTA out of the total volume now and will be in the future? We are beginning to witness an increase in LTA discussion among major memory makers and MU was very vocal in their latest results (note) about their LTA structure including duration, pricing, target margin profile, and other variables. It is unclear how big the LTA is out of the total volume for Korean memory makers and comparing the LTA quality is also very challenging at this stage. Therefore, until clear LTA visibility is out and available to the market, we may continue to see headline noise on its impact to ceiling prices and margins. We believe that more than half of the total contract volume will eventually be under LTA and it is important that memory makers will aim for their floor price and margin to be equivalent or above the pre-AI era. We continue to view LTA as a key element for the durability of earnings.

\- Will LTA lead to a slower ASP increase and cap margin improvement? LTA provides both suppliers and customers a strong bond to secure volume visibility and a certain price range. Especially when the AI hardware capex hike burden remains elevated, it is imperative that the LTA discussion provides greater clarity to both parties. On the other hand, price stabilization is natural and inevitable as both parties will reach an agreement on a certain range of pricing for the next 3-5 years. For the latest LTA contract, it was suggested that the contract pricing is benchmarked using the latest quarter. While we do not disagree on this, we believe upside is still open, as: a) we do not believe all the LTA volume has been secured and, even within key customers, not all the discussed volume is locked up by LTA, implying both parties could strike another LTA heading into 2027E at a higher price, b) we believe there are other elements that provide greater value than price ceilings, such as greater volume visibility or different contract terms (“take or pay”, for example), and c) even with an increase in LTA, we anticipate pricing to continue to move up for the non-LTA portion, which will still be pushing up the average pricing toward upside. It remains unclear how LTA translates into actual near-term pricing and margin, which is why we worry about the immediate margin cap. On a mid-to-long term horizon, we would rather focus on over-the-cycle profitability, and this is the strongest counter-argument to some investors’ view of memory as cyclical and expectations that prices should correct 50-70% during the down-cycle.

\- Near-term memory pricing outlook and 2027E projection? We still maintain our \~20%/\~10% like-for-like ASP increase expectation for CY3Q26E/4Q26E. Compared to 1-2M ago, we see an increase in the range of pricing expectations among investors (from 15-20% q-q increase to 10-30% q-q increase) as a result of the 2Q26 actual pricing trend, where we saw Korean memory makers' actual DRAM price increase was below that of global peers (MU and NYT May-quarter/June-quarter DRAM ASP trend at low-60%/high-60% q-q increases). We believe the difference could be explained by 1) base differences (Korean memory makers' March-quarter ASP increase was notably higher vs. US/TW peers) and 2) product mix differences (higher LPDDR sales into mobile customers could result in lower blended ASP increase; server vs. mobile grade price difference is as high as 30-40% per GB). Some investors asked if the LTA mix impact also resulted in price differences, but this remains unclear. Moving into 2027E, we believe a single digit % ASP increase every quarter is still a fair assumption, with half of volume based on LTA using average price point in 2026 contracts and half of volume based on contract pricing, which is likely to reflect the tightening S-D.

\- HBM ASP expectation gap remains wide between us and buyside consensus. A surprising majority of buyside expectations on HBM pricing for next year were for a 2x y-y increase, and many investors were looking for EPS upward revision from HBM ASP hikes (i.e. HBM ASP per GB needs to rise 2x in order for margin to meaningfully catch up vs. normal DDR5). In our estimates, HBM industry ASP is currently near US\$1.8/Gb, which is below that of non-HBM server industry ASP (incl. both DDR5/LPDDR5 solutions) at around \$2/Gb; therefore, investors' argument is valid from a purely economic perspective. However, we believe memory makers consider a memory operation's overall profitability when speaking to their major CSP customers (DRAM, NAND, and HBM holistically rather than individual product base) and carefully monitor customers' memory spending appetites. We should bear in mind that HBM is a bundled product with GPU installation in AI server, and CPU-driven demand upside is a secondary order impact to better manage agentic AI. Also, as HBM ASP is negotiated every year (vs. conventional memory facing 3-5 years of multi-year LTA discussions), memory makers can raise ASP the following year. We believe it is imperative to sustain the trade loss ratio concept from HBM to overall DRAM industry S-D and forecast 25-30% like-for-like ASP increases y-y to be in a more reasonable range.

\- Slower HBM4 ramp well understood by the market, higher traction on HBM4E 12Hi. Given multiple supply chain reports and discussions, the NVDA Vera Rubin rack assembly delay and subsequent HBM4 sourcing plan downward revision is not new to the market and is well understood. Kyber's rack delay speculation (link) was a new surprise to the market, but we haven't seen a capacity operation plan revision from the supply chain. (JPMe: 630k wafer allocation to HBM next year out of \~2.3k total DRAM WSPM annually.) Following the Korean memory makers' series of HBM4E 12Hi first customer samplings during 2Q26, investors seem to acknowledge that HBM4E mainstream is likely to be 12Hi instead of 16Hi. In our May-2026 HBM S-D model revisions (note), we have reflected 12Hi:16Hi usage in GPU unit mix at 65%:35% for next year, which means that downside from NVDA consumption remains limited for 2027E. Instead, as seen in our CoWoS July-2026 assumption revisions (note), we see greater demand from Google TPU and AWS Trainium pipeline, which means that the overall HBM S-D shortage is likely to continue throughout our forecast period. Some investors also pointed out that AI model labs could be a greater part of memory demand drivers as they begin direct sourcing while developing their own custom chips.

\- Where is the bigger shortage between DRAM and NAND? While both DRAM and NAND are in tight situations, we see a greater shortage in DRAM (self-sufficiency at 50-60%; supply relative to order ratio) over NAND (self-sufficiency at 70-80%). DRAM remains tight despite the increase in the capacity buildout trend (DRAM WSPM annual increase by \~390k every year over 26-29E), and suppliers should see the worsening shortage continuing into next year followed by a continued shortage into 2028E. Compared to DRAM, NAND S-D is less tight and consumer electronics grade demand downward revisions are greater than expected. On the other hand, KV cache offloading grade enterprise SSD demand is seeing exceptionally strong upward revisions, and memory makers are now forecasting 500EB and 2027E y-y growth nearing the +50% range with potential upside risk. Investors think NAND S-D could fare relatively better than the headline risk profile (relatively stronger China NAND competition risk vs. DRAM) and expect a favorable ASP trend for the eSSD segment (leading US CSP customers willing to subsidize eSSD ASP as high as US\$0.5-0.55 per GB by end of the year).

\- China competition risk assessment – investors do not yet worry about China supply. Even after all of the noise (e.g. Apple testing to qualify Chinese memory vendors for a mainland China market version – link) and aggressive capacity build out headlines, investors appeared less concerned about China competition. On DRAM, there seems to be little evidence of a meaningful technology gap narrowing versus the leading DRAM producers (frontier players on 1cm at the moment and scaling down to 1dnm, while the Chinese DRAM competitor is still working through 1znm-1anm). In addition, if the China DRAM supplier allocates greater capacity to HBM for China ecosystem inference chip buildout purposes, this would alleviate its penetration concern (applying the similar trade loss ratio logic to that of global peers) to the conventional DRAM market, not to mention the overall market is in shortage. In addition, leading Chinese NAND makers are reported to be investing in both DRAM (half of the cleanroom space) and NAND for their new fab next year (link) and this is likely to be a positive development for NAND S/D dynamics through 2028E. Overall, despite capex expectations running above market growth for Chinese memory makers, we do not see this as a material downside risk to our memory sector view and investors were generally aligned with this view.

\- Are we seeing any inventory destocking risk? Typically, a memory down-cycle begins with a surge in memory component inventory across the channel and on customers' balance sheets. Given the prevailing shortage (procurement, installation, and actual consumption trend outpacing the supply increase), we see a decline in major customers' memory inventory (across consumer electronics to server, and B2B side) and little risk of unexpected inventory destocking. As memory consumption cannot exceed the amount of supply (added by inventory), we believe memory procurement eventually needs to be normalized, narrowing the theoretical S-D gap. However, this should not be read as a signal for a potential inventory build-up immediately, as multiple end-demand areas are being disrupted by limited supply. Some segment demand (consumer and automotive applications) could recover quickly when supply improves amid stable pricing trends. Lastly, a few investors also asked if power supply will become a bottleneck and widen the gap between upstream semiconductor and downstream server rack installation in datacenter. Specific lead times and inventory in the supply chain remain unclear, and we would closely monitor finished server rack inventory related risk to memory procurement going forward.

\- Mixed takes on Korea's AI mega-investment plan; more positive bias towards memory SPE from potentially higher capex spending. Investors generally found the US\$3+trn Korean AI mega-investment master plan announcement net-negative to memory sector sentiment as the initial interpretation was focused on lack of supply discipline. We believe there are many moving parts in actual capex execution, and additional fab investment will be necessary on an extremely long-term horizon after Korean memory producers fill in Yong-in fab. It is important to note that supply debottlenecking is necessary to sustain the aforementioned AI capex race while memory sustains adequate value share. From a capex perspective, we believe up to 20% or higher annualized capex could be spent vs. our published forecast, looking at the pace of near-term and mid-to-long term fab construction schedules. MU's US\$50bn additional capex plan (link) on top of its previous US\$200bn spending echoes a similar view and news reports (link) on Samsung potentially pulling in Yong-in fab infrastructure for up to two years is a clear indication of memory makers' fab first strategy to obtain flexibility in preparing new supply and the capacity to respond to its multi-year shortage

[中间内容因长度限制已省略]

ent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Completed 14 Jul 2026 04:10 AM HKT
"""
