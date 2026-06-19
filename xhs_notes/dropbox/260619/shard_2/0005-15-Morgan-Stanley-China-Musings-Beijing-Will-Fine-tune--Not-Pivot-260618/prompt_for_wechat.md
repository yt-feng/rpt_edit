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
## China Musings | Asia Pacific

# Beijing Will Fine-tune, Not Pivot

April-May data indicate China's two-speed economy is deepening with weaker domestic demand. This should raise policy urgency at home, with faster fiscal rollout targeting strategic infrastructure. Abroad, manufacturing strength amid weak domestic absorption may fuel targeted protectionist measures.

China's two-speed economy is becoming harder to ignore. While exports and production remain resilient, April-May data point to a clearer softening in domestic demand. We think this slowdown in domestic demand does not signal an abrupt downturn that warrants policy pivot; however, the need for policy fine-tuning is rising. Abroad, the widening K-shaped pattern may intensify trade frictions.

Domestic demand is cooling, not slumping. April-May data confirm a deepening two-speed pattern: production and exports remain firm, while consumption and investment are softening. The key question is whether the slowdown is partly reversible or signals the start of an organic deceleration that could become concerning enough for policymakers to “pivot” rather than merely “fine-tune” policy implementation. Our view is that the moderation is real, but headline YoY figures for FAI and retail sales likely overstate the pace of slowdown. As such, we expect policy to be fine-tuned rather than pivoted.

(1) FAI data – direction matters more than magnitude: The post-February deceleration appears partly policy-driven. The central government's emphasis on a “correct view of performance and achievements” since late February may have pushed local governments away from new projects and toward resolving hidden debt (Exhibit 2). Some previously overstated and front-loaded FAI reporting may also be corrected.

(2) Consumption is confronting a high base from trade-in programs...: The negative YoY retail sales in May largely reflects a high base from last year's trade-in subsidy program (Exhibit 1). On a two-year CAGR basis, May looks slightly better than April.

...although the slowdown is more than a base effect. The 2Y CAGR in April-May still shows a visible step-down from 1Q. A softer labor market, ongoing property market adjustment, and oil-related pressures are weighing on spending. Meanwhile, export strength has had limited spillover into the job market due to automation and rising capital intensity. These are reflected in renewed softening in the NBS consumer confidence index (Exhibit 4).

(continued on the next page)

MS ASIA LIMITED

## Robin Xing

Chief China Economist

Robin.Xing@morganstanley.com +852 2848-6511

## Jenny Zheng, CFA

Economist

Jenny.L.Zheng@morganstanley.com +852 3963-4015

## Zhipeng Cai

Economist

Zhipeng.Cai@morganstanley.com +852 2239-7820

## Harry Zhao

Economist

Harry.Zhao@morganstanley.com +852 2239-7229

## Asia Summer School 2026

![](images/aefcc785c71dd364fe7ff3eb1d065a0441c50f9b3323599a71b9ffaab505b3fc.jpg)

## 中国思考

查看同系列内容>

![](images/a4cfeba6c273b9ceb50fab9a8ef87d0b1cfc6b8dd7b4961edeb687e8426a0b68.jpg)

<details>
<summary>natural_image</summary>

Tea set with teapot and three cups on a bamboo mat, green blurred background (no text or symbols)
</details>

## Continued Musings

(3) The perspective from oil – growth drag manageable, but reinforces the K-shaped economy: Investors have questioned whether the slump in crude imports, combined with limited evidence of strategic reserve drawdowns, signals a collapse in China's oil consumption – and, by extension, economic activity. Our view is that this is only partly the case. Consumers appear to be cutting back on non-essential oil consumption, including ICE vehicle usage (Exhibit 5) and air travel (Exhibit 6). However, overall industrial activity appears to be cushioned by several buffers: commercial crude inventories, resilient coal imports and domestic coal production, and still-robust electricity generation (Exhibit 7).

