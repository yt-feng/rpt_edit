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
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

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
## China Financials | Asia Pacific

# Recent outbound investment policies: gauging the true impact

We believe the new State Council outbound investment rules are aimed at protecting outbound business investments rather than focusing on household financial investments. Enforcement of investment account services for mainland residents is about proper licensing requirement.

New State Council regulation on outbound investments is aimed at formal legislative process to protect Chinese overseas business investments rather than aiming at household financial investments: First, during the State Council press conference announcing the new rules, only the Ministry of Justice, the NDRC.and the Ministry of Commerce were present – none of the financial regulators were involved. We view that as a clear sign that it is a policy that targets Chinese overseas investment in real businesses or large stakes in overseas companies rather than normal financial investments by households. With China's outbound investments rising, we believe the goal is to set up a centralized legislative framework to systematically protect Chinese outbound investments and long-term businesses interests and replace the various prior regulations. China's financial firms are also increasing support for expansion of Chinese overseas investment; this should help contain long-term financial risks, in our view.

## We think the CSRC is focusing on cleanup of cross-border stock trading happening onshore – the insurance business already went through similar

changes many years ago: We do not believe this is linked to the new State Council Outbound investment rules. Under the current enforcement standards, residents of mainland China can continue to open and operate their investment accounts while physically in Hong Kong, but can no longer access key online investment functions while in mainland China – essentially the same standards that apply to insurance businesses. This is echoed by the HK SFCs' circular and clarification. We also see limited risks to the annual quota of US\$50,000 FX exchange for households. Based on financial data that we track, we also believe household capital outflows remain in a reasonable range and are not a key concern behind these new rules. That said, we believe data exchange via CRS to the onshore tax authority over mainland residents' overseas investment activities will continue, which is not new and not related to these new developments.

Concerns about AIA, HSBC, and Standard Chartered look overdone; HKEX will remain a long-term beneficiary of expanding formal capital connect channels between the mainland and Hong Kong: We believe tech and industrial upgrades will continue to help Chinese companies gain global market share and generate wealth in overseas markets. Together with legal capital account flow from mainland China, this should continue to drive healthy business growth for major financial firms in Hong Kong.

MS ASIA LIMITED+

## Richard Xu, CFA

Equity Analyst

Richard.Xu@morganstanley.com +852 2848-6729

## Chiyao Huang

Equity Analyst

Chiyao.Huang@morganstanley.com +852 3963-4624

## Rick Zhao

Equity Analyst

Rick.Zhao@morganstanley.com +852 2239-7033

MS ASIA (SINGAPORE) PTE.+

## Nick Lord

Equity Analyst

Nick.Lord@morganstanley.com +65 6834-6746

MS EUROPE S.E., MADRID BRANCH+

## Alvaro Serrano

Equity Analyst

Alvaro.Serrano@morganstanley.com +44 20 7425-6942

MS ASIA LIMITED+

## Beryl Yang

Research Associate

Beryl.Yang@morganstanley.com +852 3963-2224

## Chenqian Liu

Research Associate

Chenqian.Liu@morganstanley.com +852 3963-0359

MS ASIA (SINGAPORE) PTE.+

## Aitong Li

Research Associate

Aitong.Li@morganstanley.com +65 6834-6295

![](images/19b9b1eed367df743cdc6535c63f6de816bec02e961fbfb98514ceb37ee7ebb6.jpg)

<details>
<summary>text_image</summary>

Asia Summer School 2026
</details>

## The quick brown fox jumps over the lazy dog.

## CHINA FINANCIALS

Asia Pacific

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

## For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

# Outbound Investment Regulation: More About the Real Economy Going Global Than Household Capital Flight

We think the new State Council Regulation is primarily an institutional framework for the real economy's outbound investment, not a broad tightening of household financial investment or a reversal of capital account opening.

The regulation defines outbound investment as obtaining ownership, control, operating-management rights or other interests in overseas enterprises/assets through assets, equity, financing, or guarantees. It also repeatedly frames the policy around high-quality opening-up, Belt and Road, overseas risk management, investor protection, and cross-border operating compliance.

In fact, the during the State Council press conference announcing the new rules, only the Ministry of Justice, the NDRC and the Ministry of Commerce were present. None of the financial regulators were involved.

Also, the new rules are categorized as commerce, customs, travel, and foreign economic cooperation under the State Council document categories.

