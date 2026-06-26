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
## China WFE: Fast-Growing Semi Deficit to Drive Strong WFE Capex

China's May SPE/WFE imports fell 9%/12%, but testing/packaging grew 25%/19%. Positively, WFE's fall is entirely driven by a 32% decline in etching, as deposition/ion implanting grew 12%/21%. Fall in etching is associated with a 28%/58% fall in WFE imports from Japan/Malaysia. YTD, WFE imports fell 12%, driven by 24%/18% fall in litho/etching, while imports from Japan/Netherlands dropped the most, by 28%/24%. We still expect 2026 WFE capex to fall LSD to MSD.

China's WFE imports fell 12% in May, worse than previous two months, but it is narrow-based. China's May SPE imports fell 9%, driven mainly by 12% decline in WFE. Packaging imports grew 8% YTD, the only category with positive growth. We highlighted before Huawei's "Tau" scaling law is based on advanced packaging, and China does not face any restrictions on packaging tools. Therefore, we expect this to be a strong growth area in the next 12-24 months. For WFE, even though the 12% fall in May is a deterioration from 6%/3% decline in Apr/Mar, we are encouraged that May's fall is narrow-based. It is almost entirely driven by a 24% fall in etching. Deposition and ion implanting grew 12% and 21%, respectively, while litho imports were flattish. YTD, WFE imports fell 12%, driven mainly by 24%/18% decline in litho/etching. Deposition and thermal YTD both grew 3%. We believe the YTD weakness is due to 1) CXMT slowing after big pull-in last year and likely waiting for any sign of relaxation of US restrictions and 2) decline in advanced logic due to pull in last year and very long delivery lead time of critical tools in the grey market. We remain confident of some demand recovery in 2H26, leading to low-single-digit (LSD) to mid-single digit (MSD) growth in WFE capex for the full year. We believe memory capex will be the key driver in 2H26.

Singapore has become the largest source of WFE imports for China. It is worth noting the 32% decline in May etching imports coincided with a 58%/28% fall, in WFE imports from Malaysia/Japan. We saw the same trend for the Apr data. It suggests etching tools that China buys are mainly coming from these two countries. YTD, imports of Japan and the Netherlands fell the most (24%/28%) while imports from Singapore and Taiwan rose 45% and 22%, respectively. In fact, Singapore and Taiwan are the only countries that show positive growth YTD for WFE imports into China. Singapore has overtaken Japan as the largest source of WFE imports into China (5M26), with a 25% import share. Japan ranked No. 2 with 23% share, while the Netherlands' share has fallen to No. 3 at 18%.

Rapidly rising semi trade deficit will drive strong long-term WFE capex growth. China's semiconductor imports grew 71% in May, a new high. Semiconductor imports have been accelerating sharply for five consecutive months, driven by, in our view, skyrocketing memory prices and rising demand for AI-related chips such as CPU, optics, and high-end capacitors. Note semi imports from Korea rose 154% in May and 103% YTD. In May, Korea for the first time overtook Taiwan as the largest source of China's semi imports, with a 37% import share or \~US\$18bn. Our analysis shows China's 5M26 semi trade deficit grew 19% YoY to US\$99bn vs being flattish in the past three years. We see rapidly widening semi trade deficit as one of the biggest drivers of China's WFE capex growth. Moreover, China needs much more foundry capacity in mature nodes (for SRAM/PMIC/optics/power), advanced nodes (< 14nm, CPU/GPU/ADAS), and memory to support its efforts in AI, robotics, and electrification. Together with its WFE localization efforts due to US restrictions, Chinese WFE players are among our top picks in China tech.

![](images/76f8a45386a6252308a582c4674f83583c0898f634ed0298c76d7067c2ff3984.jpg)  
Source: China Customs, JEF

Chart 2 - China WFE Imports YoY  
![](images/b0b08351232ea615c2c65372f1005f6a38436c6d56d3f3f963b469507cb8fc35.jpg)  
Source: China Customs, JEF

Chart 3 - China Semiconductor Imports YoY  
![](images/87d500ddcbeadd741d6f8ee9d1c0abd1fbe4e2e54c8145ce7a437288ea2479b5.jpg)  
Source: China Customs, JEF

Chart 4 - China Semi Trade Deficit  
![](images/622ac8abc343030d3518d195e2d9c7cb94a5a89c178f9b56182159324bd3f1e7.jpg)  
Source: China Customs, JEF

Edison Lee, CFA \* | Equity Analyst
852 3743 8009 | edison.lee@JEF.com

Nick Cheng \* | Equity Analyst
+852 3743 8750 | nick.cheng@JEF.com

Matt Ma \* | Equity Analyst
852 3767 1109 | matt.ma@JEF.com

Annie Ping, CFA, FRM \* | Equity Associate +852 3767 1273 | annie.ping@JEF.com

