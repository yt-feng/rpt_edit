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
# Global: GS Economic Indicators Update: Financial Conditions Continue to Ease in South Korea

Please find an update of our proprietary global economic indicators below. The data behind these exhibits can be downloaded here. Interactive charts can be found on our living page here.

## Chart of the Week

Exhibit 1: The South Korea FCI Eased by 29bp Last Week as Tech Continued to Lead an Equity Rally

![](images/9645f958c78d073d585d622875f619d084ff72ab1a097c5db27757c1cc9f063d.jpg)  
Source: GS Global Investment Research

Jan Hatzius
+1(212)902-0394 | jan.hatzius@gs.com
GS & Co. LLC

Joseph Briggs
+1(212)902-2163 |
joseph.briggs@gs.com
GS & Co. LLC

Sarah Dong
+1(212)357-9741 | sarah.dong@gs.com
GS & Co. LLC

Megan Peters
+44(20)7051-2058 |
megan.l.peters@gs.com
GS International

## Key FCI and Growth Charts

Exhibit 2: The Global ex Russia FCI Eased by -0.8bps Last Week Primarily on Equities  
![](images/bc0de9f62121f7f6c18d22bd45d5bd2aa8f3cf7ab58cc0e9705e03a91195de2a.jpg)

![](images/23dcf052b2a26c296866eb8feb334e988f6f7c27d095aab34ff09ef99a69abad.jpg)  
Source: GS Global Investment Research

Exhibit 3: Higher 2026 Growth in South Korea  
![](images/035d44a12e8f66b27bc608eb5940d4e1da3025b8a65d5367da0246df310fde3f.jpg)  
Source: GS Global Investment Research

Exhibit 4: Our Preliminary May CAI Fell by -0.8pp in China and Rose by +0.7pp in Japan

<table><tr><td rowspan="2">Country(% of Data Released)</td><td rowspan="2">Month</td><td colspan="2">Spot CAI(% mom annualized)</td><td rowspan="2">3 Month AverageCAI (% momannualized)</td></tr><tr><td>Value</td><td>Weekly Change</td></tr><tr><td>Global</td><td>May</td><td>+2.9</td><td>-0.1</td><td>+3.0</td></tr><tr><td>Developed Markets</td><td>May</td><td>+2.2</td><td>+0.1</td><td>+2.3</td></tr><tr><td>US (17%)</td><td>June</td><td>+2.6</td><td>+0.2</td><td>+2.7</td></tr><tr><td>Euro Area (40%)</td><td>May</td><td>+1.1</td><td>+0.1</td><td>+1.6</td></tr><tr><td>Germany (50%)</td><td>May</td><td>-0.9</td><td>0.0</td><td>-0.1</td></tr><tr><td>France (38%)</td><td>May</td><td>+0.8</td><td>0.0</td><td>+1.2</td></tr><tr><td>Italy (34%)</td><td>May</td><td>+1.3</td><td>+0.1</td><td>+1.9</td></tr><tr><td>Spain (43%)</td><td>May</td><td>+2.8</td><td>+0.1</td><td>+3.7</td></tr><tr><td>Japan (51%)</td><td>May</td><td>+1.3</td><td>+0.7</td><td>+1.3</td></tr><tr><td>UK (62%)</td><td>May</td><td>0.0</td><td>+0.2</td><td>+0.4</td></tr><tr><td>Canada (33%)</td><td>May</td><td>+2.1</td><td>+0.1</td><td>+2.1</td></tr><tr><td>Australia (58%)</td><td>May</td><td>+1.3</td><td>0.0</td><td>+1.4</td></tr><tr><td>New Zealand (80%)</td><td>May</td><td>+2.0</td><td>-0.1</td><td>+2.3</td></tr><tr><td>Norway (58%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+2.6</td></tr><tr><td>Sweden (80%)</td><td>May</td><td>+2.4</td><td>0.0</td><td>+2.4</td></tr><tr><td>Emerging Markets</td><td>May</td><td>+4.0</td><td>-0.4</td><td>+4.2</td></tr><tr><td>China (80%)</td><td>May</td><td>+4.6</td><td>-0.8</td><td>+4.4</td></tr><tr><td>India (53%)</td><td>May</td><td>+7.5</td><td>+0.1</td><td>+7.3</td></tr><tr><td>Brazil (63%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+3.6</td></tr><tr><td>Russia (37%)</td><td>May</td><td>+0.1</td><td>0.0</td><td>+2.0</td></tr></table>

CAI in countries with 0% of data released is forecasted. CAI aggregates for Global, Developed Markets, and Emerging Markets are GDP-weighted using market FX country weights.  
Source: GS Global Investment Research

Exhibit 5: Our Global CAI Remains Above Potential  
![](images/f5f7e5baebcdd8e0cff9ab7d394ea3f2154d1d4d018ae1a885c4eb6da395e70f.jpg)  
Source: GS Global Investment Research  
GS DM CAI is a market FX-weighted average of the US, Germany, France, Italy, Spain, Japan, the UK, and Canada and EM is of Brazil, Russia, India, and China. Global GS CAI is an average of all aforementioned countries.

## Key Wage and Price Inflation Charts

Exhibit 6: GS Wage Trackers and Inflation Measures  
![](images/b9e973950b7e9ade60eb6cd9bf3dd23265cad3563aea0d4a1cd9334b84855418.jpg)  
US wage tracker is composition-adjusted in 2020 and 2021.  
Source: GS Global Investment Research

Exhibit 7: GS Jobs-Workers Gaps  
![](images/b8d092ae6da7d414f1af8d32e1d3bfe8324c180a586c0a15983f9cc8a37e1cbb.jpg)  
Source: GS Global Investment Research

![](images/0d7044b4702fedb5ab7e9eca2188d2c41d5234c7039ddb65e0fb103d66b41dff.jpg)

## Detailed Indicators Update

## Financial Conditions Index (FCI)

Exhibit 8: GS Global ex Russia FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/e8415475ec6dfef008c5e3a4d9c716929f92ae542edbc5930c10980edb3342bc.jpg)  
Source: GS Global Investment Research

![](images/d1201f815fe4937059893e8ea5756c63982bf2455a5472d569c0ae9cb3433a3d.jpg)

Exhibit 9: GS Global FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/db845992c6e768e420ef64c871b46cd695850845ed1cb5914f56c46d8a89115a.jpg)  
Source: GS Global Investment Research

