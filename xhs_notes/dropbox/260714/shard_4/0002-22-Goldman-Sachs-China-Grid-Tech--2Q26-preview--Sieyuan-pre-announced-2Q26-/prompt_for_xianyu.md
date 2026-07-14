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
# China Grid Tech: 2Q26 preview: Sieyuan pre-announced 2Q26 miss on delayed revenue and FX loss, reiterate Buy; lower EPS for Huaming

## Sieyuan (002028.SZ, Buy)

Post market close on July 10, Sieyuan pre-announced 1H26 results that missed our expectations. We cut our 2026-30E EPS forecasts by 8-11%, of which around 3-6% is attributable to delayed revenue recognition, 1-2% to lower operating leverage following the revenue delay, c.3% to FX losses in 2026E, and the remainder to higher minority interests after Toshiba increased its stake in the transformer JV. Despite these revisions, we reiterate our Buy rating, as we view the earnings miss as largely timing- and FX-related rather than demand-driven, with order intake and product shipments remaining intact. Looking ahead, we expect earnings to be back-end loaded in 2H26 as deferred overseas revenue is recognized, while the margin mix should improve on a higher contribution from North American transformers and UHV/EHV projects, offsetting the lower-margin EPC and ESS businesses. We remain constructive on Sieyuan's long-term opportunity in North America, where its agile supply chain and capacity expansion plans, which could support annual transformer production value of Rmb9-10bn, position it well to benefit from the transformer shortage, which we expect to ease gradually but persist through 2030E.

1H26 revenue came in at Rmb10,803mn, up 27% yoy, implying 2Q26 revenue of Rmb6,235mn, up 18% yoy and 8% below our forecast. However, we do not believe the topline miss indicates weakening fundamentals, as 2Q26 revenue growth of 18% yoy was well below the pace of underlying new order growth of 35% in 2025. According to the company, the shortfall was mainly caused by temporary delays in revenue recognition for certain overseas projects. For some overseas contracts, possibly including North American transformer projects, changes in contract and trade terms mean that control is transferred only after onsite installation or customer acceptance, rather than shortly after shipment. As a result, part of the revenue originally expected in 2Q26 has been deferred to 3Q26 and later periods. We therefore view the miss as a timing issue rather than a deterioration in demand. We now forecast 2026E revenue growth of 30% yoy, with growth accelerating to 35% yoy in 3Q26E and remaining strong at 30% yoy in 4Q26E as the delayed overseas revenue is recognized.

Near-term operations remain intact: We estimate 2Q26 new order growth remained broadly in line with 1Q26 at around $40\%$ yoy, while product shipments continued as planned. Based on U.S. customs data, Sieyuan's transformer shipments to the U.S. increased from 2-3 units per month previously to around 10 units in July,

Zhou Li  
+86(21)2401-8648 |  
zhou.li@goldmansachs.cn  
GS (China) Securities  
Company Limited

Jacqueline Du  
+852-2978-1783 |  
jacqueline.du@gs.com  
GS (Asia) L.L.C.

Hao Chen  
+86(21)2401-8812 |  
hao.z.chen@goldmansachs.cn  
GS (China) Securities  
Company Limited

with the corresponding North American revenue expected to be recognized in 3Q26E. According to ImportYeti, Sieyuan shipped power transformers to Edge Wave, Wayli, Hitachi Energy and Max Tech, while transformer arresters and circuit breakers were shipped to Sieyuan's U.S. subsidiary and B&K Industrial.

Gross margin recovered sequentially per the company, where we estimate a recovery of around $30.8\%$ in 2Q26E from $29.0\%$ in 1Q26, although still below the prior-year level. 1H26 GPM of around $30\%$ largely reflects a business mix in which approximately $80\%$ of revenue generated gross margins of around $35\%$ , offset by lower-margin EPC and ESS businesses, which accounted for around $20\%$ of revenue and operated at mid-teens margins. The contribution from the ESS business declined in 2Q26 versus 1Q26 as Sieyuan scaled down the ESS business. In addition, management has shifted its ESS strategy from prioritizing growth to emphasizing profitability, lowering the priority of securing new orders this year. Nevertheless, we continue to expect steady revenue recognition from orders signed last year. Meanwhile, a higher contribution from North American shipments and the initial recognition of UHV and EHV projects from 3Q26 onward should support further sequential gross margin improvement.

