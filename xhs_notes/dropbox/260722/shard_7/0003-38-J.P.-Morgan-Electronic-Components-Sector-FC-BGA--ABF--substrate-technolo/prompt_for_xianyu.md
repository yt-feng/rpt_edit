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

## Electronic Components Sector

FC-BGA (ABF) substrate technology seminar report

We invited Mr. Toshihiko Nishio of SBR Technology to conduct a seminar on future technological trends for flip chip ball grid array (FC-BGA) substrate (Ajinomoto build-up film [ABF] substrate) on July 14. Main topics of discussion included technological trends for cores (organic cores, glass cores, high-density interconnect [HDI] cores, and ceramic cores), embedded multi-die interconnect bridge with through-silicon vias (EMIB-T) from the standpoint of substrate, and trends for chip-on-wafer-on-substrate (CoWoS), chip-on-panel-on-substrate (CoPoS), and chip-on-wafer-on-platform (CoWoP). We provide an overview of the seminar below and summarize implications for the electronic components sector.

## Our view

\- For CoWoS and CoPoS, connection (soldering) reliability during mounting has become an issue due to larger reticle sizes, and it appears that this could necessitate the use of high-rigidity substrates and glass core substrates. Meanwhile, although EMIB-T achieves higher connection reliability than CoWoS and CoPoS as a result of not using an interposer, Mr. Nishio cited a need to establish both mass production capabilities for the substrate and assembly processes. Considering this point, we think that CoWoS and CoPoS will require substrate technologies that deliver high rigidity and flatness, and that larger reticle sizes could increase Ibiden's relative competitive advantages. We also think that Ibiden and other Japanese companies could become key suppliers for EMIB-T. We think larger reticle sizes could increase Ibiden's competitive advantages over the medium term.

## Seminar overview

\- CoWoS-S/CoWoS-L: (1) Chip-on-wafer-on-substrate with silicon interposer (CoWoS-S) is a structure in which a local silicon interconnect (LSI) and high-bandwidth memory (HBW) are mounted on a large silicon interposer, with ABF substrate below the interposer. However, as interposers increase in size, warping also increases and mounting (soldering) reliability decreases. Mr. Nishio said a reticle size of 3.3x is the upper limit for this reason. (2) Chip-on-wafer-on-substrate-large (CoWoS-L) does not use a silicon interposer, and instead has a structure in which redistribution layer (RDL) wiring is formed on a mold and silicon bridges are positioned at the connection points between LSIs and HBM. TSMC has disclosed plans to expand reticle size from 3.3x to 5.5x and then to 9.5x by 2029. However, ensuring flatness during assembly is difficult and connection problems are more severe because large blocks are formed using materials with different coefficients of thermal expansion (CTE; e.g., mold resin, copper RDL wiring, silicon bridges, chips, and ABF substrate). Rubin Ultra, based on a 5.5x reticle size, has faced difficulty in implementation evaluations, and Mr. Nishio thinks a 9.5x size will be very hard to achieve. Soldering has been identified as an issue for 9.5x reticle size as of 1H 2027, and although evaluations are currently underway for Rubin Ultra with 5.5x reticle size, Mr. Nishio said this is not going well. He said that if CoWoS-L with 9.5x reticle size does not succeed, limitations on packaging technology could make it difficult to achieve the Nvidia Feynman generation

Japan Equity Research Technology - Electronic Components

Akinori Kanemoto AC
(81-3) 6736 8628
akinori.kanemoto@JPM.com

Ikki Shibata
(81-3) 6736 8641
ikki.shibata@JPM.com
JPM Securities Japan Co., Ltd.

See page 4 for analyst certification and important disclosures, including non-US analyst disclosures.

in 2029. Substrate sizes also increase to $85mm \times 85mm$ for 3.3x reticle size, $110mm \times 110mm$ for 5.5x reticle size, and $130mm \times 140mm$ for 9.5x reticle size.

