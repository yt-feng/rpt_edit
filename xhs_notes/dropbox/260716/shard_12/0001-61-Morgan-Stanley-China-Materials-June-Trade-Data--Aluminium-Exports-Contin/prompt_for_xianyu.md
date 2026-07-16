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
July 14, 2026 09:04 AM GMT

China Materials | Asia Pacific

# June Trade Data: Aluminium Exports Continue to Rise

Aluminium product exports rose 45% YoY; steel exports also increased 7% YoY.

Steel exports in June grew 7% YoY, flat MoM to 10.3Mt. Exports for 1H26 totaled 54.9Mt, -5.6% YoY. Daily production at CISA member mills declined 3.5% YoY in June (vs -4.4% YoY in May). Assuming similar YoY trends for nationwide total crude steel output, we estimate apparent steel consumption was -9% YoY/-5.8% MoM in June. MTD steel exports remained at a high level in July.

China's imports of copper and copper products (refined + alloys) totalled 478kt in June, up 7% MoM and 3% YoY. The import arbitrage opened intermittently despite rising copper prices, and net refined copper imports reached the highest since September 2025 in May. The Yangshan premium pulled back modestly during the month but has since rallied to \$90/t, the highest since early 2025, indicating continued solid physical demand. Copper ore and concentrate imports declined 1% MoM and YoY to 2.34Mt, while treatment charges continued to fall as strong sulfuric acid prices supported smelter margins.

Aluminium product exports rose 13% MoM and 45% YoY to 711kt in June, an all time high. Aluminium prices moderated during the month, lowering the export arbitrage which may weigh on July exports. Chinese inventories have begun to decline, particularly as semis exports increased.

China's iron ore imports totalled 113Mt in June, up $15\%$ MoM and $6\%$ YoY. Port inventories in China stabilized during the month. Pig iron production at steel mills is down $2\%$ YTD, compared with a $4\%$ YTD decline in crude steel output.

Coal imports up 29% YoY and 29% MoM in June to 43Mt. Total coal imports in 1H26 were up 2% YoY to 225mnt. The import volume in June was higher than market expectations. We think the higher volume was driven by expectations of better demand in the summer peak consumption season and the opening of an arbitrage window in June. The import volume in July is likely to stay high.

MS ASIA LIMITED+

Rachel L Zhang
Equity Analyst
Rachel.Zhang@morganstanley.com +852 2239-1520

Hannah Yang, CFA
Equity Analyst
Hannah.Yang1@morganstanley.com +852 2239-7079

Equity Analyst
Chris.Jiang@morganstanley.com +852 3963-1593

Cynthia Tang
Research Associate
Cynthia.Tang@morganstanley.com +852 3963-4360

MS & CO. INTERNATIONAL PLC+

Amy Gower (Amy Sergeant), CFA
Commodities Strategist
Amy.Gower1@morganstanley.com +44 20 7677-6937

![](images/0ca6dae63d99278671f36ea76ef3c47d106d54d2bed8d87944fc4ff53f7f5b61.jpg)

<table><tr><td colspan="2">GREATER CHINA MATERIALS</td></tr><tr><td>Asia Pacific Industry View</td><td>Attractive</td></tr><tr><td colspan="2">CHINA COAL</td></tr><tr><td>Asia Pacific Industry View</td><td>Cautious</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Additional Trade Data Comments

Exhibit 1: China: June 2026 trade data

