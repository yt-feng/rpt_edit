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
- 已识别机构名：`摩根斯坦利`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
Investor Presentation | Asia Pacific

Beijing Reacts to Weak Growth, EU Reacts to Beijing

Robin Xing
Chief China Economist
Robin.Xing@morganstanley.com

+852 2848-6511

Zhipeng.Cai@morganstanley.com

+852 2239-7820

![](images/3bf330bdb802a724285da80ce839bdf84682c7c603c63fcca79235e86fe92b69.jpg)

## China-EU Trade

## EU Reacts to Rising Trade Deficit with China

Widening trade deficit with China..

EU Trade with China, US\$Bn (12M Trailing Sum)

![](images/ccc49732afd03e759e6b0d82ad22a6e1734f51866338fd906ded04c4886a1af5.jpg)

Source: CEIC, MS

## ...raising concerns among the EU

## Latest remarks from EU

![](images/ef86a85811e97e284e7be6c4b03ec2ac5c82940ee3265135c55fabab93c4e2f2.jpg)

## READ-OUT: COLLEGE ORIENTATION DEBATE 29 MAY 2026

![](images/e6fa63feb8b7bebf6d7bf5ed5298e53a55bcbff21aec0a062af6ccc5c10a007f.jpg)

DE-RISKING, NOT DECOUPLING.

![](images/6a94ae40de679510fb9f6534b5becd56bcef5d84d35ce2c2bfa3f7691bda7898.jpg)  
CHINA IS A PARTNER, BUT THE STATUS QUO IS NOT SUSTAINABLE.

![](images/15eb708b1fd9fb0608b2f6733dd22238fe40627541b0f1828f76a8def7c24178.jpg)

![](images/f5313ece26708ccaac36da936a9c08042c1e228ddc9e7e7fb03a07e46be5e1e7.jpg)

## G7 LEADERS' STATEMENT 17 JUNE 2026

![](images/9058d15ad58c3753dca52f2c74d8d1b576306a1d294b2211f75a8fdb2a1c10d4.jpg)

SHARED INTEREST IN TACKLING THE CAUSES OF LARGE AND PERSISTENT GLOBAL IMBALANCES.

![](images/63b524a8c2cf6616bb2e3ed759568257332d49d4276d956df3cc5cf83481c73c.jpg)

WE'LL KEEP WORKING TOGETHER IN THE G20 AND OTHER KEY FORA.

![](images/4f28cff635a66143b7b3449943d1d8d4bbf829ceaf1b9613a87af00a27180593.jpg)

## EUROPEAN COUNCIL CONCLUSIONS 19 JUNE 2026

![](images/489e0a0dcbf30767863c17fa4a70ea02e9e7e4b29ef5a924b2fdad7404bae87d.jpg)

BOOST EU COMPETITIVENESS & STRATEGIC AUTONOMY.

![](images/87ac660f2dfebf2ecc42b584b0bfdd9bf513c0255e38855bfb2f80c767756de6.jpg)

BUILD RESILIENCE,
SECURITY & DRIVE INNOVATION.

![](images/401e390e2575fd5f70b82c8dbac8917c440244bed68dff0f70a8f057bf92055d.jpg)

RENEW INDUSTRY. CUT DEPENDENCIES. INVEST IN INNOVATION.

Potential China-EU Trade Pressure Points

An (increasingly) larger deficit with China shows where the pressure is, or will be

![](images/a93a437cf7f5c4f57123486a0aef88e4d7dda06afae6932a4fdbc3f5cf9f5d37.jpg)

## The overlay would be Europe's own competitiveness that it wants to defend

EU Trade Balance Against China and RoW by Product, US\$Bn  
![](images/923cf0abdc1388728c629c8b41ab07c150060705872efae2ec02a82588f8bc1d.jpg)

EU EV transition depends on China-linked battery supply chains.

![](images/1c274de9742fbf337c74cf56faf571f359f0921eabab7c283d8f63593d792791.jpg)  
EU's toolkit has expanded in recent years

## China-EU Trade

## Future Path: Navigating Preferences, Dependencies and Choke Points

![](images/630ef91a7a6ad838cd26c01260acf01b527e11c3d8766188f50f860697ca7a2f.jpg)  
FOREIGN SUBSIDIES REGULATION (FSR)  
Source: MS

## But potential tensions will likely be bounded by several forces

## TENSIONS BOUNDED BY KEY CONSTRAINTS

![](images/29513244447b74d50a84f4fa9a83eb3a6e3a798405db00ec368b32a77063ba38.jpg)

