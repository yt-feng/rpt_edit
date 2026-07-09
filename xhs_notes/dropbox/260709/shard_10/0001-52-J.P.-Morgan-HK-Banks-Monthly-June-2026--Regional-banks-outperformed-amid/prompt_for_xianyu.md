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
## HK Banks Monthly

## June 2026: Regional banks outperformed amid broad-based market weakness

HK banks on average corrected by 5% in June, but outperformed the HSI by 4% as broad market sentiment was dragged by lingering concerns on new ODI rules and adverse implications on cross-border investment flows, while improving operating trends and a more hawkish tone from the FED interest rate meeting has lent support to bank share prices, and explained the relative outperformance of regional banks over local HK banks. More favorable earnings momentum in 1H26 and a more direct beneficiary of potential FED rate hikes might allow HSBC to sustain the relative outperformance in the near future.

\- News summary for June 2026: June headlines continued to focus on tighter cross-border investment activity for mainland clients, with some banks reportedly postponing mainland-related initiatives, although the HKMA commented that the relevant account-opening process remains smooth. On asset quality, KPMG expects HK banks' NPL ratios to improve in FY27 and Fitch has upgraded the sector's outlook, citing that the worst of HK CRE stress has passed, while Deloitte observed that HK banks have sped up the collateral divestments in individual delinquent CRE cases. At the company level, HSBC has reportedly become involved in the IFFCO Group's debt crisis with exposure of up to US\$400mn, while it is also conducting a strategic review for the potential sale of its SG insurance business. Meanwhile, STAN is assessing the feasibility to set up a gold vault in HK for business expansion after it delivered a high double-digit growth in gold-related revenue in 1Q26. For BOCHK, the CRO noted that NPL pressure is likely to persist in 2H26, but the bank has adequate LLR and expects its asset quality to outperform peers.

\- Loan growth momentum continues to trend up: (1) Industry loan growth rose to 6.0% YoY in May from 5.4% in April, continuing the sequential uptrend since November 2025, driven by decent momentum in trade finance-related flows. (2) Mortgage lending growth also edged up to 3.3% YoY in May from 3.1% in April, while newly approved mortgage loans rose 10.1% MoM. BOCHK remained the market leader in completed mortgages in 1H26, capturing a 31% market share, followed by HSBC at 24%; however, HSBC led the off-plan mortgage segment with a 24% market share, higher than the 22% at BOCHK. (3) LDR fell 47 bps MoM to 52.3% in May on stronger deposit growth, with HKD LDR declining more materially (-65 bps MoM) than FCY LDR (-7 bps MoM). The overall CASA ratio was up slightly to 44.6% in May from 44.1% in April.

\- Narrowing SOFR-HIBOR gap on stronger HIBOR: (1)1M/3M SOFR was largely stable MoM in June on a daily average basis, while 1M/3M HIBOR increased by 23bps/10bps MoM, leading to a narrowing 1M/3M SOFR-HIBOR gap of 82bps/79bps (down 21bps/6bps MoM) likely reflecting the typical quarter-end liquidity conditions and changing expectations for US rate policy. (2) Aggregate balances and EFBN (Exchange Fund Bills and Notes) stabilized at c.HK\$1.4tn in June, while the HKD/USD also remained broadly unchanged at 7.84 by the end of June. (3) Composite interest rates rose to 1.26% in May from 1.21% in April, marking an uptick in banks' funding costs after a steady decline since Dec 2025, but the implied deposit spreads increased 26 bps MoM on the back of a stronger HIBOR. (4) Overall deposit competition in HK remained rational during the past month, with slightly intensified

## Asia Financials

Jemmy S Huang AC
(886-2) 2725-9870
jemmy.s.huang@JPM.com
JPM Securities (Taiwan) Limited/ JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

Amanda Chang
(886-2) 2725-9861
amanda.chang@JPM.com
JPM Securities (Taiwan) Limited

Haomin Chen
(86-21) 6106 6347
haomin.chen@JPM.com
SAC Registration Number: S1730524080002
JPM Securities (China) Company Limited

Katherine Lei
(852) 2800-8552
katherine.lei@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

competition among small and virtual banks mainly on HKD deposits in response to the quarter-end liquidity management (Table 3).

