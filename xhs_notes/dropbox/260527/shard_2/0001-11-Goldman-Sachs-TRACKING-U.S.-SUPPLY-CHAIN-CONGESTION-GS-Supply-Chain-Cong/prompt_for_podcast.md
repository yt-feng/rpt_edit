你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
TRACKING U.S. SUPPLY CHAIN CONGESTION

# GS Supply Chain Congestion Scale: May 26th; Bottleneck Scale Remains at '2'

![](images/1972e376f4baedb7cbb01269f5f4e1bbf3ec8a2e40e25a4ad610e5b462c68eb9.jpg)

<details>
<summary>gauge</summary>

| Category          | Value |
| ----------------- | ----- |
| Fully Open        | 1     |
| Fully Bottlenecked| 10    |
</details>

Scale is based solely off weekly metrics to give more granularity on high frequency data indications; see Appendix for scale that combines weekly and monthly metrics

Source: GS Global Investment Research

Our weekly bottleneck scale remained at '2' this week, reflecting the absolute level of the congestion index increasing on a sequential basis (+10% w/w after last week's -2% move; Exhibit 2). For this week's scale and index, the number of container ships waiting to dock and unload goods along the West Coast increased from 0 to 1, while backlogs along the East Coast rose from 4 to 5 (Exhibit 6). West Coast rail intermodal traffic growth accelerated sharply versus last week (+9% YoY vs +3.5% YoY last week;

Exhibit 7), while rail service metrics were mixed. Chassis dwell times were unchanged on average at US ports in the prior week (Exhibit 9), while ocean container shipping rate growth (China to US West Coast) decelerated from +18% to +14% YoY (Exhibit 10).

# Jordan Alliger

+1(212)357-4913

jordan.alliger@gs.com

GS & Co. LLC

# Andrzej Tomczyk, CFA

+1(212)357-4445

andrzej.tomczyk@gs.com

GS & Co. LLC

# Paul Stoddard

+1(801)744-3761

paul.x.stoddard@gs.com

GS & Co. LLC

Exhibit 1: Our weekly composite index increased in the most recent week (+10% w/w); the bottleneck scale remained at '2'; overall bottleneck levels remain well below peak congestion levels when scale was at '10' and now imply levels in line with pre-Covid fluidity GS Weekly Bottleneck Index, Feb 2020 - May 2026   
![](images/9ae3394b693fb9b6db4264daa3603be4fd9a695b3e6c4302908e96645dcad547.jpg)

<details>
<summary>line</summary>

| Date       | Value   |
| ---------- | ------- |
| Feb 3 - Feb 9 | 100.00  |
| May 4 - May 10 | 150.00  |
| Aug 3 - Aug 9 | 200.00  |
| Nov 2 - Nov 8 | 300.00  |
| Feb 1 - Feb 7 | 500.00  |
| May 3 - May 9 | 400.00  |
| Aug 2 - Aug 8 | 600.00  |
| Nov 1 - Nov 7 | 800.00  |
| Jan 31 - Feb 6 | 950.00  |
| May 2 - May 8 | 700.00  |
| Aug 1 - Aug 7 | 500.00  |
| Oct 31 - Nov 6 | 300.00  |
| Jan 30 - Feb 5 | 200.00  |
| May 1 - May 7 | 150.00  |
| July 31 - Aug 6 | 150.00  |
| Oct 30 - Nov 5 | 150.00  |
| Jan 29 - Feb 4 | 150.00  |
| Apr 29 - May 5 | 150.00  |
| July 29 - Aug 4 | 150.00  |
| Oct 28 - Nov 3 | 150.00  |
| Jan 27 - Feb 2 | 150.00  |
| Apr 28 - May 4 | 150.00  |
| Jul 28 - Aug 3 | 150.00  |
| Oct 27 - Nov 2 | 150.00  |
| Jan 26 - Feb 1 | 150.00  |
| Apr 27 - May 3 (2026) | 150.00 |
</details>

Source: GS Global Investment Research

Exhibit 2: Our average weekly bottleneck score in May is tracking at 2.0; this result is down significantly from the Dec21/Jan22 peak of congestion and close to in line with the pre-Covid baseline GS Weekly Congestion Scale, Scored by Month\*   
![](images/c693b9888207b2711d4699188a6f624f503cdbe24cb574076f2122a88f410e0c.jpg)

<details>
<summary>bar</summary>

| Date | Value |
|---|---|
| May-20 | 1.0 |
| Jun-20 | 1.5 |
| Jul-20 | 2.0 |
| Aug-20 | 2.0 |
| Sep-20 | 2.0 |
| Oct-20 | 3.0 |
| Nov-20 | 4.0 |
| Dec-20 | 5.0 |
| Jan-21 | 6.0 |
| Feb-21 | 5.5 |
| Mar-21 | 4.5 |
| Apr-21 | 3.5 |
| May-21 | 4.0 |
| Jun-21 | 5.5 |
| Jul-21 | 6.5 |
| Aug-21 | 7.5 |
| Sep-21 | 8.5 |
| Oct-21 | 9.5 |
| Nov-21 | 10.0 |
| Dec-21 | 9.0 |
| Jan-22 | 8.5 |
| Feb-22 | 6.5 |
| Mar-22 | 6.0 |
| Apr-22 | 5.0 |
| May-22 | 4.5 |
| Jun-22 | 5.5 |
| Jul-22 | 4.5 |
| Aug-22 | 4.0 |
| Sep-22 | 3.5 |
| Oct-22 | 3.0 |
| Nov-22 | 2.5 |
| Dec-22 | 2.0 |
| Jan-23 | 1.5 |
| Feb-23 | 1.5 |
| Mar-23 | 1.5 |
| Apr-23 | 1.5 |
| May-23 | 1.5 |
| Jun-23 | 1.5 |
| Jul-23 | 1.5 |
| Aug-23 | 1.5 |
| Sep-23 | 1.5 |
| Oct-23 | 1.5 |
| Nov-23 | 1.5 |
| Dec-23 | 1.5 |
| Jan-24 | 1.5 |
| Feb-24 | 1.5 |
| Mar-24 | 1.5 |
| Apr-24 | 1.5 |
| May-24 | 1.5 |
| Jun-24 | 1.5 |
| Jul-24 | 1.5 |
| Aug-24 | 1.5 |
| Sep-24 | 1.5 |
| Oct-24 | 1.5 |
| Nov-24 | 1.5 |
| Dec-24 | 1.5 |
| Jan-25 | 1.5 |
| Feb-25 | 1.5 |
| Mar-25 | 1.5 |
| Apr-25 | 1.5 |
| May-25 | 1.5 |
| Jun-25 | 1.5 |
| Jul-25 | 1.5 |
| Aug-25 | 1.5 |
| Sep-25 | 1.5 |
| Oct-25 | 1.5 |
| Nov-25 | 1.5 |
| Dec-25 | 1.5 |
| Jan-26 | 1.5 |
| Feb-26 | 1.5 |
| Mar-26 | 1.5 |
| Apr-26 | 1.5 |
</details>

\*Numbers reflect the average weekly score seen in each respective month   
Source: GS Global Investment Research

As a reminder (and to help reiterate why and how we construct the index), please refer to the Appendix following Exhibit 17. Additionally, for further clarity on tracked congestion metrics, please refer to the glossary following Exhibit 19.

# Transport Subsectors to Watch as Congestion Remains Muted

The key question remains as to what impact tariffs and geopolitical conflicts will have on demand and timing of freight flows, as well as ability to normalize around global trade. Please see our recent tariff impact tracker for additional commentary. Should supply chain pressures broadly continue to mitigate, then it is conceivable we could see the index remaining more consistently in ‘1’ territory in 2026.

Of the metrics we track (Exhibit 3), we provide updates for the weekly and monthly variables below (Exhibit 4 - Exhibit 5).

Exhibit 3: Tracked Congestion Metrics 

<table><tr><td colspan="2">Tracked Metrics</td></tr><tr><td>Weekly VariablesContainer Ships Waiting to Dock at LA/LBContainer Ships Waiting Along to U.S. Gulf/East CoastUNP Intermodal TrafficUNP Intermodal VelocityUNP Intermodal DwellBNSF Intermodal TrafficBNSF Intermodal VelocityBNSF Intermodal DwellOcean Shipping Rates, East Asia to U.S. West CoastChassis Street Dwell, 20ft ContainersChassis Street Dwell, 40/45ft ContainersChassis Terminal Dwell Time, 20ft ContainersChassis Terminal Dwell Time, 40/45ft Containers</td><td>Monthly VariablesContainer Weighted Average Dwell (San Pedro&#x27;s Bay)Containers Dwelling &gt;5 days (San Pedro&#x27;s Bay)PMI Manufacturing Supplier Delivery TimeBig Three&#x27; West Coast Ports&#x27; Inbound Loaded ContainersLMI Transportation CapacityLMI Warehousing CapacityLMI Warehousing UtilizationDoor to Door Shipping Days, China to USClass 8 Trucking Driver Count GrowthRail Container Dwell (San Pedro&#x27;s Bay)</td></tr></table>

Source: GS Global Investment Research

Exhibit 4: Bottleneck metrics indicated mixed results this week versus last 

<table><tr><td></td><td>Feb 23 - Mar 1</td><td>Mar 2 - Mar 8</td><td>Mar 9 - Mar 15</td><td>Mar 16 - Mar 22</td><td>Mar 23 - Mar 29</td><td>Mar 30 - Apr 5</td><td>Apr 6 - Apr 12</td><td>Apr 13 - Apr 19</td><td>Apr 20 - Apr 26</td><td>Apr 27 - May 3</td><td>May 4 - May 10</td><td>May 11 - May 17</td></tr><tr><td>Container Ships Waiting to Dock at LA/LB</td><td>3</td><td>1</td><td>2</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Container Ship Backup (East and Gulf Coast)*</td><td>12</td><td>8</td><td>9</td><td>11</td><td>5</td><td>4</td><td>4</td><td>1</td><td>2</td><td>2</td><td>4</td><td>5</td></tr><tr><td>UNP Intermodal Traffic (YoY Growth)</td><td>-5.7%</td><td>-4.7%</td><td>-6.6%</td><td>-10.4%</td><td>-8.7%</td><td>-9.0%</td><td>-8.2%</td><td>-4.3%</td><td>-2.0%</td><td>-0.3%</td><td>-0.8%</td><td>8.4%</td></tr><tr><td>UNP Intermodal Velocity (YoY Growth)</td><td>10.9%</td><td>8.6%</td><td>12.7%</td><td>11.3%</td><td>8.5%</td><td>5.0%</td><td>8.3%</td><td>7.4%</td><td>8.3%</td><td>3.9%</td><td>2.5%</td><td>4.2%</td></tr><tr><td>UNP System Dwell (Hours)</td><td>19.4</td><td>19.5</td><td>19.8</td><td>20.2</td><td>20.3</td><td>20.1</td><td>19.9</td><td>19.6</td><td>19.4</td><td>20.0</td><td>20</td><td>19.9</td></tr><tr><td>BNSF Intermodal Traffic (YoY Growth)</td><td>2.4%</td><td>4.0%</td><td>1.9%</td><td>2.6%</td><td>1.9%</td><td>2.6%</td><td>2.3%</td><td>5.7%</td><td>4.7%</td><td>7.7%</td><td>7.8%</td><td>9.7%</td></tr><tr><td>BNSF Intermodal Velocity (YoY Growth)</td><td>-0.3%</td><td>1.6%</td><td>3.2%</td><td>3.2%</td><td>3.3%</td><td>-3.1%</td><td>-1.6%</td><td>-2.4%</td><td>-2.1%</td><td>-3.9%</td><td>-0.6%</td><td>-3.7%</td></tr><tr><td>BNSF System Dwell (Hours)</td><td>21.7</td><td>21.6</td><td>21.8</td><td>22.0</td><td>22.6</td><td>22.5</td><td>22.1</td><td>22.7</td><td>22.3</td><td>22.1</td><td>22.3</td><td>23.0</td></tr><tr><td>Ocean Shipping Rates, East Asia to U.S. West Coast (YoY Growth)</td><td>-48.2%</td><td>-23.9%</td><td>-15.0%</td><td>-6.0%</td><td>-0.1%</td><td>7.7%</td><td>0.9%</td><td>13.2%</td><td>14.9%</td><td>17.4%</td><td>18.1%</td><td>14.3%</td></tr><tr><td>Chassis Street Dwell, 20ft Containers (Days)</td><td>4.8</td><td>3.8</td><td>4.1</td><td>4.3</td><td>5.3</td><td>4.9</td><td>4.4</td><td>4.2</td><td>5.4</td><td>4.5</td><td>4.2</td><td>4.9</td></tr><tr><td>Chassis Street Dwell, 40/45ft Containers (Days)</td><td>5.2</td><td>5.3</td><td>5.9</td><td>7.0</td><td>6.5</td><td>6.9</td><td>5.7</td><td>5.8</td><td>6.0</td><td>5.5</td><td>5.7</td><td>5.6</td></tr><tr><td>Chassis Terminal Dwell Time, 20ft Containers (Days)</td><td>9.7</td><td>9.9</td><td>9.7</td><td>10.2</td><td>10.6</td><td>10.6</td><td>9.4</td><td>9.1</td><td>11.4</td><td>10.3</td><td>10.2</td><td>11.5</td></tr><tr><td>Chassis Terminal Dwell Time, 40/45ft Containers (Days)</td><td>5.0</td><td>5.4</td><td>6.1</td><td>6.9</td><td>7.2</td><td>7.7</td><td>6.3</td><td>6.1</td><td>6.5</td><td>6.2</td><td>6.2</td><td>6.3</td></tr></table>

As of 3/28/22, we added and backdated our estimates for the East and Gulf Coast container ship backlog.

Source: Marine Exchange of Southern California, AAR, STB, Freightos, Pool of Pools, Pacific Merchant Shipping Association, Port of Long Beach, Port of Oakland, Port of Los Angeles, LMI, US Bureau of Labor Statistics, IHS Markit, Refinitiv Eikon, compiled by GS Global Investment Research

Exhibit 5: Lagged monthly bottleneck metrics for March indicated mixed results vs February 

<table><tr><td>Monthly Variables</td><td>Jan-25</td><td>Feb-25</td><td>Mar-25</td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td></tr><tr><td>Container Weighted Average Dwell (Days)</td><td>3.3</td><td>2.8</td><td>2.8</td><td>2.8</td><td>3.0</td><td>2.6</td><td>2.9</td><td>2.7</td><td>2.8</td><td>2.7</td><td>2.6</td><td>2.5</td><td>2.8</td><td>2.6</td><td>2.6</td></tr><tr><td>% of Containers Dwelling &gt; 5 days</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td><td>8%</td></tr><tr><td>Rail Container Dwell (Days)</td><td>7.1</td><td>8.0</td><td>6.8</td><td>4.7</td><td>4.7</td><td>3.3</td><td>5.2</td><td>5.0</td><td>4.0</td><td>3.3</td><td>3.7</td><td>5.1</td><td>6.1</td><td>5.1</td><td>4.4</td></tr><tr><td>Big Three Inbound Loaded Containers (YoY)</td><td>23.6%</td><td>5.8%</td><td>11.6%</td><td>9.5%</td><td>-10.0%</td><td>-4.6%</td><td>8.6%</td><td>-2.1%</td><td>-7.3%</td><td>-11.5%</td><td>-9.5%</td><td>-7.1%</td><td>-11.6%</td><td>0.6%</td><td>-2.0%</td></tr><tr><td>LMI Transportation Capacity</td><td>52.6</td><td>55.1</td><td>53.6</td><td>55.2</td><td>54.7</td><td>52.4</td><td>52.6</td><td>57.3</td><td>55.1</td><td>54.5</td><td>50.0</td><td>36.9</td><td>47.1</td><td>41.0</td><td>39.2</td></tr><tr><td>LMI Warehousing Capacity</td><td>51.7</td><td>50.5</td><td>52.3</td><td>55.4</td><td>50.0</td><td>47.8</td><td>51.1</td><td>50.5</td><td>51.6</td><td>52.0</td><td>54.8</td><td>61.2</td><td>50.0</td><td>50.0</td><td>46.0</td></tr><tr><td>LMI Warehousing Utilization</td><td>68.3</td><td>65.5</td><td>59.7</td><td>60.1</td><td>62.5</td><td>62.2</td><td>59.4</td><td>62.1</td><td>65.3</td><td>56.5</td><td>47.5</td><td>42.9</td><td>54.4</td><td>60.3</td><td>59.8</td></tr><tr><td>Door to Door Shipping Days, China to US</td><td>50</td><td>51</td><td>54</td><td>49</td><td>48</td><td>50</td><td>46</td><td>44</td><td>46</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td><td>47</td></tr><tr><td>Class 8 Driver Count</td><td>1493.1</td><td>1487.6</td><td>1491.4</td><td>1490.6</td><td>1487.7</td><td>1482.7</td><td>1482.5</td><td>1480.2</td><td>1472.3</td><td>1472.6</td><td>1467.8</td><td>1467.2</td><td>1465.6</td><td>1464.9</td><td>1464.1</td></tr><tr><td>PMI Manufacturing Supplier Delivery Time (YoY)</td><td>0.8</td><td>11.6</td><td>6.1</td><td>6.2</td><td>9.8</td><td>-0.3</td><td>-4.7</td><td>2.3</td><td>10.8</td><td>-0.5</td><td>0.1</td><td>5.5</td><td>-0.4</td><td>4.6</td><td>6.3</td></tr></table>

Source: Marine Exchange of Southern California, AAR, STB, Freightos, Pool of Pools, Pacific Merchant Shipping Association, Port of Long Beach, Port of Oakland, Port of Los Angeles, LMI, US Bureau of Labor Statistics, IHS Markit, compiled by GS Global Investment Research

# Weekly Indicator Update

# Anchored Container Ships

■ West Coast container ship backlogs declined from 0 to 1 in the most recent week; East Coast backlogs increased from 4 to 5.

Exhibit 6: 5/1\* container ships backed up this week on the East/West Coast   
West vs. East Coast Container Ship Backlog, Weekly Average, Feb 2020 - May 2026   
![](images/c82aee3b35c46fee633349f9ab00cdcecdcc7c4bb925f6901340ee35429aefc5.jpg)

<details>
<summary>line</summary>

| Date       | West Coast Container Ships Backup | East Coast Container Ship Backup |
|------------|-----------------------------------|----------------------------------|
| Feb 10     | 0                                 | 0                                |
| May 11     | 0                                 | 0                                |
| Aug 10     | 0                                 | 0                                |
| Nov 9      | 0                                 | 0                                |
| Feb 8      | 0                                 | 0                                |
| May 10     | 0                                 | 0                                |
| Aug 9      | 0                                 | 0                                |
| Nov 8      | 0                                 | 0                                |
| Feb 7      | 0                                 | 0                                |
| May 9      | 0                                 | 0                                |
| Aug 8      | 0                                 | 0                                |
| Nov 7      | 0                                 | 0                                |
| Feb 6      | 0                                 | 0                                |
| May 8      | 0                                 | 0                                |
| Aug 7      | 0                                 | 0                                |
| Nov 6      | 0                                 | 0                                |
| Feb 5      | 0                                 | 0                                |
| May 6      | 0                                 | 0                                |
| Aug 5      | 0                                 | 0                                |
| Nov 4      | 0                                 | 0                                |
| Feb 3      | 0                                 | 0                                |
| May 5      | 0                                 | 0                                |
| Aug 4      | 0                                 | 0                                |
| Nov 3      | 0                                 | 0                                |
| Feb 2      | 0                                 | 0                                |
| May 4      | 0                                 | 0                                |
| Aug 10     | 0                                 | 0                                |
| Nov 3      | 0                                 | 0                                |
| Feb 8      | 0                                 | 0                                |
| May 10     | 0                                 | 0                                |
</details>

\*East Coast is estimated via satellite data - includes container ships sitting for more than 3 days within 140 miles of US ports to the right of longitude 100 (i.e., Gulf and East Coast)   
Source: Marine Exchange of Southern California, Refinitiv Eikon, GS Global Investment Research

# Rail Intermodal Trends

West Coast Class 1 Rails' (Union Pacific and Burlington Northern Santa Fe) average intermodal traffic growth accelerated last week versus the prior week (average growth of +9% YoY vs +3% in the week prior).

☐ BNSF intermodal traffic at +9.7% YoY this week vs. +7.8% YoY last week; UNP intermodal traffic at +8.4% YoY vs. -0.8% YoY last week.   
☐ See average BNSF/UNP growth trends in Exhibit 7.

Exhibit 7: West Coast Class 1 Rails' Intermodal Volume Growth, Week 1 - Week 52   
YoY % growth   
![](images/e69cdd2bd632152e5896f6e9c712f49911cda3e91e2dae7007468423a7b8b795.jpg)

<details>
<summary>line</summary>

| Date | 2021 (%) | 2022 (%) | 2023 (%) | 2024 (%) | 2025 (%) | 2026 (%) |
|---|---|---|---|---|---|---|
| 1 | 10 | -18 | -10 | 0 | 15 | -5 |
| 8 | 15 | 30 | -15 | 15 | 10 | -5 |
| 15 | 45 | -5 | -18 | 10 | 15 | 0 |
| 22 | 35 | -5 | -15 | 15 | 10 | 5 |
| 29 | 10 | -5 | -10 | 10 | 5 | -5 |
| 36 | -5 | -5 | 0 | 25 | -5 | -5 |
| 43 | -10 | -5 | 5 | 10 | -10 | -5 |
| 50 | -20 | -5 | 25 | 15 | -10 | -5 |
</details>

Source: AAR, Data compiled by GS Global Investment Research

Exhibit 8: Intermodal growth (UNP and BNSF) is up \~5% YoY on average in May   
West Coast Class 1 Rail Intermodal Traffic YoY % Growth   
![](images/ef5630ca8aaffacc32769c963563f059f6e159909b9542c64e943bc6fcaa6184.jpg)

<details>
<summary>bar</summary>

| Month | Value (%) |
|---|---|
| May-21 | 26.0 |
| Aug-21 | 13.0 |
| Nov-21 | -8.0 |
| Feb-22 | -14.0 |
| May-22 | -7.0 |
| Aug-22 | -5.0 |
| Nov-22 | -3.0 |
| Feb-23 | -14.0 |
| May-23 | -12.0 |
| Aug-23 | -8.0 |
| Nov-23 | 3.0 |
| Feb-24 | 11.0 |
| May-24 | 13.0 |
| Aug-24 | 19.0 |
| Nov-24 | 17.0 |
| Feb-25 | 18.0 |
| May-25 | 10.0 |
| Aug-25 | -5.0 |
| Nov-25 | -10.0 |
| Feb-26 | -7.0 |
| May-26 | 5.0 |
</details>

Source: AAR, Data compiled by GS Global Investment Research

■ West Coast Class 1 Rail terminal dwell and intermodal train speed were mixed in the recent week (detailed below).

☐ UNP terminal dwell decreased slightly to 19.9 hours in the most r

[中间内容因长度限制已省略]

rm impact on the market price of the equity securities discussed in this report, which impact may be directionally counter to the analyst's published price target expectations for such stocks. Any such trading strategies are distinct from and do not affect the analyst's fundamental equity rating for such stocks, which rating reflects a stock's return potential relative to its coverage universe as described herein.

We and our affiliates, officers, directors, and employees will from time to time have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
