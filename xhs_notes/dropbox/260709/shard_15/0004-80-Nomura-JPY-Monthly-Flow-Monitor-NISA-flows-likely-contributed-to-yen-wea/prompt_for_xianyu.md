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
# JPY Monthly Flow Monitor

Foreign Exchange - Global

## NISA flows likely contributed to yen weakness in June

Outward direct investment in May remained above the H2 2025 average pace

\- Banks: Banks were net sellers of foreign bonds, with foreign bond selling continuing for six consecutive months, possibly reflecting the reduced attractiveness of US Treasury investments via asset swaps.

\- Trust accounts: Trust accounts were large net sellers of foreign equities (JPY1.3trn) and large net buyers of foreign bonds (JPY1.5trn), likely reflecting rebalancing from equities into bonds after strong equity market gains. Our analysis does not suggest clear signs of a GPIF portfolio review aimed at materially raising domestic bond allocations at this stage.

\- Life insurers: Life insurers were net buyers of foreign equities (JPY111bn) and marginal net sellers of foreign bonds (JPY41bn). Lifers had shown a cautious stance on FX-unhedged bonds in FY2026 investment plans, but we do not see large-scale foreign bond selling so far.

\- Investment trusts: Investment trusts remained net buyers of foreign equities (JPY767bn), while selling foreign bonds (JPY120bn). NRI's high-frequency data suggest public investment trusts increased in size, so MOF's data may reflect net sales by private equity funds in June.

\- Foreign investors: Foreign investors were net sellers of Japanese securities by JPY5.5trn, selling both Japanese equities (JPY3.0trn) and Japanese bonds (JPY2.5trn). Bond selling likely reflected fiscal concerns and concerns that the BOJ was behind the curve.

\- Current account: Japan's current account surplus narrowed to JPY3.1trn in May from JPY4.2trn in April, broadly in line with the 2026 average. The narrowing mainly reflected payback from the previous month's rise in R&D services and a weaker trade balance

Fig. 1: So called NISA flows following the launch of the new NISA scheme  
![](images/7b42003bea92c0faeb8009b5018c44a734fbec98ba1175f7fe8b4c7195c9de28.jpg)  
Source: NOM, NRI, Bloomberg

## Research Analysts

Global FX Strategy
Yujiro Goto - NSC
yujiro.goto@NOM.com
+81 3 6703 1120

Yusuke Miyairi, CFA - NIplc

yusuke.miyairi@NOM.com

+44 (0) 20 7102 4145

Tomoki Hideshima - NSC

tomoki.hideshima@NOM.com

+81 3 6703 1427

Yuki Kodera - NSC

yuki.kodera@NOM.com

+81 3 6703 1281

## Japanese investors net sold both equities and bonds

Japanese investors net sold JPY69bn of foreign securities in June (Fig. 2). By asset class, they net sold JPY51bn of foreign equities and JPY18bn of foreign bonds. By investor type, notable flows included net selling of foreign bonds by banks, net buying of foreign bonds by trust accounts and net buying of foreign equities by investment trusts (Fig. 3).

Fig. 2: Japan's net purchases of foreign securities by investor type  
![](images/ee270f55b26d7e12d2b47488877d644a9c9adad36742b0bb494219272c9cff2d.jpg)  
Source: NOM, MOF

Fig. 3: Foreign portfolio investment by investor type  
![](images/a56ab543b10bed57cc7a6193bcbf1a0a45d33ae66e38b22d38c987d8c185b1a9.jpg)  
Note: Flow data for June 2026.
Source: NOM, MOF

## Banks have net sold foreign bonds for six consecutive months

Banks net sold JPY1.6trn of foreign securities. The breakdown was net buying of JPY390bn in foreign equities and net selling of JPY2.0trn in foreign bonds. This marked six consecutive months of net selling of foreign bonds by banks.

In the second half of June, US swap spreads continued to tighten, even as expectations for Fed rate hikes rose sharply. As the relative attractiveness of investing in US Treasuries via asset swaps declined, banks may have sold US Treasuries. That said, banks' gross trading volumes in foreign bonds remained relatively low. Lower bond-market volatility may have weighed on banks' overall foreign-bond trading activity.

