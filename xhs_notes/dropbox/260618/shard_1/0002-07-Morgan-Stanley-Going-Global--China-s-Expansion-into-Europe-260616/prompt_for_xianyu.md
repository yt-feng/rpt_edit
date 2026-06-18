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
## Autos & Shared Mobility

# Going Global: China's Expansion into Europe

China's entry into Europe highlights further downside risk to earnings for European OEMs. We trim our estimates, keeping our In-line sector view despite the bottoming earning cycle and recent underperformance. We maintain our preference for Mercedes-Benz over BMW, and reiterate our UW in Renault.

Our new analysis indicates further earnings risk for European OEMs. In a collaborative analysis involving MS European and China Auto teams, we assess: (i) market share trends in all key European countries, (ii) China OEMs' segment exposure and (iii) European OEMs' defensive features, in order to quantify additional share transfer going forward. In our view, the worst is yet to come, and we still see $>10\%$ downside risk to European OEM's FY27 consensus estimates.

Pressure from Chinese OEMs only increases from here. EU OEMs' market share in EU5 has declined from 72% to 67% (2020-25). With continued pressure from Chinese OEMs, we see a decline towards 62% by 2027. Considering OEM exposure to the segments most targeted by Chinese OEMs (SUVs, BEVs, PHEVs, UK, entry-level), we expect downside risk to earnings across the board, and reiterate our preference for premium OEMs over mass market players.

## We reduce MBG/BMW estimates, and reiterate our Underweight in Renault.

Lower UK and SUV exposure positions our Top Pick, Mercedes-Benz (OW), well against peer BMW (OW). Stellantis (EW) has been the largest share donor so far, but we're incrementally most concerned about Renault (UW), which is closest to Chinese OEMs' entry-level pricing territory. Volkswagen's (EW) mass market SUV exposure also presents risk. Although a significant degree of competitive pressure is already embedded in our below-consensus estimates for mass-market OEMs, with this report we reduce MBG and BMW estimates to reflect our new analysis.

Chinese OEMs are poised to drive further share transfer in Europe. Among the leading EV players our China team covers, BYD (1211.HK) and Geely (0175.HK) are capturing growth opportunities in Europe, supported by strong uptake of their new EV models. BYD ranks among the top-selling EV brands in the UK and EU YTD, while Geely continues to gain market share through its diversified product portfolio and premium brand, Zeekr.

Approaching, but not quite at the bottom of the cycle. European OEMs have consistently underperformed the market since April 2024. Cyclical troughs have historically been good entry points in the Auto sector, but it may not work this time, as the incremental pressure coming from China suggests a complex medium-term outlook, keeping us very selective in the sector. Tactically, short-term opportunities may arise around the Middle East conflict and USMCA tariff negotiations.

MS EUROPE S.E., MADRID BRANCH+

## Javier Martinez de Olcoz Cerdan

Equity Analyst

Javier.Martinez.Olcoz@morganstanley.com +34 9141-81289

MS & CO. INTERNATIONAL PLC+

## Shaqeal A Kirunda

Equity Analyst

Shaqeal.Kirunda@morganstanley.com +44 20 7425-0736

## Matias Rodriguez Florez-Estrada

Research Associate

Matias.Rodriguez@morganstanley.com +44 20 7425-1091

MS ASIA LIMITED+

## Tim Hsiao

Equity Analyst

Tim.Hsiao@morganstanley.com +852 2848-1982

## Joey Xu, CFA

Equity Analyst

Joey.Xu@morganstanley.com +852 3963-0337

## Shelley Wang, CFA

Equity Analyst

Shelley.Wang@morganstanley.com +852 3963-0047

## AUTOS & SHARED MOBILITY

Europe

Industry View In-Line

Exhibit 1: European OEMs have continued to see their market share in Europe decline – consensus, optimistically, assumes this ceases  
![](images/18b55e85859a3e3ec02cc44b92734e2aa8d8ae9ac21bb4fa238fe17bb4b0407e.jpg)

<details>
<summary>line chart</summary>