That being said, we think financial firms, which are increasingly supporting expansion of China's overseas investment, will also benefit from systematic guardrails to protect outbound investments because they can contain long-term financial risks associated with these investments.

## State Council regulation – key focus area is real investment, not financial investment

The core policy architecture is centered on Outbound Direct Investment (ODI)/real investment. The regulation supports market-based outbound investment, investor autonomy, and overseas service systems covering legal, fiscal/tax, financial, trade, logistics, immigration, customs, and trade promotion resources. Importantly, the main policymaking and enforcement roles are assigned to the State Council's investment and commerce authorities, while financial regulators are not the lead drafters/enforcers in this State Council regulation. In fact, financial matters such as FX conversion, cross-border services, data, tax, SOE supervision and others are left to existing laws and rules.

This is why we do not read the document as evidence of immediate “capital flight control.” This is in line with our macro team's view – the report Why China Is Rewiring Outbound Investment explicitly states that “it’s not about stopping capital flight,” arguing that China’s balance of payments has shifted into a “mirror image” structure, in which a large current account surplus is increasingly recycled into overseas assets by non-official actors rather than accumulated as PBOC FX reserves.

## Rationale behind the State Council Regulation: addressing geopolitical, country risk, and competitiveness framework as companies are going global

The more important policy signal is that policymakers would like Chinese enterprises to go global in a safer, more organized and more strategically controlled way.

Article 4 of the State Council regulation explicitly refers to aligning with high-standard international trade rules, promoting high-quality Belt and Road cooperation, building multilateral/bilateral investment cooperation mechanisms, participating in international investment-rule formulation, and supporting industrial chain/supply chain cooperation.

## We think one of the main considerations in establishing this framework is to help companies better assess the foreign operating environment and potential uncertainties related to geopolitics.

The regulation also emphasizes national security review, overseas safety/risk alerts, dispute resolution, protection of Chinese citizens and enterprises overseas, and countermeasures against discriminatory foreign restrictions.

The government will also have much greater bargaining power than individual companies when negotiating more favorable terms with foreign governments over trade and investments.

## Formalizing current regulation via a legislative process

With China's rising outbound investments, we believe the goal is to set up a centralized legislation framework to systematically protect China's outbound investments and long-term businesses interests and replace the various prior regulations. This is also an effort to improve the regulatory process, which is also evidenced in the consultation paper on China's Financial Law that provides an overarching legal framework on all financial activities in China.

## We don't see much read-across to outbound financial activities

Retail outbound investment is briefly mentioned, but clearly not the core of this policy. It appears only at the end of the regulation – Article 33 says that investments in overseas financial markets using own funds, raised funds, or other entrusted funds shall be governed by this regulation and other national rules, and that detailed rules for resident individuals' outbound investment will be formulated by the State Council's investment and commerce authorities. This indicates that retail/portfolio investment is acknowledged but not the center of the document.

## It's improper to frame this regulation as prompted by capital outflow pressures – the data simply don't support that

Our tracking of household data also does not support outsized capital outflow – household financial asset growth remained above 10%, but household income increased only 4-5%. An outsized capital outflow from households would imply much higher income growth than 4-5% given still robust household financial asset growth, which we view as questionable.

Our channel checks with banks indicated that they generally saw good capital inflow and abundant liquidity from more FX settlement as RMB appreciated. PBOC liquidity withdrawal over recent months also provides evidence that policymakers have no intention to control capital outflow amid healthy FX inflows and RMB appreciation.

Exhibit 1: Household financial asset growth remained above 10%...  
![](images/c3370dcee93ba13c915284e8994a7d63f68e2a8eef42ffe498eca3245852ae85.jpg)

<details>
<summary>bar-line hybrid</summary>

China household financial assets, Rmb bn
| Year | Total Household Financial Assets (Rmb bn) | 10-year CAGR (%) |
| :--- | :--- | :--- |
| 2014 | 95,000 | |
| 2015 | 115,000 | 20.5 |
| 2016 | 130,000 | 8.5 |
| 2017 | 145,000 | 12.5 |
| 2018 | 145,000 | 3.5 |
| 2019 | 165,000 | 13.5 |
| 2020 | 190,000 | 16.5 |
| 2021 | 215,000 | 13.5 |
| 2022 | 230,000 | 7.5 |
| 2023 | 250,000 | 11.5 |
| 2024 | 280,000 | 13.5 |
| 2025 | 315,000 | 13.5 |
| 1Q26 | 325,000 | 11.5 |
</details>

