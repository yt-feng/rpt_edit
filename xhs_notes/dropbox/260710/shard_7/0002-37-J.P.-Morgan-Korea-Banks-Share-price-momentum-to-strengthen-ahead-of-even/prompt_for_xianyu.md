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
## Korea Banks

## Share price momentum to strengthen ahead of eventful 2Q26 earnings season; extended re-rating in large FGs

Korea banks have outperformed the market since July, up 8% (vs. KOSPI -15%). Going into the 2Q earnings season, we see a constructive set-up for Korean financials. 2Q26 results should be broadly solid on (i) resilient NII with modest NIM uplift and steady loan growth, (ii) stronger non-interest income on capital markets-related fees, and (iii) contained credit costs with provisioning broadly in line with full-year guidance. Beyond earnings, we expect shareholder returns to be the key catalyst: as prior buybacks conclude in July, another round of buyback/cancellation announcements looks likely—potentially larger at KB and Shinhan on stronger earnings prints—while Hana could also draw attention on a Value-Up update (introducing a shareholder return formula and refreshed ROE targets, broadly converging toward KB/Shinhan). With large FGs still trading at <1.0x P/B (vs. 11–12% mid-term ROE trajectory), we see ample upside from here and recommend investors accumulate KB, Shinhan and Hana (all OWs) to capture an extended re-rating rally on sustainable ROE trending higher lifting fair P/B.

## 2Q earnings preview on key earnings metrics

\- Widening NIM: NIM trends should diverge across banks given different repricing cycles and base effects. Still, we expect margins to remain broadly resilient and grind higher as asset yields reprice up in a higher-rate backdrop and price competition remains contained. Compared to smaller banks, we see large FGs better positioned for NIM upside on lower funding costs, with Kakao Bank also likely to stand out with a steep NIM recovery (\~6bps).

\- Solid loan growth: We expect our covered banks to deliver 1–3% q/q loan growth. While household lending remains constrained by regulation, corporate loans should drive overall expansion, supported by the productive-finance initiative and relatively more attractive economics versus debt issuance. That said, we expect banks to stay disciplined on RoRWA-led lending to manage capital, keeping RWA growth broadly within 4–5% y/y.

\- Robust non-interest income expansion: We expect 2Q non-interest income to strengthen sequentially, led by higher capital markets-related fees on solid brokerage and wealth management operations. While higher rates could still pressure bond trading gains, we see the drag easing (vs. depressed prior quarter) given a more moderate move in yields. The scale of the uplift should vary by the size and earnings mix of each group's securities arm, with KB and Shinhan best positioned to capture the fee-income upside..

\- Credit costs under control. We expect credit costs to remain broadly contained. Banks may take some one-off provisions related to the Joongang Group's court-led rehabilitation filing, but the earnings impact should be limited given modest exposure and adequate collateral coverage. While asset quality readings are under upward pressure on rising rates, we see overall credit costs staying broadly stable and in line with full-year guidance.

\- Still, progressive shareholder returns. With the previously announced buybacks set to complete in July, we expect our covered financial groups to announce another round of sizable 2Q buybacks, especially with rising expectations for KB and Shinhan on stronger earnings prints, alongside the continued rollout of quarterly dividends. We also look for Hana to update its

## Diversified Banks

Jihyun Cho AC
(82-2) 758-5480
jihyun.cho@JPM.com
JPM Securities (Far East) Limited, Seoul Branch

JPM Securities (Far East) Limited, Seoul Branch

(852) 2800-8552
katherine.lei@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 11 for analyst certification and important disclosures, including non-US analyst disclosures.

Value-Up plan, potentially introducing a more advanced formula-based shareholder return policy and setting more ambitious operating targets to lift ROE. While ongoing KRW depreciation remains a headwind, solid earnings and disciplined RWA management should keep CET1 broadly stable, enough to support further progressive shareholder returns in terms of payout ratio and absolute amounts.

Table 1: Korea banks: 2Q26 earnings preview (net profit)

