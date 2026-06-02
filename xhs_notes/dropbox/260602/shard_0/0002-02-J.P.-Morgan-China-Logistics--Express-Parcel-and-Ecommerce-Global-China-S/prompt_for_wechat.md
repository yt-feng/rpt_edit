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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Logistics, Express Parcel and Ecommerce

Global China Summit takeaways and April data: pricing power holds, ASP rises, e-commerce momentum decelerates

April operating and channel data reinforce a bifurcated but broadly constructive setup for China logistics: policy discipline continues to support pricing, while end-demand in e-commerce is clearly cooling. Company conversations with ZTO, J&T, Yunda and YMM at the 2026 JPM Global China Summit also converged on the same playbook: cost transmission to manage fuel volatility, technology and automation to protect unit economics, and service quality/reverse logistics as the key differentiation as headline pricing converges. On the express side, SPB data show volume growth steady but moderate at +3.2% Y/Y (16.84B), while revenue growth accelerated to +6.3% Y/Y (Rmb128.91B), driven by ASP recovery to Rmb7.65 (+3% Y/Y). That mix—slower volume, faster revenue, positive ASP—signals a more rational, yield-focused industry structure and aligns with Summit feedback that anti-involution has moved from a “campaign” into more repeatable operating rules (price discipline, grassroots welfare, network stability). Against this, April NBS data point to a meaningful demand deceleration (online retail +2.3% Y/Y; online physical goods GMV +0.2% Y/Y), with sharper softness in electronics categories and a tougher base plus lighter subsidies adding pressure into 2Q.

Stock view: The sector largely underperformed over the past one month, consistent with investor focus on fuel-driven margin risk, even as policy-driven pricing trends improve. YTD, performance is more constructive and more selective, with express leaders still delivering meaningful gains on the back of anti-involution durability and profitability improvement, while SF has remained a clear laggard as the market debates the pace and effectiveness of its strategy reset. We keep a selective stance: ZTO and JD Logistics remain our top picks given stronger visibility on execution and structural tailwinds from a more rational industry regime; we keep OW on SF, but it is not a preferred pick as strategy progress remains a key watch item for sentiment to inflect; and we keep Neutral on YMM, as valuation discounts have absorbed much of the regulatory and volume uncertainty, with re-entry dependent on clearer easing of headwinds and evidence of order-trend rebound.

# Infrastructure, Industrials & Transport

Karen Li, CFA AC

(852) 2800-8589

karen.yy.li@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Mufan Shi

(852) 2800-8502

mufan.shi@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Jenny Qiu, CFA

(852) 2800 8503

jenny.qiu@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Beatrice Lam

(852) 2800-8738

beatrice.lam@JPM.com

JPM Securities (Asia Pacific) Limited/

JPM Broking (Hong Kong) Limited

# Alex Yao

(86 21) 6106 6505

alex.yao@JPM.com

SAC Registration Number: S1730523020001

JPM Securities (China) Company

Limited

# Key takeaways from Global China Summit: anti-involution durability, pricing power, and operational innovation

ZTO, Yunda, J&T, and YMM attended the Global China Summit (May 2026), where discussions centered on the sector's evolving landscape and the latest operational and policy drivers. Key themes included the durability of anti-involution measures, the sector's ability to maintain pricing power amid rising costs, and the ongoing shift toward quality-driven growth. Management teams highlighted that regulatory discipline

See page 10 for analyst certification and important disclosures, including non-US analyst disclosures.

continues to underpin industry profitability, with policy support fostering a more stable and rational market environment. Companies are leveraging technology, automation, and cost transmission mechanisms to offset fuel price hikes and drive operational efficiency. Network quality, service reliability, and reverse logistics capabilities are increasingly differentiating leaders, while partnerships and international expansion remain critical for capturing new growth. The summit also underscored the importance of adapting pricing strategies, recovering demand lost to regulatory changes, and maintaining disciplined execution as the sector faces both cyclical and structural challenges.

