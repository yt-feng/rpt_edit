你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# JPM

## China AI chip

Key takeaways from WAIC 2026: China's AI infrastructure shifts

Following our two-day visit to WAIC 2026, we believe China's AI infrastructure ecosystem has demonstrated a decisive shift from single-chip benchmarking to system-level deployment, and from capacity build-out to a genuine token economy. Our key takeaways are: 1) delivering single-chip performance at effective Hopper-class level has become the baseline, while Prefill/Decode-disaggregation architectures have moved from experimental to standard; 2) super-node solutions spanning dozens to thousands of cards have emerged as the critical system-level answer to process-node constraints, explicitly targeting trillion-parameter model deployment; and 3) making AI compute affordable and ubiquitous is the driving force, but deployment requires sustained ecosystem co-innovation. Our top picks within the ramping indigenous AI supply chain are Iluvatar CoreX, JCET, NAURA, and AMEC.

\- The baseline of chip performance has reset to Hopper-class. Even though domestic AI chip vendors remain focused on solving near-term capacity and supply bottlenecks, we believe the next imperative is delivering effective Hopper-class compute by late this year and into 2027. For instance, Iluvatar CoreX launched its Tiangai 300 chip, which claims $10 - 20\%$ superior performance versus Hopper architecture on selective inference metrics. The PD-disaggregation paradigm has become a well-recognized cost-reduction mechanism for LLM inference at scale, confirming inference as the proven commercial application for domestic GPUs. Training is now widely viewed as the next scalable and critical market.

\- Extensive showcase of super-node solutions. The most significant architectural development we noted at WAIC 2026 was the emergence of super-nodes as the industry's answer to two structural constraints: the ceiling on domestic process nodes and the arrival of trillion-parameter LLMs (e.g., Kimi K3's 2.8-trillion-parameter architecture). To overcome single-chip boundaries given the inferior absolute performance of local AI chips, super-nodes serve as unified compute domains, employing different approaches to chip-to-chip interconnection, switch/fabric design, and software across the ecosystem. Liquid cooling, optical interconnects, and orthogonal cabinet architectures are likely to become the minimum requirements rather than differentiators for next-generation deployments.

\- Transforming AI tokens into workforce. Agentic AI has emerged as the key application-layer force reshaping infrastructure demand going forward, as agents functioning as digital proxies consume tokens at rates several orders of magnitude higher than human users, creating an exponential demand curve. We believe the promotion of the token factory concept in China represents a deliberate industrialization strategy aimed at making AI tokens affordable and ubiquitous across numerous

See page 3 for analyst certification and important disclosures, including non-US analyst disclosures.

Technology

Billy Feng AC

(86-21) 6106 6359

billy.feng@JPM.com

Ri Xu

SAC Registration Number: S1730520030005

(86-21) 6106 6318

ri.xu@jpmchase.com

SAC Registration Number: S1730522100001

JPM Securities (China) Company Limited

real-world applications. However, the ecosystem remains immature in critical dimensions such as industry standards for heterogeneous scheduling, token quality measurement, and the optimal super-node scale (ranging from dozens to thousands cards) across different verticals, in our view.

\- Stock implications. We believe Iluvatar CoreX (OW) is best positioned among tier-2 AI chip players, backed by secured supply and design wins at top CSP customers. Additionally, we expect back-end service providers to benefit from increasing demand for advanced packaging and testing, thus we favor JCET (OW). We are also positive on the WFE sector, underpinned by strong capex for memory and advanced logic fabs, and NAURA (OW) and AMEC (OW) are our preferred names.

# Companies Discussed in This Report (all prices in this report as of market close on 20 July 2026, unless otherwise indicated)

AMEC - A(688012.SS/Rmb342.50/OW), Iluvatar CoreX - H(9903.HK/HK\$495.20[17 July 2026]/OW), JCET -

A(600584.SS/Rmb76.99/OW), NAURA - A(002371.SZ/Rmb676.91/OW)

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

