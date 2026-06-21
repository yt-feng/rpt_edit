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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China Cosmetics: 618 pulse check: performance in Douyin: MNCs/higher-end led; MGP rebound to $50\%+$ yoy

The 618 shopping festival in 2026 concluded on 18 Jun for Douyin and will be concluded on 21 Jun for Tmall. We summarize below key early color and data points and key takeaways for Douyin:

The top 500 cosmetics brands in Douyin grew by mid-30s yoy in May to Jun-18 with Jun-to date GMV yoy moderated vs May yoy, but still faster than 1Q26; we see consolidation trend with top 50 outgrowing at c.40% yoy while brands below 100 underperformed at high-20s yoy.

Performance by MNCs & locals/pricing segment (refer to Exhibit 3 for our definition for different pricing segment): Within top 500 brands, we see global brands tracking above local brands, in majority of the pricing segment except for premium as MGP managed to deliver $54\%$ yoy during the May to Jun-to-date; Overall luxury/premium brands recorded solid result, set to accelerate from mid-20s/high-20s yoy in May to high-30s/high-50s yoy in June to date, while mid-high end/mass market brands moderated from 40s yoy in May to high-teens to 20s yoy in June to date;

Brand performance in Douyin (refer to Exhibit 1 for Douyin tracker): For full period (May 15 - Jun 18), we saw western brands have c.140% completion rate vs local brands' 110% on average, while Japanese brands are on par to prior year:

1) Local brands: We saw strong performance across our covered local brands led by higher-end brands (i.e. Forest Cabin & Mao Geping). Forest Cabin is the leader with 188% yoy growth in Douyin for 2026 5.1-6.18 and highest full-period completion rate at 356%; Mao Geping achieved 54% yoy in 5.1-6.18 and full period completion of 150%, thanks to strong Jun performance (1-18) at 91% yoy, while Giant GMV was better than expected with 15% yoy growth for 2026 5.1-6.18 and Jun performance catching up at 44% yoy, leading to a 120% full period completion rate. Shanghai Jahwa and Botanee also delivered encouraging yoy growth with 137%/130% full period completion. Proya achieved 24% yoy for 5.1-6.18 and 121% full 618 completion despite Jun weakened at 5% yoy decline. On the other hand, Bloomage and Chicmax remained under pressure at 77%/63% full period completion.

2) Western brands: Premium brands continued to be the drivers for Western brands. Estee Lauder Group led with $56\%$ yoy growth in Douyin for 2026 5.1-6.18 and further accelerated to $75\%$ yoy in 6.1-6.18, with the highest full-period completion rate at $155\%$ , where we see strength in higher-end brands (Estee

Valerie Zhou

+852-2978-0820 | valerie.zhou@gs.com
GS (Asia) L.L.C.

Lauder/Lamer at 167%/154% full period completion); L'Oréal Group also achieved 33% yoy in 5.1-6.18 and full period completion of 130%, thanks to strong performance in higher-end brands (Skinceuticals/YSL reached 190%/176% full period completion rates), though mass-market brands were behind. Beiersdorf also delivered encouraging growth with 146% full period completion thanks to strong performance of La Prairie at 168% completion.

3) Japanese brands: we note a slowdown of growth in Jun across Japanese names; Shiseido Group declined at 21% in Jun 1-18, still delivering 113% full period completion thanks to outperformance of higher-end brands CPB/NARS at 166%/151% full period completion. Decorte (under Kose) / SK-II (under P&G) saw weakness at 40%/83% full period completion.

We reiterate our top-pick Buy (on CL) on Mao Geping for the strong full 618 period results in Douyin despite the softer sales in May, which we attribute to Company's deliberate pacing and online competitive strategy, a pattern previously observed during major events like Double 11 and Company managed to deliver solid and healthy results set in topline growth and margin profile. We are going to host a cosmetics expert call at 10am on 22 Jun (Monday), focusing more on Tmall and comprehensive operational metrics including discounts/platform and governments subsidies/product returns etc, more to follow.

