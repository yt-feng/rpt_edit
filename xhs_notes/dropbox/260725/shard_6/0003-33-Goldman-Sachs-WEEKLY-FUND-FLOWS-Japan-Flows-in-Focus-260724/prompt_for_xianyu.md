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
# WEEKLY FUND FLOWS Japan Flows in Focus

## Global fund flows, week ending July 22

■ Flows into mutual funds and related investment products were positive across both equities and fixed income.

Lexi Kanter
+1(212)855-9701 |
alexandra.kanter@gs.com
GS & Co. LLC

\- Net flows into global equity funds remained positive in the week ending July 22 (+\$30bn vs +\$56bn in the previous week). DM funds saw outflows across the board outside of Japan. US funds drove the net outflows. Within EM, Mainland China, Korea, and Taiwan funds drove the net inflows. At the sector level, technology funds continued to see the largest net inflows while industrial funds saw the largest net outflows.

Flows into global fixed income funds remained well-supported from inflows across fund types. Short-duration bond funds and inflation-protected bond funds have seen sustained inflows. In EM, hard-currency and local currency bond funds saw net inflows. Money market fund assets decreased by -\$34bn. At the country level, domestic flows into Japan bond funds have seen a recent increase (see Chart of the Week). These data capture primarily retail flows and while the recent increase seems to predate comments from Japan's MoF officials which suggested that the administration is focused on encouraging greater domestic investment, we recently noted meaningful repatriation flows—if they occur—would be a source of support for the Yen.

Cross-border FX flows were largely positive, and USD and GBP saw the strongest net demand.

<table><tr><td rowspan="3"></td><td colspan="4">Global Fund Flows Summary</td></tr><tr><td colspan="2">Millions USD</td><td colspan="2">% AUM</td></tr><tr><td>4wk sum</td><td>22-Jul</td><td>4wk avg</td><td>22-Jul</td></tr><tr><td>Equity</td><td>128,677</td><td>30,425</td><td>0.10</td><td>0.10</td></tr><tr><td>Fixed Income</td><td>95,626</td><td>15,136</td><td>0.24</td><td>0.15</td></tr><tr><td>of which: EM</td><td>3,219</td><td>871</td><td>0.11</td><td>0.12</td></tr><tr><td>Money Markets</td><td>-58,933</td><td>-33,856</td><td>-0.13</td><td>-0.30</td></tr><tr><td>FX Flows*</td><td>71,945</td><td>17,066</td><td>0.11</td><td>0.10</td></tr></table>

\*Cross-border fund flows, excluding hard currency and FX-hedged funds  
Source: EPFR, Haver Analytics, GS Global Investment Research

Chart of the Week  
![](images/f108d9005ad08f0871e521f6b373fc59a260ff7b080ea30c59015bf46e97886a.jpg)  
Source: EPFR, Haver Analytics, GS Global Investment Research

## Global Fund Flow Trends

![](images/55fe97df461e64f5e8afa7f18acedabc8a73023364cb08f11a4a14a56495bc84.jpg)  
Source: EPFR, GS Global Investment Research

![](images/33b2aff7f2b2eaf1b8deb8c8bf40104696f52730a66e75903b8181d8764e1dc2.jpg)  
Source: EPFR, GS Global Investment Research

![](images/76fd99ce365a8d07d24f8546fece9cd650b8a4009399ab0e806ca76c2e589b32.jpg)

Source: EPFR, GS Global Investment Research  
![](images/73dbcfb7264fd4e5044f02665275de37da44606a9c03e572d79a8caa566293c7.jpg)  
Captures flows to sector-dedicated funds

![](images/0207a6707e7b6e1ce21d823c4bf6ee6ba941f4b42ede8b7537377352c149d476.jpg)  
Captures flows to sector dedicated funds

Source: EPFR, GS Global Investment Research  
![](images/b081a1789168dbf30355caebadcfbb3ff8f3f84325645307014082761e7e2aad.jpg)  
Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

Source: EPFR, GS Global Investment Research  
![](images/2e84b2a80bda6836e6a869899d022472f4296f73f38d15c9760d84a8ac8ae813.jpg)  
Captures flows to country- and region-dedicated funds  
Source: EPFR, GS Global Investment Research

