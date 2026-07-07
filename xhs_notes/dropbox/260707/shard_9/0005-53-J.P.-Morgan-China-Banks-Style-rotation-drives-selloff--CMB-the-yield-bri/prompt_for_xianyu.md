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
This material is neither intended to be distributed to Mainland China investors nor to provide securities investment consultancy services within the territory of Mainland China. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM.

# China Banks

Style rotation drives selloff; CMB the yield bright spot

MSCI China banks and CSI 300 banks corrected 7%/5% in the past month, compared to MSCI China and CSI 300 correcting by 10%/2% in the same period. We observed that in the past month Bloomberg consensus shows FY1 EPS estimates revision of -2.8%/-1.3% for MSCI China banks and CSI 300 banks, respectively. Instead of EPS cuts, we believe style rotation has been the key driver of the share price corrections. Our analysis shows that current dividend yields for SOE banks are not attractive, in both H/A shares. Having that said, if SOE banks further correct 9% in H shares and 6% in A shares, we believe that dividend yield will become attractive and provide strong downside support. At the current level, we see CMB as an attractive yield name, with its H share dividend yield (5.4%) almost at par with that of the SOE banks, and its A-share dividend yield (5.6%) 110bps higher than the SOE banks. We see limited downside on relative stock performance, as the room for EPS disappointment seems limited given low expectations and CMB's PB and PE premium over the Big 4 SOE banks being close to the 10Y trough, with its 2026E ROE at a 380bps spread over the Big 4 and its 2026E EPS growth 3% above the Big 4 if we consider the dilution risk of SOE banks.

\- Dividend yields for H shares of SOE banks are not attractive, even for Southbound investors: We estimate that on an ex-tax basis (10% dividend tax for all investors), H share SOE banks are trading at a dividend spread of 40bps against the 10Y UST, below the 10Y mean of 280bps, and thus not attractive for overseas investors. For example, HSBC/STAN offer 6%/7% total return (div + buyback) in 12M, higher than H-share SOE banks' 5.5% on average. Southbound investors may compare the dividend yield (excluding 20% div. tax) to the 10Y CGB. The current dividend spread is 260bps, close to the 10Y average of 220bps (Figure 1). The risk-reward may be more attractive for insurance companies, as they are exempt from dividend tax, and Ping An Insurance is the one most actively investing into China banks. However, its ownership in PSBC, ICBC, CCB, CMB and ABC is above 4%, close to the 5% regulatory threshold (Figure 5), capping Ping An's ability to increase its holdings in these banks. Having said that, if H share SOE banks' dividend yield reaches 6% (with an ex-tax div spread of \~300bps), implying another 9% downside to share prices, we may see more support for share price performance.

\- A share SOE banks' dividend yield is not attractive, particularly if we consider the dilution risk: SOE banks' A share 2026 dividend yield and dividend spread are $4.4\%$ and 270bps, higher than the respective 10Y means by $\sim 40$ bps, so the upside to share prices from the dividend angle is limited in our view. For ICBC and ABC, which could see capital injection in 2H26, we estimate potential DPS dilution of $2\%$ and $7\%$ , respectively, on a full-year basis (Table 1). If we consider the dilution risk, the dividend spread is 260bps for ICBC and 210bps for ABC, vs the respective 10Y mean of 220bps and 240bps. Having said that, if the dividend spread of SOE banks reaches 300bps, implying $6\%$ share price downside, then we see support for share prices.

## Banks & Financial Services

Katherine Lei AC
(852) 2800-8552
katherine.lei@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Peter Zhang
(852) 2800-8557
peter.zhang@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Lincoln Yu
(852) 2800 8523
lincoln.yu@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Haomin Chen
(86-21) 6106 6347
haomin.chen@JPM.com
SAC Registration Number: S1730524080002
JPM Securities (China) Company Limited

See page 8 for analyst certification and important disclosures, including non-US analyst disclosures.

\- Joint-stock banks' dividend spread is higher than SOE banks, but EPS volatility is a key concern: We estimate that H-share joint stock banks' dividend spread (ex-20% div tax) against the 10YCGB is 320bps, above the 10Y mean of 190bps. The A share dividend yield reaches 5.7% on average with dividend spread at 400bps, higher than 10Y mean of 130bps. However, investors are unlikely to treat JSBs as dividend stocks, due to higher earnings volatility, on the back of growth risks and capital dilution, as highlighted in Table 2 below.

