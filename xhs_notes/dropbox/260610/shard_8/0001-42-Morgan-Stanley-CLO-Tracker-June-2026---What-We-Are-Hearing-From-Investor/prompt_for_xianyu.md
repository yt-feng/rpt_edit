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
## Global CLOs

# CLO Tracker June 2026 – What We Are Hearing From Investors

## Key Takeaways

Rising dispersion underscores the importance of manager and deal level selection. Investors favor managers with established track records, demonstrated ability to navigate credit stress, and greater control. Deals with low software exposure and high diversity are viewed favorably.  
On PC CLOs, investors remain highly selective. While required spread premiums varied considerably across investors, many cited a pickup of at least 40bp in PC AAAs as necessary to justify incremental allocation. Several accounts expressed caution against upper-middle-market deals, noting the covenant and documentation erosion seen in the space.  
On USD vs EUR, investor preference is firmly tilted toward the US from the fundamental and structural standpoints, given the greater vulnerability of European economies to energy shock. That said, investors shared our view that demand tailwinds will keep spreads tight at the senior tranches. Relative value considerations are increasingly drawing investors toward European senior tranches.  
- May tracks \~\$17bn of new issuance, rebounding from April's lows (\$6bn). Refi/reset activity was even more notable, with the strongest month YTD at a combined \$39bn, as May's spread tightening gave managers a timely window to reset transactions that had likely been deferred during April's volatility.

Exhibit 1: PC vs BSL AAAs widened to 32bp over the 3 months ending in May  
![](images/1a10e8ed1179829c3de1e39b2117aa2d2721df3740eea4cf90aed5f10398fc79.jpg)

<details>
<summary>line chart</summary>

| Date   | PC vs BSL Basis (rs) | BSL CLO AAA | PC CLO AAA |
|--------|----------------------|-------------|------------|
| May-21 | ~140                 | ~110        | ~55        |
| May-22 | ~90                  | ~130        | ~60        |
| May-23 | ~180                 | ~230        | ~90        |
| May-24 | ~150                 | ~180        | ~70        |
| May-25 | ~80                  | ~130        | ~50        |
| May-26 | ~90                  | ~120        | ~55        |
</details>

Source: PitchBook LCD, MS

MS & CO. LLC

## Joyce Jiang

Strategist

Joyce.Jiang@morganstanley.com +1 212 761-0165

MS & CO. INTERNATIONAL PLC+

## Vasundhara Goel

Strategist

Vasundhara.Goel@morganstanley.com +44 20 7677-0693

MS & CO. LLC

## Gabriel Reyes Esclasans

Strategist

Gabriel.Reyes.Esclasans@morganstanley.com +1 212 761-4134

## James Egan

Strategist

James.F.Egan@MorganStanley.com +1 212 761-4715

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Client Feedback from our Outlook Marketing

We have been on the road meeting with a broad group of CLO investors across the Atlantic. Based on our client conversations, investors are overall more constructive towards US vs Europe on the macro and fundamental backdrop. However, with tight valuation, selectivity remains key. Manager quality, deal structure, and relative value considerations are becoming increasingly important as market participants focus more closely on downside risks and long-term differentiation.

## Manager Selection Remains Paramount

Across nearly all conversations, manager selection emerged as one of the most important considerations for CLO investing. With credit spreads remaining relatively tight across much of the capital stack and AI-disruption concerns driving greater dispersion in collateral performance, investors increasingly focused on manager specific alpha over broad market beta. Investors in general agree with our view that the cycle is characterized less by directional market moves and more by dispersion across portfolios, underscoring the importance of underwriting discipline, portfolio construction, and trading execution.

Investor preferences generally skew toward established managers with long track records and demonstrated performance through multiple credit cycles. This preference appears particularly strong in Europe, where many investors see limited compensation for taking emerging-manager risk given what they see as thin spread pickup for newer managers. Managers with lower software exposure and a well-thought-out framework for assessing AI risk are generally viewed more favorably. Among equity investors, there is a preference for managers with greater control, especially in private credit deals.