| Quarter | Market Share (%) |
| ------- | ---------------- |
| Q1'10   | 74%              |
| Q4'10   | 75%              |
| Q1'11   | 74%              |
| Q2'11   | 73%              |
| Q3'11   | 74%              |
| Q4'11   | 73%              |
| Q1'12   | 74%              |
| Q2'12   | 73%              |
| Q3'12   | 74%              |
| Q4'12   | 73%              |
| Q1'13   | 74%              |
| Q2'13   | 73%              |
| Q3'13   | 74%              |
| Q4'13   | 73%              |
| Q1'14   | 74%              |
| Q2'14   | 73%              |
| Q3'14   | 74%              |
| Q4'14   | 73%              |
| Q1'15   | 74%              |
| Q2'15   | 73%              |
| Q3'15   | 74%              |
| Q4'15   | 73%              |
| Q1'16   | 74%              |
| Q2'16   | 73%              |
| Q3'16   | 74%              |
| Q4'16   | 73%              |
| Q1'17   | 74%              |
| Q2'17   | 73%              |
| Q3'17   | 74%              |
| Q4'17   | 73%              |
| Q1'18   | 74%              |
| Q2'18   | 73%              |
| Q3'18   | 74%              |
| Q4'18   | 73%              |
| Q1'19   | 74%              |
| Q2'19   | 73%              |
| Q3'19   | 74%              |
| Q4'19   | 73%              |
| Q1'20   | 74%              |
| Q2'20   | 73%              |
| Q3'20   | 74%              |
| Q4'20   | 73%              |
| Q1'21   | 74%              |
| Q2'21   | 73%              |
| Q3'21   | 74%              |
| Q4'21   | 73%              |
| Q1'22   | 74%              |
| Q2'22   | 73%              |
| Q3'22   | 74%              |
| Q4'22   | 73%              |
| Q1'23   | 74%              |
| Q2'23   | 73%              |
| Q3'23   | 74%              |
| Q4'23   | 73%              |
| Q1'24   | 74%              |
| Q2'24   | 73%              |
| Q3'24   | 74%              |
| Q4'24   | 73%              |
| Q1'25   | 74%              |
| Q2'25   | 73%              |
| Q3'25   | 74%              |
| Q4'25   | 73%              |
| Q1'26   | 74%              |
| Q2'26   | 65%              |
| Q3'26   | 66%              |
| Q4'26   | 65%              |
| Q1'27   | 66%              |
| Q2'27   | 65%              |
</details>

Source: Local Auto Associations, MS estimates. Notes: 1) This chart includes Germany, UK, France, Italy and Spain auto sales. 2) This chart includes as EU OEMs: Stellantis, VW, Renault, MBG, BMW, Porsche, Iveco, Lada, Ferrari.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Executive Summary

Consensus expectations remain too optimistic. We see $>10\%$ downside risk for European OEM earnings expectations as Chinese players accelerate expansion into Europe amid weak domestic demand. We think consensus assumptions of flat or growing volumes appear optimistic given Chinese OEMs' localised production efforts, highly competitive product, tactical go-to-market strategy and rapid progress in dealerships, fleet sales, and financing offerings.

China is targeting all of Europe's key market segments. Chinese OEMs' entry into Europe is focused on affordable entry-level vehicles, the large and profitable SUV segment, and both BEV and HEV powertrains, widening Chinese OEMs' addressable market. Renault is most exposed to entry-level competition, while Volkswagen, Mercedes-Benz and BMW face greater SUV exposure. Chinese OEMs have made major progress in the UK, Italy and Spain in recent years, with Chinese share up 7–10 percentage points over 2020–25. Germany and France remain more resilient for now, but we suspect pressure may also start to build up here in the years to come.

Mass market OEMs more exposed, already reflected in our estimates. In our analysis, Volkswagen stands out as having the largest exposure to mass market SUVs – placing it in direct competition with Chinese OEMs in a key market segment. Whilst the company has successfully defended, and even grown share so far, we think the breadth of models available at lower price points ultimately drives demand towards Chinese OEMs. Renault is the only major OEM with meaningful exposure to the entry-level segment. Chinese OEMs are much more focused on this segment than the wider market, putting Renault in competition with some of the cheapest models in the market.

We update our estimates to reflect our new analysis. We think the pressure from Chinese OEMs will only intensify from here, supported by localisation efforts and a weak Chinese auto market. This is already well reflected in our estimates for european mass market OEMs, that, in our view, are more exposed to China competition in Europe and globally, and we now prune our estimates for premium players, reducing MBG 2027e EPS by -6% and BMW 2026e EPS by -4%, also reducing its PT by -5%. Whilst Mercedes-Benz and BMW have mostly been shielded by the premium segment for now, we think Chinese OEMs' sustained efforts to target the D-SUV and C-SUV segments will drive continued competitiveness in the market, likely driving pressure on pricing before any meaningful market share losses.

