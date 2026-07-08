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
# China alt-data trackers chartpack (Series 58)

# Pace up (narrowly) in exports & special LGB issuance

After the largely stable June manufacturing PMIs, all eyes are on the hard activity data due over the next two weeks to gauge near-term momentum and assess how the economy is positioned heading into 3Q. We have updated our alt-data trackers (vs. our last update) and our key takeaways are below.

\- Exports: Port tracking shows departing container (+8.5%) and bulk (+10.1%) shipping deadweight tonnage both accelerated in m/m nsa terms in June. Annual growth may have picked up further. In aggregate, departing shipments deadweight tonnage (excluding tankers) rose 17.2% oya in June (vs. 7.7% in May), suggesting volume growth is picking up alongside recent price gains. Oil tanker arrivals remained subdued in June, down over 30%, similar to May.

\- CCFI to USEC, USWC rose $14.3\%$ , $20.6\%$ , respectively, compared to two weeks ago; CCFI to the Persian Gulf/Red Sea route increased by another $8.6\%$ .

\- China's domestic and int'l flight cancelation rate fell back notably in the second half of June as energy prices started to normalize.

\- Production: Processed crude oil production contraction may have deepened in June (vs -9.1% oya in May), though petroleum asphalt plants' operating rates began to recover in the second half of the month. Auto IP decline may have widened in June (vs -3.2% oya in May) while steel IP contraction may have narrowed in June (vs -2.8% oya in May). Coke oven plants stabilized in the second half of June.

Fiscal: June government bond issuance reached 1138bn yuan, broadly matching May's 1140bn yuan issuance. Special LGB issuance rebounded strongly, signaling reactive acceleration, but the uncertainty remains around proceeds deployment to projects. Full-year 200bn yuan of funding for equipment upgrades has been fully deployed, per the NDRC. If recent weakness persists, we expect faster fiscal deployment in 3Q.

• Monetary: PBOC net injected 583bn yuan via pledged 7-day OMO and 200bn yuan via MLF in June, while withdrawing 300bn yuan via outright OMO.

\- The PBOC also initiated overnight reverse repos at the end of June, in line with Governor Pan's announcement at the Lujiazui forum. But the operation's rate was not disclosed, signaling a near-term focus on 7-day reverse repo. A cut could become more likely in 2H if growth weakness persists and outweighs inflation risks.

\- Auto sales remained a drag on retail sales. Passenger car retail sales fell 21% oya in June, partially on lower per-car trade-in subsidies and purchase tax exemptions, and higher fuel costs. NEV sales fell a narrower 7%.

\- Housing: Secondary home sales continued to improve in June, while new home sales contraction widened.

\- Inflation: With calmer energy conditions under the US-Iran peace deal, gasoline, diesel and LPG prices continued to moderate in the last ten days of June. Petrochemical products prices fell sharply to near pre-conflict levels, despite a continued upturn in sulfuric acid prices. Agricultural food prices fell $0.5\%$ oya in while pork wholesale prices contraction remained elevated.

See page 11 for analyst certification and important disclosures.

Emerging Markets Asia, Economic and Policy Research

Tingting Ge (852) 2800-0143 tingting.ge@JPM.com

Jiayi Li  
(852) 2800-5229  
jiayi.c.li@JPM.com

Tongfang Yuan (852) 2800-0085 tongfang.yuan@JPM.com

Feng Zhu  
(852) 2800 1745  
feng.zhu@JPM.com  
JPM Chase Bank, N.A., Hong Kong Branch

## 1. Mapping: High-frequency trackers --> official activity

Regarding the mapping efforts from high-frequency data to monthly official activity tracking:

\- Operating rates for petroleum asphalt plants suggest processed crude oil production contraction may have deepened in June, (vs -9.1% oya in May).

\- Operating rates for tire plants suggest auto IP decline may have widened in June (vs -3.2% oya in May).

\- Operating rates for steel rebar suggest that steel IP contraction may have narrowed marginally in June (vs -2.8% oya in May).

\- Housing transactions for 30 major cities fell $7.3\%$ oya in June (vs $-1.4\%$ in May).

\- Port tracking suggests that export volume growth may have picked up in June, as departing shipments deadweight tonnage (excluding tankers) rose 17.2% oya in June (vs. 7.7% in May).

