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
# ASEAN Equity Strategy Can ASEAN benefit beyond AI?

## Looking beyond the underperformance

ASEAN's underperformance relative to Asia ex Japan reflects macro headwinds, policy uncertainty and limited direct exposure to the AI theme that has driven regional equity returns. Tech accounts for just 4% of MSCI ASEAN, yet drove 25% of index returns YTD. Growth expectations and investor sentiment are subdued, leaving the region largely overlooked. While aggregate valuations have been lifted to 2SD above the 20-year average by a handful of index heavyweights, valuations across the broader market remain compelling, with 55% of MSCI ASEAN stocks trading below historical averages. Capital market reforms and domestic policy initiatives are gaining traction, creating potential re-rating catalysts. As investors diversify beyond increasingly concentrated AI-related holdings, ASEAN markets could warrant renewed attention.

## Selective flows and positioning could broaden on AI diversification

Limited large-scale AI beneficiaries have resulted in uneven participation across ASEAN. Foreign investors have been net buyers of Thailand and Malaysia, reflecting interest in reform momentum and tech-related themes, while Indonesia and the Philippines continue to see net outflows amid policy uncertainty and macro concerns. Singapore remains the only ASEAN market where global funds are overweight, while the rest are broadly neutral. We expect AI to remain the dominant driver of investor allocations, favouring markets with direct and indirect exposure to the theme, including Thailand, Malaysia and Singapore. As market leadership broadens beyond a narrow group of AI winners, however, ASEAN could attract incremental inflows particularly into markets offering earnings visibility, reform momentum and valuation support. Recent performance may be an early indication of a shift, with ASEAN outperforming broader EM and Asia by 16% since KOSPI's June 2026 peak.

## Key themes that will drive markets in H226

1) Direct AI exposure remains limited at 8% of ASEAN (versus 31% for EM/APAC), but the region provides selective opportunities and diversification benefits. 2) Oil and food inflation will be a key swing factor for growth, earnings and margins, with the Philippines, Thailand and Indonesia most vulnerable. El Niño adds a further layer of risk, with ASEAN equities underperforming by 7% on average during past cycles. 3) While the bulk of the tightening cycle is likely behind us, higher-for-longer rates remain a headwind. Philippines is the most sensitive to US rates, while local rates matter more for Indonesia. 4) Policy and political uncertainty are key overhangs for Indonesia and the Philippines, while election-related risks are building in Malaysia. 5) Value-up initiatives in Singapore, Malaysia and Thailand could create scope for a sustained re-rating.

## How are we positioned within ASEAN?

Our ASEAN market ratings are based on the EM & APAC Equity strategy framework. We are overweight Malaysia and Vietnam, where supportive structural and policy catalysts outweigh overall macro risks. Malaysia benefits from a stable macro backdrop and re-rating potential from MY Value Up as well as tech-related opportunities, despite emerging election risk. Vietnam remains the premier growth market, with ongoing reforms and potential index inclusion catalysts. We are neutral Singapore and Thailand. Singapore's capital market reforms, safe-haven characteristics and structural demand drivers particularly in banking and tech support resilience. Thailand offers recovery potential through tourism and domestic policy support offset by continued macro challenges. We are underweight Indonesia and Philippines, where policy uncertainty, earnings risks and macro pressures continue to outweigh attractive valuations. Figure 15 presents our preferred stocks across ASEAN markets.

## Equity Strategy

Asia

Karen Hizon
Strategist
karen.hizon@ubs.com
+852-2971 6741

Sunil Tirumalai
Strategist
sunil.tirumalai@ubs.com
+91-22-6155 6080

Grace Lim
Economist
grace-k.lim@ubs.com
+65-6495 5965

Joshua Tanja, CFA
Analyst
joshua.tanja@ubs.com
+62-21-2554 7030

Permada Darmono
Analyst
permada.darmono@ubs.com
+65-6495 3137

Nicole Goh
Analyst
nicole.goh@ubs.com
+603-2781 1133

Alex Manoonpol
Analyst
alex.manoonpol@ubs.com
+662-613 5770