Manager consolidation remains topical. While new managers have sprung up at a fast pace, we have also seen a number of acquisitions among managers. Managers compete to grow scale organically or inorganically to broaden capabilities, improve efficiency and deepen relationships with investors and financing providers. Larger managers typically have greater access to warehouse financing, ability to attract large anchor investors, and more dedicated workout and restructuring resources.

Increasingly, investors also view AI and data infrastructure as important differentiators. As AI disruption becomes a more prominent investment consideration, larger platforms with greater resources and budgets are better positioned to develop AI capacity – leveraging AI tools in their credit selection and portfolio management process.

## Private Credit CLOs – Not All Deals Are Created Equal

Private credit CLOs have become a key topic of discussion across our investor meetings, although sentiment has turned more cautious amid a growing number of negative headlines surrounding direct lending, BDCs, and software related risk. Despite the recent spread widening, many investors continued to view current spread premiums vs BSL CLOs as inadequately compensated for the additional complexity, illiquidity, and valuation uncertainty inherent in private credit assets.

As highlighted in our Mid-Year Outlook (A Balancing Act), we expect defaults to ramp up to 5.5% in BSL and 8% in PC through mid 2027, as AI-exposed names are forced to confront their near-term maturity walls. We expect the basis between PC and BSL deals to widen, reflecting a more balanced supply-demand backdrop, and incrementally weaker fundamentals within PC. In particular, we view 40bp spread pickup vs BSL as an interesting entry point for PC AAAs.

Investors we spoke with broadly agree with our views. While they generally do not expect the PC vs BSL AAA spread premium to revisit 60-70bp levels observed a few years ago, given the expansion of the investor base that has structurally compressed the basis, they do view current spread levels too tight to generate appealing risk-reward for the asset class. While required spread premiums varied considerably across investors, many clients shared our view, citing a pickup of at least 40bp as necessary to justify incremental allocation, with some identifying \~150bp on PC AAAs as a practical floor for meaningful participation. The view on spread pickup was similar for both US and EU PC CLOs.

That said, investors acknowledged that private credit is too diverse to be painted in a broad brushstroke. There is wide differentiation across deals. Some investors highlighted the performance should be assessed across multiple dimensions, e.g., by financing- vs arbitrage-driven deals, and by underlying borrower size. Financing transactions, particularly those sponsored by managers with greater control over assets and workout processes, were preferred. Borrower EBITDA size is another important consideration. Several investors expressed greater caution towards upper middle market (MM) segments where documentation standards and covenant protections have gradually weakened. We noted the growing prevalence of cov-lite deals in upper MM segments amid intense competition with the BSL market in Private Credit Tracker 4Q25 – As the Credit Cycle Turns. By contrast, lower MM deals were viewed more constructively, benefitting from stronger covenant protections, smaller lender groups, and greater influence over restricting outcomes, all of which should support higher recovery rates.

Exhibit 2: PC vs BSL AAAs widened to 32bp over the 3 months ending in May  
![](images/c01ebd906f8b72cd6ba9165d2b07ad315f154c959dec9734a63fda5c033fa3bc.jpg)

<details>
<summary>line chart</summary>

| Date   | PC CLO AAA | BSL CLO AAA |
|--------|------------|-------------|
| May-21 | 150        | 110         |
| May-22 | 180        | 140         |
| May-23 | 270        | 220         |
| May-24 | 240        | 160         |
| May-25 | 150        | 130         |
| May-26 | 140        | 120         |
</details>

Source: PitchBook LCD, MS

Exhibit 3: PC vs BSL BBBs widened to levels last seen two years ago  
![](images/d1a0a6cd08cd748b7ae3032a072459e4a646ff265963d90dbcc5920bc2661407.jpg)

<details>
<summary>line chart</summary>

| Date   | PC vs BSL Basis (rs) | BSL CLO BBB | PC CLO BBB |
|--------|----------------------|-------------|------------|
| May-21 | ~300                 | ~300        | ~400       |
| May-22 | ~400                 | ~400        | ~500       |
| May-23 | ~500                 | ~550        | ~700       |
| May-24 | ~450                 | ~450        | ~650       |
| May-25 | ~300                 | ~300        | ~300       |
| May-26 | ~400                 | ~300        | ~450       |
</details>

