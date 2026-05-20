你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
IT Hardware and Communications Equipment

# Highlights from Meetings in Asia

We met with companies across the IT Hardware supply chain in Asia last week. The takes were positive, as demand across segments was favorable. A lot of the incremental discussion was on capacity limitations, component shortages, and multi sourcing. We remain positive on our AI focused names.

# Compute

Our take from the compute ecosystem is that demand continues to outstrip supply, with not much relief in sight. We have a favorable view on most of our companies that have exposure.

# TPU

When we visited Asia six months ago, one of our main calls was being positive on TPU-exposed vendors as we heard of a doubling of capacity in early 2026, and a potential raise of $50\%$ in mid-2026. We believe this is developing at or above that plan. Most EMS vendors have a play here.

- CLS. We view CLS as the main supplier to TPU and variants, regardless of silicon provider. We are modeling more than a double of TPU-related revenues in 2026 to \$2.8Bn from \$1Bn in 2025. We are less concerned about others being added to the supply chain given the overall growth profile of TPU.   
- FLEX. FLEX has traditionally been the second source for CPU manufacture. While there has been some concern about share loss, we think FLEX is still involved, even if revenues don't grow like the rest of the ecosystem. FLEX would likely supply lower related products to this ecosystem as well.   
- JBL. While we do not believe JBL is directly linked to TPU, the company makes the test equipment for the main provider of testing hardware. We see steady growth in testing capacity as a positive for this segment at JBL.   
- Other ODMs. We believe there is more ODM activity in this supply chain, particularly for the TPU motherboard and the full rack assembly, where GOOG had been vertically integrated. We don't view these changes as meaningful to our companies at this time.

# Trainium

The supply chain sees solid Trainium unit growth this year, but not to the magnitude of TPU. We believe something like $30\%+$ is more reasonable, and potentially higher if the solution is more broadly adopted by other cloud players.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

IT Hardware and Communications

Equipment

NEUTRAL

# IT Hardware and Communications

# Equipment

# Tim Long

+1 212 526 4043

tim.long@BARC.com

BCI, US

Alyssa Shreves

+1 212 526 7570

alyssa.shreves@BARC.com

BCI, US

Mary Lenox

+1 212 526 6277

mary.lenox@BARC.com

BCI, US

Clarisse Yu

+1 212 526 7025

xueqian.yu@BARC.com

BCI, US

- FN. The ramp at FN has been impressive, even with the slight miss last quarter. We believe the increased production lines and incremental business will lead to a further ramp of revenues over the next year or two. We did not pick up any indications of a third source entering this market.   
- JBL. For full racks, we believe JBL entered the supply chain in a more meaningful way in mid-2025 with increased Trainium rack construction in a competitive win.

# Other accelerator

We have been disappointed by the other major accelerator launch expected over the last few years. There seems to be a little activity with MSFT's Maia program, though timing and volumes are still uncertain. The META project seems to be further from commercialization. It's unclear at this time if the NA EMS companies will have a meaningfully play in this area.

\- NVDA GPU and AMD. While the supply chain mentions potential delays to both programs, we see strong ramps at the end of this year. Many of our companies play across these ecosystems.

- DELL should remain strongly positioned in GPU based servers given the issues at SMCI and the new capacity coming on-line in Texas.   
- CLS looks well positioned to win scale up Ethernet business as these AI clusters ramp.   
• FN is a leading supplier of transceivers to NVDA, and 1.6T should start to reinvigorate growth.   
- JBL is one of the manufacturers for NVDA's switching equipment, which is often pulled through with compute.   
- FLEX would be one of the suppliers to power systems and potentially racks for these deployments.   
- ANET would be well positioned for the AI front and back ends in AMD clusters.   
• SANM (not covered) would also be well positioned in AMD powered data centers as per indications from our meetings.

# Cloud CPU

Compared to six months ago, the outlook for general purpose CPU is much improved with unit discussions moving from flat to up 20-40%, and higher ASPs. A lot of this supply chain favors Asian ODMs over North American EMS, but the increased builds should provide a more favorable backdrop for EMS and the networking companies.

# Enterprise

The tone for enterprise server has been somewhat consistent with talk of flat to slightly growing units and higher ASPs. DELL was highlighted as doing well here.

# Networking

There is less networking in the Asia supply chain, though we did meet with one of the major white box players, and had reads from other industry participants.

# DC Switching

Demand for switching is strong and is tracking with increased compute spend. Scale up Ethernet is in the early phases but seems like it could be a 2027 driver for the ecosystem.