Chart 5 - China Semiconductor Imports YoY  
![](images/b20f50810725703bee8c515dbffa06d9729a24ea0f85586fb85f1d1d3925f582.jpg)  
Source: China Customs, JEF

Chart 6 - China SPE Imports YoY  
![](images/4cc4c4b05243ecd8bf5da88d774c41677286a01ec8b88423590665ae04ec6960.jpg)  
Source: China Customs, JEF

Chart 7 - China Lithography Equipment Imports YoY  
![](images/8eb4bf48e71185fdf26a5292a41a6c0bfbc84d7980422430b1c8707f5880ecf1.jpg)  
Source: China Customs, JEF

Chart 8 - China Deposition Equipment Imports YoY  
![](images/08e686569c4d7ec138af775e794062308693b118709d2f1d31fe881c78c2166c.jpg)  
Source: China Customs, JEF

Chart 9 - China Ion Implanting Equipment Imports YoY  
![](images/27916f3bd6c452e01a6ed0f8ca324abad9de4b9f1fc0806c52ba57708a1151f9.jpg)  
Source: China Customs, JEF

Chart 10 - China Etching Equipment Imports YoY  
![](images/8449ee691e5e7a686e437f25f47a22a3a901a75c4d8bd91afe71cc0fd8aeab78.jpg)  
Source: China Customs, JEF

Table 1 - Quarterly SPE Imports by Key Countries (US\$m)

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Germany</td><td>183</td><td>193</td><td>186</td><td>249</td><td>272</td><td>272</td><td>272</td><td>232</td><td>232</td><td>265</td><td>264</td><td>284</td><td>247</td><td>244</td><td>259</td><td>336</td><td>341</td><td>305</td><td>291</td><td>367</td><td>319</td><td>364</td><td>300</td><td>380</td><td>395</td><td>325</td></tr><tr><td>Israel</td><td>93</td><td>117</td><td>120</td><td>120</td><td>202</td><td>104</td><td>179</td><td>215</td><td>187</td><td>188</td><td>205</td><td>275</td><td>238</td><td>236</td><td>318</td><td>237</td><td>310</td><td>181</td><td>154</td><td>290</td><td>268</td><td>241</td><td>233</td><td>427</td><td>158</td><td>318</td></tr><tr><td>Japan</td><td>1,544</td><td>1,788</td><td>1,988</td><td>2,912</td><td>2,292</td><td>3,071</td><td>2,762</td><td>2,923</td><td>2,748</td><td>2,255</td><td>2,673</td><td>2,045</td><td>2,421</td><td>2,343</td><td>3,160</td><td>3,342</td><td>3,066</td><td>6,156</td><td>3,108</td><td>4,242</td><td>2,901</td><td>3,146</td><td>3,737</td><td>3,168</td><td>3,137</td><td>3,970</td></tr><tr><td>Korea</td><td>852</td><td>717</td><td>1,027</td><td>911</td><td>1,089</td><td>1,304</td><td>993</td><td>955</td><td>958</td><td>888</td><td>1,038</td><td>658</td><td>556</td><td>536</td><td>877</td><td>817</td><td>870</td><td>887</td><td>875</td><td>1,150</td><td>922</td><td>1,044</td><td>1,180</td><td>913</td><td>756</td><td>1,370</td></tr><tr><td>Latvia</td><td>124</td><td>186</td><td>146</td><td>156</td><td>210</td><td>233</td><td>458</td><td>458</td><td>377</td><td>353</td><td>305</td><td>324</td><td>246</td><td>218</td><td>337</td><td>955</td><td>907</td><td>407</td><td>388</td><td>268</td><td>783</td><td>981</td><td>1,482</td><td>1,499</td><td>1,518</td><td>1,334</td></tr><tr><td>Netherlands</td><td>445</td><td>919</td><td>903</td><td>531</td><td>928</td><td>875</td><td>539</td><td>1,100</td><td>866</td><td>728</td><td>519</td><td>661</td><td>614</td><td>1,501</td><td>2,733</td><td>2,691</td><td>2,221</td><td>1,879</td><td>3,142</td><td>2,525</td><td>2,094</td><td>1,338</td><td>2,780</td><td>2,899</td><td>1,649</td><td>2,068</td></tr><tr><td>Sweden</td><td>669</td><td>837</td><td>995</td><td>766</td><td>1,107</td><td>1,469</td><td>1,569</td><td>1,579</td><td>1,512</td><td>1,642</td><td>1,371</td><td>951</td><td>1,335</td><td>1,991</td><td>1,041</td><td>2,371</td><td>1,965</td><td>1,886</td><td>2,080</td><td>6,070</td><td>4,771</td><td>2,147</td><td>2,627</td><td>1,919</td><td>1,974</td><td>5,587</td></tr><tr><td>Taiwan</td><td>344</td><td>374</td><td>405</td><td>444</td><td>461</td><td>613</td><td>672</td><td>626</td><td>635</td><td>648</td><td>625</td><td>631</td><td>512</td><td>549</td><td>590</td><td>548</td><td>446</td><td>699</td><td>837</td><td>633</td><td>690</td><td>578</td><td>776</td><td>733</td><td>743</td><td>1,288</td></tr><tr><td>US</td><td>1,344</td><td>1,443</td><td>1,696</td><td>1,330</td><td>1,834</td><td>1,978</td><td>1,902</td><td>1,876</td><td>1,797</td><td>1,879</td><td>1,740</td><td>1,121</td><td>975</td><td>1,197</td><td>1,831</td><td>1,970</td><td>1,436</td><td>1,607</td><td>1,530</td><td>1,657</td><td>3,134</td><td>1,204</td><td>1,376</td><td>709</td><td>682</td><td>1,382</td></tr><tr><td>Others</td><td>208</td><td>287</td><td>317</td><td>340</td><td>346</td><td>422</td><td>417</td><td>407</td><td>403</td><td>403</td><td>403</td><td>434</td><td>338</td><td>338</td><td>338</td><td>623</td><td>623</td><td>653</td><td>653</td><td>653</td><td>582</td><td>582</td><td>616</td><td>616</td><td>616</td><td>824</td></tr><tr><td>Total RMHS</td><td>5,778</td><td>6,784</td><td>7,750</td><td>6,758</td><td>8,736</td><td>10,355</td><td>9,483</td><td>10,453</td><td>9,693</td><td>9,143</td><td>9,300</td><td>7,256</td><td>7,159</td><td>8,788</td><td>13,076</td><td>13,968</td><td>11,558</td><td>11,485</td><td>13,029</td><td>13,938</td><td>11,472</td><td>11,635</td><td>15,296</td><td>13,337</td><td>9,775</td><td>16,454</td></tr></table>

