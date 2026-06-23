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
GLOBAL AUTOMOBILES

# Clear sign of re-electrification; updating the GS Electric Vehicle Sentiment Map

## Re-electrification is clear

The global BEV sales mix rose from 13% in February to 19% in May driven by instability in the Middle East. However, there is a regional divergence, with the most rapid BEV growth in China (up 10 percentage points) and other markets (up 6 pp). On the other hand, the BEV ratio in the US has declined by 1 pp. The growth in BEV in other markets was due to Thailand (up 19 pp) and Australia (up 6 pp). Overall, Europe was up 2 pp, but the BEV mix in Germany in particular expanded by 3 pp. It is highly likely that oil reserve conditions and rising gasoline prices are significantly impacting consumer purchasing behavior.

## Price competition moderates with re-electrification

In our proprietary price survey, we observed a moderate decline in sales prices in the US and Canada, but prices in other regions have continued to stabilize or rise. We believe that the trend toward re-electrification has led to more conservative pricing strategies by emerging BEV manufacturers. However, with

aluminum/naphtha/memory prices rising and a 3 pp yoy margin deterioration expected in 2026, there are currently no regions where price hikes are occurring at a magnitude sufficient to secure profitability.

## Potential for major changes in the BEV supply chain

The shift to BEVs is leading to an increase in market share for Chinese BEV manufacturers. The growing share and cost competitiveness of Chinese BEVs could potentially bring about major changes in the automotive supply chain. First, discussions on the IAA (Industrial Accelerator Act) have begun in Europe, with proposals outlining the localization of BEVs to protect the regional economy. Second, traditional automakers have outlined policies for a major shift in their parts procurement strategies. In particular, Japanese automakers are actively adopting Chinese parts, or Chinese-grade parts.

## Confirming the sustainability of the shift to BEVs in June-July

Anticipating the normalization of oil exports from the Strait of Hormuz, our commodities team lowered its WTI forecasts from \$85/bbl to \$80 for 2026, from \$75 to \$70 for 2027, and from \$70 to \$66 for 2028 (as of June 15). The global automotive sector is at a crossroads where stabilizing crude oil prices could soften

## Kota Yuzawa

+81(3)4587-9863 |
kota.yuzawa@gs.com
GS Japan Co., Ltd.

Tina Hou
+86(21)2401-8694 |
tina.hou@goldmansachs.cn
GS (China) Securities
Company Limited

Do Hyoung Kim
+82(2)3788-1376 |
dohyoung.kim@gs.com
GS (Asia) L.L.C., Seoul Branch

## Mark Delaney, CFA

+1(212)357-0535 | mark.delaney@gs.com GS & Co. LLC

Christian Frenes
+44(20)7051-8641 |
christian.frenes@gs.com
GS International

## Chandramouli Muthiah

+91(22)6616-9344 |
chandramouli.muthiah@gs.com
GS India SPL

Ken Kawamoto
+81(3)4587-1921 |
ken.kawamoto@gs.com
GS Japan Co., Ltd.

Will Bryant
+1(212)934-4705 | will.bryant@gs.com
GS & Co. LLC

Aman Gupta
+1(212)357-1549 |
aman.s.gupta@gs.com
GS & Co. LLC

Jenny Du
+86(21)2401-8978 |
jenny.x.du@goldmansachs.cn
GS (China) Securities
Company Limited

Monika Mengting Liu, CFA
+44(20)7051-7601 | monika.liu@gs.com
GS International

Shivam Kotecha
+1(332)245-7822 |
shivam.kotecha@gs.com
GS India SPL

Robert Triulzi
+44(20)7552-2281 |
robert.triulzi@gs.com
GS International

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

the global shift to BEVs, or conversely, the BEV shift could advance structurally through the promotion of energy mix diversification.

Exhibit 1: BEV and PHEV are on rise
Sales by powertrain  
![](images/63d029c2786b94328e5f52f6637af7b08abf96729cbf76bb7a43422f40b24b1b.jpg)  
Source: Marklines, Data compiled by GS Global Investment Research

