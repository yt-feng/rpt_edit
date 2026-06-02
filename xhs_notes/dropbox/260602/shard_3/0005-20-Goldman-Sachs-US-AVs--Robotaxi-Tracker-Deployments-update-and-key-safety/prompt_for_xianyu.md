你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# US AVs: Robotaxi Tracker - Deployments update and key safety and usage metrics

In this recurring note, we update how robotaxi deployments and announcements have evolved, including partnerships/deployments in the US and internationally, for companies within the US Internet and Autos & Industrial Tech sectors (led by Eric Sheridan and Mark Delaney, respectively).

# Key statistics - safety data, MAUs, and usage penetration

Based on available crash data from the National Highway Traffic Safety Administration (NHTSA) from July 2025 through mid-April 2026, and disclosures from Waymo (for all US cities it's operating in commercially) and Tesla (for Austin, as Dallas and Houston had not launched during the partial April reporting period) around trips/miles driven by their respective robotaxi services, we estimate that Tesla had an accident (regardless of fault) every 100K-120K miles, while Waymo had an accident (regardless of fault) every 150K-175K miles. We note that these datapoints reflect all commercial miles in those locations (including those with a safety observer/monitor for Tesla). We show estimated monthly miles between accidents for both companies in Exhibit 1. Note that Tesla's miles between accidents was \~200K miles in March and Tesla did not have any reported accidents in August, February, and the first half of April. Waymo only reported 2 accidents in April over an estimated 10 mn miles driven in the first half of the month. Further, note that April data only captures known/reported accidents through April $15^{\text{th}}$ and further accidents are typically reported in the following month's data (i.e., May data).

Note that because Tesla's fleet in Austin is a mix of vehicles, both with and without a safety monitor, and because there are differences in where the rides are occurring (with Waymo operating commercially in more cities), the data may not be directly comparable. In addition, reports are filed with NHTSA even for minor issues that would be unlikely to be reported by a human (e.g. driving over a curb), and not all accidents are the fault of the AV.

Recent filings from the Texas DOT and NHTSA indicate that Waymo's fleet is \~3,800 vehicles (including 577 in Texas), and that Tesla's fleet size in Texas is 42 vehicles. We note that these would be registered vehicles (which may not all be operational, could include test vehicles, and could be operated with a safety monitor).

# Eric Sheridan

+1(917)343-8683

eric.sheridan@gs.com

GS & Co. LLC

# Mark Delaney, CFA

+1(212)357-0535

mark.delaney@gs.com

GS & Co. LLC

# Will Bryant

+1(212)934-4705 | will.bryant@gs.com

GS & Co. LLC

# Aman Gupta

+1(212)357-1549

aman.s.gupta@gs.com

GS & Co. LLC

# Julia Fein-Ashley

+1(212)902-5070 | julia.fein-

ashley@gs.com

GS & Co. LLC

# Emma Huang

+1(212)902-7229

emma.huang@gs.com

GS & Co. LLC

# Ayush Ghose

+1(212)902-7257

ayush.ghose@gs.com

GS & Co. LLC

Exhibit 1: Waymo and Tesla miles between accidents
Note: some of Tesla's AVs in Texas have a safety monitor in vehicle; Waymo miles per month are GSe   
![](images/114df5b6061771040d087ecad9e6ebc024a2742429fa512299836861e1ade239.jpg)

<details>
<summary>bar</summary>

| Month | Waymo miles between accidents | Tesla miles between accidents |
|---|---|---|
| July | 105,000 | 0 |
| August | 130,000 | 0 |
| September | 120,000 | 20,000 |
| October | 105,000 | 165,000 |
| November | 100,000 | 175,000 |
| December | 140,000 | 200,000 |
| January | 155,000 | 60,000 |
| February | 230,000 | 0 |
| March | 405,000 | 200,000 |
</details>

Source: Company data, NHTSA, GS Global Investment Research

In addition, we highlight app usage from SensorTower within the United States (data available on request). During April, Waymo MAUs continued to grow (+20% YoY) albeit at a slower pace relative to recent months. Additionally, Waymo MAUs scaled as a percentage of US Uber MAUs YTD. Despite US MAU growth outpacing Uber/Lyft, the Waymo app continues to have lower user frequency (by way of session count).

Exhibit 2: Waymo MAUs Represent a LSD % of US Uber MAUs Today...   
![](images/b51451b4b742356bbf12d958c93e3460bfb06363a9cb33216e6310a980c705b4.jpg)

<details>
<summary>bar_line</summary>

US MAUs - YoY Growth and as % of Uber MAUs
| Month | Waymo as % of Uber MAUs (%) | MAU YoY Growth (%) |
|---|---|---|
| Jan-25 | 2.0 | 300 |
| Feb-25 | 2.1 | 220 |
| Mar-25 | 2.1 | 240 |
| Apr-25 | 3.0 | 380 |
| May-25 | 2.4 | 190 |
| Jun-25 | 3.1 | 170 |
| Jul-25 | 2.4 | 110 |
| Aug-25 | 2.7 | 110 |
| Sep-25 | 2.9 | 100 |
| Oct-25 | 2.8 | 60 |
| Nov-25 | 3.8 | 100 |
| Dec-25 | 3.9 | 110 |
| Jan-26 | 3.4 | 70 |
| Feb-26 | 4.4 | 100 |
| Mar-26 | 4.2 | 100 |
| Apr-26 | 3.9 | 30 |
</details>

Source: SensorTower, Data compiled by GS Global investment Research

Exhibit 3: ... and Usage Remains Low in Comparison to Other Rideshare Apps Today   
![](images/65331940dd7d11ab53f51998b6d8bf3b566749799f81d93179a201cf3b71b41b.jpg)

<details>
<summary>line</summary>

US Session Count of Rideshare Apps
| Month | Uber | Lyft | Waymo |
|---|---|---|---|
| Jan-22 | 20.5 | 20.8 | 7.8 |
| Mar-22 | 23.1 | 24.2 | 8.5 |
| May-22 | 22.9 | 23.5 | 8.7 |
| Jul-22 | 23.0 | 23.0 | 8.9 |
| Sep-22 | 24.5 | 27.0 | 9.0 |
| Nov-22 | 23.5 | 23.0 | 8.8 |
| Jan-23 | 23.8 | 21.5 | 8.6 |
| Mar-23 | 24.0 | 24.5 | 8.9 |
| May-23 | 24.5 | 23.0 | 9.0 |
| Jul-23 | 25.0 | 24.0 | 9.1 |
| Sep-23 | 26.0 | 24.5 | 10.5 |
| Nov-23 | 24.5 | 23.5 | 7.0 |
| Jan-24 | 24.0 | 21.5 | 6.0 |
| Mar-24 | 23.5 | 21.0 | 8.0 |
| May-24 | 23.0 | 20.5 | 6.5 |
| Jul-24 | 22.5 | 20.0 | 9.5 |
| Sep-24 | 23.0 | 21.0 | 11.5 |
| Nov-24 | 23.5 | 19.5 | 8.0 |
| Jan-25 | 23.0 | 19.0 | 7.0 |
| Mar-25 | 23.5 | 20.5 | 9.0 |
| May-25 | 23.0 | 19.5 | 7.5 |
| Jul-25 | 23.5 | 19.0 | 8.5 |
| Sep-25 | 24.0 | 20.5 | 11.0 |
| Nov-25 | 24.5 | 19.5 | 11.5 |
| Jan-26 | 24.0 | 19.0 | 10.0 |
| Mar-26 | 25.5 | 21.5 | 12.5 |
</details>

Average sessions per month per user   
Source: SensorTower, Data compiled by GS Global Investment Research

# Announced current and future deployments

Exhibit 4: Autonomous Vehicle Operations   
Triangle = Update/Announcement Made since March 1st, 2026   
![](images/cfa3b3ca46ca06cebc1ef199757920a2645aa1e4abddd8e4d6ba3e21e1f8ede0.jpg)

# Uber

Active   
In Development   
Partnership - Waymo   
Partnership - Mobileye   
Partnership - Rivian   
Partnership - Zoox

# Lyft

Active   
In Development   
Partnership - Waymo   
Partnership - Mobileye

# Waymo

Active   
In Development

# Zoox

Active   
In Development

$\triangle$ Update announced since March $1^{\mathrm{st}}$

\* Rides in Nashville are currently available to the public on the Waymo app, with joint availability with the Lyft app starting later this year   
\* Partnerships with Mobileye, Rivian, and Zoox are currently in development   
\* Waymo rides in Austin and Atlanta are exclusively available through Uber

Active cities defined as locations where operations are fully launched, fully driverless, and available to the public. In development includes cities where testing & mapping operations are currently in progress or where rides are available with safety observers/monitor onboard.

Source: Company data, GS Global Investment Research

Exhibit 5: International Robotaxi Operations (ex. China)   
Triangle = Update/Announcement Made since March 1st, 2026   
![](images/5e248b31d81b80a1177fde550c72989f0195cb590d23ab644ff7ddb47b0bf388.jpg)

<details>
<summary>geo</summary>

| Type | Description |
|---|---|
| Uber | Active |
| Uber | In Development |
| Uber | Partnership – Pony AI |
| Uber | Partnership – Baidu |
| Uber | Partnership - WeRide |
| Waymo | In Development |
| Lyft | In Development |
| Lyft | Partnership - Baidu |
| Mobileye | In Development |
| Pony AI | In Development |
| Baidu | In Development |
| WeRide | In Development |
| Tokyo, JP | Punggol, SG |
* Update announced since March 1st
* WeRide partnerships with Uber in Abu Dhabi and Dubai have commercially launched, Riyadh is in development
* WeRide partnership with Grab is in development
* Pony AI, Baidu partnerships with Uber are in development
* Baidu partnership with Lyft is in development
</details>

Active cities defined as locations where operations are fully launched, fully driverless, and available to the public. In development includes cities where testing & mapping operations are currently in progress or where rides are available with safety observers/monitor onboard.   
Source: Company data, GS Global Investment Research

# Earnings commentary and other announcements - 1Q26

Uber emphasized accelerated progress on its AV initiatives (on the back of outlining the opportunity in its prepared remarks last quarter) and highlighted a few themes: a) AV trips increased more than 10x YoY and the company is now live in 8 cities (with plans to expand to up to 15 by end of year); b) expects to continue to invest into 3P partner relationships - adding and expanding partnerships with Rivian, Zoox, Waabi, and Verne & Pony.ai (with plans to launch Europe's first commercial robotaxi service); & c) seeing strong early traction from the launch of Uber Autonomous Solutions.

Similar to Uber, Lyft also continues to invest in 3P partnerships within its AV initiatives. The company is currently building an 80,000 square ft depot in Nashville to service and maintain Waymo's AVs. The company's recent acquisition of FREENOW was also cited as beneficial to strategic initiatives, such as driving progress with AV operations internationally including by leveraging FREENOW's industry relationships in Europe to build frameworks for AV operations across cities.

For Waymo, as of late March, the company noted it provides over 500,000 rides per week across 11 cities. Since our March update, Waymo has announced full public access to Nashville, Miami, and Orlando, and announced plans to deploy in Portland over the long term, pending regulatory support. Importantly, per media reports, Waymo suspended robotaxi services on freeways to improve performance in construction zones as of May $21^{\text{st}}$ . Recall the company had been operating on freeways in San Francisco, Los Angeles, Phoenix, and Miami. Separately, per media reports, Waymo paused its robotaxi services across Atlanta, San Antonio, Dallas, and Houston due to heavy rain in the regions causing flooding (though services have resumed in some cities). The company is looking to improve the software to avoid flooded areas more effectively. Though we make no changes to our AV forecast at this time, we would also note Waymo's software recall related to the flooding issue of its full fleet indicated that Waymo has 3,791 vehicles as of May 2026 (though not all of these may be operating at a given time). Separately, per a blog post, Waymo is starting public rides with its Ojai vehicles (which use the 6th gen Waymo Driver) in the existing markets of San Francisco, Phoenix, and Los Angeles, with rides coming to new cities later this year to Denver, Las Vegas, and San Diego (all 3 cities were previously announced as part of Waymo's roadmap but have not launched any public rides as of publication). The blog post also notes that Waymo is meaningfully scaling production at its Arizona factory towards its capacity of tens of thousands of units per year.

