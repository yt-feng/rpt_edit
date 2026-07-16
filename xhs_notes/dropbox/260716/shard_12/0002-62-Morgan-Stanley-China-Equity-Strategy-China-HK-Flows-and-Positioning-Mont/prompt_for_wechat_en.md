You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
China Equity Strategy | Asia Pacific

# China/HK Flows and Positioning Monthly Tracker – June 2026

## Key Takeaways

■ Foreign fund outflows accelerated sharply in June, marking the third-highest monthly outflow since 2025, with outflows from both passive and active funds.

National Team selling remained elevated, while domestic liquidity stayed resilient with record-high margin balances and rising private fund AUM.

■ Southbound inflows rebounded strongly, but foreign passive flows into A-shares reversed to outflows.

## Foreign-domiciled long-only fund flows:

\- Chinese equity flows from foreign-domiciled (US and EU) funds saw outflows accelerate to US\$3.6bn in June, marking the third-largest monthly outflow since 2025, only behind April 2025 (reciprocal tariffs) and March 2026 (US-Iran conflict). Passive funds reversed into net outflows of US\$1.3bn, while active fund outflows accelerated to US\$2.2bn (Exhibit 2).

\- On a cumulative basis, foreign fund inflows dropped to US\$6.9bn in 1H26, representing 50% of the full-year 2025 inflow total ( Exhibit 4 , Exhibit 5 ).

\- Based on the latest available data (with most funds having disclosed position data up to May-26), Global EM funds' China UW remained stable at 1.4ppt. However, EM funds and AxJ funds narrowed their underweight positions, with EM funds now at 5.2ppt UW and AxJ funds at 0.9ppt UW (Exhibit 1).

• More details: Fund Flows in China/HK Equities.

## A-share market liquidity:

\- National Team outflows, proxied by CSI 300 ETF flows, accelerated to an estimated US\$23bn in June from US\$21bn in May; less support amid the strong rally in AI and technology stocks ( Exhibit 7).

\- Domestic liquidity remained supportive, with private fund AUM continuing to grow and margin financing balances hitting a record high, despite moderation in retail trading activity. (Exhibit 12, Exhibit 13).

• More details: A-share Liquidity Track.

## Southbound/Northbound flow:

\- Southbound flows re-accelerated to US\$3.5bn in June (vs. US\$0.4bn outflow in May). On a cumulative basis, 1H26 southbound inflows were US \$36bn, representing 21% of the 2025 full-year inflows (Exhibit 3).

\- Foreign passive fund flows into CSI 300 (a proxy for northbound flow) reversed to outflows in June after two months of inflows (Exhibit 19).

<table><tr><td colspan="2">MS ASIA LIMITED+</td></tr><tr><td colspan="2">Chloe Liu</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Chloe.Liu1@morganstanley.com</td><td>+852 2848-5497</td></tr></table>

<table><tr><td colspan="2">Laura Wang</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Laura.Wang@morganstanley.com</td><td>+852 2848-6853</td></tr><tr><td colspan="2">Vicky Wu</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Vicky.Wu@morganstanley.com</td><td>+852 3963-3928</td></tr></table>

<table><tr><td colspan="2">Kristal Ji</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Kristal.Ji@morganstanley.com</td><td>+65 6834-6949</td></tr></table>

<table><tr><td colspan="2">Daniel K Blake</td></tr><tr><td colspan="2">Equity Strategist</td></tr><tr><td>Daniel.Blake@morganstanley.com</td><td>+65 6834-6597</td></tr></table>

![](images/5b490fbd6672f8af57cefef8731975213742269f1c0fa33a359e059a7b684314.jpg)

Exhibit 1: Active weights of China/HK equities by regional fund category and manager domicile  
![](images/6ff1e343bc0a2638b2b50ff7f04aa47e6378d87710afbeeafd2a23f648b3dee1.jpg)  
Source: FactSet, MorningStar, EPFR, MS. Note: Data refreshed as of June 30, 2026, most funds have disclosed position data up to May 31. Fund universe of each category is formed by the largest 30 active mutual funds under MorningStar regional category. Funds under "non-US Managers" are mostly domiciled in Europe. We exclude ESG funds, income funds, and systematic funds. All the covered funds are benchmarking to either MSCI or FTSE standard regional indices of All Country World, Asia ex Japan, or Emerging Markets.

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Fund Flows in China/HK Equities

