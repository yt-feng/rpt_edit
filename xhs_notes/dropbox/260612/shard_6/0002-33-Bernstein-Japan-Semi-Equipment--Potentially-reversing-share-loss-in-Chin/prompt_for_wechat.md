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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Japan Semiconductors

# Japan Semi Equipment: Potentially reversing share loss in China?

![](images/bf81d71162499fe65c01fa744a7cba415ae6a39d6654da47f5cbbc48ae729e34.jpg)

David Dai, CFA

+852 2918 5704

david.dai@bernsteinsg.com

![](images/43b5f928f92e0b50cdccafbf4b205056ee23b7801d9f7ed7e7753f7040692dea.jpg)

Qingyuan Lin, Ph.D.

+852 2123 2654

qingyuan.lin@bernsteinsg.com

![](images/882b753a54ddcd8042834a1a897ea55f72422ec1de566801da405b4a5c815c19.jpg)

Juho Hwang

+852 2123 2632

juho.hwang@bernsteinsg.com

![](images/b868f45c2d8d35c8e036a97433ea4dbeea9b1cc19820a2f766505ab9eb787498.jpg)

Francis Ma

+852 2123 2626

francis.ma@bernsteinsg.com

![](images/dea3f61a1a3ad987bd649c80a97c4b021b071fe9bc85926d243b64ff373019d3.jpg)

Carmine Milano, CFA

+44 20 7762 1857

carmine.milano@bernsteinsg.com

![](images/cda6930502247b44ebc2616997bc2014f2252907658100c7afb8dd12a6052fa2.jpg)

Jack Lin

+852 2123 2683

jack.lin@bernsteinsg.com

Japanese equipment makers have been losing share in China, not only to Chinese domestic makers but to other overseas makers. Their market share among imports dropped from 26% in 2024 to 23% in 2025. Before that, their market share in China among imports peaked in 2021 at 30%. We believe that is one of the major concerns for investors, but the trend may reverse going onward.

The share loss can be explained: FX was a big reason for the nominal share loss. The JPY has depreciated 31.5% over the last 5 years, and Japanese WFE players tend to price their products in JPY. Adjusting for which the market share would have been 31%/26% (instead of 26%/23%) respectively in 2024/25, vs. 2023 adjusted market share of 27%, or 2021 share of 28%. Investment timing was another major reason, causing Japan to lose share in 2025 after gaining share in 2024. We believe some of the customers with historically higher Japanese presence such as CXMT not placing many orders in 2025 may have also caused some optical market share loss. Averaging out market share in 2024 and 25, the Japanese WFE companies' FX adjusted market share in China among imported equipment would be 28.6%, which is on par with average market share in 21-23 of 28.1%. This also suggests that 2025 share loss is mainly due to timing for order rather than structural loss. There are also some specific reasons for each individual company. All 3 front end equipment companies (TEL/Screen/Kokusai) lost share in 2025, but for different reasons. For Tokyo Electron, it was likely due to customer / process-step mix and timing, as well as historically less aggressive pricing. For Screen, it was likely due to order timing and customers' localization attempts, as cleaning is a segment where locals have become more credible, while for Kokusai it was likely mostly due to CXMT's investment timing.

We expect the Japanese equipment makers to reverse the share loss in China going forward. The FX should no longer be a headwind, and because of yen depreciation, the Japanese equipment is of considerably good value which allows them to raise prices. This, coupled with normalization of investment pattern among the Chinese customers, should allow the Japanese equipment makers to gain market share in China. Although Japan's market share among import hasn't necessarily been impressive YTD, we expect them to regain share in going forward as Chinese customers seem to have been ordering increasingly from Japan again, and we believe Japanese equipment makers have started to raise prices more actively. Specifically, Tokyo Electron (OP) has been more vocal on pricing, especially in China where certain tools remain difficult to be replaced by locals. Customer mix normalizing should also help. Kokusai (OP) could see China memory capacity expansion cycle to support demand, and we believe their core areas are not yet fully caught up by local competition. Screen (MP) expects orders from CXMT to come back after 2 years of no orders, as well as a sizeable order from JHICC.

