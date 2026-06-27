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
# China Smartphones: May shipments +19% YoY/ +7% MoM; High memory costs weigh on demand

May smartphone shipments in China were +19% YoY to 27m units, or +7% MoM. Monthly shipments continued the sequential increase trend in May post April shipments at +25% MoM. We expect 2Q26 shipments to decline at 14% YoY (report link), given rising memory cost weighing on demand. For cameras, the number of cameras per phone peaked in 2022 at 3.8 cameras and declined to 3.1/ 3.0 cameras in 2025/ 2026 YTD; however, 20MPx+ penetration increased to 57%/ 65% in 2025/ 2026 YTD (vs. 52%/ 39% in 2024/23), in line with our view on camera specification upgrades for China smartphones (report link). Read more: Smartphone TAM.

Buy: Hon Hai (on CL), AAC, Lingyi, Largan, SZS, Fositek, and TSMC (on CL).

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng
+852-2978-1681 | verena.jeng@gs.com
GS (Asia) L.L.C.

Ting Song +852-2978-6466 | ting.song@gs.com GS (Asia) L.L.C.

Yifan Hu  
+852-2978-0996 | yifan.hu@gs.com  
GS (Asia) L.L.C.

## Key China smartphone data in May

## China 5G phone market in May

5G phone shipments in China came in at 26m units in May, +6% MoM, +24% YoY, with a 95% penetration rate, per MIIT.

The number of new 5G smartphone models launched in China was $-15\%$ YoY to 11 models in May 2026 vs. $+95\%$ YoY to 37 models in Apr 2026, per MIIT.

## China smartphone market in May

■ Smartphone shipments in China were +19% YoY to 27m units in May 2026 vs. +12% YoY in Apr 2026, per MIIT.

The number of new smartphone models launched in China was $-44\%$ YoY to 15 models in May 2026 vs. $+56\%$ YoY to 50 models in April 2026, per MIIT.

## Smartphone camera pixels in leading China smartphone brands in 2026 YTD

We reviewed the 165 models launched by Honor, Xiaomi, OPPO, Vivo and Transsion in 2026 YTD, totaling 487 cameras.

Average number of cameras per model was at 3.0 in 2026 YTD, vs. 3.1/ 3.3/ 3.5/ 3.8 / 4.1 / 4.9 / 4.0 in 2025/ 2024/ 2023 / 2022 / 2021 / 2020 / 2019. Among the 487 cameras, $24\%$ of cameras were 2MPx/5MPx/8MPx, vs. $31\%$ / $36\%$ / $45\%$ / $51\%$ / $50\%$ / $57\%$ / $46\%$ in 2025/ 2024/ 2023 / 2022 / 2021 / 2020 / 2019.

■ 25 models have been launched by Honor in 2026 YTD with a total of 72 cameras, or 2.9 cameras per model, vs. Huawei at 3.0 cameras, OPPO at 3.1 cameras,

Xiaomi at 2.8 cameras, Vivo at 3.0 cameras, and Transsion at 2.8 cameras.

Among the 171 cameras in the 56 models that Oppo has launched in 2026 YTD, $24\%$ were 2MPx/5MPx/8MPx, vs. Huawei at $18\%$ , Honor at $22\%$ , Xiaomi at $24\%$ , Vivo at $22\%$ , and Transsion at $33\%$ .

## China smartphone shipments and specification

Exhibit 1: 5G smartphone shipments in China: 26m units in May  
![](images/2f20239618a794d76c5ecd094a342dd7a2f6426018dc49399ba689298bb7e346.jpg)  
Source: MIIT

Exhibit 2: Monthly # of new 5G smartphone models launched in China  
![](images/cff80c3ad5980b1566617fae1edc859e373e665ac3548398ce329b250a4f1dbb.jpg)

Exhibit 3: 2014-15 4G mobile phone shipments and penetration rate  
![](images/37839274f91e2b1ccf0d1eb031e580b9433f1985cae8f1d927b12b61af47c64a.jpg)  
Source: MIIT  
Source: MIIT

