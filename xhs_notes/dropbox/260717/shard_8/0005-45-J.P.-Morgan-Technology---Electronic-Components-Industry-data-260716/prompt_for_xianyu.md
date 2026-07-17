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
# Technology – Electronic Components Industry data

Technology – Electronic Components
Akinori Kanemoto AC
+813-6736-8628
akinori.kanemoto@JPM.com
JPM Securities Japan Co., Ltd.

Technology – Consumer/Industrial/Precision
Junya Ayada
+813-6736-8631
junya.ayada@JPM.com
JPM Securities Japan Co., Ltd.

See the end pages of this presentation for analyst certification and important disclosures, including non-US analyst disclosures.

## End demand assumptions

<table><tr><td>FY(mn units)</td></tr><tr><td>End demand volume (shipment)</td></tr><tr><td>Global smartphone shipment</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Apple</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Samsung</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Others</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global PC shipment</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Notebook PC (Including Chrome)</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Desktop PC</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Server shipment</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>General Server</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>AI server</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>IHS-Global Auto Production</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>Global Vehicle Sales</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>ICE</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>xEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>HEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>PHEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>BEV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr><tr><td>FCV</td></tr><tr><td>yoy % chg.</td></tr><tr><td>qoq % chg.</td></tr></table>

<table><tr><td>CY2020</td><td>CY2021</td><td>CY2022</td><td>CY2023</td><td>CY2024</td><td>CY2025</td><td>CY2026E</td><td>CY2027E</td></tr><tr><td>1,264.74</td><td>1,351.40</td><td>1,193.43</td><td>1,141.86</td><td>1,223.18</td><td>1,245.45</td><td>1,104.26</td><td>1,075.13</td></tr><tr><td>-</td><td>6.85%</td><td>-11.69%</td><td>-4.32%</td><td>7.12%</td><td>1.82%</td><td>-11.34%</td><td>-2.64%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>207.15</td><td>230.06</td><td>232.16</td><td>229.14</td><td>225.85</td><td>240.64</td><td>238.55</td><td>252.50</td></tr><tr><td>-</td><td>11.06%</td><td>0.91%</td><td>-1.30%</td><td>-1.44%</td><td>6.55%</td><td>-0.87%</td><td>5.85%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>255.52</td><td>274.50</td><td>257.95</td><td>225.46</td><td>222.91</td><td>239.13</td><td>230.93</td><td>228.50</td></tr><tr><td>-</td><td>7.43%</td><td>-6.03%</td><td>-12.59%</td><td>-1.13%</td><td>7.28%</td><td>-3.43%</td><td>-1.05%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>802.08</td><td>846.73</td><td>703.31</td><td>687.27</td><td>774.44</td><td>765.62</td><td>634.79</td><td>594.08</td></tr><tr><td>-</td><td>5.57%</td><td>-16.94%</td><td>-2.28%</td><td>12.68%</td><td>-1.14%</td><td>-17.09%</td><td>-6.41%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>308.17</td><td>341.73</td><td>284.20</td><td>242.28</td><td>247.65</td><td>268.63</td><td>245.71</td><td>249.53</td></tr><tr><td>-</td><td>10.89%</td><td>-16.83%</td><td>-14.75%</td><td>2.21%</td><td>8.47%</td><td>-8.53%</td><td>1.55%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>228.33</td><td>256.38</td><td>208.12</td><td>179.83</td><td>186.54</td><td>201.52</td><td>183.79</td><td>186.35</td></tr><tr><td>-</td><td>12.29%</td><td>-18.82%</td><td>-13.59%</td><td>3.73%</td><td>8.03%</td><td>-8.80%</td><td>1.39%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>79.84</td><td>85.34</td><td>76.08</td><td>62.45</td><td>61.11</td><td>67.11</td><td>61.93</td><td>63.18</td></tr><tr><td>-</td><td>6.89%</td><td>-10.85%</td><td>-17.91%</td><td>-2.15%</td><td>9.82%</td><td>-7.72%</td><td>2.03%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12.67</td><td>12.92</td><td>13.83</td><td>11.35</td><td>12.09</td><td>12.12</td><td>13.88</td><td>15.03</td></tr><tr><td>-</td><td>1.94%</td><td>7.04%</td><td>-17.90%</td><td>6.46%</td><td>0.25%</td><td>14.57%</td><td>8.27%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12.67</td><td>12.92</td><td>13.43</td><td>10.78</td><td>11.02</td><td>10.30</td><td>11.68</td><td>12.44</td></tr><tr><td>-</td><td>1.94%</td><td>3.94%</td><td>-19.75%</td><td>2.27%</td><td>-6.49%</td><td>13.39%</td><td>6.51%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>-</td><td>-</td><td>0.40</td><td>0.58</td><td>1.07</td><td>1.81</td><td>2.20</td><td>2.58</td></tr><tr><td>-</td><td>-</td><td>-</td><td>44.08%</td><td>84.66%</td><td>69.87%</td><td>21.28%</td><td>17.63%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>74.59</td><td>77.19</td><td>82.34</td><td>90.49</td><td>89.59</td><td>93.10</td><td>90.88</td><td>91.58</td></tr><tr><td>-</td><td>3.49%</td><td>6.66%</td><td>9.90%</td><td>-0.99%</td><td>3.92%</td><td>-2.38%</td><td>0.77%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>77.18</td><td>80.27</td><td>78.98</td><td>86.70</td><td>88.69</td><td>91.74</td><td>87.69</td><td>88.55</td></tr><tr><td>-</td><td>3.99%</td><td>-1.60%</td><td>9.76%</td><td>2.30%</td><td>3.44%</td><td>-4.42%</td><td>0.99%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>71.52</td><td>68.12</td><td>62.17</td><td>64.15</td><td>60.90</td><td>58.04</td><td>52.93</td><td>51.29</td></tr><tr><td>-</td><td>-4.77%</td><td>-8.73%</td><td>3.20%</td><td>-5.07%</td><td>-4.70%</td><td>-8.80%</td><td>-3.10%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>5.66</td><td>12.15</td><td>16.82</td><td>22.54</td><td>27.79</td><td>33.70</td><td>34.76</td><td>37.26</td></tr><tr><td>-</td><td>114.69%</td><td>38.42%</td><td>34.04%</td><td>23.27%</td><td>21.28%</td><td>3.13%</td><td>7.21%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2.72</td><td>5.71</td><td>6.22</td><td>8.16</td><td>9.84</td><td>11.07</td><td>12.39</td><td>13.92</td></tr><tr><td>-</td><td>110.01%</td><td>9.00%</td><td>31.17%</td><td>20.52%</td><td>12.57%</td><td>11.92%</td><td>12.33%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0.89</td><td>1.82</td><td>2.74</td><td>4.08</td><td>6.47</td><td>7.61</td><td>6.95</td><td>7.36</td></tr><tr><td>-</td><td>104.61%</td><td>51.14%</td><td>48.70%</td><td>58.63%</td><td>17.48%</td><td>-8.62%</td><td>5.91%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2.04</td><td>4.61</td><td>7.83</td><td>10.29</td><td>11.47</td><td>15.01</td><td>15.40</td><td>15.96</td></tr><tr><td>-</td><td>125.40%</td><td>69.98%</td><td>31.32%</td><td>11.48%</td><td>30.89%</td><td>2.58%</td><td>3.66%</td></tr><tr><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>0.01</td><td>0.02</td><td>0.02</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.01</td><td>0.02</td></tr><tr><td>-</td><td>86.31%</td><td>-0.36%</td><td>-40.88%</td><td>-36.62%</td><td>41.82%</td><td>35.00%</td><td>40.00%</td></tr></table>

