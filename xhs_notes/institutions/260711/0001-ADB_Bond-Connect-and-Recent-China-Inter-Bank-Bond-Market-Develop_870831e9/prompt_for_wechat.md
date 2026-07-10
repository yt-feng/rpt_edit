你是麦肯锡/研究导读风格的微信公众号文章主笔，擅长用金字塔原理把报告内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给专业读者/产业决策者的报告导读。
- 长度：约 1200 字，整体以短导读为主，通常控制在 900-1200 个中文字符。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，只讲最关键的判断、图表和未解问题，让读者有动力去看原文。
- 文章必须像人工编辑润色过的报告导读：句长有变化，段落有呼吸感，不要整齐排比，不要反复使用“这意味着/真正重要的是/换句话说/从这个角度看”等模板转折。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、市场定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须短、锐利、可转发，优先 20-35 个中文字符，最长不超过 35 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 要兼顾微信搜一搜：尽量包含一个高意图关键词，例如行业/公司/政策/AI/房地产/半导体/光伏/消费/美联储/利率/通胀/机器人/比特币等。
- `# 标题` 和正文不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
- 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达；不要写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`亚洲开发银行`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
- 标题禁止出现 GS、JPM、JEF、NOM、BARC、MS、DB、Citi、Ticker、文件编号；如果原文只有英文机构名，请翻译为中文机构名。
- 标题冒号后不要重复机构或来源类型，禁止“联合国贸发会议：联合国贸发报告，……”“麦肯锡：麦肯锡报告称，……”这类写法；冒号后直接写判断或变量。
- 标题只能保留一层信息，不要把多个长分句全部塞进标题；如果原始标题有三段以上信息，只取最有传播性的主判断，其余放在正文第一段自然展开。
- 如果报告是单一公司/个股报告，标题和正文只能写公司情况、行业变化、业务进展、竞争格局和报告里的事实；禁止出现目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等任何卖方操作口径。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 观察提示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，20-35 个中文字符。
2. 开头 2-3 段：直接给出主判断、为什么现在重要、报告提供了什么新信号；自然带出 4-6 个长尾关键词，覆盖国家/行业/公司/政策/数据/技术词，但不要写成关键词堆砌。
3. 3-4 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 1-2 个 `> **KC评论：** ...` 引用块，每个 1-2 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，不要夹带任何推广话术。
5. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许出现分析正文、图表占位和 `KC评论`。
6. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
7. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
8. 不要写任何 CTA、广告、扫码、社群、知识星球、网站、域名或关注引导；系统会在最结尾统一插入固定信息。
9. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
10. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.</p>`

【CTA 要求】
- 不要输出任何 CTA。不要写“加入社群”“扫码”“星球”“完整报告领取”“网站”“域名”“关注”“星标”“更多查看”等表达。
- 文末也不要写 CTA；系统会在最结尾统一插入固定信息。
- 正文中间不要出现“如果你从某些关键词搜到这里”“单篇文章只能解决一个切片”“我每天会把……”“这篇可以沿着……”这类表达。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。
- `KC评论` 里禁止夹带 CTA，不要写扫码、社群、知识星球、每日汇编、喂给 AI、市场主线、完整报告领取等表达；它只能做解释、提醒或追问。

【人工编辑感要求】
- 段落不要像 AI 摘要清单。每段只推进一个意思，必要时用短句收住。
- 不要展开成完整长文。每个小节只保留最有信息量的一段，细节留给原文和图表。
- 避免连续使用同一种句式开头，避免连续三段都是“报告指出/这意味着/真正重要的是”。
- 不要机械重复标题、机构名或同一句判断。标题已经写过的内容，正文第一段要换一种说法展开。
- 保留一点自然语气，但不要口水化；像一个认真读过报告的人在做导读。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 单公司报告不能写成交易提示；不要输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO，也不要保留这些英文/中文卖方评级词。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份亚洲开发银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# ASIAN BOND MARKETS INITIATIVE BRIEF No. 16

# BOND CONNECT AND RECENT CHINA INTER-BANK BOND MARKET DEVELOPMENTS

JULY 2026

## About This Brief

The ASEAN+3 Bond Market Forum (ABMF), convened under the Asian Bond Markets Initiative (ABMI), is a platform for public and private sector institutions to support the development of local currency bond markets; analyze and discuss market trends; facilitate policy dialogue and recommendations, including on digitalization and data transformation; and address challenges common to all market stakeholders. The Asian Development Bank acts as secretariat to both ABMF and the ABMI. $^{1}$

As part of its mandate, ABMF compiles the ASEAN+3 Bond Market Guides and offers knowledge sharing through other publications, including the ABMI Brief series.

The ABMI Brief series provides insights into bond markets, their development, and necessary or desirable components to issuers, investors, market intermediaries, regulatory authorities and policymakers, academia, and other interested parties. Individual briefs are dedicated to specific subjects discussed in ABMF given their relevance for domestic bond markets.

Central to the work of ABMF and its publications has been explaining regional market features and functions, highlighting the use of standards, and addressing the misperceptions that continue to exist in relation to ASEAN+3 bond or capital markets, such as on investor protection or market access. Bond Connect is a good example of practical market access and, increasingly,

## KEY TAKEAWAYS

Bond Connect represents a link between the established bond market infrastructures of the China Inter-Bank Bond Market and the Hong Kong bond market.

Participating investors can conduct bond trades and foreign exchange transactions with their existing trading platforms and use their existing custody structure and service arrangements, settling trades through the Hong Kong bond market's infrastructure and custodians. Concurrently, it satisfies the look-through management requirements of the People's Republic of China's onshore regulatory authorities.

Since its inception in 2017, Bond Connect has developed into a comprehensive cross-border ecosystem, offering risk management tools via Swap Connect and FX Services.

Significantly, Bond Connect now also allows regional and other international investors to participate in the People's Republic of China's onshore RMB repo business under international practices, as well as conduct offshore repo in RMB and also EUR, HKD, and USD in the Hong Kong bond market using bonds held by participating institutions under Northbound Bond Connect.

By providing regional and other international investors with easier access from one jurisdiction to another through the connection of financial infrastructures and a streamlined onboarding and registration process, Bond Connect represents an example of regional financial integration within ASEAN+3.

the adoption of international standards and best practices. At the same time, Bond Connect, by allowing easy cross-border access to eligible investors, represents a practical form of regional financial integration within ASEAN+3.

This brief explains the Bond Connect model, which seeks to link the investors, participants, and infrastructure of the China Inter-Bank Bond Market (CIBM) with the Hong Kong bond market.

## Introduction

The bond market in the People's Republic of China (PRC) is divided into three market segments:

(i) CIBM,

(ii) exchange bond market, and

(iii) commercial banks' counter market.

Considering the scale of these market segments, the CIBM and the exchange bond market are the dominant segments; some of their key characteristics are described in Table 1.

Table 1: Major Bond Market Segments in the People's Republic of China

<table><tr><td>Characteristic</td><td>Inter-Bank Bond Market (over-the-counter market)</td><td>Exchange Bond Market</td></tr><tr><td>Market share</td><td>88%</td><td>12%</td></tr><tr><td>Main regulator</td><td>People&#x27;s Bank of China</td><td>China Securities Regulatory Commission</td></tr><tr><td>Available debt securities or Debt financing instruments</td><td>CCDC only: government bonds, local government bonds, central bank bills, enterprise bonds, collective bonds, financial bonds (commercial bank bonds)SHCH only: medium-term notes, commercial paper, super-short-term commercial paper, private placement notes, SME collective notes, asset-backed notes, project revenue notes; Panda bonds, green debt financing tools, project income notes, SDR-denominated bonds; negotiable certificates of depositCCDC and SHCH: policy bank financial bonds, financial bonds (non-bank financial institution bonds), government-backed (agency) bonds; asset-backed securities; repurchase agreements</td><td>Government bonds, local government bonds, policy bank financial bonds, government-backed (agency) bonds (e.g., railway bonds), enterprise bonds, securities company bonds and short-term notes, corporate bonds and exchangeable corporate bonds, convertible bonds, asset-backed securities, repurchase agreements</td></tr><tr><td>Key investors</td><td>Institutional investors (e.g., international central banks, international financial organizations, sovereign wealth funds, banks, funds, insurance companies, rural credit cooperatives, securities companies, financial companies, enterprises, international institutions, QFII, RQFII, and QOII)</td><td>Small and medium-sized institutional investors (e.g., securities companies, insurance companies, funds, financial companies, qualified individual investors, enterprises); banks (only auction trading is permitted); QFII and RQFII; individuals (very limited)</td></tr></table>

CCDC = China Central Depository & Clearing Co., Ltd.; QFII = Qualified Foreign Institutional Investor; QOII = Qualified Overseas Institutional Investor; RQFII = Renminbi Qualified Foreign Institutional Investor; SME = small and medium-sized enterprise; SHCH = Shanghai Clearing House; SDR = Special Drawing Rights.  
Note: Market share data as of February 2026.  
Sources: People's Bank of China. Bond Connect Company Limited.  
https://www.pbc.gov.cn/goutongjiaoliu/113456/113469/2026021010061536132/index.html.

The CIBM and, particularly, access to it through Bond Connect is the focus of this brief. $^{2}$

## China Inter-Bank Bond Market

The CIBM represents the over-the-counter (OTC) market and is the largest of the three market segments. The CIBM is mainly regulated by the People's Bank of China (PBOC) and offers distinct features and practices, including the use of dedicated terminology. As of December 2025, the CIBM's outstanding balance of all debt financial instruments—the summary term used to describe eligible instruments—stood at CNY3.46 trillion (equivalent to approximately USD492 billion). $^{3}$

Comprehensive descriptions of the CIBM as well as of the PRC's exchange bond market are available in the respective ASEAN+3 Bond Market Guides, while this brief also discusses the latest updates for investors accessing the CIBM via Bond Connect (Northbound). $^{4}$

## Bond Connect

Bond Connect is an access method to the CIBM in addition, or as an alternative, to the Qualified Foreign Institutional Investor (QFII) and CIBM Direct investment avenues. A comparison of these access methods is provided in the Appendix.

Bond Connect was established in July 2017. As part of the opening-up policy of the PRC, the PBOC issued the interim measures for the administration of mutual bond market access between the PRC and Hong Kong, China (formally 内地与香港债券市场互联互通合作管理暂

行办法) (中国人民銀行令 [2017] 第 1 号). It allows overseas investors to access the CIBM without quota restrictions and through their established offshore operational protocols for trading and settlement, rather than requiring adaptation to domestic procedures.

Bond Connect is available for investment in the CIBM, a pathway officially known as Northbound Bond Connect, while Bond Connect Southbound enables institutional investors in the PRC to access the Hong Kong bond market through a direct link between

## ASEAN+3 Bond Market Forum

The ASEAN+3 Bond Market Forum (ABMF) was established in 2010 under the Asian Bond Markets Initiative by the ASEAN+3 Finance Ministers, with a mandate to support the development of regional local currency bond markets. Since then, ABMF has acted as a platform for dialogue among public and private sector stakeholders in regional bond markets and promoted the exchange and evaluation of ideas among finance ministries, central banks, securities regulators, securities exchanges, depositories, custodian banks, underwriters, and other market intermediary organizations. ABMF discussion outcomes have helped to address common issues and formulate policy recommendations.

The Asian Development Bank publishes the ASEAN+3 Bond Market Guide series, which ABMF created and updates for interested parties. The economy-level bond market guides serve as reference materials to learn more about the development of individual regional markets, help address misperceptions, and disseminate regional bond market information to a broader audience. ABMF has proposed, agreed on, and helped implement the ASEAN+3 Multi-Currency Bond Issuance Framework as a practical initiative to harmonize the professional bond markets in ASEAN+3 member economies.

financial infrastructure institutions. Bond Connect Southbound officially commenced operation in 2021.

Northbound Bond Connect investors can trade all cash bonds in the CIBM, the same as with onshore investors, as well as foreign exchange (FX) and some hedging products; they can also conduct repurchase agreement (repo) transactions in line with international standards. Details about these transactions are explained in later sections.

![](images/80996b321b1ca07837d56b9b2f6d974da3f8cec489b935d941150bdde0cbf42d.jpg)  
BC = Bond Connect; CCDC = China Central Depository & Clearing Co., Ltd.; CFETS = China Foreign Exchange Trade System; CMU = Central Moneymarkets Unit; SHCH = Shanghai Clearing House.
Source: Bond Connect Company Limited.

The focus of this brief is how the Bond Connect scheme enables international investors to participate in the CIBM using the Northbound path.

## Bond Connect Company Limited

Bond Connect Company Limited (BCCL) is a joint venture between China Foreign Exchange Trade System (CFETS) and Hong Kong Exchanges and Clearing; it is an authorized Automated Trading Services provider supervised by the Securities and Futures Commission of the Hong Kong Special Administrative Region of the PRC.

BCCL was established in Hong Kong, China to support investment in the China bond market via established Hong Kong bond market infrastructures and market intermediaries. BCCL acts as a service provider to eligible international investors who utilize Northbound Bond Connect, facilitating easier access to the China bond market.

## How Does Northbound Bond Connect Work?

Northbound Bond Connect allows international investors with an account in the Hong Kong bond market to invest in the CIBM and use its market features without the need to appoint domestic intermediaries. Concurrently, it satisfies the look-through disclosure requirements of the PRC's regulatory authorities.

Figure 1 illustrates the trading and settlement workflow of Northbound Bond Connect, which is characterized by the four main features described below.

## Investor Access

Northbound Bond Connect provides access to all CIBM cash bonds—including government bonds, policy financial bonds, and credit bonds—thereby satisfying most global institutional investors. There is no quota restriction on both the overall investment amount through Bond Connect and the individual transaction size. Eligible investors include central banks, sovereign wealth funds, international asset managers, pension funds, commercial banks, insurance companies, hedge funds, and other investors recognized by the PBOC.

## Use of Existing Trading Platforms

International investors can trade bonds in the CIBM through familiar interfaces using one or a combination of three established global trading platforms: Bloomberg, MarketAxess, and Tradeweb. These platforms connect directly to the CFETS system, the official trading venue for the CIBM designated by the PBOC. On CFETS, 60 onshore market makers, including branches or subsidiaries of foreign commercial banks and securities firms, are available to execute transactions. $^{5}$

![](images/f1d0863cac7709b1bbb74928e826f9c502f543f79c4b811b356110d8933e5d79.jpg)  
BCCL = Bond Connect Company Limited, CFETS = China Foreign Exchange Trade System, PBOC = People's Bank of China. Source: Bond Connect Company Limited.

## Familiar Settlement and Safekeeping

At the same time, Bond Connect allows investors to appoint their habitual service providers—a global custodian or a domestic custodian based in Hong Kong, China—to facilitate settlement. Trades routed through Bond Connect are settled using the real-time delivery-versus-payment method with cash settlement in Chinese renminbi through the Cross-Border Interbank Payment System. Overseas participants have the flexibility to determine their settlement cycle, with options ranging from T+0 to T+N. $^{6}$

Transfers of bonds are processed through the registration systems of the central securities depositories servicing the CIBM, the China Central Depository (CCDC), and Shanghai Clearing House (SHCH), which each cover specific market segments, products, and instrument types. The Central Moneymarkets Unit (CMU) maintains nominee accounts with both CCDC and SHCH, and bonds acquired by international investors via Bond Connect are registered under these accounts. In turn, the CMU maintains records of individual ownership of the bonds through participant accounts.

BCCL as a One-Stop Service Provider BCCL acts as the one-stop service provider within the cross-border ecosystem, supporting the onboarding process to Bond Connect and providing centralized information regarding the operational requirements for overseas investors in the CIBM.

Its key functions are (i) providing support to Northbound investors for admission to and registration with Bond Connect, Swap Connect, and relevant repo business; (ii) marketing and providing information on Bond Connect for both Northbound and Southbound participants; and (iii) liaising with the international trading platforms that are connected to CFETS.

BCCL offers investors a streamlined onboarding experience, as a conduit, guiding them through the onboarding process or the registration of onshore products. At the same time, BCCL regularly gathers feedback and opinions from the international investment community for potential mechanism enhancement.

## How to Participate in Bond Connect?

Looking at the practical aspects, gaining access to the CIBM via Bond Connect can be achieved through following the streamlined steps detailed in Figure 2.

1. Obtaining regulatory approval. Investors submit applications to BCCL, which assists in obtaining the filing notice from the PBOC at the entity level and then proceeds to process trading account applications with CFETS.

2. Enabling trading relationship. Investors sign up with one or more recognized trading access platforms—Tradeweb, Bloomberg, or MarketAxess—if not already connected.

3. Appoint a custodian. If not already in a service arrangement, investors approach a global custodian or a domestic custodian in Hong Kong, China to open a securities subaccount within the CMU system.

4. Establish a counterparty relationship. Investors need to establish a counterparty relationship with at least one of the CIBM market makers to enable trading.

For large and experienced international investors with existing global custody service arrangements or an established network of direct custody relationships that include the Hong Kong bond market, investing in the CIBM through Bond Connect will appear as merely “switching on” a new market. $^{7}$

While the timeframe may vary on a case-by-case basis, it generally takes 2–6 weeks for an international investor to be ready for trading.

## Key Market Features and Recent Market Developments

Table 2 provides an overview of the different access paths for international investors to the CIBM and some of their inherent key features; the different paths are illustrated in detail in the Appendix. $^{8}$

Table 2: Overview of Access Paths to the China Inter-Bank Bond Market and Their Available Features

<table><tr><td></td><td>(Northbound) Bond Connect</td><td>CIBM Direct</td></tr><tr><td>CIBM cash bonds</td><td>√</td><td>√</td></tr><tr><td>FX Services (Enhanced Currency Conversion Arrangement under Northbound Bond Connect)</td><td>√</td><td>NA</td></tr><tr><td>Swap Connect</td><td>√</td><td>√</td></tr><tr><td>Bond lending, bond forwards, and forward rate agreements</td><td>NA</td><td>√</td></tr><tr><td>Offshore RMB Bond Repo</td><td>√</td><td>NA</td></tr><tr><td>Cross-Boundary Bond Repo</td><td>√</td><td>√</td></tr><tr><td>Primary Market Subscription (ePrime Northbound)</td><td>√</td><td>√</td></tr><tr><td>Use of CIBM Bonds as Collateral at OTC Clear</td><td>√</td><td>NA</td></tr><tr><td>Treasury Bond Futures (on China Financial Futures Exchange)</td><td>NA</td><td>NA</td></tr></table>

CIBM = China Inter-Bank Bond Market, FX = foreign exchange, NA = not applicable, OTC = over-the-counter, QFII = Qualified Foreign Institutional Investor, RMB = Chinese renminbi (domestic designation), RQFII = Renminbi Qualified Foreign Institutional Investor. Source: Bond Connect Company Limited.

Since inception, the strong commitment of regulators in the PRC and Hong Kong, China has helped develop Bond Connect into a comprehensive cross-border ecosystem. From a straightforward market access option in 2017, Bond Connect now offers, among other features, access to hedging or risk management tools via Swap Connect and FX Services and, since 2025, has allowed overseas investors to participate in the onshore repo business in the CIBM, albeit under international standard repo practices; details are explained below.

## FX Services

FX Services allow Bond Connect investors to access CNY-denominated FX products—including spot, forwards, swaps, cross-currency swaps, and options—through up to three designated FX settlement banks based in Hong Kong, China. $^{9}$

Investors may appoint one primary and up to two general settlement banks. While all provide pricing and execution, only the primary settlement bank is authorized to settle Northbound transactions within the CMU system. To utilize these services, investors must either have in place or open CNY-denominat

[中间内容因长度限制已省略]

gements, allowing for operational compatibility, is complemented by safekeeping of the CIBM bonds through an account with CMU, which reduces settlement and counterparty risk.

Recent developments such as the ability for foreign investors in the CIBM to participate in repo business—specifically, the title-transfer type repo in contrast to the pledge repo type traded among onshore investors—and utilize hedging instruments, coupled with the adoption of international standards and practices, make the access to the CIBM via Bond Connect more attractive.

## Inclusion into Major Bond Indices

The accessibility of the CIBM through Bond Connect, using established trading and settlement arrangements in line with international expectations, supported the inclusion of CGBs into three major global indices, which in turn contributed to passive capital inflows.

Sources: Asian Development Bank. 2020. The Inter-Bank Bond Market in the People's Republic of China: An ASEAN+3 Bond Market Guide. Manila; People's Bank of China; Bond Connect Company Limited; and CSRC.

Specifically, the Bloomberg Barclays Global Aggregate Index began phasing in CGBs and policy bank bonds in April 2019. Subsequently, the J.P. Morgan GBI-EM Global Diversified Index added CGBs to its basket starting in February 2020, followed by the FTSE World Government Bond Index, which commenced the inclusion of CGBs in October 2021.

## The Road Ahead

BCCL activities are closely aligned with the policy direction set by the PBOC in promoting the high-level opening-up of the China bond market. In 2025, the PBOC identified four priorities: $^{18}$

1. advancing RMB bonds as High-Quality Liquid Assets,

2. enhancing cross-border connectivity between onshore and offshore infrastructures,

3. enriching risk management tools for international investors, and

4. further facilitating the investment and financing environment in the RMB bond market.

To support these goals, BCCL will continue to implement regulatory initiatives with execution details that reflect market practice and investor needs, provide clear and accurate guidance to investors accessing the China bond market, and maintain effective communication channels to keep stakeholders informed of policy developments.

Ongoing dialogue with investors will remain central, ensuring their feedback informs proposals to regulators and continues to provide potential reference cases for regional financial integration.

Appendix

Access Schemes to the China Inter-Bank Bond Market

<table><tr><td>Characteristic</td><td>QFII and RQFII</td><td>CIBM Direct</td><td>Northbound Bond Connect</td></tr><tr><td>Market</td><td>Exchange Market and CIBM</td><td>CIBM</td><td>CIBM</td></tr><tr><td>Commenced</td><td>2002 and 2011</td><td>2016</td><td>2017</td></tr><tr><td>Currency</td><td>CNY (RMB)</td><td>CNY (RMB), FCY</td><td>CNY (RMB), FCY</td></tr><tr><td>Approving Authorities</td><td>CSRC, SAFE; CSRC, SAFE, PBOC</td><td>PBOC and SAFE</td><td>PBOC</td></tr><tr><td>Description</td><td>Allows eligible international institutional investors to invest directly (using either foreign currency or CNY) in equities, bonds, and other products in domestic markets</td><td>International investors sign agency agreements and complete registration with onshore regulators. They can open onshore cash accounts and trade and clear through intermediaries in the CIBM.</td><td>International investors can participate in the CIBM with electronic trading platforms, multi-level custody, and one-stop access.</td></tr><tr><td>Holding Structure</td><td>Direct custody</td><td>Direct custody</td><td>Nominee account via CMU</td></tr><tr><td>Custody structure</td><td>Onshore and Offshore</td><td>Onshore</td><td>Offshore</td></tr></table>

CIBM = China Inter-Bank Bond Market, CMU = Central Moneymarkets Unit, CNY = Chinese renminbi (ISO code), CSRC = China Securities Regulatory Commission, FCY = foreign currency, PBOC = People's Bank of China, QFII = Qualified Foreign Institutional Investor, RMB = Chinese renminbi (domestic designation), RQFII = Renminbi Qualified Foreign Institutional Investor, SAFE = State Administration of Foreign Exchange.

## About the Asian Development Bank

ADB is a leading multilateral development bank supporting inclusive, resilient, and sustainable growth across Asia and the Pacific. Working with its members and partners to solve complex challenges together, ADB harnesses innovative financial tools and strategic partnerships to transform lives, build quality infrastructure, and safeguard our planet. Founded in 1966, ADB is owned by 69 members—50 from the region.

![](images/9329df16069f5498cd7fd352892c91587923f0754f0d20021bf7d2c2e377b99e.jpg)

Creative Commons Attribution 3.0 IGO license (CC BY 3.0 IGO)

ISBN 978-92-9277-875-0 (print)

ISBN 978-92-9277-876-7 (PDF)

Publication Stock No. BRF260318-2

DOI: http://dx.doi.org/10.22617/BRF260318-2

© 2026 Asian Development Bank. The CC license does not apply to non-ADB copyright materials in this publication.

Note: ADB recognizes “China” as the People’s Republic of China and “Hong Kong” as Hong Kong, China.

The views expressed in this publication are those of the authors and do not necessarily reflect the views and policies of ADB or its Board of Governors or the governments they represent. ADB does not guarantee the accuracy of the data included here and accepts no responsibility for any consequence of their use.

By making any designation of or reference to a particular territory or geographic area in this document, ADB does not intend to make any judgments as to the legal or other status of any territory or area.

https://www.adb.org/terms-use#openaccess
http://www.adb.org/publications/corrigenda
"""
