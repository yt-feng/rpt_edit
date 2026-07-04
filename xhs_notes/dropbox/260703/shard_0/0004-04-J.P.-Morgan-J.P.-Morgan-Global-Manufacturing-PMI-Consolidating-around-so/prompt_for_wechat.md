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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JPM`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化。汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## JPM Global Manufacturing PMI

## Consolidating around solid growth in June

The boom in global industry through April looks to be consolidating around midyear, according to the latest surveys. The JPM global manufacturing output PMI fell back 0.5-point in June from the five-year high it reached in the prior month. At 53.0, the output PMI is still elevated and consistent with a solid 2.7%ar pace of growth in global industry. Still, the dip in the new orders and future output components reinforce the message that the robust pace of growth in global industry in the first half will not be sustained. We continue to look for resilience however, as a combination of solid final goods demand and inventory rebuilding are likely to keep global factory output expanding around a 3%ar pace in the coming months. The June PMIs are roughly consistent with this call.

Jan 22 Jul 22 Jan 23 Jul 23 Jan 24 Jul 24 Jan 25 Jul 25 Jan 26
Source: JPM Global Economics  
Global manufacturing output PMI and actual output  
![](images/5e32a76039863118d7013358dd60edeeca5c93d329ca5539d669fe2d169fc431.jpg)  
Global factory output and final sales %3m, saar (through April 2026)

![](images/c57e50fd125cef6259cec1e56255295227ef72814baee1e30b48063615442fc3.jpg)

The rebound in global industry this year reflects a reacceleration in the final sales of goods, owing to gains in both consumer retail spending and business capex. The PMIs led this improvement in output as well as demand, with the global new orders PMI jumping nearly 3-points this year. We expect some cooling in the coming months as consumers take a breather and capex comes off the boil. However, a rebound in labor markets alongside strong stock market gains and the fall back in energy prices should be enough to keep goods spending well supported. While the new orders index ticked lower for a second straight month, it still remains near its four-year high. We also look for stockbuilding to perk up as inventories have gotten lean over the past year.

Manufacturing output PMI  
![](images/86387d51c035614b2af08d0ef31f2ffc76a752db8d9eb9cbec130385eba74e63.jpg)

The general trend up in the output PMIs have been broadly based, despite some moderation in June. The US output PMI slipped last month but still stands out with the most impressive gain over the past year. The increases across Asia in recent months reveal that the strength of the tech boom is outweighing the impact of the energy shock. Still, the pullback in June is a reminder that that the torrid pace is likely to cool some.

JPM global manufacturing PMI summary

<table><tr><td></td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td></tr><tr><td>Global PMI</td><td>51.8</td><td>51.3</td><td>52.6</td><td>52.7</td><td>52.2</td></tr><tr><td>Output</td><td>53.1</td><td>51.5</td><td>53.4</td><td>53.5</td><td>53.0</td></tr><tr><td>Future output</td><td>62.0</td><td>60.0</td><td>60.0</td><td>60.0</td><td>59.0</td></tr><tr><td>New orders</td><td>52.5</td><td>51.3</td><td>53.2</td><td>52.9</td><td>52.6</td></tr><tr><td>Export orders</td><td>51.4</td><td>50.0</td><td>50.2</td><td>49.6</td><td>49.4</td></tr><tr><td>Employment</td><td>50.1</td><td>49.9</td><td>49.8</td><td>50.2</td><td>49.6</td></tr><tr><td>Output prices</td><td>52.8</td><td>55.1</td><td>58.2</td><td>58.0</td><td>57.0</td></tr><tr><td>Fin goods inv</td><td>49.6</td><td>48.8</td><td>49.5</td><td>50.0</td><td>49.7</td></tr><tr><td>Delivery times</td><td>48.6</td><td>46.6</td><td>44.9</td><td>44.9</td><td>45.8</td></tr><tr><td colspan="6">memo:</td></tr><tr><td>Orders/fin goods</td><td>1.06</td><td>1.05</td><td>1.07</td><td>1.06</td><td>1.06</td></tr></table>

Source: S&P Global, JPM

%3m, saar; thru May

Manufacturing output PMI

![](images/51efce96805226c8b0551fc074e845ae48b51d1fbb1a12be69d140e80d4401f1.jpg)

Recent PMI surveys since the start of the Middle East conflict have flagged that businesses have been boosting demand and output in part as a hedge against potential bottlenecks in the coming months. If so, the earlier strength could fade some. Such a dynamic could be attributed to the pullback in the global new orders and inventory PMIs last month. However, the relief of an end to the conflict would likely dominate any such correction, particularly as energy prices normalize. Indeed, as noted above, the new orders PMI remains near a four-year high, and we still see the level of inventories as being lean. On balance, the ratio of the new orders to inventory PMIs has come off its highs but still points to global factory output expanding around a strong 3%ar pace, in line with our expectations.

Global manufacturing PMI and output  
![](images/7340f4c34fb6f48378de19c48e9b5396a210106e62c6367b508363a9cf1e7fcd.jpg)

The forward-looking component of the PMIs is the one area of notable concern. Other than a brief spike up and then back down at the start of the year, the future output PMI has been largely divorced from the trend up in the output PMI over the past year. Moreover, the future output PMI took a sizable step down in June and is now near the low end of the range of this expansion. The gap between the current and future output PMIs has widened sharply and now looks like the gap seen in the 2018-19 trade war, which saw growth in manufacturing output slow considerably below the pace implied by the output PMI.

Global PMI, manufacturing  
![](images/856e93cabb155f6a62092fc44759fbfed44cd97dddf89bccdc6c1d24286b1eff.jpg)

The impact of the Middle East conflict on pricing has been acutely visible in the PMIs. It is thus not surprising to see that the constructive steps towards ending the conflict delivered a fall back in the manufacturing PMI for prices. The output price PMI held on to the spike posted in March and April and is up 6.4 points this year. Even more striking, the input price PMI has skyrocketed 12.3 points this year. Both the input and output price PMIs slid in June. Nevertheless, both remain extremely elevated and raise upside risks to underlying core goods price inflation.

Global goods pricing, PMI and core goods
DI, sa; thru June  
![](images/c2c74d2093bd1eba6ada93a100fd9435e523566d6a19b8e091e2286895232dca.jpg)

Manufacturing output price PMI  
![](images/7d5db28ea66873a8aea028d31023aaeb0726e91761854a9abfd28f89942a2bda.jpg)

## Sector manufacturing PMI highlights

\- Underlying the move down in the June global output PMI were mixed sectoral moves. The investment and intermediate output PMIs fell back 1.1-point and 0.6-point,

respectively, after reaching multi-year highs in May. The consumer output index ticked up, but remains the weakest of the sectoral series.

\- The 1.1-point drop in the investment (or capital) goods PMI last month only partially unwound May's gain. At 53.8, the index remains well above its recent and historic average. The index's rapid gain from a November trough has mirrored the 1H26 rebound in actual capex spending, which looks to be fueled by continued tech investment but also the start of a non-tech recovery. As a diffusion index, the PMI's strength signals a broad-based pick-up rather than a narrow tech lift. Even with June's fall, the series' 2Q average is the strongest print since 2021.

JPM global manufacturing sector PMI summary

<table><tr><td colspan="2"></td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td></tr><tr><td rowspan="3">Consumer</td><td>Output</td><td>53.1</td><td>53.1</td><td>50.4</td><td>53.1</td><td>51.9</td><td>52.1</td></tr><tr><td>New orders</td><td>51.9</td><td>52.1</td><td>50.7</td><td>53.4</td><td>50.9</td><td>51.1</td></tr><tr><td>Fin goods inv</td><td>48.9</td><td>51.7</td><td>48.8</td><td>50.7</td><td>51.1</td><td>50.7</td></tr><tr><td rowspan="3">Investment</td><td>Output</td><td>51.4</td><td>52.4</td><td>51.7</td><td>53.7</td><td>54.9</td><td>53.8</td></tr><tr><td>New orders</td><td>49.1</td><td>52.7</td><td>51.7</td><td>52.0</td><td>53.8</td><td>54.4</td></tr><tr><td>Fin goods inv</td><td>49.0</td><td>47.2</td><td>47.2</td><td>48.4</td><td>49.1</td><td>48.9</td></tr><tr><td rowspan="3">Intermediate</td><td>Output</td><td>51.3</td><td>53.4</td><td>52.1</td><td>53.5</td><td>53.9</td><td>53.3</td></tr><tr><td>New orders</td><td>51.5</td><td>52.8</td><td>51.5</td><td>53.8</td><td>53.7</td><td>52.8</td></tr><tr><td>Fin goods inv</td><td>49.7</td><td>49.4</td><td>49.5</td><td>49.3</td><td>49.6</td><td>49.3</td></tr></table>

Source. S&P Global, JPM

\- The consumer goods PMI, meanwhile, ticked up 0.1-point to 52.1 in June, above its recent average but below its pre-pandemic expansion pace. We look for consumer spending to be supported by improving job markets, strong financial conditions, and a fading of the energy price shock. With the June PMI continuing to hover around 52.0, the index reinforces this expectation of resilience.

\- The intermediate goods sector PMI fell back 0.6-point last month but, as with the investment goods series, remains near its highest level in over five years. The recent moves have closely tracked the steady rise in the stocks of purchases PMI, which historically has been a positive signal for manufacturing growth.

Global manufacturing output PMI, by sector  
![](images/f8cb0a1f4bca7659036dd59a0151f694e5e798eb371d2b346540c9efbc39eecb.jpg)  
Source: S&P Global, JPM

## National manufacturing PMI highlights

\- The decline in the June global output PMI was driven by a 0.8-point slide in the EM, while the DM was unchanged. In level terms, the DM continues to outperform at 54.0, well above the EM's 52.2.

\- Most of the DM economies saw an increase in their manufacturing output PMIs last month. The Euro area and Japan moved up 0.4-pt and 0.3-pt after dropping 1.1-point in May, while the UK and Australia continued their recent climb. These increases were partially offset by a 0.4-pt fall in the US, which was revised down 1.5-pts from its flash reading. Even with the US's decline, it remains the most elevated of the DM economies we track. DM PMIs are broadly outperforming their recent levels, and at 54.0 the DM aggregate index is consistent with a solid $2.0\%$ ar rise in DM factory output.

\- In the EM, China made a second consecutive monthly decline to 52.8, though after April's surge leaves the level elevated relative to recent performance. EM Asia ex China and India meanwhile dropped 1.7-point to 51.5, its weakest level in seven months, led by drops in heavily weighted Korea and Indonesia, as well as a drop in the Philippines. These offset modest increases in Taiwan, Vietnam, and Malaysia. On aggregate, the EM Asia manufacturing PMI fell 0.9-pt to 52.8.

\- EMEA EM also dropped 1.2-point to 48.2, partially unwinding May's jump and moving to the lowest level of the aggregates we track. The decline was led by large drops in Poland (-6.5-pt) and Türkiye (-4.4-point), offsetting increases in Czechia and Russia. Latam was the only region to improve on the month, rising 1.3-point with gains in both Brazil and Mexico. At 49.4, the level is by no means strong, but it is its highest reading since December 2024.

Manufacturing output PMI, change  
DI-pts; change: May to June 2026  
![](images/3369c2f960a8333a4ccd3af0789be140ead6f2dd9375b13ffaf6c8dd6be83156.jpg)  
Source: S&P Global, JPM

JPM manufacturing PMI

Last 12m from June 2026, high/low marked

<table><tr><td></td><td>Headline</td><td>Output</td><td>Future Output</td><td>New Orders</td><td>Export Orders</td><td>FG Inventories</td><td>Orders/FG Inv</td><td>Employment</td></tr><tr><td>Global</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dev Mkt</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Emerging</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EM Asia</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EMEA EM</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Latam</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>USA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EMU</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Japan</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>UK</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Canada</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>China</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Taiwan</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Korea</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>India</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Indonesia</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Vietnam</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Czech Rep.</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Poland</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Russia</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Türkiye</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brazil</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mexico</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Source: S&P Global, JPM. Please note the long-form nomenclature for China, Hong Kong, and Taiwan is Mainland China; Hong Kong SAR (China); and Taiwan (China).

Analysts' Compensation: The research analysts responsible for the preparation of this report receive compensation based upon various factors, including the quality and accuracy of research, client feedback, competitive factors, and overall firm revenues.

## Other Disclosures

JPM is a marketing name for investment banking businesses of JPM Chase & Co. and its subsidiaries and affiliates worldwide.

UK MIFID FICC research unbundling exemption: UK clients should refer to UK MIFID Research Unbundling exemption for details of JPM's implementation of the FICC research exemption and guidance on relevant FICC research categorisation.

Any long form nomenclature for references to China; Hong Kong; Taiwan; and Macau within this research material are Mainland China; Hong Kong SAR (China); Taiwan (China); and Macau SAR (China).

JPM may, from time to time, write on issuers or securities targeted by economic or financial sanctions imposed or administered by the governmental authorities of the U.S., EU, UK or other relevant jurisdictions (Sanctioned Securities). Nothing in this report is intended to be read or construed as encouraging, facilitating, promoting or otherwise approving investment or dealing in such Sanctioned Securities. Clients should be aware of their own legal and compliance obligations when making investment decisions.

Any digital or crypto assets discussed in this research report are subject to a rapidly changing regulatory landscape. For relevant regulatory advisories on crypto assets, including bitcoin and ether, please see https://www.JPM.com/disclosures/cryptoasset-disclosure.

The author(s) of this research report may not be licensed to carry on regulated activities in your jurisdiction and, if not licensed, do not hold themselves out as being able to do so.

Exchange-Traded Funds (ETFs): JPM Securities LLC (“JPMS”) acts as authorized participant for substantially all U.S.-listed ETFs. To the extent that any ETFs are mentioned in this report, JPMS may earn commissions and transaction-based compensation in connection with the distribution of those ETF shares and may earn fees for performing other trade-related services, such as securities lending to short sellers of the ETF shares. JPMS may also perform services for the ETFs themselves, including acting as a broker or dealer to the ETFs. In addition, affiliates of JPMS may perform services for the ETFs, including trust, custodial, administration, lending, index calculation and/or maintenance and other services.

Changes to Interbank Offered Rates (IBORs) and other benchmark rates: Certain interest rate benchmarks are, or may in the future become, subject to ongoing international, national and other regulatory guidance, reform and proposals for reform. For more information, please consult: https://www.JPM.com/global/disclosures/interbank\_offered\_rates

Private Bank Clients: Where you are receiving research as a client of the private banking businesses offered by JPM Chase & Co. and its subsidiaries (“JPM Private Bank”), research is provided to you by JPM Private Bank and not by any other division of JPM, including, but not limited to, the JPM Corporate and Investment Bank and its Global Research division.

Legal entity responsible for the production and distribution of research: The legal entity identified below the name of the Reg AC Research Analyst who authored this material is the legal entity responsible for the production of this research. Where multiple Reg AC Research Analysts authored this material with different legal entities identified below their names, these legal entities are jointly responsible for the production of this research. Where more than one legal entity is listed under an analyst's name, the first legal entity is responsible for the production unless stated otherwise. Research Analysts from various JPM affiliates may have contributed to the production of this material but may not be licensed to carry out regulated activities in your jurisdiction (and do not hold themselves out as being able to do so). Unless otherwise stated below in the legal entity disclosures, this material has been distributed by the legal entity responsible for production, or where more than one legal entity is listed under the analyst's name, the first legal entity will be responsible for distribution. If you have any queries, please contact the relevant Research Analyst in your jurisdiction or the entity in your jurisdiction that has distributed this research material.

## Legal Entities Disclosures and Country-/Region-Specific Disclosures:

Argentina: JPM Chase Bank N.A Sucursal Buenos Aires is regu

[中间内容因长度限制已省略]

terial only and are therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market

conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
