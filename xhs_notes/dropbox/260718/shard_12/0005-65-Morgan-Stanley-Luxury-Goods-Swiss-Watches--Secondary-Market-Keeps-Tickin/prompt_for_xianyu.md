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
# Swiss Watches: Secondary Market Keeps Ticking Higher in 2Q26

## Key Takeaways

In 2Q26, all three listed groups – Richemont, Swatch Group and LVMH – recorded a sequential uptick in secondhand prices.

Gains were stronger than in 1Q for LVMH and broadly stable for Richemont/Swatch Group, with LVMH leading at +1.7%, followed by Richemont at +1.3% and Swatch Group at +1.0%.

Among the listed players, the standout performers by brand QoQ include TAG Heuer (+3.8%) from LVMH, Cartier (+2.2%) and Vacheron Constantin (+1.4%) from Richemont, as well as Omega (+0.9%) from Swatch Group.

\- Importantly, the value retention ratio (a barometer of desirability) continued to improve sequentially for most leading brands owned by listed groups, despite retail price increases.

All in all, while most secondhand market metrics improved again in 2Q and the recovery became more broad-based, gains for the listed players remain relatively modest, and VR ratios continue to suggest limited pricing power outside the Big Three in the coming quarters.

Tracking the price evolution of secondhand watches is interesting for equity investors, as, in general, it provides a good barometer of a brand's desirability and thus future pricing power/growth trajectory.

Overall, secondary watch market fundamentals continued to improve in 2Q26, although the pace of recovery moderated. (1) Secondary prices rose by +1.5% QoQ in 2Q26, marking a fourth consecutive quarter of gains above +1% – see Exhibit 1. The recovery is becoming increasingly broad-based, with 27 of the 35 brands we track posting positive QoQ performance in 2Q26, up from 25 in 1Q26. (2) Encouragingly, value retention also continued to slowly but gradually improve for most tracked brands, despite retail price increases. Value Retention is defined as the premium/discount that an in-production watch trades for on the secondary market relative to its retail price. Seven of the eight brands we track posted sequential improvement on a like-for-like basis. This indicates that secondary demand overall remains reasonably healthy and increasingly organic, even as near-term dynamics were distorted by Watches & Wonders anticipation, which drove a surge in listings and strong April performance before prices softened in May and June. All in all, these trends indicated a strengthening of leading brands' desirability for the three listed groups (Richemont, Swatch Group and LVMH). However we caveat

Edouard Aubin
Equity Analyst
Edouard.Aubin@morganstanley.com +44 20 7425-3160

Grace Smalley, CFA
Equity Analyst
Grace.Smalley@morganstanley.com +44 20 7425-9629

Natasha Bonnet
Equity Analyst
Natasha.Bonnet@morganstanley.com +44 20 7677-5723

Research Associate
Cedric.Norest@morganstanley.com +44 20 7425-1462

## BRANDS

Europe
Industry View In-Line

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

that, outside the Big Three, all tracked brands continue to trade at discounts of at least -27% to retail, which should limit pricing power despite improving market momentum.

What's new? We break down the latest trends in the secondary watch market in 2Q26 in this note, using data from the secondary watch market research platform WatchCharts.

## What the data says:

Secondary prices rose +1.5% in 2Q26, a fourth consecutive quarter of gains exceeding +1%. While the pace of growth moderated compared to previous quarters (+2.5% in both 4Q25 and 1Q26), gains were the most widespread of the recovery so far: 27 of the 35 brands we track posted positive QoQ performance (compared to 25 in 1Q26). Within the Big Three, Patek Philippe gained +2.2%, Audemars Piguet gained +1.5%, and Rolex gained +1.0%.

Performance of all leading Groups improved QoQ, led by LVMH (+1.7%). LVMH's performance was driven by TAG Heuer (+3.8%). However, LVMH lacks a consistent performer with significant secondary market share (such as Omega for Swatch Group and Cartier for Richemont); as a result, its long-term performance lags notably behind the other Swiss groups (see Exhibit 7). For Richemont (+1.3%), Cartier (+2.2%) remains the standout performer, while Vacheron Constantin (+1.4%) posted a third consecutive quarter of recovery. Richemont reported its sales for the three months to June this week (see note here): triangulating data points, we estimate that Cartier Watches grew in excess of 20% YoY at constant FX, still far outperforming the rest of the Swiss watch industry (as per Swiss watch exports). Interestingly, the Specialty Watchmakers division also positively surprised (constant FX sales up +8% YoY). Richemont does not disclose its sales by brand, but we estimate that Vacheron, Lange and Jaeger all grew double digit YoY (we think it is particularly encouraging for Jaeger, which had been struggling in recent years). On the secondary market, WatchCharts data shows that Jaeger-LeCoultre saw positive price momentum, rising +1.2% QoQ. As for the Rolex Group (+1.1%) gains essentially track Rolex, though Tudor (+2.6%) prices also rose. Similarly, Swatch Group's (+1.0%) performance is largely reflective of Omega (+0.9%) – though the Swatch brand was the top performer in the quarter (+9.4%). On a YoY basis, all four groups are trending positive for the first time since early 2022 (as per Exhibit 2 below).

