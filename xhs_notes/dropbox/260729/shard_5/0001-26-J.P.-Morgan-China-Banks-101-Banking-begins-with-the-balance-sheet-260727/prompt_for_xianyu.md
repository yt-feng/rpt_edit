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
# China Banks 101

## Banking begins with the balance sheet

China Financials
Katherine Lei AC
(852) 2800-8552
katherine.lei@JPM.com
JPM Securities (Asia Pacific) Limited/ JPM
Broking (Hong Kong) Limited

China Financials
Lincoln Yu
(852) 2800-8523
lincoln.yu@JPM.com
JPM Securities (Asia Pacific) Limited / JPM
Broking (Hong Kong) Limited

China Financials
Peter Zhang
(852) 2800-8557
peter.zhang@JPM.com
JPM Securities (Asia Pacific) Limited / JPM Broking (Hong Kong) Limited

China Financials
Haomin Chen
(86-21) 6106-6347
haomin.chen@JPM.com
SAC Registration Number: S1730524080002
JPM Securities (China) Company Limited

See the end pages of this presentation for analyst certification and important disclosures, including non-US analyst disclosures.

Banking Basics

## Basic P&L analysis

<table><tr><td>Sample P&amp;L</td><td>Yr Y</td><td></td></tr><tr><td>Interest Income</td><td>170</td><td rowspan="3">NIM=NII/Avg IEA=100/Avg(2850,3135)=3.3%</td></tr><tr><td>Interest Expense</td><td>-70</td></tr><tr><td>Net Interest Income (NII)</td><td>100</td></tr><tr><td>Non-Interest Income</td><td>10</td><td rowspan="3">CIR=Operating Expense/Total Income=50/110=45%</td></tr><tr><td>Total Income</td><td>110</td></tr><tr><td>Operating expenses</td><td>-50</td></tr><tr><td>Staff costs</td><td>-30</td><td rowspan="9">Credit Costs=LLP/Avg Gross Loans=8/Avg(1209,1335)=0.63%</td></tr><tr><td>Other operating expenses</td><td>-20</td></tr><tr><td>PPOP</td><td>60</td></tr><tr><td>Loan Loss Provisions (LLP)</td><td>-8</td></tr><tr><td>Pre-Tax</td><td>52</td></tr><tr><td>Income Tax</td><td>-10</td></tr><tr><td>Net profits before minorities</td><td>42</td></tr><tr><td>Minorities</td><td>-5</td></tr><tr><td>Attributable Income</td><td>37</td></tr></table>

Source: JPM. Note: For illustration only.

<table><tr><td>Sample Balance Sheet</td><td>Yr Y-1</td><td>Yr Y</td></tr><tr><td>Cash &amp; bal. with other banks</td><td>23</td><td>25</td></tr><tr><td>Balance with Central banks</td><td>385</td><td>424</td></tr><tr><td>Other Interbank</td><td>648</td><td>713</td></tr><tr><td>Net loans &amp; advances</td><td>1,159</td><td>1,275</td></tr><tr><td>Gross Loans</td><td>1,209</td><td>1,335</td></tr><tr><td>Provisions</td><td>(50)</td><td>(60)</td></tr><tr><td>Investments</td><td>725</td><td>798</td></tr><tr><td>Fixed Assets</td><td>22</td><td>24</td></tr><tr><td>Goodwill</td><td>3</td><td>3</td></tr><tr><td>Other Assets</td><td>34</td><td>37</td></tr><tr><td>Investment in associates</td><td>1</td><td>1</td></tr><tr><td>TOTAL ASSETS</td><td>3000</td><td>3,300</td></tr><tr><td>Interbank</td><td>635</td><td>699</td></tr><tr><td>Deposits</td><td>2,037</td><td>2,240</td></tr><tr><td>Sub-debts</td><td>16</td><td>17</td></tr><tr><td>Financial liabilities FVPL</td><td>35</td><td>39</td></tr><tr><td>Other Liabilities</td><td>54</td><td>60</td></tr><tr><td>TOTAL LIABILITIES</td><td>2,777</td><td>3,055</td></tr><tr><td>Equity</td><td>221</td><td>243</td></tr><tr><td>Paid-in capital</td><td>64</td><td>71</td></tr><tr><td>Capital surplus</td><td>64</td><td>70</td></tr><tr><td>Reserves</td><td>60</td><td>66</td></tr><tr><td>Investment revaluation reserve</td><td>(0)</td><td>(0)</td></tr><tr><td>Retained earnings</td><td>33</td><td>36</td></tr><tr><td>Other reserves</td><td>-</td><td>-</td></tr><tr><td>Minorities</td><td>2</td><td>2</td></tr><tr><td>TOTAL LIABILITIES &amp; EQUITIES</td><td>3,000</td><td>3,300</td></tr><tr><td>NPL</td><td>17</td><td>20</td></tr><tr><td>RWA</td><td>1,800</td><td>1,980</td></tr><tr><td>IEA</td><td>2,850</td><td>3,135</td></tr></table>

