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
1. `# 标题`：一句主判断，不超过 32 字。
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
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Internet | North America

# How Much Capacity Will \$2 Trillion of Hyperscaler Capex Bring By '27?

Compute capacity remains the key constraint and competitive differentiator as GenAI demand and inference scale. With \$2T in total hyperscaler capex upon us, we introduce a bottom-up model for cost/GW across GPUs and custom ASICs, and the GW capacity set to come online across each hyperscaler.

The Age of Inference is Here...GenAI capabilities continue advancing and gaining adoption across the economy, with hyperscale and mega-cap AI-enabled revenue streams inflecting, hyperscale product pipelines and backlogs building, and our economics and thematics teams seeing early AI-driven productivity boosts (see here and here).

...With '27 Hyperscaler Capex Expected to Surpass \$1 Trillion and an Aggregate \~\$2 Trillion Invested Since '24...The entire ecosystem remains compute constrained...with compute capacity the regulator to the pace of GenAI advances/ adoption. We view compute capacity (in the form of GW) as an increasingly important competitive differentiator. And with aggregate hyperscaler capex from '24-'27 now expected to reach \$2 trillion : 1) How much capacity has come on and will come on? 2) Is the cost to add capacity improving, set to improve or increasing? 3) What is the outlook for component inflation? 4) How large are GPUs vs custom ASICs now? 5) How does compute cost efficiency compare between chips? 6) Which companies are forward buying or building for out years?

...As Such, we Introduce a New Bottom-up Model Dissecting These GW Builds and Hyperscaler Capacity to Come... In collaboration with our colleagues in semiconductors, IT hardware/networking, software, and thematics we publish an updated multi-year bottom-up cost per GW analysis across NVDA's GPUs and other leading custom silicon architectures (TPU, Trainium, etc.) We also estimate GW deployed and to be deployed based on chip unit estimates. Please let us know if interested in our interactive bottom-up cost per GW and GW deployment models, which we hope are instructive in better understanding the "capital" portion of GenAI "return on invested capital"...and in assessing which companies have more or less compute driven competitive advantage over time.

We also detail 4 main debates and takeaways:

Debate 1: How much capacity will the hyperscalers (AMZN, GOOGL, META, MSFT) bring online in '26/'27?

\- Our View: We see AMZN, GOOGL, META, and MSFT adding an incremental 14 GW/20 GW in '26/'27...for context, we believe AWS's total capacity added

MS & CO. LLC

# Brian Nowak, CFA

Equity Analyst

Brian.Nowak@morganstanley.com +1 212 761-3365

# Keith Weiss, CFA

Equity Analyst

Keith.Weiss@morganstanley.com +1 212 761-4149

# Josh Baer, CFA

Equity Analyst

Josh.Baer@morganstanley.com +1 212 761-4223

# Julian Herrera

Research Associate

Julian.Herrera@morganstanley.com +1 212 761-1784

# Nikhil Javeri

Research Associate

Nikhil.Javeri1@morganstanley.com +1 212 761-3742

# Mason Wayne

Research Associate

Mason.Wayne@morganstanley.com +1 212 761-6012

# Ryan Lountzis

Research Associate

Ryan.Lountzis@morganstanley.com +1 212 761-3189

# Jonathan Eisenson

Research Associate

Jonathan.Eisenson@morganstanley.com +1 212 761-2808

# Gregory Gao

Research Associate

Greg.Gao@morganstanley.com +1 212 296-3125

# Jamie Reynolds

Research Associate

Jamie.Reynolds@morganstanley.com +1 212 761-2087

# INTERNET

North America

Industry View

Attractive

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

over its first \~18 years of existence (through YE24), was only \~5 GW...and 20 GW is enough to power 15 million+ US homes for a year...so capacity is coming

\- We see GOOGL (\~7 GW) again bringing on the most capacity in '27, followed by AMZN/MSFT (\~5 GW each). META's capex is only adding 3.5 GW, but when grossing up its hyperscale spend, we estimate META is really adding \~4 GW in '27.

# Debate 2: Where is the cost and compute efficiency gap between NVDA and Custom ASICs now and what are we monitoring to close that gap?

\- Our View: We estimate hyperscaler capex to build a 1 GW datacenter with current-gen NVDA GPUs (Blackwell) is up to \~2x the cost of current-gen custom ASICs (TPU, Trainium)...but compute power efficiency matters, and this is where NVDA shines...with compute performance/watt 2x-8x ahead of custom ASICs.

