你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

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
| Apr-06 | ~3000                  

[中间内容因长度限制已省略]

rmance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 10 Jun 2026 01:32 PM HKT

Disseminated 10 Jun 2026 01:35 PM HKT
"""
