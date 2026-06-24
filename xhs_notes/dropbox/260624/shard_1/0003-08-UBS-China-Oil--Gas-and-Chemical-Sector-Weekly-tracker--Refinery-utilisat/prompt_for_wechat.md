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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`UBS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份UBS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Oil, Gas and Chemical Sector Weekly tracker: Refinery utilisation and crude inventory still declining; eyes on fluorochemicals

## Refining: Teapot refineries' utilisation declined to 45.74%

SOE refineries' average utilisation edged up 0.23ppt WoW to 67.41% last week. Utilisation at teapot refineries continued to decline by 2.9ppt WoW to 45.74%. China's total crude throughput fell 128 kb/d WoW to 12,321kb/d by last week. As per Kpler data, overall China crude inventory has been declining since early June and is at 1,268MMbbl as of 22 June.

## Chemicals: Polyester filament utilisation declined 2ppt/15ppt WoW/YoY

Ethylene: Naphtha-based ethylene utilisation was broadly flat WoW at 76%, while MTO route utilisation declined 5ppt/11ppt WoW/YoY to 78%. Polyolefins: PE utilisation was flat WoW, at 80% (down 1ppt YoY), while PP utilisation decreased 1ppt/15ppt WoW/YoY to 63%. PDH utilisation increased 3ppt WoW to 66%. PVC utilisation increased 1ppt WoW to 70% (down 9ppt YoY). Aromatics chain: PX utilisation was flat WoW, at 77% (down 8ppt YoY), while PTA utilisation increased 4ppt WoW to 69% (down 13ppt YoY). Polyester filament utilisation declined 2ppt/15ppt WoW/YoY to 74%. TDI utilisation rose 7ppt WoW to 71%, while MDI utilisation declined 1ppt WoW to 82%. TiO2 utilisation was flat WoW, at 80%.

## PP/PE/silicone DMC inventory fell WoW

According to sample inventory data, PP inventory decreased 2%/26% WoW/YoY to 452kt. PE inventory declined 1% WoW and 5% YoY to 476kt. PVC inventory increased 1% WoW but declined 21% YoY to 415kt. TiO2 inventory rose 8% WoW but declined 43% YoY to 181kt. Polyester filament inventory rose 10%/112% WoW/YoY. Silicone DMC inventory declined 4% WoW and 21% YoY to 40kt.

## Stock picks

We prefer beneficiaries of easing Middle East tension, including: 1) companies impacted by raw material prices, such as polyester filament (Tongkun; Buy) and phosphate chemicals; and 2) chemicals leaders with re-rating potential (Wanhua and Yangnong; both Buy). We published a fluorochemical sector note, highlighting applications of fluorochemicals in semiconductors and data centers. We expect fast growth in the AI-related applications of fluorochemicals, amidst the higher compute power demand and the iteration of material systems induced by AI developments. Currently, fluorochemical material suppliers are trading at a notable discount to electronic chemical material firms. We think the market has yet to fully price in the growth opportunities that AI brings to fluorochemical materials and see further re-rating potential for select fluorochemical firms poised to ride the AI tailwinds.

## Equities

China
Chemicals

Amily Guo
Analyst
amily.guo@ubs.com
+86-105-832 8845

Cheryl Wen
Analyst
S1460525030002
cheryl.wen@ubs.com
+86-21-3866 8916

Richard Li
Analyst
S1460121090003
richard-ze.li@ubs.com
+86-21-3866 8802

Nayoung Kim
Analyst
nayoung.kim@ubs.com
+44-20-7568 4010

Jay LIN

Analyst

S1460525070001

jay.lin@ubs.com

+86-105-832 8044

Crude inventory and refinery utilisation
Figure 1: China crude oil inventory  
![](images/9916d015a801689ce22dd6def96568266592911a281af6d2ec8375eaf8269d27.jpg)  
Source: Kpler, UBS

Figure 2: Utilisation of China SOE/teapot refiners  
![](images/57295da90fadd9a252811225ee82f5d5d9db431878d00e1ec2dcbc9d71ac4e75.jpg)  
Source: SCI99, Wind

Chemical utilisation  
Figure 3: China ethylene (naphtha cracking) capacity utilisation  
![](images/1bc7fde7d3565a35cb7cb20d4ff062b0f5a48121fdf5408142fb76f4485bb22f.jpg)  
Source: Wind, Oilchem

Figure 4: China ethylene (MTO) capacity utilisation  
![](images/a79509862500bd24d9c5d165f2670159ec9641ac2edf037fd22d9d10593cc6eb.jpg)  
Source: Wind, Oilchem

Figure 5: China PE capacity utilisation  
![](images/83bf3adcc12e3dcf5caf9465b3e535a5b054bfd5d17068c731e514b95503a0d3.jpg)  
Source: Baiinfo

Figure 6: China PP capacity utilisation  
![](images/f07ad28b8d4332f3ecc45e5e87e899dc2a1ca394fdaffd5f0b8ae5eee5b1a8c1.jpg)  
Source: Baiinfo

Figure 7: China PVC capacity utilisation  
![](images/4307f7102fd3fa71631e082214baba173144ce6ba8e7e93e27dbe63b69713d7b.jpg)  
Source: Baiinfo

Figure 8: China PDH capacity utilisation  
![](images/f70bcf881892f3aa6834d0da60aca4e7527e7c24eda63b95cac18ae9f54fc8eb.jpg)  
Source: Baiinfo

Figure 9: China PX capacity utilisation  
![](images/410c175d126c2eba65ced3be465c67d1422c773aeec5a6a591396dddde52fe96.jpg)  
Source: Baiinfo

Figure 10: China PTA capacity utilisation  
![](images/bc56b5a529dc6e4c0586cc9f97cb713b08bb54d5c2b93ee6a344aded17589a3e.jpg)  
Source: Baiinfo

Figure 11: China Polyester filament capacity utilisation  
![](images/80ad43bdd7c67f0c45e7bc068138bf31eb8b7126d4fc5b0ee77ecaa12c80b7d4.jpg)  
Source: Baiinfo

Figure 12: China MDI capacity utilisation  
![](images/06a2547e5328b1ab4160d108f15c2ff317f5e7a23471a48556ec7a3ad56854b7.jpg)  
Source: Baiinfo

Figure 13: China TDI capacity utilisation  
![](images/dbace4d3458c2fd372b98034ba7608e930ac3b19d301a2ee921f0cc7e13955cf.jpg)  
Source: Baiinfo

Figure 14: China TiO2 capacity utilisation  
![](images/4e0e64ccc7555522aa6ff7354c3a8fb94a9caad8f340d8d3b0638451b1547bd9.jpg)  
Source: Baiinfo

## Inventory

Figure 15: Sample factories' inventory of PP  
![](images/b0da4fefe037c69124e9a4340b89351c74f44c84c952ea6db0025121c6781319.jpg)  
Source: Baiinfo

Figure 16: Sample factories' inventory of PE  
![](images/be6b95cf5190b203c47c5af8537aee3a833d9928e21a0a1c2d0cb8c3c857a4a3.jpg)  
Source: Baiinfo

Figure 17: Sample factories' inventory of PVC  
![](images/c15fbfe5be14c84f8a32c119622b987463983d217921c74da8c6955b461f5614.jpg)  
Source: Baiinfo

Figure 18: Sample factories' inventory of TiO2  
![](images/9f4132df174358151cea45f27f9e669f56e34af319080d39bb5bb02f6cbbeb02.jpg)  
Source: Baiinfo

Figure 19: Sample factories' inventory of polyester filament  
![](images/d09d64bed4a0f0ac917e620e3fea09dbc2efc5eea6f8aecf6805307e6b6924d8.jpg)  
Source: Baiinfo

Figure 20: Sample factories' inventory of silicone DMC  
![](images/b7e69f2c516366d3af93be6594d2ff2380c3720d65fb258bb9782a63b8b8dc5d.jpg)  
Source: Baiinfo

## Valuation Method and Risk Statement

O&G sector: We believe risks include: 1) declines or fluctuations in crude oil prices; 2) disappointing reserves and productivity enhancements; and 3) declining prices of major petrochemical products.

Chemicals sector: We believe risks include: 1) large earnings fluctuations due to changes in international oil prices; 2) risks to demand for chemicals due to macro uncertainty; and 3) new capacity coming online faster than expected, leading to sharp weakening of chemical fundamentals.

Wanhua Chemical: We base our price target on a DCF methodology. We believe key downside risks include: 1) an economic downturn leading to declining MDI demand; 2) a price war among MDI leaders during capacity expansion leading to significant decreases in MDI prices; 3) sluggish petrochemical fundamentals in China, causing Wanhua's petrochemical profit to be lower than expected; 4) other leaders achieving MDI technological breakthroughs; and 5) uncertainties around the development of the new materials segment, such as know-how, policies and the investment environment.

We value Yangnong Chemical on DCF. Key downside risks include: 1) new technologies or new offerings could emerge as pesticide makers continue to iterate on products, potentially disrupting the existing market landscape; 2) the pesticide sector is strongly affected by policies, and product bans, etc. could negatively impact earnings; 3) Yangnong is exposed to FX risk given its high mix of export revenue; and 4) pesticide industry dynamics could change due to frequent consolidation/spin-offs.

We use P/BV versus ROE methodology to value Tongkun. The company's key risks include: 1) polyester demand is vulnerable to macro uncertainty; 2) continued deterioration of PTA fundamentals due to new capacity; 3) uncertainty related to the launch of new refinery capacity due to strict policy and regulation; and 4) tighter policies for environmental protection and carbon emissions.

## Required Disclosures

This document has been prepared by UBS Asia Limited, an affiliate of UBS AG. UBS AG, its subsidiaries, branches and affiliates, including former CS AG and its subsidiaries, branches and affiliates are referred to herein as "UBS".

For information on the ways in which UBS manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures. Unless otherwise indicated, information and data in this report are based on company disclosures including but not limited to annual, interim, quarterly reports and other company announcements. The figures contained in performance charts refer to the past; past performance is not a reliable indicator of future results. Additional information will be made available upon request. UBS Co. Limited is licensed to conduct securities investment consultancy businesses by the China Securities Regulatory Commission. UBS acts or may act as principal in the debt securities (or in related derivatives) that may be the subject of this report. This recommendation was finalized on: 22 June 2026 01:45 PM GMT. UBS has designated certain UBS Global Research department members as Derivatives Research Analysts where those department members publish research principally on the analysis of the price or market for a derivative, and provide information reasonably sufficient upon which to base a decision to enter into a derivatives transaction. Where Derivatives Research Analysts co-author research reports with Equity Research Analysts or Economists, the Derivatives Research Analyst is responsible for the derivatives investment views, forecasts, and/or recommendations. Quantitative Research Review: UBS Global Research publishes a quantitative assessment of its analysts' responses to certain questions about the likelihood of an occurrence of a number of short term factors in a product known as the 'Quantitative Research Review'. Views contained in this assessment on a particular stock reflect only the views on those short term factors which are a different timeframe to the 12-month timeframe reflected in any equity rating set out in this note. For the latest responses, please see the Quantitative Research Review Addendum at the back of this report, where applicable. For previous responses please make reference to (i) previous UBS Global Research reports; and (ii) where no applicable research report was published that month, the Quantitative Research Review which can be found at https://neo.ubs.com/quantitative, or contact your UBS sales representative for access to the report or the Quantitative Research Team on ubs-quant-answers@ubs.com. A consolidated report which contains all responses is also available and again you should contact your UBS sales representative for details and pricing or the Quantitative Research team on the email above.

## Analyst Certification:

Each research analyst primarily responsible for the content of this research report, in whole or in part, certifies that with respect to each security or issuer that the analyst covered in this report: (1) all of the views expressed accurately reflect his or her personal views about those securities or issuers and were prepared in an independent manner, including with respect to UBS, and (2) no part of his or her compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in the research report.

UBS Global Research: Global Equity Rating Definitions

<table><tr><td>12-Month Rating</td><td>Definition</td><td>Coverage $^{1}$ </td><td>IB Services $^{2}$ </td></tr><tr><td>Buy</td><td>FSR is &gt; 6% above the MRA.</td><td>54%</td><td>24%</td></tr><tr><td>Neutral</td><td>FSR is between -6% and 6% of the MRA.</td><td>40%</td><td>21%</td></tr><tr><td>Sell</td><td>FSR is &gt; 6% below the MRA.</td><td>6%</td><td>21%</td></tr></table>

Source: UBS. Rating allocations are as of 31 March 2026.  
1: Percentage of companies under coverage globally within the 12-month rating category.

2: Percentage of companies within the 12-month rating category for which investment banking (IB) services were provided within the past 12 months.

KEY DEFINITIONS: Forecast Stock Return (FSR) is defined as expected percentage price appreciation plus gross dividend yield over the next 12 months. In some cases, this yield may be based on accrued dividends. Market Return Assumption (MRA) is defined as the one-year local market interest rate plus 5% (a proxy for, and not a forecast of, the equity risk premium). Under Review (UR) Stocks may be flagged as UR by the analyst, indicating that the stock's price target and/or rating are subject to possible change in the near term, usually in response to an event that may affect the investment case or valuation. Equity Price Targets have an investment horizon of 12 months.

EXCEPTIONS AND SPECIAL CASES:UK and European Investment Fund ratings and definitions are: Buy: Positive on factors such as structure, management, performance record, discount; Neutral: Neutral on factors such as structure, management, performance record, discount; Sell: Negative on factors such as structure, management, performance record, discount. Core Banding Exceptions (CBE): Exceptions to the standard +/-6% bands may be granted by the Investment Review Consultation (IRC). Factors considered by the IRC include the stock's volatility and the credit spread of the respective company's debt. As a result, stocks deemed to be very high or low risk may be subject to higher or lower bands as they relate to the rating. When such exceptions apply, they will be identified in the Company Disclosures table in the relevant research piece.

Research analysts contributing to this report who are employed by any non-US affiliate of UBS LLC are not registered/qualified as research analysts with FINRA. Such analysts may not be associated persons of UBS LLC and therefore are not subject to the FINRA restrictions on communications with a subject company, public appearances, and trading securities held by a research analyst account. The name of each affiliate and analyst employed by that affiliate contributing to this report, if any, follows.
UBS AG London Branch: Nayoung Kim. UBS Co. Limited: Amily Guo, Cheryl Wen, Jay LIN, Richard Li.

Company Disclosures

<table><tr><td>Company Name</td><td>Reuters</td><td>12-month rating</td><td>Price</td><td>Price date</td></tr><tr><td>Jiangsu Yangnong Chemical</td><td>600486.SS</td><td>Buy</td><td>Rmb56.84</td><td>22 Jun 2026</td></tr><tr><td>Tongkun Group</td><td>601233.SS</td><td>Buy</td><td>Rmb23.09</td><td>22 Jun 2026</td></tr><tr><td>Wanhua Chemical Group</td><td>600309.SS</td><td>Buy</td><td>Rmb74.30</td><td>22 Jun 2026</td></tr></table>

Source: UBS Global Research; LSEG Eikon. All prices as of local market close. Ratings in this table are the most current published ratings prior to this report. They may be more recent than the stock pricing date.

Unless otherwise indicated, please refer to the Valuation and Risk sections within the body of this report. For a complete set of disclosure statements associated with the companies discussed in this report, including information on valuation and risk, please contact UBS LLC, 11 Madison Avenue, New York, NY 10010, USA, Attention: Investment Research.

Jiangsu Yangnong Chemical (Rmb)  
![](images/c59171b221a6b28e680ae025da9efd5b650a24a083dc8c33263e000926b56cb7.jpg)

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-03-22</td><td>78.50</td><td>108.00</td><td>Buy</td></tr><tr><td>2023-10-24</td><td>63.52</td><td>99.00</td><td>Buy</td></tr><tr><td>2024-03-26</td><td>52.81</td><td>90.00</td><td>Buy</td></tr><tr><td>2024-08-27</td><td>48.52</td><td>82.00</td><td>Buy</td></tr><tr><td>2025-03-25</td><td>54.00</td><td>75.00</td><td>Buy</td></tr><tr><td>2025-08-22</td><td>69.88</td><td>82.00</td><td>Buy</td></tr><tr><td>2026-02-02</td><td>72.42</td><td>108.00</td><td>Buy</td></tr><tr><td>2026-03-31</td><td>75.00</td><td>103.00</td><td>Buy</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 22-Jun-2026. All prices as of local market close. Ratings as of date shown.

![](images/895e221946c36a27aecfbdcbfad2bdcaf70e81805259a3d3bb167d377d6d6d3e.jpg)

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-03-22</td><td>14.01</td><td>20.40</td><td>Buy</td></tr><tr><td>2023-04-29</td><td>12.90</td><td>18.50</td><td>Buy</td></tr><tr><td>2023-08-30</td><td>14.93</td><td>20.00</td><td>Buy</td></tr><tr><td>2023-10-27</td><td>14.01</td><td>19.00</td><td>Buy</td></tr><tr><td>2024-04-29</td><td>13.37</td><td>19.20</td><td>Buy</td></tr><tr><td>2024-06-05</td><td>15.08</td><td>20.10</td><td>Buy</td></tr><tr><td>2024-08-29</td><td>11.71</td><td>18.90</td><td>Buy</td></tr><tr><td>2024-10-31</td><td>11.78</td><td>16.90</td><td>Buy</td></tr><tr><td>2025-04-30</td><td>10.88</td><td>15.60</td><td>Buy</td></tr><tr><td>2025-08-28</td><td>14.42</td><td>17.70</td><td>Buy</td></tr><tr><td>2025-10-30</td><td>14.42</td><td>18.60</td><td>Buy</td></tr><tr><td>2025-12-26</td><td>16.85</td><td>20.90</td><td>Buy</td></tr><tr><td>2026-02-02</td><td>20.09</td><td>30.80</td><td>Buy</td></tr><tr><td>2026-04-29</td><td>23.06</td><td>32.00</td><td>Buy</td></tr></table>

Source: UBS Global Research; LSEG Eikon as of 22-Jun-2026. All prices as of local market close. Ratings as of date shown.

Wanhua Chemical Group (Rmb)  
![](images/0e4d25b50c5eccaded5cf2646a4ec903947653b4315599dff529e488116f2040.jpg)

<table><tr><td>Date</td><td>Stock Price (Rmb)</td><td>Price Target (Rmb)</td><td>Rating</td></tr><tr><td>2023-03-22</td><td>97.85</td><td>142.00</td><td>Buy</td></tr><tr><td>2023-07-28</td><td>95.71</td><td>143.00</td><td>Buy</td></tr><tr><td>2023-10-13</td><td>87.08</td><td>130.00</td><td>Buy</td></tr><tr><td>2024-03-19</td><td>78.58</td><td>125.00</td><td>Buy</td></tr><tr><td>2024-08-13</td><td>73.01</td><td>116.00</td><td>Buy</td></tr><tr><td>2024-10-29</td><td>76.84</td><td>110.00</td><td>Buy</td></tr><tr><td>2025-02-27</td><td>68.92</td><td>100.00</td><td>Buy</td></tr><tr><td>2025-04-15</td><td>56.26</td><td>87.00</td><td>Buy</td></tr><tr><td>2025-08-12</td><td>62.90</td><td>86.00</td><td>Buy</td></tr><tr><td>2025-10-24</td><td>61.45</td

[中间内容因长度限制已省略]

lated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A.' de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with “Risk information” and “Important Information About Sustainable Investing Strategies” sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