<table><tr><td rowspan="2">June 2026Trade data</td><td rowspan="2">June 2025 - June 2026</td><td colspan="12">Jan+Feb</td><td rowspan="2">2026YTD</td></tr><tr><td>Jun-26</td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>2026</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td></tr><tr><td rowspan="3">Finished Steel Imports (kt)</td><td></td><td>441</td><td>451</td><td>465</td><td>512</td><td>827</td><td>517</td><td>496</td><td>503</td><td>548</td><td>500</td><td>452</td><td>470</td><td>2,696</td></tr><tr><td>Change %, YoY</td><td>-6%</td><td>-6%</td><td>-11%</td><td>2%</td><td>-21%</td><td>-17%</td><td>5%</td><td>-6%</td><td>-1%</td><td>-2%</td><td>-10%</td><td>-18%</td><td>-11%</td></tr><tr><td>Change %, MoM</td><td>-2%</td><td>-3%</td><td>-9%</td><td>39%</td><td>NA</td><td>4%</td><td>-1%</td><td>-8%</td><td>10%</td><td>11%</td><td>-4%</td><td>-2%</td><td>NA</td></tr><tr><td rowspan="3">Finished Steel Exports (kt)</td><td></td><td>10,320</td><td>10,341</td><td>9,498</td><td>9,135</td><td>15,591</td><td>11,301</td><td>9,980</td><td>9,782</td><td>10,465</td><td>9,510</td><td>9,836</td><td>9,678</td><td>54,874</td></tr><tr><td>Change %, YoY</td><td>7%</td><td>-2%</td><td>-9%</td><td>-13%</td><td>-8%</td><td>16%</td><td>8%</td><td>-13%</td><td>3%</td><td>0%</td><td>26%</td><td>11%</td><td>-6%</td></tr><tr><td>Change %, MoM</td><td>0%</td><td>9%</td><td>4%</td><td>17%</td><td>NA</td><td>13%</td><td>2%</td><td>-7%</td><td>10%</td><td>-3%</td><td>2%</td><td>-9%</td><td>NA</td></tr><tr><td rowspan="3">Iron Ore Imports (mnt)</td><td></td><td>113</td><td>98</td><td>104</td><td>105</td><td>210</td><td>120</td><td>111</td><td>111</td><td>116</td><td>105</td><td>105</td><td>106</td><td>629</td></tr><tr><td>Change %, YoY</td><td>6%</td><td>0%</td><td>1%</td><td>11%</td><td>10%</td><td>6%</td><td>9%</td><td>7%</td><td>12%</td><td>4%</td><td>2%</td><td>9%</td><td>6%</td></tr><tr><td>Change %, MoM</td><td>15%</td><td>-6%</td><td>-1%</td><td>7%</td><td>NA</td><td>8%</td><td>-1%</td><td>-4%</td><td>11%</td><td>1%</td><td>-1%</td><td>8%</td><td>NA</td></tr><tr><td rowspan="3">Copper and Products Imports (kt)</td><td></td><td>478</td><td>446</td><td>452</td><td>416</td><td>700</td><td>437</td><td>427</td><td>438</td><td>485</td><td>425</td><td>480</td><td>464</td><td>2,491</td></tr><tr><td>Change %, YoY</td><td>3%</td><td>4%</td><td>3%</td><td>-11%</td><td>-16%</td><td>-22%</td><td>-19%</td><td>-13%</td><td>1%</td><td>2%</td><td>10%</td><td>6%</td><td>-5%</td></tr><tr><td>Change %, MoM</td><td>7%</td><td>-1%</td><td>9%</td><td>32%</td><td>NA</td><td>2%</td><td>-3%</td><td>-10%</td><td>14%</td><td>-11%</td><td>3%</td><td>9%</td><td>NA</td></tr><tr><td rowspan="3">Copper Ores &amp; Concentrates Imports (kt)</td><td></td><td>2,335</td><td>2,361</td><td>2,352</td><td>2,630</td><td>4,934</td><td>2,704</td><td>2,526</td><td>2,451</td><td>2,587</td><td>2,759</td><td>2,560</td><td>2,350</td><td>14,609</td></tr><tr><td>Change %, YoY</td><td>-1%</td><td>-1%</td><td>-20%</td><td>10%</td><td>5%</td><td>7%</td><td>13%</td><td>6%</td><td>6%</td><td>7%</td><td>18%</td><td>2%</td><td>-1%</td></tr><tr><td>Change %, MoM</td><td>-1%</td><td>0%</td><td>-11%</td><td>14%</td><td>NA</td><td>7%</td><td>3%</td><td>-5%</td><td>-6%</td><td>8%</td><td>9%</td><td>-2%</td><td>NA</td></tr><tr><td rowspan="3">Aluminum and Products Exports (kt)</td><td></td><td>711</td><td>632</td><td>598</td><td>485</td><td>971</td><td>545</td><td>570</td><td>503</td><td>521</td><td>534</td><td>542</td><td>489</td><td>3,396</td></tr><tr><td>Change %, YoY</td><td>45%</td><td>16%</td><td>15%</td><td>-4%</td><td>13%</td><td>8%</td><td>-15%</td><td>-13%</td><td>-7%</td><td>-10%</td><td>-8%</td><td>-20%</td><td>16%</td></tr><tr><td>Change %, MoM</td><td>13%</td><td>6%</td><td>23%</td><td>13%</td><td>NA</td><td>-4%</td><td>13%</td><td>-3%</td><td>-2%</td><td>-1%</td><td>11%</td><td>-11%</td><td>NA</td></tr><tr><td rowspan="3">Coal Imports (mnt)</td><td></td><td>43</td><td>33</td><td>33</td><td>39</td><td>77</td><td>59</td><td>44</td><td>42</td><td>46</td><td>43</td><td>36</td><td>33</td><td>225</td></tr><tr><td>Change %, YoY</td><td>29%</td><td>-8%</td><td>-13%</td><td>1%</td><td>1%</td><td>12%</td><td>-20%</td><td>-10%</td><td>-3%</td><td>-7%</td><td>-23%</td><td>-26%</td><td>2%</td></tr><tr><td>Change %, MoM</td><td>29%</td><td>1%</td><td>-15%</td><td>26%</td><td>NA</td><td>33%</td><td>6%</td><td>-9%</td><td>8%</td><td>20%</td><td>8%</td><td>-8%</td><td>NA</td></tr></table>

