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
# China Software: May revenue growth slowed to $8.5\%$ YoY; Agentic AI and customized industry AI to drive client spending

![](images/80626497faa1eb0eed6598f019bb647f3a51490cf28dfe3e68426a856743ac8e.jpg)

China software industry growth in May was +8.5% YoY (vs. Apr 2026/ May 2025 at +8.9%/ 12.4% YoY), slower than previous months, leading to aggregate 5M26 revenue growth of +10.5% YoY (vs. 5M25 at 11.2% YoY). Looking into 3Q ahead, we expect to see sequential QoQ growth with better seasonality, while we see software spending remaining under pressure with allocation to AI foundational model and customized AI model projects. We see accelerated monetization and expanding use cases of AI agents, for example AI agents to retain experienced employees' know-how in-house, or diversify production sites with higher efficiency. For ToC, we see users leveraging multi-modal AI models to generate content, and adopt personal AI assistants on daily basis (e.g. search file, chat etc.).

We monitor AI product momentum, SMB PMI data, company hiring, profitability, and product iteration to track the path of software spending recovery in China. By segment, semi design, IT services, and cloud computing and big data outperformed in May, with IT services contributing the major revenues in the China software industry. The SMB PMI was down in Jun and has shown volatility recently.

Buy: AI: Sensetime, Meitu; Finance: Hundsun; IoT software: TUYA. Read more: China Software product tracker; Sensetime UG to Buy; Meitu initiation.

## May software industry growth slowed; Jun SMB PMI MoM declined

China software industry growth slowed to 8.5% YoY in May 2026 (vs. 8.9% in Apr 2026), and the SMB PMI was down to 48.2 in Jun (vs. 50.1/ 48.5 in Apr/ May). We expect to see improving QoQ in 2Q26E on better seasonality, while overall the clients' software spending remained weak, and some projects were on AI foundational models and customized AI models. We see rising adoption of AI features, and expect to see new progress in foundational AI models for text/ image/video content generation to drive the application ecosystem and drive clients' IT spending.

## China software sector key indicators:

GS does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision. For Reg AC certification and other important disclosures, see the Disclosure Appendix, or go to www.gs.com/research/hedge.html. Analysts employed by non-US affiliates are not registered/qualified as research analysts with FINRA in the U.S.

Allen Chang  
+852-2978-2930 |  
allen.k.chang@gs.com  
GS (Asia) L.L.C.

Verena Jeng  
+852-2978-1681 | verena.jeng@gs.com  
GS (Asia) L.L.C.

Ting Song
+852-2978-6466 | ting.song@gs.com
GS (Asia) L.L.C.

Simon Cheung, CFA +852-2978-6102 | simon.cheung@gs.com GS (Asia) L.L.C.

Timothy Zhao  
+852-2978-2673 | timothy.zhao@gs.com GS (Asia) L.L.C.

Shuo Yang, Ph.D. +852-2978-0701 | shuo.yang@gs.com GS (Asia) L.L.C.

China SMB PMI: The PMI data reflects economic momentum and is correlated with the software market and customer budgets. In Jun 2026, SMB PMI decreased to 48.2 from 48.5 in May (Exhibit 3).

Margin stable in May 2026: We saw China software industry net margin at $11.9\%$ in May vs. net margin at $12.0\%$ in Apr, per MIIT, showing improving operational efficiency.

Exhibit 1: China software industry growth was at $10\%$ YoY in 5M26  
5M26 China Software industry revenue growth by segment  
![](images/35849bbb936fec89cd1e8eb588b1d6ae7961411e0bacd37359049b340a69a296.jpg)  
\*software products include industrial software; \*\*IT services include E-commerce IT services, semis design software, cloud computing and big data.  
Source: MIIT

Exhibit 2: Software industry growth slowed in May 2026; SMB PMI was weak in Jun 2026  
![](images/77a1b51bb1056e65f4f898a74d38b9af07168ed4932382b9038d5701113acae7.jpg)  
Source: MIIT, NBS

## Software Monthly: May revenues down to $+8.5\%$ YoY with MoM increase

## May 2026 China software quick read:

1. Revenue +8.5% YoY, leading to 5M26 at 10.3% YoY, slower than 4M26 growth of 10.9% YoY: In May, the aggregate revenue of software companies registered in China was up +8.5% YoY to Rmb1.6trn (US\$219bn), resulting in 5M26 revenue growth of +10.3% YoY, while going down from 4M26 of 11.3% YoY, per MIIT.

