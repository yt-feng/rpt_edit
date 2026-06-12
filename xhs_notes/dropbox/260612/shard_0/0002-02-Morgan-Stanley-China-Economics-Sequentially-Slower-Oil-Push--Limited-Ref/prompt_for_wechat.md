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
# China Economics | Asia Pacific

# Sequentially Slower Oil Push, Limited Reflation Elsewhere

## Key Takeaways

PPI YoY surged to a \~4-year high of 3.9% (Consensus 3.7%) on a low base, yet MoM slipped 1.2pp to 0.5% on reduced oil price impulse.  
■ Stabilized global oil prices also led to softened retail fuel prices and transportation cost, bringing seasonally adjusted CPI MoM down 50bps to 0.1%  
Limited reflation beyond oil: Some modest uptick in coal and non-ferrous metal, muted price changes in downstream PPI, softened core CPI excluding gold.  
While PPI may rise $>4\%$ Y in Jun-Jul off a low base, core CPI will likely enter a shallow moderating path. Tail risk remains a non-linear oil price spike.

Narrow industrial reflation beyond oil: May PPI MoM softened on a sequentially slower oil uptick. Excluding oil & petrochemical, PPI MoM edged up 10bps to 0.3%, led by coal (seasonally stronger summer electricity demand) and non-ferrous metals (Al-related capex demand). Downstream factory prices held flat at 0.2% MoM despite broadening export strength, constrained by prevailing excess capacity.

Limited transmission of AI demand and oil to core CPI: On a seasonally adjusted basis, core CPI ex-gold MoM softened 20bps to 0% as the impulse from AI-driven replacement demand for personal electronics faded. Price upside would be capped by continued consumption weakness amid sluggish job market and ongoing property adjustment, with limited support from capital-intensive export strength.

Outlook: Despite somewhat stabilized global oil prices, PPI YoY will likely rise >4% in Jun-Jul, given a low base. That said, core CPI will likely enter a shallow moderating path ahead, given continued consumption weakness. The key risk remains a non-linear oil price spike if prolonged geopolitical disruptions cause a more severe supply shortage – our oil strategist has lifted 4Q26 and 1H27 oil price forecasts by US\$5/bbl, in view of a slower resumption of Strait production.

MS ASIA LIMITED

Jenny Zheng, CFA

Economist

Jenny.L.Zheng@morganstanley.com +852 3963-4015

Harry Zhao

Economist

Harry.Zhao@morganstanley.com +852 2239-7229

Robin Xing

Chief China Economist

Robin.Xing@morganstanley.com +852 2848-6511

Zhipeng Cai

Economist

Zhipeng.Cai@morganstanley.com +852 2239-7820

## Asia Summer School 2026

![](images/098043ec025d9ffc6db836a74124d3cc702f382dd4b56ab6f2a919011b4c504c.jpg)

Exhibit 1 : Summary Table