<table><tr><td colspan="4">CY2025</td><td colspan="4">CY2026</td></tr><tr><td></td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td>1QE</td><td>2QE</td><td>3QE</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>296.94</td><td>288.92</td><td>320.06</td><td>339.53</td><td>292.13</td><td>262.70</td><td>272.45</td><td>276.97</td></tr><tr><td>0.24%</td><td>-0.01%</td><td>3.26%</td><td>3.49%</td><td>-1.62%</td><td>-9.07%</td><td>-14.87%</td><td>-18.43%</td></tr><tr><td>-9.49%</td><td>-2.70%</td><td>10.78%</td><td>6.09%</td><td>-13.96%</td><td>-10.08%</td><td>3.71%</td><td>1.66%</td></tr><tr><td>55.01</td><td>44.79</td><td>56.50</td><td>84.33</td><td>60.41</td><td>49.69</td><td>56.79</td><td>71.66</td></tr><tr><td>12.95%</td><td>-1.77%</td><td>3.76%</td><td>9.39%</td><td>9.81%</td><td>10.93%</td><td>0.51%</td><td>-15.02%</td></tr><tr><td>-28.64%</td><td>-18.58%</td><td>26.15%</td><td>49.24%</td><td>-28.36%</td><td>-17.75%</td><td>14.29%</td><td>26.18%</td></tr><tr><td>60.55</td><td>57.50</td><td>60.64</td><td>60.45</td><td>59.00</td><td>57.37</td><td>59.10</td><td>55.46</td></tr><tr><td>0.95%</td><td>7.40%</td><td>5.54%</td><td>16.38%</td><td>-2.55%</td><td>-0.22%</td><td>-2.55%</td><td>-8.25%</td></tr><tr><td>16.57%</td><td>-5.03%</td><td>5.46%</td><td>-0.32%</td><td>-2.39%</td><td>-2.76%</td><td>3.00%</td><td>-6.15%</td></tr><tr><td>181.54</td><td>186.83</td><td>202.62</td><td>194.17</td><td>172.91</td><td>155.70</td><td>156.42</td><td>149.74</td></tr><tr><td>-3.48%</td><td>-1.56%</td><td>2.46%</td><td>-2.25%</td><td>-4.75%</td><td>-16.66%</td><td>-22.80%</td><td>-22.88%</td></tr><tr><td>-8.61%</td><td>2.92%</td><td>8.45%</td><td>-4.17%</td><td>-10.95%</td><td>-9.95%</td><td>0.46%</td><td>-4.27%</td></tr><tr><td>60.32</td><td>65.94</td><td>72.46</td><td>69.91</td><td>65.68</td><td>59.50</td><td>60.00</td><td>60.53</td></tr><tr><td>6.58%</td><td>8.05%</td><td>12.15%</td><td>6.88%</td><td>8.89%</td><td>-9.77%</td><td>-17.19%</td><td>-13.42%</td></tr><tr><td>-7.78%</td><td>9.33%</td><td>9.88%</td><td>-3.52%</td><td>-6.05%</td><td>-9.41%</td><td>0.85%</td><td>0.88%</td></tr><tr><td>44.96</td><td>49.60</td><td>54.64</td><td>52.32</td><td>49.16</td><td>44.39</td><td>44.92</td><td>45.32</td></tr><tr><td>7.14%</td><td>7.72%</td><td>11.19%</td><td>5.95%</td><td>9.33%</td><td>-10.50%</td><td>-17.78%</td><td>-13.39%</td></tr><tr><td>-8.97%</td><td>10.32%</td><td>10.16%</td><td>-4.23%</td><td>-6.06%</td><td>-9.69%</td><td>1.19%</td><td>0.88%</td></tr><tr><td>15.36</td><td>16.34</td><td>17.82</td><td>17.59</td><td>16.52</td><td>15.11</td><td>15.08</td><td>15.21</td></tr><tr><td>4.96%</td><td>9.07%</td><td>15.19%</td><td>9.75%</td><td>7.59%</td><td>-7.55%</td><td>-15.38%</td><td>-13.49%</td></tr><tr><td>-4.14%</td><td>6.40%</td><td>9.06%</td><td>-1.33%</td><td>-6.04%</td><td>-8.57%</td><td>-0.17%</td><td>0.87%</td></tr><tr><td>2.94</td><td>2.94</td><td>2.86</td><td>3.38</td><td>3.26</td><td>3.40</td><td>3.44</td><td>3.78</td></tr><tr><td>2.94%</td><td>-1.53%</td><td>-5.62%</td><td>5.05%</td><td>11.13%</td><td>15.63%</td><td>20.17%</td><td>11.88%</td></tr><tr><td>-8.68%</td><td>0.15%</td><td>-2.68%</td><td>18.03%</td><td>-3.39%</td><td>4.20%</td><td>1.14%</td><td>9.88%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2"></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

