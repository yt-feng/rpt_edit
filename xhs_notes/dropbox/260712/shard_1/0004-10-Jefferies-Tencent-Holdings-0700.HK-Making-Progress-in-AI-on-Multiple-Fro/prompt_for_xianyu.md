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
# Making Progress in AI on Multiple Fronts; Investment is Not New to Market

Tencent has a number of new AI developments, such as the release of Hy3, testing of Weixin AI, and WorkBuddy gaining traction. In 2Q, we expect advertising continued to gain market share, while domestic games delivered faster growth vs overseas. Non-IFRS earnings growth is expected to be slower vs revenue growth on AI spending. As highlighted in our report (link), investment in AI and step-up in capex are expected in 2026. Maintain Buy.

Factoring in the latest trends, with solid progress in AI. For 2Q, we estimate total revenue growth of about 9.6% YoY (unchanged) to about RMB200bn. By segment, we estimate online game revenue growth of about 8.6% YoY (vs consensus of 11% YoY and our prior estimate of 8.6% YoY), with faster growth for domestic games than overseas games. For domestic games, we expect solid performance by evergreen game titles. Our checks on iOS grossing show in 2Q, Roco Kingdom World performed better than Honor of Kings World (link). For international games, we expect revenue deferral impact from the lapse of Supercell grossing and normalization of acquired studios. We expect AI to drive user engagement and monetization. For marketing services, we expect revenue growth of 18% YoY (vs consensus of 18% YoY) to RMB42.4bn, thanks to ad tech upgrades, and the strength of Video Accounts. For fintech and business services (FBS), we estimate revenue growth of 9% YoY (vs consensus of 9%), factoring in the latest consumer sentiment trends, and the expected acceleration in cloud revenue YoY. We expect non-IFRS operating profit growth of 6% YoY (vs consensus of 9.3% YoY) to about RMB73bn, on AI investments. We estimate non-IFRS earnings to increase by 4% (vs consensus of 9.7% you, and largely unchanged from our prior estimate) to RMB65.5bn.

Testing of Weixin AI kicked off in Jun. Tencent is conducting small-scale testing on Weixin AI across various scenarios in social & communication, information & search, productivity, entertainment/shopping, as well as tool generation. Weixin AI, called Xiao Wei, is: 1) located at top lefthand side of the main page; and 2) one of the features available inside messaging. The core model is WeLM, which was developed by the Weixin team. We view this as an important step for Tencent in Agent2Agent (A2A), and expect tofficial release in 4Q26. Please refer to report (link) for details.

WorkBuddy takes the lead in Workspace Agents market. The company highlighted third-party Analysys data on WorkBuddy's operating metrics in the segment (Mar-26). These include: 1) the number of desktop monthly visits reaching 8.85m; 2) WorkBuddy is ahead of Trae (ByteDance), QClaw (Tencent) and Qoder Work (BABA).

Continued inside...

<table><tr><td>FY (Dec)</td><td>2024A</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>Rev. (MM)</td><td>660,257.0</td><td>751,766.0</td><td>822,715.0</td><td>894,173.0</td></tr><tr><td>Adj Net Profit</td><td>222,703.0</td><td>259,626.0</td><td>269,936.0</td><td>277,310.0</td></tr></table>

<table><tr><td colspan="2">TARGET CHANGE</td></tr><tr><td>RATING</td><td>BUY</td></tr><tr><td>PRICE</td><td>HK$469.60^</td></tr><tr><td>PRICE TARGET | % TO PT</td><td>↓HK$750.00 (HK$795.00) | +60%</td></tr><tr><td>52W HIGH-LOW</td><td>HK$683.00 - HK$411.00</td></tr><tr><td>FLOAT (%) | ADV MM (USD)</td><td>68.3% | 2,179.76</td></tr><tr><td>MARKET CAP</td><td>HK$4.3T | $544.4B</td></tr><tr><td>TICKER</td><td>700 HK</td></tr></table>

^Prior trading day's closing price unless otherwise noted.

<table><tr><td>FY (Dec)</td><td colspan="2">CHANGE TO JEFe</td><td colspan="2">JEF vs CONS</td></tr><tr><td></td><td>2026</td><td>2027</td><td>2026</td><td>2027</td></tr><tr><td>REV</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>EPS</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr></table>

Thomas Chong \* | Equity Analyst
852 3743 8016 | thomas.chong@JEF.com

