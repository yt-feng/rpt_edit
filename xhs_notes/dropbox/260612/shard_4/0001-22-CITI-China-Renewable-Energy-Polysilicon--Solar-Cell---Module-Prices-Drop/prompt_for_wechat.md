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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Citi`。标题格式建议：`# Citi：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Citi研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
10 Jun 2026 05:02:41 ET | 12 pages

# China Renewable Energy

Polysilicon, Solar Cell & Module Prices Drop This Week; Overseas Sales Looks Better Than Local Demand

## CITI'S TAKE

China solar product prices along different parts of the supply chain generally remained at low levels last week, not far from variable production costs and with ample inventory. The market prices declined wow for n-type polysilicon, solar cell and solar modules last week. Export seems more encouraging than domestic sales with large framework agreements for overseas sales signed at an industry conference held in Shanghai recently. We are selective on the China solar sector due to excessive supply. Anti-involution measures from the government, if any, in 2026E would likely be softer than those in 2025 since China's PPI and CPI have rebounded partly resulting from higher energy prices driven by the Middle East conflict. In the China solar and ESS sector, we have Buy ratings on Sungrow and Deye.

Update from recent industry conference and space solar – The International Photovoltaic Power Generation and Smart Energy Conference & Exhibition ('SNEC') closed in Shanghai on 5 Jun 2026. At the exhibition, on-site signings were dominated by GW-scale framework memorandums of understanding for modules. Longi, Jinko, Trina Solar and JA Solar have signed new supply agreements with overseas buyers primarily from the Middle East, Africa and Southeast Asia, alongside a small number of integrated PV-storage strategic cooperation deals. Very few polysilicon and silicon wafer contracts were signed on site; transactions of these products were negotiated mostly off-site via annual long-term agreements instead, based on our understanding. In addition, two space PV industry alliances have been officially launched, led by GCL and JA Solar respectively. Leading manufacturers are developing lightweight tandem cells for satellites to tap into an entirely new application market.

N-type polysilicon prices dropped this week — The average market price of n-type grade rod-type polysilicon declined 1.3% wow to Rmb33.3/kg in the week ended 10 June 2026, and that of granular polysilicon was flat wow at Rmb33.5/kg in the same week. These market prices were not far from variable production costs. According to SMM, total polysilicon inventory at producer plants was 295k tons as of 4 Jun 2026, down 1.0% wow and remained at a high level with ample supply. Demand was not particularly high for the domestic market.

Wafer prices unchanged wow — The latest market price of n-type wafers was Rmb0.89/W for 182mm products and that of 210mm was Rmb1.19/W, both unchanged wow, despite that there were some price reductions for supply from small manufacturers. SMM estimates China wafer production volume could grow +6.3% mom to 54.3GW in June, and inventory level decreased 0.8% wow to 26.3k tonnes as of Jun 4.

## China Solar Sector

Pierre Lau, CFA $^{AC}$

+852-2501-2716

pierre.lau@citi.com

Air Ma

air.ma@citi.com

See Appendix A-1 for Analyst Certification, Important Disclosures and Research Analyst Affiliations

Not for distribution in the People's Republic of China, excluding the Hong Kong Special Administrative Region and Qualified Foreign Institutional Investors.

Both market prices of solar cell and solar module declined wow — Average solar cell price this past week was -4.6% wow to Rmb0.31/W for TOPCon products. And average solar module price this week was slightly down 0.3% wow to Rmb0.721/W for 182mm products.

Solar glass prices staying at low level with ample inventory — Average solar glass market price continued to be flat wow at Rmb9.0/m2 for 2.0mm products and flat wow at Rmb15.5/m2 for 3.2mm ones. Industry-wide average inventory period was high at 53.4 days as of Jun 4. China operational daily solar glass melting capacity was -0.1% wow to 82,550 tonnes (-17.4% yoy) as of Jun 4, according to SCI99.

Figure 1. PRC weekly polysilicon prices in the week ended Jun 10

