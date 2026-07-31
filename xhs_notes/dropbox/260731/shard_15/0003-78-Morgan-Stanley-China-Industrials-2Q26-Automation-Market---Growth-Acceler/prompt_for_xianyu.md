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
# 2Q26 Automation Market – Growth Accelerating

The OEM market growth accelerated notably while the project market remained muted in 2Q. Core product sales saw growth acceleration on AI and broader downstream resilience (e.g., battery, logistics, electronics, robots), and leading local players continued to gain share.

2Q26 sales by product – key FA products all saw sustained growth acceleration: In 2Q26, sales of low-voltage (LV) AC drive, servo, small PLC, mid-large PLC and industrial robots rose 7%, 25%, 15%, 14% and 17% y-y, respectively, vs. 4%, 17%, 14%, 11% and 14% y-y in 1Q26. MIR raised its 2026 estimates for overall automation market sales growth (+5% y-y vs. +2% y-y previously), and for some FA products such as servo (+21% y-y vs. +17% y-y previously), PLC (+11% y-y vs. +9% y-y previously), industrial robot (+14% y-y vs. +12% y-y previously), etc. This implies +5% y-y growth for the overall market into 2H vs. +4% y-y in 1H. (See details in Exhibit 2)

By downstream, recovery appears to be on broader basis: Industries such as battery, electronics, semi, and robots saw growth accelerate. Logistics, machine tool, and textile sustained decent growth momentum. Process industries (e.g., chemical, metallurgy) and elevator demand stayed relatively soft. Solar turned to slightly positive y-y growth YTD.

Local brands continued to outperform: Market shares of local brands of LV AC drives, servos, small PLC, mid-large PLC and industrial robots reached 42%, 59%, 39%, 17% and 61% in 2Q26, respectively, up 1ppt, 4ppt, 4ppt, 1ppt and 5ppt, y-y. Estun was the No.1 industrial robot maker in China in terms of shipments in 2Q26, with 9.9% market share.

Automation up-cycle reaffirmed: We expect automation to benefit from a broadening capex cycle, and project \~5% y-y growth in 2026 led by: 1) tech-driven demand - AI and physical AI applications, such as intelligent robots, PCB equipment, liquid cooling, electronics, etc.; 2) growing energy security demand; 3) replacement demand kicking in, with possible acceleration on rapid technology iteration; and 4) equipment companies' increasing export competitiveness. We prefer Hongfa (600885.SS) on strong order momentum, AIDC 800V architecture opportunity and attractive valuation, and Bochu (688188.SS) on manufacturing capex recovery, structural laser penetration, new products and end-market expansion.

Sheng Zhong  
Equity Analyst  
Sheng.Zhong@morganstanley.com +852 2239-7821

Chelsea Wang  
Equity Analyst  
Jinlin.Wang@morganstanley.com +852 2239-1118

Carlos Chai  
Research Associate  
Carlos.Chai@morganstanley.com +852 3963-3180

![](images/68579f320915d7e637998a32bf6650cf5a3f47a4429c5c11177bb357e93aebd3.jpg)

Asia Summer School 2026

Asia Pacific Industry View In-Line

## Exhibit 1: MIR forecast – by OEM/project market

<table><tr><td></td><td>2Q25</td><td>2Q26</td><td>y-y</td><td>1H25</td><td>1H26</td><td>y-y</td><td>2026e</td><td>y-y</td></tr><tr><td>Automation market</td><td>87,588</td><td>92,603</td><td>6%</td><td>177,213</td><td>184,638</td><td>4%</td><td>359,276</td><td>5%</td></tr><tr><td>--OEM market</td><td>32,381</td><td>37,852</td><td>17%</td><td>64,726</td><td>72,579</td><td>12%</td><td>135,158</td><td>9%</td></tr><tr><td>--Project market</td><td>55,207</td><td>54,751</td><td>-1%</td><td>112,487</td><td>112,059</td><td>0%</td><td>224,118</td><td>2%</td></tr></table>

Source: MIR data/estimates, MS

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Key Charts