More reads:

China Cosmetics: Monthly tracker: May-26: accelerating versus 1Q; local brands rebound likely on subsidies; MNCs continue to be strong June to date

China Cosmetics: 618 pulse check: Beauty GMV tracking well with likely improving ROI; Proya led, MGP accelerating and Giant better than feared; MNCs continue outperforming

China Cosmetics: 618 pulse check: Top tier KOL Day 1 livestreaming better than Women's day though not overly exciting; Mao Geping continues to lead

Exhibit 1: Douyin: For full period (May 15 - Jun 18) vs 618 last year, Forest Cabin led with $300\%+$ completion rate, partly due to an easier base, followed by MGP/Shanghai Jahwa/Botanee/Proya/Giant at $150\%/137\%/130\%/121\%/120\%$ . We note strong performances for MNC leaders as well, with Estee Lauder Group/Beiersdorf/Loreal Group/Shiseido Group at $155\%/146\%/130\%/113\%$

<table><tr><td>Douyin GMV</td><td>2026 5.1-6.18 yoy growth</td><td>2026 6.1-6.18 yoy growth</td><td>2026 5.15-6.18 as of 2025 5.13-6.18 (Full period Completion Rate)</td></tr><tr><td colspan="4">Local brands</td></tr><tr><td>Proya</td><td>24%</td><td>-5%</td><td>121%</td></tr><tr><td>Proya</td><td>31%</td><td>-13%</td><td>128%</td></tr><tr><td>TIMAGE</td><td>-25%</td><td>33%</td><td>72%</td></tr><tr><td>Off &amp; Relax</td><td>51%</td><td>84%</td><td>150%</td></tr><tr><td>Giant</td><td>15%</td><td>44%</td><td>120%</td></tr><tr><td>Comfy</td><td>7%</td><td>37%</td><td>109%</td></tr><tr><td>Collgene</td><td>52%</td><td>66%</td><td>170%</td></tr><tr><td>Botanee</td><td>31%</td><td>13%</td><td>130%</td></tr><tr><td>Winona</td><td>29%</td><td>10%</td><td>128%</td></tr><tr><td>Bloomage</td><td>-17%</td><td>-42%</td><td>77%</td></tr><tr><td>QuadHA</td><td>-35%</td><td>-71%</td><td>50%</td></tr><tr><td>Biohyalux</td><td>-15%</td><td>-33%</td><td>92%</td></tr><tr><td>Medrepair</td><td>54%</td><td>43%</td><td>159%</td></tr><tr><td>Shanghai Jahwa</td><td>68%</td><td>-16%</td><td>137%</td></tr><tr><td>Herborist</td><td>24%</td><td>-67%</td><td>67%</td></tr><tr><td>Dr. Yu</td><td>90%</td><td>78%</td><td>196%</td></tr><tr><td>Liushen</td><td>128%</td><td>73%</td><td>224%</td></tr><tr><td>Shanghai Chicmax</td><td>-21%</td><td>-55%</td><td>63%</td></tr><tr><td>KANS</td><td>-24%</td><td>-57%</td><td>59%</td></tr><tr><td>New Page</td><td>152%</td><td>51%</td><td>206%</td></tr><tr><td>ARMIYO</td><td>97%</td><td>58%</td><td>194%</td></tr><tr><td>MGP</td><td>54%</td><td>91%</td><td>150%</td></tr><tr><td>MAOEPING</td><td>54%</td><td>91%</td><td>150%</td></tr><tr><td>Forest Cabin</td><td>188%</td><td>162%</td><td>356%</td></tr><tr><td colspan="4">MNC</td></tr><tr><td>L&#x27;Oreal</td><td>33%</td><td>13%</td><td>130%</td></tr><tr><td>L&#x27;Oreal Paris</td><td>7%</td><td>-22%</td><td>101%</td></tr><tr><td>Lancome</td><td>29%</td><td>51%</td><td>124%</td></tr><tr><td>Maybelline</td><td>-7%</td><td>-21%</td><td>85%</td></tr><tr><td>HR</td><td>24%</td><td>9%</td><td>121%</td></tr><tr><td>Skinceuticals</td><td>89%</td><td>57%</td><td>190%</td></tr><tr><td>La Roche Posay</td><td>25%</td><td>-13%</td><td>111%</td></tr><tr><td>3CE</td><td>64%</td><td>23%</td><td>142%</td></tr><tr><td>Kiehl&#x27;s</td><td>91%</td><td>45%</td><td>185%</td></tr><tr><td>Armani</td><td>40%</td><td>7%</td><td>133%</td></tr><tr><td>YSL</td><td>74%</td><td>36%</td><td>176%</td></tr><tr><td>Estee Lauder</td><td>56%</td><td>75%</td><td>155%</td></tr><tr><td>Estee Lauder</td><td>65%</td><td>115%</td><td>167%</td></tr><tr><td>La Mer</td><td>54%</td><td>79%</td><td>154%</td></tr><tr><td>Clinique</td><td>10%</td><td>27%</td><td>107%</td></tr><tr><td>Origins</td><td>22%</td><td>37%</td><td>118%</td></tr><tr><td>Bobbi Brown</td><td>54%</td><td>35%</td><td>149%</td></tr><tr><td>M.A.C.</td><td>49%</td><td>-16%</td><td>134%</td></tr><tr><td>Jo Malone London</td><td>-17%</td><td>11%</td><td>92%</td></tr><tr><td colspan="4">LG H&amp;H</td></tr><tr><td>Whoo</td><td>-32%</td><td>-1%</td><td>67%</td></tr><tr><td>Shiseido</td><td>14%</td><td>-21%</td><td>113%</td></tr><tr><td>Shiseido</td><td>-38%</td><td>-56%</td><td>61%</td></tr><tr><td>CPB</td><td>63%</td><td>40%</td><td>166%</td></tr><tr><td>Nars</td><td>31%</td><td>50%</td><td>151%</td></tr><tr><td>ANESSA</td><td>35%</td><td>-41%</td><td>118%</td></tr><tr><td>The Ginza</td><td>532%</td><td>n.m.</td><td>n.m.</td></tr><tr><td>Elixir</td><td>252%</td><td>234%</td><td>319%</td></tr><tr><td>IPSA</td><td>188%</td><td>81%</td><td>292%</td></tr><tr><td>Amore</td><td>-42%</td><td>-63%</td><td>53%</td></tr><tr><td>Sulwhasoo</td><td>-54%</td><td>-76%</td><td>42%</td></tr><tr><td>Laneige</td><td>-7%</td><td>4%</td><td>90%</td></tr><tr><td>Innisfree</td><td>-36%</td><td>-52%</td><td>60%</td></tr><tr><td colspan="4">Kose</td></tr><tr><td>Decorte</td><td>-54%</td><td>-46%</td><td>40%</td></tr><tr><td>Beiersdorf</td><td>50%</td><td>17%</td><td>146%</td></tr><tr><td>NIVEA</td><td>82%</td><td>127%</td><td>176%</td></tr><tr><td>Eucerin</td><td>19%</td><td>-28%</td><td>117%</td></tr><tr><td>La Prairie</td><td>73%</td><td>38%</td><td>168%</td></tr><tr><td colspan="4">P&amp;G</td></tr><tr><td>Sk II</td><td>-15%</td><td>-27%</td><td>83%</td></tr></table>

