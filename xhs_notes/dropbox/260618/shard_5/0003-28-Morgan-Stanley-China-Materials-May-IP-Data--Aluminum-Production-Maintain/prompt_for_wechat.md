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
## China Materials | Asia Pacific

# May IP Data: Aluminum Production Maintained an Upward Trajectory

YoY production declined for crude steel, cement, coal and glass, but grew for aluminum.

Property – New starts down 24.7% YoY in May (vs. -27.1% YoY in April). GFA sold fell 14.1% YoY (vs. -10.3% YoY in April) and property completions were down 19.6% YoY (vs. -19% YoY in April), all based on restated data for 2025. Our China property team expects a weaker 3Q. Secondary real-time home sales in high-tier cities started weakening in mid-May, and have decelerated even faster in recent weeks.

Considering the still-fragile resident sentiment, diminishing policy effects/pent-up demand, and reduced new saleable resources, the team estimates secondary home sales to turn negative y-y, and primary home sales to drop further y-y in 3Q, despite the low base.

FAI was down 12.5% YoY in May 26 (vs. -9.4% YoY in April). Highway FAI slipped 13.8% YoY in May.

Crude steel output was -2.7% YoY in May (vs. -2.8% YoY in April). 5M26

production was down 3.9% YoY. We estimate domestic steel apparent consumption was down 8.5% YoY in May (vs. +1.2% in April) on apparent inventory buildup, amid a 2% slowdown in net exports.

Cement production was -8.1% YoY in May (vs. -10.8% YoY in April). 5M26

production was down 8.6% YoY. Output YoY decline narrowed in May due to lower base numbers. Cement prices in east China remained weak in early June due to weak downstream demand, wet weather, and college entrance examinations.

Aluminum production up 1.7% YoY and 0.5% MoM to 3.9mnt in May 26. Total aluminum production in 5M26 up 3.5% YoY to 19.2mnt, driven by the capacity resumption in Liaoning and new capacity in Inner Mongolia. As the operating capacity has reached the ceiling, we expect overall aluminum production to stay at an elevated level for the remainder of the year given solid industry profitability.

Coal production down 1.7% YoY but up 3% MoM to 397.2mnt in May 2026. The MoM recovery in coal production follows the seasonal trend, as restocking demand from power plants will gradually increase to prepare for the summer peak consumption season. However, a mine accident in late May and tighter safety controls in June, will likely see domestic coal production remain constrained in the near term. Thermal power generation rose 2.1% YoY in May to 472.6bn kWh, accounting for 60% of total power generation vs. 62% in Apr-26.

MS ASIA LIMITED+

## Rachel L Zhang

Equity Analyst

Rachel.Zhang@morganstanley.com +852 2239-1520

## Hannah Yang, CFA

Equity Analyst

Hannah.Yang1@morganstanley.com +852 2239-7079

## Chris Jiang

Equity Analyst

Chris.Jiang@morganstanley.com +852 3963-1593

## Cynthia Tang

Research Associate

Cynthia.Tang@morganstanley.com +852 3963-4360

## Asia Summer School 2026

![](images/d84e3c0c4a246cc32c16dcdadd5b7ae353a6daa71deef3ad04e49411b7fb3e02.jpg)

GREATER CHINA MATERIALS

<table><tr><td>Asia Pacific Industry View</td><td>Attractive</td></tr><tr><td colspan="2">CHINA COAL</td></tr><tr><td>Asia Pacific Industry View</td><td>Cautious</td></tr><tr><td colspan="2">GREATER CHINA CEMENT</td></tr><tr><td>Asia Pacific Industry View</td><td>In-Line</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## April IP Data (Continued)

Glass production down 6.3% YoY but up 3.6% MoM to 75.5mn wt cases in May 26. The higher MoM production was mainly driven by the volume contribution from resumed lines. Currently, fundamentals for float glass remains weak as inventory remains high amid muted demand. The oversupply pressure should continue to weigh on float glass prices and margins.

Exhibit 1: May 2026 industrial production data