Exhibit 1: Sieyuan's shipments to the US accelerated to 10 units in July, which will more likely be recognized in 3Q26E  
![](images/63a88a1aabbcc4cb97d183ff2835eda7ffd107d3f146b86ba7101729f12fafb9.jpg)  
Source: ImportYeti, Data compiled by GS Global Investment Research

Exhibit 2: ... where we estimate transformers (likely c.300MVA) to be priced at c.US\$10mn/c.Rmb70mn each  
![](images/3f827316a695d28df24b66511477a95ede958e63370360c8b449cdf4f7c6db9b.jpg)  
Source: Expert estimates, State Grid

Exhibit 3: Sieyuan will start to recognize more UHV and EHV GIS revenue, which are high-margin businesses, starting from 3Q26E

Sieyuan tendering won for GIS in UHV and EHV (Rmb mn)

![](images/096ae077c647953ec3300370845dbd8ab51c7a9e2b2c8d041989b185293fb4ef.jpg)  
Source: State Grid, Data compiled by GS Global Investment Research

Exhibit 4: Sieyuan is trading at 28X 12-m forward P/E, slightly above its past 10-year average of 24X, but has significantly rerated from the peak of 44X.
Sieyuan 12-m forward P/E

![](images/e6595637a26616eb987a17d2daae2bf52f3662886b7e7224ec21511a65edd205.jpg)  
Source: Company data, GS Global Investment Research

The key drag on earnings was foreign-exchange losses. The company recorded more than Rmb100mn of FX losses in 1H26, compared with FX gains in the same period last year, creating a meaningful year-on-year swing in reported profit. By contrast, the impact from Toshiba raising its stake in the JV with Sieyuan to $30\%$ was relatively limited.

Earnings and TP changes: We revise down 2026-30E revenue by $3 - 6\%$ and net income by $8 - 11\%$ to reflect the elongated revenue recognition, FX loss, and minority interest change due to Toshiba's increased JV stake. Accordingly, our TP is revised down to Rmb203.7 (vs Rmb223.9 previously), still based on 25X 2028E P/E discounted back to 2026E with $9.5\%$ CoE. Maintain Buy.

## Huaming (002270.SZ, Neutral)

## 2Q26 preview: We forecast 2Q26 sales/GP/EBIT/NP at

Rmb625mn/341mn/216mn/191mn (+4%/+0%/-5%/-3% yoy). We do not expect a meaningful revenue growth acceleration in 2Q26 compared to the -1% yoy decline in on-load tap changer revenue in 1Q26, for three reasons: First, the company already holds a dominant market share in the domestic grid segment, limiting its ability to outpace overall industry growth. Second, off-grid demand remains weak, with no clear signs of recovery. Third, although China transformer export industry growth has remained resilient, reaching 27% yoy in April and 72% yoy in May according to China Customs, the certification process for on-load tap changers still needs to be completed with end customers (i.e., global grid operators). As a result, export growth for tap changers is likely to lag transformer exports. The certification process is lengthy and requires building customer trust over time, particularly given that these components are not in global supply shortage.

Although the stock has corrected $54\%$ from the peak, we still think it is relatively fair valued, with the stock price correction reflecting an expectation reset (from a potentially fast share gain pace to a steady pace of share gain given the component is not in shortage). The stock is trading at 21x 12-m forward P/E, against $17\%$ 2026-30E EPS CAGR, lacking catalysts for both revenue acceleration and valuation rerating. We suggest investors wait for a more attractive valuation to turn more positive on the stock.

Earnings and TP changes: We maintain our Neutral rating, while lowering our 2026-30E revenue and EPS forecasts by 2%-8% and 2%-10%, respectively, as we reset our market share gain pace expectations against the backdrop of a lack of OLTC shortage. Accordingly, our TP is revised down to Rmb23.9 (vs Rmb26.1 previously), still based on 22x 2028E P/E discounted back to 2026E with 9.5% CoE.

Investment thesis, valuation methodology and risks

## Sieyuan (002028.SZ, Buy)