2. Net margin was 11.9%, leading to 5M26 at 11.5%, higher vs. 4M26 of 11.4%: In May, the aggregate net income of software companies registered in China was Rmb186.9bn (US\$26.0bn), or net margin of 11.9% (vs. 12.0% in Apr 2026), resulting in 5M26 net margin of 11.5%, higher than 4M26 net margin of 11.4%, per MIIT.

3. Overseas exposure up to 3.2%: In May, the aggregate revenue for non-China markets from software companies registered in China was US\$7.0bn, and overseas exposure rose to 3.2% (vs. 3.1% in Apr 2026).

4. IT services remain a key contributor: In 5M26, the aggregate revenue of software companies registered in China (Rmb6.2trn) was mainly generated from IT services (68% of the total), followed by software products at 22%, embedded system software at 8%, and security software and services at 2%, per MIIT.

Exhibit 3: China software market snapshot

<table><tr><td></td><td>Apr-25</td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-Feb 26</td><td>Mar-26</td><td>Apr-26</td><td>May-26</td></tr><tr><td colspan="14">China software market</td></tr><tr><td>Total revenues (Rmb m)*</td><td>1,080,566</td><td>1,452,355</td><td>1,397,917</td><td>1,266,200</td><td>1,316,100</td><td>1,471,800</td><td>1,397,700</td><td>1,467,300</td><td>1,505,500</td><td>2,153,500</td><td>1,338,500</td><td>1,176,600</td><td>1,576,400</td></tr><tr><td>Software products</td><td>239,396</td><td>304,076</td><td>271,135</td><td>257,000</td><td>310,200</td><td>274,100</td><td>265,000</td><td>300,500</td><td>285,200</td><td>472,700</td><td>318,800</td><td>254,900</td><td>314,400</td></tr><tr><td>IT services</td><td>723,960</td><td>1,044,459</td><td>994,241</td><td>888,400</td><td>867,000</td><td>1,051,700</td><td>962,000</td><td>1,005,100</td><td>1,026,200</td><td>1,447,400</td><td>895,700</td><td>790,100</td><td>1,142,900</td></tr><tr><td>Security software</td><td>19,726</td><td>22,353</td><td>1,726</td><td>12,900</td><td>20,000</td><td>24,600</td><td>18,300</td><td>19,100</td><td>23,400</td><td>41,200</td><td>24,800</td><td>20,800</td><td>23,400</td></tr><tr><td>Embedded system software</td><td>97,484</td><td>81,467</td><td>130,815</td><td>107,900</td><td>118,900</td><td>121,400</td><td>152,400</td><td>142,600</td><td>170,700</td><td>192,200</td><td>99,200</td><td>110,800</td><td>95,700</td></tr><tr><td>MoM</td><td>-10%</td><td>34%</td><td>-4%</td><td>-9%</td><td>4%</td><td>12%</td><td>-5%</td><td>5%</td><td>3%</td><td></td><td></td><td>-12%</td><td>34%</td></tr><tr><td>Software products</td><td>-18%</td><td>27%</td><td>-11%</td><td>-5%</td><td>21%</td><td>-12%</td><td>-3%</td><td>13%</td><td>-5%</td><td></td><td></td><td>-20%</td><td>23%</td></tr><tr><td>IT services</td><td>-9%</td><td>44%</td><td>-5%</td><td>-11%</td><td>-2%</td><td>21%</td><td>-9%</td><td>4%</td><td>2%</td><td></td><td></td><td>-12%</td><td>45%</td></tr><tr><td>Security software</td><td>-13%</td><td>13%</td><td>-92%</td><td>647%</td><td>55%</td><td>23%</td><td>-26%</td><td>4%</td><td>23%</td><td></td><td></td><td>-16%</td><td>13%</td></tr><tr><td>Embedded system software</td><td>6%</td><td>-16%</td><td>61%</td><td>-18%</td><td>10%</td><td>2%</td><td>26%</td><td>-6%</td><td>20%</td><td></td><td></td><td>12%</td><td>-14%</td></tr><tr><td>YoY</td><td>11%</td><td>12%</td><td>15%</td><td>14%</td><td>15%</td><td>15%</td><td>15%</td><td>15%</td><td>12%</td><td>12%</td><td>12%</td><td>9%</td><td>9%</td></tr><tr><td>Software products</td><td>10%</td><td>10%</td><td>15%</td><td>11%</td><td>16%</td><td>8%</td><td>14%</td><td>13%</td><td>1%</td><td>8%</td><td>10%</td><td>6%</td><td>3%</td></tr><tr><td>IT services</td><td>13%</td><td>13%</td><td>17%</td><td>16%</td><td>16%</td><td>18%</td><td>15%</td><td>16%</td><td>16%</td><td>13%</td><td>13%</td><td>9%</td><td>9%</td></tr><tr><td>Security software</td><td>8%</td><td>8%</td><td>-3%</td><td>-8%</td><td>11%</td><td>7%</td><td>3%</td><td>11%</td><td>5%</td><td>6%</td><td>10%</td><td>5%</td><td>5%</td></tr><tr><td>Embedded system software</td><td>5%</td><td>9%</td><td>7%</td><td>9%</td><td>10%</td><td>9%</td><td>16%</td><td>6%</td><td>9%</td><td>12%</td><td>8%</td><td>14%</td><td>17%</td></tr><tr><td>Mix</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td><td>100%</td></tr><tr><td>Software products</td><td>22%</td><td>21%</td><td>19%</td><td>20%</td><td>24%</td><td>19%</td><td>19%</td><td>20%</td><td>19%</td><td>22%</td><td>24%</td><td>22%</td><td>20%</td></tr><tr><td>IT services</td><td>67%</td><td>72%</td><td>71%</td><td>70%</td><td>66%</td><td>71%</td><td>69%</td><td>68%</td><td>68%</td><td>67%</td><td>67%</td><td>67%</td><td>73%</td></tr><tr><td>Security software</td><td>2%</td><td>2%</td><td>0%</td><td>1%</td><td>2%</td><td>2%</td><td>1%</td><td>1%</td><td>2%</td><td>2%</td><td>2%</td><td>2%</td><td>1%</td></tr><tr><td>Embedded system software</td><td>9%</td><td>6%</td><td>9%</td><td>9%</td><td>9%</td><td>8%</td><td>11%</td><td>10%</td><td>11%</td><td>9%</td><td>7%</td><td>9%</td><td>6%</td></tr><tr><td>Total net income (Rmb m)*</td><td>133,438</td><td>182,877</td><td>156,241</td><td>230,900</td><td>229,600</td><td>116,600</td><td>136,900</td><td>123,300</td><td>189,400</td><td>269,300</td><td>120,100</td><td>141,000</td><td>186,900</td></tr><tr><td>MoM</td><td>-1%</td><td>37%</td><td>-15%</td><td>48%</td><td>-1%</td><td>-49%</td><td>17%</td><td>-10%</td><td>54%</td><td></td><td></td><td></td><td></td></tr><tr><td>YoY</td><td>22%</td><td>9%</td><td>9%</td><td>14%</td><td>16%</td><td>-24%</td><td>-2%</td><td>-6%</td><td>14%</td><td>7%</td><td>-11%</td><td>6%</td><td>2%</td></tr><tr><td>Net margin</td><td>12.3%</td><td>12.6%</td><td>11.2%</td><td>18.2%</td><td>17.4%</td><td>7.9%</td><td>9.8%</td><td>8.4%</td><td>12.6%</td><td>12.5%</td><td>9.0%</td><td>12.0%</td><td>11.9%</td></tr><tr><td>Total revenues (Rmb m)</td><td>1,080,566</td><td>1,452,355</td><td>1,397,917</td><td>1,266,200</td><td>1,316,100</td><td>1,471,800</td><td>1,397,700</td><td>1,467,300</td><td>1,505,500</td><td>2,153,50O</td><td>1,338,500</td><td>1,176,600</td><td>1,576,400</td></tr><tr><td>From China market</td><td>1,048,653</td><td>1,407,441</td><td>1,370,646</td><td>1,225,304</td><td>1,269,588</td><td>1,432,200</td><td>1,360,620</td><td>1,425,540</td><td>1,463,452</td><td>2,078,764</td><td>1,300,916</td><td>1,140,240</td><td>1,526,000</td></tr><tr><td>From non-China markets</td><td>31,912</td><td>44,914</td><td>27,271</td><td>40,896</td><td>46,512</td><td>39,600</td><td>37,080</td><td>41,760</td><td>42,048</td><td>74,736</td><td>37,584</td><td>36,360</td><td>50,400</td></tr><tr><td>Export ratio</td><td>3%</td><td>3%</td><td>2%</td><td>3%</td><td>4%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td><td>3%</td></tr></table>

