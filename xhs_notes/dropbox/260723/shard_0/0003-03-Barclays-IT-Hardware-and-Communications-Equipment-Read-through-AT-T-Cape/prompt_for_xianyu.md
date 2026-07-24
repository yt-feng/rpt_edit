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
IT Hardware and Communications Equipment

# Read-through: AT&T Capex and iPhones

This morning AT&T reported Jun-Q (2Q26) earnings.

AT&T earnings have implications for stocks within our coverage universe, specifically service provider capex-exposed stocks (CIEN, CSCO, and GLW), as well as AAPL. For AT&T exposure, we estimate \~11% revenue for CIEN and LSD for overall GLW revenues (though we estimate roughly HSD of GLW's Optical revenues), and \~6% of iPhone units.

iPhones Unit Contribution from AT&T was roughly in-line with Street; 2Q26 capex came in above Street consensus: AT&T handset data points imply a unit contribution roughly meeting the Street expectations for AAPL iPhones with a tick down in the upgrade rate. 2Q26 capex came in at \$5.7Bn vs. the Street expectation of \$5.5Bn.

AT&T's handset and capex numbers:

\- AT&T (T; covered by Kannan Venkateshwar) reported smartphone unit sales of 5.2M in Jun-Q, flat Y/Y.

\- Upgrade rate moved down again to $3.2\%$ in the Q (from $3.5\%$ previous Q), down 10bps from a year ago and down 30bps sequentially, which we believe was largely due to faded enthusiasm around the carrier subsidies and the step-down in upgrade rate. We believe the telco reported upgrade rates are more important for this iPhone cycle as ASPs will likely increase by a decent amount.

Read-through for AAPL: We estimate AT&T sold roughly 3.4M iPhones in the quarter, flat Y/Y and down LSD sequentially. We think this implies in-line iPhones unit contribution for the quarter for AT&T, which we think is partially attributable to iPhone 17 line momentum, offset by a typically weaker Q2.

Capex read-through: 2Q26 capex came in above the Street at \$5.7B, though the company maintained the capital investment outlook to be in the range of \$23-24Bn annually for 2026, with the 2H capital investment being more back-end loaded. We view the reaffirmed full-year capex guide mostly neutral to our SP capex-exposed stocks in our coverage – CIEN, GLW, CSCO. Our sector continues to see a normalization in North America carrier activity. Similar to industry commentary, we expect telcos' ongoing fiber expansion to be lumpy for GLW, though we expect the recovery for SPs continuing in the back half. We continue to believe optical spend for capacity enhancements will be prioritized and expect CIEN's business with major US telcos to accelerate into next year.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

IT Hardware and Communications Equipment
NEUTRAL

Please see analyst certifications and important disclosures beginning on page 3. Completed: 22-Jul-26, 14:17 GMT Released: 22-Jul-26, 14:21 GMT Restricted - External

IT Hardware and Communications Equipment

Tim Long
+1 212 526 4043
tim.long@BARC.com
BCI, US

Alyssa Shreves
+1 212 526 7570
alyssa.shreves@BARC.com
BCI, US

Mary Lenox  
+1 212 526 6277  
mary.lenox@BARC.com  
BCI, US

Clarisse Yu  
+1 212 526 7025  
clarisse.yu@BARC.com  
BCI, US

## AT&T Handset-Related Metrics

FIGURE 1. Handset Metrics

<table><tr><td>AT&amp;T metrics</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>2Q26</td></tr><tr><td>Total smartphones</td><td>5.4</td><td>5.1</td><td>5.8</td><td>6.3</td><td>5.1</td><td>4.6</td><td>5.5</td><td>6.3</td><td>4.4</td><td>4.4</td><td>5.1</td><td>6.3</td><td>5.1</td><td>5.2</td><td>6.0</td><td>6.7</td><td>5.4</td><td>5.2</td></tr><tr><td>YoY change</td><td>5.9%</td><td>2.0%</td><td>3.6%</td><td>-4.5%</td><td>-5.6%</td><td>-9.8%</td><td>-5.2%</td><td>0.0%</td><td>-13.7%</td><td>-4.3%</td><td>-7.3%</td><td>0.0%</td><td>15.9%</td><td>18.2%</td><td>17.6%</td><td>6.3%</td><td>5.9%</td><td>0.0%</td></tr><tr><td>QoQ change</td><td>-18.2%</td><td>-5.6%</td><td>13.7%</td><td>8.6%</td><td>-19.0%</td><td>-9.8%</td><td>19.6%</td><td>14.5%</td><td>-30.2%</td><td>0.0%</td><td>15.9%</td><td>23.5%</td><td>-19.0%</td><td>2.0%</td><td>15.4%</td><td>11.7%</td><td>-19.4%</td><td>-3.7%</td></tr><tr><td>Postpaid subscribers</td><td>81.6</td><td>82.7</td><td>83.6</td><td>84.7</td><td>85.4</td><td>85.8</td><td>86.4</td><td>87.1</td><td>89.0</td><td>89.4</td><td>89.7</td><td>90.0</td><td>90.2</td><td>90.5</td><td>90.8</td><td>90.8</td><td>91.1</td><td>91.4</td></tr><tr><td>Smartphone % of subscribers</td><td>83.1%</td><td>83.0%</td><td>83.0%</td><td>82.9%</td><td>83.1%</td><td>83.7%</td><td>84.1%</td><td>84.3%</td><td>83.4%</td><td>83.9%</td><td>84.6%</td><td>85.2%</td><td>85.8%</td><td>86.4%</td><td>87.1%</td><td>87.9%</td><td>88.5%</td><td>89.0%</td></tr><tr><td>Smartphone subscribers</td><td>67.8</td><td>68.6</td><td>69.4</td><td>70.2</td><td>71.0</td><td>71.8</td><td>72.6</td><td>73.4</td><td>74.2</td><td>75.0</td><td>75.8</td><td>76.6</td><td>77.4</td><td>78.2</td><td>79.0</td><td>79.8</td><td>80.6</td><td>81.4</td></tr><tr><td>Upgrade rate</td><td>4.0%</td><td>3.6%</td><td>4.3%</td><td>4.8%</td><td>3.7%</td><td>3.1%</td><td>3.9%</td><td>4.7%</td><td>3.0%</td><td>2.9%</td><td>3.5%</td><td>4.6%</td><td>3.3%</td><td>3.3%</td><td>4.1%</td><td>4.7%</td><td>3.5%</td><td>3.2%</td></tr><tr><td>Upgrade units</td><td>3.3</td><td>2.9</td><td>3.6</td><td>4.0</td><td>3.1</td><td>2.6</td><td>3.3</td><td>4.1</td><td>2.6</td><td>2.6</td><td>3.1</td><td>4.1</td><td>3.0</td><td>3.0</td><td>3.7</td><td>4.3</td><td>3.2</td><td>2.9</td></tr><tr><td>iPhone units (estimates)</td><td>3.7</td><td>3.5</td><td>3.9</td><td>4.2</td><td>3.5</td><td>2.9</td><td>3.4</td><td>4.2</td><td>2.9</td><td>2.9</td><td>3.4</td><td>4.2</td><td>3.4</td><td>3.4</td><td>4.0</td><td>4.4</td><td>3.6</td><td>3.4</td></tr><tr><td>YoY change</td><td>20.0%</td><td>6.7%</td><td>5.1%</td><td>-7.3%</td><td>-5.3%</td><td>-15.1%</td><td>-13.5%</td><td>-1.5%</td><td>-16.5%</td><td>-1.4%</td><td>-1.3%</td><td>0.8%</td><td>15.9%</td><td>18.2%</td><td>17.6%</td><td>5.5%</td><td>5.9%</td><td>0.0%</td></tr><tr><td>QoQ change</td><td>-19.4%</td><td>-5.6%</td><td>13.7%</td><td>7.0%</td><td>-17.6%</td><td>-15.4%</td><td>15.8%</td><td>21.9%</td><td>-30.2%</td><td>0.0%</td><td>15.9%</td><td>24.5%</td><td>-19.7%</td><td>2.0%</td><td>15.4%</td><td>11.7%</td><td>-19.4%</td><td>-3.7%</td></tr></table>

Source: AT&T, BARC. Mn units.

## Analyst(s) Certification(s):

I, Tim Long, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC"). All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

Where any companies are the subject of this research report, for current important disclosures regarding those companies please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

The analysts responsible for preparing this research report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by investment banking activities, the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst.

Research analysts employed outside the US by affiliates of BARC Capital Inc. are not registered/qualified as research analysts with FINRA. Such non-US research analysts may not be associated persons of BARC Capital Inc., which is a FINRA member, and therefore may not be subject to FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst's account.

Analysts regularly conduct site visits to view the material operations of covered companies, but BARC policy prohibits them from accepting payment or reimbursement by any covered company of their travel expenses for such visits.

BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https:// publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Materially Mentioned Stocks (Ticker, Date, Price)

AT&T (T, 21-Jul-2026, USD 22.26), Equal Weight/Neutral, A/CD/CE/D/E/J/K/L/M/N

Apple, Inc. (AAPL, 21-Jul-2026, USD 327.74), Underweight/Neutral, CD/CE/D/E/J/K/L/M/N

Ciena Corporation (CIEN, 21-Jul-2026, USD 408.73), Overweight/Neutral, CD/CE/J

Cisco Systems, Inc. (CSCO, 21-Jul-2026, USD 112.18), Equal Weight/Neutral, CD/CE/D/J/K/L/M

Corning Incorporated (GLW, 21-Jul-2026, USD 162.41), Equal Weight/Neutral, CD/CE/J

Unless otherwise indicated, prices are sourced from Bloomberg and reflect the closing price in the relevant trading market, which may not be the last available closing price at the time of publication.

## Disclosure Legend:

A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of the issuer in the previous 12 months.

B: An employee or non-executive director of BARC PLC is a director of this issuer.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by this issuer.

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by this issuer.

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Conduct) in respect of this issuer.

