你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
June 2, 2026 04:22 PM GMT

## Greater China Technology Semiconductors | Asia Pacific

# Key Computex Takeaways: Agenetic AI, TSMC capacity and MediaTek's AI PC chips

Agentic AI and CPU servers dominated the Computex keynote discussions. Nvidia indicated that TSMC's capacity can support robust growth for Nvidia in 2027.

Agentic AI compute key focus: In their keynotes, Nvidia, Arm and Qualcomm emphasized Arm-based server CPUs to support future agentic AI demand, echoing our report, Global Tech: Agentic AI – The Surge Begins (11 May 2026).

Comments on Nvidia Vera CPU: Ahead of Computex, we published NVIDIA's Vera CPU and Rubin GPU seen as the main show (27 May 2026). At today's investor luncheon, our Nvidia analyst Joe Moore asked CEO Jensen Huang the first question about the US\$20bn Vera CPU revenue assumption. Management indicated that demand spans both AI server head nodes and stand-alone CPU servers. Given its materially better performance than the x86 (see Exhibit 5), Nvidia can command higher values for Vera, excl. memory sales. Our supply chain checks suggest 2.5mn–4mn units are in preparation. Rubin has already entered fab production with no apparent delays. On CPO (optics) vs. copper, Nvidia indicated that it will adopt CPO only when necessary and rely on copper as long as possible.

Sufficient TSMC capacity: At the 2024 and 2025 Computex events, we asked Jensen Huang about TSMC's pricing and value. This year, we asked whether Nvidia can secure sufficient TSMC capacity for 2027 and whether allocation could affect market share. We also asked – even more importantly – how Nvidia could secure incremental allocation versus competitors.

Nvidia indicated it has sufficient TSMC capacity to support robust growth in 2027. The company has convinced TSMC and other suppliers that demand remains strong. Even as supply expands, demand will likely still exceed supply in 2027. Management also emphasized that the AI semiconductor market is growing and does not represent a zero-sum or pure market share competition.

Agenetic AI at the edge – do we need a local LLM/agent: Nvidia announced its RTX Sparks AI PC WoA SoC in its keynote, jointly designed with MediaTek. We flagged this 9 months ago in our MediaTek report, saying "Nvidia/MediaTek WoA AI PC keeps being pushed out – now to 2H26. For N1X, we think the new timing of product launch would be next year's Computex in June (vs. the CES in January), given that Microsoft's new AI Windows system will be more of a 2H26 rollout. Moreover, the new x86 SoC will fuse an Intel CPU + Nvidia RTX GPU chiplet via NVLink". We do not see this launch as a surprise. Investors are asking about the volume of RTX Sparks in 2026 and whether edge AI compute is necessary for Agentic AI.

MS TAIWAN LIMITED+

## Charlie Chan

Equity Analyst

Charlie.Chan@morganstanley.com +886 2 2730-1725

## Daniel Yen, CFA

Equity Analyst

Daniel.Yen@morganstanley.com +886 2 2730-2863

MS ASIA LIMITED+

## Daisy Dai, CFA

Equity Analyst

Daisy.Dai@morganstanley.com +852 2848-7310

MS TAIWAN LIMITED+

## Tiffany Yeh

Equity Analyst

Tiffany.Yeh@morganstanley.com +886 2 7712-3032

## Lucas Wang

Research Associate

Lucas.Wang@morganstanley.com +886 2 2730-2875

MS ASIA LIMITED+

## Ethan Jia

Research Associate

Ethan.Jia@morganstanley.com +852 3963-2287

