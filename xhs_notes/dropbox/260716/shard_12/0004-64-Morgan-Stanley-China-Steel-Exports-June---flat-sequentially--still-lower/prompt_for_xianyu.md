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
# June - flat sequentially, still lower on the year

China's June finished-steel net exports were flat MoM day-adjusted, annualising at \~119mtpa, but remain \~5% lower YoY YtD. Europe is increasingly insulated as imports are constrained, regional HRC premiums widen and CBAM/safeguards reinforce price floors and EBITDA/t upside.

Flat sequentially, but still lower YoY. China's June finished-steel net exports were flat MoM on a day-adjusted basis, implying an annualised run-rate of \~119mtpa, above our China Materials analyst's 2026 forecast of \~110mt. However, YtD, exports remain \~5% lower YoY, likely underpinned by a combination of growing trade protectionism, as well as China's new export likenesses system to control exports. Domestic production also remains muted, YtD CISA member output is down \~6% YoY, with the latest late-June datapoint pointing to a further 5% decline YoY, heading into the weaker summer season.

In Europe, policy is incrementally constraining imports. CBAM implementation from 1 January 2026 and safeguard tightening from 1 July continue to strengthen local pricing power. Although China accounts directly for only \~11% of Europe's imports YtD, the proposed melted-and-poured clause could materially extend the framework's reach through intermediary countries. Even without a demand recovery, we estimate the measures could leave Europe structurally short by 10-15mt, tightening supply and supporting higher clearing prices. Early evidence is consistent with this view: Kallanish reported last week that ArcelorMittal has raised European coil offers by €50/t, taking HRC to €770/t base delivered, with September order books reportedly full and lead times moving into October (see here) - in spite of the soft demand environment. EU HRC spreads have risen to US\$426/t, above the long-run average of US\$320/t, suggesting that the tighter policy regime is beginning to translate into improved mill pricing power.

We remain constructive, ArcelorMittal preferred play. In Europe, the steel profit pool appears to be migrating back toward domestic mills, with higher import parity, a more robust policy framework, improving utilisation and firmer order intake supporting an EBITDA/t re-base. We continue to prefer European carbon steel equities with local integrated assets, shipment flexibility and leverage to widening regional premia. ArcelorMittal remains our preferred play on the dynamic, offering the greater scope to flex volumes, improve fixed-cost absorption and capture share as marginal tonnes are redirected toward domestic supply. The latest €50/t price hike implies \~US\$1.7bn of annualised gross EBITDA upside before timing, mix, cost and realisation offsets, equivalent to \~17% of 2027 Visible Alpha consensus EBITDA. If sustained, the increase would support upside risk to 4Q26 run-rate EBITDA and 2027 estimates, while reducing 2027 EV/EBITDA from 5.6x to around 4.8x on a commensurate ASP uplift. We also see Salzgitter as a key beneficiary, with the

<table><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Alain Gabriel, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Alain.Gabriel@MorganStanley.com</td><td>+44 20 7425-8959</td></tr><tr><td colspan="2">Ioannis Masvoulas, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Ioannis.Masvoulas@morganstanley.com</td><td>+44 20 7425-0427</td></tr><tr><td colspan="2">Adahna Ekoku</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Adahna.Ekoku@morganstanley.com</td><td>+44 20 7425-0578</td></tr><tr><td colspan="2">Ferdinand Huber</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Ferdinand.Huber@morganstanley.com</td><td>+44 20 7677-2702</td></tr></table>

<table><tr><td colspan="2">EMEA - METALS &amp; MINING</td></tr><tr><td>Europe</td><td></td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td colspan="2">CARBON STEEL</td></tr><tr><td>Europe</td><td></td></tr><tr><td>Industry View</td><td>In-Line</td></tr></table>

Exhibit 1: China's finished steel net exports were flat MoM (day-adjusted) in June  
![](images/e6bbd4c691e5769e7c8fe165e3743b5adb6026f63f15b53ed4b4533416172988.jpg)  
Source: CEIC, MS.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

![](images/7874b9eb5cd5ea284ecc0ed9f67283ec7c2923b55d0a1e78f7015c54e7234af2.jpg)

