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
CHINA CONSUMER STAPLES

# Nielsen China infant formula (Mar-Apr '26): Offline contracted by 8% yoy; Online sales down 19% yoy in May dragged by JD

## CONNECTIONS

In this report we highlight the key findings for China's infant milk formula (IMF) market from online channels (Tmall/Taobao/JD) as of May and the latest Nielsen data through Mar-Apr 2026. We also present updates on Feihe, Yili, Mengniu, Danone and A2.

## Key findings:

1. Offline infant formula market declined by $-8.2\%$ yoy in Mar-Apr (a greater decline vs $-7.7\%$ yoy in Jan-Feb). Breaking it down for Mar-Apr, volume was down by $9\%$ while ASP grew by $0.9\%$ yoy vs. $-8.7\% / +1.1\%$ yoy in Jan-Feb. By channel, we saw $7.3\%$ decline in M&B (mom & baby stores) and $-20\%$ decline from MT (modern trade) in Mar-Apr.

2. In Mar-Apr, Feihe's sales decline in the offline channel was $-12\%$ yoy (vs. $-15\%$ decline yoy in Jan-Feb), lagging the market run-rate of $-8.2\%$ yoy. Tracked omni-channel sales including online sales combined with Nielsen offline sales point to $-24\%$ yoy decline in Mar-Apr, vs. $-19\%$ yoy in Jan-Feb.

3. In Mar-Apr, Yili's sales decline in the offline channel was $1.9\%$ yoy (vs. $-0.9\%$ yoy in Jan-Feb), driven by sales growth in the M&B channel by $2.8\%$ yoy in Mar-Apr. Tracked omni-channel sales including online sales combined with Nielsen offline sales point to $-2\%$ yoy in Mar-Apr vs. $-1\%$ yoy in Jan-Feb.

4. A2: In the M&B channel, A2 recorded +2.9% sales growth in Mar-Apr, vs 2.9% in Jan-Feb. Share by value increased 0.2ppt to 4.3% in Mar-Apr vs 4.1% in Jan-Feb, +0.4ppt yoy.

5. In offline markets, large domestic companies' collective market share was largely flattish in Mar-Apr vs. Jan-Feb, and leading MNC brands' value share increased by 0.3pp to $23.8\%$ in Mar-Apr vs. $23.5\%$ in Jan-Feb.

6. Other brands in offline channels: Mengniu's sales (excl. Yashili) grew at 10% yoy in Mar-Apr vs. +36% yoy in Jan-Feb for offline markets. Junlebao's sales declined by -22.3% (vs. -25.8% in Jan-Feb). Biostime sales grew by 22.4% yoy vs.

Leaf Liu
+852-3966-4169 | leaf.liu@gs.com
GS (Asia) L.L.C.

## Peter Marks

+61(02)9321-8846 |
peter.marks@gs.com
GS Australia Pty Ltd

Christina Liu  
+852-2978-6983 | christina.liu@gs.com  
GS (Asia) L.L.C.

## Rayanne Haidar

+61(2)9321-8739 | rayanne.haidar@gs.com GS Australia Pty Ltd

Valerie Zhou  
+852-2978-0820 | valerie.zhou@gs.com  
GS (Asia) L.L.C.

## Table of Contents

<table><tr><td>Monthly summary tables by channel</td><td>4</td></tr><tr><td>Offline Market: Overall decline sequentially narrowed down; Yili gained share</td><td>4</td></tr><tr><td>Online Market: Domestic brands sequentially weakened; Top MNC brands growth moderated potentially due to high comp last year on 618</td><td>7</td></tr><tr><td>Feihe (Neutral): offline market share slightly recovered despite weak run-rate; Taobao/Tmall/JD decline narrowed</td><td>8</td></tr><tr><td>Yili (Buy): Online sequentially weakened; offline resumed to positive growth</td><td>10</td></tr><tr><td>Other player updates: Bellamy/Biostime/A2 outperformed the online market</td><td>11</td></tr><tr><td>Disclosure Appendix</td><td>13</td></tr></table>