\- ZTO's management highlighted that the policy environment remains supportive, with anti-involution measures underpinning industry profitability and structure. While the sustainability of these policies into 2027 cannot be guaranteed, ZTO expects continued government focus on grassroots welfare and network stability, making a return to aggressive price wars unlikely. ZTO's parcel volume growth in 2Q to date tracked within the guided 10–13% range, slightly below 1Q's 13% due to base effects but well ahead of industry averages. Management remains confident in achieving full-year growth targets, citing sustained outperformance versus peers and healthy underlying demand. Service quality and network strength remain ZTO's core differentiators, especially as pricing converges. ZTO's superior reverse logistics capability—handling peak daily volumes of 10MM parcels—sets it apart and is difficult for competitors to replicate quickly. Cost reduction and automation efforts are focused on the last mile, with direct sorting rates at 40–45% and unmanned vehicle deployment progressing, though broader rollout is constrained by regulatory factors. All cost savings at the last mile are passed through to franchisees, reinforcing network confidence and engagement. Alibaba's stake reduction is not expected to have a fundamental impact on ZTO's earnings or operations, as Tmall and Taobao contribute less than 20% of ZTO's parcel volume and no material contractual dependencies are expected to be affected.

\- J&T's management noted that the impact of rising fuel prices varies across Southeast Asian countries, with Indonesia and Malaysia less affected, while Thailand and Vietnam face greater challenges. The company has established a robust cost transmission mechanism, allowing it to pass increased costs to customers, which has been well received. Southeast Asia remains a key growth engine for J&T, with a projected annual growth rate of $50\%$ . The region's parcel volume per capita is only a quarter of China's, indicating substantial room for expansion. J&T's partnership with SF is progressing well, with J&T handling most of SF's overseas last-mile deliveries and expanding into Europe and the Americas. In China, J&T has significantly narrowed its pricing gap with top-tier competitors, though brand premium remains. Large clients prioritize service and stability, while smaller clients are more price-sensitive. LATAM is a major contributor to J&T's overseas business, with Brazil and Mexico leading. The business model in LATAM is evolving from direct operations and crowdsourcing to a franchise system, tailored to local market dynamics. Service levels are improving, with delivery times now under one day and costs significantly lower than local competitors.

\- YMM's management shared that oil price increases in March accelerated shipper migration to online platforms, supporting 1Q volume, but sustained oil price hikes in April pushed up freight rates and suppressed low-price shipment demand, negatively impacting 2Q volume. YMM's full-year direct volume guidance remains at 13–17%, targeting mid-to-high growth. The platform has recovered demand lost during last year's regulatory crackdown on less-than-truckload pooling, with marketing efforts successfully bringing affected shippers back online. YMM's invoicing business is transitioning to a mix of self-operated and third-party models, with third-party partners being state-owned platforms with tax advantages. The third-party invoicing model is sustainable, with high margins and risk control through diversified partners. Small loan business is shifting to a referral model, with self-operated balance expected to drop to 20% by year-end, and overall OP impact limited. Driver sensitivity to oil prices is high, with oil accounting for c.30% of costs, while commission sensitivity is lower. YMM's pure electric heavy truck penetration is c.10% overall, with faster adoption in short-haul routes. Overseas business is expanding in Egypt, Turkey, Indonesia, and UAE, with further growth planned for next year. The platform's mid-term commission rate target is at least 3%, with current levels around 2%. AI is being applied to optimize shipper and driver workflows, delivering cost savings and efficiency gains.

\- Yunda's management emphasized that anti-involution sustainability is driving the industry to grow with quality, as regulatory authorities prioritize price stability and discourage extra-low pricing. Yunda's network service quality has improved, evidenced by reduced penalties and compensation related to service failures, reflecting a more disciplined and resilient operational model. Industry growth remains positive but faces challenges, with pricing strategies adapting to market and policy shifts. Yunda believes it is challenging for the express delivery industry to grow 8–10% Y/Y this year, given the slow start in 1H26, partly due to the impact of e-commerce tax policies. However, parcel volume is expected to recover in 2H26, especially around major promotional events like 618. Fuel price hikes have increased costs, but Yunda's effective price transmission has largely offset the impact, with price transmission to end customers and franchisees varying by region. Yunda's reverse parcel business, including returns and retail parcels, has grown to c4MM orders, with returns accounting for 1.5MM. New partnerships, such as with Douyin, are expected to boost volumes and profitability, which is now improving and outperforming standard e-commerce parcels.