\*Aggregate revenue/net income for software companies registered in China. IT services growth was mainly driven by cloud computing and big data segment.  
Source: MIIT

## Exhibit 4: China software market continued to grow in May 2026

Software companies registered in China: aggregate revenues and YoY

![](images/5647f2acffece9026087655dc96597a3cf8e7eb815c7f6daf40aa60d3f01ae42.jpg)  
Source: MIIT

Exhibit 5: China security software revenues growth was at $5\%$ YoY in May (vs. $5\%$ YoY in Apr 2026) Security software companies registered in China: aggregate revenues and YoY growth

![](images/054d792ded15cf987691a6938c6d045e7570977751434fd39986836ee4da95bd.jpg)  
Source: MIIT

Exhibit 6: Net margin at $11.9\%$ in May (vs. $12.0\%$ in Apr 2026), leading to 5M26 NM at $11.5\%$

Software companies registered in China: aggregate NI YoY growth and net margin

![](images/3ba89ca52df459c999f8d75760dc618f19caffb450e2d2be4957e1aa06d9da02.jpg)  
Source: MIIT  
Exhibit 7: IT services remain the key contributor
Software companies registered in China: aggregate revenues by subsector in 5M26

![](images/a64ca1f9b4480b9f5ebe887cfb20fab26ace3bfbd2e67eceee5b71be67bd6c25.jpg)  
Source: MIIT