<table><tr><td></td><td>May-26</td><td>Apr-26</td><td>Mar-26</td><td>1Q26</td><td>4Q25</td></tr><tr><td>CPI, YoY %</td><td>1.2</td><td>1.2</td><td>1.0</td><td>0.8</td><td>0.6</td></tr><tr><td>Food</td><td>-1.7</td><td>-1.6</td><td>0.3</td><td>0.4</td><td>-0.5</td></tr><tr><td>Non-food</td><td>1.9</td><td>1.8</td><td>1.2</td><td>1.0</td><td>0.8</td></tr><tr><td>Core (excl. Food and Energy)</td><td>1.1</td><td>1.2</td><td>1.1</td><td>1.2</td><td>1.2</td></tr><tr><td>CPI, MoM %, NSA</td><td>-0.1</td><td>0.3</td><td>-0.7</td><td>0.2</td><td>0.1</td></tr><tr><td>Food</td><td>-0.4</td><td>-1.6</td><td>-2.7</td><td>-0.3</td><td>0.4</td></tr><tr><td>Non-food</td><td>-0.1</td><td>0.7</td><td>-0.2</td><td>0.3</td><td>0.0</td></tr><tr><td>Core (excl. Food and Energy)</td><td>-0.1</td><td>0.2</td><td>-0.7</td><td>0.1</td><td>0.1</td></tr><tr><td>PPI, YoY % (broad breakdown)</td><td>3.9</td><td>2.8</td><td>0.5</td><td>-0.6</td><td>-2.1</td></tr><tr><td>Producer Goods</td><td>5.2</td><td>3.8</td><td>1.0</td><td>-0.3</td><td>-2.3</td></tr><tr><td>Mining and Quarrying</td><td>15.8</td><td>10.6</td><td>2.0</td><td>-3.8</td><td>-6.2</td></tr><tr><td>Raw Material</td><td>9.2</td><td>7.1</td><td>1.1</td><td>-0.9</td><td>-2.7</td></tr><tr><td>Capital Goods</td><td>2.3</td><td>1.5</td><td>0.9</td><td>0.3</td><td>-1.8</td></tr><tr><td>Consumer Goods</td><td>-0.8</td><td>-1.0</td><td>-1.3</td><td>-1.5</td><td>-1.4</td></tr><tr><td>Durables</td><td>0.0</td><td>-0.3</td><td>-1.0</td><td>-1.5</td><td>-3.4</td></tr><tr><td>PPI, MoM % (select sectors)</td><td>0.5</td><td>1.7</td><td>1.0</td><td>0.6</td><td>0.1</td></tr><tr><td>Non-commodity, MoM %</td><td>0.5</td><td>1.2</td><td>0.5</td><td>0.4</td><td>0.0</td></tr><tr><td>General Equipment</td><td>0.0</td><td>0.0</td><td>-0.2</td><td>-0.1</td><td>-0.1</td></tr><tr><td>Automobile</td><td>-0.2</td><td>0.1</td><td>-0.5</td><td>-0.2</td><td>-0.1</td></tr><tr><td>Electrical Machinery &amp; Equipment</td><td>0.5</td><td>0.3</td><td>1.1</td><td>1.2</td><td>0.2</td></tr><tr><td>Consumer Electronics</td><td>0.6</td><td>0.6</td><td>0.7</td><td>0.6</td><td>0.0</td></tr><tr><td>Textile</td><td>0.7</td><td>0.7</td><td>0.5</td><td>0.1</td><td>0.0</td></tr><tr><td>Chemical Fibers</td><td>1.5</td><td>5.6</td><td>3.4</td><td>1.5</td><td>-0.5</td></tr><tr><td>Pharmaceutical</td><td>-0.4</td><td>-0.4</td><td>-0.1</td><td>-0.5</td><td>-0.3</td></tr><tr><td>Commodity, MoM %</td><td>0.5</td><td>2.9</td><td>2.1</td><td>1.1</td><td>0.4</td></tr><tr><td>Oil</td><td>0.0</td><td>17.5</td><td>10.8</td><td>3.7</td><td>-1.4</td></tr><tr><td>Coal</td><td>3.2</td><td>1.9</td><td>0.1</td><td>-1.2</td><td>2.3</td></tr><tr><td>Ferrous Metal Smelting</td><td>1.2</td><td>0.6</td><td>0.3</td><td>0.2</td><td>-0.4</td></tr><tr><td>Non Ferrous Metal Smelting</td><td>1.1</td><td>0.2</td><td>1.0</td><td>3.6</td><td>2.4</td></tr></table>

Source: CEIC, MS

Exhibit 2: Sequentially oil push slowed, limited reflation elsewhere  
![](images/00b63ffcf0100c4dcfdb595f37d4c7e5c23a4e33b63282c9a01e203c8c41942f.jpg)

<details>
<summary>bar chart</summary>

| Month   | Non-ferrous Metals | Non-ferrous Metals Downstream | Coal  | Oil & Petrochemical | Remainder | PPI MoM |
|---------|--------------------|----------------------------------|-------|---------------------|-----------|---------|
| Jan-25  | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Feb     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Mar     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Apr     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| May     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Jun     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Jul     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Aug     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Sep     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Oct     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Nov     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Dec     | -0.1%              | -0.1%                            | -0.1% | -0.1%               | -0.1%     | -0.1%   |
| Jan-26  | 0.4%               | 0.4%                             | 0.4%  | 0.4%                | 0.4%      | 0.4%    |
| Feb     | 0.4%               | 0.4%                             | 0.4%  | 0.4%                | 0.4%      | 0.4%    |
| Mar     | 0.4%               | 0.4%                             | 0.4%  | 0.4%                | 0.4%      | 0.4%    |
| Apr     | 1.6%               | 1.6%                             | 1.6%  | 1.6%                | 1.6%      | 1.6%    |
| May     | 0.4%               | 0.4%                             | 0.4%  | 0.4%                | 0.4%      | 0.4%    |
</details>

Source: NBS, MS

For important disclosures, refer to the Disclosure Section, located at the end of this report.

## Disclosure Section

