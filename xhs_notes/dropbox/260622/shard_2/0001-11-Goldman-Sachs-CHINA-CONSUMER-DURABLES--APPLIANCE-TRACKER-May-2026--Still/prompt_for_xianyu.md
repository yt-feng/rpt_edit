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
CHINA CONSUMER DURABLES: APPLIANCE TRACKER

# May 2026: Still weak domestic demand yet base will ease into June, 618 in focus; exports sequentially improved

Domestic appliances data continued to demonstrate weakness on a high base for both retail and ex-factory shipment in May: 1) NBS home appliances and electronics retail sales fell by 16% yoy, a similar pace to Apr despite a more challenging base; 2) AC domestic ex-factory shipment came in below expectations at -15% yoy (vs -9% in the previous production plan as compiled by IOL), presumably impacted by front-loaded demand in the previous year and price hikes. Going forward, we view it as likely that domestic demand growth will remain under pressure in early June due to a high base. However, base pressure may sequentially ease into late June/July as the trade-in boost started to fade from June last year. Specifically for 618, initial sales data does not look encouraging, against low market expectations. Moreover, we noted lower prices vs Singles' Day for select brands, which may indicate that brands resorted to promotion to boost demand despite rising input costs.

Appliances exports growth sequentially improved and beat IOL and market expectations in May. Overall appliances exports growth accelerated to HSD% growth in May with a lower base per customs data. The AC exports decline also narrowed and came in above previous production plan (-4% yoy in May). Consumer sentiment in the US/Europe and US housing sales data also demonstrated sequential improvements recently. Going forward, as details become available following the signing of the US-Iran Memorandum of Understanding, visibility around demand could improve, providing scope for leading Chinese players to further gain share in overseas markets, especially those with product portfolios with a strong value proposition.

On cyclical factors, shipping rates further increased in the past month. Key commodities costs stayed largely stable in the past month. Regarding stock ideas, we continue to favor Buy-rated Midea (A/H) as we see limited downside risk protected by shareholder returns and upside potential from overseas markets and emerging business. We continue to hold a constructive view on Ninebot for its growth potential from a comprehensive product line-up, including share gains in the domestic E2W market, structural growth of robotic lawn mowers and overseas E2W potential, against a near historical low valuation. We also like Hisense Home Appliances on stabilizing central AC business, sequentially recovering revenue growth/profitability off easing bases, and mid to long-term margin expansion

Nicolas Yi
+86(21)2401-8922 |
nicolas.yi@goldmansachs.cn
GS (China) Securities
Company Limited

Cecilia Tang
+86(21)2401-8738 |
cecilia.tang@goldmansachs.cn
GS (China) Securities
Company Limited

potential with downside protected by dividend yield.  
Exhibit 1: Domestic data continued to show weakness, while exports data sequentially improved in May
Appliances data dashboard

