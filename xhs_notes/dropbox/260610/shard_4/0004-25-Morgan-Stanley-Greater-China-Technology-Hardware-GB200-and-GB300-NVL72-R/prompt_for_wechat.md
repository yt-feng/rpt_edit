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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 8, 2026 03:55 PM GMT

# Greater China Technology Hardware | Asia Pacific GB200 and GB300 NVL72 Racks in May 2026

We provide our monthly and quarterly rack shipment forecasts for ODMs. Within the major GPU AI server ODMs, our order of preference is Wistron > Hon Hai > Quanta, based on upside to price target.

## Key Takeaways

We estimate GB200/300 rack output in May 2026 at \~7.7K (-7% m/m), within which:  
Quanta shipped 1.8-1.9K GB200/GB300 racks.  
Wistron shipped 1.3-1.4K GB200/GB300 racks.  
Hon Hai shipped \~3.3K GB200/300 racks.

We continue to forecast 70-80K racks in CY26: This year should remain a strong one for downstream rack assembly. We expect over 100% y/y growth in rack shipments, vs. \~29k last year.

We believe actual rack deliveries to end-customers are likely lower than these numbers because we include Wistron's computing tray (L10) rack equivalent (without accounting for rack assembly and test times for L11).

Quanta (2382.TW, OW): May revenue was NT\$311.5bn (-8% m/m, +94% y/y). We attribute the m/m decline primarily to lower GB200/300 rack shipments in the month, while NB shipments were flat m/m at 3.5mn units. But for GB200/300 rack shipments in the month, we estimate Quanta shipped 1.8-1.9K, slightly lower than the \~2.1K racks shipped in April. Given the lower May, we think overall 2Q shipments will likely come down slightly to \~6.7K (+40% q/q), with the lowered rack shipments pushed out into 2H and the full-year remaining unchanged at \~18.7K racks.

Wistron (3231.TW, OW): May revenue was NT\$290bn (+2% m/m, +39% y/y). We attribute the m/m growth to 1) higher revenue from Wiwynn (revenue grew 2% m/m, to NT\$84.1bn), 2) higher monitor shipments at 950K units (+6% m/m), 3) slightly higher GB200/300 server computing tray shipments (1,300-1,400 rack equivalents, by our estimates, 2% higher m/m), despite slightly lower NB units at 1.7mn (-6% m/m) and lower DT units at 600k (-25% m/m). We maintain our 2Q rack shipment estimate at \~4.2K (+4% q/q), implying \~1.5K rack equivalents in June.

Hon Hai (2317.TW, OW, covered by Sharon Shih): Based on our checks, Hon Hai's GB rack shipments were down \~11% m/m in May, to 3.3K. For 2Q26, we think Hon Hai should continue to increase AI server rack shipments q/q, with 2Q26 AI rack shipments expected to reach \~10K units (+18% q/q).

MS TAIWAN LIMITED+

## Howard Kao

Equity Analyst

Howard.Kao@morganstanley.com +886 2 2730-2989

## Sharon Shih

Equity Analyst

Sharon.Shih@morganstanley.com +886 2 2730-2865

## Irene Yen

Research Associate

Irene.Yen@morganstanley.com +886 2 2730-2869