Source: Chanmama, Data compiled by GS Global Investment Research

Tmall+Douyin+JD, latest in May:

Exhibit 2: Tmall+Douyin+JD: Growth of MNC brands has outperformed local brands since 4Q25  
Cosmetics Monthly Online GMV YoY by Brand Positioning  
![](images/23275637ebce255f76ba2ea1a1a118af32c40621def99247e57209b8753ddb8c.jpg)

<details>
<summary>line chart</summary>

| Month     | MNC   | Domestic |
| --------- | ----- | -------- |
| Jan-Feb-25 | 0%    | 18%      |
| Mar-25    | -30%  | 10%      |
| Apr-25    | -30%  | 22%      |
| May-25    | -20%  | -5%      |
| Jun-25    | -15%  | 15%      |
| Jul-25    | -5%   | 12%      |
| Aug-25    | -10%  | 10%      |
| Sep-25    | 5%    | 5%       |
| Oct-25    | 10%   | -10%     |
| Nov-25    | 10%   | -10%     |
| Dec-25    | 25%   | 20%      |
| Jan-Feb-26 | 10%   | 5%       |
| Mar-26    | 15%   | 10%      |
| Apr-26    | 10%   | 5%       |
| May-26    | 15%   | 10%      |
</details>

Source: Chanmama, Moojing, Data compiled by GS Global Investment Research

