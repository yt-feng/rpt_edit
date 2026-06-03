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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China Financials | Asia Pacific

# 1Q26: healthy payment data; Some consumption payment returned to bank cards

## Key Takeaways

Total system payment volume recorded a strong rebound in 1Q26 from a low base in 1Q25, up 29% yoy (vs +5% yoy in 4Q25).  
Overall consumption payment data trended better than official consumption data with bank card consumption payments up 3.2% yoy in 1Q26 vs a decline in 2025...  
... while official retail sales growth further moderated to 2.4% yoy, which might have resulted from a consumption shift from online back to offline channels.  
UnionPay payment growth rebounded to 11.2% yoy; while NetsUnion payment growth slightly moderated to 7.2% yoy, also above official retail sales growth.  
- Household financial asset growth remained decent in 1Q26, up 10.8% yoy, per our estimate.

## Payment growth in NetsUnion and UnionPay remained healthy in 1Q26:

NetsUnion and UnionPay payment – a good proxy for consumption payment – increased 7.2% and 11.2% yoy, respectively, still at reasonable levels compared to continued moderation in retail sales growth at 2.4% yoy.

Bank card consumption growth turned positive: While we believe banks still remain more conservative on credit card loan allocation, the trend posts positive signs for bank card consumption growth returning to a normal pace at 3-4%.

Our estimate shows 10.8% yoy household financial asset growth in 1Q26, led by equities and mutual funds. This, along with recovery in consumption payment, should support banks' fee income in 2026.

MS ASIA LIMITED+

## Richard Xu, CFA

Equity Analyst

Richard.Xu@morganstanley.com +852 2848-6729

## Beryl Yang

Research Associate

Beryl.Yang@morganstanley.com +852 3963-2224

## Chiyao Huang

Equity Analyst

Chiyao.Huang@morganstanley.com +852 3963-4624

## Chenqian Liu

Research Associate

Chenqian.Liu@morganstanley.com +852 3963-0359