## Basic balance sheet analysis

<table><tr><td>Sample Balance Sheet</td><td>Yr Y-1</td><td>Yr Y</td></tr><tr><td>Cash &amp; bal. with other banks</td><td>23</td><td>25</td></tr><tr><td>Balance with Central banks</td><td>385</td><td>424</td></tr><tr><td>Other Interbank</td><td>648</td><td>713</td></tr><tr><td>Net loans &amp; advances</td><td>1,159</td><td>1,275</td></tr><tr><td>Gross Loans</td><td>1,209</td><td>1,335</td></tr><tr><td>Provisions</td><td>(50)</td><td>(60)</td></tr><tr><td>Investments</td><td>725</td><td>798</td></tr><tr><td>Fixed Assets</td><td>22</td><td>24</td></tr><tr><td>Goodwill</td><td>3</td><td>3</td></tr><tr><td>Other Assets</td><td>34</td><td>37</td></tr><tr><td>Investment in associates</td><td>1</td><td>1</td></tr><tr><td>TOTAL ASSETS</td><td>3000</td><td>3,300</td></tr><tr><td>Interbank</td><td>635</td><td>699</td></tr><tr><td>Deposits</td><td>2,037</td><td>2,240</td></tr><tr><td>Sub-debts</td><td>16</td><td>17</td></tr><tr><td>Financial liabilities FVPL</td><td>35</td><td>39</td></tr><tr><td>Other Liabilities</td><td>54</td><td>60</td></tr><tr><td>TOTAL LIABILITIES</td><td>2,777</td><td>3,055</td></tr><tr><td>Equity</td><td>221</td><td>243</td></tr><tr><td>Paid-in capital</td><td>64</td><td>71</td></tr><tr><td>Capital surplus</td><td>64</td><td>70</td></tr><tr><td>Reserves</td><td>60</td><td>66</td></tr><tr><td>Investment revaluation reserve</td><td>(0)</td><td>(0)</td></tr><tr><td>Retained earnings</td><td>33</td><td>36</td></tr><tr><td>Other reserves</td><td>-</td><td>-</td></tr><tr><td>Minorities</td><td>2</td><td>2</td></tr><tr><td>TOTAL LIABILITIES &amp; EQUITIES</td><td>3,000</td><td>3,300</td></tr><tr><td>NPL</td><td>17</td><td>20</td></tr><tr><td>RWA</td><td>1,800</td><td>1,980</td></tr><tr><td>IEA</td><td>2,850</td><td>3,135</td></tr></table>

Source: JPM. Note: For illustration only.

Key Metrics

## Key Metrics – DuPont Summary

