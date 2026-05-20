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
# Basic Materials - China

# Copper/Ally prices remain firm; TC/RC drops on tight supply; iron ore holds strong

Industry Overview

# Spot copper TC/RC drops below -US\$100/t on tight supply

Supply disruptions remained a key support for copper prices this week. On one hand, recurring Middle East tensions continue to affect shipments through the Strait of Hormuz, keeping oil prices elevated and lifting smelting and logistics costs. On the other hand, Peru approved a US\$2bn state-backed loan for Petroperu on May 11 to sustain operations, highlighting ongoing strain in the local energy system and continued market concerns over potential mining supply disruptions. LME copper rose 2.8% WoW to USD 13,895/t, meanwhile, China spot copper prices also increased by 2.7% WoW to RMB 105,790/t. Meanwhile, spot TC/RC slid continued to decrease to a new record low of –USD 104/t, highlighting continued tightness in copper concentrate supply. LME aluminum rose by 5% WoW to USD 3,741/t, while the Changjiang spot price edged up by 0.6% WoW to RMB 24,370/t, with smelting margins improving to RMB 8,077/t. Gold fell by 3.7% WoW to USD 4,543/oz. Lithium carbonate narrowed by 1% WoW to RMB 192,000/t, while U $_{3}$ O $_{8}$ inced up by 0.1% WoW to USD 86.1/lb. Shanghai cobalt spot prices edged down by 0.2% WoW to RMB 425,000/t; NdPr oxide prices fell by 2.5% WoW to RMB 738,200/t, and tungsten prices decreased sharply by 27% WoW to RMB 493,000/t.

# Steel: Margins remain weak on high raw material costs

In the first half, speculation of a thermal coal supply meeting and capital outflows drove a sharp pullback in raw materials, dragging down the ferrous complex. In the second half, Trump's China visit and trade talks added volatility, though largely priced in. Five major steel products data showed mixed supply, stronger demand, and solid inventory drawdowns. Spot prices remained firm, but trades skewed to low levels; wider basis prompted arbitrage selling into spot. As of May 15, rebar and HRC prices fell by $1.3\%$ and $0.7\%$ WoW to RMB 3,416/t and RMB 3,482/t, respectively, amid a $0.1\%$ WoW drop in iron ore prices to USD 111.5/t. Finished-steel inventories decreased by $4.3\%$ WoW, while apparent steel consumption increased greatly by $8.4\%$ WoW to 9.1 mnt. Steel margins remained weak, with rebar and HRC margins at $-RMB$ 257/t and $-RMB$ 213/t, respectively.

# Cement/Glass/Paper: Weak performance

Cement: The average national cement price inched up by 0.4% WoW to RMB313/t as of May 15 $^{th}$ . The nationwide shipment ratio rose by 1.1ppts WoW to 43.9%, and the inventory ratio also increased by 1.2% to 65.4%. In mid-May, price trends diverged by region. North China and Central-South saw corrective price increases driven by higher coal and raw material costs, while Northeast, East China, and Northwest markets remained weak, with continued price declines dragging down the national average.

Glass: National average float glass price (incl. VAT) inched down by 0.05% WoW to RMB1,150.8/t amid weak demand capped upside. Our analysis shows Xinyi float glass GPM edged down by 0.4ppts to 11.7%. Paper: Paper prices edged up by 0.3% WoW to RMB3,652/t as of May 13 amid narrowing supply-demand gap. Solar glass: Our calculation shows Flat Glass GPM (2.0mm) and Xinyi Solar GPM (2.0mm) down 9.2%/21.1% WoW.

>> Employed by a non-US affiliate of BofAS and is not registered/qualified as a research analyst under the FINRA rules.
Refer to "Other Important Disclosures" for information on certain BofA entities that take responsibility for the information herein in particular jurisdictions.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

# 18 May 2026

Equity

China

Basic Materials

Matty Zhao >>

Research Analyst

BofA (Hong Kong)

+852 3508 4001

matty.zhao@bofa.com

Edward Leung, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 3282

edward.leung@bofa.com

Miriam Chan, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 7478

miriam.chan@bofa.com

Yibing Xia >>

Research Analyst

BofA (Hong Kong)

+852 3508 8045

yibing.xia@bofa.com

Yiming Wang >>

Research Analyst

BofA (Hong Kong)

+852 3508 5037

yiming.wang@bofa.com

Peter Wang >>

Research Analyst

BofA (Hong Kong)

+852 3508 7185

peter.wang2@bofa.com

See glossary at the end of the report

# Key charts

Exhibit 1: Copper and aluminum spot prices   
LME copper price +2.8% WoW to US\$13,895/t and LME aluminum price was +5.0% WoW at USD 3,741/t as of May 15   
![](images/d130993d87524cb0bae3530efdce034a66661020a46c808edf1adfb1f1b19965.jpg)