Value retention continued to improve for most brands, despite retail price increases. Seven out of the eight brands that we track saw a sequential improvement in VR on a LfL basis. All tracked brands saw secondary prices of in-production models rise QoQ, while at the same time retail price increases also affected five out of the eight brands – most notably Cartier, Rolex, and Patek Philippe. The Big Three (Rolex, PP and AP) continue to trade above retail, led by Patek Philippe (+15.4% VR), while all other brands trade for at least -27% below retail (and up to -38% for IWC).

Exhibit 1: Quarterly sequential performance of the WatchCharts Overall Market price tracker since 2022  
![](images/2ac4bf64137071960a6fa552fb42ac24b95ef5321b371f8ef737940ef67384d3.jpg)  
Source: WatchCharts, MS

Exhibit 2: Performance of WatchCharts price trackers for Swiss groups in 2Q26, QoQ and YoY  
![](images/0054501f236ca81e8d3675a44cee650056dafadd064ef6cfeef58b29230156a7.jpg)  
Source: WatchCharts, MS

# What's new in 2Q26

We outline several of the key trends shaping the secondary watch market in 2Q26.

Secondary prices rose +1.5% in 2Q26, the fourth consecutive quarter of gains exceeding +1%. While the pace of growth moderated compared to previous quarters (+2.5% in both 4Q25 and 1Q26), gains were the most widespread of the recovery so far: 27 of the 35 brands we track posted positive QoQ performance (compared to 25 in 1Q26). Within the Big Three, Patek Philippe gained +2.2%, Audemars Piguet gained +1.5%, and Rolex gained +1.0%.

Performance of all Groups improved QoQ, led by LVMH (+1.7%).

\- LVMH's performance was driven by TAG Heuer (+3.8%) and Zenith (+2.8%).

\- For Richemont (+1.3%), Cartier (+2.2%) remains the standout performer, while Vacheron Constantin (+1.4%) posted a third consecutive quarter of recovery.

\- Rolex SA (+1.1%) gains essentially track Rolex, though Tudor prices also rose (+2.6%).

\- Similarly, Swatch Group's (+1.0%) performance is largely reflective of Omega (+0.9%) – though the Swatch brand was the top performer in the quarter (+9.4%). On a YoY basis, all four groups are trending positive for the first time since early 2022.

Value retention continued to improve for most brands, despite retail price increases. Seven out of the eight brands that we track saw a sequential improvement in VR on a LfL basis. All tracked brands saw secondary prices of in-production models rise QoQ, while at the same time retail price increases also affected five out of the eight brands – most notably Cartier, Rolex, and Patek Philippe. The Big Three continue to trade above retail, led by Patek Philippe (+15.4% VR), while all other brands trade for at least -27% below retail.

## Market health dynamics were defined by rising supply and Watches & Wonders

anticipation. Supply levels reached record or near-record highs for all tracked brands over the past two quarters, driven primarily by an influx of new listings in March and April. We believe this influx was triggered by Watches & Wonders (which saw record-high interest this year) as dealers sought to capitalize on anticipation for the event. While demand remained steady, the surplus of new listings caused prices to stagnate in May and June, dampening momentum from a historically strong April (the best single calendar month of performance since the market downturn began in 2022, according to the WatchCharts Overall Market price tracker). Looking forward, we believe the events of 1H26 will have limited carryover into the third quarter, though the excess supply accumulated (particularly for Rolex) will still need to be absorbed.

Rolex CPO posted record sales of \$186 million in 2Q26. Sales rose +28% QoQ and +67% YoY, with 1H26 sales of \$330 million already representing about two-thirds of the program's FY25 total. Available inventory stands at approximately 11,300 watches valued at \$285 million, with three key retailers (Bucherer, Watches of Switzerland, The 1916 Company) continuing to hold roughly half of total supply across 157 RCPO retailers globally. We also observed a significant increase in median per-retailer sales, from \$578K

