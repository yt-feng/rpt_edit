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
China

# Modest improvement with sectoral divergence

June PMI details and recent high-frequency indicators continue to point to a bifurcated growth pattern, with resilience in high-tech and export-oriented sectors contrasting with weakness in traditional industries and domestic demand. Construction activity stayed weak despite faster LGSB issuance.

• May NBS manufacturing PMI: 50.3

• Bloomberg consensus forecast (BARC): 50.1 (50.1)

• May NBS manufacturing PMI: 50.0

China's NBS manufacturing PMI rose to 50.3 in June from 50.0 in May, above both our forecast and consensus of 50.1. The production sub-index edged higher, while both new orders and new export orders improved and moved back into expansion territory. The pickup suggests a modest improvement in manufacturing activity in June, supported by resilient demand for high-tech products, lower energy prices, and a normalization in production following holiday-related disruptions in May. That said, the headline PMI remained only slightly above the 50 threshold, while underlying sector performance continued to diverge.

Sector performance remained uneven. The June PMI details continued to point to a bifurcated trend, with high-tech industries outperforming traditional sectors. High-tech manufacturing PMI rose to 53.5 from 52.9 in May, reaching its highest level in more than two years and remaining in expansion for a 17th consecutive month. Equipment manufacturing also strengthened to a three-year high of 52.5. Notably, both the production and new orders indices for sectors such as special equipment and computers, communications and electronic equipment remained above 54. In contrast, traditional industries remained weak. Oil-related sectors, including chemical fibers, and rubber and plastic products, stayed in contraction, while ferrous metals processing is facing headwinds from the prolonged property sector weakness. Consumer goods manufacturing improved but continued to lag the headline PMI, underscoring still-soft domestic demand.

Recent high-frequency indicators reinforce this picture of a two-speed economy, with resilience in high-tech and export-oriented sectors, but weakness in traditional industries and domestic demand (China: Domestic demand searches for a bottom, 24 June 2026). On the domestic demand side, major e-commerce platforms reported slower sales growth during the midyear shopping festival, while auto sales remained in a double-digit decline. Property market indicators also softened, with new home sales growth slowing further from May and secondary-market transactions easing slightly, albeit still recording low double-digit growth. In contrast,

Ying Zhang
+852 2903 2652
ying.zhang3@BARC.com
BARC Bank, Hong Kong

Yingke Zhou
+852 2903 2653
yingke.zhou@BARC.com
BARC Bank, Hong Kong

Jian Chang
+852 2903 2654
jian.chang@BARC.com
BARC Bank, Hong Kong

external demand remained resilient, with port cargo throughput expanding by an average of 5.2% y/y in June, up from 4.6% in May, suggesting continued strength in exports.

## Highlights of NBS manufacturing PMI breakdown

\- On prices, manufacturing prices weakened, with the input price index falling to 54.2 and the output price index slipping back into contractionary territory at 48.2 (from 60.5 and 51.9, respectively), both below their February survey readings which were collected before the Middle East conflict broke out on 27 February. The gap between the input and output price PMIs narrowed to 6.0pp in June after reaching a four-year high of 8.6pp in April-May, reflecting some relief from lower input costs. That said, the gap remained wider than the roughly 5pp average seen in January-February before the conflict, indicating that margin pressures have eased but have not fully returned to pre-conflicts levels.

\- Both supply and demand indicators improved in June relative to May. The production PMI edged up 0.2pp, to 51.4, while the new orders PMI returned to expansion territory at 51.2 from 49.9 in May. The improvement was accompanied by a rebound in the new export orders PMI, which rose to 50.1 in June after falling to 48.6 in May.

\- High-tech manufacturing remained the strongest-performing segment, with its PMI rising to 53.5 in June from 52.9 in May, the highest in more than two years and above 50 for a 17th straight month. Equipment manufacturing also strengthened, reaching a three-year high of 52.5. Consumer goods manufacturing returned to expansion territory, at 50.2 (May: 49.7), though it continued to lag the headline PMI, while manufacturing in energy-intensive sectors remained weak at 47.1.

FIGURE 1. NBS manufacturing PMI improved...  
![](images/3f21c8075d7eb1786e9e8be5bcf80d3ce298ec8618ac2735c9c74f55a5d81ffc.jpg)  
Source: Wind, BARC

FIGURE 2. ... with new (export) orders PMIs jumping back to expansionary territory  
![](images/ecec05ab1e4708d1a4324cbaf4fb100736f7a154988e61f59438d8bd2e38de68.jpg)  
Source: Wind, BARC

FIGURE 3. Manufacturing prices normalise gradually  
![](images/da5973aaa9fdad9d2fe85c99ad5eac192f6872ce1fc1197f8bf8c81827c620f1.jpg)  
Source: Wind, BARC

FIGURE 4. High-tech sectors continued to take the lead  
![](images/6d8dbcc4d63a12bcc7467c641fc38fd79754a6e157ac2530378d6c1ac79ef295.jpg)  
Source: Wind, BARC