John Te, CFA
Analyst
john.te@ubs.com
+632-8784 8814

Kruti Shah, CFA
Strategist
kruti.shah@ubs.com
+91-22-6155 6031

Claire Long
Economist
claire.long@ubs.com
+65 6495 7426

## ASEAN AT A GLANCE

Figure 1: ASEAN markets have been largely overlooked due to limited exposure to large-scale AI beneficiaries  
![](images/9729118554cdea901038ea8d5c398a0f94412bad3ce1c84677c373012cf15aa7.jpg)  
Source: UBS

Figure 2: While IT only accounts for 4% of MSCI ASEAN, it has driven 25% of returns YTD  
![](images/23963ef30600974f1c070f7b5c808a2ff13b3b2e1f219d9bfb9933e7c91a63f9.jpg)  
Source: IBES, MSCI, Datastream

Figure 3: ASEAN valuations are largely skewed by a handful of index heavyweights  
![](images/de3652d7a540daef80780eded40d7e2ac4583a429259ecc4d065067b69808591.jpg)  
Source: IBES, MSCI, Datastream, UBS. Note: calculated on the basis of index-weighted methodology (video link)

Figure 4: 55% of MSCI ASEAN stocks are trading below their respective 10y average valuations  
![](images/1de2a79c4426e4212a7a91a2aa69b9e2c2be08af204861c873d67b70f86d1ea3.jpg)  
Source: IBES, MSCI, Datastream

Figure 5: 2026 EPS evolution: Downgrades across the region, except for Thailand and Malaysia  
![](images/65bec8ad73f7c06901ec285ebdfd125ffe163843193f1519a36925fb3beac6c4.jpg)  
Source: IBES, MSCI, Datastream, UBS. Note: calculated on the basis of index-weighted methodology

Figure 6: 2027 EPS evolution: Thailand is seeing upgrades, alongside Vietnam amid big 2026 cuts  
![](images/2e0d42293842ad28fcf97a20c55a08bae099dfbb5a7426c85f5c149481f32ee2.jpg)  
Source: IBES, MSCI, Datastream, UBS. Note: calculated on the basis of index-weighted methodology

Figure 7: EPS revisions were strongest in Korea and Taiwan, with Thailand also seeing modest upgrades. The rest of the region generally saw downgrades  
![](images/9825bdb0ffe9f2b7a81bf103a8ee4f121c3e76d236308ae7420563da77a360f6.jpg)  
Source: IBES, MSCI, Datastream, UBS. Note: calculated on the basis of index-weighted methodology

Figure 8: EPS momentum by sector contribution: Financials, which account for 50% of MSCI ASEAN, are leading downgrades, followed by consumer staples  
![](images/4adc982600bfa2b4417f159e5b6d137775b82b063f331703374697bc2252aee8.jpg)  
Source: IBES, MSCI, Datastream, UBS

Figure 9: Within ASEAN, foreigners are net buyers of Thailand and Malaysia and net sellers of Indonesia and Philippines  
![](images/d09390980dbeca52ac4a7f68c049dd8e14dfd96bd79435019bddb9353f253f26.jpg)  
Source: Bloomberg, UBS

Figure 10: Global funds are overweight Singapore, while the rest of ASEAN are largely at benchmark as of 1Q26  
![](images/9d1485c243f1357f0736f3228662ef635bfa0c075a861be718a9e97978e7a0bf.jpg)  
Source: Bloomberg, MSCI, Datastream, UBS

Figure 11: ASEAN total return attribution: PE expansion has been the primary driven of total returns since 2025, followed by dividends and currency  
![](images/a8bb0cfd39ded5b4aeac3d3bb54cc16857f1f43b9875acfb23c61970543d277c.jpg)  
Source: IBES, MSCI, Datastream, UBS

Figure 12: But over the last 10 years, EPS growth has been the biggest driver of returns, followed by PE expansion  
![](images/c4f94afb8bedfd9af9e0b5007733f755946bdd63840f8e1022f5fe15a20e51dc.jpg)  
Source: IBES, MSCI, Datastream, UBS