<table><tr><td rowspan="2"></td><td colspan="14">yoy growth (%)</td><td colspan="3">MoM trend</td><td colspan="3">vs. 2019 CAGR</td><td colspan="3">MoM trend</td></tr><tr><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="24">Retail sales</td></tr><tr><td>NBS (above designated size)</td><td>39%</td><td>53%</td><td>32%</td><td>29%</td><td>14%</td><td>3%</td><td>-15%</td><td>-19%</td><td>-19%</td><td>3%</td><td></td><td>-5%</td><td>-15%</td><td>-16%</td><td>▼</td><td>▼</td><td>—</td><td>9%</td><td>5%</td><td>4%</td><td>▲</td><td>▼</td><td>—</td></tr><tr><td colspan="24">Ex-factory shipment</td></tr><tr><td colspan="24">Total shipment</td></tr><tr><td>Split AC</td><td>2%</td><td>2%</td><td>4%</td><td>2%</td><td>-1%</td><td>-10%</td><td>-20%</td><td>-32%</td><td>-19%</td><td>12%</td><td>-20%</td><td>-2%</td><td>-9%</td><td>-11%</td><td>▲</td><td>▼</td><td>▼</td><td>5%</td><td>2%</td><td>2%</td><td>▼</td><td>▼</td><td>▲</td></tr><tr><td>Washing machine</td><td>12%</td><td>10%</td><td>4%</td><td>9%</td><td>7%</td><td>8%</td><td>-2%</td><td>8%</td><td>7%</td><td>4%</td><td>9%</td><td>1%</td><td>4%</td><td></td><td>▼</td><td>▲</td><td></td><td>3%</td><td>4%</td><td></td><td>▼</td><td>▲</td><td></td></tr><tr><td>Refrigerator</td><td>0%</td><td>2%</td><td>1%</td><td>5%</td><td>2%</td><td>0%</td><td>-6%</td><td>-3%</td><td>-3%</td><td>9%</td><td>2%</td><td>-4%</td><td>6%</td><td></td><td>▼</td><td>▲</td><td></td><td>2%</td><td>4%</td><td></td><td>▼</td><td>▲</td><td></td></tr><tr><td>VRF</td><td>-20%</td><td>-20%</td><td>-18%</td><td>-1%</td><td>1%</td><td>2%</td><td>-5%</td><td>-1%</td><td>-2%</td><td>15%</td><td>-16%</td><td>-8%</td><td>-5%</td><td></td><td>▲</td><td>▲</td><td></td><td>5%</td><td>1%</td><td></td><td>▼</td><td>▼</td><td></td></tr><tr><td colspan="24">Domestic shipment</td></tr><tr><td>Split AC</td><td>4%</td><td>13%</td><td>16%</td><td>14%</td><td>1%</td><td>-3%</td><td>-21%</td><td>-40%</td><td>-27%</td><td>15%</td><td>-21%</td><td>6%</td><td>-7%</td><td>-15%</td><td>▲</td><td>▼</td><td>▼</td><td>5%</td><td>2%</td><td>2%</td><td>▲</td><td>▼</td><td>—</td></tr><tr><td>Washing machine</td><td>8%</td><td>15%</td><td>1%</td><td>1%</td><td>1%</td><td>-7%</td><td>-9%</td><td>-5%</td><td>-10%</td><td>-3%</td><td>-8%</td><td>-6%</td><td>-6%</td><td></td><td>▲</td><td>▼</td><td></td><td>-2%</td><td>1%</td><td></td><td>▼</td><td>▲</td><td></td></tr><tr><td>Refrigerator</td><td>0%</td><td>14%</td><td>12%</td><td>8%</td><td>6%</td><td>-7%</td><td>-11%</td><td>-16%</td><td>-13%</td><td>2%</td><td>-24%</td><td>-5%</td><td>-4%</td><td></td><td>▲</td><td>▲</td><td></td><td>-2%</td><td>0%</td><td></td><td>▼</td><td>▲</td><td></td></tr><tr><td>VRF</td><td>-25%</td><td>-26%</td><td>-20%</td><td>-3%</td><td>3%</td><td>1%</td><td>-5%</td><td>-1%</td><td>-5%</td><td>14%</td><td>-21%</td><td>-10%</td><td>-6%</td><td></td><td>▲</td><td>▲</td><td></td><td>4%</td><td>-1%</td><td></td><td>▼</td><td>▼</td><td></td></tr><tr><td colspan="24">Export shipment</td></tr><tr><td>Split AC</td><td>0%</td><td>-13%</td><td>-13%</td><td>-16%</td><td>-4%</td><td>-18%</td><td>-19%</td><td>-26%</td><td>-13%</td><td>10%</td><td>-19%</td><td>-10%</td><td>-12%</td><td>-4%</td><td>▲</td><td>▼</td><td>▲</td><td>4%</td><td>2%</td><td>3%</td><td>▼</td><td>▼</td><td>▲</td></tr><tr><td>Washing machine</td><td>17%</td><td>6%</td><td>5%</td><td>17%</td><td>12%</td><td>24%</td><td>6%</td><td>23%</td><td>25%</td><td>11%</td><td>26%</td><td>7%</td><td>14%</td><td></td><td>▼</td><td>▲</td><td></td><td>9%</td><td>10%</td><td></td><td>▼</td><td>▲</td><td></td></tr><tr><td>Refrigerator</td><td>-1%</td><td>-6%</td><td>-5%</td><td>3%</td><td>-1%</td><td>8%</td><td>-1%</td><td>10%</td><td>8%</td><td>14%</td><td>24%</td><td>-3%</td><td>13%</td><td></td><td>▼</td><td>▲</td><td></td><td>10%</td><td>8%</td><td></td><td>▼</td><td>▼</td><td></td></tr><tr><td>VRF</td><td>12%</td><td>30%</td><td>-3%</td><td>11%</td><td>-13%</td><td>14%</td><td>-9%</td><td>2%</td><td>19%</td><td>22%</td><td>9%</td><td>5%</td><td>1%</td><td></td><td>▼</td><td>▼</td><td></td><td>18%</td><td>16%</td><td></td><td>▼</td><td>▼</td><td></td></tr></table>

Source: AVC, IOL, NBS, Data compiled by GS Global Investment Research