Exhibit 2: The industrial enterprise profit's gradual recovery echoes our view that automation capex will be in an up-cycle in 2026  
![](images/ac9feb181c9168b2854ee6a44438c66b0289f3b9ba744a62c32dba11f7348a27.jpg)  
Source: NBS. MIR, MS estimates

Exhibit 3: 2Q26 automation market by downstream segment and key domestic players' shares

<table><tr><td>Rmb mn</td><td>2Q25</td><td>2Q26</td><td>y-y</td><td>1H25</td><td>1H26</td><td>y-y</td><td>Key players 2Q26 m/s</td><td>y-y</td><td>2026E</td><td>y-y</td></tr><tr><td rowspan="3">Low-voltage AC drive</td><td rowspan="3">7,244</td><td rowspan="3">7,715</td><td rowspan="3">7%</td><td rowspan="3">14,614</td><td rowspan="3">15,380</td><td rowspan="3">5%</td><td>ABB 17.2%</td><td>↑+1.0ppt</td><td rowspan="3">29,506</td><td rowspan="3">3%</td></tr><tr><td>Siemens 12.9%</td><td>↓-0.2ppt</td></tr><tr><td>INVT 5.4%</td><td>↓-0.2ppt</td></tr><tr><td rowspan="6">Servo</td><td rowspan="6">5,782</td><td rowspan="6">7,204</td><td rowspan="6">25%</td><td rowspan="6">11,262</td><td rowspan="6">13,604</td><td rowspan="6">21%</td><td>Siemens 10.7%</td><td>↓-0.6ppt</td><td rowspan="6">26,976</td><td rowspan="6">21%</td></tr><tr><td>Panasonic 7.5%</td><td>↓-0.3ppt</td></tr><tr><td>Yaskawa 5.8%</td><td>↓-1.5ppt</td></tr><tr><td>Leadshine 5.4%</td><td>↑+1.2ppt</td></tr><tr><td>Delta 5.2%</td><td>↓-0.7ppt</td></tr><tr><td>Wuxi Xinjie 4.6%</td><td>↑+0.7ppt</td></tr><tr><td rowspan="2">Small PLC</td><td rowspan="2">1,512</td><td rowspan="2">1,732</td><td rowspan="2">15%</td><td rowspan="2">2,955</td><td rowspan="2">3,383</td><td rowspan="2">14%</td><td>Siemens 29.6%</td><td>↓-1.1ppt</td><td rowspan="2">6,849</td><td rowspan="2">12%</td></tr><tr><td>Wuxi Xinjie 11.7%</td><td>↑+0.2ppt</td></tr><tr><td rowspan="2">Mid-large PLC</td><td rowspan="2">2,600</td><td rowspan="2">2,961</td><td rowspan="2">14%</td><td rowspan="2">5,286</td><td rowspan="2">5,938</td><td rowspan="2">12%</td><td>Siemens 51.3%</td><td>↓-1.2ppt</td><td rowspan="2">10,874</td><td rowspan="2">8%</td></tr><tr><td>Omron 9.7%</td><td>↑+1.8ppt</td></tr><tr><td rowspan="6">Industrial robots (unit)</td><td rowspan="6">86,090</td><td rowspan="6">100,806</td><td rowspan="6">17%</td><td rowspan="6">162,871</td><td rowspan="6">188,612</td><td rowspan="6">16%</td><td>Estun 9.9%</td><td>↓-0.3ppt</td><td rowspan="6">382,122</td><td rowspan="6">14%</td></tr><tr><td>KUKA 9.8%</td><td>↑+0.6ppt</td></tr><tr><td>Fanuc 8.0%</td><td>↓-1.0ppt</td></tr><tr><td>ABB 4.1%</td><td>↓-1.3ppt</td></tr><tr><td>Epson 5.6%</td><td>↓-0.7ppt</td></tr><tr><td>Efort 6.3%</td><td>↑+0.9ppt</td></tr><tr><td>--&lt;20kg 6-axis</td><td>27,025</td><td>31,167</td><td>15%</td><td>51,215</td><td>58,537</td><td>14%</td><td>-</td><td>-</td><td>113,557</td><td>12%</td></tr><tr><td>--&gt;20kg 6-axis</td><td>24,725</td><td>27,470</td><td>11%</td><td>49,832</td><td>53,352</td><td>7%</td><td>-</td><td>-</td><td>113,171</td><td>7%</td></tr><tr><td>--SCARA</td><td>21,495</td><td>24,205</td><td>13%</td><td>39,615</td><td>46,565</td><td>18%</td><td>-</td><td>-</td><td>92,437</td><td>15%</td></tr><tr><td>--Cobot</td><td>11,250</td><td>16,320</td><td>45%</td><td>19,185</td><td>26,970</td><td>41%</td><td>-</td><td>-</td><td>56,168</td><td>40%</td></tr></table>