Sieyuan is a Chinese grid equipment company, ranking among the top 1-3 in various product categories with the State Grid. With recognized exceptional product quality and operational excellence, we expect Sieyuan's export revenue to grow at a $43\%$ CAGR in 2025-2030E driven by the global grid upgrade cycle due to aged infrastructure, economy development, renewable energy and Sieyuan's market share gain in switchgear/power transformers from $6\% / 1\%$ in 2025 to $8\% / 6\%$ in 2030E. In particular, Sieyuan has made breakthroughs with US data center operators due to the supply shortage in power transformers, hence we expect its US revenue to take up $26\% - 30\%$ of overseas revenue over 2026E-28E, and higher profit contribution helping with firmwide margin uplift. We think there is visibility for global power transformer supply shortage at least into 2030E and global grid upgrade into at least 2040E-2050E. We like its unique positioning because we believe only a few Chinese companies can combine high quality with a long-term commitment to navigating rigorous certification processes, making sustained upfront investments, and establishing a proven track record overseas - areas where Sieyuan excels in our view.

Price target risks & methodology: Our TP is Rmb203.7, based on 25x 2028E P/E discounted back to 2026E with $9.5\%$ CoE. Key downside risks: (1) Overseas execution risk; (2) Margin may come below our expectations; (3) Slowdown in data center construction pace.

<table><tr><td>002028.SZ</td><td>12m Price Target: Rmb203.7</td><td colspan="2">Price: Rmb151.73</td><td colspan="2">Upside: 34.3%</td></tr><tr><td>Buy</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: Rmb117.4bn / $17.3bn</td><td>Revenue (Rmb mn) New</td><td>21,539.0</td><td>28,005.1</td><td>35,605.8</td><td>43,107.7</td></tr><tr><td>Enterprise value: Rmb112.3bn / $16.6bn</td><td>Revenue (Rmb mn) Old</td><td>21,539.0</td><td>28,760.3</td><td>37,402.4</td><td>45,659.5</td></tr><tr><td>3m ADTV :Rmb2.5bn/ $368.4mn</td><td>EBITDA (Rmb mn)</td><td>3,873.1</td><td>5,000.5</td><td>6,637.6</td><td>8,386.4</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>4.03</td><td>5.10</td><td>7.10</td><td>8.92</td></tr><tr><td>China Industrial Tech &amp; Machinery</td><td>EPS (Rmb) Old</td><td>4.03</td><td>5.73</td><td>7.75</td><td>9.80</td></tr><tr><td></td><td>P/E (X)</td><td>23.1</td><td>29.7</td><td>21.4</td><td>17.0</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>4.7</td><td>6.3</td><td>5.1</td><td>4.2</td></tr><tr><td>Leases incl. in net debt &amp; EV?: Yes</td><td>Dividend yield (%)</td><td>0.8</td><td>0.7</td><td>1.0</td><td>1.4</td></tr><tr><td></td><td>CROCI (%)</td><td>33.2</td><td>30.7</td><td>34.7</td><td>35.6</td></tr><tr><td></td><td></td><td>12/25</td><td>3/26E</td><td>6/26E</td><td>9/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>1.23</td><td>0.70</td><td>1.20</td><td>1.41</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 10 Jul 2026 close.

Exhibit 5: Sieyuan earnings change summary

<table><tr><td>Sieyuan</td><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue (new)</td><td>Rmb mn</td><td>28,005</td><td>35,606</td><td>43,108</td><td>51,493</td><td>59,971</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>28,760</td><td>37,402</td><td>45,660</td><td>54,482</td><td>63,404</td></tr><tr><td>vs. Previous</td><td>%</td><td>-2.6%</td><td>-4.8%</td><td>-5.6%</td><td>-5.5%</td><td>-5.4%</td></tr><tr><td>EBIT (new)</td><td>Rmb mn</td><td>4,404</td><td>5,858</td><td>7,387</td><td>9,111</td><td>10,956</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>4,536</td><td>6,172</td><td>7,842</td><td>9,713</td><td>11,887</td></tr><tr><td>vs. Previous</td><td>%</td><td>-2.9%</td><td>-5.1%</td><td>-5.8%</td><td>-6.2%</td><td>-7.8%</td></tr><tr><td>Net Income (new)</td><td>Rmb mn</td><td>3,989</td><td>5,555</td><td>6,979</td><td>8,594</td><td>10,338</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>4,481</td><td>6,059</td><td>7,668</td><td>9,467</td><td>11,529</td></tr><tr><td>vs. Previous</td><td>%</td><td>-11.0%</td><td>-8.3%</td><td>-9.0%</td><td>-9.2%</td><td>-10.3%</td></tr></table>