in 1H25 to \$899K in 1H26.  
Exhibit 3: Performance of the WatchCharts Overall Market price tracker and price trackers for the Big Three brands since 2021  
![](images/49cfa0487e0ff2ccba348ddbf7f26b5b5b8a668c4de061f5f1d29575c38d957a.jpg)  
Source: WatchCharts, MS

Exhibit 4: Quarterly sequential performance of the WatchCharts Overall Market price tracker since 2022  
![](images/7d09e7792d7d37cd90469e3aa8589555779554411e8144e93631e2cb4d052e7a.jpg)  
Source: WatchCharts, MS

Unless otherwise stated, the analysis of the overall watch market in this report is based on the WatchCharts Overall Market price tracker, which aggregates the secondary market performance of 300 watches from 10 major brands, weighted by annual transaction value in USD. Brand or collection performance is analyzed using its respective WatchCharts price tracker, derived from the top 30 watches within the brand or collection. Group performance is based on the top 30 watches for each brand within the group, all weighted by annual transaction value in USD. WatchCharts data can be subsequently revised or adjusted. The most recent publications prevail.

# Secondary prices see broad-based gains for fourth consecutive quarter in 2Q26

The WatchCharts Overall Market price tracker rose +1.5% in 2Q26, marking the fourth consecutive quarter of gains exceeding +1%. More brands continued to see prices rise than fall, with 27 out of 35 tracked brands being up QoQ and 29 up YoY. However, the vast majority of 2Q26 growth can be attributed to April's performance specifically, primarily driven by anticipation for Watches & Wonders. Specifically, the WatchCharts Overall Market price tracker rose +2.5% in April (the single best month since March 2022), yet fell by -1.0% across May and June. As a result, the pace of growth was in line with previous quarters (+2.3% in 3Q25, +2.5% in 4Q25, +2.5% in 1Q26).

Exhibit 5: Price performance summary for watch brands on the secondary market in 2Q26 (QoQ change)  
![](images/104f0e0c18d5f5944a3159111750cb68ca266ab0471d7a6ca15cbd3b05cc4146.jpg)  
Source: WatchCharts, MS

Exhibit 6: Price performance summary for watch brands on the secondary market in 2Q26 (YoY change)  
![](images/106cae329eb1e34c7a84ab19cddf59bf8a310a1a533095e491f0270ae3aee6e3.jpg)  
Source: WatchCharts, MS

Rolex (+1.0% QoQ): despite sports hype, classic models led the rise. While the GMT-Master collection and specifically the “Pepsi” reference 126710BLRO were in the spotlight, they were not among the brand’s best performers. The GMT-Master collection was up just +0.3% QoQ, and Pepsi prices actually fell by -2.3% QoQ as buyers had front-run the widely anticipated discontinuation. Instead, Rolex’s QoQ gains can primarily be attributed to its dressier models, with Air-King (+2.1%), Datejust (+1.7%), and Sky-Dweller (+1.6%) collections all outperforming. Meanwhile, the Sea-Dweller collection continued to fall, down -2.0% QoQ.

Patek Philippe (+2.2% QoQ) and Audemars Piguet (+1.5% QoQ) both continued to rise in 2Q, though momentum similarly faded in May and June, mirroring Rolex. For Patek, prices of all collections continued to rise QoQ, led by Aquanaut (+3.6%), Gondolo (+2.2%), and Nautilus (+1.7%). Meanwhile for AP, the Royal Oak (+2.0%) was strong while CODE 11.59 (-0.5%) and Royal Oak Offshore (-1.5%) fell QoQ.

Among mid-level brands, TAG Heuer and Breitling emerged as top performers ... TAG Heuer (+3.8% QoQ, +9.9% YoY) and Breitling (+3.8% QoQ, +8.7% YoY) ranked among the top performers both QoQ and YoY.

\- TAG Heuer's recent gains have been concentrated in motorsports collections, most notably Formula 1 (+5.0% QoQ, +8.7% YoY) and Monaco (+2.2% QoQ, +8.0% YoY) – likely driven by increased interest as a result of the brand's return to Formula 1 as its official timekeeper last year.

\- Meanwhile, Breitling's gains were broad-based, led by the Superocean Heritage (+4.5%) and Chronomat (+4.4%). However, both brands generally lag behind mid-level leaders in terms of value retention; popular in-production TAG Heuer Formula 1 models trade more than -60% below retail, while popular in-production Breitling Navitimer, Endurance, and Chronomat models trade for around -40% to -50% below retail.

