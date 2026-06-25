你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# Global Markets Daily: Tech Support—The AI Boom and The Dollar

Coming into the year, we argued that less exceptional US performance should lead to a weaker Dollar over time. Not only has the conflict in the Middle East disrupted expectations for more notable relative underperformance, but a surge in AI momentum has also challenged that narrative. The strength of the AI trade has driven another leg of US equity outperformance; if anything, the Dollar has appeared slightly weaker than expected from this perspective alone.

Lexi Kanter  
+1(212)855-9701 | alexandra.kanter@gs.com GS & Co. LLC

We see three reasons that help explain the flatter Dollar relative to clear US equity outperformance. First, US equity outperformance is less pronounced versus EMs than DMs, and flows tend to matter more for EM FX. Second, we find evidence that durability matters: sharp upgrades to near-term US earnings expectations do not generate as much Dollar demand as more sustained earnings power would. Third, narrow equity market breadth appears to limit FX spillovers.

Together, these factors reinforce that relative equity returns can proxy broader balance-of-payments pressures that influence exchange rates. While they suggest that this year's tech sector strength may overstate the extent of US outperformance and demand for Dollar assets, the broader equity impulse has clearly shifted from an expected drag to a source of support for the Dollar.

## Tech Support—The AI Boom and The Dollar

Demand for US equity exposure has increasingly helped fund the US current account deficit, supporting the Dollar's rich valuation in recent years. Coming into 2026, we argued that less exceptional US performance should lead to a weaker Dollar over time. Despite the Dollar's resilience through the “software sell-off” in February, concerns around AI disruption seemed to accelerate that narrative towards the end of last year and early this year. Not only has the conflict in the Middle East disrupted expectations for more notable relative underperformance, but a surge in AI momentum has also challenged that thesis. The strength of the AI trade has driven another leg of US equity outperformance; if anything, the Dollar has appeared slightly weaker than would be expected from this perspective alone. Typically, US equity performance versus major DM equity indices (MSCI World ex US) is a good gauge of US versus rest of world performance and tracks the broad Dollar closely, but that relationship has recently dislocated (Exhibit 1).

Exhibit 1: Typically, US equity performance versus major DM equity indices (MSCI World ex US) tracks the broad Dollar closely, but that relationship has recently dislocated  
![](images/004328154b134a7417cfd0d15ebf8c3a4f23a12ffba61b457bf7ccb0ecc860e1.jpg)  
Source: Bloomberg, GS Global Investment Research

We see three reasons that help explain the flatter Dollar relative to clear US equity outperformance. First, US equity outperformance has been less pronounced versus EM equities than DM equities (Exhibit 2), and flows are typically more relevant for EM FX. Stronger tech earnings and capex plans have driven gains in tech-heavy Asian markets, including Korea and Taiwan, which the DM index does not capture. As we recently noted, this DM metric would normally imply room for “catch-up” in the broad Dollar, but it now overstates the extent of US equity outperformance.

Equity flows also tend to matter more for EM FX than DM FX. Regressing weekly returns in FX (USD/XXX) on net bilateral equity flows, we find that US equity inflows are a more significant driver of the Dollar versus EM currencies than versus DM currencies. Because recent US equity outperformance has occurred mainly against DM markets, the FX spillover should ultimately be more limited.

Exhibit 2: US outperformance has been less pronounced versus EM equities than DM equities  
![](images/964b3e45eff5120356367797981a4233509a3ca1239b303c831c767d853542df.jpg)  
MSCI World ex USA tracks developed markets, while MSCI ACWI ex USA covers both developed and emerging markets.  
Source: Bloomberg, GS Global Investment Research

Exhibit 3: US equity inflows are a more significant driver of the Dollar versus EM FX than DM FX  
![](images/1d98edbe731cfe6e598dd56067fd5afe9a2788aa8d4855a937b2107a760441a6.jpg)  
Univariate regression of weekly FX returns (USD/XXX) on net bilateral equity flows since 2010  
Source: EPFR, GS Global Investment Research, Bloomberg

