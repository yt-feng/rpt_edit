你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
## Global Memory Tech

# Weekly theme: Vera memory cut, strong June, Samsung dividend, Kor conf preview

Industry Overview

## Thoughts on NVIDIA Vera CPU memory capacity reduction

The street is speculating a 50% SOCAMM memory content cut for NVIDIA's new CPU, Vera, vs the original spec (new 750GB vs old 1,500GB). We believe this is not true. Our check still shows 1,500GB-centric SOCAMM (192GB x 8) as a mainstream for Vera Rubin (with HBM4) vs 750GB (96GB x 8) for Vera CPU rack (without HBM). Of course, clients (Google, Amazon, MSFT, Meta) can opt 750GB or 1,500GB for Vera Rubin superchip or Vera CPU rack. Net-net, we conclude 1) Vera Rubin should continue to use 1,500GB (750GB possible but lower performance), and 2) Vera CPU rack also should initially use 1,500GB, but it can work with 750GB too. Initial SOCAMM orders were for Vera Rubin; thus, Vera CPU rack offers incremental SOCAMM demand – positive for its TAM.

## Upbeat memory sales/exports continue QTD

Korea's semis exports hit a new record high during the first 10 days of June: US\$11bn, +30% MoM or +206% YoY. Key contributors should be 100%+ ASP increase YoY. We also observed a more notable DRAM spot price rally this week (DDR4/DDR5 up by 3-4% WoW). We think NVIDIA Jensen's Korea visit after Computex Taiwan may have further supported sentiment (e.g., NVIDIA's L-T concern on memory chip shortages). Taiwanese memory names have also reported robust May sales growth YoY (Nanya Tech +730%, Phison Electronics +301%, etc.). China also reported very strong IC imports for May (US\$57bn +68% YoY) due to high chip prices (up near-70% YoY; volume down 1%). Overall, we expect memory chip pricing to remain strong across the region.

## Samsung: dividend payments likely to be larger and earlier

Samsung Electronics (SEC) can be a dividend play, in our view. We outline a simple analysis showing why cash dividends for 2026 results could be W50-70tn, with half potentially paid 4-5 months earlier than usual: 1) annual FCF likely W200tn+/-; 2) 50% payout ratio (of FCF) well guided; 3) employee special bonus to be paid (Jan 2027) by buyback-based treasury shares; 4) Samsung Life's (032830 KS) 10.0% stake cap may require it to sell excess SEC shares following SEC's buyback; and 5) retail investor tax benefits if 2026 year-end dividends are distributed in a 50:50 or 40:60 split through 4Q26/1Q27. SEC's preferred shares could be more attractive to investors that focus on higher dividend yields.

## BofA Korea Conference to reinforce super-cycle theme

We will host the Korea Conference over 15-19 June, marking its 18th anniversary with record high participants (\~200 investors, \~120 corporates). We anticipate more bullish sentiment during the conference. Three reasons: memory expert forecasts (chip shortages for 2027 or even 2028 likely to be presented); corporate guidance (global leadership/growth in tech, robot, defense, power, beauty, consumer, etc); and more favorable fund flows (ETF, long-only money) and value-up program (dividend, buyback, US listing). The BofA Korea research team will host a large-group investor call on 23 June 9:00AM HKT to share what the analysts learned during the conference.

## 13 June 2026

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

Exhibit 1: DRAM price strongly rebounded for two consecutive weeks, while NAND remained flat  
Spot prices – DRAM and NAND

<table><tr><td>US$</td><td>Current</td><td>WoW</td><td>QoQ</td><td>YoY</td></tr><tr><td colspan="5">DRAM spot</td></tr><tr><td>16Gb DDR5</td><td>44.8</td><td>3%</td><td>14%</td><td>675%</td></tr><tr><td>16Gb DDR4</td><td>66.6</td><td>4%</td><td>-14%</td><td>985%</td></tr><tr><td>8Gb DDR4</td><td>36.3</td><td>2%</td><td>8%</td><td>961%</td></tr><tr><td>4Gb DDR4</td><td>10.1</td><td>7%</td><td>56%</td><td>475%</td></tr><tr><td colspan="5">NAND spot</td></tr><tr><td>1Tb wafer</td><td>25.1</td><td>-1%</td><td>3%</td><td>390%</td></tr><tr><td>512Gb wafer</td><td>20.6</td><td>0%</td><td>0%</td><td>661%</td></tr><tr><td>256Gb wafer</td><td>10.5</td><td>0%</td><td>3%</td><td>601%</td></tr></table>

Source: DRAMeXchange  
BofA GLOBAL RESEARCH

AI: Artificial intelligence

ASP: Average selling price

CPU: Central processing unit

