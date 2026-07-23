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
MS & CO. LLC
Brian Nowak, CFA
Equity Analyst
Brian.Nowak@morganstanley.com +1 212 761-3365
Matthew Cost
Equity Analyst
Matthew.Cost@morganstanley.com +1 212 761-7252
Nathan Feather
Equity Analyst
Nathan.Feather@morganstanley.com +1 212 761-9812
Julian Herrera
Research Associate
Julian.Herrera@morganstanley.com +1 212 761-1784
Gregory Gao
Research Associate
Greg.Gao@morganstanley.com +1 212 296-3125
Kavya A Narayanan
Research Associate
Kavya.Narayanan@morganstanley.com +1 212 761-4183
Nikhil Javeri
Research Associate
Nikhil.Javeri1@morganstanley.com +1 212 761-3742
Cela VanLieshout
Research Associate
Cela.Vanlieshout1@morganstanley.com +1 212 761-2679

Internet | North America

# Where Are We Trading Now: Entering 2Q Earnings

Internet names fell -4% (SPX/NDX -2/-4%) led by META/GOOGL both -3% while AMZN +1%. APP -16%, and RDDT-7%, and SNAP -3%. AMZN/GOOGL/META 26X/23X/20X '26 EPS (-17%/-11%/-16% vs TTM avg).

## INTERNET

## Comp Sheet