\- CMB has emerged as a dividend name, with its valuation premium vs SOE banks reaching the trough level in the past decade: On our estimates, CMB-H and A shares are trading at 5.4%/5.6% dividend yield, implying a dividend spread against the 10Y CGB of 370bps/390bps, both higher than the respective 10Y mean of 100bps/90bps. CMB's H share dividend is close to the average for the Big 4 banks of 5.6%, while its A share dividend yield is 140ps higher than the Big 4 average of 4.2%. More importantly, we estimate CMB is the only bank in our coverage that offers above-zero EPS growth throughout the past decade (Table 2). And its high CET 1 buffer (Figure 8) means that the capital dilution risk is low. The key investor pushback to our view of CMB as a dividend name could be stock volatility, which we expect to be low, given low expectations for earnings and an undemanding valuation. Note that the JPM/Bloomberg consensus estimate for CMB's 2026 EPS growth is 3.0%/3.5%. We believe the downside is limited, given slowing of NIM contraction on a y/y basis and the robust capital markets in China supporting its non-NII. Furthermore, on our estimates, CMB's PB and PE premium over the Big 4 banks is close to a decade's trough (Figure 9-Figure 10), despite which its ROE is 380bps higher than the Big 4 average, close to the 10Y mean ROE premium of 400bps. Also, its 2026E EPS growth of 3% is higher than the Big 4 average (0%), if we consider the dilution risks to ICBC and ABC.

Figure 1: H share SOE banks avg dividend yield spread against China 10-year bond yields has been 260bps lately, vs the 10Y average of \~220bps  
![](images/06af6deefbd8ad9fe339b4a48587ef8d00d0af305b3a013420f7aaad7a69f70b.jpg)  
H-sh SOE banks avg ex-tax div yields spread against China 10-yr yields (for SB with 20% tax rate)
SOE banks 10 year avg  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 2: H share JSBs' avg dividend yield spread against China 10-year bond yields has been 320bps lately, vs the 10Y average of \~190bps  
![](images/d20e7622981deb2790124192678e5c167c3a53ac16b5fe19056e7254983a3a6c.jpg)  
H-sh JSBs avg ex-tax div yields spread against China 10-yr yields (for SB with 20% tax rate)
JSBs 10 year avg  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 3: A share SOE banks' avg dividend yield spread against China 10-year bond yields has been 270bps lately, vs the 10Y average of \~230bps  
![](images/2689a06edc8c1d0e26c260b859a6eed912d7f464135f2343f77ad4b15b95182c.jpg)  
A listed SOE bank avg dividend yields spread against 10Y govt bond yields — SOE banks - 10 year avg  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 4: A share JSBs' avg dividend yield spread against China 10-year bond yields has been 400bps lately, vs the 10Y average of \~130bps  
![](images/6d941c6b78b762986ed4746da48a7c1403c9f8736b7dbb1c9fd086b5d1fd61fa.jpg)  
A listed JSB bank avg dividend yields spread against 10Y govt bond yields — JSBs - 10 year avg  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 5: Ping An Group's holdings in ICBC, CCB, CMB, PSBC and ABC are all above $4\%$ , so its further buying capacity is limited  
![](images/0d6d18865f3c98a5376126b6527aef66bf462c4ab1d1037ba43d383bc297df98.jpg)  
Source: HKEX, SSE. Note: Based on company's disclosures. Ping An Group may have holdings in other China banks that haven't reached the threshold for disclosures.

Table 1: Pro forma impact of the potential capital raising on ABC and ICBC's financials

<table><tr><td rowspan="2">In Rmb</td><td rowspan="2">Raised amount (bn)</td><td colspan="3">2026E EPS</td><td colspan="3">2026E DPS</td><td colspan="3">2026E ROCE</td><td colspan="3">A-sh dividend yield</td></tr><tr><td>Base</td><td>Pro-forma</td><td>diff</td><td>Base</td><td>Pro-forma</td><td>diff</td><td>Base</td><td>Pro-forma</td><td>diff</td><td>Base</td><td>Pro-forma</td><td>diff</td></tr><tr><td>ABC</td><td>235</td><td>0.82</td><td>0.78</td><td>-5.2%</td><td>0.26</td><td>0.24</td><td>-7.3%</td><td>9.8%</td><td>9.2%</td><td>-57 bps</td><td>4.4%</td><td>4.1%</td><td>-32 bps</td></tr><tr><td>ICBC</td><td>65</td><td>1.03</td><td>1.01</td><td>-1.3%</td><td>0.32</td><td>0.31</td><td>-1.9%</td><td>9.2%</td><td>9.1%</td><td>-11 bps</td><td>4.5%</td><td>4.4%</td><td>-9 bps</td></tr></table>

