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
## PCB/CCL Update: New Prelim Results from Some Key Local Names

We update some new major PCB players prelim results, including WUS/Shennan/SYE all delivering much stronger NP growth vs other non-AI players. We also include CCL's results, which saw surged NP especially for low-end players ramping up from low bases. Among our coverages, WUS/Sytech beat both sellside/buyside cons, while the progress of next gen material/spec upgrade (e.g. M9/10, PTFE, CoWoP etc.) is crucial for sustained structural growth in dollar content.

Update on several new preliminary results. Following our earlier note (Link) on analyzing the earnings performance for different types of PCB players, we have another update (summarized in Table 2 on next page) given there are multiple key names announcing their 1H26 prelim results. Basically, the AI players with high exposure to high-end products (WUS, Shennan, SYE) continue to deliver strong YoY growth in Q2 NP with solid QoQ ramp, echoing our earlier view on 1) robust order pipelines fulfilled by continued capacity expansion, and 2) limited impact on rising materials cost for these types of names. For WUS, its Q2 NP of \~Rmb1.7bn (at mid-pt) beat sellside cons by 10%, which is also higher than buyside cons of <Rmb1.6bn driven by strong AI-related demand and improved profitability especially in Thailand factory (already achieved break-even in Q2). Shennan/SYE's Q2 NP also beat sellside cons, which at least met buyide cons based on our understanding. For most the remaining names, we see the pressure from both supply/demand is just going on. For example, Redboard saw notable YoY/QoQ NP drop in Q2 (using adj.NP here to exclude a material one-off item) due to limited AI exposure, despite its capabilities in mSAP/SAP-related products. Moving into 2H26, we expect AI PCB names to continue outperforming non-AI names in earnings quality.

CCL players are on fire; Sustainability remains to be tested. We now also include the earnings of major CCL players in this earnings analysis (exclude Kingboard Laminates as of now given it reports in semi-annual basis), as many of them also have announced the prelim results. Unlike PCB names, low-end CCL players are experiencing significant NP/profitability rebound driven by both lifting utilization rate and ASP as results of 1) smooth pass-through of rising upstream materials price hike thank to more concentrated landscape, 2) supply tightness of conventional CCL due to capacity shift toward high-end products by leading globally vendors, and 3) some pull-in orders amidst lean downstream inventory levels. Sytech's Q2 NP of \~Rmb2bn largely beat sellside cons by 40%, which should also be even higher than some aggressive buyside expectations in our view. As the most leading local high-end CCL vendor (though its current AI exposure is also limited), although Sytech's NP growth rate seems not as exciting as other names, we do note the latter are ramping up from low bases (all <5% NPM in 1H25 vs Sytech >10%). For conventional CCL names, we think the supply/demand and pricing dynamics of upstream raw materials are critical for continuous monitoring. For high-end/AI CCL (e.g. Sytech and other global players) as well as PCB names, we consider the progress of next gen material/spec upgrade is crucial, given we only see limited adoption of M9 in this year due to the immature supply chain. We believe any breakthrough in the commercialization of leading-edge solutions (e.g. M9/10, PTFE, CoWoP etc.) in the next few quarters will boost investor confidence regarding sustained structural growth in PCB/CCL's dollar content in the coming years.

Table 1 - China PCB/CCL Earnings Summary (Condensed)