## For foreign-domiciled mutual funds

\- By sector: Active fund managers added the most active weights in Semiconductors, Tech Hardware and Media & Entertainment vs. last month, while they trimmed most in Consumer Discretionary Distribution & Retail, Insurance and Food Beverage & Tobacco (Exhibit 22).

\- By company: Tencent, Advanced Micro-Fabrication Equipment, and Wuxi App Tech were most added, while BABA, Ping An Insurance and Lenovo were most trimmed vs. last month (Exhibit 19).

\- Also read: Fund Positions Changes vs. Last Month – Top 50 Mutual Fund Holdings, Funds Positions Changes vs. Last Month – By GICS Industry Group

Exhibit 2: Monthly fund flows in China/HK equities by foreign passive and active funds  
![](images/67270936890aefec64c85fefc4d489f7ae841b133780d642a9e4e56baaabb62a.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

Exhibit 3: Southbound monthly net fund flows  
![](images/39c0c622e6463141df87f80c451c53ee5a5e554251dbb5a898045c6f77e436c6.jpg)  
Source: CEIC, MS. Note: Data as of Jun 30, 2026.

Exhibit 4: Cumulative fund flows in China/HK equities by both US- and EU-domiciled active funds  
![](images/20a2fa9229f1109b88da9c011700eaeccb9d88c15a029ce07fb452f7baa8c7f2.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

Exhibit 5: Cumulative fund flows in China/HK equities by both US- and EU-domiciled passive funds  
![](images/8d85d2370d7e3bef819d9492a078009b1af891989d4604a74641cb430b8ac3ec.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

Exhibit 6: Daily net fund flows in China/HK equities by both US- and EU-domiciled active funds  
![](images/fab69dd9b58cf235bb30717f5ec5c9073afbd67cdcc214592a70b82650c3e455.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

Exhibit 7 Daily net fund flows in China/HK equities by both US- and EU-domiciled passive funds  
![](images/4ada098573cee22d980d394b67f591281d1ac3895245b1c5a1873bc447df7cac.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

## A-share Liquidity Track

\- National Team ETF selling accelerated in June, led by CSI 300 ETF outflows of US\$23bn, while CSI 500 and CSI 1000 flows were broadly stable. (Exhibit 7).

\- Retail participation softened at the margin in June: New account openings rose slightly and margin financing balances reached another record high at Rmb3.0tn, but daily small-order net inflows moderated to Rmb25bn (vs. Rmb33bn in May), pointing to more mixed retail activity (Exhibit 11, Exhibit 12).

\- Domestic liquidity remained supportive: Private fund AUM continued to expand, up 42% from mid-2025 levels (Exhibit 13), while active mutual funds (hybrid funds) extended their steady AUM growth. ETF AUM saw a modest decline, likely reflecting continued National Team redemptions (Exhibit 14).

\- Foreign passive flows into A-shares turned negative in June: Passive funds tracking the CSI 300 reversed to net outflows after two consecutive months of inflows in April and May. (Exhibit 19).

National Team ETF selling accelerated in June, led by CSI 300 ETFs; CSI 500 and CSI 1000 flows remained broadly stable.

We use CSI 300 passive ETF flows as a proxy for the National Team's cumulative buying and selling activity. CSI 300 ETF outflows further accelerated to US\$23bn in June (vs. US\$21bn in May), while CSI 500 and CSI 1000 flows were broadly flat.

Exhibit 7: China domestic broad-market index ETF flow – ETF selling continued in June  
![](images/96fd863d4d6a0377d60bd083522acee6d329f2985eda956797b782b5e526e429.jpg)  
Source: EPFR, MS. Data as of Jun 30, 2026.

Exhibit 8: Cumulative fund flows in China/HK equities from Chinese domestic domiciled passive funds  
![](images/2f105e3f75c872802c103de7865bc5edd7245e3d32712a8b59f6f1bd31fb5f6f.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

Exhibit 9: Daily fund flows in China/HK equities from Chinese domestic domiciled passive funds  
![](images/01970ddfafa9745d2fc3b494d81fef5d9c04db239743a84d28b03adb243d1696.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

Retail participation was more mixed in June, with account openings and margin financing balances continuing to rise, while small-order inflows softened.

\- New SSE account opening rose slightly to 2.9mn in June from 2.8mn in May.

\- The daily average net inflow of A-share small orders (under Rmb40,000, a proxy for retail participation) declined to Rmb25bn in June from Rmb33bn in May, suggesting softer retail trading activity.

\- A-share total margin financing balance (a proxy for leveraged retail participation) rose 4% m-m to a record high of Rmb3.0tn.

Exhibit 10: SSE registered new accounts – Slight pick-up in June  
SSE registered new account (mn units)  
![](images/24378e84ba32af0dc07c2d311adb9ea78ca90d3736ccd2d786da34e0849029ad.jpg)  
Source: CEIC, MS. Data as of Jun 2026.

Exhibit 11: Daily average of A-share small orders net inflow – Inflows dropped significantly in June  
Daily average of total A-share small orders net flow (Rmb bn)  
![](images/b8dbd30b82d9c205817eea45d6e0bd6d92604c367369e147abb340825ade2646.jpg)  
Note: Small order refers to these below Rmb40,000.
Source: Wind, MS. Data as of Jun, 2026.

Exhibit 12: A-share total margin financing balance and m-m % – Another historical high in June with 4% m-m increase

![](images/ffe33dffedd031d12432bf18eab80fe8c434795b0ecb75d97435261c9ac8938c.jpg)  
Source: CEIC, MS. Data as of Jun 2026.

Domestic liquidity remained supportive, with private funds and active

## mutual funds continuing to see AUM growth.

\- Private fund AUM recorded a slight increase of Rmb69bn in May (vs. Rmb386bn in April). Since mid-2025, total private fund AUM has risen by 42%, highlighting a sustained recovery in domestic risk appetite (Exhibit 13).

\- Mutual active fund continued steady AUM increase: Onshore equity funds (mostly ETFs) saw a slight AUM decline of Rmb12bn in June, while onshore hybrid funds (mostly active funds) recorded a steady AUM increase of Rmb45bn (Exhibit 14).

Exhibit 13: Onshore private equity funds AUM – Strong AUM increase indicates active HNWI participation in equity market  
![](images/34c0ebb515f2dddb4198aaf1c261a5d69208f8fa1ba5d2f07ac30f44a59189d7.jpg)  
Source: Wind, MS. Data as of May 2026.

Exhibit 14: Onshore mutual funds AUM (equity and hybrid funds)  
![](images/3c55e0326fec93421cbe0b4d2e035f56f633bdda0a4c790669fe52f0c24b5b6c.jpg)  
Source: Wind, MS. Data as of Jun 2026.

Exhibit 15: Onshore mutual funds AUM (bond and money market funds)  
![](images/9919110bee4dec35787b316ecac90bd23681e8c4881df362bc7c77bd35a76bd4.jpg)  
Source: Wind, MS. Data as of Jun 2026.

Exhibit 16: China onshore mutual funds AUM, 2014-YTD2026  
![](images/8f6eb7bf920b625964bb86bb182750656fc24f9eec217ae1c134d5544757d858.jpg)  
Source: Wind, MS. Data as of Jun 2026.

Exhibit 17: China onshore mutual funds AUM net increase, 2014-YTD2026  
![](images/f91f5ea33458a7ea3e4bcaf9f3d5c23fc07dd68319c2f6ede97d219ddfd29e71.jpg)  
Source: Wind, MS. Data as of Jun 2026.

## Northbound proxy: Foreign passive into A-shares reversed to outflows in June

The northbound net flow daily data disclosure was terminated as of August 19, 2024. As an alternative, we look at foreign passive funds flow to CSI 300 as it shows a good correlation with northbound net flow historically.

Foreign passive funds tracking CSI 300 reversed to outflows in June, after two months of inflows in April and May.

Exhibit 18: Proxy of northbound net flow – foreign-domiciled passive funds flow to CSI 300  
![](images/5b89557991c6e4f5eb36429d06104d41dbb360b9a2070450ef0617496ca9cfb5.jpg)  
Source: EPFR, MS. Note: Data as of August 16, 2024.

Exhibit 19: Cumulative fund flows in CSI 300 by foreign-domiciled passive funds  
![](images/6b9ffc034850acaee50dd2e6d3c4f3864114376c6e59f68a158aff57fa4471a2.jpg)  
Source: EPFR, MS. Note: Data as of Jun 30, 2026.

# Fund Positions Changes vs. Last Month – Top 50 Mutual Fund Holdings

Exhibit 20: Top 50 China/HK holdings among long-only EM and China active managers vs. last month

<table><tr><td rowspan="2">Ticker</td><td rowspan="2">Company Name</td><td rowspan="2">GICS Industry Group</td><td colspan="4">International &amp; US Funds</td><td colspan="3">International Funds - UCITS</td><td colspan="3">US Funds</td></tr><tr><td>Portfolio Composite Weights</td><td>MSCI China Index Weights</td><td>Active Weights</td><td>Active Wgt. Changes vs. last month</td><td>Portfolio Composite Weights</td><td>Active Weights</td><td>Active Wgt. Changes vs. last month</td><td>Portfolio Composite Weights</td><td>Active Weights</td><td>Active Wgt. Changes vs. last month</td></tr><tr><td>700-HK</td><td>Tencent Holdings</td><td>Media &amp; Entertainment</td><td>14.3%</td><td>13.4%</td><td>0.9%</td><td>1.7%</td><td>11.5%</td><td>-1.9%</td><td>1.5%</td><td>17.5%</td><td>4.1%</td><td>1.7%</td></tr><tr><td>9988-HK</td><td>Alibaba Group Holding</td><td>Consumer Discretionary Distribution &amp; Retail</td><td>7.6%</td><td>10.2%</td><td>-2.6%</td><td>-1.4%</td><td>6.7%</td><td>-3.4%</td><td>-1.3%</td><td>8.5%</td><td>-1.6%</td><td>-1.5%</td></tr><tr><td>300750-CN</td><td>Contemporary Amperex Technology</td><td>Capital Goods</td><td>5.0%</td><td>1.3%</td><td>3.7%</td><td>-0.1%</td><td>4.8%</td><td>3.5%</td><td>-0.1%</td><td>5.2%</td><td>3.9%</td><td>0.0%</td></tr><tr><td>939-HK</td><td>China Construction Bank</td><td>Banks</td><td>3.1%</td><td>4.1%</td><td>-1.0%</td><td>-0.2%</td><td>2.4%</td><td>-1.6%</td><td>0.0%</td><td>3.9%</td><td>0.2%</td><td>-0.5%</td></tr><tr><td>2318-HK</td><td>Ping An Insurance Group</td><td>Insurance</td><td>2.8%</td><td>2.2%</td><td>0.7%</td><td>-0.5%</td><td>3.0%</td><td>0.9%</td><td>-0.4%</td><td>2.6%</td><td>0.5%</td><td>-0.7%</td></tr><tr><td>1299-HK</td><td>AIA Group</td><td>Insurance</td><td>2.6%</td><td>0.0%</td><td>2.6%</td><td>-0.3%</td><td>2.2%</td><td>2.2%</td><td>-0.3%</td><td>3.1%</td><td>3.1%</td><td>-0.2%</td></tr><tr><td>9999-HK</td><td>NetEase</td><td>Media &amp; Entertainment</td><td>2.3%</td><td>1.7%</td><td>0.6%</td><td>0.1%</td><td>2.6%</td><td>0.9%</td><td>0.1%</td><td>2.0%</td><td>0.3%</td><td>0.1%</td></tr><tr><td>688008-CN</td><td>Montage Technology</td><td>Semiconductors &amp; Semiconductor Equipment</td><td>2.0%</td><td>0.1%</td><td>1.9%</td><td>0.3%</td><td>2.0%</td><td>1.9%</td><td>0.3%</td><td>1.9%</td><td>1.8%</td><td>0.3%</td></tr><tr><td>3968-HK</td><td>China Merchants Bank</td><td>Banks</td><td>1.7%</td><td>1.2%</td><td>0.5%</td><td>0.0%</td><td>2.1%</td><td>0.9%</td><td>0.0%</td><td>1.2%</td><td>0.1%</td><td>0.0%</td></tr><tr><td>2899-HK</td><td>Zijin Mining Group</td><td>Materials</td><td>1.7%</td><td>1.2%</td><td>0.5%</td><td>0.0%</td><td>1.3%</td><td>0.1%</td><td>0.0%</td><td>2.2%</td><td>1.0%</td><td>-0.1%</td></tr><tr><td>688012-CN</td><td>Advanced Micro-Fabrication Equipment</td><td>Semiconductors &amp; Semiconductor Equipment</td><td>1.5%</td><td>0.1%</td><td>1.4%</td><td>0.9%</td><td>1.5%</td><td>1.4%</td><td>0.9%</td><td>1.5%</td><td>1.4%</td><td>0.9%</td></tr><tr><td>2359-HK</td><td>WuXi AppTec</td><td>Pharmaceuticals Biotechnology &amp; Life Sciences</td><td>1.4%</td><td>0.3%</td><td>1.1%</td><td>0.4%</td><td>0.8%</td><td>0.5%</td><td>0.3%</td><td>2.0%</td><td>1.7%</td><td>0.5%</td></tr><tr><td>000333-CN</td><td>Midea Group</td><td>Consumer Durables &amp; Apparel</td><td>1.3%</td><td>0.3%</td><td>1.0%</td><td>-0.1%</td><td>1.3%</td><td>1.0%</td><td>0.0%</td><td>1.3%</td><td>1.0%</td><td>-0.1%</td></tr><tr><td>1211-HK</td><td>BYD</td><td>Automobiles &amp; Components</td><td>1.3%</td><td>1.8%</td><td>-0.6%</td><td>0.0%</td><td>0.6%</td><td>-1.2%</td><td>0.2%</td><td>2.0%</td><td>0.1%</td><td>-0.1%</td></tr><tr><td>HTHT-US</td><td>H World Group</td><td>Consumer Services</td><td>1.1%</td><td>0.3%</td><td>0.8%</td><td>0.0%</td><td>1.0%</td><td>0.6%</td><td>0.0%</td><td>1.3%</td><td>1.0%</td><td>0.0%</td></tr><tr><td>PDD-US</td><td>PDD Holdings</td><td>Consumer Discretionary Distribution &amp; Retail</td><td>1.1%</td><td>2.3%</td><td>-1.2%</td><td>0.0%</td><td>1.3%</td><td>-1.0%</td><td>0.0%</td><td>0.9%</td><td>-1.4%</td><td>-0.1%</td></tr><tr><td>300308-CN</td><td>Zhongji Innolight</td><td>Technology Hardware &amp; Equipment</td><td>1.1%</td><td>0.4%</td><td>0.7%</td><td>0.1%</td><td>1.3%</td><td>0.8%</td><td>0.1%</td><td>0.9%</td><td>0.4%</td><td>0.0%</td></tr><tr><td>002371-CN</td><td>NAURA Technology Group</td><td>Semiconductors &amp; Semiconductor Equipment</td><td>1.1%</td><td>0.2%</td><td>0.9%</td><td>0.3%</td><td>1.2%</td><td>1.0%</td><td>0.5%</td><td>0.9%</td><td>0.8%</td><td>0.1%</td></tr><tr><td>600519-CN</td><td>Kweichow Moutai</td><td>Food Beverage &amp; Tobacco</td><td>1.0%</td><td>0.6%</td><td>0.5%</td><td>-0.1%</td><td>1.2%</td><td>0.6%</td><td>-0.1%</td><td>0.9%</td><td>0.3%</td><td>-0.2%</td></tr><tr><td>300124-CN</td><td>Shenzhen Inovance Technology</td><td>Capital Goods</td><td>1.0%</td><td>0.0%</td><td>1.0%</td><td>-0.1%</td><td>0.7%</td><td>0.7%</td><td>-0.1%</td><td>1.3%</td><td>1.3%</td><td>-0.1%</td></tr><tr><td>002028-CN</td><td>Sieyuan Electric</td><td>Capital Goods</td><td>1.0%</td><td>0.0%</td><td>1.0%</td><td>-0.1%</td><td>0.9%</td><td>0.9%</td><td>-0.1%</td><td>1.2%</td><td>1.2%</td><td>-0.2%</td></tr><tr><td>2628-HK</td><td>China Life Insurance</td><td>Insurance</td><td>0.9%</td><td>1.1%</td><td>-0.2%</td><td>0.0%</td><td>0.4%</td><td>-0.7%</td><td>0.0%</td><td>1.4%</td><td>0.3%</td><td>0.1%</td></tr><tr><td>2328-HK</td><td>PICC Property &amp; Casualty</td><td>Insurance</td><td>0.8%</td><td>0.5%</td><td>0.3%</td><td>

[中间内容因长度限制已省略]

nal Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital

Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## © 2026 MS
"""