## Trust accounts sold foreign equities and bought foreign bonds as part of rebalancing

Trust accounts net bought JPY262bn of foreign securities in June (Fig. 4). By asset class, they net sold JPY1.3trn of foreign equities, while net buying JPY1.5trn of foreign bonds. We think this reflected rebalancing, with trust accounts selling foreign equities and buying foreign bonds after the rise in equity markets lifted the portfolio weighting of foreign equities.

Our estimates of GPIF's portfolio allocation show domestic bonds, domestic equities, foreign bonds and foreign equities all broadly tracking around $25\%$ (Fig. 5). As such, at this stage, we do not see clear signs of a review of the basic portfolio that would materially raise the allocation to domestic bonds.

The asset allocation as of end-FY2025, released on 3 July, showed a slight rise in the domestic bond allocation. However, based on the contents of the FY2025 annual report, it is difficult to argue that GPIF has a strong intention to keep increasing its domestic bond weightings from 25%.

Fig. 4: Trust accounts' foreign portfolio flows  
![](images/9d841119643a7d8561b3960e37bacb4c793e2f3250332b4ba93adba1a5f11900.jpg)  
Source: NOM, MOF

Fig. 5: GPIF's portfolio (NOM's estimate) and current policy portfolio

<table><tr><td colspan="2"></td><td>Domestic</td><td>Foreign</td><td>Domestic</td><td>Foreign</td></tr><tr><td rowspan="4"></td><td>end Jun 2025</td><td>26.1</td><td>24.4</td><td>24.3</td><td>25.2</td></tr><tr><td>end Sep 2025</td><td>26.3</td><td>24.2</td><td>24.4</td><td>25.1</td></tr><tr><td>end Dec 2025</td><td>25.3</td><td>24.7</td><td>24.7</td><td>25.3</td></tr><tr><td>end Mar 2026</td><td>26.9</td><td>24.5</td><td>23.8</td><td>24.8</td></tr><tr><td colspan="6">(a) Assuming 50% of trust account&#x27;s net purchase was by GPIF</td></tr><tr><td>Estimate</td><td>latest (a)</td><td>25.0</td><td>24.1</td><td>25.0</td><td>25.9</td></tr><tr><td colspan="6">(b) Assuming 75% of trust account&#x27;s net purchase was by GPIF</td></tr><tr><td>Estimate</td><td>latest (b)</td><td>25.2</td><td>24.5</td><td>24.9</td><td>25.3</td></tr><tr><td colspan="6">(c) Assuming 100% of trust account&#x27;s net purchase was by GPIF</td></tr><tr><td>Estimate</td><td>latest (c)</td><td>25.5</td><td>24.9</td><td>24.8</td><td>24.8</td></tr><tr><td colspan="6">Policy portfolio</td></tr><tr><td rowspan="3">Current</td><td>Target</td><td>25</td><td>25</td><td>25</td><td>25</td></tr><tr><td>Deviation limits</td><td>+/-6%</td><td>+/-5%</td><td>+/-6%</td><td>+/-6%</td></tr><tr><td></td><td>+/-9%</td><td></td><td>+/-9%</td><td></td></tr></table>

Note: Calculations based on the GPIF's portfolio weight as of end-March 2026, flows in April-June 2026, and valuation changes in the benchmark indices from end-March to latest.  
Source: NOM, GPIF, MOF, JSDA, JPX, Bloomberg

## Life insurers bought foreign equities and sold foreign bonds

Life insurers net bought JPY70bn of foreign securities. The breakdown was net buying of JPY111bn in foreign equities and net selling of JPY41bn in foreign bonds (Fig. 6). Looking at both purchase and sale flows in foreign bonds, activity remained small by historical standards.

Life insurers had signalled a cautious stance on unhedged foreign bonds and foreign equities in their FY2026 investment plans, but at this point we do not see evidence of large-scale net selling of foreign bonds. With USD/JPY and the yen crosses remaining elevated, if lifers continue to expect ongoing JPY depreciation, considering limited JPY appreciation factors in the near term, they might prefer unhedged foreign bonds over hedged foreign bonds.