Exhibit 1: Internet Comp Sheet: North America

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">FactSet Ticker</td><td rowspan="2">MW Ticker</td><td rowspan="2">Price 7/17/2026</td><td rowspan="2">Mkt Cap ($ MM)</td><td rowspan="2">EV ($ MM)</td><td colspan="2">EV/Rev</td><td colspan="2">EV/GP</td><td colspan="2">EV/EBITDA</td><td colspan="2">FCF Yield</td><td colspan="2">EPS</td><td colspan="2">P/E</td><td rowspan="2">Short Interest</td></tr><tr><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td><td>2026E</td><td>2027E</td></tr><tr><td colspan="19">Digital Media</td></tr><tr><td>BMBL</td><td>BMBL-US</td><td>BMBL.O</td><td>$2.92</td><td>479</td><td>821</td><td>1.0x</td><td>1.0x</td><td>1.3x</td><td>1.4x</td><td>3.1x</td><td>3.5x</td><td>46.9%</td><td>29.3%</td><td>0.78</td><td>0.61</td><td>3.7x</td><td>4.8x</td><td>14.0%</td></tr><tr><td>CRTO</td><td>CRTO-US</td><td>CRTO.O</td><td>$22.48</td><td>1,146</td><td>987</td><td>0.9x</td><td>0.8x</td><td>0.9x</td><td>0.9x</td><td>2.6x</td><td>2.5x</td><td>11.3%</td><td>13.6%</td><td>4.24</td><td>4.97</td><td>5.3x</td><td>4.5x</td><td>1.9%</td></tr><tr><td>DUOL</td><td>DUOL-US</td><td>DUOL.O</td><td>$133.85</td><td>6,536</td><td>5,284</td><td>4.3x</td><td>3.8x</td><td>6.0x</td><td>5.4x</td><td>16.6x</td><td>13.8x</td><td>5.8%</td><td>5.8%</td><td>2.73</td><td>3.16</td><td>49.0x</td><td>42.4x</td><td>18.8%</td></tr><tr><td>DV</td><td>DV-US</td><td>DV.N</td><td>$11.42</td><td>1,874</td><td>1,700</td><td>2.1x</td><td>1.9x</td><td>2.5x</td><td>2.3x</td><td>6.1x</td><td>5.5x</td><td>10.2%</td><td>10.6%</td><td>0.62</td><td>0.76</td><td>18.4x</td><td>15.0x</td><td>9.9%</td></tr><tr><td>GOOGL</td><td>GOOGL-US</td><td>GOOGL.O</td><td>$346.77</td><td>4,243,771</td><td>4,087,486</td><td>8.2x</td><td>6.3x</td><td>13.4x</td><td>10.4x</td><td>16.7x</td><td>11.8x</td><td>0.5%</td><td>NM</td><td>14.80</td><td>16.30</td><td>23.4x</td><td>21.3x</td><td>1.5%</td></tr><tr><td>GRND</td><td>GRND-US</td><td>GRND.N</td><td>$15.26</td><td>2,824</td><td>3,192</td><td>5.9x</td><td>5.0x</td><td>7.9x</td><td>6.7x</td><td>13.7x</td><td>11.9x</td><td>5.2%</td><td>6.4%</td><td>0.57</td><td>0.67</td><td>26.7x</td><td>22.8x</td><td>27.0%</td></tr><tr><td>META</td><td>META-US</td><td>META.O</td><td>$646.01</td><td>1,656,370</td><td>1,633,938</td><td>6.4x</td><td>5.3x</td><td>8.7x</td><td>7.6x</td><td>11.0x</td><td>8.7x</td><td>0.7%</td><td>NM</td><td>32.49</td><td>32.99</td><td>19.9x</td><td>19.6x</td><td>1.6%</td></tr><tr><td>MNTN</td><td>MNTN-US</td><td>MNTN.N</td><td>$8.94</td><td>705</td><td>491</td><td>1.4x</td><td>1.2x</td><td>1.8x</td><td>1.5x</td><td>4.9x</td><td>4.0x</td><td>NA</td><td>NA</td><td>1.06</td><td>1.08</td><td>8.4x</td><td>8.3x</td><td>14.2%</td></tr><tr><td>MTCH</td><td>MTCH-US</td><td>MTCH.O</td><td>$39.15</td><td>9,841</td><td>12,791</td><td>3.7x</td><td>3.6x</td><td>4.9x</td><td>4.7x</td><td>9.6x</td><td>9.1x</td><td>9.7%</td><td>9.9%</td><td>2.61</td><td>3.14</td><td>15.0x</td><td>12.5x</td><td>5.4%</td></tr><tr><td>PINS</td><td>PINS-US</td><td>PINS.N</td><td>$23.20</td><td>15,716</td><td>15,998</td><td>3.3x</td><td>2.9x</td><td>4.2x</td><td>3.7x</td><td>11.3x</td><td>10.1x</td><td>8.1%</td><td>9.3%</td><td>0.59</td><td>0.70</td><td>39.2x</td><td>33.2x</td><td>12.6%</td></tr><tr><td>RDDT</td><td>RDDT-US</td><td>RDDT.N</td><td>$181.18</td><td>36,693</td><td>33,923</td><td>10.0x</td><td>7.4x</td><td>10.9x</td><td>8.0x</td><td>22.1x</td><td>15.4x</td><td>3.3%</td><td>4.7%</td><td>6.86</td><td>9.10</td><td>26.4x</td><td>19.9x</td><td>12.4%</td></tr><tr><td>SNAP</td><td>SNAP-US</td><td>SNAP.N</td><td>$4.53</td><td>8,548</td><td>9,214</td><td>1.4x</td><td>1.2x</td><td>2.3x</td><td>2.0x</td><td>6.7x</td><td>5.2x</td><td>7.5%</td><td>13.4%</td><td>(0.07)</td><td>0.17</td><td>NM</td><td>26.1x</td><td>10.6%</td></tr><tr><td>SPCX</td><td>SPCX-US</td><td>SPCX.O</td><td>$123.99</td><td>1,471,982</td><td>1,486,395</td><td>33.1x</td><td>16.3x</td><td>53.7x</td><td>26.0x</td><td>68.5x</td><td>26.1x</td><td>NM</td><td>NM</td><td>0.28</td><td>2.18</td><td>437.9x</td><td>56.8x</td><td>17.4%</td></tr><tr><td>SSTK</td><td>SSTK-US</td><td>SSTK.N</td><td>$7.41</td><td>272</td><td>383</td><td>0.5x</td><td>0.5x</td><td>0.9x</td><td>0.9x</td><td>2.6x</td><td>2.9x</td><td>6.8%</td><td>NM</td><td>(1.02)</td><td>0.49</td><td>NM</td><td>15.2x</td><td>4.6%</td></tr><tr><td>TTD</td><td>TTD-US</td><td>TTD.O</td><td>$18.59</td><td>8,865</td><td>7,987</td><td>2.5x</td><td>2.3x</td><td>3.2x</td><td>2.9x</td><td>6.2x</td><td>5.7x</td><td>10.4%</td><td>11.9%</td><td>2.02</td><td>2.21</td><td>9.2x</td><td>8.4x</td><td>18.4%</td></tr><tr><td>YELP</td><td>YELP-US</td><td>YELP.N</td><td>$26.22</td><td>1,684</td><td>1,350</td><td>0.9x</td><td>0.9x</td><td>1.0x</td><td>1.0x</td><td>4.4x</td><td>4.2x</td><td>13.6%</td><td>14.9%</td><td>2.11</td><td>2.13</td><td>12.4x</td><td>12.3x</td><td>16.5%</td></tr><tr><td colspan="4">Digital Media Med.</td><td>8,548</td><td>7,987</td><td>3.3x</td><td>2.9x</td><td>4.2x</td><td>3.7x</td><td>9.6x</td><td>8.7x</td><td>7.5%</td><td>10.3%</td><td>$1.06</td><td>$2.18</td><td>19.9x</td><td>19.6x</td><td>11.5%</td></tr><tr><td colspan="19">eCommerce/Marketplace</td></tr><tr><td>AMZN</td><td>AMZN-US</td><td>AMZN.O</td><td>$247.23</td><td>2,688,379</td><td>2,664,364</td><td>3.2x</td><td>2.8x</td><td>6.2x</td><td>5.1x</td><td>11.9x</td><td>8.8x</td><td>NM</td><td>1.4%</td><td>9.59</td><td>11.53</td><td>25.8x</td><td>21.4x</td><td>1.0%</td></tr><tr><td>CHWY</td><td>CHWY-US</td><td>CHWY.N</td><td>$20.93</td><td>8,772</td><td>8,252</td><td>0.6x</td><td>0.6x</td><td>2.0x</td><td>1.9x</td><td>9.1x</td><td>7.6x</td><td>0.4%</td><td>0.1%</td><td>1.52</td><td>1.82</td><td>13.7x</td><td>11.5x</td><td>10.9%</td></tr><tr><td>EBAY</td><td>EBAY-US</td><td>EBAY.O</td><td>$112.06</td><td>51,211</td><td>52,559</td><td>4.3x</td><td>4.0x</td><td>5.8x</td><td>5.4x</td><td>14.1x</td><td>12.6x</td><td>5.9%</td><td>6.3%</td><td>6.03</td><td>6.76</td><td>18.6x</td><td>16.6x</td><td>3.4%</td></tr><tr><td>ETSY</td><td>ETSY-US</td><td>ETSY.O</td><td>$84.10</td><td>10,179</td><td>9,225</td><td>3.3x</td><td>3.2x</td><td>4.5x</td><td>4.4x</td><td>11.2x</td><td>10.9x</td><td>7.1%</td><td>6.7%</td><td>3.71</td><td>4.40</td><td>22.7x</td><td>19.1x</td><td>13.4%</td></tr><tr><td>FIGS</td><td>FIGS-US</td><td>FIGS.N</td><td>$10.31</td><td>2,022</td><td>1,717</td><td>2.3x</td><td>2.2x</td><td>3.5x</td><td>3.3x</td><td>17.9x</td><td>14.3x</td><td>5.8%</td><td>7.1%</td><td>0.24</td><td>0.31</td><td>43.8x</td><td>33.0x</td><td>11.6%</td></tr><tr><td>PTON</td><td>PTON-US</td><td>PTON.O</td><td>$6.12</td><td>2,829</td><td>1,668</td><td>0.7x</td><td>0.7x</td><td>1.3x</td><td>1.3x</td><td>3.5x</td><td>3.4x</td><td>18.3%</td><td>17.0%</td><td>0.12</td><td>0.27</td><td>49.2x</td><td>22.4x</td><td>15.3%</td></tr><tr><td>RVLV</td><td>RVLV-US</td><td>RVLV.N</td><td>$24.88</td><td>1,798</td><td>1,462</td><td>1.1x</td><td>1.0x</td><td>2.0x</td><td>1.8x</td><td>15.5x</td><td>10.9x</td><td>5.0%</td><td>5.3%</td><td>0.83</td><td>1.18</td><td>30.1x</td><td>21.1x</td><td>11.9%</td></tr><tr><td>WW</td><td>WW-US</td><td>WW.N</td><td>$14.57</td><td>146</td><td>611</td><td>1.0x</td><td>1.0x</td><td>1.3x</td><td>1.4x</td><td>5.7x</td><td>6.0x</td><td>20.5%</td><td>23.8%</td><td>(4.68)</td><td>(0.90)</td><td>NM</td><td>NM</td><td>21.7%</td></tr><tr><td colspan="4">eCommerce Med.</td><td>2,829</td><td>1,717</td><td>1.1x</td><td>1.0x</td><td>2.0x</td><td>1.9x</td><td>11.2x</td><td>8.8x</td><td>5.9%</td><td>6.7%</td><td>$1.52</td><td>$1.18</td><td>24.2x</td><td>21.1x</td><td>11.9%</td></tr><tr><td colspan="19">Shared Economy/Rideshare</td></tr><tr><td>CART</td><td>CART-US</td><td>CART.O</td><td>$45.82</td><td>11,620</td><td>11,128</td><td>2.7x</td><td>2.4x</td><td>3.6x</td><td>3.3x</td><td>8.7x</td><td>7.5x</td><td>8.4%</td><td>10.4%</td><td>2.62</td><td>3.48</td><td>17.5x</td><td>13.2x</td><td>10.5%</td></tr><tr><td>DASH</td><td>DASH-US</td><td>DASH.O</td><td>$184.14</td><td>81,942</td><td>76,409</td><td>4.3x</td><td>3.6x</td><td>8.5x</td><td>6.9x</td><td>21.4x</td><td>15.9x</td><td>3.2%</td><td>4.6%</td><td>2.28</td><td>4.04</td><td>80.9x</td><td>45.5x</td><td>5.7%</td></tr><tr><td>LYFT</td><td>LYFT-US</td><td>LYFT.O</td><td>$15.52</td><td>6,245</td><td>5,411</td><td>0.8x</td><td>0.7x</td><td>1.7x</td><td>1.5x</td><td>8.1x</td><td>6.8x</td><td>21.2%</td><td>22.0%</td><td>0.67</td><td>1.01</td><td>23.3x</td><td>15.3x</td><td>25.3%</td></tr><tr><td>UBER</td><td>UBER-US</td><td>UBER.N</td><td>$72.46</td><td>150,093</td><td>153,836</td><td>2.7x</td><td>2.3x</td><td>6.0x</td><td>5.1x</td><td>13.5x</td><td>10.8x</td><td>NM</td><td>NM</td><td>3.38</td><td>4.40</td><td>21.4x</td><td>16.5x</td><td>2.9%</td></tr><tr><td colspan="4">Shared Economy Med.</td><td>46,781</td><td>43,769</td><td>2.7x</td><td>2.3x</td><td>4.8x</td><td>4.2x</td><td>11.1x</td><td>9.2x</td><td>8.4%</td><td>10.4%</td><td>$2.45</td><td>$3.76</td><td>22.4x</td><td>15.9x</td><td>8.1%</td></tr><tr><td colspan="19">Gaming/Mobile App</td></tr><tr><td>APP</td><td>APP-US</td><td>APP.O</td><td>$424.54</td><td>143,804</td><td>144,559</td><td>17.4x</td><td>13.9x</td><td>19.3x</td><td>15.3x</td><td>20.8x</td><td>16.5x</td><td>4.0%</td><td>4.9%</td><td>15.24</td><td>19.75</td><td>27.9x</td><td>21.5x</td><td>4.7%</td></tr><tr><td>EA</td><td>EA-US</td><td>EA.O</td><td>$208.90</td><td>53,061</td><td>51,566</td><td>6.1x</td><td>5.4x</td><td>7.3x</td><td>6.4x</td><td>17.3x</td><td>13.9x</td><td>1.3%</td><td>4.5%</td><td>9.08</td><td>11.38</td><td>23.0x</td><td>18.4x</td><td>4.2%</td></tr><tr><td>LFTO</td><td>LFTO-US</td><td>LFTO.O</td><td>$22.61</td><td>4,201</td><td>5,816</td><td>6.8x</td><td>5.9x</td><td>7.9x</td><td>6.8x</td><td>12.0x</td><td>10.0x</td><td>6.4%</td><td>5.9%</td><td>0.16</td><td>1.23</td><td>141.3x</td><td>18.4x</td><td>5.9%</td></tr><tr><td>PLTK</td><td>PLTK-US</td><td>PLTK.O</td><td>$4.02</td><td>1,482</td><td>3,420</td><td>1.2x</td><td>1.2x</td><td>1.6x</td><td>1.6x</td><td>4.6x</td><td>4.5x</td><td>2.8%</td><td>18.3%</td><td>0.48</td><td>0.68</td><td>8.4x</td><td>5.9x</td><td>10.3%</td></tr><tr><td>RBLX</td><td>RBLX-US</td><td>RBLX.N</td><td>$51.68</td><td>38,502</td><td>36,311</td><td>5.8x</td><td>4.7x</td><td>7.1x</td><td>5.7x</td><td>21.2x</td><td>17.1x</td><td>3.5%</td><td>4.0%</td><td>(1.35)</td><td>(0.83)</td><td>NM</td><td>NM</td><td>4.7%</td></tr><tr><td>TTWO</td><td>TTWO-US</td><td>TTWO.O</td><td>$236.68</td><td>43,781</td><td>44,267</td><td>6.3x</td><td>4.8x</td><td>10.7x</td><td>6.9x</td><td>29.3x</td><td>15.8x</td><td>3.1%</td><td>4.3%</td><td>6.00</td><td>11.40</td><td>39.4x</td><td>20.8x</td><td>5.0%</td></tr><tr><td>U</td><td>U-US</td><td>U.N</td><td>$28.99</td><td>14,567</td><td>14,370</td><td>6.8x</td><td>5.8x</td><td>9.5x</td><td>6.7x</td><td>23.9x</td><td>19.4x</td><td>NM</td><td>2.0%</td><td>(0.90)</td><td>0.65</td><td>NM</td><td>44.6x</td><td>9.7%</td></tr><tr><td colspan="4">Video Game Med.</td><td>38,502</td><td>36,311</td><td>6.3x</td><td>5.4x</td><td>7.9x</td><td>6.7x</td><td>20.8x</td><td>15.8x</td><td>3.3%</td><td>4.5%</td><td>$0.48</td><td>$1.23</td><td>27.9x</td><td>19.6x</td><td>5.0%</td></tr><tr><td colspan="19">Travel</td></tr><tr><td>ABNB</td><td>ABNB-US</td><td>ABNB.O</td><td>$145.98</td><td>93,573</td><td>84,043</td><td>6.0x</td><td>5.6x</td><td>7.2x</td><td>6.7x</td><td>17.2x</td><td>16.0x</td><td>5.9%</td><td>6.1%</td><td>4.85</td><td>5.35</td><td>30.1x</td><td>27.3x</td><td>3.7%</td></tr><tr><td>EXPE</td><td>EXPE-US</td><td>EXPE.O</td><td>$268.77</td><td>33,588</td><td>35,215</td><td>2.2x</td><td>2.0x</td><td>2.4x</td><td>2.2x</td><td>8.4x</td><td>7.5x</td><td>11.0%</td><td>11.7%</td><td>20.39</td><td>23.40</td><td>13.2x</td><td>11.5x</td><td>8.2%</td></tr><tr><td>BKNG</td><td>BKNG-US</td><td>BKNG.O</td><td>$181.68</td><td>144,254</td><td>143,628</td><td>4.9x</td><td>4.5x</td><td>4.9x</td><td>4.5x</td><td>12.3x</td><td>11.1x</td><td>6.3%</td><td>7.0%</td><td>10.29</td><td>12.12</td><td>17.7x</td><td>15.0x</td><td>3.8%</td></tr><tr><td colspan="4">Travel Avg.</td><td>90,472</td><td>87,629</td><td>4.3x</td><td>4.0x</td><td>4.8x</td><td>4.5x</td><td>12.6x</td><td>11.5x</td><td>7.7%</td><td>8.3%</td><td>$11.84</td><td>$13.62</td><td>20.3x</td><td>17.9x</td><td>5.2%</td></tr><tr><td colspan="19">Real Estate Tech</td></tr><tr><td>COMP</td><td colspan="2">COMP.EQ-ICOMP.N</td><td>$12.00</td><td>9,881</td><td>12,693</td><td>0.9x</td><td>0.9x</td><td>NA</td><td>NA</td><td>15.2x</td><td>11.0x</td><td>0.0%</td><td>0.0%</td><td>0.36</td><td>0.55</td><td>33.0x</td><td>21.7x</td><td>7.5%</td></tr><tr><td>Z</td><td colspan="2">Z-US Z.O</td><td>$33.91</td><td>8,125</td><td>7,677</td><td>2.6x</td><td>2.3x</td><td>3.5x</td><td>3.2x</td><td>9.9x</td><td>8.1x</td><td>8.0%</td><td>9.0%</td><td>2.12</td><td>2.58</td><td>16.0x</td><td>13.1x</td><td>9.0%</td></tr><tr><td>OPEN</td><td colspan="2">OPEN-US OPEN.O</td><td>$4.50</td><td>3,121 3,159 7,042 7,843 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,841 9,</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: Company data, MS estimates