Source: JPM estimates. We assume the capital raising is completed by Sep 2026. We assume ABC raises Rmb235bn and ICBC raises Rmb65bn, and the placement price for ABC and ICBC are 15% and 9% above their latest A share closing price as of July 3, 2026.

Figure 6: CMB-A dividend yield is higher than its 10-year average and A share SOE banks' average  
![](images/89e34970dfda5d3e5e643c402a65fa440773ef280d8f8248ed17c7555c457c2f.jpg)  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 7: CMB-H div yield is higher than its 10yr avg but slightly below H share SOE banks' avg  
![](images/46070e23efbfd338112dd93a1fc5d5519d447942c6e0dc8f5e588daacfdae224.jpg)  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 8: CMB has the strongest capital buffer among China banks in our coverage  
![](images/ccd39938c017a2a1d494bf320bd023f55cfdddcb13d6ebe1a0d8adacd2f01d63.jpg)  
Source: Company reports.

Figure 9: CMB-H is trading at a 58% PB valuation premium over the Big 4 banks, compared to the average level of 130%  
![](images/d1b9b5b1577c07bb671e275b906fb31aa4d609d63ec718bb5a6b7f0f2c96738d.jpg)  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 10: CMB-H is trading at an 18% PE valuation premium over the Big 4 banks, compared to the average level of 70%  
![](images/acd25ebc98fee444a6fb74813efcde6c972b4cae13c203add8872ce5fed94b52.jpg)  
Source: Bloomberg Finance L.P. Data as of July 2, 2026.

Figure 11: CMB's ROE is 380bps higher than the Big 4 average ROE, compared to the 10Y average of 400bps  
![](images/e8d13f71b1ceabb916d08dbd83064faa74af4a715ee003654d8190660558854e.jpg)  
Source: Company reports, JPM estimates.

Figure 12: CMB EPS growth compared to the Big 4 bank average EPS growth  
![](images/cc56badf740c6127aacae4de73472a80b4ade439598a9be36209de81b8837547.jpg)  
Source: Company reports, JPM estimates.

Table 2: China banks' EPS growth – CMB is the only bank we cover to have offered above-zero EPS growth throughout the past decade

<table><tr><td>EPS growth</td><td>2015</td><td>2016</td><td>2017</td><td>2018</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td></tr><tr><td>ABC*</td><td>-1%</td><td>1%</td><td>5%</td><td>1%</td><td>1%</td><td>-1%</td><td>10%</td><td>6%</td><td>5%</td><td>4%</td><td>4%</td><td>0%</td></tr><tr><td>BOC</td><td>-7%</td><td>-5%</td><td>5%</td><td>5%</td><td>4%</td><td>0%</td><td>14%</td><td>3%</td><td>2%</td><td>2%</td><td>-2%</td><td>-1%</td></tr><tr><td>CCB</td><td>0%</td><td>1%</td><td>5%</td><td>4%</td><td>5%</td><td>1%</td><td>12%</td><td>7%</td><td>2%</td><td>0%</td><td>-1%</td><td>0%</td></tr><tr><td>ICBC*</td><td>-1%</td><td>0%</td><td>3%</td><td>4%</td><td>5%</td><td>0%</td><td>10%</td><td>2%</td><td>1%</td><td>1%</td><td>2%</td><td>1%</td></tr><tr><td>PSBC</td><td>-12%</td><td>-9%</td><td>6%</td><td>5%</td><td>17%</td><td>-1%</td><td>10%</td><td>9%</td><td>-2%</td><td>-3%</td><td>-10%</td><td>-7%</td></tr><tr><td>BoComm</td><td>1%</td><td>0%</td><td>2%</td><td>5%</td><td>5%</td><td>-1%</td><td>11%</td><td>3%</td><td>1%</td><td>1%</td><td>-7%</td><td>-3%</td></tr><tr><td>Citic</td><td>1%</td><td>-3%</td><td>-1%</td><td>5%</td><td>1%</td><td>-3%</td><td>14%</td><td>8%</td><td>8%</td><td>5%</td><td>0%</td><td>3%</td></tr><tr><td>CMB</td><td>3%</td><td>8%</td><td>13%</td><td>12%</td><td>16%</td><td>5%</td><td>22%</td><td>14%</td><td>7%</td><td>1%</td><td>1%</td><td>3%</td></tr><tr><td>Minsheng</td><td>3%</td><td>4%</td><td>3%</td><td>1%</td><td>7%</td><td>-42%</td><td>0%</td><td>0%</td><td>1%</td><td>-11%</td><td>-2%</td><td>0%</td></tr><tr><td>Industrial</td><td>6%</td><td>5%</td><td>1%</td><td>2%</td><td>7%</td><td>-2%</td><td>26%</td><td>11%</td><td>-16%</td><td>0%</td><td>-1%</td><td>2%</td></tr><tr><td>Everbright</td><td>2%</td><td>-1%</td><td>3%</td><td>-5%</td><td>-2%</td><td>-1%</td><td>8%</td><td>3%</td><td>-8%</td><td>3%</td><td>-7%</td><td>-3%</td></tr><tr><td>SPDB</td><td>6%</td><td>-10%</td><td>-23%</td><td>0%</td><td>6%</td><td>-3%</td><td>-14%</td><td>-4%</td><td>-32%</td><td>27%</td><td>12%</td><td>-5%</td></tr><tr><td>Pingan</td><td>-10%</td><td>-16%</td><td>-9%</td><td>7%</td><td>10%</td><td>-9%</td><td>23%</td><td>27%</td><td>2%</td><td>-4%</td><td>-4%</td><td>3%</td></tr><tr><td>Huaxia</td><td>-5%</td><td>-4%</td><td>-20%</td><td>5%</td><td>-12%</td><td>-12%</td><td>12%</td><td>3%</td><td>6%</td><td>10%</td><td>0%</td><td>6%</td></tr><tr><td>SOE banks avg</td><td>-3%</td><td>-2%</td><td>4%</td><td>4%</td><td>6%</td><td>0%</td><td>11%</td><td>5%</td><td>1%</td><td>1%</td><td>-2%</td><td>-2%</td></tr><tr><td>JSB avg</td><td>1%</td><td>-2%</td><td>-4%</td><td>4%</td><td>4%</td><td>-8%</td><td>11%</td><td>8%</td><td>-4%</td><td>4%</td><td>0%</td><td>1%</td></tr><tr><td>Sector avg</td><td>-1%</td><td>-2%</td><td>-1%</td><td>4%</td><td>5%</td><td>-5%</td><td>11%</td><td>7%</td><td>-2%</td><td>3%</td><td>-1%</td><td>0%</td></tr></table>