Source: MIR data, MS. E = MIR estimates.

Exhibit 4: Japan machine tool orders to China continued to build momentum  
![](images/30f59b21abb643c716520cddef7173c4bea6e5ef4ccf8183936a9bceb5a910c0.jpg)  
Source: JMTBA, MS

Exhibit 5: 2025 automation market fell 1% y-y; MIR sees full-year 2026 improving to +5% y-y  
![](images/ef029d2f710840df33f0195bb36252568138c22c376d976f0d19f7c80e2e9b38.jpg)  
Source: MIR, MS. e = MIR estimates

Exhibit 6: China's automation market accelerated to +6% y-y in 2Q26, mainly driven by OEM market  
![](images/d1779b1f23fa802f61949ac03883acb083bac5494c5a3183f2a44ac2bd3d55b4.jpg)  
Source: MIR, MS

Exhibit 7: China's automation OEM market by downstream segment, in 2Q26  
![](images/41bc8b1f90e9107a10aa93ce7c89e6332225fc0d39637a3acafaf0282b488f24.jpg)  
Source: MIR, MS

Exhibit 8: China's automation project market by downstream segment, in 2Q26  
![](images/14f32c70789cbe191d350c1c4d2ec505ba784c3bcadca5c005aa51397eab3ba3.jpg)  
Source: MIR, MS

Exhibit 9: China's LV AC drive market: Localization rate reached 42% in 2Q26, up 1ppt y-y  
![](images/cf4238ac33faa40ef73f0db069285baadc5dc3833034702db181d30eba09b9a9.jpg)  
Source: MIR, MS

Exhibit 10: China's 2Q26 LV AC drive market grew 7% y-y, among which logistics and HVAC outperformed  
![](images/e2bf65726e9fd051c67c3032ac898b5972ca9f3e2bfc7afcf8019f01ecf3bec5.jpg)  
Source: MIR, MS

Exhibit 11: China's servo market: Localization rate reached 59% in 2Q26, up 4ppt y-y  
![](images/5240df0ecaa4f30bafe9a5c1cf2778c39fc40d1fd0a91c2f00225561c5e6a4b3.jpg)  
Source: MIR, MS

Exhibit 12: China's 2Q26 servo market grew 25% y-y, supported by battery, electronics and semiconductor  
![](images/5f78a9d47c2fb2eba2ed27028eeb92791a922def86f5f8b4030e8ddff0ca81e0.jpg)  
Source: MIR, MS

Exhibit 13: China's small PLC market: Localization rate reached $39\%$ in 2Q26, up 4ppt y-y  
![](images/83c0a5956a607da168379352d30ae048acf3a2dba71987e955b5b4d9fcb129db.jpg)  
Source: MIR, MS

Exhibit 14: China's small PLC market grew 15% y-y in 2Q26, supported by logistics, electronics, battery, semiconductor  
![](images/1d63c7e6248036a1d00cf5a9326398a14cb649ecb17e2e88d6c7ac4c724a2edf.jpg)  
Source: MIR, MS

Exhibit 15: China's mid-large PLC market: local brands share is still relatively low at 17% in 2Q26, up 1ppt y-y  
![](images/17ca31134068c98993571a677de3556b808a5b29b0253e7bb021bca2dc690020.jpg)  
Source: MIR, MS

Exhibit 16: China's mid-large PLC market grew 14% y-y in 2Q26, supported by battery and electronics  
![](images/0f99849a92dcfae3abbd81d68f8368725bbf861d5f4b1fbbe58da48332da7ce1.jpg)  
Source: MIR, MS