Source: PitchBook LCD, MS

## Investors Prefer US Risk, but See Better Value in Europe

Regional preferences varied across investors. Most investors still favor US over Europe from a fundamental perspective. While acknowledging the greater software exposure in the US market, investors appeared more concerned about the weaker macro in Europe. The higher exposure of Europe to the energy shock ranks high in the factors, and investors also cited slower growth prospects and longer-term structural challenges as reasons for maintaining an overall preference for US over Europe.

Beyond macro considerations, investors highlighted several structural advantages of the US CLO market. The US benefits from greater market depth, a broader manager universe, and a significantly more diversified issuer base. This diversity is particularly valuable in the current environment, where aggregate credit fundamentals remain healthy, but performance dispersion across sectors and issuers continues to widen.

That said, investors also noted that European CLOs currently screen more attractive on a relative value basis, particularly at the top of the stack. Several investors preferred European AAA/AA tranches to US equivalents, also in expectation of favorable technicals with a potential demand boost from insurers under the new Solvency 2 rules. However, enthusiasm generally diminished further down the capital structure, where investors thought valuation advantages were less compelling relative to the underlying macro and credit risks and more overlap within CLO portfolios. In short, while the fundamental preference remains firmly tilted toward the US, relative value considerations are increasingly drawing investors toward Europe senior tranches.

Exhibit 4: In US NI AAAs screen cheaper to AAs and As  
![](images/e696401285016a971b4442fe546b69181b2f162ada84d1f5f31ccf601ad0a665.jpg)

<details>
<summary>bar chart</summary>

%-Tile Range of US CLO Spreads in Primary Market (2016-Nov)
| Ticker | Current (%) | 2026 Tights (%) |
| :--- | :--- | :--- |
| AAA | 3.2 | 1.0 |
| AA | 0.8 | 0.4 |
| A | 0.0 | 0.0 |
| BBB | 4.8 | 3.2 |
| BB | 8.8 | 6.1 |
</details>

Source: MS, Bloomberg

Exhibit 5: In Europe, NI AAAs screen relatively cheaper, tracking \~45th %-tile  
![](images/dd19f72a17e8cb929ad5a9e48e6df0c6f2e7e827f43e7acb27b6bf9cbbd47c68.jpg)

<details>
<summary>bar chart</summary>

Percentile of EU CLO NI spreads(inc floor) versus 10 year range
| Rating | Current (%) | 2026 tights (%) |
| :--- | :--- | :--- |
| AAA | 44 | 35 |
| AA | 20 | 8 |
| A | 5 | 5 |
| BBB | 11 | 0 |
| BB | 6 | 0 |
| B | 24 | 11 |
</details>

Source: MS

# Market Performance, Issuance, & Relative Value

## Cross-Asset Spreads Monitors

Exhibit 6: US Cross-Asset Spreads Monitor: 12-Month Ranges and Month-end Levels