D: BARC Bank PLC and/or an affiliate has received compensation for investment banking services from this issuer in the past 12 months.

E: BARC Bank PLC and/or an affiliate expects to receive or intends to seek compensation for investment banking services from this issuer within the next 3 months.

FA: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with US regulations.

FB: BARC Bank PLC and/or an affiliate beneficially owns a long position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FC: BARC Bank PLC and/or an affiliate beneficially owns a short position of more than 0.5% of a class of equity securities of this issuer, as calculated in accordance with EU regulations.

FD: BARC Bank PLC and/or an affiliate beneficially owns 1% or more of a class of equity securities of this issuer, as calculated in accordance with South Korean regulations.

FE: BARC Bank PLC and/or its group companies has financial interests in relation to this issuer and such interests aggregate to an amount equal to or more than $1\%$ of this issuer's market capitalization, as calculated in accordance with HK regulations.

GD: One of the Research Analysts on the fundamental credit coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

GE: One of the Research Analysts on the fundamental equity coverage team (and/or a member of his or her household) has a long position in the common equity securities of this issuer.

H: This issuer beneficially owns more than 5% of any class of common equity securities of BARC PLC.

I: BARC Bank PLC and/or an affiliate is party to an agreement with this issuer for the provision of financial services to BARC Bank PLC and/or an affiliate.

