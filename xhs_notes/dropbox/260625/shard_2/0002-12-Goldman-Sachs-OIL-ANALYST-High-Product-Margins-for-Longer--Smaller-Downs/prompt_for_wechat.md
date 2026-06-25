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
OIL ANALYST

# High Product Margins for Longer; Smaller Downside Risks Than for Crude Prices

\- Limited relief to refined products margins from Hormuz reopening. While crude prices declined by over \$10 following the US-Iran interim peace deal announcement, refined products margins have fallen less, with our global refined products margins index still double its pre-war level (Exhibit 1). While we remain constructive on products margins following the reopening, we have nudged down our diesel margins forecast given our assumption that Persian Gulf exports normalize by end-July (vs. our end-August assumption before the announcement). We now expect US/EU diesel margins to moderate to \$46/31/bbl by 2026Q4 (vs. \$50/37 prior), still 2-3 times above their 2013-2019 seasonal averages, but keep our gasoline margins forecast for 2026Q4 roughly unchanged at \$23/13 for US/Europe (Exhibit 2).

Not out of the (Hormuz) woods yet. Lower-for-longer refined products stocks are the key reason for our constructive margins view. Both gasoline and diesel stocks remain below their 2022-2026 seasonal range in the US (Exhibit 3), and we expect diesel/gasoline stocks to edge down further for the next 1/4 months, followed by a gradual recovery to 2025 seasonal levels by 2027H2. Gasoline stocks are especially low as refineries have prioritized diesel and jet fuel production at the expense of gasoline over the last 4 months (Exhibit 5). Although Persian Gulf refinery outages decreased by 1/2 since the ceasefire announcement, the remaining 1.3mb/d of unplanned outages may take several months to repair (Exhibit 6). $^{1}$ While products supply is likely to remain constrained for longer, we expect refined product demand to largely rebound over the next quarter, with moderate demand scarring in 2027. As a result, we see gasoline and diesel margins averaging slightly above market forwards for the remainder of the year (Exhibit 7).

■ Structural tailwinds keep 2027 margins elevated. Despite some sequential moderation in products margins next year as Asia and Middle East refineries ramp up production and stocks rebuild, we see margins remaining above their 2025 levels, with average 2027 US/EU diesel margins at \$38/25/bbl (vs. \$41/29 prior) and average 2027 US/EU gasoline margins at \$22/15/bbl (unchanged) (Exhibit 7). Extended delays in China and India refining capacity additions and

Yulia Zhestkova Grigsby
+1(646)446-3905 |
yulia.grigsby@gs.com
GS & Co. LLC

Filippo Cuscito
+44(20)7051-9073 |
filippo.cuscito@gs.com
GS International

Daan Struyven  
+1(212)357-4172 |  
daan.struyven@gs.com  
GS & Co. LLC

continuing attacks on Russian refineries are likely to keep global utilization rates near their all-time highs in 2027. $^{2}$

## ■ Two-sided risks, with more limited downside than for crude prices.

☐ With structural tailwinds providing a floor under products margins, we see more limited downside risk to margins than to crude prices.

☐ More limited downside. Assuming Gulf exports normalize by early July, crude production beats, and demand losses appear to be stickier, US diesel/gasoline margins might average 14/9% (\$5/2/bbl) below our 2027 base case vs. 28% (\$21/bbl) lower for Brent (Exhibit 8, green line).

☐ More upside. Assuming Hormuz remains disrupted through 2027 with Gulf crude exports recovering gradually by 10mb/d by Dec 2027 (Exhibit 9), 2027 average US diesel/gasoline margins might exceed our base case by 66% (\$25/bbl) vs. Brent by 41% (\$30/bbl) given a larger Hormuz supply hit to middle distillates than for crude (Exhibit 8, red line).

## High Product Margins for Longer

Exhibit 1: Refined Products Margins Have Fallen Less Since the Interim Peace Deal Announcement Than Crude Prices, With Our Global Refined Product Margin Index Still Double Its Pre-War Level

![](images/5bf4292affd348bd44e416cbb28536c5891b611c1cf951c37fce05a934889db4.jpg)  
Source: ICE, Platts, GS Global Investment Research

![](images/4ae30c0d8872ae60898ee85eb7d9c0003eb285258598410952fc332820d0e6f7.jpg)

Exhibit 2: We Have Nudged Down Our Diesel Margins Forecast and Now Expect US/EU Diesel Margins to Decline to \$50/35/bbl in 2026H2, While Keeping Our Gasoline Margins Forecast for 2026H2 Roughly Unchanged at \$27/16 for US/Europe

![](images/27af26f1458975a5c67620b599df1d20e7bb12500b22772d9c909ddc37609044.jpg)  
Source: Platts, ICE, GS Global Investment Research

![](images/36d1ec2db12eeafabb3275bca35714ffb0b3280497c59e91b973916fa081cd0d.jpg)  
Exhibit 4: Already Low Storage, a Stretched Refining System, and Rapidly Recovering Demand Will Likely Keep Product Stocks at Low Levels Over the Next 12 Months

