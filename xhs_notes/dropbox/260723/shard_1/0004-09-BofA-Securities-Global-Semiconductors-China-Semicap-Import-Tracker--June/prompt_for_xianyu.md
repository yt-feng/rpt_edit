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
# Global Semiconductors

# China Semicap Import Tracker - June 2026 down 1% yoy

Industry Overview

## June '26 Semicap imports – down 1% yoy/up 45% mom

We analyze monthly China customs import data relating to semiconductor equipment. The data is relevant for tracking China sales for global semicap players. China accounted for 33.5% of global WFE in 2025, making it one of the most important regions for global semicaps. China's semiconductor equipment imports were \$4.7bn in June 2026, above the previous 3mth (Mar'26-May'26) average of \$3.9bn and above the previous 12mth (Jun'25-May'26) average of \$4.4bn. Import value was down 1% yoy and up 45% mom. On a 3MMA, import value was down 3% yoy and up 1% mom, below the historical 3MMA mom average for the month of +5%. June brings the YTD decline to -9% for 2026, a year in which most semicap suppliers expect China sales to normalize.

## Front-end – up 1% yoy and up 57% mom

China imported \$3.4bn worth of front-end equipment in June. Front-end imports were up 1% yoy and up 57% mom, driven primarily by Heat treatment (\$188mm; +78% yoy/+42% mom), Other Front-end (\$488mm; +48% yoy/+104% mom), Process control (\$444mm; +24% yoy/+41% mom) and Lithography (\$842mm; +3% yoy/+184% mom), while other segments were down: Etching (\$505mm; -24% yoy/+32% mom), Ion implanters (\$115mm; -13% yoy/+8% mom), and Deposition (\$831 mm; -12% yoy/+17% mom).

YTD, front-end imports of \$15.5bn are down 10% yoy, driven by Lithography (\$3.0bn; -18% yoy), Etching (\$2.9bn; -19% yoy), Other Front-end (\$2.2bn; -9% yoy), Process control (\$1.8bn; -8% yoy), and Ion implanters (\$677mm; -4% yoy), while Heat treatment (\$863mm; +13% yoy) and Deposition (\$4.1bn; flat yoy) are flat/up.

## Back-end categories in June

\- Assembly & Packaging: \$415mm, down 6% yoy and up 21% mom. Within A&P, wire bonder imports were up 153% yoy and up 33% mom while mounting and bonding was down 9% yoy and up 19% mom. YTD, A&P was down 14% yoy to \$1.9bn.

\- Wafer manufacturing: \$98mm, down 22% yoy and up 44% mom. YTD, imports were down 25% yoy to \$563mm.

\- Flat panel display: \$208mm, down 5% yoy and down 6% mom. YTD, imports were up 14% yoy to \$1.3bn.

\- Spares: \$480mm, down 1% yoy and up 29% mom. YTD, down 5% yoy to \$2.5bn.

\- Testing: \$46mm, down 7% yoy and up 29% mom. YTD, down 12% yoy to \$214mm.

This research report provides general information only. No part of this report may be used or reproduced or quoted in any manner whatsoever in Taiwan by the press or other persons without the express written consent of BofA.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

## 21 July 2026

Equity
Global
Semiconductors

Research Analyst
MLI (UK)
+44 20 7995 6751
didier.scemama@bofa.com

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Simon Woo, CFA >> Research Analyst BofA (Seoul) simon.woo@bofa.com

Mikio Hirakawa >>
Research Analyst
BofAS Japan
mikio.hirakawa@bofa.com

Haas Liu >>
Research Analyst
BofA (Taiwan)
haas.liu@bofa.com

Dai Shen >>
Research Analyst
BofA (Hong Kong)
dai.shen@bofa.com

Daley Li, CFA >>
Research Analyst
BofA (Hong Kong)
daley.li2@bofa.com

Oliver Wong >>
Research Analyst
MLI (UK)
oliver.wong2@bofa.com

Amelia Banks >>
Research Analyst
MLI (UK)
amelia.banks@bofa.com

## 3MMA: 3 month moving average

WFE: Wafer fabrication equipment

## Contents