<table><tr><td rowspan="2">Company</td><td rowspan="2">Mkt Cap (Rmb bn)</td><td colspan="2">Net Profit (YoY)</td></tr><tr><td>1Q26</td><td>2Q26</td></tr><tr><td colspan="4">Major PCB Maker</td></tr><tr><td>Founder</td><td>55</td><td>195%</td><td>260%</td></tr><tr><td>SYE</td><td>103</td><td>122%</td><td>101%</td></tr><tr><td>Fastprint</td><td>70</td><td>100%</td><td></td></tr><tr><td>Jove</td><td>31</td><td>89%</td><td></td></tr><tr><td>Shennan</td><td>290</td><td>73%</td><td>55%</td></tr><tr><td>Delton</td><td>83</td><td>63%</td><td>108%</td></tr><tr><td>WUS</td><td>249</td><td>63%</td><td>82%</td></tr><tr><td>Victory Giant</td><td>267</td><td>40%</td><td></td></tr><tr><td>Sunshine</td><td>11</td><td>22%</td><td>-14%</td></tr><tr><td>Redboard</td><td>69</td><td>12%</td><td>-20%</td></tr><tr><td>Avary</td><td>228</td><td>-5%</td><td></td></tr><tr><td>CEE</td><td>11</td><td>-17%</td><td></td></tr><tr><td>Goworld</td><td>11</td><td>-21%</td><td></td></tr><tr><td>Kinwong</td><td>69</td><td>-28%</td><td></td></tr><tr><td>Kingshine</td><td>37</td><td>-56%</td><td></td></tr><tr><td>Ellington</td><td>11</td><td>-68%</td><td></td></tr><tr><td>Welgao</td><td>10</td><td>-70%</td><td></td></tr><tr><td>Suntak</td><td>22</td><td>-72%</td><td></td></tr><tr><td>Olympic</td><td>30</td><td>-80%</td><td>-77%</td></tr><tr><td>Aoshikang</td><td>17</td><td>-84%</td><td>-14%</td></tr><tr><td>Bomin</td><td>13</td><td>-140%</td><td>-461%</td></tr><tr><td>Dynamic</td><td>35</td><td>-234%</td><td></td></tr><tr><td colspan="4">Major CCL Maker</td></tr><tr><td>Goldenmax</td><td>70</td><td>764%</td><td>1116%</td></tr><tr><td>Nanya</td><td>78</td><td>611%</td><td></td></tr><tr><td>Baoding</td><td>23</td><td>268%</td><td>1618%</td></tr><tr><td>Sytech</td><td>363</td><td>105%</td><td>136%</td></tr><tr><td>Wazam</td><td>28</td><td>68%</td><td>514%</td></tr></table>

Source: Company data, FactSet, JEF

Jacky He \* | Equity Analyst

+852 3743 8084 | jacky.he@JEF.com

Edison Lee, CFA \* | Equity Analyst

852 3743 8009 | edison.lee@JEF.com

Nick Cheng \* | Equity Analyst

+852 3743 8750 | nick.cheng@JEF.com

Matt Ma \* | Equity Analyst

852 3767 1109 | matt.ma@JEF.com

Annie Ping, CFA, FRM \* | Equity Associate +852 3767 1273 | annie.ping@JEF.com

Table 2 - China PCB/CCL Earnings Summary

