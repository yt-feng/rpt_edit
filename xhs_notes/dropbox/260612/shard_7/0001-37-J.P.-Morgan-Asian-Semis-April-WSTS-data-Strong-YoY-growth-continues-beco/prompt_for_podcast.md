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
## Asian Semis

April WSTS data: Strong YoY growth continues, becoming more broad-based with healthy unit growth and ex-memory ASP uptick

Overall semi revenues rose 106% YoY in April (vs. 88% YoY in March), with logic semis increasing 33% YoY (vs. 25% YoY in March) and memory increasing 359% YoY (vs. 269% YoY in March). Semis marked the eighth consecutive month of acceleration and the highest YoY growth since 1994. This was mostly due to 1) sustained AI compute demand driven by strong growth in AI accelerators (GPUs and ASICs), networking and server CPUs, and 2) ongoing memory ASP strength amid persistently tight supply conditions. Memory growth was driven by CSP-led demand across both HBM and conventional memory, with suppliers continuing to prioritize HBM allocation.

- Logic semi revenue rose 33% YoY (vs. 25% in March), marking 32 consecutive months of YoY growth. We believe this was mostly due to leading-edge demand, which continues to tighten. Strong demand for N5/N3 wafers—driven by GPUs/ASICs, server CPUs, networking, and Apple iPhone/Mac products—has kept the capacity tight. We believe N3 will be the primary bottleneck for AI accelerators, as most leading AI accelerators (such as NVIDIA Rubin, Google TPU v8t/i, and AWS Trn 3) are expected to adopt N3. We have also seen recent upside in server CPU demand due to booming demand for agentic AI. We now estimate the demand–supply gap for N3 in 2026 at \~600K wafers, equivalent to \$15bn–18bn in foundry revenues. Continued upward revisions to US CSP capex (with total capex for the top four US CSPs now indicating 80%+ YoY growth in 2026) suggest more structural AI demand. We expect the AI-driven semi upcycle to extend at least through 2026, with robust leading-edge demand continuing into 2028. For mature foundries, we see strong demand for AI peripheral products such as PMICs, early signs of industrial recovery, and some PC pull-in. However, downside risk remains from tepid consumer electronics demand given rising memory costs in 2H26.  
- Overall, semis units increased 15% YoY (vs. 10% YoY in March). Memory units increased 54% YoY (vs. 21% YoY in March). We forecast the HBM S-D shortage to worsen over the next three years, with DRAM wafer allocation to HBM continuing to rise (from 24% in 2026E to 31% in 2028E), adding greater pressure on conventional DRAM S-D, as HBM bit installation demand CAGR is likely to be +85% over the next three years. Logic semis units increased 14% YoY (vs. 9% YoY in March). We believe this growth is supported by demand for AI alongside pockets of strength in industrials. In addition, resilient iPhone 17 demand (iPhone shipments up 9% YoY versus overall smartphone shipments down 11% YoY in 2Q26E) especially share gains in the China market and strong customer interest in the MacBook Neo are helping offset weakness in mid- to low-end smartphone demand.  
- Overall, semis ASPs were up 79% YoY (vs. 71% YoY in March), driven by tight S-D across leading-edge and memory. Memory ASPs surged 198% YoY (vs. 206% YoY in March). We expect memory prices to increase 220-250% YoY this year, although we see a rather stable pricing trend next year, supported by a rising LTA contract sales mix. Given the dollar per bit crossover

## Technology and Telecoms

## Gokul Hariharan AC

(852) 2800-8564

gokul.hariharan@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

## Jennifer Hsieh

(886-2) 2725-9868

jennifer.hsieh@JPM.com

JPM Securities (Taiwan) Limited

## David Chou

(886-2) 2725-9618

david.chou@JPM.com

JPM Securities (Taiwan) Limited

## Jason Chen

(886-2) 2725-9864

jason.bh.chen@JPM.com

JPM Securities (Taiwan) Limited

## Subham Singhania

(91-22) 6157-3801

subham.singhania@JPM.com

JPM India Private Limited