Source: China Customs, JEF

Table 2 - Quarterly SPE Imports YoY by Key Countries

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Germany</td><td>-21%</td><td>-23%</td><td>-40%</td><td>50%</td><td>67%</td><td>41%</td><td>47%</td><td>25%</td><td>-14%</td><td>-3%</td><td>-3%</td><td>-38%</td><td>6%</td><td>-19%</td><td>36%</td><td>74%</td><td>38%</td><td>43%</td><td>-19%</td><td>5%</td><td>-6%</td><td>19%</td><td>3%</td><td>4%</td><td>-39%</td><td>-42%</td></tr><tr><td>Israel</td><td>166%</td><td>-27%</td><td>35%</td><td>0%</td><td>116%</td><td>-31%</td><td>39%</td><td>110%</td><td>-10%</td><td>-43%</td><td>54%</td><td>10%</td><td>-10%</td><td>-55%</td><td>-14%</td><td>31%</td><td>23%</td><td>-52%</td><td>-23%</td><td>-13%</td><td>33%</td><td>-12%</td><td>47%</td><td>-7%</td><td>-34%</td><td>-19%</td></tr><tr><td>Japan</td><td>30%</td><td>40%</td><td>27%</td><td>11%</td><td>48%</td><td>72%</td><td>39%</td><td>53%</td><td>20%</td><td>-27%</td><td>-3%</td><td>-30%</td><td>-12%</td><td>4%</td><td>18%</td><td>63%</td><td>27%</td><td>35%</td><td>-2%</td><td>25%</td><td>-5%</td><td>0%</td><td>20%</td><td>-25%</td><td>-20%</td><td>-20%</td></tr><tr><td>Korea</td><td>24%</td><td>-6%</td><td>32%</td><td>4%</td><td>28%</td><td>82%</td><td>-3%</td><td>5%</td><td>-14%</td><td>-32%</td><td>5%</td><td>-31%</td><td>-43%</td><td>-33%</td><td>-15%</td><td>24%</td><td>63%</td><td>50%</td><td>0%</td><td>38%</td><td>6%</td><td>-18%</td><td>35%</td><td>-29%</td><td>-18%</td><td>-15%</td></tr><tr><td>Russia</td><td>246%</td><td>-10%</td><td>32%</td><td>52%</td><td>70%</td><td>-15%</td><td>65%</td><td>194%</td><td>-7%</td><td>-86%</td><td>64%</td><td>-29%</td><td>-61%</td><td>-55%</td><td>49%</td><td>190%</td><td>188%</td><td>61%</td><td>-41%</td><td>-11%</td><td>87%</td><td>143%</td><td>274%</td><td>-7%</td><td>27%</td><td>-10%</td></tr><tr><td>Netherlands</td><td>75%</td><td>135%</td><td>167%</td><td>-24%</td><td>108%</td><td>-5%</td><td>-40%</td><td>107%</td><td>-7%</td><td>-17%</td><td>-4%</td><td>-40%</td><td>-29%</td><td>106%</td><td>426%</td><td>307%</td><td>262%</td><td>25%</td><td>-15%</td><td>-6%</td><td>-29%</td><td>-29%</td><td>-124%</td><td>54%</td><td>-21%</td><td>-21%</td></tr><tr><td>Other</td><td>200%</td><td>-20%</td><td>54%</td><td>6%</td><td>65%</td><td>-1%</td><td>48%</td><td>106%</td><td>37%</td><td>-10%</td><td>-7%</td><td>-40%</td><td>-25%</td><td>-5%</td><td>49%</td><td>149%</td><td>91%</td><td>36%</td><td>-25%</td><td>-32%</td><td>-18%</td><td>-14%</td><td>26%</td><td>-15%</td><td>-1%</td><td>20%</td></tr><tr><td>Taiwan</td><td>-40%</td><td>-17%</td><td>7%</td><td>26%</td><td>34%</td><td>64%</td><td>66%</td><td>42%</td><td>38%</td><td>6%</td><td>-7%</td><td>0%</td><td>-19%</td><td>-15%</td><td>-6%</td><td>-13%</td><td>-13%</td><td>27%</td><td>42%</td><td>15%</td><td>55%</td><td>-17%</td><td>-7%</td><td>-10%</td><td>8%</td><td>18%</td></tr><tr><td>US</td><td>90%</td><td>15%</td><td>27%</td><td>7%</td><td>36%</td><td>37%</td><td>12%</td><td>41%</td><td>-2%</td><td>-5%</td><td>-9%</td><td>-40%</td><td>-46%</td><td>-36%</td><td>5%</td><td>76%</td><td>47%</td><td>34%</td><td>-16%</td><td>-18%</td><td>-8%</td><td>-25%</td><td>-10%</td><td>-57%</td><td>-48%</td><td>-33%</td></tr><tr><td>Others</td><td>15%</td><td>15%</td><td>23%</td><td>33%</td><td>73%</td><td>25%</td><td>36%</td><td>13%</td><td>-2%</td><td>-9%</td><td>4%</td><td>7%</td><td>-17%</td><td>-14%</td><td>32%</td><td>44%</td><td>22%</td><td>15%</td><td>-27%</td><td>7%</td><td>-18%</td><td>27%</td><td>-27%</td><td>-17%</td><td>-18%</td><td></td></tr><tr><td>Total</td><td>42%</td><td>23%</td><td>33%</td><td>7%</td><td>51%</td><td>53%</td><td>22%</td><td>55%</td><td>11%</td><td>-32%</td><td>-1%</td><td>-31%</td><td>-26%</td><td>-4%</td><td>39%</td><td>92%</td><td>61%</td><td>31%</td><td>0%</td><td>0%</td><td>-1%</td><td>-1%</td><td>17%</td><td>-4%</td><td>-16%</td><td>-13%</td></tr></table>