![](images/435f49fdf93f82c2778585ce10516a4dcb4aa65cdc5301940dcf2a85d7cc1264.jpg)  
Source: EPFR, GS Global Investment Research

![](images/6d2efacb9fa0b28e5d1eccaec7e854846c0149363065e43b7378bfb93f76b9ee.jpg)  
Source: EPFR, GS Global Investment Research

Total Unhedged Foreign Flows By Country  
![](images/a6716567994c5812000ead6cabf4e3d58e7a74758c08b1e9f9ea87ccb4132bd6.jpg)

![](images/0d2ee55942ba5c50e8c6c6d128ff800a85dcd5858bed48d63881ffcdd40f215b.jpg)

![](images/13a4735aea90f7410d244acb99d397bf1f3d3b74de3e57642c620f2a4e102ab6.jpg)

![](images/6d82e75cc4a3521a99177fe215c137a2e68e13beaf67e6fae125858cefad8ff7.jpg)  
Source: EPFR, GS Global Investment Research

![](images/837c6f7de11be8091304805406f7f5c30a29c12e27c219bf683421be16ae1ce1.jpg)

![](images/8e77df646166096cee79971ef69e43d8cdc38ef789628e8d02505d19c5e4d42b.jpg)

Net Unhedged Flows into US Equity Funds  
![](images/ecdb5204b1a80d5de530c486e90aa4880377c56cfd739584a6b3b69016995923.jpg)  
Source: EPFR, Haver Analytics, GS Global Investment Research

Fixed Income & Equity Flows

