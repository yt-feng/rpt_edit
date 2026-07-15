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
<table><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td>Charlie Chan</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Charlie.Chan@morganstanley.com</td><td>+886 2 2730-1725</td></tr><tr><td>Daniel Yen, CFA</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Daniel.Yen@morganstanley.com</td><td>+886 2 2730-2863</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td>Daisy Dai, CFA</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Daisy.Dai@morganstanley.com</td><td>+852 2848-7310</td></tr><tr><td colspan="2">MS TAIWAN LIMITED+</td></tr><tr><td>Tiffany Yeh</td><td></td></tr><tr><td>Equity Analyst</td><td></td></tr><tr><td>Tiffany.Yeh@morganstanley.com</td><td>+886 2 7712-3032</td></tr><tr><td>Lucas Wang</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Lucas.Wang@morganstanley.com</td><td>+886 2 2730-2875</td></tr><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td>Henry Zhao</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Henry.Zhao@morganstanley.com</td><td>+852 2239-7731</td></tr><tr><td>Ethan Jia</td><td></td></tr><tr><td>Research Associate</td><td></td></tr><tr><td>Ethan.Jia@morganstanley.com</td><td>+852 3963-2287</td></tr></table>

Greater China Technology Semiconductors | Taiwan

July 13, 2026 06:02 PM GMT

TSMC | Asia Pacific

# Earnings preview and catalysts for 2Q26 analyst meeting

We suggest accumulating the stock given potential for full-year 2026 guidance to be raised.

What and when is the catalyst? TSMC will host its 2Q26 analyst meeting on July 16. In TSMC: Domination in leading-edge foundry continues; OW (29 June 2026), we noted that TSMC may lift 2026e revenue guidance to close to 40% Y/Y growth and raise capex to US\$56bn, the high end of its initial US\$52-56bn range. Looking ahead to 3Q26, we forecast revenue to be up in the low to mid-teens Q/Q given strong demand in both 3nm and 2nm products. The margin should improve further Q/Q, in our view, with better utilization rate, but higher costs and depreciation are potential offsets. See our preview and key questions to ask.

## What are the potential outcomes for this event?

\- Scenario 1: TSMC guides for 3Q26 revenue to be up 15% Q/Q in USD, full-year revenue growth target raised to \~40% Y/Y, 3Q gross margin to be \~70%. 2026 full-year capex raised to US\$60bn, and 2024-2029 five-year AI semi revenue CAGR is raised to 80%. TSMC cannot fulfill the strong AI demand until the end of the decade.

\- Scenario 2 (base case): TSMC guides for 3Q26 revenue to be up 10%-15% Q/Q in USD, full-year revenue growth target raised to high 30s (% Y/Y) or close to 40% Y/Y, 3Q gross margin to be \~67%-68% (flat Q/Q). Full-year 2026 capex updated to US\$56bn, while five-year AI semi revenue CAGR raised to 70% from the current mid- to high 50s (%), mainly from memory cost increase. TSMC is trying to meet strong AI demand in 2028.

\- Scenario 3:TSMC guides for 3Q26 revenue to be up 5%-10% Q/Q in USD, full-year revenue growth updated to \~35% Y/Y, 3Q gross margin to be \~66%-67% (down Q/Q). 2026 full-year capex guidance unchanged at US\$54-56bn, while five-year AI semi revenue CAGR is also unchanged at mid- to high 50s (%). AI demand is strong but could be affected by memory costs.

## What are the potential implications of these outcomes for TSMC's share price?

Scenario 1: up 3-5%. Scenario 2: up 1-3%. Scenario 3: down 3-5%.

See Exhibit 1.

![](images/5f0353c592c9e928cd7632f369992f9d2c41d46f99aad5bf37e10880b6fa3bdf.jpg)

## TSMC (2330.TW, 2330 TT)

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>Attractive</td></tr><tr><td>Price target</td><td>NT$2,888.00</td></tr><tr><td>Up/downside to price target (%)</td><td>18</td></tr><tr><td>Shr price, close (Jul 13, 2026)</td><td>NT$2,440.00</td></tr><tr><td>Mkt cap, curr (mn)</td><td>NT$63,264,271</td></tr><tr><td>Avg daily trading value (mn)</td><td>NT$64,514</td></tr></table>

<table><tr><td>Fiscal Year Ending</td><td>12/25</td><td>12/26e</td><td>12/27e</td><td>12/28e</td></tr><tr><td>EPS (NT$)**</td><td>66.25</td><td>107.56</td><td>143.01</td><td>177.30</td></tr><tr><td>Prior EPS (NT$)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>EPS (NT$)§</td><td>64.56</td><td>99.97</td><td>129.74</td><td>164.77</td></tr><tr><td>ModelWare net inc (NT $ bn)</td><td>1,718</td><td>2,778</td><td>3,708</td><td>4,597</td></tr><tr><td>P/E</td><td>23.4</td><td>22.8</td><td>17.1</td><td>13.8</td></tr><tr><td>Div yld (%)</td><td>1.4</td><td>1.1</td><td>1.4</td><td>1.8</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Unless otherwise noted, all metrics are based on MS ModelWare framework