earnings inflection increasingly visible. See: Earnings Inflect, Leverage Peaks – Overweight (1 Jun 2026)

European Metals & Mining

## Chart gallery: key trade data

Exhibit 2: China steel trade data

<table><tr><td rowspan="2"></td><td colspan="6">China Trade Data</td></tr><tr><td>Gross Exports (kt)</td><td>Gross Imports (kt)</td><td>Data (kt)</td><td>Net Exports MoM, %</td><td>YoY, %</td><td>YTD, %</td></tr><tr><td>Jun-26</td><td>10,320</td><td>441</td><td>9,879</td><td>0%</td><td>7%</td><td>-5%</td></tr><tr><td>May-26</td><td>10,341</td><td>451</td><td>9,890</td><td>10%</td><td>-2%</td><td>-8%</td></tr><tr><td>Apr-26</td><td>9,500</td><td>470</td><td>9,030</td><td>5%</td><td>-9%</td><td>-10%</td></tr><tr><td>Mar-26</td><td>9,130</td><td>510</td><td>8,620</td><td>15%</td><td>-13%</td><td>-10%</td></tr><tr><td>Feb-26</td><td>7,840</td><td>370</td><td>7,470</td><td>2%</td><td>0%</td><td>-7%</td></tr><tr><td>Jan-26</td><td>7,750</td><td>460</td><td>7,290</td><td>-32%</td><td>-14%</td><td>-14%</td></tr><tr><td>Dec-25</td><td>11,300</td><td>520</td><td>10,780</td><td>14%</td><td>18%</td><td>8%</td></tr><tr><td>Nov-25</td><td>9,980</td><td>500</td><td>9,480</td><td>2%</td><td>8%</td><td>7%</td></tr><tr><td>Oct-25</td><td>9,780</td><td>500</td><td>9,280</td><td>-6%</td><td>-13%</td><td>7%</td></tr><tr><td>Sep-25</td><td>10,470</td><td>550</td><td>9,920</td><td>10%</td><td>3%</td><td>10%</td></tr><tr><td>Aug-25</td><td>9,510</td><td>500</td><td>9,010</td><td>-4%</td><td>0%</td><td>11%</td></tr><tr><td>Jul-25</td><td>9,840</td><td>450</td><td>9,390</td><td>2%</td><td>28%</td><td>13%</td></tr><tr><td>Jun-25</td><td>9,680</td><td>470</td><td>9,210</td><td>-9%</td><td>13%</td><td>11%</td></tr><tr><td>May-25</td><td>10,580</td><td>480</td><td>10,100</td><td>2%</td><td>12%</td><td>10%</td></tr><tr><td>Apr-25</td><td>10,460</td><td>520</td><td>9,940</td><td>0%</td><td>16%</td><td>10%</td></tr><tr><td>Mar-25</td><td>10,460</td><td>500</td><td>9,960</td><td>33%</td><td>7%</td><td>8%</td></tr><tr><td>Feb-25</td><td>8,040</td><td>550</td><td>7,490</td><td>-11%</td><td>13%</td><td>8%</td></tr><tr><td>Jan-25</td><td>8,940</td><td>500</td><td>8,440</td><td>-7%</td><td>4%</td><td>4%</td></tr><tr><td>Dec-24</td><td>9,730</td><td>620</td><td>9,110</td><td>3%</td><td>29%</td><td>25%</td></tr><tr><td>Nov-24</td><td>9,280</td><td>470</td><td>8,810</td><td>-17%</td><td>19%</td><td>24%</td></tr><tr><td>Oct-24</td><td>11,180</td><td>540</td><td>10,640</td><td>11%</td><td>46%</td><td>25%</td></tr><tr><td>Sep-24</td><td>10,150</td><td>550</td><td>9,600</td><td>7%</td><td>29%</td><td>22%</td></tr><tr><td>Aug-24</td><td>9,500</td><td>510</td><td>8,990</td><td>23%</td><td>18%</td><td>21%</td></tr><tr><td>Jul-24</td><td>7,830</td><td>500</td><td>7,330</td><td>-10%</td><td>11%</td><td>22%</td></tr><tr><td>Jun-24</td><td>8,740</td><td>570</td><td>8,170</td><td>-9%</td><td>18%</td><td>24%</td></tr></table>