Exhibit 4: Monthly # of new 4G mobile phone models launched in China  
![](images/c3b67dd42d8a9983eb55a7133c9249793ae7f02e3178a27912a831067e5d54d0.jpg)  
Source: MIIT

(m units)

Exhibit 5: Smartphone shipments in China  
![](images/bcf0fc2d44c1c393947ed4298934248a7e175692f58e409804fbe88a52d17503.jpg)  
Source: MIIT

Exhibit 6: Number of new smartphone models launched in China  
![](images/507238e29f3c72a87dbac134234839a3e4b2b76bba5ea27b6c305a7103254de9.jpg)  
Source: MIIT

Exhibit 7: Mobile phone shipments in China

<table><tr><td>m units</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td>Mobile phones</td><td>24</td><td>23</td><td>28</td><td>23</td><td>28</td><td>32</td><td>30</td><td>24</td><td>23</td><td>17</td><td>21</td><td>26</td><td>28</td></tr><tr><td>YoY</td><td>-22%</td><td>-9%</td><td>16%</td><td>-6%</td><td>10%</td><td>9%</td><td>2%</td><td>-29%</td><td>-16%</td><td>-15%</td><td>-7%</td><td>3%</td><td>17%</td></tr><tr><td>MoM</td><td>-5%</td><td>-5%</td><td>24%</td><td>-20%</td><td>24%</td><td>16%</td><td>-7%</td><td>-19%</td><td>-7%</td><td>-27%</td><td>26%</td><td>22%</td><td>7%</td></tr><tr><td>5G</td><td>21.2</td><td>18.4</td><td>22.6</td><td>20.0</td><td>24.1</td><td>29.3</td><td>27.6</td><td>22.1</td><td>19.9</td><td>15.9</td><td>19.7</td><td>24.7</td><td>26.2</td></tr><tr><td>5G to mobile phones</td><td>89%</td><td>82%</td><td>81%</td><td>88%</td><td>86%</td><td>91%</td><td>92%</td><td>90%</td><td>87%</td><td>95%</td><td>93%</td><td>96%</td><td>95%</td></tr><tr><td>Chinese Brands</td><td>19</td><td>17</td><td>25</td><td>21</td><td>24</td><td>25</td><td>23</td><td>21</td><td>20</td><td>14</td><td>18</td><td>22</td><td>24</td></tr><tr><td>Chinese Brands to mobile phones</td><td>81%</td><td>77%</td><td>90%</td><td>94%</td><td>85%</td><td>78%</td><td>77%</td><td>87%</td><td>88%</td><td>86%</td><td>84%</td><td>86%</td><td>87%</td></tr><tr><td>Smartphone</td><td>23</td><td>21</td><td>24</td><td>22</td><td>26</td><td>31</td><td>29</td><td>23</td><td>21</td><td>16</td><td>20</td><td>25</td><td>27</td></tr><tr><td>YoY</td><td>-21%</td><td>-14%</td><td>10%</td><td>3%</td><td>8%</td><td>12%</td><td>2%</td><td>-29%</td><td>-16%</td><td>-13%</td><td>-6%</td><td>12%</td><td>19%</td></tr><tr><td>MoM</td><td>1%</td><td>-9%</td><td>19%</td><td>-11%</td><td>18%</td><td>22%</td><td>-8%</td><td>-20%</td><td>-9%</td><td>-21%</td><td>24%</td><td>25%</td><td>7%</td></tr><tr><td>Smartphone to mobile phones</td><td>95%</td><td>91%</td><td>87%</td><td>96%</td><td>92%</td><td>97%</td><td>95%</td><td>93%</td><td>91%</td><td>97%</td><td>95%</td><td>97%</td><td>97%</td></tr><tr><td># of new smartphone models (units)</td><td>27</td><td>10</td><td>28</td><td>49</td><td>29</td><td>26</td><td>24</td><td>21</td><td>32</td><td>18</td><td>15</td><td>50</td><td>15</td></tr><tr><td>YoY</td><td>-27%</td><td>-47%</td><td>56%</td><td>40%</td><td>53%</td><td>-21%</td><td>-8%</td><td>17%</td><td>28%</td><td>64%</td><td>-69%</td><td>56%</td><td>-44%</td></tr><tr><td>MoM</td><td>-16%</td><td>-63%</td><td>180%</td><td>75%</td><td>-41%</td><td>-10%</td><td>-8%</td><td>-13%</td><td>52%</td><td>-44%</td><td>-17%</td><td>233%</td><td>-70%</td></tr><tr><td># of new mobile models (units)</td><td>39</td><td>36</td><td>48</td><td>65</td><td>47</td><td>45</td><td>31</td><td>41</td><td>37</td><td>23</td><td>19</td><td>59</td><td>19</td></tr><tr><td>5G</td><td>13</td><td>8</td><td>23</td><td>31</td><td>23</td><td>19</td><td>24</td><td>11</td><td>20</td><td>15</td><td>13</td><td>37</td><td>11</td></tr><tr><td>5G to total new mobile models</td><td>33%</td><td>22%</td><td>48%</td><td>48%</td><td>49%</td><td>42%</td><td>77%</td><td>27%</td><td>54%</td><td>65%</td><td>68%</td><td>63%</td><td>58%</td></tr></table>