\- EMIB/EMIB-T: (1) EMIB is a packaging technology from Intel that embeds silicon bridges in the package substrate and connects LSI and HBM with localized fine-pitch wiring. Large silicon interposers are not required. The bump pitch for HBM4 could shrink from $65\mu \mathrm{m}$ to $36\mu \mathrm{m}$ in the future, and because this is finer than the typical LSI connection pitch, it requires high-density wiring between the HBM and LSI. (2) EMIB-T is a structure in which through-silicon vias (TSV) are formed in a silicon bridge to enable signal and power delivery to HBM and LSI from the substrate side. The ability to optimize power supply on the bridge enables the suppression of power noise in HBM operating at high frequencies and low voltages. In addition, because HBM and LSI with different sizes and connection conditions can be mounted individually on the substrate without using a large interposer, it eliminates the need to bond an entire large module at once, as is done with CoWoS-L, making the overall interposer less susceptible to warping and offering advantages for back-end process yields. Mr. Nishio said Intel claims EMIB-T can support up to 12x reticle size and can serve as an alternative for CoWoS-L. (3) While Intel has a mass production track record with conventional EMIB, Mr. Nishio explained that EMIB-T has not yet been established as a mass production technology, given a lack of reliable mass production capacity for external customers at Intel Foundry Services (IFS) and inadequate capabilities on the substrate side as well. Broadcom and Google have expressed interest, but whether Intel can launch EMIB-T as a mass production technology is a key focus point. (4) EMIB-T faces challenges not only for developing substrate but for assembly processes as well, but Mr. Nishio said IFS plans to license assembly technology to Amkor Technology and outsource assembly to Amkor.

\- CoPoS/CoWoP: (1) CoPoS is a production method in which the CoWoS processes that are normally done on a 300mm wafer are instead implemented on a 310mm square panel. This method improves productivity by using glass carriers and fully utilizing the area of a square panel. Mr. Nishio said the launch of this technology could proceed as TSMC plans, or could be delayed by up to around two years. However, Mr. Nishio believes this technology is relatively easy for TSMC to control, because any delays can be offset by increasing existing CoWoS capacity. (2) CoWoP is a packaging technology that Nvidia aims to adopt in the future. CoWoP eliminates conventional ABF substrate and directly mounts interposers equipped with graphics processing units (GPUs) and HBM on substrate-like printed circuit boards (SLP). Reducing the number of intermediate substrates is expected to simplify the structure, shorten signal paths, increase design flexibility for heat dissipation, and reduce costs. Mr. Nishio said Nvidia intends to reduce its reliance on Japanese substrate makers and use the PCB supply chains in Taiwan and China. (3) However, CoWoP requires miniaturization to an SLP trace width of 10μm or less for mass production, versus the current 15-20μm. Other remaining challenges include PCB processing precision, yield, and flip-chip mounting. Consequently, Nvidia needs to change chip-side wiring rules and bump pitch, but this would make standardization with existing CoWoS chips difficult. With Nvidia prioritizing support for the Feynman generation, Mr. Nishio believes it has limited capacity for simultaneously developing CoWoP as a separate technology, and has doubts about the feasibility of CoWoP. Mr. Nishio noted that while Nvidia's HGX products use SMX and have a dual-layer structure with one PCB mounted on another PCB, it might want to eliminate the intermediate PCB in this dual-layer structure.

\- Organic cores: (1) ABF substrates that use an organic core are currently the mainstream for advanced packaging. The shift to chiplets and the increase in package sizes have created a need for larger substrates. Packaging is also embedding a rising percentage of silicon components, such as AI chips and HBM. CTE mismatches between substrate and chips cause warping during assembly and solder connection failures. It is important for organic cores to have low CTE and high rigidity. (2) Nittobo's T-glass is a type of glass cloth used in organic cores, and its ability to control substrate CTE and help to improve strength and electrical properties make it an extremely important material. At present, other glass cloth makers such as Taiwan Glass are unable to keep pace technologically, and Mr. Nishio said Nittobo is effectively the only supplier for high-end products. Nittobo is moving forward with capex in response to requests to increase production from Nvidia, Broadcom, and other end-users, but because it also sees risk from competitors catching up and future oversupply, Mr. Nishio said it is gradually expanding capacity while watching demand. (3) Low CTE and high rigidity make substrate harder and increases the difficulty of drilling. Mr. Nishio said Union Tool is the leader in supplying drilling tools capable of stable micro-hole machining in such hard materials, and other companies are unable to keep pace.

\- Glass cores: Glass cores are superior in terms of low CTE, high rigidity, and flatness, and can mitigate warping in large packaging. Consequently, Mr. Nishio said Intel, AMD, and others view glass cores as a future core material. While many substrate makers are developing glass cores, virtually none are capable of mass production, and Mr. Nishio said Absolics is currently the only company that has mass production facilities and has advanced to the stage of small-scale production. Ibiden, Shinko Electric Industries, and Unimicron are still at the development stage and have not announced specific start dates for mass production. Samsung Electro-Mechanics announced the construction of a mass production plant with Sumitomo Chemical and plans to start mass production prototyping from 2028, but customer certifications will take time after completing plant production. Mr. Nishio said Dai Nippon Printing has not made a decision on full-scale investment. Consequently, glass cores still have inadequate infrastructure, including mass production plants, and Mr. Nishio thinks mass production will be difficult until 2030. The recent announcement at the JPCA Show 2026 that TSMC will cooperate with Ibiden and Innolux to develop glass core substrate for CoPoS has attracted attention.