We are positive on front end equipment companies — Tokyo Electron, Kokusai as well as Screen especially after the recent commodity / materials rally. SPEs have been underperforming the commodity semi names (memory, analog, substrate, wafer, etc.) in the past 2-3 months. We expect the strength for SPE companies to recover as investors recognize the capex increase in the next few years, as well as their potential share gain in China, and prefer TEL (OP) and Kokusai (OP).

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">11 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Reported EPS</td><td colspan="3">Reported P/E (x)</td></tr><tr><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>8035.JP (Tokyo Electron)</td><td>O</td><td>JPY</td><td>63,400</td><td>59,200</td><td>114.7%</td><td>JPY</td><td>1,250.88</td><td>1,504.14</td><td>1,848.77</td><td>50.7</td><td>42.2</td><td>34.3</td></tr><tr><td>7735.JP (Screen)</td><td>M</td><td>JPY</td><td>12,990</td><td>12,600</td><td>97.2%</td><td>JPY</td><td>486.61</td><td>572.60</td><td>662.24</td><td>26.7</td><td>22.7</td><td>19.6</td></tr><tr><td>6525.JP (Kokusai)</td><td>O</td><td>JPY</td><td>8,042.00</td><td>8,240.00</td><td>103.9%</td><td>JPY</td><td>128.63</td><td>200.23</td><td>274.61</td><td>62.5</td><td>40.2</td><td>29.3</td></tr><tr><td>002371.CH (NAURA)</td><td>O</td><td>CNY</td><td>637.50</td><td>680.00</td><td>71.1%</td><td>CNY</td><td>5.66</td><td>10.22</td><td>16.41</td><td>112.6</td><td>62.4</td><td>38.9</td></tr><tr><td>688012.CH (AMEC)</td><td>O</td><td>CNY</td><td>303.12</td><td>500.00</td><td>130.4%</td><td>CNY</td><td>3.40</td><td>4.95</td><td>7.18</td><td>89.2</td><td>61.3</td><td>42.2</td></tr><tr><td>688072.CH (Piotech)</td><td>O</td><td>CNY</td><td>655.27</td><td>580.00</td><td>322.3%</td><td>CNY</td><td>3.32</td><td>8.12</td><td>12.40</td><td>197.4</td><td>80.7</td><td>52.9</td></tr><tr><td>ASML (ASML)</td><td>O</td><td>USD</td><td>1,734.19</td><td>1,971.00</td><td>98.4%</td><td>USD</td><td>27.95</td><td>36.96</td><td>53.13</td><td>53.6</td><td>40.5</td><td>28.2</td></tr><tr><td>ASML.NA (ASML)</td><td>O</td><td>EUR</td><td>1,507.20</td><td>1,700.00</td><td>109.2%</td><td>EUR</td><td>24.72</td><td>32.69</td><td>46.98</td><td>61.0</td><td>46.1</td><td>32.1</td></tr><tr><td>JPL</td><td></td><td></td><td>2,508.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>ASIAX</td><td></td><td></td><td>1,911.22</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SPX</td><td></td><td></td><td>7,394.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EDME</td><td></td><td></td><td>1,541.87</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We rate Tokyo Electron (TP=¥59,200) and Kokusai (TP=¥8,240.00 Outperform, and Screen (TP=¥12,600) Market-Perform.

We rate ASML (PT=€1,700.00) Outperform.

We rate Naura Outperform, with TP at CNY 680.

We rate AMEC Outperform, with TP at CNY 500.

We rate Piotech Outperform, with TP at CNY 580.

## DETAILS

Japanese equipment makers, led by TEL, have been underperforming global peers in 2025 in growth and market share. One big reason for that is China, which represents c. $42\%$ of global WFE as of 2025, where Japanese equipment makers have been losing share. In today's report, we examine the cause of the share loss, and discuss the future market share trend in China.