# Debate 3: Which hyperscalers are investing the most and least in forward year capacity yet to come on?

\- Our View: We see AMZN/MSFT/META doing the most forward purchasing/building (powered shells, land, equipment, memory, etc.) and estimate 50%+ of '26 AMZN/MSFT/META capex will come online in '27 and beyond. This is a potential positive for second derivative capex slowing and is a hedge against delays/component inflation. In contrast, we estimate only \~10% of '26 GOOGL capex is for '27 and beyond.

# Debate 4: Beyond the rack, which costs within the data center build have the most swing in driving cost of capacity higher or lower?

\- Our View: Networking (\~20%) and Powered Shells (\~HSD-low-teens%) are the largest sources of investment after racks. DRAM (single digit % of the cost) and HBM (\~MSD-mid-teens%) also pose upside risks to the rack prices that hyperscalers pay.

# MS

MS

![](images/1c8667ad8ec1e5a76a2b77926c79f6d448992aace53ed99f23fab110615cf586.jpg)

<details>
<summary>natural_image</summary>

Modern glass building facade with geometric window patterns and light reflections (no text or symbols)
</details>

# FOUNDATION

# How Much Capacity Will \$2 Trillion of Hyperscaler Capex Bring By 2027?

May 2026

Brian Nowak

+1 212 761-3365

Keith Weiss

+1 212 761-4149

Josh Baer

+1 212 761-4223

Julian Herrera

+1 212 761-1784

Nikhil Javeri

+1 212 761-3742

Mason Wayne

+1 212 761-6012

Ryan Lountzis

+1 212 761-3189

Jon Eisenson

+1 212 761-4149

Greg Gao

+1 212 296-3125

Jamie Reynolds

+1 212 761-2087

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

# MS

MS

# Executive Summary

The Age of Inference is Here...GenAI capabilities and offerings continue advancing and gaining adoption across the economy, with hyperscale and mega-cap AI-enabled revenue streams inflecting, hyperscale product pipelines and backlogs building, and our economics and thematics teams seeing early AI-driven productivity boosts (see here and here).

...With '27 Hyperscaler Capex Expected to Surpass \$1 trillion and an Aggregate \~\$2 trillion Invested since '24...The entire ecosystem remains compute constrained...with compute capacity the regulator to the pace of GenAI advances and adoption. We view compute capacity (in the form of GW) as an increasingly important competitive differentiator. In all, aggregate hyperscale data center spend is set to eclipse \~\$2 trillion from '24-'27, which raises multiple questions, including: 1) How much capacity has come on and will come on? 2) Is the cost to add capacity improving, set to improve or increasing? 3) What is the outlook for component inflation? 4) How large are GPUs vs custom ASICs now? 5) How does compute cost efficiency compare between chips? 6) Which companies are forward buying or building for out years?

...As Such, we Introduce a New Bottom-up Model Dissecting These GW Builds and Hyperscaler Capacity to Come... In collaboration with our colleagues in semiconductors, IT hardware/networking, software, and thematics we publish an updated multi-year bottom-up cost per GW analysis across NVDA's GPUs and other leading custom silicon architectures (TPU, Trainium, etc.) We also estimate GW deployed and to be deployed based on chip unit estimates. Please let us know if interested in our interactive bottom-up cost per GW and GW deployment models, which we hope are instructive in better understanding the “capital” portion of GenAI “return on invested capital”...and in assessing which companies have more or less compute driven competitive advantage over time.

# MS

MS

# Executive Summary (Continued)

We detail 4 main debates and takeaways:

Debate 1: How much capacity will the hyperscalers (AMZN, GOOGL, META, MSFT) bring online in '26/'27?

Our View: We see AMZN, GOOGL, META, and MSFT adding an incremental 14 GW/20 GW in '26/'27...for context, we believe AWS's total capacity added over its first \~18 years of existence (through YE24), was only \~5 GW...and 20 GW is enough to power 15 million+ US homes for a year...so capacity is coming

We see GOOGL (\~7 GW) again bringing on the most capacity in '27, followed by AMZN/MSFT (\~5 GW each). META's capex is only adding 3.5 GW, but when grossing up its hyperscale spend, we estimate META is really adding \~4 GW in '27. META doesn't have a hyperscale business, which means this level of investment speaks to the importance for META to productize its investment and drive incremental durable revenue.

