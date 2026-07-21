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
# US Semiconductors and Semi Equipment SemiBytes: Thoughts on Kimi K3, MU, Analog, Cash Flow, Crowding

## Preliminary thoughts on Kimi K3; Read-through to semis

This past week, Moonshot AI released Kimi K3 - a model that is the largest open source model in the world and outperforms some key US frontier models for certain workloads. There are parallels to the release of DeepSeek R1 - which drove a similar correction in stocks - but K3 is more about scale as it is the largest open source model in the world at 2.8T parameters and has a 1M token context window and always-on reasoning mode. Increased usage of open source models was evident at UBS' Private AI, Software and Internet conference this past week (see our summary here). Overall, we would note that the costs of an open source model are inherently going to be better than a frontier model because of the margins, but irrespective of this point, we feel this is much like the release of R1 and part of the normal course of technology businesses - cost scaling drives increased usage/demand (e.g Jevons Paradox) - and in this case, we would also reiterate that NVDA is a big winner in the open source model debate with Nemotron. Another point to make here is that open source models are generally more memory intensive than frontier labs because context windows are longer and KV cache requirements are growing in absolute terms even with quantization, making open-source deployment more HBM- and storage-intensive.

## Fielding questions on MU in relation to the SKHY ADR listing

We continue to field a number of investor questions around how to justify the existing discount between MU and SKHY (SK Hynix's ADR), which we acknowledge exists, but is now quite small (\~0.3x on an NTM EV/S basis (Figure 1 and Figure 2). First, we would argue that MU has historically traded at a premium to SKHY so this is not consistent with normal valuation patterns. Part of this historic pattern may be due to the US versus Korea market dynamics, but we would note that MU has also been able to achieve aggressive density without immediate EUV adoption in DRAM (at 1-alpha and 1-beta nodes), has led the 2XX-L product transition, proven market leadership in LP-DDR, and more broadly, has shown very competitive power efficiency and cost-per-bit. Most importantly, MU is set to generate a prodigious amount of FCF over the coming years (> \$400B in FCF through C2028E). The company remains restricted from share repo through 12/9/26, but from this point forward, we have already said it could potentially use all FCF to buy back stock and this would mean it could buy back 40%+ of the company through CYE2028E at the current stock price.

## What's priced into the analog recovery?

We have been fielding numerous questions regarding the duration of the analog cycle as the industry has now reported 4Qs of above-seasonal growth after 8Qs of being below seasonal dating back to CQ1:23. When looking historically, the 2009-2010 and 2020-2021 recoveries each sustained above-seasonal growth for 5-8 quarters, on average, once the turn took hold. To some degree, stocks are already pricing in a strong recovery and in prior cycles, the multiple peaked at or before the growth inflection and compressed as the above-seasonal quarters progressed; while this cycle, the market has actually driven the multiples up into the recovery with the aggregate multiple achieving new highs a full 4Qs after the turn of the cycle. This all makes sense if one believes in a more sustained upcycle - which is our view. Dispersion within the group suggests the market is already picking sides, with perceived AI power winners such as ALGM (UBSe \~20% DC mix by CY26E) commanding a meaningful premium (42x NTM P/E), while more auto/industrial-weighted names sit closer to historical averages.

## Equities

Americas
Semiconductors

Timothy Arcuri
Analyst
timothy.arcuri@ubs.com
+1-415-352 5676

Natalia Winkler, CFA
Analyst
natalia.winkler@ubs.com
+1-415-352 4626

Alex Kivali
Analyst
alex.kivali@ubs.com
+1-212-713 3945

Gianmarco Vella
Associate Analyst
gianmarco.vella@ubs.com
+1-415-352 4555

Aaryan Wadhwa
Associate Analyst
aaryan.wadhwa@ubs.com
+1-212-821 6481

## Parsing through FCF across our coverage

Semis companies are generating a lot of cash - indeed, FCF through C2028E averages \~10% of market cap across our coverage. Memory & Storage screens highest at \~30% (due to the view that this will likely be the most cyclical on the other side) led by MU at 47% as the current memory tightness drives a step-change in cash generation. Surprisingly, Smartphone follows at 21% (SWKS 26%, QRVO 22%). Conversely, compute averages just 4% with wide dispersion between the companies (NVDA 18% but INTC and AMD very low). Analog (\~10%) and Semicap (\~10%) are slightly below average. AVGO leads Networking/Infra at 16% on \$278B in cumulative FCF; the largest absolute cash generator in our coverage outside of MU and NVDA.

## Crowding update - Semis pulling back from record highs

Following the pullback in semis over the past few weeks, we revisit our UBS Quant Answers crowding factor (where scores range from -30 on the short end to +30 on the long end). For the overall sector, sentiment has tapered slightly since reaching record levels in late June. LRCX, AVGO, STX, MU, and AMD are the stocks in our coverage that appear the most long-crowded, with 12 of 63 stocks still at or above +24 out of +30 despite the drawdown across the broader Semis space. The most short-crowded stocks include SWKS (-13.9), PI (-11.0), and ENTG (-7.9). In Compute, both INTC and AMD remain significantly long-crowded, while ARM (-4.6) and CBRS (-7.7) are short-crowded. Networking sentiment has faded slightly as MRVL sentiment has trended lower, while ALAB is now short-crowded. Memory/Storage remain steady and well-loved, with STX and MU the most crowded followed closely by WDC. Sentiment within Analog has diverged, with ADI and ON fading over the past month while ALGM sentiment has improved (albeit still slightly short-crowded at -3.2). Semicap sentiment is overall little changed over the past month, although AMAT has declined slightly - offset by an increase in KLAC long-crowding. Finally, Smartphone continues to fall out of favor as SWKS is the most short-crowded within our coverage, and QCOM is now short-crowded for only the second time in our 9 year history.

## MU / SKHY VALUATION

Figure 1: MU and SKHY NTM EV/S - 3YR History  
![](images/d4bd14cc06aace97b5f6b340ff9d091a2b04c593d7d5f6077d5f4c8269d4774f.jpg)  
Source: FactSet

Figure 2: MU and SKHY NTM EV/S - 1M History  
![](images/a44c964f538633312aedc127a3ad828d08ab21390533fcb5d9be5b7e4b45bd0a.jpg)  
Source: FactSet

Figure 3: MU and SKHY vs Other Semi Peers - 3YR History  
![](images/2100f190bb520e07968223e0f4b98d459f0cc11b5e9ecd3021bce0079c03961e.jpg)  
Source: FactSet

## ANALOG RECOVERY - WHAT'S PRICED IN?

Figure 4: NTM P/E vs Analog Seasonality  
![](images/8d4ef8df3a28e01e3dee55e2a8e9a5f413df026f3d3c10187ed698e19b4c2132.jpg)  
Source: UBS, FactSet.

Figure 5: FCF Through CY28 as % of Market Cap Across Our Coverage

![](images/df0a9795ecbf9a677ab57ba674d83ca96d4e117886f54f55c7798d9cb653601f.jpg)  
Source: UBS estimates, FactSet.

Figure 6: Compute - FCF Through CY28 as % of Market Cap  
![](images/294b2469d67e8733552351adb7cd428d733ae4aefefc5e189b6fc1a705b600d4.jpg)  
Source: UBS estimates, FactSet.

Figure 7: Analog - FCF Through CY28 as % of Market Cap  
![](images/7e1ad86d9aa86721d67fbdcaf9fd6ebc287b31c6749a69a19f87c6d25fcf9deb.jpg)  
Source: UBS estimates, FactSet.

Figure 8: Memory/Storage - FCF Through CY28 as % of Market Cap  
![](images/fbc4e9a09b67b13fc11bb0ac54bd1f1d4296288116088713908575c59e502786.jpg)  
Source: UBS estimates, FactSet.

Figure 9: Networking - FCF Through CY28 as % of Market Cap  
![](images/8bdeda8fb40766de555d355e64e75b666a88d52271da52ad3afbc08cc19639fe.jpg)  
Source: UBS estimates, FactSet.

Figure 10: Semicap Equipment - FCF Through CY28 as % of Market Cap  
Figure 11: Smartphone - FCF Through CY28 as % of Market Cap  
![](images/8279633b0094e2b81562765b14f2e7fd4751ae355c32d21b936e28c2328633ff.jpg)  
Source: UBS estimates, FactSet.

![](images/6c16769ef2822ad59ba8f37db094ef70b0762a46ae6a9e7041cc2bd6a2af43a7.jpg)  
Source: UBS estimates, FactSet.

## SENTIMENT/INVESTOR POSITIONING

Figure 12: Crowding Dashboard

<table><tr><td rowspan="10">Subsectors</td><td>Stock</td><td>Crowding</td><td>9 year average</td><td>Standard deviation</td><td>1-month change</td><td>1-quarter change</td><td>1-year change</td><td>52 week Trend</td></tr><tr><td>Semis</td><td>+8.2</td><td>+4.5</td><td>±1.8</td><td>-0.6</td><td>+1.9</td><td>+4.5</td><td></td></tr><tr><td>Compute</td><td>+9.4</td><td>+5.2</td><td>±4.1</td><td>-1.0</td><td>-2.4</td><td>+2.8</td><td></td></tr><tr><td>Smartphone</td><td>+1.1</td><td>+10.2</td><td>±5.2</td><td>-3.9</td><td>-8.5</td><td>-5.2</td><td></td></tr><tr><td>Networking/Infra</td><td>+19.6</td><td>+5.1</td><td>±7.9</td><td>-2.6</td><td>-3.3</td><td>-2.3</td><td></td></tr><tr><td>Foundry</td><td>+6.2</td><td>-0.6</td><td>±4.6</td><td>+0.4</td><td>+2.7</td><td>+5.6</td><td></td></tr><tr><td>Memory &amp; Storage</td><td>+19.3</td><td>+7.1</td><td>±5.6</td><td>-1.3</td><td>+0.6</td><td>+7.9</td><td></td></tr><tr><td>Analog</td><td>+3.1</td><td>+0.6</td><td>±2.7</td><td>-0.2</td><td>+4.3</td><td>+3.7</td><td></td></tr><tr><td>SPE &amp; EDA</td><td>+11.4</td><td>+8.2</td><td>±2.5</td><td>+0.4</td><td>+3.4</td><td>+8.3</td><td></td></tr><tr><td>Disty &amp; OSAT</td><td>+8.6</td><td>+2.7</td><td>±3.4</td><td>-0.8</td><td>+0.4</td><td>+4.2</td><td></td></tr><tr><td rowspan="7">Compute</td><td>AMD</td><td>+25.5</td><td>+1.1</td><td>±12.4</td><td>-0.7</td><td>+1.4</td><td>+7.6</td><td></td></tr><tr><td>ARM</td><td>-1.5</td><td>-4.1</td><td>±4.8</td><td>+3.0</td><td>-2.5</td><td>+8.3</td><td></td></tr><tr><td>Cerebras</td><td>-6.9</td><td>-3.9</td><td>±2.8</td><td>-3.5</td><td>-6.9</td><td>-6.9</td><td></td></tr><tr><td>Ceva</td><td>-1.9</td><td>+1.9</td><td>±3.0</td><td>-6.6</td><td>-4.1</td><td>-0.5</td><td></td></tr><tr><td>Intel</td><td>+25.3</td><td>+10.9</td><td>±8.9</td><td>+0.0</td><td>-0.1</td><td>+8.8</td><td></td></tr><tr><td>Lattice*</td><td>+1.4</td><td>+3.5</td><td>±7.9</td><td>+1.3</td><td>+8.9</td><td>+9.8</td><td></td></tr><tr><td>Nvidia</td><td>+24.0</td><td>+12.3</td><td>±12.5</td><td>-0.8</td><td>-1.7</td><td>-0.8</td><td></td></tr><tr><td rowspan="4">Smartphone</td><td>Mediatek*</td><td>+6.1</td><td>+6.9</td><td>±8.6</td><td>-5.2</td><td>+0.3</td><td>-1.5</td><td></td></tr><tr><td>Qualcomm</td><td>-1.5</td><td>+19.2</td><td>±7.0</td><td>-9.8</td><td>-18.8</td><td>-26.3</td><td></td></tr><tr><td>Qorvo</td><td>+13.7</td><td>+6.3</td><td>±8.7</td><td>0</td><td>0</td><td>+12.3</td><td></td></tr><tr><td>Skyworks</td><td>-13.9</td><td>+8.1</td><td>±8.1</td><td>-0.5</td><td>-15.4</td><td>-5.4</td><td></td></tr><tr><td rowspan="5">Networking</td><td>Astera Labs</td><td>-3.6</td><td>-0.8</td><td>±6.8</td><td>-8.8</td><td>+7.7</td><td>-12.2</td><td></td></tr><tr><td>Broadcom</td><td>+26.5</td><td>+9.2</td><td>±9.5</td><td>+0.1</td><td>+0.1</td><td>+0.2</td><td></td></tr><tr><td>Marvell</td><td>+12.7</td><td>+4.5</td><td>±10.2</td><td>-5.2</td><td>-6.7</td><td>-4.8</td><td></td></tr><tr><td>MACOM*</td><td>+8.6</td><td>-4.1</td><td>±7.4</td><td>+5.5</td><td>+20.7</td><td>-0.6</td><td></td></tr><tr><td>Semtech</td><td>+3.2</td><td>+3.8</td><td>±7.8</td><td>+4.2</td><td>+3.9</td><td>+11.6</td><td></td></tr><tr><td rowspan="6">Foundry</td><td>GloFo</td><td>+8.7</td><td>-4.2</td><td>±8.4</td><td>+4.2</td><td>+2.9</td><td>+5.8</td><td></td></tr><tr><td>Hua Hong*</td><td>-2.2</td><td>-9.2</td><td>±3.7</td><td>+4.8</td><td>+7.8</td><td>+13.5</td><td></td></tr><tr><td>SMIC*</td><td>+1.9</td><td>-6.1</td><td>±8.1</td><td>-2.9</td><td>-0.1</td><td>-1.0</td><td></td></tr><tr><td>TSMC*</td><td>+9.7</td><td>+12.7</td><td>±8.5</td><td>-0.3</td><td>+0.0</td><td>+1.6</td><td></td></tr><tr><td>UMC*</td><td>+4.5</td><td>-1.6</td><td>±8.3</td><td>+0.5</td><td>+8.1</td><td>+15.8</td><td></td></tr><tr><td>Vanguard*</td><td>-1.9</td><td>-4.2</td><td>±5.0</td><td>-1.0</td><td>+5.4</td><td>+9.4</td><td></td></tr><tr><td rowspan="7">Memory &amp; Storage</td><td>Micron</td><td>+25.7</td><td>+13.9</td><td>±10.0</td><td>-0.5</td><td>-1.2</td><td>+8.7</td><td></td></tr><tr><td>Nanya Tech*</td><td>-1.1</td><td>-0.2</td><td>±5.0</td><td>-3.2</td><td>+1.0</td><td>+4.5</td><td></td></tr><tr><td>Samsung*</td><td>+17.1</td><td>+14.1</td><td>±4.6</td><td>-2.2</td><td>-2.4</td><td>+3.4</td><td></td></tr><tr><td>Sandisk*</td><td>+23.7</td><td>+16.9</td><td>±8.8</td><td>-0.7</td><td>-0.3</td><td>+13.4</td><td></td></tr><tr><td>SK Hynix*</td><td>+18.5</td><td>+8.1</td><td>±6.6</td><td>-1.1</td><td>-1.5</td><td>+0.0</td><td></td></tr><tr><td>Seagate</td><td>+25.8</td><td>+0.2</td><td>±9.1</td><td>-1.1</td><td>+7.2</td><td>+13.0</td><td></td></tr><tr><td>Western Digital</td><td>+25.2</td><td>+5.5</td><td>±10.9</td><td>-0.6</td><td>+1.4</td><td>+12.5</td><td></td></tr></table>

<table><tr><td colspan="2">Stock</td><td>Crowding</td><td>9 year average</td><td>Standard deviation</td><td>1-month change</td><td>1-quarter change</td><td>1-year change</td><td>52 week Trend</td></tr><tr><td rowspan="15">Analog</td><td>Analog Devices</td><td>+18.4</td><td>+8.2</td><td>±9.7</td><td>-8.1</td><td>-1.5</td><td>+1.3</td><td></td></tr><tr><td>Allegro</td><td>-3.2</td><td>+1.1</td><td>±6.0</td><td>+7.4</td><td>-1.3</td><td>+2.8</td><td></td></tr><tr><td>Ambiq</td><td>-7.2</td><td>-5.6</td><td>±2.3</td><td>+0.1</td><td>-2.3</td><td>-7.2</td><td></td></tr><tr><td>ams AG*</td><td>+1.5</td><td>-5.9</td><td>±8.1</td><td>+0.9</td><td>+0.2</td><td>+2.2</td><td></td></tr><tr><td>indie</td><td>-1.9</td><td>-6.2</td><td>±5.1</td><td>+1.1</td><td>+10.8</td><td>+8.1</td><td></td></tr><tr><td>Infineon*</td><td>+15.0</td><td>+3.0</td><td>±9.3</td><td>+2.4</td><td>+13.0</td><td>+14.6</td><td></td></tr><tr><td>Impinj</td><td>-11.0</td><td>-4.7</td><td>±5.2</td><td>+1.3</td><td>+3.3</td><td>-7.6</td><td></td></tr><tr><td>Microchip</td><td>+8.2</td><td>-0.7</td><td>±9.7</td><td>-3.9</td><td>+4.7</td><td>+17.1</td><td></td></tr><tr><td>Melexis*</td><td>-3.0</td><td>-4.8</td><td>±5.5</td><td>+0.6</td><td>+0.6</td><td>+1.6</td><td></td></tr><tr><td>NXP*</td><td>+8.1</td><td>+15.1</td><td>±9.5</td><td>-3.1</td><td>+7.9</td><td>+6.1</td><td></td></tr><tr><td>ON Semi</td><td>-7.9</td><td>-0.0</td><td>±9.0</td><td>-3.6</td><td>-1.9</td><td>+0.1</td><td></td></tr><tr><td>Renesas*</td><td>+6.0</td><td>-0.8</td><td>±8.7</td><td>+1.8</td><td>+4.6</td><td>-6.8</td><td></td></tr><tr><td>SiTime</td><td>-3.2</td><td>-3.6</td><td>±5.0</td><td>+2.4</td><td>+1.3</td><td>-2.7</td><td></td></tr><tr><td>STMicro*</td><td>+2.0</td><td>-3.2</td><td>±3.5</td><td>+1.1</td><td>+3.1</td><td>+3.2</td><td></td></tr><tr><td>Texas Inst</td><td>+24.5</td><td>+7.0</td><td>±8.5</td><td>-2.7</td><td>+22.6</td><td>+22.0</td><td></td></tr><tr><td rowspan="14">SPE &amp; EDA</td><td>Advantest*</td><td>+6.7</td><td>-3.0</td><td>±7.9</td><td>-5.1</td><td>-5.1</td><td>+12.4</td><td></td></tr><tr><td>Applied Materials</td><td>+24.9</td><td>+20.7</td><td>±5.7</td><td>-2.4</td><td>+5.0</td><td>+8.8</td><td></td></tr><tr><td>ASM Intl*</td><td>+10.4</td><td>+7.8</td><td>±7.8</td><td>-2.9</td><td>+2.0</td><td>+7.7</td><td></td></tr><tr><td>ASML*</td><td>+9.6</td><td>+3.7</td><td>±6.3</td><td>+0.1</td><td>+0.2</td><td>+4.5</td><td></td></tr><tr><td>Cadence*</td><td>-4.0</td><td>+16.2</td><td>±8.8</td><td>-1.2</td><td>+0.3</td><td>-10.8</td><td></td></tr><tr><td>DISCO*</td><td>+7.7</td><td>-1.8</td><td>±7.2</td><td>+4.3</td><td>+8.7</td><td>+7.1</td><td></td></tr><tr><td>Entegris</td><td>-7.9</td><td>-1.4</td><td>±8.5</td><td>+3.5</td><td>+3.

[中间内容因长度限制已省略]

 and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