Japanese equipment makers have been losing share in China, not only to Chinese domestic makers but to other overseas makers. Their market share among imports dropped from 26% in 2024 to 23% in 2025. Before that, their market share in China among imports peaked in 2021 at 30%. However, we believe the trend may reverse going forward.

Japanese makers have been losing share in 2025 not only to domestic competition but among global players as well. Alongside China WFE market growth, WFE imports to China has been on a constant rise (Exhibit 1). Although, Japan's market share within WFE imports has been on a constant decline since 2021 peak. The absolute dollar amount of Japan-origin imports also fell in 2025 from the 2024 peak, and 2026 YTD (up to April) run-rate also appears lower than the 2025 level (Exhibit 2).

EXHIBIT 1: WFE imports to China has been on a constant rise...  
![](images/170a6d1fd98d30e0c0fd6b7350b9b403a228c6ee0f0298963eb25b7d3bf81d86.jpg)

<details>
<summary>bar chart</summary>

Total China WFE imports (USD bn)
| Year | Total China WFE imports (USD bn) |
| :--- | :--- |
| 2015 | 4.8 |
| 2016 | 5.8 |
| 2017 | 7.1 |
| 2018 | 12.7 |
| 2019 | 11.9 |
| 2020 | 15.3 |
| 2021 | 23.8 |
| 2022 | 22.0 |
| 2023 | 31.5 |
| 2024 | 37.9 |
| 2025 | 39.2 |
| 2026 YTD | 10.0 |
</details>

Source: General Administrations of Customs of PRC, Bernstein analysis.

EXHIBIT 2: ...but Japan has been constantly dropping market share since 2022.  
![](images/e3af368ad4c1f91820e3071066f583d0482854f53f085784b9073445e5841472.jpg)

<details>
<summary>bar-line hybrid</summary>

2015-2026 YTD: WFE imports from Japan (USD bn)
| Year | Imports from Japan (USD bn) | % Market share (%) |
| :--- | :--- | :--- |
| 2015 | 0.9 | 20 |
| 2016 | 1.3 | 24 |
| 2017 | 1.7 | 26 |
| 2018 | 3.1 | 26 |
| 2019 | 3.1 | 28 |
| 2020 | 4.3 | 30 |
| 2021 | 7.1 | 31 |
| 2022 | 6.1 | 29 |
| 2023 | 7.7 | 25 |
| 2024 | 9.9 | 27 |
| 2025 | 8.8 | 23 |
| 2026 YTD | 2.2 | 22 |
</details>

Source: General Administration of Customs of PRC, Bernstein analysis.

A big part of the reason for nominal share loss was FX. We would not attribute all of this to pure market share loss to competition. Firstly, the Japanese yen has depreciated 31.5% over the last 5 years (Exhibit 3), and we suspect that this FX movement definitely would have played a role since most of the Japanese WFE vendors price their equipment mostly in JPY. If we adjust for FX, Japan's market share loss can be seen as largely stable (Exhibit 4).

EXHIBIT 3: JPY has depreciated 31.5% over the last 5 years.  
![](images/ad14a91f489f16cf37dc5bc35cc31324336c06394a66022490953b3dd52a0d9d.jpg)

<details>
<summary>line chart</summary>

| Date   | USDJPY |
|--------|--------|
| Jun-21 | 110    |
| Jun-22 | 130    |
| Jun-23 | 145    |
| Jun-24 | 160    |
| Jun-25 | 150    |
| Jun-26 | 160    |
</details>

Source: Bloomberg, Bernstein analysis.

EXHIBIT 4: FX may have some impact on Japan's market share loss as they charge customers mostly in JPY.  
![](images/6e3723b6266be81acac0ca13d75e693a5df4da41b4e8504d261d8d23c8bd137f.jpg)

<details>
<summary>line chart</summary>

