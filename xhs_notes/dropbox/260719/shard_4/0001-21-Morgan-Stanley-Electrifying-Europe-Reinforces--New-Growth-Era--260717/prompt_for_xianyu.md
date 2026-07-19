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
<table><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Robert Pulleyn</td></tr><tr><td colspan="2">Equity Analyst and Commodity Strategist</td></tr><tr><td>Robert.Pulleyn@morganstanley.com</td><td>+44 20 7425-4388</td></tr><tr><td colspan="2">MS EUROPE S.E., PARIS BRANCH+</td></tr><tr><td colspan="2">Arthur Sitbon, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Arthur.Sitbon@morganstanley.com</td><td>+33 1 42 90 71-03</td></tr><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Sarah E Lester, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Sarah.Lester@morganstanley.com</td><td>+44 20 7425-0551</td></tr><tr><td colspan="2">Marina Fuentes Juan</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Marina.Fuentes.Juan@morganstanley.com</td><td>+44 20 7425-2268</td></tr><tr><td colspan="2">Arthur Descazeaud</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Arthur.Descazeaud1@morganstanley.com</td><td>+44 20 7677-1282</td></tr></table>

Utilities | Europe

# Electrifying Europe Reinforces 'New Growth Era'

## Key Takeaways

We expect a positive read-across for the Utility sector from future policy direction supporting electricity networks & clean power generation.

Draft EU electrification plan aims to increase the share of electricity in final energy consumption from the current 23% to 46% by 2040.

\- Utilities is a key beneficiary via required investment in electricity networks and clean power generation to facilitate this increase.

We estimate the plan implies 2040 Electricity demand of \~5,000 TWh, \~50% higher than our current forecasts, at a 2025-40 CAGR of 4.9% (MSe 2.1%).

Even progress towards this target strengthens the 'New Growth Era' for Utilities, with our preferred EU exposure to this theme in Orsted, RWE, Elia, and E.ON.

Electrifying plan: The EU followed its 22nd April AccelerateEU Response to Energy Crisis with the indicated Electrification plan. The EU targets a doubling in the share of electricity in final energy consumption from the current 23% to 46% by 2040, with next steps in 4Q26. We consider this ambitious, given the slow pace of European electrification thus far, and the current highest regional electrification is \~25% in ASPAC. Furthermore, the IEA's 'Stated Policies Scenario' sees the EU27 reaching 46% by 2050 (and 41% under a 'Current Policies' Scenario) – see Exhibit 4. However, we note that EU/ Government targets are signposts for desired direction of travel, not necessarily literal targets. This was evident in 2022 REPowerEU Renewable targets of 1,236GW capacity vs MSe 783GW (see March 2022 note and May 2022 note.)

We see EU/Europe lagging Asia's progress in Electrification, with China & Japan already approaching 30%. Latest IEA data from 2024 shows China has increased its electrification ratio by 10% points since 2010, Japan by 3%, SE Asia 6%, overall ASPAC 7% vs EU \~1% (Exhibit 1) – also see Electrifying Energy Security, May 2026. Electrification rates vary across the EU, with notable outliers in Iceland, Sweden and France (Exhibit 2), but this is largely a result of legacy power mix (nuclear/geothermal), and progress has stalled over past 10 years (Exhibit 3). However, we find Electrification targets more achievable than wider Decarbonisation aims, given use of existing proven technologies (such as electric public transport, EVs, Electric heat pumps) and the pathway already seen in other regions

Potential material impact for electricity system: We estimate that the EU27 target implies 2040 total power demand of \~5,000TWh, representing a doubling over 2025 demand of 2,529 TWh and \~50% higher than MSe 2040 forecast of \~3,400. The implied 2025-40 CAGR of 4.9% compares to MSe 2.1% (1H26 2% YoY). We further estimate this level of power demand implies EU27 Generation capacity of

## UTILITIES

Europe
Industry View Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

\~3,000GW, up from 2026 1,132 GW (current MSe 2035 forecast for 1,470GW). Given the lead time of new nuclear, we envisage the majority of generation capacity will come from Renewables plus further flexgen (Batteries and CCGT) to balance the system. Such a material expansion in electricity generation will most likely require continued growth in electricity network capex investments to enable generation delivery to demand.