![](images/26e227264bc55d916ddf856e65a1c3134adce373091d9af28c5088f6c5a5159d.jpg)

![](images/e972914d95679c1e1abdf639fb29fab5db14494e82f58ab85facf40fd364b8ff.jpg)  
Align with EU economic interests. Consensus takes time.

![](images/9af51fc30bc9f143150604edc64a29a7d2b63963ba53a03963eac5b63ab769ba.jpg)  
Example: EV countervailing duties
Announced Sep-23 → completed Oct-24

![](images/a4e60ecaa0c7fb179b4c588e4e3fc12752dd8923ef4ed094f10d4b0adc65a277.jpg)

![](images/82a5a9957c6669e818f890c7873acaffedaaae5db6309614446c653e5d5f8b16.jpg)

![](images/d75ba92897e316dd5e55ede0298d824e69673e7ac9bd9109548c3c36c3dc60d2.jpg)

![](images/d6ec7d2414be9d6cdd7e12112a0a8760f5e383505115a31a51b151754ad34bb5.jpg)

![](images/e122ae519583a3046f2ca6f566baed09c7e61c6657d5f1abe2ff6aae53b65646.jpg)

Overly aggressive curbs risk retaliation, supply-chain friction and slower EV uptake.

![](images/ddc374c2ac19b76c92df8f5188120fd5356c2a6a65734247308c7d14a3aba71e.jpg)

![](images/e5501db40537b8666dc4910da28ab650b3e737460342c3c6c061e61e2c8d03e9.jpg)

## China retains retaliation tools:

![](images/d41e411fbbdcec2f464ea3b440217068a22fefed0972b0e808b2ed48c6d42736.jpg)

![](images/e5f07921e3fa2e4fd67528c3b2d49e5ddbf7fa27bca93cf2a0689abf7ee38e60.jpg)

![](images/a526f7fa0803ea11bdfd0a292b8fc57780c2d2b44b450cf984a056cbdffcdaa8.jpg)  
Source: European Parliament

![](images/7e791b53bb215b380fbdc3450b5846776a3d7dfe4c46771957c56e8b401062b6.jpg)

![](images/ac7a6642b711320597f581746faa579f658f38891b012fb393c903e3982661fb.jpg)

![](images/e8098e88e99ce73ccd5521d41113edc9a3c816c2864819fdf8077801d7c10858.jpg)

![](images/4d0185001653538bf92bd096bec0b91ce61036a07f263af9b7c2508bc7228a8f.jpg)  
Rare-earth magnets from China

## China Economy

## High-end Manufacturing/Exports Remain Solid

June emerging industries PMI (EPMI) is decent despite some moderation

![](images/cda1b5175d43c29106689aa0ff8ca0bcb1e1d2fc63dade9d78723dfa0b5a6e02.jpg)  
Exports likely resilient, with stabilized EPMI new orders

![](images/64e3c7f568ce6653670289da7a8a125463b084f3b780164e8538218a09ac7d23.jpg)

## China Economy

## Domestic Demand Continues to Soften

## Secondary housing sales weakened again

![](images/e380f80c0c00c93de8f9aeafa36824cafd2ec00362876df34d3dc73393ff82fb.jpg)  
Holiday travel: strong footfall, weak wallet conversion

China Holiday Tourism (Avg. YoY Per Day)  
![](images/d915815542d41722ed897ed6c64a3491ef1ee3eaaf865c2ff3136c16b83c3379.jpg)

## China Economy

## Domestic Demand Continues to Soften (Cont.)

Auto and online home appliance sales: in line with seasonality sequentially, YoY pressured by a high base

![](images/46cde9a34ffa72fbd0653463a687534150fa6cb2a33e3c9040b2b2c67f5ca422.jpg)  
On the bright side, construction activities seemed to have improved marginally

![](images/ccf79f90dcf7c9ad347b780d18cc5068fd694c51a819b52578d7ea52262989c8.jpg)

## China Economy

## Fiscal Policy: Yet to Catch Up

No clear acceleration in the issuance of government bonds...

![](images/2e73395e647ac08d98487b4e149207f2b893d9d625214f6312d0622e6cfe39b4.jpg)  
...or policy bank bonds in June

![](images/beabb6cc97e14f7514dbb653daa9655b2188a0a2a3b0166c91b8ba46f3fb20a9.jpg)

## China Economy

Monetary Policy: Continued Transition Towards Rate-Based Framework

PBoC enhances liquidity toolkit and reinforces transition to short-rate policy framework