Zoey Zong \* | Equity Analyst
852 3743 8163 | zoey.zong@JEF.com

## The Long View: Tencent Holdings

## Investment Thesis

\- Tencent's evolution from consumer to industry internet, while retaining its solid foundation in gaming and growing ad market share, paves the way for future success, in our view.

\- Expected solid revenue growth is backed by multiple drivers that lower concentration risk amid macro headwinds.

\- The social ecosystem of Tencent, with an emphasis on ROI and significant synergistic effects, gives it a key competitive edge over its peers amid macro headwinds and intensified competition.

Risk/Reward - 12 Month View  
![](images/0a14efa32c6f2d6dad941a8ee8d77d41b3810dadd153cb83164a7544261bb482.jpg)

## Base Case, HK\$750, +60%

• We consider Tencent a global mobile game leader, with a proven track record in developing successful games.

\- The success of HoK, with record-high DAU and positive feedback on new games, backed by portfolio strategy, should drive LT growth.

• We view content as king in video advertising.

• PT of HK\$750 based on a SOTP valuation.

Upside Scenario, HK\$900, +92%

\- Successful launch of strong-grossing new games.

\- Faster-than-expected growth in online ads on macro recovery.

\- Narrower-than-expected loss from cloud business segment.

\- Upside PT of HK\$900 based on a SOTP valuation.

Downside Scenario, HK\$450, -4%

• Unsuccessful launch of new games.

\- Slower-than-expected growth in online ads on macro headwinds.

\- Aggressive subsidy campaign on payments and capex spending on Cloud.

\- Downside PT of HK\$450 based on a SOTP valuation.

## Sustainability Matters

Top Material Issue(s): 1) Data security and customer privacy. Privacy protection and data security measures are important for a technology company. The company needs to develop and use technology ethically and maintain the trust of partners, customers, counterparties. 2) Employee engagement, diversity, & inclusion. Talent is key in creating value for the company, and workforce diversity is important for innovation. The company should prioritize employee engagement and work-life balance, which can help in recruitment and retention of a diverse workforce.

## Catalysts

Company target(s): 1) Pledged to reach carbon-neutrality across operations and supply chains by 2030 and to switch electricity supply to 100% green power or renewable energy where feasible. 2) Electricity consumption per capita in all Tencent-owned office buildings in mainland China to be reduced by 15% by the end of 2025, benchmarking 2019.

\- Launch of high-grossing new games.

• Stronger-than-expected outlook.

\- Faster-than-expected ad market share gains.

Qs to Mgmt: 1) What are you investing in to protect your firm and your customer data? 2) What is the margin effect of the environmental protection measures?

Hy3 official version has a number of enhancements in response to user feedback. Highlights of Hy3 vs preview version include the following. 1) Feedback received across more than 50 business units, and upgraded with better user experience. On input/output price, Hy3 has a lower price of RMB1/RMB4 per million tokens vs RMB2/RMB8 for the preview version. This aims to support more users and scenarios. 2) Further enhancements in post training such as Reinforcement Learning (RL). Better performance in long contexts vs large models, which have 2-5x more parameters. 3) Value creation in productivity scenario, such as software development, office, financial, design and game development. 4) Blind test with 270 experts in real work scenarios shows that Hy3 scores better than GLM-5.1 (e.g. frontend, data, storage, CI/CD). 5) Further improvements in: a) task success rate vs preview version (90% vs prior 72%); b) token efficiency; compared to GLM-5.2, savings in token consumption achieved in word processing (47.4%) and PPT (49%); c) reduced hallucination by 15 pp. Please refer to our report (link) for details.

Key takeaways from Tencent Cloud AI Industry Applications Summit. Highlights: 1) foundation models, products and frontier tech exploration are keys; 2) Tencent stands out with comprehensive product offerings across different scenarios, which provide a more complete set of data insights to models and agents/coding products; 3) co-design between product and model teams is important and trust is key; 4) model performance is achieving efficiencies in token consumption; 5) AI is a long-term story, and is in the early stage of development. Please refer to our report (link) for details.