+25.8% in Jan-Feb, with market share trending down by 0.3pp to 7.5% in Mar-Apr vs. 7.8% at Jan-Feb.

7. Online industry: On Tmall/Taobao/JD combined, infant milk formula sales declined by 19% yoy in May (vs. -14% yoy in Apr), with -2% yoy growth on Tmall/Taobao and -26% on JD on a tough base.

8. Feihe online sales (Taobao/Tmall/JD combined) declined by $-31\%$ yoy in May, vs. $-47\%$ in Apr.

9. Yili online sales (Taobao/Tmall/JD combined, incl. Pro-Kido on Taobao/Tmall) decreased by -17% in May vs -10% in Apr.

10. A2 Milk recorded -25% yoy online sales decline in May potentially due to the supply cut since Apr (Taobao/Tmall/JD combined) vs. 27% yoy in Apr.

11. Outperforming brands in May 26 (Online): Aptamil, Bellamy's; Underperformers: Firmus, A2, Nutrilon, Wyeth.

The authors would like to thank Lily Qi for her contribution to this report.

## Monthly summary tables by channel

Exhibit 1: Offline: Feihe/Yili/Dannone/A2 gained share sequentially in MA26 while Nestle lost share

<table><tr><td>Brands - offline</td><td>Company</td><td>IMF recall date</td><td colspan="4">Market share</td><td colspan="5">Sales yoy</td></tr><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td colspan="9">Modern Trade + M&amp;B</td></tr><tr><td>Trend</td><td>MA26</td><td>JF26</td><td>ND25</td><td>SO25</td><td>JA25</td><td>MJ25</td><td>MA25</td><td>JF25</td></tr><tr><td>Baby products</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="12">Infant Formula</td></tr><tr><td>Feihe</td><td>Feihe</td><td>n.a.</td><td>↑</td><td>-12%</td><td>-15%</td><td>-19%</td><td>-23%</td><td>-14%</td><td>-7%</td><td>-1%</td><td>-6%</td></tr><tr><td>Yili</td><td>Yili</td><td>Jan-26</td><td>↑</td><td>2%</td><td>-1%</td><td>-1%</td><td>0%</td><td>-1%</td><td>1%</td><td>5%</td><td>5%</td></tr><tr><td>Danone (Dumex + Nutrica)</td><td>Danone</td><td>Jan-26</td><td>↑</td><td>1%</td><td>6%</td><td>5%</td><td>10%</td><td>6%</td><td>5%</td><td>-2%</td><td>-8%</td></tr><tr><td>A2</td><td>A2 Milk</td><td>May-26</td><td>↑</td><td>3%</td><td>3%</td><td>5%</td><td>4%</td><td>12%</td><td>18%</td><td>7%</td><td>10%</td></tr><tr><td>Wyeth</td><td>Nestle</td><td>Jan-26</td><td>↓</td><td>-60%</td><td>-51%</td><td>-40%</td><td>-40%</td><td>-39%</td><td>-41%</td><td>-31%</td><td>-35%</td></tr></table>

Source: Nielsen

Exhibit 2: Online: Aptamil/Wyeth gained share sequentially while Feihe/A2/Bellamy's/Nutrilon lost share on Tmall/Taobao/JD combined in May