Source: China customs, JEF

Table 3 - Quarterly SPE Imports by Key Product Categories (US\$m)

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Wafer Fabrication</td><td>2,906</td><td>3,488</td><td>3,839</td><td>3,302</td><td>4,928</td><td>6,027</td><td>4,723</td><td>5,458</td><td>5,173</td><td>4,702</td><td>4,876</td><td>3,915</td><td>4,060</td><td>5,152</td><td>8,801</td><td>9,353</td><td>7,764</td><td>7,527</td><td>8,826</td><td>9,378</td><td>7,377</td><td>7,629</td><td>10,175</td><td>9,240</td><td>6,504</td><td>10,719</td></tr><tr><td>Inspecting &amp; Testing</td><td>548</td><td>615</td><td>597</td><td>451</td><td>725</td><td>803</td><td>881</td><td>1,022</td><td>883</td><td>1,037</td><td>1,079</td><td>942</td><td>805</td><td>1,141</td><td>1,531</td><td>1,418</td><td>1,078</td><td>1,059</td><td>1,291</td><td>1,607</td><td>1,207</td><td>1,051</td><td>1,661</td><td>1,062</td><td>778</td><td>1,567</td></tr><tr><td>Other</td><td>274</td><td>343</td><td>518</td><td>493</td><td>577</td><td>724</td><td>845</td><td>795</td><td>634</td><td>651</td><td>501</td><td>328</td><td>312</td><td>334</td><td>355</td><td>377</td><td>294</td><td>350</td><td>360</td><td>340</td><td>315</td><td>320</td><td>398</td><td>481</td><td>296</td><td>463</td></tr><tr><td>Cristival Gruwine</td><td>189</td><td>226</td><td>212</td><td>231</td><td>2

[中间内容因长度限制已省略]

the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