<table><tr><td>May 2026 Production Data</td><td>Growth rate trend</td><td>May 2026</td><td>MoM May 2026</td><td>YoY May 2026</td><td>Apr 2026</td><td>Mar 2026</td><td>Jan+Feb 2026</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td><td>May-25</td><td>2026YTD</td></tr><tr><td>Crude steel (Mnt)</td><td></td><td>84.4</td><td>0.9%</td><td>-2.7%</td><td>-2.8%</td><td>-6.3%</td><td>-3.6%</td><td>-10.3%</td><td>-10.9%</td><td>-12.1%</td><td>-4.6%</td><td>-0.7%</td><td>-4.0%</td><td>-9.2%</td><td>-6.9%</td><td>-3.9%</td></tr><tr><td>Finished steel (Mnt)</td><td></td><td>123.0</td><td>0.3%</td><td>-2.8%</td><td>-1.7%</td><td>-2.3%</td><td>-1.1%</td><td>-3.8%</td><td>-2.6%</td><td>-0.9%</td><td>5.1%</td><td>9.7%</td><td>6.4%</td><td>1.8%</td><td>3.4%</td><td>-1.5%</td></tr><tr><td>Cement (Mnt)</td><td></td><td>149.9</td><td>2.9%</td><td>-8.1%</td><td>-10.8%</td><td>-21.0%</td><td>6.8%</td><td>-6.6%</td><td>-8.2%</td><td>-15.8%</td><td>-8.6%</td><td>-6.2%</td><td>-5.6%</td><td>-5.3%</td><td>-8.1%</td><td>-8.6%</td></tr><tr><td>Aluminum (Mnt)</td><td></td><td>3.9</td><td>0.5%</td><td>1.7%</td><td>3.1%</td><td>2.7%</td><td>3.0%</td><td>3.0%</td><td>2.5%</td><td>0.4%</td><td>1.8%</td><td>-0.5%</td><td>0.6%</td><td>3.4%</td><td>5.0%</td><td>3.5%</td></tr><tr><td>Glass (mn wt cases)</td><td></td><td>75.5</td><td>3.6%</td><td>-6.3%</td><td>-7.9%</td><td>-6.6%</td><td>-3.5%</td><td>3.4%</td><td>3.7%</td><td>3.3%</td><td>-9.7%</td><td>-2.0%</td><td>-3.4%</td><td>-4.5%</td><td>-5.7%</td><td>-6.3%</td></tr><tr><td>Coal production (Mnt)</td><td></td><td>397.2</td><td>3.0%</td><td>-1.7%</td><td>-1.0%</td><td>0.0%</td><td>-0.3%</td><td>-1.0%</td><td>-0.5%</td><td>-2.3%</td><td>-1.8%</td><td>-3.2%</td><td>-3.8%</td><td>3.0%</td><td>4.2%</td><td>-0.3%</td></tr><tr><td>Thermal power generation (KWH bn)</td><td></td><td>472.6</td><td>1.9%</td><td>2.1%</td><td>3.1%</td><td>4.2%</td><td>3.3%</td><td>-3.2%</td><td>-4.2%</td><td>7.3%</td><td>-5.4%</td><td>1.7%</td><td>4.3%</td><td>1.1%</td><td>1.2%</td><td>3.4%</td></tr><tr><td>FAI, % YoY</td><td></td><td>-12.5%</td><td>-14.1ppt</td><td>-12.5%</td><td>-9.4%</td><td>1.6%</td><td>-4.4%</td><td>-15.1%</td><td>-12.0%</td><td>-12.2%</td><td>-7.1%</td><td>-7.1%</td><td>-5.3%</td><td>-0.1%</td><td>2.7%</td><td>-4.1%</td></tr><tr><td>IP, %, YoY</td><td></td><td>4.5%</td><td>-1.2ppt</td><td>4.5%</td><td>4.1%</td><td>5.7%</td><td>6.3%</td><td>5.2%</td><td>4.8%</td><td>4.9%</td><td>6.5%</td><td>5.2%</td><td>5.7%</td><td>6.8%</td><td>5.8%</td><td>5.4%</td></tr><tr><td colspan="17">Property</td></tr><tr><td>FS starts (mn sqm)</td><td></td><td>40.3</td><td>14.2%</td><td>-24.7%</td><td>-27.1%</td><td>-17.1%</td><td>-23.1%</td><td>-19.3%</td><td>-27.7%</td><td>-29.3%</td><td>-15.0%</td><td>-19.8%</td><td>-15.2%</td><td>-9.5%</td><td>-18.7%</td><td>-24.7%</td></tr><tr><td>FS sold (mn sqm)</td><td></td><td>60.6</td><td>5.7%</td><td>-14.1%</td><td>-10.3%</td><td>-8.0%</td><td>-13.5%</td><td>-16.6%</td><td>-17.9%</td><td>-19.6%</td><td>-11.9%</td><td>-11.0%</td><td>-8.4%</td><td>-6.6%</td><td>-4.6%</td><td>-14.1%</td></tr><tr><td>FS completions (mn sqm)</td><td></td><td>22.0</td><td>5.0%</td><td>-19.6%</td><td>-19.0%</td><td>-19.3%</td><td>-27.9%</td><td>-18.4%</td><td>-25.4%</td><td>-27.9%</td><td>0.4%</td><td>-21.3%</td><td>-29.4%</td><td>-2.2%</td><td>-19.1%</td><td>-19.6%</td></tr><tr><td>Investment (Rmb bn)</td><td></td><td>638.7</td><td>2.2%</td><td>-24.9%</td><td>-20.1%</td><td>-11.7%</td><td>-10.3%</td><td>-36.8%</td><td>-31.4%</td><td>-23.2%</td><td>-21.3%</td><td>-19.9%</td><td>-17.1%</td><td>-12.4%</td><td>-12.4%</td><td>-16.2%</td></tr><tr><td colspan="17">Infrastructure FAI</td></tr><tr><td>Highway (Rmb bn)*</td><td></td><td>350.3</td><td>24.8%</td><td>-13.8%</td><td>-18.1%</td><td>5.6%</td><td>-0.6%</td><td>-18.4%</td><td>-8.7%</td><td>-15.4%</td><td>0.9%</td><td>-11.6%</td><td>-16.6%</td><td>3.4%</td><td>1.1%</td><td>-5.7%</td></tr></table>