FIGURE 5. Strong shipments of AI and green-tech product  
![](images/ad1f9e9045f7f058fb8490cf955a1f28bdf537216a1c46d2838b2e45cf4192e0.jpg)  
Data as of May
Source: Wind, BARC

FIGURE 6. Port cargo throughput stayed resilient in June  
![](images/f1864ae6043055bf3b261504e600dd58286933a6c7aaedc501b193dd914d5450.jpg)  
Source: Wind, BARC

## Non-manufacturing PMI edged up

The non-manufacturing PMI improved marginally to 50.2 in June from 50.1 in May, supported by modest gains in both services and construction activity. Within services, the PMI edged up to 50.4 from 50.3. Growth remained concentrated in technology- and finance-related sectors, including telecommunications, broadcasting, satellite transmission, software and IT services, monetary and financial services, and insurance, where activity indices stood above 55. By contrast, air transport and real estate services lag, with PMIs below the breakeven threshold, pointing to weaker demand in these sectors.

The construction PMI edged higher for a second month, rising to 49 in June from the post-COVID low in April. However, the new orders index remained weak although improving to 46.3 from 43.5, underscoring still-weak demand conditions. We note that the pace of local-government special bond issuance accelerated in June after March-May slowdown, with the single-month issuance amounting to 13% of the annual quota, versus a monthly average of 4% in April-May and 9% on average in Q1, although cumulative YTD issuance is still fell 2.1% than in H1 25.

The property sector is likely to remain a drag on construction activity. High-frequency data showed June new property sales growth weakened further from May and secondary transactions slowed slightly while maintaining low double-digit growth. Home prices in both the new and secondary markets continued to fall, while most housing indicators, notably property investment and new starts stayed deep in contraction.

FIGURE 7. Services PMI showed signs of recovery  
![](images/7db78d6f10a62df39f2028bb72f8e59d9ee01eac8b6837d1d34872ee66074120.jpg)  
Source: Wind, BARC

FIGURE 8. Construction PMI stayed in contraction despite faster LGSB issuance  
![](images/b0d0da5fcf04dbde5483b7d728297734a655becf790d6950009fad913fcc3e88.jpg)  
Source: Wind, BARC

FIGURE 9. NBS manufacturing and non-manufacturing PMIs