Exhibit 2: BEV penetration advances in China and Others
BEV mix by region  
![](images/49c86f1fc98e762d4e8a9f3af064e9be7fa0100c3531cb7a28af9e761e8b4f1c.jpg)  
Source: Marklines, Data compiled by GS Global Investment Research

Exhibit 3: BEV adoption advances in Thailand, Australia, and Brazil
BEV mix by region  
![](images/afe9b8f1698c384bd3b42b32e8fcefd3b7063e1883f87861da0778b5842be560.jpg)  
Source: Marklines, Data compiled by GS Global Investment Research

Exhibit 4: Strong regional divergence for BEV penetration
BEV mix by region  
![](images/0286a7233869c29e66b59278c8549df729d55a3f2b61b7108990c22b84786a16.jpg)  
Source: Marklines, Data compiled by GS Global Investment Research

Exhibit 5: Pricing remains stable
Sentiment map

<table><tr><td colspan="3">Sales performance</td><td colspan="3">Total TIV (YoY)</td><td colspan="3">Pricing (YTD)</td><td colspan="3">BEV penetration (MoM)</td></tr><tr><td></td><td>Apr</td><td>May</td><td colspan="2">Apr</td><td>May</td><td colspan="2">Apr</td><td>May</td><td colspan="2">Apr</td><td>May</td></tr><tr><td>Thailand</td><td></td><td>→</td><td>3.5%</td><td>→</td><td>10.2%</td><td>1.6%</td><td>→</td><td>1.6%</td><td>3.3%</td><td>→</td><td>9.3%</td></tr><tr><td>Indonesia</td><td></td><td>→</td><td>55.0%</td><td>→</td><td>14.0%</td><td>0.5%</td><td>→</td><td>0.5%</td><td>0.8%</td><td>→</td><td>-5.2%</td></tr><tr><td>Australia</td><td></td><td>→</td><td>3.0%</td><td>→</td><td>-2.3%</td><td>0.9%</td><td>→</td><td>0.9%</td><td>1.3%</td><td>→</td><td>2.7%</td></tr><tr><td>UK</td><td></td><td>→</td><td>21.7%</td><td>→</td><td>6.9%</td><td>1.9%</td><td>→</td><td>1.9%</td><td>3.3%</td><td>→</td><td>0.8%</td></tr><tr><td>EU</td><td></td><td>→</td><td>4.0%</td><td>→</td><td>1.1%</td><td>0.0%</td><td>→</td><td>0.0%</td><td>0.1%</td><td>→</td><td>0.1%</td></tr><tr><td>Brazil</td><td></td><td>→</td><td>19.0%</td><td>→</td><td>21.6%</td><td>0.0%</td><td>→</td><td>0.0%</td><td>1.9%</td><td>→</td><td>0.9%</td></tr><tr><td>USA</td><td></td><td>→</td><td>-6.2%</td><td>→</td><td>-0.8%</td><td>-3.9%</td><td>→</td><td>-3.8%</td><td>-0.7%</td><td>→</td><td>0.2%</td></tr><tr><td>Canada</td><td></td><td>→</td><td>0.0%</td><td>→</td><td>1.2%</td><td>0.3%</td><td>→</td><td>-0.2%</td><td>0.1%</td><td>→</td><td>0.3%</td></tr><tr><td colspan="12">*EU based on the sum of Germany, France, Italy and Spain</td></tr><tr><td>😊</td><td colspan="11">Sales volumes remain robust, with minimal downward pressure on pricing.</td></tr><tr><td>💡</td><td colspan="11">Sales volumes are underperforming, or there is a downward trend in pricing.</td></tr><tr><td>💡</td><td colspan="11">Both sales volumes and prices are experiencing a decline.</td></tr></table>

Source: Company data, Marklines, GS Global Investment Research

Exhibit 6: BEV penetration advances
BEV sales momentum by region

