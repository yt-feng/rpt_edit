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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# China: Q1 2026 BOP data show lower current account surplus

# Bottom line:

China's preliminary Balance of Payments (BOP) data showed a lower but still solid current account surplus and a narrower capital/financial account deficit in Q1 2026. The current account surplus decreased to $3.8\%$ of GDP in Q1 from $4.5\%$ in Q4 2025 (not seasonally adjusted), and FX reserves increased in Q1.

# Main points:

1. The preliminary BOP data show three main categories of China's international transactions—i.e., the current account (with breakdown into various sub-categories), the capital and financial account (including the net errors and omissions, with net FDI individually reported), and reserve assets flow. In Q1 2026, the current account surplus stood at US\$184bn, or 3.8% of GDP (NSA basis; vs. 4.5% of GDP in Q4 2025, Exhibit 2). The goods trade surplus declined on seasonal patterns and remained unchanged year-over-year, and the services trade deficit widened slightly. The income and transfer balance showed smaller outflows in Q1 vs Q4 2025. Altogether, the current account surplus narrowed in Q1 from Q4 2025 on a NSA basis (Exhibit 1). After seasonal adjustment, the current account surplus also narrowed in Q1 (3.9% of GDP) vs. Q4 2025 (4.3% of GDP).

2. The capital and financial account (including net error and omissions) showed slower net outflows. The outflows through net direct investment were US\$10bn in Q1, vs. US\$6bn inflows in Q4 2025 (Exhibit 3). SAFE FX net receipts related to portfolio investment declined from Q4 2025 to Q1 2026, implying that portfolio investment likely saw increased net outflows from Q4 2025 to Q1 2026. A detailed breakdown on portfolio and other investment flows will be released towards the end of June.

3. Reserve assets showed a US\$48bn increase (higher reserves) in Q1, in comparison with the US\$6bn increase in Q4 2025. By contrast, the headline FX reserves rose by US\$7bn in Q1 vs Q4 2025, suggesting around -US\$41bn valuation effect in FX reserves in Q1.

4. Looking forward, we recently revised up our 2026 forecasts for China's total goods export and import volume growth to $7.2\%$ and $6.8\%$ , respectively (up from our previous estimates of $5.3\%$ and $1.5\%$ ). Furthermore, we have raised our forecast for import and export price growth, primarily driven by higher energy prices. Taken together, China's goods trade surplus is likely to decrease slightly to $4.8\%$ of GDP in 2026 (vs. $5.4\%$ in 2025). Combining the narrower goods trade surplus and services trade deficit, we expect China's overall current account surplus to decrease modestly

Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

to $3.4\%$ of GDP in 2026 from $3.7\%$ in 2025. For capital and financial accounts, we expect the picture of inward and outward FDI to remain similar this year vs. last year, and portfolio investment outflow to be smaller this year compared to last year. Taken together, we project China's broad balance of payments (BBOP) to increase to $1.8\%$ of GDP in 2026 from $1.2\%$ in 2025, supporting our constructive view on the RMB (Exhibit 4).

# Yuting Yang

Exhibit 1: Capital outflows decelerated and reserves rose in Q1 2026 