## June NISA flows may have contributed to faster yen depreciation

Foreign securities investment via investment trusts recorded net buying of JPY647bn in June, which was composed of JPY767bn of net buying in foreign equities and JPY120bn of net selling in foreign bonds.

Although the MOF data showed somewhat smaller foreign-equity buying than what is suggested by NRI's data on publicly offered foreign equity funds, the former may include selling by private funds and quarter-end cash-management flows (Fig. 7). Other proxies, such as inflows into the top 10 investment trusts, also point to firm inflows. Taken together, we think NISA-related flows were sizeable in June and may have contributed to the acceleration in yen depreciation.

That said, the pace of foreign-equity buying via investment trusts is likely to slow from July, as global equity gains have moderated and June flows were probably boosted by summer bonuses. Together with heightened caution over FX intervention by the authorities, a slowdown in investment-trust flows is likely to help limit a further upside overshoot in USD/JPY.

Fig. 6: Japanese life insurance companies' foreign asset flow  
![](images/e659ae061850b34ba65cc31f928289c03ab3c37de8cada81e9a9ce6af1b2b6c0.jpg)  
Source: NOM, MOF

Fig. 7: So called NISA flows following the launch of the new NISA scheme  
![](images/9fe5162b479256b50b287d7ee3738a0c79c4a44a4ec83115bf99713493019077.jpg)  
Source: NOM, NRI, Bloomberg

Foreign investors net sold both Japanese equities and Japanese bonds
Foreign investors net sold JPY5.5trn of Japanese securities. The breakdown was net selling of JPY3.0trn in Japanese equities and JPY2.5trn in Japanese bonds (Fig. 8). This was the first month of net selling of Japanese equities by foreign investors in three months.

Weekly international securities investment data show that net selling of Japanese equities was concentrated in the fourth week of June, 21-27 June. At the same time, outflows from Korea and Taiwan were also notable, which suggests the move was largely driven by a withdrawal of capital from East Asia following a correction in technology stocks.

In bonds, foreign investors turned net sellers for the first time since December 2022. This likely reflected concerns that the BOJ was behind the curve, as well as fiscal-related headlines, including the Cabinet Office's macroeconomic projections (released on 24 June), which suggested it was possible to reduce the debt-to-GDP ratio while delivering additional government investment of around JPY10trn per year.

In early July, Kyodo reported that language on appropriate monetary policy management would be added to the government's Basic Policy, fuelling concerns about stronger government pressure on the BOJ. The JGB curve steepened in sectors such as 2s10s and 5s10s. However, more recently, the Takaichi administration may be starting to show greater consideration for markets, with Asahi reporting on 7 July that the wording on monetary policy in the government's Basic Policy could be revised. If the Takaichi administration makes its market-sensitive stance clearer, foreign investors could become more positive on JGBs.

Fig. 8: Foreign investors' net purchases of Japanese assets  
![](images/0ccdaaff6497f2736a46016e4bbe8f70f65b386b99afc750026dfbaad0362800.jpg)  
Source: NOM, MOF

Japanese investors bought around JPY3.0trn of foreign bonds in May, centred on US bonds

In May, Japanese investors net bought approximately JPY3.0trn of foreign bonds (Fig. 9). Net buying was concentrated in US bonds, at JPY1.2trn. Elsewhere, net buying of German bonds, at JPY380bn, also stood out.

By contrast, Japanese investors net sold UK and Belgian bonds. They have also net sold Australian bonds for two consecutive months, albeit in small size. With expectations for RBA rate hikes rising, Japanese investors appear to have sold Australian bonds.

Fig. 9: Foreign LT bond investment, country breakdown