Debate 2: Where is the cost and compute efficiency gap between NVDA and Custom ASICs now and what are we monitoring to close that gap?

Our View: We estimate hyperscaler capex to build a 1 GW datacenter with current-gen NVDA GPUs (Blackwell) is up to \~2x the cost of current-gen custom ASICs (TPU, Trainium)...with the server/rack cost driving the biggest delta...but compute power efficiency matters, and this is where NVDA shines...with compute performance/watt 2x-8x ahead of custom ASICs. For the custom ASICs, we look for system-level perf/watt improvements via networking, high-bandwidth memory capacity, and software optimizations. In effect, cost/token/watt advances will matter from here.

# MS

MS

# Executive Summary (Continued)

Debate 3: Which hyperscalers are investing the most and least in forward year capacity yet to come on?

Our View: We see AMZN/MSFT/META doing the most forward purchasing/building (powered shells, land, equipment, memory, etc.) and estimate 50%+ of '26 AMZN/MSFT/META capex will come online in '27 and beyond. This is a potential positive for second derivative capex slowing and is a hedge against delays/component inflation. In contrast, we estimate only \~10% of '26 GOOGL capex is for '27 and beyond (higher execution and component inflation risk).

Debate 4: Beyond the rack, which costs within the data center build have the most swing in driving cost of capacity higher or lower?

Our View: Networking (\~20%) and Powered Shells (\~HSD-low-teens%) are the largest sources of investment after racks. DRAM (single digit % of the cost) and HBM (\~MSD-mid-teens%) also pose upside risks to the rack prices that hyperscalers pay. Remember, with Blackwell racks, NVDA bundles and makes a margin on memory content and hyperscalers generally absorb these costs. With Rubin and its plug-in memory modules, hyperscale customers may increasingly be able to source approved memory directly (possible savings), but “bundling” may still be more efficient.

# MS

MS

# Roadmap for Future Research

What are potential ranges on hyperscaler revenue per GW...and what does this imply for growth ahead?

\- As hyperscalers add NVDA/Custom ASIC capacity, what are reasonable ranges of Revenue per MW/GW to better determine near-term cloud revenue estimates and ROIC?

What will drive cost per token per watt advances from here?

• What improvements will Trainium 4 and TPU 8 show?

How will the hyperscalers finance the forward build out?

\- Hyperscalers predominantly fund datacenter capex through operating cash flow, but will they continue to mix shift toward long-term, fixed rate debt and potentially more creative financing structures?

Could physical, real-world constraints impact timing of capacity coming online?

\- Will power cause a snag in build times? Do we have enough labor (contractors, electricians, plumbers, etc.) to complete ongoing projects as well as available for sale land for future builds?

How many TPUs will ultimately end up on GOOGL's balance sheet? When will AMZN start selling Trainium to third party data centers?

\- Our Asia Semis Team estimates there will be \~4mn/\~6mn TPU units shipped in '26/'27...how many of these will ultimately end up in GOOGL vs third party data centers? (we est. \~50% split). We have zero assumption for AMZN third party Trainium sales...they are all upside.

# MS

MS

Debate #1: Capacity Additions

Debate #2: Cost of Capacity

Debate #3: Investments in Forward Capacity

Debate #4: Costs Outside the Rack to Monitor

# Debate 1: How Much Capacity Will the Hyperscalers (AMZN, GOOGL, META, MSFT) Bring Online in '26/'27?

Our View: We see AMZN, GOOGL, META, and MSFT adding an incremental 14 GW / 20 GW in '26/'27. For context, we believe AWS's total capacity added over its first \~18 years of existence was \~4-6 GW (YE24), and 20 GW is enough to power 15 million+ US homes...so capacity is growing.

We model GOOGL (\~7 GW) to bring on the most capacity in '27, followed by AMZN/MSFT (\~5 GW each). From a chip perspective, we see NVDA supplying \~60% of incremental capacity through '27, with TPU and Trainium growing in the mix.

# MS

MS

We See Hyperscaler Capex Reaching \~\$1tr in '27, With Over \$2tr Invested Since '24   
![](images/884c59fe47c0cbf8e0c497ac4fafae8ed9efc3439ed92b399ded1c855fba98dc.jpg)  
Source: Company data, MS Estimates; Note: AMZN = Total Company Capex excluding proceeds from property and equipment sales and incentives

# MS

MS