# April express delivery data reflects sustained policy support, ASP recovery, and healthy volume growth

\- The April express delivery sector data further reinforces the positive momentum established in recent months, as continued policy support and a notable improvement in ASP underpin a healthier industry landscape. Despite a modest deceleration in parcel volume growth—industry volume reached 16.84B, up $3.2\%$ Y/Y—the sector delivered robust revenue expansion, with total industry revenue rising $6.3\%$ Y/Y to Rmb128.91B. This outperformance was driven by a sustained ASP recovery, as the industry ASP climbed to Rmb7.65, marking a $3\%$ Y/Y increase. The sector's ability to maintain pricing power in a more rational, yield-focused environment highlights the effectiveness of ongoing anti-involution measures and regulatory discipline, and signals that the industry is successfully transitioning away from volume-at-any-cost toward quality-driven growth.

- The persistence of policy support continues to shape the sector's competitive landscape, with authorities emphasizing rational competition and the elimination of ultra-low-price flows. This regulatory backdrop is fostering a more stable and orderly market, enabling leading players to prioritize service quality and profitability. Anti-involution measures are now embedded in industry practice, giving companies the confidence to focus on yield rather than pure volume expansion. As a result, the sector is increasingly characterized by disciplined execution and strategic differentiation, which should support healthier long-term development and reinforce the market's preference for quality over scale.   
- Divergence among major express delivery players persisted in April, underscoring the importance of strategic focus and mix quality. STO delivered standout performance, with parcel volume surging 14% Y/Y to 2.38B and ASP rising 15% to Rmb2.26, demonstrating strong mix quality and ongoing consolidation benefits. YTO maintained steady volume growth at 2.73B (+1% Y/Y) and improved ASP to Rmb2.23 (+4% Y/Y), while Yunda's focus on pruning ultra-low-price flows resulted in softer volume (-4% Y/Y) but a notable ASP increase (+10% Y/Y). SF continued to realign its e-commerce strategy, with volume down 3% Y/Y but ASP up 5% to Rmb14.2, signaling improved revenue quality and margin resilience. Market share dynamics remained stable, with STO gaining 1.3ppts Y/Y helped by Danniao consolidation, while Yunda, YTO, and SF saw slight declines, reflecting ongoing consolidation and the importance of strategic differentiation in a more rational market environment.

# April ecommerce data demonstrates a meaningful deceleration, highlighting persistent softness in discretionary demand

- The latest NBS data for April reveal a clear slowdown in China's online retail sales, with growth moderating to $2.3\%$ Y/Y, down from $5.8\%$ in March. Online physical goods GMV grew just $0.2\%$ Y/Y in April, a significant deceleration from $2.5\%$ in March and marking the lowest monthly growth since December 2024. Online penetration of physical goods sales reached $25.7\%$ in April, up 0.6ppts Y/Y, but the underlying pace points to continued sluggish discretionary demand. Our internet team believes this softness signals downside risk for ecommerce companies' 2Q GMV and revenue, as the April trend sets a weaker tone for the quarter.   
- Category-level data for April show mounting pressure in home appliance and communication device sales, with both segments experiencing sharper declines. Home appliances sales dropped further to -15% Y/Y in April, compared to -5% Y/Y in March, while communication device sales growth slowed to 6% Y/Y, down from 27% in March. The pronounced deceleration across these categories is largely attributable to a still-high comparable base from last year (39% Y/Y for home appliances and 20% Y/Y for communication devices), as well as a less intensive subsidy program in 2026. With the comp base stepping up further into May and June, we expect continued pressure on JD's electronic sales in 2Q, as the sector faces both cyclical and policy-driven headwinds.   
- Apparel and daily-use product sales also reflect the broader deceleration in online discretionary demand, with apparel online sales growth slowing to 7% Y/Y in 4M26, from 12% in 1Q26. This suggests an 8% Y/Y decline in