DDR4/5: $4^{th}/5^{th}$ gen double-data rate DRAM

DRAM: Dynamic random-access memory

GB: Gigabyte

GPU: Graphics processing unit

HBM: High bandwidth memory

HBM4/4e/5: $6^{th}/7^{th}/8^{th}$ gen of HBM

IC: Integrated circuit

NAND: Not-AND memory

SOCAMM: Small-outline compression attached memory module

TAM: Total addressable market

## Korea exports, China imports and Taiwan monthly sales

Exhibit 2: Significant jump in Jun (US\$11.1bn; +30% MoM); around 3x higher than 2025-average  
Korea semis exports – First 10 days of month US\$bn  
![](images/eaa96252518bb7d92d1b763261801b00447e0476c0f11e0dfd3c7f5e00af53bc.jpg)

<details>
<summary>line chart</summary>

| Date    | Value (US$bn) |
|---------|---------------|
| Jun-26  | 11            |
</details>

Source: MoTIR  
BofA GLOBAL RESEARCH

Exhibit 4: China monthly integrated circuit (IC) imports and YoY  
IC imports reached a record high at US\$56.6bn in May, +68% YoY  
![](images/330fdac1b6407a9f224f618cb9330410a4cf76301ddea37af2ad66f33032b0f3.jpg)

<details>
<summary>line chart</summary>

| Date    | China IC imports (US$bn) | YoY, RH (%) |
|---------|---------------------------|-------------|
| Jan-18  | ~25                       | ~45%        |
| May-18  | ~30                       | ~30%        |
| Sep-18  | ~20                       | ~20%        |
| Jan-19  | ~15                       | ~10%        |
| May-19  | ~25                       | ~25%        |
| Sep-19  | ~30                       | ~30%        |
| Jan-20  | ~20                       | ~20%        |
| May-20  | ~30                       | ~30%        |
| Sep-20  | ~35                       | ~45%        |
| Jan-21  | ~30                       | ~30%        |
| May-21  | ~35                       | ~35%        |
| Sep-21  | ~40                       | ~40%        |
| Jan-22  | ~35                       | ~30%        |
| May-22  | ~30                       | ~20%        |
| Sep-22  | ~25                       | ~10%        |
| Jan-23  | ~30                       | ~20%        |
| May-23  | ~35                       | ~30%        |
| Sep-23  | ~30                       | ~20%        |
| Jan-24  | ~35                       | ~30%        |
| May-24  | ~40                       | ~35%        |
| Sep-24  | ~35                       | ~30%        |
| Jan-25  | ~30                       | ~20%        |
| May-25  | ~35                       | ~30%        |
| Sep-25  | ~40                       | ~35%        |
| Jan-26  | ~45                       | ~40%        |
| May-26  | ~55                       | ~50%        |
</details>

Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 6: Solid MoM growth led by memory names – ADATA +23%, Phison +13%, Nanya Tech +9%  
Taiwan tech companies' MoM monthly sales (May 2026)  
![](images/b0d0f15cd968334d54f4a4151b67a8d84d6fabcc141bb1f1c0c346636c64ea93.jpg)

<details>
<summary>bar chart</summary>

| Company      | MoM Change |
| ------------ | ---------- |
| ADATA        | 22%        |
| Mitac        | 17%        |
| PSMC         | 14%        |
| Phison       | 13%        |
| Pegatron     | 10%        |
| Nanya Tech   | 8%         |
| AUO          | 7%         |
| Yageo        | 6%         |
| Macronix     | 5%         |
| Vanguard     | 4%         |
| Powertech    | 3%         |
| Winbond      | 2%         |
| Hon Hai      | 2%         |
| Kinsus       | 1%         |
| Wistron      | 1%         |
| Novatek      | 1%         |
| Wiwynn       | 1%         |
| TSMC         | 1%         |
| MediaTek     | 1%         |
| ASE          | 1%         |
| UMC          | 1%         |
| Win Semi     | 1%         |
| Unmicron     | 0%         |
| Aspeed       | 0%         |
| Walsin       | 0%         |
| Nanya PCB    | -2%        |
| Compal       | -3%        |
| Inventec     | -4%        |
| Innolux      | -5%        |
| Gigabyte     | -6%        |
| Quanta       | -7%        |
| Holystone    | -8%        |
| Lotes        | -9%        |
| Transcend    | -15%       |
| Asustek      | -16%       |
| Acer         | -17%       |
</details>

Source: Company reports  
BofA GLOBAL RESEARCH

Exhibit 3: YoY rebound accelerated to +206% in Jun; already five consecutive months of triple-digit growth  
Korea semis exports – First 10 days of month YoY growth  
![](images/a398d23d41dc5f281f7a9bc3c018984ac14083f49cc22a196d02ae71cc4a55ee.jpg)