# From a Capacity Perspective, Bottom-Up Modeling Implies This Should Lead to an Incremental \~20 GW Capacity Coming on in '27...up from 14 GW in '26

- We believe hyperscaler incremental capacity coming online in '27 is set to be \~3x higher than '25...speaking to the multi-year capex build yielding results   
- For more perspective, we estimate AWS's total capacity at year end '24 was \~4-6 GW, for what was then a \$108bn annual revenue business   
- Notably, we estimate GOOGL adds the most capacity in '27 (\~7 GW)...followed by AMZN, MSFT and META. This speaks to GOOGL's surging demand to 1) Train leading frontier models (Gemini) 2) Enable GCP growth and 3) Deploy new GenAI enabled offerings across its core Search/YouTube offerings

![](images/7f060fcd93a7e2474e11da3c839c371e19eba7af79d201c70ecc2df93fb467c8.jpg)

<details>
<summary>bar_stacked</summary>

| Year | GOOGL | AMZN* | MSFT | META |
|------|-------|-------|------|------|
| 2025 | 2.1   | 1.8   | 1.4  | 1.4  |
| 2026 | 5.6   | 3.5   | 2.6  | 1.9  |
| 2027 | 6.8   | 4.7   | 4.7  | 3.4  |
</details>

Source: Company data, MS Estimates; Note: \*We acknowledge AMZN comments of adding 3.9 GW of new power capacity in 2025. Please note our capacity addition est. are based on coincident timing of server/rack deliveries each year. We believe the delta in '25 vs. company comments is related to IT capacity/servers purchased prior to '25 that weren't brought online until '25 as well as traditional cloud/CPU data center capacity

# MS

MS

# At a Hyperscaler Level, We See GOOGL Adding the Most Incremental Capacity Followed by AMZN and MSFT

- Again, we model GOOGL to add the most capacity in '27 (\~7 GW)...followed by AMZN, MSFT and META. This speaks to GOOGL's surging demand to 1) Train leading frontier models (Gemini) 2) Enable GCP growth and 3) Deploy new GenAI enabled offerings across its core Search/YouTube offerings   
- AMZN/AWS's '26/'27 capacity catch up is notable given its slower start to building GenAI capacity in '23/'24   
- META's \~2GW/3GW of incremental capacity in '26/'27 is still notable given it doesn't have a hyperscale business and is also spending an estimated \~\$25bn of annual opex with hyperscalers, which would equate to incremental \~3GW added (see next slide)

![](images/799f217c4aae19d5aba9f45094ab86ad8efdcb04307843c286cb61f603e14f61.jpg)

<details>
<summary>bar</summary>

| Company | 2025 (GW) | 2026 (GW) | 2027 (GW) |
| :--- | :--- | :--- | :--- |
| GOOGL | 2.1 | 5.6 | 6.8 |
| AMZN* | 1.8 | 3.5 | 4.7 |
| MSFT | 1.4 | 2.6 | 4.7 |
| META | 1.4 | 1.9 | 3.4 |
</details>

Source: Company data, MS Estimates; Note: \*We acknowledge AMZN comments of adding 3.9 GW of new power capacity in 2025. Please note our capacity addition est. are based on coincident timing of server/rack deliveries each year. We believe the delta in '25 vs. company comments is related to IT capacity/servers purchased prior to '25 that weren't brought online until '25 as well as traditional cloud/CPU data center capacity

# MS

MS

# But META's Total Effective \~4 GW Added in '26 and '27 (Including Hyperscale Deals) Speaks to Importance of Product Innovation and Incremental Revenue to Prove ROIC

- Combining META's reported capex and grossing up its external compute deals with CRWV/NBIS/ORCL/GOOGL/AMZN, we find META is set to bring on an effective \~4GW in '26 and '27   
- This places higher importance on META's ability to productize its models to drive adoption and monetization.

\- We have highlighted the potential for a ‘MetaClaw’ consumer agent here and continue to believe META’s ability to leverage its leading 1P data is underappreciated

\- NeoCloud Safety Valve? We will also continue monitoring META's compute strategy and whether they ultimately choose to offload acquired compute given the demand we are seeing for LLM enterprise tools

![](images/357118ff5a250c43d7fca1e3a63bcc368f39aa008757c3fe36e4c4b43b73cce2.jpg)

<details>
<summary>bar_stacked</summary>

