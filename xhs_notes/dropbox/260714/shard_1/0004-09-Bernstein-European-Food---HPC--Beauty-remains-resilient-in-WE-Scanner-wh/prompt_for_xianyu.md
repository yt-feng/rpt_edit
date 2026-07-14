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
European Food & HPC

# European Food & HPC: Beauty remains resilient in WE Scanner while Food and Consumer Health slow

![](images/de1f014f085273cb58adb247c996101caae6b7523fdd580f1dba358c94d15129.jpg)

Callum Elliott, CFA, ACA

+44 20 7676 7183

callum.elliott@bernsteinsg.com

![](images/d6819a909e25d84928a43aafceab676b91003d9aefb12f38383b29f596a45685.jpg)

Victoria Nice, CFA

+44 20 7762 5862

victoria.nice@bernsteinsg.com

![](images/b1ea1fa85641847e283858561e058cfd81ab196b1ecc4ae7f00ac597b9ea0d19.jpg)

Henry Dennis

+44 20 7676 6776

henry.dennis@bernsteinsg.com

![](images/68b8cf3158c2cc18b5f52bb9642adb3060363a24e1c45ebe38cfdd2250724a9c.jpg)

Simran Cheema

+44 20 7676 6705

simran.cheema@bernsteinsg.com

This note covers latest trends in Western Europe Scanner data for the four weeks ending 14 $^{th}$ June.

Key highlights: CPG performance moderated in the period, with Food decelerating to +1.9% (vs +4.2%), Consumer Health slowing to -1.3% (vs +5.0%), and Household remaining weak at -0.7% (vs -0.3%). The Beauty & Personal Care category remains resilient, improving to +4.1% (vs +3.6%), supported by strong volume growth alongside improving (but still negative price/mix).

At the company level, Nestlé continues to accelerate with growth of +2.6% (vs +1.8%) on recovering volumes alongside share gains, while L'Oréal stays strong alongside the Beauty market with growth of +5.6% (vs +5.1%). Unilever growth weakened, turning slightly negative at -1.5% (vs -0.1%) with declining volumes. Danone growth improves significantly, accelerating to +4.5% (vs +1.5%) as volumes continue to step up. Haleon turns negative with -0.4% growth (vs +2.4%), as volumes significantly decelerate. Reckitt likewise slows in the period, with growth of -4.3% (vs +1.5%) again due to a volume slowdown. Henkel maintains its track record of weak growth, delivering -3.0% (vs -2.1%) as volumes slow. Beiersdorf growth significantly improved, growing +10.5% (vs -4.1%), and Lindt continued to decline (-12.0%).

Food market delivered +1.9% value growth, decelerating from +4.2% in the prior period. Volumes remained positive with +0.5% growth (from +2.4%), while price/mix grew +1.3% in the period (vs +1.8%).

Beauty & Personal Care (B&PC) market delivered +4.1% value growth, up slightly from +3.6% in the prior period. Growth was supported by continued strong volume performance at +4.7% (vs +4.9%), while price/mix remained negative at -0.6% (vs -1.3%), indicating ongoing price pressure partially offsetting volume gains.

Household market was again negative in this period with -0.7% value growth, down from -0.3% in the prior period. This decline was driven by negative volume growth of -0.6% (vs +0.1%), while price/mix improved slightly to 0.0% (vs -0.3%).

Consumer Health market growth slowed to -1.3% value growth, down from +5.0% in the prior period. This deceleration was mostly volume driven, with volume growth slowing to -4.6% (vs +3.4%). Price/mix accelerated to +3.5% (vs +1.5%).

## Company performance:

Nestlé's value growth improved slightly to $+2.6\%$ , up from $1.8\%$ in the prior period. This was driven by volume growth of $+3.3\%$ (vs $+0.9\%$ ), while price/mix softened to $-0.7\%$ (vs $+1.0\%$ ). Market shares improved +33bps, compared to -23bps in the previous period, driven mainly by a big improvement in performance in instant coffee.