<table><tr><td rowspan="2"></td><td colspan="6">SPREADS</td><td colspan="7">PRICES</td></tr><tr><td>Current</td><td>1Y Tights</td><td>1Y Wides</td><td>▲ MTD</td><td>▲ YTD</td><td>%-tile, 12m</td><td>Current</td><td>1Y Highs</td><td>1Y Lows</td><td>▲ MTD</td><td>▲ YTD</td><td colspan="2">%-tile, 12m</td></tr><tr><td>US CLO AAA</td><td>123</td><td>123</td><td>136</td><td>-4.50</td><td>-5.62</td><td>4.6% ■</td><td>100.21</td><td>100.35</td><td>99.97</td><td>0.05</td><td>-0.03</td><td>30.5%</td><td>■</td></tr><tr><td>US CLO AA</td><td>164</td><td>162</td><td>182</td><td>0.49</td><td>-6.68</td><td>5.0% ■</td><td>100.15</td><td>100.33</td><td>99.79</td><td>-0.07</td><td>0.03</td><td>83.3%</td><td>■</td></tr><tr><td>US CLO A</td><td>196</td><td>195</td><td>218</td><td>-1.65</td><td>-4.84</td><td>6.5% ■</td><td>100.19</td><td>100.47</td><td>99.78</td><td>-0.02</td><td>-0.16</td><td>14.6%</td><td>■</td></tr><tr><td>US CLO BBB</td><td>326</td><td>318</td><td>352</td><td>-3.51</td><td>0.38</td><td>39.3% ■</td><td>99.80</td><td>100.85</td><td>98.60</td><td>0.10</td><td>-0.42</td><td>23.5%</td><td>■</td></tr><tr><td>US CLO BB</td><td>820</td><td>684</td><td>893</td><td>-21.42</td><td>87.16</td><td>77.6% ■</td><td>93.72</td><td>98.22</td><td>90.57</td><td>0.65</td><td>-2.76</td><td>23.1%</td><td>■</td></tr><tr><td>US Loans</td><td>428</td><td>387</td><td>458</td><td>0.55</td><td>33.49</td><td>80.6% ■</td><td>95.63</td><td>97.77</td><td>94.57</td><td>-0.05</td><td>-1.45</td><td>18.9%</td><td>■</td></tr><tr><td>BB Loans</td><td>250</td><td>245</td><td>268</td><td>-0.08</td><td>-5.64</td><td>7.3% ■</td><td>99.51</td><td>99.88</td><td>98.85</td><td>-0.04</td><td>0.06</td><td>61.7%</td><td>■</td></tr><tr><td>B Loans</td><td>430</td><td>387</td><td>476</td><td>-2.22</td><td>37.95</td><td>76.8% ■</td><td>96.43</td><td>98.43</td><td>94.76</td><td>0.06</td><td>-1.63</td><td>22.7%</td><td>■</td></tr><tr><td>IG Cash Index OAS</td><td>71</td><td>71</td><td>93</td><td>-6.81</td><td>-6.10</td><td>1.5% ■</td><td>94.20</td><td>96.46</td><td>92.15</td><td>0.40</td><td>-0.99</td><td>35.9%</td><td>■</td></tr><tr><td>IG Cash Index OAS BBB</td><td>90</td><td>90</td><td>114</td><td>-7.98</td><td>-8.41</td><td>0.0% ■</td><td>94.83</td><td>97.05</td><td>92.43</td><td>0.39</td><td>-0.95</td><td>36.6%</td><td>■</td></tr><tr><td>HY Cash Index OAS</td><td>256</td><td>248</td><td>338</td><td>-15.04</td><td>-11.87</td><td>2.7% ■</td><td>97.49</td><td>98.53</td><td>95.56</td><td>-0.02</td><td>-0.56</td><td>45.9%</td><td>■</td></tr><tr><td>HY Cash Index OAS BB</td><td>150</td><td>148</td><td>212</td><td>-11.33</td><td>-13.34</td><td>1.1% ■</td><td>98.84</td><td>100.35</td><td>97.24</td><td>0.01</td><td>-1.12</td><td>30.5%</td><td>■</td></tr><tr><td>HY Cash Index OAS B</td><td>272</td><td>250</td><td>367</td><td>-20.09</td><td>4.34</td><td>25.8% ■</td><td>99.53</td><td>100.68</td><td>97.22</td><td>0.23</td><td>-0.81</td><td>49.4%</td><td>■</td></tr></table>

Source: MS, Bloomberg, Markit, PitchBook | LCD. Note: Spreads are in basis points

Exhibit 7: EU Cross-Asset Spreads Monitor: 12-Month Ranges and Month-end Levels

<table><tr><td rowspan="2"></td><td colspan="5">SPREADS

[中间内容因长度限制已省略]

uer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity securities: Vasundhara Goel; Gabriel Reyes Esclasans; James Egan; Joyce Jiang.

© 2026 MS
"""
