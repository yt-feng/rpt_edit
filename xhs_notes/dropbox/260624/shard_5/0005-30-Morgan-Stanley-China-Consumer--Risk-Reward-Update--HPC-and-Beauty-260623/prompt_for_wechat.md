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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
June 23, 2026 12:31 AM GMT

China Consumer | Asia Pacific

# Risk/Reward Update: HPC and Beauty

This report covers our changes for Hengan, C&S Paper, and Shanghai Jahwa.

Hengan (1044.HK; EW): Tissue should remain Hengan's key growth driver, supported by volume growth and share gains, but revenue growth is likely to stay moderate due to ASP pressure from online and new retail channels. Tissue margin should be stable in 2026 due to favorable pulp prices, while sanitary napkins and diapers are still under pressure from intense competition and weak demand. Overall margins may edge down as the company invests more in branding and channel expansion. Despite lukewarm earnings trends and a lack of upside catalysts in the near term, Hengan's commitment to Rmb1.4+/share annual payout, equivalent to \~6% dividend yield now, supports its share price, leading to our EW rating.

C&S Paper (002511.SZ; UW): C&S Paper's revenue growth should remain mostly volume- and share-gain-driven, as smaller players exit, but pricing power remains limited. Online and new retail channels should support volume growth, but higher promotion and sharper pricing may continue to dilute ASP and limit margin upside. Gross margin should stay broadly stable, helped by product premiumization and efficiency gains, though pulp costs and channel competition constrain further GPM upside. Earnings recovery is visible but still moderate, as operating leverage is limited by continued investment in branding, e-commerce, and new retail. We cut earnings estimates by 20%/27% for 2026/27 to reflect slower-than-expected earnings recovery. Given its still-demanding valuation (trading at 24x 2026E P/E) with limited pricing power, low ROE and only modest margin upside, risk-reward is not compelling, and we remain UW.

Shanghai Jahwa (600315.SS; UW): Jahwa is back to growth, driven by online strength and beauty segment recovery, while the recovery remains largely brand-investment led. Beauty brands such as Herborist and Dr. Yu should remain the key growth drivers, while Liushen's offline business is expected to stabilize from the pressure last year. The rising online and Douyin mix is strategically positive, but it also requires continued investment in content, traffic and brand building, limiting near-term operating leverage. Gross margin should improve gradually with a better category mix, but selling expenses are likely to stay high as the company rebuilds brand equity. We cut earnings estimates by 35%/39% for 2026/27 to reflect slower-than-expected earnings recovery, as selling expenses are likely to stay high. With the stock trading at over 35x 2026E P/E, valuation looks demanding relative to limited profit visibility, so we remain UW.

MS ASIA LIMITED+

Dustin Wei

Equity Analyst

Dustin.Wei@morganstanley.com +852 2239-7823

Research Associate

Jenny.Yu1@morganstanley.com +852 3963-1925

Lillian Lou

Equity Analyst

Lillian.Lou@morganstanley.com +852 2848-6502

Asia Summer School 2026

![](images/a8debeaf80ff54c3232ef94ad3bf8a49c6301f781a2bf6f3250b9f61d6dc1000.jpg)

<table><tr><td colspan="3">CHINA/HONG KONG CONSUMER</td></tr><tr><td>Asia Pacific Industry View</td><td></td><td>In-Line</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>C&amp;S Paper Co Ltd (002511.SZ)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb5.60</td><td>Rmb5.70</td></tr><tr><td>Shanghai Jahwa United Co. Ltd. (600315.SS)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>Rmb16.00</td><td>Rmb14.00</td></tr><tr><td>Hengan International Group (1044.HK)</td><td>From</td><td>To</td></tr><tr><td>Price Target</td><td>HK$24.00</td><td>HK$23.00</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## What's Changed