April alone, per JPMe, indicating that the post-holiday pullback in March has persisted into the new quarter. Online food sales growth decelerated to 16% Y/Y in 4M26, from 17% in 1Q26, but the April growth rate accelerated marginally to c.11% on JPMe, from c.10% in March, providing a modest offset. Online daily-use products sales growth was 3% Y/Y in 4M26, suggesting a flat April, further underscoring the subdued consumer appetite for non-essential categories.

# Share price performance review

\- The logistics sector experienced broad underperformance in the latest period, as most names posted negative returns amid heightened concerns over rising fuel prices and cost pressures. This weakness was particularly pronounced among leading express delivery players, with JD Logistics (-16%), YTO Express (-15%), and ZTO Express (both H and US listings, -14% and -12% respectively) leading the declines. FTA was the only notable exception, delivering a positive return (+6%) despite the challenging backdrop. Broader indices, including HSCI (-4%) and Nasdaq Golden Dragon (-3%), also posted losses, but the logistics sector's declines were more severe, reflecting the market's acute sensitivity to input price volatility and the ongoing challenges in maintaining profitability. The sector's underperformance highlights the importance of cost discipline and strategic adaptation as companies navigate a more uncertain operating environment.

\- YTD performance reveals a clear divergence, with Tongda players and JD Logistics delivering substantial gains, supported by profitability improvement and robust earnings outlooks. YTO Express (+14%), STO Express (+14%), JD Logistics (+13%), and ZTO Express (H +7%, US +6%) outperformed, driven by anti-involution sustainability initiatives and margin expansion. This outperformance was concentrated among top-tier express delivery names, underscoring their ability to capture incremental market share and drive operational efficiency. In contrast, FTA (-18%), J&T (-14%), and Nasdaq Golden Dragon (-13%) lagged, reflecting persistent structural headwinds and weaker fundamentals. SF Holdings continued to underperform (-10% H, -9% A), weighed down by ongoing profitability concerns and slower strategic transformation. The sector's rally among leaders highlights the critical role of operational discipline, technology leadership, and strategic clarity in sustaining growth and navigating market volatility.

Figure 1: China logistics share price performance (past one month)   
![](images/a859a5bafa41afb50e3f3dfead035705e3f91ee7a2a08484ad572f8844faa1f3.jpg)

<details>
<summary>bar</summary>

| Company | Change (%) |
| :--- | :--- |
| FTA | 6 |
| Nasdaq Golden Dragon | -3 |
| HSCI | -4 |
| SF Holding - A | -5 |
| STO Express | -8 |
| J&T | -11 |
| YUNDA Holding | -12 |
| ZTO Express - US | -12 |
| SF Holding - H | -13 |
| ZTO Express - H | -14 |
| YTO Express | -15 |
| JD Logistics | -16 |
</details>

Source: Bloomberg Finance L.P. Note: Past performance is not an indicator of future results. Data as of 29 Mayl 2026.

Figure 2: China logistics share price performance (year to date)   
![](images/827b337aea27c0129c106ed63ebaf1e85b30153db6a7f6cba3042c2aec1f2fa1.jpg)

<details>
<summary>bar</summary>

| Entity | Value (%) |
| :--- | :--- |
| YTO Express | 14 |
| STO Express | 14 |
| JD Logistics | 13 |
| ZTO Express - H | 7 |
| ZTO Express - US | 6 |
| YUNDA Holding | 2 |
| HSCI | -4 |
| SF Holding - A | -9 |
| SF Holding - H | -10 |
| Nasdaq Golden Dragon | -13 |
| J&T | -14 |
| FTA | -18 |
</details>

Source: Bloomberg Finance L.P. Note: Past performance is not an indicator of future results. Data as of 29 May 2026.

Table 1: Snapshot of China's express parcel monthly data 

<table><tr><td></td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>2M26</td><td>Mar-26</td><td>Apr-26</td></tr><tr>

[中间内容因长度限制已省略]

aterial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