<table><tr><td></td><td colspan="4">Mono-Si</td></tr><tr><td>182mm TOPCon</td><td>This week</td><td>WoW</td><td>MoM</td><td>YoY</td></tr><tr><td>Polysilicon (Rmb/kg)</td><td>33.3</td><td>-1.3%</td><td>-4.7%</td><td>-2.2%</td></tr><tr><td>Wafer (Rmb/pc)</td><td>0.89</td><td>0.0%</td><td>-3.3%</td><td>-2.2%</td></tr><tr><td>Cell (Rmb/W)</td><td>0.31</td><td>-4.6%</td><td>-6.1%</td><td>31.9%</td></tr><tr><td>Module (Rmb/W)</td><td>0.72</td><td>-0.3%</td><td>-0.3%</td><td>9.6%</td></tr><tr><td>Glass -2.0mm (Rmb/m2)</td><td>9.0</td><td>0.0%</td><td>-1.6%</td><td>-21.1%</td></tr></table>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 2. PRC weekly polysilicon price  
![](images/eb1ec66ceedd6e388678081262b6c05c8c75171b6d56dd959acb9f5ab129b7b6.jpg)

<details>
<summary>line chart</summary>

| Date    | mono-grade polysilicon | multi-grade polysilicon | granular silicon |
|---------|------------------------|-------------------------|------------------|
| May-22  | 250                    | -                       | -                |
| Dec-22  | 300                    | -                       | -                |
| Jul-23  | 150                    | -                       | -                |
| Feb-24  | 70                     | -                       | -                |
| Sep-24  | 40                     | -                       | -                |
| Apr-25  | 40                     | -                       | -                |
| Nov-25  | 50                     | -                       | -                |
| Jun-26  | 30                     | -                       | -                |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 3. PRC weekly wafer price  
![](images/ece833a0b94fad115cbb355a7ad1929c7f7b6dfb66f26fb58f72d7d888d004ab.jpg)

<details>
<summary>line chart</summary>

| Date    | Mono wafer M2 | Mono wafer 166mm | Mono wafer 182mm | N-type wafer 182mm |
|---------|---------------|------------------|------------------|--------------------|
| Dec-18  | 3.0           | 3.0              | 3.0              | 3.0                |
| Oct-19  | 3.0           | 3.5              | 3.0              | 3.0                |
| Aug-20  | 3.5           | 4.0              | 4.0              | 4.0                |
| Jun-21  | 5.0           | 5.5              | 6.0              | 6.0                |
| Apr-22  | 7.0           | 6.5              | 7.5              | 7.0                |
| Feb-23  | 6.0           | 6.0              | 6.5              | 6.5                |
| Dec-23  | 2.0           | 2.0              | 2.0              | 2.0                |
| Oct-24  | 1.0           | 1.0              | 1.0              | 1.0                |
| Aug-25  | 1.0           | 1.0              | 1.0              | 1.0                |
| Jun-26  | 1.0           | 1.0              | 1.0              | 1.0                |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 4. PRC weekly cell price  
![](images/60f4a720d95b8ecf089c23fc1d6a7d4da44b7ef5c71e6eef81a36c211bd171b5.jpg)

<details>
<summary>line chart</summary>

| Date    | Multi cell 18.7% | Mono cell G1 | Mono cell 182mm | Mono cell 210mm | TOPCon cell M10 |
|---------|------------------|--------------|-----------------|-----------------|-----------------|
| Dec-18  | 0.9              | 0.9          | 0.9             | 0.9             | 0.9             |
| Oct-19  | 0.8              | 1.1          | 0.9             | 0.9             | 0.9             |
| Aug-20  | 0.5              | 0.8          | 0.9             | 0.9             | 0.9             |
| Jun-21  | 0.6              | 1.0          | 1.0             | 1.0             | 1.0             |
| Apr-22  | 0.8              | 1.2          | 1.2             | 1.2             | 1.2             |
| Feb-23  | 0.9              | 1.4          | 1.4             | 1.4             | 1.4             |
| Dec-23  | 0.7              | 0.8          | 0.8             | 0.8             | 0.8             |
| Oct-24  | 0.3              | 0.3          | 0.3             | 0.3             | 0.3             |
| Aug-25  | 0.2              | 0.2          | 0.2             | 0.2             | 0.2             |
| Jun-26  | 0.3              | 0.3          | 0.3             | 0.3             | 0.3             |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