Source: CEIC. MoM = Month on month, YoY = Year on year, YTD = Year to date, N/A = not applicable.

Exhibit 3: China finished steel net exports  
![](images/66777d0ef3cbe48744ee2ad08b2d40de0846135ccba0cad62fd8a76983efd866.jpg)  
Source: CEIC, MS

Exhibit 4: China finished steel gross exports to EU28  
![](images/f4553b9ac68a0482549a1f1b957770b640019a935a5394afd2250187a930e6fb.jpg)  
Source: CEIC, MS

Exhibit5: Price spreads: EU HRC less China HRC  
![](images/f84591f42a24b8c158288281edc19a929f9cf1be97141c66179072e90fc9273a.jpg)  
Source: Bloomberg, MS. \* China domestic prices are based on the Shanghai benchmark for HRC excluding 17% VAT.

Exhibit6: Spreads: EU HRC gross profit per tonne\*  
![](images/1f7e993c7b5f0119edcecb8046519db085a89aa13f91a6bf2555c7f8a7c9fe62.jpg)  
Source: Bloomberg, MS. \* Gross profit per tonne is calculated based on EU HRC prices less the prices of iron ore and coking coal.

Exhibit 7: Monthly steel imports to EU from all destinations  
![](images/1ae579a9e09fc6fa5845f12fa0262fa32b6d7920e985377b6a39a6efe627b45f.jpg)  
Source: Eurofer, Eurostat, MS. Note: There is a discrepancy between data sourced from CEIC and Eurofer.

Exhibit 8: Monthly steel imports to US from all destinations  
![](images/3422fc1cdef53f1cccfda6f62b05e3cc405b09c5d259eee1def81b6a59d5a1a7.jpg)  
Source: US DOC, MS

Exhibit 9: India's monthly steel imports/exports  
![](images/60140119321145e3707e1b65354a1a321ae14078ba16661a95e19b01dea52b06.jpg)  
Source: Joint Plant Committee, MS

Exhibit 10: Russia's monthly steel imports/exports  
![](images/f17388b4339d1d282779577d7b27a716385b7a36afde1e9e81168d954bf328e7.jpg)  
Source: Metal Expert, MS

Exhibit 11: Turkey's monthly steel imports/exports  
![](images/4a85ef9c40751c363aa438fc8eec7e09f824fcbfd8e95484b81a7717752bc663.jpg)  
Source: Metal Expert, MS

Exhibit 12: Vietnam's monthly steel imports/exports  
![](images/be60265ae2d867a0af59b3c53592ebf3072a58c85b9253666937c7fc74ae3a3f.jpg)  
Source: Metal Expert, MS

Exhibit 13: EU total steel imports by geography – Turkey, S. Korea, China and Vietnam dominate  
EU total steel imports by geography (YTD Apr 2026)  
![](images/d531fdbcc3cc2d1b00d528e175c1fc2c4617e8cca0ccbcd35ad78a1e03a30ec1.jpg)  
Exhibit 14: China's steel exports by geography, showing significant fragmentation of recipients  
Source: Eurofer, Eurostat, MS

![](images/5b2fe14afc1928c46fbc1b3895b19ca9bd18023ab435fcf1580790770c2407e2.jpg)

Exhibit 15: EU imports from China (cold rolled sheet) – sharp declines following AD  
![](images/985c95e9eca241fb5242fc55c460d0b982b9b9657f6153d028ac33a627c54b0c.jpg)  
Source: Eurofer, Eurostat, MS  
Source: CEIC

Exhibit 16: EU imports from China (hot dipped) – at low level  
![](images/b220cf0da18865da80b5c270f12f06eca6899445690e82d81c36cac32430d8b8.jpg)  
Source: Eurofer, Eurostat, MS

Exhibit 17: EU imports from China (hot rolled wide strip) – impact of AD driving lower  
![](images/29cec294afa3846fd05a0ee57b9f488ec00bf2b0bcebad1e012b0d9da6404f32.jpg)  
Source: Eurofer, Eurostat, MS

