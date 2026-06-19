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
# Greater China Semiconductors | Asia Pacific

# Power Semis – Supply Driven Upcycle

Global power discrete sales returned to growth since 4Q25. On the back of limited capacity additions in the past two years, we expect power semi pricing to rise further in 2H26. We like Yangjie (OW) on auto localization, while staying UW on Silan Micro and CR Micro on hyped expectations.

Overall power discrete sales back to growth since 4Q25: Global power discrete revenue growth is now tracking at 16% YoY in April and the yoy growth was back to positive territory since 4Q25 (Exhibit 1). Many Greater China power discrete companies issued price hike notices in Feb 2026, citing higher raw material prices and foundry costs. Except for IGBT for automotive customers, distributors and other end-market customers were willing to accept the price hikes, given low inventory and fears of even higher pricing in 2H26. We think pricing power could support gross margin, with gradual improvement expected for the rest of the year.

Mixed demand picture: robust industrial demand, slower EV growth, and weak solar demand: Auto and industrial segments accounted for 72% of total demand in power discrete in 2025, so the power semi market is less affected by weak smartphone and PC sell-through this year due to memory price hikes. Industrial demand is strong, and leading industrial automation companies' revenue grew at 21% in 1Q26 (Exhibit 4). China EV wholesale growth (3MMA) was tracking at 7% yoy in May, up from zero in April (Exhibit 3). Solar demand was weak, with YTD capacity additions down 51% yoy.

Limited supply additions in the past two years: Global leading power discrete companies' capex declined for two consecutive years, and this year we saw a mild capex increase of around 11% (Exhibit 5). In China, we expect limited capacity additions in power discrete (IGBT, MOSFET etc.) in the next three years, as companies like Silan Micro and UNT (688469.SS, NC) shift focus to AI power management (PMIC, etc.). Given limited capacity additions and high utilization, we think if demand does not sharply deteriorate, the upward pricing trend could sustain into 2H26.

## We like Yangjie (OW), and raise PTs for Yangjie, Silan Micro and CR Micro:

Although we are positive on power discrete pricing, we think it is a supply-driven upcycle. We raise PTs for Yangjie, Silan Micro and CR Micro but make no rating changes. We remain OW on Yangjie Technology – auto is rising in its mix, and operating efficiency is strong. We remain UW on Silan Micro and CR Micro on hyped expectations. We are EW on Starpower due to depreciation concerns.

MS ASIA LIMITED+

## Daisy Dai, CFA

Equity Analyst

Daisy.Dai@morganstanley.com +852 2848-7310

MS TAIWAN LIMITED+

## Charlie Chan

Equity Analyst

Charlie.Chan@morganstanley.com +886 2 2730-1725

## Daniel Yen, CFA

Equity Analyst

Daniel.Yen@morganstanley.com +886 2 2730-2863

## Tiffany Yeh

Equity Analyst

Tiffany.Yeh@morganstanley.com +886 2 7712-3032

MS ASIA LIMITED+

## Henry Zhao

Research Associate

Henry.Zhao@morganstanley.com +852 2239-7731

## Ethan Jia

Research Associate

Ethan.Jia@morganstanley.com +852 3963-2287

## Asia Summer School 2026

![](images/e4ebfb26e7ae22647a5f3eda113d63be60c9a1c9424225b625af990f1cae6142.jpg)

GREATER CHINA TECHNOLOGY SEMICONDUCTORS

<table><tr><td colspan="2">Asia Pacific Industry View</td><td>Attractive</td></tr><tr><td colspan="3">WHAT&#x27;S CHANGED</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)Price Target</td><td>FromRmb20.00</td><td>ToRmb26.90</td></tr><tr><td>Yangjie Technology (300373.SZ)Price Target</td><td>FromRmb91.00</td><td>ToRmb136.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)Price Target</td><td>FromRmb43.00</td><td>ToRmb51.60</td></tr></table>

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

Earnings Estimates Revisions

