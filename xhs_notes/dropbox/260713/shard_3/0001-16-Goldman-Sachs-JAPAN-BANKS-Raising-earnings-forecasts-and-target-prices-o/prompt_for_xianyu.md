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
JAPAN BANKS

# Raising earnings forecasts and target prices on the 3 megabanks to reflect capital markets activity and growing loan demand

We raise our earnings forecasts and 12m target prices for the three megabanks (MUFG, SMFG, and Mizuho), to reflect capital markets activity and growing loan demand. We currently expect that the expansion in loan demand (April-June loans were up +6.1% yoy total, of which major banks were +8.4% yoy; BOJ Loans and Deposits statistics released July 8), the impact of the December rate hike last year, and the rise in short-term interest rates into the June rate hike will positively contribute to net interest income. Additionally, we see robust capital markets-related revenue (accelerated corporate governance improvement efforts by Japanese companies, bond issuances, etc.) and the rise in market indicators such as TOPIX all suggest a smooth start to the fiscal year, while downside risks such as the Middle East situation remain. For FY3/27E for SMFG and Mizuho, we assume and reflect that net income will exceed initial guidance by the net interest income impact of the June rate hike (BOJ policy rate assumption 0.75%), and for MUFG, we reflect the upward revision of our US team's MS estimates (US analyst: Richard Ramsden) in equity-method investment income. Furthermore, we raised our net interest income forecasts for FY3/28 and FY3/29, when the full contribution of the previous fiscal year's bond rebalancing and the June rate hike will be realized.

Due to this upward revision, our FY3/29E ROE forecasts for the megabanks rise from 10-12% to 12-13%, and FY3/28E P/B between 1.56-1.69X. We maintain our Buy ratings on MUFG, SMFG, and Mizuho. Our top pick remains Mizuho; its business focus on corporate lending and GCIB business dovetails with the current cyclical phase and market environment, and we believe the hurdle for an upward revision in 1H is relatively low compared to other banks, as the policy rate assumption for both FY3/27 guidance and FY3/29 medium-term financial targets is 0.75%.

Heading into the 1Q megabank earnings (late July to early August), the points of focus are: 1) the extent of upside versus each bank's initial guidance given tailwinds such as BOJ rate hikes, capital market activity, and growing loan demand, and on the other hand, the extent of downside risks. Wider spreads and loan growth would contribute to profit growth from net interest income, and the rise in TOPIX should also be positive for cancellation gains on equity investment trusts, fee income from capital markets business, and others. On the other hand, there is a possibility that unrealized gains on strategic shareholdings have not increased as much as the rise in TOPIX. In addition, downside risks include a prolonged Middle East situation and

Makoto Kuroda  
+81(3)4587-9920 |  
makoto.kuroda@gs.com  
GS Japan Co., Ltd.

Hibiki Takuma  
+81(3)4587-4935 |  
hibiki.takuma@gs.com  
GS Japan Co., Ltd.

bond rebalancing due to rising long-term interest rates. 2) The impact of these factors on the CET1 ratio is also a key point to watch. Regarding MUFG's CET1 ratio recovery back to its target range, there is a possibility that the accumulation of retained earnings from core business profits is progressing given the backdrop of active capital markets, but this needs to be confirmed. 3) That said, we maintain our constructive view on the banking sector as a whole, with upside potential for P/B given the higher potential ROE over the medium to long term. From that perspective, any ongoing efforts by the banks to improve ROE will also be noteworthy.

## MUFG (8306.T, Buy)

We raise our earnings forecasts and 12m target price for MUFG to reflect capital markets activity and the upward revision of US team's MS estimates (US analyst: Richard Ramsden). We raise our FY3/27E-FY3/29E net income forecasts by 12-15% and lift our target price by 15% to ¥3,900 (from ¥3,400). We maintain our Buy rating. With mid-10% handle ROE in sight over the medium to long term, we continue to see P/B upside potential on ROE far in excess of cost of capital.

One issue at FY3/26 results was the CET1 ratio (finalized basis, excluding AOCI: 9.2%) miss versus 9.5–10.5% target range, and we believe the company is in the process of accumulating several hundred billion yen in retained earnings against its ¥132 tn in risk assets. We think investment banking businesses such as ECM and DCM were likely solid given the subsequent active capital markets and rush of bond issuances, and interest income may also be increasing due to loan growth and bond rebalancing in 4Q of the previous fiscal year. Even if we assume that bond trading revenue has not accelerated due to uncertainty over the direction of US interest rates, there is a possibility that the accumulation of retained earnings is progressing. In adjusting our FY3/27E earnings forecasts for MUFG, we have incorporated a larger upward revision to net interest income than for the other megabanks, factoring in spread expansion (rising short-term interest rates, higher bond yields due to the rebalancing of yen bonds in the previous fiscal year, and US interest rates staying higher) and the possibility of cancellation gains on investment trusts. Driven by strength in the core business, we expect the bank can achieve the profit levels necessary to accumulate its CET1 ratio in 1H, carry out potential bond rebalancing in 2H (we assume a smaller amount than the previous fiscal year), and execute our estimated shareholder returns (assuming a 40% payout ratio and share buybacks of ¥200 bn in FY3/27E and ¥300 bn in FY3/28E).