<details>
<summary>line chart</summary>

| Date    | YoY   |
|---------|-------|
| Jun-21  | ~30%  |
| Sep-21  | ~40%  |
| Dec-21  | ~30%  |
| Mar-22  | ~20%  |
| Jun-22  | ~10%  |
| Sep-22  | ~0%   |
| Dec-22  | ~-20% |
| Mar-23  | ~-40% |
| Jun-23  | ~-30% |
| Sep-23  | ~-10% |
| Dec-23  | ~0%   |
| Mar-24  | ~40%  |
| Jun-24  | ~80%  |
| Sep-24  | ~60%  |
| Dec-24  | ~40%  |
| Mar-25  | ~20%  |
| Jun-25  | ~30%  |
| Sep-25  | ~40%  |
| Dec-25  | ~60%  |
| Mar-26  | ~160% |
| Jun-26  | ~200% |
</details>

Source: MoTIR  
BofA GLOBAL RESEARCH

Exhibit 5: China monthly integrated circuit (IC) imports volume and YoY  
China IC imports reached 49.7bn units in May, -1% YoY  
![](images/97f0441d5c72931680e16b9540fb4a1f265271e9e11548824df39919920bccc6.jpg)

<details>
<summary>line chart</summary>

| Date    | China IC import unit | YoY, RH |
|---------|----------------------|---------|
| Jan-18  | ~30                  | ~40%    |
| May-18  | ~35                  | ~30%    |
| Sep-18  | ~30                  | ~20%    |
| Jan-19  | ~25                  | ~10%    |
| May-19  | ~35                  | ~25%    |
| Sep-19  | ~45                  | ~40%    |
| Jan-20  | ~65                  | ~60%    |
| May-20  | ~50                  | ~30%    |
| Sep-20  | ~55                  | ~40%    |
| Jan-21  | ~60                  | ~35%    |
| May-21  | ~50                  | ~20%    |
| Sep-21  | ~45                  | ~10%    |
| Jan-22  | ~40                  | ~0%     |
| May-22  | ~35                  | -10%    |
| Sep-22  | ~30                  | -20%    |
| Jan-23  | ~25                  | -30%    |
| May-23  | ~30                  | -20%    |
| Sep-23  | ~35                  | -10%    |
| Jan-24  | ~40                  | 0%      |
| May-24  | ~45                  | 10%     |
| Sep-24  | ~50                  | 20%     |
| Jan-25  | ~45                  | 10%     |
| May-25  | ~50                  | 20%     |
| Sep-25  | ~55                  | 30%     |
| Jan-26  | ~60                  | 40%     |
| May-26  | ~55                  | 30%     |
</details>

Source: China General Customs  
BofA GLOBAL RESEARCH

Exhibit 7: Positive YoY growth across all companies; notably strong rebound seen – Nanya +730%, Phison +301%, Quanta +94%, TSMC +30%  
Taiwan tech companies' YoY monthly sales (May 2026)  
![](images/8c9b65edb9551f5a5936f54128b9761b2a749ce3bdb1166362f4a8e65bd029ed.jpg)

<details>
<summary>bar chart</summary>

| Company     | YoY   |
| ----------- | ----- |
| Nanya Tech  | 200%  |
| Transcend   | 200%  |
| Phison      | 200%  |
| ADATIA      | 200%  |
| Winbond     | 180%  |
| Quanta      | 170%  |
| Aspeed      | 90%   |
| PSMC        | 60%   |
| Mitac       | 50%   |
| Yageo       | 45%   |
| Win Semi    | 40%   |
| Hon Hai     | 35%   |
| Wistron     | 35%   |
| Acer        | 35%   |
| Nanya PCB   | 35%   |
| Inventec    | 35%   |
| Kinsus      | 30%   |
| Unimicron   | 30%   |
| Powertech   | 30%   |
| TSMC        | 30%   |
| ASE         | 25%   |
| Compal      | 20%   |
| Holystone    | 20%   |
| Vanguard    | 15%   |
| Wiwynn      | 15%   |
| UMC         | 15%   |
| Walsin      | 15%   |
| Pegatron    | 10%   |
| Inmolux     | 10%   |
| Novatek     | 10%   |
| Astrek      | 10%   |
| Lotes       | 10%   |
| MediaTek    | 5%    |
| Gigabyte    | 5%    |
| AUAO        | 0%    |
</details>

\*Nanya Tech up 730% YoY, Transcend +470%, Phison +301%, ADATA +210%  
Source: Company reports  
BofA GLOBAL RESEARCH

## BofA Memory Indicator

