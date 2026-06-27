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
# Investor Feedback on Sodium-Ion Batteries

Investor discussions regarding sodium-ion batteries have centered on three key areas: 1) supply chain validation and scalability, 2) suitability for AIDC applications vs. Lithium Iron Phosphate (LFP) batteries, and 3) the new breed's competitive landscape.

## Key Takeaways

On Monday in Munich, Germany, CATL unveiled TENER Sodium ESS – the world's first field-validated sodium-ion battery energy storage system.

CATL is targeting TENER Sodium shipments of 1GWh by end-2026, with global deliveries scheduled to commence in June 2027.

>10GWh of material supply has been secured now; further supply chain expansion is on the way

\- Superior rate capability vs. LFP makes batteries particularly well suited for AIDC storage, apart from cheaper cost and cold performance.

Sodium-ion chemistry sets higher technical barriers to entry given extensive material science innovations, resulting in concentrated supply structure.

Sodium-ion batteries are better positioned than LFP in AIDC storage: Sodium-ion batteries appear particularly well suited to AIDC applications in view of their superior rate capability relative to conventional LFP batteries. Though energy density remains somewhat lower, sodium-ion chemistry generally exhibits faster ion transport kinetics, lower polarization under high-current operation, and better power retention at low temperatures. These characteristics enable stronger charge/discharge performance during frequent acceleration, braking and power-demand fluctuations, which are often seen in AIDCs.

Thus, sodium-ion batteries are especially valuable for AIDC use cases, which require rapid response, high peak power output, and repeated cycling. As a result, we believe they could offer a more compelling balance of performance, durability, and cost than LFP in AIDC applications, making them a natural early-adoption segment for sodium-ion commercialization.

