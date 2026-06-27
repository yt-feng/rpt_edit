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
CENTRAL BANK POLICY TRACKER

June 2026

■ Recent policy changes: Central bank actions have shifted more hawkish due to the war in Iran. In DMs, no central banks lowered and 39% raised rates over the last three months. In EMs, 16% cut rates and 7% raised rates over the same period. But our Global Financial Conditions Index (GS FCI) has eased by 24bp over the last three months, reflecting 34bp of easing in DMs and 10bp of easing in EMs (largely reflecting higher rates). At the country level, financial conditions have eased the most in Türkiye (-117bps), South Korea (-93bps), and Romania (-83bps) and tightened the most in Russia (158bps), Israel (57bps), and Brazil (57bps).

Forecast updates: We have made several policy rate forecast revisions over the last 30 days. In the US, we pushed back the final two rate cuts in our Fed forecast back to June and December of 2027 (vs. December 2026 and March 2027 previously). In Brazil, we raised our end-2026 policy rate forecasts by +75bp to 14.0%, in Hungary we lowered our end-2026 policy rate forecasts by -50bp to 5.25%, and in Taiwan we removed further rate cuts and now forecast a hold at 2% (vs 2.25% previously) through end-2026. In South Korea we raised our end-2027 policy rate forecasts by +25bp to 3.25%.

■ Current forecasts: We forecast that global central banks will lower rates by 0.1pp to $3.1\%$ (on a GDP-weighted basis) over the next four quarters. We expect that DM central banks will increase policy rates by 8bp on average over the next four quarters, reflecting rate hikes in New Zealand (+50bps), Euro Area (+25bps), Sweden (+25bps), Norway (+25bps) and Japan (+25bps) that are partially offset by holds or decreases elsewhere, particularly the US (-25bps through June 2027; -50bp through end-2027) and the UK (-50bps through June 2027; -75bp through end-2027). We expect that EM central banks will cut rates by -33bp on average, reflecting -208bp of cuts in CEEMEA and -35bp in Latin America, with 4bp of hikes in Asia.

■ Forecasts relative to consensus and current pricing: Our end-2026 policy rate forecasts are dovish relative to market pricing (our forecasts are below pricing in 73% of DMs and 57% of EMs; above in 18% of DMs and 43% of EMs). Our forecasts are balanced relative to consensus in both DMs (at least 0.1pp below in 27% vs. at least 0.1pp above in 27%) and EMs (at least 0.1pp below in 32% vs. at least 0.1pp above in 36%).

■ Balance sheet policy: Balance sheets as a share of GDP remain particularly

Jan Hatzius
+1(212)902-0394 | jan.hatzius@gs.com
GS & Co. LLC

Joseph Briggs +1(212)902-2163 | joseph.briggs@gs.com GS & Co. LLC

Sarah Dong
+1(212)357-9741 | sarah.dong@gs.com
GS & Co. LLC

Megan Peters  
+44(20)7051-2058 |  
megan.l.peters@gs.com  
GS International

elevated relative to their 2019 levels in New Zealand (8pp higher) and Australia (4pp). In the US, we see scope for a modest reduction in the Fed's balance sheet size if a reduction in reserve demand warrants an adjustment, but think the bar to a meaningful decline is high.

Exhibit 1: Global Central Banks Have Mostly Either Held or Hiked Over the Last Three Months  
![](images/373cddf35a3da51bcd18ebadbffc66d49ca85718a74e975a586de5cf03a7b165.jpg)  
Source: GS Global Investment Research

![](images/89fa2e88d938d72fde0b9ebe98b7be9e904e5276acacbd6510a38f8527edba56.jpg)

Exhibit 2: We Forecast Further Policy Rate Declines in the UK, US, and Some EMs, but Rate Hikes or Holds in Most DMs Over the Next Four Quarters  
![](images/f4ab4560bbe4cd72ca87a8092fc31a24ac7e8de368158e3759850e8d32d50446.jpg)  
Source: GS Global Investment Research

![](images/4738990b1d685f005f3e677e47e39a1f055c9965bb302ccd98585094f66683ab.jpg)

