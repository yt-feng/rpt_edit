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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Tanker Shipping | Asia Pacific

# Beneficiary of Strait Reopening; Reiterate Bullish Views

We answer the market's key questions and pushback on our tanker shipping call, and preview tanker names' 2Q26 earnings.

## Key Takeaways

We see a potential spot rally if the Strait reopening materializes. Spot rates will likely stay elevated for months amid potential global oil re-stocking.  
We expect CMES will deliver strong 2Q26 earnings. CSE's 2Q26 earnings will likely be relatively soft vs. CMES, but it is in the price.

A reverse of market pessimism in the past three weeks: Tanker shipping names' share prices underperformed market indexes by 17-27ppts during May 21 and Jun 11, 2026, mainly on the market's disappointment that the Strait of Hormuz had remained closed for longer than expected. As global oil reserves have been running lower, the market was worried that oil shipment demand would decrease (Exhibit 6), leading to tanker shipping oversupply, weighing on spot rates (Exhibit 2). Now, that expectation is reversed with the potential reopening of the Strait.

What will happen if the Strait reopens? Spot rates will hike, supporting tanker sentiment – we would expect to see: 1) a potential surge in oil shipment demand – importers would likely see strong willingness to rebuild inventory, while exporters would need to release their storage in the Gulf; and 2) a potential shortage of tanker capacity in Middle East – some tankers have sailed to the Atlantic market. We are not worried about the current capacity in the Gulf – tankers currently in the Gulf are laden and will not become available capacity anytime soon.

## Will the spot rally fade quickly after the initial surge post the Strait's reopening?

We would expect high spot rate volatility after the reopening. However, equilibrium rate levels beyond the initial volatility are more important. We focus on two moving factors in the next 3-6 months: 1) global oil storage build – we think this will last for a few quarters, if not longer; and 2) whether sanctions on Iranian oil are removed. Either could act as potential demand support and lead to sustained strong earnings.

2Q26 preview: We expect an earnings increase of over 50% QoQ for China Merchant Energy Shipping in 2Q26, driven by the post disruption VLCC spot market surge in March 2026, as well as the strengthened dry bulk shipping market. For COSCO SHIPPING Energy Transportation, we only expect a minor QoQ increase in total profit, considering: 1) Effective rates dilution from vessels trapped in the Arabian Gulf since March 2026; 2) softened international product oil shipping amid the shortage in product oil exports from the Middle East; and 3) slowed China crude imports, which drag on domestic oil profits.

Downside risks to our call: The Strait's reopening fails to materialize.

MS ASIA LIMITED+

## Qianlei Fan, CFA

Equity Analyst

Qianlei.Fan@morganstanley.com +852 2239-1875

## Evan Chen

Research Associate

Evan.Chen@morganstanley.com +852 2848-7317

## Tenny Song

Equity Analyst

Tenny.Song@morganstanley.com +852 3963-1737

## Asia Summer School 2026

![](images/e7cfb4daa70a44ad32ecfc6a452cc99d335772013a29a9c4ef9263fb27ca64e9.jpg)

## HONG KONG/CHINA TRANSPORTATION & INFRASTRUCTURE

Asia Pacific

Industry View

In-Line

Also read:

Our positive RTIs on CSE-H, CSE-A and CMES

Shipping: Geopolitics Playbook: Middle East Tension in Focus (9 Apr 2026)

Asia Energy Security and AI: Energy Meets

Compute: Supercycle Recharges (21 May 2026)

This report references jurisdiction(s) or person(s) which may be the subject of economic sanctions. Readers are solely responsible for ensuring that their investment activities are carried out in compliance with applicable laws.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Preview to earnings