L'Oréal's performance remains strong, recording +5.6% value growth compared to +5.1% in the prior period. Volume growth accelerated modestly to +5.2% (vs +4.3%), while price/mix slowed to +0.4% (vs +0.8%). Market share gains slowed to +4bps from +17bps previously.

Unilever's value performance weakened to $-1.5\%$ , down from $-0.1\%$ in the prior period. This was driven by weaker volume performance at $-2.6\%$ (vs $-3.8\%$ ), while price/mix remained positive but softened to $+1.1\%$ (vs $+3.8\%$ ).

Danone's performance stepped up to value growth of $+4.5\%$ compared to $+1.5\%$ in the prior period. Volumes accelerated to $+3.3\%$ (vs $+1.2\%$ ). Price/mix also improved with growth of $+1.2\%$ (vs $+0.3\%$ ).

Haleon's performance sharply decelerated, with value growth easing to $-0.4\%$ (vs $+2.4\%$ ). Price/mix growth stepped up significantly, to $+3.1\%$ (vs $+0.3\%$ ), however volumes declined to $-3.3\%$ (vs $+2.1\%$ ) dragging down overall performance. However, it is important to note that European scanner data has channel limitations, meaning these figures may not fully capture Haleon's total sales performance.

Reckitt (Core RKT) declined with value growth of -4.3%, compared to +1.5% in the prior period. This was driven primarily by a marked volume slow-down, with volume growth of -6.5% (vs +1.0%), while price/mix increased to +2.3% (vs +0.6%). Market share fell in the period with -62bps share loss.

Henkel's persistent growth declines continue, with value growth of $-3.0\%$ , from $-2.1\%$ in the prior period. This was driven by softer volume performance, which declined at $-2.5\%$ (vs $-0.1\%$ ), with price/mix slightly improving but remaining negative at $-0.6\%$ (vs $-2.0\%$ ). Market share losses continued at a similar pace of $-47bps$ (vs $-49bps$ ), reflecting ongoing competitive pressure.

Beiersdorf growth significantly improved in the period, accelerating to +10.5%, compared with -4.1% in the prior period. Growth was driven by strong acceleration in both the Deodorants and Sun Care categories. Volume performance stepped up to 12%, while price/mix improved modestly to -1.3% (vs -2.9%), though remained a drag on growth. Market share losses improved to narrowed to +22bps from -60bps previously.

Lindt recorded weak sales growth in May at -12.0% (vs -13.7%), with volume growth at -18.2% (vs -22.9%).

## BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Rating</td><td colspan="3">10 Jul 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">EV/EBITDA (x)</td></tr><tr><td>Cur</td><td>ClosingPrice</td><td>PriceTarget</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>BEI.GR (Beiersdorf)</td><td>O</td><td>EUR</td><td>77.66</td><td>95.00</td><td>(47.7)%</td><td>EUR</td><td>4.44</td><td>4.29</td><td>4.59</td><td>8.9</td><td>9.1</td><td>8.6</td></tr><tr><td>BN.FP (Danone)</td><td>O</td><td>EUR</td><td>72.42</td><td>92.00</td><td>(11.4)%</td><td>EUR</td><td>3.80</td><td>3.93</td><td>4.38</td><td>13.6</td><td>12.4</td><td>11.6</td></tr><tr><td>HLN.LN (Haleon)</td><td>M</td><td>GBp</td><td>361.80</td><td>415.00</td><td>(20.4)%</td><td>GBP</td><td>0.19</td><td>0.20</td><td>0.22</td><td>14.4</td><td>13.6</td><td>12.9</td></tr><tr><td>HEN3.GR (Henkel)</td><td>M</td><td>EUR</td><td>74.44</td><td>74.96</td><td>(8.9)%</td><td>EUR</td><td>5.34</td><td>5.45</td><td>6.01</td><td>9.2</td><td>9.1</td><td>8.2</td></tr><tr><td>HEN.GR (Henkel)</td><td>M</td><td>EUR</td><td>70.05</td><td>70.00</td><td>(6.2)%</td><td>EUR</td><td>5.32</td><td>5.43</td><td>5.99</td><td>9.2</td><td>9.1</td><td>8.2</td></tr><tr><td>OR.FP (L&#x27;Oréal)</td><td>M</td><td>EUR</td><td>381.00</td><td>405.00</td><td>(17.9)%</td><td>EUR</td><td>12.25</td><td>14.05</td><td>15.43</td><td>20.4</td><td>18.6</td><td>17.3</td></tr><tr><td>LISP.SW (Lindt)</td><td>M</td><td>CHF</td><td>9,250.00</td><td>11,600</td><td>(47.0)%</td><td>CHF</td><td>3,136.79</td><td>3,233.70</td><td>3,640.96</td><td>17.9</td><td>17.0</td><td>15.3</td></tr><tr><td>LISN.SW (Lindt)</td><td>M</td><td>CHF</td><td>94,700</td><td>116,000</td><td>(44.7)%</td><td>CHF</td><td>3,136.79</td><td>3,233.70</td><td>3,640.96</td><td>17.9</td><td>17.0</td><td>15.3</td></tr><tr><td>NESN.SW (Nestle)</td><td>M</td><td>CHF</td><td>83.16</td><td>74.00</td><td>(10.8)%</td><td>CHF</td><td>4.42</td><td>4.31</td><td>4.67</td><td>19.5</td><td>21.2</td><td>19.8</td></tr><tr><td>RKT.LN (Reckitt)</td><td>O</td><td>GBp</td><td>5,018.00</td><td>7,500.00</td><td>(19.3)%</td><td>GBP</td><td>3.53</td><td>3.31</td><td>3.67</td><td>7.7</td><td>10.8</td><td>10.1</td></tr><tr><td>ULVR.LN (Unilever)</td><td>O</td><td>GBp</td><td>4,599.00</td><td>5,800.00</td><td>(22.9)%</td><td>EUR</td><td>3.08</td><td>3.23</td><td>3.45</td><td>13.8</td><td>13.8</td><td>12.9</td></tr><tr><td>UNA.NA (Unilever)</td><td>O</td><td>EUR</td><td>54.01</td><td>66.90</td><td>(21.8)%</td><td>EUR</td><td>3.08</td><td>3.23</td><td>3.45</td><td>13.8</td><td>13.8</td><td>12.9</td></tr><tr><td>EDME</td><td></td><td></td><td>1,593.41</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

We have Outperform ratings on Beiersdorf (€95), Reckitt (£75), Danone (€92), and Unilever (€66.90/£58); and Market-Perform ratings Henkel (€74.96 preference / €70 ordinary), Haleon (£4.15), Nestlé (CHF 74), L'Oréal (€405), and Lindt (CHF 116,000/11,600).

## DETAILS