Source: Company data, GS Global Investment Research

## Huaming (002270.SZ, Neutral)

Investment thesis: Huaming Power Equipment is China's dominant supplier of on-load tap changers (OLTC), with $90\%$ domestic market share by volume (as of 2025E), and is increasingly expanding into overseas markets where margins are structurally higher. With roughly on-par product quality with Germany's Maschinenfabrik Reinhausen (MR), much cheaper price and faster product supply, supported by new overseas factories in Turkey and Indonesia, we believe Huaming can ramp up from $13\%$ global market share in 2025E to $18\%$ by 2030E, with overseas revenue reaching $53\%$ of firmwide revenue. We expect 2025E-2030E revenue/net profit to deliver $13\% / 15\%$ CAGR, with dividend yield at $2\%$ in 2026E. However, given that tap changers are such a critical component, and take a long time for certification, in our view, US exposure won't meaningfully grow for Huaming in the near term. We believe the share price has temporarily run ahead of earnings hence rate it Neutral.  
Price target risks & methodology: Our TP isRmb23.9, based on 22x 2028E P/E discounted back to 2026E with $9.5\%$ CoE. Key upside/downside risks: (1) Better/worse-than-expected overseas share gain; (2) Better/worse-than-expected margin profile; (3) Better/worse-than-expected domestic revenue growth.

<table><tr><td>002270.SZ</td><td>12m Price Target: Rmb23.9</td><td colspan="2">Price: Rmb18.19</td><td colspan="2">Upside: 31.4%</td></tr><tr><td>Neutral</td><td>GS Forecast</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>12/25</td><td>12/26E</td><td>12/27E</td><td>12/28E</td></tr><tr><td>Market cap: Rmb16.2bn / $2.4bn</td><td>Revenue (Rmb mn) New</td><td>2,426.8</td><td>2,615.0</td><td>3,001.4</td><td>3,419.1</td></tr><tr><td>Enterprise value: Rmb15.7bn / $2.3bn</td><td>Revenue (Rmb mn) Old</td><td>2,426.8</td><td>2,664.6</td><td>3,114.0</td><td>3,608.5</td></tr><tr><td>3m ADTV :Rmb492.2mn/ $72.4mn</td><td>EBITDA (Rmb mn)</td><td>856.6</td><td>1,017.3</td><td>1,172.3</td><td>1,349.3</td></tr><tr><td>China</td><td>EPS (Rmb) New</td><td>0.79</td><td>0.87</td><td>1.02</td><td>1.19</td></tr><tr><td>China Industrial Tech &amp; Machinery</td><td>EPS (Rmb) Old</td><td>0.79</td><td>0.89</td><td>1.06</td><td>1.30</td></tr><tr><td></td><td>P/E (X)</td><td>23.7</td><td>20.8</td><td>17.9</td><td>15.3</td></tr><tr><td>M&amp;A Rank: 3</td><td>P/B (X)</td><td>5.4</td><td>4.8</td><td>4.5</td><td>4.1</td></tr><tr><td>Leases incl. in net debt &amp; EV?: Yes</td><td>Dividend yield (%)</td><td>3.2</td><td>3.4</td><td>3.9</td><td>4.6</td></tr><tr><td></td><td>CROCI (%)</td><td>27.4</td><td>22.7</td><td>24.2</td><td>26.4</td></tr><tr><td></td><td></td><td>3/26</td><td>6/26E</td><td>9/26E</td><td>12/26E</td></tr><tr><td></td><td>EPS (Rmb)</td><td>0.72</td><td>0.84</td><td>0.96</td><td>0.93</td></tr></table>

Source: Company data, GS estimates, FactSet. Price as of 10 Jul 2026 close.

Exhibit 6: Huaming earnings change summary

<table><tr><td>Huaming</td><td></td><td>2026E</td><td>2027E</td><td>2028E</td><td>2029E</td><td>2030E</td></tr><tr><td>Revenue (new)</td><td>Rmb mn</td><td>2,615</td><td>3,001</td><td>3,419</td><td>3,881</td><td>4,426</td></tr><tr><td>Previous</td><td>Rmb mn</td><td>2,665<

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