Figure 1.1: Industrial production - Processed crude oil  
![](images/06bad05033d3fc4923bbe507b72e88f920577a49077176f778a701166ebf3c34.jpg)  
Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.2: Industrial production - Auto  
![](images/c7e5ba0ad61b8bed805d13510bbb4ac040465a60e41313ca54ce61b65ca7056c.jpg)  
Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.3: Industrial production - Steel  
![](images/b3896e1fcada82f0caafb4307e4173a4f82a6eab51a986a2b46adf4887253865.jpg)  
Source: CEIC, Wind, JPM; 1/ Latest for June 2026.

Figure 1.4: China exports  
![](images/f81672825db43435d845763e419364bd863c5849ee76597ba5d534c1b63583cc.jpg)  
Source: Elane Shipping, China Customs, JPM; 1/ Latest for June 2026, excl. tankers

## 2. Trade

China's outbound container costs increased further across major routes, despite the signing of a 60-day US–Iran MoU. By destination, CCFI to USEC, USWC rose 14.3%, 20.6%, respectively, compared to two weeks ago; CCFI to the Persian Gulf/Red Sea route increased by another 13.6%. Baltic Dry Index ticked down further after several weeks of increases since April. US-bound shipping rose 6.9% oya or 15.8%m/m nsa in June (vs 25.9% oya or 1.5%m/m nsa in May).

\- Container ships usually carry consumer goods, as well as some machinery equipment and electronics. Departing container ships' deadweight tonnage rose 4.6% oya or 8.5% m/m nsa in June. Arriving container ships' deadweight tonnage fell 0.4% oya or up 6.7% m/m nsa.

\- Bulk carriers transport unpackaged bulk cargo for grain, coal, iron ore, steel, etc., in

Source: Baltic Exchange Information Services Limited, JPM their cargo holds. Departing bulk ships' deadweight tonnage rose 20.9% oya (or 10.1% m/m nsa), while arriving bulk ships' deadweight tonnage rose 23.3% oya or 8.0% m/m nsa.

\- Oil tanker arrivals remained subdued in June, down over 30%, similar to May.

China's domestic and international flight cancelation rates fell back notably in the second half of June as energy prices started to normalize.

China's soybean imports from the US decreased in May, after an uptick in April. The White House statement said China would purchase at least US\$17bn of US agricultural products annually from 2026 to 2028.

![](images/b105fdf10ded929611c6e8469a9ceb8784ea0cf25e7142a2d8f7b17874f11179.jpg)  
Source: Wind, JPM

Figure 2.2: BEISL freight index  
![](images/a86288fdf8caca52a87678241e121a3b4e3c6ff5193a328ce8f719e43a35d2e7.jpg)

Figure 2.3: Deadweight tonnage of departing ships - Container Ton mn  
![](images/98f602e5aade709d88b0a1390e36800f71fcab0d16ae7ef5d804bd2374d6daaa.jpg)  
Source: Elane Shipping Statistics, JPM.

Figure 2.4: Deadweight tonnage of arrived ships - Container Ton mn  
![](images/bb4e7061775df59602e4a8ea62e3ec901dd42b2a14a7028736ec0df452c17495.jpg)  
Source: Elane Shipping Statistics, JPM.

Figure 2.5: Deadweight tonnage of departing ships - Bulk Ton mn  
![](images/2533f8b8e98e3802e9f0766695bdcabc1a5b1a89a3de632d29adb8c3a7150dc4.jpg)  
Source: Elane Shipping Statistics, JPM.

Figure 2.6: Deadweight tonnage of arrived ships - Bulk Ton mn  
![](images/349866ff8e3ab8282eee74185514ac99c2cb7b3bbeeb374a4aa5521978240c2d.jpg)  
Source: Elane Shipping Statistics, JPM.

Source: Elane Shipping Statistics, JPM.

Figure 2.7: Deadweight tonnage of arrived ships - Oil Tanker Ton mn  
![](images/c60f6ec2328bf734f2109af8b7b1a315190657443248af7b801fdc16477c84c5.jpg)  
Source: Elane Shipping Statistics, JPM.

Figure 2.8: Deadweight tonnage of departing ships - Oil Tanker Ton mn  
![](images/8dbe1852246ba53f448dbb288b830bd795952c23afa7fcbe290362852f4e7b9d.jpg)

Figure 2.9: China flight execution % of 2019 avg, 7dma  
![](images/a860c3ded4af337281456adb6504ab5b15d4991750af1a9b25ff712e8e70eb4b.jpg)  
Source: Wind, JPM

Figure 2.10: China flight cancellation rate % of planned, 7dma  
![](images/915d97ae8b3148a3f5a524ce1f18551077fa004b70bde1c04b4a12b88a56e853.jpg)

