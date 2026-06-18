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

MS and its affilia

[中间内容因长度限制已省略]

8.65</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$19.98</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb20.92</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb48.79</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$31.24</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb6.00</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb71.32</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$61.85</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb70.57</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb26.55</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$37.20</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb47.36</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$18.99</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb31.41</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$7.33</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>O (04/23/2025)</td><td>Rmb28.66</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>O (12/12/2024)</td><td>HK$23.08</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>O (11/30/2020)</td><td>Rmb4.81</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$48.30</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb63.72</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb9.15</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>O (06/21/2024)</td><td>HK$21.40</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$121.50</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$33.56</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb31.31</td></tr></table>

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