Figure 5. PRC weekly module price  
![](images/ffb438ffd5ee4b9d5cade4c40402546e063ff29a79a17328344d9eed9b00103f.jpg)

<details>
<summary>line chart</summary>

| Date    | Multi module | PERC module 166mm | PERC module 182mm | PERC module 210mm | TOPCon module 182mm | HJT module 210mm |
|---------|--------------|-------------------|-------------------|-------------------|---------------------|------------------|
| Dec-18  | 1.90         | 2.25              | 2.25              | 2.25              | 2.25                | 2.25             |
| Oct-19  | 1.70         | 1.80              | 1.80              | 1.80              | 1.80                | 1.80             |
| Aug-20  | 1.30         | 1.50              | 1.50              | 1.50              | 1.50                | 1.50             |
| Jun-21  | 1.40         | 1.60              | 1.60              | 1.60              | 1.60                | 1.60             |
| Apr-22  | 1.50         | 1.70              | 1.70              | 1.70              | 1.70                | 1.70             |
| Feb-23  | 1.60         | 1.80              | 1.80              | 1.80              | 1.80                | 1.80             |
| Dec-23  | 1.40         | 1.60              | 1.60              | 1.60              | 1.60                | 1.60             |
| Oct-24  | 1.20         | 1.40              | 1.40              | 1.40              | 1.40                | 1.40             |
| Aug-25  | 1.00         | 1.20              | 1.20              | 1.20              | 1.20                | 1.20             |
| Jun-26  | 0.80         | 1.00              | 1.00              | 1.00              | 1.00                | 1.00             |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: Citi, SMM

Figure 6. PRC weekly solar glass price  
![](images/dec32d649169035b49c8af84be4f6d8497af369997132b02cdc80fe7487c9596.jpg)

<details>
<summary>line chart</summary>

| Date    | Solar glass 3.2mm (Rmb/m2) | Solar glass 2.0 mm (Rmb/m2) |
|---------|-----------------------------|-----------------------------|
| Dec-18  | ~24.0                       | ~24.0                       |
| Oct-19  | ~27.0                       | ~25.0                       |
| Aug-20  | ~43.0                       | ~35.0                       |
| Jun-21  | ~23.0                       | ~18.0                       |
| Apr-22  | ~30.0                       | ~22.0                       |
| Feb-23  | ~28.0                       | ~19.0                       |
| Dec-23  | ~27.0                       | ~18.0                       |
| Oct-24  | ~25.0                       | ~15.0                       |
| Aug-25  | ~20.0                       | ~13.0                       |
| Jun-26  | ~15.0                       | ~10.0                       |
</details>

© 2026 Citi Inc. No redistribution without Citi's written permission.  
Source: SMM, Citi

## Ningbo Deye Technology

(605117.SS; Rmb103.7; 1; 10 Jun 26; 15:00)

## Valuation

Our target price for Deye of Rmb142.9/share is based on a DCF model, which we believe is a suitable valuation methodology as we expect sustainable growth in energy storage demand from emerging markets, from current low penetration levels. Our model incorporates our forecasts for cash flows up to 2035E and assumes a terminal growth rate of 3.0%. We apply a WACC of 8.4%, derived from a risk-free rate of 1.6%, a market risk premium of 8.9%, and an equity beta of 0.9x. Our target price equates to a 2027E P/E of 26.8x and P/B of 10.0x.

## Risks

Key downside risks that could cause Deye's shares to trade below our target price include: (i) lower-than-expected residential and C&I energy storage demand in emerging markets; (ii) fiercer-than-expected price competition among inverter peers; and (iii) higher-than-expected trade tariffs against Chinese inverter products in overseas markets.

## Sungrow Power Supply

(300274.SZ; Rmb143.55; 1; 10 Jun 26; 15:00)

## Valuation