Exhibit 2: Price Target changes

<table><tr><td colspan="2"></td><td>BMW</td><td>Mercedes</td><td>Porsche</td><td>Volkswagen</td><td>Renault</td><td>Stellantis</td><td>OEMs</td></tr><tr><td rowspan="3">New</td><td>Base</td><td>91.0</td><td>65.0</td><td>42.0</td><td>100.0</td><td>29.0</td><td>7.1</td><td></td></tr><tr><td>Bull</td><td>107.0</td><td>76.0</td><td>51.0</td><td>118.0</td><td>35.0</td><td>9.4</td><td></td></tr><tr><td>Bear</td><td>64.0</td><td>44.0</td><td>32.0</td><td>68.0</td><td>22.0</td><td>4.0</td><td></td></tr><tr><td rowspan="3">Previous</td><td>Base</td><td>96.0</td><td>65.00</td><td>42.00</td><td>100.00</td><td>29.00</td><td>7.1</td><td></td></tr><tr><td>Bull</td><td>114.0</td><td>76.00</td><td>51.00</td><td>118.00</td><td>35.00</td><td>9.4</td><td></td></tr><tr><td>Bear</td><td>67.0</td><td>44.00</td><td>32.00</td><td>68.00</td><td>22.00</td><td>4.0</td><td></td></tr><tr><td rowspan="3">Change</td><td>Base</td><td>-5%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>-1%</td></tr><tr><td>Bull</td><td>-6%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>-1%</td></tr><tr><td>Bear</td><td>-4%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>-1%</td></tr></table>

Source: MS

Do not confuse tactical rallies for underlying improvement. Despite sustained underperformance over the past two years, European OEMs have once again started the year with shares lagging the wider European market. At this time, OEM shares are down \~15-30% YTD, and near-term share price performance is mostly driven by sentiment surrounding the Middle East conflict, and the impact it may have on supply chains, inflation, interest rates, supply chains, and consumer confidence. Valuation multiples are above recent averages, reflecting a degree of optimism about the direction of travel for earnings going forward. Whilst we see the case for a Middle East conflict resolution (or US tariff improvement) related tactical rally, we still think fundamental underlying market dynamics will largely be driven by Chinese OEMs' global expansion efforts. Whilst this is far from a new topic, consensus expectations continue to assume flat or even growing volumes, suggesting further downside could be ahead, and keeping us In-line on the sector for now.

## Quantifying the impact on European OEMs

Further downside risk to mass market OEM earnings. Our new analysis implies $>10\%$ downside risk to mass market OEMs' FY27 earnings. We see European OEM market shares in EU5 continuing to decline, falling to 62% by FY27, from 67% in FY25. The decline is driven by Chinese OEMs' sharp gains in Italy, Spain and the UK – whilst France and Germany remain relatively resilient.

## More Headwinds for European OEMs

The worst is yet to come – market share losses have been modest so far. Despite Chinese OEMs' aggressive plans for growth in Europe, consensus continues to expect flattish volume for European OEMs into the medium term. Chinese OEMs have gained share within the European market, and this has indeed mostly come at the expense of European OEMs, but these losses can be disproportionately attributed to one player – Stellantis, which lost 6%pp during 2020-25. In the meantime, most legacy OEMs have steadily held market share, or even grown it in some cases. EU5 individual country trends highlight that European market share losses are constant, or even accelerating YoY in some countries – suggesting the pressure is likely to continue.

## Dissecting China's Go-To-Market Strategy

Chinese players are highly targeted in where they compete. Across Europe, Chinese OEMs employ a range of entry models, focusing on affordable models targeting the, SUVs, BEVs, PHEVs and HEVs market segments. The Chinese offering is particularly suited to the European light vehicle market, which has struggled with affordability issues, has seen rapid growth in hybrids, and continues to favour SUVs over all other model types.

## Protective Market Dynamics

European OEMs benefit from inherent defence mechanisms. Whilst we think price is ultimately king for many consumers, the very nature of the European automotive market creates some degree of inherent protection for incumbents. Weak underlying BEV demand, technological preferences, protectionist measures, brand loyalty, financing, fleets and residual value are all critical elements of the market that legacy European OEMs

know best.

## Improving Competitiveness

## European OEMs are doing everything in their power to improve competitiveness.

