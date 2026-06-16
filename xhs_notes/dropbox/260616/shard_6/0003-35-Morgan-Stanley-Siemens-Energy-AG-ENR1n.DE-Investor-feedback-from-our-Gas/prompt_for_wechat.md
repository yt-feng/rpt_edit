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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Siemens Energy AG | Europe

# Investor feedback from our Gas turbine supply / demand report

After a busy week of discussions on our supply / demand report, we aim to summarize investor feedback below. It is clear that the stock is still very well owned, and mostly we received fairly wide-ranging push back to our supply demand view in 2030.

## Key Takeaways

Despite recent underperformance, we think ENR is still a consensus long. Some had used the May / June pull back to €150 to re-enter the stock.  
Investors reasons for owning here. (1) Consensus still too low in 2030, (2) Grid underappreciated, (3) Gas turbine order can grow into 2027, (4) Valuation.  
On Supply demand. We were surprised that the supply side Gas turbine capacity was not better understood. Many disagree that 2026 is peak (GW) orders.  
Where we agree, is that the supply / demand thesis playing out is a slow-burn, and turbine pricing is still strong today. In part, why we keep ENR OW.  
Overall view: Stock still range-bound through fiscal 3Q26 results, with potential for new 2030 targets (11th Nov) to act as the final clear positive catalyst.

Exhibit 1: Change to 2028 consensus EBITA following results and the 2025 CMD (14th Nov), and change in share price in the next 30 days. More recently, as consensus has moved higher, the rate of consensus upgrades has been decreasing. This has resulted in less share price follow through, which is a natural reaction as the 'rate of change' diminishes. We expect mid-single digit upgrades to 2030 consensus EBITA to be triggered by new 2030 targets (11th November)  
![](images/b896bb4b5ae38bd4263d812b003faa5940ae7849cff8a1ce07c9cd38f2e0fa6c.jpg)

<details>
<summary>bar chart</summary>

| Date | Change in ENR group 2028 EBITA consensus in the next 30 days (%) | Share price move in the next 30 days (%) |
| :--- | :--- | :--- |
| 7th Aug '24 | 7.7 | 2 |
| 12th Nov '24 | 13.2 | 30 |
| 27th Jan '25 | 4.9 | 16 |
| 16th Apr '25 | 13.3 | 30 |
| 14th Nov '25 | 16.2 | 18 |
| 11th Feb '26 | 5.3 | 5 |
| 23rd Apr '26 (pre-release) | 6.5 | -2 |
</details>

Source: Visible alpha consensus. Refinitiv

We published an update of our Gas turbine supply model last week (Exhibit 2) in a report: Siemens Energy. Caught in multiple crosswinds. Supply demand dynamics are a valid concern for 2030

MS & CO. INTERNATIONAL PLC+

## Max R Yates

Equity Analyst

Max.Yates@morganstanley.com +44 20 7425-1917

## Sara Chemello

Research Associate

Sara.Chemello@morganstanley.com +44 20 7425-2931

Siemens Energy AG (ENR1n.DE, ENR GY)  
Capital Goods | Germany

<table><tr><td>Stock Rating</td><td>Overweight</td></tr><tr><td>Industry View</td><td>In-Line</td></tr><tr><td>Price target</td><td>€200.00</td></tr><tr><td>Shr price, close (Jun 12, 2026)</td><td>€153.58</td></tr><tr><td>52-Week Range</td><td>€191.66-82.72</td></tr><tr><td>Mkt cap, curr (mn)</td><td>€111,598</td></tr><tr><td>Net debt (09/26e) (mn)*</td><td>€(8,010)</td></tr><tr><td>EV, curr (mn)*</td><td>€107,182</td></tr></table>

\* = GAAP or approximated based on GAAP