<table><tr><td>Level (Bil USD)</td><td>2019 Q1</td><td>2020 Q1</td><td>2021 Q1</td><td>2022 Q1</td><td>2023Q1</td><td>2024Q1</td><td>2025Q1</td><td>2025Q2</td><td>2025Q3</td><td>2025Q4</td><td>2026Q1</td></tr><tr><td>Current Account Balance (a)</td><td>19</td><td>-57</td><td>66</td><td>84</td><td>71</td><td>58</td><td>164</td><td>125</td><td>202</td><td>244</td><td>184</td></tr><tr><td>as share of GDP (%)</td><td>0.6</td><td>-1.9</td><td>1.7</td><td>1.9</td><td>1.7</td><td>1.4</td><td>3.7</td><td>2.7</td><td>4.1</td><td>4.5</td><td>3.8</td></tr><tr><td>Trade in Goods Balance</td><td>63</td><td>12</td><td>119</td><td>137</td><td>128</td><td>132</td><td>247</td><td>227</td><td>276</td><td>310</td><td>247</td></tr><tr><td>Exports</td><td>532</td><td>476</td><td>704</td><td>810</td><td>759</td><td>780</td><td>855</td><td>900</td><td>969</td><td>1028</td><td>960</td></tr><tr><td>Imports</td><td>468</td><td>464</td><td>586</td><td>673</td><td>631</td><td>648</td><td>608</td><td>673</td><td>692</td><td>718</td><td>712</td></tr><tr><td>Trade in Services Balance</td><td>-62</td><td>-54</td><td>-36</td><td>-22</td><td>-47</td><td>-66</td><td>-72</td><td>-58</td><td>-60</td><td>-49</td><td>-60</td></tr><tr><td>Exports</td><td>56</td><td>49</td><td>62</td><td>81</td><td>77</td><td>83</td><td>88</td><td>90</td><td>98</td><td>108</td><td>101</td></tr><tr><td>Imports</td><td>118</td><td>103</td><td>98</td><td>103</td><td>124</td><td>148</td><td>160</td><td>148</td><td>158</td><td>157</td><td>161</td></tr><tr><td>Income and transfer balance</td><td>18</td><td>-14</td><td>-17</td><td>-31</td><td>-9</td><td>-8</td><td>-12</td><td>-43</td><td>-14</td><td>-18</td><td>-4</td></tr><tr><td>Capital and Financial Account Balance* (b)</td><td>-9</td><td>32</td><td>-32</td><td>-45</td><td>-49</td><td>-14</td><td>-195</td><td>-135</td><td>-214</td><td>-238</td><td>-136</td></tr><tr><td>Direct Investment</td><td>23</td><td>10</td><td>57</td><td>49</td><td>-32</td><td>-27</td><td>-35</td><td>-13</td><td>-36</td><td>6</td><td>-10</td></tr><tr><td>Portfolio Investment</td><td>19</td><td>-51</td><td>-13</td><td>-79</td><td>-52</td><td>-20</td><td>-61</td><td>-56</td><td>-191</td><td>-117</td><td>n.a.</td></tr><tr><td>Other Investment</td><td>-11</td><td>32</td><td>-91</td><td>-1</td><td>28</td><td>17</td><td>-89</td><td>-59</td><td>-33</td><td>-113</td><td>n.a.</td></tr><tr><td>Net errors and omissions</td><td>-41</td><td>45</td><td>11</td><td>-7</td><td>5</td><td>21</td><td>-3</td><td>2</td><td>48</td><td>-9</td><td>n.a.</td></tr><tr><td>Reserve Assets** (c=a+b)</td><td>10</td><td>-25</td><td>35</td><td>39</td><td>22</td><td>43</td><td>-31</td><td>-10</td><td>-12</td><td>6</td><td>48</td></tr></table>

\*Included net error and omissions   
\*\*Positive sign means increase in reserve assets   
Source: SAFE, GS Global Investment Research

Exhibit 2: Current account balance moderated in Q1   
![](images/7bb645361853c8a0e1f187057e12011b6f401892b847fc3b664edcd8ca4bf003.jpg)

<details>
<summary>line</summary>

| Year | Current account balance (Billion USD) | Current account balance as a percentage of GDP (RHS) (%) |
|---|---|---|
| 1998 | 10 | 3 |
| 2001 | 15 | 1 |
| 2004 | 30 | 4 |
| 2007 | 90 | 10 |
| 2010 | 130 | 6 |
| 2013 | 60 | 2 |
| 2016 | 70 | 3 |
| 2019 | -40 | -2 |
| 2022 | 140 | 3 |
| 2025 | 250 | 8 |
Percent axis on right, likely indicating growth or change in the metric.
</details>

Source: Haver Analytics

Exhibit 3: Outward FDI marginally outpaced inward FDI in Q1   
![](images/22d67deba84f1cc4629822cf1efd30f1776bbecf0f1b3bbc172a281e3803c5d5.jpg)

<details>
<summary>line</summary>

| Year | Outward (USD bn) | Inward (USD bn) | Net (USD bn) |
|------|------------------|-----------------|--------------|
| 2000 | ~0               | ~0              | ~0           |
| 2002 | ~0               | ~0              | ~0           |
| 2004 | ~0               | ~0              | ~0           |
| 2006 | ~0               | ~0              | ~0           |
| 2008 | ~0               | ~0              | ~0           |
| 2010 | ~0               | ~0              | ~0           |
| 2012 | ~0               | ~0              | ~0           |
| 2014 | ~0               | ~0              | ~0           |
| 2016 | ~0               | ~0              | ~0           |
| 2018 | ~0               | ~0              | ~0           |
| 2020 | ~0               | ~0              | ~0           |
| 2022 | ~0               | ~0              | ~0           |
| 2024 | ~0               | ~0              | ~0           |
</details>

Source: Haver Analytics, GS Global Investment Research

Exhibit 4: We expect the broad balance of payments (BBOP) to increase in 2026 