\- Underlying asset quality trends were largely stable: (1) 3M mortgage delinquency ratio was further down to $0.11\%$ in May from $0.12\%$ in April, representing a gradual declining trend since Nov 2025 amid stabilizing property market, while the 6M ratio was unchanged at $0.09\%$ in May. (2) The unemployment rate was $3.7\%$ in May, as the labor market in HK remained stable after seeing a downward trend YTD. (3) In May, there were 728 bankruptcy petitions $(-7\% \mathrm{MoM})$ , with the cumulative 5M26 figure showing a $12\%$ YoY decline; meanwhile, bankruptcies reached 753 cases, up $25\%$ MoM, but the 5M26 figure was still down $5\%$ YoY. (4) According to HKMA, HK banks' NPL ratio fell to $1.87\%$ in 1Q26 from $2.01\%$ in 4Q25, marking an eight-quarter low under an improving asset quality trend.

\- HSBC>BOCHK & STAN into 1H26 results. Both BOCHK and STAN would be facing higher base effects on non-NII in 1H26 due to stronger trading gains and episodic income in 2Q25 respectively, thus HSBC may deliver better momentum on operating profits into 1H26 results to sustain its relative outperformance YTD. Meanwhile, market focus should also be on management guidance on WM business implications/impacts due to the new ODI rules as well as on shareholder return measures, in particular the relaunch of SBB at HSBC and details of the three-year shareholder return enhancement program at BOCHK.

Table 1: Summary of key news in June

<table><tr><td>Date</td><td>Summary</td><td>Details</td><td>Link</td></tr><tr><td>6/6/2026</td><td>Banks Postpone Mainland Activities and Limit Travel Due to Tightened Scrutiny</td><td>Following tightened cross-border investment scrutiny by authorities, certain private banks like UBS have postponed mainland activities, while HSBC has advised private bankers to avoid non-essential travel to China.</td><td>Link</td></tr><tr><td>6/7/2026</td><td>HKMA: Bank Account Opening for Mainland Customers Remains Smooth</td><td>The HKMA stated that the banking sector has implemented the latest regulatory requirements for mainland clients, and the overall process for mainland customers opening accounts remains smooth.</td><td>Link</td></tr><tr><td>6/11/2026</td><td>Fitch Upgrades China/HK Banking Sector Outlook</td><td>Fitch has upgraded the banking sector outlook for HK and China from &quot;deteriorating&quot; to &quot;neutral.&quot; The agency also noted that the worst period for HK CRE has largely passed and HK banks continue to benefit from cross-border WM flows and robust capital market activities.</td><td>Link</td></tr><tr><td>6/13/2026</td><td>HSBC Reportedly Faces Up to US $400mn Exposure in IFFCO&#x27;s Debt Crisis</td><td>HSBC is reportedly involved in a bankruptcy debt crisis of IFFCO Group, a major consumer goods company in the Middle East. As the largest creditor, HSBC&#x27;s debt exposure could reach up to US$400m.</td><td>Link</td></tr><tr><td>6/15/2026</td><td>STAN Explores Setting Up Gold Vault in HK</td><td>STAN reported a high double-digit growth in gold-related revenue for 1Q26 and is currently evaluating locations to set up its own gold vault in HK to expand its gold business in 2H26.</td><td>Link</td></tr><tr><td>6/15/2026</td><td>HSBC Considers Sale of SG Insurance Business with Allianz Reportedly Leading the Bid</td><td>HSBC is conducting a strategic review regarding the potential sale of its Singapore insurance business, which could be valued at up to US$2bn. Allianz has reportedly emerged as the leading contender in the bidding process.</td><td>Link</td></tr><tr><td>6/18/2026</td><td>KPMG: HK Banks&#x27; FY25 Revenue Rose Over 5% with Improving NPL Outlook Next Year</td><td>A KPMG report highlighted that HK banks saw 5.1% revenue growth for 2025. Although future profitability may face pressure from uncertainty in interest rates, continued weakness in CRE and rising deposit competition, the impaired loan ratio is expected to decline next year.</td><td>Link</td></tr><tr><td>6/18/2026</td><td>HKMA Proposes 23% Hike in Bank License Fees</td><td>The government has proposed raising bank license fees by 23% to HK$750k. Authorities emphasized that this fee represents a minimal fraction of financial institutions&#x27; expenses and will not harm HK&#x27;s international financial competitiveness.</td><td>Link</td></tr><tr><td>6/22/2026</td><td>HK Banks Sped up the Collateral Divestments in Individual Delinquent CRE Cases</td><td>According to Deloitte, HK banks are stepping up efforts to resolve NPL tied to local property developers, even if it means realizing losses, as prolonged weakness in the CRE market has increased pressure on collateral values and regulatory capital.</td><td>Link</td></tr><tr><td>6/25/2026</td><td>STAN Explores Sale of Bahrain Wealth &amp; Retail Banking Business</td><td>STAN is exploring the sale of its WM and retail banking operations in Bahrain as part of its strategy to focus on larger-scale business and customer segments with greater product differentiation. The bank will retain its CIB business in Bahrain, with the transition expected to take 18-24 months, subject to regulatory approvals.</td><td>Link</td></tr><tr><td>6/25/2026</td><td>BOCHK Expects Continued NPL Pressure in 2H26</td><td>BOCHK&#x27;s Chief Risk Officer said at the AGM that NPL pressure is expected to remain elevated in 2H26 amid ongoing geopolitical tensions and persistent inflation. The bank has maintained adequate loan-loss provisions and expects its asset quality to remain better than the market average.</td><td>Link</td></tr></table>