Exhibit 1: What's changed - Price targets and ratings

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="2">PT</td><td rowspan="2">Last closing</td><td rowspan="2">Up/downside to PT (%)</td><td rowspan="2">Currency</td></tr><tr><td>New</td><td>Old</td></tr><tr><td>Hengan</td><td>1044.HK</td><td>EW</td><td>23</td><td>24</td><td>23</td><td>-0.9%</td><td>HKD</td></tr><tr><td>C&amp;S Paper</td><td>002511.SZ</td><td>UW</td><td>5.7</td><td>5.6</td><td>7</td><td>-16.5%</td><td>Rmb</td></tr><tr><td>Shanghai Jahwa</td><td>600315.SS</td><td>UW</td><td>14</td><td>16</td><td>18</td><td>-20.4%</td><td>Rmb</td></tr></table>

Source: MS estimates

Exhibit 2: What's changed - Revenue and net profit estimates (Rmb mn)

<table><tr><td rowspan="3">Company</td><td rowspan="3">Ticker</td><td rowspan="3">Currency</td><td colspan="6">Revenue</td><td colspan="6">Net profit</td></tr><tr><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2026E</td><td colspan="3">2027E</td></tr><tr><td>New</td><td>Old</td><td>% chg</td><td>New</td><td>Old</td><td>% chg</td><td>New</td><td>Old</td><td>% chg</td><td>New</td><td>Old</td><td>% chg</td></tr><tr><td>Hengan</td><td>1044.HK</td><td>Rmb</td><td>23,967</td><td>23,952</td><td>0%</td><td>24,695</td><td>24,549</td><td>1%</td><td>2,449</td><td>2,393</td><td>2%</td><td>2,491</td><td>2,438</td><td>2%</td></tr><tr><td>C&amp;S Paper</td><td>002511.SZ</td><td>Rmb</td><td>9,646</td><td>9,842</td><td>-2%</td><td>10,410</td><td>10,334</td><td>1%</td><td>365</td><td>456</td><td>-20%</td><td>436</td><td>593</td><td>-27%</td></tr><tr><td>Shanghai Jahwa</td><td>600315.SS</td><td>Rmb</td><td>7,031</td><td>6,725</td><td>5%</td><td>7,735</td><td>7,371</td><td>5%</td><td>330</td><td>505</td><td>-35%</td><td>385</td><td>628</td><td>-39%</td></tr></table>

Source: MS estimates

## Hengan (EW, New Price Target HK\$23.0)

\- Tissue should remain the key growth driver, but quality of growth is mixed. We expect tissue sales to grow 5.0%/3.5%/4.0% in 2026/27/28. The driver is mainly volume growth, as some small and mid-sized manufacturers exit the market and Hengan, as a leading player, should continue to gain share. However, the rising mix of online and new retail channels is likely to remain a drag on ASP. As a result, tissue revenue growth should stay at MSD% rather than accelerate meaningfully, even though volume growth remains healthy.

\- Tissue GPM should stay broadly stable, but 2025's strong margin improvement is unlikely to repeat. Tissue GPM improved to $23.0\%$ in 2025, helped by relatively low pulp prices, less promotional pressure and better product mix. Looking into 2026, pulp cost is still manageable but has seen small increases. We therefore do not expect a major margin squeeze, but also do not assume further meaningful upside. We forecast tissue GPM to be $22.5\% / 23.0\% / 23.0\%$ in 2026/27/28.

\- Sanitary napkins remain the most challenging part of the business. Although hygiene products showed some improvement in 2H25, we think this was more due to a low base rather than easing competition. Competition in sanitary napkins remains intense, with both domestic and overseas brands still using aggressive promotions to gain share. We therefore think flat sanitary napkin sales in 2026 would already be a decent outcome. We estimate sales will be down 0.5% y/y in 2026, followed by only 1.5%/2.0% growth in 2027/28. Margin-wise, sanitary napkin GPM above 60% in 2025 was high, and we expect it to normalize to around 59-60% in 2026-28.

\- Diapers are also under pressure, despite mix upgrade. Premium QMo and adult diapers should still grow, but growth has slowed. Anerle remains in decline due to weak demand and competition. ASP may improve as the mix shifts toward higher-end and adult products, but volume decline is likely to more than offset ASP improvement. We expect diaper sales to decline 1.0% in 2026, stay flattish in 2027 and grow only 1.0% in 2028. Overall, diapers should not be a major earnings driver in the near term.

