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
# BofA Equity Client Flow Trends

# Record Tech outflows

## Historic single stock selling, driven by institutional clients

- Record stock outflows: Last week (S&P 500 -2.6%, biggest weekly decline since Apr. '25), clients were record net sellers of US equities, driven by record single stock outflows (\$14.2bn). They bought equity ETFs (\$0.3bn) for the 11 $^{th}$ straight week.  
- Selling was driven by institutional clients (biggest outflows since mid-March), after they bought equities the previous 5 weeks. Hedge funds and private clients sold equities as well for the second and third consecutive weeks, respectively. Net sales by private clients were the largest since Nov. 2024.  
- Outflows were entirely in large caps, as clients bought small & mid cap equities.  
- Corporate client buybacks slowed for a 2 $^{nd}$ week, though the rolling 4-wk. avg. rose to its highest level since late March. YTD, cumulative corp. client buybacks are tracking slightly below full-year 2025 levels if annualized, and below 2024's records, but above 2016-2023 levels. As a % of mkt. cap, trailing 52-wk. buybacks are the lowest since late '23. Buybacks by our clients have slowed most notably in Tech vs. picked up in Discretionary/Financials/Energy YTD; Financials has been the biggest buyback contributor in recent weeks (followed by Discretionary).

## Biggest Tech outflows ever

- Clients sold stocks in 8 of 11 sectors, led by Tech, which saw its largest outflows in our data history since 2008 (or largest since early 2014 as a % of mkt. cap). Tech outflows were led by institutional clients, but hedge funds and private clients sold Tech stocks, too. Communication Services stocks also saw outflows (for the $5^{\text{th}}$ consecutive week), but outflows were much more muted than Tech outflows.  
- Industrials, Real Estate and Utilities were the only sectors to see inflows. Real Estate has seen inflows for 6 straight weeks.

## ETFs: Value>Growth; big Health Care ETF inflows

- Clients bought Value/Blend ETFs vs. sold Growth ETFs and bought ETFs across most size segments (large/mid/broad market) except small caps.  
- Clients bought ETFs in 6 of 11 sectors, led by Health Care ETFs (largest ETF inflows since Oct. '21). Tech ETFs saw the biggest outflows, followed by Financials.

Exhibit 3: Tech net flows as a % of S&P 500 Tech Market cap were the most negative since Feb. '14  
Weekly Tech net flows as a % of S&P 500 Tech market cap, since 2008  
![](images/e2bba7197725dfa48ad2beb899233ea945d37104d4097431606ae93660f81289.jpg)

<details>
<summary>line chart</summary>

| Year | Value     |
|------|-----------|
| 08   | -0.040%   |
| 09   | 0.040%    |
| 10   | -0.040%   |
| 11   | 0.040%    |
| 12   | -0.040%   |
| 13   | 0.040%    |
| 14   | -0.080%   |
| 15   | 0.040%    |
| 16   | -0.040%   |
| 17   | 0.040%    |
| 18   | -0.040%   |
| 19   | 0.040%    |
| 20   | -0.040%   |
| 21   | 0.040%    |
| 22   | -0.040%   |
| 23   | 0.040%    |
| 24   | -0.040%   |
| 25   | 0.040%    |
| 26   | -0.040%   |
</details>

Source: BofA  
BofA GLOBAL RESEARCH

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 19 to 21.

12982757

## 09 June 2026

Equity and Quant Strategy
United States

BofA

## Data Analytics

![](images/165b383a6177c8838a4d2bae69ba0917fd6afe4ad1c5bd64cb5036d8a51f54b0.jpg)

Jill Carey Hall, CFA

Equity & Quant Strategist

BofAS

+1 646 855 3327

jill.carey@bofa.com

Trey Brown

Equity & Quant Strategist

BofAS

+1 646 855 2689

harold.brown2@bofa.com

## Exhibit 1: Institutional clients are the biggest net sellers post-crisis

Cumulative flows (\$ bn) by client type, February 2008-present

![](images/9853990ae0e83625473c4f22543ab10ec915e9179ed9ae208430501c025dcd53.jpg)

<details>
<summary>line chart</summary>

| Year | Hedge Funds | Institutional | Private Client |
|------|-------------|---------------|----------------|
| 07   | 0           | 0             | 0              |
| 10   | -50         | -50           | -100           |
| 13   | -100        | -100          | -150           |
| 16   | -150        | -150          | -200           |
| 19   | -200        | -200          | -250           |
| 22   | -250        | -250          | -250           |
| 25   | -300        | -350          | -300           |
</details>

Source: BofA  
BofA GLOBAL RESEARCH

## Exhibit 2: Hedge funds and institutional clients are the biggest net sellers vs private clients are net buyers over the past 12 mos

L12m cumulative flows (\$ bn) by client type, June 2025-present

![](images/9b6c48698fba555499b62ac55d061961b024aa453e3d786d20290164788ccb84.jpg)

<details>
<summary>line chart</summary>

| Date   | Hedge Funds | Institutional | Private Client |
|--------|-------------|---------------|----------------|
| May-25 | -           | -             | -              |
| Jun-25 | -           | -             | -              |
| Jul-25 | -           | -             | -              |
| Aug-25 | -           | -             | -              |
| Sep-25 | -           | -             | -              |
| Oct-25 | -           | -             | -              |
| Nov-25 | -           | -             | -              |
| Dec-25 | -           | -             | -              |
| Jan-26 | -           | -             | -              |
| Feb-26 | -           | -             | -              |
| Mar-26 | -           | -             | -              |
| Apr-26 | -           | -             | -              |
| May-26 | -           | -             | -              |
</details>

Source: BofA  
BofA GLOBAL RESEARCH

## BofA Equity Client Flow Trends

Exhibit 4: Rolling 4wk avg. US equity flows (based on single stock+ETF flows) is at -\$2.9bn  
BofA client total net buys of US equities (stocks & ETFs): four-week avg (\$ mn) vs. S&P 500, 2008-present  
![](images/383e661f0105312161562549b58581a1ea2f8193a92bbd89f67b43aa24d269c0.jpg)

<details>
<summary>line chart</summary>

| Year | Net buys (LHS) | S&P 500 Index (RHS) |
|------|-----------------|---------------------|
| 08   | ~0              | ~1000               |
| 09   | ~-1000          | ~500                |
| 10   | ~-500           | ~1000               |
| 11   | ~-100           | ~1500               |
| 12   | ~-50            | ~2000               |
| 13   | ~-10            | ~2500               |
| 14   | ~-5             | ~3000               |
| 15   | ~-10            | ~3500               |
| 16   | ~-5             | ~4000               |
| 17   | ~-10            | ~4500               |
| 18   | ~-5             | ~5000               |
| 19   | ~-10            | ~5500               |
| 20   | ~-5             | ~6000               |
| 21   | ~-10            | ~6500               |
| 22   | ~-5             | ~7000               |
| 23   | ~-10            | ~7500               |
| 24   | ~-5             | ~8000               |
| 25   | ~-10            | ~8500               |
| 26   | ~-5             | ~9000               |
</details>

Source: BofA  
BofA GLOBAL RESEARCH

## Cumulative flows by year

## Exhibit 5: Flows by client group: BofA equity client flows by year (single stocks vs. ETFs)

Cumulative net buying (selling) of single stocks and ETFs by client group (\$mn) by year (2026 is YTD)

<table><tr><td>Category</td><td>2026</td><td>2025</td><td>2024</td><td>2023</td><td>2022</td><td>2021</td><td>2020</td><td>2019</td><td>2018</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td><td>2009</td></tr><tr><td colspan="19">Flows by client group: Single stocks</td></tr><tr><td>Hedge funds</td><td>(8,625)</td><td>(29,878)</td><td>(19,415)</td><td>1,515</td><td>(26,293)</td><td>(39,284)</td><td>(12,057)</td><td>(4,722)</td><td>(2,989)</td><td>(3,852)</td><td>(4,559)</td><td>(6,798)</td><td>(8,519)</td><td>(717)</td><td>(2,723)</td><td>(3,590)</td><td>(3,635)</td><td>7,538</td></tr><tr><td>Institutional clients</td><td>(27,112)</td><td>(48,044)</td><td>(43,602)</td><td>(7,169)</td><td>5,460</td><td>(27,730)</td><td>(7,482)</td><td>(9,852)</td><td>(11,255)</td><td>(60,771)</td><td>(49,729)</td><td>(19,538)</td><td>(26,155)</td><td>(29,437)</td><td>(4,693)</td><td>1,725</td><td>(14,927)</td><td>7,987</td></tr><tr><td>Private clients</td><td>(18,734)</td><td>(18,438)</td><td>(47,792)</td><td>(40,162)</td><td>(19,521)</td><td>(51,253)</td><td>(32,464)</td><td>(36,846)</td><td>(38,596)</td><td>(39,604)</td><td>(35,049)</td><td>(29,739)</td><td>(35,619)</td><td>(34,599)</td><td>(50,657)</td><td>(31,983)</td><td>(34,605)</td><td>(31,919)</td></tr><tr><td>Total single stocks</td><td>(54,471)</td><td>(96,360)</td><td>(110,810)</td><td>(45,816)</td><td>(40,354)</td><td>(118,266)</td><td>(52,004)</td><td>(51,421)</td><td>(52,840)</td><td>(104,227)</td><td>(89,337)</td><td>(56,075)</td><td>(70,293)</td><td>(64,753)</td><td>(58,074)</td><td>(33,848)</td><td>(53,167)</td><td>(16,393)</td></tr><tr><td colspan="19">Flows by client group: ETFs</td></tr><tr><td>Hedge funds</td><td>1,865</td><td>(2,939)</td><td>2,316</td><td>9,438</td><td>(395)</td><td>20,972</td><td>4,114</td><td>5,085</td><td>(4,307)</td><td>1,688</td><td>1,942</td><td>3,664</td><td>3,474</td><td>(1,980)</td><td>638</td><td>(2,105)</td><td>(648)</td><td>(1,696)</td></tr><tr><td>Institutional clients</td><td>9,263</td><td>15,624</td><td>7,901</td><td>(7,833)</td><td>1,195</td><td>7,057</td><td>9,736</td><td>10,610</td><td>(5,991)</td><td>8,054</td><td>1,192</td><td>(6,429)</td><td>7,535</td><td>(3,757)</td><td>7,362</td><td>(232)</td><td>1,141</td><td>(1,672)</td></tr><tr><td>Private clients</td><td>21,096</td><td>43,002</td><td>44,455</td><td>21,778</td><td>35,606</td><td>49,424</td><td>22,269</td><td>8,740</td><td>37,134</td><td>47,391</td><td>20,676</td><td>31,687</td><td>22,481</td><td>15,937</td><td>10,684</td><td>8,934</td><td>8,154</td><td>8,572</td></tr><tr><td>Total ETFs</td><td>32,225</td><td>55,687</td><td>54,672</td><td>23,383</td><td>36,406</td><td>77,453</td><td>36,120</td><td>24,435</td><td>26,836</td><td>57,133</td><td>23,810</td><td>28,923</td><td>33,491</td><td>10,200</td><td>18,684</td><td>6,597</td><td>8,647</td><td>5,205</td></tr><tr><td colspan="19">Flows by client group: Total (stocks &amp; ETFs)</td></tr><tr><td>Hedge funds</td><td>(6,760)</td><td>(32,817)</td><td>(17,099)</td><td>10,953</td><td>(26,688)</td><td>(18,312)</td><td>(7,943)</td><td>363</td><td>(7,297)</td><td>(2,164)</td><td>(2,617)</td><td>(3,134)</td><td>(5,044)</td><td>(2,697)</td><td>(2,085)</td><td>(5,695)</td><td>(4,283)</td><td>5,843</td></tr><tr><td>Institutional clients</td><td>(17,849)</td><td>(32,420)</td><td>(35,702)</td><td>(15,002)</td><td>6,655</td><td>(20,672)</td><td>2,254</td><td>758</td><td>(17,246)</td><td>(52,717)</td><td>(48,537)</td><td>(25,967)</td><td>(18,620)</td><td>(33,194)</td><td>2,668</td><td>1,493</td><td>(13,785)</td><td>6,316</td></tr><tr><td>Private clients</td><td>2,363</td><td>24,564</td><td>(3,336)</td><td>(18,384)</td><td>16,086</td><td>(1,829)</td><td>(10,195)</td><td>(28,106)</td><td>(1,462)</td><td>7,787</td><td>(14,373)</td><td>1,949</td><td>(13,137)</td><td>(18,662)</td><td>(39,973)</td><td>(23,049)</td><td>(26,451)</td><td>(23,347)</td></tr><tr><td>Total stocks + ETFs</td><td>(22,246)</td><td>(40,673)</td><td>(56,137)</td><td>(22,433)</td><td>(3,947)</td><td>(40,813)</td><td>(15,884)</td><td>(26,985)</td><td>(26,004)</td><td>(47,094)</td><td>(65,527)</td><td>(27,152)</td><td>(36,802)</td><td>(54,553)</td><td>(39,390)</td><td>(27,251)</td><td>(44,519)</td><td>(11,189)</td></tr><tr><td colspan="19">Corporate client flows (stocks)</td></tr><tr><td>Corporate Buybacks</td><td>55,176</td><td>135,739</td><td>182,188</td><td>92,617</td><td>80,823</td><td>89,406</td><td>38,250</td><td>89,721</td><td>75,091</td><td>38,587</td><td>37,272</td><td>40,774</td><td>45,393</td><td>38,598</td><td>32,449</td><td>32,897</td><td>32,172</td><td></td></tr></table>

Source: BofA. Note: ETF aggregates based on equity ETFs from 8/25/25 onward vs. all ETFs (included some non-equity) prior to that (see Methodology for details). Corporate client buybacks (available from June 2010 and onward) are shown as a separate flow and not included in any totals above.  
BofA GLOBAL RESEARCH

## Exhibit 6: Flows by size segment: BofA equity client flows by year (single stocks vs. size ETFs)

Cumulative net buying (selling) of single stocks and ETFs by market cap size classification (\$mn) by year (2026 is YTD)

<table><tr><td>Category</td><td>2026</td><td>2025</td><td>2024</td><td>2023</td><td>2022</td><td>2021</td><td>2020</td><td>2019</td><td>2018</td><td>2017</td><td>2016</td><td>2015</td><td>2014</td><td>2013</td><td>2012</td><td>2011</td><td>2010</td><td>2009</td></tr><tr><td colspan="19">Sizes: Single stocks</td></tr><tr><td>Large cap</td><td>(45,452)</td><td>(84,419)</td><td>(68,579)</td><td>(20,482)</td><td>(38,285)</td><td>(76,061)</td><td>(22,421)</td><td>(38,027)</td><td>(34,870)</td><td>(65,081)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mid cap</td><td>(3,856)</td><td>(6,735)</td><td>(10,388)</td><td>(11,794)</td><td>12,977</td><td>(1,157)</td><td>(8,606)</td><td>(3,318)</td><td>(3,041)</td><td>(7,749)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Small &amp; micro cap</td><td>(5,163)</td><td>4,545</td><td>(6,793)</td><td>(3,341)</td><td>3,650</td><td>(8,381)</td><td>(3,626)</td><td>(398)</td><td>(3,117)</td><td>(4,223)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="19">Sizes: ETFs</td></tr><tr><td>Large cap</td><td>25,805</td><td>38,497</td><td>25,988</td><td>7,379</td><td>15,652</td><td>37,281</td><td>17,840</td><td>14,426</td><td>14,600</td><td>28,536</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mid cap</td><td>489</td><td>1,063</td><td>375</td><td>(418)</td><td>77</td><td>443</td><td>(815)</td><td>211</td><td>160</td><td>358</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Small cap</td><td>(953)</td><td>1,830</td><td>7,031</td><td>3,590</td><td>(3,376)</td><td>7,062</td><td>1,744</td><td>121</td><td>264</td><td>1,064</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Broad Market</td><td>7,718</td><td>5,033</td><td>4,582</td><td>4,111</td><td>9,005</td><td>12,786</td><td>1,480</td><td>658</td><td>2,125</td><td>8,591</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="19">Sizes: Total flows (stocks + ETFs)</td></tr><tr><td>Large cap</td><td>(19,647)</td><td>(45,922)</td><td>(42,591)</td><td>(13,103)</td><td>(22,634)</td><td>(38,780)</td><td>(4,580)</td><td>(23,601)</td><td>(20,270)</td><td>(36,545)</td><td>(49,493)</td><td>(29,521)</td><td>(32,765)</td><td>(47,301)</td><td>(32,890)</td><td>(18,556)</td><td>(33,537)</td><td>(10,411)</td></tr><tr><td>Mid cap</td><td>(3,367)</td><td>(5,672)</td><td>(10,013)</td><td>(12,211)</td><td>13,054</td><td>(714)</td><td>(9,421)</td><td>(3,107)</td><td>(2,882)</td><td>(7,391)</td><td>(12,240)</td><td>603</td><td>(2,264)</td><td>(5,328)</td><td>(5,070)</td><td>(7,677)</td><td>(9,775)</td><td>(1,691)</td></tr><tr><td>Small

[中间内容因长度限制已省略]

lect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