between HBM and non-HBM, we expect memory makers to turn vocal on raising HBM ASPs next year (+10% YoY like-for-like, +30% blended). Logic semi ASPs rose 18% YoY (vs. 15% in March), supported by price hikes in leading edge node and a continued mix shift toward advanced nodes (higher N3/N5 mix). ASP growth is further supported by rising demand for mature-node (primarily 8") products, driven by AI-related PMICs, power discrete, and industrial applications, with selective price hikes observed in 1H this year. For 2H26, we believe leading edge pricing for hot-runs and super-hot-runs has moved up, but regular N3 pricing is unchanged.

\- Looking ahead, we expect leading-edge capacity tightness to persist well into 2027 or early 2028, driven by strong AI accelerator demand, increasing demand for AI interconnect, rising AI-driven power demand and continued strength from Apple iPhone and Mac. For memory, our team has revised up the FY26E/28E memory TAM by 37/53% (vs. the Mar-26 model). We now forecast capex at US\$450bn in memory spending over the next three years (vs. US\$300bn in Dec-25 model), with DRAM CY28-end WSPM at 2.8mn (up 880k from CY25-end) and 60% of incremental WSPM allocation directed toward HBM, keeping S-D tight and pricing biased to the upside. Overall, we reiterate our top picks among major AI beneficiaries: TSMC, Mediatek, Lasertec, Tokyo Electron, ASMPT, ASE, Alchip, Unimicron, EMC, SEC, and SK Hynix.

## Key charts

Figure 1: Semi ex-memory revenue YoY (May-24 onwards)  
![](images/22a555d14fb07e4dfe4815996084ceaa2f714d960d47c3f63720567126bc7789.jpg)

<details>
<summary>line chart</summary>

| Month    | Semi-ex Memory Revenue YoY (%) |
| -------- | ------------------------------ |
| May-24   | 4%                             |
| Jun-24   | 3%                             |
| Jul-24   | 7%                             |
| Aug-24   | 6%                             |
| Sep-24   | 14%                            |
| Oct-24   | 9%                             |
| Nov-24   | 8%                             |
| Dec-24   | 8%                             |
| Jan-25   | 11%                            |
| Feb-25   | 19%                            |
| Mar-25   | 18%                            |
| Apr-25   | 22%                            |
| May-25   | 18%                            |
| Jun-25   | 20%                            |
| Jul-25   | 26%                            |
| Aug-25   | 23%                            |
| Sep-25   | 20%                            |
| Oct-25   | 24%                            |
| Nov-25   | 27%                            |
| Dec-25   | 28%                            |
| Jan-26   | 31%                            |
| Feb-26   | 28%                            |
| Mar-26   | 25%                            |
| Apr-26   | 33%                            |
</details>

Source: WSTS.

Figure 3: Semi revenue (monthly) and YoY  
![](images/3ff6b8e56f83227775dfc0b26dee2e1e03cb4972698fd0e97031fccf32fc3673.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Semi revenue (US$mn) | YoY (%) |
|--------|----------------------|---------|
| Apr-02 | ~10,000              | ~20%    |
| Apr-03 | ~15,000              | ~40%    |
| Apr-04 | ~20,000              | ~60%    |
| Apr-05 | ~25,000              | ~80%    |
| Apr-06 | ~30,000              | ~60%    |
| Apr-07 | ~35,000              | ~40%    |
| Apr-08 | ~40,000              | ~20%    |
| Apr-09 | ~25,000              | ~-20%   |
| Apr-10 | ~30,000              | ~100%   |
| Apr-11 | ~35,000              | ~60%    |
| Apr-12 | ~40,000              | ~40%    |
| Apr-13 | ~45,000              | ~20%    |
| Apr-14 | ~50,000              | ~40%    |
| Apr-15 | ~55,000              | ~60%    |
| Apr-16 | ~60,000              | ~80%    |
| Apr-17 | ~65,000              | ~100%   |
| Apr-18 | ~70,000              | ~120%   |
| Apr-19 | ~75,000              | ~140%   |
| Apr-20 | ~80,000              | ~160%   |
| Apr-21 | ~85,000              | ~180%   |
| Apr-22 | ~90,000              | ~20%    |
| Apr-23 | ~95,000              | ~40%    |
| Apr-24 | ~1,00,000            | ~60%    |
| Apr-25 | ~1,10,000            | ~80%    |
| Apr-26 | ~135,000            | ~120%   |
</details>

Source: WSTS.

Figure 5: Semi ASP and YoY  
![](images/021d0cddc581fc81d5ea7194e78ce36bab7f71f500628d1c7794bd098709fea1.jpg)

<details>
<summary>line chart</summary>

| Date   | Overall Semi ASP (US$) | YoY(%) |
|--------|------------------------|--------|
| Apr-02 | ~0.20                  | ~0%    |
| Apr-03 | ~0.40                  | ~20%   |
| Apr-04 | ~0.50                  | ~30%   |
| Apr-05 | ~0.60                  | ~40%   |
| Apr-06 | ~0.50                  | ~30%   |
| Apr-07 | ~0.40                  | ~20%   |
| Apr-08 | ~0.50                  | ~30%   |
| Apr-09 | ~0.40                  | ~20%   |
| Apr-10 | ~0.50                  | ~30%   |
| Apr-11 | ~0.40                  | ~20%   |
| Apr-12 | ~0.50                  | ~30%   |
| Apr-13 | ~0.40                  | ~20%   |
| Apr-14 | ~0.50                  | ~30%   |
| Apr-15 | ~0.40                  | ~20%   |
| Apr-16 | ~0.50                  | ~30%   |
| Apr-17 | ~0.40                  | ~20%   |
| Apr-18 | ~0.50                  | ~30%   |
| Apr-19 | ~0.40                  | ~20%   |
| Apr-20 | ~0.50                  | ~30%   |
| Apr-21 | ~0.40                  | ~20%   |
| Apr-22 | ~0.50                  | ~30%   |
| Apr-23 | ~0.60                  | ~40%   |
| Apr-24 | ~0.70                  | ~50%   |
| Apr-25 | ~0.80                  | ~60%   |
| Apr-26 | ~1.20                  | ~80%   |
</details>

Source: WSTS.

Figure 2: Memory revenue YoY (May-24 onwards)  
![](images/aa9583941dd9d10035ee8c22bf6b10e84e05c456e008617fe9620b28b4223376.jpg)

<details>
<summary>line chart</summary>

| Month    | Memory Revenue YoY (%) |
| -------- | ---------------------- |
| May-24   | 121%                   |
| Jun-24   | 68%                    |
| Jul-24   | 87%                    |
| Aug-24   | 148%                   |
| Sep-24   | 60%                    |
| Oct-24   | 53%                    |
| Nov-24   | 89%                    |
| Dec-24   | 39%                    |
| Jan-25   | 30%                    |
| Feb-25   | 27%                    |
| Mar-25   | 21%                    |
| Apr-25   | 26%                    |
| May-25   | 19%                    |
| Jun-25   | 15%                    |
| Jul-25   | 30%                    |
| Aug-25   | 22%                    |
| Sep-25   | 51%                    |
| Oct-25   | 66%                    |
| Nov-25   | 68%                    |
| Dec-25   | 77%                    |
| Jan-26   | 160%                   |
| Feb-26   | 259%                   |
| Mar-26   | 269%                   |
| Apr-26   | 359%                   |
</details>

Source: WSTS.

Figure 4: Semi units (monthly) and YoY  
![](images/085513f894f65d910bb1a04d7d5fb092e3e695cc5cdbaa238938691036cafe9f.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Overall Semi units (Mn) | YoY (%) |
|--------|--------------------------|---------|
| Apr-02 | ~30000                   | ~60%    |
| Apr-03 | ~40000                   | ~40%    |
| Apr-04 | ~50000                   | ~60%    |
| Apr-05 | ~45000                   | ~40%    |
| Apr-06 | ~55000                   | ~60%    |
| Apr-07 | ~50000                   | ~40%    |
| Apr-08 | ~45000                   | ~20%    |
| Apr-09 | ~15000                   | ~-40%   |
| Apr-10 | ~110000                  | ~100%   |
| Apr-11 | ~45000                   | ~-20%   |
| Apr-12 | ~50000                   | ~-20%   |
| Apr-13 | ~55000                   | ~20%    |
| Apr-14 | ~60000                   | ~20%    |
| Apr-15 | ~65000                   | ~20%    |
| Apr-16 | ~70000                   | ~20%    |
| Apr-17 | ~75000                   | ~20%    |
| Apr-18 | ~80000                   | ~20%    |
| Apr-19 | ~85000                   | ~20%    |
| Apr-20 | ~90000                   | ~20%    |
| Apr-21 | ~95000                   | ~40%    |
| Apr-22 | ~100000                  | ~60%    |
| Apr-23 | ~95000                   | ~20%    |
| Apr-24 | ~90000                   | ~20%    |
| Apr-25 | ~95000                   | ~20%    |
| Apr-26 | ~100000                  | ~20%    |
</details>

Source: WSTS.

Figure 6: Semi ex-memory revenue (monthly) and YoY  
![](images/9d9fbe54796425b1c99bad8506cf963ed46bdc46860ab1356935b1585d66bb17.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Semi ex-Memory revenue (US$mn) | YoY (%) |
|--------|----------------------------------|---------|
| Apr-02 | ~10,000                          | ~35%    |
| Apr-03 | ~15,000                          | ~45%    |
| Apr-04 | ~20,000                          | ~40%    |
| Apr-05 | ~25,000                          | ~35%    |
| Apr-06 | ~30,000                          | ~30%    |
| Apr-07 | ~35,000                          | ~35%    |
| Apr-08 | ~40,000                          | ~30%    |
| Apr-09 | ~15,000                          | ~-20%   |
| Apr-10 | ~20,000                          | ~60%    |
| Apr-11 | ~25,000                          | ~30%    |
| Apr-12 | ~30,000                          | ~25%    |
| Apr-13 | ~35,000                          | ~30%    |
| Apr-14 | ~40,000                          | ~25%    |
| Apr-15 | ~45,000                          | ~20%    |
| Apr-16 | ~50,000                          | ~15%    |
| Apr-17 | ~55,000                          | ~10%    |
| Apr-18 | ~60,000                          | ~5%     |
| Apr-19 | ~65,000                          | ~0%     |
| Apr-20 | ~70,000                          | ~5%     |
| Apr-21 | ~75,000                          | ~15%    |
| Apr-22 | ~80,000                          | ~25%    |
| Apr-23 | ~85,000                          | ~35%    |
| Apr-24 | ~90,000                          | ~45%    |
| Apr-25 | ~95,000                          | ~55%    |
| Apr-26 | ~10,000                          | ~65%    |
</details>

Source: WSTS.

Figure 7: Semi ex-memory units and YoY  
![](images/37d143a22cb97887a0bbffdd40cb06ee1dadb3526cfba67935ff4adc0f2a7375.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Semi ex-Memory units (Mn) | YoY (%) |
|--------|---------------------------|---------|
| Apr-02 | ~30000                    | ~20%    |
| Apr-03 | ~40000                    | ~30%    |
| Apr-04 | ~50000                    | ~40%    |
| Apr-05 | ~45000                    | ~35%    |
| Apr-06 | ~55000                    | ~45%    |
| Apr-07 | ~50000                    | ~40%    |
| Apr-08 | ~45000                    | ~35%    |
| Apr-09 | ~15000                    | ~-40%   |
| Apr-10 | ~110000                   | ~90%    |
| Apr-11 | ~45000                    | ~20%    |
| Apr-12 | ~45000                    | ~25%    |
| Apr-13 | ~50000                    | ~30%    |
| Apr-14 | ~55000                    | ~35%    |
| Apr-15 | ~60000                    | ~40%    |
| Apr-16 | ~65000                    | ~45%    |
| Apr-17 | ~70000                    | ~50%    |
| Apr-18 | ~75000                    | ~55%    |
| Apr-19 | ~80000                    | ~60%    |
| Apr-20 | ~85000                    | ~65%    |
| Apr-21 | ~90000                    | ~70%    |
| Apr-22 | ~95000                    | ~75%    |
| Apr-23 | ~100000                   | ~80%    |
| Apr-24 | ~95000                    | ~75%    |
| Apr-25 | ~90000                    | ~70%    |
| Apr-26 | ~85000                    | ~65%    |
</details>

Source: WSTS.

Figure 9: Memory revenue (monthly) and YoY  
![](images/1d43e4933c40432853a40644110df9745186d4d797d51420f89449d4f3ec67ea.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Memory revenue (US$mn) | YoY (%) |
|--------|------------------------|---------|
| Apr-02 | ~1000                  | ~100%   |
| Apr-03 | ~1500                  | ~150%   |
| Apr-04 | ~2000                  | ~200%   |
| Apr-05 | ~2500                  | ~250%   |
| Apr-06 | ~3000                  | ~300%   |
| Apr-07 | ~3500                  | ~350%   |
| Apr-08 | ~4000                  | ~400%   |
| Apr-09 | ~4500                  | ~450%   |
| Apr-10 | ~5000                  | ~500%   |
| Apr-11 | ~5500                  | ~550%   |
| Apr-12 | ~6000                  | ~600%   |
| Apr-13 | ~6500                  | ~650%   |
| Apr-14 | ~7000                  | ~700%   |
| Apr-15 | ~7500                  | ~750%   |
| Apr-16 | ~8000                  | ~800%   |
| Apr-17 | ~8500                  | ~850%   |
| Apr-18 | ~9000                  | ~900%   |
| Apr-19 | ~9500                  | ~950%   |
| Apr-20 | ~10000                 | ~1000%  |
| Apr-21 | ~11000                 | ~1100%  |
| Apr-22 | ~12000                 | ~1200%  |
| Apr-23 | ~13000                 | ~1300%  |
| Apr-24 | ~14000                 | ~1400%  |
| Apr-25 | ~15000                 | ~1500%  |
| Apr-26 | ~16000                 | ~1600%  |
</details>

Source: WSTS.

Figure 11: Memory ASP and YoY  
![](images/63c6f249525d2fa556fd0fd873c50ede2abd194040ad8d3adf63c9679a8666ac.jpg)

<details>
<summary>bar-line hybrid chart</summary>

| Date   | Memory ASP (US$) | YoY (%) |
|--------|------------------|---------|
| Apr-02 | ~2.5             | ~50%    |
| Apr-03 | ~3.0             | ~40%    |
| Apr-04 | ~3.5             | ~35%    |
| Apr-05 | ~3.0             | ~30%    |
| Apr-06 | ~2.5             | ~25%    |
| Apr-07 | ~2.0             | ~20%    |
| Apr-08 | ~1.5             | ~15%    |
| Apr-09 | ~1.0             | ~10%    |
| Apr-10 | ~1.5             | ~15%    |
| Apr-11 | ~2.0             | ~20%    |
| Apr-12 | ~1.5             | ~15%    |
| Apr-13 | ~2.0             | ~20%    |
| Apr-14 | ~2.5             | ~25%    |
| Apr-15 | ~2.0             | ~20%    |
| Apr-16 | ~1.5             | ~15%    |
| Apr-17 | ~2.0             | ~20%    |
| Apr-18 | ~3.0             | ~30%    |
| Apr-19 | ~2.5             | ~25%    |
| Apr-20 | ~2.0             | ~20%    |
| Apr-21 | ~2.5             | ~25%    |
| Apr-22 | ~3.0             | ~30%    |
| Apr-23 | ~2.5             | ~25%    |
| Apr-24 | ~4.0             | ~40%    |
| Apr-25 | ~6.0             | ~60%    |
| Apr-26 | ~11.0            | ~250%   |
</details>

Source: WSTS.

Figure 8: Semi ex-memory ASP and YoY  
![](images/9bce2d9f283c1ec500de3951be914db32ff8222602dc2a5236b3f5190a9a9553.jpg)

<details>
<summary>line chart</summary>

| Date   | Semi ex-Memory ASP (US$) | YoY (%) |
|--------|--------------------------|---------|
| Apr-02 | ~0.15                    | ~-10%   |
| Apr-03 | ~0.35                    | ~10%    |
| Apr-04 | ~0.45                    | ~15%    |
| Apr-05 | ~0.50                    | ~20%    |
| Apr-06 | ~0.30                    | ~-10%   |
| Apr-07 | ~0.45                    | ~10%    |
| Apr-08 | ~0.55            

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 10 Jun 2026 01:32 PM HKT

Disseminated 10 Jun 2026 01:35 PM HKT
"""
