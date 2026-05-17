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
# Global Memory Tech

# Theme of the week: NAND surprise, Samsung labor strike, TCB sales miss

Industry Overview

# Kioxia's guidance signals significantly strong NAND ASPs

We were surprised by Kioxia's more-than-doubled 1Q CY26 ASP QoQ, which was 20ppt higher than Korean chipmakers' results (80%+/-). We believe Kioxia's SSD sales increase (including enterprise solutions) vs 4Q CY25 was one of the key contributors. Its 2Q CY26 sales guidance (+74.5% QoQ) also implies upbeat NAND ASP (\~70% QoQ increase vs consensus / our estimate: sub-50%). Taiwan-based NAND module maker, Phison Electronics (8299 TT), also reported super-cycle-level April results (sales +237% YoY; pre-tax profit margin 45%; net profit margin 38%). Overall, we acknowledge high upside risk to our global NAND ASP forecasts (+34%/+9%/+3% QoQ in 2Q/3Q/4Q26) or even bullish camp's view (e.g., TrendForce expects only 8-13% increase after 70-75% in 2Q).

# Samsung labor strike may lead to stronger contract pricing

Samsung Electronics is the No. 1 supplier of DRAM and NAND. Thus, its potential labor strike should affect global memory chip supply. Since the labor union is targeting only an 18-day strike (21 May - 7 June) if special bonus payments (15% of OP) are not settled, the actual impact may theoretically be not significant. However, it usually takes at least a few months to normalize fab operations after a full suspension. Of course, Samsung's memory fab operations are mostly based on factory automation (not many people inside clean rooms), so we don't expect a complete shutdown. That said, labor-intensive backend packaging areas can be hit. Some OEMs and Big Tech companies may rush to secure more Samsung memory chips ahead of Sept/Oct peak season. This can also lead to higher spot market prices. Interestingly, both DRAM/NAND spot prices slightly rebounded this week vs softening in April and early May. 3Q contract price, which is usually negotiated in June, can also be affected positively (for memory chipmakers).

# Hanmi Semi's 1Q TCB sales miss a manageable risk

