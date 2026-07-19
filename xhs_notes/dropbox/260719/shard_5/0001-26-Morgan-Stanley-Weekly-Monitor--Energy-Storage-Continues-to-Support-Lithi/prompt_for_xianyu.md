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
Greater China Materials | Asia Pacific

# Weekly Monitor: Energy Storage Continues to Support Lithium Battery Demand

## Key Takeaways

China unveils draft rules for long-term energy supply contracts, emphasizing "base price+floating price" mechanism for port-based contracts.

Qinyuan County currently has two resumed coal mines, with a total approved capacity of 3.6 million tons.

Planned lithium battery production in July reached a record high, with energy storage accounting for over 40% of demand.

DRC president ordered state revenue agencies to refrain from heavy-handed enforcement operations against mining companies.

\- Indonesia refuses to grant a comprehensive increase to the national nickel production quota.

Base metals: Shanghai copper prices stayed flat and inventories declined 34.9% WoW. Shanghai aluminum prices inched up 0.4% and inventories decreased 1.1% compared to a week ago.

Battery metals: Domestic industrial- and battery-grade hydroxide prices decreased 5.6% WoW and 5.1% WoW, respectively. Industrial- and battery-grade lithium carbonate prices dropped 4.9% and 4.7% WoW, respectively.

Gold: Prices slipped 3.6% WoW, to US\$3,977/oz.

Steel: Shanghai HRC inched up 0.6% while CRC prices rose 0.1% WoW. Shanghai rebar prices edged down 0.8% while Tangshan billet prices increased 0.7% WoW. Long steel inventories at traders decreased 1.3% while those of flat steel dipped 0.9% WoW.

Cement: Prices inched up 0.1% WoW, to Rmb310/t as of July 17.

Coal: QHD5500 prices edged up 0.1% WoW, to Rmb722/t as of July 17; inventory was flattish WoW, at 6.8mnt. BSPI dipped 0.1% WoW.

Glass: Glass fiber industry average 2400tex prices remained unchanged at Rmb4,067/t. Float glass prices dipped 0.2% WoW. Solar glass 3.2mm tempered prices stayed at Rmb15.0/m $^{2}$ .

MS ASIA LIMITED+

Rachel L Zhang
Equity Analyst
Rachel.Zhang@morganstanley.com +852 2239-1520

Chris Jiang
Equity Analyst
Chris.Jiang@morganstanley.com +852 3963-1593

Equity Analyst
Hannah.Yang1@morganstanley.com +852 2239-7079

Cynthia.Tang@morganstanley.com +852 3963-4360

![](images/2a2b2a675f6e3ccae66e40a511e701201623cfcab01a82eee0ead956d76534ed.jpg)

GREATER CHINA MATERIALS

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 1: Price and Inventory Movements Snapshot