For Tesla, the company has been offering fully driverless rides in Austin with some vehicles since January, and also offers rides in Austin with a safety observer in the passenger/driver seat in other instances. The company also operates as a ride-hailing service in the Bay Area (and does not currently have the regulatory approvals to be a driverless service there) and expanded driverless service to Dallas and Houston in mid April. Per crowdsourced data, the number of potentially available fully driverless vehicles has grown in all three metros where the service is offered. Tesla continues to expect Robotaxi operations to expand to 7 metros (with further deployments in Orlando, Tampa, Las Vegas, Phoenix, and Miami) in the coming months (we believe this could include using safety observers and/or drivers to start, though Dallas and Houston launched driverlessly). Importantly, on the 1Q26 call, Tesla's CEO noted that the next version of FSD (v15) could be needed to start scaling more meaningfully (and Tesla is targeting for this version of FSD to be available late this year). Furthermore, media reports suggest that availability of the service in the driverless cities (i.e. Austin, Dallas, and Houston) remains limited.

For Rivian, on its 1Q26 earnings call the company highlighted its March announcement with Uber, where Uber will deploy up to 50K robotaxis based on the R2 platform and invest up to \$1.25 bn into Rivian. The companies plan for the initial launch to be in Miami and San Francisco in 2028, with 25 cities (including potentially in Europe and Canada) by 2031. Rivian will receive a licensing fee for vehicles using its tech, and Rivian is not limited in selling its AV software to consumers, but its R2 robotaxis will be offered exclusively on the Uber platform. See our note linked here for more details.

