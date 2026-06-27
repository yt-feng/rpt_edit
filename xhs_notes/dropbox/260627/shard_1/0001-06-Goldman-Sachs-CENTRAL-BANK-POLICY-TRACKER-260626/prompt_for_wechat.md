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
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
CENTRAL BANK POLICY TRACKER

June 2026

■ Recent policy changes: Central bank actions have shifted more hawkish due to the war in Iran. In DMs, no central banks lowered and 39% raised rates over the last three months. In EMs, 16% cut rates and 7% raised rates over the same period. But our Global Financial Conditions Index (GS FCI) has eased by 24bp over the last three months, reflecting 34bp of easing in DMs and 10bp of easing in EMs (largely reflecting higher rates). At the country level, financial conditions have eased the most in Türkiye (-117bps), South Korea (-93bps), and Romania (-83bps) and tightened the most in Russia (158bps), Israel (57bps), and Brazil (57bps).

Forecast updates: We have made several policy rate forecast revisions over the last 30 days. In the US, we pushed back the final two rate cuts in our Fed forecast back to June and December of 2027 (vs. December 2026 and March 2027 previously). In Brazil, we raised our end-2026 policy rate forecasts by +75bp to 14.0%, in Hungary we lowered our end-2026 policy rate forecasts by -50bp to 5.25%, and in Taiwan we removed further rate cuts and now forecast a hold at 2% (vs 2.25% previously) through end-2026. In South Korea we raised our end-2027 policy rate forecasts by +25bp to 3.25%.

■ Current forecasts: We forecast that global central banks will lower rates by 0.1pp to $3.1\%$ (on a GDP-weighted basis) over the next four quarters. We expect that DM central banks will increase policy rates by 8bp on average over the next four quarters, reflecting rate hikes in New Zealand (+50bps), Euro Area (+25bps), Sweden (+25bps), Norway (+25bps) and Japan (+25bps) that are partially offset by holds or decreases elsewhere, particularly the US (-25bps through June 2027; -50bp through end-2027) and the UK (-50bps through June 2027; -75bp through end-2027). We expect that EM central banks will cut rates by -33bp on average, reflecting -208bp of cuts in CEEMEA and -35bp in Latin America, with 4bp of hikes in Asia.

■ Forecasts relative to consensus and current pricing: Our end-2026 policy rate forecasts are dovish relative to market pricing (our forecasts are below pricing in 73% of DMs and 57% of EMs; above in 18% of DMs and 43% of EMs). Our forecasts are balanced relative to consensus in both DMs (at least 0.1pp below in 27% vs. at least 0.1pp above in 27%) and EMs (at least 0.1pp below in 32% vs. at least 0.1pp above in 36%).

■ Balance sheet policy: Balance sheets as a share of GDP remain particularly

Jan Hatzius
+1(212)902-0394 | jan.hatzius@gs.com
GS & Co. LLC

Joseph Briggs +1(212)902-2163 | joseph.briggs@gs.com GS & Co. LLC

Sarah Dong
+1(212)357-9741 | sarah.dong@gs.com
GS & Co. LLC

Megan Peters  
+44(20)7051-2058 |  
megan.l.peters@gs.com  
GS International

elevated relative to their 2019 levels in New Zealand (8pp higher) and Australia (4pp). In the US, we see scope for a modest reduction in the Fed's balance sheet size if a reduction in reserve demand warrants an adjustment, but think the bar to a meaningful decline is high.

Exhibit 1: Global Central Banks Have Mostly Either Held or Hiked Over the Last Three Months  
![](images/373cddf35a3da51bcd18ebadbffc66d49ca85718a74e975a586de5cf03a7b165.jpg)  
Source: GS Global Investment Research

![](images/89fa2e88d938d72fde0b9ebe98b7be9e904e5276acacbd6510a38f8527edba56.jpg)

Exhibit 2: We Forecast Further Policy Rate Declines in the UK, US, and Some EMs, but Rate Hikes or Holds in Most DMs Over the Next Four Quarters  
![](images/f4ab4560bbe4cd72ca87a8092fc31a24ac7e8de368158e3759850e8d32d50446.jpg)  
Source: GS Global Investment Research