<table><tr><td>Steel</td><td>Price/Inventory</td><td>WoW</td><td>MoM</td><td>YoY</td><td>YTD</td></tr><tr><td>HR Sheet 3mm Shanghai</td><td>3,340</td><td>0.6%</td><td>-1.5%</td><td>1.5%</td><td>1.8%</td></tr><tr><td>CR Sheet 1mm</td><td>3,780</td><td>0.1%</td><td>-1.2%</td><td>1.5%</td><td>-0.6%</td></tr><tr><td>Shanghai Rebar incl. 13% VAT (Rmb/t)</td><td>3,139</td><td>-0.8%</td><td>-2.7%</td><td>-3.3%</td><td>-3.5%</td></tr><tr><td>Tangshan Billet inc. 13% VAT (Rmb/t)</td><td>2,990</td><td>0.7%</td><td>-1.0%</td><td>1.4%</td><td>-2.0%</td></tr><tr><td>Flat Steel Inventory (mnt) - as of Jul 16</td><td>6,012</td><td>-0.9%</td><td>1.7%</td><td>21.3%</td><td>37.6%</td></tr><tr><td>Long Steel Inventory (mnt) - as of Jul 16</td><td>5,677</td><td>-1.3%</td><td>4.9%</td><td>33.2%</td><td>76.2%</td></tr><tr><td>Iron ore-China import CFR (US$/t)</td><td>100</td><td>1.0%</td><td>-1.0%</td><td>1.0%</td><td>-3.8%</td></tr><tr><td>GP/ton - as of Jul 17</td><td>Current</td><td>1-wk ago</td><td>1-mt ago</td><td>1-yr ago</td><td>end 2025</td></tr><tr><td>HRC GP/t at Spot, est.(Rmb)</td><td>(67)</td><td>(51)</td><td>5</td><td>193</td><td>9</td></tr><tr><td>CRC GP/t at Spot, est.(Rmb)</td><td>(106)</td><td>(78)</td><td>(41)</td><td>115</td><td>45</td></tr><tr><td>Rebar GP/t at Spot, est.(Rmb)</td><td>(78)</td><td>(75)</td><td>(31)</td><td>192</td><td>119</td></tr><tr><td>Mid-Plate GP/t at Spot, est.(Rmb)</td><td>14</td><td>37</td><td>81</td><td>208</td><td>33</td></tr><tr><td>Base and Precious Metals</td><td>Price/Inventory</td><td>WoW</td><td>MoM</td><td>YoY</td><td>YTD</td></tr><tr><td>Copper Spot (Rmb/t)</td><td>104,250</td><td>0.0%</td><td>-1.3%</td><td>33.3%</td><td>4.9%</td></tr><tr><td>- SHFE/LME Premium (Discount)</td><td>0.4%</td><td></td><td></td><td></td><td></td></tr><tr><td>SHFE Inventory - Copper (Kt)</td><td>80</td><td>-34.9%</td><td>-57.6%</td><td>-1.9%</td><td>-45.0%</td></tr><tr><td>Aluminum Spot (Rmb/t)</td><td>23,220</td><td>0.4%</td><td>-2.7%</td><td>13.2%</td><td>3.4%</td></tr><tr><td>- SHFE/LME Premium (Discount)</td><td>-5.1%</td><td></td><td></td><td></td><td></td></tr><tr><td>SHFE Inventory - Aluminum (Kt)</td><td>476</td><td>-1.1%</td><td>-9.9%</td><td>361.5%</td><td>266.9%</td></tr><tr><td>Zinc Spot (Rmb/t)</td><td>24,430</td><td>-1.2%</td><td>-0.5%</td><td>11.2%</td><td>5.1%</td></tr><tr><td>- SHFE/LME Premium (Discount)</td><td>-11.6%</td><td></td><td></td><td></td><td></td></tr><tr><td>Gold (US$/oz)</td><td>3,977</td><td>-3.6%</td><td>-6.6%</td><td>18.8%</td><td>-7.9%</td></tr><tr><td colspan="6">Battery metals</td></tr><tr><td>Industrial-grade lithium hydroxide - as of Jul 16</td><td>125,250</td><td>-5.6%</td><td>-11.8%</td><td>141.0%</td><td>101.0%</td></tr><tr><td>Battery-grade lithium hydroxide - as of Jul 16</td><td>137,850</td><td>-5.1%</td><td>-10.8%</td><td>140.1%</td><td>98.1%</td></tr><tr><td>Industrial-grade lithium carbonate - as of Jul 16</td><td>147,000</td><td>-4.9%</td><td>-11.2%</td><td>132.2%</td><td>104.7%</td></tr><tr><td>Battery-grade lithium carnobate- as of Jul 16</td><td>151,000</td><td>-4.7%</td><td>-10.9%</td><td>132.7%</td><td>101.2%</td></tr><tr><td colspan="6">Coal</td></tr><tr><td>China Qinhuangdao 5500kcal/kg Rmb/t</td><td>722</td><td>0.1%</td><td>-0.7%</td><td>9.7%</td><td>1.8%</td></tr><tr><td>Qinhuangdao port inventory (mnt)</td><td>6.80</td><td>0.0%</td><td>4.6%</td><td>21.4%</td><td>3.5%</td></tr><tr><td>BSPI (Baohai Coal Index) Rmb/t</td><td>713</td><td>-0.1%</td><td>-0.1%</td><td>7.7%</td><td>1.4%</td></tr><tr><td colspan="6">Cement</td></tr><tr><td>China Cement Price (Rmb/t)</td><td>310</td><td>0.1%</td><td>-1.2%</td><td>-5.3%</td><td>-10.9%</td></tr><tr><td colspan="6">Glass</td></tr><tr><td>Glass Fiber 2400tex Price - industry average (Rmb/t) - as of Jul 16</td><td>4,067</td><td>0.0%</td><td>-2.8%</td><td>4.3%</td><td>3.4%</td></tr><tr><td>Float Glass Price (Rmb/t) - as of Jul 16</td><td>1,160</td><td>-0.2%</td><td>6.8%</td><td>-7.2%</td><td>-19.7%</td></tr><tr><td>PV Glass 3.2mm tempered (Rmb/m2) - as of Jul 16</td><td>15.0</td><td>0.0%</td><td>0.0%</td><td>-16.7%</td><td>-23.1%</td></tr></table>

Source: Bloomberg, FactSet, Mysteel, CCTD, Digital Cement, UM Paper, SCI, MS. Note: Prices as of July 17, 2026, except where specified otherwise.