Exhibit 3: Tmall+Douyin+JD: Growth of Domestic Premium brands (i.e. Mao Geping) has outperformed MNC peers  
Cosmetics Monthly Online GMV YoY by Brand Positioning  
![](images/feeaf5ce18fdb5a8beb27e6546849279ab983c93f228375feb1502c529a2fccb.jpg)

<details>
<summary>line chart</summary>

| Month     | MNC Luxury | MNC Premium | Domestic Premium |
|-----------|------------|-------------|------------------|
| Jan-Feb-25 | -          | -           | 80%              |
| Mar-25    | -          | -           | 30%              |
| Apr-25    | -          | -           | 50%              |
| May-25    | 10%        | -           | 90%              |
| Jun-25    | -          | -           | 70%              |
| Jul-25    | -          | -           | 10%              |
| Aug-25    | -          | -           | 120%             |
| Sep-25    | 20%        | -           | 50%              |
| Oct-25    | 10%        | 30%         | 40%              |
| Nov-25    | 10%        | 30%         | 40%              |
| Dec-25    | 30%        | 40%         | 130%             |
| Jan-Feb-26 | 30%        | 30%         | 20%              |
| Mar-26    | 40%        | 20%         | 110%             |
| Apr-26    | -          | 20%         | 40%              |
| May-26    | 10%        | 30%         | 40%              |
</details>

Classification of brand positioning (by core SKU retail price on Tmall flagship store): Luxury: Skincare > Rmb 730, Colour Cosmetics > Rmb 400; Premium: Skincare Rmb 490-730, Colour Cosmetics Rmb 260-400 (also include professional color cosmetics brands). Exception: Sisley, Guerlain, Tom Ford in luxury; Clarins, SK-II, Shu Uemure, Charlotte Tibury, Nars in premium.  
Source: Chanmama, Moojing, Data compiled by GS Global Investment Research

Exhibit 4: Tmall+Douyin+JD: Growth of MNC Mid-to-high end brands has outperformed local peers in 2026  
Cosmetics Monthly Online GMV YoY by Brand Positioning  
![](images/464ad4e6067ede6f4de73af6595c07cd646f4ddc79df18f41614c7837605c617.jpg)

<details>
<summary>line chart</summary>

| Month     | MNC Mid-to-high end | Domestic Mid-to-high end |
| --------- | -------------------- | ------------------------- |
| Jan-Feb-25 | -5%                  | 12%                       |
| Mar-25    | -10%                 | 8%                        |
| Apr-25    | -20%                 | 10%                       |
| May-25    | -35%                 | -20%                      |
| Jun-25    | -10%                 | -5%                       |
| Jul-25    | 10%                  | -5%                       |
| Aug-25    | -15%                 | -5%                       |
| Sep-25    | -10%                 | -10%                      |
| Oct-25    | -5%                  | -25%                      |
| Nov-25    | 0%                   | -10%                      |
| Dec-25    | 5%                   | 10%                       |
| Jan-Feb-26 | 0%                   | -5%                       |
| Mar-26    | 5%                   | -10%                      |
| Apr-26    | 10%                  | -5%                       |
| May-26    | 15%                  | 5%                        |
</details>