Our 12-month target price of ¥3,900 is based on a target P/B of 1.69X (previously 1.52X) and our end-FY3/28E BPS estimate of ¥2,292 (previously ¥2,240). We derive our target P/B multiple from our FY3/29E normalized ROE estimate of 13.51% (previously 12.16%) and a cost of equity of 8.0% (unchanged). We maintain our Buy rating.

Exhibit 1: MUFG: Our new vs. old estimates (P/L)

<table><tr><td rowspan="2">(bn JPY)</td><td>FY3/26</td><td>FY3/27 CoE</td><td colspan="2">FY3/27E</td><td rowspan="2">change</td><td rowspan="2">% change</td><td colspan="2">FY3/28E</td><td rowspan="2">change</td><td rowspan="2">% change</td><td colspan="2">FY3/29E</td><td rowspan="2">change</td><td rowspan="2">% change</td></tr><tr><td>Actual</td><td></td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>Net revenue</td><td>5,944.5</td><td></td><td>6,401.9</td><td>6,821.2</td><td>419.2</td><td>7%</td><td>6,852.5</td><td>7,392.3</td><td>539.8</td><td>8%</td><td>7,280.4</td><td>7,934.2</td><td>653.9</td><td>9%</td></tr><tr><td>Net interest income</td><td>3,006.3</td><td></td><td>3,231.0</td><td>3,654.6</td><td>423.6</td><td>13%</td><td>3,818.5</td><td>4,224.8</td><td>406.4</td><td>11%</td><td>4,123.5</td><td>4,642.8</td><td>519.3</td><td>13%</td></tr><tr><td>Net fees and commissions</td><td>2,226.8</td><td></td><td>2,401.1</td><td>2,426.4</td><td>25.3</td><td>1%</td><td>2,384.7</td><td>2,511.3</td><td>126.6</td><td>5%</td><td>2,461.6</td><td>2,588.9</td><td>127.3</td><td>5%</td></tr><tr><td>Net trading profit</td><td>329.5</td><td></td><td>371.4</td><td>371.4</td><td>0.0</td><td>0%</td><td>372.1</td><td>372.1</td><td>0.0</td><td>0%</td><td>405.2</td><td>405.2</td><td>0.0</td><td>0%</td></tr><tr><td>Net other business income</td><td>218.8</td><td></td><td>232.2</td><td>202.5</td><td>-29.7</td><td>-13%</td><td>108.0</td><td>114.8</td><td>6.8</td><td>6%</td><td>110.4</td><td>117.6</td><td>7.3</td><td>7%</td></tr><tr><td>o/w bond gains</td><td>-179.3</td><td></td><td>0.0</td><td>0.0</td><td>0.0</td><td>n/a</td><td>0.0</td><td>0.0</td><td>0.0</td><td>n/a</td><td>0.0</td><td>0.0</td><td>0.0</td><td>n/a</td></tr><tr><td>Trust fees</td><td>163.1</td><td></td><td>166.3</td><td>166.3</td><td>0.0</td><td>0%</td><td>169.2</td><td>169.2</td><td>0.0</td><td>0%</td><td>179.7</td><td>179.7</td><td>0.0</td><td>0%</td></tr><tr><td>Operating expenses</td><td>3,567.2</td><td></td><td>3,792.8</td><td>3,834.3</td><td>41.5</td><td>1%</td><td>3,879.8</td><td>3,973.1</td><td>93.3</td><td>2%</td><td>3,998.5</td><td>4,114.9</td><td>116.4</td><td>3%</td></tr><tr><td>NBP before general allowance</td><td>2,377.2</td><td></td><td>2,609.1</td><td>2,986.9</td><td>377.7</td><td>14%</td><td>2,972.7</td><td>3,419.2</td><td>446.5</td><td>15%</td><td>3,281.9</td><td>3,819.3</td><td>537.4</td><td>16%</td></tr><tr><td>Net credit cost</td><td>-355.9</td><td>-350.0</td><td>-347.6</td><td>-355.5</td><td>-7.8</td><td>n/a</td><td>-345.6</td><td>-363.2</td><td>-17.7</td><td>n/a</td><td>-301.0</td><td>-305.5</td><td>-4.5</td><td>n/a</td></tr><tr><td>Net gains on equity securities</td><td>486.0</td><td></td><td>509.3</td><td>492.6</td><td>-16.8</td><td>-3%</td><td>526.2</td><td>550.9</td><td>24.7</td><td>5%</td><td>526.2</td><td>550.8</td><td>24.6</td><td>5%</td></tr><tr><td>Equity method profits</td><td>845.5</td><td></td><td>810.0</td><td>881.4</td><td>71.4</td><td>9%</td><td>842.6</td><td>920.0</td><td>77.4</td><td>9%</td><td>819.7</td><td>866.8</td><td>47.1</td><td>6%</td></tr><tr><td>Other</td><td>57.2</td><td></td><td>-20.0</td><td>10.0</td><td>30.0</td><td>n/a</td><td>-20.0</td><td>10.0</td><td>30.0</td><td>n/a</td><td>-20.0</td><td>10.0</td><td>30.0</td><td>n/a</td></tr><tr><td>Ordinary Profit</td><td>3,410.2</td><td>3,950.0</td><td>3,560.8</td><td>4,015.4</td><td>454.6</td><td>13%</td><td>3,976.0</td><td>4,536.9</td><td>561.0</td><td>14%</td><td>4,306.9</td><td>4,941.5</td><td>634.6</td><td>15%</td></tr><tr><td>Net extraordinary gain/losses</td><td>-88.0</td><td></td><td>-20.0</td><td>-60.0</td><td>-40.0</td><td>n/a</td><td>-20.0</td><td>-50.0</td><td>-30.0</td><td>n/a</td><td>-20.0</td><td>-50.0</td><td>-30.0</td><td>n/a</td></tr><tr><td>Pre-tax profit</td><td>3,322.2</td><td></td><td>3,540.8</td><td>3,955.4</td><td>414.6</td><td>12%</td><td>3,956.0</td><td>4,486.9</td><td>531.0</td><td>13%</td><td>4,286.9</td><td>4,891.5</td><td>604.6</td><td>14%</td></tr><tr><td>Income taxes</td><td>761.6</td><td></td><td>878.2</td><td>978.2</td><td>99.9</td><td>11%</td><td>979.4</td><td>1,111.7</td><td>132.4</td><td>14%</td><td>1,071.7</td><td>1,222.9</td><td>151.2</td><td>14%</td></tr><tr><td>Minority share profits</td><td>133.3</td><td></td><td>152.3</td><td>154.2</td><td>1.9</td><td>1%</td><td>154.0</td><td>158.2</td><td>4.2</td><td>3%</td><td>160.0</td><td>161.6</td><td>1.6</td><td>1%</td></tr><tr><td>Net income</td><td>2,427.2</td><td>2,700.0</td><td>2,510.2</td><td>2,823.1</td><td>312.8</td><td>12%</td><td>2,822.6</td><td>3,217.0</td><td>394.4</td><td>14%</td><td>3,055.1</td><td>3,507.0</td><td>451.9</td><td>15%</td></tr><tr><td>EPS</td><td>¥213.2</td><td></td><td>¥224.2</td><td>¥250.8</td><td>¥26.6</td><td>12%</td><td>¥256.1</td><td>¥287.8</td><td>¥31.7</td><td>12%</td><td>¥281.8</td><td>¥316.6</td><td>¥34.8</td><td>12%</td></tr><tr><td>DPS</td><td>¥86.0</td><td>¥96.0</td><td>¥96.0</td><td>¥98.0</td><td>¥2.0</td><td>2%</td><td>¥96.0</td><td>¥108.0</td><td>¥12.0</td><td>13%</td><td>¥96.0</td><td>¥120.0</td><td>¥24.0</td><td>25%</td></tr><tr><td>BPS</td><td>¥1,973.3</td><td></td><td>¥2,089.6</td><td>¥2,120.0</td><td>¥30.4</td><td>1%</td><td>¥2,239.8</td><td>¥2,291.6</td><td>¥51.8</td><td>2%</td><td>¥2,418.7</td><td>¥2,484.8</td><td>¥66.1</td><td>3%</td></tr><tr><td>ROE (company KPI)</td><td>11.3%</td><td></td><td>11.0%</td><td>12.3%</td><td></td><td>1.2%pt</td><td>11.8%</td><td>13.0%</td><td></td><td>1.2%pt</td><td>12.1%</td><td>13.3%</td><td></td><td>1.2%pt</td></tr></table>

