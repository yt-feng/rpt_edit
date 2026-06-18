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

<table><tr><td>Page</td><td>Section / Subsection</td><td>Key Messages</td></tr><tr><td>2</td><td>Executive Summary</td><td></td></tr><tr><td>5</td><td>Quantifying impact on European OEMs</td><td></td></tr><tr><td>8</td><td>Analysing China&#x27;s Entry into Europe</td><td>The worst is yet to come</td></tr><tr><td>9</td><td>- The EU LV market suits Chinese OEMs product suite</td><td>China offering is well suited to the EU market</td></tr><tr><td>11</td><td>- Europe is emerging as a key competitive market</td><td>Europe is a strategic focus for China OEMs</td></tr><tr><td>12</td><td>- Conditions could become more challenging from here</td><td>The impact on EU OEMs has only just started</td></tr><tr><td>14</td><td>- Europe&#x27;s individual markets paint differing pictures</td><td>Penetration rhythm: UK/Italy/Spain vs France/Germany</td></tr><tr><td>17</td><td>+ Norway</td><td>A glimpse into an electrified future</td></tr><tr><td>19</td><td>+ Germany</td><td>EU OEMs holding share well, US/SK/Japan share down</td></tr><tr><td>21</td><td>+ Italy</td><td>Ongoing China share gains to EU OEMs (Stellantis)</td></tr><tr><td>24</td><td>+ Spain</td><td>Receptive market, China share gains accelerating</td></tr><tr><td>26</td><td>+ UK</td><td>The no-tariff reference</td></tr><tr><td>29</td><td>+ France</td><td>Resilient market</td></tr><tr><td>31</td><td>- BEV growth is not a constraint for Chinese OEMs</td><td>China increasingly focused on hybrid, following demand</td></tr><tr><td>34</td><td>- Chinese OEMs disproportionately target the C/D-SUV segment</td><td>SUV focus, driving entry-level growth</td></tr><tr><td>37</td><td>- Dealership targets imply significant growth ambitions</td><td>China OEMs growing fast retail networks</td></tr><tr><td>38</td><td>- Six key players dominate Chinese OEM sales</td><td>China OEMs: wide range of EU strategies</td></tr><tr><td>40</td><td>- Product mapping highlights Chinese competitiveness</td><td>Competitive price offerings</td></tr><tr><td>43</td><td>Global Profit Pools Attract Chinese OEMs</td><td>China competition moving faster than consensus</td></tr><tr><td>43</td><td>- Building a position in the European market</td><td>China competition increasing in Europe</td></tr><tr><td>44</td><td>- China weakness further weighs on the outlook</td><td>Weak Chinese market increases pressure on legacy OEMs</td></tr><tr><td>45</td><td>- Globalisation continues despite tariffs</td><td>From exports to localization, driving China OEMs&#x27; volume</td></tr><tr><td>46</td><td>Protective Market Dynamics</td><td>Policy, brand loyalty and residual values</td></tr><tr><td>46</td><td>- European BEV demand is policy driven</td><td>Powertrain flexibility would support legacy OEMs</td></tr><tr><td>46</td><td>- Policy support is emerging</td><td>Driving EU-China OEMs JVs</td></tr><tr><td>47</td><td>- Could European consumers care less for tech?</td><td>China strength may not completely translate into EU</td></tr><tr><td>47</td><td>- Brand loyalty still matters</td><td>Price is testing European brand loyalty</td></tr><tr><td>49</td><td>- Residual values, FinCos, Fleets provide structural support</td><td>The incumbent advantage</td></tr><tr><td>50</td><td>Improving competitiveness</td><td>EU OEMs are not standing still</td></tr><tr><td>50</td><td>- Battery cost reduction</td><td>Key for EV competitiveness</td></tr><tr><td>51</td><td>- Platforms and commonality</td><td>Radical overhaul</td></t

[中间内容因长度限制已省略]

ited, Geely Automobile Holdings listed on the Stock Exchange of Hong Kong Limited. An updated list can be found on HKEx website: http://www.hkex.com.hk.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

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