Our target price for Sungrow shares of Rmb168.0 is based on a DCF valuation, which we believe is appropriate because it captures the long-term potential returns of the company. We factor in earnings forecasts up to 2035E and terminal growth of 4%. Our WACC for Sungrow is 9.0%, which assumes: 1) a risk-free rate of 5.2%; 2) a market risk premium of 6.8%; 3) an equity beta of 0.9x; 4) a cost-of-debt of 3.9%; 5) a target debt-to-capital ratio of 30%; and 6) a 25.0% corporate tax rate. At our DCF-based target price, Sungrow would trade at 25.5x 2026E PE and 6.1x PB.

## Risks

Key downside risks that could prevent Sungrow shares from reaching our target price include: (i) slower-than-expected solar installation that could accelerate Sungrow's PV inverter and EPC business growth; (ii) less-than-expected energy storage system demand from China and the overseas market; and (iii) intensification of overseas trade tensions that could lessen the exports of Sungrow's products.

If you are visually impaired and would like to speak to a Citi representative regarding the details of the graphics in this document, please call USA 1-888-500-5008 (TTY: 711), from outside the US +1-210-677-3788

## Appendix A-1

## ANALYST CERTIFICATION

The research analysts primarily responsible for the preparation and content of this research report are either (i) designated by “AC” in the author block or (ii) listed in bold alongside content which is attributable to that analyst. If multiple AC analysts are designated in the author block, each analyst is certifying with respect to the entire research report other than (a) content attributable to another AC certifying analyst listed in bold alongside the content and (b) views expressed solely with respect to a specific issuer which are attributable to another AC certifying analyst identified in the price charts or rating history tables for that issuer shown below. Each of these analysts certify, with respect to the sections of the report for which they are responsible: (1) that the views expressed therein accurately reflect their personal views about each issuer and security referenced and were prepared in an independent manner, including with respect to Citi Global Markets Inc. and its affiliates; and (2) no part of the research analyst's compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed by that research analyst in this report.

## IMPORTANT DISCLOSURES

Ningbo Deye Technology (605117.SS)

Ratings and Target Price History
Fundamental Research

Analyst: Air Ma

![](images/0b0c2b2c1ddf71e3997669fb78f5dca38b64d5abfdbc62185f83674096e396c3.jpg)

<details>
<summary>line chart</summary>