Source: News websites, JPM.

Figure 1: Industry loan YoY growth – for use in vs outside HK  
![](images/f933595fc70c1bf8933827b4885947b57b9d41f0aad46a166f9ffbafb4b255f0.jpg)  
Total loans and advances - YoY growth
Total loans and advances for use in HK - YoY growth
Total loans for use outside HK - YoY growth  
Source: HKMA, JPM.

Figure 2: Industry loan YoY growth – HKD vs FCY loans  
![](images/4de51e848b95ae94224f82fac769ef66fc4d2c29ae2712d03155e39b5b70c79f.jpg)  
Source: HKMA, JPM.

Figure 3: Industry mortgage YoY growth  
![](images/0261ef929d121055f67508e6b39382e9c9eccffd658ca0d5dd630008377aac4b.jpg)  
Table 2: Mortgage share ranking for completed and off-plan properties – 1H26  
Source: HKMA, JPM.

<table><tr><td colspan="2"></td><td colspan="2">Completed property</td><td colspan="2">Off-plan property</td></tr><tr><td>No.</td><td>Company</td><td>Unit</td><td>% shares</td><td>Unit</td><td>% shares</td></tr><tr><td>1</td><td>BOCHK</td><td>12,703</td><td>31.3%</td><td>630</td><td>22.1%</td></tr><tr><td>2</td><td>HSBC</td><td>9,649</td><td>23.7%</td><td>684</td><td>24.0%</td></tr><tr><td>3</td><td>HSB</td><td>5,180</td><td>12.7%</td><td>382</td><td>13.4%</td></tr><tr><td>4</td><td>STAN</td><td>3,423</td><td>8.4%</td><td>328</td><td>11.5%</td></tr><tr><td>5</td><td>ICBC Asia</td><td>2,116</td><td>5.2%</td><td>295</td><td>10.3%</td></tr><tr><td>6</td><td>BEA</td><td>1,527</td><td>3.8%</td><td>112</td><td>3.9%</td></tr><tr><td>7</td><td>BoCom (HK)</td><td>972</td><td>2.4%</td><td>146</td><td>5.1%</td></tr><tr><td>8</td><td>Citic Bank</td><td>910</td><td>2.2%</td><td>60</td><td>2.1%</td></tr><tr><td>9</td><td>Citi</td><td>891</td><td>2.2%</td><td>48</td><td>1.7%</td></tr><tr><td>10</td><td>OCBC (HK)</td><td>714</td><td>1.8%</td><td>79</td><td>2.8%</td></tr><tr><td></td><td>Industry</td><td>40,642</td><td>100.0%</td><td>2,854</td><td>100.0%</td></tr></table>

Source: Centraline.

Figure 4: Industry LDR and CASA %  
![](images/6ae9cb9d3d5a989f9f23682ef623db274c1e43a8b21d712533106c8f429625e7.jpg)  
Source: HKMA, JPM.

Figure 5: Industry LDR by currency – HKD vs FCY  
![](images/91f5967c75e829641de009a3db15b2a051adf363007234b18b0b221f0f50e719.jpg)

Figure 6: Daily average 1M SOFR and HIBOR  
![](images/02adf03b6517af760c8405887262090eb7d726c8adc3bdafc457bf09b77d33d4.jpg)  
Source: Bloomberg Finance L.P., JPM.  
Source: HKMA, JPM.

Figure 7: Daily average 3M SOFR and HIBOR  
![](images/7de2aaf0f999be9664bd03154af99ccd9e01a1cf35627ee7438350d86bfb08f0.jpg)  
Source: Bloomberg Finance L.P., JPM.