<table><tr><td rowspan="2"></td><td rowspan="2">2Q25(W bn)</td><td rowspan="2">3Q25(W bn)</td><td rowspan="2">4Q25(W bn)</td><td rowspan="2">1Q26(W bn)</td><td rowspan="2">2Q26E(W bn)</td><td rowspan="2">Cons.(W bn)</td><td colspan="2">Change</td><td rowspan="2">Forecast details (q/q)</td></tr><tr><td>(q/q)</td><td>(y/y)</td></tr><tr><td>KB</td><td>1,738</td><td>1,686</td><td>721</td><td>1,892</td><td>1,906</td><td>1,814</td><td>1</td><td>10</td><td>NIM +1bp, Credit cost 0.54%, Loan growth +0.6%</td></tr><tr><td>Shinhan</td><td>1,549</td><td>1,424</td><td>511</td><td>1,623</td><td>1,652</td><td>1,630</td><td>2</td><td>7</td><td>NIM +1bp, Credit cost 0.54%, Loan growth +0.3%</td></tr><tr><td>Hana</td><td>1,173</td><td>1,132</td><td>569</td><td>1,210</td><td>1,238</td><td>1,225</td><td>2</td><td>5</td><td>NIM +4bps, Credit cost 0.38%, Loan growth +1.3%</td></tr><tr><td>IBK</td><td>693</td><td>747</td><td>462</td><td>749</td><td>606</td><td>709</td><td>(19)</td><td>(13)</td><td>NIM +1bp, Credit cost 0.64%, Loan growth +1.7%</td></tr><tr><td>BNK</td><td>309</td><td>294</td><td>45</td><td>211</td><td>225</td><td>259</td><td>6</td><td>(27)</td><td>NIM -1bp, Credit cost 0.60%, Loan growth +2.8%</td></tr><tr><td>iM</td><td>155</td><td>122</td><td>12</td><td>155</td><td>145</td><td>154</td><td>(6)</td><td>(7)</td><td>NIM -1bp, Credit cost 0.62%, Loan growth +1.7%</td></tr><tr><td>Kakao Bank</td><td>126</td><td>111</td><td>105</td><td>187</td><td>128</td><td>138</td><td>(32)</td><td>2</td><td>NIM +6bps, Credit cost 0.57%, Loan growth +1.4%</td></tr><tr><td>Total</td><td>5,745</td><td>5,517</td><td>2,426</td><td>6,027</td><td>5,899</td><td>5,933</td><td>(2)</td><td>3</td><td></td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates.

Table 2: Korea banks: Summary of results release schedule

<table><tr><td>Company</td><td>Date</td><td>Seoul time (GMT+9)</td><td>Conference call</td><td>Things to look for on management calls</td></tr><tr><td>KB FG</td><td>23-Jul</td><td>1600</td><td>Yes</td><td>2Q DPS, share buyback program, CET1 ratio, NIM, loan growth and credit cost outlook</td></tr><tr><td>Shinhan FG</td><td>23-Jul</td><td>1400</td><td>Yes</td><td>2Q DPS, share buyback program, CET1 ratio, NIM, loan growth and credit cost outlookk</td></tr><tr><td>Hana FG</td><td>24-Jul</td><td>1500</td><td>Yes</td><td>Updated Value-Up measures, 2Q DPS, share buyback program, CET1 ratio, NIM, loan growth and credit cost outlook</td></tr><tr><td>IBK</td><td>27-Jul</td><td>TBD</td><td>Yes</td><td> $1^{st}$  interim dividend payout, credit cost outlook for SMEs, loan growth target in increasing competition</td></tr><tr><td>BNK FG</td><td>28-Jul</td><td>1530</td><td>Yes</td><td>2Q DPS, CET1 ratio, NIM, loan growth and credit cost outlook</td></tr><tr><td>iM FG</td><td>27-Jul</td><td>1600</td><td>Yes</td><td>CET1 ratio, share buyback program, NIM, loan growth and credit cost outlook</td></tr><tr><td>Kakao Bank</td><td>5-Aug</td><td>1000</td><td>Yes</td><td>NIM, loan growth, credit cost outlook, fee/platform/overseas business strategy, SOHO loan penetration</td></tr></table>

Source: Company data, JPM. Note: Tentative schedule.

Figure 1: 2026 YTD bank sector performance  
![](images/f0c86558e76440b067171f83230ecf47cd7972635d3c116afe89cc1f17889fd4.jpg)  
Source: Bloomberg Finance L.P.

Figure 2: Asia banks: 2026E P/B (x) vs. ROE (%)  
![](images/34471153551f77128af69c4792ce42de31a235d71b5ff1f375fa27a7f4d36f98.jpg)  
Source: Bloomberg Finance L.P., JPM estimates. Note: Consensus numbers used for global peers.

Figure 3: Korea Banks:12M-fwd P/B band Wtn  
![](images/6e73957effefaa9302ccd7e1d6ce23ec26f2814bf405c4800855ac717b26648b.jpg)  
Figure 4: Korea Banks: 12M-fwd P/B (x) vs. ROE (%)

![](images/d4529b85eb9e837b442555eca7a0779c77f1197eccd32656c2d68058988a85a7.jpg)  
Source: Company data, Bloomberg Finance L.P., JPM estimates. Note: Kakao Bank is Source: Company data, Bloomberg Finance L.P., JPM estimates. excluded.

Figure 5: Total payout ratio (cash dividend + share buyback/cancellation)  
![](images/1206f6bef91302de6e66fff561c21dda878916f7dcafe0dc6fba5a525b6446e9.jpg)  
Source: Company data, JPM estimates. Note: Total payout includes cash dividends and share buybacks and/or cancelations.