Exhibit 17: China's industrial robot shipments grew 14% y-y in 2025; MIR estimates 14% y-y rise in 2026  
![](images/4e72fc845fd2ffbac6cd93f9fbe63947d4dc5e460d06c65c3be0f87823e75c68.jpg)

Exhibit 18: In 2Q26, industrial robots shipment grew 17% y-y; cobots outperformed with 45% y-y growth  
![](images/3d64b6e9a35f35cc8e819e8aef221c8b892bf4a8282b076913453910b02465bf.jpg)  
Source: MIR, MS  
Source: MIR, MS. e=MIR estimates

Exhibit 19: Growth in robot shipments in 2Q26 was mainly supported by battery, electronics, auto electronics,  
![](images/a20ce7fcc69e301f36ef74308d9a2b525edde566873fb71ae7fa981b2aa71d77.jpg)  
Source: MIR, MS

Exhibit 20: China's industrial robots market share dynamics - localization further exceeded 60% in 2Q26  
![](images/95ebbadaf4693930dee76d6a443606a8ab107f2846dc838f9aa1bea9868bb454.jpg)  
Source: MIR, MS

## Valuation Methodology and Risks

## Hongfa Technology Co Ltd (600885.SS)

Base case, P/E. We apply FY2 P/E multiple of 25x to 2027e EPS. This is largely in line with the historical average +1sd, reflecting our positive view on Hongfa's strong global business presence, diversified downstream exposure, and continued market share gains supported by rapid product iteration.

## Risks to Upside

■ Faster-than-expected growth in AIDC, ESS and new electrical products

■ Faster-than-expected commodity price decline

■ Faster-than-expected adoption of 800V products

## Risks to Downside

■ More intense price competition and rising raw material costs, hampering Hongfa's margin

■ Sharp decline in China's property market, resulting in weak home appliance consumption

■ Downturn in global EV demand

## Shanghai BOCHU Electronic Technology (688188.SS)

Base case, derived from P/E methodology. Our target multiple is 30x 2027e P/E, this is largely in-line with Inovance, given Bochu's dominant position in laser cutting motion control system, but it's still below Bochu's 5-year historical average FY2 P/E of 36x due to our expectation of slower revenue growth in 2026-27.

## Risks to Upside

■ Better-than-expected market share gains in high-power MCS market.

■ Faster-than-expected market expansion in welding MCS market.

## Risks to Downside

\- Narrowing demand for low- to mid-power equipment.

■ Margin pressure from intensified competition in the low- to mid-power market.

■ Unfavorable product mix.

## Disclosure Section

The information and opinions in MS were prepared or are disseminated by MS Asia Limited (which accepts the responsibility for its contents) and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents), and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS, and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Carlos Chai; Andy Huang; Chelsea Wang; Sheng Zhong.

## Global Research Conflict Management Policy

MS has been published in accordance with our conf

[中间内容因长度限制已省略]