Source: MIIT

Exhibit 8: Model pricing for various foldable smartphone brands  
![](images/32d0f7515e2bd438b541dc4b45ba8789799c9e0341ba43f8c051616379727b0e.jpg)  
Source: Company data, Data compiled by GS Global Investment Research

![](images/837671a1012a3b62e8e5fa70118465ebc7776ee09af66c9030117f579e03b093.jpg)  
Expected model and launch date for those cells with white background  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 10: Cameras per smartphone model peaking out Smartphone models launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since Dec 2020

![](images/4e50ae011d671657dfd66376d41b391b31c3f3aa9e71710c988d693ef0908380.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 12: Huawei/Honor/Xiaomi/OPPO/Vivo/Transsion: 20MPx+ becomes the main contributor

Cameras on smartphones launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since 2018: % of cameras in terms of pixels

![](images/fbb1547cd16388cfec82393252c984fdbabf814b1ce3ba1e305813ece4b5eeb5.jpg)  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 11: 20MPx+ becomes the main contributor Cameras on smartphones launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion since Dec 2020, % of cameras in terms of pixels

![](images/1a6e2b2b52bf833aad084ab2df4f2e2952518f60785b148030c997fd9c0be715.jpg)  
Data as of Jun 26, 2026

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 13: 2/5/8MPx at $24\%$ in 2026 YTD  
487 cameras on 165 models launched by Huawei, Honor, Xiaomi, OPPO, Vivo, Transsion in 2026 YTD, divided by pixel count

![](images/aeb8e6afac4d9ebf66ca3e2884153ed8e22efce781d03583c9cad4c678ff73f0.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research

Exhibit 14: Honor: 20MPx+ remains the main contributor Cameras on smartphones launched by Honor since 2018: % of cameras in terms of pixels

![](images/cfad35e2fbc359c6325bda11436ee0ca27688a649c6a482049ba76241a1cae56.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research  
Exhibit 15: Honor: $22\%$ at 2/5/8MPx  
72 cameras on 25 models launched by Honor in 2026 YTD, by pixel number

![](images/3ecc57939dfe29fb02f09e3d6bdb799623bfffeb5d7db0c61e4aed796113abda.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research  
Exhibit 16: Xiaomi: 20MPx+ decreasing
Cameras on smartphones launched by Xiaomi since 2018: % of cameras in terms of pixels

![](images/b641994b049a10c2e35b887d80304a5ae07f7e72ad2fe075aba5dc7b72464810.jpg)  
Exhibit 17: Xiaomi: $24\%$ at 2/5/8MPx  
67 cameras on 24 models launched by Xiaomi in 2026 YTD, by pixel number

Data as of Jun 26, 2026

Source: Company data, Data compiled by GS Global Investment Research

![](images/5203a9562e3947137c9e07e215fbd8498cf73065de92c854260aebcc38205c45.jpg)

Data as of Jun 26, 2026

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 18: OPPO: 20MPx+ remains the main contributor Cameras on smartphones launched by OPPO since 2018: % of cameras in terms of pixels

![](images/32301a5958dda9f618f11c238aeddd2ccafb35c446f54a130aaaaa9b92144f26.jpg)

Data as of Jun 26, 2026

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 20: Vivo: 20MPx+ becomes the main contributor Cameras on smartphones launched by Vivo since 2018: % of cameras in terms of pixels

![](images/0ca79e9a6d86f146d7fd5f96dcc2506877807f9fed64db545ac09bed441e9a15.jpg)  
Exhibit 19: OPPO: $25\%$ at 2/5/8MPx  
171 cameras on 56 models launched by OPPO in 2026 YTD, by pixel number

Data as of Jun 26, 2026

Source: Company data, Data compiled by GS Global Investment Research

![](images/2ee970df6569ee427d6013f0d3d04f0a85085f98fb5a6e3a74556be51908127f.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research  
Exhibit 21: Vivo: $22\%$ at 2/5/8MPx  
93 cameras on 31 models launched by Vivo in 2026 YTD, by pixel count

![](images/b9cd35a3302c41c32de0dc0e1cd2c7c2ab0a4edd6edae41615c6367e0f40a867.jpg)

Data as of Jun 26, 2026

Source: Company data, Data compiled by GS Global Investment Research

Exhibit 22: Transsion: 20MPx+ remains as the main contributor

Cameras on smartphones launched by Transsion since 2021: % of cameras in terms of pixels

![](images/68f2f260ed4483f5f1331a51aaa4313550cf49961848ff5418bfb1b843f32aa3.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research  
Exhibit 23: Transsion: $33\%$ at 2/5/8MPx  
45 cameras on 16 models launched by Transsion in 2026 YTD, by pixel

![](images/c54b5152b2b4ca81e85b1f074938ba4c2b6ba755449e11031e8825e6e7ab84b5.jpg)  
Data as of Jun 26, 2026  
Source: Company data, Data compiled by GS Global Investment Research

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng, Ting Song and Yifan Hu, hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Ting Song GS (Asia) L.L.C., Yifan Hu GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. The Integrated percentile is calculated as the average of the Growth percentile, Financial Returns percentile and (100% - Multiple percentile).

Financial Returns and Multiple use the GS analyst forecasts at the fiscal year-end at least three quarters in the future. Growth uses inputs for the fiscal year at least seven quarters in the future compared with the year at least three quarters in the future (on a per-share basis for all metrics).

For a more detailed description of how we calculate the GS Factor Profile, please contact your GS representative.

## M&A Rank

Across our global coverage, we examine stocks using an M&A framework, considering both qualitative factors and quantitative factors (which may vary across sectors and regions) to incorporate the potential that certain companies could be acquired. We then assign a M&A rank as a means of scoring companies under our rated coverage from 1 to 3, with 1 representing high (30%-50%) probability of the company becoming an acquisition target, 2 representing medium (15%-30%) probability and 3 representing low (0%-15%) probability. For companies ranked 1 or 2, in line with our standard departmental guidelines we incorporate an M&A component into our target price. M&A rank of 3 is considered immaterial and therefore does not factor into our price target, and may or may not be discussed in research.

## Quantum

Quantum is GS' proprietary database providing access to detailed financial statement histories, forecasts and ratios. It can be used for in-depth analysis of a single company, or to make comparisons between companies in different sectors and markets.

## Disclo

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