Exhibit 2: Digital Ads vs. Travel/Shared Economy 1-Week Price Performance

<table><tr><td></td><td>Market Cap ($mn)</td><td>1 Week Performance</td></tr><tr><td colspan="3">Digital Ads</td></tr><tr><td>GOOGL</td><td>$4,243,771</td><td>-2.9%</td></tr><tr><td>META</td><td>$1,656,370</td><td>-3.5%</td></tr><tr><td>SNAP</td><td>$8,548</td><td>-3.2%</td></tr><tr><td>PINS</td><td>$15,716</td><td>3.0%</td></tr><tr><td>RDDT</td><td>$36,693</td><td>-7.2%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>-3.1%</td></tr><tr><td colspan="3">E-Commerce</td></tr><tr><td>AMZN</td><td>$2,688,379</td><td>0.8%</td></tr><tr><td>CHWY</td><td>$8,772</td><td>0.2%</td></tr><tr><td>EBAY</td><td>$51,211</td><td>-4.4%</td></tr><tr><td>ETSY</td><td>$10,179</td><td>3.8%</td></tr><tr><td>FIGS</td><td>$2,022</td><td>2.7%</td></tr><tr><td>PTON</td><td>$2,829</td><td>4.4%</td></tr><tr><td>RVLV</td><td>$1,798</td><td>4.0%</td></tr><tr><td>WW</td><td>$146</td><td>-5.4%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>0.7%</td></tr><tr><td colspan="3">Travel</td></tr><tr><td>ABNB</td><td>$93,573</td><td>-1.8%</td></tr><tr><td>BKNG</td><td>$144,254</td><td>1.8%</td></tr><tr><td>EXPE</td><td>$33,588</td><td>-0.8%</td></tr><tr><td colspan="2">Market-Cap Weighted Avg.</td><td>0.3%</td></tr><tr><td colspan="3">Shared Economy</td></tr><tr><td>UBER</td><td>$150,093</td><td>-2.8%</td></tr><tr><td>DASH</td><td>$81,942</td><td>-4.0%</td></tr><tr><td>CART</td><td>$11,620</td><td>-5.3%</td></tr><tr><td>LYFT</td><td>$6,245</td><td>-0.6%</td></tr><tr><td colspan="2">M