<table><tr><td rowspan="2">Company</td><td rowspan="2">Ticker</td><td rowspan="2">Mkt Cap (Rmb bn)</td><td colspan="4">Net Profit (Rmb m)</td><td colspan="2">Net Profit (YoY)</td></tr><tr><td>1Q25</td><td>2Q25</td><td>1Q26</td><td>2Q26</td><td>1Q26</td><td>2Q26</td></tr><tr><td colspan="9">Major PCB Maker</td></tr><tr><td>Founder</td><td>600601 CH</td><td>55</td><td>78</td><td>94</td><td>232</td><td>338</td><td>195%</td><td>260%</td></tr><tr><td>SYE</td><td>688183 CH</td><td>103</td><td>200</td><td>330</td><td>445</td><td>665</td><td>122%</td><td>101%</td></tr><tr><td>Fastprint</td><td>002436 CH</td><td>70</td><td>9</td><td>19</td><td>19</td><td></td><td>100%</td><td></td></tr><tr><td>Jove</td><td>300814 CH</td><td>31</td><td>10</td><td>7</td><td>19</td><td></td><td>89%</td><td></td></tr><tr><td>Shennan</td><td>002916 CH</td><td>290</td><td>491</td><td>869</td><td>850</td><td>1,350</td><td>73%</td><td>55%</td></tr><tr><td>Delton</td><td>001389 CH</td><td>83</td><td>240</td><td>251</td><td>393</td><td>522</td><td>63%</td><td>108%</td></tr><tr><td>WUS</td><td>002463 CH</td><td>249</td><td>762</td><td>920</td><td>1,242</td><td>1,673</td><td>63%</td><td>82%</td></tr><tr><td>Victory Giant</td><td>300476 CH</td><td>267</td><td>921</td><td>1,222</td><td>1,288</td><td></td><td>40%</td><td></td></tr><tr><td>Sunshine</td><td>300739 CH</td><td>11</td><td>12</td><td>29</td><td>15</td><td>25</td><td>22%</td><td>-14%</td></tr><tr><td>Redboard*</td><td>603459 CH</td><td>69</td><td>105</td><td>128</td><td>117</td><td>103</td><td>12%</td><td>-20%</td></tr><tr><td>Avary</td><td>002938 CH</td><td>228</td><td>488</td><td>745</td><td>463</td><td></td><td>-5%</td><td></td></tr><tr><td>CEE</td><td>002579 CH</td><td>11</td><td>7</td><td>12</td><td>6</td><td></td><td>-17%</td><td></td></tr><tr><td>Goworld</td><td>000823 CH</td><td>11</td><td>42</td><td>73</td><td>33</td><td></td><td>-21%</td><td></td></tr><tr><td>Kinwong</td><td>603228 CH</td><td>69</td><td>325</td><td>325</td><td>233</td><td></td><td>-28%</td><td></td></tr><tr><td>Kingshine</td><td>300903 CH</td><td>37</td><td>(33)</td><td>(29)</td><td>(52)</td><td></td><td>-56%</td><td></td></tr><tr><td>Ellington</td><td>603328 CH</td><td>11</td><td>116</td><td>144</td><td>38</td><td></td><td>-68%</td><td></td></tr><tr><td>Welgao</td><td>301251 CH</td><td>10</td><td>22</td><td>23</td><td>7</td><td></td><td>-70%</td><td></td></tr><tr><td>Suntak</td><td>002815 CH</td><td>22</td><td>115</td><td>106</td><td>32</td><td></td><td>-72%</td><td></td></tr><tr><td>Olympic</td><td>603920 CH</td><td>30</td><td>180</td><td>204</td><td>37</td><td>47</td><td>-80%</td><td>-77%</td></tr><tr><td>Aoshikang</td><td>002913 CH</td><td>17</td><td>112</td><td>84</td><td>17</td><td>72</td><td>-84%</td><td>-14%</td></tr><tr><td>Bomin</td><td>603936 CH</td><td>13</td><td>27</td><td>11</td><td>(11)</td><td>(38)</td><td>-140%</td><td>-461%</td></tr><tr><td>Dynamic</td><td>603175 CH</td><td>35</td><td>72</td><td>87</td><td>(96)</td><td></td><td>-234%</td><td></td></tr><tr><td colspan="9">Major CCL Maker</td></tr><tr><td>Goldenmax</td><td>002636 CH</td><td>70</td><td>23</td><td>47</td><td>202</td><td>573</td><td>764%</td><td>1116%</td></tr><tr><td>Nanya</td><td>688519 CH</td><td>78</td><td>21</td><td>66</td><td>150</td><td></td><td>611%</td><td></td></tr><tr><td>Baoding</td><td>002552 CH</td><td>23</td><td>18</td><td>4</td><td>66</td><td>69</td><td>268%</td><td>1618%</td></tr><tr><td>Sytech</td><td>600183 CH</td><td>363</td><td>564</td><td>863</td><td>1,158</td><td>2,040</td><td>105%</td><td>136%</td></tr><tr><td>Wazam</td><td>603186 CH</td><td>28</td><td>18</td><td>24</td><td>31</td><td>149</td><td>68%</td><td>514%</td></tr><tr><td colspan="9">Other PCB Maker</td></tr><tr><td>Printronics</td><td>002134 CH</td><td>7</td><td>1</td><td>6</td><td>12</td><td>32</td><td>2187%</td><td>422%</td></tr><tr><td>Edadoc</td><td>301366 CH</td><td>9</td><td>(7)</td><td>11</td><td>12</td><td></td><td>273%</td><td></td></tr><tr><td>DSBJ</td><td>002384 CH</td><td>444</td><td>456</td><td>302</td><td>1,110</td><td></td><td>143%</td><td></td></tr><tr><td>King Brother</td><td>301041 CH</td><td>3</td><td>(2)</td><td>6</td><td>(0)</td><td></td><td>93%</td><td></td></tr><tr><td>Allfavor</td><td>300964 CH</td><td>7</td><td>10</td><td>11</td><td>12</td><td>28</td><td>15%</td><td>152%</td></tr><tr><td>Sihui Fuji</td><td>300852 CH</td><td>9</td><td>29</td><td>47</td><td>29</td><td></td><td>3%</td><td></td></tr><tr><td>Aohong</td><td>605058 CH</td><td>4</td><td>37</td><td>44</td><td>33</td><td></td><td>-10%</td><td></td></tr><tr><td>Xunjiexing</td><td>688655 CH</td><td>5</td><td>(5)</td><td>2</td><td>(5)</td><td></td><td>-10%</td><td></td></tr><tr><td>Q&amp;D</td><td>301628 CH</td><td>7</td><td>26</td><td>32</td><td>23</td><td></td><td>-15%</td><td></td></tr><tr><td>Mankun</td><td>301132 CH</td><td>4</td><td>28</td><td>35</td><td>18</td><td></td><td>-36%</td><td></td></tr><tr><td>Camelot</td><td>301282 CH</td><td>6</td><td>16</td><td>37</td><td>9</td><td></td><td>-43%</td><td></td></tr><tr><td>Xiehe</td><td>605258 CH</td><td>2</td><td>12</td><td>17</td><td>5</td><td></td><td>-57%</td><td></td></tr><tr><td>Champion</td><td>603386 CH</td><td>5</td><td>15</td><td>23</td><td>(20)</td><td>11</td><td>-235%</td><td>-50%</td></tr></table>