Second, we find evidence that the expected durability of equity performance matters. When US earnings growth is expected to slow—with consensus one-year expectations above two-year expectations—the Dollar tends to underperform what relative equity performance would imply (Exhibit 4). Our equity strategists note that surging near-term earnings estimates have driven the recent market rally, while two-year-ahead consensus earnings growth expectations point to future deceleration. Consistent with this, the recent sharp upgrades to near-term US earnings expectations have not generated as much Dollar demand as more sustained earnings power would. The broad Dollar also appears more geared to US earnings expectations than to the relative earnings backdrop. While relative forward earnings expectations have slightly stronger explanatory power, US forward earnings growth expectations alone explain much of the residual between Dollar performance and relative equity performance (Exhibit 5).

Of course, earnings expectations are only a part of the story. Generally, we expect other macro drivers, including rate differentials and terms of trade, to matter more. This was clearly the case in the 2011-2014 period, when dovish Fed policy weighed on the Dollar despite supportive relative equity performance, and more recently when flatter relative terms of trade versus other DM economies constrained the Dollar against DM FX compared with what equity performance would imply.

USD - Relative Equity Residual vs Earnings Growth Acceleration

Exhibit 4: Recent sharp upgrades to near-term US earnings expectations have not generated as much Dollar demand as more sustained earnings power would

![](images/3a927d0edec9d09bf8f191665b96cd49e45da44b73406af3a2f72b8b0931c946.jpg)  
Levels regression of USDTWI on log(S&P 500 / MSCI World ex-US). Sample: weekly since 2000. Expected earnings growth acceleration measures the slope of consensus forward earnings growth expectations, calculated as two-year-ahead minus one-year-ahead earnings growth estimates.

Exhibit 5: US forward earnings growth expectations alone explain much of the residual between Dollar performance and relative equity performance  
![](images/9f0c424e138989e3d06b84a0bfd5354d47232b3940374b194d8f20ee2d939d44.jpg)  
Univariate regression of the USD\~log(S&P 500 / MSCI World ex-US) residual on US and relative expected earnings growth acceleration. Sample: monthly since 2007 given data availability.  
Source: Bloomberg, FactSet, GS Global Investment Research  
Source: Bloomberg, FactSet, GS Global Investment Research

Third, equity market breadth appears to limit FX spillovers. Our equity strategists note that the concentration of the recent market rally has compressed US equity market breadth to one of its tightest levels in recent decades. Using their measure of market breadth $^{1}$ , we find that more concentrated market rallies tend to coincide with larger Dollar underperformance relative to what equity performance would imply (Exhibit 6).

Exhibit 6: Equity market breadth appears to limit FX spillovers  
![](images/676d8d671882db82971f0ba78b76e0f887e2e6521d223ca9365b753bc44972ef.jpg)  
For residual calculation see Exhibit 4. Monthly data since 2000 excluding 2011-2014 period.  
Source: Bloomberg, GS Global Investment Research, FactSet

More broadly, we have previously noted that the FX relationship to equity performance depends on the nature of the underlying shock. The Dollar's resilience through the software sell-off (and equity market wobbles in recent days) has reflected, in part, that the shock was not clearly US-negative, with global equities selling off alongside US equities. The recent AI boom has had a similar, but inverse, dynamic—global equities have also benefited from the rally (in some cases more so than the US), making more muted support for the Dollar less surprising (Exhibit 7). In fact, a broader procyclical, risk-supportive environment typically weighs on the Dollar. In this sense, “exceptional” US equity performance has helped keep the Dollar more supported than we might otherwise expect in a procyclical backdrop.

Exhibit 7: Global equities have also benefited from the AI boom (in some cases more so than the US) making the more muted support for the Dollar less surprising  
![](images/6e52fad5d470ae4ccfeb4462ddc82dce869ef39122bf1aa516ca19cfa1428909.jpg)  
We reference the following equity indices: the S&P 500, Euro Stoxx 600, MSCI China, TOPIX, MSCI EM, and KOSPI  
Source: Bloomberg, GS Global Investment Research

