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
# China Financials | Asia Pacific

# Good GDP growth but no rebound in bond yield; what's implication for China financials?

# Key Takeaways

Nominal GDP growth has improved notably, supported by strong export growth and PPI returning to positive levels, however, bond yields have not rebounded.   
- Our meetings with banks shows two key factors for stable bond yields...   
...1) ample liquidity from solid export growth and more dollar-to-RMB conversion by exports; and 2) seasonally slow loan growth after a strong 1Q26.   
Continued liquidity withdrawals from PBOC also signals policymakers' intention to keep stable financial asset yields.   
We continue to expect some rebound in financial asset yields with reduced PPI pressure, which is also evidenced in stabilizing new loan yields in 1Q26.

Our conversation with banks shows that they view current government bond yields are at a good level to take some profits, as they focus on trading the market to generate gains.

Nevertheless, we continue to expect a gradual rebound in financial asset yields despite some near-term volatility, as China's financial sector returns to a positive development loop with a refocus on risk-based loan pricing and moderating deflation pressure, evidenced in: 1) stable new loan pricing in 1Q26 with sequential NIM rebound at most banks we cover; and 2) a faster-than-expected reduction in industrial credit risk based on recent data.

In addition, we believe gradual stabilization of China's property market will be another key catalyst for improving financial asset yields over the next two years, which will support further revenue and income growth improvement for domestic financial sectors, as well as a further sector re-rating. Ningbo remains our Top Pick, and we see good performance at Big 4 SOE banks and CitiC Bank H-shares.

MS ASIA LIMITED+

Richard Xu, CFA

Equity Analyst

Richard.Xu@morganstanley.com +852 2848-6729

Beryl Yang

Research Associate

Beryl.Yang@morganstanley.com +852 3963-2224

Chiyao Huang

Equity Analyst

Chiyao.Huang@morganstanley.com +852 3963-4624

Chenqian Liu

Research Associate

Chenqian.Liu@morganstanley.com +852 3963-0359

# CHINA FINANCIALS

Asia Pacific

Industry View

Attractive

# Related reports:

China Financials: 2026 Outlook: Gradually back to a positive loop (11 Jan 2026)

China – Banks 1Q26 Wrap: Revenue Jumped in 1Q26 Supported by Stable NIM and Healthy Fee Income Growth (29 Apr 2026)