Focus areas of earnings call. 1) AI strategy updates and feedback on the latest trends for WorkBuddy. In addition, the market is paying attention to user feedback on Weixin AI testing. 2) AI model competitive landscape and feedback on the official release of Hy3. 3) Domestic online gaming strategies, such as updates on rejuvenating existing games (e.g., HoK, PKE), and emerging franchises. 4) International games outlook. 5) Advertising outlook and trends across different industry categories. 6) Fintech (e.g., payment and non-payment) revenue trends. 7) Capex trends and cloud revenue outlook. 8) Trend in operating expenses. 9) Updates on AI monetization opportunities across different business segments. 10) Earnings growth in 2H. 11) Capital return to shareholders.

Valuation and risks. We maintain our Buy rating and adjust our PT to HKD750 (vs prior HKD795), factoring in AI investments and lower P/E multiples to take into consideration sector valuation amid dynamic market sentiment on industry developments. Risks include: 1) unsuccessful launch of new games; 2) slower-than-expected growth in online ads amid macro headwinds; and 3) aggressive investment in new initiatives.

Exhibit 1 - 700 HK: Income Statement

<table><tr><td colspan="7">Income Statement (700 HK)</td></tr><tr><td>RMB mn</td><td>2022A</td><td>2023A</td><td>2024A</td><td>2025A</td><td>2026F</td><td>2027F</td></tr><tr><td>Total Revenue</td><td>554,552</td><td>609,015</td><td>660,257</td><td>751,766</td><td>822,715</td><td>894,173</td></tr><tr><td>Cost of revenue</td><td>-315,806</td><td>-315,906</td><td>-311,011</td><td>-329,173</td><td>-364,765</td><td>-409,654</td></tr><tr><td>Gross profit</td><td>238,746</td><td>293,109</td><td>349,246</td><td>422,593</td><td>457,949</td><td>484,519</td></tr><tr><td>Sales and marketing expense</td><td>-29,229</td><td>-34,211</td><td>-36,388</td><td>-41,727</td><td>-49,061</td><td>-53,967</td></tr><tr><td>Research and development expense</td><td>-61,401</td><td>-64,078</td><td>-70,686</td><td>-85,747</td><td>-108,005</td><td>-118,806</td></tr><tr><td>General and administrative expense</td><td>-45,295</td><td>-39,447</td><td>-42,075</td><td>-50,380</td><td>-45,032</td><td>-47,284</td></tr><tr><td>Non-IFRS operating profit</td><td>153,538</td><td>191,886</td><td>237,811</td><td>280,656</td><td>293,736</td><td>303,554</td></tr><tr><td>Non-IFRS operating margin</td><td>27.7%</td><td>31.5%</td><td>36.0%</td><td>37.3%</td><td>35.7%</td><td>33.9%</td></tr><tr><td>Non-IFRS net income</td><td>115,549</td><td>157,688</td><td>222,703</td><td>259,626</td><td>269,936</td><td>277,310</td></tr><tr><td>Non-IFRS net margin</td><td>20.8%</td><td>25.9%</td><td>33.7%</td><td>34.5%</td><td>32.8%</td><td>31.0%</td></tr></table>

Source: Company, JEF estimates

Exhibit 2 - 700 HK: Balance Sheet