Hanmi Semiconductor (042700 KS) posted much weaker-than-expected 1Q results (sales only W51bn; -65% YoY; OPM also low at 17% vs the normal 40-50% range). We believe weaker TCB orders from SK Hynix were the key contributor. However, 2Q/2H recovery is well expected on a more diversified TCB (for not only HBM, but also 2.5D logic and even HBF) and customers (not well disclosed, but we assume Hynix, Micron, ASE, TSMC, etc.). In fact, 1Q NP (W19bn vs W8bn OP) was upbeat due to FX gains. As such, our EPS estimates are mostly unchanged. Another Korean semis supply company, Soulbrain (357780 KS; HF etching materials for Samsung's/Hynix's chips), reported in-line 1Q results, although growth and margins remained below trend (OPM only 17% vs normal 20%+). This is consistent with the current memory cycle (weak bit growth or low production volume vs super-strong chip pricing). SK Square (SK Hynix's holdco) also disclosed in-line 1Q earnings, but OP/NP reached record highs as it recognizes 20% of Hynix's profits as a holdco. Since we have already reflected Hynix's strong 2026E earnings into our SK Square's forecasts, our EPS revisions (SK Square) are almost nil this time.

# 16 May 2026

Equity

Global

Technology

Simon Woo, CFA >>

Research Analyst

BofA (Seoul)

+82 2 3707 0554

simon.woo@bofa.com

Dai Shen >>

Research Analyst

BofA (Hong Kong)

dai.shen@bofa.com

Vivek Arya

Research Analyst

BofAS

vivek.arya@bofa.com

Mikio Hirakawa >>

Research Analyst

BofAS Japan

mikio.hirakawa@bofa.com

Matt Shin >>

Research Analyst

BofA (Seoul)

matt.shin2@bofa.com

# Exhibit 1: DDR5 rose further this week, while DDR4 and NAND prices stabilized following several weeks of decline

Spot prices – DRAM and NAND

<table><tr><td>US$</td><td>Current</td><td>WoW</td><td>QoQ</td><td>YoY</td></tr><tr><td colspan="5">DRAM spot</td></tr><tr><td>16Gb DDR5</td><td>40.7</td><td>2%</td><td>7%</td><td>639%</td></tr><tr><td>16Gb DDR4</td><td>58.2</td><td>0%</td><td>-26%</td><td>1281%</td></tr><tr><td>8Gb DDR4</td><td>32.0</td><td>0%</td><td>2%</td><td>1403%</td></tr><tr><td>4Gb DDR4</td><td>7.8</td><td>5%</td><td>24%</td><td>431%</td></tr></table>

<table><tr><td colspan="5">NAND spot</td></tr><tr><td>1Tb wafer</td><td>25.0</td><td>1%</td><td>16%</td><td>386%</td></tr><tr><td>512Gb wafer</td><td>20.5</td><td>0%</td><td>14%</td><td>651%</td></tr><tr><td>256Gb wafer</td><td>10.5</td><td>0%</td><td>20%</td><td>601%</td></tr></table>

Source: DRAMeXchange

BofA GLOBAL RESEARCH

ASP: Average selling price

DDR4/5: $4^{th}/5^{th}$ gen double-data rate DRAM

DRAM: Dynamic random-access memory

HBF: High bandwidth flash

HBM: High bandwidth memory

HF: Hydrogen fluoride

NAND: Not-AND memory

OEM: Original equipment manufacturer

OPM: Operating profit margin

SSD: Solid-state drive

TCB: Thermal compression bonding

# Korea exports and Taiwan monthly sales trend

Exhibit 2: Remained flat MoM but still at record-high level in May (US\$8.5bn)   
Korea semis exports – First 10 days of month US\$bn   
![](images/3eded605340310236079ccc8168c7f12e42e3241ff183ab87f14c16fe68a8877.jpg)

<details>
<summary>line</summary>

| Date    | Value (US$bn) |
|---------|---------------|
| Nov-22  | 2.5           |
| Feb-23  | 2.0           |
| May-23  | 1.8           |
| Aug-23  | 2.2           |
| Nov-23  | 2.5           |
| Feb-24  | 2.7           |
| May-24  | 3.0           |
| Aug-24  | 3.3           |
| Nov-24  | 3.5           |
| Feb-25  | 3.0           |
| May-25  | 3.5           |
| Aug-25  | 4.0           |
| Nov-25  | 4.5           |
| Feb-26  | 5.0           |
| May-26  | 8.5           |
</details>

Source: MoTIR   
BofA GLOBAL RESEARCH

Exhibit 4: Robust MoM growth mostly led by memory names, such as Nanya Tech (+40%), Transcend (+31%), Macronix/Winbond (+34%/33%)   
Taiwan tech companies' monthly sales – Apr 2026   
![](images/edbc0e328b70c0865bfea80cd7e3e623dc9aadfe4aa6ad8ef7a429b8339b48de.jpg)

<details>
<summary>bar</summary>

| Company      | MoM % |
| ------------ | ----- |
| Nanya Tech   | 40%   |
| Gigabyte     | 35%   |
| Macronix     | 35%   |
| Winbond     | 35%   |
| Transcend    | 30%   |
| Holystone    | 10%   |
| Prison       | 10%   |
| Novatek      | 10%   |
| Wasin        | 10%   |
| UMC          | 10%   |
| PSMC         | 10%   |
| Unimicron    | 10%   |
| Win Semi     | 10%   |
| Acer         | 10%   |
| Pegatron     | 10%   |
| Nanya PCB    | 10%   |
| Aspeed       | 10%   |
| Hon Hai      | 10%   |
| Kinsus       | 10%   |
| Yageo        | 10%   |
| Powertech    | 10%   |
| ASE          | 10%   |
| ADATA        | 10%   |
| TSMC         | 10%   |
| Inventec     | 10%   |
| Lotes        | 10%   |
| Mitzac       | 10%   |
| Assistec     | 10%   |
| Quanta       | 10%   |
| Wistron      | 10%   |
| Innolux      | 10%   |
| AUO          | 10%   |
| Wiwynn       | 10%   |
| Vanguard     | 10%   |
| Compal       | 10%   |
| MediaTek     | -25%  |
</details>

Source: Companies   
BofA GLOBAL RESEARCH

Exhibit 3: YoY rebound still high at 150% in May; already four consecutive months of triple-digit growth   
Korea semis exports – YoY change in first 10 days of month   
![](images/008baa24a22b63ccc05927fc62a1a0079fede7fdc75d1d662fbdf5d2d69b80cd.jpg)

<details>
<summary>line</summary>

| Month    | YoY   |
| -------- | ----- |
| May-21   | 40%   |
| Aug-21   | 0%    |
| Nov-21   | 40%   |
| Feb-22   | 0%    |
| May-22   | 0%    |
| Aug-22   | 0%    |
| Nov-22   | -40%  |
| Feb-23   | -40%  |
| May-23   | -40%  |
| Aug-23   | 0%    |
| Nov-23   | 0%    |
| Feb-24   | 40%   |
| May-24   | 80%   |
| Aug-24   | 40%   |
| Nov-24   | 0%    |
| Feb-25   | 0%    |
| May-25   | 0%    |
| Aug-25   | 40%   |
| Nov-25   | 0%    |
| Feb-26   | 160%  |
| May-26   | 140%  |
</details>

Source: MoTIR   
BofA GLOBAL RESEARCH

Exhibit 5: Also notably strong rebound seen from memory names and resilient growth across most companies including TSMC (+18%), Quanta (+121%), Yageo (+22%)   
Taiwan tech companies' monthly sales YoY – Apr 2026   
![](images/3e295065fa92654f8b24e30e2a8f908908cfe15c8d0bf83f70766d172d3854cf.jpg)

<details>
<summary>bar</summary>

| Company      | YoY   |
| ------------ | ----- |
| Nanya Tech   | 200%  |
| Transcend    | 200%  |
| Phison       | 180%  |
| Winbond      | 160%  |
| ADATA        | 140%  |
| Macronix     | 120%  |
| Quanta       | 100%  |
| Wistron      | 80%   |
| Aspeed       | 60%   |
| Gigabyte     | 40%   |
| Acer         | 20%   |
| Win Semi     | 0%    |
| Asustek      | -20%  |
| Nanya PCB    | -40%  |
| Inventec     | -60%  |
| Powertech    | -80%  |
| PSMC         | -100% |
| Mitac        | -120% |
| Hon Hai      | -140% |
| Wiwynn       | -160% |
| Unimicron    | -180% |
| Kinsus       | -200% |
| Yageo        | -220% |
| Holystone    | -240% |
| ASE          | -260% |
| TSMC         | -280% |
| Walsin       | -300% |
| Compal       | -320% |
| Lotes        | -340% |
| Innolux      | -360% |
| UMC          | -380% |
| Vanguard     | -400% |
| Novatek      | -420% |
| MediaTek     | -440% |
| AUO          | -460% |
| Pegatron     | -480% |
</details>

\*Nanya +717%, Transcend +594%, Phison +237%   
Source: Companies   
BofA GLOBAL RESEARCH

Hanmi Semi (042700 KS; C-1-7; PO W500,000)

Exhibit 6: Weaker-than-expected 1Q results (sales only W51bn; -65% YoY, OPM also low at 17% vs normal 40-50% range); we believe weaker TCB orders from Hynix was the key contributor. However, 2Q/2H recovery is well-expected on more diversified TCB (for not only HBM, but also 2.5D logic and even HBF) and customers (not well disclosed, but we assume Hynix, Micron, ASE, TSMC, etc.)

Hanmi Semi – Earnings revisions (2026-28E)

<table><tr><td>(Wbn, Won)</td><td>1Q26</td><td>2Q26E</td><td>3Q26E</td><td>4Q26E</td><td>1Q27E</td><td>2Q27E</td><td>3Q27E</td><td>4Q27E</td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td colspan="17">EPS</td></tr><tr><td>New</td><td>201</td><td>791</td><td>1,053</td><td>1,110</td><td>1,173</td><td>1,428</td><td>1,665</td><td>1,770</td><td>2,112</td><td>948</td><td>2,759</td><td>1,608</td><td>2,256</td><td>3,154</td><td>6,036</td><td>10,656</td></tr><tr><td>Old</td><td>145</td><td>815</td><td>1,074</td><td>1,110</td><td>1,173</td><td>1,428</td><td>1,665</td><td>1,770</td><td>2,112</td><td>948</td><td>2,759</td><td>1,608</td><td>2,256</td><td>3,144</td><td>6,036</td><td>10,656</td></tr><tr><td>Difference</td><td>39%</td><td>-3%</td><td>-2%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">Dividend/share</td></tr><tr><td>New</td><td>0</td><td>0</td><td>0</td><td>1,100</td><td>0</td><td>0</td><td>0</td><td>2,050</td><td>600</td><td>200</td><td>420</td><td>720</td><td>800</td><td>1,100</td><td>2,050</td><td>3,100</td></tr><tr><td>Old</td><td>0</td><td>0</td><td>0</td><td>1,100</td><td>0</td><td>0</td><td>0</td><td>2,050</td><td>600</td><td>200</td><td>420</td><td>720</td><td>800</td><td>1,100</td><td>2,050</td><td>3,100</td></tr><tr><td>Difference</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">Sales</td></tr><tr><td>New</td><td>51</td><td>204</td><td>252</td><td>272</td><td>281</td><td>331</td><td>382</td><td>403</td><td>373</td><td>328</td><td>159</td><td>559</td><td>577</td><td>779</td><td>1,397</td><td>2,324</td></tr><tr><td>Old</td><td>85</td><td>204</td><td>252</td><td>272</td><td>281</td><td>331</td><td>382</td><td>403</td><td>373</td><td>328</td><td>159</td><td>559</td><td>577</td><td>813</td><td>1,397</td><td>2,324</td></tr><tr><td>Difference</td><td>-40%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-4%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">Gross margin</td></tr><tr><td>New</td><td>54.1%</td><td>59.5%</td><td>61.0%</td><td>60.2%</td><td>61.0%</td><td>62.0%</td><td>62.0%</td><td>63.0%</td><td>48.3%</td><td>56.5%</td><td>49.9%</td><td>56.3%</td><td>57.6%</td><td>59.9%</td><td>62.1%</td><td>63.6%</td></tr><tr><td>Old</td><td>47.0%</td><td>61.0%</td><td>62.0%</td><td>60.2%</td><td>61.0%</td><td>62.0%</td><td>62.0%</td><td>63.0%</td><td>48.3%</td><td>56.5%</td><td>49.9%</td><td>56.3%</td><td>57.6%</td><td>59.6%</td><td>62.1%</td><td>63.6%</td></tr><tr><td>Difference</td><td>15.2%</td><td>-2.5%</td><td>-1.6%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.5%</td><td>0.0%</td><td>0.0%</td></tr><tr><td colspan="17">OP</td></tr><tr><td>New</td><td>8</td><td>96</td><td>129</td><td>136</td><td>145</td><td>177</td><td>207</td><td>220</td><td>122</td><td>112</td><td>35</td><td>255</td><td>251</td><td>369</td><td>749</td><td>1,344</td></tr><tr><td>Old</td><td>17</td><td>99</td><td>131</td><td>136</td><td>145</td><td>177</td><td>207</td><td>220</td><td>122</td><td>112</td><td>35</td><td>255</td><td>251</td><td>383</td><td>749</td><td>1,344</td></tr><tr><td>Difference</td><td>-50%</td><td>-3%</td><td>-2%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-4%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">OP margin</td></tr><tr><td>New</td><td>16.6%</td><td>47.2%</td><td>51.1%</td><td>49.9%</td><td>51.7%</td><td>53.5%</td><td>54.1%</td><td>54.6%</td><td>32.8%</td><td>34.1%</td><td>21.7%</td><td>45.7%</td><td>43.6%</td><td>47.4%</td><td>53.6%</td><td>57.8%</td></tr><tr><td>Old</td><td>19.9%</td><td>48.7%</td><td>52.1%</td><td>49.9%</td><td>51.7%</td><td>53.5%</td><td>54.1%</td><td>54.6%</td><td>32.8%</td><td>34.1%</td><td>21.7%</td><td>45.7%</td><td>43.6%</td><td>47.2%</td><td>53.6%</td><td>57.8%</td></tr><tr><td>Difference</td><td>-16.4%</td><td>-3.1%</td><td>-1.9%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.5%</td><td>0.0%</td><td>0.0%</td></tr><tr><td colspan="17">Pre-tax income</td></tr><tr><td>New</td><td>25</td><td>97</td><td>130</td><td>137</td><td>146</td><td>178</td><td>208</td><td>221</td><td>136</td><td>128</td><td>345</td><td>198</td><td>278</td><td>389</td><td>753</td><td>1,348</td></tr><tr><td>Old</td><td>18</td><td>100</td><td>132</td><td>137</td><td>146</td><td>178</td><td>208</td><td>221</td><td>136</td><td>128</td><td>345</td><td>198</td><td>278</td><td>387</td><td>753</td><td>1,348</td></tr><tr><td>Difference</td><td>41%</td><td>-3%</td><td>-2%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">Effective tax rate</td></tr><tr><td>New</td><td>24.1%</td><td>23.0%</td><td>23.0%</td><td>23.0%</td><td>24.0%</td><td>24.0%</td><td>24.0%</td><td>24.0%</td><td>23.3%</td><td>27.8%</td><td>22.6%</td><td>23.1%</td><td>23.1%</td><td>23.1%</td><td>24.0%</td><td>25.0%</td></tr><tr><td>Old</td><td>23.0%</td><td>23.0%</td><td>23.0%</td><td>23.0%</td><td>24.0%</td><td>24.0%</td><td>24.0%</td><td>24.0%</td><td>23.3%</td><td>27.8%</td><td>22.6%</td><td>23.1%</td><td>23.1%</td><td>23.0%</td><td>24.0%</td><td>25.0%</td></tr><tr><td>Difference</td><td>4.9%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>0.0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.3%</td><td>0.0%</td><td>0.0%</td></tr><tr><td colspan="17">Net profit</td></tr><tr><td>New</td><td>19</td><td>75</td><td>100</td><td>105</td><td>111</td><td>135</td><td>158</td><td>168</td><td>104</td><td>92</td><td>267</td><td>153</td><td>214</td><td>299</td><td>573</td><td>1,011</td></tr><tr><td>Old</td><td>14</td><td>77</td><td>102</td><td>105</td><td>111</td><td>135</td><td>158</td><td>168</td><td>104</td><td>92</td><td>267</td><td>153</td><td>214</td><td>298</td><td>573</td><td>1,011</td></tr><tr><td>Difference</td><td>39%</td><td>-3%</td><td>-2%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">ROE - annualized</td></tr><tr><td>New</td><td>11.5%</td><td>44.5%</td><td>52.5%</td><td>48.8%</td><td>48.4%</td><td>54.7%</td><td>55.6%</td><td>51.6%</td><td>34.6%</td><td>25.0%</td><td>55.5%</td><td>27.4%</td><td>34.8%</td><td>37.3%</td><td>49.8%</td><td>56.4%</td></tr><tr><td>Old</td><td>8.3%</td><td>46.4%</td><td>53.8%</td><td>49.0%</td><td>48.6%</td><td>54.9%</td><td>55.7%</td><td>51.8%</td><td>34.6%</td><td>25.0%</td><td>55.5%</td><td>27.4%</td><td>34.8%</td><td>37.2%</td><td>49.9%</td><td>56.5%</td></tr><tr><td>Difference</td><td>37.8%</td><td>-4.0%</td><td>-2.5%</td><td>-0.4%</td><td>-0.4%</td><td>-0.3%</td><td>-0.3%</td><td>-0.3%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>0.1%</td><td>-0.3%</td><td>-0.2%</td></tr><tr><td colspan="17">EBITDA</td></tr><tr><td>New</td><td>11</td><td>99</td><td>132</td><td>139</td><td>149</td><td>181</td><td>211</td><td>224</td><td>129</td><td>121</td><td>43</td><td>265</td><td>263</td><td>382</td><td>765</td><td>1,362</td></tr><tr><td>Old</td><td>20</td><td>103</td><td>135</td><td>140</td><td>149</td><td>181</td><td>211</td><td>224</td><td>129</td><td>121</td><td>43</td><td>265</td><td>263</td><td>397</td><td>766</td><td>1,364</td></tr><tr><td>Difference</td><td>-43%</td><td>-3%</td><td>-2%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-4%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">Capex</td></tr><tr><td>New</td><td>5</td><td>15</td><td>15</td><td>15</td><td>20</td><td>20</td><td>20</td><td>20</td><td>25</td><td>9</td><td>28</td><td>54</td><td>75</td><td>50</td><td>80</td><td>80</td></tr><tr><td>Old</td><td>15</td><td>15</td><td>15</td><td>15</td><td>20</td><td>20</td><td>20</td><td>20</td><td>25</td><td>9</td><td>28</td><td>54</td><td>75</td><td>60</td><td>80</td><td>80</td></tr><tr><td>Difference</td><td>-64%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>0%</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>n/a</td><td>-16%</td><td>0%</td><td>0%</td></tr><tr><td colspan="17">Net cash</td></tr><tr><td>New</td><td>175</td><td>212</td><td>283</td><td>367</td><td>369</td><td>482</td><td>617</td><td>773</td><td>50</td><td>91</td><td>180</td><td>104</td><td>276</td><td>367</td><td>

[中间内容因长度限制已省略]

ons, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in

connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