<details>
<summary>line</summary>

| Year | SHFE Copper price (RMB/t) | SHFE Aluminium price (RMB/t) |
|------|----------------------------|-------------------------------|
| 2011 | ~75,000                    | ~20,000                       |
| 2013 | ~60,000                    | ~18,000                       |
| 2015 | ~40,000                    | ~15,000                       |
| 2017 | ~50,000                    | ~18,000                       |
| 2019 | ~45,000                    | ~20,000                       |
| 2021 | ~75,000                    | ~25,000                       |
| 2023 | ~85,000                    | ~30,000                       |
| 2025 | ~110,000                   | ~35,000                       |
</details>

Source: Bloomberg, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 3: Domestic monthly treatment charges on Cu concentrate   
Domestic monthly treatment charges on copper concentrate: -US\$103.72/t as of May 15   
![](images/ba4f646fdacbfa9fa0200901945db2ce91d84691525a9f0bc20d5295b940d481.jpg)

<details>
<summary>line</summary>

| Year | Domestic monthly Cu treatment charges (US$/t) |
| ---- | --------------------------------------------- |
| 2018 | ~75                                           |
| 2019 | ~90                                           |
| 2020 | ~60                                           |
| 2021 | ~30                                           |
| 2022 | ~70                                           |
| 2023 | ~90                                           |
| 2024 | ~100                                          |
| 2025 | ~-50                                          |
| 2026 | ~-100                                         |
</details>

Source: Wind, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 5: COMEX gold spot price   
COMEX gold (spot) price decreased by 3.7% WoW to US\$4,543/oz as of May 15   
![](images/da95ce519d3d3d0939bb036dafa010d431c2f29b1bdc63afbc7466c3d20bfaee.jpg)

<details>
<summary>line</summary>

| Year | Gold Spot (US$/oz) |
| ---- | ------------------ |
| 2025 | 4,543              |
</details>

Source: Bloomberg, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 2: Copper social inventory   
As of May 15, Shanghai bonded warehouse inventory/Shanghai social inventory was -2.7% / +4.5% WoW; Guangdong bonded warehouse inventory/Guangdong social inventory was +2.6% / flattish WoW   
![](images/320a66c8ce08683ee1374b2638e5a5b04cdb51b8bb9a792af12de15da6cbeb94.jpg)

<details>
<summary>line</summary>

| Date   | Shanghai Bonded Warehouse Inventory | Social Inventory Shanghai | Guangdong Bonded Warehouse Inventory | Social Inventory Guangdong |
|--------|--------------------------------------|----------------------------|---------------------------------------|-----------------------------|
| Jan-23 | ~180,000                             | ~190,000                   | ~5,000                                | ~60,000                     |
| Jul-23 | ~100,000                             | ~150,000                   | ~5,000                                | ~40,000                     |
| Jan-24 | ~50,000                              | ~50,000                    | ~5,000                                | ~30,000                     |
| Jul-24 | ~100,000                             | ~310,000                   | ~5,000                                | ~70,000                     |
| Jan-25 | ~80,000                              | ~150,000                   | ~5,000                                | ~60,000                     |
| Jul-25 | ~120,000                             | ~180,000                   | ~5,000                                | ~80,000                     |
| Jan-26 | ~180,000                             | ~340,000                   | ~5,000                                | ~100,000                    |
</details>

Source: Bloomberg, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 4: Avg. national aluminum margin (60% captive plant)   
Avg. national aluminum margin rose by RMB 115/t WoW to RMB8,077/t as of May 15   
![](images/1af9a83c84c9db10d585d45743b3ba9db47a715902ae83fe39d368651168cb6b.jpg)

<details>
<summary>line</summary>

| Year | Avg. national aluminum margin (RMB/t) |
| ---- | ------------------------------------- |
| 2026 | 8,077                                 |
</details>

Source: Bloomberg, SMM, Wind, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 6: Spot cash margins at steel mills   
By May 15, spot rebar cash margins rose by RMB 23/t to -RMB 257/t, while spot HRC cash margins decreased by RMB 30/t to -RMB 213/t   
![](images/11fc75a8f4bca3331d373b30429e93c70bba7c2d5fe0171afc7bb1b78cd3c33b.jpg)

<details>
<summary>line</summary>

| Year | Rebar - spot mills | HRC - spot mills |
|------|---------------------|------------------|
| 2026 | -257                | -213             |
</details>

Source: Wind, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 7: Containerboard margin tracker   
Nine Dragons margin tracker is now indicating NP/t of RMB118/t for this week   
![](images/a32cae3a1eff8174d38190ae1f65c5dda4ff6b4d83d7718703afdaddf6928d12.jpg)

<details>
<summary>line</summary>