<table><tr><td>Fiscal Year Ending</td><td>09/25</td><td>09/26e</td><td>09/27e</td><td>09/28e</td></tr><tr><td>Sales / Revenue (€mn)**</td><td>39,077</td><td>44,002</td><td>49,407</td><td>54,637</td></tr><tr><td>EBITDA (€mn)**</td><td>3,350</td><td>6,604</td><td>8,608</td><td>10,909</td></tr><tr><td>EBIT (€mn)**</td><td>2,355</td><td>5,059</td><td>7,061</td><td>9,333</td></tr><tr><td>EPS (€)**</td><td>1.78</td><td>4.32</td><td>6.28</td><td>8.52</td></tr><tr><td>Prior EPS (€)**</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>ModelWare EPS (€)</td><td>1.78</td><td>4.32</td><td>6.28</td><td>8.52</td></tr><tr><td>EPS (€)§</td><td>1.58</td><td>4.38</td><td>6.01</td><td>7.68</td></tr><tr><td>P/E**</td><td>55.7</td><td>35.6</td><td>24.5</td><td>18.0</td></tr><tr><td>EV/revenue*</td><td>2.1</td><td>2.4</td><td>2.0</td><td>1.7</td></tr><tr><td>EV/EBITDA**</td><td>24.9</td><td>15.8</td><td>11.5</td><td>8.6</td></tr><tr><td>EV/EBIT**</td><td>35.4</td><td>20.6</td><td>14.1</td><td>10.1</td></tr><tr><td>DPS (€)</td><td>0.70</td><td>2.07</td><td>3.04</td><td>4.16</td></tr><tr><td>Div yld (%)</td><td>0.7</td><td>1.3</td><td>2.0</td><td>2.7</td></tr><tr><td>FCF yld ratio (%)*</td><td>4.4</td><td>5.8</td><td>5.3</td><td>6.2</td></tr><tr><td>Net debt (€mn)*</td><td>(5,196)</td><td>(8,010)</td><td>(10,789)</td><td>(13,838)</td></tr><tr><td>Net debt/EBITDA**</td><td>NM</td><td>NM</td><td>NM</td><td>NM</td></tr><tr><td>RNOA (%)**</td><td>18.2</td><td>90.4</td><td>(7,749.7)</td><td>(420.2)</td></tr><tr><td>ROE (%)**</td><td>17.3</td><td>35.9</td><td>54.7</td><td>62.4</td></tr></table>

Unless otherwise noted, all metrics are based on MS ModelWare  
framework  
\*\* = Based on consensus methodology  
§ = Consensus data is provided by Refinitiv Estimates  
\* = GAAP or approximated based on GAAP  
e = MS estimates

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

For other recent Siemens Energy reports, see (1) 1Q26 Gas turbine orders. A step-change in DC bookings (May-26) (2) Siemens Energy. Getting into thin air. Stay OW (April-26), (3) Siemens Energy: Remove as a top-pick, but stay OW (March-26).

Backdrop. Since we removed Siemens Energy as a top-pick (March-26) our message on Siemens Energy has become more nuanced, despite keeping the overweight. As a recap of our view today, our thoughts on the stock are as follows. In our view, Siemens Energy is an earnings momentum story in end markets have historically been highly cyclical (see Exhibit 4) from a demand and profitability stand-point. For Siemens Energy, we think we are in the latter part of the earnings upgrades story, as we are now only 5% ahead of consensus for 2030 EBITA (for much of 2024-25 we were 20% ahead of consensus 2028 EBITA). In addition, the rate of change in the equity story across a number of areas is slowing down. We think the size of consensus upgrades is becoming smaller (see Exhibit 1), and the quarterly rate of increases in customer commitments (slot reservations and backlog) has also peaked (Exhibit 3). We also think Gas turbine (new unit GW orders) in FY27 will be flat YOY at best, but more likely lower YOY for Siemens Energy than in FY26. Finally, we disagree with the idea that Gas turbine aftermarket alone can carry the equity story into next decade as we expect this to only account for 20-25% of group EBITA in 2030.

The risk that longer-term investors need to grapple with is whether EBITA margin normalization in Gas services new equipment and Grid tech will offset the further EBIT growth in the services business into the 2030s. Ultimately, the key debate on the stock in our mind is on whether Siemens Energy can continue to generate mid-to-high single digit earnings growth in 2030-35, or earnings growth flattens out beyond 2030, and what the appropriate multiple for the stock on 2030 is in both those scenarios.

