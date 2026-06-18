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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`NOM`。标题格式建议：`# NOM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份NOM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Asia Insights

Global Markets Research

17 June 2026

Foreign Exchange - Asia ex-Japan

# BI and RBI continued to drain their FX reserves aggressively in May

Relatively limited intervention by the remainder of AeJ central banks, as broad USD traded in a narrow range.

- BI and RBI responded to sustained FX depreciation pressures through aggressive FX/USD selling intervention in May, as USD/IDR and USDINR broke new highs.  
- Arguably, the recent, large drawdowns in their FX reserves could have pressured BI and RBI to take stronger measures, such as the off-cycle rate hike and concessional FX swap for FCNR(B) deposits, respectively.  
- BOK's spot FX/USD selling intervention was rather limited, even as KRW depreciation pressures mounted.  
- The PBoC, MAS, BOT and CBC accumulated limited FX reserves, as their currencies remained stable or even appreciated against USD (i.e., CNH and TWD).

## Key observations

- Our estimates show that BI was one of the most aggressive sellers of FX/USD within AeJ in May, at USD4.8bn (\~3.9% of April 2026 FXR; spot + forward). This brought BI's 2026 YTD intervention to USD21.2bn (\~15.7% of 2025 FXR). Despite the heavy intervention, onshore USD/IDR traded to an all-time high of 17,887 in May, and then higher to 18,190 on 8 June 2026. Under the IMF's four FX adequacy measures, BI's FX reserve adequacy stood at 90% as of April. However, accounting for predetermined short-term drainage, the reserve adequacy deteriorates to 46%.  
- The RBI was also an aggressive seller of FXR in May, totaling USD11.5bn (\~2.1% of April 2026 FXR; spot only). Onshore spot USD/INR rose to an all-time high of 96.965 on 20 May, before paring back some gains to end the month at 95.0, likely on RBI's FX intervention (Bloomberg, 29 May). Overall, the RBI's 2026 YTD FX/USD selling intervention stood at USD49.1bn (\~8.9% of 2025 FXR; spot + forward; forward until April 2026).  
The RBI's net short forward book was reduced by USD7.8bn in April 2026, bringing the overall short forward book to USD95.3bn from USD103.1bn in March. We note that the RBI conducted a USD5bn buy/sell FX swap on 26 May, which will increase the size of RBI's short forward book (ceteris paribus).  
- In China, we estimate the PBoC net bought USD28.7bn of FX reserves in May (0.8% of April 2026 FXR; spot only). Broad USD was 0.9% stronger in May; however, CNH strengthened by \~0.9% against USD, making it one of the best performing FX in AeJ in May. The PBoC and state banks might have bought FX/USD in the market to slow the pace of RMB appreciation. May FX deposit data showed that state banks accumulated another USD10.9bn of FX deposits, bringing a total of \~USD39.6bn of FX/USD accumulation by Chinese authorities in May (\~1.2% of April FXR).

## Research Analysts

Asia FX Strategy

Craig Chan - NSL

craig.chan@NOM.com

+65 6433 6106

Wee Choon Teo - NSL

weechoon.teo@NOM.com

+65 6433 6107

Vicky Chen - NSL

vicky.chen1@NOM.com

+65 6433 6540

Manthan Shingala - NSL

manthan.shingala1@NOM.com

+65 6433 6427

Fig. 1: Estimated intervention by AeJ central banks[1] in May

<table><tr><td>(USD bn)</td><td>CN</td><td>IN</td><td>ID</td><td>KR</td><td>PH</td><td>SG</td><td>TW</td><td>TH</td></tr><tr><td>May 2026 FX Reserves (USD bn)</td><td>3442</td><td>546</td><td>123</td><td>402</td><td>80</td><td>417</td><td>605</td><td>246</td></tr><tr><td>May intervention (spot &amp; forward)</td><td>28.7</td><td>-11.5</td><td>-4.8</td><td>-1.4</td><td>-0.3</td><td>1.7</td><td>0.6</td><td>1.4</td></tr><tr><td>May intervention as % of Apr FXR</td><td>0.8%</td><td>-2.1%</td><td>-3.9%</td><td>-0.4%</td><td>-0.4%</td><td>0.4%</td><td>0.1%</td><td>0.6%</td></tr><tr><td>Month of recent peak in FX reserves</td><td>May-26</td><td>Jun-25</td><td>Dec-25</td><td>Nov-25</td><td>Oct-25</td><td>May-26</td><td>Feb-26</td><td>Feb-26</td></tr><tr><td>Drawdown after the recent peak in FX reserves (spot &amp; forward)</td><td>-</td><td>-100.8</td><td>-21.2</td><td>-13.0</td><td>-11.8</td><td>-</td><td>-5.1</td><td>-1.0</td></tr><tr><td>Interv. since recent intensification in drawdown (spot &amp; forward) % of FXR</td><td>-</td><td>-17.0%</td><td>-15.7%</td><td>-3.2%</td><td>-13.3%</td><td>-</td><td>-0.9%</td><td>-0.4%</td></tr><tr><td>2026 YTD Interv. as % of end 2025 FXR</td><td>1.7%</td><td>-8.9%</td><td>-15.7%</td><td>-0.9%</td><td>-11.3%</td><td>0.0%</td><td>-1.1%</td><td>0.3%</td></tr><tr><td>2026 YTD Interv. as a % of GDP</td><td>0.3%</td><td>-1.3%</td><td>-1.5%</td><td>-0.2%</td><td>-2.0%</td><td>0.0%</td><td>-0.7%</td><td>0.1%</td></tr><tr><td>2025 Interv. as % of end 2024 FXR</td><td>-2.4%</td><td>-8.4%</td><td>-17.4%</td><td>-7.1%</td><td>-7.7%</td><td>3.9%</td><td>1.3%</td><td>8.5%</td></tr><tr><td>2024 Interv. as % of end 2023 FXR</td><td>-0.3%</td><td>-15.0%</td><td>-0.2%</td><td>-2.8%</td><td>-7.5%</td><td>8.6%</td><td>-2.9%</td><td>2.6%</td></tr><tr><td>May foreign equity flow (A)</td><td>-</td><td>-4.9</td><td>-0.2</td><td>-27.9</td><td>-0.2</td><td>-</td><td>8.4</td><td>0.1</td></tr><tr><td>May foreign bond flow (B)</td><td>-</td><td>0.5</td><td>-0.2</td><td>7.8</td><td>-</td><td>-</td><td>-</td><td>-1.0</td></tr><tr><td>Basic Balance monthly average (C)</td><td>50.3</td><td>-10.6</td><td>-1.2</td><td>22.2</td><td>-1.9</td><td>14.4</td><td>13.2</td><td>1.8</td></tr><tr><td>Current Account monthly average</td><td>54.7</td><td>-9.8</td><td>-2.4</td><td>24.7</td><td>-2.4</td><td>8.7</td><td>16.3</td><td>1.0</td></tr><tr><td>FDI monthly average</td><td>-4.4</td><td>-0.8</td><td>1.1</td><td>-2.5</td><td>0.5</td><td>5.7</td><td>-3.1</td><td>0.8</td></tr><tr><td>Total of BB and foreign equity and bond flow (A+B+C)</td><td>50.3</td><td>-15.1</td><td>-1.7</td><td>2.2</td><td>-2.1</td><td>14.4</td><td>21.6</td><td>0.9</td></tr><tr><td>USD/Asia in May</td><td>-0.9%</td><td>0.1%</td><td>3.1%</td><td>2.3%</td><td>0.3%</td><td>0.1%</td><td>-1.0%</td><td>0.0%</td></tr><tr><td>Average Reserve Adequacy</td><td>98%</td><td>234%</td><td>88%</td><td>76%</td><td>144%</td><td>60%</td><td>117%</td><td>250%</td></tr><tr><td>Average Reserve Adequacy with a fixed exchange rate regime</td><td>71%</td><td>192%</td><td>71%</td><td>60%</td><td>114%</td><td>56%</td><td>95%</td><td>193%</td></tr></table>

Note: FX reserves data (spot and forward) is for May 2026 or the latest available. We have used actual FX intervention data where available for the BOK (to Q4 2025), CBC (to Q4 2025), the MAS (to H2 2025), and the RBI (to March 2026). FX forwards for May are available for the CBC and BOT, based on our estimates for BI (using FX swaps), and unavailable for the RBI, PBoC, BOK, BSP and MAS (only using adjusted spot reserves). The recent peak in FX reserves is the peak of headline FX reserves in the last 12 months. Bond data for Thailand from the BOT. India bond flow data from WFII. CA is based on Q3 2026 (NOM forecast), divided by 3. FDI is last 4Q average divided by 4. Basic Balance is the sum of CA and FDI. Reserve Adequacy as of May2026.  
Source: CEIC, Bloomberg, NOM.

1. For BOK spot intervention, we adjusted for FX valuations, coupons receipts and FX bond issuance and maturities. For MAS spot intervention, we adjusted for FX valuations, coupons receipts and outstanding amount of Reserves Management Government Securities. For BI spot intervention, we adjusted for FX valuations, coupons, receipts and FX bond issuance and maturities, FX term deposits, and government foreign currency loans. FX forwards for May are available for the CBC (+USD0.02bn) and BOT (+USD0.6bn), and based on our estimates for BI (using FX swaps; -USD0.5bn).

## Appendix A-1

This report has been produced by NOM Singapore Ltd. (NSL), Singapore.

See Disclaimers for NOM Group entity details.

## Analyst Certification

We, Craig Chan, Wee Choon Teo, Vicky Chen and Manthan Shingala, hereby certify (1) that the views expressed in this Research report accurately reflect our personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of our compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of our compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.

Important disclosures may be read at http://go.NOMnow.com/research/m/Disclosures or requested from NOM Securities International, Inc. If you have any difficulties with the website, please email grpsupport@NOM.com for help.

The analysts responsible for preparing this report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by Investment Banking activities. Unless otherwise noted, the non-US analysts listed at the front of this report are not registered/qualified as research analysts under FINRA rules, may not be associated persons of NSI, and may not be subject to FINRA Rule 2241 restrictions on communications with covered companies, public appearances, and trading securities held by a research analyst account.

NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## ADDITIONAL DISCLOSURES REQUIRED IN THE U.S.

Principal Trading: NOM Securities International, Inc and its affiliates will usually trade as principal in the fixed income securities (or in related derivatives) that are the subject of this research report. Analyst Interactions with other NOM Securities International, Inc. Personnel: The fixed income research analysts of NOM Securities International, Inc and its affiliates regularly interact with sales and trading desk personnel in connection with obtaining liquidity and pricing information for their respective coverage universe.

## Valuation methodology - Fixed Income

NOM's Fixed Income Strategists express views on the price of securities and financial markets by providing trade recommendations. These can be relative value recommendations, directional trade recommendations, asset allocation recommendations, or a mixture of all three.

The analysis which is embedded in a trade recommendation would include, but not be limited to:

- Fundamental analysis regarding whether a security's price deviates from its underlying macro- or micro-economic fundamentals.  
• Quantitative analysis of price variations.  
- Technical factors such as regulatory changes, changes to risk appetite in the market, unexpected rating actions, primary market activity and supply/ demand considerations.

The timeframe for a trade recommendation is variable. Tactical ideas have a short timeframe, typically less than three months. Strategic trade ideas have a longer timeframe of typically more than three months.

For the purposes of the EU Market Abuse Regulation, the distribution of ratings published by NOM Global Fixed Income Research is as follows:

52% have been assigned a Buy (or equivalent) rating; 50% of issuers with this rating were supplied material services\* by the NOM Group\*\*.
0% have been assigned a Neutral (or equivalent) rating.

48% have been assigned a Sell (or equivalent) rating; 50% of issuers with this rating were supplied material services by the NOM Group. As at 31 Mar 2026.

\*As defined by the EU Market Abuse Regulation

\*\*The NOM Group as defined in the Disclaimer section at the end of this report

## Disclaimers

This publication contains material that has been prepared by the NOM Group entity identified on page 1 and, if applicable, with the contributions of one or more NOM Group entities whose employees and their respective affiliations are specified on page 1 or identified elsewhere in this publication. The term "NOM Group" used herein refers to NOM Holdings, Inc. and its affiliates and subsidiaries including: (a) NOM Securities Co., Ltd. ('NSC') Tokyo, Japan, (b) NOM Financial Products Europe GmbH ('NFPE'), Germany, (c) NOM International plc ('NIplc'), UK, (d) NOM Securities International, Inc. ('NSI'), New York, US, (e) NOM International (Hong Kong) Ltd.

('NIHK'), Hong Kong, (f) NOM Financial Investment (Korea) Co., Ltd. ('NFIK'), Korea (Information on NOM analysts registered with the Korea Financial Investment Association ('KOFIA') can be found on the KOFIA Intranet at http://dis.kofia.or.kr, (g) NOM Singapore Ltd. ('NSL'), Singapore (Registration number 197201440E, regulated by the Monetary Authority of Singapore) (h) NOM Australia Ltd. ('NAL'), Australia (ABN 48 003 032 513), regulated by the Australian Securities and Investment Commission ('ASIC') and holder of an Australian financial services licence number 246412, (i) NOM Securities Malaysia Sdn. Bhd. ('NSM'), Malaysia, (j) NIHK, Taipei Branch ('NITB'), Taiwan, (k) NOM Financial Advisory and Securities (India) Private Limited ('NFASL'), Mumbai, India (Registered Address: Ceejay House, Level 11, Plot F, Shivsagar Estate, Dr. Annie Besant Road, Worli, Mumbai- 400 018, India; Tel: 91 22 4037 4037, Fax: 91 22 4037 4111; CIN No: U74140MH2007PTC169116, SEBI Registration No. for Stock Broking activities : INZ000255633; SEBI Registration No. for Merchant Banking : INM000011419; SEBI Registration No. for Research: INH000001014 - Compliance Officer: Ms. Pratiksha Tondwalkar, 91 22 40374904, grievance email: investorgrievancesra@NOM.com Webpage: LINK

For reports with respect to Indian public companies or authored by India-based NFASL research analysts: (i) Investment in securities markets is subject to market risks. Read all the related documents carefully before investing. (ii) Registration granted by SEBI, and certification from NISM in no way guarantee performance of the intermediary or provide any assurance of returns to investors. (iii) NFASL terms and conditions for availing research services is disclosed on NFASL webpage.

(I) NOM Fiduciary Research & Consulting Co., Ltd. ('NFRC') Tokyo, Japan. (m) NOM Orient International Securities Co., Ltd ("NOI"), is a majority owned joint venture amongst NOM Group, Orient International (Holding) Co., Ltd, and Shanghai Huangpu Investment Holding (Group) Co., Ltd. In accordance with the laws of the People's Republic of China ("PRC", excluding Hong Kong, Macau and Taiwan, for the purpose of this document), NOI is licensed in the PRC to provide securities research and investment recommendations and it operates independently from the other members of the NOM Group; in particular, NOI's interests in PRC securities are not disclosed to, or aggregated with the holdings of, any other NOM Group entities and the interests in PRC securities of other NOM Group entities are not disclosed to, or aggregated with the holdings of, NOI. An individual name printed next to NOI on the front page of a research report indicates that individual is employed by NOI to provide research assistance to NIHK under a research partnership agreement. 'NSFSPL' next to an employee's name on the front page of a research report indicates that the individual is employed by NOM Structured Finance Services Private Limited to provide assistance to certain NOM entities under inter-company agreements. 'Verdhana' next to an individual's name on the front page of a research report indicates that the individual is employed by PT Verdhana Sekuritas Indonesia ('Verdhana') to provide research assistance to NIHK under a research partnership agreement and neither Verdhana nor such individual is licensed outside of Indonesia.

THIS MATERIAL IS: (I) FOR YOUR PRIVATE INFORMATION, AND WE ARE NOT SOLICITING ANY ACTION BASED UPON IT; (II) NOT TO BE CONSTRUED AS AN OFFER TO SELL OR A SOLICITATION OF AN OFFER TO BUY ANY SECURITIES IN ANY JURISDICTION WHERE SUCH OFFER OR SOLICITATION WOULD BE ILLEGAL; AND (III) OTHER THAN DISCLOSURES RELATING TO THE NOM GROUP, BASED UPON INFORMATION FROM SOURCES THAT WE CONSIDER RELIABLE, BUT HAS NOT BEEN INDEPENDENTLY VERIFIED BY NOM GROUP.

Other than disclosures relating to the NOM Group, the NOM Group does not warrant, represent or undertake, express or implied, that the document is fair, accurate, complete, correct, reliable or fit for any particular purpose or merchantable, and to the maximum extent permissible by law and/or regulation, does not accept liability (in negligence or otherwise, and in whole or in part) for any act (or decision not to act) resulting from use of this document and related data. To the maximum extent permissible by law and/or regulation, all warranties and other assurances by the NOM Group are hereby excluded and the NOM Group shall have no liability (in negligence or otherwise, and in whole or in part) for any loss howsoever arising from the use, misuse, or distribution of this material or the information contained in this material or otherwise arising in connection therewith.

Opinions or estimates expressed are current opinions as of the original publication date appearing on this material and the information, including the opinions and estimates contained herein, are subject to change without notice. The NOM Group, however, expressly disclaims any obligation, and therefore is under no duty, to update or revise this document. Any comments or statements made herein are those of the author(s) and may differ from views held by other parties within NOM Group. Clients should consider whether any advice or recommendation in this report is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The NOM Group does not provide tax advice.

The NOM Group, and/or its officers, directors, employees and affiliates, may, to the extent permitted by applicable law and/or regulation, deal as principal, agent, or otherwise, or have long or short positions in, or buy or sell, the securities, commodities or instruments, or options or other derivative instruments based thereon, of issuers or securities mentioned herein. The NOM Group companies may also act as market maker or liquidity provider (within the meaning of applicable 

[中间内容因长度限制已省略]

ER REGARDING THE SUITABILITY OF THE INVESTMENT, UNDER A SEPARATE ENGAGEMENT, AS THE RECIPIENT DEEMS FIT. Unless prohibited by the provisions of Regulation S of the 1933 Act, this material is distributed in the US, by NSI, a US-registered broker-dealer, which accepts responsibility for its contents in accordance with the provisions of Rule 15a-6, under the US Securities Exchange Act of 1934. The entity that prepared this document permits its separately operated affiliates within the NOM Group to make copies of such documents available to their clients.

This document has not been approved for distribution to persons other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ (as defined by the Capital Markets Authority) in the Kingdom of Saudi Arabia (‘Saudi Arabia’) or a ‘Market Counterparty’ or a ‘Professional Client’ (as defined by the Dubai Financial Services Authority) in the United Arab Emirates (‘UAE’) or a ‘Market Counterparty’ or a ‘Business Customer’ (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar (‘Qatar’) by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a ‘Market Counterparty’ or a ‘Professional Client’ in the UAE or a ‘Market Counterparty’ or a ‘Business Customer’ in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved.
"""