Legacy players are engaging in a broad overhaul of fixed and variable cost structures, software capability, and overall product competitiveness. A major focus is battery cost reduction through LFP adoption, localised sourcing, cell standardisation, and partnerships with key battery players, while software-defined vehicle capabilities, 800V charging systems, advanced ADAS, AI-enabled cockpits, and OTA functionality are increasingly being integrated to close the technology gap with Chinese OEMs.

## Valuation

## Valuation multiples reflecting an improving outlook despite potential earnings risk.

Cyclical sectors tend to trade at low multiples at cycle peaks (exit points), on concerns that OEMs will eventually see a margin reset, and at high multiples at the bottom (entry points). Examining current valuation multiplies implies that the market already expects a considerable portion of earnings cuts to be priced in, with OEM P/E multiples above recent averages. We see valuation multiples as indicative of investor confidence in earnings growth from here, despite the risk of Chinese OEMs continuing to gain share.

Exhibit 3: Report structure

<table><tr><td>Page</td><td>Section / Subsection</td><td>Key Messages</td></tr><tr><td>2</td><td>Executive Summary</td><td></td></tr><tr><td>5</td><td>Quantifying impact on European OEMs</td><td></td></tr><tr><td>8</td><td>Analysing China&#x27;s Entry into Europe</td><td>The worst is yet to come</td></tr><tr><td>9</td><td>- The EU LV market suits Chinese OEMs product suite</td><td>China offering is well suited to the EU market</td></tr><tr><td>11</td><td>- Europe is emerging as a key competitive market</td><td>Europe is a strategic focus for China OEMs</td></tr><tr><td>12</td><td>- Conditions could become more challenging from here</td><td>The impact on EU OEMs has only just started</td></tr><tr><td>14</td><td>- Eur

[中间内容因长度限制已省略]

Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The following companies do business in countries which are generally subject to comprehensive sanctions programs administered or enforced by the U.S. Department of the Treasury's Office of Foreign Assets Control ("OFAC") and by other countries and multi-national bodies: Renault.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Autos & Shared Mobility

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Javier Martinez de Olcoz Cerdan</td></tr><tr><td>Autoliv (ALV.N)</td><td>E (09/24/2021)</td><td>US$128.53</td></tr><tr><td>BMW (BMWG.DE)</td><td>O (11/12/2024)</td><td>€68.34</td></tr><tr><td>Continental AG (CONG.DE)</td><td>E (06/26/2025)</td><td>€73.54</td></tr><tr><td>Forvia (FRVIA.PA)</td><td>E (03/19/2024)</td><td>€10.19</td></tr><tr><td>Mercedes-Benz Group AG (MBGn.DE)</td><td>O (05/20/2024)</td><td>€49.38</td></tr><tr><td>Michelin (MICP.PA)</td><td>E (12/02/2025)</td><td>€33.58</td></tr><tr><td>Opmobility SE (OPM.PA)</td><td>++</td><td>€15.40</td></tr><tr><td>Pirelli &amp; C SpA (PIRC.MI)</td><td>E (09/28/2025)</td><td>€6.50</td></tr><tr><td>Porsche AG (P911_p.DE)</td><td>U (05/20/2024)</td><td>€49.81</td></tr><tr><td>Renault (RENA.PA)</td><td>U (02/03/2026)</td><td>€28.80</td></tr><tr><td>Stellantis (STLAM.MI)</td><td>E (02/03/2026)</td><td>€6.09</td></tr><tr><td>Stellantis (STLA.N)</td><td>E (02/03/2026)</td><td>US$6.87</td></tr><tr><td>Valeo SE (VLOF.PA)</td><td>O (06/26/2025)</td><td>€14.86</td></tr><tr><td>Volkswagen (VOWG_p.DE)</td><td>E (04/25/2025)</td><td>€90.42</td></tr><tr><td colspan="3">Shaqeal A Kirunda</td></tr><tr><td>Aramis Autos (ARAMI.PA)</td><td>O (02/19/2026)</td><td>€3.04</td></tr><tr><td>AUTO1 Group SE (AG1G.DE)</td><td>E (03/26/2024)</td><td>€24.84</td></tr><tr><td>Daimler Truck Holding AG (DTGGe.DE)</td><td>O (01/28/2022)</td><td>€42.70</td></tr><tr><td>Iveco Group NV (IVG.MI)</td><td>++</td><td>€13.90</td></tr><tr><td>Traton SE (8TRA.DE)</td><td>U (01/13/2026)</td><td>€34.48</td></tr><tr><td>Volvo (VOLVb.ST)</td><td>E (01/13/2026)</td><td>SKr 320.20</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