Our logic for keeping the Overweight in last week's report was largely for three reasons. The first was that when we wrote the report, we felt the risk reward overall was still skewed positively into year end. We argued in that report for a floor in the stock at €138, and we felt that the shares could have a run-up towards our €200 target price into year end around the new targets issued on 11th November. Second, we noted there was another catalyst for the stock into year end - the new targets which would trigger further consensus upgrade, albeit lower upgrades than what was seen with the last 2025 CMD. Equally, we did not think that we would immediately see signs of Gas turbine pricing plateauing, or even moderating for some of the engine companies this fiscal year. Higher slot reservation pricing alone should underpin better pricing on new orders for the next twelve months. Finally, we wrote that one of the reasons Siemens Energy had lagged GEV, and the valuation gap had widened, was concerns around Siemens Energy's Middle East exposure. If we were to see a US deal signed around the Iran conflict we felt this would help the relative valuation of Siemens Energy versus GE Vernova in the near-term, given Siemens Energy has relatively higher middle east exposure.

Shifting to investor feedback, from our conversations, we found that ownership of Siemens Energy across all types of investors is still relatively high. We have previously discussed (Exhibit6) that European long-only positioning in Siemens Energy now reflects other large-cap Electrical stocks in our coverage. We also found that a few investors we spoke with had used the May/ June pull-back in the stock (before last week) to turn more positive. It remains clear that the region with the highest investor optimism on the broader gas turbine cycle, and scope for orders to continue to move higher, was across US investors. A couple of points that surprised us from our discussions were as follows. We were surprised that we received so many requests for our gas turbine supply model (>50 requests) which suggests that supply dynamics have received less focus compared to demand until now. We also were surprised that the discussions with investors were very 'bottom up focused' and were surprised that we were not having more discussions linking the bigger picture risk of data center build out delays to the gas turbine stocks and specifically phasing of order intake.

## The five main discussion / push back points we had with investors last week on our report.

(1) A debate on how much of our 135GW Gas turbine / power supply solutions would materialize. We spent a lot of last week discussion how much of our 135GW of tracked power solutions would materialize. In our chart in Exhibit 2, there was agreement that the 97GW of Gas turbine capacity was largely underpinned. However, some investors argued that the newer solutions may not actually materialize, and therefore the eventual capacity could be lower than our calculation. We would argue that the 'non-Gas turbine' solutions are seeing success given recent primary power order wins across CAT, Wartsila and Hyundai in primary power, as well as recent Bloom Energy successes. Similarly, as Stephen Byrd observes in his recent report, Bitcoin miners also continue to play an active role in solving the time to power equation in the US (Link to report). In our view, this highlights that 'lead times' and 'time to power' remain the primary driver of decision making when it comes to behind the meter power solutions for data centers. Ultimately, there is a sharp increase in small gas turbine capacity and engine capacity that is all competing for the same behind the meter opportunity, and this will in our view have implications for pricing and profitability down the line.

(2) The consensus view is that the demand from data centers will eventually accrue to the Gas turbine manufacturers, as gas turbines replaced some of the 'bridging solutions' and more data centers receive grid connections in the medium term. We frequently encountered the view that the data center demand would eventually accrue to the gas turbine manufacturers in the form of larger turbines. The consensus view is that gas turbines will either eventually be connected to the grid (and served by large utility gas turbines), or that some of the bridging power solutions would be replaced by more permanent turbines. We agree that this is directionally correct, though speed and timing of this trend is difficult to know. Equally, in the meantime, we can also find that alternative behind the meter solutions initially continue to take share, and then in the medium term potentially drive some over-supply. We think behind the meter smaller gas turbine orders has been a very profitable market for the gas turbine manufacturers, and this is not immune from pressure. However, we also think in this scenario Wartsila would start to look quite vulnerable from a pricing perspective, hence our underweight rating on the stock. Ultimately, we think it is the capacity additions from the non-turbine makers which are arguably causing the bigger risks, as opposed to the capacity

additions made by the large gas turbine makers.

(3) Some investors argue for stronger for longer demand and gas turbine orders, which would more than offset supply side capacity additions. We found it interesting from our conversations that there was quite often a fairly simplistic link that was made from a high level of demand for compute and tokens, to Gas turbines orders continuing to grow out to the end of the decade. Our observation would be that the data center build out can only occur was fast as the weakest part of the supply chain will allow (ie permitting and labour). We would simply argue that a lot of data center behind the meter solutions have been ordered, relative to what can actually be built in the US by the end of the decade. In the end, we think there will not be unlimited gas turbine orders added to backlogs if the rate of actual data center build cannot keep up. Ultimately, we think the constraint for data center build is shifting from being power solutions (ie Gas turbines), and is increasingly areas like Engineering and construction, labour and permitting.