Table 3: Valuation comparison

<table><tr><td rowspan="2"></td><td rowspan="2">Rating</td><td rowspan="2">Price (W)</td><td rowspan="2">PT (W)</td><td rowspan="2">PT +/- (%)</td><td colspan="2">P/E (x)</td><td colspan="2">EPS growth (%)</td><td colspan="2">P/BV (x)</td><td colspan="2">ROE (%)</td><td colspan="2">Total Yield (%)</td><td colspan="3">Stock perf.</td></tr><tr><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>26E</td><td>27E</td><td>YTD (%)</td><td>2025 (%)</td><td>2024 (%)</td></tr><tr><td>KB FG</td><td>OW</td><td>171,000</td><td>220,000</td><td>28.7</td><td>9.1</td><td>8.2</td><td>17.2</td><td>12.7</td><td>0.99</td><td>0.92</td><td>11.0</td><td>11.6</td><td>6.0</td><td>7.2</td><td>37%</td><td>51%</td><td>53%</td></tr><tr><td>Shinhan FG</td><td>OW</td><td>107,300</td><td>145,000</td><td>35.1</td><td>8.7</td><td>7.9</td><td>21.0</td><td>15.5</td><td>0.82</td><td>0.75</td><td>9.6</td><td>10.1</td><td>6.1</td><td>7.1</td><td>39%</td><td>62%</td><td>19%</td></tr><tr><td>Hana FG</td><td>OW</td><td>122,300</td><td>180,000</td><td>47.2</td><td>7.4</td><td>6.7</td><td>16.1</td><td>13.1</td><td>0.70</td><td>0.65</td><td>9.8</td><td>10.3</td><td>6.7</td><td>7.8</td><td>30%</td><td>66%</td><td>31%</td></tr><tr><td>IBK</td><td>N</td><td>20,950</td><td>24,000</td><td>14.6</td><td>7.0</td><td>6.2</td><td>-12.1</td><td>11.9</td><td>0.45</td><td>0.43</td><td>6.6</td><td>7.0</td><td>4.5</td><td>5.1</td><td>0%</td><td>46%</td><td>21%</td></tr><tr><td>BNK FG</td><td>N</td><td>17,930</td><td>21,000</td><td>17.1</td><td>7.6</td><td>6.7</td><td>-9.5</td><td>15.4</td><td>0.50</td><td>0.48</td><td>6.6</td><td>7.3</td><td>5.9</td><td>7.5</td><td>12%</td><td>55%</td><td>45%</td></tr><tr><td>iM FG</td><td>N</td><td>18,090</td><td>20,000</td><td>10.6</td><td>6.6</td><td>6.2</td><td>0.7</td><td>8.8</td><td>0.46</td><td>0.44</td><td>7.0</td><td>7.3</td><td>5.9</td><td>6.4</td><td>16%</td><td>91%</td><td>-4%</td></tr><tr><td>Kakao Bank</td><td>N</td><td>22,000</td><td>24,000</td><td>9.1</td><td>17.9</td><td>17.0</td><td>19.8</td><td>5.4</td><td>1.50</td><td>1.43</td><td>8.4</td><td>8.5</td><td>2.9</td><td>3.1</td><td>1%</td><td>3%</td><td>-26%</td></tr></table>

Source: Company data, Bloomberg Finance L.P., JPM estimates. Note: Share prices as of 8 Jul. 2026 market close.

Table 4: Value-Up measures and detailed framework announced by our covered FGs