Exhibit 3: Our End-2026 Policy Rate Forecasts Are Dovish Relative to Market Pricing but Skewed Hawkish Relative to Consensus

<table><tr><td rowspan="4"></td><td colspan="6">End-2026 Policy Rate</td></tr><tr><td colspan="4">Policy Rate Forecasts</td><td colspan="2">vs. GS Forecast</td></tr><tr><td>Latest</td><td>GS</td><td>Consensus</td><td>Market Pricing</td><td>GS - Consensus</td><td>GS - Market Pricing</td></tr><tr><td colspan="4">(%)</td><td colspan="2">(pp)</td></tr><tr><td>Global*</td><td>4.6</td><td>4.7</td><td>4.6</td><td>4.5</td><td>0.0</td><td>0.2</td></tr><tr><td colspan="7">Developed Economies</td></tr><tr><td>US</td><td>3.6</td><td>3.6</td><td>3.1</td><td>4.0</td><td>0.5</td><td>-0.3</td></tr><tr><td>Euro Area</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td><td>0.0</td><td>0.0</td></tr><tr><td>Japan</td><td>1.0</td><td>1.0</td><td>1.3</td><td>1.2</td><td>-0.3</td><td>-0.2</td></tr><tr><td>UK</td><td>3.8</td><td>3.8</td><td>3.9</td><td>4.0</td><td>-0.1</td><td>-0.2</td></tr><tr><td>Canada</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.4</td><td>0.0</td><td>-0.2</td></tr><tr><td>Australia</td><td>4.4</td><td>4.6</td><td>4.4</td><td>4.5</td><td>0.2</td><td>0.1</td></tr><tr><td>Switzerland</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Sweden</td><td>1.8</td><td>2.0</td><td>1.9</td><td>1.9</td><td>0.1</td><td>0.1</td></tr><tr><td>Hong Kong</td><td>2.8</td><td>2.1</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>New Zealand</td><td>2.3</td><td>2.8</td><td>2.6</td><td>2.8</td><td>0.2</td><td>-0.1</td></tr><tr><td colspan="7">Latam</td></tr><tr><td>Brazil</td><td>14.3</td><td>14.0</td><td>13.4</td><td>13.8</td><td>0.6</td><td>0.2</td></tr><tr><td>Mexico</td><td>6.5</td><td>6.5</td><td>6.5</td><td>6.9</td><td>0.0</td><td>-0.4</td></tr><tr><td>Colombia</td><td>11.3</td><td>12.3</td><td>11.9</td><td>11.7</td><td>0.3</td><td>0.6</td></tr><tr><td>Chile</td><td>4.5</td><td>4.5</td><td>4.7</td><td>4.4</td><td>-0.2</td><td>0.1</td></tr><tr><td>Peru</td><td>4.3</td><td>4.3</td><td>4.3</td><td>NA</td><td>-0.1</td><td>NA</td></tr><tr><td colspan="7">CEEMEA</td></tr><tr><td>Russia</td><td>14.3</td><td>12.0</td><td>13.0</td><td>NA</td><td>-0.9</td><td>NA</td></tr><tr><td>Turkiye</td><td>37.0</td><td>37.0</td><td>35.2</td><td>39.4</td><td>1.8</td><td>-2.4</td></tr><tr><td>Poland</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.8</td><td>0.0</td><td>-0.1</td></tr><tr><td>Israel</td><td>3.8</td><td>3.3</td><td>3.6</td><td>3.9</td><td>-0.3</td><td>-0.6</td></tr><tr><td>Egypt</td><td>19.0</td><td>21.0</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>South Africa</td><td>7.0</td><td>7.3</td><td>7.0</td><td>7.3</td><td>0.3</td><td>0.0</td></tr><tr><td>Romania</td><td>6.5</td><td>6.5</td><td>6.3</td><td>NA</td><td>0.2</td><td>NA</td></tr><tr><td>Czech Republic</td><td>3.5</td><td>3.8</td><td>3.6</td><td>4.0</td><td>0.1</td><td>-0.3</td></tr><tr><td>Hungary</td><td>6.0</td><td>5.3</td><td>5.9</td><td>5.0</td><td>-0.7</td><td>0.2</td></tr><tr><td>Ukraine</td><td>15.0</td><td>13.5</td><td>14.2</td><td>NA</td><td>-0.7</td><td>NA</td></tr><tr><td>Ghana</td><td>14.0</td><td>14.0</td><td>13.2</td><td>NA</td><td>0.8</td><td>NA</td></tr><tr><td>Kazakhstan</td><td>17.0</td><td>15.5</td><td>16.2</td><td>NA</td><td>-0.7</td><td>NA</td></tr><tr><td colspan="7">Asia</td></tr><tr><td>Mainland China</td><td>1.4</td><td>1.4</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>India</td><td>5.3</td><td>5.8</td><td>5.5</td><td>5.6</td><td>0.2</td><td>0.1</td></tr><tr><td>South Korea</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.7</td><td>0.0</td><td>-0.7</td></tr><tr><td>Indonesia</td><td>5.8</td><td>5.8</td><td>5.6</td><td>NA</td><td>0.1</td><td>NA</td></tr><tr><td>Taiwan</td><td>2.0</td><td>2.0</td><td>2.1</td><td>1.9</td><td>-0.1</td><td>0.1</td></tr><tr><td>Thailand</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.0</td><td>-0.1</td><td>0.0</td></tr><tr><td>Philippines</td><td>4.8</td><td>5.5</td><td>5.1</td><td>NA</td><td>0.4</td><td>NA</td></tr><tr><td>Vietnam</td><td>4.5</td><td>4.5</td><td>4.9</td><td>NA</td><td>-0.4</td><td>NA</td></tr><tr><td>Malaysia</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>-0.1</td><td>0.0</td></tr></table>