<table><tr><td>(USD bn)</td><td>2019</td><td>2020</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026F</td></tr><tr><td>CA balance</td><td>90</td><td>224</td><td>297</td><td>404</td><td>257</td><td>462</td><td>735</td><td>751</td></tr><tr><td>CA as % of GDP</td><td>0.6</td><td>1.5</td><td>1.6</td><td>2.2</td><td>1.4</td><td>2.4</td><td>3.7</td><td>3.4</td></tr><tr><td>Goods trade balance</td><td>371</td><td>500</td><td>537</td><td>651</td><td>600</td><td>809</td><td>1061</td><td>1056</td></tr><tr><td>Exports</td><td>2412</td><td>2539</td><td>3255</td><td>3397</td><td>3263</td><td>3523</td><td>3752</td><td>4126</td></tr><tr><td>Imports</td><td>2040</td><td>2039</td><td>2718</td><td>2746</td><td>2663</td><td>2714</td><td>2692</td><td>3070</td></tr><tr><td>Service trade balance</td><td>-252</td><td>-167</td><td>-131</td><td>-113</td><td>-221</td><td>-255</td><td>-238</td><td>-215</td></tr><tr><td>Exports</td><td>232</td><td>210</td><td>284</td><td>310</td><td>300</td><td>347</td><td>385</td><td>427</td></tr><tr><td>Imports</td><td>484</td><td>377</td><td>414</td><td>422</td><td>521</td><td>602</td><td>623</td><td>642</td></tr><tr><td>Primary/secondary income</td><td>-29</td><td>-110</td><td>-109</td><td>-134</td><td>-122</td><td>-92</td><td>-87</td><td>-89</td></tr><tr><td>Direct investment</td><td>50</td><td>99</td><td>165</td><td>-20</td><td>-174</td><td>-150</td><td>-77</td><td>-50</td></tr><tr><td>Inward</td><td>187</td><td>253</td><td>344</td><td>190</td><td>51</td><td>43</td><td>80</td><td>100</td></tr><tr><td>Outward</td><td>-137</td><td>-154</td><td>-179</td><td>-210</td><td>-226</td><td>-192</td><td>-157</td><td>-150</td></tr><tr><td>Portfolio investment</td><td>58</td><td>96</td><td>51</td><td>-289</td><td>-58</td><td>-179</td><td>-426</td><td>-310</td></tr><tr><td>Equity</td><td>16</td><td>-51</td><td>-2</td><td>-9</td><td>-44</td><td>-138</td><td>-172</td><td>-110</td></tr><tr><td>Bond</td><td>42</td><td>147</td><td>53</td><td>-280</td><td>-14</td><td>-42</td><td>-253</td><td>-200</td></tr><tr><td>BBoP</td><td>198</td><td>419</td><td>514</td><td>95</td><td>25</td><td>133</td><td>232</td><td>391</td></tr><tr><td>BBoP as % of GDP</td><td>1.4</td><td>2.8</td><td>2.8</td><td>0.5</td><td>0.1</td><td>0.7</td><td>1.2</td><td>1.8</td></tr></table>

Source: GS Global Investment Research, Haver Analytics

# The China Economics Team

# Andrew Tilton

+852-2978-1802

andrew.tilton@gs.com

GS (Asia) L.L.C.

# Hui Shan

+852-2978-6634

hui.shan@gs.com

GS (Asia) L.L.C.

# Lisheng Wang

+852-3966-4004

lisheng.wang@gs.com

GS (Asia) L.L.C.

# Xinquan Chen

+852-2978-2418

xinquan.chen@gs.com

GS (Asia) L.L.C.

# Yuting Yang

+852-2978-7283

yuting.y.yang@gs.com

GS (Asia) L.L.C.

# Chelsea Song

+852-2978-0106

chelsea.song@gs.com

GS (Asia) L.L.C.

# Disclosure Appendix

# Reg AC

I, Yuting Yang, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Yuting Yang GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

# Disclosures

# Regulatory disclosures

# Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

# Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst - SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. GS (India) Securities Private Limited compliance officer and investor grievance contact details can be found at: https://www.goldmansachs.com/worldwide/india/documents/Grievance-Redressal-and-Escalation-Matrix.pdf, and a copy of the annual audit compliance report can be found at this link: https://publishing.gs.com/content/site/india-annual-compliance-report.html. Japan: See below. Korea: This research, and any access to it, is intended only for “professional investors” within the meaning of the Financial Services and Capital Markets Act, unless otherwise agreed by GS. Further information on the subject company or companies referred to in this research may be obtained from GS (Asia) L.L.C., Seoul Branch. New Zealand: GS New Zealand Limited and its affiliates are neither “registered banks” nor “deposit takers” (as defined in the Reserve Bank of New Zealand Act 1989) in New Zealand. This research, and any access to it, is intended for “wholesale clients” (as defined in the Financial Advisers Act 2008) unless otherwise agreed by GS. A copy of certain GS Australia and New Zealand disclosure of interests is available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Russia: Research reports distributed in the Russian Federation are not advertising as defined in the Russian legislation, but are information and analysis not having product promotion as their main purpose and do not provide appraisal within the m

[中间内容因长度限制已省略]

e have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to sUBStantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

# © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