<table><tr><td>Focus KPI</td><td>Focus KPI Surprise</td><td>Likely impact to consensus EPS*</td></tr><tr><td colspan="3">COSCO SHIPPING Energy Transportation 1138.HK</td></tr><tr><td>2Q26 net profit</td><td>– In-line</td><td>– Largely unchanged</td></tr><tr><td colspan="3">• We expect Rmb2.2bn net profit in 2Q26.</td></tr><tr><td colspan="3">• We see limited downside to our full-year forecasts amid the potential reopening of the Strait.</td></tr><tr><td colspan="3">COSCO SHIPPING Energy Transportation 600026.SS</td></tr><tr><td>2Q26 net profit</td><td>– In-line</td><td>– Largely unchanged</td></tr><tr><td colspan="3">• We expect Rmb2.2bn net profit in 2Q26.</td></tr><tr><td colspan="3">• We see limited downside to our full-year forecasts amid the potential reopening of the Strait.</td></tr></table>

China Merchants Energy Shipping Co. Ltd. 601872.SS

<table><tr><td>2Q26 net profit</td><td>↑ Very likely upside surprise</td><td>↑ Modest revision higher</td></tr><tr><td colspan="3">• We expect Rmb4.2bn net profit in 2Q26.</td></tr></table>

\*Likely impact to consensus EPS is for the next 12 months  
Source: Company data, MS

## Key Charts

Exhibit 1: Relative share performance: Tankers  
![](images/a17c9def26849f1e8ca9f0d7db26fec73fdb0e8f0e0f6ba49ffc6974be128b41.jpg)

<details>
<summary>line chart</summary>

| Date     | CMES  | CSE-A | CSE-H |
| -------- | ----- | ----- | ----- |
| 27-Feb   | 15%   | 20%   | 10%   |
| 13-Mar   | 5%    | 10%   | 0%    |
| 27-Mar   | 10%   | 30%   | 15%   |
| 10-Apr   | 30%   | 30%   | 10%   |
| 24-Apr   | 15%   | 10%   | 0%    |
| 8-May    | 20%   | 10%   | 10%   |
| 22-May   | 10%   | 10%   | 5%    |
| 5-Jun    | -10%  | -15%  | -20%  |
</details>

Source: Factset, MS

Exhibit 2: Tanker Spot Earnings have corrected mildly since May 2026  
![](images/e383b2397b28eec7d340e7e95b8bbcff66a9c3cb64bcda6e87adf3fd36e1f9d3.jpg)

<details>
<summary>line chart</summary>

| Date   | TCE: West Africa - China | TCE: US Gulf - China |
|--------|--------------------------|----------------------|
| Mar-26 | ~180,000                 | ~170,000             |
| Apr-26 | ~130,000                 | ~150,000             |
| May-26 | ~120,000                 | ~110,000             |
| Jun-26 | ~90,000                  | ~95,000              |
</details>

Source: Clarksons, MS

Exhibit 3: US oil inventory (including SPR)  
![](images/4f901e054e91d98f9c75dd5018f4f6266425a47734c967b55b6b7b054cd1065f.jpg)

<details>
<summary>line chart</summary>

| Date   | US Crude Oil inventory (million barrels) | YoY (%) |
|--------|-------------------------------------------|---------|
| Jan-18 | ~1,050                                    | ~-10%   |
| Jul-18 | ~1,050                                    | ~-5%    |
| Jan-19 | ~1,050                                    | ~0%     |
| Jul-19 | ~1,050                                    | ~5%     |
| Jan-20 | ~1,050                                    | ~10%    |
| Jul-20 | ~1,200                                    | ~15%    |
| Jan-21 | ~1,150                                    | ~5%     |
| Jul-21 | ~1,050                                    | ~0%     |
| Jan-22 | ~900                                      | ~-10%   |
| Jul-22 | ~700                                      | ~-15%   |
| Jan-23 | ~600                                      | ~-20%   |
| Jul-23 | ~700                                      | ~-5%    |
| Jan-24 | ~800                                      | ~0%     |
| Jul-24 | ~850                                      | ~5%     |
| Jan-25 | ~850                                      | ~5%     |
| Jul-25 | ~850                                      | ~5%     |
| Jan-26 | ~900                                      | ~5%     |
</details>