\- Operating margin is likely to edge down as the company invests more in channels and branding. Although gross margin should remain in a stable range, Hengan is likely to increase spending on brand investment, online channels, and new retail expansion. These channels can help defend market share and reach younger consumers, but they also bring additional promotional and platform costs. We forecast the opex ratio to rise from 23.2% in 2025 to 23.3%/23.5%/23.4% in 2026/27/28, driving OPM down from 10.6% in 2025 to around 9.5-9.6% in 2026-28.

\- Net, earnings in 2026 are still under pressure. We now forecast net profit to decline in 2026, before only a modest recovery in 2027/28. The 2026 earnings decline is mainly driven by lower GPM and a higher opex ratio. NPM is likely to step down from $11.0\%$ in 2025 and stay at $10.1 - 10.2\%$ in 2026-28. We think Hengan's earnings are still relatively defensive, supported by its strong tissue franchise, stable pulp cost and high hygiene margin. However, we do not see strong earnings acceleration, given continued competition in sanitary napkins, and channel mix dilution from higher online / new retail penetration.

\- Valuation-wise, Hengan is not expensive, but rerating catalysts are limited. The stock is trading at around 10x 2026 P/E, with a dividend yield of around $6\%$ . We think the valuation is undemanding and the dividend yield should provide downside support, especially given the company's stable cash generation. However, without stronger revenue acceleration or clearer evidence that hygiene products can return to sustainable growth, we think a higher multiple is hard to justify. Remain EW.

## Estimate changes

We slightly revise up our revenue forecasts by 0.1% and 0.6% for 2026 and 2027, mainly due to higher revenue forecasts for all three main products. We introduce our 2028 forecasts and now expect revenue growth to be 4%/3%/4% in 2026/27/28, respectively.

We increase our GPM assumptions by 0.7ppt and 0.6ppt for 2026 and 2027 on lower raw material prices. We expect blended GPM to be 32.8%/32.9%/33.0% in 2026/27/28.

We raise the opex ratio forecasts by 0.6ppt and 0.7ppt for 2026 and 2027, reflecting increasing penetration in online and new retail channels, and heavier investment for branding. We now estimate the opex ratio to be 23.3%/23.5%/23.4% in 2026/27/28, respectively.

As a result, we revise up our net profit forecasts by 2.4% and 2.2% for 2026 and 2027, mainly driven by higher GPM. We estimate NPM will be 10.2%, 10.1%, and 10.1% in 2026, 2027, and 2028, respectively.

Exhibit 3: Hengan: Summary of changes