We recognize that such ambitions may be difficult to deliver in 15-year time-frame, and the market is unlikely to capitalize the literal interpretation. Nevertheless, as a signpost for desired direction of travel – and further potential policy support to make progress towards it – we consider it positive for European Utilities even if only half of the targeted increase were to be achieved.

Electrification supports and extends the 'New Growth Era' for European Utilities: Electric Utilities are critical for enabling greater electrification as the key avenue for allocating capital to the Electricity system. We see the pathway to 2030/early 2030s largely set in planned electricity network build-out, much of which is 'catch-up', and the evolving electricity generation mix that is unlikely to change before 2030. The Electrification plan provides support for, and greater market confidence in, the outlook for continued growth >2030. We acknowledge that EPS upgrades related to more capex are unlikely before late decade, given long-lead times in Utility hard assets. Nevertheless, we expect policy support extending the investment time-frame to be reflected in higher valuation multiples. Our preferred EU exposed stocks include RWE for Renewables clean power, Electricity Transmission & Gas plants to balance system, Orsted for new Offshore Wind Capacity and Elia and E.ON for Electricity network growth.

Reducing fossil imports: The electrification drive is now seen through an Energy security lens, rather than solely through Energy Transition dynamics – see Electrifying Energy Security, May 2026. Greater electrification of energy demand, if backed by largely clean power generation, should reduce fossil fuel imports. The EU plan references reducing the cost of fossil fuel imports, namely Gas & Oil, by €260bn by 2040. In power markets, reducing the role of Gas fired power in setting the price in the marginal variable cost curve 'merit order' is critical to lowering wholesale power prices and helping customer bills.

See 6 key charts in next section

## 6 Key Charts

Exhibit 1: EU/Europe electrification lags Asia and has barely increased in recent years  
![](images/0d03c3847023042d63ea03376cbfdccd17f3b0e860503eab3df7e5f3075fb7df.jpg)  
Source: IEA, MS Estimates

Exhibit 2: Electrification rates vary from 14% to 53% across the EU ...  
![](images/2a07f294debec09b4498f7d763937bd3d52914c498c3159db58d19898d875b94.jpg)  
Source: Eurostat, MS Estimates

Exhibit 3: ... yet there has been little improvement in the large economies over the last decade  
![](images/50f9cd86d5ee1be3d1e83d7329a0f5c4f3d60a591e1fd0fb2b7dbdbbad7154d3.jpg)  
Source: Eurostat, MS estimates

Exhibit 4: The EU plan for 46% by 2040 is more ambitious than the IEA Stated Policies Scenario for 2050  
![](images/60d543aaae92d45bcccef1f265e5691b499a63816956dac5a4dcfe0f95af4e81.jpg)  
Source: IEA, MS

Exhibit 5: The EU's 46% target would imply EU power demand of 5,206 TWh, a 4.9% CAGR from 2026, vs MSe 3,400 TWh and 2.1% CAGR  
![](images/b22ff591addf2c571c6dab334f8a6268f788546f3198cbb866f817c0074f7224.jpg)  
Source: ENTSOE, MS Estimates

Exhibit 6: Accommodating higher electricity demand requires a greater step-up in generation & networks than we currently forecast.  
![](images/530b1a97015aeaeecbe868fdbfbfe5f75c956e48dabd73829eadea5836cb9ff0.jpg)  
Source: ENTSOE, MS estimates

## Valuation Methodology and Risks

## Elia (ELI.BR)

Our base case valuation is a SOTP of the two network businesses. For both, we take the value of the RAB in 2026 and DCF the future value of likely outperformance via incentives & opex in Belgium and in Germany. We use a CoE of 6.0% in Belgium and 5.3% in Germany. Our valuation delivers a 22% premium to RAB for ETB and a 46% premium to RAB for 50 Hertz.

## Risks to Upside

■ Lower bond yields

■ Improvement in German regulation to support high capex requirements

## Risks to Downside

■ Higher bond yields

■ Less supportive regulation in Belgium and Germany

■ Failure to deliver on expansive capex plan

## E.ON (EONGn.DE)

Our SOTP valuation is based on DCFs for the Network businesses, including JVs and non-regulated activities, out to 2060, and then includes the final RAB (discounted back). We apply a 4.7% WACC for Germany RAB based networks, 5.4% for non-RAB earnings, 4.8% for Sweden and 6-10% for CEE networks country dependent. We value Retail at 7.5x EV/2025 EBITDA for Germany, 6.5x for the UK, 3.5x for Other, and EIS at 10x EV/EBITDA.