<table><tr><td rowspan="2">Brands - online</td><td rowspan="2">Company</td><td rowspan="2">IMF recall date</td><td colspan="8">Market share</td><td colspan="10">Sales yoy</td></tr><tr><td>Tmall/Taobao/JDTrend</td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td><td>May-25</td><td>Apr-25</td><td>Mar-25</td><td>Feb-25</td><td>Jan-25</td></tr><tr><td colspan="21">Baby products</td></tr><tr><td colspan="21">Infant Formula</td></tr><tr><td>Aptamil</td><td>Danone</td><td>Jan-26</td><td>↑</td><td>6%</td><td>2%</td><td>-9%</td><td>15%</td><td>24%</td><td>56%</td><td>34%</td><td>19%</td><td>30%</td><td>5%</td><td>20%</td><td>27%</td><td>26%</td><td>12%</td><td>9%</td><td>34%</td><td>5%</td></tr><tr><td>Feihe</td><td>Feihe</td><td>n.a.</td><td>↓</td><td>-31%</td><td>-47%</td><td>-47%</td><td>-40%</td><td>-22%</td><td>-25%</td><td>-9%</td><td>-17%</td><td>-13%</td><td>-22%</td><td>-12%</td><td>-20%</td><td>35%</td><td>73%</td><td>42%</td><td>39%</td><td>7%</td></tr><tr><td>A2</td><td>A2 Milk</td><td>May-26</td><td>↓</td><td>-25%</td><td>27%</td><td>17%</td><td>14%</td><td>28%</td><td>31%</td><td>20%</td><td>28%</td><td>10%</td><td>20%</td><td>24%</td><td>36%</td><td>21%</td><td>-18%</td><td>5%</td><td>35%</td><td>-11%</td></tr><tr><td>Yii</td><td>Yii</td><td>May-26</td><td>→</td><td>-5%</td><td>20%</td><td>-43%</td><td>-48%</td><td>-48%</td><td>-14%</td><td>-33%</td><td>30%</td><td>15%</td><td>-9%</td><td>27%</td><td>-5%</td><td>71%</td><td>-10%</td><td>60%</td><td>34%</td><td>51%</td></tr><tr><td>Wyeth</td><td>Nestle</td><td>Jan-26</td><td>↑</td><td>-45%</td><td>-32%</td><td>-27%</td><td>-33%</td><td>-41%</td><td>-38%</td><td>-23%</td><td>-22%</td><td>-18%</td><td>-14%</td><td>4%</td><td>-12%</td><td>47%</td><td>6%</td><td>-14%</td><td>25%</td><td>5%</td></tr><tr><td>Bellamy&#x27;s</td><td>Mengniu</td><td>n.a.</td><td>↓</td><td>19%</td><td>80%</td><td>68%</td><td>60%</td><td>73%</td><td>-19%</td><td>38%</td><td>26%</td><td>49%</td><td>28%</td><td>48%</td><td>34%</td><td>119%</td><td>38%</td><td>30%</td><td>173%</td><td>30%</td></tr><tr><td>Nutrition</td><td>Danone</td><td>Jan-26</td><td>↓</td><td>-71%</td><td>-45%</td><td>-44%</td><td>-50%</td><td>-42%</td><td>-74%</td><td>-47%</td><td>-48%</td><td>-26%</td><td>-37%</td><td>9%</td><td>-27%</td><td>46%</td><td>-22%</td><td>-46%</td><td>6%</td><td>-34%</td></tr></table>

Moojing

## Offline Market: Overall decline sequentially narrowed down; Yili gained share

## Offline market Mar-Apr 2026 updates

The Nielsen IMF sales data (surveying both modern trade (MT) and mom & baby (M&B) stores) declined by -8.2% yoy in Mar-Apr (vs -7.7% yoy decline for Jan-Feb), with 7% decline in M&B and -20% decline from MT (vs -6.7%/-21% yoy in Jan-Feb).

Volume remained the main drag in the IMF sales decline, down by 9% yoy in Mar-Apr, down 0.3ppt sequentially. Volume for M&B channel decreased by 7.9% yoy in Mar-Apr vs -7.4% yoy decline in Jan-Feb. ASP growth increased slightly at +0.9% yoy in Mar-Apr with 0.6% yoy growth in the M&B channel in Mar-Apr and 2.8% yoy growth in the MT channel.

For the M&B channel, Feihe saw its ASP increase by 0.7% yoy (vs. -0.2% yoy in Jan-Feb) and Yili recorded 1.1% yoy decrease in Mar-Apr vs. 1.2% yoy decrease in Jan-Feb. Among foreign players, Danone/Nestle/Friesland showed ASP growth of 2.5%/1.8%/-0.2% yoy (vs. 0.7%/4.0%/-0.4% in Jan-Feb), and A2 Milk ASP continued declining, by -1.3% yoy vs. -2.6% yoy in Jan-Feb.

