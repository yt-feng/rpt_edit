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
# China/Hong Kong Consumer | Asia Pacific

# China Retail Sales – May 2026: Weakness Remains

China retail sales down 0.6% YoY in May (3.2% CAGR vs. 2019), below -0.2% consensus and +0.2% in Apr 26, the first decline post Covid. Major categories' growth slowing, while online retail sales picked up. For June, consumer sentiment during Dragon Boat Festival remains the key to watch.

YoY trend by category (reported YoY, with rebasing among categories): Further deceleration from retail sales of goods at -0.7% yoy in May vs. -0.1% in Apr, and restaurants showed a larger slowdown to 0.6% from 2.2% in Apr, partly dragged by soft consumer sentiment during the May Labor Day holiday and calendar shift of the Dragon Boat holiday. Online retail sales growth picked up to 3.4% yoy (2.3% in Apr).

- Among all categories, soft drink and apparel recorded growth yoy (+6.1% and +3.8%, respectively) with improvements vs. last month (+3.6% and +3.6%, respectively).  
- Most staples categories slowed, F&B growth further decelerated to 2.8% from 5.4% in Apr, of which soft drinks was the only category with growth acceleration. Cosmetics decelerated to 2.5% from 4.7% in Apr.  
- Discretionary categories generally stayed weaker than staples with a few categories' declines narrowed: Gold & Jewelry decline narrowed to -8.9% vs. -21.3% yoy in Apr. Electronics & Appliances remained weak at -15.6% yoy (-15.1% in Apr) and Home Furnishing decline narrowed to -8.7% (-10.4% in Apr), as fading subsidy effects and still-soft property-related demand persisted.

Compared with 2019 on a CAGR basis, overall momentum picked up to 3.2% from 2.9% in Apr, with most categories posting improved growth. Restaurants & Dining and F&B slightly softened.

Stock implications: Consumption recovery path could be gradual and bumpy, in our view, and our latest consumer survey shows that sentiment has mildly improved, though our caution remains. Our focus remains on: 1) supply recalibration and demand improvement: Mengniu (2319.HK), Yili (600887.SS); 2) improvement in offline consumption: Haidilao (6862.HK), CRB (0291.HK) and 3) company-specific drivers leading to turnaround and attractive risk-reward: Giant Biogene (2367.HK), Chagee (CHA.O).

MS ASIA LIMITED+

## Lillian Lou

Equity Analyst

Lillian.Lou@morganstanley.com +852 2848-6502

## Dustin Wei

Equity Analyst

Dustin.Wei@morganstanley.com +852 2239-7823

## Hildy Ling

Equity Analyst

Hildy.Ling@morganstanley.com +852 2239-7834

MS TAIWAN LIMITED+

## Terence Cheng

Equity Analyst

Terence.Cheng@morganstanley.com +886 2 2730-2873

## Jenny Ting

Research Associate

Jenny.Ting@morganstanley.com +886 2 2730-2995

MS ASIA LIMITED+

## Jenny Yu

Research Associate

Jenny.Yu1@morganstanley.com +852 3963-1925

## Carlos Liu, CFA

Research Associate

Carlos.Liu@morganstanley.com +852 2848-5206