[中间内容因长度限制已省略]

on Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Internet

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/20/2026)</td></tr><tr><td colspan="3">Brian Nowak, CFA</td></tr><tr><td>Airbnb Inc (ABNB.O)</td><td>U (12/06/2022)</td><td>$144.94</td></tr><tr><td>Alphabet Inc. (GOOGL.O)</td><td>O (08/11/2015)</td><td>$351.99</td></tr><tr><td>Amazon.com Inc (AMZN.O)</td><td>O (04/24/2015)</td><td>$249.99</td></tr><tr><td>Booking Holdings Inc (BKNG.O)</td><td>O (02/23/2026)</td><td>$179.45</td></tr><tr><td>DoorDash Inc (DASH.O)</td><td>O (02/21/2024)</td><td>$189.02</td></tr><tr><td>Expedia Inc. (EXPE.O)</td><td>E (01/09/2019)</td><td>$265.08</td></tr><tr><td>Instacart (CART.O)</td><td>E (01/29/2024)</td><td>$46.75</td></tr><tr><td>Lyft Inc (LYFT.O)</td><td>E (10/24/2019)</td><td>$15.43</td></tr><tr><td>Meta Platforms Inc (META.O)</td><td>O (03/20/2023)</td><td>$645.85</td></tr><tr><td>Pinterest Inc (PINS.N)</td><td>O (07/20/2025)</td><td>$22.81</td></tr><tr><td>Reddit Inc (RDDT.N)</td><td>O (12/08/2024)</td><td>$181.64</td></tr><tr><td>Snap Inc. (SNAP.N)</td><td>E (07/22/2024)</td><td>$4.56</td></tr><tr><td>Uber Technologies Inc (UBER.N)</td><td>++</td><td>$72.17</td></tr><tr><td colspan="3">Matthew Cost</td></tr><tr><td>AppLovin Corp (APP.O)</td><td>O (04/10/2025)</td><td>$424.60</td></tr><tr><td>Compass, Inc. (COMP.N)</td><td>E (01/12/2026)</td><td>$11.74</td></tr><tr><td>Criteo SA (CRTO.O)</td><td>E (01/26/2016)</td><td>$22.00</td></tr><tr><td>DoubleVerify Holdings Inc (DV.N)</td><td>E (06/25/2024)</td><td>$11.56</td></tr><tr><td>Electronic Arts Inc (EA.O)</td><td>E (08/04/2021)</td><td>$209.29</td></tr><tr><td>Liftoff Mobile Inc. (LFTO.O)</td><td>E (06/29/2026)</td><td>$23.16</td></tr><tr><td>MNTN Inc (MNTN.N)</td><td>E (06/16/2025)</td><td>$8.77</td></tr><tr><td>Opendoor Technologies Inc (OPEN.O)</td><td>E (07/24/2023)</td><td>$4.45</td></tr><tr><td>Playtika Holding Corp (PLTK.O)</td><td>E (11/27/2022)</td><td>$3.78</td></tr><tr><td>Roblox Corporation (RBLX.N)</td><td>O (11/04/2024)</td><td>$53.25</td></tr><tr><td>Shutterstock Inc (SSTK.N)</td><td>E (07/28/2022)</td><td>$7.68</td></tr><tr><td>Take-Two Interactive Software (TTWO.O)</td><td>O (02/01/2018)</td><td>$238.98</td></tr><tr><td>Trade Desk Inc (TTD.O)</td><td>E (09/10/2025)</td><td>$18.64</td></tr><tr><td>Unity Software Inc (U.N)</td><td>O (09/02/2024)</td><td>$29.81</td></tr><tr><td>Webtoon Entertainment Inc (WBTN.O)</td><td>E (07/22/2024)</td><td>$9.87</td></tr><tr><td>Yelp Inc (YELP.N)</td><td>U (01/10/2019)</td><td>$26.33</td></tr><tr><td>Zillow Group Inc (Z.O)</td><td>E (04/18/2018)</td><td>$33.03</td></tr><tr><td colspan="3">Nathan Feather</td></tr><tr><td>Bumble Inc. (BMBL.O)</td><td>E (03/08/2021)</td><td>$2.93</td></tr><tr><td>Chewy Inc (CHWY.N)</td><td>O (10/31/2023)</td><td>$21.99</td></tr><tr><td>Duolingo Inc (DUOL.O)</td><td>E (02/27/2026)</td><td>$133.89</td></tr><tr><td>eBay Inc (EBAY.O)</td><td>O (04/18/2024)</td><td>$114.19</td></tr><tr><td>Etsy Inc (ETSY.N)</td><td>E (07/20/2025)</td><td>$84.03</td></tr><tr><td>FIGS, Inc. (FIGS.N)</td><td>E (02/29/2024)</td><td>$10.26</td></tr><tr><td>Grindr Inc. (GRND.N)</td><td>O (07/01/2026)</td><td>$15.57</td></tr><tr><td>Match Group Inc (MTCH.O)</td><td>E (04/18/2024)</td><td>$39.04</td></tr><tr><td>Peloton Interactive, Inc. (PTON.O)</td><td>E (03/14/2022)</td><td>$6.52</td></tr><tr><td>Revolve Group Inc (RVLV.N)</td><td>E (10/20/2024)</td><td>$26.03</td></tr><tr><td>WW International Inc (WW.O)</td><td>E (08/01/2025)</td><td>$14.87</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