<table><tr><td>Ticker</td><td>Company</td><td>Earnings estimates revision and price target change</td></tr><tr><td>300373.SZ</td><td>Yangjie Technology</td><td>We raise EPS estimates by 3%/6%/9% for 2026/27/28 respectively: We expect stronger sales growth, mainly from better industrial demand, and we also raise our gross margin assumption on better power discrete pricing. We expect Yangjie&#x27;s overseas business could also grow strongly on the back of its Vietnam packaging and foundry capacity ramp.We raise our price target by 50% to Rmb136 from Rmb91: We factor in earnings estimate changes and raise our intermediate growth rate to 18% from 15% previously, as the company decides to allocate more funding to automotive and AI infrastructure related power devices. We continue to derive our base case/price target from a residual income model. All other assumptions are unchanged, including an 8.4% cost of equity (beta 1.06, risk-free rate 2.0% and risk premium 6.0%) and a terminal growth rate of 5.5%, in line with other semiconductor companies we cover.Our base case value/price target implies 33x our 2027e EPS.Our bull and bear case values also rise 50% to Rmb173.8 and Rmb53.4, respectively, implying 42x and 13x our 2027e EPS, in line with our base case change.</td></tr><tr><td>688396.SS</td><td>CR Micro</td><td>We raise our EPS estimates by 9%/14%/14% for 2026/27/28: We raise our sales forecasts slightly on better industrial demand, and we also raise our margin assumptions. We expect CR Micro&#x27;s power semis prices could go up further on the back of full utilization. While the company continues to expand capacity in Shenzhen, it is mainly for YMTC&#x27;s outsourcing orders, with limited capacity additions in power semis.We raise our target price by 20% to Rmb51.6 from Rmb43.0: Our new price target reflects the changes in our earnings estimates. We derive our price target from a residual income model, which we believe best captures the stock&#x27;s long-term value. Our key assumptions include: an 8.2% cost of equity (beta 1.04, risk-free rate 2.0% and risk premium 6.0%; all unchanged), a medium-term growth rate of 19% and a terminal growth rate of 5.5%. We raise our bull case to Rmb109.7 from Rmb91.4, and our bear case to Rmb24.5 from Rmb20.4, both in line with our base case/price target adjustment.</td></tr><tr><td>600460.SS</td><td>Silan Micro</td><td>We raise our 2026/27/28 EPS forecasts by 4%/6%/9%: We raise our sales forecasts slightly on better industrial demand, and we also raise our margin assumptions. Silan Micro has a higher portion of sales through distributors. We think it would be easier for them to raise prices vs. peers, which have more direct sales.We raise our price target by 35% to Rmb26.9 from Rmb20: Our new price target reflects the changes in our earnings estimates. We also raise the payout ratio to 20% from 5%, as we expect the company to increase payout given higher net margin.We continue to derive our price target (base case scenario value) from a residual income model. Our key assumptions are unchanged: an 8.6% cost of equity (beta 1.1, risk-free rate 2.0%, and risk premium 6.0%), an intermediate growth rate of 18% and a terminal growth rate of 5.5%.We raise our bull case value by 70% to Rmb61.2 from Rmb36.1, the upward revision is higher than our base case change, considering higher operating leverage of Silan&#x27;s IDM model compared to its peers (design houses or fab-lite business model). Our bear case value is raised by 35% to Rmb16.8 from Rmb12.5, due to better pricing environment and margin improvement.</td></tr></table>

## Power Semi Industry Tracker

Exhibit 1: Total discrete revenue yoy growth turned positive since 4Q25  
![](images/563a7d0f9081e0d60348cc3a4231258a0b6591e5dbfa07f0c1efa974d2a25cb4.jpg)

<details>
<summary>line chart</summary>

| Date   | Discrete YoY growth (3MMA) |
|--------|-----------------------------|
| Mar-95 | ~45%                        |
| Mar-98 | ~10%                        |
| Mar-01 | ~40%                        |
| Mar-04 | ~20%                        |
| Mar-07 | ~10%                        |
| Mar-10 | ~65%                        |
| Mar-13 | ~-20%                       |
| Mar-16 | ~15%                        |
| Mar-19 | ~10%                        |
| Mar-22 | ~35%                        |
| Mar-25 | ~15%                        |
</details>

Source: WSTS, MS

Exhibit 2: Auto and industrial accounted for 70% of end demand in discrete semiconductors (2025)  
![](images/715dddb17386ec9f4d6448fd7e6c8fa3cc40eff7bd052fd954c8074bc137242c.jpg)

<details>
<summary>pie chart</summary>

| Category | Percentage (%) |
| :--- | :--- |
| Auto | 41 |
| Industrial | 31 |
| Consumer | 12 |
| Communication | 8 |
| Data processing | 8 |
</details>

Source: Gartner, MS