\- CLS. While we heard no direct data points, the switching TAM for those using white box continues to expand, and we view CLS as the main beneficiary. We heard of a ramp at AWS from a major WB competitor, but we still see leading share and strong growth for CLS. Meta will likely remain more competitive for all players.

\- JBL. We believe JBL is the time beneficiary for NVDA switches. Given the strong GPU outlook, we see continued growth here.

\- ANET. We came away with two indirect positives for ANET in our meetings. First, the inflection in Cloud CPU servers is meaningful for the front end networking market, where we view ANET as a leader. Second, there did not seem to be much activity for newer cloud companies accelerating their white box strategies. As such, we see a lot more new customer activity for the best-in-breed branded vendor, with CSCO also seeing opportunities.

# Campus Switching

Like with the enterprise server market, there was not a lot of growth expectation for campus switching and WiFi. The supply chain sees LSD-MSD, just at the low end of our model. JNPR/HPE was highlighted as doing well.

# Power

The power market is much more fragmented as products span the boards, racks, and full data centers. It was clear from our meetings that the incremental power (and cooling) requirements per rack are growing. It's hard to put a number to this growth, but in-line with compute could be a good proxy.

\- FLEX. FLEX is the most exposed to power with \$2.1Bn of revenue in FY26 growing 61%. With the announcement of an almost 2x of growth in FY27 and FY28 for the cloud/AI business, we view the company as a market share gainer in this segment.

\- JBL. We estimate JBL annual power revenues at \~\$600M/year and also growing 30%+. The recent addition of Hanley should further bolster this business.

# Devices

The device segment is being much more impacted by the increased memory prices given more exposure, and more of a consumer mix in the end market.

\- PCs. We recently discussed weak numbers across the PC supply chain for the month of April. The ODM are expecting a rebound later in Q2, and most are expecting units to be down $5 - 10\%$ for the year, slightly better than our industry model.

\- Smartphones. Similarly, unit expectations for phones are weak this year. We did hear about some weakness creeping into the high-end Android market (excluding Samsung), which we view as new. iPhones continue to sell well in China, with some industry participants seeing pricing/promotion activity from the high-end vendor helping to maintain the momentum. We question the sustainability for AAPL.

\- Cameras. We met with a leading video security company that competes with MSI. While there are some pressures, there is more of a secular growth dynamic in security. We believe increased ASPs will help revenues across the ecosystem, and we also see MSI as a share gainer.

# Analyst(s) Certification(s):

I, Tim Long, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

# Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC"). All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

# Availability of Disclosures:

Where any companies are the subject of this research report, for current important disclosures regarding those companies please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

The analysts responsible for preparing this research report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by investment banking activities, the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst.

Research analysts employed outside the US by affiliates of BARC Capital Inc. are not registered/qualified as research analysts with FINRA. Such non-US research analysts may not be associated persons of BARC Capital Inc., which is a FINRA member, and therefore may not be subject to FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst's account.

Analysts regularly conduct site visits to view the material operations of covered companies, but BARC policy prohibits them from accepting payment or reimbursement by any covered company of their travel expenses for such visits.

BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

# Materially Mentioned Stocks (Ticker, Date, Price)

Apple, Inc. (AAPL, 15-May-2026, USD 300.23), Underweight/Neutral, CD/CE/D/E/J/K/L/M/N

Arista Networks, Inc. (ANET, 15-May-2026, USD 141.97), Overweight/Neutral, J

Celestica Inc. (CLS, 15-May-2026, USD 358.55), Overweight/Neutral, J

Cisco Systems, Inc. (CSCO, 15-May-2026, USD 118.21), Equal Weight/Neutral, CD/CE/D/J/K/L/M

Dell Technologies Inc. (DELL, 15-May-2026, USD 241.99), Overweight/Neutral, A/D/E/J/K/L/M/N

Fabrinet (FN, 15-May-2026, USD 722.04), Overweight/Neutral, CE/J

Flex Ltd (FLEX, 15-May-2026, USD 137.86), Overweight/Neutral, A/CD/CE/D/J/K/L/M/N

Jabil (JBL, 15-May-2026, USD 339.82), Overweight/Neutral, CD/CE/J

Motorola Solutions, Inc. (MSI, 15-May-2026, USD 393.28), Overweight/Neutral, CD/J

Unless otherwise indicated, prices are sourced from Bloomberg and reflect the closing price in the relevant trading market, which may not be the last available closing price at the time of publication.

# Disclosure Legend:

A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of the issuer in the previous 12 months.

B: An employee or non-executive director of BARC PLC is a director of this issuer.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by this issuer.

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by this issuer.

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Conduct) in respect of this issuer.

D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from this issuer in the past 12 months.

E: BARC Bank PLC and/or an affiliate expects to receive or intends to seek compensation for investment banking services from this issuer within the next 3 months.

FA: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with US regulations.

FB: BARC Bank PLC and/or an affiliate beneficially owns a long position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FC: BARC Bank PLC and/or an affiliate beneficially owns a short position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FD: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with South Korean regulations.

FE: BARC Bank PLC and/or its group companies has financial interests in relation to this issuer and such interests aggregate to an amount equal to or more than 1% of this issuer's market capitalization, as calculated in accordance with HK regulations.

GD: One of the Research Analysts on the fundamental credit coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

GE: One of the Research Analysts on the fundamental equity coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

H: This issuer beneficially owns more than 5% of any class of common equity securities of BARC PLC.

I: BARC Bank PLC and/or an affiliate is party to an agreement with this issuer for the provision of financial services to BARC Bank PLC and/or an affiliate.

J: BARC Bank PLC and/or an affiliate is a liquidity provider and/or trades regularly in the securities of this issuer and/or in any related derivatives.

K: BARC Bank PLC and/or an affiliate has received non-investment banking related compensation (including compensation for brokerage services, if applicable) from this issuer within the past 12 months.

L: This issuer is, or during the past 12 months has been, an investment banking client of BARC Bank PLC and/or an affiliate.

M: This issuer is, or during the past 12 months has been, a non-investment banking client (securities related services) of BARC Bank PLC and/or an affiliate.

N: This issuer is, or during the past 12 months has been, a non-investment banking client (non-securities related services) of BARC Bank PLC and/or an affiliate.

O: Not in use.

P: A partner, director or officer of BARC Capital Canada Inc. has, during the preceding 12 months, provided services to the subject company for remuneration, other than normal course investment advisory or trade execution services.

Q: BARC Bank PLC and/or an affiliate is a Corporate Broker to this issuer.

R: BARC Capital Canada Inc. has received compensation for investment banking services from this issuer in the past 12 months.

S: This issuer is a Corporate Broker to BARC PLC.

T: BARC Bank PLC and/or an affiliate is providing investor engagement services to this issuer.

U: The equity securities of this Canadian issuer include subordinate voting restricted shares.

V: The equity securities of this Canadian issuer include non-voting restricted shares.

# Risk Disclosure(s)

Master limited partnerships (MLPs) are pass-through entities structured as publicly listed partnerships. For tax purposes, distributions to MLP unit holders may be treated as a return of principal. Investors should consult their own tax advisors before investing in MLP units.

# Disclosure(s) regarding Information Sources

Bloomberg® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

# Guide to the BARC Fundamental Equity Research Rating System:

Our coverage analysts use a relative rating system in which they rate stocks as Overweight, Equal Weight or Underweight (see definitions below) relative to other companies covered by the analyst or a team of analysts that are deemed to be in the same industry (the "industry coverage universe").

In addition to the stock rating, we provide industry views which rate the outlook for the industry coverage universe as Positive, Neutral or Negative (see definitions below). A rating system using terms such as buy, hold and sell is not the equivalent of our rating system. Investors should carefully read the entire research report including the definitions of all ratings and not infer its contents from ratings alone.

# Stock Rating

Overweight - The stock is expected to outperform the unweighted expected total return of the industry coverage universe over a 12-month investment horizon.

Equal Weight - The stock is expected to perform in line with the unweighted expected total return of the industry coverage universe over a 12-month investm

[中间内容因长度限制已省略]

scope of its existing DFSA licence. Related financial products or services are only available to Professional Clients, as defined by the Dubai Financial Services Authority. BARC Bank PLC in the

UAE is regulated by the Central Bank of the UAE and is licensed to conduct business activities as a branch of a commercial bank incorporated outside the UAE in Dubai (Licence No.: 13/1844/2008, Registered Office: Building No. 6, Burj Dubai Business Hub, Sheikh Zayed Road, Dubai City) and Abu Dhabi (Licence No.: 13/952/2008, Registered Office: Al Jazira Towers, Hamdan Street, PO Box 2734, Abu Dhabi). This material does not constitute or form part of any offer to issue or sell, or any solicitation of any offer to subscribe for or purchase, any securities or investment products in the UAE (including the Dubai International Financial Centre) and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