J: BARC Bank PLC and/or an affiliate is a liquidity provider and/or trades regularly in the securities of this issuer and/or in any related derivatives.

K: BARC Bank PLC and/or an affiliate has received non-investment banking related compensation (including compensation for brokerage services, if applicable) from this issuer within the past 12 months.

L: This issuer is, or during the past 12 months has been, an investment banking client of BARC Bank PLC and/or an affiliate.

M: This issuer is, or during the past 12 months has been, a non-investment banking client (securities related services) of BARC Bank PLC and/or an affiliate.

N: This issuer is, or during the past 12 months has been, a non-investment banking client (non-securities related services) of BARC Bank PLC and/or an affiliate.

O: Not in use.

P: Not in use.

Q: BARC Bank PLC and/or an affiliate is a Corporate Broker to this issuer.

R: Not in use.

S: This issuer is a Corporate Broker to BARC PLC.

T: BARC Bank PLC and/or an affiliate is providing investor engagement services to this issuer.

## Risk Disclosure(s)

Master limited partnerships (MLPs) are pass-through entities structured as publicly listed partnerships. For tax purposes, distributions to MLP unit holders may be treated as a return of principal. Investors should consult their own tax advisors before investing in MLP units.

## Disclosure(s) regarding Information Sources

Bloomberg® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibility for injury or damages arising in connection therewith.

## Guide to the BARC Fundamental Equity Research Rating System:

Our coverage analysts use a relative rating system in which they rate stocks as Overweight, Equal Weight or Underweight (see definitions below) relative to other companies covered by the analyst or a team of analysts that are deemed to be in the same industry (the "industry coverage universe").

In addition to the stock rating, we provide industry views which rate the outlook for the industry coverage universe as Positive, Neutral or Negative (see definitions below). A rating system using terms such as buy, hold and sell is not the equivalent of our rating system. Investors should carefully read the entire research report including the definitions of all ratings and not infer its contents from ratings alone.

## Stock Rating

Overweight - The stock is expected to outperform the unweighted expected total return of the industry coverage universe over a 12-month investment horizon.

Equal Weight - The stock is expected to perform in line with the unweighted expected total return of the industry coverage universe over a 12-month investment ho

[中间内容因长度限制已省略]

and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be

challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