written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: China Industrials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/28/2026)</td></tr><tr><td>Chelsea Wang</td><td></td><td></td></tr><tr><td>China Railway Group (601390.SS)</td><td>E (05/12/2022)</td><td>Rmb4.55</td></tr><tr><td>China Railway Group (0390.HK)</td><td>E (08/11/2025)</td><td>HK$3.59</td></tr><tr><td>China State Construction Engineering (601668.SS)</td><td>U (08/11/2025)</td><td>Rmb4.64</td></tr><tr><td>Han's Laser (002008.SZ)</td><td>O (10/02/2025)</td><td>Rmb94.17</td></tr><tr><td>Hefei Meyer Optoelectronic Technology (002690.SZ)</td><td>E (09/08/2025)</td><td>Rmb15.30</td></tr><tr><td>iRay Technology Company Limited (688301.SS)</td><td>O (07/07/2026)</td><td>Rmb86.17</td></tr><tr><td>Neway Valve (Suzhou) Co., Ltd (603699.SS)</td><td>O (09/12/2025)</td><td>Rmb40.70</td></tr><tr><td>Shanghai BOCHU Electronic Technology (688188.SS)</td><td>O (08/22/2024)</td><td>Rmb99.03</td></tr><tr><td>Shenzhen Envicool Technology Co Ltd (002837.SZ)</td><td>O (08/19/2024)</td><td>Rmb55.13</td></tr><tr><td colspan="3">Sheng Zhong</td></tr><tr><td>Beijing Geekplus Technology Co., Ltd. (2590.HK)</td><td>O (08/07/2025)</td><td>HK$9.26</td></tr><tr><td>Centre Testing International Group (300012.SZ)</td><td>E (11/18/2024)</td><td>Rmb13.41</td></tr><tr><td>CRRC Corp Ltd (1766.HK)</td><td>U (01/22/2026)</td><td>HK$4.97</td></tr><tr><td>CRRC Corp Ltd (601766.SS)</td><td>U (01/22/2026)</td><td>Rmb6.00</td></tr><tr><td>DR Laser (300776.SZ)</td><td>E (12/17/2021)</td><td>Rmb109.59</td></tr><tr><td>Estun Automation Co Ltd (002747.SZ)</td><td>U (06/30/2022)</td><td>Rmb30.34</td></tr><tr><td>Haitian International Holdings Limited (1882.HK)</td><td>E (09/08/2025)</td><td>HK$20.38</td></tr><tr><td>Hongfa Technology Co Ltd (600885.SS)</td><td>O (05/23/2023)</td><td>Rmb33.28</td></tr><tr><td>Jiangsu Guomao Reducer Co Ltd (603915.SS)</td><td>U (01/08/2025)</td><td>Rmb12.35</td></tr><tr><td>Jiangsu Hengli Hydraulic Co.Ltd (601100.SS)</td><td>O (05/23/2023)</td><td>Rmb103.80</td></tr><tr><td>Jingsheng Mechanical &amp; Electrical Co (300316.SZ)</td><td>U (01/08/2025)</td><td>Rmb38.46</td></tr><tr><td>Leader Harmonious Drive Systems (688017.SS)</td><td>O (01/22/2026)</td><td>Rmb293.03</td></tr><tr><td>Sany Heavy Industry Co., Ltd. (600031.SS)</td><td>O (01/08/2025)</td><td>Rmb19.70</td></tr><tr><td>Shenzhen Inovance Technology (300124.SZ)</td><td>++</td><td>Rmb58.67</td></tr><tr><td>Shenzhen SC New Energy Technology Corp (300724.SZ)</td><td>U (09/08/2025)</td><td>Rmb56.04</td></tr><tr><td>Sinotruk (Hong Kong) Limited (3808.HK)</td><td>E (05/19/2025)</td><td>HK$40.08</td></tr><tr><td>Suzhou Maxwell Technologies Co Ltd (300751.SZ)</td><td>U (09/15/2023)</td><td>Rmb168.26</td></tr><tr><td>Times Electric (3898.HK)</td><td>E (01/22/2026)</td><td>HK$32.66</td></tr><tr><td>WeiChai Power (2338.HK)</td><td>O (03/30/2026)</td><td>HK$30.92</td></tr><tr><td>WeiChai Power (000338.SZ)</td><td>O (03/30/2026)</td><td>Rmb26.19</td></tr><tr><td>Wuxi Autowell Technology Co Ltd (688516.SS)</td><td>U (09/08/2025)</td><td>Rmb37.20</td></tr><tr><td>Wuxi Lead Intelligent (300450.SZ)</td><td>O (09/08/2025)</td><td>Rmb33.03</td></tr><tr><td>Zhejiang Dingli Machinery Co Ltd. (603338.SS)</td><td>O (11/05/2025)</td><td>Rmb58.21</td></tr><tr><td>Zhejiang Hangke Technology (688006.SS)</td><td>O (09/08/2025)</td><td>Rmb20.49</td></tr><tr><td>Zhejiang Shuanghuan Driveline Co. Ltd. (002472.SZ)</td><td>O (08/25/2023)</td><td>Rmb35.63</td></tr><tr><td>Zoomlion Heavy Industry (1157.HK)</td><td>O (09/08/2025)</td><td>HK$7.50</td></tr><tr><td>Zoomlion Heavy Industry (000157.SZ)</td><td>O (09/08/2025)</td><td>Rmb7.54</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