Source: Company data, GS Global Investment Research

## SMFG (8316.T, Buy)

Reflecting capital markets activity and an expansion in loan demand, we raise our earnings estimates and 12m target price for SMFG. We raise our FY3/27E-FY3/29E net profit estimates by 4-12% and our target price by 14% to ¥7,300 from ¥6,400 previously. We maintain our Buy rating. With a 15% ROE/ROTE target in sight over the medium to long term, we believe ROE could further exceed the cost of equity, drive upside potential for P/B multiple.

The FY3/29 medium-term plan targets an 8% 3y CAGR in net business profits, driven primarily by domestic corporate, digital, and multi-franchise operations, but in our conversations with market participants suggest an unfavorable view of SMFG's India investment Yes Bank (not covered), which is potentially hindering the market from fully pricing in the medium-term plan. In our estimates as well, our FY3/29E net business profit forecast of ¥2.8 tn does not fully price in the midterm plan target of ¥2.94 tn. Furthermore, a July 10 Bloomberg report suggested the possibility of SMFG raising its stake in Yes Bank, which could be taken negatively by the market but conversely could become a catalyst for a re-rating of SMFG should investor sentiment or strategy on the business align. We expect strong progress in 1Q, as operations appear to be going well due to the booming capital markets, a rise in TOPIX, and the weak yen, in addition to the possibility that interest income is increasing due to loan portfolio growth (a shift from bridge loans to corporate loans) and policy rate hikes. For shareholder returns, we