This report references jurisdiction(s) or person(s) which may be the subject of economic sanctions. Readers are solely responsible for ensuring that their investment activities are carried out in compliance with applicable laws.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Chris Jiang; Hannah Yang, CFA; Rachel L Zhang.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Aluminum Corp. of China Ltd., Anhui Honglu Steel Construction, Beijing Oriental Yuhong Waterproof Techn, China Lesso Group Holdings Ltd, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Flat Glass Group Co Ltd, Ganfeng Lithium Co. Ltd., Jiangxi Copper, JL Mag Rare-Earth Co. Ltd, Shandong Gold Mining Co. Ltd, Shenhuo Coal and Power, Shenzhen Kedali Industry Co Ltd, Sinomine Resource Group Co Ltd, Tianqi Lithium Industries Inc., Zhejiang Huayou Cobalt Co Ltd, Zijin Mining Group.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of CNGR Advanced Material Co., Ltd., MMG Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for investment banking services from Ganfeng Lithium Co. Ltd., MMG Ltd, Zijin Mining Group.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Baoshan Iron & Steel, China Jushi, China Steel Corp., CMOC Group Ltd, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Mining Group.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Baoshan Iron & Steel, China Jushi, China Steel Corp., CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Gold International, Zijin Mining Group.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report. Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

## STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's exis

[中间内容因长度限制已省略]

d>CGN Mining Co Ltd (1164.HK)</td><td>O (01/18/2023)</td><td>HK$2.13</td></tr><tr><td>Chengxin Lithium Group Co. Ltd. (002240.SZ)</td><td>E (12/16/2025)</td><td>Rmb28.88</td></tr><tr><td>GEM Co Ltd (002340.SZ)</td><td>U (04/20/2026)</td><td>Rmb6.30</td></tr><tr><td>Shenzhen Kedali Industry Co Ltd (002850.SZ)</td><td>O (08/21/2023)</td><td>Rmb179.81</td></tr><tr><td>Sinomine Resource Group Co Ltd (002738.SZ)</td><td>O (12/16/2025)</td><td>Rmb46.55</td></tr><tr><td>Yongxing Special Materials Technology (002756.SZ)</td><td>E (11/25/2022)</td><td>Rmb42.54</td></tr><tr><td>Zhejiang Huayou Cobalt Co Ltd (603799.SS)</td><td>O (10/08/2025)</td><td>Rmb37.00</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>China Hongqiao Group (1378.HK)</td><td>O (09/15/2023)</td><td>HK$22.10</td></tr><tr><td>Chuangxin Industries Holdings Ltd. (2788.HK)</td><td>O (03/19/2026)</td><td>HK$15.70</td></tr><tr><td>Flat Glass Group Co Ltd (6865.HK)</td><td>O (07/30/2020)</td><td>HK$6.33</td></tr><tr><td>Flat Glass Group Co Ltd (601865.SS)</td><td>O (07/30/2020)</td><td>Rmb9.00</td></tr><tr><td>MMG Ltd (1208.HK)</td><td>O (12/16/2024)</td><td>HK$7.16</td></tr><tr><td>Shandong Pharmaceutical Glass Co. Ltd. (600529.SS)</td><td>U (04/20/2026)</td><td>Rmb18.80</td></tr><tr><td>Shenhuo Coal and Power (000933.SZ)</td><td>O (09/02/2025)</td><td>Rmb23.98</td></tr><tr><td>Tianshan Aluminum (002532.SZ)</td><td>E (07/08/2026)</td><td>Rmb11.99</td></tr><tr><td>Xinyi Glass Holding Limited (0868.HK)</td><td>U (05/14/2024)</td><td>HK$8.77</td></tr><tr><td>Zhongfu Shenying Carbon Fiber Co Ltd (688295.SS)</td><td>O (08/25/2023)</td><td>Rmb38.88</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Aluminum Corp. of China Ltd. (601600.SS)</td><td>O (11/30/2020)</td><td>Rmb8.44</td></tr><tr><td>Aluminum Corp. of China Ltd. (2600.HK)</td><td>O (11/30/2020)</td><td>HK$7.61</td></tr><tr><td>Baoshan Iron &amp; Steel (600019.SS)</td><td>O (01/16/2016)</td><td>Rmb5.76</td></tr><tr><td>Beijing New Building Materials (000786.SZ)</td><td>O (04/09/2024)</td><td>Rmb18.53</td></tr><tr><td>Beijing Oriental Yuhong Waterproof Techn (002271.SZ)</td><td>E (09/25/2024)</td><td>Rmb10.74</td></tr><tr><td>China Jushi (600176.SS)</td><td>O (12/22/2020)</td><td>Rmb43.80</td></tr><tr><td>China Lesso Group Holdings Ltd (2128.HK)</td><td>U (10/08/2025)</td><td>HK$3.86</td></tr><tr><td>China Steel Corp. (2002.TW)</td><td>U (12/16/2025)</td><td>NT$18.65</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$15.49</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb17.41</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb36.62</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$24.00</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb4.97</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb48.48</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$37.82</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb62.90</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb19.35</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$30.58</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb39.03</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$16.42</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb25.16</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$7.21</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>E (07/09/2026)</td><td>Rmb23.76</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>E (07/09/2026)</td><td>HK$17.15</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>E (07/08/2026)</td><td>Rmb3.98</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$32.46</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb46.99</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb7.79</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>E (07/09/2026)</td><td>HK$17.52</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$96.50</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$29.38</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb28.36</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