| Month-Year | Covered | Not covered |
| --- | --- | --- |
| Jan 2024 |  | 50 |
| Feb 2024 |  | 45 |
| Mar 2024 |  | 40 |
| Apr 2024 |  | 35 |
| May 2024 |  | 30 |
| Jun 2024 |  | 25 |
| Jul 2024 |  | 20 |
| Aug 2024 |  | 25 |
| Sep 2024 |  | 30 |
| Oct 2024 |  | 35 |
| Nov 2024 |  | 40 |
| Dec 2024 |  | 45 |
| Jan 2025 |  | 50 |
| Feb 2025 |  | 45 |
| Mar 2025 |  | 40 |
| Apr 2025 |  | 35 |
| May 2025 |  | 30 |
| Jun 2025 |  | 25 |
| Jul 2025 |  | 20 |
| Aug 2025 |  | 15 |
| Sep 2025 |  | 10 |
| Oct 2025 |  | 5 |
| Nov 2025 |  | 10 |
| Dec 2025 |  | 15 |
| Jan 2026 |  | 20 |
| Feb 2026 |  | 25 |
| Mar 2026 |  | 30 |
| Apr 2026 |  | 35 |
| May 2026 |  | 40 |
| Jun 2026 |  | 45 |
| Jul 2026 |  | 50 |
| Aug 2026 |  | 55 |
| Sep 2026 |  | 60 |
| Oct 2026 |  | 65 |
| Nov 2026 |  | 70 |
| Dec 2026 |  | 75 |
| Jan 2027 |  | 80 |
| Feb 2027 |  | 85 |
| Mar 2027 |  | 90 |
| Apr 2027 |  | 95 |
| May 2027 |  | 100 |
| Jun 2027 |  | 110 |
| Jul 2027 |  | 115 |
| Aug 2027 |  | 118 |
| Sep 2027 |  | 119 |
| Oct 2027 |  | 118 |
| Nov 2027 |  | 116 |
| Dec 2027 |  | 114 |
| Jan 2028 |  | 113 |
| Feb 2028 |  | 111 |
| Mar 2028 |  | 110 |
| Apr 2028 |  | 111 |
| May 2028 |  | 113 |
| Jun 2028 |  | 114 |
| Jul 2028 |  | 115 |
| Aug 2028 |  | 116 |
| Sep 2028 |  | 117 |
| Oct 2028 |  | 118 |
| Nov 2028 |  |  |
| Dec 2028 |  |  |
| Jan 2029 |  |  |
| Feb 2029 |  |  |
| Mar 2029 |  |  |
| Apr 2029 |  |  |
| May 2029 |  |  |
| Jun 2029 |  |  |
| Jul 2029 |  |  |
| Aug 2029 |  |  |
| Sep 2029 |  |  |
| Oct 2029 |  |  |
| Nov 2029 |  |  |
| Dec 2029 |  |  |
| Jan 2030 |  |  |
| Feb 2030 |  |  |
| Mar 2030 |  |  |
| Apr 2030 |  |  |
| May 2030 |  |  |
| Jun 2030 |  |  |
| Jul 2030 |  |  |
| Aug 2030 |  |  |
| Sep 2030 |  |  |
| Oct 2030 |  |  |
| Nov 2030 |  |  |
| Dec 2030 |  |  |
| Jan 2031 |  |  |
| Feb 2031 |  |  |
| Mar 2031 |  |  |
| Apr 2031 |  |  |
| May 2031 |  |  |
| Jun 2031 |  |  |
| Jul 2031 |  |  |
| Aug 2031 |  |  |
| Sep 2031 |  |  |
| Oct 2031 |  |  |
| Nov 2031 |  |  |
| Dec 2031 |  |  |
| Jan 2032 |  |  |
| Feb 2032 |  |  |
| Mar 2032 |  |  |
| Apr 2032 |  |  |
| May 2033 |  |  |
| Jun 2033 |  |  |
| Jul 2033 |  |  |
| Aug 2033 |  |  |
| Sep 2033 |  |  |
| Oct 2033 |  |  |
| Nov 2033 |  |  |
| Dec 2033 |  |  |
| Jan 2034 |  |  |
| Feb 2034 |  |  |
| Mar 2034 |  |  |
| Apr 2034 |  |  |
| May 2034 |  |  |
| Jun 2034 |  |  |
| Jul 2034 |  |  |
| Aug 2034 |  |  |
| Sep 2034 |  |  |
| Oct 2034 |  |  |
| Nov 2034 |  |  |
| Dec 2034 |  |  |
| Jan 2035 |  |  |
| Feb 2035 |  |  |
| Mar 2035 |  |  |
| Apr 2035 |  |  |
| May 2035 |  |  |
| Jun 2035 |  |  |
| Jul 2035 |  |  |
| Aug 2035 |  |  |
| Sep 2035 |  |  |
| Oct 2035 |  |  |
| Nov 2035 |  |  |
| Dec 2035 |  |  |
| Jan 2036 |  |  |
| Feb 2036 |  |  |
| Mar 2036 |  |  |
| Apr 2036 |  |  |
| May 2036 |  |  |
| Jun 2036 |  |  |
| Jul 2036 |  |  |
| Aug 2036 |  |  |
| Sep 2036 |  |  |
| Oct 2036 |  |  |
| Nov 2036 |  |  |
</details>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></tr><tr><td>1</td><td>11-Jul-25 15:08:17</td><td>*1</td><td>*48.57</td><td>39.34</td></tr><tr><td>2</td><td>28-Aug-25 12:58:00</td><td>1</td><td>*50.71</td><td>44.42</td></tr><tr><td>3</td><td>22-Sep-25 03:45:06</td><td>1</td><td>*55.86</td><td>49.53</td></tr></table>

<table><tr><td colspan="2">Date</td><td>Rating</td><td>Target Price</td><td>Closing Price</td></t

