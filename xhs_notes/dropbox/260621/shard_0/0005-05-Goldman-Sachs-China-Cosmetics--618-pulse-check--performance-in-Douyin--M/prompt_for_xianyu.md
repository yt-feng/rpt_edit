你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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

<table><tr><td colspan="13">GMV contribuion</td></tr><tr><td></td><td></td><td>Jan/Feb</td><td>Mar (3.08)</td><td>Apr</td><td>May (6.18)</td><td>Jun (6.18)</td><td>Jul</td><td>Aug</td><td>Sept</td><td>Oct (11.11)</td><td>Nov (11.11)</td><td>Dec</td></tr><tr><td rowspan="6">Cosmetics</td><td>2020</td><td>10%</td><td>8%</td><td>7%</td><td>8%</td><td>9%</td><td>6%</td><td>8%</td><td>7%</td><td>8%</td><td>21%</td><td>8%</td></tr><tr><td>2021</td><td>13%</td><td>9%</td><td>6%</td><td>7%</td><td>12%</td><td>6%</td><td>7%</td><td>7%</td><td>7%</td><td>20%</td><td>7%</td></tr><tr><td>2022</td><td>15%</td><td>8%</td><td>6%</td><td>6%</td><td>13%</td><td>5%</td><td>7%</td><td>7%</td><td>7%</td><td>19%</td><td>6%</td></tr><tr><td>2023</td><td>15%</td><td>10%</td><td>8%</td><td>6%</td><td>12%</td><td>6%</td><td>7%</td><td>6%</td><td>7%</td><td>17%</td><td>6%</td></tr><tr><td>2024</td><td>14%</td><td>9%</td><td>7%</td><td>13%</td><td>7%</td><td>5%</td><td>6%</td><td>7%</td><td>15%</td><td>10%</td><td>6%</td></tr><tr><td>2025</td><td>15%</td><td>9%</td><td>7%</td><td>12%</td><td

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