| Date    | Value |
|---------|-------|
| Feb-26  | 118   |
</details>

Source: Wind, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 9: China national cement shipment ratio   
The nationwide shipment ratio rose by 1.1ppts WoW to 43.9% as of May 15   
![](images/b3e5ab7c19fc3beb442ac7114cb015927460cc924fbe848a63088fee0c769572.jpg)

<details>
<summary>line</summary>

| Month | 2022 | 2023 | 2024 | 2025 | 2026 |
|-------|------|------|------|------|------|
| Jan   | 45   | 40   | 35   | 30   | 30   |
| Feb   | 10   | 10   | 5    | 5    | 10   |
| Mar   | 30   | 40   | 10   | 10   | 10   |
| Apr   | 60   | 65   | 30   | 30   | 30   |
| May   | 65   | 60   | 45   | 40   | 40   |
| Jun   | 65   | 60   | 50   | 45   | 45   |
| Jul   | 65   | 55   | 45   | 40   | 40   |
| Aug   | 65   | 55   | 45   | 40   | 40   |
| Sep   | 65   | 60   | 50   | 45   | 45   |
| Oct   | 70   | 60   | 50   | 45   | 45   |
| Nov   | 65   | 60   | 45   | 40   | 40   |
| Dec   | 50   | 55   | 35   | 35   | 35   |
</details>

Source: Digital cement, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 10: National Float Glass Price and Xinyi Float Glass GPM   
As of May 14 $^{th}$ , the national average float glass price inched down by 0.05% WoW to RMB1,150.8/t. Our analysis shows Xinyi float glass GPM edged down by 0.4ppts to 11.7%   
![](images/c5b4529160832f2c03fc1bc969542bb160e9a9a8bcddc3f1b820bd7bae1a0982.jpg)

<details>
<summary>line</summary>

| Year | GPM (LHS) | ASP (RHS) |
|------|-----------|-----------|
| 2019 | ~25%      | ~20%      |
| 2020 | ~50%      | ~40%      |
| 2021 | ~65%      | ~3,500    |
| 2022 | ~10%      | ~1,500    |
| 2023 | ~30%      | ~2,000    |
| 2024 | ~5%       | ~1,000    |
| 2025 | ~15%      | ~1,000    |
</details>

Source: SCI99, Wind, BofA Global Research, SCI99   
BofA GLOBAL RESEARCH

Exhibit 8: ASP at Qinhuangdao port (Kcal 5,500)   
ASP of QHD 5,500kcal spot price rose by 2.3% WoW to RMB830/t as of May 13   
![](images/a5c92e05e6a1eec9cf6bb1a5c8e396a25dbe062b10abba685d11b43991d8fb06.jpg)

<details>
<summary>line</summary>

| Year | QHD price (5,500 Kcal/kg) |
| ---- | ------------------------- |
| 2012 | ~800                      |
| 2014 | ~600                      |
| 2016 | ~400                      |
| 2018 | ~700                      |
| 2020 | ~500                      |
| 2022 | ~1,600                    |
| 2024 | ~900                      |
| 2026 | ~800                      |
</details>

Source: Sxcoal, BofA Global Research   
BofA GLOBAL RESEARCH

Exhibit 5: Lithium carbonate unit refining margin   
Current lithium carbonate refining margin based on spodumene has narrowed and still stayed negative amid decreasing spodumene price   
![](images/dc6709280b811804905ace92a0e443a3b42acc0865890c1e7ccd5b741aaecbe6.jpg)

<details>
<summary>line</summary>

| Year | Unit margin - Li2CO3 (SC) | Unit margin - Li2CO3 (Brine) |
|------|---------------------------|------------------------------|
| 2019 | ~0                        | ~0                           |
| 2020 | ~0                        | ~0                           |
| 2021 | ~50,000                   | ~100,000                     |
| 2022 | ~300,000                  | ~450,000                     |
| 2023 | ~-50,000                  | ~150,000                     |
| 2024 | ~0                        | ~50,000                      |
| 2025 | ~0                        | ~150,000                     |
</details>

Source: SMM, BofA Global Research, SCI99   
BofA GLOBAL RESEARCH

Exhibit 11: China Solar Glass Price vs GPM (%)   
Spot 3.2mm coated solar glass mid-point prices remained flat WoW as 15.25/sqm while 2.0mm coated solar glass mid-point prices down RMB 0.55/sqm to RMB8.45/sqm   
![](images/10612b4cddd0bb986d0b1ce5a3cf3817b2dcf8289f19d8da1d6d8f1c8300c5b1.jpg)

<details>
<summary>line</summary>