<table><tr><td colspan="7">Balance Sheet (700 HK)</td></tr><tr><td>RMBmn</td><td>2022A</td><td>2023A</td><td>2024A</td><td>2025A</td><td>2026F</td><td>2027F</td></tr><tr><td>Cash and cash equivalents</td><td>156,739</td><td>172,320</td><td>132,519</td><td>141,041</td><td>201,399</td><td>254,150</td></tr><tr><td>Financial assets held for trading</td><td>27,963</td><td>14,903</td><td>12,913</td><td>44,710</td><td>44,710</td><td>44,710</td></tr><tr><td>Term deposits</td><td>104,776</td><td>185,983</td><td>192,977</td><td>236,801</td><td>238,801</td><td>240,801</td></tr><tr><td>Restricted cash</td><td>2,783</td><td>3,818</td><td>3,334</td><td>6,977</td><td>6,977</td><td>6,977</td></tr><tr><td>Receivables</td><td>45,467</td><td>46,606</td><td>48,203</td><td>49,930</td><td>54,642</td><td>59,388</td></tr><tr><td>Inventories</td><td>2,333</td><td>456</td><td>440</td><td>530</td><td>530</td><td>530</td></tr><tr><td>Prepayments. deposits and other receivables</td><td>77,963</td><td>94,360</td><td>105,794</td><td>115,471</td><td>126,369</td><td>137,345</td></tr><tr><td>Assets held for distribution</td><td>147,965</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Total current assets</td><td>565,989</td><td>518,446</td><td>496,180</td><td>595,460</td><td>673,428</td><td>743,901</td></tr><tr><td>Available-for-sale financial assets</td><td>391,332</td><td>425,096</td><td>507,359</td><td>563,797</td><td>563,997</td><td>564,197</td></tr><tr><td>PPE</td><td>63,766</td><td>67,385</td><td>93,288</td><td>160,525</td><td>330,080</td><td>537,435</td></tr><tr><td>Land use rights</td><td>18,046</td><td>17,179</td><td>23,117</td><td>22,339</td><td>22,339</td><td>22,339</td></tr><tr><td>Intangibles</td><td>161,802</td><td>177,727</td><td>196,127</td><td>205,999</td><td>209,710</td><td>213,421</td></tr><tr><td>Investment in associates</td><td>252,715</td><td>261,665</td><td>297,415</td><td>348,712</td><td>348,712</td><td>348,712</td></tr><tr><td>Deferred income tax assets</td><td>29,882</td><td>29,017</td><td>28,325</td><td>28,618</td><td>28,618</td><td>28,618</td></tr><tr><td>Term deposit</td><td>28,336</td><td>29,301</td><td>77,601</td><td>70,302</td><td>70,302</td><td>70,302</td></tr><tr><td>Right-of-use assets</td><td>22,524</td><td>20,464</td><td>17,679</td><td>17,367</td><td>17,367</td><td>17,367</td></tr><tr><td>Prepayments, deposits and other assets</td><td>43,739</td><td>30,966</td><td>43,904</td><td>25,867</td><td>31,040</td><td>37,248</td></tr><tr><td>Total non-current assets</td><td>1,012,142</td><td>1,058,800</td><td>1,284,815</td><td>1,443,526</td><td>1,622,165</td><td>1,839,639</td></tr><tr><td>Total assets</td><td>1,578,131</td><td>1,577,246</td><td>1,780,995</td><td>2,038,986</td><td>2,295,593</td><td>2,583,540</td></tr><tr><td>Deferred revenue</td><td>82,216</td><td>86,168</td><td>100,097</td><td>110,309</td><td>120,720</td><td>131,205</td></tr><tr><td>Accounts Pavables</td><td>92,381</td><td>100,948</td><td>118,712</td><td>121,127</td><td>135,422</td><td>150,435</td></tr><tr><td>Other payables and accruals</td><td>61,139</td><td>76,595</td><td>84,032</td><td>96,496</td><td>79,206</td><td>87,987</td></tr><tr><td>Lease liabilities</td><td>6,354</td><td>6,154</td><td>5,600</td><td>5,386</td><td>5,386</td><td>5,386</td></tr><tr><td>ST debt</td><td>11,580</td><td>41,537</td><td>52,885</td><td>42,618</td><td>42,618</td><td>42,618</td></tr><tr><td>Dividend payable</td><td>147,965</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Other current liabilities</td><td>32,569</td><td>40,755</td><td>35,583</td><td>36,815</td><td>37,615</td><td>38,415</td></tr><tr><td>Total current liabilities</td><td>434,204</td><td>352,157</td><td>396,909</td><td>412,751</td><td>420,966</td><td>456,046</td></tr><tr><td>Long term notes payable</td><td>312,337</td><td>292,920</td><td>277,107</td><td>334,573</td><td>334,573</td><td>334,573</td></tr><tr><td>Deferred income tax liabilities</td><td>12,162</td><td>17,635</td><td>18,546</td><td>21,684</td><td>21,684</td><td>21,684</td></tr><tr><td>Lease liabilities</td><td>18,424</td><td>16,468</td><td>13,897</td><td>13,280</td><td>13,280</td><td>13,280</td></tr><tr><td>Other financial liabilities</td><td>5,574</td><td>8,781</td><td>4,203</td><td>2,879</td><td>2,879</td><td>2,879</td></tr><tr><td>Long term payables</td><td>12,570</td><td>15,604</td><td>16,437</td><td>12,754</td><td>12,754</td><td>12,754</td></tr><tr><td>Total non-current liabilities</td><td>361,067</td><td>351,408</td><td>330,

[中间内容因长度限制已省略]

the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