Note: Nielsen data has rebased since May-Jun 24.

Exhibit 3: The mom & baby channel declined by 7% yoy and modern trade declined by 20% yoy  
![](images/4c5947ce39a5af69986f120a1b5fcf0444ced908c59b88b65dfaf3df5b6f286f.jpg)  
Source: Nielsen

Exhibit 4: For modern trade and mom & baby stores, infant formula sales recorded a 9% volume decline with 0.9% ASP growth yoy

![](images/0523783289a5889e5aad895a555585be411e39260273f2d103e714df366a3027.jpg)  
Source: Nielsen

## Offline Mar-Apr brand performance

Compared with Jan-Feb, some domestic players saw slight sequential improvement. Yili sales resumed positive growth at 1.9% yoy vs -0.9% in Jan-Feb. Feihe saw a narrowed 12% decline yoy vs 15% in Jan-Feb, still lagging the market run-rate. Biostime sales continued growth to 22.4% yoy vs. 25.8% in Jan-Feb. Among the MNC brands, Nestle declined at -36% yoy vs. -22% yoy in Jan-Feb and Friesland also declined at -4% yoy (vs. -8% in Jan-Feb). Wyeth and Abbott continued underperforming the market, seeing -60%/-43% yoy sales decline, while Mead Johnson continued positive growth at 4% in Mar-Apr vs. 7% in Jan-Feb.

1. Large domestic companies' collective market share was largely flattish in Mar-Apr vs. Jan-Feb, with Yili/Feihe gaining shares while Mengniu/Biostime losing shares sequentially, together accounting for $62\%$ of market share. Leading MNC brands' value share increased by 0.3pp to $23.8\%$ in Mar-Apr vs. $23.5\%$ in Jan-Feb.

2. Yili delivered positive sales growth in Mar-Apr at $1.9\%$ yoy vs $-0.9\%$ in Jan-Feb. Ausnutria (acquired by Yili) recorded a $28\%$ decline yoy in sales in Mar-Apr, vs. $-20\%$ in Jan-Feb.

3. Feihe's market share recorded $21\%$ in Mar-Apr, up by 0.4pp vs. Jan-Feb at $20.6\%$ , down 0.9pp yoy.

4. A2 Milk China Label sales in Mar-Apr grew by 2.9% YoY in M&B channels with market share increasing by 0.2pp to 4.3% vs. Jan-Feb, +0.4pp yoy, mainly driven by volume growth by 4% yoy.

5. Biostime saw market share trending down from 7.8% in Jan-Feb to 7.5% in Mar-Apr, and Beingmate's market share decreased slightly to 4.7% in Mar-Apr. The majority of MNC players saw divergent market share movement, with Danone at 5.8% (+0.2ppt vs Jan-Feb, +0.6pp yoy), Wyeth at 1.1% (-0.2ppt vs. Jan-Feb, -1.5pp yoy), Nestle at 2.3% (-0.3ppt vs. Jan-Feb, -1ppt yoy), and MJN at 2.7% (-0.2ppt vs. Jan-Feb, +0.3pp yoy).

Exhibit 5: Feihe maintained its leading market share in IMF and value share increased slightly in Mar-Apr, and Yili/Mengniu's (excl. Yashili) offline market share was at $17.9\% / 1.2\%$

Offline domestic IMF brands' market share by value  
![](images/aa12f03dad179608ca2d745e938c7d17edecbf346cbfe9bebe76e3e8a2245bec.jpg)  
Source: Nielsen  
Exhibit 7: Feihe's/Yili's market share increased in Mar-Apr in the offline market, while Mengniu's market share decreased  
Nielsen market share for leading brands

![](images/2a3ea51c3588cf77a9d1010b9e4cf9d1b5569d1995a41ea5ea6158e7cade8bef.jpg)  
Source: Nielsen  
Source: Nielsen

Exhibit 6: MNC players saw sequential market share trend mixed in Mar-Apr, Friesland/Danone/A2 value share increased while Wyeth decreased vs. Jan-Feb Offline international IMF brands market share by value