<table><tr><td>MoM %pts change in BEV penetration</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Jul-26</td><td>Aug-26</td><td>Sep-26</td><td>Oct-26</td><td>Nov-26</td><td>Dec-26</td></tr><tr><td>China</td><td>-7.3%</td><td>1.9%</td><td>1.1%</td><td>6.2%</td><td>3.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>United States</td><td>-0.6%</td><td>0.6%</td><td>0.0%</td><td>-0.7%</td><td>0.2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Germany</td><td>-0.3%</td><td>0.0%</td><td>2.0%</td><td>1.4%</td><td>-0.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>United Kingdom</td><td>-9.1%</td><td>3.1%</td><td>-1.7%</td><td>3.3%</td><td>0.8%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>France</td><td>3.0%</td><td>-1.0%</td><td>1.4%</td><td>-1.5%</td><td>2.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>South Korea</td><td>2.0%</td><td>21.1%</td><td>-4.5%</td><td>0.6%</td><td>-1.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>India</td><td>0.0%</td><td>-0.4%</td><td>1.3%</td><td>0.3%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vietnam</td><td>-4.7%</td><td>3.4%</td><td>8.9%</td><td>3.2%</td><td>-5.7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Norway</td><td>-33.7%</td><td>24.6%</td><td>9.8%</td><td>-4.7%</td><td>1.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Netherlands</td><td>-36.9%</td><td>5.1%</td><td>4.7%</td><td>2.5%</td><td>-6.8%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Turkey</td><td>0.3%</td><td>-1.0%</td><td>0.5%</td><td>0.3%</td><td>-1.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Thailand</td><td>12.0%</td><td>-35.0%</td><td>6.8%</td><td>3.3%</td><td>9.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Denmark</td><td>-1.0%</td><td>0.7%</td><td>-1.5%</td><td>3.8%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Belgium</td><td>-2.8%</td><td>-1.6%</td><td>4.2%</td><td>0.5%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Indonesia</td><td>-7.7%</td><td>-0.3%</td><td>2.0%</td><td>0.8%</td><td>-5.2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sweden</td><td>-2.5%</td><td>0.1%</td><td>0.9%</td><td>-0.1%</td><td>1.2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Italy</td><td>-4.1%</td><td>1.3%</td><td>0.7%</td><td>-0.2%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Spain</td><td>-1.8%</td><td>0.3%</td><td>0.1%</td><td>-0.2%</td><td>-0.8%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Australia</td><td>-2.0%</td><td>3.2%</td><td>2.2%</td><td>1.3%</td><td>2.7%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Canada</td><td>1.5%</td><td>0.1%</td><td>0.1%</td><td>0.1%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brazil</td><td>0.4%</td><td>0.2%</td><td>0.5%</td><td>1.9%</td><td>0.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Austria</td><td>-0.2%</td><td>-0.2%</td><td>4.1%</td><td>0.7%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Japan</td><td>0.2%</td><td>0.4%</td><td>0.7%</td><td>-0.7%</td><td>0.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Portugal</td><td>0.7%</td><td>-3.4%</td><td>0.1%</td><td>0.8%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Switzerland</td><td>-10.3%</td><td>-0.5%</td><td>3.0%</td><td>1.2%</td><td>-4.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Israel</td><td>-23.0%</td><td>1.7%</td><td>3.9%</td><td>-9.0%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Poland</td><td>-2.4%</td><td>-2.3%</td><td>1.0%</td><td>0.0%</td><td>0.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Malaysia</td><td>6.6%</td><td>-2.8%</td><td>-0.1%</td><td>0.8%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Taiwan</td><td>-13.8%</td><td>2.8%</td><td>12.3%</td><td>-12.9%</td><td>4.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Finland</td><td>-5.7%</td><td>-1.3%</td><td>5.4%</td><td>-2.2%</td><td>0.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MoM %pts change in PHEV penetration</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Jun-26</td><td>Jul-26</td><td>Aug-26</td><td>Sep-26</td><td>Oct-26</td><td>Nov-26</td><td>Dec-26</td></tr><tr><td>China</td><td>-3.7%</td><td>0.7%</td><td>-1.0%</td><td>2.8%</td><td>0.4%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>United States</td><td>-0.2%</td><td>-0.1%</td><td>0.0%</td><td>-0.2%</td><td>0.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Germany</td><td>-0.9%</td><td>0.3%</td><td>-1.1%</td><td>0.7%</td><td>0.6%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>United Kingdom</td><td>1.9%</td><td>-1.3%</td><td>1.5%</td><td>0.4%</td><td>0.0%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>France</td><td>-5.2%</td><td>0.8%</td><td>-0.5%</td><td>1.1%</td><td>-0.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>South Korea</td><td>-0.1%</td><td>-0.1%</td><td>-0.1%</td><td>0.0%</td><td>0.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>India</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vietnam</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Norway</td><td>-0.4%</td><td>0.1%</td><td>0.1%</td><td>-0.4%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Netherlands</td><td>15.7%</td><td>-3.5%</td><td>-0.1%</td><td>-0.2%</td><td>-20.9%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Turkey</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Thailand</td><td>0.1%</td><td>-0.1%</td><td>-0.1%</td><td>0.6%</td><td>1.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Denmark</td><td>-0.7%</td><td>0.0%</td><td>-0.4%</td><td>0.4%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Belgium</td><td>-2.9%</td><td>-0.9%</td><td>-0.1%</td><td>1.2%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Indonesia</td><td>-0.4%</td><td>0.1%</td><td>-0.1%</td><td>0.5%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sweden</td><td>-2.4%</td><td>2.4%</td><td>-0.8%</td><td>-0.3%</td><td>1.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Italy</td><td>-0.8%</td><td>-0.1%</td><td>0.4%</td><td>0.3%</td><td>1.2%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Spain</td><td>-0.7%</td><td>0.8%</td><td>-0.9%</td><td>0.7%</td><td>-8.8%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Australia</td><td>-0.1%</td><td>0.2%</td><td>0.0%</td><td>1.1%</td><td>-0.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Canada</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brazil</td><td>-0.3%</td><td>-0.2%</td><td>0.0%</td><td>0.6%</td><td>0.1%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Austria</td><td>1.7%</td><td>-2.4%</td><td>0.1%</td><td>1.8%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Japan</td><td>0.3%</td><td>-0.2%</td><td>0.0%</td><td>-0.1%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Portugal</td><td>0.1%</td><td>-1.3%</td><td>1.1%</td><td>0.8%</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Switzerland</td><td>0.3%</td><td>-0.2%</td><td>0.7%</td><td>-0.2%</td><td>-9.6%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Israel</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Poland</td><td>-0.6%</td><td>0.3%</td><td>0.0%</td><td>-0.1%</td><td>0.3%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Malaysia</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Taiwan</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Finland</td><td>0.5%</td><td>1.2%</td><td>-2.4%</td><td>-2.0%</td><td>-0.5%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Marklines, Data compiled by GS Global Investment Research