![](images/95fca60c275b689c2dc853594f64e6f640251347b28ebba8ac1032bd9f790037.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## CHINA/HONG KONG CONSUMER

Asia Pacific

Industry View

In-Line

Read Also:

Investor Presentation: China Consumer: Where is consumption trending now? (1 Jun 2026)

Haidilao International Holding Ltd: May 2026

Operational Update (10 Jun 2026)

China Beauty: 6.18 Pre-sale Rankings: Proya No.1, Giant Biogene Positive Surprise, MGP Gains (29 May 2026)

China/Hong Kong Consumer: China Broader Consumption Trip – Key Takeaways (17 May 2026)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Key Charts

Exhibit 1: Summary of Retail Sales Trends

<table><tr><td></td><td colspan="2">Reported YoY Basis</td><td colspan="2">Calculated CAGR vs. 2019</td></tr><tr><td>Categories</td><td>May 26</td><td>Apr 26</td><td>May 26</td><td>Apr 26</td></tr><tr><td>Overall Retail Sales</td><td>-0.6%</td><td>0.2%</td><td>3.2%</td><td>2.9%</td></tr><tr><td>Overall Retail Sales - ex Autos</td><td>1.1%</td><td>1.8%</td><td>3.5%</td><td>3.2%</td></tr><tr><td>Restaurant &amp; Dining</td><td>0.6%</td><td>2.2%</td><td>3.5%</td><td>3.8%</td></tr><tr><td>Enterprises above a designated size</td><td>-1.7%</td><td>0.9%</td><td>9.2%</td><td>9.3%</td></tr><tr><td>Retail Sales of Goods</td><td>-0.7%</td><td>-0.1%</td><td>3.2%</td><td>2.7%</td></tr><tr><td>Enterprises above a designated size</td><td>-5.2%</td><td>-4.9%</td><td>3.8%</td><td>3.0%</td></tr><tr><td>Apparel, Shoes and Textile</td><td>3.8%</td><td>3.6%</td><td>2.6%</td><td>1.5%</td></tr><tr><td>Gold &amp; Jewelry</td><td>-8.9%</td><td>-21.3%</td><td>2.8%</td><td>3.0%</td></tr><tr><td>Cosmetics</td><td>2.5%</td><td>4.7%</td><td>9.8%</td><td>6.5%</td></tr><tr><td>Home Furnishing</td><td>-8.7%</td><td>-10.4%</td><td>-0.1%</td><td>-0.9%</td></tr><tr><td>F&amp;B (incl. Alcohol &amp; Tobacco)</td><td>2.8%</td><td>5.4%</td><td>7.9%</td><td>8.4%</td></tr><tr><td>Food, Grain and Oil</td><td>1.9%</td><td>4.1%</td><td>7.8%</td><td>8.5%</td></tr><tr><td>Soft Drinks</td><td>6.1%</td><td>3.6%</td><td>7.0%</td><td>6.9%</td></tr><tr><td>Alcohol &amp; Tobacco</td><td>4.8%</td><td>11.7%</td><td>8.6%</td><td>8.9%</td></tr><tr><td>HPC</td><td>1.6%</td><td>3.5%</td><td>7.1%</td><td>5.8%</td></tr><tr><td>Electronics &amp; Appliances</td><td>-15.6%</td><td>-15.1%</td><td>4.2%</td><td>1.8%</td></tr><tr><td>Sports and Entertainment Equipment</td><td>-8.0%</td><td>-8.0%</td><td>NA</td><td>NA</td></tr><tr><td>Online Retail Sales</td><td>3.4%</td><td>2.3%</td><td>11.8%</td><td>9.8%</td></tr><tr><td>Commercial Goods</td><td>2.6%</td><td>0.2%</td><td>8.6%</td><td>6.5%</td></tr></table>

Source: CEIC, National Bureau of Statistics (NBS), MS

Exhibit 2: We note rebasing adjustments for some categories. We summarize the differences between reported YoY growth rates (with rebase) and YoY growth rates based on previously reported absolute amounts in 2024 & 2025 (without rebase).

<table><tr><td colspan="8">Comparison of Monthly YoY Trend</td><td colspan="7">YoY growth (No rebase)</td><td colspan="7">Difference</td></tr><tr><td>Monthly yoy</td><td>Oct 25</td><td>Nov 25</td><td>Dec 25</td><td>Jan-Feb 26</td><td>Mar 26</td><td>Apr 26</td><td>May 26</td><td>Oct 25</td><td>Nov 25</td><td>Dec 25</td><td>Jan-Feb 26</td><td>Mar 26</td><td>Apr 26</td><td>May 26</td><td>Oct 25</td><td>Nov 25</td><td>Dec 25</td><td>Jan-Feb 26</td><td>Mar 26</td><td>Apr 26</td><td>May 26</td></tr><tr><td>Retail Sales</td><td>2.9%</td><td>1.3%</td><td>0.9%</td><td>2.8%</td><td>1.7%</td><td>0.2%</td><td>-0.6%</td><td>2.0%</td><td>0.3%</td><td>-0.1%</td><td>2.8%</td><td>1.7%</td><td>0.2%</td><td>-0.6%</td><td>1%</td><td>1%</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Urban</td><td>2.7%</td><td>1.0%</td><td>0.7%</td><td>2.7%</td><td>1.5%</td><td>-0.1%</td><td>-0.9%</td><td>2.0%</td><td>0.2%</td><td>0.0%</td><td>2.7%</td><td>1.5%</td><td>-0.1%</td><td>-0.9%</td><td>1%</td><td>1%</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Rural</td><td>4.1%</td><td>2.8%</td><td>1.7%</td><td>3.2%</td><td>2.7%</td><td>2.1%</td><td>1.5%</td><td>2.1%</td><td>0.8%</td><td>-0.3%</td><td>3.2%</td><td>2.7%</td><td>2.1%</td><td>1.5%</td><td>2%</td><td>2%</td><td>2%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Online Retail Sales</td><td>8.1%</td><td>5.4%</td><td>4.0%</td><td>9.2%</td><td>5.8%</td><td>2.3%</td><td>3.4%</td><td>2.6%</td><td>-0.1%</td><td>1.5%</td><td>43.0%</td><td>27.8%</td><td>39.0%</td><td>37.6%</td><td>6%</td><td>5%</td><td>3%</td><td>-34%</td><td>-22%</td><td>-37%</td><td>-34%</td></tr><tr><td>Commercial Goods</td><td>4.9%</td><td>1.5%</td><td>0.8%</td><td>10.3%</td><td>2.5%</td><td>0.2%</td><td>2.6%</td><td>-1.2%</td><td>-3.5%</td><td>-0.2%</td><td>11.7%</td><td>-4.5%</td><td>2.7%</td><td>8.7%</td><td>6%</td><td>5%</td><td>1%</td><td>-1%</td><td>7%</td><td>-3%</td><td>-6%</td></tr><tr><td>Service</td><td>26.9%</td><td>35.5%</td><td>25.6%</td><td>7.3%</td><td>11.9%</td><td>6.1%</td><td>5.0%</td><td>25.5%</td><td>26.2%</td><td>11.6%</td><td>184.1%</td><td>197.0%</td><td>220.6%</td><td>167.3%</td><td>1%</td><td>9%</td><td>14%</td><td>-177%</td><td>-185%</td><td>-215%</td><td>-162%</td></tr><tr><td>Restaurants &amp; Dining</td><td>3.8%</td><td>3.2%</td><td>2.2%</td><td>4.8%</td><td>2.9%</td><td>2.2%</td><td>0.6%</td><td>5.0%</td><td>4.4%</td><td>3.4%</td><td>4.8%</td><td>2.9%</td><td>2.2%</td><td>0.6%</td><td>-1%</td><td>-1%</td><td>-1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Enterprises above certain size:</td><td>3.7%</td><td>1.2%</td><td>-1.1%</td><td>4.7%</td><td>2.0%</td><td>0.9%</td><td>-1.7%</td><td>10.4%</td><td>6.4%</td><td>4.3%</td><td>7.4%</td><td>4.9%</td><td>4.6%</td><td>1.6%</td><td>-7%</td><td>-5%</td><td>-5%</td><td>-3%</td><td>-3%</td><td>-4%</td><td>-3%</td></tr><tr><td>Retail Sales of Goods</td><td>2.8%</td><td>1.0%</td><td>0.7%</td><td>2.5%</td><td>1.5%</td><td>-0.1%</td><td>-0.7%</td><td>1.6%</td><td>-0.3%</td><td>-0.6%</td><td>2.5%</td><td>1.5%</td><td>-0.1%</td><td>-0.7%</td><td>1%</td><td>1%</td><td>1%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td>Enterprises above certain size:</td><td>1.4%</td><td>-2.2%</td><td>-2.0%</td><td>2.5%</td><td>1.2%</td><td>-4.9%</td><td>-5.2%</td><td>4.2%</td><td>-0.1%</td><td>0.2%</td><td>0.2%</td><td>-1.5%</td><td>-6.6%</td><td>-7.4%</td><td>-3%</td><td>-2%</td><td>-2%</td><td>2%</td><td>3%</td><td>2%</td><td>2%</td></tr><tr><td>Apparel, Shoes and Textile</td><td>6.3%</td><td>3.5%</td><td>0.6%</td><td>10.4%</td><td>7.0%</td><td>3.6%</td><td>3.8%</td><td>9.2%</td><td>4.2%</td><td>2.0%</td><td>7.9%</td><td>4.5%</td><td>1.8%</td><td>2.1%</td><td>-3%</td><td>-1%</td><td>-1%</td><td>3%</td><td>2%</td><td>2%</td><td>2%</td></tr><tr><td>Gold &amp; Jewelry</td><td>37.6%</td><td>8.5%</td><td>5.9%</td><td>13.0%</td><td>11.7%</td><td>-21.3%</td><td>-8.9%</td><td>39.0%</td><td>9.0%</td><td>5.8%</td><td>10.9%</td><td>9.5%</td><td>-23.0%</td><td>-11.0%</td><td>-1%</td><td>0%</td><td>0%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td></tr><tr><td>Cosmetics</td><td>9.6%</td><td>6.1%</td><td>8.8%</td><td>4.5%</td><td>8.3%</td><td>4.7%</td><td>2.5%</td><td>11.8%</td><td>7.8%</td><td>10.1%</td><td>4.6%</td><td>8.2%</td><td>5.5%</td><td>3.2%</td><td>-2%</td><td>-2%</td><td>-1%</td><td>0%</td><td>0%</td><td>-1%</td><td>-1%</td></tr><tr><td>Home Furnishing</td><td>9.6%</td><td>-3.8%</td><td>-2.2%</td><td>8.8%</td><td>-8.7%</td><td>-10.4%</td><td>-8.7%</td><td>17.8%</td><td>2.6%</td><td>6.7%</td><td>5.3%</td><td>-11.3%</td><td>-12.4%</td><td>-11.8%</td><td>-8%</td><td>-6%</td><td>-9%</td><td>3%</td><td>3%</td><td>2%</td><td>3%</td></tr><tr><td>Sports and Entertainment Equipmer</td><td>10.1%</td><td>0.4%</td><td>9.0%</td><td>4.1%</td><td>-2.0%</td><td>-8.0%</td><td>-8.0%</td><td>15.4%</td><td>4.1%</td><td>13.4%</td><td>7.3%</td><td>-4.0%</td><td>-2.3%</td><td>-3.1%</td><td>-5%</td><td>-4%</td><td>-4%</td><td>-3%</td><td>2%</td><td>-6%</td><td>-5%</td></tr><tr><td>F&amp;B (incl. Alcohol &amp; Tobacco)</td><td>8.0%</td><td>4.0%</td><td>2.3%</td><td>11.8%</td><td>9.0%</td><td>5.4%</td><td>2.8%</td><td>11.0%</td><td>6.4%</td><td>4.6%</td><td>8.3%</td><td>4.0%</td><td>1.8%</td><td>-2.3%</td><td>-3%</td><td>-2%</td><td>-2%</td><td>4%</td><td>5%</td><td>4%</td><td>5%</td></tr><tr><td>Food, Grain and Oil</td><td>9.1%</td><td>6.1%</td><td>3.9%</td><td>10.2%</td><td>9.5%</td><td>4.1%</td><td>1.9%</td><td>12.1%</td><td>8.8%</td><td>6.3%</td><td>6.6%</td><td>4.0%</td><td>0.4%</td><td>-3.4%</td><td>-3%</td><td>-3%</td><td>-2%</td><td>4%</td><td>6%</td><td>4%</td><td>5%</td></tr><tr><td>Soft Drinks</td><td>7.1%</td><td>2.9%</td><td>1.7%</td><td>6.0%</td><td>8.2%</td><td>3.6%</td><td>6.1%</td><td>11.0%</td><td>5.5%</td><td>4.6%</td><td>2.6%</td><td>3.1%</td><td>0.8%</td><td>0.7%</td><td>-4%</td><td>-3%</td><td>-3%</td><td>3%</td><td>5%</td><td>3%</td><td>5%</td></tr><tr><td>Alcohol &amp; Tobacco</td><td>4.1%</td><td>-3.4%</td><td>-2.9%</td><td>19.1%</td><td>7.7%</td><td>11.7%</td><td>4.8%</td><td>6.5%</td><td>-1.8%</td><td>-1.4%</td><td>15.9%</td><td>4.7%</td><td>8.0%</td><td>0.4%</td><td>-2%</td><td>-2%</td><td>-1%</td><td>3%</td><td>3%</td><td>4%</td><td>4%</td></tr><tr><td>Pharma</td><td>3.6%</td><td>4.9%</td><td>1.2%</td><td>0.7%</td><td>5.7%</td><td>4.2%</td><td>4.0%</td><td>5.0%</td><td>6.1%</td><td>2.3%</td><td>-1.7%</td><td>2.8%</td><td>2.2%</td><td>1.4%</td><td>-1%</td><td>-1%</td><td>-1%</td><td>2%</td><td>3%</td><td>2%</td><td>3%</td></tr><tr><td>HPC</td><td>7.4%</td><td>-0.8%</td><td>3.7%</td><td>6.6%</td><td>4.6%</td><td>3.5%</td><td>1.6%</td><td>10.4%</td><td>0.7%</td><td>5.1%</td><td>3.7%</td><td>1.2%</td><td>0.6%</td><td>-2.0%</td><td>-3%</td><td>-1%</td><td>-1%</td><td>3%</td><td>3%</td><td>3%</td><td>4%</td></tr><tr><td>Electronics &amp; Appliances</td><td>-14.6%</td><td>-19.4%</td><td>-18.7%</td><td>3.3%</td><td>-5.0%</td><td>-15.1%</td><td>-15.6%</td><td>-10.3%</td><td>-16.7%</td><td>-14.3%</td><td>2.3%</td><td>-6.3%</td><td>-15.1%</td><td>-16.4%</td><td>-4%</td><td>-3%</td><td>-4%</td><td>1%</td><td>1%</td><td>0%</td><td>1%</td></tr><tr><td>Office Supply</td><td>13.5%</td><td>11.7%</td><td>9.2%</td><td>5.8%</td><td>15.0%</td><td>-6.9%</td><td>-1.5%</td><td>17.8%</td><td>15.7%</td><td>12.4%</td><td>2.7%</td><td>11.6%</td><td>-7.5%</td><td>-2.3%</td><td>-4%</td><td>-4%</td><td>-3%</td><td>3%</td><td>3%</td><td>1%</td><td>1%</td></tr><tr><td>Mobile &amp; Communication</td><td>23.2%</td><td>20.6%</td><td>20.9%</td><td>17.8%</td><td>27.3%</td><td>6.2%</td><td>0.7%</td><td>29.3%</td><td>25.9%</td><td>27.7%</td><td>17.6%</td><td>24.4%</td><td>7.7%</td><td>2.1%</td><td>-6%</td><td>-5%</td><td>-7%</td><td>0%</td><td>3%</td><td>-2%</td><td>-1%</td></tr><tr><td>Auto</td><td>-6.6%</td><td>-8.3%</td><td>-5.0%</td><td>-7.3%</td><td>-11.8%</td><td>-15.3%</td><td>-16.1%</td><td>-4.4%</td><td>-6.5%</td><td>-3.2%</td><td>-9.3%</td><td>-13.6%</td><td>-16.5%</td><td>-17.5%</td><td>-2%</td><td>-2%</td><td>-2%</td><td>2%</td><td>2%</td><td>1%</td><td>1%</td></tr><tr><td>Oil Related Products</td><td>-5.9%</td><td>-8.0%</td><td>-11.0%</td><td>-9.7%</td><td>0.1%</td><td>-6.5%</td><td>-3.2%</td><td>-4.8%</td><td>-7.1%</td><td>-10.1%</td><td>-10.7%</td><td>-1.3%</td><td>-7.5%</td><td>-5.4%</td><td>-1%</td><td>-1%</td><td>-1%</td><td>1%</td><td>1%</td><td>1%</td><td>2%</td></tr><tr><td>Construction Materials</td><td>-8.3%</td><td>-17.0%</td><td>-11.8%</td><td>-2.2%</td><td>-9.0%</td><td>-13.8%</td><td>-13.6%</td><td>-4.0%</td><td>-12.9%</td><td>-7.5%</td><td>-17.1%</td><td>-25.8%</td><td>-26.8%</td><td>-27.5%</td><td>-4%</td><td>-4%</td><td>-4%</td><td>15%</td><td>17%</td><td>13%</td><td>14%</td></tr></table>

Source: CEIC, NBS, MS

Exhibit 3: MSCI China vs. Retail Sales  
![](images/abb81a4d15cdbfb8c1cc9d91a1d3cd8697519efaa1d9fe0eb04cf220c73780dd.jpg)

<details>
<summary>line chart</summary>

| Date    | MSCI China (L) | Electronics & Appliance yoy | Gold & Jewellery yoy | Cosmetics yoy | Auto yoy | Catering yoy |
|---------|----------------|-----------------------------|----------------------|---------------|----------|--------------|
| May-15  | ~80            | ~55                         | ~55                  | ~55           | ~55      | ~55          |
| Sep-15  | ~60            | ~50                         | ~25                  | ~50           | ~50      | ~50          |
| Jan-16  | ~55            | ~50                         | ~50                  | ~50           | ~50      | ~50          |
| May-16  | ~60            | ~55                         | ~55                  | ~55           | ~55      | ~55          |
| Sep-16  | ~65            | ~60                         | ~60                  | ~60           | ~60      | ~60          |
| Jan-17  | ~70            | ~65                         | ~65                  | ~65           | ~65      | ~65          |
| May-17  | ~80            | ~70                         | ~70                  | ~70           | ~70      | ~70          |
| Sep-17  | ~90            | ~75                         | ~75                  | ~75           | ~75      | ~75          |
| Jan-18  | ~100           | ~80                         | ~80                  | ~80           | ~80      | ~80          |
| May-18  | ~95            | ~75                         | ~75                  | ~75           | ~75      | ~75          |
| Sep-18  | ~85            | ~70                         | ~70                  | ~70           | ~70      | ~70          |
| Jan-19  | ~80            | ~65                         | ~65                  | ~65           | ~65      | ~65          |
| May-19  | ~85            | ~70                         | ~70                  | ~70           | ~70      | ~70          |
| Sep-19  | ~90            | ~75                         | ~75                  | ~75           | ~75      | ~75          |
| Jan-20  | ~95            | ~80                         | ~80                  | ~80           | ~80      | ~80          |
| May-20  | ~100           | ~85                         | ~85                  | ~85           | ~85      | ~85          |
| Sep-20  | ~110           | ~90                         | ~90                  | ~90           | ~90      | ~90          |
| Jan-21  | ~120           | ~95                         | ~95                  | ~95           | ~95      | ~95          |
| May-21  | ~130           | ~100                        | ~100                 | ~100          | ~100     | ~100         |
| Sep-21  | ~125           | ~95                         | ~95                  | ~95           | ~95      | ~95          |
| Jan-22  | ~110           | ~90                         | ~90                  | ~90           | ~90      | ~90          |
| May-22  | ~100           | ~85                         | ~85                  | ~85           | ~85      | ~85          |
| Sep-22  | ~90            | ~80                         | ~80                  | ~80           | ~80      | ~80          |
| Jan-23  | ~85            | ~75        

[中间内容因长度限制已省略]

</tr><tr><td>Topsports International Holdings Ltd (6110.HK)</td><td>O (11/13/2019)</td><td>HK$2.80</td></tr><tr><td>Weilong Delicious Global Holdings Ltd (9985.HK)</td><td>O (06/11/2025)</td><td>HK$7.97</td></tr><tr><td>Yonghui Superstores (601933.SS)</td><td>U (05/18/2023)</td><td>Rmb3.25</td></tr></table>

Hildy Ling

<table><tr><td>Angel Yeast Co. Ltd. (600298.SS)</td><td>E (05/21/2026)</td><td>Rmb35.59</td></tr><tr><td>Beijing Roborock Technology Co Ltd (688169.SS)</td><td>O (09/25/2024)</td><td>Rmb102.60</td></tr><tr><td>China Tourism Group Duty Free (1880.HK)</td><td>E (12/13/2023)</td><td>HK$56.75</td></tr><tr><td>China Tourism Group Duty Free (601888.SS)</td><td>E (12/13/2023)</td><td>Rmb59.08</td></tr><tr><td>Chow Tai Fook Jewellery Group Ltd (1929.HK)</td><td>O (03/04/2025)</td><td>HK$12.90</td></tr><tr><td>Chow Tai Seng Jewellery Co Ltd (002867.SZ)</td><td>U (03/04/2025)</td><td>Rmb12.29</td></tr><tr><td>Ecovacs Robotics Co Ltd (603486.SS)</td><td>E (10/30/2023)</td><td>Rmb55.58</td></tr><tr><td>Foshan Haitian Flavouring and Food (603288.SS)</td><td>E (07/28/2025)</td><td>Rmb34.14</td></tr><tr><td>Foshan Haitian Flavouring and Food (3288.HK)</td><td>E (05/21/2026)</td><td>HK$31.48</td></tr><tr><td>Haidilao International Holding Ltd (6862.HK)</td><td>O (05/26/2021)</td><td>HK$12.55</td></tr><tr><td>Hangzhou Robam Appliances Co Ltd (002508.SZ)</td><td>U (02/21/2024)</td><td>Rmb16.30</td></tr><tr><td>Laopu Gold (6181.HK)</td><td>O (10/20/2025)</td><td>HK$487.40</td></tr><tr><td>Super Hi (HDL.O)</td><td>E (01/14/2025)</td><td>US$13.73</td></tr><tr><td>Zhejiang Supor Co. Ltd. (002032.SZ)</td><td>E (01/17/2022)</td><td>Rmb42.40</td></tr></table>

Lillian Lou

<table><tr><td>Anhui Gujing Distillery Company Limited (000596.SZ)</td><td>U (02/13/2026)</td><td>Rmb87.10</td></tr><tr><td>Budweiser Brewing Company APAC Ltd (1876.HK)</td><td>O (11/04/2019)</td><td>HK$7.03</td></tr><tr><td>Chagee Holdings Ltd (CHA.O)</td><td>O (06/02/2025)</td><td>US$11.80</td></tr><tr><td>China Mengniu Dairy (2319.HK)</td><td>O (09/14/2017)</td><td>HK$16.26</td></tr><tr><td>China Resources Beer Holdings Co Ltd (0291.HK)</td><td>O (12/11/2018)</td><td>HK$23.70</td></tr><tr><td>Chongqing Brewery Co. Ltd. (600132.SS)</td><td>U (07/30/2021)</td><td>Rmb49.40</td></tr><tr><td>Eastroc Beverages (605499.SS)</td><td>O (03/12/2026)</td><td>Rmb128.26</td></tr><tr><td>Eastroc Beverages (9980.HK)</td><td>O (03/12/2026)</td><td>HK$125.20</td></tr><tr><td>Gree Electric Appliances Inc of Zhuhai (000651.SZ)</td><td>O (04/14/2020)</td><td>Rmb37.86</td></tr><tr><td>Haier Smart Home Co Ltd (600690.SS)</td><td>E (01/17/2022)</td><td>Rmb20.97</td></tr><tr><td>Haier Smart Home Co Ltd (6690.HK)</td><td>E (01/17/2022)</td><td>HK$21.78</td></tr><tr><td>Kweichow Moutai Company Ltd. (600519.SS)</td><td>O (10/17/2014)</td><td>Rmb1,271.10</td></tr><tr><td>Luzhou Lao Jiao Co. Ltd (000568.SZ)</td><td>E (01/23/2019)</td><td>Rmb84.68</td></tr><tr><td>Midea Group Co Ltd. (0300.HK)</td><td>O (11/01/2024)</td><td>HK$90.85</td></tr><tr><td>Midea Group Co Ltd. (000333.SZ)</td><td>O (01/17/2022)</td><td>Rmb80.93</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (2714.HK)</td><td>O (03/17/2026)</td><td>HK$32.18</td></tr><tr><td>Muyuan Foodstuff Co. Ltd (002714.SZ)</td><td>O (03/17/2026)</td><td>Rmb35.28</td></tr><tr><td>Nongfu Spring Co Ltd (9633.HK)</td><td>E (07/30/2021)</td><td>HK$44.30</td></tr><tr><td>Shanxi Xinghuacun Fen Wine Factory Co. (600809.SS)</td><td>O (10/28/2020)</td><td>Rmb119.28</td></tr><tr><td>Shuanghui Development (000895.SZ)</td><td>U (03/16/2021)</td><td>Rmb24.15</td></tr><tr><td>Tingyi (Cayman Islands) (0322.HK)</td><td>E (07/25/2025)</td><td>HK$10.89</td></tr><tr><td>Tsingtao Brewery Co Ltd (0168.HK)</td><td>E (11/01/2024)</td><td>HK$49.34</td></tr><tr><td>Tsingtao Brewery Co Ltd (600600.SS)</td><td>E (02/28/2024)</td><td>Rmb59.50</td></tr><tr><td>Uni-President China (0220.HK)</td><td>E (07/25/2025)</td><td>HK$7.41</td></tr><tr><td>Want Want China Holdings Ltd (0151.HK)</td><td>E (11/29/2023)</td><td>HK$4.14</td></tr><tr><td>WH Group (0288.HK)</td><td>O (02/24/2025)</td><td>HK$8.85</td></tr><tr><td>Wuliangye Yibin Company Ltd. (000858.SZ)</td><td>E (08/15/2024)</td><td>Rmb79.63</td></tr><tr><td>Yanghe Brewery (002304.SZ)</td><td>U (01/05/2021)</td><td>Rmb43.09</td></tr><tr><td>Yanjing Brewery (000729.SZ)</td><td>U (09/02/2015)</td><td>Rmb11.36</td></tr><tr><td>Yili Industrial (600887.SS)</td><td>O (01/29/2014)</td><td>Rmb25.41</td></tr><tr><td>Yum China Holdings Inc. (YUMC.N)</td><td>O (03/20/2018)</td><td>US$44.25</td></tr><tr><td>ZJLD Group (6979.HK)</td><td>E (02/13/2026)</td><td>HK$7.68</td></tr><tr><td colspan="3">Terence Cheng</td></tr><tr><td>Chervon Holdings Ltd. (2285.HK)</td><td>E (04/12/2024)</td><td>HK$17.39</td></tr><tr><td>Crystal International Group Ltd. (2232.HK)</td><td>E (06/23/2025)</td><td>HK$6.48</td></tr><tr><td>Gongniu Group Co Ltd (603195.SS)</td><td>O (05/08/2023)</td><td>Rmb40.05</td></tr><tr><td>Hangzhou Greatstar Industrial Co Ltd (002444.SZ)</td><td>E (10/26/2022)</td><td>Rmb31.80</td></tr><tr><td>Huali Industrial Group Co (300979.SZ)</td><td>U (02/10/2026)</td><td>Rmb32.74</td></tr><tr><td>Shenzhou International Group Holdings (2313.HK)</td><td>O (07/13/2017)</td><td>HK$44.50</td></tr><tr><td>Stella International Holdings Ltd (1836.HK)</td><td>E (06/23/2025)</td><td>HK$13.82</td></tr><tr><td>Techtronic Industries Co Ltd (0669.HK)</td><td>O (12/05/2019)</td><td>HK$124.40</td></tr><tr><td>Yue Yuen Industrial Hldg (0551.HK)</td><td>E (09/14/2021)</td><td>HK$14.15</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
