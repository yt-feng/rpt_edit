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
# Asia Fund Manager Survey

# Fed headwinds vs. AI tailwinds

## BofA July Asia Fund Manager Survey

Spotlight: Our US Economics team now expects the Fed to hike by 75bp this year (see note), starting in Sep. FMS investor views on the implications for Asia are mixed: nearly half would maintain their Asia equity exposure following Fed hikes, a similar proportion would reduce allocations. Looking ahead to the next phase of the AI cycle, Japan (28%) and the US (28%) have overtaken Taiwan (11%) as the biggest beneficiaries. Investor optimism toward Asia ex-Japan equities improved further, reaching 89th percentile.

Macro: APAC ex-Japan growth expectations have rebounded to pre-Middle East conflict levels. China and Japan growth expectations remain sharply divergent, with Japan growth sentiment staying robust while sentiment toward China remains subdued. On Japanese monetary policy, 60% of investors surveyed expect the next BoJ rate hike in 4Q26 (Oct or Dec), broadly consistent with our Japan economist's base case for an Oct'26 hike (see note).

Valuations: 60% of investors surveyed believe the positive impact of AI on equities is only partially or mostly not priced in, suggesting continued scope for AI-driven upside.

Themes: Earnings continue to be the dominant driver of Japan equities, cited by 64% of investors surveyed vs. 41% in Jun (Exhibit 13). Power & Energy (28%, up from 9% in Jun) stands out as a key beneficiary within the AI value chain (Exhibit 16).

Positioning: Taiwan surpassed Japan to become the most favored market, while India and Indonesia stay at the bottom of investor preferences (Exhibit 18). Within Asia ex Japan, Tech Hardware/Semis retained its leadership position, while Industrials rose sharply to rank third (Exhibit 19). In Japan, Semis holds onto the top spot, Banks gained favor, and Tech Hardware lost some momentum vs. June (Exhibit 21).

Exhibit 1: Nearly half of investors would maintain their Asia equity exposure following Fed rate hikes, while an equal proportion would trim allocations

If the US Fed were to hike rates, how would you adjust exposure to Asia equities?

![](images/fcfb5fd0565e7e3c14a19ea50ca58b2156c84e8efd4e9c91dcb104f5f64f9a53.jpg)  
Source: BofA Asia Fund Manager Survey

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.

Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Refer to important disclosures on page 15 to 17.

## 14 July 2026

Equity Strategy Asia Pacific

## BofA Data Analytics

![](images/8bcc09c10c79d110433696ff438c44d0967bb0545e07e33ea4a361cf0f433877.jpg)

Kaspar Lam >>
Research Analyst
BofA (Hong Kong)
kaspar.lam@bofa.com

Winnie Wu >>  
Research Analyst  
BofA (Hong Kong)  
winnie.wu@bofa.com

Masashi Akutsu >>
Strategist
BofAS Japan
masashi.akutsu@bofa.com

Amish Shah, CFA >> Research Analyst BofAS India shah.amish@bofa.com

FMS: Fund Manager Survey  
APAC: Asia Pacific

## Notes to readers

A total of 210 panelists with \$555bn AUM participated in the July survey. 181 participants with \$484bn AUM responded to the Global FMS questions and 101 participants with \$274bn AUM responded to the Regional FMS questions.

Survey period: Jul 2 – 9, 2026

## How to join the FMS panel

Investors/clients are encouraged to sign up to participate in the Survey. This can be done by contacting Michael Hartnett or your BofA sales representative.

Participants in the survey receive the full set of results for the months in which they participate.

## Macro

Exhibit 2: APAC ex-Japan growth expectations have recovered to pre-Middle East conflict levels Net % expecting a stronger Global / APAC ex-Japan economy