<table><tr><td colspan="2"></td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="2">Total</td><td>1,848</td><td>4,226</td><td>350</td><td>2,107</td><td>-933</td><td>1,066</td><td>-271</td><td>637</td><td>-4,747</td><td>-3,750</td><td>622</td><td>2,980</td></tr><tr><td colspan="2">Asia</td><td>-107</td><td>-166</td><td>17</td><td>-25</td><td>44</td><td>-20</td><td>-158</td><td>-150</td><td>-29</td><td>-38</td><td>442</td><td>377</td></tr><tr><td colspan="2">North America</td><td>-144</td><td>3,221</td><td>313</td><td>1,379</td><td>-78</td><td>598</td><td>832</td><td>500</td><td>-3,667</td><td>-1,956</td><td>377</td><td>1,340</td></tr><tr><td></td><td>US</td><td>-166</td><td>2,984</td><td>294</td><td>1,357</td><td>-132</td><td>473</td><td>794</td><td>403</td><td>-3,602</td><td>-2,008</td><td>297</td><td>1,208</td></tr><tr><td></td><td>Canada</td><td>22</td><td>237</td><td>19</td><td>22</td><td>54</td><td>125</td><td>39</td><td>97</td><td>-65</td><td>52</td><td>80</td><td>132</td></tr><tr><td colspan="2">Central &amp; South America</td><td>27</td><td>227</td><td>198</td><td>123</td><td>-253</td><td>523</td><td>62</td><td>35</td><td>64</td><td>23</td><td>-26</td><td>535</td></tr><tr><td></td><td>Mexico</td><td>33</td><td>23</td><td>37</td><td>1</td><td>17</td><td>11</td><td>26</td><td>42</td><td>27</td><td>-69</td><td>0</td><td>62</td></tr><tr><td></td><td>Brazil</td><td>-1</td><td>-1</td><td>0</td><td>3</td><td>1</td><td>1</td><td>-0</td><td>-2</td><td>-1</td><td>2</td><td>12</td><td>5</td></tr><tr><td></td><td>Cayman Island</td><td>-63</td><td>311</td><td>154</td><td>121</td><td>-175</td><td>518</td><td>32</td><td>-5</td><td>33</td><td>115</td><td>-49</td><td>473</td></tr><tr><td colspan="2">Oceania</td><td>296</td><td>-16</td><td>23</td><td>114</td><td>-107</td><td>103</td><td>-87</td><td>-128</td><td>-135</td><td>-35</td><td>-99</td><td>-26</td></tr><tr><td></td><td>Australia</td><td>282</td><td>-17</td><td>16</td><td>120</td><td>-117</td><td>83</td><td>-125</td><td>-134</td><td>-137</td><td>14</td><td>-95</td><td>-34</td></tr><tr><td></td><td>New Zealand</td><td>14</td><td>0</td><td>7</td><td>-7</td><td>10</td><td>20</td><td>37</td><td>6</td><td>3</td><td>-49</td><td>-4</td><td>8</td></tr><tr><td colspan="2">Europe</td><td>1,386</td><td>721</td><td>-237</td><td>433</td><td>-576</td><td>-265</td><td>-820</td><td>293</td><td>-662</td><td>-1,548</td><td>-10</td><td>730</td></tr><tr><td></td><td>Germany</td><td>570</td><td>315</td><td>71</td><td>-165</td><td>-434</td><td>404</td><td>48</td><td>336</td><td>-404</td><td>-542</td><td>-39</td><td>380</td></tr><tr><td></td><td>UK</td><td>256</td><td>43</td><td>-117</td><td>64</td><td>218</td><td>-437</td><td>-14</td><td>-30</td><td>-110</td><td>-248</td><td>-57</td><td>-99</td></tr><tr><td></td><td>France</td><td>27</td><td>367</td><td>-6</td><td>140</td><td>-607</td><td>-115</td><td>-361</td><td>27</td><td>-302</td><td>-421</td><td>-11</td><td>-95</td></tr><tr><td></td><td>Netherlands</td><td>-43</td><td>31</td><td>-180</td><td>9</td><td>66</td><td>-52</td><td>-132</td><td>-188</td><td>-42</td><td>-167</td><td>17</td><td>91</td></tr><tr><td></td><td>Italy</td><td>-55</td><td>-319</td><td>-135</td><td>376</td><td>68</td><td>159</td><td>-69</td><td>-86</td><td>172</td><td>-62</td><td>-41</td><td>254</td></tr><tr><td></td><td>Belgium</td><td>-43</td><td>-16</td><td>-32</td><td>-8</td><td>105</td><td>-100</td><td>-27</td><td>-149</td><td>52</td><td>30</td><td>35</td><td>-158</td></tr><tr><td></td><td>Luxembourg</td><td>-4</td><td>175</td><td>-1</td><td>-12</td><td>-5</td><td>14</td><td>-24</td><td>26</td><td>-56</td><td>-47</td><td>-72</td><td>-41</td></tr><tr><td></td><td>Switzerland</td><td>3</td><td>-9</td><td>9</td><td>-4</td><td>-6</td><td>-10</td><td>-52</td><td>-30</td><td>5</td><td>-6</td><td>-21</td><td>13</td></tr><tr><td></td><td>Sweden</td><td>1</td><td>-12</td><td>25</td><td>1</td><td>19</td><td>-89</td><td>4</td><td>1</td><td>5</td><td>-7</td><td>3</td><td>-12</td></tr><tr><td></td><td>Spain</td><td>132</td><td>-13</td><td>9</td><td>-174</td><td>92</td><td>-113</td><td>-76</td><td>318</td><td>-125</td><td>-25</td><td>47</td><td>69</td></tr><tr><td></td><td>Ireland</td><td>277</td><td>231</td><td>306</td><td>254</td><td>86</td><td>106</td><td