China Financials: Lower overcapacity risk as new credit-demand cycle emerges (13 Apr 2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

# For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Charts

Exhibit 1: Government bond yields have declined recently. We see liquidity withdrawal from PBOC.   
![](images/238324ea908217d0941726c377c406338274c8a6fef4f755a5d2e5719f391206.jpg)

<details>
<summary>line</summary>

| Date    | 10-year treasury bond yield (%) |
|---------|----------------------------------|
| May-23  | 2.7                              |
| Jul-23  | 2.6                              |
| Sep-23  | 2.7                              |
| Nov-23  | 2.6                              |
| Jan-24  | 2.5                              |
| Mar-24  | 2.4                              |
| May-24  | 2.3                              |
| Jul-24  | 2.2                              |
| Sep-24  | 2.1                              |
| Nov-24  | 1.6                              |
| Jan-25  | 1.7                              |
| Mar-25  | 1.8                              |
| May-25  | 1.7                              |
| Jul-25  | 1.8                              |
| Sep-25  | 1.9                              |
| Nov-25  | 1.8                              |
| Jan-26  | 1.9                              |
| Mar-26  | 1.8                              |
| May-26  | 1.7                              |
</details>

![](images/491a4aaa587a3d63ab29a1ba4a3635310f28f578c077ddf5062a8eb842005f9b.jpg)

<details>
<summary>bar</summary>

Net Injection/(Withdrawal) via reverse repo (Rmb mn)
| Month | Net Injection/(Withdrawal) (Rmb mn) |
|---|---|
| Jan-24 | -300,000 |
| Feb-24 | -1,500,000 |
| Mar-24 | 400,000 |
| Apr-24 | -300,000 |
| May-24 | 600,000 |
| Jun-24 | 300,000 |
| Jul-24 | 400,000 |
| Aug-24 | 300,000 |
| Sep-24 | 800,000 |
| Oct-24 | -300,000 |
| Nov-24 | -300,000 |
| Dec-24 | 2,100,000 |
| Jan-25 | -1,100,000 |
| Feb-25 | -300,000 |
| Mar-25 | -300,000 |
| Apr-25 | 700,000 |
| May-25 | 450,000 |
| Jun-25 | -350,000 |
| Jul-25 | 650,000 |
| Aug-25 | 350,000 |
| Sep-25 | 350,000 |
| Oct-25 | -350,000 |
| Nov-25 | -450,000 |
| Dec-25 | -1,150,000 |
| Jan-26 | 1,150,000 |
| Feb-26 | -350,000 |
| Mar-26 | -1,150,000 |
| Apr-26 | -350,000 |
| May-26 | -350,000 |
</details>

Source: PBOC, CEIC, MS

# Valuation Methodology and Risks

# Bank of Ningbo Co. Ltd (002142.SZ)

We continue to use a three-stage dividend discount model, probability-weighted 60% base, 20% bull, 20% bear. The discount rate is 11.4% in the base case, and we assume 13.5% for second-stage and 13% for long-term ROE with a 61% dividend payout ratio in the long run. Our price target implies 2026E P/B of 1.2x.

# Risks to Upside

- Noticeable reduction in policy intervention amid a rapid rebound in business fundamentals.   
■ Better-than-expected NIM and asset quality.   
■ Higher-than-expected non-interest income from stronger wealth management business revenue.

# Risks to Downside

■ Risks from potential change in leadership.   
■ Higher default risks from SME and retail business expansion.   
■ Pricing pressure from destructive competition in the market.

# China CitiC Bank Corporation Limited (0998.HK)

We continue to use a 3-stage dividend discount model, probability-weighted 60% base, 20% bull, 20% bear. The discount rate is 10.0% in the base case, and we assume 9.2% for second-stage and 9.0% for long-term ROE, with a 40% long-term dividend payout ratio. We apply a 1.13 RMB/HKD exchange rate for our H-share price target. We also apply a 10% discount in deriving our target P/B for the H-shares.

# Risks to Upside

■ Faster-than-expected fee growth.   
■ Better-than-expected asset quality.   
■ Noticeable reduction in policy intervention.

# Risks to Downside

■ Asset quality could deteriorate if economic trends worsen.   
■ Unexpected decrease/slowdown in fee income.   
■ Social responsibilities continue to weigh in.

# Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

# Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Chiyao Huang; Richard Xu, CFA.

# Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

# Important Regulatory Disclosures on Subject Companies

As of April 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: China International Capital Corp. Ltd., China Merchants Bank, Chongqing Rural Commercial Bank, Futu Holdings Ltd, Qifu Technology Inc.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Bank of China Limited.

Within the last 12 months, MS has received compensation for investment banking services from Agricultural Bank of China Limited, Bank of China Limited, Industrial and Commercial Bank of China.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Agricultural Bank of China Limited, Bank of China Limited, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CitiC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CitiC Co., East Money Information Co Ltd, Futu Holdings Ltd, GF, HTSC, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Lufax, Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Agricultural Bank of China Limited, Bank of Beijing Co Ltd, Bank of China Limited, Bank of Communications, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CitiC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CMS Co Ltd, China Minsheng Banking Corp., CitiC Co., Futu Holdings Ltd, Galaxy Securities, GF, HTSC, Hua Xia Bank, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Agricultural Bank of China Limited, Bank of China Limited, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CitiC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CitiC Co., East Money Information Co Ltd, Futu Holdings Ltd, GF, HTSC, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Lufax, Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Agricultural Bank of China Limited, Bank of Beijing Co Ltd, Bank of China Limited, Bank of Communications, Bank of Hangzhou Co Ltd, Bank of Ningbo Co. Ltd, China CitiC Bank Corporation Limited, China Construction Bank Corp., China Everbright Bank Co Ltd, China International Capital Corp. Ltd., China Merchants Bank, CMS Co Ltd, China Minsheng Banking Corp., CitiC Co., Futu Holdings Ltd, Galaxy Securities, GF, HTSC, Hua Xia Bank, Industrial and Commercial Bank of China, Industrial Bank Co. Ltd., Ping An Bank, Postal Savings Bank of China Co Ltd, Qifu Technology Inc, Shanghai Pudong Development Bank.

The equity research analysts or strategists principally responsible for the preparation of MS have received compensation based upon various factors, including quality of research, investor client feedback, stock picking, competitive factors, firm revenues and overall investment banking revenues. Equity Research analysts' or strategists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

MS and its affiliates do business that relates to companies/instruments covered in MS, including market making, providing liquidity, fund management, commercial banking, extension of credit, investment services and investment banking. MS sells to and buys from customers the securities/instruments of companies covered in MS on a principal basis. MS may have a position in the debt of the Company or instruments discussed in this report. MS trades or may trade as principal in the debt securities (or in related derivatives) that are the subject of the debt research report.

Certain disclosures listed above are also for compliance with applicable regulations in non-US jurisdictions.

# STOCK RATINGS

MS uses a relative rating system using terms such as Overweight, Equal-weight, Not-Rated or Underweight (see definitions below). MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold and sell. Investors should carefully read the definitions of all ratings used in MS. In addition, since MS contains more complete information concerning the analyst's views, investors should carefully read MS, in its entirety, and not infer the contents from the rating alone. In any case, ratings (or research) should not be used or relied upon as investment advice. An investor's decision to buy or sell a stock should depend on individual circumstances (such as the investor's existing holdings) and other considerations.

# Global Stock Ratings Distribution

(as of April 30, 2026)

The Stock Ratings described below apply to MS's Fundamental Equity Research and do not apply to Debt Research produced by the Firm.

For disclosure purposes only (in accordance with FINRA requirements), we include the category headings of Buy, Hold, and Sell alongside our ratings of Overweight, Equal-weight, Not-Rated and Underweight. MS does not assign ratings of Buy, Hold or Sell to the stocks we cover. Overweight, Equal-weight, Not-Rated and Underweight are not the equivalent of buy, hold, and sell but represent recommended relative weightings (see definitions below). To satisfy regulatory requirements, we correspond Overweight, our most positive stock rating, with a buy recommendation; we correspond Equal-weight and Not-Rated to hold and Underweight to sell recommendations, respectively.

<table><tr><td></td><td colspan="2">Coverage Universe</td><td colspan="3">Investment Banking Clients (IBC)</td><td colspan="2">Other Material Investment ServicesClients (MISC)</td></tr><tr><td>Stock RatingCategory</td><td>Count</td><td>% of Total</td><td>Count</td><td>% of Total IBC</td><td>% of RatingCategory</td><td>Count</td><td>% of Total OtherMISC</td></tr><tr><td>Overweight/Buy</td><td>1546</td><td>42%</td><td>467</td><td>51%</td><td>30%</td><td>709</td><td>44%</td></tr><tr><td>Equal-weight/Hold</td><td>1568</td><td>43%</td><td>358</td><td>39%</td><td>23%</td><td>715</td><td>44%</td></tr><tr><td>Not-Rated/Hold</td><td>4</td><td>0%</td><td>0</td><td>0%</td><td>0%</td><td>1</td><td>0%</td></tr><tr><td>Underweight/Sell</td><td>555</td><td>15%</td><td>84</td><td>9%</td><td>

[中间内容因长度限制已省略]

 not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Financials 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/08/2026)</td></tr></table>

Chiyao Huang

<table><tr><td>China International Capital Corp. Ltd. (3908.HK)</td><td>O (02/28/2025)</td><td>HK$21.46</td></tr><tr><td>CMS Co Ltd (600999.SS)</td><td>U (09/29/2022)</td><td>Rmb15.92</td></tr><tr><td>CMS Co Ltd (6099.HK)</td><td>U (10/29/2024)</td><td>HK$13.88</td></tr><tr><td>CitiC Co. (6030.HK)</td><td>E (10/29/2024)</td><td>HK$27.12</td></tr><tr><td>CitiC Co. (600030.SS)</td><td>O (08/07/2025)</td><td>Rmb26.95</td></tr><tr><td>East Money Information Co Ltd (300059.SZ)</td><td>E (09/19/2025)</td><td>Rmb20.49</td></tr><tr><td>Futu Holdings Ltd (FUTU.O)</td><td>O (11/18/2024)</td><td>US$144.59</td></tr><tr><td>Galaxy Securities (6881.HK)</td><td>E (02/27/2020)</td><td>HK$8.37</td></tr><tr><td>Galaxy Securities (601881.SS)</td><td>U (09/29/2022)</td><td>Rmb12.84</td></tr><tr><td>GF (000776.SZ)</td><td>E (08/07/2025)</td><td>Rmb20.96</td></tr><tr><td>GF (1776.HK)</td><td>E (01/06/2023)</td><td>HK$17.41</td></tr><tr><td>HTSC (601688.SS)</td><td>E (09/23/2024)</td><td>Rmb19.11</td></tr><tr><td>HTSC (6886.HK)</td><td>E (09/23/2024)</td><td>HK$16.40</td></tr><tr><td colspan="3">Richard Xu, CFA</td></tr><tr><td>Agricultural Bank of China Limited (601288.SS)</td><td>E (05/07/2019)</td><td>Rmb6.90</td></tr><tr><td>Agricultural Bank of China Limited (1288.HK)</td><td>O (10/19/2020)</td><td>HK$5.94</td></tr><tr><td>Bairong Inc. (6608.HK)</td><td>E (09/09/2025)</td><td>HK$6.95</td></tr><tr><td>Bank of Beijing Co Ltd (601169.SS)</td><td>E (08/17/2022)</td><td>Rmb5.27</td></tr><tr><td>Bank of Chengdu Co Ltd (601838.SS)</td><td>O (08/17/2022)</td><td>Rmb18.87</td></tr><tr><td>Bank of China Limited (601988.SS)</td><td>E (05/07/2019)</td><td>Rmb5.68</td></tr><tr><td>Bank of China Limited (3988.HK)</td><td>O (01/10/2020)</td><td>HK$5.11</td></tr><tr><td>Bank of Communications (3328.HK)</td><td>U (05/20/2022)</td><td>HK$7.23</td></tr><tr><td>Bank of Communications (601328.SS)</td><td>U (09/05/2014)</td><td>Rmb6.70</td></tr><tr><td>Bank of Hangzhou Co Ltd (600926.SS)</td><td>E (08/17/2022)</td><td>Rmb16.79</td></tr><tr><td>Bank of Ningbo Co. Ltd (002142.SZ)</td><td>O (08/17/2022)</td><td>Rmb32.05</td></tr><tr><td>China CitiC Bank Corporation Limited (601998.SS)</td><td>E (04/16/2025)</td><td>Rmb8.26</td></tr><tr><td>China CitiC Bank Corporation Limited (0998.HK)</td><td>O (04/16/2025)</td><td>HK$8.34</td></tr><tr><td>China Construction Bank Corp. (0939.HK)</td><td>O (10/11/2012)</td><td>HK$8.76</td></tr><tr><td>China Construction Bank Corp. (601939.SS)</td><td>E (05/07/2019)</td><td>Rmb9.69</td></tr><tr><td>China Everbright Bank Co Ltd (6818.HK)</td><td>U (05/12/2023)</td><td>HK$3.12</td></tr><tr><td>China Everbright Bank Co Ltd (601818.SS)</td><td>U (05/20/2022)</td><td>Rmb3.12</td></tr><tr><td>China Merchants Bank (600036.SS)</td><td>O (01/07/2019)</td><td>Rmb37.94</td></tr><tr><td>China Merchants Bank (3968.HK)</td><td>O (09/20/2018)</td><td>HK$47.24</td></tr><tr><td>China Minsheng Banking Corp. (600016.SS)</td><td>O (08/28/2025)</td><td>Rmb3.69</td></tr><tr><td>China Minsheng Banking Corp. (1988.HK)</td><td>O (05/12/2023)</td><td>HK$3.57</td></tr><tr><td>Chongqing Rural Commercial Bank (3618.HK)</td><td>U (05/12/2023)</td><td>HK$6.81</td></tr><tr><td>Hua Xia Bank (600015.SS)</td><td>U (06/30/2015)</td><td>Rmb6.66</td></tr><tr><td>Industrial and Commercial Bank of China (1398.HK)</td><td>O (08/09/2013)</td><td>HK$6.92</td></tr><tr><td>Industrial and Commercial Bank of China (601398.SS)</td><td>E (09/19/2022)</td><td>Rmb7.46</td></tr><tr><td>Industrial Bank Co. Ltd. (601166.SS)</td><td>O (02/25/2019)</td><td>Rmb17.73</td></tr><tr><td>Lufax (LU.N)</td><td></td><td>US$1.95</td></tr><tr><td>Ping An Bank (000001.SZ)</td><td>O (05/07/2019)</td><td>Rmb11.30</td></tr><tr><td>Postal Savings Bank of China Co Ltd (1658.HK)</td><td>O (11/01/2016)</td><td>HK$5.10</td></tr><tr><td>Qifu Technology Inc (QFIN.O)</td><td>O (08/25/2020)</td><td>US$13.15</td></tr><tr><td>Shanghai Pudong Development Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.07</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.
"""