![](images/6636b0cfd7d802e78309e452a4774952ac6a2f670eb17c04dfddebff568bdbd8.jpg)  
Exhibit 8: Big local brands collectively took 62% market share, flattish vs. Jan-Feb, while MNCs saw market share gain of 0.3pp vs Jan-Feb Market share, % of total infant formula offline channel  
Market share, % of total infant formula offline channel  
Offline sales market share breakdown

![](images/fcb15f9539988a2472f6eb89324058f615da3a1b3ea6876e919cd671a42e48a8.jpg)  
Source: Nielsen

## Online Market: Domestic brands sequentially weakened; Top MNC brands growth moderated potentially due to high comp last year on 618

On Tmall/Taobao/JD combined, infant milk formula sales declined by 19% yoy in May (vs. -14% yoy in Apr), with -2% yoy growth on Tmall/Taobao and -26% on JD on a tough base. Feihe declined by -30% yoy in May, vs. -47% yoy in Apr. Yili declined at -23% yoy in May vs. -21% yoy in Apr, and Yili + Pro-kido combined declined -17% in May vs. -10% in Apr. Among MNCs, Aptamil/A2/Biostime grew +6%/-25%/25% yoy in May, vs. +2%/+27%/+68% yoy in Apr, and Mead Johnson/Wyeth/Nutrilon declined significantly at -45%/-45%/-71% vs. -31%/-32%/-45% in Apr. Bellamy's growth momentum moderated at 19% in May vs. +80% in Apr.

On Tmall/Taobao, infant milk formula sales decreased by -2% in May vs 14% yoy in Apr. Top domestic brands gained market share sequentially in May, mainly Junlebao/Yili/Firmus/Biostime. Among local brands, Feihe's sales momentum sequentially moderated with 1% in May vs. 26% yoy in Apr potentially due to a tough comp in May 25. Yili (including Pro-Kido) increased by 3% in May vs 33% in Apr. Yili alone recorded +3% in May vs. +31% in Apr. Among MNC brands, Biostime/Mead Johnson (MJN)/Wyeth growth was mixed in May to +15%/+34%/+7% yoy vs. +56%/+70%/+19% in Apr.

Exhibit 9: Online IMF sales declined by -11% yoy in 1Q26 vs 4% growth in 4Q25
Tmall/Taobao/JD combined IMF quarterly growth

![](images/931f56268fdff45ac7aa51182f19d1d1d7f5c5fda18e963075562cd877b5eb61.jpg)  
Source: Moojing  
Exhibit 10: Online IMF sales declined by $19\%$ yoy in May vs. $-14\%$ yoy in Apr Tmall/Taobao/JD combined IMF monthly growth

![](images/3615e083bfc808f8e011c53a7509e4aab1b815aa07ef152a35efea1788c144b5.jpg)

Exhibit 11: Tmall/Taobao IMF sales decreased by -2% in May vs 14% yoy in Apr mainly on volume growth
Tmall/Taobao IMF monthly growth

![](images/f9f1f8b57c05ff3a63e2c9ea356e136b855a4efd3ec447cc9f67ddfe2b54045e.jpg)  
Exhibit 12: JD IMF sales declined at $-19\% / -14\%$ yoy in May/Apr  
JD IMF monthly growth

JD IMF  
![](images/f16518c05dd02ee17a2a04e33d32c4bc553941954b95f449e67af32c3fb4432b.jpg)  
Source: Moojing

Exhibit 13: Aptamil maintained its No.1 position with market share loss 0.9ppt mom to $20\%$ ; A2 lost 2.7ppt market share in May International IMF value Market share (Tmall+Taobao)  
![](images/4c7159bc842756ad195d23d152fb2e82e3d633f33d82144b982e6e53fd580639.jpg)  
Source: Moojing  
Source: Moojing  
Exhibit 14: Feihe/Yili's Market share on Tmall/Taobao was $14\% /9\%$ in May  
Domestic IMF value Market share (Tmall+Taobao)