Classification of brand positioning (by core SKU retail price on Tmall flagship store): Mid-to-high end: Skincare Rmb 150-490, Colour Cosmetics Rmb 170-260. Exception: La Roche-Posay in mid-to-high end.  
Source: Chanmama, Moojing, Data compiled by GS Global Investment Research

Exhibit 5: Tmall+Douyin+JD: In mass brands, local has outperformed MNC growth  
Cosmetics Monthly Online GMV YoY by Brand Positioning  
![](images/e5b9434012164b6a54a75b8e03912e8768bbec4d8438432505d6791edd70fcbf.jpg)

<details>
<summary>line chart</summary>

Cosmetics Monthly Online GMV YoY by Brand Positioning
| Month | MNC Mass (%) | Domestic Mass (%) |
|---|---|---|
| Jan-Feb-25 | 5 | 15 |
| Mar-25 | -20 | 10 |
| Apr-25 | -45 | 40 |
| May-25 | -35 | 15 |
| Jun-25 | -10 | 35 |
| Jul-25 | -5 | 48 |
| Aug-25 | -25 | 25 |
| Sep-25 | -15 | 22 |
| Oct-25 | -25 | 18 |
| Nov-25 | 5 | 10 |
| Dec-25 | 10 | 12 |
| Jan-Feb-26 | 5 | 8 |
| Mar-26 | -5 | 18 |
| Apr-26 | 20 | 8 |
| May-26 | -18 | 12 |
</details>

Classification of brand positioning (by core SKU retail price on Tmall flagship store): Mass: Skincare <Rmb 150, Colour Cosmetics <Rmb 170.  
Source: Chanmama, Moojing, Data compiled by GS Global Investment Research

Exhibit 6: 618 (May+ Jun) contributed around close to $75\%$ of 2Q online GMV (incl. Taobao/Tmall/JD), or $21\%$ of full year GMV distribution by month over 2020-2025 (Tmall+Taobao+JD)

<table><tr><td colspan="13">GMV contribuion</td></tr><tr><td></td><td></td><td>Jan/Feb</td><td>Mar (3.08)</td><td>Apr</td><td>May (6.18)</td><td>Jun (6.18)</td><td>Jul</td><td>Aug</td><td>Sept</td><td>Oct (11.11)</td><td>Nov (11.11)</td><td>Dec</td></tr><tr><td rowspan="6">Cosmetics</td><td>2020</td><td>10%</td><td>8%</td><td>7%</td><td>8%</td><td>9%</td><td>6%</td><td>8%</td><td>7%</td><td>8%</td><td>21%</td><td>8%</td></tr><tr><td>2021</td><td>13%</td><td>9%</td><td>6%</td><td>7%</td><td>12%</td><td>6%</td><td>7%</td><td>7%</td><td>7%</td><td>20%</td><td>7%</td></tr><tr><td>2022</td><td>15%</td><td>8%</td><td>6%</td><td>6%</td><td>13%</td><td>5%</td><td>7%</td><td>7%</td><td>7%</td><td>19%</td><td>6%</td></tr><tr><td>2023</td><td>15%</td><td>10%</td><td>8%</td><td>6%</td><td>12%</td><td>6%</td><td>7%</td><td>6%</td><td>7%</td><td>17%</td><td>6%</td></tr><tr><td>2024</td><td>14%</td><td>9%</td><td>7%</td><td>13%</td><td>7%</td><td>5%</td><td>6%</td><td>7%</td><td>15%</td><td>10%</td><td>6%</td></tr><tr><td>2025</td><td>15%</td><td>9%</td><td>7%</td><td>12%</td><td>9%</td><td>5%</td><td>6%</td><td>6%</td><td>14%</td><td>9%</td><td>6%</td></tr></table>