Exhibit 3: Inflation expectations continue to ease in July, moving closer to the long-term average  
![](images/88ca042f735d823771e58d9de2caf47fd827a75cbdcb9e1cdce1c15f973bfe22.jpg)  
Source: BofA Global & Asia Fund Manager Survey  
BofA GLOBAL RESEARCH  
Net % expecting higher inflation in Asia Pacific ex-Japan in the next 12 months

![](images/670bde56150851e24016500c029618300cef9a644c84349c3f4abb01169494cd.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 4: Corporate profit expectations stay well above the long-run average in July Net % expecting better corporate profits in Asia Pacific ex-Japan in the next 12 months  
![](images/674a26072da8d3a908b46afb8f920e8b3ab3d33e721a7bbdbd529a9552f51443.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 5: Concern that APAC ex-Japan earnings estimates are too high continue to fade in July, now at 11th percentile historically

Net % deeming consensus EPS estimates for the coming year as high

— Net % deeming consensus EPS estimates for the coming year as high
— Asia Pac ex-Japan 1m ERR, inverted, RHS

![](images/3103cac093ddcc4056996af1fe5e5433fe0d3303154ec305881aa7789ff7c410.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 6: China-Japan growth expectations remain sharply bifurcated, with Japan growth sentiment remaining robust while China sentiment stays negative

Net % expecting stronger Chinese and Japanese economies in the next 12 months

![](images/6ca8b2946a1f709516a1fb693c696c89f2ddfe11d885ccf7125aaa781837728a.jpg)  
Source: BofA Asia Fund Manager Survey. Notes: Votes for 'Don't know' are not shown above.  
BofA GLOBAL RESEARCH  
When do you think the BOJ next rate hike will be?

Exhibit 7: $60\%$ of investors expect the next rate hike to be most likely in 4Q (Oct or Dec) When do you think the BOJ next rate hike will be?

![](images/375cc2a7deb3532be937242fd6c03d4e03bdff3483782ae17da85a2758d4a232.jpg)  
Source: BofA Asia Fund Manager  
BofA GLOBAL RESEARCH

## Expected Returns and Valuations

Exhibit 8: Investor optimism toward Asia ex-Japan equities rose to $89^{\text{th}}$ percentile in July FMS views on expected upside for Asia Pac ex-Japan equities over the next 12 months  
![](images/71bc98947962b5200d6f32e3c902da336d007f8e5ea0860fcffcaac215627960.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 9: Investor optimism toward Japanese equities also improved in July FMS views on expected upside for Japan equities over the next 12 months  
![](images/e191e618200873c77671e1eac9aa6761a9068ea149f246b64c24309c5687c31b.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

Exhibit 10: FMS investors still see APAC ex-Japan equities as slightly undervalued  
Net % saying Asia Pacific ex-Japan equities are overvalued  
![](images/52200eec58e4b70ac42620fe7675e4968254c8f74efbfe6133dfd9d761e4280f.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH  
How much of the positive AI impact on equities is already reflected in the price?

Exhibit 11: $56\%$ of FMS investors say the positive AI impact on equities is only partially priced in

![](images/4576cf21915f8d49ddee8d82e9d60d6cf245c09b968078e532950ad0df085b4d.jpg)  
Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

## Themes

Exhibit 12: Within China, AI/semis and buybacks/dividend remain key investor priorities FMS views on TWO most favorite themes in China

![](images/cbc997bef8a1d6d7ba70b3ea39078236d8e3c58a12cdfa847769207d9038492f.jpg)  
Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH  
Exhibit 13: Earnings continue to be the most important driver of Japan equities FMS views on the themes that hold the key for Japan equities in the near-to-medium term  
Key themes for Japan equities in the near-to-medium term

![](images/7ea5bc76d8bbcde50be54bf111313611826ea1a17b1be0f06cbb83baa4bea9ba.jpg)  
Source: BofA Asia Fund Manager Survey. Notes: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

Exhibit 14: Investor expectations for the Korea/Taiwan semis cycle stay firmly positive in July FMS views on the semis cycle (Korea/Taiwan exports growth) over the next 12 months  
![](images/927c484386a08d1513c952c2ee8b3d7c021bf122e595c22c364f633b9c84b639.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH  
Which market benefits most from the next phase of the AI cycle?

Exhibit 15: Japan and US have overtaken Taiwan as the clearest beneficiaries of the next phase of the AI cycle

![](images/bdefc5a1f743f76d2bbbff49331512be1fb7ca85adb453cbf42c52993ac70e00.jpg)  
Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

Exhibit 16: Power & Energy ranks among the most favored segments of the AI value chain Which part of the AI value chain offers the best risk-reward over the next 12 months?  
![](images/07da17ce95ab61e6621228b2d3882d39d27ae4f1f86a658dd06f7e44d05e7a37.jpg)  
Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH  
Exhibit 17: The lack of a clear AI exposure remains the key concern for Indian equities, with weak growth emerging as the next most important risk What is your key concern for Indian market?

![](images/edf3278ab4146393808cdd28e7cc381e506c1ac2e01afa53297ecbd7702514a4.jpg)  
Source: BofA Asia Fund Manager Survey. Note: Votes for 'Don't know' are not shown above  
BofA GLOBAL RESEARCH

## Positioning

Exhibit 18: Taiwan surpassed Japan to become the most favored market, while India and Indonesia remain the least favored

Asia Pacific market sentiment: Net % overweight

Asia Pacific market sentiment: Net % overweight (% saying overweight - % saying underweight)

![](images/66e46eddd2b313e3a38ad8c7cf4656dfa046d1ebcafb516cd48ad94abdde933b.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH  
Exhibit 19: Tech Hardware/Semis retained the top spot, while Industrials climbed sharply to rank third Asia Pacific ex-Japan sector sentiment: Net % overweight  
APAC ex-Japan sector sentiment: Net % FMS investors overweight (% saying overweight - % saying underweight)

![](images/ab44b13da7cf0ae4c05e31502de4523a640ea888d2d10e58f26447cb030f5e30.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH

## Exhibit 20: July saw a rotation out of Software, Energy, and Retailing/e-Commerce into Industrials, Healthcare/Pharma, and Materials

Monthly change in FMS investor positioning

APAC ex-Japan sector sentiment: MoM ppt change in FMS investor positioning  
![](images/d70885e80d28d7a4a4d2f9d8355b3baeabf13b34111e62abbda3c9beae611723.jpg)  
Source: BofA Asia Fund Manager Survey  
BofA GLOBAL RESEARCH  
Exhibit 21: Semis remains the most preferred sector, while Banks gained favor and Tech Hardware lost some momentum vs. June  
FMS opinion on the two most overweight sectors in Japan  
FMS opinion on the two most overweight sectors in Japan

![](images/c1cc177dd43b988ef4dfc2e87923e91fb75fbded10024d28e51ff92477fbe07f.jpg)  
Source: BofA Asia Fund Manager Survey

Exhibit 22: Investors are split on de-risking the AI trade, with $44\%$ remaining unhedged and another $40\%$ rotating into other sectors or underweighting

How are you currently hedging downside risk in the AI trade over the next 6-12 months?

![](images/702cfd1757b7b9ef642c9f447cfde4790b38ffb011c019d0839b1c29c259afa5.jpg)  
Source: BofA Asia Fund Manager Survey. Notes: Votes for 'Don't know' are not shown above.  
BofA GLOBAL RESEARCH

## Regional survey demographics data

## Exhibit 23: Position / institution / approach of participants in the regional survey Demographics details for regional Fund Manager Survey participants

<table><tr><td></td><td>Jul-26</td><td>Jun-26</td><td>May-26</td></tr><tr><td colspan="4">Structure of the panel - by position</td></tr><tr><td>Chief Investment Officer</td><td>10</td><td>11</td><td>11</td></tr><tr><td>Asset Allocator / Strategist / Economist</td><td>17</td><td>18</td><td>14</td></tr><tr><td>Portfolio Manager</td><td>72</td><td>63</td><td>60</td></tr><tr><td>Other</td><td>10</td><td>7</td><td>7</td></tr><tr><td colspan="4">Structure of the panel - by expertise</td></tr><tr><td>Regional specialists + EM specialists only</td><td>29</td><td>26</td><td>30</td></tr><tr><td>Regional specialists with a global view</td><td>80</td><td>73</td><td>62</td></tr><tr><td>Total # of respondents to regional questions</td><td>109</td><td>99</td><td>92</td></tr><tr><td colspan="4">Which of the following best describes the type of money you are running?</td></tr><tr><td>Institutional funds (e.g. pension funds / insurance companies)</td><td>29</td><td>27</td><td>20</td></tr><tr><td>Hedge funds / proprietary trading desks</td><td>18</td><td>13</td><td>16</td></tr><tr><td>Mutual funds / unit trusts / investment trusts</td><td>54</td><td>48</td><td>45</td></tr><tr><td>None of the above</td><td>8</td><td>11</td><td>11</td></tr><tr><td colspan="4">What do you estimate to be the total current value of assets under your direct control?</td></tr><tr><td>Up to $250mn</td><td>16</td><td>15</td><td>17</td></tr><tr><td>Around $500mn</td><td>16</td><td>10</td><td>13</td></tr><tr><td>Around $1bn</td><td>19</td><td>21</td><td>13</td></tr><tr><td>Around $2.5bn</td><td>22</td><td>16</td><td>18</td></tr><tr><td>Around $5bn</td><td>8</td><td>12</td><td>9</td></tr><tr><td>Around $7.5bn</td><td>5</td><td>4</td><td>2</td></tr><tr><td>Around $10bn or more</td><td>11</td><td>11</td><td>8</td></tr><tr><td>No funds under my direct control</td><td>12</td><td>10</td><td>12</td></tr><tr><td>Total (USD bn)</td><td>274</td><td>270</td><td>209</td></tr><tr><td colspan="4">What best describes your investment time horizon at this moment?</td></tr><tr><td>3 months or less</td><td>33</td><td>34</td><td>30</td></tr><tr><td>6 months</td><td>36</td><td>26</td><td>28</td></tr><tr><td>9 months</td><td>6</td><td>9</td><td>7</td></tr><tr><td>12 months or more</td><td>29</td><td>27</td><td>24</td></tr><tr><td>Weighted average</td><td>6.9</td><td>6.9</td><td>6.8</td></tr><tr><td>Don&#x27;t know</td><td>5</td><td>3</td><td>3</td></tr><tr><td colspan="4">Which region do you specialise in?</td></tr><tr><td>US / North America</td><td>32</td><td>30</td><td>24</td></tr><tr><td>Europe / Continental Europe / Eurozone / UK</td><td>35</td><td>28</td><td>31</td></tr><tr><td>Asia Pacific / Asia Pacific ex Japan / Japan</td><td>25</td><td>22</td><td>21</td></tr><tr><td>South Africa</td><td>11</td><td>14</td><td>12</td></tr><tr><td>MENA (Middle East and North Africa)</td><td>0</td><td>0</td><td>0</td></tr><tr><td>None of the above</td><td>6</td><td>5</td><td>4</td></tr><tr><td colspan="4">Source: BofA Fund Manager Survey BofA GLOBAL RESEARCH</td></tr></table>

## Special Disclosures

In accordance with the SEBI (Foreign Portfolio Investors) Regulations, 2019 and with guidelines issued by the Securities and Exchange Board of India (SEBI), foreign investors (individuals as well as institutional) that wish to transact the common stock of Indian companies must have applied to, and have been approved as per SEBI (Foreign Portfolio Investors) Regulations, 2019. Each investor who proposes to transact common stock of Indian companies will be required to obtain Foreign Portfolio Investor (FPI) registration as per SEBI

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