Source: General Administration of Customs, MS.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Amy Gower (Amy Sergeant), CFA; Rachel L Zhang.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Aluminum Corp. of China Ltd., Anhui Honglu Steel Construction, Beijing Oriental Yuhong Waterproof Techn, China Lesso Group Holdings Ltd, China Shenhua Energy, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Flat Glass Group Co Ltd, Ganfeng Lithium Co. Ltd., Jiangxi Copper, JL Mag Rare-Earth Co. Ltd, Shandong Gold Mining Co. Ltd, Shenhuo Coal and Power, Shenzhen Kedali Industry Co Ltd, Sinomine Resource Group Co Ltd, Tianqi Lithium Industries Inc., Yancoal Australia Ltd, Yankuang Energy Group Co Ltd, Zhejiang Huayou Cobalt Co Ltd, Zijin Mining Group. Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of CNGR Advanced Material Co., Ltd., MMG Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for investment banking services from Ganfeng Lithium Co. Ltd., MMG Ltd, Zijin Mining Group.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Yancoal Australia Ltd, Yankuang Energy Group Co Ltd, Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Baoshan Iron & Steel, China Jushi, China Steel Corp., CMOC Group Ltd, Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Zijin Mining Group.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Aluminum Corp. of China Ltd., Beijing Oriental Yuhong Waterproof Techn, CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Jiangxi Copper, MMG Ltd, Shenzhen Kedali Industry Co Ltd, Tianqi Lithium Industries Inc., Yancoal Australia Ltd, Yankuang Energy Group Co Ltd, Zhaojin Mining Industry, Zhejiang Huayou Cobalt Co Ltd, Zijin Gold International, Zijin Mining Group. Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Baoshan Iron & Steel, China Jushi, China Steel Corp., CMOC Group Ltd, CNGR Advanced Material Co., Ltd., Ganfeng Lithium Co. Ltd., Tianqi Lithium Industries Inc., Xinyi Glass Holding Limited, Yankuang Energy Group Co Ltd, Zijin Gold International, Zijin Mining Group.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or i

[中间内容因长度限制已省略]

