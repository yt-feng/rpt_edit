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
July 27, 2026 09:00 PM GMT

# Greater China Semiconductors | Asia Pacific

# Old Memory: Divergent Trends in the Near Term

Recent memory cycle debate + CSP FCF concern + China memory position offload have caused a derating of old memory stocks, but we see stronger DDR4 pricing hikes and unprecedented legacy flash pricing power into 3Q. We think 1.0x 2028E BVPS offers good downside support.

Changing tide on mainstream memory: According to Trendforce (Exhibit 1), 3Q26 conventional DRAM mixed pricing is expected to increase by 13-18% Q/Q. Specifically, PC DDR5 pricing is seen rising by 15-20% Q/Q, server DDR5 pricing by 13-18% Q/Q, mobile LPDDR5(X) by 8-13% Q/Q, and NAND pricing by 10-15% Q/Q. Further, for 4Q26, Trendforce estimates price hikes of 3-8% Q/Q for conventional DRAM and 0-5% Q/Q for NAND. These estimated growth rates seem lower than some investors previously expected.

Yet, recently, we've seen stronger legacy memory pricing: Similar to our prior note (link), we believe DDR4 could enjoy continued monthly pricing hikes in 3Q. Compared to our pricing expectations one month ago, we believe CSPs are willing to offer higher pricing on DDR4 and may even try to sign a 1-2 year LTA (volume only) with suppliers. As a result, we believe monthly pricing could rise by 20%+ in 3Q, suggesting the Q/Q pricing hike could be 30% at least. We also continue to expect a 50-60% Q/Q price hike for SLC/MLC NAND in 3Q, and a 30-40% Q/Q price hike for NOR flash in 3Q.

Position offload in A share likely to see some stabilization: GigaDevice issued an announcement (link) that the company's niche memory products may see substantial price declines in the future. We see this warning as a potential longer term trend, rather than a near-term possibility, as we continue to see a structural supply gap across DDR4, SLC/MLC NAND, and NOR flash, supporting continued strong price hikes.

What is the downside support? GigaDevice (603986.SS): as a design house, it is hard to gauge the P/E floor, but the stock has already corrected 45.6% from its peak of Rmb840 as of Jun 29, providing some valuation support. Macronix/Nanya/Winbond trade at 1.5x/1.2x/1.2x 2028E BVPS, respectively; 1.0x historically has been a strong downside support level for greater China IDM companies.

MS TAIWAN LIMITED+

Daniel Yen, CFA
Equity Analyst
Daniel.Yen@morganstanley.com +886 2 2730-2863

Charlie Chan
Equity Analyst
Charlie.Chan@morganstanley.com +886 2 2730-1725

MS ASIA LIMITED+
Daisy Dai, CFA
Equity Analyst
Daisy.Dai@morganstanley.com +852 2848-7310

MS TAIWAN LIMITED+
Tiffany Yeh
Equity Analyst
Tiffany.Yeh@morganstanley.com +886 2 7712-3032

MS ASIA LIMITED+

Ethan Jia
Research Associate
Ethan.Jia@morganstanley.com +852 3963-2287

![](images/46ece527c540a569870056d2cddeb4bad71c5187eec0fbe84b731d0c1e16b013.jpg)  
GREATER CHINA TECHNOLOGY SEMICONDUCTORS
Asia Pacific
Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Key Charts and Exhibits

Exhibit 1: Latest pricing forecast for DRAM and NAND

<table><tr><td></td><td>1Q26</td><td>2Q26</td><td>3Q26E - Old</td><td>3Q26E - New</td><td>4Q26E - Old</td><td>4Q26E - New</td></tr><tr><td>PC DRAM</td><td>DDR4: up 120-125%DDR5: up 110-115%Blended ASP: up 110-115%</td><td>DDR4: up 35-40%DDR5: up 45-50%Blended ASP: up 45-50%</td><td>up 3-8%</td><td>DDR4: up 15-20%DDR5: up 15-20%Blended ASP: up 15-20%</td><td>up 0-5%</td><td>up 3-8%</td></tr><tr><td>Server DRAM</td><td>DDR4: up 95-100%DDR5: up 93-98%Blended ASP: up 93-98%</td><td>DDR4: up 50-55%DDR5: up 53-58%Blended ASP: up 53-58%</td><td>up 10-15%</td><td>DDR4: up 13-18%DDR5: up 13-18%Blended ASP: up 13-18%</td><td>up 3-8%</td><td>up 3-8%</td></tr><tr><td>Mobile DRAM</td><td>LPDDR4X: up 58-63%LPDDR5(x): up 58-63%</td><td>LPDDR4X: up 73-78%LPDDR5(x): up 80-85%</td><td>up 3-8%</td><td>LPDDR4X: up 8-13%LPDDR5(x): up 8-13%</td><td>up 0-5%</td><td>up 0-5%</td></tr><tr><td>Graphics DRAM</td><td>GDDR6: up 95-100%GDDR7: up 95-100%</td><td>GDDR6: up 30-35%GDDR7: up 40-45%</td><td>GDDR6: up 3-8%GDDR7: up 10-15%</td><td>GDDR6: up 15-20%GDDR7: up 15-20%</td><td>GDDR6: up 0-5%GDDR7: up 3-8%</td><td>GDDR6: up 0-5%GDDR7: up 3-8%</td></tr><tr><td>Consumer DRAM</td><td>DDR3: up 75-80%DDR4: up 75-80%</td><td>DDR3: up 55-60%DDR4: up 55-60%</td><td>up 10-15%</td><td>DDR3: up 35-40%DDR4: up 28-33%</td><td>up 3-8%</td><td>up 3-8%</td></tr><tr><td>Total DRAM</td><td>Conventional DRAM: up 93-98%HBM Blended: up 83-88%</td><td>Conventional DRAM: up 58-63%HBM Blended: 53-58%</td><td>Conventional DRAM: up 8-13%</td><td>Conventional DRAM: up 13-18%HBM Blended: 8-13%</td><td>Conventional DRAM: up 3-8%</td><td>Conventional DRAM: up 3-8%</td></tr><tr><td></td><td>1Q26</td><td>2Q26</td><td>3Q26E - Old</td><td>3Q26E - New</td><td>4Q26E - Old</td><td>4Q26E - New</td></tr><tr><td>eMMCUFS</td><td>up 95-100%</td><td>up 75-80%</td><td>up 5-10%</td><td>up 5-10%</td><td>mostly flat</td><td>mostly flat</td></tr><tr><td>Enterprise SSD</td><td>up 75-80%</td><td>up 48-53%</td><td>up 13-18%</td><td>up 18-23%</td><td>up 3-8%</td><td>up 3-8%</td></tr><tr><td>Client SSD</td><td>up 105-110%</td><td>up 70-75%</td><td>up 5-10%</td><td>up 13-18%</td><td>mostly flat</td><td>mostly flat</td></tr><tr><td>3D NAND Wafers (TLC &amp; QLC)</td><td>up 75-80%</td><td>up 28-33%</td><td>up 5-10%</td><td>up 5-10%</td><td>mostly flat</td><td>mostly flat</td></tr><tr><td>Total NAND Flash</td><td>up 85-90%</td><td>up 55-60%</td><td>up 8-13%</td><td>up 10-15%</td><td>up 0-5%</td><td>up 0-5%</td></tr></table>