![](images/4738990b1d685f005f3e677e47e39a1f055c9965bb302ccd98585094f66683ab.jpg)

Exhibit 3: Our End-2026 Policy Rate Forecasts Are Dovish Relative to Market Pricing but Skewed Hawkish Relative to Consensus

<table><tr><td rowspan="4"></td><td colspan="6">End-2026 Policy Rate</td></tr><tr><td colspan="4">Policy Rate Forecasts</td><td colspan="2">vs. GS Forecast</td></tr><tr><td>Latest</td><td>GS</td><td>Consensus</td><td>Market Pricing</td><td>GS - Consensus</td><td>GS - Market Pricing</td></tr><tr><td colspan="4">(%)</td><td colspan="2">(pp)</td></tr><tr><td>Global*</td><td>4.6</td><td>4.7</td><td>4.6</td><td>4.5</td><td>0.0</td><td>0.2</td></tr><tr><td colspan="7">Developed Economies</td></tr><tr><td>US</td><td>3.6</td><td>3.6</td><td>3.1</td><td>4.0</td><td>0.5</td><td>-0.3</td></tr><tr><td>Euro Area</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td><td>0.0</td><td>0.0</td></tr><tr><td>Japan</td><td>1.0</td><td>1.0</td><td>1.3</td><td>1.2</td><td>-0.3</td><td>-0.2</td></tr><tr><td>UK</td><td>3.8</td><td>3.8</td><td>3.9</td><td>4.0</td><td>-0.1</td><td>-0.2</td></tr><tr><td>Canada</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.4</td><td>0.0</td><td>-0.2</td></tr><tr><td>Australia</td><td>4.4</td><td>4.6</td><td>4.4</td><td>4.5</td><td>0.2</td><td>0.1</td></tr><tr><td>Switzerland</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Sweden</td><td>1.8</td><td>2.0</td><td>1.9</td><td>1.9</td><td>0.1</td><td>0.1</td></tr><tr><td>Hong Kong</td><td>2.8</td><td>2.1</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>New Zealand</td><td>2.3</td><td>2.8</td><td>2.6</td><td>2.8</td><td>0.2</td><td>-0.1</td></tr><tr><td colspan="7">Latam</td></tr><tr><td>Brazil</td><td>14.3</td><td>14.0</td><td>13.4</td><td>13.8</td><td>0.6</td><td>0.2</td></tr><tr><td>Mexico</td><td>6.5</td><td>6.5</td><td>6.5</td><td>6.9</td><td>0.0</td><td>-0.4</td></tr><tr><td>Colombia</td><td>11.3</td><td>12.3</td><td>11.9</td><td>11.7</td><td>0.3</td><td>0.6</td></tr><tr><td>Chile</td><td>4.5</td><td>4.5</td><td>4.7</td><td>4.4</td><td>-0.2</td><td>0.1</td></tr><tr><td>Peru</td><td>4.3</td><td>4.3</td><td>4.3</td><td>NA</td><td>-0.1</td><td>NA</td></tr><tr><td colspan="7">CEEMEA</td></tr><tr><td>Russia</td><td>14.3</td><td>12.0</td><td>13.0</td><td>NA</td><td>-0.9</td><td>NA</td></tr><tr><td>Turkiye</td><td>37.0</td><td>37.0</td><td>35.2</td><td>39.4</td><td>1.8</td><td>-2.4</td></tr><tr><td>Poland</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.8</td><td>0.0</td><td>-0.1</td></tr><tr><td>Israel</td><td>3.8</td><td>3.3</td><td>3.6</td><td>3.9</td><td>-0.3</td><td>-0.6</td></tr><tr><td>Egypt</td><td>19.0</td><td>21.0</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>South Africa</td><td>7.0</td><td>7.3</td><td>7.0</td><td>7.3</td><td>0.3</td><td>0.0</td></tr><tr><td>Romania</td><td>6.5</td><td>6.5</td><td>6.3</td><td>NA</td><td>0.2</td><td>NA</td></tr><tr><td>Czech Republic</td><td>3.5</td><td>3.8</td><td>3.6</td><td>4.0</td><td>0.1</td><td>-0.3</td></tr><tr><td>Hungary</td><td>6.0</td><td>5.3</td><td>5.9</td><td>5.0</td><td>-0.7</td><td>0.2</td></tr><tr><td>Ukraine</td><td>15.0</td><td>13.5</td><td>14.2</td><td>NA</td><td>-0.7</td><td>NA</td></tr><tr><td>Ghana</td><td>14.0</td><td>14.0</td><td>13.2</td><td>NA</td><td>0.8</td><td>NA</td></tr><tr><td>Kazakhstan</td><td>17.0</td><td>15.5</td><td>16.2</td><td>NA</td><td>-0.7</td><td>NA</td></tr><tr><td colspan="7">Asia</td></tr><tr><td>Mainland China</td><td>1.4</td><td>1.4</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>India</td><td>5.3</td><td>5.8</td><td>5.5</td><td>5.6</td><td>0.2</td><td>0.1</td></tr><tr><td>South Korea</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.7</td><td>0.0</td><td>-0.7</td></tr><tr><td>Indonesia</td><td>5.8</td><td>5.8</td><td>5.6</td><td>NA</td><td>0.1</td><td>NA</td></tr><tr><td>Taiwan</td><td>2.0</td><td>2.0</td><td>2.1</td><td>1.9</td><td>-0.1</td><td>0.1</td></tr><tr><td>Thailand</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.0</td><td>-0.1</td><td>0.0</td></tr><tr><td>Philippines</td><td>4.8</td><td>5.5</td><td>5.1</td><td>NA</td><td>0.4</td><td>NA</td></tr><tr><td>Vietnam</td><td>4.5</td><td>4.5</td><td>4.9</td><td>NA</td><td>-0.4</td><td>NA</td></tr><tr><td>Malaysia</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>-0.1</td><td>0.0</td></tr></table>