Exhibit 3: China EV wholesale growth is turning incrementally positive  
![](images/1cfae95d23a302502620689c36e61863dd08ad7502cc1d27a75b28980d67ddad.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Month    | China EV (whole sales, k unit) | China EV wholesale YoY (3MMA, RHS) |
| -------- | ------------------------------ | ---------------------------------- |
| Jan-23   | 400                            | 10%                                |
| Feb-23   | 500                            | 8%                                 |
| Mar-23   | 600                            | 15%                                |
| Apr-23   | 700                            | 20%                                |
| May-23   | 800                            | 25%                                |
| Jun-23   | 900                            | 30%                                |
| Jul-23   | 1000                           | 35%                                |
| Aug-23   | 1100                           | 40%                                |
| Sep-23   | 1200                           | 45%                                |
| Oct-23   | 1300                           | 50%                                |
| Nov-23   | 1400                           | 55%                                |
| Dec-23   | 1500                           | 60%                                |
| Jan-24   | 1600                           | 65%                                |
| Feb-24   | 1700                           | 70%                                |
| Mar-24   | 1800                           | 75%                                |
| Apr-24   | 1900                           | 80%                                |
| May-24   | 2000                           | 85%                                |
| Jun-24   | 2100                           | 90%                                |
| Jul-24   | 2200                           | 95%                                |
| Aug-24   | 2300                           | 100%                               |
| Sep-24   | 2400                           | 105%                               |
| Oct-24   | 2500                           | 110%                               |
| Nov-24   | 2600                           | 115%                               |
| Dec-24   | 2700                           | 120%                               |
| Jan-25   | 2800                           | 125%                               |
| Feb-25   | 2900                           | 130%                               |
| Mar-25   | 3000                           | 135%                               |
| Apr-25   | 3100                           | 140%                               |
| May-25   | 3200                           | 145%                               |
| Jun-25   | 3300                           | 150%                               |
| Jul-25   | 3400                           | 155%                               |
| Aug-25   | 3500                           | 160%                               |
| Sep-25   | 3600                           | 165%                               |
| Oct-25   | 3700                           | 170%                               |
| Nov-25   | 3800                           | 175%                               |
| Dec-25   | 3900                           | 180%                               |
| Jan-26   | 4000                           | 185%                               |
| Feb-26   | 4100                           | 190%                               |
| Mar-26   | 4200                           | 195%                               |
| Apr-26   | 4300                           | 200%                               |
| May-26   | 4400                           | 205%                               |
| Jun-26   | 4500                           | 210%                               |
| Jul-26   | 4600                           | 215%                               |
| Aug-26   | 4700                           | 220%                               |
| Sep-26   | 4800                           | 225%                               |
| Oct-26   | 4900                           | 230%                               |
| Nov-26   | 5000                           | 235%                               |
| Dec-26   | 5100                           | 240%                               |
| Jan-27   | 5200                           | 245%                               |
| Feb-27   | 5300                           | 250%                               |
| Mar-27   | 5400                           | 255%                               |
| Apr-27   | 5500                           | 260%                               |
| May-27   | 5600                           | 265%                               |
| Jun-27   | 5700                           | 270%                               |
| Jul-27   | 5800                           | 275%                               |
| Aug-27   | 5900                           | 280%                               |
| Sep-27   | 6000                           | 285%                               |
| Oct-27   | 6100                           | 290%                               |
| Nov-27   | 6200                           | 295%                               |
| Dec-27   | 6300                           | 300%                               |
| Jan-28   | 6400                           | 305%                               |
| Feb-28   | 6500                           | 310%                               |
| Mar-28   | 6600                           | 315%                               |
| Apr-28   | 6700                           | 320%                               |
| May-28   | 6800                           | 325%                               |
| Jun-28   | 6900                           | 330%                               |
| Jul-28   | 7000                           | 335%                               |
| Aug-28   | 7100                           | 340%                               |
| Sep-28   | 7200                           | 345%                               |
| Oct-28   | 7300                           | 350%                               |
| Nov-28   | 7400                           | 355%                               |
| Dec-28   | 7500                           | 360%                               |
| Jan-29   | 7600                           | 365%                               |
| Feb-29   | 7700                           | 370%                               |
| Mar-29   | 7800                           | 375%                               |
| Apr-29   | 7900                           | 380%                               |
| May-29   | 8000                           | 385%                               |
| Jun-29   | 8100                           | 390%                               |
| Jul-29   | 8200                           | 395%                               |
| Aug-29   | 8300                           | 400%                               |
| Sep-29   | 8400                           | 405%                               |
| Oct-29   | 8500                           | 410%                               |
| Nov-29   | 8600                           | 415%                               |
| Dec-29   | 8700                           | 420%                               |
| Jan-30   | 8800                           | -1%                                |
| Feb-30   | 8900                           | -1%                                |
| Mar-31   | 9000                           | -1%                                |
| Apr-31   | 9100                           | -1%                                |
| May-31   | 9200                           | -1%                                |
| Jun-31   | 9300                           | -1%                                |
| Jul-31   | 9400                           | -1%                                |
| Aug-31   | 9500                           | -1%                                |
| Sep-31   | 9600                           | -1%                                |
| Oct-31   | 9700                           | -1%                                |
| Nov-31   | 9800                           | -1%                                |
| Dec-31   | 9900                           | -1%                                |
| Jan-32   | -1                   | -1%                                |
| Feb-32   | -1                   | -1%                                |
| Mar-32   | -1                   | -1%                                |
| Apr-32   | -1                   | -1%                                |
| May-32   | -1                   | -1%                                |
| Jun-32   | -1                   | -1%                                |
| Jul-32   | -1                   | -1%                                |
| Aug-32   | -1                   | -1%                                |
| Sep-32   | -1                   | -1%                                |
| Oct-32   | -1                   | -1%                                |
| Nov-32   | -1                   | -1%                                |
| Dec-32   | -1                   | -1%                                |
| Jan-33   

[中间内容因长度限制已省略]

td><td>O (11/25/2025)</td><td>NT$517.00</td></tr><tr><td>Hua Hong Semiconductor Ltd (1347.HK)</td><td>E (03/12/2026)</td><td>HK$159.20</td></tr><tr><td>Iluvatar CoreX Semiconductor Co., Ltd. (9903.HK)</td><td>O (04/27/2026)</td><td>HK$520.00</td></tr><tr><td>King Yuan Electronics Co Ltd (2449.TW)</td><td>O (03/03/2023)</td><td>NT$280.50</td></tr><tr><td>Maxscend Microelectronics Co Ltd (300782.SZ)</td><td>U (01/11/2021)</td><td>Rmb99.80</td></tr><tr><td>MediaTek (2454.TW)</td><td>O (11/28/2025)</td><td>NT$4,460.00</td></tr><tr><td>MetaX Integrated Circuits (688802.SS)</td><td>E (04/27/2026)</td><td>Rmb732.50</td></tr><tr><td>Nanya Technology Corp. (2408.TW)</td><td>O (05/28/2026)</td><td>NT$437.00</td></tr><tr><td>NAURA Technology Group Co Ltd (002371.SZ)</td><td>O (11/06/2023)</td><td>Rmb704.22</td></tr><tr><td>OmniVision Integrated Circuits Group Inc (603501.SS)</td><td>E (11/17/2025)</td><td>Rmb90.12</td></tr><tr><td>Phison Electronics Corp (8299.TWO)</td><td>E (02/25/2026)</td><td>NT$2,330.00</td></tr><tr><td>SG Micro Corp. (300661.SZ)</td><td>E (11/03/2025)</td><td>Rmb131.55</td></tr><tr><td>Silergy Corp. (6415.TW)</td><td>U (05/19/2026)</td><td>NT$572.00</td></tr><tr><td>SMIC (0981.HK)</td><td>O (10/21/2025)</td><td>HK$75.75</td></tr><tr><td>TSMC (2330.TW)</td><td>O (02/07/2022)</td><td>NT$2,385.00</td></tr><tr><td>UMC (2303.TW)</td><td>O (05/19/2026)</td><td>NT$140.00</td></tr><tr><td>Vanguard International Semiconductor (5347.TWO)</td><td>E (01/14/2026)</td><td>NT$166.50</td></tr><tr><td>WIN Semiconductors Corp (3105.TWO)</td><td>U (07/14/2025)</td><td>NT$519.00</td></tr></table>

<table><tr><td colspan="3">Daisy Dai, CFA</td></tr><tr><td>ASMPT Ltd (0522.HK)</td><td>O (07/24/2025)</td><td>HK$210.00</td></tr><tr><td>China Resources Microelectronics Limited (688396.SS)</td><td>U (03/02/2026)</td><td>Rmb73.78</td></tr><tr><td>Elan Microelectronics Corp (2458.TW)</td><td>O (10/03/2025)</td><td>NT$156.50</td></tr><tr><td>Empyrean Technology Co Ltd (301269.SZ)</td><td>E (01/17/2025)</td><td>Rmb105.01</td></tr><tr><td>Hangzhou Silan Microelectronics Co. Ltd. (600460.SS)</td><td>U (08/25/2025)</td><td>Rmb40.83</td></tr><tr><td>Innoscience (2577.HK)</td><td>E (10/13/2025)</td><td>HK$63.05</td></tr><tr><td>JCET Group Co Ltd (600584.SS)</td><td>E (01/16/2026)</td><td>Rmb81.76</td></tr><tr><td>Shanghai Fudan Microelectronics (1385.HK)</td><td>O (03/07/2025)</td><td>HK$29.48</td></tr><tr><td>SICC Co Ltd (688234.SS)</td><td>O (03/20/2026)</td><td>Rmb149.66</td></tr><tr><td>StarPower Semiconductor Ltd (603290.SS)</td><td>E (05/14/2026)</td><td>Rmb130.98</td></tr><tr><td>Unigroup Guoxin Microelectronics Co Ltd (002049.SZ)</td><td>U (01/10/2023)</td><td>Rmb80.00</td></tr><tr><td>Universal Scientific Ind. (Shanghai) (601231.SS)</td><td>O (11/05/2025)</td><td>Rmb37.08</td></tr><tr><td>Yangjie Technology (300373.SZ)</td><td>O (06/10/2022)</td><td>Rmb114.10</td></tr></table>

<table><tr><td colspan="3">Daniel Yen, CFA</td></tr><tr><td>AP Memory Technology Corp (6531.TW)</td><td>O (07/11/2025)</td><td>NT$933.00</td></tr><tr><td>ASMedia Technology Inc (5269.TW)</td><td>U (10/03/2025)</td><td>NT$1,425.00</td></tr><tr><td>Aspeed Technology (5274.TWO)</td><td>O (06/09/2025)</td><td>NT$18,485.00</td></tr><tr><td>Egis Technology Inc (6462.TWO)</td><td>E (01/28/2026)</td><td>NT$112.50</td></tr><tr><td>Espressif Systems (688018.SS)</td><td>O (05/15/2023)</td><td>Rmb122.40</td></tr><tr><td>GigaDevice Semiconductor Beijing Inc (603986.SS)</td><td>O (05/15/2025)</td><td>Rmb586.04</td></tr><tr><td>Macronix International Co Ltd (2337.TW)</td><td>O (09/18/2025)</td><td>NT$161.50</td></tr><tr><td>Montage Technology Co Ltd (6809.HK)</td><td>O (03/18/2026)</td><td>HK$420.60</td></tr><tr><td>Montage Technology Co Ltd (688008.SS)</td><td>O (03/18/2026)</td><td>Rmb262.50</td></tr><tr><td>Novatek (3034.TW)</td><td>U (02/04/2026)</td><td>NT$515.00</td></tr><tr><td>Nuvoton Technology Corporation (4919.TW)</td><td>U (11/10/2025)</td><td>NT$187.50</td></tr><tr><td>Parade Technologies Ltd (4966.TWO)</td><td>O (05/27/2026)</td><td>NT$675.00</td></tr><tr><td>Powerchip Semiconductor Manufacturing Co (6770.TW)</td><td>O (10/27/2025)</td><td>NT$70.20</td></tr><tr><td>Realtek Semiconductor (2379.TW)</td><td>E (01/30/2026)</td><td>NT$745.00</td></tr><tr><td>Shenzhen Goodix Technology Co Ltd (603160.SS)</td><td>U (07/14/2025)</td><td>Rmb59.74</td></tr><tr><td>Winbond Electronics Corp (2344.TW)</td><td>O (05/28/2026)</td><td>NT$199.00</td></tr><tr><td>WPG Holdings (3702.TW)</td><td>O (03/16/2026)</td><td>NT$107.00</td></tr><tr><td>WT Microelectronics Co. Ltd. (3036.TW)</td><td>O (01/27/2026)</td><td>NT$224.00</td></tr><tr><td colspan="3">Duan Liu</td></tr><tr><td>Dosilicon Co Ltd (688110.SS)</td><td>U (09/06/2024)</td><td>Rmb152.91</td></tr><tr><td>Shenzhen Longsys Electronics Co Ltd (301308.SZ)</td><td>E (02/25/2026)</td><td>Rmb571.68</td></tr><tr><td colspan="3">Tiffany Yeh</td></tr><tr><td>AllRing Tech Co. (6187.TWO)</td><td>O (09/23/2025)</td><td>NT$1,155.00</td></tr><tr><td>FOCI Fiber Optic Communications Inc (3363.TWO)</td><td>O (01/15/2025)</td><td>NT$685.00</td></tr><tr><td>Himax Technologies Inc (HIMX.O)</td><td>E (02/04/2026)</td><td>US$16.95</td></tr><tr><td>Hon Precision (7769.TW)</td><td>O (04/17/2026)</td><td>NT$7,330.00</td></tr><tr><td>MPI Corporation (6223.TWO)</td><td>O (04/17/2026)</td><td>NT$6,420.00</td></tr><tr><td>Silicon Motion (SIMO.O)</td><td>O (05/06/2024)</td><td>US$307.12</td></tr><tr><td>WinWay Technology Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$9,450.00</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