Source: Trendforce, MS estimates

Exhibit 2: NOR flash demand and supply growth rates  
![](images/ebe98d2e8b3e5cc4125c887aed1378197f96909f8ab90aa4fb2af40d775ca5e0.jpg)  
Source: Company data, MS

Exhibit 3: NOR flash demand growth and supply growth by  
![](images/d0e5b218126c40d984a175e77fa72ab158cc30c18269d0f25161e1561c00fdb8.jpg)  
Source: Company data, MS

Exhibit 4: DDR4 quarterly supply and demand summary  
![](images/edb1b6e1630216df67b9c3d8b4ebfb519dac5c90168c8a4d9053f34b35c46f6c.jpg)  
Source: Company data, IDC, MS (e) estimates

Exhibit 5: Quarterly oversupply/undersupply ratio vs. Nanya and Winbond pricing Q/Q change  
![](images/e38efb43821e25530f3a42436dfa151a8c107f9a78b2bfb54219e54c3b885b74.jpg)  
Source: Company data, IDC, MS (e) estimates

Exhibit 6: Quarterly supply breakdown (mn Gb)  
![](images/a52980307e7aaa7e32b48ca50d6c9b7957182f61b9076e1cf697b12e736e7da2.jpg)  
Source: Company data, MS (e) estimates

Exhibit 7: Quarterly demand breakdown by product (mn Gb)  
![](images/94a5c8c768baf85d88293e40a988528cdddb9258f345028ed9ae05780f5a9888.jpg)  
Source: IDC, MS (e) estimates

Exhibit 8: DDR4 8Gb (1Gx8) pricing chart  
![](images/e76dcd3485258d681f3ff22e602fb0858d17885204b97d66d00d8e498135a4e1.jpg)  
Source: DRAMeXchange, MS. Data as of Jun 2026.

Exhibit 9: DDR5 16Gb (2Gx8) pricing chart  
![](images/133b0024d43788fd2dd9c340d696b4bffc4dc6649802b220e9969ce6aa0943b2.jpg)  
Source: DRAMeXchange, MS. Data as of Jun 2026.

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

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Alchip Technologies Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co.

Within the last 12 months, MS has received compensation for investment banking services from ASMPT Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Montage Technology Co Ltd, Powerchip Semiconductor Manufacturing Co.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, MetaX Integrated Circuits, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, SG Micro Corp., Shenzhen Longsys Electronics Co Ltd, SICC Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Universal Scientific Ind. (Shanghai), Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: ASE Technology Holding Co. Ltd., Iluvatar CoreX Semiconductor Co., Ltd., King Yuan Electronics Co Ltd, MediaTek, Montage Technology Co Ltd, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind.

[中间内容因长度限制已省略]

1.SS)</td><td>E (11/17/2025)</td><td>Rmb95.31</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$1,820.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb98.89</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$449.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$70.65</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,350.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$126.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$157.00</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$355.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$161.60</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb60.74</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb92.22</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb32.33</td></tr><tr><td>Hygon Information Technology Co., Ltd. (688041.SS)</td><td>O (07/03/2026)</td><td>Rmb313.59</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$44.12</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb82.35</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$24.88</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb100.00</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb84.88</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb66.00</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb24.77</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb93.22</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$773.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,385.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$14,695.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$98.70</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$166.00</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb104.23</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb434.03</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$125.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$322.00</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb227.45</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$518.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$132.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$615.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$61.90</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$762.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb50.31</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$160.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$116.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$203.50</td></tr></table>

Duan Liu  
Dosilicon Co Ltd (688110.SS)

<table><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb373.90</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,035.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$598.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$12.62</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$6,110.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,720.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$270.90</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$6,395.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