Exhibit 18: EU imports from China (quarto plate) – impact of AD driving lower  
![](images/dd1de1dc022b005e5567c178455637ebb9c3aaa3c7b9d4ac71ac33fc847167c2.jpg)  
Source: Eurofer, Eurostat, MS

## EU Safeguard Quotas & Balances

Exhibit 19: Quarterly Quotas

<table><tr><td rowspan="2">Product</td><td colspan="4">01-Apr-2026 to 30-Jun-2026</td></tr><tr><td>Quota^kt</td><td>B/F^^kt</td><td>Importskt</td><td>Utilised%</td></tr><tr><td colspan="5">Carbon Steel</td></tr><tr><td colspan="5">Non Alloy and Other Alloy Hot Rolled Sheets and Strips</td></tr><tr><td>Turkey</td><td>398</td><td>0</td><td>398</td><td>100%</td></tr><tr><td>India</td><td>225</td><td>0</td><td>225</td><td>100%</td></tr><tr><td>South Korea</td><td>161</td><td>0</td><td>161</td><td>100%</td></tr><tr><td>United Kingdom</td><td>139</td><td>0</td><td>15</td><td>11%</td></tr><tr><td>Serbia</td><td>143</td><td>0</td><td>71</td><td>50%</td></tr><tr><td>Others</td><td>858</td><td>0</td><td>512</td><td>60%</td></tr><tr><td colspan="5">Non Alloy and Other Alloy Cold Rolled Sheets</td></tr><tr><td>India</td><td>163</td><td>0</td><td>8</td><td>5%</td></tr><tr><td>Korea</td><td>95</td><td>0</td><td>94</td><td>100%</td></tr><tr><td>United Kingdom</td><td>88</td><td>0</td><td>1</td><td>1%</td></tr><tr><td>Serbia</td><td>41</td><td>0</td><td>18</td><td>43%</td></tr><tr><td>Others</td><td>335</td><td>0</td><td>96</td><td>29%</td></tr><tr><td colspan="5">Metallic Coated Sheets</td></tr><tr><td>Korea</td><td>38</td><td>179</td><td>216</td><td>100%</td></tr><tr><td>India</td><td>54</td><td>134</td><td>42</td><td>22%</td></tr><tr><td>United Kingdom</td><td>35</td><td>89</td><td>32</td><td>26%</td></tr><tr><td>China</td><td>128</td><td>0</td><td>128</td><td>100%</td></tr><tr><td>Others</td><td>473</td><td>108</td><td>531</td><td>92%</td></tr><tr><td colspan="5">Non Alloy and Other Alloy Quarto Plates</td></tr><tr><td>Ukraine</td><td>254</td><td>0</td><td>0</td><td>0%</td></tr><tr><td>United Kingdom</td><td>5</td><td>0</td><td>0</td><td>0%</td></tr><tr><td>Others</td><td>551</td><td>0</td><td>402</td><td>73%</td></tr><tr><td colspan="5">Stainless Steel</td></tr><tr><td colspan="5">Stainless Hot Rolled Sheets and Strips</td></tr><tr><td>Others</td><td>110</td><td>72</td><td>48</td><td>26%</td></tr><tr><td colspan="5">Stainless Cold Rolled Sheets and Strips</td></tr><tr><td>Korea</td><td>50</td><td>40</td><td>45</td><td>51%</td></tr><tr><td>Taiwan</td><td>46</td><td>27</td><td>26</td><td>35%</td></tr><tr><td>India</td><td>31</td><td>60</td><td>10</td><td>11%</td></tr><tr><td>USA</td><td>25</td><td>71</td><td>1</td><td>1%</td></tr><tr><td>Turkey</td><td>21</td><td>7</td><td>23</td><td>82%</td></tr><tr><td>Others</td><td>53</td><td>16</td><td>29</td><td>41%</td></tr></table>

Source: European Commission, MS. ^ Updated from Annex IV.1 Volumes of tariff-rate quotas, ^^ Unused quotas from previous period brought forward.

## Valuation Methodology and Risks

## ArcelorMittal SA (MT.AS)