## Closely monitoring IAA trends in Europe

Market access restrictions due to “Made in EU” requirements: The IAA, proposed in March 2026, mandates that 70% or more of components excluding the battery be procured within the region (Union-origin) as a condition for BEVs to be eligible for purchase subsidies and public procurement in European countries. We believe that if this regulation is implemented, it could act as a de facto non-tariff barrier against completely built-up (CBU) export models from outside the region, significantly reducing their price competitiveness. While traditional countervailing duties by the EU have primarily targeted Chinese vehicles backed by Chinese government subsidies, the IAA is based on local production ratios. Manufacturers exporting CBU BEVs from Japan and

South Korea would also be equally excluded from public support.

The IAA bill aims to raise the manufacturing sector's share of GDP to 20% by 2035 (from approximately 14.3% in 2024). The schedule aims for deeper discussions in the second half of 2026, formal adoption in the first half of 2027, and implementation in the second half of 2027. Reports from the Nikkei and others have expressed concerns about the possibility of the IAA conflicting with the WTO agreement's “national treatment” principle. In the automotive industry, which has a complex supply chain, a 70% local content requirement could risk disrupting existing supply networks and consequently leading to higher vehicle prices.

If the IAA is implemented, vehicles that do not meet the local content requirements will be uniformly excluded from purchase subsidies in member countr

[中间内容因长度限制已省略]

 impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global

Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