<table><tr><td colspan="10">DuPont Summary – NIM, Non-II/Revenues, Revenue/Assets</td></tr><tr><td>NIM</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>China</td><td>1.98%</td><td>2.06%</td><td>2.27%</td><td>2.22%</td><td>2.11%</td><td>1.98%</td><td>1.74%</td><td>1.57%</td><td>1.47%</td></tr><tr><td>Hong Kong</td><td>1.73%</td><td>1.79%</td><td>1.77%</td><td>1.46%</td><td>1.38%</td><td>1.58%</td><td>1.89%</td><td>1.91%</td><td>1.90%</td></tr><tr><td>Korea</td><td>2.05%</td><td>2.06%</td><td>1.93%</td><td>1.73%</td><td>1.76%</td><td>1.94%</td><td>1.93%</td><td>1.86%</td><td>1.80%</td></tr><tr><td>Taiwan</td><td>1.14%</td><td>1.11%</td><td>1.03%</td><td>0.97%</td><td>0.97%</td><td>1.07%</td><td>0.95%</td><td>0.92%</td><td>1.02%</td></tr><tr><td>India</td><td>2.96%</td><td>3.06%</td><td>3.65%</td><td>3.79%</td><td>3.92%</td><td>3.86%</td><td>4.15%</td><td>4.16%</td><td>3.96%</td></tr><tr><td>Indonesia</td><td>6.31%</td><td>6.04%</td><td>5.90%</td><td>5.21%</td><td>5.64%</td><td>5.87%</td><td>5.89%</td><td>5.74%</td><td>5.56%</td></tr><tr><td>Malaysia</td><td>2.25%</td><td>2.23%</td><td>2.14%</td><td>2.05%</td><td>2.20%</td><td>2.29%</td><td>2.07%</td><td>2.00%</td><td>2.00%</td></tr><tr><td>Philippines</td><td>3.19%</td><td>3.33%</td><td>3.70%</td><td>4.04%</td><td>3.71%</td><td>3.79%</td><td>4.20%</td><td>4.23%</td><td>4.26%</td></tr><tr><td>Thailand</td><td>2.36%</td><td>2.31%</td><td>2.35%</td><td>2.81%</td><td>2.75%</td><td>2.87%</td><td>3.13%</td><td>3.14%</td><td>2.88%</td></tr><tr><td>Singapore</td><td>1.76%</td><td>1.84%</td><td>1.84%</td><td>1.79%</td><td>1.78%</td><td>1.69%</td><td>1.74%</td><td>1.68%</td><td>1.68%</td></tr><tr><td>Australia</td><td>1.72%</td><td>1.71%</td><td>1.68%</td><td>1.83%</td><td>1.83%</td><td>1.74%</td><td>1.93%</td><td>1.84%</td><td>1.84%</td></tr><tr><td colspan="10"></td></tr><tr><td>Non-NII/Rev</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>China</td><td>30%</td><td>30%</td><td>25%</td><td>24%</td><td>26%</td><td>25%</td><td>26%</td><td>28%</td><td>29%</td></tr><tr><td>Hong Kong</td><td>26%</td><td>26%</td><td>27%</td><td>33%</td><td>31%</td><td>24%</td><td>20%</td><td>24%</td><td>28%</td></tr><tr><td>Korea</td><td>13%</td><td>13%</td><td>16%</td><td>20%</td><td>22%</td><td>12%</td><td>18%</td><td>16%</td><td>19%</td></tr><tr><td>Taiwan</td><td>41%</td><td>41%</td><td>45%</td><td>43%</td><td>43%</td><td>33%</td><td>47%</td><td>52%</td><td>44%</td></tr><tr><td>India</td><td>32%</td><td>34%</td><td>30%</td><td>33%</td><td>28%</td><td>29%</td><td>26%</td><td>28%</td><td>29%</td></tr><tr><td>Indonesia</td><td>24%</td><td>25%</td><td>26%</td><td>27%</td><td>26%</td><td>24%</td><td>24%</td><td>25%</td><td>26%</td></tr><tr><td>Malaysia</td><td>28%</td><td>27%</td><td>27%</td><td>28%</td><td>24%</td><td>21%</td><td>23%</td><td>25%</td><td>26%</td></tr><tr><td>Philippines</td><td>30%</td><td>26%</td><td>28%</td><td>31%</td><td>28%</td><td>27%</td><td>24%</td><td>24%</td><td>25%</td></tr><tr><td>Thailand</td><td>35%</td><td>34%</td><td>35%</td><td>30%</td><td>31%</td><td>27%</td><td>24%</td><td>25%</td><td>30%</td></tr><tr><td>Singapore</td><td>39%</td><td>34%</td><td>37%</td><td>38%</td><td>40%</td><td>32%</td><td>31%</td><td>34%</td><td>36%</td></tr><tr><td>Australia</td><td>32%</td><td>30%</td><td>30%</td><td>28%</td><td>26%</td><td>26%</td><td>25%</td><td>25%</td><td>24%</td></tr><tr><td colspan="10"></td></tr><tr><td>Revenue/Average Assets</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>China</td><td>3.2%</td><td>3.2%</td><td>3.3%</td><td>3.3%</td><td>3.3%</td><td>2.9%</td><td>2.7%</td><td>2.8%</td><td>2.9%</td></tr><tr><td>Hong Kong</td><td>2.0%</td><td>2.1%</td><td>2.3%</td><td>2.3%</td><td>2.1%</td><td>2.0%</td><td>2.1%</td><td>2.2%</td><td>2.2%</td></tr><tr><td>Korea</td><td>3.2%</td><td>2.9%</td><td>2.5%</td><td>2.5%</td><td>2.3%</td><td>2.2%</td><td>2.3%</td><td>2.3%</td><td>2.2%</td></tr><tr><td>Taiwan</td><td>1.9%</td><td>2.0%</td><td>2.1%</td><td>2.2%</td><td>2.1%</td><td>2.0%</td><td>2.0%</td><td>2.0%</td><td>2.0%</td></tr><tr><td>India</td><td>4.6%</td><td>4.5%</td><td>4.5%</td><td>4.8%</td><td>5.3%</td><td>4.7%</td><td>5.9%</td><td>5.0%</td><td>4.9%</td></tr><tr><td>Indonesia</td><td>7.2%</td><td>7.1%</td><td>7.4%</td><td>7.6%</td><td>7.7%</td><td>7.7%</td><td>7.4%</td><td>7.2%</td><td>7.1%</td></tr><tr><td>Malaysia</td><td>3.3%</td><td>3.4%</td><td>3.3%</td><td>3.1%</td><td>2.9%</td><td>2.8%</td><td>2.8%</td><td>2.8%</td><td>2.7%</td></tr><tr><td>Philippines</td><td>5.4%</td><td>5.5%</td><td>4.9%</td><td>4.4%</td><td>4.1%</td><td>4.2%</td><td>4.2%</td><td>4.2%</td><td>4.8%</td></tr><tr><td>Thailand</td><td>4.6%</td><td>4.5%</td><td>4.5%</td><td>4.4%</td><td>4.7%</td><td>4.8%</td><td>4.9%</td><td>4.7%</td><td>4.6%</td></tr><tr><td>Singapore</td><td>2.4%</td><td>2.4%</td><td>2.3%</td><td>2.3%</td><td>2.4%</td><td>2.3%</td><td>2.4%</td><td>2.3%</td><td>2.5%</td></tr><tr><td>Australia</td><td>2.9%</td><td>2.8%</td><td>2.8%</td><td>2.9%</td><td>2.9%</td><td>2.8%</td><td>2.8%</td><td>2.8%</td><td>2.6%</td></tr></table>