(4) Investors view was that the company commentary / industry channel checks on leading edge gas turbine pricing remained positive. We found investors still felt that industry commentary on gas turbine pricing remained positive. This is fair as our own discussions with industry analysts of US customers still point to resilient pricing. Equally, we also expect the companies to point to resilient pricing on slot reservations in the next 1-2 quarter. What we would expect is that the first cracks start to appear in behind the meter solutions pricing, particularly as companies like Wartsila (and others expanding capacity) start to open up bookings for 2030 with enlarged capacity. We would argue that price points across the likes of Wartsila and other engine makers like Hyundai (as we have flagged in previous reports) remain comparatively underwhelming to what we hear from Gas turbine manufacturers.

(5) We are finding that a large part of the narrative for the Gas turbines OEMs has become about shifting the debate more towards the upside of the Grid division (as opposed to the debate previously focusing on 'just' gas turbines). As a starting point for grid, we would start by saying that numbers have moved up a long way already. For context, consensus EBITA for Grid tech in 2029 is €5bn, and this is up \~100% from where 2029 consensus expectations were at the start of 2025. Consensus margins are expected to be 23.5% in 2030 (vs MSe at 25%) and versus a previous cyclical peak of 15%. Finally, order intake will land at around €25bn in 2026, compared to €7.3bn in 2021, and consensus assumes this continues to grow mid-single digit percentage for 2027-28. We agree the US is earlier on in its Grid investment cycle, but in contrast, we think a lot of the order intake for the European grid build out is already in the order-book. We see European order intake for Siemens Grid tech as more a case of stabilizing at a high level. Simply put, we also think the positive surprises in Grid are also diminishing, just by a function of expectations also having moved up significantly for this division. In addition, we also argue there is a limit to where revenues in this division can get to as a result of capacity constraints. We expect a 2029-30 deceleration in Grid technology revenue growth, after \~20% growth per year in 2026-28. Finally, as a result of lower barriers to entry, more volatile margins across the cycle, and limited aftermarket, we are cautious about making arguments about placing similar multiples on the grid tech business as either the Gas services multiple, or other Electrification companies like

Schneider and Eaton.

Valuation. After a volatile week in the share price, Siemens Energy is left trading on 12.3x 2028 EV/EBITA, which is a small discount to the broader Cap Goods sector on 13x 2028 EV/EBITA. In absolute, Siemens Energy is trading on a 6.2% FCF yield. Siemens Energy is also trading at a 42% discount to GE Vernova (21.2x), and this compares to a recent discount of 25-50%. Finally, it also compares to Wartsila trading on 14.6x 2028 EV/EBITA, and we think Wartsila remains comparatively expensive and we retain an Underweight here. We found from our conversations there was sympathy towards our more cautious view on Wartsila, but equally a hesitancy to be outright negative ahead of what we know will be a very good quarter for Energy orders given already announced data center contracts.

Exhibit 2: MS Gas turbine / power solutions supply model. We have updated our supply model for recent announcements, and the potential 2030 supply rises to 135GW by 2030 (we forecast 116GW supply in our Jan 2026 report: The capacity conundrum). The traditional gas turbine capacity in 2030 (97GW) looks broadly consistent with where orders should stabilize in 2027-30, but increasingly there are alternative solutions (engines and fuel-cells) that are competing in the 'behind the meter' data center primary power market.

Total Gas turbine + Primary engine + Fuel cell Supply (GW)  
![](images/24e84ced6181e4ccc7a769763ec2d33572aec11b81bdeb59f22ca5aae4765ee7.jpg)

<details>
<summary>bar chart</summary>

| Company | Value |
| :--- | :--- |
| GEV | 26 |
| Siemens Energy | 25.5 |
| Mitsubishi | 19.9 |
| CAT Solar Turbines | 78 |
| Doosan | 84 |
| Other Turbine OEM | 92 |
| Total 2030 trad. Gas Turbines | 97 |
| FTA+ Boom + Arbor | 102 |
| Engines targeting DC (prime) | 130 |
| Bloom Energy | 135 |
| Total 'all in '2030 Supply | 135 |
</details>