<table><tr><td rowspan="2">(Rmb mn)</td><td colspan="3">New</td><td colspan="4">Old</td></tr><tr><td>2026e</td><td>2027e</td><td>2028e</td><td>2026e</td><td>2027e</td><td>2026e</td><td>2027e</td></tr><tr><td>Sales</td><td>23,967</td><td>24,695</td><td>25,570</td><td>23,952</td><td>24,549</td><td>0.1%</td><td>0.6%</td></tr><tr><td>Core Products</td><td>21,405</td><td>22,005</td><td>22,745</td><td>21,244</td><td>21,787</td><td>0.8%</td><td>1.0%</td></tr><tr><td>- Sanitary napkins</td><td>5,185</td><td>5,263</td><td>5,369</td><td>5,151</td><td>5,229</td><td>0.7%</td><td>0.7%</td></tr><tr><td>- Disposable diapers</td><td>1,347</td><td>1,347</td><td>1,360</td><td>1,286</td><td>1,304</td><td>4.7%</td><td>3.3%</td></tr><tr><td>- Tissue paper</td><td>14,873</td><td>15,396</td><td>16,016</td><td>14,807</td><td>15,254</td><td>0.4%</td><td>0.9%</td></tr><tr><td>Skincare and others</td><td>2,562</td><td>2,690</td><td>2,824</td><td>2,707</td><td>2,762</td><td>-5.4%</td><td>-2.6%</td></tr><tr><td>Gross Profit</td><td>7,863</td><td>8,134</td><td>8,432</td><td>7,686</td><td>7,946</td><td>2.3%</td><td>2.4%</td></tr><tr><td>Operating Expenses</td><td>(5,583)</td><td>(5,793)</td><td>(5,983)</td><td>(5,432)</td><td>(5,589)</td><td>2.8%</td><td>3.6%</td></tr><tr><td>Operating Income excl Others</td><td>2,280</td><td>2,341</td><td>2,448</td><td>2,254</td><td>2,356</td><td>1.2%</td><td>-0.7%</td></tr><tr><td>Net Profit</td><td>2,449</td><td>2,491</td><td>2,582</td><td>2,393</td><td>2,438</td><td>2.4%</td><td>2.2%</td></tr><tr><td>EPS (basic; Rmb)</td><td>2.15</td><td>2.19</td><td>2.27</td><td>2.10</td><td>2.14</td><td>2.6%</td><td>2.4%</td></tr><tr><td>EPS (diluted; Rmb)</td><td>2.15</td><td>2.19</td><td>2.27</td><td>2.10</td><td>2.14</td><td>2.6%</td><td>2.4%</td></tr><tr><td>Gross Margin</td><td>32.8%</td><td>32.9%</td><td>33.0%</td><td>32.1%</td><td>32.4%</td><td>0.7%</td><td>0.6%</td></tr><tr><td>SG&amp;A to Sales</td><td>23.3%</td><td>23.5%</td><td>23.4%</td><td>22.7%</td><td>22.8%</td><td>0.6%</td><td>0.7%</td></tr><tr><td>Operating Margin</td><td>9.5%</td><td>9.5%</td><td>9.6%</td><td>9.4%</td><td>9.6%</td><td>0.1%</td><td>-0.1%</td></tr><tr><td>Net Margin</td><td>10.2%</td><td>10.1%</td><td>10.1%</td><td>10.0%</td><td>9.9%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>Tax Rate</td><td>22.0%</td><td>22.0%</td><td>22.0%</td><td>22.7%</td><td>22.7%</td><td>-0.7%</td><td>-0.7%</td></tr></table>

Source: MS, E=MS estimates

Our PT falls by 4% from HK\$24.0 to HK\$23.0 on lower government grants/tax refunds and more conservative working capital assumptions. We derive our PT from a DCF valuation methodology using a 14% WACC and 1% terminal growth (both unchanged).

We cut our bull and bear case values accordingly. Our bull case value of HK\$31.5 is derived from a target P/E of 13x 2026e, and our bear case value of HK\$17.6 is derived from a target P/E of 9x 2026e.

Exhibit 4: Hengan: DCF Valuation

<table><tr><td>DCF</td><td>2026</td><td>2027</td><td>2028</td><td>2029</td><td>2030</td><td></td></tr><tr><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td><td>Term Val</td></tr><tr><td>Operating Income (EBIT)</td><td>2,280</td><td>2,341</td><td>2,448</td><td>2,827</td><td>3,207</td><td>3,239</td></tr><tr><td>Tax</td><td>(570)</td><td>(585)</td><td>(612)</td><td>(707)</td><td>(802)</td><td>(810)</td></tr><tr><td>Government Grants (tax return)</td><td>227</td><td>227</td><td>227</td><td>227</td><td>227</td><td>227</td></tr><tr><td>Depreciation/Amortization (excl g/w)</td><td>1,010</td><td>1,004</td><td>1,001</td><td>998</td><td>996</td><td>996</td></tr><tr><td>Changes in Net Working Capital</td><td>(269)</td><td>(53)</td><td>(167)</td><td>(185)</td><td>(186)</td><td>(186)</td></tr><tr><td>Capex and Investment</td><td>(1,012)</td><td>(1,012)</td><td>(1,012)</td><td>(1,012)</td><td>(1,012)</td><td>(1,012)</td></tr><tr><td>Free Cash Flow</td><td>1,666</td><td>1,921</td><td>1,886</td><td>2,149</td><td>2,430</td><td>2,454</td></tr><tr><td colspan="7">Discount Rate = 14%Long-term growth rate=1%</td></tr><tr><td>Discount Factor</td><td></td><td>0.88</td><td>0.77</td><td>0.67</td><td>0.59</td><td>4.55</td></tr><tr><td>PV FCF</td><td></td><td>1,685</td><td>1,451</td><td>1,450</td><td>1,439</td><td>11,178</td></tr><tr><td>Sum of PV FCF</td><td>17,203</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Less Net Debt</td><td>(7,577)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Equity Value</td><td>24,781</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Per Share Value - Rmb</td><td>21.8</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Per Share Value - HK$</td><td>23.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>WACC</td><td>14.0%</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Terminal Growth</td><td>1.0%</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: MS, E=MS estimates