2015-2026 YTD: Japan WFE import market share in China
| Year | % Market share (%) | % share (FX adjusted) (%) |
| :--- | :--- | :--- |
| 2015 | 19.5 | 19.5 |
| 2016 | 22.0 | 20.0 |
| 2017 | 24.5 | 23.0 |
| 2018 | 24.5 | 23.0 |
| 2019 | 26.0 | 24.5 |
| 2020 | 27.5 | 25.5 |
| 2021 | 29.5 | 27.5 |
| 2022 | 27.5 | 29.0 |
| 2023 | 24.5 | 27.0 |
| 2024 | 26.0 | 31.0 |
| 2025 | 23.0 | 26.0 |
| 2026 YTD | 21.5 | 26.0 |
</details>

USDJPY FX is indexed to 2015  
Source: Bloomberg, General Administration of Customs of PRC, Bernstein analysis.

The other part is timing of order from different customers. For instance, CXMT as one of the Chinese companies who used a lot of Japanese equipments not only invested less overall last year due to fab expansion timing and their funding issues, but they also had tried to localize their equipment base and ordered less from Japan.

Averaging out market share in 2024 and 2025, the Japanese WFE companies' FX adjusted market share in China among imported equipment would be $28.6\%$ , which is on par with average market share in 21-23 of $28.1\%$ . This also suggests that 2025 share loss is mainly due to timing for order rather than structural loss.

The company-level read-through is therefore more nuanced than the headline share decline. All three front-end equipment companies under our coverage appear to have lost share in 2025, but the reasons differ by company. We also believe part of the share loss could reverse in 2H26–2027, supported by customer order normalization and more active pricing by Japanese vendors.

There are also some specific reasons for each individual company. All 3 front end equipment companies (TEL/Screen/Kokusai) lost share in 2025, but for different reasons. Overall, it seems clear that Japanese WFE companies under our coverage lost some market share in 2025 (Exhibit 5, Exhibit 6), but we believe this share loss could be reversed going forward.

Tokyo Electron (OP): For TEL, we believe they wouldn't have necessarily lost POR market share even in 2025, and the nominal market share loss is attributable firstly to customer mix and their timing of investment. For instance, CXMT — for which TEL has a relatively high market share — didn't invest much last year. Secondly, TEL has historically priced less aggressively, which lost them quite a bit of market share given FX depreciation. Also, some product-level / process .step-level mix may have also impacted optical market share.

Screen (MP): For Screen, the 2025 share loss appears to have been driven by order timing and customer localization attempts. CXMT did not place meaningful orders with Screen over the last two years as it tried to localize parts of its equipment base, which likely hurt Screen's China share. Swaysure, a major customer of Screen's in China DRAM space, wasn't very successful and ceased investment in 2025, which also impacted Screen's market share.

Kokusai (OP): For Kokusai, the 2024-2025 market share loss we believe also had a lot to do with CXMT, as in 2024 we estimate CXMT accounted for around ¥47bn whereas in 2025 we believe CXMT investment faded to around ¥11bn.

