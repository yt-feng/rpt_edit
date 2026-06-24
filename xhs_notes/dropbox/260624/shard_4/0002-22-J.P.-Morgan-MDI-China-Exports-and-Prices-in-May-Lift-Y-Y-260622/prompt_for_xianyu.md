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
## MDI

China Exports and Prices in May Lift Y/Y

\- May MDI exports from China of 101kt were $49\%$ higher versus 68kt in May of 2025. 2026 YTD exports are $15.6\%$ higher y/y. 2026 YTD net exports of 258kt are 55kt higher y/y. Notably, shipments to Europe jumped $63\%$ from 51kt to 82kt ytd. Shipments to Turkey grew $68\%$ from 28kt to 47kt ytd.

\- Chinese average MDI export prices were 13% higher m/m and 25% higher y/y in May: prices averaged \$2,193/t compared with \$1,942/t in April and \$1,756/t in the prior-year period. The China import price was \$2,979/t in May, 115% higher m/m compared with \$1,906/t in April, and 21% higher y/y vs. \$1,385/t in May 2025. Please see Table 5 for more details.

\- 2025 net exports were 400kt or (496kt) lower y/y. 2025 exports were 805kt or (33%) lower y/y. See Table 3 for China exports by destination. 2025 exports to the US were sharply lower (83%) as were exports to Russia and the Netherlands. Full-year 2024 exports of 1,204kt were 15% or 160kt higher y/y. 2024 net exports were 896kt or 170kt higher y/y relative to 2023 net exports of 726kt. Full-year 2023 exports of 1,044kt were 6% or 55kt higher y/y. We estimate Huntsman's MDI volume to have been roughly lower by (10%) in 2022, lower by (14%) in 2023, higher by 7% in 2024, and 2% in 2025.

Chemicals: Specialty, Commodity, Agricultural, and Paper & Packaging

Jeffrey J. Zekauskas AC (1-212) 622-6644  
jeffrey.zekauskas@JPM.com

Katie Zhang (1-212) 622-3262 katie.zhang@jpmchase.com

Silke Kueck (1-212) 622-6503 silke.x.kueck@JPM.com

Lydia Huang  
(1-212) 622-0086  
lydia.huang@JPM.com  
JPM Securities LLC

Table 1: China MDI Trade Data (in kt)

<table><tr><td>Exports</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>44</td><td>43</td><td>40</td><td>43</td><td>66</td><td>83</td><td>91</td><td>101</td><td>63</td><td>64</td></tr><tr><td>February</td><td>32</td><td>53</td><td>47</td><td>45</td><td>91</td><td>59</td><td>116</td><td>76</td><td>80</td><td>61</td></tr><tr><td>March</td><td>46</td><td>40</td><td>76</td><td>89</td><td>106</td><td>100</td><td>102</td><td>113</td><td>75</td><td>90</td></tr><tr><td>April</td><td>40</td><td>63</td><td>65</td><td>33</td><td>82</td><td>83</td><td>99</td><td>127</td><td>57</td><td>81</td></tr><tr><td>May</td><td>57</td><td>44</td><td>43</td><td>28</td><td>113</td><td>114</td><td>109</td><td>94</td><td>68</td><td>101</td></tr><tr><td>June</td><td>68</td><td>80</td><td>43</td><td>30</td><td>76</td><td>117</td><td>89</td><td>134</td><td>70</td><td></td></tr><tr><td>July</td><td>51</td><td>46</td><td>63</td><td>53</td><td>79</td><td>83</td><td>78</td><td>78</td><td>64</td><td></td></tr><tr><td>August</td><td>55</td><td>53</td><td>59</td><td>64</td><td>85</td><td>58</td><td>97</td><td>87</td><td>61</td><td></td></tr><tr><td>September</td><td>46</td><td>64</td><td>49</td><td>54</td><td>90</td><td>89</td><td>75</td><td>95</td><td>80</td><td></td></tr><tr><td>October</td><td>30</td><td>46</td><td>55</td><td>51</td><td>74</td><td>57</td><td>55</td><td>97</td><td>70</td><td></td></tr><tr><td>November</td><td>47</td><td>45</td><td>51</td><td>55</td><td>78</td><td>93</td><td>79</td><td>102</td><td>58</td><td></td></tr><tr><td>December</td><td>46</td><td>39</td><td>40</td><td>69</td><td>75</td><td>53</td><td>54</td><td>101</td><td>60</td><td></td></tr><tr><td>Total</td><td>563</td><td>617</td><td>629</td><td>613</td><td>1,014</td><td>988</td><td>1,044</td><td>1,204</td><td>805</td><td>396</td></tr><tr><td>% change</td><td></td><td>9.7%</td><td>1.8%</td><td>(2.4%)</td><td>65.2%</td><td>(2.5%)</td><td>5.6%</td><td>15.3%</td><td>(33.1%)</td><td>15.6%</td></tr></table>