Figure 2.11: China imports of soybeans from world Ton mn  
![](images/836bdff57c1ec5d8b5af0999a89f8dca1d0f8070e615f973576d55542b97cdc1.jpg)  
Source: CEIC, JPM

Figure 2.12: China imports of soybeans from US  
![](images/0b5739b0a37ad2a1d58a552c20fccb05a693bead5a789339d02f7ff026128f9f.jpg)

## 3. Sales and production

\- Auto sales: According to CPCA, passenger car retail sales fell 21% oya in June, partially on lower per-car trade-in subsidies and purchase tax exemptions, and higher fuel costs. NEV sales fell a narrower 7%. This suggests that auto sales may have remained a drag on headline retail sales in June.

\- Operating rates of petroleum asphalt plants rebounded in the second half of June, though still much lower than the pre-Middle East conflict levels. Operating rates for steel rebar held steady in June, while semi-steel and all-steel tires declined modestly. Coke oven plants' operation rates stabilized in the second half of June after the modest fall since mid-May.

Figure 3.1: Weekly auto retail sales Thousand units  
![](images/96a83300838855c3142be49871335701e1a150360bf7b5fb6949ceef680b69c0.jpg)  
Source: Wind, JPM

Figure 3.2: Operating rate for all-steel tire  
![](images/58c62803baf7e6eb4e3eb28bbe0e69402908e582d2964e1e7df476399c567a31.jpg)  
Source: Wind, JPM

Figure 3.3: Operating rate for semi-steel tire  
![](images/5710ba5efb888c031c11422ec069039f1e9afc82382d712f42841bbb93450787.jpg)  
Source: Wind, JPM

Figure 3.4: Operating rate for petroleum asphalt plants  
![](images/d5bd4280b56197638f3aa79837b62720bc08e3dce63735fd6677037d3b10bfcb.jpg)  
Source: Wind, JPM

Figure 3.5: Operating rate for steel rebar at major steel plants  
![](images/b3c9c628f5090782071347778d4ca980273c84a2c8964a1b3efbcda18f5fba21.jpg)  
Source: Wind, JPM

Figure 3.6: Operating rate for coke oven plants  
![](images/201b334ac16c2b2f8a5242974f9de19f9c1bd8ab547afcd6223809f0a3c14880.jpg)  
Source: Wind, JPM

## 4. Policy: Government bond issuance and liquidity operations

June's government bond issuance reached 1138bn yuan, broadly matching May's 1140bn yuan of issuance. Special LGB issuance rebounded strongly, signaling a reactive acceleration, but the uncertainty remains around proceeds deployment to projects. If recent weakness persists, we expect faster fiscal deployment in 3Q.

\- CGB issuance nearly halved to 318bn yuan in June from 708bn yuan in May. Ytd issuance reached $40.2\%$ of the annual issuance target, trailing last year's $50.8\%$ pace. In terms of further breakdown, special CGB issuance remained solid at 204bn yuan in June (vs. 249bn yuan in May), followed by 80bn yuan in July mtd. According to the NRDC, full-year 200bn yuan funding for equipment upgrades has been fully deployed.

\- Special LGB issuance rose strongly to 572bn yuan in June (vs.161bn yuan in May), exceeding last June's level, signaling a reactive acceleration in utilizing the remaining fiscal resources approved at the March NPC. This has lifted year-to-date issuance to

$47.0\%$ of the annual target, now catching up with last year's pace.

\- General LGB issuance ticked up to 41bn yuan; refinancing LGB reached 207bn yuan.

\- PBOC net injected 582.6bn yuan via pledged 7-day OMO and 200bn yuan via MLF in June, while withdrawing 300bn yuan via outright OMO. The PBOC also initiated overnight reverse repos at the end of June, with 300bn yuan on June 29 and 600bn yuan on June 30. This is in line with Governor Pan's announcement at the Lujiazui forum. But the operation's rate was not disclosed, signaling the PBOC's near-term focus on 7-day reverse repo.

\- The surprisingly soft April activity data and downside risks to 2Q GDP should keep a rate cut on the table. A more hawkish Fed may complicate the backdrop, but China's decision should remain domestically driven given a resilient CNY. A cut could become more likely in 2H if growth headwinds intensify and outweigh inflation risks. As usual, a 10bp move would likely be more of a policy signal than a meaningful easing impulse.

Figure 4.1: China CGB net issuance  
![](images/2812d9db03731a9a90f00615d3da0fef8b84d7f173aed555215a1d5752508da3.jpg)  
Source: Wind, JPM.