Taken together, these factors reinforce that relative equity returns can proxy broader balance-of-payments pressures that influence exchange rates. We maintain that a US equity market sell-off with clearer rest-of-world outperformance should still be one catalyst for Dollar depreciation. That said, while this year's AI-driven outperformance, particularly vs other DM markets, may overstate the extent of US outperformance and demand for Dollar assets, the broader equity impulse has clearly shifted from an expected drag to a support for the Dollar (Exhibit 8).

Exhibit 8: The broader equity impulse has clearly shifted from an expected drag to a support for the Dollar  
![](images/e47c3837c97a319f5a37a76776bf128b3c1fb227e5b817e27c8799c1c0a070e4.jpg)  
Source: Bloomberg, GS Global Investment Research

## TRADE IDEAS

## Best Trade Ideas Across Assets

For pricing, charts, and a list of previous recommendations, please visit our Trade Ideas page.

1. Stay short SGD/MYR, opened January 24, 2026, at 3.13, with a target at 2.90 and a stop at 3.30, currently trading at 3.20.

2. Stay long TRY, NGN and KZT against the USD, as an equally weighted basket, opened February 18, 2026, at 0%, with a total return target of 7.5%, and a revised stop of 0%, currently trading at 2.6%.

3. Stay long 3y France, Spain, Italy vs OIS (equally weighted), opened April 10, 2026, at 0.33, with a target at 0.23 and a revised stop at 0.32, currently trading at 0.30.

4. Stay long MSCI Korea and Taiwan (equal weight) vs. short MSCI India, Philippines, Thailand (equal weight), opened April 16, 2026, at 100, with a revised target of 155 and a revised stop of 130, currently trading at 136.

5. Stay short EUR/HUF, opened 17 April 2026, at 361, with a revised target of 345 and a revised stop of 360, currently trading at 356.

6. Stay long 3y SOFR swap spread, opened 17 April 2026, at -22.6bp, with a target at -18bp inclusive of carry; and a revised stop at -23bp, currently trading at -20bp.

7. 2s5s CAD steepener, opened 24 April 2026, at 20bp, with a target at 35bp and a revised stop at 20bp, current trading at 24bp.

8. Stay short USD/EGP, opened 24 April 2026, at 0%, with a revised total return target at 10% and a revised stop at 4%, currently trading at 8.2%.

9. Stay long 5y Receivers on 3m 2s5s10s Receiver Fly (bp running), opened 09 May 2026, at 1bp, with a target at 10bp and a stop at -5bp, currently trading at -1bp.

10. 1y forward 2s10s GBP OIS steepeners, opened 29 May 2026, at 0.38, with a target at 0.55 and a stop at 0.25, currently trading at 0.37.

11. Close 2Y ZAR OIS, opened 03 June 2026, at $7.47\%$ , for a potential gain of 7bp.

12. Stay short THB/INR, opened 12 June 2026, at 2.91, with a target at 2.70 and a stop at 3.05, currently trading at 2.85.

G10 FX Strategy Team

Michael Cahill  
+44(20)7552-8314  
michael.e.cahill@gs.com  
GS International

Karen Reichgott Fishman +1(212)855-6006  
karen.fishman@gs.com  
GS & Co. LLC

Stuart Jenkins  
+44(20)7051-4700  
stuart.jenkins@gs.com  
GS International

Lexi Kanter  
+1(212)855-9701  
alexandra.kanter@gs.com  
GS & Co. LLC

## Disclosure Appendix

## Reg AC

I, Lexi Kanter, hereby certify that all of the views expressed in this report accurately reflect my personal views, which have not been influenced by considerations of the firm's business or client relationships.

Unless otherwise stated, the individuals listed on the cover page of this report are analysts in GS' Global Investment Research division.

Contributing Authors: Lexi Kanter GS & Co. LLC.

Unless otherwise stated, the individuals listed in the Contributing Authors disclosure of this report are analysts in GS' Global Investment Research division.

## Disclosures

## Regulatory disclosures

## Disclosures required by United States laws and regulations

See company-specific regulatory disclosures above for any of the following disclosures required as to companies referred to in this report: manager or co-manager in a pending transaction; $1\%$ or other ownership; compensation for certain services; types of client relationships; managed/co-managed public offerings in prior periods; directorships; for equity securities, market making and/or specialist role. GS trades or may trade as a principal in debt securities (or in related derivatives) of issuers discussed in this report.