EXHIBIT 5: Overall, Japanese vendors have lost some market share in 2025...  
2023-2025: China market share among foreign vendors (Overall)  
![](images/b1efcb0fddb87c09e18c3e7c0875689cced99270d04ac4751de9ab211e6e9dbe.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | TEL (%) | Screen (%) | Kokusai (%) | ASML (%) | Lam (%) | AMAT (%) | Other (%) |
|---|---|---|---|---|---|---|---|
| 2023 | 11 | 3 | 9 | 24 | 3 | 18 | 34 |
| 2024 | 13 | 4 | 8 | 26 | 1 | 16 | 32 |
| 2025 | 10 | 3 | 12 | 26 | 3 | 12 | 36 |
</details>

Source: Gartner, Company disclosures, Bernstein China Semi Team analysis and estimates.

EXHIBIT 6: ...and the trend looks more pronounced for the 4 segments with Japanese exposure.  
2023-2025: China market share among foreign vendors (Deposition+Etch+Cleaning+Thermal)  
![](images/fbe9debf315643488f99f8dcb3edd3efdb4ab0ddb530bf6adb48bd106af367f2.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | TEL (%) | Screen (%) | Kokusai (%) | Lam (%) | AMAT (%) | Other (%) |
|---|---|---|---|---|---|---|
| 2023 | 19 | 7 | 2 | 20 | 31 | 21 |
| 2024 | 23 | 8 | 3 | 17 | 28 | 22 |
| 2025 | 16 | 6 | 2 | 24 | 20 | 32 |
</details>

Source: Gartner, Company disclosures, Bernstein China Semi Team analysis and estimates.

We expect them to regain share from 2H26 onward, especially with the active price raise. Going forward, the FX should no longer be a headwind, and because of yen depreciation of \~31% over the past 5 years, the Japanese equipment is of considerably good value which allows them to raise prices. This, coupled with normalization of investment pattern among the Chinese customers, should allow the Japanese equipment makers to gain market share in China (Exhibit 7-Exhibit 9).

TEL: We expect TEL's China share to improve from the weak 2025 level as customer mix normalizes and pricing becomes more supportive. TEL has recently been more vocal on pricing, especially in China, where it sees room for price increases given that certain tools remain difficult to replace with local alternatives. The company also appears to be introducing additional surcharges for cost increases and expedited delivery. Therefore, while 2025 share may have been weak, we do not think it should be extrapolated into 2026 and beyond.

Screen: For Screen, we are now more constructive after our recent group call with the company. While they have also lost some nominal market share in 2025, Screen expects orders from CXMT to come back — who did not place orders for them in the last 2 years in an attempt to localize the equipments, a sizable order from JHICC, and YMTC ordering 1.5x of what they ordered last year. Foundry customers are expected to continue to rely heavily on Screen as well.

Kokusai: For Kokusai, we expect China memory capacity expansion to support demand, while local competition has not yet fully caught up in Kokusai's core areas. Therefore, although China thermal localization remains a medium-term risk, we do not think the 2025 China import-share data alone should change the investment thesis. Kokusai's near-term upside/downside should remain more driven by capacity constraints.

Meanwhile, SPEs have been underperforming the commodity semi names (memory, analog, substrate, wafer, etc.) in the past 2-3 months (Exhibit 10). We expect the strength for SPE companies to recover as investors recognize the capex increase in the next few years, as well as their potential share gain in China. Our pecking order in Japan frontend SPE is TEL (OP) > Kokusai (OP) > Screen (MP) for the China exposure.

EXHIBIT 7: TEL China's sales declined in FY26...  
![](images/7b8397f515b151185d504401632ef7e2983df73198b8d30723f70b7edc581b64.jpg)

<details>
<summary>bar chart</summary>

FY22-FY26: TEL China sales
| Fiscal Year | Sales (JPY bn) |
| :--- | :--- |
| FY22/3 | 510 |
| FY23/3 | 495 |
| FY24/3 | 810 |
| FY25/3 | 1010 |
| FY26/3 | 830 |
</details>

Source: Company disclosures, Bernstein analysis.

EXHIBIT 8: ...as did Screen's...  
![](images/807d134bea57ada89b2e82158112bc2441bb61e1a36fb6c76e6253a58831cb2e.jpg)

<details>
<summary>bar chart</summary>

| Fiscal Year | JPY bn |
| ----------- | ------ |
| FY22/3      | 75     |
| FY23/3      | 70     |
| FY24/3      | 180    |
| FY25/3      | 230    |
| FY26/3      | 195    |
</details>

Source: Company disclosures, Bernstein analysis

EXHIBIT 9: ...and Kokusai's, but we expect them to resume growth.  
![](images/e59697ac6b3c0e59397e7780d412524cc359904cbcf36d1e71dfc81d2532dd1d.jpg)

<details>
<summary>bar chart</summary>

FY22-FY26: Kokusai China sales
| Fiscal Year | Sales (JPY bn) |
| :--- | :--- |
| F

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