## Risks to Upside

■ Improved German regulatory package (cost of debt, opex & redistribution costs)

■ Higher network capex and EPS CAGR

■ Non-core asset disposals at attractive valuations

■ Increasing DPS growth/payout ratio

## Risks to Downside

■ Higher bond yields triggering de-rating

■ Supply chain challenges to deploying capex

■ Changes to German energy policy reducing RES targets/network capex growth

■ Lower retail margins

■ Lower regulated returns

## Orsted A/S (ORSTED.CO)

We value Orsted on a SOTP, using a project-by-project DCF for Offshore wind and a DCF for Onshore business using a weighted average regional WACC of 6.2% for Offshore and 6.4% for Onshore.

In offshore we includes operational assets, projects under construction (Revolution, Sunrise, H3, Changhua 2B&4, Baltica 2), as well as 4 projects under development. Our price target implies 2027 EV/EBITDA of 12.5x and P/E of 31x with low gearing.

## Risks to Upside

■ Falling bond yields increase NPV

■ Attractive dividend distribution policy

■ Positive newsflow on US projects

■ Attractive terms on new offshore wind projects

■ Consolidation / M&A in renewables

## Risks to Downside

■ Further halt orders or cancellations on US projects (Sunrise & Revolution)

■ Further cost overruns, delays and/or impairments on projects

■ Rising yields eroding NPV

■ Lower power prices

■ Anti renewable energy policies

## RWE AG (RWEG.DE)

We value each business division separately through a DCF. We value Renewables targets to 2030 and assume value of 3GW new German CCGTs. We assume no terminal value and use business-specific WACCs. We apply a 6.7% WACC to Offshore & 6.6% for Onshore Renewables, 7.8% for the Flexgen division, and Trading on 6x EV/EBITDA. We value 15% E.ON stake at market, Amprion using DCF and 1/2 of 3GW data centre site pipeline.

## Risks to Upside

■ More data centre site deals

■ Higher PPA prices support renewable growth

■ Capacity wins in German CCGT auction

■ Lignite foundation to exit coal early

■ Higher power prices driven EPS upgrades

■ Lower bond yields

## Risks to Downside

■ Lower German & UK power prices

■ Price caps, lower carbon prices, intervention

■ Execution / cost overruns in Renewables

■ Higher yield curve

■ Negative evolution in German Energy policy

■ Poor trading

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) and/or MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority. MS & Co. International plc disseminates in the UK research that it has prepared, and which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. As used in this disclosure section, MS includes RMB MS Proprietary Limited, MS Europe S.E., MS & Co International plc and its affiliates.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Marina Fuentes Juan; Sarah E Lester, CFA; Robert Pulleyn; Arthur Sitbon, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Centrica, Drax Group Plc, EDP Energias de Portugal SA, Enagas SA, ENGIE, Naturgy, Pennon Group, Redeia, RWE AG, Severn Trent, Solaria Energia y Medio Ambiente SA, SSE, United Utilities Group PLC, Veolia. Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of A2A SpA, E.ON, EDP Energias de Portugal SA, ENEL, ENGIE, Iberdrola SA, National Grid plc, Naturgy, Orsted A/S, RWE AG, SSE, Veolia.

Within the last 12 months, MS has received compensation for investment banking services from A2A SpA, E.ON, EDP Energias de Portugal SA, Enagas SA, ENEL, ENGIE, Iberdrola SA, National Grid plc, Naturgy, Orsted A/S, Pennon Group, RWE AG, Severn Trent, Snam SpA, SSE, Veolia.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from A2A SpA, Centrica, CEZ, Drax Group Plc, E.ON, EDP Energias de Portugal SA, EDP Renovaveis, Elia, Enagas SA, Endesa SA, ENEL, ENGIE, ERG SpA, Fortum Oyj, Hidroelectrica SA, Iberdr