Information and opinions in MS were prepared or are disseminated by one or more of the following, which accept responsibility for its contents: MS Asia Limited, and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Disclosures

MS is not acting as a municipal advisor and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of Section 975 of the Dodd-Frank Wall Street Reform and Consumer Protection Act.

MS does not provide individually tailored investment advice. MS has been prepared without regard to the circumstances and objectives of those who receive it. MS recommends that investors independently evaluate particular investments and strategies, and encourages investors to seek the advice of a financial adviser. The appropriateness of an investment or strategy will depend on an investor's circumstances and objectives. The securities, instruments, or strategies discussed in MS may not be suitable for all investors, and certain investors may not be eligible to purchase or participate in some or all of them. MS is not an offer to buy or sell or the solicitation of an offer to buy or sell any security/instrument or to participate in any particular trading strategy. The value of and income from your investments may vary because of changes in interest rates, foreign exchange rates, default rates, prepayment rates, securities/instruments prices, market indexes, operational or financial conditions of companies or other factors. There may be time limitations on the exercise of options or other rights in securities/instruments transactions. Past performance is not necessarily a guide to future performance. Estimates of future performance are based on assumptions that may not be realized. If provided, and unless otherwise stated, the closing price on the cover page is that of the primary exchange for the subject company's securities/instruments.

The fixed income research analysts, strategists or economists principally responsible for the preparation of MS have received compensation based upon various factors, including quality, accuracy and value of research, firm profitability or revenues (which include fixed income trading and capital markets profitability or revenues), client feedback and competitive factors. Fixed Income Research analysts', strategists' or economists' compensation is not linked to investment banking or capital markets transactions performed by MS or the profitability or revenues of particular trading desks.

With the exception of information regarding MS, MS is based on public information. MS makes every effort to use reliable, comprehensive information, but we make no representation that it is accurate or complete. We have no obligation to tell you when opinions or information in MS change apart from when we intend to discontinue equity research coverage of a subject company. Facts and views presented in MS have not been reviewed by, and may not reflect information known to, professionals in other MS business areas, including investment banking personnel.

MS may make investment decisions that are inconsistent with the recommendations or views in this report.

To our readers based in Taiwan or trading in Taiwan securities/instruments: Information on securities/instruments that trade in Taiwan is distributed by MS Taiwan Limited ("MSTL"). Such information is for your reference only. The reader should independently evaluate the investment risks and is solely responsible for their investment decisions. MS may not be distributed to the public media or quoted or used by the public media without the express written consent of MS. Any non-customer reader within the scope of Article 7-1 of the Taiwan Stock Exchange Recommendation Regulations accessing and/or receiving MS is not permitted to provide MS to any third party (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities regarding MS which may create or give the appearance of creating a conflict of interest. Information on securities/instruments that do not trade in Taiwan is for informational purposes only and is not to be construed as a recommendation or a solicitation to trade in such securities/instruments. MSTL may not execute transactions for clients in these securities/instruments.

MS is not incorporated under PRC law and the research in relation to this report is conducted outside the PRC. MS does not constitute an offer to sell or the solicitation of an offer to buy any securities in the PRC. PRC investors shall have the relevant qualifications to invest in such securities and shall be responsible for obtaining all relevant approvals, licenses, verifications and/or registrations from the relevant governmental authorities themselves. Neither this report nor any part of it is intended as, or shall constitute, provision of any consultancy or advisory service of securities investment as defined under PRC law. Such information is provided for your reference only.

MS is disseminated in Brazil by MS C.T.V.M. S.A. located at Av. Brigadeiro Faria Lima, 3600, 6th floor, São Paulo - SP, Brazil; and is regulated by the Comissão de Valores Mobiliários; in Mexico by MS México, Casa de Bolsa, S.A. de C.V which is regulated by Comision Nacional Bancaria y de Valores. Paseo de los Tamarindos 90, Torre 1, Col. Bosques de las Lomas Floor 29, 05120 Mexico City; in Japan by MS MUFG Securities Co., Ltd. and, for Commodities related research reports only, MS Capital Group Japan Co., Ltd; in Hong Kong by MS Asia Limited (which accepts responsibility for its contents) and by MS Bank Asia Limited; in Singapore by MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of

Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS) and by MS Bank Asia Limited, Singapore Branch (Registration number T14FC0118); in Australia to "wholesale clients" within the meaning of the Australian Corporations Act by MS Australia Limited A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742, which accepts responsibility for its contents; in Australia to "wholesale clients" and "retail clients" within the meaning of the Australian Corporations Act by MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, which accepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