Finally, Mobileye commented that it remains on track for deployment in LA with the VW Group (MOIA) on the Uber network without a safety driver by year end, and scaling in 2027. VW also remains on track to homologate the autonomous ID. Buzz vehicle (which is operated by Mobileye software) in Europe in 1H27. In addition, Mobileye outlined plans to be in at least 6 cities and operating hundreds of robotaxis for 2027. As a part of its plans outside of LA, Mobileye expects to the start offering rides in Orlando later this year on VW ID.Buzz vehicles, with Beep as a partner, albeit with a safety driver for now.

# Implications

Within the Autos & Industrial Tech space, autonomy remains a key theme. For Tesla, we think that investors will remain focused on the performance of Tesla's robotaxi service, the pace with which the company can scale fully driverless operations and hit its launch targets, and its ability to make its FSD consumer product an eyes-off solution (recall the company now expects this to be in the late 2026 timeframe at the earliest and only for HW4/AI4 vehicles). For Rivian, with the company now charging for its Autonomy+ product, its ability to execute on its tech roadmap (including point-to-point L2 later in 2026, L3 in 2027, and L4 with Uber in 2028) will be important for how fast it can ramp its high-margin software and digital services revenue.

Within the US rideshare landscape, we remain constructive on Uber and Lyft. Near term, we expect investors to focus on the health of the digital consumer, and on announcements surrounding AV partnerships and market share dynamics - to which we believe that the two companies are well positioned to capitalize on the growing AV opportunity. We expect that the two platforms will continue to invest in 3P partnerships as they seek to operate as asset-light-third-party (3P) marketplaces for AV fleet operators to plug their supply into as a way to generate demand.

We also discussed our global outlook and progress on AVs, along with stocks tied to the theme, in our April robotaxi deep dive linked here.

# Valuation and key risks

Exhibit 6: Stock ratings, key risks, and 12-month price targets 

<table><tr><td>Company</td><td>Ticker</td><td>GS Rating</td><td>Current Price</td><td>Price Target</td><td>PT Methodology</td><td>Key upside/downside risks</td></tr><tr><td>Tesla</td><td>TSLA</td><td>Neutral</td><td>$416</td><td>$375</td><td>Q5-Q8 EPS</td><td>EV adoption, margins, market share, the auto cycle, operational execution, key person risk, products/capabilities like FSD/4680, tariffs</td></tr><tr><td>Rivian</td><td>RIVN</td><td>Neutral</td><td>$17</td><td>$16</td><td>Q5-Q8 Sales</td><td>Pre-orders/sales volumes, produ

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be

supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