Source: Company data. MS Gas turbine supply model estimates.

Exhibit 3: GE Vernova (single cycle) and Siemens Energy (combined cycle) customer commitments (based on calendar dates). Siemens Energy have guided to 'customer commitments' ending

[中间内容因长度限制已省略]

lients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: Capital Goods

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/12/2026)</td></tr><tr><td>Arthur Sitbon, CFA</td><td></td><td></td></tr><tr><td>ITM Power (ITM.L)</td><td>O (04/29/2026)</td><td>129p</td></tr><tr><td>Luke Holbrook</td><td></td><td></td></tr><tr><td>AutoStore Holdings Ltd-W/I (AUTO.OL)</td><td>E (08/15/2025)</td><td>NKr 11.36</td></tr><tr><td>Max R Yates</td><td></td><td></td></tr><tr><td>ABB (ABBN.S)</td><td>E (12/09/2024)</td><td>SFr 81.62</td></tr><tr><td>Alfa Laval AB (ALFA.ST)</td><td>E (03/05/2026)</td><td>SKr 530.80</td></tr><tr><td>Alstom (ALSO.PA)</td><td>E (12/07/2022)</td><td>€16.19</td></tr><tr><td>Assa Abloy AB (ASSAb.ST)</td><td>E (03/16/2020)</td><td>SKr 332.40</td></tr><tr><td>Atlas Copco (ATCOa.ST)</td><td>O (12/08/2025)</td><td>SKr 185.95</td></tr><tr><td>Epiroc AB (EPIRa.ST)</td><td>O (03/12/2026)</td><td>SKr 266.50</td></tr><tr><td>GEA Group AG (G1AG.DE)</td><td>U (12/08/2025)</td><td>€55.90</td></tr><tr><td>Halma PLC (HLMA.L)</td><td>E (11/22/2018)</td><td>3,898p</td></tr><tr><td>KION Group AG (KGX.DE)</td><td>E (03/10/2023)</td><td>€37.28</td></tr><tr><td>Knorr Bremse AG (KBX.DE)</td><td>O (12/08/2025)</td><td>€101.80</td></tr><tr><td>Kone Oyj (KNEBV.HE)</td><td>U (12/09/2024)</td><td>€48.72</td></tr><tr><td>Legrand (LEGD.PA)</td><td>O (03/28/2024)</td><td>€133.55</td></tr><tr><td>Metso Corporation (METSO.HE)</td><td>E (12/07/2022)</td><td>€14.80</td></tr><tr><td>Prysmian SpA (PRY.MI)</td><td>E (11/05/2024)</td><td>€143.90</td></tr><tr><td>Rexel S.A. (RXL.PA)</td><td>O (12/09/2024)</td><td>€36.42</td></tr><tr><td>Rotork PLC (ROR.L)</td><td>E (12/08/2025)</td><td>306p</td></tr><tr><td>Sandvik (SAND.ST)</td><td>E (03/12/2026)</td><td>SKr 378.60</td></tr><tr><td>Schindler Holding AG (SCHP.S)</td><td>E (12/08/2025)</td><td>SFr 262.60</td></tr><tr><td>Schneider Electric (SCHN.PA)</td><td>O (10/27/2025)</td><td>€265.30</td></tr><tr><td>Siemens (SIEGn.DE)</td><td>E (10/14/2025)</td><td>€264.50</td></tr><tr><td>Siemens Energy AG (ENR1n.DE)</td><td>O (04/03/2023)</td><td>€153.58</td></tr><tr><td>Signify NV (LIGHT.AS)</td><td>U (12/08/2025)</td><td>€20.42</td></tr><tr><td>SKF (SKFb.ST)</td><td>++</td><td>SKr 237.90</td></tr><tr><td>Spirax Group PLC (SPX.L)</td><td>O (12/09/2024)</td><td>6,810p</td></tr><tr><td>Vestas Wind Systems A/S (VWS.CO)</td><td>E (05/05/2020)</td><td>DKr 166.10</td></tr><tr><td>Wartsila Oyj Abp (WRT1V.HE)</td><td>U (03/03/2026)</td><td>€33.06</td></tr><tr><td>Weir Group PLC (WEIR.L)</td><td>E (05/12/2025)</td><td>2,324p</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