forecast a dividend payout ratio of 40% and share buybacks of ¥360 bn in FY3/27E.

Our 12-month target price of ¥7,300 is based on a target P/B of 1.56X (previously 1.36X) and our end-FY3/28E BPS estimate of ¥4,661 (previously ¥4,689). We derive our target P/B multiple from our FY3/29E normalized ROE estimate of 12.48% (previously 10.90%) and a cost of equity of 8.0% (unchanged). For cost of equity, we use a risk-free rate of 0.0%, equity risk premium of 10.0%, and long-term growth of 0.0% (unchanged). We maintain our Buy rating.

Exhibit 2: SMFG: Our new vs. old estimates (P/L)

<table><tr><td rowspan="2">(bn JPY)</td><td>FY3/26</td><td>FY3/27</td><td colspan="2">FY3/27E</td><td rowspan="2">change</td><td rowspan="2">% change</td><td colspan="2">FY3/28E</td><td rowspan="2">change</td><td rowspan="2">% change</td><td colspan="2">FY3/29E</td><td rowspan="2">change</td><td rowspan="2">% change</td></tr><tr><td>Actual</td><td>CoE</td><td>Old</td><td>New</td><td>Old</td><td>New</td><td>Old</td><td>New</td></tr><tr><td>Net revenue</td><td>4,844.7</td><td></td><td>4,889.0</td><td>4,998.5</td><td>109.6</td><td>2%</td><td>5,076.1</td><td>5,078.7</td><td>2.6</td><td>0%</td><td>5,195.7</td><td>5,392.9</td><td>197.2</td><td>4%</td></tr><tr><td>Net interest income</td><td>2,719.6</td><td></td><td>2,726.7</td><td>2,827.7</td><td>101.0</td><td>4%</td><td>3,046.4</td><td>3,018.1</td><td>-28.3</td><td>-1%</td><td>3,138.4</td><td>3,267.4</td><td>129.0</td><td>4%</td></tr><tr><td>Net fees and commissions</td><td>1,820.6</td><td></td><td>1,888.2</td><td>1,896.1</td><td>8.0</td><td>0%</td><td>1,754.5</td><td>1,781.6</td><td>27.1</td><td>2%</td><td>1,763.5</td><td>1,800.4</td><td>37.0</td><td>2%</td></tr><tr><td>Net trading profit</td><td>199.4</td><td></td><td>191.0</td><td>191.0</td><td>0.0</td><td>0%</td><td>191.0</td><td>191.0</td><td>0.0</td><td>0%</td><td>191.0</td><td>200.0</td><td>9.0</td><td>5%</td></tr><tr><td>Net other business income</td><td>93.3</td><td></td><td>73.0</td><td>73.7</td><td>0.7</td><td>1%</td><td>74.2</td><td>77.9</td><td>3.7</td><td>5%</td><td>93.0</td><td>114.5</td><td>21.4</td><td>23%</td></tr><tr><td>Trust fees</td><td>11.7</td><td></td><td>10.0</td><td>10.0</td><td>0.0</td><td>0%</td><td>10.0</td><td>10.0</td><td>0.0</td><td>0%</td><td>9.7</td><td>10.5</td><td>0.8</td><td>8%</td></tr><tr><td>Operating expenses</td><td>2,651.5</td><td></td><td>2,639.1</td><td>2,639.7</td><td>0.6</td><td>0%</td><td>2,702.4</td><td>2,674.7</td><td>-27.7</td><td>-1%</td><td>2,692.4</td><td>2,624.2</td><td>-68.2</td><td>-3%</td></tr><tr><td>Core NBP (mgmt accounting, w/eq. meth

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