| Year | GPU (GW) | ASIC (GW) | GPU Neocloud (GW) |
| :--- | :--- | :--- | :--- |
| 2025 | 1.3 | 0.1 | 1.4 |
| 2026 | 1.7 | 0.2 | 4.4 |
| 2027 | 2.6 | 0.8 | 3.9 |
</details>

MET

[中间内容因长度限制已省略]

E (04/22/2025)</td><td>$114.22</td></tr><tr><td>Intuit (INTU.O)</td><td>O (02/26/2025)</td><td>$378.29</td></tr><tr><td>Microsoft (MSFT.O)</td><td>O (01/13/2016)</td><td>$409.43</td></tr><tr><td>Oracle Corporation (ORCL.N)</td><td>E (01/15/2019)</td><td>$195.61</td></tr><tr><td>Salesforce, Inc. (CRM.N)</td><td>O (12/21/2023)</td><td>$167.58</td></tr><tr><td>Samsara Inc (IOT.N)</td><td>E (03/23/2023)</td><td>$27.99</td></tr><tr><td>ServiceNow Inc (NOW.N)</td><td>O (09/24/2025)</td><td>$90.50</td></tr><tr><td>Shopify Inc (SHOP.O)</td><td>O (04/19/2024)</td><td>$97.42</td></tr><tr><td>Workday Inc (WDAY.O)</td><td>E (02/19/2025)</td><td>$118.75</td></tr><tr><td colspan="3">Meta A Marshall</td></tr><tr><td>Check Point Software Technologies Ltd. (CHKP.O)</td><td>E (10/16/2023)</td><td>$120.25</td></tr><tr><td>CrowdStrike Holdings Inc (CRWD.O)</td><td>O (03/10/2026)</td><td>$579.95</td></tr><tr><td>Fortinet Inc. (FTNT.O)</td><td>U (09/02/2025)</td><td>$121.86</td></tr><tr><td>Gen Digital Inc. (GEN.O)</td><td>E (06/07/2024)</td><td>$23.18</td></tr><tr><td>Netskope, Inc. (NTSK.O)</td><td>O (10/13/2025)</td><td>$10.92</td></tr><tr><td>Okta, Inc. (OKTA.O)</td><td>O (12/02/2024)</td><td>$81.05</td></tr><tr><td>Palo Alto Networks Inc (PANW.O)</td><td>O (10/10/2017)</td><td>$238.21</td></tr><tr><td>Qualys Inc (QLYS.O)</td><td>U (02/09/2021)</td><td>$86.73</td></tr><tr><td>Rapid7 Inc (RPD.O)</td><td>E (08/11/2015)</td><td>$6.23</td></tr><tr><td>SailPoint Inc (SAIL.O)</td><td>O (09/02/2025)</td><td>$13.18</td></tr><tr><td>SentinelOne, Inc. (S.N)</td><td>E (12/02/2024)</td><td>$16.51</td></tr><tr><td>Tenable Holdings Inc (TENB.O)</td><td>E (12/02/2024)</td><td>$20.45</td></tr><tr><td>Varonis Systems, Inc. (VRNS.O)</td><td>E (01/26/2026)</td><td>$27.22</td></tr><tr><td>Zscaler Inc (ZS.O)</td><td>E (04/22/2026)</td><td>$153.70</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Akamai Technologies, Inc. (AKAM.O)</td><td>O (01/12/2026)</td><td>$155.67</td></tr><tr><td>Appian Corp (APPN.O)</td><td>E (04/30/2026)</td><td>$19.22</td></tr><tr><td>C3.ai (AI.N)</td><td>U (01/04/2021)</td><td>$9.03</td></tr><tr><td>Datadog, Inc. (DDOG.O)</td><td>O (01/12/2026)</td><td>$202.84</td></tr><tr><td>Dynatrace Inc (DT.N)</td><td>E (02/13/2024)</td><td>$37.12</td></tr><tr><td>Elastic NV (ESTC.N)</td><td>O (12/16/2024)</td><td>$49.78</td></tr><tr><td>GitLab Inc (GTLB.O)</td><td>E (01/12/2026)</td><td>$22.60</td></tr><tr><td>JFrog Ltd. (FROG.O)</td><td>O (12/21/2023)</td><td>$65.08</td></tr><tr><td>MongoDB Inc (MDB.O)</td><td>O (04/12/2023)</td><td>$303.09</td></tr><tr><td>PagerDuty, Inc. (PD.N)</td><td>E (01/24/2024)</td><td>$6.73</td></tr><tr><td>Palantir Technologies Inc. (PLTR.O)</td><td>E (02/04/2025)</td><td>$133.73</td></tr><tr><td>Snowflake Inc. (SNOW.N)</td><td>O (06/24/2025)</td><td>$150.76</td></tr><tr><td>UiPath Inc (PATH.N)</td><td>E (09/07/2022)</td><td>$9.67</td></tr></table>