![](images/09657982247ed353efda0c430d557ecd42dcb5e352179fa4e0fcf61068182caa.jpg)  
Source: Moojing

Feihe (Neutral): offline market share slightly recovered despite weak run-rate; Taobao/Tmall/JD decline narrowed

Tracked omni-channel sales including online sales combined with Nielsen offline sales point to -24% yoy decline in Mar-Apr, vs. -19% yoy in Jan-Feb.

In Mar-Apr 2026, Feihe's sales decline in the offline channel was $-12\%$ yoy (vs. $-15\%$ decline yoy in Jan-Feb), lagging the market run-rate of $-8.2\%$ yoy. Feihe's market share recorded $21\%$ in Mar-Apr, up by 0.4pp vs. Jan-Feb at $20.6\%$ , down 0.9pp yoy. The ASP in offline markets was $+0.9\%$ yoy in Mar-Apr, vs. $0.3\%$ in Jan-Feb. M&B saw ASP increased by $0.7\%$ yoy and MT channel saw ASP recovery at $3.2\%$ yoy, respectively.

On Tmall/Taobao/JD combined: Feihe declined by $-31\%$ yoy in May, vs. $-47\%$ in Apr. On Tmall/Taobao: Feihe's sales grew at $1\%$ in May vs. $+26\%$ yoy in Apr.

Exhibit 16: Feihe tracked Omnichannel sales down -18% yoy in 2H25 vs -16% sales decline reported

Exhibit 15: Feihe's sales decline narrowed to $-12\%$ yoy vs. $-15\%$ decline yoy in Jan-Feb, vs. industry's $-8.2\%$ yoy run-rate

Sales growth yoy (MT & MB channel combined)  
![](images/b8bded27ef297ef9d316f908e5707c40cb0ec71ba9b4c8d541ac4f9a7551dbd1.jpg)  
Source: Nielsen

![](images/aa702aae4e54b5d8408ad9a63a060559f59d93fd79871b20edd58b7565471092.jpg)  
Source: Company data, GS Global Investment Research, Nielsen, Moojing  
Exhibit 17: GS tracking online channel sales decline at -31% yoy in May, vs. -47% in Apr

Feihe: GS IMF tracker online sales yoy (Tmall/Taobao/JD)  
![](images/37c1eaaab7b08f0902e3dcc27236390c806aa875d5be4bc7ce5f98f55e997f1f.jpg)  
Exhibit 18: Feihe Tmall/Taobao IMF sales increased by grew at $1\%$ in May vs. $+26\%$ yoy in Apr. Tmall/Taobao IMF monthly growth

Firmus (Tmall/Taobao)  
![](images/eb8efcd1bb0be1c0e99b0681667e52dc099d4066bcc1e3c2b906a41499768c09.jpg)  
Source: Moojing, GS Global Investment Research  
Source: Moojing  
Exhibit 19: Feihe JD IMF sales decreased by $40\%$ yoy in May following the $-60\%$ yoy decline in Apr, mainly on weak volume since Jun 25  
JD IMF monthly growth

Firmus (JD)  
![](images/f94d642dacfe08d6f6b561077ca4519b45f69886b5e99f97f8c4ff7924646256.jpg)  
Source: Nielsen

## Valuation and key risks

## Feihe (Neutral):

Valuation methodology: We are Neutral-rated on Feihe. Our 12-m TP of HK\$3.43 is based on 11.0x 2027E P/E discounted back to mid-2027 using a 10.3% COE.

Key risks: 1) Higher/Lower-than-expected new birth rates; 2) More/Less intense competition; 3) Quicker/Slower premium segment growth; 4) Industry-wide food safety issues; 5) Higher/Lower-than-expected incremental policy support.

## Yili (Buy): Online sequentially weakened; offline resumed to positive growth

Tracked omni-channel sales including online sales combined with Nielsen offline sales point to -2% yoy in Mar-Apr vs. -1% yoy in Jan-Feb.

In Mar-Apr, Yili's sales growth in the offline channel was $1.9\%$ yoy (vs. $-0.9\%$ yoy in Jan-Feb), above the market run-rate o

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
