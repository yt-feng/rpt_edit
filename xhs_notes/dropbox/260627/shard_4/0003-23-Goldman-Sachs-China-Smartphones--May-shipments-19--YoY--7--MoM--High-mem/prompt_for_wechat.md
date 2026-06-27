你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`GS`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

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

## Disclosures

## Rating and pricing information

AAC (Buy, HK\$43.02), Fositek (Buy, NT\$1,640.00), Hon Hai (Buy, NT\$248.50), Largan (Buy, NT\$4,720.00), Lingyi (Buy, Rmb16.41), SZS (Buy, NT\$194.50), TSMC (Buy, NT\$2,340.00) and TSMC (ADR) (Buy, \$432.35)

## Distribution of ratings/investment banking relationships

GS Investment Research global Equity coverage universe

<table><tr><td rowspan="2"></td><td colspan="3">Rating Distribution</td><td colspan="3">Investment Banking Relationships</td></tr><tr><td>Buy</td><td>Hold</td><td>Sell</td><td>Buy</td><td>Hold</td><td>Sell</td></tr><tr><td>Global</td><td>50%</td><td>34%</td><td>16%</td><td>65%</td><td>60%</td><td>45%</td></tr></table>

As of April 1, 2026, GS Global Investment Research had investment ratings on 3,074 equity securities. GS assigns stocks as Buys and Sells on various regional Investment Lists; stocks not so assigned are deemed Neutral. Such assignments equate to Buy, Hold and Sell for the purposes of the above disclosure required by the FINRA Rules. See ‘Ratings, Coverage universe and related definitions’ below. The Investment Banking Relationships chart reflects the percentage of subject companies within each rating category for whom GS has provided investment banking services within the previous twelve months.

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an offic

[中间内容因长度限制已省略]

m impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