Note: Red shading indicates GS forecast above consensus forecast or market pricing, and blue shading indicates GS forecast below consensus forecast or market pricing.  
\* Global policy rate forecasts represent a GDP-weighted average of the economies with both consensus forecasts and market pricing available.

## Changes in Policy Rates and Financial Conditions

Exhibit 4: Recent Policy Rate Changes  
![](images/676f76fed9545a23c4680abb6a10ee2b639a14bfbbeb165c2716d909211c9d95.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 5: Change in Average Global Policy Rate Over Time  
![](images/6e5d200c7a5bf2025e24a98062e21c06dcbf4bcee39ad717dace078a6aeb8b50.jpg)  
Source: GS Global Investment Research

Exhibit 6: Changes in Financial Conditions Over the Last 3 Months  
![](images/d758405e1cb91ebc80c8b43e6b3d2b681246a1663f25eebe90c8ac89026ceb4a.jpg)  
Source: GS Global Investment Research

Exhibit 7: Changes in Financial Conditions Over the Last 12 Months  
![](images/bafb55e9c723a03f99f34f12ba076d4e618ba50c17f8b0abcaa6a1a4744a8473.jpg)  
Source: GS Global Investment Research

## Policy Rate Forecasts

Exhibit 8: Policy Rate Forecast Revisions in Last 30 Days  
![](images/1ca27c56e1201d4d9fe0111ef88f2a34489691046c0b043d2361b79586b3bbec.jpg)  
Source: GS Global Investment Research

Exhibit 9: GS Forecast Policy Rate Changes  
![](images/a9ad4cef4391e5e57f142b2ea673ea55aa875cdb796d2bf3a9acdc8e99b87b76.jpg)  
Source: GS Global Investment Research

## Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing

![](images/d98816de227dcfa99271195d38a824584831f557c48bb81adb13e0fec9977882.jpg)

![](images/aaa6a715b2b89418eb633b1dfc23d48e667dd48174de28d62ed66c0f636b2e7f.jpg)

![](images/0f7d1b742e1d632be8b95471c80df710b133930cbb675d5c4dfd2cc5c0876181.jpg)

![](images/f4b93b2521f143e2fa7b75becc4598b12a942908a7e0871a7e99aa2dd936def9.jpg)

![](images/949b76bc20780fc8306698217a9254f65d14bf0b952c65f255833d8764894121.jpg)

![](images/cad9580bd436ff322fa70ca7ec4374769c5e8d97a0d0ef1e69fe7efb0d4f4565.jpg)

![](images/2a2b7e9916c4c601011bf0b31dc40ed5d7fc7f76ee19051500e580d83df9ae51.jpg)  
We exclude economies where GS forecasts differ from market pricing and consensus by more than 3pp due to data quality concerns, as well as economies where policy rate forecasts exceed $10\%$ for easier exposition.  
Source: GS Global Investment Research, Bloomberg

Exhibit 12: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing

<table><tr><td rowspan="4"></td><td colspan="7">Year-End Policy Rate, Percent</td></tr><tr><td rowspan="3">Latest</td><td colspan="3">End-2026</td><td colspan="3">End-2027</td></tr><tr><td colspan="3">Policy Rate Forecasts</td><td colspan="3">Policy Rate Forecasts</td></tr><tr><td>GS</td><td>Consensus</td><td>Market Pricing</td><td>GS</td><td>Consensus</td><td>Market Pricing</td></tr><tr><td>Global*</td><td>4.6</td><td>4.7</td><td>4.6</td><td>4.5</td><td>4.0</td><td>4.1</td><td>4.5</td></tr><tr><td colspan="8">Developed Economies</td></tr><tr><td>US</td><td>3.6</td><td>3.6</td><td>3.7</td><td>4.0</td><td>3.1</td><td>3.4</td><td>3.8</td></tr><tr><td>Euro Area</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.0</td><td>2.3</td><td>2.5</td></tr><tr><td>Japan</td><td>1.0</td><td>1.0</td><td>1.3</td><td>1.2</td><td>1.5</td><td>1.5</td><td>1.7</td></tr><tr><td>UK</td><td>3.8</td><td>3.8</td><td>3.9</td><td>4.0</td><td>3.0</td><td>3.3</td><td>3.9</td></tr><tr><td>Canada</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.4</td><td>2.8</td><td>2.8</td><td>2.9</td></tr><tr><td>Australia</td><td>4.4</td><td>4.6</td><td>4.4</td><td>4.5</td><td>3.6</td><td>4.2</td><td>4.2</td></tr><tr><td>Switzerland</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.1</td></tr><tr><td>Sweden</td><td>1.8</td><td>2.0</td><td>1.9</td><td>1.9</td><td>2.3</td><td>2.0</td><td>2.1</td></tr><tr><td>Hong Kong</td><td>2.8</td><td>2.1</td><td>NA</td><td>NA</td><td>1.9</td><td>NA</td><td>NA</td></tr><tr><td>New Zealand</td><td>2.3</td><td>2.8</td><td>2.6</td><td>2.8</td><td>2.8</td><td>3.1</td><td>3.3</td></tr><tr><td colspan="8">Latam</td></tr><tr><td>Brazil</td><td>14.3</td><td>14.0</td><td>13.4</td><td>-0.1</td><td>12.0</td><td>11.5</td><td>0.9</td></tr><tr><td>Mexico</td><td>6.5</td><td>6.5</td><td>6.5</td><td>6.9</td><td>6.5</td><td>6.5</td><td>7.6</td></tr><tr><td>Colombia</td><td>11.3</td><td>12.3</td><td>11.9</td><td>11.7</td><td>11.3</td><td>10.6</td><td>10.1</td></tr><tr><td>Chile</td><td>4.5</td><td>4.5</td><td>4.7</td><td>4.4</td><td>4.3</td><td>4.6</td><td>4.5</td></tr><tr><td>Peru</td><td>4.3</td><td>4.3</td><td>4.3</td><td>NA</td><td>4.3</td><td>4.5</td><td>NA</td></tr><tr><td colspan="8">CEEMEA</td></tr><tr><td>Russia</td><td>14.3</td><td>12.0</td><td>13.0</td><td>NA</td><td>8.0</td><td>9.5</td><td>NA</td></tr><tr><td>Turkiye</td><td>37.0</td><td>37.0</td><td>35.2</td><td>39.4</td><td>29.0</td><td>26.4</td><td>NA</td></tr><tr><td>Poland</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.5</td><td>3.6</td><td>3.8</td></tr><tr><td>Israel</td><td>3.8</td><td>3.3</td><td>3.6</td><td>3.9</td><td>3.3</td><td>3.2</td><td>3.5</td></tr><tr><td>Egypt</td><td>19.0</td><td>21.0</td><td>NA</td><td>NA</td><td>14.0</td><td>NA</td><td>NA</td></tr><tr><td>South Africa</td><td>7.0</td><td>7.3</td><td>7.0</td><td>7.3</td><td>6.5</td><td>6.4</td><td>7.2</td></tr><tr><td>Romania</td><td>6.5</td><td>6.5</td><td>6.3</td><td>NA</td><td>4.5</td><td>5.2</td><td>NA</td></tr><tr><td>Czech Republic</td><td>3.5</td><td>3.8</td><td>3.6</td><td>4.0</td><td>3.0</td><td>3.5</td><td>4.0</td></tr><tr><td>Hungary</td><td>6.0</td><td>5.3</td><td>5.9</td><td>5.0</td><td>4.0</td><td>5.0</td><td>4.7</td></tr><tr><td>Ukraine</td><td>15.0</td><td>13.5</td><td>14.2</td><td>NA</td><td>11.5</td><td>12.3</td><td>NA</td></tr><tr><td>Ghana</td><td>14.0</td><td>14.0</td><td>13.2</td><td>NA</td><td>16.0</td><td>13.3</td><td>NA</td></tr><tr><td>Kazakhstan</td><td>17.0</td><td>15.5</td><td>16.2</td><td>NA</td><td>11.0</td><td>NA</td><td>NA</td></tr><tr><td colspan="8">Asia</td></tr><tr><td>Mainland China</td><td>1.4</td><td>1.4</td><td>NA</td><td>NA</td><td>1.3</td><td>NA</td><td>NA</td></tr><tr><td>India</td><td>5.3</td><td>5.8</td><td>5.5</td><td>5.6</td><td>5.8</td><td>5.6</td><td>6.1</td></tr><tr><td>South Korea</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.7</td><td>3.3</td><td>3.1</td><td>4.0</td></tr><tr><td>Indonesia</td><td>5.8</td><td>5.8</td><td>5.6</td><td>NA</td><td>5.8</td><td>5.2</td><td>NA</td></tr><tr><td>Taiwan</td><td>2.0</td><td>2.0</td><td>2.1</td><td>1.9</td><td>2.0</td><td>2.1</td><td>1.9</td></tr><tr><td>Thailand</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.2</td></tr><tr><td>Philippines</td><td>4.8</td><td>5.5</td><td>5.1</td><td>NA</td><td>5.5</td><td>4.9</td><td>NA</td></tr><tr><td>Vietnam</td><td>4.5</td><td>4.5</td><td>4.9</td><td>NA</td><td>4.5</td><td>4.8</td><td>NA</td></tr><tr><td>Malaysia</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.9</td><td>NA</td></tr></table>

Note: Red shading indicates consensus forecast or market pricing above GS forecast, and blue shading indicates consensus forecast or market pricing below GS forecast.  
\* Global policy rate forecasts represent a GDP-weighted average of the economies with both consensus forecasts and market pricing available.

## Policy Rate Forecast Drivers

Exhibit 13: GS Growth and Policy Rate Forecasts vs. Bloomberg Consensus Forecasts  
![](images/e064bc28aec7076a713383a178bb494cc90649f057c8a98e0905b777304cb602.jpg)  
Source: GS Global Investment Research, Bloomberg

Exhibit 14: GS GDP Growth Forecasts vs. Central Bank and Bloomberg Consensus Forecasts

<table><tr><td rowspan="3"></td><td rowspan="2">End-2025</td><td colspan="6">Real GDP Growth (Annual Average), Percent Change</td></tr><tr><td colspan="3">End-2026</td><td colspan="3">End-2027</td></tr><tr><td>Actual****</td><td>GS</td><td>GS - Central Bank</td><td>GS - Consensus</td><td>GS</td><td>GS - Central Bank</td><td>GS - Consensus</td></tr><tr><td>Global*</td><td>1.8</td><td>1.7</td><td>NA</td><td>0.0</td><td>1.9</td><td>NA</td><td>0.3</td></tr><tr><td colspan="8">Developed Economies</td></tr><tr><td>US**</td><td>2.0</td><td>2.0</td><td>-0.2</td><td>-0.1</td><td>2.2</td><td>-0.1</td><td>0.1</td></tr><tr><td>Euro Area</td><td>1.5</td><td>0.5</td><td>-0.3</td><td>-0.1</td><td>1.2</td><td>0.0</td><td>0.6</td></tr><tr><td>Japan***</td><td>0.8</td><td>0.5</td><td>-0.2</td><td>NA</td><td>1.2</td><td>0.4</td><td>NA</td></tr><tr><td>UK**</td><td>1.0</td><td>1.2</td><td>-0.1</td><td>0.2</td><td>1.6</td><td>0.0</td><td>0.6</td></tr><tr><td>Canada**</td><td>0.7</td><td>1.6</td><td>-0.2</td><td>0.6</td><td>2.0</td><td>0.6</td><td>0.9</td></tr><tr><td>Australia</td><td>2.0</td><td>1.7</td><td>0.4</td><td>-0.3</td><td>2.2</td><td>0.8</td><td>0.2</td></tr><tr><td>Switzerland</td><td>1.5</td><td>0.9</td><td>-0.1</td><td>-0.2</td><td>1.5</td><td>0.0</td><td>0.4</td></tr><tr><td>Sweden</td><td>1.7</td><td>1.7</td><td>1.9</td><td>-0.3</td><td>2.0</td><td>0.7</td><td>0.0</td></tr><tr><td>Hong Kong</td><td>3.6</td><td>4.6</td><td>NA</td><td>1.2</td><td>2.5</td><td>NA</td><td>-1.0</td></tr><tr><td>New Zealand</td><td>0.2</td><td>2.1</td><td>0.4</td><td>0.5</td><td>2.5</td><td>-1.1</td><td>0.9</td></tr><tr><td colspan="8">Latam</td></tr><tr><td>Brazil</td><td>2.3</td><td>2.2</td><td>0.2</td><td>0.3</td><td>1.6</td><td>NA</td><td>-0.3</td></tr><tr><td>Mexico</td><td>0.5</td><td>1.2</td><td>-0.4</td><td>0.1</td><td>1.7</td><td>-0.3</td><td>0.6</td></tr><tr><td>Colombia</td><td>2.6</td><td>2.4</td><td>0.0</td><td>0.0</td><td>2.4</td><td>0.3</td><td>0.0</td></tr><tr><td>Chile</td><td>2.5</td><td>1.6</td><td>NA</td><td>-0.1</td><td>2.6</td><td>NA</td><td>0.9</td></tr><tr><td>Peru</td><td>3.4</td><td>3.4</td><td>0.5</td><td>0.5</td><td>2.5</td><td>NA</td><td>-0.4</td></tr><tr><td colspan="8">CEEMEA</td></tr><tr><td>Russia**</td><td>1.0</td><td>0.9</td><td>NA</td><td>0.0</td><td>1.8</td><td>NA</td><td>1.0</td></tr><tr><td>Turkiye</td><td>3.6</td><td>2.7</td><td>NA</td><td>NA</td><td>3.6</td><td>NA</td><td>NA</td></tr><tr><td>Poland**</td><td>3.8</td><td>3.3</td><td>-0.8</td><td>-0.1</td><td>3.6</td><td>1.5</td><td>0.1</td></tr><tr><td>Israel</td><td>3.2</td><td>2.2</td><td>-2.4</td><td>-0.9</td><td>4.8</td><td>NA</td><td>1.7</td></tr><tr><td>Egypt</td><td>4.4</td><td>4.7</td><td>NA</td><td>0.2</td><td>4.7</td><td>NA</td><td>0.2</td></tr><tr><td>South Africa</td><td>1.1</td><td>1.6</td><td>-0.3</td><td>0.4</td><

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