![](images/2ea059bb85967dffd7506c8d7c86d4104e778b19836fce862c3ed76910dcc836.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

![](images/7e6bf7942e7e3d0c92184fb207f6e010354daf9844b504093ceacd23c7944287.jpg)

<details>
<summary>text_image</summary>

India Investment Forum 2026
</details>

## CHINA FINANCIALS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Exhibit 1: Total system payment volume picked up 29% yoy in 1Q26 vs 5% in 4Q25. Bank card consumption growth turned positive, up 3.2% yoy, vs decline in 2025.  
![](images/b0cc8a7409388e47078aa51fcc56c38e450e8455b3b92c6b42daa081e71a4b73.jpg)

<details>
<summary>line chart</summary>

| Year       | Total system payment volume yoy |
| ---------- | ------------------------------- |
| 2025-12    | 29.3%                           |
</details>

Source: PBOC, CEIC, MS

![](images/21cd721fcfe93511d904b532288c8950668dcad593b96b9d2233cfec5f6aab1b.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Quarter | Quarterly bank card consumption volume - Rmb bn | YoY   |
|---------|-----------------------------------------------|-------|
| 1Q16    | 13,000                                        | 17.5% |
| 2Q16    | 14,000                                        | 10.0% |
| 3Q16    | 15,000                                        | 15.0% |
| 4Q16    | 16,000                                        | 20.0% |
| 1Q17    | 17,000                                        | 25.0% |
| 2Q17    | 18,000                                        | 30.0% |
| 3Q17    | 19,000                                        | 35.0% |
| 4Q17    | 20,000                                        | 40.0% |
| 1Q18    | 21,000                                        | 45.0% |
| 2Q18    | 22,000                                        | 40.0% |
| 3Q18    | 23,000                                        | 35.0% |
| 4Q18    | 24,000                                        | 30.0% |
| 1Q19    | 25,000                                        | 25.0% |
| 2Q19    | 26,000                                        | 20.0% |
| 3Q19    | 27,000                                        | 15.0% |
| 4Q19    | 28,000                                        | 10.0% |
| 1Q20    | 29,000                                        | -5.0% |
| 2Q20    | 30,000                                        | -10.0%|
| 3Q20    | 31,000                                        | -5.0% |
| 4Q20    | 32,000                                        | 0.0%  |
| 1Q21    | 33,000                                        | 5.0%  |
| 2Q21    | 34,000                                        | 15.0% |
| 3Q21    | 35,000                                        | 25.0% |
| 4Q21    | 36,000                                        | 35.0% |
| 1Q22    | 37,000                                        | 45.0% |
| 2Q22    | 38,000                                        | 55.0% |
| 3Q22    | 39,000                                        | 65.0% |
| 4Q22    | 40,000                                        | 75.0% |
| 1Q23    | 41,000                                        | 85.0% |
| 2Q23    | 42,000                                        | 95.0% |
| 3Q23    | 43,000                                        | 105.0%|
| 4Q23    | 44,000                                        | 115.0%|
| 1Q24    | 45,000                                        | 125.0%|
| 2Q24    | 46,000                                        | 135.0%|
| 3Q24    | 47,000                                        | 145.0%|
| 4Q24    | 48,000                                        | 155.0%|
| 1Q25    | 49,000                                        | 165.0%|
| 2Q25    | 50,000                                        | 175.0%|
| 3Q25    | 51,000                                        | 185.0%|
| 4Q25    | 52,000                                        | 195.0%|
| 1Q26    | 53,000                                        | 3.2%  |
</details>

Exhibit 2: UnionPay payment growth rebounded from 4Q, up 11.2% yoy; while NetsUnion payment growth slightly moderated to 7.2% yoy.  
![](images/0de2c97134b8ccd6d012a4e42eeacfb9374e271cf7e432d919e11dec76a161b4.jpg)

<details>
<summary>bar-line hybrid</summary>

| Quarter | NetsUnion payment volume - Rmb bn | YoY   |
| ------- | --------------------------------- | ----- |
| 1Q20    | 65,000                            | 7.2%  |
| 2Q20    | 80,000                            | 15.0% |
| 3Q20    | 95,000                            | 40.0% |
| 4Q20    | 110,000                           | 45.0% |
| 1Q21    | 105,000                           | 65.0% |
| 2Q21    | 115,000                           | 45.0% |
| 3Q21    | 125,000                           | 30.0% |
| 4Q21    | 120,000                           | 25.0% |
| 1Q22    | 105,000                           | 10.0% |
| 2Q22    | 110,000                           | -5.0% |
| 3Q22    | 120,000                           | -5.0% |
| 4Q22    | 125,000                           | -5.0% |
| 1Q23    | 125,000                           | -5.0% |
| 2Q23    | 130,000                           | -5.0% |
| 3Q23    | 135,000                           | -5.0% |
| 4Q23    | 140,000                           | -5.0% |
| 1Q24    | 135,000                           | -5.0% |
| 2Q24    | 145,000                           | -5.0% |
| 3Q24    | 150,000                           | -5.0% |
| 4Q24    | 155,000                           | -5.0% |
| 1Q25    | 160,000                           | -5.0% |
| 2Q25    | 165,000                           | -5.0% |
| 3Q25    | 170,000                           | -5.0% |
| 4Q25    | 175,000                           | -5.0% |
| 1Q26    | 180,000                           | -7.2% |
</details>

Source: PBOC, CEIC, MS

![](images/57fb76ed733d3656758f35271e6dbcfe8a60e1df4508b739735bb6b85305a255.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Quarter | UnionPay Payment Volume - Rmb bn | YoY Growth |
| ------- | -------------------------------- | ---------- |
| 3Q16    | 18,000                           | 40%        |
| 1Q17    | 20,000                           | 35%        |
| 2Q17    | 22,000                           | 45%        |
| 3Q17    | 24,000                           | 50%        |
| 4Q17    | 26,000                           | 55%        |
| 1Q18    | 28,000                           | 50%        |
| 2Q18    | 30,000                           | 45%        |
| 3Q18    | 32,000                           | 40%        |
| 4Q18    | 34,000                           | 35%        |
| 1Q19    | 36,000                           | 30%        |
| 2Q19    | 38,000                           | 25%        |
| 3Q19    | 40,000                           | 20%        |
| 4Q19    | 42,000                           | 15%        |
| 1Q20    | 44,000                           | 10%        |
| 2Q20    | 46,000                           | 5%         |
| 3Q20    | 48,000                           | 0%         |
| 4Q20    | 50,000                           | -5%        |
| 1Q21    | 52,000                           | -10%       |
| 2Q21    | 54,000                           | -15%       |
| 3Q21    | 56,000                           | -20%       |
| 4Q21    | 58,000                           | -25%       |
| 1Q22    | 60,000                           | -30%       |
| 2Q22    | 62,000                           | -35%       |
| 3Q22    | 64,000                           | -40%       |
| 4Q22    | 66,000                           | -45%       |
| 1Q23    | 68,000                           | -50%       |
| 2Q23    | 70,000                           | -55%       |
| 3Q23    | 72,000                           | -60%       |
| 4Q23    | 74,000                           | -65%       |
| 1Q24    | 76,000                           | -70%       |
| 2Q24    | 78,000                           | -75%       |
| 3Q24    | 80,000                           | -80%       |
| 4Q24    | 82,000                           | -85%       |
| 1Q25    | 84,000                           | -90%       |
| 2Q25    | 86,000                           | -95%       |
| 3Q25    | 88,000                           | -100%      |
| 4Q25    | 90,000                           | -105%      |
| 1Q26    | 92,000                           | -112%      |
</details>

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Chiyao Huang; Richard Xu, CFA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: China International Capital Corp. Ltd., China Merchants Bank, Chongqing Rural Commercial Bank, Futu Holdings Ltd, Qifu Technology Inc.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Bank of China Limited.

Within the last 12 months, MS has received compensation for investment banking services from Agricultural Bank of China Limited, Bank of China Limited, Industrial and Commercial Bank of China.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Agricultural Bank of China Limited, Bank of Beijing Co Ltd, Bank of China Limited, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CITIC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CITIC Co., East Money Information Co Ltd, Futu Holdings Ltd, GF Securities, HTSC, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Lufax, Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Agricultural Bank of China Limited, Bank of Beijing Co Ltd, Bank of China Limited, Bank of Communications, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CITIC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CMS Co Ltd, China Minsheng Banking Corp., CITIC Co., Futu Holdings Ltd, Galaxy Securities, GF Securities, HTSC, Hua Xia Bank, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Agricultural Bank of China Limited, Bank of Beijing Co Ltd, Bank of China Limited, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CITIC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CITIC Co., East Money Information Co Ltd, Futu Holdings Ltd, GF Securities, HTSC, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Lufax, Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Agricultural Bank of China Limited, Bank of Beijing Co Ltd, Bank of China Limited, Bank of Communications, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CITIC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CMS Co Ltd, China Minsheng Banking Corp., CITIC Co., East Money Information Co Ltd, Futu Holdings Ltd, Galaxy Securities, GF Securities, HTSC, Hua Xia Bank, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Ping An Bank, Postal Savi

[中间内容因长度限制已省略]

ges relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Financials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/29/2026)</td></tr><tr><td colspan="3">Chiyao Huang</td></tr><tr><td>China International Capital Corp. Ltd. (3908.HK)</td><td>O (02/28/2025)</td><td>HK$19.62</td></tr><tr><td>CMS Co Ltd (600999.SS)</td><td>U (09/29/2022)</td><td>Rmb16.99</td></tr><tr><td>CMS Co Ltd (6099.HK)</td><td>U (10/29/2024)</td><td>HK$14.64</td></tr><tr><td>CITIC Co. (6030.HK)</td><td>E (10/29/2024)</td><td>HK$26.04</td></tr><tr><td>CITIC Co. (600030.SS)</td><td>O (08/07/2025)</td><td>Rmb26.05</td></tr><tr><td>East Money Information Co Ltd (300059.SZ)</td><td>E (09/19/2025)</td><td>Rmb19.16</td></tr><tr><td>Futu Holdings Ltd (FUTU.O)</td><td>O (11/18/2024)</td><td>US$104.07</td></tr><tr><td>Galaxy Securities (6881.HK)</td><td>E (02/27/2020)</td><td>HK$7.76</td></tr><tr><td>Galaxy Securities (601881.SS)</td><td>U (09/29/2022)</td><td>Rmb12.28</td></tr><tr><td>GF Securities (000776.SZ)</td><td>E (08/07/2025)</td><td>Rmb18.89</td></tr><tr><td>GF Securities (1776.HK)</td><td>E (01/06/2023)</td><td>HK$16.15</td></tr><tr><td>HTSC (601688.SS)</td><td>E (09/23/2024)</td><td>Rmb18.18</td></tr><tr><td>HTSC (6886.HK)</td><td>E (09/23/2024)</td><td>HK$15.85</td></tr><tr><td colspan="3">Richard Xu, CFA</td></tr><tr><td>Agricultural Bank of China Limited (601288.SS)</td><td>E (05/07/2019)</td><td>Rmb6.32</td></tr><tr><td>Agricultural Bank of China Limited (1288.HK)</td><td>O (10/19/2020)</td><td>HK$5.77</td></tr><tr><td>Bairong Inc. (6608.HK)</td><td>E (09/09/2025)</td><td>HK$5.43</td></tr><tr><td>Bank of Beijing Co Ltd (601169.SS)</td><td>E (08/17/2022)</td><td>Rmb5.09</td></tr><tr><td>Bank of Chengdu Co Ltd (601838.SS)</td><td>O (08/17/2022)</td><td>Rmb18.60</td></tr><tr><td>Bank of China Limited (601988.SS)</td><td>E (05/07/2019)</td><td>Rmb5.86</td></tr><tr><td>Bank of China Limited (3988.HK)</td><td>O (01/10/2020)</td><td>HK$5.21</td></tr><tr><td>Bank of Communications (3328.HK)</td><td>U (05/20/2022)</td><td>HK$7.30</td></tr><tr><td>Bank of Communications (601328.SS)</td><td>U (09/05/2014)</td><td>Rmb6.66</td></tr><tr><td>Bank of Hangzhou Co Ltd (600926.SS)</td><td>E (08/17/2022)</td><td>Rmb16.01</td></tr><tr><td>Bank of Ningbo Co. Ltd (002142.SZ)</td><td>O (08/17/2022)</td><td>Rmb31.03</td></tr><tr><td>China CITIC Bank Corporation Limited (601998.SS)</td><td>E (04/16/2025)</td><td>Rmb7.42</td></tr><tr><td>China CITIC Bank Corporation Limited (0998.HK)</td><td>O (04/16/2025)</td><td>HK$7.29</td></tr><tr><td>China Construction Bank Corp. (0939.HK)</td><td>O (10/11/2012)</td><td>HK$8.49</td></tr><tr><td>China Construction Bank Corp. (601939.SS)</td><td>E (05/07/2019)</td><td>Rmb9.96</td></tr><tr><td>China Everbright Bank Co Ltd (6818.HK)</td><td>U (05/12/2023)</td><td>HK$3.05</td></tr><tr><td>China Everbright Bank Co Ltd (601818.SS)</td><td>U (05/20/2022)</td><td>Rmb3.10</td></tr><tr><td>China Merchants Bank (600036.SS)</td><td>O (01/07/2019)</td><td>Rmb38.01</td></tr><tr><td>China Merchants Bank (3968.HK)</td><td>O (09/20/2018)</td><td>HK$47.10</td></tr><tr><td>China Minsheng Banking Corp. (600016.SS)</td><td>O (08/28/2025)</td><td>Rmb3.55</td></tr><tr><td>China Minsheng Banking Corp. (1988.HK)</td><td>O (05/12/2023)</td><td>HK$3.36</td></tr><tr><td>Chongqing Rural Commercial Bank (3618.HK)</td><td>U (05/12/2023)</td><td>HK$6.36</td></tr><tr><td>Hua Xia Bank (600015.SS)</td><td>U (06/30/2015)</td><td>Rmb6.71</td></tr><tr><td>Industrial and Commercial Bank of China (1398.HK)</td><td>O (08/09/2013)</td><td>HK$6.64</td></tr><tr><td>Industrial and Commercial Bank of China (601398.SS)</td><td>E (09/19/2022)</td><td>Rmb7.22</td></tr><tr><td>Industrial Bank Co. Ltd. (601166.SS)</td><td>O (02/25/2019)</td><td>Rmb18.50</td></tr><tr><td>Lufax (LU.N)</td><td></td><td>US$1.65</td></tr><tr><td>Ping An Bank (000001.SZ)</td><td>O (05/07/2019)</td><td>Rmb10.93</td></tr><tr><td>Postal Savings Bank of China Co Ltd (1658.HK)</td><td>O (11/01/2016)</td><td>HK$5.02</td></tr><tr><td>Qifu Technology Inc (QFIN.O)</td><td>O (08/25/2020)</td><td>US$16.08</td></tr><tr><td>Shanghai Pudong Development Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.37</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