... while Tudor (+2.6%), Cartier (+2.2%) and Omega (+0.9%) saw continued growth. For Cartier, all collections saw QoQ gains, with Panthère (+3.8%), Santos (+3.0%), and Tank (+2.9%) QoQ performance being particularly strong. Meanwhile, Tudor's performance continues to be driven by its dive watch collections, with the vintage Submariner collection up +3.2% QoQ and the modern Black Bay collection up +2.6% QoQ. Meanwhile, Omega's performance was led by the Speedmaster and De Ville collections, both up +1.4% QoQ.

## All three listed groups were up +1% or more QoQ.

\- LVMH led the listed groups at +1.7%, as a result of strong performance from TAG Heuer (+3.8%, discussed above) and Zenith (+2.8%). Hublot (-0.3%) remains the group's laggard, though prices have stabilized over the past year.

\- For Richemont (+1.3%), Cartier (+2.2%) remains the standout, while Vacheron Constantin (+1.4%) also outperformed thanks to broad gains from its collections (in particular, the Overseas was up +1.6%).

\- For Swatch Group (+1.0%), Omega (+0.9%), Breguet (+2.5%), and Glashütte Original (+1.7%) rose, while Mido (-1.3%) lagged. The Swatch brand jumped +9.4%. On a YoY basis, all four Swiss groups recorded positive performance for the first time since 2022.

Exhibit 7: Performance of WatchCharts price trackers for Swiss groups since 2021  
![](images/8d1bf40f66d83b70bdd34720c333c1de94a77d661fac86b6f375b842c71fa2d3.jpg)  
Source: WatchCharts, MS

Exhibit 8: Performance of WatchCharts price trackers for Swiss groups in 2Q26, QoQ and YoY  
![](images/5

[中间内容因长度限制已省略]

RA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Brands

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/16/2026)</td></tr><tr><td colspan="3">Edouard Aubin</td></tr><tr><td>Adidas (ADSGn.DE)</td><td>O (04/15/2024)</td><td>€182.95</td></tr><tr><td>Birkenstock Holding plc (BIRK.N)</td><td>E (11/06/2023)</td><td>US$42.86</td></tr><tr><td>Ferrari NV (RACE.N)</td><td>O (06/15/2026)</td><td>US$375.74</td></tr><tr><td>Ferrari NV (RACE.MI)</td><td>O (06/15/2026)</td><td>€329.15</td></tr><tr><td>Hermes International S.C.A. (HRMS.PA)</td><td>E (10/06/2025)</td><td>€1,683.50</td></tr><tr><td>Kering (PRTP.PA)</td><td>E (04/10/2026)</td><td>€253.15</td></tr><tr><td>LVMH Moet Hennessy Louis Vuitton SA (LVMH.PA)</td><td>E (01/19/2026)</td><td>€495.80</td></tr><tr><td>Richemont SA (CFR.S)</td><td>O (02/05/2025)</td><td>SFr 197.40</td></tr><tr><td colspan="3">Grace Smalley, CFA</td></tr><tr><td>Burberry (BRBY.L)</td><td>O (05/18/2026)</td><td>1,095p</td></tr><tr><td>EssilorLuxottica SA (ESLX.PA)</td><td>O (07/05/2023)</td><td>€168.20</td></tr><tr><td>Hugo Boss AG (BOSSn.DE)</td><td>E (07/09/2024)</td><td>€37.90</td></tr><tr><td>Luxexperience BV (LUXE.N)</td><td>E (09/15/2023)</td><td>US$8.06</td></tr><tr><td>Pandora A/S (PNDORA.CO)</td><td>E (01/16/2023)</td><td>DKr 800.60</td></tr><tr><td>PUMA SE (PUMG.DE)</td><td>++</td><td>€29.37</td></tr><tr><td colspan="3">Natasha Bonnet</td></tr><tr><td>Avolta AG (AVOL.S)</td><td>E (04/24/2026)</td><td>SFr 48.68</td></tr><tr><td>Brunello Cucinelli (BCU.MI)</td><td>O (01/27/2026)</td><td>€83.98</td></tr><tr><td>Ermenegildo Zegna (ZGN.N)</td><td>E (02/12/2026)</td><td>US$13.44</td></tr><tr><td>Moncler SpA (MONC.MI)</td><td>E (06/22/2026)</td><td>€50.72</td></tr><tr><td>Prada SpA (1913.HK)</td><td>E (06/29/2026)</td><td>HK$40.96</td></tr><tr><td>Salvatore Ferragamo Spa (SFER.MI)</td><td>U (02/12/2026)</td><td>€10.38</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.
"""