Source: CEIC, WIND, PBOC, SSE, Trust Association, AMAC, NFRA, China Bank Association, MS

Exhibit 2: ...but household income increased only 4-5% in 2023-2025  
![](images/1509b03d7cf00de7bc3ff85f069de2ce7bc3c57f264c5e5145d979a1315d3a6c.jpg)

<details>
<summary>line chart</summary>

| Year | Adjusted HH disposable income, ex. Equity portion | HH financial assets (Rmb bn) |
|------|--------------------------------------------------|------------------------------|
| 2020 | 9.0%                                             | 16.0%                        |
| 2021 | 11.0%                                            | 12.0%                        |
| 2022 | -3.0%                                            | 7.0%                         |
| 2023 | 5.0%                                             | 9.0%                         |
| 2024 | 4.0%                                             | 12.0%                        |
| 2025 | 4.0%                                             | 12.0%                        |
</details>

Source: CEIC, WIND, PBOC, SSE, Trust Association, AMAC, NFRA, China Bank Association, MS

Exhibit 3:
The PBOC withdrew liquidity over the past three months  
![](images/767bb506d01b14856a892cb10b43cf369143df57b774f1968f27d65d335d8085.jpg)

<details>
<summary>stacked bar chart</summary>

Monthly PBoC Liquidity Injection/(withdrawal), Rmb mn
| Month | Treasury bond net purchase (Rmb mn) | MLF net injection/(withdrawal) (Rmb mn) | SLF net injection/(withdrawal) (Rmb mn) | Ourright reverse repo net (Rmb mn) | 7-day reverse repo (Rmb mn) |
|---|---|---|---|---|---|
| 1/2025 | - | - | - | 1,680,000 | -1,450,000 |
| 2/2025 | - | -300,000 | - | 550,000 | 1,250,000 |
| 3/2025 | - | - | - | 100,000 | -350,000 |
| 4/2025 | - | 450,000 | - | -550,000 | 750,000 |
| 5/2025 | - | 350,000 | - | -250,000 | - |
| 6/2025 | - | 150,000 | - | 250,000 | 750,000 |
| 7/2025 | - | 150,000 | - | 250,000 | 350,000 |
| 8/2025 | - | 250,000 | - | 450,000 | -150,000 |
| 9/2025 | - | 250,000 | - | 450,000 | -550,000 |
| 10/2025 | - | 250,000 | - | 450,000 | 850,000 |
| 11/2025 | - | 150,000 | - | 650,000 | -650,000 |
| 12/2025 | - | 150,000 | - | 350,000 | 350,000 |
| 1/2026 | 15,000 | 75,000 | 15,000 | 35,000 | 35,000 |
| 2/2026 | -15,000 | 35,000 | 15,000 | 75,000 | -15,000 |
| 3/2026 | -1,35,000 | 15,000 | 15,000 | 15,000 | -1,35,000 |
| 4/2026 | -1,35,000 | 15,000 | 15,000 | 35,000 | -75,000 |
| 5/2026 | -1,35,000 | 15,000 | 15,000 | -1,35,000 | 45,75,75 |
</details>

Source: PBOC, CEIC, MS

# The CSRC's recent cleanup of cross-border stock trade: the focus is on activities taking place onshore

In a nutshell, what will be affected: Mainland investors directly trading overseas stocks from onshore – this will no longer be allowed.

What will not be affected: Opening investment accounts, bank accounts, trading, or buying insurance when physically taking place offshore.

The CSRC led the Notice on the Implementation Scheme for the Comprehensive Rectification of Illegal Cross-Border Securities, Futures, and Fund Business Activities on 22 May. That plan aims to stop offshore institutions illegally conducting securities brokerage business in mainland China, including apps and social media accounts providing marketing, account-opening guidance or trading services to onshore investors. It sets a two-year rectification period:

- During the period, offshore institutions are prohibited from providing new buy trades or fund-in services to existing onshore investors in China, while sell trades and fund-out are allowed.  
- After the rectification period, illegal onshore websites, trading software, and supporting servers should be fully shut down.

Though it's a continuation of the cross-border tightening in 2022, we think the bigger picture is the deliberation of Financial Law, which underwent a consultation phase in March 2026.