Figure 4.2: China CGB net issuance progress % of annual issuance (target)  
![](images/6c2b62b568e42da1ee8a6c4812710da1c2f6703e65ffa5384eb99c228e0a50c6.jpg)  
Source: Wind, JPM.

Figure 4.3: China special LGB issuance  
![](images/82a6dff1b89f54993bd31f523e041f1ee17c66f61e46afcfc04c0cc28312c287.jpg)  
Source: Wind, JPM.

Figure 4.4: China special LGB issuance progress  
![](images/2cac79895365b1212d24e1939be57f9cc97c882875c4b129a5a583c356598e88.jpg)  
Source: Wind, JPM.

Jan 24 Apr 24 Jul 24 Oct 24 Jan 25 Apr 25 Jul 25 Oct 25 Jan 26 Apr 26  
Source: Wind, JPM.

Figure 4.5: China special CGB net issuance RMB bn  
![](images/3b4e1b21d62a1c20d05271d2346b77831789ada42127c2491410bc86295952f0.jpg)

Figure 4.6: Local government special refinancing bonds issuance RMB bn  
![](images/82d2ad4c4a15420e79bcd117a43e8bde246cf1b06fbf44a1da9ea7105daa6ff6.jpg)  
Source: Wind, JPM.

Figure 4.7: General LGB new issuance  
![](images/10f936c4956c06bb5016002f801dbc00060ea9d9e5a6561763a2db8bd4c7837f.jpg)  
Source: Wind, JPM.

Figure 4.8: General LGB new issuance progress  
![](images/84e2d211b5c129fab6712d8f329a15054c05b6925a8c32d6f165547234b7582f.jpg)  
Source: Wind, JPM.

Figure 4.9: Outstanding major monetary policy instruments  
![](images/d8062cdaffdbaf3cc5686885b2b5634a56da2e721dfc2c86553f9a296220cc50.jpg)  
Source: PBOC, JPM

Figure 4.10: Outright OMO operation  
![](images/11c9e52d33c7afca9e530403ceda0a00a03e9b6a6af07b7e704b16492fceae01.jpg)  
Source: PBOC, JPM

## 5. Housing

Secondary home sales continued to improve in June, albeit at a slower pace, while new home sales contraction widened.

\- The contraction in 30 major cities' new home sales widened to $-7.3\%$ oya in June from $-1.4\%$ in May, after a brief growth of $2.8\%$ in April. Major cities' secondary home sales rose a solid $12.3\%$ in June (vs. $18.0\%$ in May).

\- Centraline's sales manager confidence index and the secondary home asking price index both edged down in June.

Land sales values were below last year's level from mid- to end-June, continuing to weigh on government fund account revenues. The sales premium rate moderated from its recent peak before a brief uptick, likely affected by a few auction cases.

Figure 5.1: Housing transactions by sqm in 30 major cities Thousand sqm, 7dma  
![](images/3b44e6fafe1b0d0d028076953feab22fa10b6fbdf3530e1cdc75d7b9e10bb3d2.jpg)  
Source: Wind, JPM

Figure 5.2: Major cities' secondary housing transactions Avg unit, 7dma  
![](images/ea204502c919f1053c5e02c4f37af5bd48798654ad5a1ac04e7ab8768258e49c.jpg)  
Source: Wind, JPM

Figure 5.3: Centraline tier-1 cities' secondary asking price index Index  
![](images/6f84a26fb5b02407983be2fc35def17adfd688d24987dcd891d729036af735c0.jpg)  
Source: Wind, JPM. Note: Simple average for 4 tier-1 cities.

Figure 5.4: Centraline sales manager index  
![](images/a59cbd04ffb8ebd8dbe2dc73ef064aa63bc1cccb5ce714af0101f40697fee71f.jpg)  
Source: Wind, JPM. Note: Simple average for Shanghai, Shenzhen and Guangzhou.

Figure 5.5: Weekly land sales  
![](images/5289a8b32c585f8595e119036f16d4c14dde9bedea709557ed9e35624360d72c.jpg)  
Source: Wind, JPM

Figure 5.6: Land sale premium rate  
![](images/f7173ecef30b37bf6ccd4ba5ca25a45ee4f551102a1e1851753756d9f32e83ef.jpg)  
Source: Wind, JPM

## 6. Inflation

\- With calmer energy conditions under the US-Iran peace deal, gasoline, diesel and LPG prices continued to moderate in the last ten days of June, whil

[中间内容因长度限制已省略]

f market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