[中间内容因长度限制已省略]

 an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Utilities

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/16/2026)</td></tr><tr><td colspan="3">Arthur Sitbon, CFA</td></tr><tr><td>CEZ (CEZP.PR)</td><td>E (06/02/2026)</td><td>CZK 1,310.00</td></tr><tr><td>Corporacion Acciona Energia Renovables (ANE.MC)</td><td>E (04/16/2025)</td><td>€21.60</td></tr><tr><td>EDP Energias de Portugal SA (EDP.LS)</td><td>E (02/10/2025)</td><td>€4.52</td></tr><tr><td>EDP Renovaveis (EDPR.LS)</td><td>E (10/24/2025)</td><td>€13.84</td></tr><tr><td>Elia (ELI.BR)</td><td>O (03/18/2026)</td><td>€135.10</td></tr><tr><td>Enagas SA (ENAG.MC)</td><td>E (03/31/2026)</td><td>€16.60</td></tr><tr><td>ENGIE (ENGIE.PA)</td><td>O (10/19/2020)</td><td>€26.65</td></tr><tr><td>Naturgy (NTGY.MC)</td><td>O (05/20/2026)</td><td>€28.66</td></tr><tr><td>NEL ASA (NEL.OL)</td><td>U (10/29/2024)</td><td>NKr 2.18</td></tr><tr><td>Redeia (REDE.MC)</td><td>E (03/25/2026)</td><td>€15.38</td></tr><tr><td>Solaria Energia y Medio Ambiente SA (SLRS.MC)</td><td>E (12/03/2025)</td><td>€18.22</td></tr><tr><td>Veolia (VIE.PA)</td><td>O (12/03/2025)</td><td>€37.22</td></tr><tr><td>Voltalia SA (VLTSA.PA)</td><td>U (06/10/2026)</td><td>€6.67</td></tr><tr><td colspan="3">Ricardo Rezende, CFA</td></tr><tr><td>Hidroelectrica SA (ROH20.BX)</td><td>U (01/22/2024)</td><td>RON 205.00</td></tr><tr><td colspan="3">Robert Pulleyn</td></tr><tr><td>E.ON (EONGn.DE)</td><td>O (12/03/2025)</td><td>€18.90</td></tr><tr><td>Endesa SA (ELE.MC)</td><td>U (12/11/2023)</td><td>€39.54</td></tr><tr><td>ENEL (ENEI.MI)</td><td>U (05/01/2026)</td><td>€10.00</td></tr><tr><td>Fortum Oyj (FORTUM.HE)</td><td>E (05/01/2026)</td><td>€19.58</td></tr><tr><td>Iberdrola SA (IBE.MC)</td><td>E (03/18/2025)</td><td>€20.97</td></tr><tr><td>Orsted A/S (ORSTED.CO)</td><td>O (05/13/2026)</td><td>DKr 148.00</td></tr><tr><td>RWE AG (RWEG.DE)</td><td>O (11/29/2019)</td><td>€55.60</td></tr><tr><td>SSE (SSE.L)</td><td>O (11/03/2020)</td><td>2,429p</td></tr><tr><td>Verbund AG (VERB.VI)</td><td>U (08/09/2023)</td><td>€58.55</td></tr><tr><td colspan="3">Sarah E Lester, CFA</td></tr><tr><td>A2A SpA (A2.MI)</td><td>O (10/31/2025)</td><td>€2.32</td></tr><tr><td>Centrica (CNA.L)</td><td>E (03/02/2026)</td><td>172p</td></tr><tr><td>Drax Group Plc (DRX.L)</td><td>E (03/02/2026)</td><td>766p</td></tr><tr><td>ERG SpA (ERG.MI)</td><td>U (12/11/2023)</td><td>€22.68</td></tr><tr><td>Italgas SpA (IG.MI)</td><td>E (12/03/2025)</td><td>€9.98</td></tr><tr><td>National Grid plc (NG.L)</td><td>O (01/06/2023)</td><td>1,217p</td></tr><tr><td>National Grid plc (NGG.N)</td><td>O (12/11/2025)</td><td>US$82.51</td></tr><tr><td>Pennon Group (PNN.L)</td><td>O (01/23/2026)</td><td>488p</td></tr><tr><td>Severn Trent (SVT.L)</td><td>E (01/23/2026)</td><td>2,980p</td></tr><tr><td>Snam SpA (SRG.MI)</td><td>U (03/16/2021)</td><td>€6.12</td></tr><tr><td>Terna - Rete Elettrica Nazionale SpA (TRN.MI)</td><td>U (12/06/2022)</td><td>€10.06</td></tr><tr><td>United Utilities Group PLC (UU.L)</td><td>E (01/23/2026)</td><td>1,351p</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