Effectively, we think regulators and lawmakers are trying to set up a comprehensive legal framework to ensure that all financial activities are properly regulated and licensed....

...which is good for long term risk prevention.

## The targeted area is very clear: onshore activities

Based on its Notice, we think the CSRC aims to clean up cross-border stock trading that is physically taking place onshore. The rationale is straightforward:

1. There is no such license in Mainland China that would allow brokers to offer direct overseas stock trading (except for via Stock Connect) to onshore investors.  
2. Foreign brokers without local license are not allowed to solicit or serve clients from onshore – these are regulated activities.

However, contrary to some market concerns, the regulator has never indicated that the goal is to force closure of mainland investors' investment accounts overseas – this has been confirmed by a report from a PBOC-affiliated medium, the Financial Times.

Regarding the HK SFC's circular on 22 May, it clearly stated that forced account closure will be applied only to fraudulent accounts – those using forged documents or dormant accounts. We think this is justified by anti-money laundering concerns that do not apply only to mainland Chinese accounts.

## Activities happening offshore are governed by rules in that particular jurisdiction

We understand that opening investment accounts for non-local residents is a legitimate and standard practice for HK and many other markets under local regulatory frameworks, as long as KYC and AML conditions are met.

The HK SFC's circular on 22 May required that HK-licensed brokers should apply additional requirements when opening accounts for mainland customers visiting HK.

On June 10, 2026, the SFC further clarified that licensed companies could still open accounts for qualified investors from mainland China, on the premise that funds are all from offshore legally, and because KYC and due diligence are strictly followed.

On the other hand, the SFC also instructed HK brokers to observe overseas rules when serving residents in that jurisdiction. This means even though account opening is permissible, HK brokers cannot provide trading services to mainland customers when they are physically onshore. We think this aligns exactly with the CSRC's requirements.

## Separately, ordinary bank account opening, which is overseen by the HKMA, is not a target of the CSRC's recent Notice

This underscores the fact that many mainland Chinese residents do have lawful income generated offshore – such as working overseas or doing export business. This is a direct spillover result of China's wealth creation from supply chain competitiveness and should continue to benefit offshore financial firms that service related asset allocation demand taking place outside of mainland China.

## We think regulators will gradually open up official outbound financial investment channels

The policy direction is therefore not an effort to “ban all offshore accounts” but rather to push flows into official channels, such as QDII, Southbound Stock Connect, and Wealth Management Connect. The opening up of the official channels is a gradual process, and investors currently still see some constraints from quotas, eligibility, regional restriction,s and closed-loop management, which our macro team has also pointed out.

Take QDII as an example – China Daily reported th

[中间内容因长度限制已省略]

ges relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