The following are additional required disclosures: Ownership and material conflicts of interest: GS policy prohibits its analysts, professionals reporting to analysts and members of their households from owning securities of any company in the analyst's area of coverage. Analyst compensation: Analysts are paid in part based on the profitability of GS, which includes investment banking revenues. Analyst as officer or director: GS policy generally prohibits its analysts, persons reporting to analysts or members of their households from serving as an officer, director or advisor of any company in the analyst's area of coverage. Non-U.S. Analysts: Non-U.S. analysts may not be associated persons of GS & Co. LLC and therefore may not be subject to FINRA Rule 2241 or FINRA Rule 2242 restrictions on communications with a subject company, public appearances and trading in securities covered by the analysts.

## Additional disclosures required under the laws and regulations of jurisdictions other than the United States

Additional disclosures required under the laws and regulations of jurisdictions other than the United States

The following disclosures are those required by the jurisdiction indicated, except to the extent already made above pursuant to United States laws and regulations. Australia: GS Australia Pty Ltd and its affiliates are not authorised deposit-taking institutions (as that term is defined in the Banking Act 1959 (Cth)) in Australia and do not provide banking services, nor carry on a banking business, in Australia. This research, and any access to it, is intended only for “wholesale clients” within the meaning of the Australian Corporations Act, unless otherwise agreed by GS. In producing research reports, members of Global Investment Research of GS Australia may attend site visits and other meetings hosted by the companies and other entities which are the subject of its research reports. In some instances the costs of such site visits or meetings may be met in part or in whole by the issuers concerned if GS Australia considers it is appropriate and reasonable in the specific circumstances relating to the site visit or meeting. To the extent that the contents of this document contains any financial product advice, it is general advice only and has been prepared by GS without taking into account a client’s objectives, financial situation or needs. A client should, before acting on any such advice, consider the appropriateness of the advice having regard to the client’s own objectives, financial situation and needs. A copy of certain GS Australia and New Zealand disclosure of interests and a copy of GS’ Australian Sell-Side Research Independence Policy Statement are available at: https://www.goldmansachs.com/disclosures/australia-new-zealand/index.html. Brazil: Disclosure information in relation to CVM Resolution n. 20 is available at https://www.gs.com/worldwide/brazil/area/gir/index.html. Where applicable, the Brazil-registered analyst primarily responsible for the content of this research report, as defined in Article 20 of CVM Resolution n. 20, is the first author named at the beginning of this report, unless indicated otherwise at the end of the text. Canada: This information is being provided to you for information purposes only and is not, and under no circumstances should be construed as, an advertisement, offering or solicitation by GS & Co. LLC for purchasers of securities in Canada to trade in any Canadian security. GS & Co. LLC is not registered as a dealer in any jurisdiction in Canada under applicable Canadian securities laws and generally is not permitted to trade in Canadian securities and may be prohibited from selling certain securities and products in certain jurisdictions in Canada. If you wish to trade in any Canadian securities or other products in Canada please contact GS Canada Inc., an affiliate of The GS Group Inc., or another registered Canadian dealer. Hong Kong: Further information on the securities of covered companies referred to in this research may be obtained on request from GS (Asia) L.L.C. India: Further information on the subject company or companies referred to in this research may be obtained from GS (India) Securities Private Limited, Research Analyst – SEBI Registration Number INH000001493, 10th Floor, Ascent-Worli, Sudam Kalu Ahire Marg, Worli, Mumbai-400 025, India, Corporate Identity Number U74140MH2006FTC160634, Phone +91 22 6616 9000, Fax +91 22 6616 9001. GS may beneficially own 1% or more of the securities (as such term is defined in clause 2 (h) the Indian Securities Contracts (Regulation) Act, 1956) of the subject company or companies referred to in this research report. Investment in securities market are subject to market risks. Read all the related documents carefully before investing. Registration granted by SEBI and certification from NISM in no way guarantee performance of the intermediary or provide any assur

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