Figure 13: Similar to broader regional trends, ASEAN markets have high concentration at the single-stock level  
![](images/0b7c4eba68567aa0850acf919c3dfc1d13f88d20845d75b3f7592a7896b06dab.jpg)  
Source: IBES, MSCI, Datastream. Note: based on free-float adjusted market cap

Figure 14: Excluding Indonesia, over 50% of YTD returns in each market were driven by the single largest stock  
![](images/b9d4001085ab6ef9f6b31b9d0e00372ece9ad61620fdd5b89865c34538d8e86e.jpg)  
Source: IBES, MSCI, Datastream. Note: based on free-float adjusted market cap

Figure 15: Our preferred stocks in ASEAN

<table><tr><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">RIC</td><td rowspan="2">Mkt Cap (US$ bn)</td><td rowspan="2">Price (LC)</td><td rowspan="2">Price Target (LC)</td><td colspan="2">P/E (x)</td><td colspan="2">P/BV (x)</td><td colspan="2">Div yield (%)</td><td colspan="2">EPS growth (%)</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td>BCA</td><td>ID</td><td>BBCA.JK</td><td>43.1</td><td>6275.0</td><td>7150.0</td><td>13.3</td><td>12.8</td><td>2.6</td><td>2.4</td><td>5.4</td><td>5.4</td><td>0.6</td><td>4.0</td></tr><tr><td>AIS</td><td>TH</td><td>ADVANC.BK</td><td>33.2</td><td>376.0</td><td>400.0</td><td>21.4</td><td>20.3</td><td>19.5</td><td>18.2</td><td>4.5</td><td>4.9</td><td>13.4</td><td>5.4</td></tr><tr><td>Gulf Development</td><td>TH</td><td>GULF.BK</td><td>29.2</td><td>66.0</td><td>82.0</td><td>29.4</td><td>27.1</td><td>3.0</td><td>2.8</td><td>2.2</td><td>2.4</td><td>16.6</td><td>8.4</td></tr><tr><td>ST Engineering</td><td>SG</td><td>STEG.SI</td><td>25.6</td><td>10.6</td><td>12.6</td><td>31.6</td><td>25.6</td><td>11.0</td><td>9.2</td><td>1.9</td><td>2.1</td><td>126.1</td><td>23.3</td></tr><tr><td>Tenaga</td><td>MY</td><td>TENA.KL</td><td>20.4</td><td>14.4</td><td>17.0</td><td>17.0</td><td>16.1</td><td>1.6</td><td>1.6</td><td>3.8</td><td>4.0</td><td>19.3</td><td>5.9</td></tr><tr><td>CIMB Group</td><td>MY</td><td>CIMB.KL</td><td>20.3</td><td>7.7</td><td>9.2</td><td>10.5</td><td>9.8</td><td>1.1</td><td>1.1</td><td>6.1</td><td>6.2</td><td>0.0</td><td>6.8</td></tr><tr><td>Jardine Matheson</td><td>SG</td><td>JARD.SI</td><td>18.7</td><td>63.6</td><td>80.0</td><td>12.2</td><td>10.1</td><td>0.7</td><td>0.6</td><td>3.9</td><td>4.1</td><td>-9.0</td><td>21.2</td></tr><tr><td>Kasikornbank</td><td>TH</td><td>KBANK.BK</td><td>16.9</td><td>240.0</td><td>255.0</td><td>11.3</td><td>11.7</td><td>1.0</td><td>0.9</td><td>5.8</td><td>5.5</td><td>1.5</td><td>-3.6</td></tr><tr><td>Amman</td><td>ID</td><td>AMMN.JK</td><td>16.3</td><td>4040.0</td><td>6100.0</td><td>19.6</td><td>10.7</td><td>2.6</td><td>2.1</td><td>0.0</td><td>0.0</td><td>242.7</td><td>78.5</td></tr><tr><td>Telkom Indonesia</td><td>ID</td><td>TLKM.JK</td><td>14.5</td><td>2630.0</td><td>3400.0</td><td>12.0</td><td>10.7</td><td>2.0</td><td>1.9</td><td>8.1</td><td>8.1</td><td>-3.8</td><td>11.5</td></tr><tr><td>True Corp</td><td>TH</td><td>TRUE.BK</td><td>14.3</td><td>14.0</td><td>19.3</td><td>19.0</td><td>17.8</td><td>5.9</td><td>5.5</td><td>3.9</td><td>4.2</td><td>33.3</td><td>7.0</td></tr><tr><td>CP All</td><td>TH</td><td>CPALL.BK</td><td>12.3</td><td>46.5</td><td>61.0</td><td>13.7</td><td>12.4</td><td>2.7</td><td>2.4</td><td>3.4</td><td>3.7</td><td>7.6</td><td>10.4</td></tr><tr><td>Meralco</td><td>PH</td><td>MER.PS</td><td>10.9</td><td>600.0</td><td>750.0</td><td>13.5</td><td>12.3</td><td>3.6</td><td>3.2</td><td>4.8</td><td>4.9</td><td>-2.2</td><td>9.6</td></tr><tr><td>Banco de Oro</td><td>PH</td><td>BDO.PS</td><td>10.6</td><td>123.0</td><td>180.0</td><td>7.7</td><td>6.5</td><td>1.0</td><td>0.9</td><td>3.7</td><td>4.1</td><td>-2.5</td><td>17.8</td></tr><tr><td>Petronas Chemicals</td><td>MY</td><td>PCGB.KL</td><td>9.6</td><td>4.9</td><td>6.9</td><td>21.2</td><td>23.6</td><td>1.1</td><td>1.0</td><td>2.6</td><td>2.3</td><td>-269.2</td><td>-10.1</td></tr><tr><td>Bangkok Dusit</td><td>TH</td><td>BDMS.BK</td><td>8.9</td><td>18.9</td><td>23.0</td><td>19.1</td><td>17.7</td><td>2.8</td><td>2.7</td><td>4.5</td><td>4.9</td><td>-0.7</td><td>7.6</td></tr><tr><td>BPI</td><td>PH</td><td>BPI.PS</td><td>8.8</td><td>102.5</td><td>145.0</td><td>8.3</td><td>7.1</td><td>1.1</td><td>1.0</td><td>4.9</td><td>4.8</td><td>-1.9</td><td>16.8</td></tr><tr><td>TECHCOMBank</td><td>VN</td><td>TCB.HM</td><td>7.7</td><td>28600.0</td><td>45000.0</td><td>7.2</td><td>5.6</td><td>1.1</td><td>1.0</td><td>2.5</td><td>5.6</td><td>10.7</td><td>29.0</td></tr><tr><td>HPG</td><td>VN</td><td>HPG.HM</td><td>6.7</td><td>20800.0</td><td>31500.0</td><td>8.8</td><td>6.8</td><td>1.1</td><td>0.9</td><td>0.5</td><td>1.3</td><td>32.2</td><td>28.7</td></tr><tr><td>UOL Group</td><td>SG</td><td>UTOS.SI</td><td>6.2</td><td>9.4</td><td>12.7</td><td>16.8</td><td>12.7</td><td>n/a</td><td>n/a</td><td>2.1</td><td>2.3</td><td>20.6</td><td>31.8</td></tr><tr><td>City Developments</td><td>SG</td><td>CTDM.SI</td><td>5.2</td><td>7.5</td><td>11.6</td><td>15.2</td><td>13.3</td><td>n/a</td><td>n/a</td><td>2.7</td><td>2.7</td><td>-39.1</td><td>14.1</td></tr><tr><td>Asia Commercial Bank</td><td>VN</td><td>ACB.HM</td><td>4.4</td><td>22500.0</td><td>36000.0</td><td>6.1</td><td>4.9</td><td>1.1</td><td>0.9</td><td>3.1</td><td>5.0</td><td>21.3</td><td>23.8</td></tr><tr><td>Mobile World</td><td>VN</td><td>MWG.HM</td><td>3.8</td><td>68000.0</td><td>118000.0</td><td>11.9</td><td>10.6</td><td>3.2</td><td>3.0</td><td>1.8</td><td>2.0</td><td>18.4</td><td>12.5</td></tr><tr><td>Mr D.I.Y.</td><td>MY</td><td>MRDI.KL</td><td>3.7</td><td>1.6</td><td>2.15</td><td>21.1</td><td>18.8</td><td>8.0</td><td>8.0</td><td>5.7</td><td>5.3</td><td>11.7</td><td>11.8</td></tr><tr><td>Alamtri Minerals</td><td>ID</td><td>ADMR.JK</td><td>3.4</td><td>1480.0</td><td>2500.0</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td></tr><tr><td>Vale Indonesia</td><td>ID</td><td>INCO.JK</td><td>2.7</td><td>4870.0</td><td>8400.0</td><td>11.2</td><td>6.2</td><td>0.9</td><td>0.8</td><td>1.1</td><td>3.7</td><td>224.3</td><td>75.2</td></tr><tr><td>Jollibee</td><td>PH</td><td>JFC.PS</td><td>2.6</td><td>144.0</td><td>220.0</td><td>16.0</td><td>11.1</td><td>1.9</td><td>1.7</td><td>2.3</td><td>3.3</td><td>-4.2</td><td>44.1</td></tr><tr><td>Maynilad</td><td>PH</td><td>MYNLD.PS</td><td>2.3</td><td>19.5</td><td>25.5</td><td>8.7</td><td>8.6</td><td>1.2</td><td>1.1</td><td>5.8</td><td>6.4</td><td>-13.3</td><td>1.7</td></tr><tr><td>AEM Holdings</td><td>SG</td><td>AEM.SI</td><td>2.2</td><td>9.0</td><td>16.0</td><td>38.5</td><td>22.9</td><td>5.1</td><td>4.3</td><td>0.5</td><td>0.9</td><td>332.9</td><td>68.3</td></tr><tr><td>Cimory</td><td>ID</td><td>CMRY.JK</td><td>2.0</td><td>4580.0</td><td>6800.0</td><td>16.1</td><td>13.1</td><td>4.9</td><td>4.3</td><td>4.4</td><td>4.9</td><td>12.3</td><td>23.0</td></tr><tr><td>Monde Nissin</td><td>PH</td><td>MONDE.PS</td><td>2.0</td><td>6.7</td><td>8.4</td><td>10.9</td><td>10.4</td><td>2.0</td><td>1.9</td><td>8.9</td><td>6.9</td><td>13.7</td><td>4.9</td></tr><tr><td>Vincom Retail</td><td>VN</td><td>VRE.HM</td><td>1.9</td><td>21900.0</td><td>41100.0</td><td>9.0</td><td>8.3</td><td>n/a</td><td>n/a</td><td>4.6</td><td>0.0</td><td>-13.8</td><td>8.0</td></tr><tr><td>Kelington Group</td><td>MY</td><td>KELG.KL</td><td>1.5</td><td>8.0</td><td>9.0</td><td>34.2</td><td>26.8</td><td>8.4</td><td>7.4</td><td>1.7</td><td>2.1</td><td>10.4</td><td>27.7</td></tr><tr><td>Gemadept</td><td>VN</td><td>GMD.HM</td><td>1.2</td><td>73200.0</td><td>92000.0</td><td>15.3</td><td>14.5</td><td>2.3</td><td>2.2</td><td>4.6</td><td>4.8</td><td>19.7</td><td>5.5</td></tr><tr><td>FPT Retail</td><td>VN</td><td>FRT.HM</td><td>0.7</td><td>107800.0</td><td>200000.0</td><td>18.1</td><td>14.1</td><td>3.7</td><td>3.0</td><td>1.1</td><td>1.4</td><td>27.9</td><td>27.7</td></tr><tr><td>Nam Long Investment</td><td>VN</td><td>NLG.HM</td><td>0.4</td><td>21350.0</td><td>37000.0</td><td>11.7</td><td>12.2</td><td>n/a</td><td>n/a</td><td>4.7</td><td>4.7</td><td>13.6</td><td>-4.4</td></tr></table>