| Date    | Flat Glass GPM% (2.0mm) | Xinyi Solar GPM% (2.0mm) |
|---------|--------------------------|---------------------------|
| Jan-21  | ~60%                     | ~65%                      |
| Apr-21  | ~50%                     | ~45%                      |
| Jul-21  | ~15%                     | ~30%                      |
| Oct-21  | ~20%                     | ~35%                      |
| Jan-22  | ~15%                     | ~30%                      |
| Apr-22  | ~20%                     | ~35%                      |
| Jul-22  | ~25%                     | ~30%                      |
| Oct-22  | ~20%                     | ~25%                      |
| Jan-23  | ~15%                     | ~15%                      |
| Apr-23  | ~20%                     | ~25%                      |
| Jul-23  | ~25%                     | ~30%                      |
| Oct-23  | ~20%                     | ~35%                      |
| Jan-24  | ~15%                     | ~30%                      |
| Apr-24  | ~10%                     | ~25%                      |
| Jul-24  | ~5%                      | ~15%                      |
| Oct-24  | ~0%                      | ~10%                      |
| Jan-25  | ~5%                      | ~5%                       |
| Apr-25  | ~10%                     | ~15%                      |
| Jul-25  | ~5%                      | ~10%                      |
| Oct-25  | ~10%                     | ~15%                      |
| Jan-26  | ~5%                      | ~10%                      |
| Apr-26  | ~0%                      | ~5%                       |
</details>

Source: Wind, SCI99, BofA Global Research   
BofA GLOBAL RESEARCH

# Spot copper TC/RC drops below - US\$100/t on tight supply

Supply disruptions remained a key support for copper prices this week. On one hand, recurring Middle East tensions continue to affect shipments through the Strait of Hormuz, keeping oil prices elevated and lifting smelting and logistics costs. On the other hand, Peru approved a US\$2bn state-backed loan for Petroperu on May 11 to sustain operations, highlighting ongoing strain in the local energy system and continued market concerns over potential mining supply disruptions. LME copper rose 2.8% WoW to USD 13,895/t, meanwhile, China spot copper prices also increased by 2.7% WoW to RMB 105,790/t. Meanwhile, spot TC/RC slid continued to decrease to a new record low of –USD 103.72/t, highlighting continued tightness in copper concentrate supply. LME aluminum rose by 5% WoW to USD 3,741/t, while the Changjiang spot price edged up by 0.6% WoW to RMB 24,370/t, with smelting margins improving to RMB 8,077/t. Gold fell by 3.7% WoW to USD 4,543/oz. Lithium carbonate narrowed by 1% WoW to RMB 192,000/t, while U $_{3}$ O $_{8}$ inced up by 0.1% WoW to USD 86.1/lb. Shanghai cobalt spot prices edged down by 0.2% WoW to RMB 425,000/t; NdPr oxide prices fell by 2.5% WoW to RMB 738,200/t, and tungsten prices decreased sharply by 27.3% WoW to RMB 493,000/t.

Exhibit 12: Price comparison in LME & Changjiang copper

LME copper price +2.8% WoW to US\$13,895/t and Changjiang price +2.7% WoW to RMB105,790/t (US\$13,036/t ex.VAT) as of May 15

![](images/80795b87ba9ca602eeb088093fa15f2a4010fe44c484a5d8d7d0fb4d0518515f.jpg)

<details>
<summary>line</summary>

| Year | Changjiang Copper (US$/t) - ex. VAT | LME Copper spot (US$/t) |
|------|-------------------------------------|--------------------------|
| 2025 | 13,895                              | 13,036                   |
</details>

Source: Bloomberg, BofA Global Research   
BofA GLOBAL RESEARCH   
As of May 15, Shanghai bonded warehouse inventory/Shanghai social inventory was -2.7% / +4.5% WoW; Guangdong bonded warehouse inventory/Guangdong social inventory was +2.6% / flattish WoW

Exhibit 14: Copper social inventory

![](images/0d20a931650577f34e0ac2147da6b80d0ca8de890a086936a5dba11591be56a2.jpg)

<details>
<summary>line</summary>

| Date   | Shanghai Bonded Warehouse Inventory | Social Inventory Shanghai | Guangdong Bonded Warehouse Inventory | Social Inventory Guangdong |
|--------|--------------------------------------|----------------------------|---------------------------------------|-----------------------------|
| Jan-23 | ~180,000                             | ~190,000                   | ~10,000                               | ~50,000                     |
| Jul-23 | ~100,000                             | ~150,000                   | ~5,000                                | ~20,000                     |
| Jan-24 | ~50,000                              | ~70,000                    | ~2,000                                | ~10,000                     |
| Jul-24 | ~100,000                             | ~310,000                   | ~5,000     

[中间内容因长度限制已省略]

ch information is distributed simultaneously to internal and client websites and other portals by BofA and is not publicly-available material. Any unauthorized use or disclosure is prohibited. Receipt and review of this information constitutes your agreement not to redistribute, retransmit, or disclose to others the contents, opinions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