## Ex-factory shipments showed divergence between domestic and exports

According to China Industry Online (IOL), AC total ex-factory shipments growth weakened to -11% yoy in May (vs -9% yoy in Apr), with weaker growth from domestic (-15% yoy in May vs -7% yoy in Apr) but better growth from exports (-4% yoy in May vs -12% yoy in Apr). Compared to previous production plans, domestic came lower than expected but exports came above (vs -9% and -6% yoy of previous production plan respectively). Similar to previous months, we note that overall exports by Chinese players should be greater than that indicated by IOL export data as leading companies such as Midea also export from their overseas factories.

Domestic shipment came in weaker than expected by IOL in May on a high base, consistent with continued weakness from retail sales, presumably impacted by front-loaded demand in the previous year and price hikes since Apr. Going forward, IOL revised down the growth forecast to a low-teens % decline (vs previously SD% yoy decline) for major white goods in 2Q26 on the back of weak demand.

Exports sequentially improved and came in better than expected in May. Apart from a lower base, exports showed resilience despite the Middle East conflict, likely supported by Chinese players' continued share gains. Property sales data (Exhibit 12) in DM and consumer sentiment (Exhibit 11) both showed sequential improvements in the past month. Going forward, the current production plan still indicates SD% yoy exports decline for major white goods in 2Q26 with relatively better growth from refrigerators and washing machines vs AC.

By brand, Haier and Hisense outpaced the industry in terms of total shipments growth, while Gree and Midea lagged. Haier's total AC ex-factory shipments were up by 6% yoy, underpinned by +5%/+10% domestic/exports growth. Hisense's total AC ex-factory shipments decreased by 8% yoy in May, underpinned by +3%/-17% domestic/exports growth. Midea's total AC ex-factory shipments decreased by 23% yoy in May, with a wider decline of domestic and but better exports (-35% and +4% yoy). Gree's total AC ex-factory shipments decreased by 13% yoy in May, with above-industry domestic but below-industry exports (-6% and -33% yoy).

Total ex-factory shipment volume growth for washing machines/refrigerators demonstrated improving trends in Apr.

\- Washing machine total shipments growth improved to $+4\%$ yoy in Apr (vs $+1\%$ yoy in Mar). Domestic decline stayed stable at $-6\%$ yoy in Apr, but exports growth improved to $+14\%$ yoy (vs $+7\%$ yoy in Mar). By brand, both Midea and Haier came in below industry. Midea's total shipments were up by $+3\%$ yoy in Apr, with domestic/export shipments growing by $-1\%/ +8\%$ yoy. Haier's total shipments were flattish yoy in Apr, with domestic/exports growth of $-1\%/ +2\%$ yoy.

Refrigerator total shipments growth improved to +6% yoy in Apr (vs -4% yoy in Mar). Domestic sales narrowed slightly to -4% yoy in Apr (vs -5% yoy in Mar), and exports growth turned positive to +6% yoy (vs -3% yoy in Mar). By brand, Midea and Hisense came above industry but Haier came below in Apr. Midea's total shipments grew by +25% yoy, with domestic/export shipments growing by +25%/+26% yoy. Hisense's total shipments grew by +15% yoy, with domestic/overseas shipments growth

+2%/+21% yoy. Haier's total shipments were flattish yoy, of which domestic/exports growth -24%/+36% yoy.

Total shipment value for variable refrigerant flow systems (VRF) decreased by 5% in Apr, narrowed from -8% yoy in Mar. Domestic shipment decline narrowed but export shipment growth moderated (domestic/exports -6%/+1% yoy in Apr vs -10%/+5% yoy in Mar). By brand, in domestic market growth, Midea, Gree and Hisense-Hitachi came above industry at -2%/-2%/-3% yoy, while Daikin lagged at -10% yoy. For exports, Midea and Daikin showed faster growth vs the industry average.

May ex-factory shipment data for refrigerators/washing machines/refrigerant flow systems will be released at the end of June.

Exhibit 2: AC domestic ex-factory shipment growth weakened sequentially in May
Domestic ex-factory shipment vol. (10,000 units)  
![](images/bf6f4478a6552fd8d41bdcf47f5eee64617d45e1d16f29e03a1b7ffded06e8ec.jpg)  
Source: IOL, Data compiled by GS Global Investment Research

Exhibit 3: AC domestic shipment moderated in May (-15% yoy in May vs -7% yoy in Apr)...

AC domestic ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)

![](images/c839eab0c73725a538a0a1fe81951fd8de16eb6c68aa68fb81d04f2f69597212.jpg)  
Source: IOL  
Washing machine domestic ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)