[中间内容因长度限制已省略]

stic investment trusts, an asset management fee (trust fee) of up to 5.5% (tax included/annualized basis) of the net assets in trust, as well as fees based on investment performance. Other indirect costs may also be incurred. For foreign investment trusts, indirect fees may be incurred during the course of holding such as investment company compensation.

Investment trusts invest mainly in securities such as Japanese and foreign equities and bonds, whose prices fluctuate. Investment trust unit prices fluctuate owing to price fluctuations in the underlying assets and to foreign exchange rate fluctuations. As such, investment trusts carry the risk of losses. Fees and risks vary by investment trust. Maximum applicable fees are subject to change; please thoroughly read the written materials provided, such as prospectuses or documents delivered before making a contract.

In interest rate swap transactions and USD/JPY basis swap transactions (“interest rate swap transactions, etc.”), only the agreed transaction payments shall be made on the settlement dates. Some interest rate swap transactions, etc. may require pledging of margin collateral. In some of these cases, transaction payments may exceed the amount of collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the transaction. Interest rate swap transactions, etc. carry the risk of losses owing to fluctuations in market prices in the interest rate, currency and other markets, as well as reference indices. Losses incurred as such may exceed the value of margin collateral, in which case margin calls may be triggered. In the event that both parties agree to enter a replacement (or termination) transaction, the interest rates received (paid) under the new arrangement may differ from those in the original arrangement, even if terms other than the interest rates are identical to those in the original transaction. Risks vary by transaction. Please thoroughly read the written materials provided, such as documents delivered before making a contract and disclosure statements.

In OTC transactions of credit default swaps (CDS), no sales commission will be charged. When entering into CDS transactions, the protection buyer will be required to pledge or entrust an agreed amount of margin collateral. In some of these cases, the transaction payments may exceed the amount of margin collateral. There shall be no advance notification of required collateral value or collateral ratios as they vary depending on the financial position of the protection buyer. CDS transactions carry the risk of losses owing to changes in the credit position of some or all of the referenced entities, and/or fluctuations of the interest rate market. The amount the protection buyer receives in the event that the CDS is triggered by a credit event may undercut the total amount of premiums that he/she has paid in the course of the transaction. Similarly, the amount the protection seller pays in the event of a credit event may exceed the total amount of premiums that he/she has received in the transaction. All other conditions being equal, the amount of premiums that the protection buyer pays and that received by the protection seller shall differ. In principle, CDS transactions will be limited to financial instruments business operators and qualified institutional investors. Transfers of equities to another securities company via the Japan Securities Depository Center are subject to a transfer fee of up to ¥11,000 (tax included) per issue transferred depending on volume. No account fee will be charged for marketable securities or monies deposited.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Securities Co., Ltd., Japan. All rights reserved.
"""