Domestic policy implication – renewed urgency for fiscal fine-tuning, with scope for catch-up: Softer April-May data now challenge policy complacency after a strong 1Q. 2Q GDP is tracking around 4.4%. If unaddressed, full-year growth could approach, or undershoot, the lower end of the 4.5-5% target range. This raises the need for policy fine-tuning rather than a broad pivot. In our view, the near-term response will likely focus on faster implementation of approved budgets, a stance that should be reaffirmed at the July Politburo meeting. The room for catch-up is visible: \~60% of the annual government bond quota remains unused. More importantly, rollout of the Rmb800bn in quasi-fiscal financing tools for infrastructure – as proxied by policy bank bond issuance in Exhibit 3 – remains slow.

Beijing's preferred demand support remains strategic infrastructure: Specifically, the focus is on projects that stabilize near-term growth while advancing longer-term goals around energy security, technology self-sufficiency, and supply-chain resilience. The "Six Networks" framework provides the clearest policy bridge: water management, new-type power grids, computing-power networks, next-generation communications, urban underground pipelines, and logistics infrastructure. Within this framework, AI computing networks, data centers, and smart grids are likely to see the most immediate support. On the other hand, we do not expect to see major pivotal policies targeting private consumption. The economy will likely remain distinctly K-shaped even with additional domestic demand support.

Is our above-consensus 4.8% GDP forecast still reachable? In our base case, growth reaccelerates to around 4.8-4.9%Y in 2H, as aforementioned policy easing on domestic demand is complemented by a partial unwind of the oil overhang. With progress toward a US-Iran peace deal, our global oil strategist now expects dated Brent to settle at around US\$80/bbl from 4Q26 onward, indicating a more balanced supply-demand outlook. For China, lower energy prices would reduce terms-of-trade losses and indirectly support exports by reinforcing the global trade and investment cycle. Consistent with this, our Asia economists now see modest upside risks to the region's growth outlook and have greater conviction in the ongoing industrial and capex super-cycle.

The deepening two-speed economy has an external corollary: Weak domestic absorption means more of China's manufacturing output is being directed toward export markets, accelerating market share gains abroad. This is most visible in the EU, where the bilateral trade relationship has arguably become increasingly competitive rather than complementary. China's share in steel, EVs, batteries, solar, and chemicals has risen meaningfully over the past two years. Europe's response, if any, is likely to be targeted

rather than systemic. Policy tools may include sector-specific tariffs, foreign-subsidy investigations, procurement restrictions, domestic content rules, and anti-dumping measures. While this is unlikely to become a major macro shock — particularly given China's countermeasure leverage in areas such as rare earths and luxury goods imports — the direction of travel matters. If Europe progressively narrows access in high-value manufacturing segments, China's export engine risks being redirected toward lower-friction but lower-margin markets.

Exhibit 1: Retail sales YoY weakened due to a high base and a softening job market  
![](images/c8fac0cf197fcd84a95ba388e47510163776f69f980486c295b08234eb538a80.jpg)

<details>
<summary>line chart</summary>

| Month    | Goods Retail sales ex Consumer Trade-in Goods | Housing Related Consumption | Automobiles | Mobile Phone |
|----------|--------------------------------------------------|------------------------------|-------------|--------------|
| Nov-23   | ~8%                                              | ~0%                          | ~15%        | ~17%         |
| Feb-24   | ~4%                                              | ~0%                          | ~10%        | ~18%         |
| May-24   | ~3%                                              | ~5%                          | ~-5%        | ~15%         |
| Aug-24   | ~3%                                              | ~0%                          | ~-5%        | ~15%         |
| Nov-24   | ~3%                                              | ~25%                         | ~5%         | ~25%         |
| Feb-25   | ~3%                                              | ~30%                         | ~0%         | ~30%         |
| May-25   | ~3%                                              | ~40%                         | ~0%         | ~35%         |
| Aug-25   | ~3%                                              | ~20%                         | ~0%         | ~15%         |
| Nov-25   | ~3%                                              | ~-15%                        | ~-10%       | ~20%         |
| Feb-26   | ~3%                                              | ~0%                          | ~-15%       | ~28%         |
| May-26   | ~3%                                              | ~-15%                        | ~-20%       | ~0%          |
</details>

Source: CEIC, MS.