Exhibit 5: Hengan: Bull/Base/Bear Cases

<table><tr><td>Hengan</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026e</td><td>2027e</td><td>2028e</td><td>2024-26e CAGR</td><td>2025-27e CAGR</td></tr><tr><td colspan="11">Base Case Scenario</td></tr><tr><td>Sales</td><td>20,790</td><td>22,616</td><td>23,768</td><td>22,669</td><td>23,069</td><td>23,967</td><td>24,695</td><td>25,570</td><td>3%</td><td>3%</td></tr><tr><td>% YoY</td><td>-7%</td><td>9%</td><td>5%</td><td>-5%</td><td>2%</td><td>4%</td><td>3%</td><td>4%</td><td></td><td></td></tr><tr><td>Net Profit</td><td>3,274</td><td>1,925</td><td>2,801</td><td>2,298</td><td>2,535</td><td>2,449</td><td>2,491</td><td>2,582</td><td>3%</td><td>-1%</td></tr><tr><td>% YoY</td><td>-29%</td><td>-41%</td><td>45%</td><td>-18%</td><td>10%</td><td>-3%</td><td>2%</td><td>4%</td><td></td><td></td></tr><tr><td>EPS - Rmb</td><td>2.79</td><td>1.66</td><td>2.41</td><td>2.02</td><td>2.23</td><td>2.15</td><td>2.19</td><td>2.27</td><td>3%</td><td>-1%</td></tr><tr><td>EPS - HKD</td><td>3.31</td><td>1.97</td><td>2.77</td><td>2.16</td><td>2.39</td><td>2.31</td><td>2.35</td><td>2.43</td><td></td><td></td></tr><tr><td>Implied Target P/E</td><td></td><td>12</td><td>8</td><td>11</td><td>10</td><td>10</td><td>10</td><td>9</td><td></td><td></td></tr><tr><td>Base Value</td><td></td><td></td><td></td><td></td><td>HKD</td><td>23.0</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="11">Bull Case Scenario</td></tr><tr><td>Sales</td><td>20,790</td><td>22,616</td><td>23,768</td><td>22,669</td><td>23,069</td><td>25,165</td><td>27,165</td><td>28,127</td><td>5%</td><td>9%</td></tr><tr><td>% YoY</td><td>-7%</td><td>9%</td><td>5%</td><td>-5%</td><td>2%</td><td>9%</td><td>8%</td><td>4%</td><td></td><td></td></tr><tr><td>% Higher than Base</td><td></td><td></td><td></td><td></td><td></td><td>5%</td><td>10%</td><td>10%</td><td></td><td></td></tr><tr><td>Net Profit</td><td>3,274</td><td>1,925</td><td>2,801</td><td>2,298</td><td>2,535</td><td>2,572</td><td>2,740</td><td>2,840</td><td>6%</td><td>4%</td></tr><tr><td>% YoY</td><td>-29%</td><td>-41%</td><td>45%</td><td>-18%</td><td>10%</td><td>1%</td><td>7%</td><td>4%</td><td></td><td></td></tr><tr><td>% Higher than Base</td><td></td><td></td><td></td><td></td><td></td><td>5%</td><td>10%</td><td>10%</td><td></td><td></td></tr><tr><td>EPS - HKD</td><td>3.31</td><td>1.97</td><td>2.77</td><td>2.16</td><td>2.39</td><td>2.42</td><td>2.58<

[中间内容因长度限制已省略]