## Key Metrics – DuPont Summary (cont'd)

<table><tr><td colspan="10">DuPont Summary – CIR, PPoP/average assets, Credit Costs</td></tr><tr><td>CIR</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>China</td><td>38%</td><td>35%</td><td>34%</td><td>33%</td><td>32%</td><td>32%</td><td>33%</td><td>34%</td><td>36%</td></tr><tr><td>Hong Kong</td><td>45%</td><td>45%</td><td>42%</td><td>42%</td><td>44%</td><td>45%</td><td>49%</td><td>46%</td><td>41%</td></tr><tr><td>Korea</td><td>55%</td><td>55%</td><td>50%</td><td>51%</td><td>50%</td><td>49%</td><td>47%</td><td>45%</td><td>42%</td></tr><tr><td>Taiwan</td><td>54%</td><td>54%</td><td>53%</td><td>54%</td><td>54%</td><td>56%</td><td>54%</td><td>55%</td><td>52%</td></tr><tr><td>India</td><td>47%</td><td>48%</td><td>44%</td><td>47%</td><td>48%</td><td>46%</td><td>47%</td><td>50%</td><td>52%</td></tr><tr><td>Indonesia</td><td>46%</td><td>45%</td><td>46%</td><td>45%</td><td>45%</td><td>47%</td><td>46%</td><td>45%</td><td>43%</td></tr><tr><td>Malaysia</td><td>47%</td><td>48%</td><td>48%</td><td>47%</td><td>47%</td><td>45%</td><td>42%</td><td>42%</td><td>43%</td></tr><tr><td>Philippines</td><td>56%</td><td>56%</td><td>57%</td><td>58%</td><td>55%</td><td>49%</td><td>58%</td><td>56%</td><td>55%</td></tr><tr><td>Thailand</td><td>42%</td><td>42%</td><td>43%</td><td>45%</td><td>46%</td><td>46%</td><td>45%</td><td>45%</td><td>44%</td></tr><tr><td>Singapore</td><td>44%</td><td>45%</td><td>43%</td><td>44%</td><td>43%</td><td>44%</td><td>45%</td><td>43%</td><td>40%</td></tr><tr><td>Australia</td><td>50%</td><td>50%</td><td>49%</td><td>51%</td><td>53%</td><td>57%</td><td>56%</td><td>54%</td><td>51%</td></tr><tr><td colspan="10"></td></tr><tr><td>PPOP/average assets</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>China</td><td>2.0%</td><td>2.0%</td><td>1.9%</td><td>1.8%</td><td>1.9%</td><td>2.0%</td><td>1.9%</td><td>1.8%</td><td>1.6%</td></tr><tr><td>Hong Kong</td><td>1.2%</td><td>1.1%</td><td>1.1%</td><td>1.2%</td><td>1.3%</td><td>1.2%</td><td>1.0%</td><td>0.9%</td><td>1.0%</td></tr><tr><td>Korea</td><td>1.2%</td><td>1.1%</td><td>1.0%</td><td>1.1%</td><td>1.1%</td><td>1.1%</td><td>1.1%</td><td>1.1%</td><td>1.1%</td></tr><tr><td>Taiwan</td><td>1.0%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.9%</td><td>0.8%</td><td>0.8%</td><td>0.7%</td></tr><tr><td>India</td><td>2.6%</td><td>2.8%</td><td>2.5%</td><td>3.4%</td><td>2.8%</td><td>2.7%</td><td>3.0%</td><td>2.8%</td><td>2.6%</td></tr><tr><td>Indonesia</td><td>4.0%</td><td>4.2%</td><td>4.3%</td><td>4.0%</td><td>3.9%</td><td>3.9%</td><td>3.5%</td><td>3.7%</td><td>3.8%</td></tr><tr><td>Malaysia</td><td>1.6%</td><td>1.5%</td><td>1.4%</td><td>1.5%</td><td>1.5%</td><td>1.4%</td><td>1.4%</td><td>1.6%</td><td>1.6%</td></tr><tr><td>Philippines</td><td>1.9%</td><td>1.8%</td><td>1.8%</td><td>1.8%</td><td>1.7%</td><td>2.1%</td><td>2.8%</td><td>2.0%</td><td>2.2%</td></tr><tr><td>Thailand</td><td>2.5%</td><td>2.8%</td><td>2.8%</td><td>2.8%</td><td>2.6%</td><td>2.5%</td><td>2.4%</td><td>2.4%</td><td>2.4%</td></tr><tr><td>Singapore</td><td>1.3%</td><td>1.3%</td><td>1.3%</td><td>1.3%</td><td>1.3%</td><td>1.4%</td><td>1.2%</td><td>1.2%</td><td>1.3%</td></tr><tr><td>Australia</td><td>1.4%</td><td>1.4%</td><td>1.3%</td><td>1.3%</td><td>1.3%</td><td>1.2%</td><td>1.1%</td><td>1.1%</td><td>1.1%</td></tr><tr><td colspan="10"></td></tr><tr><td>Credit cost</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>China</td><td>1.2%</td><td>1.4%</td><td>1.4%</td><td>1.4%</td><td>1.1%</td><td>1.0%</td><td>0.9%</td><td>0.8%</td><td>0.8%</td></tr><tr><td>Hong Kong</td><td>0.3%</td><td>0.2%</td><td>0.6%</td><td>0.6%</td><td>0.2%</td><td>0.6%</td><td>0.7%</td><td>0.9%</td><td>0.9%</td></tr><tr><td>Korea</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.4%</td><td>0.3%</td><td>0.5%</td><td>0.7%</td><td>0.6%</td><td>0.5%</td></tr><tr><td>Taiwan</td><td>0.3%</td><td>0.2%</td><td>0.1%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>India</td><td>1.6%</td><td>2.2%</td><td>2.2%</td><td>3.5%</td><td>2.7%</td><td>2.2%</td><td>1.2%</td><td>1.0%</td><td>1.1%</td></tr><tr><td>Indonesia</td><td>1.2%</td><td>1.0%</td><td>1.0%</td><td>2.4%</td><td>2.1%</td><td>1.0%</td><td>0.4%</td><td>0.6%</td><td>0.8%</td></tr><tr><td>Malaysia</td><td>0.2%</td><td>0.2%</td><td>0.1%</td><td>0.6%</td><td>0.5%</td><td>0.2%</td><td>0.2%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Philippines</td><td>0.4%</td><td>0.4%</td><td>0.6%</td><td>3.0%</td><td>0.9%</td><td>0.6%</td><td>0.6%</td><td>0.5%</td><td>0.9%</td></tr><tr><td>Thailand</td><td>1.6%</td><td>1.5%</td><td>1.3%</td><td>1.8%</td><td>1.5%</td><td>1.2%</td><td>1.4%</td><td>1.4%</td><td>1.4%</td></tr><tr><td>Singapore</td><td>0.4%</td><td>0.2%</td><td>0.2%</td><td>0.7%</td><td>0.2%</td><td>0.2%</t

[中间内容因长度限制已省略]

llectively JPM) make no representations or warranties whatsoever to the completeness or accuracy of the material provided, except with respect to any disclosures relative to JPM and the Research Analyst's involvement with the issuer that is the subject of the material. Accordingly, no reliance should be placed on the accuracy, fairness or completeness of the information contained in this material. There may be certain discrepancies with data and/or limited content in this material as a result of calculations, adjustments, translations to different languages, and/or local regulatory restrictions, as applicable. These discrepancies should not impact the overall investment analysis, views and/or recommendations of the subject company(ies) that may be discussed in the material. Artificial intelligence tools may have been used in the preparation of this material, including assisting in data analysis, pattern recognition, and content drafting for research material. JPM accepts no liability whatsoever for any loss arising from any use of this material or its contents, and neither JPM nor any of its respective directors, officers or employees, shall be in any way responsible for the contents hereof, apart from the liabilities and responsibilities that may be imposed on them by the relevant regulatory authority in the jurisdiction in question, or the regulatory regime thereunder. Opinions, forecasts or projections contained in this material represent JPM's current opinions or judgment as of the date of the material only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer
"""
