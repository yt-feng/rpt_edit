你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

<table><tr><td colspan="2">Stock</td><td>Crowding</td><td>9 year average</td><td>Standard deviation</td><td>1-month change</td><td>1-quarter change</td><td>1-year change</td><td>52 week Trend</td></tr><tr><td rowspan="15">Analog</td><td>Analog Devices</td><td>+18.4</td><td>+8.2</td><td>±9.7</td><td>-8.1</td><td>-1.5</td><td>+1.3</td><td></td></tr><tr><td>Allegro</td><td>-3.2</td><td>+1.1</td><td>±6.0</td><td>+7.4</td><td>-1.3</td><td>+2.8</td><td></td></tr><tr><td>Ambiq</td><td>-7.2</td><td>-5.6</td><td>±2.3</td><td>+0.1</td><td>-2.3</td><td>-7.2</td><td></td></tr><tr><td>ams AG*</td><td>+1.5</td><td>-5.9</td><td>±8.1</td><td>+0.9</td><td>+0.2</td><td>+2.2</td><td></td></tr><tr><td>indie</td><td>-1.9</td><td>-6.2</td><td>±5.1</td><td>+1.1</td><td>+10.8</td><td>+8.1</td><td></td></tr><tr><td>Infineon*</td><td>+15.0</td><td>+3.0</td><td>±9.3</td><td>+2.4</td><td>+13.0</td><td>+14.6</td><td></td></tr><tr><td>Impinj</td><td>-11.0</td><td>-4.7</td><td>±5.2</td><td>+1.3</td><td>+3.3</td><td>-7.6</td><td></td></tr><tr><td>Microchip</td><td>+8.2</td><td>-0.7</td><td>±9.7</td><td>-3.9</td><td>+4.7</td><td>+17.1</td><td></td></tr><tr><td>Melexis*</td><td>-3.0</td><td>-4.8</td><td>±5.5</td><td>+0.6</td><td>+0.6</td><td>+1.6</td><td></td></tr><tr><td>NXP*</td><td>+8.1</td><td>+15.1</td><td>±9.5</td><td>-3.1</td><td>+7.9</td><td>+6.1</td><td></td></tr><tr><td>ON Semi</td><td>-7.9</td><td>-0.0</td><td>±9.0</td><td>-3.6</td><td>-1.9</td><td>+0.1</td><td></td></tr><tr><td>Renesas*</td><td>+6.0</td><td>-0.8</td><td>±8.7</td><td>+1.8</td><td>+4.6</td><td>-6.8</td><td></td></tr><tr><td>SiTime</td><td>-3.2</td><td>-3.6</td><td>±5.0</td><td>+2.4</td><td>+1.3</td><td>-2.7</td><td></td></tr><tr><td>STMicro*</td><td>+2.0</td><td>-3.2</td><td>±3.5</td><td>+1.1</td><td>+3.1</td><td>+3.2</td><td></td></tr><tr><td>Texas Inst</td><td>+24.5</td><td>+7.0</td><td>±8.5</td><td>-2.7</td><td>+22.6</td><td>+22.0</td><td></td></tr><tr><td rowspan="14">SPE &amp; EDA</td><td>Advantest*</td><td>+6.7</td><td>-3.0</td><td>±7.9</td><td>-5.1</td><td>-5.1</td><td>+12.4</td><td></td></tr><tr><td>Applied Materials</td><td>+24.9</td><td>+20.7</td><td>±5.7</td><td>-2.4</td><td>+5.0</td><td>+8.8</td><td></td></tr><tr><td>ASM Intl*</td><td>+10.4</td><td>+7.8</td><td>±7.8</td><td>-2.9</td><td>+2.0</td><td>+7.7</td><td></td></tr><tr><td>ASML*</td><td>+9.6</td><td>+3.7</td><td>±6.3</td><td>+0.1</td><td>+0.2</td><td>+4.5</td><td></td></tr><tr><td>Cadence*</td><td>-4.0</td><td>+16.2</td><td>±8.8</td><td>-1.2</td><td>+0.3</td><td>-10.8</td><td></td></tr><tr><td>DISCO*</td><td>+7.7</td><td>-1.8</td><td>±7.2</td><td>+4.3</td><td>+8.7</td><td>+7.1</td><td></td></tr><tr><td>Entegris</td><td>-7.9</td><td>-1.4</td><td>±8.5</td><td>+3.5</td><td>+3.9</td><td>+3.4</td><td></td></tr><tr><td>KLA</td><td>+8.3</td><td>+11.7</td><td>±8.6</td><td>+1.8</td><td>+6.0</td><td>+11.8</td><td></td></tr><tr><td>Lam Research</td><td>+27.4</td><td>+18.3</td><td>±6.2</td><td>-0.4</td><td>+0.2</td><td>+21.0</td><td></td></tr><tr><td>Qnity*</td><td>-1.5</td><td>+3.8</td><td>±3.0</td><td>-5.3</td><td>-4.5</td><td>-1.5</td><td></td></tr><tr><td>Synopsys*</td><td>+24.9</td><td>+14.4</td><td>±9.2</td><td>+4.3</td><td>+23.2</td><td>+7.0</td><td></td></tr><tr><td>Teradyne</td><td>+24.3</td><td>+12.1</td><td>±7.4</td><td>-1.8</td><td>-1.6</td><td>+24.3</td><td></td></tr><tr><td>Tokyo Electron*</td><td>+16.7</td><td>+6.7</td><td>±6.0</td><td>+0.6</td><td>+1.8</td><td>+9.7</td><td></td></tr><tr><td>Ultra Clean</td><td>+7.9</td><td>+0.9</td><td>±4.0</td><td>+7.0</td><td>+3.6</td><td>+10.3</td><td></td></tr><tr><td rowspan="5">Disty &amp; OSAT</td><td>Amkor*</td><td>+8.8</td><td>+1.7</td><td>±5.8</td><td>-0.1</td><td>-5.1</td><td>+2.0</td><td></td></tr><tr><td>Arrow*</td><td>+17.1</td><td>+6.8</td><td>±6.7</td><td>-0.9</td><td>+5.8</td><td>+3.1</td><td></td></tr><tr><td>ASE*</td><td>+1.6</td><td>+0.0</td><td>±4.9</td><td>-0.2</td><td>-0.3</td><td>+4.0</td><td></td></tr><tr><td>Avnet*</td><td>+12.8</td><td>+5.5</td><td>±5.7</td><td>-1.3</td><td>+3.0</td><td>+5.4</td><td></td></tr><tr><td>WPG*</td><td>+2.9</td><td>-1.8</td><td>±4.0</td><td>-1.5</td><td>-1.2</td><td>+6.7</td><td></td><

[中间内容因长度限制已省略]

 (UAE) / DIFC / Abu Dhabi: UBS is not licensed in the UAE by the Central Bank of the UAE nor by the Emirates' Securities and Commodities Authority and does not undertake banking activities in the UAE. This document is provided for your information only and does not constitute financial advice. DIFC: UBS AG Dubai Branch is regulated by the DFSA in the DIFC. This material is strictly intended for Professional Clients and/or Market Counterparties only as classified under the DFSA rulebook. It should not be distributed to Retail Clients. The Investment Research is provided for information purposes only and is not a recommendation or offer to buy/sell/hold a particular investment. The investment research may be out of date. You should seek investment advice before acting on the basis of the Investment Research. Abu Dhabi: UBS AG Abu Dhabi Branch is licensed and regulated by the Financial Services Regulatory Authority ("FSRA") of the Abu Dhabi Global Market. This material is intended solely for professional clients or market counterparties, as defined in the rules of the FSRA. It is not directed at, nor intended for, retail clients or any person who does not meet the criteria of a professional client or market counterparty. United Kingdom: This document is issued by UBS Wealth Management, a division of UBS AG which is authorised and regulated by the Financial Market Supervisory Authority in Switzerland. In the United Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.
"""