\- Market Maker/ Liquidity Provider: JPM is a market maker and/or liquidity provider in the financial instruments of/related to JCET - A, NAURA - A, AMEC - A or related entities.

\- Manager or Co-manager: JPM acted as manager or co-manager in a public offering of securities or financial instruments (as such term is defined in Directive 2014/65/EU) of/for Iluvatar CoreX - H or related entities within the past 12 months.

\- Client: JPM currently has, or had within the past 12 months, the following entity(ies) as clients: Iluvatar CoreX - H, JCET - A or related entities.

- Client/Investment Banking: JPM currently has, or had within the past 12 months, the following entity(ies) as investment banking clients: Iluvatar CoreX - H or related entities.

\- Client/Non-Investment Banking, Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-investment-banking, securities-related: JCET - A or related entities.

\- Client/Non-Securities-Related: JPM currently has, or had within the past 12 months, the following entity(ies) as clients, and the services provided were non-securities-related: JCET - A or related entities.

\- Investment Banking Compensation Received: JPM has received in the past 12 months compensation for investment banking services from Iluvatar CoreX - H or related entities.

\- Potential Investment Banking Compensation: JPM expects to receive, or intends to seek, compensation for investment banking services in the next three months from Iluvatar CoreX - H, JCET - A or related entities.

\- Non-Investment Banking Compensation Received: JPM has received compensation in the past 12 months for products or services other than investment banking from JCET - A or related entities.

- Debt Position: JPM may hold a position in the debt securities of Iluvatar CoreX - H, JCET - A, NAURA - A, AMEC - A or related entities, if any.

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