Source: National Bureau of Statistics, MS. \*Note: Railway and highway FAI growth is rebased.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Chris Jiang; Hannah Yang, CFA; Rachel L Zhang.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Aluminum Corp. of China Ltd., Anhui Honglu Steel Construction, Asia Cement, Beijing Oriental Yuhong Waterproof Techn, China Shenhua Energy, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Flat Glass Group Co Ltd, Ganfeng Lithium Co. Ltd., GEM Co Ltd, Jiangxi Copper, JL Mag Rare-Earth Co. Ltd, Shandong Gold Mining Co. Ltd, Shenzhen Kedali Industry Co Ltd, Sinomine Resource Group Co Ltd, Taiwan Cement, Tianqi Lithium Industries Inc., Yankuang Energy Group Co Ltd, Zijin Mining Group.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of CNGR Advanced Material Co., Ltd., Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for investment banking services from Zijin Mining Group.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Aluminum Corp. of China Ltd., Anhui Conch Cement Co. Ltd, Asia Cement, Beijing Oriental Yuhong Waterproof Techn, China National Building Material Company, China Resources Building Materials, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Huaxin Building Materials, Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Taiwan Cement, Tianqi Lithium Industries Inc., Yancoal Australia Ltd, Yankuang Energy Group Co Ltd, Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Jushi, China National Building Material Company, China Steel Corp., CMOC Group Ltd, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Mining Group.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Aluminum Corp. of China Ltd., Anhui Conch Cement Co. Ltd, Asia Cement, Beijing Oriental Yuhong Waterproof Techn, China National Building Material Company, China Resources Building Materials, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Huaxin Building Materials, Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Taiwan Cement, Tianqi Lithium Industries Inc., Yancoal Australia Ltd, Yankuang Energy Group Co Ltd, Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: China Jushi, China National Building Material Company, China Steel Corp., CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Taiwan Cement, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Yankuang Energy Group Co Ltd, Zijin Gold International, Zijin Mining Group.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy,

Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

## Global Stock Ratings Distribution