![](images/9c4f5148a8e02bcf1bc8dc24b7118925e7b75b22b0345b32f361dbe9724418ee.jpg)  
Source: CEIC, MS

## Disclosure Section

Information and opinions in MS were prepared or are disseminated by one or more of the following, which accept responsibility for its contents: MS Asia Limited, and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts;

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1800 303-2495; Hong Kong +852 2848-5999; Latin America +1718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61(0)2-9770-1505; Tokyo +81(0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Disclosures

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act. MS does not provide individually tailored investment advice. MS has been prepared without regard to the circumstances and objectives of those who receive it. MS recommends that investors independently evaluate particular investments and strategies, and encourages investors to seek the advice of a financial adviser. The appropriateness of an investment or strategy will depend on an investor's circumstances and objectives. The securities, instruments, or strategies discussed in MS may not be suitable for all investors, and certain investors may not be eligible to purchase or participate in some or all of them. MS is not an offer to buy or sell or the solicitation of an offer to buy or sell any security/instrument or to participate in any particular trading strategy. The value of and income from your investments may vary because of changes in interest rates, foreign exchange rates, default rates, prepayment rates, securities/instruments prices, market indexes, operational or financial conditions of companies or other factors. There may be time limitations on the exercise of options or other rights in securities/instruments transactions. Past performance is not necessarily a guide to future performance. Estimates of future performance are based on assumptions that may not be realized. If provided, and unless otherwise stated, the closing price on the cover page is that of the primary exchange for the subject company's securities/instruments.

The fixed income research analysts, strategists or economists principally responsible for the preparation of MS have received compensation based upon various factors, including quality, accuracy and value of research, firm profitability or revenues (which include fixed income trading and capital markets profitability or revenues), client feedback and competitive factors. Fixed Income Research analysts', strategists' or economists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

With the exception of information regarding MS, MS is based on public information. MS makes every effort to use reliable, comprehensive information, but we make no representation that it is accurate or complete. We have no obligation to tell you when opinions or information in MS change apart from when we intend to discontinue equity research coverage of a subject company. Facts and views presented in MS have not been reviewed by, and may not reflect information known to, professionals in other MS business areas, including investment banking personnel.

MS may make investment decisions that are inconsistent with the recommendations or views in this report.

To our readers based in Taiwan or trading in Taiwan securities/instruments: Information on securities/instruments that trade in Taiwan is distributed by MS Taiwan Limited ("MSTL"). Such information is for your reference only. The reader should independently evaluate the investment risks and is solely responsible for their investment decisions. MS may not be distributed to the public media or quoted or used by the public media without the express written consent of MS. Any non-customer reader within the scope of Article 7-1 of the Taiwan Stock Exchange Recommendation Regulations accessing and/or receiving MS is not permitted to provide MS to any third party (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities regarding MS which may create or give the appearance of creating a conflict of interest. Information on securities/instruments that do not trade in Taiwan is for informational purposes only and is not to be construed as a recommendation or a solicitation to trade in such securities/instruments. MSTL may not execute transactions for clients in these securities/instruments.

MS is not incorporated under PRC law and the research in relation to this report is conducted outside the PRC. MS does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC. PRC investors shall have the relevant qualifications to invest in such securities and shall be responsible for obtaining all relevant approvals, licenses, verifications and/or registrations from the relevant governmental authorities themselves. Neither this report nor any part of it is intended as, or shall constitute, provision of any consultancy or advisory service of securities investment as defined under PRC law. Such information is provided for your reference only.

MS is disseminated in Brazil by MS C.T.V.M. S.A. located at Av. Brigadeiro Faria Lima, 3600, 6th floor, São Paulo - SP, Brazil; and is regulated by the Comissão de Valores Mobiliários; in Mexico by MS México, Casa de Bolsa, S.A. de C.V which is regulated by Comision Nacional Bancaria y de Valores. Paseo de los Tamarindos 90, Torre 1, Col. Bosques de las Lomas Floor 29, 05120 Mexico City; in Japan by MS MUFG Securities Co., Ltd. and, for Commodities related research reports only, MS Capital Group Japan Co., Ltd; in Hong Kong by MS Asia Limited (which accepts responsibility for its contents) and by MS Bank Asia Limited; in Singapore by MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS) and by MS Bank Asia Limited, Singapore Branch (Registration number T14FC0118); in Australia to "wholesale clients" within the meaning of the Australian Corporations Act by MS Australia Limited A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents; in Australia to "wholesale clients" and "retail clients" within the meaning of the Australian Corporations Act by MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
