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
<table><tr><td colspan="2">MS &amp; CO. INTERNATIONAL PLC+</td></tr><tr><td colspan="2">Bart Gysens, CFA</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Bart.Gysens@morganstanley.com</td><td>+44 20 7425-5862</td></tr><tr><td colspan="2">Ana Escalante</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Ana.Escalante@morganstanley.com</td><td>+44 20 7425-3271</td></tr><tr><td colspan="2">Paula Bayer</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Paula.Bayer@morganstanley.com</td><td>+44 20 7425-3053</td></tr></table>

Property | Europe

# Monthly Chartbook

Pan-European property chartbook. We publish this chartbook monthly. It includes performance statistics, stock valuation metrics, our property market assumptions, direct property market statistics and the latest macro data.

## Key Takeaways

European property sector was up 1% in June, but is flat year to date vs European equities up 9%.

The UK has outperformed continental Europe in June, and also year to date.

■ Sector trading at a 32% discount to NAV, 14x median PE.

Performance statistics. Our chartbook provides regional and sector-specific, absolute and relative performance statistics. The European property sector is flat year to date vs MSCI Europe up +9% (in euros). On a total shareholder return basis (including dividends), the property sector returned +3% vs MSCI Europe +11%. UK property stocks are up 4% year to date (in local currency), vs UK equities up +5% (UK equities largely driven by the energy sector). Retail and logistics are the best performing subsectors year to date, vs residential and self storage lagging.

Stock valuation metrics. The chartbook also includes long-term data series of key valuation metrics, such as discount to NAV, dividend yield, EPS yield and EBITDA/EV yield. The sector is trading at a 32% discount to NAV vs the historical average discount of 17%. NAV valuation dispersion has materially increased in the last few months and remains above the 10-year average in June. From an EPS yield perspective, dispersion is at an all-time low.

Detailed direct property market assumptions. In addition, we set out our assumptions for direct property markets across Europe, including rental growth, yield shift and capital growth. For 2026, we forecast a 3% capital value growth on average across the UK stocks we cover, vs 1% in Continental Europe.

Macro data. The chartbook includes data on GDP growth, bond yields, capital availability, inflation and currency moves, and how they correlate with property markets.

Direct property market statistics. We publish long-term data series for European office main property markets, including rents, values and yields, as well as e-commerce penetration and logistics rents.

Our latest sector views. See Property: From Asymmetric to More Symmetric Risk Reward (16 Mar 2026)

## PROPERTY

Europe
Industry View Attractive

## For specific subsectors see:

• UK Property: May IPD Update (15 Jun 2026)

• European Property Transaction Tracker: Slowdown in 1Q26 (8 May 2026)

• German Residential Chartbook: Pause in Rental Growth in 1Q (22 Apr 2026)