China security software / IT services market +5%/ +9% YoY in May 2026

China security software market revenue growth slowed in May: In May, the aggregate revenue of security software companies registered in China was up 5% YoY to Rmb23.4bn (US\$3.3bn), and 5M26 revenue came to Rmb110bn (US\$15.3bn).

China IT services market revenue +9% YoY in May: In May, the aggregate revenue of IT services companies registered in China was up 9% YoY to Rmb1.1trn (US\$159bn), and 5M26 revenue came to Rmb4.3tn (US\$594bn), per MIIT.

■ Service outsourcing contract value increased in May 2026: In May, the aggregate contract value of service outsourcing was up (YoY) to Rmb121bn, and 5M26 contract value came to Rmb824bn, per Ministry of Commerce. The aggregate value of service outsourcing (execution) was up 14% YoY to Rmb74bn in May 2026, driven by rising AI-related projects.

## Disclosure Appendix

## Reg AC

We, Allen Chang, Verena Jeng, Ting Song, Simon Cheung, CFA, Timothy Zhao and Shuo Yang, Ph.D., hereby certify that all of the views expressed in this report accurately reflect our personal views about the subject company or companies and its or their securities. We also certify that no part of our compensation was, is or will be, directly or indirectly, related to the specific recommendations or views expressed in this report.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Allen Chang GS (Asia) L.L.C., Verena Jeng GS (Asia) L.L.C., Ting Song GS (Asia) L.L.C., Simon Cheung, CFA GS (Asia) L.L.C., Timothy Zhao GS (Asia) L.L.C., Shuo Yang, Ph.D. GS (Asia) L.L.C..

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## GS Factor Profile

The GS Factor Profile provides investment context for a stock by comparing key attributes to the market (i.e. our universe of rated stocks) and its sector peers. The four key attributes depicted are: Growth, Financial Returns, Multiple (e.g. valuation) and Integrated (a composite of Growth, Financial Returns and Multiple). Growth, Financial Returns and Multiple are calculated by using normalized ranks for specific metrics for each stock. The normalized ranks for the metrics are then averaged and converted into percentiles for the relevant attribute. The precise calculation of each metric may vary depending on the fiscal year, industry and region, but the standard approach is as follows:

Growth is based on a stock's forward-looking sales growth, EBITDA growth and EPS growth (for financial stocks, only EPS and sales growth), with a higher percentile indicating a higher growth company. Financial Returns is based on a stock's forward-looking ROE, ROCE and CROCI (for financial stocks, only ROE), with a higher percentile indicating a company with higher financial returns. Multiple is based on a stock's forward-looking P/E, P/B, price/dividend (P/D), EV/EBITDA, EV/FCF and EV/Debt Adjusted Cash Flow (DACF) (for financial stocks, only P/E, P/B and P/D), with a higher percentile indicating a stock trading at a higher multiple. 

[中间内容因长度限制已省略]

 including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