Source: UBS estimates. Note: Sorted by market cap. Pricing data as of 24 July 2026.

MSCI Asia ex Japan sector breakdown by market cap

## Key themes

We believe five key themes could shape A

[中间内容因长度限制已省略]

ofessional/institutional clients only and not for distribution to any retail clients. Malaysia: This material is authorized to be distributed in Malaysia by UBS Malaysia Sdn. Bhd (Capital Markets Services License No.: CMSL/A0063/2007). This material is intended for professional/institutional clients only and not for distribution to any retail clients. India: Distributed by UBS India Private Ltd. (Corporate Identity Number U67120MH1996PTC097299) Unit 2901, Level 29 Altimus, Pandurang Budhkar Road, Worli, Mumbai – 400 018. It provides brokerage services bearing SEBI Registration Number: INZ000259830; Merchant Banking services bearing SEBI Registration Number: INM000013101; and Research Analyst services bearing SEBI Registration Number: INH000001204. Name of Compliance Officer Mr Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email : parameshwaran.s@ubs.com, Name of Grievance Officer Parameshwaran Shivaramakrishnan, Phone : +912261556151, Email: ol-ubs-sec-compliance@ubs.com Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. UBS may have debt holdings or positions in the subject Indian company/companies. UBS may have financial interests (e.g. loan/derivative products, rights to or interests in investments, etc.) in the subject Indian company / companies from time to time. Within the past 12 months, UBS may have received compensation for non-investment banking securities-related services and/or non-securities services from the subject Indian company/companies. The subject company/companies may have been a client/clients of UBS during the 12 months preceding the date of distribution of the research report with respect to investment banking and/or non-investment banking securities-related services and/or non-securities services. With regard to information on associates, please refer to the Annual Report at: https://www.ubs.com/global/en/about\_ubs/investor\_relations/annualreporting.html The Research Annual Compliance Report for UBS India Private Limited is available on www.ubs.com/ubssi under Research tab. Taiwan: Except as otherwise specified herein, this material may not be distributed in Taiwan. Information and material on securities/instruments that are traded in a Taiwan organized exchange is deemed to be issued and distributed by UBS Pte. LTD., Taipei Branch to professional institutional investors and/or persons permitted under applicable regulation. Unless permitted by applicable Taiwan laws and regulations, this material is for reference and information only and should not constitute "recommendation" to clients or recipients in Taiwan for the covered companies or any companies mentioned in this document. No portion of the document may be reprinted, reproduced or quoted by the press or any other person without authorisation from UBS. Indonesia: This report is being distributed by PT UBS Sekuritas Indonesia and is delivered by its licensed employee(s), including marketing/sales person, to its client. PT UBS Sekuritas Indonesia, having its registered office at Sequis Tower Level 22 unit 22-1,Jl Jend. Sudirman, kav.71, SCBD lot 11B, Jakarta 12190. Indonesia, is a subsidiary company of UBS AG and licensed under Capital Market Law no. 8 year 1995, a holder of broker-dealer and underwriter licenses issued by the Capital Market and Financial Institution Supervisory Agency (now Otoritas Jasa Keuangan/OJK). PT UBS Sekuritas Indonesia is also a member of Indonesia Stock Exchange and supervised by Otoritas Jasa Keuangan (OJK). Neither this report nor any copy hereof may be distributed in Indonesia or to any Indonesian citizens except in compliance with applicable Indonesian capital market laws and regulations. This report is not an offer of securities in Indonesia and may not be distributed within the territory of the Republic of Indonesia or to Indonesian citizens in circumstance which constitutes an offering within the meaning of Indonesian capital market laws and regulations.

The disclosures contained in research documents produced by UBS AG, London Branch or UBS Europe SE shall be governed by and construed in accordance with English law.

UBS specifically prohibits the redistribution of this document in whole or in part without the written permission of UBS and in any event UBS accepts no liability whatsoever for any redistribution of this document or its contents or the actions of third parties in this respect. Images may depict objects or elements that are protected by third party copyright, trademarks and other intellectual property rights. © UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/b90ab6b3bede5f4164d3ac74bdd1221cdab18403a2094e66aba49de8c2c45565.jpg)
"""