\*\* = Based on consensus methodology

§ = Consensus data is provided by Refinitiv Estimates

e = MS estimates

## Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr></table>

## TSMC 2330.TW

2Q26 margin, 3Q26/2026 full-year guidance — In-line

↑ Modest revision higher

\- We think TSMC may guide for 3Q26 revenue growth of $10 - 15\%$ Y/Y, with the midpoint of margin guidance within the range of $67 - 68\%$ .

\- Full-year revenue growth target raised to high 30s (%) Y/Y, or close to 40% Y/Y. 2026 full-year capex updated to US\$56bn; five-year AI semi revenue CAGR is raised to 70%.

\- Management's comments on AI demand sustainability - still very strong until 2028.

\*Likely impact to consensus EPS is for the next 12 months

Source: Company data, MS

Exhibit

Exhibit 1: Scenario 2 is our base case, to which we assign a 60% probability.

<table><tr><td>Details of the scenario</td><td>Scenario 1</td><td>Scenario 2</td><td>Scenario 3</td></tr><tr><td>PROBABILITIES</td><td>20%</td><td>60%</td><td>20%</td></tr><tr><td>3Q26 USD revenue growth</td><td>15% Q/Q</td><td>10-15% Q/Q</td><td>5-10% Q/Q</td></tr><tr><td>3Q26 gross margin</td><td>70%</td><td>67-68%</td><td>66-67%</td></tr><tr><td>2026 full-year revenue growth</td><td>Around 40%</td><td>Close to 40%</td><td>Around 35%</td></tr><tr><td>2026 full-year capex in USD</td><td>Raised to US $60bn</td><td>Raised to US $56bn</td><td>Unchanged at US $54-56bn</td></tr><tr><td>Five-year AI semi revenue CAGR</td><td>Raised to 80%</td><td>Raised to 70%</td><td>Unchanged at mid-high 50s (%)</td></tr><tr><td>AI demand sustainability</td><td>Until the end of the decade</td><td>Strong until 2028</td><td>Could be affected by memory costs</td></tr><tr><td>Potential change in stock price (%)</td><td>Up 3-5%</td><td>Up 1-3%</td><td>Down 3-5%</td></tr><tr><td>Corresponding projected stock price</td><td>NT$2,487-2,535</td><td>NT$2,439-2,487</td><td>NT$2,294-2,342</td></tr></table>

Source: MS estimates

## Valuation Methodology and Risks

## TSMC (2330.TW)

Base case, residual income model. Key assumptions: a cost of equity of 9.2% (beta of 1.2, risk-free rate of 2.0% and risk premium of 6.0%), an intermediate growth rate of 10.5%, and a terminal growth rate of 4.0%.

## Risks to Upside

■ TSMC charges large customers more to keep its gross margin above 56% in the long term.

■ AI semi demand grows more significantly than expected, while TSMC maintains high market share in leading-edge foundry business.

■ Outsourcing from Intel CPU increases in 2025-27.

## Risks to Downside

■ Inventory correction occurs in 2026.

■ Demand for leading edge technologies weakens.

■ Costs of overseas fabs grow significantly.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Charlie Chan; Daisy Dai, CFA; Tiffany Yeh; Daniel Yen, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: ACM Research Inc, Advanced Micro-Fabrication Equipment Inc, Advanced Wireless Semiconductor Co, Alchip Technologies Ltd, AllRing Tech Co., AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMPT Ltd, Cambricon Technology Corporation, Dosilicon Co Ltd, FOCI Fiber Optic Communications Inc, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Hangzhou Silan Microelectronics Co. Ltd., King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, Montage Technology Co Ltd, Parade Technologies Ltd, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, SG Micro Corp., Shanghai Fudan Microelectronics, Silergy Corp., Silicon Motion, TSMC, UMC, Unigroup Guoxin Microelectronics Co Ltd, Vanguard International Semiconductor, WIN Semiconductors Corp, Winbond Electronics Corp, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Alchip Technologies Ltd, Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co.

Within the last 12 months, MS has received compensation for investment banking services from ASMPT Ltd, Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-re

[中间内容因长度限制已省略]

ronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,170.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb116.26</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$524.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$78.35</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,440.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$153.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$178.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$403.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$185.40</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb77.60</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb119.83</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb41.93</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb345.00</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$49.38</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb99.05</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$29.38</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb138.59</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb116.99</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb81.74</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb27.80</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb113.31</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$893.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,510.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$13,520.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$107.00</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$183.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb125.80</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb550.80</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$138.00</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$332.20</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb252.79</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$467.50</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$163.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$647.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$69.00</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$756.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb55.63</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$167.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$117.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$211.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb154.15</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb522.04</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,035.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$601.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$15.23</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,705.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,640.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$326.35</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$7,375.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