This monthly report shows sales, volume, pricing growth and share trends in Europe for the top categories of the 11 major companies in our European Food & HPC Group (Beiersdorf, Danone, Essity, Haleon, Henkel, Lindt, L'Oréal, Nestlé, Reckitt and Unilever), as well as Private Label and the overall market. We use NielsenIQ data which covers mostly the grocery, convenience and drug channels, and so does not necessarily cover all channels used by all companies. The data is an aggregate of the top 9 markets in Europe (France, Germany, Italy, Spain, UK, Netherlands, Belgium, Portugal and Austria).

Latest Data: 4 weeks to 14 $^{th}$ June.

## INDEX

Exhibit 1 shows performance by our covered companies in previous two quarters.

Exhibit 2 shows the market value, volume and pricing growth for the 37 major Food categories we track.

Exhibits 4,6 and 8 show HPC market growth: Exhibit 3 shows the market value, volume and pricing growth for the 17 major Beauty & Personal Care categories we track; and Exhibit 5 shows the market value, volume and pricing growth for the 9 major Household categories we track; and Exhibit 7 show the market value, volume and pricing growth for the 4 major Consumer Health categories we track.

Exhibits 10-103 show the market share and market value, volume and pricing growth for Beiersdorf, Danone, Essity, Haleon, Henkel, Lindt, L'Oréal, Nestlé, Reckitt, Unilever, and for Private Label.

Exhibits 104 and 105 show sales growth for the Food & HPC market categories.

EXHIBIT 1: Growth Data Summary for Latest Quarters

<table><tr><td rowspan="2">Company</td><td colspan="3">YoY Value Growth</td><td colspan="3">YoY Volume Growth</td><td colspan="3">YoY Pricing Growth</td><td colspan="3">% Promo Sales</td></tr><tr><td>2026Q2</td><td>2026Q1</td><td>Δ</td><td>2026Q2</td><td>2026Q1</td><td>Δ</td><td>2026Q2</td><td>2026Q1</td><td>Δ</td><td>2026Q2</td><td>2026Q1</td><td>Δ</td></tr><tr><td>Nestle</td><td>0.7%</td><td>2.0%</td><td>-1.3%</td><td>0.0%</td><td>-1.7%</td><td>1.7%</td><td>0.7%</td><td>3.7%</td><td>-3.0%</td><td>28.0%</td><td>26.9%</td><td>1.0%</td></tr><tr><td>L&#x27;Oreal</td><td>6.0%</td><td>4.2%</td><td>1.8%</td><td>5.4%</td><td>4.3%</td><td>1.1%</td><td>0.6%</td><td>-0.1%</td><td>0.6%</td><td>27.7%</td><td>24.6%</td><td>3.1%</td></tr><tr><td>Unilever</td><td>0.5%</td><td>0.0%</td><td>0.5%</td><td>-2.5%</td><td>-3.7%</td><td>1.2%</td><td>3.0%</td><td>3.9%</td><td>-0.8%</td><td>35.9%</td><td>35.9%</td><td>0.0%</td></tr><tr><td>Danone</td><td>1.3%</td><td>-0.2%</td><td>1.5%</td><td>0.4%</td><td>-2.1%</td><td>2.5%</td><td>1.0%</td><td>2.0%</td><td>-1.0%</td><td>23.7%</td><td>24.4%</td><td>-0.7%</td></tr><tr><td>Haleon</td><td>2.8%</td><td>2.7%</td><td>0.1%</td><td>2.2%</td><td>1.2%</td><td>0.9%</td><td>0.6%</td><td>1.5%</td><td>-0.8%</td><td>26.2%</td><td>24.6%</td><td>1.6%</td></tr><tr><td>Reckitt</td><td>-1.2%</td><td>-1.6%</td><td>0.3%</td><td>-2.4%</td><td>-4.7%</td><td>2.3%</td><td>1.2%</td><td>3.2%</td><td>-2.1%</td><td>29.3%</td><td>29.2%</td><td>0.2%</td></tr><tr><td>Henkel</td><td>-2.0%</td><td>-3.0%</td><td>1.1%</td><td>-0.5%</td><td>-2.6%</td><td>2.1%</td><td>-1.5%</td><td>-0.4%</td><td>-1.1%</td><td>32.4%</td><td>34.1%</td><td>-1.7%</td></tr><tr><td>Beiersdorf</td><td>0.9%</td><td>0.2%</td><td>0.7%</td><td>3.4%</td><td>2.1%</td><td>1.3%</td><td>-2.4%</td><td>-1.9%</td><td>-0.5%</td><td>29.6%</td><td>26.6%</td><td>3.1%</td></tr><tr><td>Lindt</td><td>-15.9%</td><td>17.8%</td><td>-33.7%</td><td>-22.6%</td><td>-1.7%</td><td>-20.9%</td><td>8.6%</td><td>19.8%</td><td>-11.2%</td><td>45.8%</td><td>42.6%</td><td>3.2%</td></tr></table>

Source: NielsenIQ, Bernstein analysis

## FOOD AND HPC MARKET

EXHIBIT 2: Food mkt value/volume/price growth  
![](images/13ace52dc2ce1ee6094da1b3ff7262ceb5017c6e1c39d6d67bbf01dd8a78e761.jpg)  
Source: NielsenIQ, Bernstein analysis  
Notes: Growth rates are weighted by our company sales in the categories

EXHIBIT 3: Food Private Label (PL) market share change  
![](images/2cbc73480876db41f14eec1507f5ddad29fce9ad42b417fe1e7e766c550f013d.jpg)  
Source: NielsenIQ, Bernstein analysis  
Note: PL market share is weighted by our company sales in the categories

## HPC MARKET SEGMENTS

EXHIBIT 4: B&PC mkt value/volume/price growth  
![](images/8a1adb695dba47b47aa67cd7b344d3da9152ec1e9626f85b5e2e6ea44653aeff.jpg)  
Source: NielsenIQ, Bernstein analysis

Note: Growth rates are weighted by our company sales in the categories

EXHIBIT 5: B&PC Private Label market share change  
![](images/c6b985e9df8768aa0ad88ccb5dde8e3e57936c443e6fd5a0b457cb62f687379d.jpg)  
Source: NielsenIQ, Bernstein analysis  
Note: PL market share is weighted by our company sales in the categories

EXHIBIT 6: Household Mkt Value/Volume/Price Growth  
![](images/ba5ad1c849fcf99810a9c7834ad01e194271aff3a7e2070db8e31aa270da9bfa.jpg)  
Household consists of Home Care, Laundry Care, Dish Care, Air Fresheners, Fabric Softeners, Toilet Cleaners, Stain Removers, etc.
Source: NielsenIQ, Bernstein analysis  
Note: Growth rates are weighted by our company sales in the categories

EXHIBIT 7: Household Private Label Market Share Change  
![](images/8e87c3781cd6f8377272c4b8e8fbf1dcd94695896ca866b9d1fd92d2c3706894.jpg)  
Household consists of Home Care, Laundry Care, Dish Care, Air Fresheners, Fabric Softeners, Toilet Cleaners, Stain Removers, etc.  
Source: NielsenIQ, Bernstein analysis  
Note: PL market share is weighted by our company sales in the categories

EXHIBIT 8: CH Mkt Value/Volume/Price Growth  
![](images/e908ed923fe946ebd754e03746dc5101fc05eebf97b31c076ed03c199a9e9d70.jpg)  
Source: NielsenIQ, Bernstein analysis  
Note: Growth rates are weighted by our company sales in the categories

EXHIBIT 9: Consumer Health Private Label Mkt Share Ch.  
![](images/d8196e0499b255b49ac4a2e0d90d3f81e2ac0d530a924e2173f7850313da9689.jpg)  
Source: NielsenIQ, Bernstein analysis  
Note: PL market share is weighted by our company sales in the categories

## NESTLÉ

EXHIBIT 10: NESN market share change  
![](images/f6e3eaa4db193fbbf2e33d4527af740590082299795fc0e32c630cb075f6985f.jpg)  
Source: NielsenIQ, Bernstein analysis

EXHIBIT 11: Private Label market share change  
![](images/670060239e5935a1c5e3b270fcc19abdbc0d29526028887d2bba34975883b4b7.jpg)

Source: NielsenIQ, Bernstein analysis

EXHIBIT 12: NESN value growth  
![](images/b7763dbe148d88487ff43601aa27c28d3170eb6f9d6773def012b7a288f32e0a.jpg)  
Source: NielsenIQ, Bernstein analysis

EXHIBIT 13: NESN market share and PL share  
![](images/d64f7e2a696e296e5b7afd52b3cbc3243f2c3b921b0c600db2cadcf4671fab92.jpg)  
Source: NielsenIQ, Bernstein analysis

EXHIBIT 14: NESN value/volume/price growth  
![](images/f99ee56da2d8a742da46384e5445ed78ad9ccc96e448455a19d95ac3896caed2.jpg)  
Source: NielsenIQ, Bernstein analysis

EXHIBIT 15: NESN relative value/vo

[中间内容因长度限制已省略]

 you of any change in the reported

information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