![](images/fbcbeea8f3ea2a0aa5f31ca97c6420ad83d2eb8a3c359a36b4af1f1eecb85365.jpg)

Exhibit 10: GS US FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/9a83add430c714fe744df442bb094918a5ad017831737a0e8c00380b1750561c.jpg)  
Source: GS Global Investment Research

![](images/8b7038c604604fdd5e1b7ce0019cdec57d4887c55e2aa3eb5b11b6bb213341cd.jpg)

Exhibit 11: GS Euro Area FCI Level (Left) and Weekly Change With Contributions (Right)  
![](images/18be927e28299a1ad963a2c9dbc77a12c2a911ae15d38ecc7a72b19b48b41dc8.jpg)  
Source: GS Global Investment Research

![](images/6a2d81d3665fc3ce0a9390c9542bafa91ea93d860c73e4771ff9a8839ca05c2f.jpg)

Exhibit 12: Weekly Change in FCI Across Countries  
![](images/b1ade29adf48bb65f513e402af7db8e4669ce15e9e533eafd9b09ea7c1b518c8.jpg)  
Source: GS Global Investment Research

Exhibit 13: Year-Over-Year Change in FCI Across Countries  
![](images/eaf2fde19055a84a2f91388bb9fa2b34af857aa05de47125c8eb6f6ba17eb7b8.jpg)  
Source: GS Global Investment Research

FCI Impulses  
Exhibit 14: FCI Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right)  
![](images/48a46232ad7ecef9af27a453dff974b18bb34022a4e6908b5d9d20c7dc650426.jpg)  
Source: GS Global Investment Research

Exhibit 15: FCI Impulses in the US, Euro Area, Japan, and UK  
![](images/19a40d88f2abb9d55f016f358eb065d02ecb42260b5563390b1626d9a04fa5c4.jpg)  
Source: GS Global Investment Research