Source: Moojing, Data compiled by GS Global Investment Research

Exhibit 7: We saw shorter period for 618 with later start for Tmall/Douyin Time period of 618 promotion events (2026 vs. 2025)

<table><tr><td>Platform</td><td>Pre-sale period</td><td>Official sales period</td></tr><tr><td colspan="3">2026</td></tr><tr><td>Tmall</td><td>May 21 20:00 - May 26</td><td>First Round: May 27 - May 30Second Round: May 31 - Jun 3Third Round: Jun 4 - Jun 21</td></tr><tr><td>JD</td><td>-</td><td>Mothers&#x27; Day Festival: May 6 - May 10618 First Round: May 11 - May 30618 Second round: May 31 - Jun 20</td></tr><tr><td>Douyin</td><td>-</td><td>May 15 00:00 - Jun 18 23:59</td></tr><tr><td colspan="3">2025</td></tr><tr><td>Tmall</td><td>First Round: May 13 20:00 - May 16 17:59Second Round: Jun 12 10:00 - Jun 14 22:59</td><td>First round: May 16 20:00 - May 26 23:59Secound round: Jun 15 00:00 - Jun 20 23:59</td></tr><tr><td>JD</td><td>-</td><td>First round: May 13 20:00 - May 28 23:59Second round: May 31 20:00 - Jun 20 23:59</td></tr><tr><td>Douyin</td><td>-</td><td>May 13 00:00 - Jun 18 23:59</td></tr></table>

Source: Tmall, JD, Douyin, Data compiled by GS Global Investment Research

Exhibit 8: JD/Douyin offering smaller discounts vs. last year's 618 Discount level across major online platform of cosmetics

<table><tr><td rowspan="2">Platform</td><td colspan="2">2026</td><td colspan="3">2025</td><td colspan="3">2024</td><td colspan="3">2023</td></tr><tr><td>618</td><td>38 Women&#x27;s day</td><td>Double 11</td><td>618</td><td>38 Women&#x27;s day</td><td>Double 11</td><td>618</td><td>38 Women&#x27;s day</td><td>Double 11</td><td>618</td><td>38 Women&#x27;s day</td></tr><tr><td>Tmall</td><td>From 15% off</td><td>Taobao: from 12% off Tmall: from 12% off</td><td>Taobao: from 15% off Tmall: from 15% off</td><td>15% off (up to 50% off)</td><td>30 off 200+ (up to 15% off)</td><td>Taobao: 30 off 200+ (up to 15% off) Tmall: 50 off 300+ (up to 17% off)</td><td>50 off 300+ (up to 17% off)</td><td>40 off 300+ (up to 13% off)</td><td>50 off 300+ (up to 17% off)</td><td>50 off 300+ (up to 17% off)</td><td>From 10% off</td></tr><tr><td>JD</td><td>10 off 100+/ 20 off 200+/ 300 off 5,000+/80 off for any (up to 10% off)</td><td>20 off 200+ (up to 10% off)</td><td>From 15% off/50 off 300 (up to 17% off)</td><td>20 off 200+/ 50 off 299+</td><td>30 off 200+ (up to 15% off)</td><td>50 off 299+ (up to 17% off)</td><td>50 off 299+ (up to 17% off)</td><td>40 off 300+ (up to 13% off)</td><td>50 off 299+ (up to 17% off)</td><td>50 off 299+ (up to 17% off)</td><td>20 off 200+ (up to 10% off)</td></tr><tr><td>Douyin</td><td>40 off 300+/ 80 off 600+/ 180 off 1,500+/ 420 off 3,000+/780 off 6,000+ (u

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