Exhibit 2: Firm pace of resolving hidden debt after a relatively slow start  
![](images/a658b565476eea0ef875b76f0a4fb884f4ebfe9041601964fd4c22c01bb638ef.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 |
|-------|------|------|
| Jan   | 10%  | 10%  |
| Feb   | 45%  | 35%  |
| Mar   | 65%  | 50%  |
| Apr   | 78%  | 60%  |
| May   | 79%  | 70%  |
| Jun   | 85%  | 80%  |
| Jul   | 90%  | -    |
| Aug   | 92%  | -    |
| Sep   | 95%  | -    |
| Oct   | 96%  | -    |
| Nov   | 98%  | -    |
| Dec   | 100% | -    |
</details>

Source: Wind, MS.

Exhibit 3: Policy bank bond issuance has seen a net contraction YTD  
![](images/8594005e6e1ea235d126a221a24368e4c6a7fbf67e22da59796d9539b36653c8.jpg)

<details>
<summary>line chart</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   | 0    | -100 | 0    | 0    | 100  |
| Feb   | 100  | 150  | -300 | 150  | -100 |
| Mar   | 350  | 400  | 100  | 100  | 0    |
| Apr   | -200 | 0    | 300  | -100 | -400 |
| May   | 150  | 150  | 200  | 200  | 0    |
| Jun   | 350  | 200  | 150  | 300  | 150  |
| Jul   | 50   | 150  | 100  | 200  | 150  |
| Aug   | 300  | -100 | 50   | 450  | 150  |
| Sep   | 450  | 50   | 50   | 50   | 150  |
| Oct   | 250  | 150  | 350  | 50   | 150  |
| Nov   | 150  | 250  | 150  | 150  | 150  |
| Dec   | 150  | -100 | -100 | -100 | -100 |
</details>

Source: CEIC, MS.

Exhibit 4: Consumer confidence has dipped again after a period of modest improvement  
![](images/c6427e1b2ca1dfef1991206286e8a641da95f82f46e49fa2daf61f3d0eff4674.jpg)

<details>
<summary>line chart</summary>

| Date   | Consumer Confidence Index |
|--------|---------------------------|
| Oct-15 | 105                       |
| Apr-16 | 100                       |
| Oct-16 | 105                       |
| Apr-17 | 110                       |
| Oct-17 | 120                       |
| Apr-18 | 125                       |
| Oct-18 | 120                       |
| Apr-19 | 125                       |
| Oct-19 | 125                       |
| Apr-20 | 120                       |
| Oct-20 | 125                       |
| Apr-21 | 120                       |
| Oct-21 | 120                       |
| Apr-22 | 85                        |
| Oct-22 | 95                        |
| Apr-23 | 85                        |
| Oct-23 | 85                        |
| Apr-24 | 85                        |
| Oct-24 | 85                        |
| Apr-25 | 85                        |
| Oct-25 | 90                        |
| Apr-26 | 90                        |
</details>

Source: CEIC, MS.

Exhibit 5: Domestic flight weakened from 2Q amid the energy shock  
![](images/7f61fe33ebeca26da7fb11e26876691921db08b491a7d9e22ad4256b89094f9d.jpg)

<details>
<summary>line chart</summary>

| Month | 2023   | 2024   | 2025   | 2026   |
|-------|--------|--------|--------|--------|
| Jan   | 70000  | 98000  | 105000 | 95000  |
| Feb   | 95000  | 105000 | 110000 | 115000 |
| Mar   | 90000  | 95000  | 105000 | 115000 |
| Apr   | 95000  | 98000  | 102000 | 105000 |
| May   | 105000 | 108000 | 115000 | 102000 |
| Jun   | 102000 | 98000  | 112000 | 85000  |
| Jul   | 115000 | 112000 | 118000 | 115000 |
| Aug   | 118000 | 115000 | 115000 | 118000 |
| Sep   | 115000 | 112000 | 118000 | 115000 |
| Oct   | 118000 | 115000 | 112000 | 118000 |
| Nov   | 95000  | 98000  | 95000  | 95000  |
| Dec   | 92000  | 95000  | 98000  | 98000  |
</details>

Source: CEIC, MS.

Exhibit 6: Domestic petroleum retail volume slumped  
![](images/8dd11e7578bac6ddcd7925a5f3b0b05146418cded59ab7d3d71c6fccb2e093fb.jpg)

<details>
<summary>line chart</summary>

| Month    | Crude petroleum import (quantity) | Retail sales of petroleum (real) |
| -------- | --------------------------------- | -------------------------------- |
| Feb-22   | -20%                              | 0%                               |
| May-22   | 10%                               | -10%                             |
| Aug-22   | -10%                              | -5%                              |
| Nov-22   | 15%                               | -10%                             |
| Feb-23   | 20%                               | 5%                               |
| May-23   | 45%                               | 20%                              |
| Aug-23   | 30%                               | 15%                              |
| Nov-23   | 10%                               | 5%                               |
| Feb-24   | 5%                                | 0%                               |
| May-24   | -10%                              | -5%                              |
| Aug-24   | -5%                               | 0%                               |
| Nov-24   | 15%                               | 5%                               |
| Feb-25   | -5%                               | 0%                               |
| May-25   | 10%                               | 5%                               |
| Aug-25   | 5%                                | 0%                               |
| Nov-25   | 10%                               | -5%                              |
| Feb-26   | 15%                               | -10%                             |
| May-26   | -30%                              | -20%                             |
</details>

Source: CEIC, MS.

Exhibit 7: Electricity generation remains robust  
![](images/ad55e7f0e2a41fae1c2e88c36d179cabd270bf6577df8dd6597d634e4845310f.jpg)

<details>
<summary>line chart</summary>

| Month   | Total  | Thermal | Renewable |
|---------|--------|---------|-----------|
| Jan-24  | 9.0%   | 10.0%   | 5.0%      |
| Mar-24  | 3.0%   | 1.0%    | 8.0%      |
| May-24  | 2.0%   | -5.0%   | 25.0%     |
| Jul-24  | 6.0%   | -3.0%   | 23.0%     |
| Sep-24  | 5.0%   | 9.0%    | 1.0%      |
| Nov-24  | 1.0%   | -1.0%   | 0.0%      |
| Jan-25  | -1.0%  | -4.0%   | 12.0%     |
| Mar-25  | 2.0%   | -2.0%   | 13.0%     |
| May-25  | 1.0%   | -1.0%   | 0.0%      |
| Jul-25  | 3.0%   | 4.0%    | 3.0%      |
| Sep-25  | 8.0%   | -5.0%   | 17.0%     |
| Nov-25  | 7.0%   | -3.0%   | 19.0%     |
| Jan-26  | 3.0%   | -1.0%   | 6.0%      |
| Mar-26  | 1.0%   | 4.0%    | -5.0%     |
| May-26  | 4.0%   | 3.0%    | 9.0%      |
</details>

Source: CEIC, MS.

## Disclosure Section

Information and opinions in MS were prepared or are disseminated by one or more of the following, which accept responsibility for its contents: MS Asia Limited, and/or MS Asia (Singapore) Pte. (Registration number 199206298Z) and/or MS Asia (Singapore) Securities Pte Ltd (Registration number 200008434H), regulated by the Monetary Authority of Singapore (which accepts legal responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS), and/or MS Taiwan Limited and/or MS & Co International plc, Seoul Branch, and/or MS Australia Limited (A.B.N. 67 003 734 576, holder of Australian financial services license No. 233742), and/or MS Wealth Management Australia Pty Ltd (A.B.N. 19 009 145 555, holder of Australian financial services license No. 240813, and/or MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105), Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com which accepts the responsibility for its contents and should be contacted with respect to any matters arising from, or in connection with, MS and their affiliates (collectively, "MS"). MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or Morg

[中间内容因长度限制已省略]

ccepts responsibility for its contents; in Korea by MS & Co International plc, Seoul Branch; in India by MS India Company Private Limited having Corporate Identification No (CIN) U22990MH1998PTC115305, regulated by the Securities and Exchange Board of India ("SEBI") and holder of licenses as a Research Analyst (SEBI Registration No. INH000001105); Stock Broker (SEBI Stock Broker Registration No. INZ000244438), Merchant Banker (SEBI Registration No. INM000011203), and depository participant with National Securities Depository Limited (SEBI Registration No. IN-DP-NSDL-567-2021) having registered office at Altimus, Level 39 & 40, Pandurang Budhkar Marg, Worli, Mumbai 400018, India; Telephone no. +91-22-61181000; Compliance Officer Details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the United States by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

© 2026 MS
"""