Current Activity Indicator (CAI)  
Exhibit 16: CAI Aggregates  
![](images/5c6aff77a609d953ba6ad2c15311196f826d3dcd33899374769c75fee5611c6e.jpg)

![](images/78cc733320cafa61a01d5436872106eba3b22fa14d78be2e391deae5961d5d03.jpg)  
GS DM CAI is a market FX-weighted average of the US, Germany, France, Italy, Spain, Japan, the UK, and Canada and EM is of Brazil, Russia, India, and China. Global GS CAI is an average of all aforementioned countries.  
Source: GS Global Investment Research

Exhibit 17: CAI Heatmap

<table><tr><td rowspan="2">Country(% of Data Released)</td><td rowspan="2">Month</td><td colspan="2">Spot CAI(% mom annualized)</td><td rowspan="2">3 Month AverageCAI (% momannualized)</td></tr><tr><td>Value</td><td>Weekly Change</td></tr><tr><td>Global</td><td>May</td><td>+2.9</td><td>-0.1</td><td>+3.0</td></tr><tr><td>Developed Markets</td><td>May</td><td>+2.2</td><td>+0.1</td><td>+2.3</td></tr><tr><td>US (17%)</td><td>June</td><td>+2.6</td><td>+0.2</td><td>+2.7</td></tr><tr><td>Euro Area (40%)</td><td>May</td><td>+1.1</td><td>+0.1</td><td>+1.6</td></tr><tr><td>Germany (50%)</td><td>May</td><td>-0.9</td><td>0.0</td><td>-0.1</td></tr><tr><td>France (38%)</td><td>May</td><td>+0.8</td><td>0.0</td><td>+1.2</td></tr><tr><td>Italy (34%)</td><td>May</td><td>+1.3</td><td>+0.1</td><td>+1.9</td></tr><tr><td>Spain (43%)</td><td>May</td><td>+2.8</td><td>+0.1</td><td>+3.7</td></tr><tr><td>Japan (51%)</td><td>May</td><td>+1.3</td><td>+0.7</td><td>+1.3</td></tr><tr><td>UK (62%)</td><td>May</td><td>0.0</td><td>+0.2</td><td>+0.4</td></tr><tr><td>Canada (33%)</td><td>May</td><td>+2.1</td><td>+0.1</td><td>+2.1</td></tr><tr><td>Australia (58%)</td><td>May</td><td>+1.3</td><td>0.0</td><td>+1.4</td></tr><tr><td>New Zealand (80%)</td><td>May</td><td>+2.0</td><td>-0.1</td><td>+2.3</td></tr><tr><td>Norway (58%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+2.6</td></tr><tr><td>Sweden (80%)</td><td>May</td><td>+2.4</td><td>0.0</td><td>+2.4</td></tr><tr><td>Emerging Markets</td><td>May</td><td>+4.0</td><td>-0.4</td><td>+4.2</td></tr><tr><td>China (80%)</td><td>May</td><td>+4.6</td><td>-0.8</td><td>+4.4</td></tr><tr><td>India (53%)</td><td>May</td><td>+7.5</td><td>+0.1</td><td>+7.3</td></tr><tr><td>Brazil (63%)</td><td>May</td><td>+2.1</td><td>0.0</td><td>+3.6</td></tr><tr><td>Russia (37%)</td><td>May</td><td>+0.1</td><td>0.0</td><td>+2.0</td></tr></table>

CAI in countries with 0% of data released is forecasted. CAI aggregates for Global, Developed Markets, and Emerging Markets are GDP-weighted using market FX country weights.  
Source: GS Global Investment Research

Exhibit 18: CAIs for Large DMs and EMs  
![](images/04f0caa84f5735f1f970a1c06867c8592b48b2a0995e18d34f63bfbf43676023.jpg)  
Source: GS Global Investment Research

![](images/c5bc23331413f89d59d02c9956677c13d9d87c2dd28870cedc01cacf7ecd8305.jpg)

MAP  
Exhibit 19: GS MAP Surprise Index  
![](images/f06099127306e567faa9972f4f273ebe8e9c9b96d2c24c5cd8574b94395be472.jpg)  
We present the 21-day moving average of daily MAP scores.

![](images/0da6f3e7e369929c869b8a6225940190c6d37d8c46020690383487aee63dedae.jpg)  
Source: GS Global Investment Research

![](images/4f199dfbfb7b088d0ff0084f16f04ff63dff650a0a4a4662dfdb33842619961f.jpg)  
We present the 21 day moving average of daily MAP scores.  
Source: GS Global Investment Research

## Trimmed Core Inflation

Exhibit 21: GS Trimmed Core Inflation  
![](images/4938e35ad1a79610f25c535c1cc9042b7a68cd0c4fd581900452e1eb46f50cc3.jpg)  
Source: GS Global Investment Research

## Wage Trackers

Exhibit 22: GS Wage Trackers  
![](images/3e1fe99f8789bb4aaf546d99d33d4003323b2ebdaa77ab0f4268a88498e5db5d.jpg)  
Source: GS Global Investment Research

Exhibit 23: GS Sequential Wage Trackers  
![](images/9fe84538751267f9816f9117509c5b69acb6c1c6ded882ed25c292c54be48c6b.jpg)

![](images/d2987a948443abfd0cd8b449a4056991e41e267d6a51bdb1857f90485edd6a1d.jpg)

![](images/05b29f1d96a54bae73f3eb3ec9c329dce87b9a87553680b1849754be23d4dfc0.jpg)

![](images/47fcd5a344bee27c4d5135f910cbfe7350b015b79a9d27f00738e0bd9f42fee3.jpg)

![](images/a58b9c040c30a1daaad72a42b54ccdc47f40bf1d9a4a046c7145084a629184d4.jpg)  
Source: GS Global Investment Research

![](images/e73fc166e79a3b5c4a64a23bfe78c70c90871c816cc330bfb2a1fee257095194.jpg)

Exhibit 24: GS Jobs-Workers Gaps  
![](images/113504d880384e4228f88c10ede1484f9efcacb9d1b3e61deeaa82f0aa97c4df.jpg)

![](images/5cd7e3dfde384702b652cdb435c95ad13d7a5f03782782af7bd89c53aaa32237.jpg)

Source: GS Global Investment Research  
Exhibit 25: Wage Survey Leading Indicators  
![](images/8c7cd06c29e9d8a1a15f4fe6f80b7ada6aa5efc55e250445178a8baef66197b6.jpg)  
Source: GS Global Investment Research

![](images/bb59ef6a29618f0b3a969e4353f0495bf0b3b8595c34dffedeb3af823393f03c.jpg)

## Top-Down Fiscal Impulses

Exhibit 26: Top-Down Fiscal Impulses Over the Next 4 Quarters (Left) and in the Euro Area, UK, and US (Right)  
![](images/11fae9f258e6a536d4a7cea5d1d1990c8c010bb6dd5669fc080ee3002c28597e.jpg)  
We compute the 4-quarter measure using average fiscal growth impulses from 2026Q1 to 2026Q4. The US impulse captures both expansionary fiscal discretionary policy and the tax-like effects of tariffs.  
Source: GS Global Investment Research

## Exhibit 27: Top-Down Fiscal Impulses in the US, Euro Area, China, and UK

![](images/99e3318742d0568109a951d7b0e7e0065ccf5d6dca62345fc34c67ae90b7f038.jpg)  
Source: GS Global Investment Research  
The US impulse captures both expansionary fiscal discretionary policy and the tax-like effects of tariffs.

Output Gaps  
Exhibit 28: Latest Short-Run Utilization Scores

<table><tr><td rowspan="2">Country</td><td rowspan="2">Month</td><td colspan="2">Spot Short-Run Utilization Scores (% of Potential)</td><td rowspan="2">3 Month Average (% of Potential)</td></tr><tr><td>Value</td><td>Weekly Change</td></tr><tr><td>US</td><td>June</td><td>-1.8</td><td>+0.1</td><td>-1.9</td></tr><tr><td>Germany</td><td>June</td><td>+0.5</td><td>0.0</td><td>+0.5</td></tr><tr><td>France</td><td>June</td><td>+0.9</td><td>+0.1</td><td>+0.9</td></tr><tr><td>Italy</td><td>June</td><td>+6.5</td><td>0.0</td><td>+6.5</td></tr><tr><td>Spain</td><td>June</td><td>+5.6</td><td>+0.4</td><td>+5.1</td></tr><tr><td>Japan</td><td>April</td><td>-0.2</td><td>0.0</td><td>-0.5</td></tr><tr><td>UK</td><td>June</td><td>-1.4</td><td>+0.1</td><td>-1.2</td></tr><tr><td>Canada</td><td>May</td><td>-0.8</td><td>0.0</td><td>-1.0</td></tr><tr><td>Australia</td><td>May</td><td>+0.1</td><td>-0.1</td><td>+0.2</td></tr><tr><td>China</td><td>May</td><td>-0.1</td><td>+0.1</td><td>-0.1</td></tr><tr><td>India</td><td>May</td><td>+0.3</td><td>0.0</td><td>+0.2</td></tr><tr><td>Brazil</td><td>April</td><td>+0.7</td><td>0.0</td><td>+0.6</td></tr><tr><td>Russia</td><td>May</td><td>+1.3</td><td>0.0</td><td>+1.3</td></tr></table>

Source: GS Global Investment Research

Exhibit 29: Short-Run Utilization Scores  
![](images/eeeeb1997a7888dd2d7913a1caac205d798b4e7e975b98d70d55351165a466d2.jpg)  
Source: GS Global Investment Research

## GS Forecasts vs. Consensus

Exhibit 30: Change in GS 2026 Inflation Forecasts  
![](images/db05c6b75b109696fd5ebc9db09cfa119378ae92c85370029671d3a97af8ad0e.jpg)  
Source: GS Global Investment Research

## Exhibit 31: Change in GS 2027 Inflation Forecasts

![](images/afb9dd8575e2f5233e06ee5ebcee8c5f3e8bd6b3a257975560fdd73b0946c41b.jpg)  
Source: GS Global Investment Research

Exhibit 32: Change in GS 2026 GDP Forecasts  
![](images/6d286f9d7d4f9b1a18c11a9ecb7f13e07a3b2ec277b0dd3dc786cb166f87a5e3.jpg)  
Source: GS Global Investment Research

## Exhibit 33: Change in GS 2027 GDP Forecasts

![](images/ec0a5eeba7ebfb2f9cad72e401cf52937426508199d405bd05d64c5ee2faf8ca.jpg)  
Source: GS Global Investment Research

## Exhibit 34: GS 2026 Global GDP Forecasts vs. Other Forecasters

![](images/4a1ab462532bb16e10404a10ca4026c05d5a4e1acddc6166ff78c7c5ad95867d.jpg)  
Source: Bloomberg, GS Global Investment Research

Exhibit 35: GS 2027 Global GDP Forecasts vs. Other Forecasters  
![](images/080377932f613932d4c6d761808795fa9fbb946cbbd212113a9399411deb2958.jpg)  
Source: Bloomberg, GS Global Investment Research

Thank you to Jamal Lawal, intern on the Global Economics team, for his contributions to this report.

## Methodology Notes for GS Proprietary Economic Indicators

1. Financial Conditions: Our Financial Conditions Indexes are designed to gauge the overall looseness or tightness of financial conditions across the world's major economies. The GSFCIs can provide valuable information about the GDP growth outlook, the transmission of monetary policy to the real economy, and the importance of financial shocks hitting the economy. (Latest methodology notes here and here.)

2. FCI Impulses: Our FCI impulses measure the effect of financial conditions on real GDP growth. For details on the methodology please see here.

3. Current Activity Indicator: In statistical jargon, the CAIs are the “first principal component” of several real activity indicators, expressed in GDP-equivalent units. The CAIs can be interpreted as the growth signal in the main high-frequency indicators for each economy. At any given point, data for certain indicators may not be available. The CAIs therefore incorporate forecasted values for missing indicators, which are then replaced with actual values when they are released. (Latest methodology note here.)

4. MAP Surprise Index: Our daily MAP surprise indices summarize the importance and strength (relative to consensus e

[中间内容因长度限制已省略]

attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