<table><tr><td rowspan="3"></td><td colspan="8">Global Fund Flows</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>22-Jul</td><td>15-Jul</td><td>8-Jul</td><td>1-Jul</td><td>4wk avg</td><td>22-Jul</td></tr><tr><td>Total Equity</td><td>128,677</td><td>30,425</td><td>55,759</td><td>56,352</td><td>-13,859</td><td>0.10</td><td>0.10</td><td>1.75</td></tr><tr><td> $Global\ Benchmarks^1$ </td><td>40,010</td><td>6,800</td><td>11,729</td><td>12,561</td><td>8,921</td><td>0.13</td><td>0.09</td><td>1.32</td></tr><tr><td>Including US</td><td>28,748</td><td>3,952</td><td>8,801</td><td>10,410</td><td>5,584</td><td>0.13</td><td>0.07</td><td>1.49</td></tr><tr><td>Excluding US</td><td>11,263</td><td>2,848</td><td>2,927</td><td>2,150</td><td>3,337</td><td>0.12</td><td>0.12</td><td>0.56</td></tr><tr><td>Developed Markets2</td><td>23,133</td><td>-5,972</td><td>19,047</td><td>28,808</td><td>-18,751</td><td>0.03</td><td>-0.03</td><td>-0.37</td></tr><tr><td>US</td><td>16,397</td><td>-7,227</td><td>15,735</td><td>25,096</td><td>-17,207</td><td>0.02</td><td>-0.04</td><td>-0.54</td></tr><tr><td>Western Europe</td><td>-4,201</td><td>-1,557</td><td>684</td><td>376</td><td>-3,704</td><td>-0.05</td><td>-0.07</td><td>-0.41</td></tr><tr><td>UK-dedicated</td><td>-1,750</td><td>-1,209</td><td>-561</td><td>102</td><td>-81</td><td>-0.13</td><td>-0.36</td><td>0.25</td></tr><tr><td>Other</td><td>-2,451</td><td>-348</td><td>1,245</td><td>275</td><td>-3,623</td><td>-0.03</td><td>-0.02</td><td>-0.42</td></tr><tr><td>Japan</td><td>6,506</td><td>1,536</td><td>1,880</td><td>1,236</td><td>1,855</td><td>0.13</td><td>0.13</td><td>1.08</td></tr><tr><td>Other</td><td>4,431</td><td>1,276</td><td>749</td><td>2,101</td><td>306</td><td>0.26</td><td>0.30</td><td>1.35</td></tr><tr><td>Emerging Markets3</td><td>65,532</td><td>29,596</td><td>24,983</td><td>14,983</td><td>-4,030</td><td>0.56</td><td>1.02</td><td>2.70</td></tr><tr><td>Global EM Benchmarks</td><td>1,627</td><td>1,929</td><td>1,757</td><td>-46</td><td>-2,013</td><td>0.03</td><td>0.14</td><td>0.05</td></tr><tr><td>Mainland China</td><td>40,823</td><td>21,330</td><td>16,165</td><td>9,057</td><td>-5,729</td><td>1.59</td><td>3.31</td><td>1.67</td></tr><tr><td>Taiwan</td><td>12,655</td><td>4,790</td><td>2,804</td><td>2,635</td><td>2,426</td><td>1.29</td><td>1.99</td><td>3.75</td></tr><tr><td>Korea</td><td>16,337</td><td>1,490</td><td>6,292</td><td>4,009</td><td>4,545</td><td>2.09</td><td>0.82</td><td>3.90</td></tr><tr><td>India</td><td>-661</td><td>17</td><td>-203</td><td>-225</td><td>-250</td><td>-0.20</td><td>0.02</td><td>-0.70</td></tr><tr><td>Brazil</td><td>-270</td><td>414</td><td>-397</td><td>-137</td><td>-151</td><td>-0.29</td><td>1.72</td><td>-0.59</td></tr><tr><td>Other</td><td>-4,979</td><td>-373</td><td>-1,435</td><td>-311</td><td>-2,859</td><td>-0.33</td><td>-0.10</td><td>-2.01</td></tr><tr><td colspan="9">Equity Sector Flows</td></tr><tr><td>Commodities/Materials</td><td>-1,114</td><td>-628</td><td>24</td><td>1,334</td><td>-1,843</td><td>-0.10</td><td>-0.24</td><td>-0.36</td></tr><tr><td>Consumer Goods</td><td>-1,614</td><td>-462</td><td>-1,863</td><td>299</td><td>412</td><td>-0.20</td><td>-0.23</td><td>-0.12</td></tr><tr><td>Energy</td><td>-4,468</td><td>421</td><td>653</td><td>60</td><td>-5,602</td><td>-0.36</td><td>0.13</td><td>-0.88</td></tr><tr><td>Financials</td><td>13,110</td><td>1,689</td><td>4,023</td><td>3,390</td><td>4,008</td><td>0.71</td><td>0.36</td><td>2.22</td></tr><tr><td>Health Care</td><td>6,446</td><td>796</td><td>1,435</td><td>1,713</td><td>2,502</td><td>0.39</td><td>0.19</td><td>2.23</td></tr><tr><td>Industrials</td><td>36</td><td>-1,385</td><td>-381</td><td>990</td><td>812</td><td>0.00</td><td>-0.50</td><td>-0.73</td></tr><tr><td>Infrastructure</td><td>1,816</td><td>255</td><td>277</td><td>469</td><td>815</td><td>0.30</td><td>0.16</td><td>0.59</td></tr><tr><td>Real Estate</td><td>-561</td><td>-501</td><td>-757</td><td>926</td><td>-230</td><td>-0.02</td><td>-0.08</td><td>0.05</td></tr><tr><td>Technology</td><td>65,776</td><td>3,544</td><td>17,439</td><td>28,855</td><td>15,937</td><td>0.70</td><td>0.15</td><td>4.57</td></tr><tr><td>Telecom</td><td>2,932</td><td>-437</td><td>-291</td><td>497</td><td>3,163</td><td>0.87</td><td>-0.53</td><td>1.66</td></tr><tr><td>Utilities</td><td>1,410</td><td>18</td><td>238</td><td>603</td><td>550</td><td>0.19</td><td>0.01</td><td>0.73</td></tr><tr><td>High  $Beta^4$ </td><td>7,933</td><td>258</td><td>2,554</td><td>4,217</td><td>904</td><td>0.29</td><td>0.04</td><td>0.57</td></tr><tr><td>Low  $Beta^4$ </td><td>-961</td><td>-670</td><td>-1,291</td><td>962</td><td>38</td><td>-0.03</td><td>-0.10</td><td>0.36</td></tr><tr><td>Total Fixed Income</td><td>95,626</td><td>15,136</td><td>19,840</td><td>31,414</td><td>29,236</td><td>0.24</td><td>0.15</td><td>1.42</td></tr><tr><td>Developed Markets5</td><td>92,010</td><td>13,980</td><td>19,169</td><td>30,625</td><td>28,237</td><td>0.25</td><td>0.15</td><td>1.65</td></tr><tr><td>Government</td><td>25,340</td><td>5,700</td><td>6,479</td><td>8,425</td><td>4,736</td><td>0.39</td><td>0.35</td><td>1.66</td></tr><tr><td>Mortgage-backed</td><td>1,387</td><td>302</td><td>459</td><td>332</td><td>293</td><td>0.11</td><td>0.10</td><td>-0.48</td></tr><tr><td>Municipal</td><td>5,841</td><td>262</td><td>1,843</td><td>1,877</td><td>1,859</td><td>0.21</td><td>0.04</td><td>0.98</td></tr><tr><td>Agg-type</td><td>27,233</td><td>3,589</td><td>6,209</td><td>8,219</td><td>9,215</td><td>0.24</td><td>0.12</td><td>0.94</td></tr><tr><td>IG Credit</td><td>8,577</td><td>816</td><td>890</td><td>3,570</td><td>3,301</td><td>0.19</td><td>0.07</td><td>0.48</td></tr><tr><td>High yield</td><td>5,521</td><td>396</td><td>-246</td><td>2,021</td><td>3,350</td><td>0.20</td><td>0.06</td><td>0.52</td></tr><tr><td>Bank loan</td><td>3,856</td><td>955</td><td>567</td><td>1,528</td><td>806</td><td>0.52</td><td>0.51</td><td>0.75</td></tr><tr><td>Long-duration6</td><td>5,584</td><td>1,306</td><td>1,940</td><td>1,214</td><td>1,124</td><td>0.27</td><td>0.26</td><td>0.07</td></tr><tr><td>Short-duration6</td><td>26,940</td><td>5,695</td><td>4,395</td><td>10,273</td><td>6,576</td><td>0.29</td><td>0.24</td><td>1.23</td></tr><tr><td>Inflation-protected</td><td>1,713</td><td>391</td><td>586</td><td>442</td><td>294</td><td>0.25</td><td>0.22</td><td>0.94</td></tr><tr><td>Emerging Markets</td><td>3,219</td><td>871</td><td>878</td><td>631</td><td>838</td><td>0.11</td><td>0.12</td><td>0.27</td></tr><tr><td>Hard</td><td>1,053</td><td>155</td><td>397</td><td>339</td><td>162</td><td>0.10</td><td>0.06</td><td>0.64</td></tr><tr><td>Blend</td><td>794</td><td>450</td><td>132</td><td>293</td><td>-81</td><td>0.29</td><td>0.65</td><td>1.07</td></tr><tr><td>Local</td><td>1,372</td><td>266</td><td>348.4</td><td>0</td><td>757</td><td>0.09</td><td>0.07</td><td>-0.13</td></tr><tr><td>Money Markets</td><td>-58,933</td><td>-33,856</td><td>-119,614</td><td>39,538</td><td>54,999</td><td>-0.13</td><td>-0.30</td><td>-1.81</td></tr></table>