Source: Bloomberg, MS

Exhibit 4: OPEC crude oil production  
![](images/7ba08ba66482c1e1e2ecbb6550cb0d9a05317f422e54c98944e1ff396aa8f63f.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | OPEC crude oil production (million barrels/day) | YoY (%) |
|---------|--------------------------------------------------|---------|
| Jan-24  | 27                                               | -5      |
| Apr-24  | 27                                               | -5      |
| Jul-24  | 27                                               | -5      |
| Oct-24  | 27                                               | -5      |
| Jan-25  | 27                                               | -5      |
| Apr-25  | 28                                               | -5      |
| Jul-25  | 29                                               | -5      |
| Oct-25  | 30                                               | -5      |
| Jan-26  | 30                                               | -5      |
| Apr-26  | 16                                               | -45     |
</details>

Source: Bloomberg, MS

Exhibit 5: 20% of crude tankers are "sanctioned", 24% of global tankers are "non-compliant"  
![](images/4fbbc58395416d7c1c056bb45ef09a35fe3ddfbb829cf06defda9c437cfead9e.jpg)

<details>
<summary>line chart</summary>

| Month    | Oil tankers | Crude tankers | Product tankers |
| -------- | ----------- | ------------- | --------------- |
| Jan-24   | 3.5         | 4.0           | 1.0             |
| Feb-24   | 3.8         | 4.2           | 1.2             |
| Mar-24   | 4.0         | 4.5           | 1.5             |
| Apr-24   | 4.2         | 4.8           | 1.8             |
| May-24   | 4.5         | 5.0           | 2.0             |
| Jun-24   | 4.8         | 5.2           | 2.2             |
| Jul-24   | 5.0         | 5.5           | 2.5             |
| Aug-24   | 5.2         | 5.8           | 2.8             |
| Sep-24   | 5.5         | 6.0           | 3.0             |
| Oct-24   | 6.0         | 7.0           | 3.5             |
| Nov-24   | 7.0         | 8.0           | 4.0             |
| Dec-24   | 8.0         | 9.0           | 4.5             |
| Jan-25   | 9.0         | 10.0          | 5.0             |
| Feb-25   | 10.0        | 11.0          | 5.5             |
| Mar-25   | 11.0        | 12.0          | 6.0             |
| Apr-25   | 12.0        | 13.0          | 6.5             |
| May-25   | 13.0        | 14.0          | 7.0             |
| Jun-25   | 14.0        | 15.0          | 7.5             |
| Jul-25   | 15.0        | 16.0          | 8.0             |
| Aug-25   | 15.5        | 16.5          | 8.5             |
| Sep-25   | 16.0        | 17.0          | 9.0             |
| Oct-25   | 16.5        | 17.5          | 9.5             |
| Nov-25   | 17.0        | 18.0          | 10.0            |
| Dec-25   | 17.5        | 18.5          | 10.5            |
| Jan-26   | 18.0        | 19.0          | 11.0            |
| Feb-26   | 18.5        | 19.5          | 11.5            |
| Mar-26   | 19.0        | 20.0          | 12.0            |
| Apr-26   | 19.5        | 20.5          | 12.5            |
| May-26   | 20.0        | 21.0          | 13.0            |
| Jun-26   | 20.5        | 21.5          | 13.5            |
</details>

Source: Clarkson, MS

Exhibit 6: China crude imports have been decreasing since April 2026  
![](images/e5a3942695da589de9030626da59e975bfc0b94ab0e6ed75e94f5ed3bf1294bd.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month   | CN: Import: Crude Petroleum Oil (Ton th) | YoY    |
|---------|------------------------------------------|--------|
| Jan-25  | ~40,000                                  | ~0%    |
| Feb-25  | ~42,000                                  | ~5%    |
| Mar-25  | ~50,000                                  | ~10%   |
| Apr-25  | ~48,000                                  | ~5%    |
| May-25  | ~47,000                                  | ~0%    |
| Jun-25  | ~49,000                                  | ~5%    |
| Jul-25  | ~48,000                                  | ~10%   |
| Aug-25  | ~49,000                                  | ~5%    |
| Sep-25  | ~48,000                                  | ~0%    |
| Oct-25  | ~49,000                                  | ~5%    |
| Nov-25  | ~50,000                                  | ~10%   |
| Dec-25  | ~55,000                                  | ~15%   |
| Jan-26  | ~50,000                                  | ~15%   |
| Feb-26  | ~48,000                                  | ~10%   |
| Mar-26  | ~49,000                                  | ~5%    |
| Apr-26  | ~38,000                                  | ~-15%  |
| May-26  | ~32,000                                  | ~-30%  |
</details>

Source: CEIC, MS

## Valuation Methodology and Risks

## COSCO SHIPPING Energy Transportation (1138.HK)

Price/book, probability-weighted 25% bull, 60% base, 15% bear. The more positive skew toward our bull case reflects VLCC's tight supply, more sanctions on the "dark fleet," and continuous OPEC+ production hikes.

Target 2027e P/B multiples:

Base - 1.9x (3.5x SD above historical mean since 2009)

Bull - 3.8x (9.1x SD above historical mean since 2009)

Bear - 1.0x (0.8x SD above historical mean since 2009)

## Risks to Upside

■ More crude oil shipping demand thanks to Hormuz reopening, or potential future licensing, or removal of sanctions on Iranian oil exports.  
■ Longer shipment distances  
■ More scrapping of aged vessels

## Risks to Downside

■ Weaker global economy leading to lower crude demand  
■ Lower-than-expected crude oil output from OPEC  
■ The return of shadow fleets

## COSCO SHIPPING Energy Transportation (600026.SS)

Price/book, probability-weighted 25% bull, 60% base, 15% bear. The more positive skew toward our bull cases reflects VLCC's tight supply, more sanctions on the "dark fleet," and continuous OPEC+ production hikes.

Target P/B multiples: 5.6x bull, 2.5x base, 1.2x bear (9.1x SD above, 2.7x SD above, and largely equivalent to historical mean since 2009)

Target A/H premiums: 45% bull, 30% base, 15% bear.

## Risks to Upside

■ More crude oil shipping demand thanks to Hormuz reopening, or potential future licensing, or removal of sanctions on Iranian oil exports.  
■ Longer shipment distances  
■ More scrapping of aged vessels

## Risks to Downside

■ Weaker global economy leading to lower crude demand  
■ Lower-than-expected crude oil output  
■ Compression of A-H premium

## China Merchants Energy Shipping Co. Ltd. (601872.SS)

Price/book, probability-weighted 25% bull, 60% base, 15% bear. The more positive skew toward our bull cases reflects VLCC's tight supply, more sanctions on the "dark fleet," and OPEC+ production hikes, despite downside risks from containers.

Target 2027e P/B multiples:

Base - 3.2x, 2.7SD above historical mean since 2009

Bull - 6.3x, 7.8SD above historical mean since 2009

Bear - 1.6x, 0.1SD above historical mean since 2009

## Risks to Upside

■ More crude oil shipping demand thanks to Hormuz reopening, or potential future licensing, or removal of sanctions on Iranian oil exports.  
■ Longer shipment distance for crude and dry bulks  
■ Potential OPEC+ production increase

## Risks to Downside

■ Weaker global economy leading to lower crude demand  
■ Lower-than-expected crude oil output from OPEC  
■ Weaker than expected infrastructure demand in China

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Su

[中间内容因长度限制已省略]

tor covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Hong Kong/China Transportation & Infrastructure

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/15/2026)</td></tr><tr><td colspan="3">Qianlei Fan, CFA</td></tr><tr><td>Air China Limited (601111.SS)</td><td>O (02/09/2026)</td><td>Rmb6.52</td></tr><tr><td>Air China Limited (0753.HK)</td><td>O (01/13/2025)</td><td>HK$4.90</td></tr><tr><td>Beijing-Shanghai High-Speed Railway (601816.SS)</td><td>O (07/03/2020)</td><td>Rmb4.87</td></tr><tr><td>BOC Aviation (2588.HK)</td><td>O (03/21/2022)</td><td>HK$79.00</td></tr><tr><td>Cathay Pacific Airways (0293.HK)</td><td>O (06/10/2026)</td><td>HK$12.17</td></tr><tr><td>China Eastern Airlines (600115.SS)</td><td>O (02/09/2026)</td><td>Rmb4.12</td></tr><tr><td>China Eastern Airlines (0670.HK)</td><td>O (01/13/2025)</td><td>HK$3.72</td></tr><tr><td>China Merchants Energy Shipping Co. Ltd. (601872.SS)</td><td>O (03/10/2020)</td><td>Rmb17.16</td></tr><tr><td>China Southern Airlines (600029.SS)</td><td>O (02/09/2026)</td><td>Rmb5.46</td></tr><tr><td>China Southern Airlines (1055.HK)</td><td>O (01/13/2025)</td><td>HK$3.90</td></tr><tr><td>COSCO SHIPPING Energy Transportation (1138.HK)</td><td>O (01/12/2023)</td><td>HK$16.95</td></tr><tr><td>COSCO SHIPPING Energy Transportation (600026.SS)</td><td>O (11/25/2025)</td><td>Rmb19.25</td></tr><tr><td>COSCO Shipping Holdings Ltd (601919.SS)</td><td>U (07/15/2024)</td><td>Rmb14.49</td></tr><tr><td>COSCO Shipping Holdings Ltd (1919.HK)</td><td>U (07/15/2024)</td><td>HK$14.35</td></tr><tr><td>J&amp;T Global Express Ltd (1519.HK)</td><td>E (08/21/2024)</td><td>HK$9.10</td></tr><tr><td>Orient Overseas (International) Ltd (0316.HK)</td><td>U (07/15/2024)</td><td>HK$132.00</td></tr><tr><td>Pacific Basin Shipping (2343.HK)</td><td>E (07/04/2025)</td><td>HK$3.09</td></tr><tr><td>S.F. Holding Co Ltd (002352.SZ)</td><td>E (09/01/2025)</td><td>Rmb33.59</td></tr><tr><td>SITC International Holdings Company (1308.HK)</td><td>E (01/12/2023)</td><td>HK$34.60</td></tr><tr><td>Spring Airlines (601021.SS)</td><td>O (08/31/2015)</td><td>Rmb48.41</td></tr><tr><td>TravelSky Technology (0696.HK)</td><td>U (01/13/2025)</td><td>HK$9.10</td></tr><tr><td>ZTO Express (ZTO.N)</td><td>O (11/21/2016)</td><td>US$22.83</td></tr><tr><td colspan="3">Tenny Song</td></tr><tr><td>Beijing Capital Int'l Airport (0694.HK)</td><td>U (09/23/2025)</td><td>HK$1.67</td></tr><tr><td>Guangzhou Baiyun Int'l Airport (600004.SS)</td><td>U (06/10/2026)</td><td>Rmb8.34</td></tr><tr><td>JD Logistics, Inc. (2618.HK)</td><td>O (03/09/2026)</td><td>HK$13.11</td></tr><tr><td>Shanghai International Airport (600009.SS)</td><td>E (09/23/2025)</td><td>Rmb24.20</td></tr><tr><td>STO Express Co Ltd (002468.SZ)</td><td>E (10/22/2024)</td><td>Rmb13.98</td></tr><tr><td>YTO Express Group Co Ltd (600233.SS)</td><td>O (09/11/2025)</td><td>Rmb17.11</td></tr><tr><td>YUNDA Holding Co Ltd (002120.SZ)</td><td>U (07/29/2020)</td><td>Rmb6.71</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