Iluvatar CoreX - H (9903.HK, 9903 HK) Price Chart  
![](images/4f2c0fcba0b83b6b6e2737b9b3e3efdc7075659ce57e36e9337be787e077b394.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (HK$)</td><td>Price Target (HK$)</td></tr><tr><td>07-Apr-26</td><td>OW</td><td>219.80</td><td>620</td></tr><tr><td>28-Jun-26</td><td>OW</td><td>684.00</td><td>920</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 07, 2026. All share prices are as of market close on the previous business day.  
JCET - A (600584.SS, 600584 CH) Price Chart  
![](images/6a85ee6d462c994e32032ddf26f13e19c3f3d9725930a07c834b94e39d866dc4.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>05-Sep-23</td><td>OW</td><td>33.62</td><td>38</td></tr><tr><td>28-Aug-24</td><td>OW</td><td>30.10</td><td>43</td></tr><tr><td>27-Aug-25</td><td>N</td><td>38.99</td><td>43</td></tr><tr><td>28-Oct-25</td><td>N</td><td>42.09</td><td>45</td></tr><tr><td>16-Jun-26</td><td>OW</td><td>74.32</td><td>110</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Apr 26, 2021. All share prices are as of market close on the previous business day.

NAURA - A (002371.SZ, 002371 CH) Price Chart  
![](images/cf02e5ffcd5dc3ef4bb444b900b77701975a05ce594f46920725e22d44cc2c64.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>04-Nov-25</td><td>OW</td><td>401.00</td><td>610</td></tr><tr><td>30-Apr-26</td><td>OW</td><td>510.71</td><td>700</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Nov 04, 2025. All share prices are as of market close on the previous business day.

AMEC - A (688012.SS, 688012 CH) Price Chart  
![](images/05ebd22efafc3b5d989e4a8622c2301a9393d68d4df3f5c47b5220a92432efcc.jpg)

<table><tr><td>Date</td><td>Rating</td><td>Price (Rmb)</td><td>Price Target (Rmb)</td></tr><tr><td>29-Jul-24</td><td>OW</td><td>146.78</td><td>120</td></tr><tr><td>31-Oct-24</td><td>OW</td><td>181.15</td><td>131</td></tr><tr><td>20-Feb-25</td><td>OW</td><td>201.27</td><td>148</td></tr><tr><td>31-Aug-25</td><td>OW</td><td>214.17</td><td>155</td></tr><tr><td>24-Sep-25</td><td>OW</td><td>280.00</td><td>232</td></tr><tr><td>30-Oct-25</td><td>OW</td><td>296.66</td><td>237</td></tr><tr><td>11-Jan-26</td><td>OW</td><td>336.68</td><td>255</td></tr><tr><td>06-Apr-26</td><td>OW</td><td>293.50</td><td>269</td></tr><tr><td>28-Apr-26</td><td>OW</td><td>352.01</td><td>289</td></tr></table>

Source: Bloomberg Finance L.P. and JPM; price data adjusted for stock splits and dividends. Initiated coverage Jul 29, 2024. All share prices are as of market close on the previous business day.

The chart(s) show JPM's continuing coverage of the stocks; the current analysts may or may not have covered it over the entire period.

JPM ratings or designations: OW = Overweight, N = Neutral, UW = Underweight, NR = Not Rated

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Feng, Billy : AMEC - A (688012.SS), AtHub - A (603881.SS), China Resources Microelectronics - A (688396.SS), Dongshan Precision - A (002384.SZ), Gigadevice Semiconductor - A (603986.SS), Goertek - A (002241.SZ), Hangzhou HikVision Digital Technology Co., Ltd - A (002415.SZ), Huafeng Test & Control - A (688200.SS), Iluvatar CoreX - H (9903.HK), Inspur - A (000977.SZ), JCET - A (600584.SS), Luxshare - A (002475.SZ), Maxscend Microelectronics - A (300782.SZ), MetaX - A (688802.SH), NAURA - A (002371.SZ), OmniVision - A (603501.SS), Sinnet - A (300383.SZ), Universal Scientific Industrial (Shanghai) - A (601231.SS), Wingtech Tech - A (600745.SS), Zhejiang Dahua Technology Co., Ltd - A (002236.SZ), Zhongji Innolight - A (300308.SZ)

## JPM Equity Research Ratings Distribution, as of July 04, 2026

<table><tr><td></td><td>Overweight (buy)</td><td>Neutral (hold)</td><td>Underweight (sell)</td></tr><tr><td>JPM Global Equity Research Coverage*</td><td>53%</td><td>36%</td><td>12%</td></tr><tr><td>IB clients**</td><td>83%</td><td>80%</td><td>73%</td></tr><tr><td>JPMS Equity Research Coverage*</td><td>51%</td><td>37%</td><td>12%</td></tr><tr><td>IB clients**</td><td>95%</td><td>92%</td><td>87%</td></tr></table>

\*Please note that the percentages may not add to 100% because of rounding.  
\*\*Percentage of subject companies within each of the "buy," "hold" and "sell" categories for which JPM has provided investment banking services within the previous 12 months.

For purposes of FINRA ratings distribution rules only, our Overweight rating falls into a buy rating category; our Neutral rating falls into a hold rating category; and our Underweight rating falls into a sell rating category. Please note that stocks with an NR designation are not included in the table above. This information is current as of the end of the most recent calendar quarter.

Equity Valuation and Risks: For valuation methodology and risks associated with covered companies or price targets for covered companies, please see the most recent company-specific research report at http://www.JPMmarkets.com, contact the primary analyst or your JPM representative, or email research.disclosure.inquiries@JPM.com. For material information about the proprietary models used, please see the Summary of Financials in company-specific research reports and the Company Tearsheets, which are available to download on the company pages of our client website, http://www.JPMmarkets.com. This report also sets out within it the material underlying assumptions used.

## History of Investment Recommendations:

A history of JPM investment recommendations disseminated during the preceding 12 months can be accessed on the Research & Commentary page of http://www.JPMmarkets.com where you can also search by analyst name, sector or financial instrument.

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

Registration of non-US Analysts: Unless otherwise noted, the non-US analysts listed on the front of this report are employees of non-US affiliates of JPM Securities LLC, may not be registered as research analysts under FINRA rules, may not be associated persons of JPM Securities LLC, and may not be subject to FINRA Rule 2241 or 2242 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

## Other Disclosures

JPM is a marketing name for investm

[中间内容因长度限制已省略]

bject to

certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Securities (China) Company Limited. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