## Electronic components Sales index by application

![](images/db4bdf31f5f296c60cc3d5e110cd4b89929f2e6eee281f13e049b705665e9b54.jpg)

For PC & Servers (including FCBGA, HDD related, 2Q18=100)  
![](images/267b1d68d2e4d95c5ec9cdef89cbdd8371e1547751bb3ddad0b7bb813548c765.jpg)

For Industrial Applications (2Q18=100)  
![](images/0b65d6adc619116a54c9e20297380b70be85be629ccdf695390d97b6d54769c1.jpg)

For Automotive (2Q18=100)  
![](images/30298bdd89b5ea0128aaaed1983a55351818bce3399ad7e9717296a220dfcf76.jpg)

## Quarterly automotive component revenues and \$ contents per car, comparison with theoretical contents growth

Automotive component revenues for 14 Japanese component makers  
![](images/81e41d0a9fcadea25eb5e7c038d48a527789bd489a0c62fd78b0018d1eb58824.jpg)

\$ contents per car for 14 Japanese component makers  
![](images/2b20bcb2478c7bdd2de312f3434557defce89920d8d9837b37d751e1a032bf3b.jpg)

Comparison between \$ contents per car for 14 Japanese component makers and theoretical \$ contents trend  
![](images/a4abb539d44133914e86c60fe0b0263b8ed902df09a36f6014c2fcf2b3404842.jpg)  
Source: Company data from Ibiden, Niterra, Mabuchi Motor, Murata Mfg., TDK, Taiyo Yuden, Nichicon, Nippon Chemi-con, Nippon Denpa Kogyo, Alps Alpine, Hirose Electric, JAE, Yokowo, Rohm, JPM