1. Primarily MSCI World and MSCI ACWI benchmarks. 2. Sum of DM country- and region-dedicated funds; excludes global DM benchmark funds (e.g. MSCI World funds). 3. Sum of Global EM benchmark funds and EM country- and region-dedicated funds. 4. High beta funds include commodity, financial, & industrial sector funds. Low beta funds include consumer goods, real estate, & utility sector funds. 5. Benchmarks may include some investment grade EM bonds; categories below include DM & EM funds. 6. Long-duration includes long-term Agg-type, long-term corporate, and long-term government bond funds. Short-duration includes short-term Agg-type, short-term corporate, and short-term government bond funds.  
Source: EPFR, Haver Analytics, GS Global Investment Research

FX Flows

<table><tr><td rowspan="3"></td><td colspan="8">FX Flows1</td></tr><tr><td colspan="5">Millions USD</td><td colspan="2">% AUM</td><td rowspan="2">Z-score of 4wk sum</td></tr><tr><td>4wk sum</td><td>22-Jul</td><td>15-Jul</td><td>8-Jul</td><td>1-Jul</td><td>4wk avg</td><td>22-Jul</td></tr><tr><td>Total</td><td>71,945</td><td>17,066</td><td>24,827</td><td>26,241</td><td>3,811</td><td>0.11</td><td>0.10</td><td>0.98</td></tr><tr><td>G10</td><td>54,260</td><td>11,272</td><td>16,601</td><td>18,814</td><td>7,573</td><td>0.13</td><td>0.10</td><td>1.32</td></tr><tr><td>USD</td><td>34,441</td><td>8,395</td><td>9,757</td><td>11,464</td><td>4,825</td><td>0.14</td><td>0.14</td><td>1.13</td></tr><tr><td>EUR</td><td>4,640</td><td>413</td><td>1,459</td><td>1,553</td><td>1,215</td><td>0.09</td><td>0.03</td><td>0.35</td></tr><tr><td>GBP</td><td>5,853</td><td>1,329</td><td>1,784</td><td>1,890</td><td>850</td><td>0.14</td><td>0.13</td><td>1.14</td></tr><tr><td>AUD</td><td>281</td><td>143</td><td>52</td><td>278</td><td>-192</td><td>0.04</td><td>0.07</td><td>-0.10</td></tr><tr><td>NZD</td><td>70</td><td>25</td><td>13</td><td>25</td><td>6</td><td>0.13</td><td>0.19</td><td>1.01</td></tr><tr><td>CAD</td><td>1,589</td><td>395</td><td>336</td><td>745</td><td>112</td><td>0.11</td><td>0.11</td><td>0.75</td></tr><tr><td>CHF</td><td>1,616</td><td>360</td><td>674</td><td>560</td><td>22</td><td>0.09</td><td>0.08</td><td>0.60</td></tr><tr><td>NOK</td><td>540</td><td>97</td><td>168</td><td>209</td><td>66</td><td>0.14</td><td>0.10</td><td>1.29</td></tr><tr><td>SEK</td><td>1,129</td><td>124</td><td>483</td><td>356</td><td>166</td><td>0.12</td><td>0.05</td><td>1.13</td></tr><tr><td>JPY</td><td>4,102</td><td>-9</td><td>1,875</td><td>1,733</td><td>503</td><td>0.11</td><td>0.00</td><td>0.79</td></tr><tr><td>Asia</td><td>4,206</td><td>2,397</td><td>5,249</td><td>14</td><td>-3,453</td><td>0.04</td><td>0.10</td><td>0.25</td></tr><tr><td>CNY</td><td>-3,033</td><td>239</td><td>-314</td><td>-1,232</td><td>-1,727</td><td>-0.10</td><td>0.03</td><td>-0.59</td></tr><tr><td>HKD</td><td>243</td><td>75</td><td>77</td><td>106</td><td>-15</td><td>0.05</td><td>0.07</td><td>0.27</td></tr><tr><td>INR</td><td>-650</td><td>241</td><td>-84</td><td>-236</td><td>-571</td><td>-0.06</td><td>0.09</td><td>-0.70</td></tr><tr><td>KRW</td><td>6,650</td><td>977</td><td>4,881</td><td>1,049</td><td>-257</td><td>0.30</td><td>0.17</td><td>2.64</td></tr><tr><td>MYR</td><td>65</td><td>64</td><td>46</td><td>12</td><td>-57</td><td>0.05</td><td>0.19</td><td>0.19</td></tr><tr><td>SGD</td><td>294</td><td>107</td><td>75</td><td>93</td><td>20</td><td>0.08</td><td>0.12</td><td>0.91</td></tr><tr><td>TWD</td><td>295</td><td>514</td><td>412</td><td>163</td><td>-794</td><td>0.01</td><td>0.09</td><td>-0.02</td></tr><tr><td>THB</td><td>32</td><td>59</td><td>33</td><td>-2</td><td>-58</td><td>0.02</td><td>0.15</td><td>0.06</td></tr><tr><td>IDR</td><td>261</td><td>87</td><td>97</td><td>58</td><td>18</td><td>0.15</td><td>0.20</td><td>0.67</td></tr><tr><td>PHP</td><td>51</td><td>33</td><td>26</td><td>2</td><td>-11</td><td>0.07</td><td>0.18</td><td>0.34</td></tr><tr><td>Americas</td><td>313</td><td>616</td><td>153</td><td>113</td><td>-569</td><td>0.02</td><td>0.16</td><td>-0.25</td></tr><tr><td>ARS</td><td>17</td><td>16</td><td>12</td><td>0</td><td>-11</td><td>0.05</td><td

[中间内容因长度限制已省略]

ttempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