<table><tr><td></td><td colspan="3">2025</td><td>Value-Up Measures</td></tr><tr><td>Company</td><td>Cash Dividend(% of Net profit)</td><td>Share buyback/cancellation(% of Net profit)</td><td>Total shareholder return(% of Net profit)</td><td>Key Targets &amp; Framework</td></tr><tr><td>KB</td><td>27%</td><td>25% (W1,480bn)</td><td>52%</td><td>1) Industry-leading TSR ratio2) Over 10mn shares for buyback/cancellation on annual avg.(to be conducted on a semi-annual basis)3) 10% EPS growth4) 13%+ CET1 ratio5) 11% ROE in 1-2 years and 13%+ over the mid-to-long term[Key Framework]1) Annual shareholder return budget set at the beginning of each year to return excess capital above 13% CET1 ratio on dividends + share buyback/cancellation2) Additional budget allocation if interim CET1 ratio is above 13.5%</td></tr><tr><td>Shinhan</td><td>25%</td><td>25% (W1,250bn)</td><td>50%</td><td>1) 50%+ payout in total shareholder return (dividend + share buyback)2) 10%+ ROE (Mid-term target: 10-12%), 11.5%+ ROTCE3) 13%+ CET1 ratio (Mid-term target: 13.0-13.4%)[Key Framework]1) Remove TSR ceiling2) Prioritize tax-exempt and separately taxed dividends3) Formula based return: TSR = (1-Growth rate) / Target ROE</td></tr><tr><td>Hana</td><td>28%</td><td>19% (W754bn)</td><td>47%</td><td>1) 50% payout in total shareholder return (dividend + share buyback)2) RWA growth within nominal GDP growth3) 10+% ROE4) 13.0 ~ 13.5% CET1</td></tr><tr><td>IBK</td><td>33%</td><td>-</td><td>33%</td><td>1) 40+% payout in total shareholder return (cash dividend)2) 10+% ROE3) 12.5% CET1 ratio[Key Framework]1) Dividend payout according to CET1 ratio level~ 30% / ~35% / ~40% / 40%~ payout ratio under ~ 11.0% / ~12.0% / ~12.5% / 12.5% ~ CET1 ratio, respectively2) Adoption of quarterly dividend payout (To be implemented in 2026)</td></tr><tr><td>BNK</td><td>28%</td><td>12% (W100bn)</td><td>40%</td><td>1) 50% total shareholder return (cash dividend + share buyback)2) 4% RWA growth3) 10+% ROE (above COE)4) 12.5% CET1 ratio</td></tr><tr><td>iM</td><td>25%</td><td>14% (W60bn)</td><td>39%</td><td>1) 40% total shareholder return (dividend + share buyback) by 2027 (50% in the long term)2) W150bn share buyback/cancellation in aggregate3) 4% RWA growth4) 9% ROE by 2027 (10% in the long term)5) 12.3% CET1 ratio by 2027 (13% in the long term)</td></tr><tr><td>Kakao Bank</td><td>46%</td><td>-</td><td>46%</td><td>Mid-to-long-term Target1) Total Users: 30mn (MAU 25mn) by 20272) Total assets: W100tm by 20273) Fee &amp; Platform Income CAGR 20% (2025-2027)4) ROE 15% by 2030Shareholder return policy1) ~50% TSR by 2026- TSR to be raised to up to 50% (vs. currently 20%) if the company&#x27;s BIS ratio is higher than the average of major banks (KB/Shinhan/Hana/Woori) over the next 3 years2) Gradual increase in DPS (to be maintained at least ) from 2027- To be converted to DPS based shareholder return policy if the company&#x27;s BIS ratio is higher than the average of major banks</td></tr></table>

Source: Company data, JPM.

Figure 6: Korea Banks: Improved ROE vs. 2026E P/B %, X  
![](images/80dfff5bdcdfa851d218ced29c3108c8e055491b4c3f7fcf40c032e621553c88.jpg)  
Source: Company data, JPM estimates.
Note: Prices as of Jul. 8, 2026.

Figure 7: KB FG: ROE vs. 12M-fwd P/B  
![](images/118db1fec8fb82933bf6f73d84719cb97830ca304a8ec3c6daa58e8bb415f5db.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

Figure 8: Shinhan FG: ROE vs. 12M-fwd P/B  
![](images/63e69e8fa4df50a3833cb366eef2b78d937a39471e7ec59a23d8e6995f3a9728.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

Figure 9: Hana FG: ROE vs. 12M-fwd P/B  
![](images/e3a812abc13fd5b3d4f2ca8f5a0c79e342446cf7fe3a7e85692d96d422a088ad.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

Figure 10: IBK: ROE vs. 12M-fwd P/B  
![](images/46729cd1b8bda80ca1f4cc7df459cff2f3f1f7147e64f5e07941a5a5475d5e8a.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

Figure 11: BNK FG: ROE vs. 12M-fwd P/B  
![](images/faa9aaf371ef38d538cbaa59a34ebd033f81e2f12a775911d0fb980557f050f8.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

Figure 12: iM FG: ROE vs. 12M-fwd P/B %, X  
![](images/5baf92c3c6aaa0af2a7e4f15dff027a42ba420416fd8d888298b523c87d13c88.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

![](images/71bcdf081264d0dc59ae3fa2a1347fc6044c996dee697a1a148f9864b0521769.jpg)  
Source: Bloomberg Finance L.P., company data, JPM estimates.

## 2Q26 earnings preview in details

Table 5: KB FG: 2Q26 preview

<table><tr><td rowspan="2"></td><td rowspan="2">2Q25(W bn)</td><td rowspan="2">1Q26(W bn)</td><td rowspan="2">JPM 2Q26E(W bn)</td><td colspan="2">--- Change ---</td><td rowspan="2">Consensus(W bn)</td><td rowspan="2">vs consensus(%)</td></tr><tr><td>(q/q %)</td><td>(y/y %)</td><

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