In line with the other carbon steel equities, we apply a through-the-cycle multiple on 2027-2028 average EBITDA, which captures the first period in which the new, stronger European trade policy regime is fully reflected in industry economics. We apply a multiple of 7.1x, which is the stock's own historical average.

## Risks to Upside

■ Strong China steel demand or a supply reform programme leading to lower exports.

■ A faster end market demand improvement in key markets.

■ A larger buyback programme.

## Risks to Downside

■ Weaker steel demand in China, boosting exports and pressuring seaborne prices.

■ Escalating trade friction leading to weaker demand

■ Renewed end-market weakness and contracting steel spreads

■ Unexpected (sizeable) investments in new regions

## Salzgitter AG (SZGG.DE)

In line with the other carbon steel equities, we apply a through-the-cycle multiple on estimated average EBITDA over 2027-28, which captures the first period in which the new, stronger European trade policy regime is fully reflected in industry economics. We apply a multiple of 7.0x, which is the stock's own historical average.

## Risks to Upside

■ Further re-rating in Aurubis shares and a higher earnings profile going forward

■ The full margin upside from the new EU policy framework, driving further EBITDA upgrades

■ Successful restructuring of the HKM asset, driving upside to earnings estimates

## Risks to Downside

■ A de-rating of Aurubis shares

■ Worse than expected demand environment in Europe

■ Spending slippage at SALCOS Phases 1/2/3

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) and/or MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Au

[中间内容因长度限制已省略]

f a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: EEMEA - Metals & Mining

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td colspan="3">Alain Gabriel, CFA</td></tr><tr><td>Anglo American (AGLJ.J)</td><td>++</td><td>ZAc 78,780</td></tr><tr><td>Erdemir (EREGL.IS)</td><td>U (09/14/2022)</td><td>TL 40.86</td></tr><tr><td colspan="3">Brian Morgan</td></tr><tr><td>African Rainbow Minerals (ARIJ.J)</td><td>E (04/08/2025)</td><td>ZAc 17,264</td></tr><tr><td>Exxaro Resources Limited (EXXJ.J)</td><td>O (04/08/2025)</td><td>ZAc 19,465</td></tr><tr><td>Implats Limited (IMPJ.J)</td><td>O (01/23/2026)</td><td>ZAc 18,260</td></tr><tr><td>Kumba Iron Ore (KIOJ.J)</td><td>E (10/07/2025)</td><td>ZAc 28,107</td></tr><tr><td>Northam Platinum Limited (NPHJ.J)</td><td>U (03/20/2026)</td><td>ZAc 23,679</td></tr><tr><td>Sibanye-Stillwater (SSWJ.J)</td><td>E (01/23/2026)</td><td>ZAc 3,445</td></tr><tr><td>Thungela Resources Ltd (TGAJ.J)</td><td>U (09/11/2025)</td><td>ZAc 9,679</td></tr><tr><td>Valterra Platinum Limited (VALJ.J)</td><td>E (05/30/2025)</td><td>ZAc 108,221</td></tr><tr><td colspan="3">Christopher Nicholson</td></tr><tr><td>AngloGold Ashanti Ltd (ANGJ.J)</td><td>E (10/18/2023)</td><td>ZAc 131,535</td></tr><tr><td>Gold Fields Limited (GFIJ.J)</td><td>E (04/16/2026)</td><td>ZAc 55,494</td></tr><tr><td>Harmony Gold Mining Company Ltd (HARJ.J)</td><td>O (04/16/2026)</td><td>ZAc 24,802</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## INDUSTRY COVERAGE: Carbon Steel

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/13/2026)</td></tr><tr><td colspan="3">Alain Gabriel, CFA</td></tr><tr><td>ArcelorMittal SA (MT.AS)</td><td>O (01/06/2026)</td><td>€58.04</td></tr><tr><td>Salzgitter AG (SZGG.DE)</td><td>O (06/01/2026)</td><td>€51.40</td></tr><tr><td>SSAB AB (SSABa.ST)</td><td>O (05/05/2026)</td><td>SKr 98.60</td></tr><tr><td>thyssenkrupp AG (TKAG.DE)</td><td>E (03/23/2026)</td><td>€11.68</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.
\* Historical prices are not split adjusted.

© 2026 MS
"""