<table><tr><td>Imports</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>January</td><td>20</td><td>33</td><td>30</td><td>18</td><td>28</td><td>17</td><td>27</td><td>38</td><td>25</td><td>39</td></tr><tr><td>February</td><td>22</td><td>20</td><td>23</td><td>36</td><td>26</td><td>20</td><td>19</td><td>27</td><td>20</td><td>30</td></tr><tr><td>March</td><td>27</td><td>26</td><td>28</td><td>25</td><td>28</td><td>29</td><td>26</td><td>23</td><td>30</td><td>42</td></tr><tr><td>April</td><td>15</td><td>32</td><td>27</td><td>33</td><td>21</td><td>24</td><td>25</td><td>22</td><td>34</td><td>16</td></tr><tr><td>May</td><td>14</td><td>34</td><td>23</td><td>36</td><td>28</td><td>23</td><td>23</td><td>23</td><td>31</td><td>11</td></tr><tr><td>June</td><td>15</td><td>26</td><td>26</td><td>26</td><td>23</td><td>15</td><td>18</td><td>18</td><td>23</td><td></td></tr><tr><td>July</td><td>18</td><td>21</td><td>26</td><td>44</td><td>28</td><td>23</td><td>32</td><td>25</td><td>42</td><td></td></tr><tr><td>August</td><td>19</td><td>37</td><td>22</td><td>33</td><td>21</td><td>28</td><td>28</td><td>19</td><td>30</td><td></td></tr><tr><td>September</td><td>22</td><td>30</td><td>18</td><td>35</td><td>27</td><td>41</td><td>38</td><td>33</td><td>49</td><td></td></tr><tr><td>October</td><td>16</td><td>20</td><td>18</td><td>28</td><td>24</td><td>17</td><td>21</td><td>20</td><td>31</td><td></td></tr><tr><td>November</td><td>21</td><td>18</td><td>37</td><td>26</td><td>29</td><td>22</td><td>36</td><td>28</td><td>34</td><td></td></tr><tr><td>December</td><td>26</td><td>37</td><td>40</td><td>27</td><td>14</td><td>27</td><td>25</td><td>32</td><td>56</td><td></td></tr><tr><td>Total</td><td>234</td><td>333</td><td>318</td><td>369</td><td>298</td><td>286</td><td>318</td><td>309</td><td>405</td><td>138</td></tr><tr><td>% change</td><td></td><td>42.2%</td><td>(4.5%)</td><td>16.1%</td><td>(19.3%)</td><td>(3.8%)</td><td>11.2%</td><td>(3.1%)</td><td>31.4%</td><td>(1.3%)</td></tr></table>

Source: China General Administration of Customs

Table 2: China MDI Annual Trade Data (in kt)

<table><tr><td></td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026</td></tr><tr><td>Net exports/imports</td><td>329</td><td>285</td><td>311</td><td>245</td><td>716</td><td>702</td><td>726</td><td>896</td><td>400</td><td>258</td></tr><tr><td>Net Change</td><td></td><td>(44)</td><td>26</td><td>(66)</td><td>471</td><td>(14)</td><td>23</td><td>170</td><td>(496)</td><td>55</td></tr></table>

Source: China General Administration of Customs

See page 4 for analyst certification and important disclosures.

Table 3: China MDI Exports by Destination (2024-2026YTD)