International Holdings Ltd (6110.HK)</td><td>O (11/13/2019)</td><td>HK$2.51</td></tr><tr><td>Weilong Delicious Global Holdings Ltd (9985.HK)</td><td>O (06/11/2025)</td><td>HK$7.41</td></tr><tr><td>Yonghui Superstores (601933.SS)</td><td>U (05/18/2023)</td><td>Rmb3.08</td></tr><tr><td colspan="3">Hildy Ling</td></tr><tr><td>Angel Yeast Co. Ltd. (600298.SS)</td><td>E (05/21/2026)</td><td>Rmb35.69</td></tr><tr><td>Beijing Roborock Technology Co Ltd (688169.SS)</td><td>O (09/25/2024)</td><td>Rmb98.47</td></tr><tr><td>China Tourism Group Duty Free (1880.HK)</td><td>E (12/13/2023)</td><td>HK$52.95</td></tr><tr><td>China Tourism Group Duty Free (601888.SS)</td><td>E (12/13/2023)</td><td>Rmb56.79</td></tr><tr><td>Chow Tai Fook Jewellery Group Ltd (1929.HK)</td><td>O (03/04/2025)</td><td>HK$12.22</td></tr><tr><td>Chow Tai Seng Jewellery Co Ltd (002867.SZ)</td><td>U (03/04/2025)</td><td>Rmb11.74</td></tr><tr><td>Ecovacs Robotics Co Ltd (603486.SS)</td><td>E (10/30/2023)</td><td>Rmb53.80</td></tr><tr><td>Foshan Haitian Flavouring and Food (603288.SS)</td><td>E (07/28/2025)</td><td>Rmb33.04</td></tr><tr><td>Foshan Haitian Flavouring and Food (3288.HK)</td><td>E (05/21/2026)</td><td>HK$29.14</td></tr><tr><td>Haidilao International Holding Ltd (6862.HK)</td><td>O (05/26/2021)</td><td>HK$11.40</td></tr><tr><td>Hangzhou Robam Appliances Co Ltd (002508.SZ)</td><td>U (02/21/2024)</td><td>Rmb15.46</td></tr><tr><td>Laopu Gold (6181.HK)</td><td>O (10/20/2025)</td><td>HK$434.80</td></tr><tr><td>Super Hi (HDL.O)</td><td>E (01/14/2025)</td><td>US$12.58</td></tr><tr><td>Zhejiang Supor Co. Ltd. (002032.SZ)</td><td>E (01/17/2022)</td><td>Rmb40.59</td></tr><tr><td colspan="3">Lillian Lou</td></tr><tr><td>Anhui Gujing Distillery Company Limited (000596.SZ)</td><td>U (02/13/2026)</td><td>Rmb82.54</td></tr><tr><td>Budweiser Brewing Company APAC Ltd (1876.HK)</td><td>O (11/04/2019)</td><td>HK$6.46</td></tr><tr><td>Chagee Holdings Ltd (CHA.O)</td><td>O (06/02/2025)</td><td>US$11.22</td></tr><tr><td>China Mengniu Dairy (2319.HK)</td><td>O (09/14/2017)</td><td>HK$15.89</td></tr><tr><td>China Resources Beer Holdings Co Ltd (0291.HK)</td><td>O (12/11/2018)</td><td>HK$21.46</td></tr><tr><td>Chongqing Brewery Co. Ltd. (600132.SS)</td><td>U (07/30/2021)</td><td>Rmb44.22</td></tr><tr><td>Eastroc Beverages (605499.SS)</td><td>O (03/12/2026)</td><td>Rmb120.63</td></tr><tr><td>Eastroc Beverages (9980.HK)</td><td>O (03/12/2026)</td><td>HK$108.90</td></tr><tr><td>Gree Electric Appliances Inc of Zhuhai (000651.SZ)</td><td>O (04/14/2020)</td><td>Rmb36.99</td></tr><tr><td>Haier Smart Home Co Ltd (600690.SS)</td><td>E (01/17/2022)</td><td>Rmb19.98</td></tr><tr><td>Haier Smart Home Co Ltd (6690.HK)</td><td>E (01/17/2022)</td><td>HK$19.98</td></tr><tr><td>Kweichow Moutai Company Ltd. (600519.SS)</td><td>O (10/17/2014)</td><td>Rmb1,241.41</td></tr><tr><td>Luzhou Lao Jiao Co. Ltd (000568.SZ)</td><td>E (01/23/2019)</td><td>Rmb81.27</td></tr><tr><td>Midea Group Co Ltd. (0300.HK)</td><td>O (11/01/2024)</td><td>HK$82.65</td></tr><tr><td>Midea Group Co Ltd. (000333.SZ)</td><td>O (01/17/2022)</td><td>Rmb78.28</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (2714.HK)</td><td>O (03/17/2026)</td><td>HK$29.62</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (002714.SZ)</td><td>O (03/17/2026)</td><td>Rmb33.95</td></tr><tr><td>Nongfu Spring Co Ltd (9633.HK)</td><td>E (07/30/2021)</td><td>HK$41.72</td></tr><tr><td>Shanxi Xinghuacun Fen Wine Factory Co. (600809.SS)</td><td>O (10/28/2020)</td><td>Rmb113.61</td></tr><tr><td>Shuanghui Development (000895.SZ)</td><td>U (03/16/2021)</td><td>Rmb22.86</td></tr><tr><td>Tingyi (Cayman Islands) (0322.HK)</td><td>E (07/25/2025)</td><td>HK$9.99</td></tr><tr><td>Tsingtao Brewery Co Ltd (0168.HK)</td><td>E (11/01/2024)</td><td>HK$44.80</td></tr><tr><td>Tsingtao Brewery Co Ltd (600600.SS)</td><td>E (02/28/2024)</td><td>Rmb53.92</td></tr><tr><td>Uni-President China (0220.HK)</td><td>E (07/25/2025)</td><td>HK$6.84</td></tr><tr><td>Want Want China Holdings Ltd (0151.HK)</td><td>E (11/29/2023)</td><td>HK$3.99</td></tr><tr><td>WH Group (0288.HK)</td><td>O (02/24/2025)</td><td>HK$8.61</td></tr><tr><td>Wuliangye Yibin Company Ltd. (000858.SZ)</td><td>E (08/15/2024)</td><td>Rmb76.55</td></tr><tr><td>Yanghe Brewery (002304.SZ)</td><td>U (01/05/2021)</td><td>Rmb41.25</td></tr><tr><td>Yanjing Brewery (000729.SZ)</td><td>U (09/02/2015)</td><td>Rmb10.28</td></tr><tr><td>Yili Industrial (600887.SS)</td><td>O (01/29/2014)</td><td>Rmb24.63</td></tr><tr><td>Yum China Holdings Inc. (YUMC.N)</td><td>O (03/20/2018)</td><td>US$41.53</td></tr><tr><td>ZJLD Group (6979.HK)</td><td>E (02/13/2026)</td><td>HK$7.55</td></tr><tr><td colspan="3">Terence Cheng</td></tr><tr><td>Chervon Holdings Ltd. (2285.HK)</td><td>E (04/12/2024)</td><td>HK$16.58</td></tr><tr><td>Crystal International Group Ltd. (2232.HK)</td><td>E (06/23/2025)</td><td>HK$5.67</td></tr><tr><td>Gongniu Group Co Ltd (603195.SS)</td><td>O (05/08/2023)</td><td>Rmb39.47</td></tr><tr><td>Hangzhou Greatstar Industrial Co Ltd (002444.SZ)</td><td>E (10/26/2022)</td><td>Rmb29.43</td></tr><tr><td>Huali Industrial Group Co (300979.SZ)</td><td>U (02/10/2026)</td><td>Rmb31.22</td></tr><tr><td>Shenzhou International Group Holdings (2313.HK)</td><td>O (07/13/2017)</td><td>HK$40.70</td></tr><tr><td>Stella International Holdings Ltd (1836.HK)</td><td>E (06/23/2025)</td><td>HK$12.39</td></tr><tr><td>Techtronic Industries Co Ltd (0669.HK)</td><td>O (12/05/2019)</td><td>HK$121.90</td></tr><tr><td>Yue Yuen Industrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$12.97</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