Exhibit 3: US Gasoline and Diesel Stocks Are Below Their 2022-2026 Seasonal Range  
![](images/d0d4df7b4a94a74fb2660c4d51af049af96e677aff2a61e95b190fc95f75318d.jpg)  
Source: EIA, GS Global Investment Research  
Source: IEA, GS Global Investment Research

Exhibit 5: High Diesel and Jet Fuel Margins Following the Hormuz Shock Pushed Refineries to Prioritize Middle Distillates Production Over Gasoline  
![](images/dcd86dae64cf1a199e51c5350adc04345f70d36c1208027b06677cbe3ed73f83.jpg)  
Source: EIA, GS Global Investment Research

Exhibit 6: Nearly 1.3mb/d of Persian Gulf Refining Capacity Remains Under Unplanned Maintenance/Repair More Than Two Months After the Ceasefire Announcement  
![](images/21f0199238b2c1b418979c0e3d84037a61e207ba502e59f8178f92356a1b5a11.jpg)  
Source: IIR, GS Global Investment Research

Exhibit 7: We Expect Diesel and Gasoline Margins to Stay Slightly Above Market Forwards in 2026H2 and Remain Above 2025 Levels Through 2027  
![](images/cd193b203443d834f462dcbafaff70f8318478c8743c41f4950275782b712f80.jpg)  
Source: Platts, ICE, GS Global Investment Research

## Two-Sided Risks to Margins, With a Smaller Downside Than for Crude

Exhibit 8: We See a Limited Downside to Refined Products Margins if Demand Recovery Disappoints, and a Much Larger Upside for Diesel Margins Than For Gasoline in Case of Prolonged Disruptions to Hormuz Flows

![](images/c2d927333cd9b74da8c4ac0a1001dca2955cb4654d3be61b7e6a755621c5c81e.jpg)  
Source: GS Global Investment Research

Exhibit 9: We See a Relatively Higher Upside for Diesel Margins Than for Crude Prices in Case of a Prolong Disruption to Gulf Flows, but a Smaller Upside for Gasoline Margins

![](images/677d415a04ea007844252d531f113928c96dd33d22aa5561ced57726afdd37e5.jpg)

Price upside scenario assumes that Hormuz flows remain disrupted indefinitely, but Gulf exports trend up 10mb/d by end-2027 due to more redirections and eventual slow pick up in Hormuz flows. Price downside scenario assumes that Gulf exports normalize to pre-war levels by early-July (vs. late-July in our base case), crude production beats expectations 1.4mb/d, demand losses are stickier at 1.5mb/d vs. 0.5mb/d in our baseline, and \$5/bbl higher backend (36M-ahead Brent forwards).

Source: GS Global Investment Research

## Appendix

Exhibit 10: We See a Narrower Risk Range for Refined Products Than for Brent Prices Given Near-Term Tailwinds (Ongoing Middle East and Russia Refinery Outages, Low Current Stocks, Hurricane Season in the US) and Structural Support (Tight Refining, Stricter Government Policies)

![](images/1c0c619748284ad6b6d05fd91d02e72e8bd205b91267e5d08d28b80e86b74cc7.jpg)  
Source: GS Global Investment Research

Exhibit 11: We Expect US/Europe Diesel Refined Products Margins to Average \$38/25/bbl in 2027 and US 3-2-1 Crack Spread to Average at \$27/bbl