Source: Company reports, JPM estimates. \*We assume ABC and ICBC capital raising by Sep. 2026. We expect ABC to raise Rmb235bn and ICBC to raise Rmb65bn; the placement price for ABC and ICBC are 15% and 9% above their latest A share closing prices as of July 3, 2026.

Table 3: A share broker dividend yields spread compared to 10Y average spread

<table><tr><td colspan="2"></td><td>Latest share price</td><td>2026E PB</td><td>YTD shr performance</td><td>JPMe 2026 dividend yields</td><td>Current div spread</td><td>10Y avg div spread</td></tr><tr><td>601288 CH</td><td>ABC*</td><td>5.90</td><td>0.67</td><td>-23%</td><td>4.1%</td><td>2.5%</td><td>2.4%</td></tr><tr><td>601988 CH</td><td>BOC</td><td>5.56</td><td>0.63</td><td>-3%</td><td>4.2%</td><td>2.6%</td><td>2.4%</td></tr><tr><td>601939 CH</td><td>CCB</td><td>9.49</td><td>0.67</td><td>2%</td><td>4.2%</td><td>2.6%</td><td>2.1%</td></tr><tr><td>601398 CH</td><td>ICBC*</td><td>7.04</td><td>0.61</td><td>-11%</td><td>4.4%</td><td>2.8%</td><td>2.2%</td></tr><tr><td>601658 CH</td><td>PSBC</td><td>4.94</td><td>0.55</td><td>-9%</td><td>4.5%</td><td>2.8%</td><td>2.2%</td></tr><tr><td>601328 CH</td><td>BoComm</td><td>6.51</td><td>0.46</td><td>-10%</td><td>5.3%</td><td>3.6%</td><td>2.8%</td></tr><tr><td colspan="3">SOE banks avg</td><td>0.60</td><td>-9%</td><td>4.5%</td><td>2.8%</td><td>2.3%</td></tr><tr><td>601998 CH</td><td>Citic</td><td>6.99</td><td>0.50</td><td>-9%</td><td>5.6%</td><td>3.9%</td><td>1.8%</td></tr><tr><td>600036 CH</td><td>CMB</td><td>36.83</td><td>0.78</td><td>-13%</td><td>5.6%</td><td>4.0%</td><td>0.9%</td></tr><tr><td>600016 CH</td><td>Minsheng</td><td>3.28</td><td>0.25</td><td>-14%</td><td>5.7%</td><td>4.1%</td><td>2.2%</td></tr><tr><td>601818 CH</td><td>Everbright</td><td>2.98</td><td>0.31</td><td>-15%</td><td>5.6%</t

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