See the following section – Key Themes (cont'd)

MS ASIA LIMITED+
Jack Lu
Equity Analyst
Jack.Lu@morganstanley.com +852 2848-5044

MS ASIA (SINGAPORE) PTE.+

Mayank Maheshwari
Equity Analyst
Mayank.Maheshwari@morganstanley.com

+65 6834-6719

MS EUROPE S.E., MADRID BRANCH+
Javier Martinez de Olcoz Cerdan
Equity Analyst
Javier.Martinez.Olcoz@morganstanley.com

+34 9141-81289

MS & CO. INTERNATIONAL PLC+
Amy Gower (Amy Sergeant), CFA
Commodities Strategist
Amy.Gower1@morganstanley.com +44 20 7677-6937

MS ASIA LIMITED+

Tim Hsiao
Equity Analyst
Tim.Hsiao@morganstanley.com +852 2848-1982

MS & CO. LLC

Andrew S Percoco
Equity Analyst
Andrew.Percoco@morganstanley.com

+1 212 296-4322

MS & CO. INTERNATIONAL PLC, SEOUL BRANCH+

Young Suk Shin
Equity Analyst
Young.Shin@morganstanley.com

+82 2 399-4994

MS ASIA LIMITED+

Kaylee Xu
Equity Analyst
Kaylee.Xu@morganstanley.com +852 2239-1506

![](images/412a37a85b4a8015c946273cbf8cfe0fa3667d4bee2ec13e36b7baad1ce5803c.jpg)

## CHINA ENERGY & CHEMICALS

Asia Pacific
Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Key Themes (cont'd)

Further progress, a new milestone: CATL officially launched the TENER Sodium ESS on Monday this week (the same day we published our Global Insight report on sodium-ion batteries), marking an important milestone in the commercialization of sodium-ion batteries. It is the world's first field-validated sodium-ion energy storage system, indicating that the technology, manufacturing capability, and supply chain have reached commercial readiness. Management targets cumulative shipments of 1GWh by end-2026, with initial deliveries in China scheduled to begin in September 2026 and global deliveries commencing in June 2027.

We view this announcement as a meaningful validation of sodium-ion technology. It moves the industry beyond laboratory demonstrations and pilot projects toward GWh-scale deployment. More importantly, CATL's willingness to commit to commercial volume targets suggests increasing confidence in supply-chain maturity and cost competitiveness. In our view, the TENER Sodium launch could represent a key inflection point for broader sodium-ion adoption in ESS.

Supply chain validation: While sodium-ion batteries benefit from abundant raw materials and significant overlap with existing lithium-ion manufacturing processes, investors are looking for evidence that the entire value chain – from cathode materials and hard carbon anodes to cell manufacturing and system integration – can achieve commercial-scale production with consistent quality and costs.

CATL's recent launch of the TENER Sodium ESS also provided an important validation of supply-chain readiness. Management disclosed that the company has already secured tens of thousands of tonnes of sodium-ion cathode and anode material supply, which is sufficient to support more than 10GWh of sodium-ion battery production, according to our calculation.

We expect CATL to continue expanding its materials ecosystem and supplier base, particularly given its stated target to build 40GWh of sodium-ion manufacturing capacity by the end of this year. In our view, the ability to secure upstream materials at scale may become a key competitive differentiator, further reinforcing the advantages of early movers with integrated R&D, supplier relationships, and manufacturing scale.

Higher barriers to entry in the new breed: We believe sodium-ion batteries carry higher technical barriers to entry than LFP, stemming from the extensive material science innovations required across cathode chemistry, hard-carbon anodes or anode-free solutions, electrolyte formulation, and cell architecture. Unlike LFP, whose supply chain has become largely mature and commoditized after a decade of industry scaling, sodium-ion remains in an earlier stage where performance differentiation depends heavily on proprietary materials and manufacturing know-how. This has resulted in a more concentrated industry structure, with CATL and a small number of leading players holding meaningful technology, capacity, and supply-chain advantages. As commercialization accelerates, we expect the sodium-ion market to remain more consolidated than the LFP market, supporting stronger pricing power for incumbents, with higher barriers to entry for newcomers.

## Key technical challenges in producing high-quality sodium-ion batteries include:

Cathode material optimization: Sodium-ion cathodes suffer from greater structural instability than LFP, requiring sophisticated materials engineering, surface coating, and elemental doping to simultaneously improve energy density, cycle life and safety. Different pathways (layered oxides, Prussian Blue, polyanion systems) each present unique trade-offs.

Anode development: Unlike lithium batteries, which typically use mature graphite anodes, sodium-ion batteries rely predominantly on hard carbon. Achieving high initial Coulombic efficiency, low irreversible capacity loss, and consistent pore structure remains a major technical hurdle and manufacturing challenge.

Importantly, CATL has also developed an anode-free sodium-ion battery architecture for EV applications, which significantly improves energy density and narrows the gap versus LFP. Management has indicated that next-generation sodium-ion batteries are approaching high-end LFP-level energy density, potentially removing one of the last major obstacles to broader adoption in passenger vehicles. The achievement is technologically significant because anode-free designs require sophisticated control of sodium plating/stripping behavior, electrolyte stability, interface engineering and cycle-life management.

In our view, this further reinforces the notion that sodium-ion batteries are not merely a lower-cost alternative chemistry, but a technology platform requiring deep materials-science expertise and substantial R&D investment. Such capabilities are concentrated among a small number of industry leaders, potentially resulting in a more consolidated market structure than the commoditized LFP industry.

Electrolyte and SEI engineering: Sodium-ion batteries require highly customized electrolyte formulations to stabilize the solid-electrolyte interphase (SEI), improve cycle life and support wide-temperature operation. This remains a key area of proprietary differentiation among leading players.

Low-temperature and high-rate performance balancing. While sodium-ion batteries naturally exhibit strong low-temperature and high-rate characteristics, achieving these advantages without sacrificing cycle life, energy density and safety requires substantial cell-level optimization.

Manufacturing yield and consistency: Although sodium-ion production can leverage much of the lithium-ion manufacturing infrastructure, achieving automotive- and utility-grade consistency requires extensive process tuning. Yield management and cell consistency are especially important given the relatively immature state of the supply chain.

System integration and commercialization validation: Utility-scale deployments require validation of long-duration performance, thermal stability, safety and degradation characteristics. CATL's recent launch of the TENER Sodium ESS highlights the importance of proving readiness not only at the cell level, but across manufacturing, supply chain and system integration.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Tim Hsiao; Jack Lu; Mayank Maheshwari; Javier Martinez de Olcoz Cerdan; Andrew S Percoco; Young Suk Shin; Kaylee Xu.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of May 29, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: China Oilfield Services Ltd., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, PetroChina, Shandong Sinocera Functional Material, Shenzhen Senior Technology Material Co, Sunresin New Materials Co Ltd.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Bluestar Adisseo Co, Contemporary Amperex Technology Co. Ltd.. Within the last 12 months, MS has received compensation for investment banking services from Bluestar Adisseo Co, Contemporary Amperex Technology Co. Ltd..

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Bluestar Adisseo Co, China Petroleum & Chemical Corp., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, Hengli Petrochemical Co Ltd, Ningbo Ronbay New Energy Technology, REPT Battero Energy Co, Rongsheng Petrochemical Co Ltd, Shanghai Putailai New Energy Tech Co Ltd, Shenzhen Senior Technology Material Co, Wanhua Chemical, Yunnan Energy New Material Co Ltd, Zhejiang NHU Co. Ltd..

Within the last 12 months, MS has received compensation for products and services other than investment banking services from China Petroleum & Chemical Corp., CNOOC, PetroChina, Wanhua Chemical.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Bluestar Adisseo Co, China Petroleum & Chemical Corp., Contemporary Amperex Technology Co. Ltd., EVE Energy Co Ltd, Hengli Petrochemical Co Ltd, Ningbo Ronbay New Energy Technology, REPT Battero Energy Co, Rongsheng Petrochemical Co Ltd, Shanghai Putailai New Energy Tech Co Ltd, Shenzhen Senior Technology Material Co, Wanhua Chemical, Yunnan Energy New Material Co Ltd, Zhejiang NHU Co. Ltd..

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related ser

[中间内容因长度限制已省略]

general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Energy & Chemicals

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/25/2026)</td></tr><tr><td colspan="3">Jack Lu</td></tr><tr><td>Bluestar Adisseo Co (600299.SS)</td><td></td><td>Rmb9.04</td></tr><tr><td>China Oilfield Services Ltd. (2883.HK)</td><td>E (03/28/2026)</td><td>HK$6.43</td></tr><tr><td>China Oilfield Services Ltd. (601808.SS)</td><td>U (03/28/2026)</td><td>Rmb11.09</td></tr><tr><td>China Petroleum &amp; Chemical Corp. (600028.SS)</td><td>E (08/19/2024)</td><td>Rmb4.55</td></tr><tr><td>China Petroleum &amp; Chemical Corp. (0386.HK)</td><td>O (07/29/2025)</td><td>HK$4.10</td></tr><tr><td>CNOOC (0883.HK)</td><td>O (03/17/2021)</td><td>HK$21.22</td></tr><tr><td>Contemporary Amperex Technology Co. Ltd. (300750.SZ)</td><td>O (06/25/2025)</td><td>Rmb401.90</td></tr><tr><td>Contemporary Amperex Technology Co. Ltd. (3750.HK)</td><td>O (05/04/2026)</td><td>HK$716.50</td></tr><tr><td>EVE Energy Co Ltd (300014.SZ)</td><td>E (05/31/2022)</td><td>Rmb66.81</td></tr><tr><td>Gotion High Tech Co Ltd (002074.SZ)</td><td>E (04/17/2023)</td><td>Rmb28.66</td></tr><tr><td>Guangzhou Tinci Materials Technology Co (002709.SZ)</td><td>E (01/08/2026)</td><td>Rmb55.20</td></tr><tr><td>Hengli Petrochemical Co Ltd (600346.SS)</td><td>++</td><td>Rmb18.21</td></tr><tr><td>Ningbo Ronbay New Energy Technology (688005.SS)</td><td>U (10/27/2025)</td><td>Rmb32.80</td></tr><tr><td>Ningxia Baofeng Energy Group Co., Ltd. (600989.SS)</td><td>E (04/15/2026)</td><td>Rmb21.17</td></tr><tr><td>PetroChina (601857.SS)</td><td>O (08/19/2024)</td><td>Rmb9.06</td></tr><tr><td>PetroChina (0857.HK)</td><td>O (03/17/2021)</td><td>HK$8.73</td></tr><tr><td>REPT Battero Energy Co (0666.HK)</td><td>E (10/20/2025)</td><td>HK$13.34</td></tr><tr><td>Rongsheng Petrochemical Co Ltd (002493.SZ)</td><td>E (07/29/2025)</td><td>Rmb11.71</td></tr><tr><td>Shanghai Putailai New Energy Tech Co Ltd (603659.SS)</td><td>U (10/27/2025)</td><td>Rmb28.55</td></tr><tr><td>Shenzhen Senior Technology Material Co (300568.SZ)</td><td>E (01/08/2026)</td><td>Rmb17.82</td></tr><tr><td>Yunnan Energy New Material Co Ltd (002812.SZ)</td><td>O (10/27/2025)</td><td>Rmb68.27</td></tr><tr><td colspan="3">Kaylee Xu</td></tr><tr><td>Jiangsu Cnano Technology Co Ltd (688116.SS)</td><td>U (03/10/2025)</td><td>Rmb40.10</td></tr><tr><td>Jiangsu Yangnong Chemical (600486.SS)</td><td>O (06/12/2026)</td><td>Rmb53.80</td></tr><tr><td>Shandong Sinocera Functional Material (300285.SZ)</td><td>E (03/23/2026)</td><td>Rmb98.40</td></tr><tr><td>Shenzhen Capchem Technology Co Ltd (300037.SZ)</td><td>E (06/07/2023)</td><td>Rmb90.29</td></tr><tr><td>Sunresin New Materials Co Ltd (300487.SZ)</td><td>E (10/25/2024)</td><td>Rmb60.15</td></tr><tr><td>Wanhua Chemical (600309.SS)</td><td>O (04/10/2026)</td><td>Rmb73.61</td></tr><tr><td>Zhejiang NHU Co. Ltd. (002001.SZ)</td><td>E (01/26/2026)</td><td>Rmb30.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