Figure 8: 1M SOFR-HIBOR gap vs. USD/HKD FX rates  
![](images/4cb20ec80a8bf1b28f92689c9e7c8fd40818af15f88dba2055a5e85f21dc93b7.jpg)  
Source: Bloomberg Finance L.P., JPM.

Figure 9: 1M SOFR-HIBOR gap vs. aggregate balance + EFBN  
![](images/232152caee1512a7312f62d7fcff9869d53738d52f92a50da24e949cc757ae1c.jpg)  
Source: Bloomberg Finance L.P., JPM.

Figure 10: The composite interest rate was 1.26% in May 2026  
![](images/a74141c11f6a8abd93e5ebd6213aabf1dfa932da0ba43fa563dc4a323615b387.jpg)  
Source: HKMA.

Figure 11: Implied deposit spreads increased MoM in May on higher HIBOR  
![](images/8998e06a35e8715ca1be9b9b0dd7c4f08aa19442e742850d71a6fb20c873e00f.jpg)  
Source: Bloomberg Finance L.P., HKMA, JPM. Note: Spreads calculated based on the composite interest rate since July 2025 (previously weighted deposit rate) due to data unavailability.

Table 3: Special deposit terms for HKD and USD in June

<table><tr><td>Date</td><td>Bank</td><td>Deposit</td><td>Annual rates</td><td>Note</td></tr><tr><td>6/1/2026</td><td>ICBC (Asia)</td><td>HKD time deposit (3M)</td><td>3.88%</td><td>New customers opening an integrated account via the mobile banking&#x27;s &quot;e-Account Opening&quot; feature and placing a 3M HKD time deposit.</td></tr><tr><td>6/2/2026</td><td>OCBC</td><td>HKD time deposit (3M)</td><td>2.70%</td><td>Wealth management customers opening a 3M HKD time deposit with at least HK$100k of new funds at a branch can enjoy a promotional annual interest rate of 2.7%.</td></tr><tr><td>6/2/2026</td><td>Fusion Bank</td><td>USD time deposit (12M)</td><td>3.70%</td><td>Customers opening a 12M USD time deposit through the mobile app can enjoy a 3.7% annual interest rate, with no minimum deposit requirement.</td></tr><tr><td>6/3/2026</td><td>EleBank</td><td>HKD time deposit (12M)</td><td>2.90%</td><td>Customers who place a 12M HKD time deposit via the mobile app can enjoy an annual interest rate of 2.90%; min deposit amount: HK$1k</td></tr><tr><td>6/5/2026</td><td>WeLab Bank</td><td>HKD time deposit (12M)</td><td>2.80%</td><td>Customers opening a 12M HKD time deposit via the mobile app can enjoy an annual interest rate of 2.8%.</td></tr><tr><td>6/8/2026</td><td>STAN</td><td>HKD time deposit (7D)</td><td>5.00%</td><td>Customers who exchange foreign currency into HKD via online or mobile banking, and open a 7-day designated HKD time deposit; min deposit amount: HK$10k</td></tr><tr><td>6/9/2026</td><td>EleBank</td><td>HKD time deposit (12M)</td><td>2.90%</td><td>Customers who place a 12M HKD time deposit via the mobile app can enjoy an annual interest rate of 2.90%; min deposit amount: HK$1k</td></tr><tr><td>6/9/2026</td><td>CCB (Asia)</td><td>USD time deposit (3M)</td><td>7.38%</td><td>Visit a CCB (Asia) branch in person to place a 3 month time deposit using new funds or by exchanging into USD; deposit an amount no less than the time deposit amount into a CASA account and keep it until the time deposit matures.</td></tr><tr><td>6/10/2026</td><td>Fusion Bank</td><td>HKD time deposit (12M)</td><td>2.90%</td><td>Customers opening 12M HKD time deposit through the mobile app can enjoy a 2.9% annual interest rate, with no minimum deposit requirement.</td></tr><tr><td>6/10/2026</td><td>EleBank</td><td>USD time deposit (12M)</td><td>3.80%</td><td>Customers who place a 12M USD time deposit via the mobile app can enjoy an annual interest rate of 3.8%; min deposit amount: US$1k</td></tr><tr><td>6/11/2026</td><td>DBS</td><td>HKD time deposit (6M)</td><td>3.00%</td><td>DBS customers who successfully register and open a 4- or 6-month HKD time deposit with

[中间内容因长度限制已省略]

 date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not
"""