![](images/0f9fc14a646c498541b18adad94ed8b0026f738289549f9b8a31bf4051346c1a.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## GREATER CHINA TECHNOLOGY HARDWARE

Asia Pacific

Industry View

In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## GB200/300 Exhibits

Exhibit 1: Industry-wide GB200/300 NVL72-equivalent monthly rack output, by major ODMs (2025)  
![](images/f1d3a4344d85d278309382d87ab16aa3faeb3d6db16d8f19b6570453aa56e6b7.jpg)

<details>
<summary>stacked bar chart</summary>

GB200/300 NVL72 racks by major ODMs (000s)
| Quarter | Total (000s) | Blue Segment | Beige Segment | Green Segment | Yellow Segment |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1Q | 0.9 | 0.5 | 0.2 | 0.1 | 0.0 |
| 2Q | 4.3 | 1.8 | 1.2 | 1.5 | 0.1 |
| 3Q | 8.3 | 3.5 | 1.5 | 1.0 | 0.3 |
| 4Q | 15.5 | 6.5 | 2.5 | 2.0 | 0.5 |
</details>

Source: MS estimates.

Exhibit 2: Industry-wide GB200/300 NVL72-equivalent monthly rack output, by major ODMs (2026)  
![](images/f8b115fa80d3f5db0e8064c0c001a1590d88ac4ff22a3c303e744a028cf5c813.jpg)

<details>
<summary>stacked bar chart</summary>

GB200/300 NVL72 racks by major ODMs (000s)
| Quarter | Hon Hai | Quanta | Wistron | Wiwynn | Others |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1Q | 15.0 | 8.0 | 6.0 | 0.0 | 5.6 |
| 2Q | 16.0 | 9.0 | 6.0 | 0.0 | 6.3 |
| 3Q | 12.0 | 8.0 | 4.0 | 0.0 | 5.5 |
| 4Q | 8.0 | 4.0 | 4.0 | 0.0 | 5.0 |
</details>

Source: MS estimates.

Exhibit 3: Industry-wide GB200/300 NVL72-equivalent monthly rack output, by major ODMs (2025-2026)  
![](images/f4a1827a27d47e900b2534b903f3cfb121254ecfdab15b1826055e4fb5ed0c08.jpg)

<details>
<summary>stacked bar chart</summary>

GB200/300 NVL72 racks by major ODMs (000s)
| Month | Hon Hai | Quanta | Wistron | Wiwynn | Others |
|---|---|---|---|---|---|
| Jan | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 |
| Feb | 0.3 | 0.1 | 0.0 | 0.0 | 0.0 |
| Mar | 0.5 | 0.1 | 0.1 | 0.0 | 0.0 |
| Apr | 0.7 | 0.2 | 0.2 | 0.0 | 0.0 |
| May | 1.8 | 0.4 | 1.6 | 0.0 | 0.0 |
| Jun | 1.8 | 0.5 | 1.2 | 0.0 | 0.1 |
| Jul | 1.7 | 0.6 | 0.8 | 0.1 | 0.1 |
| Aug | 2.4 | 0.4 | 0.3 | 0.2 | 0.1 |
| Sep | 4.2 | 1.2 | 1.1 | 0.3 | 0.3 |
| Oct | 4.2 | 1.4 | 0.5 | 0.1 | 0.5 |
| Nov | 5.4 | 1.9 | 2.3 | 0.3 | 0.6 |
| Dec | 5.9 | 2.4 | 1.4 | 0.3 | 0.6 |
| Jan | 5.9 | 2.3 | 1.4 | 0.1 | 1.6 |
| Feb | 6.3 | 2.2 | 2.1 | 0.1 | 1.6 |
| Mar | 8.5 | 3.3 | 2.3 | 0.1 | 1.7 |
| Apr | 8.3 | 3.4 | 1.9 | 0.1 | 1.7 |
| May | 7.7 | 3.2 | 2.1 | 0.1 | 1.7 |
</details>

Source: MS estimates.

Exhibit 4: GB200/300 rack supply share, by major ODMs (2025)  
![](images/d8d2b16fdc0f99a355a659a9179df8c66b1c6b0ff5793c95df2ab74299dfc124.jpg)

<details>
<summary>pie chart</summary>

GB200/300 NVL72-equivalent rack supply share (2025)
| Company | Share (%) |
|---|---|
| Hon Hai | 51 |
| Quanta | 21 |
| Wistron | 20 |
| Others | 6 |
| Wiwynn | 2 |
</details>

Source: MS estimates.

Exhibit 5: GB200/300 rack supply share, by major ODMs (2026)  
![](images/02325210dc1da17aed3b7b9642f38aad67729d8f441ce9480fe0c62f9cdbdc32.jpg)

<details>
<summary>pie chart</summary>

GB200/300 NVL72-equivalent rack supply share (2026)
| Company | Share (%) |
| :--- | :--- |
| Hon Hai | 41 |
| Quanta | 24 |
| Wistron | 18 |
| Others | 17 |
| Wiwynn | 0 |
</details>

Source: MS estimates.

## Valuation Methodology and Risks

## Hon Hai Precision (2317.TW)

Base case scenario value, derived from a residual income valuation model. Our key assumptions include a cost of equity of 8.5%, a medium-term growth rate of 13%, and a terminal growth rate of 3%.

## Risks to Upside

■ Better-than-expected iPhone sell-through  
■ Faster progress in AI server business  
■ Faster EV business development progress  
■ Any new M&A activity that could improve sentiment

## Risks to Downside

■ Lower iPhone sell-through  
■ Smaller profit contribution from AI business  
■ Slower EV business development progress  
■ Geopolitical developments that could negatively affect foreign investment

## Quanta Computer Inc. (2382.TW)

Base case, residual income model. Key assumptions include a cost of equity of 9.0% (beta of 1.2, equity premium of 6.0% and risk-free rate of 1.5%), an 8.5% medium-term growth rate, and a 3% terminal growth rate.

## Risks to Upside

■ Stronger-than-expected NB demand  
■ Stronger-than-expected Apple Watch demand  
■ Stronger-than-expected server demand  
■ Faster-than-expected AI server penetration

## Risks to Downside

■ Weaker-than-expected NB demand  
■ Softer-than-expected Apple Watch demand  
■ Weak margin performance owing to rising labor costs and sales shortfalls  
■ Fierce price competition in the mega data center segment  
■ Slower-than-expected AI server penetration

## Wistron Corporation (3231.TW)

Base case, residual income valuation. Key assumptions: 8.7% cost of equity, 7.0% medium-term growth rate and 3% terminal growth rate.

## Risks to Upside

■ Faster-than-expected divestiture of consumer electronics business  
■ Stronger-than-expected NB demand  
■ Margin expansion from better product mix

■ Faster-than-expected AI server penetration

## Risks to Downside

■ Slower-than-expected divestiture of consumer electronics business  
■ Weaker-than-expected NB demand  
■ Margin contraction from sales shortfall and fierce competition  
■ Slower-than-expected AI server penetration

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Howard Kao; Sharon Shih.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned $1\%$ or more of a class of common equity securities of the following companies covered in MS: AAC Technologies Holdings, Accelink Technologies Co. Ltd., Accton Technology Corporation, AirTAC International, Asia Vital Components Co. Ltd., Auras Technology Co Ltd, Bizlink, Catcher Technology, Chenbro, Chroma Ate Inc., Delta Electronics Inc., E Ink Holdings Inc., Eoptolink Technology Inc Ltd, Fositek Corp, Genius Electronic Optical Co. Ltd., Giga-Byte Technology Co. Ltd., Gold Circuit Electronics Ltd., Hiwin Technologies Corp., Inspur Electronic Information, LandMark Optoelectronics Corporation, Lens Technology, Luxshare Precision Industry Co., Ltd., Nan Ya PCB, Pegatron Corporation, Radiant Opto-Electronics Corporation, Sunny Optical, Sunonwealth Electric Machine Industry Co, Suzhou TFC Optical Communication Co Ltd., Tong Hsing, Unimicron, Visual Photonics Epitaxy Co Ltd, Wistron Corporation, Wiwynn Corp, Xiaomi Corp, Yageo Corp., Zhejiang Crystal-Optech Co Ltd, Zhen Ding, Zhongji Innolight Co Ltd, ZTE Corporation.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Wistron Corporation, Wiwynn Corp, Zhen Ding.

Within the last 12 months, MS has received compensation for investment banking services from Lenovo, Wistron Corporation, Wiwynn Corp, Xiaomi Corp, Yageo Corp., Zhen Ding. In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from AAC Technologies Holdings, Accton Technology Corporation, Acer Inc., Advantech, AirTAC International, Asia Vital Components Co. Ltd., Asustek Computer Inc., AU Optronics, Bizlink, Catcher Technology, Chenbro, Compal Electronics, Delta Electronics Inc., E Ink Holdings Inc., Ennostar Inc, Eoptolink Technology Inc Ltd, FIT Hon Teng Ltd, Giga-Byte Technology Co. Ltd., GoerTek Inc, Gold Circuit Electronics Ltd., Hon Hai Precision, Innolux, Lenovo, Lens Technology, Lingyi Itech Guangdong Co, Lite-On Technology, Luxshare Precision Industry Co., Ltd., Pegatron Corporation, Q Technology (Group) Company Ltd, Quanta Computer Inc., Sanan Optoelectronics, Shenzhen Transsion Holdings Co Ltd, Suzhou TFC Optical Communication Co Ltd., TCL Corp., Unimicron, Wistron Corporation, Wiwynn Corp, Xiaomi Corp, Yageo Corp., Yangtze Optical Fibre and Cable JSC Ltd, Zhen Ding, Zhongji Innolight Co Ltd.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from AAC Technologies Holdings, Accton Technology Corporation, Acer Inc., Asustek Computer Inc., AU Optronics, BYD Electronics, Compal Electronics, E Ink Holdings Inc., Eoptolink Technology Inc Ltd, Foxconn Technology, Giga-Byte Technology Co. Ltd., GoerTek Inc, Hon Hai Precision, Innolux, Lenovo, Lingyi Itech Guangdong Co, Quanta Computer Inc., Xiaomi Corp, Yageo Corp..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: AAC Technologies Holdings, Accton Technology Corporation, Acer Inc., Advantech, AirTAC International, Asia Vital Components Co. Ltd., Asustek Computer Inc., AU Optronics, Bizlink, Catcher Technology, Chenbro, Compal Electronics, Delta Electronics Inc., E Ink Holdings Inc., Ennostar Inc, Eoptolink Technology Inc Ltd, FIT Hon Teng Ltd, Giga-Byte Technology Co. Ltd., GoerTek Inc, Gold Circuit Electronics Ltd., Hon Hai Precision, Innolux, Lenovo, Lens Technology, Lingyi Itech Guangdong Co, Lite-On Technology, Luxshare Precision Industry Co., Ltd., Pegatron Corporation, Q Technology (Group) Company Ltd, Quanta Computer Inc., Sanan Optoelectronics, Shenzhen Transsion Holdings Co Ltd, Suzhou TFC Optical Communication Co Ltd., TCL Corp., Unimicron, Wistron Corporation, Wiwynn Corp, Xiaomi Corp, Yageo Corp., Yangtze Optical Fibre and Cable JSC Ltd, Zhen Ding, Zhongji Innolight Co Ltd.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: AAC Technologies Holdings, Accton Technology Corporation, Acer Inc., Asustek Computer Inc., AU Optronics, BYD Electronics, Compal Electronics, E Ink Holdings Inc., Eoptolink Technology Inc Ltd, Foxconn Technology, Giga-Byte Technology Co. Ltd., GoerTek Inc, Hon Hai Precision, Innolux, Lenovo, Lingyi Itech Guangdong Co, Quanta Computer Inc., Xiaomi Corp, Yageo Corp., Zhen Ding.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US

[中间内容因长度限制已省略]

 JSC Ltd (601869.SS)</td><td>U (10/13/2021)</td><td>Rmb440.30</td></tr><tr><td>Yangtze Optical Fibre and Cable JSC Ltd (6869.HK)</td><td>E (04/20/2023)</td><td>HK$234.20</td></tr><tr><td>Yongxin Optics Co Ltd (603297.SS)</td><td>E (11/15/2022)</td><td>Rmb115.68</td></tr><tr><td>Zhejiang Crystal-Optech Co Ltd (002273.SZ)</td><td>O (11/15/2022)</td><td>Rmb34.23</td></tr><tr><td>Zhongji Innolight Co Ltd (300308.SZ)</td><td>++</td><td>Rmb1,154.99</td></tr><tr><td>ZTE Corporation (0763.HK)</td><td>O (06/04/2026)</td><td>HK$27.54</td></tr><tr><td>ZTE Corporation (000063.SZ)</td><td>E (06/04/2026)</td><td>Rmb36.81</td></tr><tr><td colspan="3">Derrick Yang</td></tr><tr><td>Accton Technology Corporation (2345.TW)</td><td>O (06/06/2024)</td><td>NT$2,420.00</td></tr><tr><td>Advantech (2395.TW)</td><td>O (01/20/2021)</td><td>NT$471.00</td></tr><tr><td>AirTAC International (1590.TW)</td><td>O (04/16/2025)</td><td>NT$1,280.00</td></tr><tr><td>AU Optronics (2409.TW)</td><td>E (02/10/2026)</td><td>NT$24.40</td></tr><tr><td>Bizlink (3665.TW)</td><td>O (03/10/2025)</td><td>NT$2,095.00</td></tr><tr><td>BOE Technology (000725.SZ)</td><td>O (09/06/2019)</td><td>Rmb6.29</td></tr><tr><td>Chenbro (8210.TW)</td><td>O (07/23/2025)</td><td>NT$1,375.00</td></tr><tr><td>Chroma Ate Inc. (2360.TW)</td><td>O (10/05/2021)</td><td>NT$2,450.00</td></tr><tr><td>E Ink Holdings Inc. (8069.TWO)</td><td>O (05/11/2026)</td><td>NT$198.50</td></tr><tr><td>Ennostar Inc (3714.TW)</td><td>U (09/23/2022)</td><td>NT$64.80</td></tr><tr><td>Hiwin Technologies Corp. (2049.TW)</td><td>O (03/30/2026)</td><td>NT$329.50</td></tr><tr><td>Innolux (3481.TW)</td><td>E (04/07/2025)</td><td>NT$48.35</td></tr><tr><td>King Slide Works Co. Ltd. (2059.TW)</td><td>O (11/08/2023)</td><td>NT$6,180.00</td></tr><tr><td>Lens Technology (300433.SZ)</td><td>E (07/22/2020)</td><td>Rmb42.64</td></tr><tr><td>Radiant Opto-Electronics Corporation (6176.TW)</td><td>E (03/01/2024)</td><td>NT$94.10</td></tr><tr><td>Sanan Optoelectronics (600703.SS)</td><td>U (08/21/2023)</td><td>Rmb16.45</td></tr><tr><td>TCL Corp. (000100.SZ)</td><td>E (04/07/2025)</td><td>Rmb4.65</td></tr><tr><td>Tianma Microelectronics (000050.SZ)</td><td>U (01/24/2018)</td><td>Rmb8.22</td></tr><tr><td>Wuhan Jingce Electronic Group Co Ltd (300567.SZ)</td><td>E (11/26/2021)</td><td>Rmb177.80</td></tr><tr><td colspan="3">Howard Kao</td></tr><tr><td>Acer Inc. (2353.TW)</td><td>U (04/23/2025)</td><td>NT$35.30</td></tr><tr><td>Asustek Computer Inc. (2357.TW)</td><td>U (11/16/2025)</td><td>NT$844.00</td></tr><tr><td>Compal Electronics (2324.TW)</td><td>U (04/23/2025)</td><td>NT$38.60</td></tr><tr><td>FIT Hon Teng Ltd (6088.HK)</td><td>O (11/03/2025)</td><td>HK$8.02</td></tr><tr><td>Giga-Byte Technology Co. Ltd. (2376.TW)</td><td>E (11/16/2025)</td><td>NT$345.00</td></tr><tr><td>Gold Circuit Electronics Ltd. (2368.TW)</td><td>O (10/06/2022)</td><td>NT$1,360.00</td></tr><tr><td>Inspur Electronic Information (000977.SZ)</td><td>E (08/28/2023)</td><td>Rmb57.89</td></tr><tr><td>Lenovo (0992.HK)</td><td>E (11/16/2025)</td><td>HK$24.56</td></tr><tr><td>Lotes Co. Ltd. (3533.TW)</td><td>E (05/12/2025)</td><td>NT$2,290.00</td></tr><tr><td>Nan Ya PCB (8046.TW)</td><td>O (02/23/2026)</td><td>NT$831.00</td></tr><tr><td>Pegatron Corporation (4938.TW)</td><td>E (03/25/2026)</td><td>NT$92.10</td></tr><tr><td>Quanta Computer Inc. (2382.TW)</td><td>O (05/01/2023)</td><td>NT$376.50</td></tr><tr><td>Shengyi Technology Co Ltd. (600183.SS)</td><td>E (05/26/2022)</td><td>Rmb134.06</td></tr><tr><td>Shennan Circuits Co Ltd (002916.SZ)</td><td>E (08/24/2023)</td><td>Rmb369.64</td></tr><tr><td>Unimicron (3037.TW)</td><td>O (02/23/2026)</td><td>NT$911.00</td></tr><tr><td>Wistron Corporation (3231.TW)</td><td>O (07/12/2023)</td><td>NT$163.50</td></tr><tr><td>Wiwynn Corp (6669.TW)</td><td>O (11/10/2025)</td><td>NT$5,275.00</td></tr><tr><td>Yageo Corp. (2327.TW)</td><td>O (10/28/2025)</td><td>NT$751.00</td></tr><tr><td>Zhen Ding (4958.TW)</td><td>O (05/18/2026)</td><td>NT$512.00</td></tr><tr><td colspan="3">Sharon Shih</td></tr><tr><td>Asia Vital Components Co. Ltd. (3017.TW)</td><td>O (07/30/2024)</td><td>NT$2,570.00</td></tr><tr><td>Auras Technology Co Ltd (3324.TWO)</td><td>E (05/04/2023)</td><td>NT$1,095.00</td></tr><tr><td>Catcher Technology (2474.TW)</td><td>U (11/17/2025)</td><td>NT$220.00</td></tr><tr><td>Delta Electronics Inc. (2308.TW)</td><td>O (07/13/2017)</td><td>NT$2,255.00</td></tr><tr><td>Fositek Corp (6805.TW)</td><td>O (06/25/2025)</td><td>NT$1,895.00</td></tr><tr><td>Foxconn Industrial Internet Co. Ltd. (601138.SS)</td><td>O (07/10/2019)</td><td>Rmb70.48</td></tr><tr><td>Foxconn Technology (2354.TW)</td><td>U (04/23/2025)</td><td>NT$56.40</td></tr><tr><td>GoerTek Inc (002241.SZ)</td><td>U (04/23/2025)</td><td>Rmb23.10</td></tr><tr><td>Hon Hai Precision (2317.TW)</td><td>O (03/15/2024)</td><td>NT$269.50</td></tr><tr><td>LandMark Optoelectronics Corporation (3081.TWO)</td><td>E (03/26/2026)</td><td>NT$2,495.00</td></tr><tr><td>Lingyi Itech Guangdong Co (002600.SZ)</td><td>U (04/23/2025)</td><td>Rmb14.34</td></tr><tr><td>Lite-On Technology (2301.TW)</td><td>E (01/15/2025)</td><td>NT$218.50</td></tr><tr><td>Luxshare Precision Industry Co., Ltd. (002475.SZ)</td><td>O (10/24/2016)</td><td>Rmb66.14</td></tr><tr><td>Sunonwealth Electric Machine Industry Co (2421.TW)</td><td>E (02/23/2024)</td><td>NT$157.00</td></tr><tr><td>Tong Hsing (6271.TW)</td><td>E (03/18/2019)</td><td>NT$218.50</td></tr><tr><td>Visual Photonics Epitaxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$359.50</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