China semiconductor equipment imports – major categories at a glance (\$mm) 3
China semiconductor equipment imports – major categories at a glance (yoy %) 4
China semiconductor equipment imports – category breakdown 5
China semiconductor equipment imports – major categories in June 6
China semiconductor equipment imports – further analysis 8
Front-end equipment import total compared to semi equipment suppliers’ disclosed China equipment sales 10
Lithography imports – up 3% in June 2026 11
Netherlands lithography machine imports 14
Deposition imports – down 12% in June 2026 17
Etching imports – down 24% in June 2026 20
Heat treatment imports – up 78% in June 2026 23
Ion implanters imports – down 13% in June 2026 25
Process Control imports – up 24% in June 2026 27
Wafer manufacturing equipment – down 22% in June 2026 29
Flat panel display manufacturing equipment – down 5% in June 2026 30
Assembly and packaging equipment – down 6% in June 2026 31
Spares – down 1% in June 2026 32
Wire bonders – up 153% in June 2026 33
Mounting and bonding – down 9% in June 2026 34
Testing equipment – down 7% in June 2026 35
Appendix: China semiconductor equipment imports – summary tables 36

# China semiconductor equipment imports - major categories at a glance (\$mm)

Exhibit 1: Up 184% mom to \$842mm in June 2026
Lithography monthly and 3MMA import value  
![](images/b6694b1945d0dd0a030420f518eddc8673c60333c9b7a174d58a2d5aada197bc.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 2: Up 17% mom to \$831mm in June 2026
Deposition monthly and 3MMA import value  
![](images/bc51ce1d09933d31712eac9bdd529dfab3ef314861cc1ca260a77ae6a450881b.jpg)  
Source: China General Customs

Exhibit 3: Up 32% mom to \$505mm in June 2026
Etching monthly and 3MMA import value  
![](images/2be4020d12388bce4f9efb31d3e8a0cca3f49487e455e1837f094c7dc2626c2b.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH

Exhibit 4: Up 41% mom to \$444mm in June 2026
Process Control monthly and 3MMA import value  
![](images/3b975bfd11798e1583ee8d05a8265dc0ab64fefe0b7361d474b7ec6092cefac6.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 5: Up 21% mom to \$415mm in June 2026
Assembly & Packaging monthly and 3MMA import value  
![](images/d29401f05a9037ee41f80852fa0c70ce84da0f61c6f28e31fa46fbf9fa0e7efc.jpg)  
Source: China General Customs

Exhibit 6: Up 29% mom to \$46mm in June 2026
Testing equipment monthly and 3MMA import value  
![](images/6d82e1856ab1a53fbb591d3d03c08437b5b9d9ca0eadd0b152efce8e2bc24835.jpg)  
Source: China General Customs

# China semiconductor equipment imports – major categories at a glance (yoy %)

Exhibit 7: Up 3% yoy and down 8% yoy on a 3MMA in June 2026
Lithography monthly and 3MMA import value yoy %  
![](images/6eec9249fab2677b87e3b240d5324070447be8bc82b6cabff6346a3d0459a9bb.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 8: Down 12% yoy and up 9% yoy on a 3MMA in June 2026
Deposition monthly and 3MMA import value yoy %  
![](images/f91a514d419769a3b8e0b8f05afd91cfb205ce3da295fd919f7488be53e13eb6.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 9: Down 24% yoy and down 28% yoy on a 3MMA in June 2026
Etching monthly and 3MMA import value yoy %  
![](images/4681924697b0edfa43fee7cf21467c86887902e65a2296bb0c6f661c518c15bc.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 10: Up 24% yoy and up 22% yoy on a 3MMA in June 2026
Process Control monthly and 3MMA import value yoy %  
![](images/130dfd84d491d0bb461379d3a6f3486af4f5c46d2b53ed4086c79e577b6ec346.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 11: Down 6% yoy and down 12% yoy on a 3MMA in June 2026
Assembly & Pkg monthly and 3MMA import value yoy %  
![](images/a27fcbcedafab3cf939a9680ef4b1487dd11322866457ba443f3ccf4efc70088.jpg)  
Source: China General Customs

Exhibit 12: Down 7% yoy and up 24% yoy on a 3MMA in June 2026
Testing equipment monthly and 3MMA import value yoy %  
![](images/080a339f846f072b7f73c51988f85b0b9f138c75d98c55654606022940fc8996.jpg)  
Source: China General Customs

## China semiconductor equipment imports – category breakdown

Exhibit 13: China semi equipment imports totalled \$52.1bn in 2024
China semi equipment import value breakdown in 2024

![](images/6bc71fe92f51cba5d473df8ee5d837b326eeee788c269231c127ae538d73d0c8.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
Exhibit 14: China semi equipment imports totalled \$4.7bn in June 2026
China semi equipment import value breakdown in June 2026

![](images/07264d4728bb46ee4dca34fc9faaf9374ac14ef1ae290466f67f89f87fae611c.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
Exhibit 15: China semi equipment imports totalled \$55.3bn in 2025
China semi equipment import value breakdown in 2025

![](images/04ab258a6c644798abba798ae1c96b5c11a620450e2a6a2d0ce24869f14232f2.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

## China semiconductor equipment imports – major categories in June

Exhibit 16: On a yoy %, Wire bonders outperformed at 153% China semi equipment import value yoy % in June 2026

![](images/6c4de1798a69b87e8be8560653ff6b671ea28b823122ec38c5464aaa8472bc7c.jpg)  
Source: China General Customs  
Exhibit 17: On a mom %, Lithography outperformed at 184% China semi equipment import value mom % in June 2026

![](images/34bdae85eef339937408f4acea4fb62f7b70d429d4666d13e4626540012fd50d.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
BofA GLOBAL RESEARCH  
Exhibit 18: On a 3MMA yoy %, Wire bonders outperformed at 65% China semi equip import value yoy % in June 2026 (3MMA)

![](images/13c825f08f45a4a4c64c3dd58fbc4ca11f3698ba4531fb10badf09d81192756a.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
Exhibit 19: On a 3MMA mom %, Wire bonders outperformed at 30% China semi equip import value mom % in June 2026 (3MMA)

![](images/9d5c2553f27fea12cf5a49d07fc79d84b14c493ff7af7529f83151fee63f690f.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 20: For YTD 2026, Wire bonders had the highest yoy % China semi equip import value yoy % for YTD 2026  
![](images/9711589d0d11b13221fc0c941f9d6bb7db48255b40c635e9b85084deeaf4ad05.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

## China semiconductor equipment imports – further analysis

Exhibit 21: Down 1% yoy and up 45% mom in June 2026
China semi equipment monthly import value  
![](images/d48efff003f94ec315dfa028e6239a76ab4fb74ff5c07b05a0c950abb56ba382.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 22: Down 3% yoy and up 1% mom in June 2026 on a 3MMA China semi equipment monthly import value (3MMA)  
![](images/f4cfb0e87be685dc0cab71f29acdd12de55b7fc70d9147e11062e89e84763087.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 23: Down 3% yoy and up 13% qoq in 2Q26
China semi equipment quarterly import value  
![](images/78611d24a8359c829b92bc8e56cc54716179906ab6e15f50306ba04a634df765.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 24: Import value was \$55.3bn in 2025, up 6% yoy China semi equipment annual import value  
![](images/1d8d0f81e1389471b3f3248c5466a0ba10d8d28f64bc44934d6b1eda3572a138.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
China semi equipment import value through and after June

Exhibit 25: Import value in 2026 through June outpaced prior years; at \$14.2bn

![](images/197339f5581e8661701c2b7d4dbe90069e839129e1399180cfc684660fc9740a.jpg)

Exhibit 26: Back-end's proportion has decreased over the years China semi equipment import value by category  
![](images/3ed526010ebb1bdfbd7ee119e75cb11e544b23a74457b6151601b1f4a70de264.jpg)  
Source: China General Customs

## Exhibit 27: Since 2H23, lithography has disproportionally increased relative to others

China semi equipment import value by four key categories

![](images/b241cd084ef74861a31f8d692ff36f51b0162a60b288c3bc15137b992cf5e244.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 29: Japan's share of imports at $25\%$ of total in 2026 YTD China semi equipment import value by key countries  
![](images/fb38115bd438ab33c70b176129dba6195990a16c786b620a86777610742234c5.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH  
Global wafer fab equipment (WFE) end Market in 2024

![](images/a2664a482750f0d7315344397c7f1cbd4e51289db7ab518fddf535e35d8503cc.jpg)  
Source: Gartner

## Exhibit 28: Etching and Plasma dry etchers have gained good proportion

Exhibit 31: In 2024, China accounted for 36.2% of the global WFE end-market  
China semi equipment import proportion by category  
![](images/e7a067af2b57b358b6be649439bb90dbe2e447a01c88240a30ff6ba07d0cb4e0.jpg)  
Source: China General Customs  
Source: China General Customs  
BofA GLOBAL RESEARCH  
Exhibit 30: Japan and Netherlands accounted for a combined 38% of semi equipment imports into China in 2026  
2026 China semi equipment import value by country

![](images/4dc38dfd51e7961fa4c576ff1e72dea9e3ab5f5a2d8364f4aad20ae7e74c6e34.jpg)  
BofA GLOBAL RESEARCH

# Front-end equipment import total compared to semi equipment suppliers' disclosed China equipment sales

On an annual basis, the disclosed China equipment sales of the five largest semi equipment companies (Applied Materials, Lam Research, Tokyo Electron, ASML KLA) total to \~75% of the customs import total for front-end semi equipment over the same period. On a quarterly basis, it ranges between 58% and 85%. Thus, we believe that tracking monthly China import data can be a useful indicator of how semi equipment suppliers' China sales are trending.

Exhibit 32: Top five semicap suppliers' disclosed China sales accounted for 79% of front-end China imports in 2Q26

Top five semi equipment suppliers' disclosed China sales as % of front-end equipment customs import value

![](images/63aaade993d2e33e6a203449e732ef24cf3cd0e77b05d2d7334c0ea8d07c5eaa.jpg)  
Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 33: Top five's disclosed sales as % of import total was steady at 65-77% between 2021-25 on an annual basis. Semi equipment suppliers' disclosed China equipment sales compared to China customs' front-end semi equipment total

<table><tr><td>US$mm</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td></tr><tr><td>Applied Materials (FY Jan 29 to Jan 28)</td><td>6,394</td><td>5,036</td><td>7,093</td><td>7,215</td><td>6,496</td></tr><tr><td>Lam Research</td><td>3,630</td><td>3,581</td><td>2,833</td><td>3,542</td><td>4,843</td></tr><tr><td>Tokyo Electron</td><td>3,493</td><td>2,883</td><td>3,728</td><td>5,291</td><td>4,226</td></tr><tr><td>ASML</td><td>2,536</td><td>2,379</td><td>6,954</td><td>9,729</td><td>8,124</td></tr><tr><td>KLA Corporation</td><td>1,707</td><td>2,378</td><td>2,620</td><td>3,395</td><td>3,078</td></tr><tr><td>Total disclosed China equipment sales</td><td>17,760</td><td>16,257</td><td>23,228</td><td>29,171</td><td>26,768</td></tr><tr><td>Front-end equipment imports total</td><td>23,835</td><td>21,996</td><td>31,521</td><td>37,909</td><td>41,115</td></tr><tr><td>Disclosed China sales as % of front-end equipment imports</td><td>75%</td><td>74%</td><td>74%</td><td>77%</td><td>65%</td></tr></table>

Source: Company reports, China General Customs  
BofA GLOBAL RESEARCH

## Lithography imports - up 3% in June 2026

Lithography import value in June 2026 was up 3% yoy and up 184% mom. Unit volume was up down 13% yoy and up 36% mom. ASP was up 18% yoy and up 108% mom. This followed a weak May with imports down 2% yoy.

Import value in 2Q26 was down 13% yoy and down 25% qoq. Unit volume was down 27% yoy and up 9% qoq. ASP was \$9.2mm, below the previous 4qtr average of \$13.8mm.

China's lithography import value has grown at a $32\%$ CAGR between 2021-2024 and was down $1\%$ in 2025, driven by an increase in ASP.

Note that the lithography import category co

[中间内容因长度限制已省略]

ect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