<table><tr><td rowspan="3"></td><td colspan="7">GS Forecast of Average Monthly Refined Products Margins vs. Brent ($/bbl)</td></tr><tr><td colspan="3">Diesel</td><td colspan="3">Gasoline</td><td>3-2-1 Crack Spread</td></tr><tr><td>USNYH HeatingOil</td><td>EuropeICE ARA Gasoil</td><td>AsiaSingaporeGasoil</td><td>USNYH RBOBGasoline</td><td>EuropeEurope EBOBGasoline</td><td>AsiaSingaporeMogas</td><td>US</td></tr><tr><td>2025</td><td>28</td><td>22</td><td>18</td><td>18</td><td>14</td><td>10</td><td>21</td></tr><tr><td>2026</td><td>50</td><td>38</td><td>35</td><td>28</td><td>18</td><td>15</td><td>36</td></tr><tr><td>2027</td><td>38</td><td>25</td><td>22</td><td>22</td><td>15</td><td>11</td><td>27</td></tr><tr><td>1Q26</td><td>41</td><td>33</td><td>30</td><td>21</td><td>14</td><td>13</td><td>28</td></tr><tr><td>2Q26</td><td>59</td><td>51</td><td>47</td><td>38</td><td>27</td><td>23</td><td>45</td></tr><tr><td>3Q26</td><td>55</td><td>39</td><td>35</td><td>31</td><td>18</td><td>15</td><td>39</td></tr><tr><td>4Q26</td><td>46</td><td>31</td><td>28</td><td>23</td><td>13</td><td>11</td><td>31</td></tr><tr><td>1Q27</td><td>40</td><td>28</td><td>25</td><td>26</td><td>15</td><td>12</td><td>31</td></tr><tr><td>2Q27</td><td>39</td><td>26</td><td>23</td><td>27</td><td>18</td><td>12</td><td>31</td></tr><tr><td>3Q27</td><td>35</td><td>23</td><td>20</td><td>20</td><td>16</td><td>11</td><td>25</td></tr><tr><td>4Q27</td><td>36</td><td>24</td><td>21</td><td>15</td><td>11</td><td>10</td><td>22</td></tr><tr><td>Jan-26</td><td>31</td><td>24</td><td>18</td><td>13</td><td>11</td><td>8</td><td>19</td></tr><tr><td>Feb-26</td><td>32</td><td>25</td><td>19</td><td>23</td><td>11</td><td>8</td><td>26</td></tr><tr><td>Mar-26</td><td>59</td><td>50</td><td>53</td><td>27</td><td>20</td><td>23</td><td>38</td></tr><tr><td>Apr-26</td><td>62</td><td>58</td><td>56</td><td>36</td><td>25</td><td>25</td><td>45</td></tr><tr><td>May-26</td><td>58</td><td>51</td><td>46</td><td>42</td><td>30</td><td>24</td><td>47</td></tr><tr><td>Jun-26</td><td>56</td><td>43</td><td>38</td><td>37</td><td>25</td><td>19</td><td>44</td></tr><tr><td>Jul-26</td><td>57</td><td>42</td><td>40</td><td>37</td><td>20</td><td>17</td><td>43</td></tr><tr><td>Aug-26</td><td>57</td><td>40</td><td>35</td><td>29</td><td>21</td><td>15</td><td>38</td></tr><tr><td>Sep-26</td><td>50</td><td>35</td><td>30</td><td>27</td><td>14</td><td>13</td><td>35</td></tr><tr><td>Oct-26</td><td>49</td><td>33</td><td>29</td><td>25</td><td>14</td><td>11</td><td>33</td></tr><tr><td>Nov-26</td><td>46</td><td>31</td><td>28</td><td>22</td><td>13</td><td>10</td><td>30</td></tr><tr><td>Dec-26</td><td>43</td><td>29</td><td>26</td><td>21</td><td>14</td><td>10</td><td>29</td></tr><tr><td>Jan-27</td><td>38</td><td>26</td><td>24</td><td>21</td><td>13</td><td>12</td><td>27</td></tr><tr><td>Feb-27</td><td>41</td><td>28</td><td>25</td><td>29</td><td>13</td><td>12</td><td>33</td></tr><tr><td>Mar-27</td><td>42</td><td>28</td><td>25</td><td>29</td><td>19</td><td>12</td><td>33</td></tr><tr><td>Apr-27</td><td>40</td><td>27</td><td>24</td><td>27</td><td>18</td><td>11</td><td>32</td></tr><tr><td>May-27</td><td>38</td><td>26</td><td>23</td><td>26</td><td>17</td><td>12</td><td>30</td></tr><tr><td>Jun-27</td><td>39</td><td>26</td><td>23</td><td>27</td><td>18</td><td>13</td><td>31</td></tr><tr><td>Jul-27</td><td>36</td><td>25</td><td>21</td><td>27</td><td>19</td><td>13</td><td>30</td></tr><tr><td>Aug-27</td><td>34</td><td>23</td><td>20</td><td>18</td><td>19</td><td>10</td><td>23</td></tr><tr><td>Sep-27</td><td>34</td><td>23</td><td>20</td><td>16</td><td>11</td><td>9</td><td>22</td></tr><tr><td>Oct-27</td><td>37</td><td>25</td><td>21</td><td>15</td><td>11</td><td>10</td><td>22</td></tr><tr><td>Nov-27</td><td>36</td><td>24</td><td>21</td><td>15</td><td>11</td><td>10</td><td>22</td></tr><tr><td>Dec-27</td><td>35</td><td>24</td><td>20</td><td>16</td><td>11</td><td>10</td><td>22</td></tr></table>

Source: GS Global Investment Research

Team Oil

Daan Struyven +1(212)357-4172 daan.struyven@gs.com GS & Co. LLC

Alexandra Paulus +1(212)902-7111 alexandra.paulus@gs.com GS & Co. LLC

Yulia Zhestkova Grigsby
+1(646)446-3905
yulia.grigsby@gs.com
GS & Co. LLC

Filippo Cuscito +44(20)7051-9073  
filippo.cuscito@gs.com GS International

## Disclosure Appendix

## Reg AC

We, Yulia Zhestkova Grigsby, Filippo Cuscito and Daan Struyven, hereby certify that all of the views expressed in this report accurately reflect our personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yulia Zhestkova Grigsby GS & Co. LLC, Filippo Cuscito GS International, Daan Struyven GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; 1% or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit com

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
