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

Tracked omni-channel sales including online sales combined with Nielsen offline sale

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