nd Power (000933.SZ)</td><td>O (09/02/2025)</td><td>Rmb24.68</td></tr><tr><td>Tianshan Aluminum (002532.SZ)</td><td>E (07/08/2026)</td><td>Rmb12.25</td></tr><tr><td>Xinyi Glass Holding Limited (0868.HK)</td><td>U (05/14/2024)</td><td>HK$8.83</td></tr><tr><td>Zhongfu Shenying Carbon Fiber Co Ltd (688295.SS)</td><td>O (08/25/2023)</td><td>Rmb43.40</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Aluminum Corp. of China Ltd. (601600.SS)</td><td>O (11/30/2020)</td><td>Rmb8.86</td></tr><tr><td>Aluminum Corp. of China Ltd. (2600.HK)</td><td>O (11/30/2020)</td><td>HK$8.23</td></tr><tr><td>Baoshan Iron &amp; Steel (600019.SS)</td><td>O (01/16/2016)</td><td>Rmb5.60</td></tr><tr><td>Beijing New Building Materials (000786.SZ)</td><td>O (04/09/2024)</td><td>Rmb17.22</td></tr><tr><td>Beijing Oriental Yuhong Waterproof Techn (002271.SZ)</td><td>E (09/25/2024)</td><td>Rmb10.74</td></tr><tr><td>China Jushi (600176.SS)</td><td>O (12/22/2020)</td><td>Rmb54.52</td></tr><tr><td>China Lesso Group Holdings Ltd (2128.HK)</td><td>U (10/08/2025)</td><td>HK$3.82</td></tr><tr><td>China Steel Corp. (2002.TW)</td><td>U (12/16/2025)</td><td>NT$18.50</td></tr><tr><td>CMOC Group Ltd (3993.HK)</td><td>O (09/24/2019)</td><td>HK$15.95</td></tr><tr><td>CMOC Group Ltd (603993.SS)</td><td>O (06/21/2024)</td><td>Rmb18.21</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (300919.SZ)</td><td>E (01/12/2026)</td><td>Rmb38.27</td></tr><tr><td>CNGR Advanced Material Co., Ltd. (2579.HK)</td><td>O (01/12/2026)</td><td>HK$25.38</td></tr><tr><td>FangDa Carbon New Material Co. Ltd. (600516.SS)</td><td>U (12/16/2024)</td><td>Rmb5.08</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (002460.SZ)</td><td>O (04/20/2026)</td><td>Rmb52.55</td></tr><tr><td>Ganfeng Lithium Co. Ltd. (1772.HK)</td><td>O (12/16/2025)</td><td>HK$41.72</td></tr><tr><td>Henan Liliang Diamond Co. Ltd (301071.SZ)</td><td>U (04/20/2026)</td><td>Rmb75.29</td></tr><tr><td>Jiangsu Dingsheng New Materials (603876.SS)</td><td>U (04/20/2026)</td><td>Rmb20.46</td></tr><tr><td>Jiangxi Copper (0358.HK)</td><td>O (10/08/2025)</td><td>HK$32.18</td></tr><tr><td>Jiangxi Copper (600362.SS)</td><td>O (10/08/2025)</td><td>Rmb43.85</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (6680.HK)</td><td>O (04/23/2025)</td><td>HK$16.86</td></tr><tr><td>JL Mag Rare-Earth Co. Ltd (300748.SZ)</td><td>O (04/23/2025)</td><td>Rmb27.26</td></tr><tr><td>Nine Dragons Paper (2689.HK)</td><td>E (01/04/2023)</td><td>HK$7.57</td></tr><tr><td>Shandong Gold Mining Co. Ltd (600547.SS)</td><td>E (07/09/2026)</td><td>Rmb25.26</td></tr><tr><td>Shandong Gold Mining Co. Ltd (1787.HK)</td><td>E (07/09/2026)</td><td>HK$18.38</td></tr><tr><td>Shandong Nanshan Aluminium Co. (600219.SS)</td><td>E (07/08/2026)</td><td>Rmb4.16</td></tr><tr><td>Tianqi Lithium Industries Inc. (9696.HK)</td><td>O (12/16/2025)</td><td>HK$34.16</td></tr><tr><td>Tianqi Lithium Industries Inc. (002466.SZ)</td><td>O (04/20/2026)</td><td>Rmb47.35</td></tr><tr><td>Weixing New Building Materials (002372.SZ)</td><td>U (10/08/2025)</td><td>Rmb7.63</td></tr><tr><td>Zhaojin Mining Industry (1818.HK)</td><td>E (07/09/2026)</td><td>HK$18.55</td></tr><tr><td>Zijin Gold International (2259.HK)</td><td>O (11/06/2025)</td><td>HK$103.00</td></tr><tr><td>Zijin Mining Group (2899.HK)</td><td>O (11/06/2025)</td><td>HK$30.50</td></tr><tr><td>Zijin Mining Group (601899.SS)</td><td>O (11/06/2025)</td><td>Rmb29.06</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.

\* Historical prices are not split adjusted.

INDUSTRY COVERAGE: China Coal

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/14/2026)</td></tr><tr><td colspan="3">Hannah Yang, CFA</td></tr><tr><td>China Coal Energy Co., Ltd. (601898.SS)</td><td>E (03/16/2026)</td><td>Rmb13.25</td></tr><tr><td>China Coal Energy Co., Ltd. (1898.HK)</td><td>O (03/16/2026)</td><td>HK$10.24</td></tr><tr><td>China Shenhua Energy (1088.HK)</td><td>O (11/02/2017)</td><td>HK$42.30</td></tr><tr><td>China Shenhua Energy (601088.SS)</td><td>E (04/04/2019)</td><td>Rmb43.42</td></tr><tr><td>Shaanxi Coal Industry (601225.SS)</td><td>O (03/16/2026)</td><td>Rmb24.55</td></tr><tr><td>Shanxi Coking Coal (000983.SZ)</td><td>E (10/26/2021)</td><td>Rmb6.35</td></tr><tr><td>Yancoal Australia Ltd (3668.HK)</td><td>O (03/16/2026)</td><td>HK$30.20</td></tr><tr><td>Yankuang Energy Group Co Ltd (1171.HK)</td><td>O (03/16/2026)</td><td>HK$11.03</td></tr><tr><td>Yankuang Energy Group Co Ltd (600188.SS)</td><td>E (03/16/2026)</td><td>Rmb19.23</td></tr><tr><td colspan="3">Rachel L Zhang</td></tr><tr><td>Shougang Fushan Resources Group Limited (0639.HK)</td><td>O (09/15/2022)</td><td>HK$2.24</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.
\* Historical prices are not split adjusted.

© 2026 MS
"""