![](images/54ba687aef8899ee271daf2a9a521bf637e407a54560dbd5e07b43bc1b3146d3.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## GREATER CHINA TECHNOLOGY SEMICONDUCTORS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Key takeaways from Computex Day 1 + implications for Greater China semis

## Potential volume of Nvidia RTX Spark:

Our checks with PC brands at this year's Computex suggest AI PCs with N1X will need to price at US\$2,899, while N1 models will be priced at US\$1,799. We therefore estimate \~5mn–8mn units of N1X/N1 SoC shipments in 2026, contributing 5–10% of MediaTek's 2026 EPS, assuming an average US\$40 royalty fee per chip.

Exhibit 1: New AI PC announced by Nvidia (N1X)  
![](images/ec42aced4b85d5bb348021df6aca464f79661b075765ce8b9529daae6fac0354.jpg)

<details>
<summary>text_image</summary>

Announcing NVIDIA and
Microsoft Reinvent PC
Powered by RTX Spark

Blackwell RTX GPU
1 Intel GPU AI Performance

20 Core Grace CPU
Custom Built with Medatek

128 GB Unified Memory
600 Slb/s NVLink CBC

Full NVIDIA Stack
CUDA | TensorRIT | NVP4
RTX Ray Tracing | DLSS | Reflex | G-SYHC
</details>

Source: Nvidia

Exhibit 2: MediaTek provides 20-core customized Grace CPU for N1X  
![](images/c9c785d64f9fb88e8f18255a21f14fc0802783166567a76db2f2ab44cf065fac.jpg)

<details>
<summary>text_image</summary>

20-Core Grace CPU
Custom Built With MediaTek
</details>

Source: Nvidia

Exhibit 3: RTX Spark (N1X) provided by MSI (available in 3Q26)  
![](images/90c021950c268223864f2a30ea5d9fd52f018857fdc4fb7bafb37f9470865707.jpg)

<details>
<summary>text_image</summary>

MSI
MSI Prestige N16 Flip AI
NVIDIA RTX Spark
AI3.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
AI3.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 123
AI3.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.25 4.7
AI3.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35 4.35
AI3.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38 4.38
AI3.41 4.41 4.41 4.41 4.41 4.41 4.41 4.41 4.41 4.41 4.41 4.41
AI3.43 4.43 4.43 4.43 4.43 4.43 4.43 4.43 4.43 4.43
AI3.61
AI3.69
AI3.78
AI3.87
AI3.96
AI3.97
AI3.98
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.99
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AI3.
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
AIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
BIA
</details>

Source: MSI

Exhibit 4: RTX Spark (N1X) provided by ASUS (available in 3Q26)  
![](images/e5195b8771c09d05beb11a0adae452bbf727ca2b73796c1b78c5878a498b7f08.jpg)

<details>
<summary>text_image</summary>

ProArt
ASUS RIGHT P14
December 19th December 20th
</details>

Source: ASUS

## Greater China semis in the supply chain:

- Nvidia AI GPU supply chain: TSMC (foundry), ASE (packaging), KYEC (testing), AllRing (equipment)  
- CPO supply chain: FOCI (FAU), Himax (WLO), ASE (optical insertion testing), Hon Precision (optical insertion tool)  
- CPU supply chain: KYEC (Vera and Google CPU test), Aspeed (general server BMC)  
- WoA AI PC: MediaTek (N1X and N1 chips), Macronix (NOR Flash for AI PC)

Exhibit 5: Vera performance could be 1.8x that of highest-performance x86 CPU  
![](images/f446e52b891760afdab7dc339f2d54e40d8044942a6aff9d423ba01ab09dd47e.jpg)

<details>
<summary>bar chart</summary>

| Category | x86 CPU (x1X) | NVIDIA Vera (x1X) |
| :--- | :--- | :--- |
| Compilation | 1X | 1.7X |
| Python | 1X | 1.9X |
</details>

Source: Nvidia

Exhibit 6: Vera CPU cores are not split across chiplets, enabling faster core-to-core connection  
![](images/a2db5fd9292693835f1786d579501bec94f1c483c7bbcad651bebaf62b25669f.jpg)

<details>
<summary>text_image</summary>

88 NVIDIA Custom Olympus Core
With Spatial Multithreading
PCIe Gen 6 CXL 3.1
164 MB L3 Cache
3.4 TB/s Core-to-Core
Bisection Bandwidth
Up to 1.5 TB LPDDR5X Memory
NVLink-C2C 1.8 TB/s Coherent
CPU-CPU and CPU-GPU Interface
</details>

Source: Nvidia

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Charlie Chan; Daisy Dai, CFA; Tiffany Yeh; Daniel Yen, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned $1\%$ or more of a class of common equity securities of the following companies covered in MS: ACM Research Inc, Advanced Micro-Fabrication Equipment Inc, Advanced Wireless Semiconductor Co, Alchip Technologies Ltd, AllRing Tech Co., AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMPT Ltd, Aspeed Technology, Cambricon Technology Corporation, Global Unichip Corp, GlobalWafers Co Ltd, Gudeng Precision, Hon Precision, Hua Hong Semiconductor Ltd, JCET Group Co Ltd, King Yuan Electronics Co Ltd, Macronix International Co Ltd, Montage Technology Co Ltd, MPI Corporation, Nanya Technology Corp., NAURA Technology Group Co Ltd, Novatek, Nuvoton Technology Corporation, Phison Electronics Corp, Realtek Semiconductor, SG Micro Corp., Shanghai Fudan Microelectronics, Silergy Corp., Silicon Motion, TSMC, UMC, Vanguard International Semiconductor, WIN Semiconductors Corp, Winbond Electronics Corp, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Montage Technology Co Ltd.

Within the last 12 months, MS has received compensation for investment banking services from ASMPT Ltd, Montage Technology Co Ltd.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, Shenzhen Longsys Electronics Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from ASE Technology Holding Co. Ltd., King Yuan Electronics Co Ltd, MediaTek, Nanya Technology Corp., Novatek, Nuvoton Technology Corporation, Realtek Semiconductor, Silicon Motion, SMIC, TSMC, UMC, Universal Scientific Ind. (Shanghai), Winbond Electronics Corp, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Advanced Micro-Fabrication Equipment Inc, Alchip Technologies Ltd, AP Memory Technology Corp, ASE Technology Holding Co. Ltd., ASMedia Technology Inc, ASMPT Ltd, Aspeed Technology, Espressif Systems, GigaDevice Semiconductor Beijing Inc, GlobalWafers Co Ltd, Gudeng Precision, Himax Technologies Inc, Hua Hong Semiconductor Ltd, Iluvatar CoreX Semiconductor Co., Ltd., Innoscience, King Yuan Electronics Co Ltd, Macronix International Co Ltd, MediaTek, Montage Technology Co Ltd, Novatek, Phison Electronics Corp, Powerchip Semiconductor Manufacturing Co, Realtek Semiconductor, Shenzhen Longsys Electronics Co Ltd, Silergy Corp., Silicon Motion, TSMC, UMC, Vanguard International Semiconductor, Winbond Electronics Corp, WinWay Technology Co Ltd, WPG Holdings, WT Microelectronics Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide servi

[中间内容因长度限制已省略]

td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb92.65</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,820.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb106.58</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$578.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$81.95</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,380.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$141.50</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$171.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$519.00</td></tr><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$184.80</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb67.65</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$167.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb105.30</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb33.03</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$68.80</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb75.35</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$31.22</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb135.00</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb116.91</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb76.19</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb39.65</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb101.50</td></tr><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$1,075.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,590.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$18,095.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$122.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb162.72</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb474.69</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$175.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$380.20</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb237.00</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$507.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$211.00</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$827.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$85.90</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$653.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb55.64</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$184.50</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$119.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$290.50</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb126.50</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb519.50</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,010.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$804.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$21.91</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$7,175.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$5,515.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$268.05</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,080.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

Tiffany Yeh

© 2026 MS
"""