INDUSTRY COVERAGE: China Financials

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (06/10/2026)</td></tr><tr><td colspan="3">Chiyao Huang</td></tr><tr><td>China International Capital Corp. Ltd. (3908.HK)</td><td>O (02/28/2025)</td><td>HK$19.11</td></tr><tr><td>CMS Co Ltd (600999.SS)</td><td>U (09/29/2022)</td><td>Rmb17.20</td></tr><tr><td>CMS Co Ltd (6099.HK)</td><td>U (10/29/2024)</td><td>HK$15.33</td></tr><tr><td>CITIC Co. (6030.HK)</td><td>E (10/29/2024)</td><td>HK$25.06</td></tr><tr><td>CITIC Co. (600030.SS)</td><td>O (08/07/2025)</td><td>Rmb25.66</td></tr><tr><td>East Money Information Co Ltd (300059.SZ)</td><td>E (09/19/2025)</td><td>Rmb17.78</td></tr><tr><td>Futu Holdings Ltd (FUTU.O)</td><td>O (11/18/2024)</td><td>US$91.31</td></tr><tr><td>Galaxy Securities (6881.HK)</td><td>E (02/27/2020)</td><td>HK$7.65</td></tr><tr><td>Galaxy Securities (601881.SS)</td><td>U (09/29/2022)</td><td>Rmb12.07</td></tr><tr><td>GF Securities (000776.SZ)</td><td>E (08/07/2025)</td><td>Rmb19.06</td></tr><tr><td>GF Securities (1776.HK)</td><td>E (01/06/2023)</td><td>HK$16.25</td></tr><tr><td>HTSC (601688.SS)</td><td>E (09/23/2024)</td><td>Rmb19.37</td></tr><tr><td>HTSC (6886.HK)</td><td>E (09/23/2024)</td><td>HK$16.62</td></tr><tr><td colspan="3">Richard Xu, CFA</td></tr><tr><td>Agricultural Bank of China Limited (601288.SS)</td><td>E (05/07/2019)</td><td>Rmb6.71</td></tr><tr><td>Agricultural Bank of China Limited (1288.HK)</td><td>O (10/19/2020)</td><td>HK$5.80</td></tr><tr><td>Bairong Inc. (6608.HK)</td><td>E (09/09/2025)</td><td>HK$5.48</td></tr><tr><td>Bank of Beijing Co Ltd (601169.SS)</td><td>E (08/17/2022)</td><td>Rmb5.20</td></tr><tr><td>Bank of Chengdu Co Ltd (601838.SS)</td><td>O (08/17/2022)</td><td>Rmb19.80</td></tr><tr><td>Bank of China Limited (601988.SS)</td><td>E (05/07/2019)</td><td>Rmb6.22</td></tr><tr><td>Bank of China Limited (3988.HK)</td><td>O (01/10/2020)</td><td>HK$5.42</td></tr><tr><td>Bank of Communications (3328.HK)</td><td>U (05/20/2022)</td><td>HK$7.49</td></tr><tr><td>Bank of Communications (601328.SS)</td><td>U (09/05/2014)</td><td>Rmb6.94</td></tr><tr><td>Bank of Hangzhou Co Ltd (600926.SS)</td><td>E (08/17/2022)</td><td>Rmb16.61</td></tr><tr><td>Bank of Ningbo Co. Ltd (002142.SZ)</td><td>O (08/17/2022)</td><td>Rmb32.70</td></tr><tr><td>China CITIC Bank Corporation Limited (601998.SS)</td><td>E (04/16/2025)</td><td>Rmb7.69</td></tr><tr><td>China CITIC Bank Corporation Limited (0998.HK)</td><td>O (04/16/2025)</td><td>HK$7.69</td></tr><tr><td>China Construction Bank Corp. (0939.HK)</td><td>O (10/11/2012)</td><td>HK$8.75</td></tr><tr><td>China Construction Bank Corp. (601939.SS)</td><td>E (05/07/2019)</td><td>Rmb10.49</td></tr><tr><td>China Everbright Bank Co Ltd (6818.HK)</td><td>U (05/12/2023)</td><td>HK$3.28</td></tr><tr><td>China Everbright Bank Co Ltd (601818.SS)</td><td>U (05/20/2022)</td><td>Rmb3.18</td></tr><tr><td>China Merchants Bank (600036.SS)</td><td>O (01/07/2019)</td><td>Rmb38.90</td></tr><tr><td>China Merchants Bank (3968.HK)</td><td>O (09/20/2018)</td><td>HK$48.48</td></tr><tr><td>China Minsheng Banking Corp. (600016.SS)</td><td>O (08/28/2025)</td><td>Rmb3.60</td></tr><tr><td>China Minsheng Banking Corp. (1988.HK)</td><td>O (05/12/2023)</td><td>HK$3.51</td></tr><tr><td>Chongqing Rural Commercial Bank (3618.HK)</td><td>U (05/12/2023)</td><td>HK$6.59</td></tr><tr><td>Hua Xia Bank (600015.SS)</td><td>U (06/30/2015)</td><td>Rmb6.94</td></tr><tr><td>Industrial and Commercial Bank of China (1398.HK)</td><td>O (08/09/2013)</td><td>HK$7.00</td></tr><tr><td>Industrial and Commercial Bank of China (601398.SS)</td><td>E (09/19/2022)</td><td>Rmb7.69</td></tr><tr><td>Industrial Bank Co. Ltd. (601166.SS)</td><td>O (02/25/2019)</td><td>Rmb18.89</td></tr><tr><td>Lufax (LU.N)</td><td></td><td>US$1.34</td></tr><tr><td>Ping An Bank (000001.SZ)</td><td>O (05/07/2019)</td><td>Rmb11.32</td></tr><tr><td>Postal Savings Bank of China Co Ltd (1658.HK)</td><td>O (11/01/2016)</td><td>HK$5.07</td></tr><tr><td>Qifu Technology Inc (QFIN.O)</td><td>O (08/25/2020)</td><td>US$14.24</td></tr><tr><td>Shanghai Pudong Development Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.59</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

© 2026 MS
"""