(as of May 31, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory req

[中间内容因长度限制已省略]

 Shenying Carbon Fiber Co Ltd (688295.SS)</td><td>O (08/25/2023)</td><td>Rmb51.09</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Aluminum Corp. of China Ltd. (601600.SS)</td><td>O (11/30/2020)</td><td>Rmb10.67</td></tr><tr><td>Aluminum Corp. of China Ltd. (2600.HK)</td><td>O (11/30/2020)</td><td>HK$9.45</td></tr><tr><td>Baoshan Iron &amp; Steel (600019.SS)</td><td>O (01/16/2016)</td><td>Rmb5.97</td></tr><tr><td>Beijing New Building Materials (000786.SZ)</td><td>O (04/09/2024)</td><td>Rmb20.91</td></tr><tr><td>Beijing Oriental Yuhong Waterproof Techn (002271.SZ)</td><td>E (09/25/2024)</td><td>Rmb12.56</td></tr><tr><td>China Jushi (600176.SS)</td><td>O (12/22/2020)</td><td>Rmb45.77</td></tr><tr><td>China Lesso Group Holdings Ltd (2128.HK)</td><td>U (10/08/2025)</td><td>HK$4.24</td></tr><tr><td>China Steel Corp. (2002.TW)</td><td>U (12/16/2025)</td><td>NT$18.65</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$19.98</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb20.92</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb48.79</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$31.24</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb6.00</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb71.32</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$61.85</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb70.57</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb26.55</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$37.20</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb47.36</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$18.99</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb31.41</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$7.33</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>O (04/23/2025)</td><td>Rmb28.66</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>O (12/12/2024)</td><td>HK$23.08</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>O (11/30/2020)</td><td>Rmb4.81</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$48.30</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb63.72</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb9.15</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>O (06/21/2024)</td><td>HK$21.40</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$121.50</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$33.56</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb31.31</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: China Coal

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>China Coal Energy Co., Ltd. (601898.SS)</td><td>E (03/16/2026)</td><td>Rmb14.77</td></tr><tr><td>China Coal Energy Co., Ltd. (1898.HK)</td><td>O (03/16/2026)</td><td>HK$11.50</td></tr><tr><td>China Shenhua Energy (1088.HK)</td><td>O (11/02/2017)</td><td>HK$43.06</td></tr><tr><td>China Shenhua Energy (601088.SS)</td><td>E (04/04/2019)</td><td>Rmb43.39</td></tr><tr><td>Shaanxi Coal Industry (601225.SS)</td><td>O (03/16/2026)</td><td>Rmb25.26</td></tr><tr><td>Shanxi Coking Coal (000983.SZ)</td><td>E (10/26/2021)</td><td>Rmb7.05</td></tr><tr><td>Yancoal Australia Ltd (3668.HK)</td><td>O (03/16/2026)</td><td>HK$32.74</td></tr><tr><td>Yankuang Energy Group Co Ltd (1171.HK)</td><td>O (03/16/2026)</td><td>HK$12.86</td></tr><tr><td>Yankuang Energy Group Co Ltd (600188.SS)</td><td>E (03/16/2026)</td><td>Rmb21.08</td></tr><tr><td>Rachel L Zhang</td><td></td><td></td></tr><tr><td>Shougang Fushan Resources Group Limited (0639.HK)</td><td>O (09/15/2022)</td><td>HK$2.61</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: Greater China Cement

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Anhui Conch Cement Co. Ltd (0914.HK)</td><td>E (04/20/2026)</td><td>HK$18.16</td></tr><tr><td>Anhui Conch Cement Co. Ltd (600585.SS)</td><td>E (04/20/2026)</td><td>Rmb18.44</td></tr><tr><td>Asia Cement (1102.TW)</td><td>U (04/01/2021)</td><td>NT$35.60</td></tr><tr><td>China National Building Material Company (3323.HK)</td><td>O (04/07/2025)</td><td>HK$5.15</td></tr><tr><td>China Resources Building Materials (1313.HK)</td><td>U (04/20/2026)</td><td>HK$1.19</td></tr><tr><td>Huaxin Building Materials (6655.HK)</td><td>O (10/17/2025)</td><td>HK$14.40</td></tr><tr><td>Huaxin Building Materials (600801.SS)</td><td>O (04/14/2017)</td><td>Rmb19.32</td></tr><tr><td>Taiwan Cement (1101.TW)</td><td>U (04/01/2021)</td><td>NT$24.50</td></tr><tr><td>West China Cement (2233.HK)</td><td>U (04/20/2026)</td><td>HK$1.75</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