<table><tr><td rowspan="2"></td><td colspan="3">Volumes in &#x27;000s of tons</td><td colspan="3">% of Total</td></tr><tr><td>2026</td><td>2025</td><td>2024</td><td>2026</td><td>2025</td><td>2024</td></tr><tr><td>EU-27</td><td>82</td><td>50</td><td>100</td><td>21%</td><td>15%</td><td>20%</td></tr><tr><td>Türkiye</td><td>47</td><td>28</td><td>33</td><td>12%</td><td>8%</td><td>7%</td></tr><tr><td>Russia</td><td>30</td><td>36</td><td>38</td><td>7%</td><td>11%</td><td>7%</td></tr><tr><td>India</td><td>26</td><td>26</td><td>21</td><td>7%</td><td>8%</td><td>4%</td></tr><tr><td>Republic of Korea</td><td>25</td><td>20</td><td>30</td><td>6%</td><td>6%</td><td>6%</td></tr><tr><td>Viet Nam</td><td>21</td><td>18</td><td>17</td><td>5%</td><td>5%</td><td>3%</td></tr><tr><td>Thailand</td><td>18</td><td>17</td><td>14</td><td>5%</td><td>5%</td><td>3%</td></tr><tr><td>Japan</td><td>16</td><td>11</td><td>12</td><td>4%</td><td>3%</td><td>2%</td></tr><tr><td>Brazil</td><td>15</td><td>15</td><td>17</td><td>4%</td><td>4%</td><td>3%</td></tr><tr><td>Other</td><td>116</td><td>121</td><td>227</td><td>29%</td><td>35%</td><td>45%</td></tr><tr><td>All</td><td>396</td><td>343</td><td>510</td><td></td><td></td><td></td></tr></table>

Source: China General Administration of Customs

Table 4: Chinese MDI Export/Import Price