[中间内容因长度限制已省略]

lar investor. Accordingly, investors should, before acting on the advice, consider the appropriateness of the advice, having regard to their objectives, financial situation and needs. Prior to acquiring any financial product, it is the client's responsibility to obtain the relevant offer document for the product and consider it before making a decision as to whether to purchase the product.

Card Insights. Where this report references Card Insights data, Card Insights consists of selected data from a subset of Citi's proprietary credit card transactions. Such data has undergone rigorous security protocols to keep all customer information confidential and secure; the data is highly aggregated and anonymized so that all unique customer identifiable information is removed from the data prior to receipt by the report's author or distribution to external parties. This data should be considered in the context of other economic indicators and publicly available information. Further, the selected data represents only a subset of Citi's proprietary credit card transactions due to the selection methodology or other limitations and should not be considered as indicative or predictive of the past or future financial performance of Citi or its credit card business.

Citi product may source data from dataCentral. dataCentral is a Citi proprietary database, which includes the Firm's estimates, data from company reports and feeds from LSEG Data & Analytics. The source for all referenced prices, unless otherwise stated, is DataCentral. Past performance is not a guarantee or reliable indicator of future results. Forecasts are not a guarantee or reliable indicator of future performance. The printed and printable version of the research report may not include all the information <(e.g. certain financial summary information and comparable company data) that is linked to the online version available on the Firm's proprietary electronic distribution platforms.

Where included in this report, MSCI sourced information is the exclusive property of MS Capital International Inc. (MSCI). Without prior written permission of MSCI, this information and any other MSCI intellectual property may not be reproduced, redisseminated or used to create any financial products, including any indices. This information is provided on an "as is" basis. The user assumes the entire risk of any use made of this information. MSCI, its affiliates and any third party involved in, or related to, computing or compiling the information hereby expressly disclaim all warranties of originality, accuracy, completeness, merchantability or fitness for a particular purpose with respect to any of this information. Without limiting any of the foregoing, in no event shall MSCI, any of its affiliates or any third party involved in, or related to, computing or compiling the information have any liability for any damages of any kind. MSCI, MS Capital International and the MSCI indexes are services marks of MSCI and its affiliates. Where data is attributed to Morningstar that data is © 2026 Morningstar, Inc. All Rights Reserved. That information: (1) is proprietary to Morningstar and/or its content providers; (2) may not be copied or distributed; and (3) is not warranted to be accurate, complete or timely. Neither Morningstar nor its content providers are responsible for any damages or losses arising from any use of this information.

The Firm accepts no liability whatsoever for the actions of third parties. The Product may provide the addresses of, or contain hyperlinks to, websites. Except to the extent to which the Product refers to website material of the Firm, the Firm has not reviewed the linked site. Equally, except to the extent to which the Product refers to website material of the Firm, the Firm takes no responsibility for, and makes no representations or warranties whatsoever as to, the data and information contained therein. Such address or hyperlink (including addresses or hyperlinks to website material of the Firm) is provided solely for your convenience and information and the content of the linked site does not in any way form part of this document. Accessing such website or following such link through the Product or the website of the Firm shall be at your own risk and the Firm shall have no liability arising out of, or in connection with, any such referenced website.

© 2026 Citi Global Markets Inc. Citi is a division of Citi Global Markets Inc. Citi and Citi and Arc Design are trademarks and service marks of Citi Inc. and its affiliates and are used and registered throughout the world. All rights reserved. The research data in this report are not intended to be used for the purpose of (a) determining the price of or amounts due in respect of (or to value) one or more financial products or instruments and/or (b) measuring or comparing the performance of, or defining the asset allocation of a financial product, a portfolio of financial instruments, or a collective investment undertaking, and any such use is strictly prohibited without the prior written consent of Citi. Any unauthorized use, duplication, redistribution or disclosure of this report (the “Product”), including, but not limited to, redistribution of the Product by electronic mail, posting of the Product on a website or page, and/or providing to a third party a link to the Product, is prohibited by law and will result in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.

ADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST
"""