Note: Red shading indicates GS forecast above consensus forecast or market pricing, and blue shading indicates GS forecast below consensus forecast or market pricing.  
\* Global policy rate forecasts represent a GDP-weighted average of the economies with both consensus forecasts and market pricing available.

## Changes in Policy Rates and Financial Conditions

Exhibit 4: Recent Policy Rate Changes  
![](images/676f76fed9545a23c4680abb6a10ee2b639a14bfbbeb165c2716d909211c9d95.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 5: Change in Average Global Policy Rate Over Time  
![](images/6e5d200c7a5bf2025e24a98062e21c06dcbf4bcee39ad717dace078a6aeb8b50.jpg)  
Source: GS Global Investment Research

Exhibit 6: Changes in Financial Conditions Over the Last 3 Months  
![](images/d758405e1cb91ebc80c8b43e6b3d2b681246a1663f25eebe90c8ac89026ceb4a.jpg)  
Source: GS Global Investment Research

Exhibit 7: Changes in Financial Conditions Over the Last 12 Months  
![](images/bafb55e9c723a03f99f34f12ba076d4e618ba50c17f8b0abcaa6a1a4744a8473.jpg)  
Source: GS Global Investment Research

## Policy Rate Forecasts

Exhibit 8: Policy Rate Forecast Revisions in Last 30 Days  
![](images/1ca27c56e1201d4d9fe0111ef88f2a34489691046c0b043d2361b79586b3bbec.jpg)  
Source: GS Global Investment Research

Exhibit 9: GS Forecast Policy Rate Changes  
![](images/a9ad4cef4391e5e57f142b2ea673ea55aa875cdb796d2bf3a9acdc8e99b87b76.jpg)  
Source: GS Global Investment Research

## Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing

![](images/d98816de227dcfa99271195d38a824584831f557c48bb81adb13e0fec9977882.jpg)

![](images/aaa6a715b2b89418eb633b1dfc23d48e667dd48174de28d62ed66c0f636b2e7f.jpg)

![](images/0f7d1b742e1d632be8b95471c80df710b133930cbb675d5c4dfd2cc5c0876181.jpg)

![](images/f4b93b2521f143e2fa7b75becc4598b12a942908a7e0871a7e99aa2dd936def9.jpg)

![](images/949b76bc20780fc8306698217a9254f65d14bf0b952c65f255833d8764894121.jpg)

![](images/cad9580bd436ff322fa70ca7ec4374769c5e8d97a0d0ef1e69fe7efb0d4f4565.jpg)

![](images/2a2b7e9916c4c601011bf0b31dc40ed5d7fc7f76ee19051500e580d83df9ae51.jpg)  
We exclude economies where GS forecasts differ from market pricing and consensus by more than 3pp due to data quality concerns, as well as economies where policy rate forecasts exceed $10\%$ for easier exposition.  
Source: GS Global Investment Research, Bloomberg

Exhibit 12: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing

<table><tr><td rowspan="4"></td><td colspan="7">Year-End Policy Rate, Percent</td></tr><tr><td rowspan="3">Latest</td><td colspan="3">End-2026</td><td colspan="3">End-2027</td></tr><tr><td colspan="3">Policy Rate Forecasts</td><td colspan="3">Policy Rate Forecasts</td></tr><tr><td>GS</td><td>Consensus</td><td>Market Pricing</td><td>GS</td><td>Consensus</td><td>Market Pricing</td></tr><tr><td>Global*</td><td>4.6</td><td>4.7</td><td>4.6</td><td>4.5</td><td>4.0</td><td>4.1</td><td>4.5</td></tr><tr><td colspan="8">Developed Economies</td></tr><tr><td>US</td><td>3.6</td><td>3.6</td><td>3.7</td><td>4.0</td><td>3.1</td><td>3.4</td><td>3.8</td></tr><tr><td>Euro Area</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.0</td><td>2.3</td><td>2.5</td></tr><tr><td>Japan</td><td>1.0</td><td>1.0</td><td>1.3</td><td>1.2</td><td>1.5</td><td>1.5</td><td>1.7</td></tr><tr><td>UK</td><td>3.8</td><td>3.8</td><td>3.9</td><td>4.0</td><td>3.0</td><td>3.3</td><td>3.9</td></tr><tr><td>Canada</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.4</td><td>2.8</td><td>2.8</td><td>2.9</td></tr><tr><td>Australia</td><td>4.4</td><td>4.6</td><td>4.4</td><td>4.5</td><td>3.6</td><td>4.2</td><td>4.2</td></tr><tr><td>Switzerland</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.1</td></tr><tr><td>Sweden</td><td>1.8</td><td>2.0</td><td>1.9</td><td>1.9</td><td>2.3</td><td>2.0</td><td>2.1</td></tr><tr><td>Hong Kong</td><td>2.8</td><td>2.1</td><td>NA</td><td>NA</td><td>1.9</td><td>NA</td><td>NA</td></tr><tr><td>New Zealand</td><td>2.3</td><td>2.8</td><td>2.6</td><td>2.8</td><td>2.8</td><td>3.1</td><td>3.3</td></tr><tr><td colspan="8">Latam</td></tr><tr><td>Brazil</td><td>14.3</td><td>14.0</td><td>13.4</td><td>-0.1</td><td>12.0</td><td>11.5</td><td>0.9</td></tr><tr><td>Mexico</td><td>6.5</td><td>6.5</td><td>6.5</td><td>6.9</td><td>6.5</td><td>6.5</td><td>7.6</td></tr><tr><td>Colombia</td><td>11.3</td><td>12.3</td><td>11.9</td><td>11.7</td><td>11.3</td><td>10.6</td><td>10.1</td></tr><tr><td>Chile</td><td>4.5</td><td>4.5</td><td>4.7</td><td>4.4</td><td>4.3</td><td>4.6</td><td>4.5</td></tr><tr><td>Peru</td><td>4.3</td><td>4.3</td><td>4.3</td><td>NA</td><td>4.3</td><td>4.5</td><td>NA</td></tr><tr><td colspan="8">CEEMEA</td></tr><tr><td>Russia</td><td>14.3</td><td>12.0</td><td>13.0</td><td>NA</td><td>8.0</td><td>9.5</td><td>NA</td></tr><tr><td>Turkiye</td><td>37.0</td><td>37.0</td><td>35.2</td><td>39.4</td><td>29.0</td><td>26.4</td><td>NA</td></tr><tr><td>Poland</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.5</td><td>3.6</td><td>3.8</td></tr><tr><td>Israel</td><td>3.8</td><td>3.3</td><td>3.6</td><td>3.9</td><td>3.3</td><td>3.2</td><td>3.5</td></tr><tr><td>Egypt</td><td>19.0</td><td>21.0</td><td>NA</td><td>NA</td><td>14.0</td><td>NA</td><td>NA</td></tr><tr><td>South Africa</td><td>7.0</td><td>7.3</td><td>7.0</td><td>7.3</td><td>6.5</td><td>6.4</td><td>7.2</td></tr><tr><td>Romania</td><td>6.5</td><td>6.5</td><td>6.3</td><td>NA</td><td>4.5</td><td>5.2</td><td>NA</td></tr><tr><td>Czech Republic</td><td>3.5</td><td>3.8</td><td>3.6</td><td>4.0</td><td>3.0</td><td>3.5</td><td>4.0</td></tr><tr><td>Hungary</td><td>6.0</td><td>5.3</td><td>5.9</td><td>5.0</td><td>4.0</td><td>5.0</td><td>4.7</td></tr><tr><td>Ukraine</td><td>15.0</td><td>13.5</td><td>14.2</td><td>NA</td><td>11.5</td><td>12.3</td><td>NA</td></tr><tr><td>Ghana</td><td>14.0</td><td>14.0</td><td>13.2</td><td>NA</td><td>16.0</td><td>13.3</td><td>NA</td></tr><tr><td>Kazakhstan</td><td>17.0</td><td>15.5</td><td>16.2</td><td>NA</td><td>11.0</td><td>NA</td><td>NA</td></tr><tr><td colspan="8">Asia</td></tr><tr><td>Mainland China</td><td>1.4</td><td>1.4</td><td>NA</td><td>NA</td><td>1.3</td><td>NA</td><td>NA</td></tr><tr><td>India</td><td>5.3</td><td>5.8</td><td>5.5</td><td>5.6</td><td>5.8</td><td>5.6</td><td>6.1</td></tr><tr><td>South Korea</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.7</td><td>3.3</td><td>3.1</td><td>4.0</td></tr><tr><td>Indonesia</td><td>5.8</td><td>5.8</td><td>5.6</td><td>NA</td><td>5.8</td><td>5.2</td><td>NA</td></tr><tr><td>Taiwan</td><td>2.0</td><td>2.0</td><td>2.1</td><td>1.9</td><td>2.0</td><td>2.1</td><td>1.9</td></tr><tr><td>Thailand</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.2</td></tr><tr><td>Philippines</td><td>4.8</td><td>5.5</td><td>5.1</td><td>NA</td><td>5.5</td><td>4.9</td><td>NA</td></tr><tr><td>Vietnam</td><td>4.5</td><td>4.5</td><td>4.9</td><td>NA</td><td>4.5</td><td>4.8</td><td>NA</td></tr><tr><td>Malaysia</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.9</td><td>NA</td></tr></table>

Note: Red shading indicates consensus forecast or market pricing above GS forecast, and blue shading indicates consensus forecast or market pricing below GS forecast.  
\* Global policy rate forecasts represent a GDP-weighted average of the economies with both consensus forecasts and market pricing available.

## Policy Rate Forecast Drivers

Exhibit 13: GS Growth and Policy Rate Forecasts vs. Bloomberg Consensus Forecasts  
![](images/e064bc28aec7076a713383a178bb494cc90649f057c8a98e0905b777304cb602.jpg)  
Source: GS Global Investment Research, Bloomberg

Exhibit 14: GS GDP Growth Forecasts vs. Central Bank and Bloomberg Consensus Forecasts

<table><tr><td rowspan="3"></td><td rowspan="2">End-2025</td><td colspan="6">Real GDP Growth (Annual Average), Per

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