<table><tr><td></td><td>export $/ton</td><td>Sq % change</td><td>Y/y % change</td><td>import $/ton</td><td>Sq % change</td><td>Y/y % change</td></tr><tr><td>Jan-20</td><td>1,280</td><td>-1%</td><td>-17%</td><td>1,298</td><td>2%</td><td>-21%</td></tr><tr><td>Feb-20</td><td>1,269</td><td>-1%</td><td>-13%</td><td>1,224</td><td>-6%</td><td>-25%</td></tr><tr><td>Mar-20</td><td>1,234</td><td>-3%</td><td>-15%</td><td>1,308</td><td>7%</td><td>-16%</td></tr><tr><td>Apr-20</td><td>1,275</td><td>3%</td><td>-3%</td><td>1,163</td><td>-11%</td><td>-25%</td></tr><tr><td>May-20</td><td>1,311</td><td>3%</td><td>-9%</td><td>1,156</td><td>-1%</td><td>-29%</td></tr><tr><td>Jun-20</td><td>1,270</td><td>-3%</td><td>-11%</td><td>1,255</td><td>9%</td><td>5%</td></tr><tr><td>Jul-20</td><td>1,235</td><td>-3%</td><td>-5%</td><td>1,121</td><td>-11%</td><td>-11%</td></tr><tr><td>Aug-20</td><td>1,234</td><td>0%</td><td>-6%</td><td>1,095</td><td>-2%</td><td>-21%</td></tr><tr><td>Sep-20</td><td>1,274</td><td>3%</td><td>-2%</td><td>1,313</td><td>20%</td><td>-6%</td></tr><tr><td>Oct-20</td><td>1,316</td><td>3%</td><td>0%</td><td>1,335</td><td>2%</td><td>-1%</td></tr><tr><td>Nov-20</td><td>1,436</td><td>9%</td><td>18%</td><td>2,073</td><td>55%</td><td>66%</td></tr><tr><td>Dec-20</td><td>1,467</td><td>2%</td><td>13%</td><td>2,066</td><td>0%</td><td>62%</td></tr><tr><td>Jan-21</td><td>1,582</td><td>8%</td><td>24%</td><td>1,600</td><td>-23%</td><td>23%</td></tr><tr><td>Feb-21</td><td>1,494</td><td>-6%</td><td>18%</td><td>1,798</td><td>12%</td><td>47%</td></tr><tr><td>Mar-21</td><td>1,718</td><td>15%</td><td>39%</td><td>2,145</td><td>19%</td><td>64%</td></tr><tr><td>Apr-21</td><td>1,982</td><td>15%</td><td>55%</td><td>2,254</td><td>5%</td><td>94%</td></tr><tr><td>May-21</td><td>2,057</td><td>4%</td><td>57%</td><td>2,108</td><td>-6%</td><td>82%</td></tr><tr><td>Jun-21</td><td>2,034</td><td>-1%</td><td>60%</td><td>2,139</td><td>1%</td><td>70%</td></tr><tr><td>Jul-21</td><td>2,106</td><td>4%</td><td>71%</td><td>2,142</td><td>0%</td><td>91%</td></tr><tr><td>Aug-21</td><td>2,269</td><td>8%</td><td>84%</td><td>2,360</td><td>10%</td><td>115%</td></tr><tr><td>Sep-21</td><td>2,343</td><td>3%</td><td>84%</td><td>2,204</td><td>-7%</td><td>68%</td></tr><tr><td>Oct-21</td><td>2,315</td><td>-1%</td><td>76%</td><td>2,364</td><td>7%</td><td>77%</td></tr><tr><td>Nov-21</td><td>2,412</td><td>4%</td><td>68%</td><td>2,241</td><td>-5%</td><td>8%</td></tr><tr><td>Dec-21</td><td>2,349</td><td>-3%</td><td>60%</td><td>1,820</td><td>-19%</td><td>-12%</td></tr><tr><td>Jan-22</td><td>2,280</td><td>-3%</td><td>44%</td><td>2,016</td><td>11%</td><td>26%</td></tr><tr><td>Feb-22</td><td>2,218</td><td>-3%</td><td>48%</td><td>2,270</td><td>13%</td><td>26%</td></tr><tr><td>Mar-22</td><td>2,257</td><td>2%</td><td>31%</td><td>2,216</td><td>-2%</td><td>3%</td></tr><tr><td>Apr-22</td><td>2,298</td><td>2%</td><td>16%</td><td>2,223</td><td>0%</td><td>-1%</td></tr><tr><td>May-22</td><td>2,300</td><td>0%</td><td>12%</td><td>2,188</td><td>-2%</td><td>4%</td></tr><tr><td>Jun-22</td><td>2,093</td><td>-9%</td><td>3%</td><td>2,146</td><td>-2%</td><td>0%</td></tr><tr><td>Jul-22</td><td>2,259</td><td>8%</td><td>7%</td><td>2,122</td><td>-1%</td><td>-1%</td></tr><tr><td>Aug-22</td><td>2,271</td><td>1%</td><td>0%</td><td>1,972</td><td>-7%</td><td>-16%</td></tr><tr><td>Sep-22</td><td>2,109</td><td>-7%</td><td>-10%</td><td>1,734</td><td>-12%</td><td>-21%</td></tr><tr><td>Oct-22</td><td>2,053</td><td>-3%</td><td>-11%</td><td>1,671</td><td>-4%</td><td>-29%</td></tr><tr><td>Nov-22</td><td>1,914</td><td>-7%</td><td>-21%</td><td>1,492</td><td>-11%</td><td>-33%</td></tr><tr><td>Dec-22</td><td>1,862</td><td>-3%</td><td>-21%</td><td>1,340</td><td>-10%</td><td>-26%</td></tr><tr><td>Jan-23</td><td>1,758</td><td>-6%</td><td>-23%</td><td>1,436</td><td>7%</td><td>-29%</td></tr><tr><td>Feb-23</td><td>1,659</td><td>-6%</td><td>-25%</td><td>1,695</td><td>18%</td><td>-25%</td></tr><tr><td>Mar-23</td><td>1,700</td><td>3%</td><td>-25%</td><td>1,676</td><td>-1%</td><td>-24%</td></tr><tr><td>Apr-23</td><td>1,772</td><td>4%</td><td>-23%</td><td>1,616</td><td>-4%</td><td>-27%</td></tr><tr><td>May-23</td><td>1,661</td><td>-6%</td><td>-28%</td><td>1,506</td><td>-7%</td><td>-31%</td></tr><tr><td>Jun-23</td><td>1,645</td><td>-1%</td><td>-21%</td><td>1,498</td><td>-1%</td><td>-30%</td></tr><tr><td>Jul-23</td><td>1,722</td><td>5%</td><td>-24%</td><td>1,483</td><td>-1%</td><td>-30%</td></tr><tr><td>Aug-23</td><td>1,542</td><td>-10%</td><td>-32%</td><td>1,550</td><td>5%</td><td>-21%</td></tr><tr><td>Sep-23</td><td>1,462</td><td>-5%</td><td>-31%</td><td>1,461</td><td>-6%</td><td>-16%</td></tr><tr><td>Oct-23</td><td>1,420</td><td>-3%</td><td>-31%</td><td>1,659</td><td>14%</td><td>-1%</td></tr><tr><td>Nov-23</td><td>1,223</td><td>-14%</td><td>-36%</td><td>1,568</td><td>-6%</td><td>5%</td></tr><tr><td>Dec-23</td><td>1,567</td><td>28%</td><td>-16%</td><td>1,568</td><td>0%</td><td>17%</td></tr><tr><td>Jan-24</td><td>1,277</td><td>-18%</td><td>-27%</td><td>1,570</td><td>0%</td><td>9%</td></tr><tr><td>Feb-24</td><td>1,337</td><td>5%</td><td>-19%</td><td>1,578</td><td>1%</td><td>-7%</td></tr><tr><td>Mar-24</td><td>1,431</td><td>7%</td><td>-16%</td><td>1,657</td><td>5%</td><td>-1%</td></tr><tr><td>Apr-24</td><td>1,540</td><td>8%</td><td>-13%</td><td>1,580</td><td>-5%</td><td>-2%</td></tr><tr><td>May-24</td><td>1,678</td><td>9%</td><td>1%</td><td>1,591</td><td>1%</td><td>6%</td></tr><tr><td>Jun-24</td><td>1,646</td><td>-2%</td><td>0%</td><td>1,685</td><td>6%</td><td>13%</td></tr><tr><td>Jul-24</td><td>1,831</td><td>11%</td><td>6%</td><td>1,534</td><td>-9%</td><td>3%</td></tr><tr><td>Aug-24</td><td>2,020</td><td>10%</td><td>31%</td><td>1,508</td><td>-2%</td><td>-3%</td></tr><tr><td>Sep-24</td><td>2,024</td><td>0%</td><td>38%</td><td>1,521</td><td>1%</td><td>4%</td></tr><tr><td>Oct-24</td><td>1,878</td><td>-7%</td><td>32%</td><td>1,820</td><td>20%</td><td>10%</td></tr><tr><td>Nov-24</td><td>1,715</td><td>-9%</td><td>40%</td><td>1,629</td><td>-10%</td><td>4%</td></tr><tr><td>Dec-24</td><td>1,785</td><td>4%</td><td>14%</td><td>1,442</td><td>-12%</td><td>-8%</td></tr><tr><td>Jan-25</td><td>1,965</td><td>10%</td><td>54%</td><td>1,588</td><td>10%</td><td>1%</td></tr><tr><td>Feb-25</td><td>1,664</td><td>-15%</td><td>24%</td><td>1,736</td><td>9%</td><td>10%</td></tr><tr><td>Mar-25</td><td>1,733</td><td>4%</td><td>21%</td><td>1,563</td><td>-10%</td><td>-6%</td></tr><tr><td>Apr-25</td><td>1,791</td><td>3%</td><td>16%</td><td>1,578</td><td>1%</td><td>0%</td></tr><tr><td>May-25</td><td>1,756</td><td>-2%</td><td>5%</td><td>1,385</td><td>-12%</td><td>-13%</td></tr><tr><td>Jun-25</td><td>1,641</td><td>-7%</td><td>0%</td><td>1,616</td><td>17%</td><td>-4%</td></tr><tr><td>Jul-25</td><td>1,651</td><td>1%</td><td>-10%</td><td>1,512</td><td>-6%</td><td>-1%</td></tr><tr><td>Aug-25</td><td>1,596</td><td>-3%</td><td>-21%</td><td>1,543</td><td>2%</td><td>2%</td></tr><tr><td>Sep-25</td><td>1,569</td><td>-2%</td><td>-22%</td><td>1,541</td><td>0%</td><td>1%</td></tr><tr><td>Oct-25</td><td>1,567</td><td>0%</td><td>-17%</td><td>1,620</td><td>5%</td><td>-11%</td></tr><tr><td>Nov-25</td><td>1,542</td><td>-2%</td><td>-10%</td><td>1,530</td><td>-6%</td><td>-6%</td></tr><tr><td>Dec-25</td><td>1,448</td><td>-6%</td><td>-19%</td><td>1,520</td><td>-1%</td><td>5%</td></tr><tr><td>Jan-26</td><td>1,416</td><td>-2%</td><td>-28%</td><td>1,594</td><td>5%</td><td>0%</td></tr><tr><td>Feb-26</td><td>1,371</td><td>-3%</td><td>-18%</td><td>1,464</td><td>-8%</td><td>-16%</td></tr><tr><td>Mar-26</td><td>1,491</td><td>9%</td><td>-14%</td><td>1,657</td><td>13%</td><td>6%</td></tr><tr><td>Apr-26</td><td>1,942</td><td>30%</td><td>8%</td><td>1,906</td><td>15%</td><td>21%</td></tr><tr><td>May-26</td><td>2,193</td><td>13%</td><td>25%</td><td>2,979</td><td>56%</td><td>115%</td></tr></table>

Source: China General Administration of Customs.

Analyst Certification: The Research Analyst(s) denot

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 22 Jun 2026 04:16 PM EDT

Disseminated 22 Jun 2026 04:16 PM EDT
"""