Exhibit 8: Our memory indicator reached an all-time high of 189 in Mar/Apr-26, driven by exceptionally strong DRAM/NAND spot pricing, rising ASPs and billings, along with Korea's $150\%+$ export growth.

BofA Memory Indicator – back to upturn level since Oct-2025 and hit highest peak in Mar/Apr-26 (back-tested)

![](images/d66d487f49c2c38defa97d1e37c0f54dc31eaa45021dc42b0002ab99a4cacc63.jpg)

<details>
<summary>line chart</summary>

| Date    | Value |
|---------|-------|
| Apr-94  | 110   |
| Apr-95  | 115   |
| Apr-96  | 105   |
| Apr-97  | 95    |
| Apr-98  | 100   |
| Apr-99  | 110   |
| Apr-00  | 135   |
| Apr-01  | 75    |
| Apr-02  | 135   |
| Apr-03  | 90    |
| Apr-04  | 120   |
| Apr-05  | 105   |
| Apr-06  | 100   |
| Apr-07  | 105   |
| Apr-08  | 95    |
| Apr-09  | 85    |
| Apr-10  | 135   |
| Apr-11  | 100   |
| Apr-12  | 105   |
| Apr-13  | 115   |
| Apr-14  | 105   |
| Apr-15  | 100   |
| Apr-16  | 95    |
| Apr-17  | 120   |
| Apr-18  | 125   |
| Apr-19  | 95    |
| Apr-20  | 85    |
| Apr-21  | 105   |
| Apr-22  | 110   |
| Apr-23  | 80    |
| Apr-24  | 130   |
| Apr-25  | 105   |
| Apr-26  | 190   |
</details>

Note: Our indicator had previously been capped at \~140, but the recent unprecedented surge—driven by memory spot prices, ASPs, and billings—has led us to raise the ceiling (up to 240 levels) to reflect a more accurate relative comparison. This exceptional strength is further validated by strong earnings from memory chipmakers.  
Source: DRAMeXchange, WSTS, MoTIR Korea, BofA Global Research  
\*The shaded area represents back-tested results from January 1991 to March 2021. The unshaded area represents actual performance since April 2021. This performance is back-tested up to March-2021, and does not represent the actual performance of any account or fund. Back-tested performance depicts the theoretical (not actual) performance of a particular strategy over the time period indicated. No representation is being made that any actual portfolio is likely to have achieved returns similar to those shown herein.  
Disclaimer: The BofA Memory Indicator is intended to be an indicative metric only and may not be used for reference purposes or as a measure of performance for any financial instrument or contract, or otherwise relied upon by third parties for any other purpose, without the prior written consent of BofA Global Research. This indicator was not created to act as a benchmark. For methodology, see the 5 Aug 2024 Global Memory Tech report.  
BofA GLOBAL RESEARCH

Exhibit 9: May share price surged to record highs, supported by Samsung (strong 1Q results, optimism around HBM4 upside, and higher exposure to conventional DRAM), SK Hynix (solid 1Q performance and leadership in HBM3e/4), and Nanya Tech (record Jan–May monthly sales, up \~500–700% YoY).

BofA Memory Indicator is highly correlated with stock performance (back-tested)

![](images/e409dc4185f697a3c72a27ac2d7320a791f439a8020777c421f6fdb72043816c.jpg)

<details>
<summary>line chart</summary>

| Date   | Memory indicator | Memory companies' share price (RH) |
|--------|------------------|-----------------------------------|
| May-96 | ~80              | ~90%                              |
| May-97 | ~90              | ~100%                             |
| May-98 | ~100             | ~110%                             |
| May-99 | ~130             | ~130%                             |
| May-00 | ~140             | ~120%                             |
| May-01 | ~80              | ~70%                              |
| May-02 | ~130             | ~90%                              |
| May-03 | ~90              | ~80%                              |
| May-04 | ~120             | ~100%                             |
| May-05 | ~100             | ~90%                              |
| May-06 | ~100             | ~80%                              |
| May-07 | ~90              | ~70%                              |
| May-08 | ~80              | ~60%                              |
| May-09 | ~130             | ~110%                             |
| May-10 | ~100             | ~90%                              |
| May-11 | ~90              | ~80%                              |
| May-12 | ~100             | ~90%                              |
| May-13 | ~110             | ~100%                             |
| May-14 | ~100             | ~90%                              |
| May-15 | ~90              | ~80%                              |
| May-16 | ~120             | ~100%                             |
| May-17 | ~110             | ~110%                             |
| May-18 | ~100             | ~90%                              |
| May-19 | ~90              | ~80%                              |
| May-20 | ~100             | ~90%                              |
| May-21 | ~110             | ~100%           

[中间内容因长度限制已省略]

s areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

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