\- Other core materials: (1) HDI cores replace conventional cores comprised of two layers of copper clad laminate (CCL) with around eight HDI layers (multilayer PCB). HDI cores make it easier to use existing PCB technologies than glass cores, and evaluations are underway. However, substrate makers will need to cooperate with external parties if they are unable to make high-rigidity cores in-house, resulting in a more complex supply chain. Mr. Nishio said production is currently not possible at either Ibiden or Shinko Electric Industries. (2) Regarding ceramic cores, ceramic substrate was used in IBM mainframes and Intel products from the 1980s to the 1990s, and although the mainstream then shifted to organic, there are existing material technologies and mass production plants for ceramic. Mr. Nishio said ceramic cores have attracted attention as one option amid the slow launch of glass cores, but also noted lingering issues in terms of drilling holes in ceramic and bonding with ABF.

Analyst Certification: The Research Analyst(s) denoted by an “AC” on the cover of this report certifies (or, where multiple Research Analysts are primarily responsible for this report, the Research Analyst denoted by an “AC” on the cover or within the document individually certifies, with respect to each security or issuer that the Research Analyst covers in this research) that: (1) all of the views expressed in this report accurately reflect the Research Analyst’s personal views about any and all of the subject securities or issuers; and (2) no part of any of the Research Analyst's compensation was, is, or will be directly or indirectly related to the specific recommendations or views expressed by the Research Analyst(s) in this report. For all Korea-based Research Analysts listed on the front cover, if applicable, they also certify, as per KOFIA requirements, that the Research Analyst’s analysis was made in good faith and that the views reflect the Research Analyst’s own opinion, without undue influence or intervention.

All authors named within this report are Research Analysts who produce independent research unless otherwise specified. In Europe, Sector Specialists (Sales and Trading) may be shown on this report as contacts but are not authors of the report or part of the Research Department.

## Important Disclosures

Company-Specific Disclosures: JPM does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. Important disclosures, including price charts and credit opinion history tables (if applicable), are available for compendium reports and all JPM-covered companies, and certain non-covered companies, by visiting https://www.jpmm.com/research/disclosures, calling 1-800-477-0406, or e-mailing research.disclosure.inquiries@JPM.com with your request.

## Explanation of Equity Research Ratings, Designations and Analyst(s) Coverage Universe:

JPM uses the following rating system: Overweight (over the duration of the price target indicated in this report, we expect this stock will outperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); Neutral (over the duration of the price target indicated in this report, we expect this stock will perform in line with the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe); and Underweight (over the duration of the price target indicated in this report, we expect this stock will underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe. NR is Not Rated. In this case, JPM has removed the rating and, if applicable, the price target, for this stock because of either a lack of a sufficient fundamental basis or for legal, regulatory or policy reasons. The previous rating and, if applicable, the price target, no longer should be relied upon. An NR designation is not a recommendation or a rating. Some stocks under coverage have a rating but no price target; in these cases, we expect the stock will outperform/perform in line/underperform the average total return of the stocks in the Research Analyst's, or the Research Analyst's team's, coverage universe of the relevant duration of the region. In our Asia (ex-Australia and ex-India) and U.K. small- and mid-cap Equity Research, each stock's expected total return is compared to the expected total return of a benchmark country market index, not to those Research Analysts' coverage universe. If it does not appear in the Important Disclosures section of this report, the certifying Research Analyst's coverage universe can be found on JPM's Research website, https://www.JPMmarkets.com.

Coverage Universe: Kanemoto, Akinori : Alps Alpine (6770) (6770.T), Hirose Electric (6806) (6806.T), Ibiden (4062) (4062.T), Japan Aviation Electronics (6807) (6807.T), Kyocera (6971) (6971.T), MinebeaMitsumi (6479) (6479.T), Murata Manufacturing (6981) (6981.T), NISSHA (7915) (7915.T), Nichicon (6996) (6996.T), Nidec (6594) (6594.T), Nippon Chemi-Con (6997) (6997.T), Niterra (5334) (5334.T), Rohm (6963) (6963.T), TDK (6762) (6762.T), Taiyo Yuden (6976) (6976.T), Wacom (6727) (6727.T)

## JPM Equity Resea

[中间内容因长度限制已省略]

 forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not

Completed 21 Jul 2026 11:04 AM JST
"""