\- Paris Office Property: Slipping Further (8 Apr 2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Absolute and relative performance

Exhibit 1: Pan-European absolute performance (euro-based)  
![](images/07cb252a1f6ca296249851fe52b0c3e30211ecee35c06358da3ab8a5a316b62e.jpg)  
Source: Datastream, MS

Exhibit 2: Regional absolute performance  
![](images/8a4d42fad898aaf06844318c5c332cf8c5bd5b25a5dbd036d668748c5922955d.jpg)  
Source: Datastream, MS

Exhibit 3: Pan-European relative performance (US dollar-based)  
![](images/2048c444a9379c392a9bac23a51d5f8c5ce62ad9a8b29731ff6a8d83bbca356b.jpg)  
Source: Datastream, MS

Exhibit 4: Regional relative performance (US dollar-based)  
![](images/923a9e01d3f0fb0c44bc1e08f63658a9114db72c15c77dc6ed63e822dc6f0d46.jpg)  
Source: Datastream, MS

Share price performance YTD (%)

Exhibit 5: Regional absolute performance in recent periods  
Share price performance (\%, at month end)  
![](images/684c07add822557acb438728b8c59983839af1ab64daa106dfe011754a40afdd.jpg)  
Source: Datastream, MS

Exhibit 6: Absolute performance by country  
![](images/f2811b29e887100522fcaa6bc49de66ee7f968cb31e8706d5f84a35773fb16d6.jpg)  
Source: Datastream, MS

Exhibit 7: UK property stocks relative to those in continental Europe (euro-based)  
![](images/6d95658c5c6aa789e7c51a01dce9cf8761190ff715ef404314745a98346854d0.jpg)  
Source: Datastream, MS

Exhibit 8: EPRA REITs vs Non REITs (euro-based)  
![](images/367113ef30ab4bec3c74c15b00361c4a19bee6d1548e2b09c7fb9371c7ee2380.jpg)  
Source: Datastream, MS

Exhibit 9: Shareholder return by subsector (euro-based)  
![](images/13834e19b0f336e1b7c88678d52c0496e23f989a2faeaa2e4ec4081df6912952.jpg)  
Source: Datastream, MS

Exhibit 10: Performance by subsector (euro-based), recent periods  
![](images/eb32ad6e4c9cf8287c1c1b0d2a37b6b358b522c20d706bd2d126a61d6f29e934.jpg)  
Source: Datastream, MS

Exhibit 11: Stock performance dispersion (last 12 months)  
European Property Stocks: shareprice performance gap between 75th and 25th percentile, percentage points  
![](images/3d9f8968093868edfaeeda32b60c942fbdbe43f25ff07ee02c4c33adafd8fdb2.jpg)  
Source: Company data, Datastream, MS

## Absolute total returns

Exhibit 12: Total share price return by country (in percent, last month)

![](images/2d59e0aa1727a52fc9808701b6736d2a29692f8502cef1438897891a6ce0ddfe.jpg)  
Source: Datastream, EPRA, MS

Exhibit 13: Total share price return by country (in percent, YTD)  
![](images/32fc5df4280277167d3ed1e8e6cfd14e4d4050fdc43707e747dfe9da7f944136.jpg)  
Source: Datastream, EPRA, MS

Exhibit 14: Shareholder return by market (in percent, euro-based, to month end)
Total Shareholder Return (\%, at month end)  
![](images/bfdd0493768eead7960046ba943c1366d21a5984564922ab787984b04d861792.jpg)  
Source: Datastream, EPRA, MS

Exhibit 15: Shareholder by subsector (in percent, euro-based, to month end)  
![](images/38159a775c790ff6a45048ee8158d77c97dfccb239d97cb525ab7505b1ccc1f3.jpg)  
Source: Datastream, EPRA, MS

## Discount to NAV

Exhibit 16: Pan-European discount to NAV

![](images/1ae164337e4d8fe48daa948034472022eddf20e01e2d59aff08eb4982d260536.jpg)  
Source: Company data, Datastream, MS

Exhibit 17: UK and continental European discounts to NAV  
![](images/85d18085b996c9dfb871b45c3804ac2f1dbde3e1233e18bb69592311d62af863.jpg)  
Source: Company data, Datastream, MS  
Exhibit 18: Spread between UK and continental Europe

![](images/239af7861a0eb2572d76a8456031398fc6aec094de36dd665d147a25bb641a8d.jpg)  
Source: Company data, Datastream, MS  
Exhibit 19: Regional discounts to NAV

![](images/e2d4d70e4e44c43058450cf639d43df3a7b22a6d03a225a9ad719c69ed35a012.jpg)  
Source: Company data, Datastream, MS

Exhibit 20: Regional discounts to NAV  
![](images/3ac3c1247a7e3c0fe14f4cdf0b40d6789495c853c7954e42cbd1e51c867c097a.jpg)  
Source: Company data, Datastream, MS

Exhibit 21: Regional discounts to NAV  
![](images/da478c9f2f5d20ed3543c3a9f0f93761357b387a2a607854e7c955e18f080d75.jpg)  
Source: Company data, Datastream, MS

Exhibit 22: Pan-European retail vs office discount to NAV  
Pan-European office/retail Premium/(Discount) to NAV (%)  
![](images/95e7a5168c8d8dbf17579b9fad71fc9d391313156bb9a2d60448cd01416c3894.jpg)  
Source: Company data, Datastream, MS

Exhibit 23: Pan-European logistics vs German resi discount to NAV  
Pan-EU logistics/German resi Premium/(Discount) to NAV (%)  
![](images/78e096422a0350185d3c02b5c8c47cf45195bb179b4733c52bfbe7577fe2d30c.jpg)  
Source: Company data, Datastream, MS

## Discount to NAV and Growth

Exhibit 24: Discount to NAV and NAV growth for pan-European quoted property sector  
![](images/230adebba0815c85b47b971202b2f8b938929fd2e77b57f4a94172041a342aa0.jpg)  
Source: Company data, Datastream, MS

Exhibit 25: Discount to NAV and NAV growth for the UK property sector  
![](images/ca5e4a77f8c5ddc02c80ce96ed1c7279a68deaaad2a8ef332dbba9111f6af213.jpg)  
Source: Company data, Datastream, MS

Exhibit 26: NAV valuation vs OECD Composite Leading Indicator – UK  
![](images/6ea788cb13aa6a7a6ecc27886a7cf7dd42e170e0c938eac5fba2e9a044cb4e88.jpg)  
Source: OECD, MS

Exhibit 27: NAV valuation vs OECD Composite Leading Indicator – continental Europe  
![](images/aa3d91ae9794c1d05157fcbb9de735e3cf42c83172de608fc048e8420d8773ce.jpg)  
Source: OECD, MS

## Volatility

Exhibit 28: Share price volatility measures: Pan-Europe  
Pan-Europe Real Estate volatility (%)  
![](images/5654d28f6e0576853b424c88e3d538425e0c34f007416ed8e5c7a7f1f4d2987d.jpg)  
Source: Bloomberg, MS

Exhibit 30: Share price volatility measures: Continental Europe  
Continental Europe Real Estate volatility (%)  
![](images/4874a4ac0370cbb53dcb142e237af0b69246c69f3ac4942f8bc0901af99b253a.jpg)  
Source: Bloomberg, MS

Exhibit 29: Share price volatility measures: UK  
UK Real Estate volatility (%)  
![](images/1eab0e70bd729a57a1502e034fb878fc08cfa4429378515f27c6a010a7bacae7.jpg)  
Source: Bloomberg, MS

## A note on the Bloomberg volatility series

These series show the standard deviation of day to day logarithmic historical price changes for the names under our coverage. The 12-week price volatility shown equals the average annualised standard deviation of the relative price change for the 12 most recent trading weeks' closing prices on average, expressed as a percentage.

For example, assuming a stock trades at \$100 and has a volatility of 30%, we can expect that within one standard deviation (or 68% of the time) the price will fall between a range of \$70 to \$130. Given the historical prices of the stock, historical volatility shows how variant the price has been over a specified time period.

## Dividend Yield

Exhibit 31: Pan-European dividend yield  
![](images/e3f738629f3762a2b589ae86a17b46e2ca5fbbfa1e0373d0cdb465d4273004bb.jpg)  
Source: Datastream, MS

Exhibit 32: Dividend yield by region (1)  
![](images/1f9609745e00f6fcf1cbb3e875acbbe03bd097de39034c274fad7213e5ce6241.jpg)  
Source: Datastream, MS

Exhibit 33: Dividend yield by region (2)  
![](images/0f5df06e8494f07e00ea9caf5f3ec2c1c37a994d7fe496ba9608c33a46525a5a.jpg)  
Source: Datastream, MS

Exhibit 34: Dividend yield by region (3)  
![](images/d8d88eaee5134dc4a8f5ea836c6d6311cd5f56ed9fa76601f80c6c7ccf9dc789.jpg)  
Source: Datastream, MS

## EBITDA/EV

Exhibit 35: Pan-European EBITDA/EV yield  
EBITDA/EV yield (%)  
![](images/d3250be6fcc4e308c90e6f9c972c801093224ad9e17b434f80dda38bf859aa5a.jpg)  
Source: Datastream, Company data, MS

Exhibit 36: UK and continental European EBITDA/EV yields  
EBITDA/EV yield (%)  
![](images/7feff6648f18f72afc19a83cb874b1672dc06c8e789e83d1d62aab9cff06756d.jpg)  
Source: Datastream, Company data, MS

Exhibit 37: EBITDA/EV yield margin over local 5-year swap rates

EBITDA/EV yield spread over 5Y swap, bp  
![](images/59755e25e3c97fdeadf9868b27d90608ceda559fb06008f186c057996da880c3.jpg)  
Exhibit 38: EBITDA/EV yields, property yields and UK swap rates  
Source: Datastream, Company data, MS

EBITDA/EV yield (%)  
![](images/529f4738795c3622c72b42e7752a85da33665ca4c614f1962555967c0f732f17.jpg)  
Source: Datastream, Company data, MS

## MS coverage-specific metrics

Exhibit 39: Net debt to gross assets less cash and goodwill (proxy for LTV)  
![](images/df3041c1f287b901ba4a9da86613ced5b1739c2dfaf7bd9c4986797adec0fd4c.jpg)  
Source: Company data, MS. Uses EPRA LTV since introduced  
Exhibit 41: EPS yield (trailing)  
Exhibit 40: Net debt to EBITDA

![](images/cb10cfaa75966c9fdcfe71a83ef4bcebc08657ff857a2a968ac08d597ce15a71.jpg)  
Source: Company data, MS

Trailing EPS yield (%)  
![](images/49d57a7ea0501a83b0ee8f2a43088f33c5b778305c45997ff1af029ef95d498c.jpg)  
Source: Company data, MS  
Exhibit 42: EPS yield (trailing) vs LTV

Trailing EPS yield vs. LTV  
![](images/bf1def9d26efdcec3f3614bc2aaaa987cf70d7812f5cdccd823d3cdd12f5ed84.jpg)  
Source: Company data, MS. Uses EPRA LTV since introduced

## Beta

Exhibit 43: EPRA developed Europe beta vs LTV  
![](images/4799b8a7b16448bce0d40720b174c959185788076c0c8a0cd7ed40e0276787d6.jpg)  
Source: Company data, Datastream, MS. Note: 5 year monthly beta, regression vs EPRA developed Europe index

Exhibit 44: EPRA developed Europe beta vs Price to NAV  
![](images/64c1754ab4d483b0c45634ea39a9d8b2dec3b3ffe7b31736e0b4dcfb6441c3e7.jpg)  
Source: Company data, Datastream, MS. Note: 5 year monthly beta, regression vs EPRA developed Europe index

## Valuation Dispersion

Exhibit 45: Stock valuation dispersion, using Price to NAV  
![](images/572d6abd14cc9621ecd63a6f8b3ce21db052f832c3ad4fa38ca5a517ca5eae77.jpg)  
Source: Company data, Datastream, MS

Exhibit 46: Stock valuation dispersion, using adjusted EPRA EPS yield (EPRA EPS excluding capitalised interest)  
![](images/0c2e8d9516ccaf49ddec6fd0c59c3b89f5e95e3f05b4029f07b2e83e82ea0787.jpg)  
Source: Company data, Datastream, MS

Exhibit 47: Total return vs NAV (premium/discount) valuation  
![](images/7ddaa6e89f623ef4106a62fe49c1f72b08bf63c60609e1cdbf8bb4bd86e2f068.jpg)  
Source: Company data, Datastream, MS  
Exhibit 48: P/E vs EPS growth

![](images/da3a90666c53dcdf13d4e2a114b43be0e1031c4f26a15b9f8e5af879732353d4.jpg)  
Source: Company data, Datastream, MS

## Direct property market assumptions – UK

Exhibit 49: Summary of assumptions – UK

<table><tr><td></td><td>FY26</td><td>FY27</td><td>FY28</td></tr><tr><td colspan="4">Capital growth (%)</td></tr><tr><td>Listed UK retail</td><td>3</td><td>4</td><td>3</td></tr><tr><td>London offices</td><td>3</td><td>4</td><td>4</td></tr><tr><td>UK industrial/logistics</td><td>2</td><td>2</td><td>4</td></tr><tr><td colspan="4">Yield shift (bp)</td></tr><tr><td>Listed UK retail</td><td>0</td><td>-7</td><td>-7</td></tr><tr><td>London offices</td><td>9</td><td>-1</td><td>-4</td></tr><tr><td>UK industrial/logistics</td><td>0</td><td>0</td><td>-5</td></tr><tr><td colspan="4">Market rental growth (%)</td></tr><tr><td>Listed UK retail</td><td>3</td><td>3</td><td>3</td></tr><tr><td>London offices</td><td>5</td><td>4</td><td>3</td></tr><tr><td>UK industrial/logistics</td><td>3</td><td>3</td><td>3</td></tr></table>

Source: MS estimates. Notes: FY26 is equivalent to year to December 2026, or year to March 2027, depending on company year end. Except where specified, these assumptions represent simple averages of our underlying assumptions for the key portfolios in the main sub-segments represented within the UK property sector. These assumptions may vary on a company-specific basis.

## Direct property market assumptions – Continental Europe

## Exhibit 50: Summary of assumptions - continental Europe

<table><tr><td></td><td>FY26</td><td>FY27</td><td>FY28</td></tr><tr><td colspan="4">Capital growth (%)</td></tr><tr><td>Paris offices</td><td>-0</td><td>0</td><td>0</td></tr><tr><td>Madrid offices</td><td>2</td><td>2</td><td>2</td></tr><tr><td>German offices</td><td>-2</td><td>-1</td><td>-1</td></tr><tr><td>Stockholm offices</td><td>-2</td><td>-1</td><td>1</td></tr><tr><td>Average retail</td><td>1</td><td>2</td><td>2</td></tr><tr><td>German residential</td><td>2</td><td>2</td><td>2</td></tr><tr><td>Average logistics</td><td>1</td><td>3</td><td>3</td></tr><tr><td colspan="4">Yield shift (bp)</td></tr><tr><td>Paris offices</td><td>4</td><td>2</td><td>2</td></tr><tr><td>Madrid offices</td><td>0</td><td>0</td><td>0</td></tr><tr><td>German offices</td><td>13</td><td>13</td><td>10</td></tr><tr><td>Stockholm offices</td><td>5</td><td>5</td><td>0</td></tr><tr><td>Average retail</td><td>6</td><td>7</td><td>3</td></tr><tr><td>German residential</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Average logistics</td><td>2</td><td>-3</td><td>-2</td></tr><tr><td colspan="4">Market rental growth (%)</td></tr><tr><td>Paris offices</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Madrid offices</td><td>2</td><td>2</td><td>2</td></tr><tr><td>German offices</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Stockholm offices</td><td>-1</td><td>0</td><td>1</td></tr><tr><td>Average retail</td><td>2</td><td>2</td><td>2</td></tr><tr><td>German residential</td><td>3</td><td>2</td><td>3</td></tr><tr><td>Average logistics</td><td>2</td><td>2</td><td>2</td></tr></table>

Source: MS estimates

# Office market statistics: rents and vacancy

Exhibit 51: London, Paris and Frankfurt: Prime office rents in euros ...  
![](images/3ba436103ba61063b2083e4bd0e4bbd5b9a22c0ec5ed22b602615025979d5428.jpg)  
Source: CBRE, JLL, Cushman, MS  
Exhibit 52: ... and office vacancy rates

![](images/3452c7c092dffd603b43238d37f2c5ccd35bc4c34a59f721e97c9e7ace00260e.jpg)  
Source: CBRE, DTZ, JLL, MS

Exhibit 53: Amsterdam, Brussels and Madrid: Prime office rents ...

Prime Office Rent (€ per sq m per annum)

![](images/af1d908343e8f9de12a86896b54b5acb81b71d5a2ae867118e889b5841fcaf48.jpg)  
Source: CBRE (until 2016), JLL (from 2017), Coll

[中间内容因长度限制已省略]

nancial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: Property

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/01/2026)</td></tr><tr><td colspan="3">Ana Escalante</td></tr><tr><td>Big Yellow Group (BYG.L)</td><td>U (03/16/2026)</td><td>905p</td></tr><tr><td>Colonial SFL (COL.MC)</td><td>O (03/25/2025)</td><td>€5.62</td></tr><tr><td>Covivio (CVO.PA)</td><td>U (12/03/2024)</td><td>€52.85</td></tr><tr><td>Gecina (GFCP.PA)</td><td>U (01/08/2024)</td><td>€72.05</td></tr><tr><td>Icade (ICAD.PA)</td><td>E (02/23/2026)</td><td>€18.97</td></tr><tr><td>LondonMetric (LMPL.L)</td><td>U (03/16/2026)</td><td>188p</td></tr><tr><td>MERLIN Properties (MRL.MC)</td><td>O (03/16/2026)</td><td>€15.31</td></tr><tr><td>Safestore (SAFE.L)</td><td>U (02/10/2025)</td><td>612p</td></tr><tr><td>Shurgard (SHUR.BR)</td><td>E (09/01/2025)</td><td>€26.30</td></tr><tr><td>Swiss Prime Site (SPSN.S)</td><td>U (01/13/2026)</td><td>SFr 130.40</td></tr><tr><td>Unite Group (UTG.L)</td><td>O (09/01/2022)</td><td>513p</td></tr><tr><td>Warehouses de Pauw (WDPP.BR)</td><td>E (02/13/2025)</td><td>€21.98</td></tr><tr><td>Xior (XIOR.BR)</td><td>O (06/05/2024)</td><td>€26.40</td></tr><tr><td colspan="3">Bart Gysens, CFA</td></tr><tr><td>Aedifica (AOO.BR)</td><td>E (11/24/2022)</td><td>€70.35</td></tr><tr><td>Aroundtown (AT1.DE)</td><td>U (04/16/2026)</td><td>€2.28</td></tr><tr><td>British Land (BLND.L)</td><td>O (04/21/2026)</td><td>412p</td></tr><tr><td>Castellum (CAST.ST)</td><td>U (08/29/2017)</td><td>SKr 128.65</td></tr><tr><td>Cofinimmo (COFB.BR)</td><td>E (09/04/2023)</td><td>€82.85</td></tr><tr><td>CTP (CTPNV.AS)</td><td>O (05/05/2021)</td><td>€16.16</td></tr><tr><td>Derwent London (DLN.L)</td><td>O (11/28/2019)</td><td>1,958p</td></tr><tr><td>Fabege (FABG.ST)</td><td>U (03/25/2015)</td><td>SKr 74.20</td></tr><tr><td>Great Portland Estates (GPEG.L)</td><td>O (09/01/2022)</td><td>333p</td></tr><tr><td>Hammerson (HMSO.L)</td><td>O (03/16/2026)</td><td>369p</td></tr><tr><td>Klepierre (LOIM.PA)</td><td>U (08/30/2018)</td><td>€36.12</td></tr><tr><td>Land Securities (LAND.L)</td><td>E (03/25/2025)</td><td>649p</td></tr><tr><td>LEG (LEGn.DE)</td><td>U (03/25/2025)</td><td>€55.20</td></tr><tr><td>NEPI Rockcastle (NRP.AS)</td><td>E (04/29/2026)</td><td>€7.81</td></tr><tr><td>PSP Swiss Property (PSPN.S)</td><td>U (09/02/2024)</td><td>SFr 143.40</td></tr><tr><td>SEGRO (SGRO.L)</td><td>++</td><td>886p</td></tr><tr><td>Shaftesbury (SHCS.L)</td><td>E (09/01/2025)</td><td>140p</td></tr><tr><td>Unibail-Rodamco-Westfield (URW.PA)</td><td>E (05/19/2025)</td><td>€101.10</td></tr><tr><td>Vonovia (VNAn.DE)</td><td>E (02/19/2026)</td><td>€21.34</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