## Comparison of automotive semiconductors and electronic components

Automotive SEMI revenues for major analog/discrete/MCU makers  
![](images/c0f3e81c35bc61792f9c0209a8512b45009c6b7cbdd67761d9169ab76b2c9f0c.jpg)  
■ Renesas (Automotive) ■ ROHM (Automotive) ■ NXP (Automotive) ■ ON (Automotive) ■ STM (ADG) ■ IFX(ATV)

Note: For semiconductors, it is the total of IFX, STM, ON Semiconductor, NXP, Rohm, and Renesas Electronics; for Japanese electronic components, it is the total of Ibiden, Niterra, Mabuchi Motor, Murata Mfg., TDK, Taiyo Yuden, Nichicon, Nippon Chemicon, Nippon Denpa Kogyo, Alps Alpine, Hirose Electric, JAE, and Yokowo.

## \$ contents comparison for major analog/discrete/MCU makers and 14 Japanese component makers

![](images/2d50b128e56841943017484054221c88fd21c4f043afd4e3ebb691c7367e71d4.jpg)

YoY % change of \$ contents for major analog/discrete/MCU makers and 14 Japanese component makers  
![](images/8b7ac4004215f9420a625e85d90a4f712459f8672755348fd7460939e1ad212a.jpg)

## FA makers sales/orders vs. industrial component sales

FA makers sales and industrial component sales index (2Q18=100)  
![](images/1561556474263e9c3af0f7a232f7a0e293de05cc41d6870e2c3d2ea4120ab19e.jpg)  
FA makers orders and industrial component sales index (2Q18=100)

![](images/93ae330497ed44b636fff12e90152535bcf5a6730c50ca952b6a77c54a18c3b2.jpg)

## BB ratio and order index for Murata, Tai

[中间内容因长度限制已省略]

tions, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is

## Disclosures

under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.
"""