<table><tr><td></td><td>Weight</td><td>Jun-26</td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>Feb-26</td><td>Jan-26</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>Sep-25</td><td>Aug-25</td><td>Jul-25</td><td>Jun-25</td></tr><tr><td>NBS manufacturing PMI</td><td></td><td>50.3</td><td>50.0</td><td>50.3</td><td>50.4</td><td>49.0</td><td>49.3</td><td>50.1</td><td>49.2</td><td>49.0</td><td>49.8</td><td>49.4</td><td>49.3</td><td>49.7</td></tr><tr><td>New Orders</td><td>30%</td><td>51.2</td><td>49.9</td><td>50.6</td><td>51.6</td><td>48.6</td><td>49.2</td><td>50.8</td><td>49.2</td><td>48.8</td><td>49.7</td><td>49.5</td><td>49.4</td><td>50.2</td></tr><tr><td>Production</td><td>25%</td><td>51.4</td><td>51.2</td><td>51.5</td><td>51.4</td><td>49.6</td><td>50.6</td><td>51.7</td><td>50.0</td><td>49.7</td><td>51.9</td><td>50.8</td><td>50.5</td><td>51.0</td></tr><tr><td>Employment</td><td>20%</td><td>48.5</td><td>48.6</td><td>48.8</td><td>48.6</td><td>48.0</td><td>48.1</td><td>48.2</td><td>48.4</td><td>48.3</td><td>48.5</td><td>47.9</td><td>48.0</td><td>47.9</td></tr><tr><td>Supplier Deliveries</td><td>15%</td><td>49.9</td><td>49.2</td><td>49.5</td><td>49.5</td><td>49.1</td><td>50.1</td><td>50.2</td><td>50.1</td><td>50.0</td><td>50.8</td><td>50.5</td><td>50.3</td><td>50.2</td></tr><tr><td>Raw Material Inventory</td><td>10%</td><td>48.4</td><td>48.6</td><td>49.3</td><td>47.7</td><td>47.5</td><td>47.4</td><td>47.8</td><td>47.3</td><td>47.3</td><td>48.5</td><td>48.0</td><td>47.7</td><td>48.0</td></tr><tr><td>New Export Orders</td><td></td><td>50.1</td><td>48.6</td><td>50.3</td><td>49.1</td><td>45.0</td><td>47.8</td><td>49.0</td><td>47.6</td><td>45.9</td><td>47.8</td><td>47.2</td><td>47.1</td><td>47.7</td></tr><tr><td>Imports</td><td></td><td>49.6</td><td>48.8</td><td>50.1</td><td>49.8</td><td>45.6</td><td>47.3</td><td>47.0</td><td>47.0</td><td>46.8</td><td>48.1</td><td>48.0</td><td>47.8</td><td>47.8</td></tr><tr><td>Input Prices</td><td></td><td>54.2</td><td>60.5</td><td>63.7</td><td>63.9</td><td>54.8</td><td>56.1</td><td>53.1</td><td>53.6</td><td>52.5</td><td>53.2</td><td>53.3</td><td>51.5</td><td>48.4</td></tr><tr><td>Output Prices</td><td></td><td>48.2</td><td>51.9</td><td>55.1</td><td>55.4</td><td>50.6</td><td>50.6</td><td>48.9</td><td>48.2</td><td>47.5</td><td>48.2</td><td>49.1</td><td>48.3</td><td>46.2</td></tr><tr><td>Finished Goods Inventory</td><td></td><td>47.7</td><td>49.3</td><td>47.5</td><td>46.7</td><td>45.8</td><td>48.6</td><td>48.2</td><td>47.3</td><td>48.1</td><td>48.2</td><td>46.8</td><td>47.4</td><td>48.1</td></tr><tr><td>Large Enterprises</td><td></td><td>50.7</td><td>51.1</td><td>50.2</td><td>51.6</td><td>51.5</td><td>50.3</td><td>50.8</td><td>49.3</td><td>49.9</td><td>51.0</td><td>50.8</td><td>50.3</td><td>51.2</td></tr><tr><td>Medium Enterprises</td><td></td><td>50.5</td><td>48.6</td><td>50.5</td><td>49.0</td><td>47.5</td><td>48.7</td><td>49.8</td><td>48.9</td><td>48.7</td><td>48.8</td><td>48.9</td><td>49.5</td><td>48.6</td></tr><tr><td>Small Enterprises</td><td></td><td>48.2</td><td>48.5</td><td>50.1</td><td>49.3</td><td>44.8</td><td>47.4</td><td>48.6</td><td>49.1</td><td>47.1</td><td>48.2</td><td>46.6</td><td>46.4</td><td>47.3</td></tr><tr><td>RatingDog China manufacturing PMI</td><td></td><td></td><td>51.8</td><td>52.2</td><td>50.8</td><td>52.1</td><td>50.3</td><td>50.1</td><td>49.9</td><td>50.6</td><td>51.2</td><td>50.5</td><td>49.5</td><td>50.4</td></tr><tr><td>NBS services PMI</td><td></td><td>50.4</td><td>50.3</td><td>49.6</td><td>50.2</td><td>49.7</td><td>49.5</td><td>49.7</td><td>49.5</td><td>50.2</td><td>50.1</td><td>50.5</td><td>50.0</td><td>50.1</td></tr><tr><td>NBS construction PMI</td><td></td><td>49.0</td><td>48.8</td><td>48.0</td><td>49.3</td><td>48.2</td><td>48.8</td><td>52.8</td><td>49.6</td><td>49.1</td><td>49.3</td><td>49.1</td><td>50.6</td><td>52.8</td></tr><tr><td>NBS composite PMI</td><td></td><td>50.6</td><td>50.5</td><td>50.1</td><td>50.5</td><td>49.5</td><td>49.8</td><td>50.7</td><td>49.7</td><td>50.0</td><td>50.6</td><td>50.5</td><td>50.2</td><td>50.7</td></tr></table>

Source: Wind, BARC

## Analyst(s) Certification(s):

We, Yingke Zhou, Jian Chang and Ying Zhang, hereby certify (1) that the views expressed in this research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC").

All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

For current important disclosures regarding any issuers which are the subject of this research report please refer to https://

publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that BARC may have a conflict of interest that could affect the objectivity of this report. BARC Capital Inc. and/or one of its affiliates regularly trades, generally deals as principal and generally provides liquidity (as market maker or otherwise) in the debt securities that are the subject of this research report (and related derivatives thereof). BARC trading desks may have either a long and / or short position in such securities, other financial instruments and / or derivatives, which may pose a conflict with the interests of investing customers. Where permitted and subject to appropriate information barrier restrictions, BARC fixed income research analysts regularly interact with its trading desk personnel regarding current market conditions and prices. BARC fixed income research analysts receive compensation based on various factors including, but not limited to, the quality of their work, the overall performance of the firm (including the profitability of the Investment Banking Department), the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst. To the extent that any historical pricing information was obtained from BARC trading desks, the firm makes no representation that it is accurate or complete. All levels, prices and spreads are historical and do not necessarily represent current market levels, prices or spreads, some or all of which may have changed since the publication of this document. BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis, quantitative analysis, and trade ideas. Recommendations and trade ideas contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https://

publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

## Disclosure(s) regarding Information Sources

Bloomberg $^{\textregistered}$ is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”) and the Bloomberg Indices are trademarks of Bloomberg. Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Bloomberg does not approve or endorse this material, or guarantee the accuracy or completeness of any information herein, or make any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, Bloomberg shall have no liability or responsibi

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