Source: Company data, FactSet, JEF

We would like to thank Connie Yan, employee of Evalueserve Inc., for providing research support services to our preparation of this report.

## Company Valuation/Risks

For Important Disclosure information on companies recommended in this report, please visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action or call 212.284.2300.

## Analyst Certification:

I, Jacky He, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Edison Lee, CFA, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Nick Cheng, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Matt Ma, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Annie Ping, CFA, FRM, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

Registration of non-US analysts: Jacky He is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. Registration of non-US analysts: Edison Lee, CFA is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

Registration of non-US analysts: Nick Cheng is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. Registration of non-US analysts: Matt Ma is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. Registration of non-US analysts: Annie Ping, CFA, FRM is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

## Investment Recommendation Record

## (Article 3(1)e and Article 7 of MAR)

Recommendation Published July 13, 2026 11:56 A.M.
Recommendation Distributed July 13, 2026 11:56 A.M.

## Company Specific Disclosures

For Important Disclosure information on companies recommended in this report, please visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action or call 212.284.2300.

## Explanation of JEF Ratings

Buy - Describes securities that we expect to provide a total return (price appreciation plus yield) of 15% or more within a 12-month period. Hold - Describes securities that we expect to provide a total return (price appreciation plus yield) of plus 15% or minus 10% within a 12-month period.

Underperform - Describes securities that we expect to provide a total return (price appreciation plus yield) of minus 10% or less within a 12-month period. The expected total return (price appreciation plus yield) for Buy rated securities with an average security price consistently below \$10 is 20% or more within a 12-month period as these companies are typically more volatile than the overall stock market. For Hold rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is plus or minus 20% within a 12-month period. For Underperform rated securities with an average security price consistently below \$10, the expected total return (price appreciation plus yield) is minus 20% or less within a 12-month period.

NR - The investment rating and price target have been temporarily suspended. Such suspensions are in compliance with applicable regulations and/or JEF policies.

CS - Coverage Suspended. JEF has suspended coverage of this company.

NC - Not covered. JEF does not cover this company.

Restricted - Describes issuers where, in conjunction with JEF engagement in certain transactions, company policy or applicable securities regulations prohibit certain types of communications, including investment recommendations.

Monitor - Describes securities whose company fundamentals and financials are being monitored, and for which no financial projections or opinions on the investment merits of the company are provided.

## Valuation Methodology

JEF' methodology for assigning ratings may include

[中间内容因长度限制已省略]

lar investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