INDUSTRY COVERAGE: Semiconductors 

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (05/14/2026)</td></tr><tr><td colspan="3">Joseph Moore</td></tr><tr><td>Advanced Micro Devices (AMD.O)</td><td>E (06/09/2024)</td><td>$449.70</td></tr><tr><td>Aeva Technologies Inc (AEVA.O)</td><td>E (07/19/2021)</td><td>$21.23</td></tr><tr><td>Allegro Microsystems Inc (ALGM.O)</td><td>O (02/13/2026)</td><td>$44.97</td></tr><tr><td>Ambarella Inc (AMBA.O)</td><td>O (03/29/2016)</td><td>$81.04</td></tr><tr><td>Amkor Technology Inc (AMKR.O)</td><td>E (11/08/2023)</td><td>$72.09</td></tr><tr><td>Analog Devices Inc. (ADI.O)</td><td>O (11/16/2023)</td><td>$426.79</td></tr><tr><td>Astera Labs Inc (ALAB.O)</td><td>O (05/11/2025)</td><td>$228.64</td></tr><tr><td>Broadcom Inc. (AVGO.O)</td><td>O (06/09/2024)</td><td>$439.79</td></tr><tr><td>GlobalFoundries Inc (GFS.O)</td><td>E (10/28/2024)</td><td>$73.84</td></tr><tr><td>Intel Corporation (INTC.O)</td><td>E (02/22/2023)</td><td>$115.93</td></tr><tr><td>IonQ Inc (IONQ.N)</td><td>E (04/25/2023)</td><td>$57.47</td></tr><tr><td>Marvell Technology Group Ltd (MRVL.O)</td><td>E (09/14/2015)</td><td>$182.58</td></tr><tr><td>Microchip Technology Inc. (MCHP.O)</td><td>E (07/10/2024)</td><td>$97.04</td></tr><tr><td>Micron Technology Inc. (MU.O)</td><td>O (10/06/2025)</td><td>$776.01</td></tr><tr><td>Navitas Semiconductor Corp (NVTS.O)</td><td>U (04/06/2025)</td><td>$22.32</td></tr><tr><td>NVIDIA Corp. (NVDA.O)</td><td>O (03/16/2023)</td><td>$235.74</td></tr><tr><td>NXP Semiconductor NV (NXPI.O)</td><td>O (02/11/2025)</td><td>$294.17</td></tr><tr><td>ON Semiconductor Corp. (ON.O)</td><td>E (05/11/2025)</td><td>$118.37</td></tr><tr><td>Qorvo Inc (QRVO.O)</td><td>E (10/28/2025)</td><td>$90.46</td></tr><tr><td>Qualcomm Inc. (QCOM.O)</td><td>U (02/10/2026)</td><td>$200.08</td></tr><tr><td>SanDisk Corporation. (SNDK.O)</td><td>O (03/03/2025)</td><td>$1,382.72</td></tr><tr><td>Semtech Corp. (SMTC.O)</td><td>E (04/06/2025)</td><td>$141.16</td></tr><tr><td>Silicon Laboratories Inc. (SLAB.O)</td><td>E (01/19/2021)</td><td>$217.31</td></tr><tr><td>Skyworks Solutions Inc (SWKS.O)</td><td>E (11/28/2018)</td><td>$67.06</td></tr><tr><td>Texas Instruments (TXN.O)</td><td>U (04/13/2020)</td><td>$308.17</td></tr><tr><td>Wolfspeed, INC (WOLF.N)</td><td>NR (04/06/2025)</td><td>$69.96</td></tr><tr><td colspan="3">Lee Simpson</td></tr><tr><td>Arm Holdings plc (ARM.O)</td><td>E (04/07/2026)</td><td>$228.50</td></tr><tr><td>Cadence Design Systems Inc (CDNS.O)</td><td>O (02/14/2024)</td><td>$352.84</td></tr><tr><td>Synopsys Inc. (SNPS.O)</td><td>E (02/27/2026)</td><td>$510.02</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.   
\* Historical prices are not split adjusted.

© 2026 MS
"""