![](images/d901e47ba070492847893b29a036d799e5e5cd8b82d00941f0be55b9e75067d3.jpg)  
Source: IOL  
Exhibit 7: Domestic refrigerator ex-factory shipments improved to -4% yoy growth in Apr
Refrigerator domestic ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)

Exhibit 4: ...with Midea/Gree/Haier/Hisense's domestic shipments growing by -35%/-6%/+5%/-5% yoy in May AC ex-factory domestic shipment yoy growth by company

![](images/8ed46a6597ca80b3541e405cb8fc7b4626d83f660eb30fc404b099cb9d897a79.jpg)

Exhibit 5: Washing machine domestic shipment growth stayed at -6% yoy in Apr  
![](images/89965c508b435f2c9fc5d2596f8aad38aedcaeb77952bda6ff1a56685a63df0e.jpg)  
Source: IOL  
Exhibit 6: Haier/Midea grew above industry at -1%/-1% yoy in Apr  
Washing machine (WM) domestic ex-factory shipment yoy growth by company

![](images/cbe445bb3359271a3db10d808604e36ae35682531347fd2bda39703c79e1d77a.jpg)  
Source: IOL  
Source: IOL  
Exhibit 8: Midea/Haier came above/in-line with the industry at +25%/-4% yoy growth in Apr
Refrigerator domestic ex-factory shipment yoy growth by company

![](images/1f477ee0d6765c8525a55a1c1211a41ba2bbf5a706047df0d08f5db51259b72f.jpg)  
Source: IOL

Washing machine export ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)

Exhibit 9: Domestic VRF ex-factory sales improved to -6% yoy in Apr
VRF domestic sales (LHS, RMB mn); yoy growth (RHS, %)  
![](images/d57d08ed4bf8f9df8ac5efa5f8c89a47ea57d8078ba79d7e6354d46ba820073e.jpg)  
Source: IOL

Exhibit 10: Gree, Midea and Hisense-Hitachi came above industry, while Daikin lagged
VRF domestic sales yoy growth by company  
![](images/1346ae90d322f306a2370fd84029b1caf3bb089f45b64a1895499acb9a935b8b.jpg)  
Source: IOL

Exhibit 11: China white goods exports improved in Apr, with better EU/US consumer sentiment in May/Jun  
![](images/9847781b4f852475192d53063dbe87a122a5c1491181e654eff1dfd440845a0a.jpg)  
Source: IOL, University of Michigan

Exhibit 12: US pending home sales, a leading indicator of existing home sales, showed improvements in May  
![](images/e3ad410bc4eefb622336a899cd4499f28a76a1506c791c041629c5b148d1dbc1.jpg)  
Source: Bureau of Economic Analysis, Wind, National Association of Realtors (NAR)  
Exhibit 13: AC ex-factory export shipments decreased by 4% yoy in May, up from -12% yoy in Apr
AC export ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)

![](images/10ef0e465fd2d54c8db9f24555988791845591470d421c7caad6e455c1879a3b.jpg)  
Source: IOL  
Exhibit 14: Washing machine export growth was +14% yoy in Apr, vs. +7% yoy in Mar

![](images/e68f4a3a9f6fd2436bcdcc1c50b9919e4e7826b1c08057eeadb657086cf033e9.jpg)  
Source: IOL

Exhibit 15: Refrigerator export shipment growth improved to +13% yoy in Apr, vs. -3% yoy in Mar  
Refrigerator export ex-factory shipment vol. (LHS, 10,000 units); yoy growth (RHS, %)  
![](images/48d5842d1c069afd5d882d4083717799aea6ff062fef2ae9b7089c8472a3734f.jpg)  
Source: IOL

Exhibit 17: Shipping rates increased in the past month...
Weekly CCFI  
![](images/a972bc152d411a1f9e1288aca618898f051914958ea1a35606f60dd54789a50e.jpg)  
Source: Wind

## Exhibit 16: VRF export ex-factory sales grew +1% yoy in Apr

VRF export sales (LHS, RMB mn); yoy growth (RHS, %)  
![](images/026fd0a69121a752988acf894f91cf62366af65dbaa5f28438d30bead8436be6.jpg)  
Source: IOL

Exhibit 18: ... and yoy growth increased as of mid-June
Weekly CCFI yoy growth %  
![](images/3edf89d4bd5e5b6bd9550dfe70168536a1fe32ea24e9e6c27bb4ac553dc11067.jpg)  
Source: Wind

## Retail sales remained weak on a higher base

Retail sales growth showed a similar 

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
